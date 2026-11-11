"""`bin/bundle --emit claude-code` (the plan, §3a; SPEC.md §7): a fixture for
every `enforce:` row's emitted object, the `paths:` row, the stub process
documents, the CLAUDE.md line count, and the two consistency checks.

Runs the real command against a stand-in store repository
(`tests.emit_fixtures.emit_store_files`, plus `bin/hooks/` copied in, since
the emitter copies the scripts from the store repo it runs in).
"""

from __future__ import annotations

import json
import os
import re
import shutil
import unittest

from rulestore.emit import EmitError, EmitInputs, load_tiers, targets
from rulestore.store import Row
from tests.emit_fixtures import (
    AGENT_IDS,
    DENY_IDS,
    HOOK_IDS,
    SKILL_IDS,
    emit_store_files,
)
from tests.helpers import (
    BIN_DIR,
    base_env,
    commit,
    make_store_repo,
    no_traceback,
    rs_process,
    rs_row,
    run_bundle,
    temp_dir,
    write,
)

HOOKS_SRC = BIN_DIR / "hooks"
HOOKS_PREFIX = '"$CLAUDE_PROJECT_DIR"/.claude/hooks/'
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def install_hooks(clone, env):
    for path in sorted(HOOKS_SRC.iterdir()):
        if not path.is_file():
            continue
        dest = clone / "bin" / "hooks" / path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
    commit(clone, "bin: the hook scripts", env=env)


def frontmatter_of(text):
    match = FRONTMATTER_RE.match(text)
    assert match, text[:200]
    return match.group(1), text[match.end():]


def field(front, key):
    """A frontmatter scalar's value, a JSON-quoted one read back."""
    for line in front.splitlines():
        if line.startswith(key + ":"):
            value = line[len(key) + 1:].strip()
            return json.loads(value) if value.startswith('"') else value
    return None


class ClaudeCodeTestCase(unittest.TestCase):
    files = None

    def setUp(self):
        self.env = base_env()
        files = emit_store_files() if self.files is None else self.files
        self.origin, self.clone = make_store_repo(self, files=files)
        install_hooks(self.clone, self.env)
        self.out = temp_dir(self, "emit-claude-code-")

    def emit(self, *extra):
        return run_bundle("--emit", "claude-code", "--out", str(self.out), *extra,
                          cwd=self.clone, env=self.env)

    def emitted(self):
        found = []
        for root, _dirs, names in os.walk(self.out):
            for name in names:
                found.append(os.path.relpath(os.path.join(root, name), self.out))
        return sorted(found)

    def read(self, relpath):
        return (self.out / relpath).read_text(encoding="utf-8")


