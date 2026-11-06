"""Codex emission contracts and executable hooks in a stand-in repository.

Live harness discovery/trust acceptance is reported separately in the PR;
these tests never spend model calls or claim that a model honored instructions.
"""
from __future__ import annotations

import dataclasses
import json
import os
import shlex
import subprocess
import tomllib
import unittest

from rulestore.emit import EmitError, EmitInputs, load_tiers, targets
from rulestore.emit.codex import SCOPED_GUARD, AGENTS_MD_LIMIT, CodexTarget
from rulestore.emit.common import read_enforced
from rulestore.named_queries import sequences
from rulestore.store import FileRowSource, Row
from tests.emit_codex_fixtures import DENIES, codex_store_files
from tests.helpers import (BIN_DIR, base_env, commit, git, make_repo, make_store_repo,
                           rs_row, run_bundle, temp_dir, write)
from tests.test_emit_claude_code import install_hooks


def store_inputs(root):
    rows = list(FileRowSource(root).rows())
    return EmitInputs(rows=rows, sequences=sequences((root / "process/named-queries.md").read_text()),
                      tiers=load_tiers(), hooks={p.name: p.read_text() for p in (BIN_DIR / "hooks").iterdir()
                                                if p.is_file()}, repo="fixture/store", head="a" * 40)


class TestSkillDefinitionClosure(unittest.TestCase):
    """Contract-verified generated text for synthetic local store rows.

    These fixtures exercise process-only and transitive term dependencies,
    not native skill loading, model adherence, or any external service.
    """

    def test_process_definitions_follow_skill_without_repeating_root_or_spill(self):
        doc = Row(id="sample", kind="process", path="process/sample.md",
                  body="# Sample\n\nUse a quuxstage.\n", keys={"topic": ["sample"]})
        first = Row(id="R9001", kind="rule", body="A quuxstage uses a quuxledger.",
                    keys={"term": ["quuxstage"], "verb": ["define"]})
        second = Row(id="R9002", kind="rule", body="A quuxledger records the result.",
                     keys={"term": ["quuxledger"], "verb": ["define"]})
        unused = Row(id="R9003", kind="rule", body="Unrelated glossary prose.",
                     keys={"term": ["unusedterm"], "verb": ["define"]})
        scope = {"role": ["chief-of-staff"], "session": ["decision"]}
        for placement in ("process-only", "root", "spill"):
            rows = [doc, first, second, unused]
            if placement != "process-only":
                rows.append(Row(id="R9004", kind="rule", body="Check the quuxstage.",
                                keys={**scope, "topic": ["core" if placement == "root" else "sample"]}))
            inputs = EmitInputs(rows=rows, sequences=([['core'], ['sample']], ['sample']),
                                tiers=load_tiers(), hooks={}, repo="fixture/store", head="a" * 40)
            for harness, root, prefix in (("claude-code", "CLAUDE.md", ".claude"),
                                           ("codex", "AGENTS.md", ".agents")):
                with self.subTest(placement=placement, harness=harness):
                    files = targets()[harness].emit(inputs).files
                    skill = files[prefix + "/skills/sample/SKILL.md"]
                    for definition in (first, second):
                        self.assertEqual((files[root] + skill).count(definition.body), 1)
                        self.assertEqual(skill.count(definition.body), 0 if placement == "root" else 1)
                    self.assertNotIn(unused.body, files[root] + skill)


class TestCodexTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Reuse one read-only emitted tree across assertions. Mutation tests use
        # in-memory inputs or a separate stand-in repository.
        cls.case = unittest.TestCase()
        cls.env = base_env()
        cls.origin, cls.clone = make_store_repo(cls.case, files=codex_store_files())
        install_hooks(cls.clone, cls.env)
        cls.out = temp_dir(cls.case, "codex-emitted-")
        code, cls.stdout, cls.stderr = run_bundle("--emit", "codex", "--out", str(cls.out),
                                                cwd=cls.clone, env=cls.env)
        if code:
            raise AssertionError(cls.stderr)
        cls.inputs = store_inputs(cls.clone)

    @classmethod
    def tearDownClass(cls):
        cls.case.doCleanups()

    def read(self, name):
        return (self.out / name).read_text()

    def agent(self, role):
        return tomllib.loads(self.read(".codex/agents/%s.toml" % role))

    def test_registry_and_tree(self):
        self.assertIn("codex", targets())
        expected = {".codex/agents/%s.toml" % role for role in load_tiers()["roles"]}
        agents = {p.relative_to(self.out).as_posix() for p in (self.out / ".codex/agents").glob("*.toml")}
        self.assertEqual(agents, expected)
        emitted = {p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file()}
        self.assertEqual({os.path.relpath(p, self.out) for p in self.stdout.splitlines()}, emitted)
        self.assertNotIn(".codex/config.toml", emitted, "standalone agents are discovered directly")

    def test_standing_selection_principles_definitions_and_exclusions(self):
        text = self.read("AGENTS.md")
        self.assertLess(len(text.encode()), AGENTS_MD_LIMIT)
        self.assertIn("Propose; do not decide.", text)
        self.assertIn("State the obligation at its shortest", text)
        self.assertIn("Deny principle R0164.", text)
        self.assertIn("Append to `decisions/log.md`", text)
        self.assertIn("**tranche**", text)
        for excluded in ("```", "Read(./.env)", "field: model", "# Process:",
                         "DEC-000001", "Run the red gate", "A test asserts", "retired row"):
            self.assertNotIn(excluded, text)

    def test_entire_tree_is_byte_identical_across_runs(self):
        out = temp_dir(self, "codex-again-")
        code, _, err = run_bundle("--emit", "codex", "--out", str(out), cwd=self.clone, env=self.env)
        self.assertEqual(code, 0, err)
        first = {p.relative_to(self.out): p.read_bytes() for p in self.out.rglob("*") if p.is_file()}
        second = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
        self.assertEqual(first, second)
        self.assertEqual(CodexTarget().emit(self.inputs), CodexTarget().emit(
            dataclasses.replace(self.inputs, generated="different timestamp")))

    def test_every_script_is_copied_byte_for_byte_and_executable(self):
        for name, script in self.inputs.hooks.items():
            path = self.out / ".codex/hooks" / name
            self.assertEqual(path.read_bytes(), script.encode())
            self.assertTrue(os.access(path, os.X_OK), name)

    def test_agent_fields_model_and_judgment(self):
        tiers = load_tiers()
        self.assertEqual(tiers["harnesses"]["codex"], {
            "frontier": "gpt-6-astra", "solid": "gpt-6.1-sol", "cheap": "gpt-6-luna"})
        for role, tier in tiers["roles"].items():
            agent = self.agent(role)
            self.assertEqual(agent["name"], role)
            self.assertEqual(agent["model"], tiers["harnesses"]["codex"][tier])
            self.assertNotIn("Propose; do not decide.", agent["developer_instructions"])
            self.assertNotIn("**tranche**", agent["developer_instructions"])
        coder = self.agent("coder-agent")
        self.assertIn("Implement changes", coder["description"])
        self.assertIn("Run the red gate", coder["developer_instructions"])
        self.assertNotIn("Implement changes", coder["developer_instructions"])
        self.assertIn("In force until a published code-review standard", self.agent("reviewer-agent")["description"])
        self.assertIn("ship/no-ship", self.agent("release-manager-agent")["description"])
        self.assertIn("Define how correctness", self.agent("test-designer-agent")["description"])

    def test_agent_lanes_use_role_scoped_repository_hooks(self):
        for role, row_id, lane in (("architect-agent", "R0091", "specs"),
                                   ("test-designer-agent", "R1156", "tests")):
            body = self.agent(role)["developer_instructions"]
            self.assertIn("Scoped lane guard (%s): .codex/hooks/lane-guard --lane %s" % (row_id, lane), body)
            self.assertEqual(body.splitlines()[0], SCOPED_GUARD)
            self.assertIn("a finding, not an edit", body)
        self.assertIn("lane-guard", self.read(".codex/hooks.json"))
        self.assertNotIn("hooks", self.agent("architect-agent"))

    def test_path_rules_remain_conditional_in_matching_roles(self):
        body = self.agent("coder-agent")["developer_instructions"]
        self.assertIn("## Rules for paths matching tests/**, SPEC.md", body)
        self.assertIn("A test asserts one behaviour", body)
        self.assertNotIn("A test asserts", self.agent("reviewer-agent")["developer_instructions"])

    def test_skills_and_missing_procedures(self):
        gate = self.read(".agents/skills/gate/SKILL.md")
        self.assertIn('name: "gate"', gate)
        self.assertIn("disable-model-invocation: true", gate)
        self.assertIn("Request the human's go/no-go", gate)
        self.assertIn("1. Open the issue.", gate)
        self.assertNotIn("disable-model-invocation", self.read(".agents/skills/release/SKILL.md"))
        self.assertFalse((self.out / ".agents/skills/named-queries").exists())
        self.assertFalse((self.out / ".agents/skills/project-setup").exists())
        self.assertIn("$release (.agents/skills/release/SKILL.md)", self.agent("reviewer-agent")["developer_instructions"])
        self.assertIn("R0486 names skill 'build'", self.stderr)
        self.assertIn("R0506 names skill 'review'", self.stderr)

    def test_repo_hook_blocks_and_three_deny_blocks(self):
        hooks = json.loads(self.read(".codex/hooks.json"))["hooks"]
        commands = [h["command"] for entries in hooks.values() for entry in entries for h in entry["hooks"]]
        for script in ("decision-log-append-only", "review-artifact-immutable", "intake-branch-guard",
                       "store-lint --check generated-filename", "store-lint --check verdict-lines",
                       "store-lint --check citations", "push-readback"):
            self.assertTrue(any(script in command for command in commands), script)
        deny = [h["command"] for entry in hooks["PreToolUse"] for h in entry["hooks"] if " deny " in h["command"]]
        self.assertEqual(len(deny), 3)
        for patterns in DENIES.values():
            self.assertIn(patterns, [json.loads(shlex.split(command)[-1]) for command in deny])
        for command in commands:
            self.assertIn('"$(git rev-parse --show-toplevel)/.codex/hooks/codex-hook"', command)

    def test_fixture_has_all_real_enforced_blocks_and_every_emitted_object(self):
        real = read_enforced(store_inputs(BIN_DIR.parent).rows)
        fixture = read_enforced(self.inputs.rows)
        self.assertTrue(set(fixture).issubset(real))
        self.assertEqual(len(fixture), 34)
        for row_id, item in fixture.items():
            # Package 4 deliberately renames R0506's missing review procedure.
            # Hook/deny/agent blocks remain independently snapshotted verbatim;
            # every live row, including added procedure rows, is checked below.
            if row_id != "R0506":
                self.assertEqual(item.fields, real[row_id].fields, row_id)
            else:
                self.assertIn(real[row_id].skills, (["release", "review"], ["release", "review-artifact"]))
            if item.kind == "hook":
                obj = self.read(".codex/hooks.json") if not item.agent_scoped else "".join(
                    self.agent(role)["developer_instructions"] for role in item.roles if role in load_tiers()["roles"])
                self.assertIn(item.hook_name, obj, row_id)
            elif item.kind == "deny":
                for pattern in item.deny:
                    self.assertIn(pattern, self.read(".codex/hooks.json"), row_id)
            elif item.kind == "agent":
                for role in item.roles:
                    if role not in load_tiers()["roles"]:
                        continue  # R0259 chooses the harness tier column, never creates a role.
                    self.assertIn(fixture[row_id].prose, self.agent(role)["description"], row_id)
                self.assertTrue(all(self.agent(role)["model"] for role in load_tiers()["roles"]))
            else:
                for skill in item.skills:
                    self.assertTrue((self.out / ".agents/skills" / skill / "SKILL.md").is_file()
                                    or "%s names skill %r" % (row_id, skill) in self.stderr, row_id)

    def test_spill_and_real_store(self):
        inputs = store_inputs(BIN_DIR.parent)
        result = CodexTarget().emit(inputs)
        self.assertLessEqual(len(result.files["AGENTS.md"].encode()), AGENTS_MD_LIMIT)
        retro = result.files[".agents/skills/retro/SKILL.md"]
        self.assertIn("\n## Rules\n", retro)
        live = read_enforced(inputs.rows)
        emitted_hooks = result.files[".codex/hooks.json"]
        for row_id, item in live.items():
            if item.kind == "hook":
                self.assertIn(item.hook_invocation, emitted_hooks, row_id)
                if item.agent_scoped:
                    for role in item.roles:
                        self.assertIn(role, emitted_hooks, row_id)
                        body = tomllib.loads(result.files[".codex/agents/%s.toml" % role])["developer_instructions"]
                        self.assertIn(item.hook_invocation, body, row_id)
            elif item.kind == "deny":
                for pattern in item.deny:
                    self.assertIn(pattern, emitted_hooks, row_id)
            elif item.kind == "agent":
                for role in item.roles:
                    if role in inputs.tiers["roles"]:
                        agent = tomllib.loads(result.files[".codex/agents/%s.toml" % role])
                        if item.field == "description":
                            self.assertIn(item.prose, agent["description"], row_id)
                        self.assertEqual(agent["model"], inputs.tiers["harnesses"]["codex"][inputs.tiers["roles"][role]])
            else:
                for skill in item.skills:
                    self.assertTrue(".agents/skills/%s/SKILL.md" % skill in result.files
                                    or any("%s names skill %r" % (row_id, skill) in note for note in result.notes), row_id)
        # Every process document except the two non-skills has an output.
        from rulestore.emit.common import skill_documents
        for stem, _ in skill_documents([row for row in inputs.rows if row.kind == "process"]):
            self.assertIn(".agents/skills/%s/SKILL.md" % stem, result.files)

    def test_spill_uses_the_same_topic_stem_and_avoids_duplicate_definitions(self):
        doc = Row(id="decision-log", kind="process", path="process/decision-log.md",
                  body="# Decision log\n\nWrite entries.\n", keys={"topic": ["decision-log"]})
        inputs = dataclasses.replace(self.inputs, rows=self.inputs.rows + [doc],
                                     sequences=(self.inputs.sequences[0], self.inputs.sequences[1] + ["decision-log"]))
        result = CodexTarget().emit(inputs)
        self.assertNotIn("Append to `decisions/log.md`", result.files["AGENTS.md"])
        self.assertIn("\n## Rules\n\nAppend to `decisions/log.md`", result.files[".agents/skills/decision-log/SKILL.md"])

    def test_refusals_are_atomic_and_report_utf8_bytes(self):
        row = Row(id="R9999", body="é" * 17000, kind="rule", order=1,
                  keys={"role": ["chief-of-staff"], "session": ["decision"], "topic": ["core"]})
        inputs = dataclasses.replace(self.inputs, rows=self.inputs.rows + [row])
        with self.assertRaisesRegex(EmitError, r"AGENTS.md is \d+ bytes, over the 32768-byte limit"):
            CodexTarget().emit(inputs)
        for broken in (dataclasses.replace(self.inputs, hooks={}),
                       dataclasses.replace(self.inputs, tiers={}),
                       dataclasses.replace(self.inputs, rows=self.inputs.rows + [dataclasses.replace(
                           row, body="No hook block", keys={"enforce": ["hook"]})])):
            with self.assertRaises(EmitError):
                CodexTarget().emit(broken)
        out = temp_dir(self, "codex-query-refused-")
        code, _, err = run_bundle("--emit", "codex", "--out", str(out), "--where", "role=writer",
                                  cwd=self.clone, env=self.env)
        self.assertEqual(code, 2, err)
        self.assertEqual(list(out.iterdir()), [])

    def test_cli_over_byte_limit_refuses_without_writing_any_file(self):
        files = codex_store_files()
        files["rules/R9999.md"] = rs_row(
            "R9999", "é" * 17000, order=1, topic=["core"], role=["chief-of-staff"],
            session=["decision"], corpus=["software"], verb="require", term=None)
        _, clone = make_store_repo(self, files=files)
        install_hooks(clone, self.env)
        out = temp_dir(self, "codex-byte-refused-")
        code, stdout, stderr = run_bundle("--emit", "codex", "--out", str(out), cwd=clone, env=self.env)
        self.assertEqual(code, 2, stderr)
        self.assertEqual(stdout, "")
        self.assertRegex(stderr.strip(), r"^refused: AGENTS.md is \d+ bytes, over the 32768-byte limit$")
        self.assertEqual(list(out.iterdir()), [])

    def test_exact_byte_limit_accepts_32768_and_refuses_32769(self):
        row = Row(id="R9999", body="x", order=1, keys={"role": ["chief-of-staff"],
                  "session": ["decision"], "topic": ["core"]})
        inputs = dataclasses.replace(self.inputs, rows=[row])
        overhead = len(CodexTarget().emit(inputs).files["AGENTS.md"].encode()) - 1
        exact = dataclasses.replace(inputs, rows=[dataclasses.replace(row, body="x" * (AGENTS_MD_LIMIT - overhead))])
        self.assertEqual(len(CodexTarget().emit(exact).files["AGENTS.md"].encode()), AGENTS_MD_LIMIT)
        with self.assertRaisesRegex(EmitError, "32769 bytes"):
            CodexTarget().emit(dataclasses.replace(exact, rows=[dataclasses.replace(exact.rows[0], body=exact.rows[0].body + "x")]))