class TestEmittedTree(ClaudeCodeTestCase):
    def setUp(self):
        super().setUp()
        self.code, self.stdout, self.stderr = self.emit()
        self.assertEqual(self.code, 0, self.stderr)

    def test_the_tree_holds_every_shape_and_prints_each_path(self):
        files = self.emitted()
        self.assertIn("CLAUDE.md", files)
        self.assertIn(".claude/settings.json", files)
        self.assertIn(".claude/rules/verification.md", files)
        self.assertIn(".claude/skills/gate/SKILL.md", files)
        self.assertIn(".claude/skills/release/SKILL.md", files)
        self.assertNotIn(".claude/skills/project-setup/SKILL.md", files)
        self.assertNotIn(".claude/skills/named-queries/SKILL.md", files)
        for name in ("store-lint", "intake-branch-guard", "push-readback",
                     "decision-log-append-only", "review-artifact-immutable", "lane-guard"):
            self.assertIn(".claude/hooks/%s" % name, files)
            self.assertTrue(os.access(self.out / ".claude/hooks" / name, os.X_OK), name)
        printed = sorted(os.path.relpath(p, self.out) for p in self.stdout.strip().splitlines())
        self.assertEqual(printed, files)

    def test_claude_md_is_the_standing_context_under_200_lines(self):
        text = self.read("CLAUDE.md")
        lines = text.splitlines()
        self.assertLess(len(lines), 200)
        self.assertRegex(lines[0], r"^<!-- fiducial \S+ @ [0-9a-f]{40} -->$")
        self.assertNotRegex(lines[0], r"\d{8}T\d{6}Z", "a harness tree carries no timestamp")
        # judgment rows of role=chief-of-staff session=decision, in order
        self.assertIn("Propose; do not decide.", text)
        self.assertIn("State the obligation at its shortest", text)
        self.assertLess(text.index("Propose; do not decide."),
                        text.index("State the obligation at its shortest"))
        # the deny and hook principles, never their blocks
        self.assertIn("Never let a secret value enter context.", text)
        self.assertIn("Push plainly; never force-push.", text)
        self.assertIn("Append to `decisions/log.md`", text)
        self.assertNotIn("```", text)
        self.assertNotIn("Read(./.env)", text)
        self.assertNotIn("bin/hooks/", text)
        # block-only hook rows, agent-field rows and skill rows are elsewhere
        self.assertNotIn("intake/*", text)
        self.assertNotIn("Choose the model tier", text)
        self.assertNotIn("Open one `human-gate` tracker issue", text)
        # no Human note, no process document, no retired row, no paths: row
        self.assertNotIn("DEC-000001", text)
        self.assertNotIn("# Process: Gate", text)
        self.assertNotIn("never emitted", text)
        self.assertNotIn("A test asserts one behaviour", text)
        # definitions pulled by term, last
        self.assertIn("**tranche** — A tranche is one concurrent workstream", text)
        self.assertEqual([l for l in lines if l.startswith("## ")], ["## Definitions"])

    def test_claude_md_is_byte_stable_across_runs(self):
        first = self.read("CLAUDE.md")
        out2 = temp_dir(self, "emit-again-")
        code, _, err = run_bundle("--emit", "claude-code", "--out", str(out2),
                                  cwd=self.clone, env=self.env)
        self.assertEqual(code, 0, err)
        self.assertEqual((out2 / "CLAUDE.md").read_text(), first)
        self.assertEqual((out2 / ".claude/settings.json").read_text(),
                         self.read(".claude/settings.json"))

    def test_settings_deny_carries_every_deny_block_pattern_once(self):
        settings = json.loads(self.read(".claude/settings.json"))
        deny = settings["permissions"]["deny"]
        for pattern in ("Read(./.env)", "Read(./**/.env)", "Read(~/.ssh/**)", "Bash(printenv*)",
                        "Bash(kubectl apply*)", "Bash(terraform apply*)", "Bash(ssh *prod*)",
                        "Bash(git push --force*)", "Bash(git push -f*)", "Bash(git push * +*)"):
            self.assertIn(pattern, deny)
        self.assertEqual(len(deny), len(set(deny)))
        self.assertEqual(len(deny), 10)
        # R0164 and R0203 (core) precede R0564 (commit-control): row order
        self.assertLess(deny.index("Read(./.env)"), deny.index("Bash(git push -f*)"))

    def test_settings_hooks_carry_the_repo_level_hook_rows_and_not_the_agent_scoped(self):
        hooks = json.loads(self.read(".claude/settings.json"))["hooks"]
        pre = {e["matcher"]: [h["command"] for h in e["hooks"]] for e in hooks["PreToolUse"]}
        post = {e["matcher"]: [h["command"] for h in e["hooks"]] for e in hooks["PostToolUse"]}
        d = HOOKS_PREFIX
        self.assertEqual(sorted(pre["Edit|Write"]), [
            d + "decision-log-append-only",
            d + "intake-branch-guard",
            d + "review-artifact-immutable",
        ])
        self.assertEqual(sorted(post["Edit|Write"]), [
            d + "store-lint --check citations",
            d + "store-lint --check generated-filename",
            d + "store-lint --check verdict-lines",
        ])
        self.assertEqual(post["Bash"], [d + "push-readback"])
        flat = json.dumps(hooks)
        self.assertNotIn("lane-guard", flat)
        self.assertNotIn("bin/hooks/", flat)
        for entry in hooks["PreToolUse"] + hooks["PostToolUse"]:
            for hook in entry["hooks"]:
                self.assertEqual(hook["type"], "command")
                # F-1: from the project root the harness names, not the cwd
                self.assertTrue(hook["command"].startswith(HOOKS_PREFIX), hook["command"])
                script = hook["command"].split()[0][len('"$CLAUDE_PROJECT_DIR"/'):]
                self.assertTrue((self.out / script).is_file(), script)

    def test_every_agent_scoped_hook_row_lands_in_its_roles_agent_file(self):
        architect, _ = frontmatter_of(self.read(".claude/agents/architect-agent.md"))
        designer, _ = frontmatter_of(self.read(".claude/agents/test-designer-agent.md"))
        self.assertIn("command: " + json.dumps(HOOKS_PREFIX + "lane-guard --lane specs"), architect)
        self.assertIn("command: " + json.dumps(HOOKS_PREFIX + "lane-guard --lane tests"), designer)
        self.assertIn("hooks:\n  PreToolUse:\n    - matcher: \"Edit|Write\"", designer)
        self.assertIn("type: command", designer)
        coder, _ = frontmatter_of(self.read(".claude/agents/coder-agent.md"))
        self.assertNotIn("hooks:", coder)

    def test_agents_are_emitted_for_the_tiered_roles_only(self):
        agents = sorted(f for f in self.emitted() if f.startswith(".claude/agents/"))
        self.assertEqual(agents, [".claude/agents/%s.md" % role for role in (
            "architect-agent", "coder-agent", "context-quality-reviewer",
            "release-manager-agent", "reviewer-agent", "skeptic-risk-agent",
            "spec-reviewer-agent", "test-designer-agent")])

    def test_agent_description_and_model_come_from_the_agent_rows_and_the_tier_map(self):
        front, body = frontmatter_of(self.read(".claude/agents/coder-agent.md"))
        self.assertEqual(field(front, "name"), "coder-agent")
        self.assertEqual(field(front, "description"),
                         "Implement changes according to the spec and the test plan.")
        self.assertEqual(field(front, "model"), "sonnet")
        self.assertNotIn("Implement changes according to the spec", body)
        self.assertNotIn("field: description", body)
        reviewer, _ = frontmatter_of(self.read(".claude/agents/reviewer-agent.md"))
        self.assertEqual(field(reviewer, "model"), "opus")
        self.assertIn("Do not review spec documents", field(reviewer, "description"))
        self.assertIn("In force until a published code-review standard",
                      field(reviewer, "description"), "R1056's Human note rides along")
        designer, _ = frontmatter_of(self.read(".claude/agents/test-designer-agent.md"))
        self.assertIn("Define how correctness will be evaluated", field(designer, "description"))
        manager, _ = frontmatter_of(self.read(".claude/agents/release-manager-agent.md"))
        self.assertIn("ship/no-ship", field(manager, "description"))
        architect, _ = frontmatter_of(self.read(".claude/agents/architect-agent.md"))
        self.assertEqual(field(architect, "description"), "Fiducial's architect-agent role.")

    def test_every_agent_gets_the_same_tools(self):
        """A role's lane is a `scope: agent` lane-guard row, not a tool list."""
        for role in ("reviewer-agent", "skeptic-risk-agent", "spec-reviewer-agent",
                     "context-quality-reviewer", "coder-agent", "test-designer-agent",
                     "architect-agent", "release-manager-agent"):
            front, _ = frontmatter_of(self.read(".claude/agents/%s.md" % role))
            self.assertEqual(field(front, "tools"), "[Read, Grep, Glob, Edit, Write, Bash]", role)

    def test_agent_skills_name_the_skills_the_emission_provides_and_note_the_rest(self):
        manager, _ = frontmatter_of(self.read(".claude/agents/release-manager-agent.md"))
        self.assertEqual(field(manager, "skills"), "[release]")
        reviewer, _ = frontmatter_of(self.read(".claude/agents/reviewer-agent.md"))
        self.assertEqual(field(reviewer, "skills"), "[release]")
        coder, _ = frontmatter_of(self.read(".claude/agents/coder-agent.md"))
        self.assertIsNone(field(coder, "skills"))
        self.assertIn("note: coder-agent names skill 'build'", self.stderr)
        self.assertIn("note: reviewer-agent names skill 'review'", self.stderr)

    def test_agent_body_is_the_roles_rows_rendered_as_a_bundle(self):
        _, body = frontmatter_of(self.read(".claude/agents/test-designer-agent.md"))
        self.assertIn("Edit tests and nothing else; a change you need outside your lane "
                      "is a finding, not an edit.", body)
        self.assertNotIn("```", body)
        self.assertNotIn("lane-guard", body)
        self.assertNotIn("Give a unit's implementation", body, "a skill row is the skill's")
        self.assertNotIn("A test asserts one behaviour", body, "a paths: row is .claude/rules/'")
        _, coder_body = frontmatter_of(self.read(".claude/agents/coder-agent.md"))
        self.assertIn("Run the red gate before any implementation.", coder_body)

    def test_agent_body_subtracts_what_claude_md_already_carries(self):
        """F-4: the subagent loads CLAUDE.md too; its body is what that lacks."""
        claude_md = self.read("CLAUDE.md")
        self.assertIn("Propose; do not decide.", claude_md)
        self.assertIn("**tranche** —", claude_md)
        for role in ("coder-agent", "reviewer-agent", "test-designer-agent"):
            _, body = frontmatter_of(self.read(".claude/agents/%s.md" % role))
            self.assertNotIn("Propose; do not decide.", body, role)
            self.assertNotIn("**tranche**", body, role)
        _, reviewer = frontmatter_of(self.read(".claude/agents/reviewer-agent.md"))
        self.assertIn("Read the whole delta before the first finding.", reviewer)
        # a hook row the standing selection carries is not repeated either
        _, designer = frontmatter_of(self.read(".claude/agents/test-designer-agent.md"))
        self.assertNotIn("Never let a secret value enter context.", designer)

    def test_rules_file_carries_the_paths_rows_under_their_topic(self):
        front, body = frontmatter_of(self.read(".claude/rules/verification.md"))
        self.assertEqual(field(front, "paths"), "[tests/**, SPEC.md]")
        self.assertIn("A test asserts one behaviour and names it.", body)
        self.assertEqual([f for f in self.emitted() if f.startswith(".claude/rules/")],
                         [".claude/rules/verification.md"])

    def test_skills_come_from_the_process_documents(self):
        front, body = frontmatter_of(self.read(".claude/skills/gate/SKILL.md"))
        self.assertEqual(field(front, "name"), "gate")
        self.assertEqual(field(front, "description"),
                         "Request the human's go/no-go for a consequential change.")
        self.assertEqual(field(front, "disable-model-invocation"), "true")
        self.assertTrue(body.strip().startswith("# Process: Gate"))
        self.assertIn("1. Open the issue.", body)
        release, _ = frontmatter_of(self.read(".claude/skills/release/SKILL.md"))
        self.assertEqual(field(release, "name"), "release")
        self.assertEqual(field(release, "description"), "Assemble the change package!")
        self.assertIsNone(field(release, "disable-model-invocation"))

    def test_every_enforce_row_has_its_emitted_object(self):
        """SPEC.md §6: every `harness:*` row's emitted object exists."""
        settings = self.read(".claude/settings.json")
        agents = "".join(self.read(".claude/agents/%s.md" % r) for r in (
            "architect-agent", "test-designer-agent", "coder-agent", "reviewer-agent",
            "release-manager-agent"))
        objects = {
            "R0164": ("Read(./.env)", settings), "R0203": ("kubectl apply", settings),
            "R0564": ("git push --force", settings),
            "R0583": ("decision-log-append-only", settings),
            "R1408": ("review-artifact-immutable", settings),
            "R0196": ("--check generated-filename", settings),
            "R1414": ("--check verdict-lines", settings),
            "R1605": ("--check citations", settings),
            "R0934": ("intake-branch-guard", settings), "R0720": ("push-readback", settings),
            "R0091": ("lane-guard --lane specs", agents),
            "R1156": ("lane-guard --lane tests", agents),
            "R0259": ("model: sonnet", agents), "R0939": ("Implement changes", agents),
            "R1031": ("ship/no-ship", agents), "R1056": ("Do not review spec", agents),
            "R1141": ("Define how correctness", agents),
            "R0486": ("coder-agent names skill 'build'", self.stderr),
            "R0506": ("skills: [release]", agents),
            "R0551": ("name: gate", self.read(".claude/skills/gate/SKILL.md")),
            "R0944": ("context-quality-reviewer names skill 'intake'", self.stderr),
        }
        self.assertEqual(sorted(objects), sorted(HOOK_IDS + DENY_IDS + AGENT_IDS + SKILL_IDS))
        for row_id, (needle, haystack) in objects.items():
            self.assertIn(needle, haystack, row_id)