class TestCodexHookExecution(unittest.TestCase):
    def setUp(self):
        self.env = base_env()
        self.repo = make_repo(self, name="stand-in")
        for name, content in (("README.md", "safe\n"), ("decisions/log.md", "First.\nSecond.\n"),
                              ("reviews/landed-20260101T000000Z.md", "Verdict: ready\n")):
            write(self.repo, name, content)
        commit(self.repo, "seed", env=self.env)
        inputs = store_inputs(BIN_DIR.parent)
        result = CodexTarget().emit(inputs)
        for name, content in result.files.items():
            write(self.repo, name, content)
        self.hooks = json.loads(result.files[".codex/hooks.json"])["hooks"]

    def run_command(self, command, *, tool="apply_patch", args=None, event="PreToolUse", cwd=None, agent_type=None):
        data = {"hook_event_name": event, "tool_name": tool,
                "tool_input": args or {}, "cwd": str(cwd or self.repo)}
        if agent_type is not None:
            data["agent_type"] = agent_type
        proc = subprocess.run(command, shell=True, input=json.dumps(data), cwd=cwd or self.repo,
                              text=True, capture_output=True, env=self.env, timeout=20)
        self.assertNotIn("Traceback", proc.stderr)
        return proc

    def script(self, needle):
        return next(h["command"] for entries in self.hooks.values() for entry in entries
                    for h in entry["hooks"] if " script " in h["command"] and needle in h["command"])

    def patch(self, script, patch, event="PreToolUse", cwd=None, agent_type=None):
        return self.run_command(self.script(script), args={"command": "*** Begin Patch\n" + patch + "*** End Patch"},
                                event=event, cwd=cwd, agent_type=agent_type)

    def test_all_real_deny_patterns_block_and_harmless_calls_pass(self):
        for entry in self.hooks["PreToolUse"]:
            for hook in entry["hooks"]:
                if " deny " not in hook["command"]:
                    continue
                patterns = json.loads(shlex.split(hook["command"])[-1])
                for pattern in patterns:
                    kind, glob = pattern.split("(", 1)
                    sample = glob[:-1].replace("**", "nested").replace("*", "sample")
                    args = {"file_path": sample} if kind == "Read" else {"command": sample}
                    with self.subTest(pattern=pattern):
                        proc = self.run_command(hook["command"], tool=kind, args=args)
                        self.assertEqual(proc.returncode, 2, proc.stderr)
                        self.assertIn("denied by ", proc.stderr)
                for tool, args in (("Read", {"file_path": "README.md"}),
                                   ("Bash", {"command": "git push origin main"}),
                                   ("Bash", {"command": "terraform plan"})):
                    proc = self.run_command(hook["command"], tool=tool, args=args)
                    self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_recursive_secret_path_globs_include_root_and_nested_directories(self):
        command = next(h["command"] for entry in self.hooks["PreToolUse"] for h in entry["hooks"]
                       if " deny " in h["command"] and "Read(" in h["command"])
        for name in ("secrets/key", "nested/secrets/key", ".env", "nested/.env.local"):
            proc = self.run_command(command, tool="Read", args={"file_path": str(self.repo / name)})
            self.assertEqual(proc.returncode, 2, (name, proc.stderr))
        for name in ("public/secrets-guide.md", ".environment", "README.md"):
            proc = self.run_command(command, tool="Read", args={"file_path": str(self.repo / name)})
            self.assertEqual(proc.returncode, 0, (name, proc.stderr))

    def test_intake_guard_inspects_each_patch_file_and_subdirectory(self):
        patch = "*** Add File: safe.txt\n+safe\n*** Add File: rules/R9999.md\n+rule\n"
        self.assertEqual(self.patch("intake-branch-guard", patch).returncode, 2)
        git(self.repo, "checkout", "-q", "-b", "intake/example", env=self.env, check=True)
        self.assertEqual(self.patch("intake-branch-guard", patch).returncode, 0)
        nested = self.repo / "nested"
        nested.mkdir()
        git(self.repo, "checkout", "-q", "main", env=self.env, check=True)
        self.assertEqual(self.patch("intake-branch-guard", "*** Add File: ../process/new.md\n+doc\n", cwd=nested).returncode, 2)
        self.assertEqual(self.patch("intake-branch-guard", "*** Add File: src/safe.py\n+x = 1\n").returncode, 0)

    def test_decision_log_appends_pass_rewrites_and_deletes_block(self):
        append = "*** Update File: decisions/log.md\n@@\n First.\n Second.\n+Third.\n"
        self.assertEqual(self.patch("decision-log-append-only", append).returncode, 0)
        rewrite = "*** Update File: decisions/log.md\n@@\n-First.\n+Changed.\n Second.\n"
        self.assertEqual(self.patch("decision-log-append-only", rewrite).returncode, 2)
        self.assertEqual(self.patch("decision-log-append-only", "*** Delete File: decisions/log.md\n").returncode, 2)
        self.assertEqual(self.patch("decision-log-append-only", "*** Update File: decisions/log.md\n*** Move to: elsewhere.md\n@@\n First.\n Second.\n+Third.\n").returncode, 2)
        self.assertEqual(self.patch("decision-log-append-only", "*** Add File: safe.txt\n+safe\n").returncode, 0)

    def test_landed_review_edits_and_move_destinations_block_new_reviews_pass(self):
        self.assertEqual(self.patch("review-artifact-immutable", "*** Update File: reviews/landed-20260101T000000Z.md\n@@\n-Verdict: ready\n+changed\n").returncode, 2)
        self.assertEqual(self.patch("review-artifact-immutable", "*** Update File: README.md\n*** Move to: reviews/landed-20260101T000000Z.md\n@@\n-safe\n+changed\n").returncode, 2)
        self.assertEqual(self.patch("review-artifact-immutable", "*** Add File: reviews/new-20260102T000000Z.md\n+draft\n").returncode, 0)

    def test_post_lints_use_paths_after_patch_has_already_run(self):
        cases = [("generated-filename", "reviews/new.md", "Verdict: ready\n", "timestamp"),
                 ("verdict-lines", "reviews/new-20260102T000000Z.md", "# Missing verdict\n", "Verdict"),
                 ("citations", "rules/R9999.md", rs_row("R9999", "As [R9998] says.", topic=["core"]), "not in the store")]
        for check, path, bad, reason in cases:
            write(self.repo, path, bad)
            proc = self.patch("store-lint --check " + check, "*** Add File: %s\n+placeholder\n" % path, event="PostToolUse")
            self.assertEqual(proc.returncode, 2, proc.stderr)
            self.assertIn(reason, proc.stderr)
            write(self.repo, path, "Verdict: ready\n\nVerdict (quality): ready\n")
        path = "reviews/good-20260102T000000Z.md"
        write(self.repo, path, "Verdict: ready\n\nVerdict (quality): ready\n")
        for check in ("generated-filename", "verdict-lines", "citations"):
            self.assertEqual(self.patch("store-lint --check " + check, "*** Update File: %s\n@@\n-old\n+new\n" % path,
                                        event="PostToolUse").returncode, 0)

    def test_bash_push_readback_evidence_becomes_model_visible_json(self):
        origin = temp_dir(self, "codex-push-") / "origin.git"
        git(self.repo, "init", "--bare", "-q", "-b", "main", str(origin), env=self.env, check=True)
        git(self.repo, "remote", "add", "origin", str(origin), env=self.env, check=True)
        git(self.repo, "push", "-q", "origin", "main", env=self.env, check=True)
        proc = self.run_command(self.script("push-readback"), tool="Bash", args={"command": "git push origin main"}, event="PostToolUse")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        context = json.loads(proc.stdout)["hookSpecificOutput"]
        self.assertEqual(context["hookEventName"], "PostToolUse")
        self.assertIn("origin/main is at " + git(self.repo, "rev-parse", "HEAD", env=self.env, check=True)[1].strip(), context["additionalContext"])
        write(self.repo, "README.md", "changed\n")
        commit(self.repo, "unpublished", env=self.env)
        proc = self.run_command(self.script("push-readback"), tool="Bash", args={"command": "git push origin main"}, event="PostToolUse")
        self.assertEqual(proc.returncode, 2, proc.stderr)
        self.assertIn("reads back", proc.stderr)
        self.assertEqual(self.run_command(self.script("push-readback"), tool="Bash", args={"command": "git status"}, event="PostToolUse").returncode, 0)

    def test_lane_scope_matches_only_the_runtime_agent_type(self):
        patch = "*** Add File: src/outside.py\n+x = 1\n"
        for role, lane in (("architect-agent", "specs"), ("test-designer-agent", "tests")):
            command = self.script("lane-guard --lane " + lane)
            args = {"command": "*** Begin Patch\n" + patch + "*** End Patch"}
            for agent_type, expected in ((role, 2), ("coder-agent", 0), (None, 0)):
                proc = self.run_command(command, args=args, agent_type=agent_type)
                self.assertEqual(proc.returncode, expected, proc.stderr)
            inside = "SPEC.md" if lane == "specs" else "tests/test_good.py"
            args = {"command": "*** Begin Patch\n*** Add File: %s\n+safe\n*** End Patch" % inside}
            self.assertEqual(self.run_command(command, args=args, agent_type=role).returncode, 0)

    def test_future_agent_scoped_row_uses_its_roles_without_hardcoding(self):
        row = Row(id="R9999", kind="rule", order=1, keys={"enforce": ["hook"],
                  "role": ["reviewer-agent", "skeptic-risk-agent"]},
                  body="Reviews only.\n\n```yaml\nscope: agent\nevent: PreToolUse\nmatcher: Edit|Write\ncommand: bin/hooks/lane-guard --lane reviews\n```")
        inputs = store_inputs(BIN_DIR.parent)
        result = CodexTarget().emit(dataclasses.replace(inputs, rows=inputs.rows + [row]))
        hooks = json.loads(result.files[".codex/hooks.json"])["hooks"]
        command = next(h["command"] for entry in hooks["PreToolUse"] for h in entry["hooks"]
                       if "lane-guard --lane reviews" in h["command"])
        args = {"command": "*** Begin Patch\n*** Add File: src/outside.py\n+bad\n*** End Patch"}
        for role, expected in (("reviewer-agent", 2), ("skeptic-risk-agent", 2),
                               ("coder-agent", 0), (None, 0)):
            self.assertEqual(self.run_command(command, args=args, agent_type=role).returncode, expected)
        for role in ("reviewer-agent", "skeptic-risk-agent"):
            instructions = tomllib.loads(result.files[".codex/agents/%s.toml" % role])["developer_instructions"]
            self.assertEqual(instructions.splitlines()[0], SCOPED_GUARD)
            self.assertIn("--lane reviews", instructions)

    def test_malformed_patch_and_hook_inputs_fail_closed(self):
        proc = self.run_command(self.script("intake-branch-guard"), args={"command": "not a patch"})
        self.assertEqual(proc.returncode, 2)
        self.assertIn("envelope", proc.stderr)
        proc = subprocess.run(self.script("intake-branch-guard"), shell=True, input="invalid json", cwd=self.repo,
                              text=True, capture_output=True, env=self.env)
        self.assertEqual(proc.returncode, 2)
        self.assertNotIn("Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