class TestClaudeCodeRefusals(ClaudeCodeTestCase):
    def assert_refused(self, code, out, err):
        self.assertEqual(code, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertEqual(self.emitted(), [])

    def test_a_query_is_refused(self):
        code, out, err = self.emit("--where", "role=writer")
        self.assert_refused(code, out, err)

    def test_claude_md_over_200_lines_warns_with_the_count_and_still_emits(self):
        long_body = "\n\n".join("Line %d of a long standing rule." % i for i in range(120))
        write(self.clone, "rules/R0050.md", rs_row(
            "R0050", long_body, order=15, topic=["core"], role=["chief-of-staff"],
            session=["decision"], corpus=["software"], verb="require", term=None))
        commit(self.clone, "store: a long row", env=self.env)
        code, out, err = self.emit()
        self.assertEqual(code, 0, err)
        self.assertTrue(no_traceback(out, err), err)
        match = re.search(r"^warning: CLAUDE\.md is (\d+) lines, over the 200-line guidance",
                          err, re.MULTILINE)
        self.assertIsNotNone(match, err)
        self.assertGreater(int(match.group(1)), 200)
        self.assertEqual(int(match.group(1)), self.read("CLAUDE.md").count("\n"))
        self.assertIn("Line 119 of a long standing rule.", self.read("CLAUDE.md"))

    def test_an_enforce_row_without_a_block_is_refused(self):
        write(self.clone, "rules/R0051.md", rs_row(
            "R0051", "A hook row with no block.", order=15, topic=["core"],
            role=["chief-of-staff"], session=["decision"], corpus=["software"],
            verb="require", term=None, enforce="hook"))
        commit(self.clone, "store: a blockless hook row", env=self.env)
        code, out, err = self.emit()
        self.assert_refused(code, out, err)
        self.assertIn("R0051", err)

    def test_a_block_naming_a_script_the_store_lacks_is_refused(self):
        write(self.clone, "rules/R0052.md", rs_row(
            "R0052", "```yaml\nevent: PreToolUse\nmatcher: Bash\ncommand: bin/hooks/nope\n```",
            order=15, topic=["core"], role=["chief-of-staff"], session=["decision"],
            corpus=["software"], verb="require", term=None, enforce="hook"))
        commit(self.clone, "store: a hook row naming no script", env=self.env)
        code, out, err = self.emit()
        self.assert_refused(code, out, err)
        self.assertIn("bin/hooks/nope", err)


class TestClaudeCodeWithoutPathsRows(ClaudeCodeTestCase):
    files = {k: v for k, v in emit_store_files().items() if "R0500" not in k}

    def test_no_rules_directory_when_no_row_carries_paths(self):
        code, _, err = self.emit()
        self.assertEqual(code, 0, err)
        self.assertEqual([f for f in self.emitted() if f.startswith(".claude/rules/")], [])


class TestClaudeCodeSpill(ClaudeCodeTestCase):
    """A topic whose process document is emitted as a skill has its standing
    rows appended to that SKILL.md and omitted from CLAUDE.md; a topic with
    no document stays."""

    files = dict(emit_store_files())
    files["process/decision-log.md"] = rs_process(
        "# Process: Decision Log\n\nHow entries are written.\n",
        order=30, topic=["decision-log"], role=["chief-of-staff"], session=["decision"],
        corpus=["software"])
    files["process/named-queries.md"] = files["process/named-queries.md"].replace(
        "```text\ngate\nrelease\n```", "```text\ngate\nrelease\ndecision-log\n```")

    def setUp(self):
        super().setUp()
        self.code, self.stdout, self.stderr = self.emit()
        self.assertEqual(self.code, 0, self.stderr)

    def test_the_topic_with_a_document_moves_to_the_skill(self):
        # R0583's topic is decision-log-policy; the stem is decision-log
        skill = self.read(".claude/skills/decision-log/SKILL.md")
        self.assertIn("How entries are written.", skill)
        self.assertIn("\n## Rules\n\n", skill)
        rules = skill.split("\n## Rules\n\n", 1)[1]
        self.assertIn("Append to `decisions/log.md`", rules)
        self.assertNotIn("```", rules)
        self.assertNotIn("Append to `decisions/log.md`", self.read("CLAUDE.md"))

    def test_a_topic_with_no_document_stays_in_claude_md(self):
        claude_md = self.read("CLAUDE.md")
        self.assertIn("Propose; do not decide.", claude_md)  # core
        self.assertIn("Never let a secret value enter context.", claude_md)

    def test_a_skill_with_no_rows_gets_no_rules_heading(self):
        self.assertNotIn("## Rules", self.read(".claude/skills/release/SKILL.md"))
        self.assertNotIn("## Rules", self.read(".claude/skills/gate/SKILL.md"))

    def test_the_stem_must_be_one_named_queries_lists(self):
        from rulestore.emit.common import topic_stem
        stems = ["decision-log", "review-artifact", "change-flow", "voice"]
        self.assertEqual(topic_stem("decision-log-policy", stems), "decision-log")
        self.assertEqual(topic_stem("review-artifact-schema", stems), "review-artifact")
        self.assertEqual(topic_stem("change-flow", stems), "change-flow")
        self.assertIsNone(topic_stem("core", stems))
        self.assertIsNone(topic_stem("voices", stems))
        self.assertIsNone(topic_stem("decision-layer", stems))


class TestClaudeCodeWithoutASpillingDocument(ClaudeCodeTestCase):
    def test_without_the_document_the_rows_stay_in_claude_md(self):
        code, _, err = self.emit()
        self.assertEqual(code, 0, err)
        self.assertIn("Append to `decisions/log.md`", self.read("CLAUDE.md"))


class TestClaudeCodeOverTheRealStore(unittest.TestCase):
    """The plan, §3a acceptance: over this repository's own store the
    emission succeeds, CLAUDE.md warns with its count when over the 200-line
    guidance, and the topics that have a skill live in that skill."""

    def test_the_real_store_emits_and_spills_topics_into_their_skills(self):
        out = temp_dir(self, "emit-real-")
        code, stdout, stderr = run_bundle("--emit", "claude-code", "--out", str(out),
                                          cwd=BIN_DIR.parent, env=base_env())
        self.assertTrue(no_traceback(stdout, stderr), stderr)
        self.assertEqual(code, 0, stderr)
        count = (out / "CLAUDE.md").read_text().count("\n")
        if count > 200:
            self.assertIn("warning: CLAUDE.md is %d lines" % count, stderr)
        else:
            self.assertNotIn("warning: CLAUDE.md", stderr)
        self.assertTrue((out / ".claude/settings.json").is_file())
        retro = (out / ".claude/skills/retro/SKILL.md").read_text()
        self.assertIn("\n## Rules\n", retro)


# ---- #416: cross-procedure references resolve in the emitted layout --------

REF_RE = re.compile(r"process/[\w-]+\.md")
CLAUDE_REF_RE = re.compile(r"the ([\w-]+) skill \((\.claude/skills/[\w-]+/SKILL\.md)\)")


def named_bundle_roles():
    """Role slugs of the twelve standalone bundles, from the one list that names them."""
    text = (BIN_DIR.parent / "process/named-queries.md").read_text()
    return re.findall(r"^\S+\s+role=(\S+)$", text, re.M)


class TestClaudeCodeCrossProcedureReferences(unittest.TestCase):
    """Synthetic process documents: the rewrite form is fixed, backticks are consumed."""

    def emit(self, body, extra=()):
        rows = [Row(id="a", kind="process", path="process/a.md", body="# Process: A\n\n" + body,
                    keys={"topic": ["a"]}),
                Row(id="b", kind="process", path="process/b.md", body="# Process: B\n\nThe B form.\n",
                    keys={"topic": ["b"]}), *extra]
        inputs = EmitInputs(rows=rows, sequences=([["core"]], ["a", "b"]), tiers=load_tiers(),
                            hooks={}, repo="fixture/store", head="a" * 40)
        return targets()["claude-code"].emit(inputs).files

    def test_a_reference_to_an_emitted_skill_names_the_skill_in_the_claude_code_form(self):
        ref = "the b skill (.claude/skills/b/SKILL.md)"
        cases = (("Use `process/b.md` for the form.", "Use %s for the form." % ref),
                 ("Apply `process/b.md`'s dispositions.", "Apply %s's dispositions." % ref),
                 ("See process/b.md.", "See %s." % ref),
                 ("Both `process/b.md` and process/b.md.", "Both %s and %s." % (ref, ref)))
        for source, expected in cases:
            with self.subTest(source=source):
                skill = self.emit("Plain first sentence.\n\n" + source + "\n")[".claude/skills/a/SKILL.md"]
                self.assertIn(expected, skill)
                self.assertNotIn("process/b.md", skill)
                self.assertNotIn("`the b skill", skill)
                self.assertNotIn(")`", skill)

    def test_a_reference_to_a_document_that_is_not_a_skill_fails_emission_naming_file_and_reference(self):
        setup = Row(id="project-setup", kind="process", path="process/project-setup.md",
                    body="# Process: Setup\n\nSet up.\n", keys={"topic": ["project-setup"]})
        for reference in ("process/project-setup.md", "process/nope.md"):
            with self.subTest(reference=reference):
                with self.assertRaises(EmitError) as caught:
                    self.emit("Plain first sentence.\n\nRead `%s` first.\n" % reference, extra=[setup])
                self.assertIn("process/a.md", str(caught.exception))
                self.assertIn(reference, str(caught.exception))

    def test_a_skill_with_no_cross_references_emits_unchanged(self):
        skill = self.emit("Nothing to cite.\n")[".claude/skills/a/SKILL.md"]
        self.assertTrue(skill.rstrip().endswith("Nothing to cite."))


class TestClaudeCodeRealStoreReferences(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = unittest.TestCase()
        cls.out = temp_dir(cls.case, "emit-refs-")
        code, _, err = run_bundle("--emit", "claude-code", "--out", str(cls.out),
                                  cwd=BIN_DIR.parent, env=base_env())
        assert code == 0, err

    @classmethod
    def tearDownClass(cls):
        cls.case.doCleanups()

    def skills(self):
        return {p: p.read_text() for p in sorted(self.out.glob(".claude/skills/*/SKILL.md"))}

    def test_every_cross_procedure_reference_resolves_to_a_file_in_the_layout(self):
        emitted = {p.parent.name for p in self.skills()}
        found = 0
        for path, text in self.skills().items():
            with self.subTest(skill=path.parent.name):
                self.assertEqual(REF_RE.findall(text), [], "a process/ path an adopted repository lacks")
                for name, target in CLAUDE_REF_RE.findall(text):
                    found += 1
                    self.assertIn(name, emitted)
                    self.assertEqual(target, ".claude/skills/%s/SKILL.md" % name)
                    self.assertTrue((self.out / target).is_file(), target)
        self.assertGreaterEqual(found, 9, "the nine references the sources carry must survive as skill names")


class TestRoleBundlesAreUnchangedByTheReferenceRewrite(unittest.TestCase):
    """C4. The twelve standalone bundles are not emitted skills: they keep the
    source `process/<stem>.md` paths, and `--emit bundle` still writes the
    bytes `--where` writes. (A byte-for-byte comparison with the pre-change
    bundles needs a pinned baseline the suite does not carry; this guards the
    two ways a rewrite could leak into them.)"""

    def test_each_bundle_keeps_source_references_and_both_paths_agree(self):
        roles = named_bundle_roles()
        self.assertEqual(len(roles), 12, roles)
        env, kept = base_env(), {}
        for role in roles:
            with self.subTest(role=role):
                where, emit = temp_dir(self, "bundle-where-"), temp_dir(self, "bundle-emit-")
                self.assertEqual(run_bundle("--where", "role=" + role, "--out", str(where),
                                            cwd=BIN_DIR.parent, env=env)[0], 0)
                self.assertEqual(run_bundle("--emit", "bundle", "--where", "role=" + role, "--out", str(emit),
                                            cwd=BIN_DIR.parent, env=env)[0], 0)
                (a,), (b,) = sorted(where.iterdir()), sorted(emit.iterdir())
                body = lambda path: "\n".join(path.read_text().splitlines()[1:])
                self.assertEqual(body(a), body(b))
                text = body(a)
                self.assertNotRegex(text, r"the [\w-]+ skill \(\.claude/skills/")
                self.assertNotIn(".agents/skills/", text)
                kept[role] = len(REF_RE.findall(text))
        self.assertGreater(kept["coder-agent"], 0, kept)
        self.assertGreater(kept["chief-of-staff"], 0, kept)


if __name__ == "__main__":
    unittest.main()
