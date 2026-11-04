"""`bin/hooks/*` against a stand-in git repository (the plan, §3a acceptance):
each hook blocks what its row says and passes what it should, both ways.

Every script is run as Claude Code runs it — a subprocess with the hook's
JSON on stdin — from a copy under a temp dir, the way the emitter installs
it, so a script that forgot to carry `_hooklib.py` along would fail here.
Exit 2 with a reason on stderr is a block; exit 0 is a pass.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import unittest

from tests.helpers import BIN_DIR, base_env, commit, git, make_repo, temp_dir, write

HOOKS_SRC = BIN_DIR / "hooks"
LOG = ("## DEC-000001 — First\nDate: 2026-01-01\nDecision: One.\n\n"
       "## DEC-000002 — Second\nDate: 2026-01-02\nDecision: Two.\n")


class HookTestCase(unittest.TestCase):
    def setUp(self):
        self.env = base_env()
        self.repo = make_repo(self, name="target")
        self.hooks = temp_dir(self, "hooks-") / "hooks"
        shutil.copytree(HOOKS_SRC, self.hooks, ignore=shutil.ignore_patterns("__pycache__"))
        write(self.repo, "README.md", "A stand-in repository.\n")
        write(self.repo, "decisions/log.md", LOG)
        write(self.repo, "reviews/landed-20260101T000000Z.md",
              "# Review\n\nVerdict: ready\n\n## Verdict (Quality): ready\n")
        write(self.repo, "rules/R0001.md",
              "---\nid: R0001\norder: 10\ntopic: [core]\nrole: [writer, critic]\n"
              "session: [decision]\ncorpus: [writing]\nverb: require\nterm: null\n---\n\n"
              "Propose; do not decide.\n")
        write(self.repo, "rules/R0002.md",
              "---\nid: R0002\norder: 20\ntopic: [core]\nrole: [writer]\n"
              "session: [decision]\ncorpus: [writing]\nverb: require\nterm: null\n---\n\n"
              "State the obligation at its shortest.\n")
        write(self.repo, "rules/R0100.md",
              "---\nid: R0100\norder: 20\ntopic: [lexicon]\nverb: define\n"
              "term: [tranche]\n---\n\nA tranche is one workstream.\n")
        write(self.repo, "process/retro.md", "# Retro\n")
        write(self.repo, "SPEC.md", "# Spec\n")
        write(self.repo, "specs/one.md", "# One\n")
        write(self.repo, "tests/test_one.py", "def test_one(): pass\n")
        write(self.repo, "src/one.py", "x = 1\n")
        commit(self.repo, "seed", env=self.env)

    def run_hook(self, name, *args, tool="Write", file_path=None, extra=None, cwd=None):
        tool_input = dict(extra or {})
        if file_path is not None:
            tool_input["file_path"] = str(self.repo / file_path)
        payload = {
            "hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": tool_input,
            "cwd": str(cwd or self.repo),
        }
        proc = subprocess.run(
            [str(self.hooks / name), *args], input=json.dumps(payload), cwd=str(cwd or self.repo),
            env=self.env, capture_output=True, text=True, timeout=60,
        )
        return proc.returncode, proc.stdout, proc.stderr

    def assert_blocks(self, result, *needles):
        code, out, err = result
        self.assertEqual(code, 2, "stdout=%r stderr=%r" % (out, err))
        for needle in needles:
            self.assertIn(needle, err)
        self.assertNotIn("Traceback", err)

    def assert_passes(self, result):
        code, out, err = result
        self.assertEqual(code, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("Traceback", err)

    def checkout(self, branch):
        git(self.repo, "checkout", "-q", "-b", branch, env=self.env, check=True)


class TestIntakeBranchGuard(HookTestCase):
    """R0934: rules/ and process/ edit only on intake/*."""

    def test_blocks_a_rules_edit_off_an_intake_branch(self):
        self.checkout("pkg-9-anything")
        self.assert_blocks(self.run_hook("intake-branch-guard", file_path="rules/R0001.md"),
                           "rules/R0001.md", "intake/")

    def test_blocks_a_process_edit_on_main(self):
        self.assert_blocks(self.run_hook("intake-branch-guard", tool="Edit",
                                         file_path="process/retro.md"), "process/retro.md")

    def test_passes_a_rules_edit_on_an_intake_branch(self):
        self.checkout("intake/new-row")
        self.assert_passes(self.run_hook("intake-branch-guard", file_path="rules/R0001.md"))

    def test_passes_a_new_row_on_an_intake_branch(self):
        self.checkout("intake/new-row")
        self.assert_passes(self.run_hook("intake-branch-guard", file_path="rules/R0099.md"))

    def test_passes_an_edit_outside_the_governed_paths_on_any_branch(self):
        self.assert_passes(self.run_hook("intake-branch-guard", file_path="src/one.py"))
        self.assert_passes(self.run_hook("intake-branch-guard", file_path="README.md"))

    def test_passes_a_call_naming_no_file(self):
        self.assert_passes(self.run_hook("intake-branch-guard", tool="Bash",
                                         extra={"command": "ls"}))

    def test_a_relative_path_resolves_against_cwd(self):
        proc_input = {"tool_name": "Write", "tool_input": {"file_path": "rules/R0001.md"},
                      "cwd": str(self.repo)}
        proc = subprocess.run([str(self.hooks / "intake-branch-guard")],
                              input=json.dumps(proc_input), cwd="/", env=self.env,
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 2, proc.stderr)


class TestReviewArtifactImmutable(HookTestCase):
    """R1408: a reviews/ file tracked at HEAD is never rewritten."""

    def test_blocks_a_write_to_a_landed_artifact(self):
        self.assert_blocks(self.run_hook("review-artifact-immutable",
                                         file_path="reviews/landed-20260101T000000Z.md"),
                           "landed review artifact")

    def test_blocks_an_edit_to_a_landed_artifact(self):
        self.assert_blocks(self.run_hook("review-artifact-immutable", tool="Edit",
                                         file_path="reviews/landed-20260101T000000Z.md"))

    def test_passes_a_new_untracked_artifact(self):
        self.assert_passes(self.run_hook("review-artifact-immutable",
                                         file_path="reviews/draft-20260102T000000Z.md"))

    def test_passes_an_untracked_artifact_being_revised_before_it_lands(self):
        write(self.repo, "reviews/draft-20260102T000000Z.md", "Verdict: ready\n")
        self.assert_passes(self.run_hook("review-artifact-immutable", tool="Edit",
                                         file_path="reviews/draft-20260102T000000Z.md"))

    def test_passes_a_tracked_file_outside_reviews(self):
        self.assert_passes(self.run_hook("review-artifact-immutable", file_path="README.md"))


class TestDecisionLogAppendOnly(HookTestCase):
    """R0583: decisions/log.md takes appends after the last entry only."""

    def test_write_that_appends_passes(self):
        self.assert_passes(self.run_hook(
            "decision-log-append-only", file_path="decisions/log.md",
            extra={"content": LOG + "\n## DEC-000003 — Third\nDecision: Three.\n"}))

    def test_write_that_changes_an_entry_is_blocked(self):
        self.assert_blocks(self.run_hook(
            "decision-log-append-only", file_path="decisions/log.md",
            extra={"content": LOG.replace("Decision: One.", "Decision: Uno.")}),
            "only an append")

    def test_write_that_drops_an_entry_is_blocked(self):
        self.assert_blocks(self.run_hook(
            "decision-log-append-only", file_path="decisions/log.md",
            extra={"content": LOG.split("## DEC-000002")[0]}))

    def test_edit_that_appends_after_the_last_entry_passes(self):
        tail = "## DEC-000002 — Second\nDate: 2026-01-02\nDecision: Two.\n"
        self.assert_passes(self.run_hook(
            "decision-log-append-only", tool="Edit", file_path="decisions/log.md",
            extra={"old_string": tail, "new_string": tail + "\n## DEC-000003 — Third\n"}))

    def test_edit_in_the_middle_is_blocked(self):
        self.assert_blocks(self.run_hook(
            "decision-log-append-only", tool="Edit", file_path="decisions/log.md",
            extra={"old_string": "Decision: One.", "new_string": "Decision: One. Amended."}),
            "not the end of the log")

    def test_edit_that_rewrites_the_tail_is_blocked(self):
        tail = "Decision: Two.\n"
        self.assert_blocks(self.run_hook(
            "decision-log-append-only", tool="Edit", file_path="decisions/log.md",
            extra={"old_string": tail, "new_string": "Decision: Two, revised.\n"}),
            "does not begin with old_string")

    def test_edit_with_replace_all_is_blocked(self):
        self.assert_blocks(self.run_hook(
            "decision-log-append-only", tool="Edit", file_path="decisions/log.md",
            extra={"old_string": "Decision: Two.\n", "new_string": "Decision: Two.\nMore.\n",
                   "replace_all": True}), "replace_all")

    def test_any_other_file_passes(self):
        self.assert_passes(self.run_hook(
            "decision-log-append-only", file_path="README.md", extra={"content": "x"}))

    def test_creating_the_log_passes(self):
        (self.repo / "decisions/log.md").unlink()
        self.assert_passes(self.run_hook(
            "decision-log-append-only", file_path="decisions/log.md",
            extra={"content": "## DEC-000001 — First\n"}))


class TestLaneGuard(HookTestCase):
    """R0091, R1156: a lane-bound agent writes inside its lane only."""

    def test_specs_lane_passes_spec_md_and_specs_tree(self):
        self.assert_passes(self.run_hook("lane-guard", "--lane", "specs", file_path="SPEC.md"))
        self.assert_passes(self.run_hook("lane-guard", "--lane", "specs",
                                         file_path="specs/two.md"))

    def test_specs_lane_blocks_source_and_tests(self):
        self.assert_blocks(self.run_hook("lane-guard", "--lane", "specs", file_path="src/one.py"),
                           "outside the specs lane", "finding, not an edit")
        self.assert_blocks(self.run_hook("lane-guard", "--lane", "specs",
                                         file_path="tests/test_one.py"))

    def test_tests_lane_passes_the_test_tree(self):
        for path in ("tests/test_one.py", "bin/tests/test_two.py", "src/foo_test.go",
                     "web/__tests__/app.test.ts", "pkg/conftest.py"):
            self.assert_passes(self.run_hook("lane-guard", "--lane", "tests", file_path=path))

    def test_tests_lane_blocks_source_and_specs(self):
        self.assert_blocks(self.run_hook("lane-guard", "--lane", "tests", file_path="src/one.py"),
                           "outside the tests lane")
        self.assert_blocks(self.run_hook("lane-guard", "--lane", "tests", file_path="SPEC.md"))

    def test_a_call_naming_no_file_passes(self):
        self.assert_passes(self.run_hook("lane-guard", "--lane", "tests", tool="Bash",
                                         extra={"command": "pytest"}))

    def test_an_unknown_lane_is_an_error_not_a_pass(self):
        code, _, _ = self.run_hook("lane-guard", "--lane", "docs", file_path="src/one.py")
        self.assertEqual(code, 2)


class TestStoreLintGeneratedFilename(HookTestCase):
    """R0196: a new file under retros/ or reviews/ carries the timestamp."""

    def test_blocks_a_new_review_without_a_timestamp(self):
        write(self.repo, "reviews/pkg-3a-read.md", "Verdict: ready\n")
        self.assert_blocks(self.run_hook("store-lint", "--check", "generated-filename",
                                         file_path="reviews/pkg-3a-read.md"),
                           "lacks a <YYYYMMDD>T<HHMMSS>Z timestamp")

    def test_blocks_a_new_retro_without_a_timestamp(self):
        write(self.repo, "retros/retro.md", "# Retro\n")
        self.assert_blocks(self.run_hook("store-lint", "--check", "generated-filename",
                                         file_path="retros/retro.md"))

    def test_passes_a_new_review_with_a_timestamp(self):
        write(self.repo, "reviews/pkg-3a-read-20260104T120000Z.md", "Verdict: ready\n")
        self.assert_passes(self.run_hook("store-lint", "--check", "generated-filename",
                                         file_path="reviews/pkg-3a-read-20260104T120000Z.md"))

    def test_passes_a_tracked_file_whatever_its_name(self):
        write(self.repo, "reviews/old-cycle-1.md", "Verdict: ready\n")
        commit(self.repo, "an old artifact", env=self.env)
        self.assert_passes(self.run_hook("store-lint", "--check", "generated-filename",
                                         file_path="reviews/old-cycle-1.md"))

    def test_passes_a_file_elsewhere(self):
        write(self.repo, "docs/notes.md", "notes\n")
        self.assert_passes(self.run_hook("store-lint", "--check", "generated-filename",
                                         file_path="docs/notes.md"))


class TestStoreLintVerdictLines(HookTestCase):
    """R1414: one overall Verdict, one per pass, the enum, the most severe."""

    def lint(self, text, name="reviews/x-20260104T120000Z.md"):
        write(self.repo, name, text)
        return self.run_hook("store-lint", "--check", "verdict-lines", file_path=name)

    def test_passes_a_well_formed_artifact(self):
        self.assert_passes(self.lint(
            "# Review\n\nVerdict: changes-required\n\n## Verdict (Quality): ready\n\n"
            "## Verdict (Skepticism): changes-required\n"))

    def test_blocks_a_missing_overall_verdict(self):
        self.assert_blocks(self.lint("# Review\n\n## Verdict (Quality): ready\n"),
                           "exactly one overall")

    def test_blocks_a_value_outside_the_enum(self):
        self.assert_blocks(self.lint("Verdict: approved\n\n## Verdict (Quality): approved\n"),
                           "not one of ready|ready-with-findings|changes-required")

    def test_blocks_an_overall_milder_than_a_pass(self):
        self.assert_blocks(self.lint(
            "Verdict: ready\n\n## Verdict (Quality): ready\n\n"
            "## Verdict (Skepticism): ready-with-findings\n"), "most severe")

    def test_blocks_an_artifact_with_no_pass_verdict(self):
        self.assert_blocks(self.lint("Verdict: ready\n"), "no `Verdict (<pass>):`")

    def test_passes_a_file_outside_reviews(self):
        write(self.repo, "docs/verdict.md", "Verdict: whatever\n")
        self.assert_passes(self.run_hook("store-lint", "--check", "verdict-lines",
                                         file_path="docs/verdict.md"))


class TestStoreLintCitations(HookTestCase):
    """R1605 and R0264's four criteria, over a row under rules/."""

    def row(self, row_id, body, **overrides):
        fields = {"topic": "[core]", "role": "[writer]", "session": "[decision]",
                  "corpus": "[writing]", "verb": "require", "term": "null"}
        fields.update(overrides)
        front = "".join("%s: %s\n" % (k, v) for k, v in fields.items())
        write(self.repo, "rules/%s.md" % row_id,
              "---\nid: %s\norder: 30\n%s---\n\n%s\n" % (row_id, front, body))
        return self.run_hook("store-lint", "--check", "citations",
                             file_path="rules/%s.md" % row_id)

    def test_passes_a_citation_that_co_renders(self):
        self.assert_passes(self.row("R0003", "As [R0001] says, propose."))

    def test_blocks_a_citation_that_cannot_co_render(self):
        # R0002 carries role writer only; the citing row also carries critic
        self.assert_blocks(self.row("R0003", "As [R0002] says.", role="[writer, critic]"),
                           "[R0002] does not carry role critic")

    def test_blocks_a_citation_of_a_row_not_in_the_store(self):
        self.assert_blocks(self.row("R0003", "As [R0777] says."), "not in the store")

    def test_blocks_a_file_path_in_the_body(self):
        self.assert_blocks(self.row("R0003", "Read src/main.py first."),
                           "refers to a file by path: 'src/main.py'")

    def test_passes_the_exempt_names(self):
        self.assert_passes(self.row(
            "R0003", "Read SPEC.md whole; append to decisions/log.md; the hook is "
            "bin/hooks/store-lint; rows live under rules/ and go/no-go is a word pair."))

    def test_passes_a_path_inside_the_fenced_block_and_the_human_note(self):
        self.assert_passes(self.row(
            "R0003", "Push plainly.\n\n```yaml\ncommand: bin/hooks/x\n```\n\n## Human\n\n"
            "See src/main.py.", enforce="hook"))

    def test_blocks_a_key_value_no_other_row_holds(self):
        self.assert_blocks(self.row("R0003", "A new topic.", topic="[novel-topic]"),
                           "topic: 'novel-topic' is a value no other row holds")

    def test_blocks_a_role_row_naming_no_session(self):
        self.assert_blocks(self.row("R0003", "No session.", session="null"),
                           "names no session")

    def test_passes_a_definition_with_no_role_or_session(self):
        self.assert_passes(self.row("R0003", "A tranche is a workstream.", role="null",
                                    session="null", corpus="null", verb="define",
                                    term="[tranche]"))

    def test_blocks_a_model_name(self):
        self.assert_blocks(self.row("R0003", "Use opus for the review gate."),
                           "names a model, not a tier: 'opus'")

    def test_passes_a_tier_name(self):
        self.assert_passes(self.row("R0003", "Use the frontier tier for the review gate."))

    def test_passes_a_file_outside_rules(self):
        write(self.repo, "docs/notes.md", "See src/main.py and [R0777].\n")
        self.assert_passes(self.run_hook("store-lint", "--check", "citations",
                                         file_path="docs/notes.md"))

    def test_passes_a_retired_row(self):
        write(self.repo, "rules/retired/R0009.md", "---\nid: R0009\n---\n\nSee src/main.py.\n")
        self.assert_passes(self.run_hook("store-lint", "--check", "citations",
                                         file_path="rules/retired/R0009.md"))


class TestPushReadback(HookTestCase):
    """R0720: after a git push, fetch and print the remote ref; fail on a
    mismatch."""

    def setUp(self):
        super().setUp()
        parent = temp_dir(self, "push-readback-")
        self.origin = parent / "origin.git"
        git(parent, "init", "--bare", "-q", "-b", "main", str(self.origin), env=self.env,
            check=True)
        git(self.repo, "remote", "add", "origin", str(self.origin), env=self.env, check=True)

    def bash(self, command):
        return self.run_hook("push-readback", tool="Bash", extra={"command": command})

    def head(self):
        return git(self.repo, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()

    def test_a_push_that_landed_passes_and_prints_the_remote_sha(self):
        git(self.repo, "push", "-q", "origin", "main", env=self.env, check=True)
        code, out, err = self.bash("git push origin main")
        self.assertEqual(code, 0, err)
        self.assertIn("push-readback: origin/main is at %s" % self.head(), out)

    def test_a_push_with_no_refspec_reads_back_the_current_branch(self):
        git(self.repo, "push", "-q", "-u", "origin", "main", env=self.env, check=True)
        code, out, err = self.bash("git push")
        self.assertEqual(code, 0, err)
        self.assertIn("origin/main is at %s" % self.head(), out)

    def test_a_push_the_remote_did_not_take_fails_loudly(self):
        git(self.repo, "push", "-q", "origin", "main", env=self.env, check=True)
        write(self.repo, "README.md", "changed\n")
        commit(self.repo, "a commit that never reached origin", env=self.env)
        code, out, err = self.bash("git push origin main")
        self.assertEqual(code, 2, out)
        self.assertIn("reads back", err)
        self.assertIn(self.head(), err)

    def test_a_push_to_a_missing_remote_fails_loudly(self):
        code, _, err = self.bash("git push nowhere main")
        self.assertEqual(code, 2)
        self.assertIn("fetch nowhere main failed", err)

    def test_a_push_in_a_compound_command_is_found(self):
        git(self.repo, "push", "-q", "origin", "main", env=self.env, check=True)
        code, out, err = self.bash("git add -A && git push origin main 2>&1 | tail -1")
        self.assertEqual(code, 0, err)
        self.assertIn("origin/main is at", out)

    def test_a_command_that_is_not_a_push_passes_silently(self):
        code, out, err = self.bash("git status && echo 'git pushover'")
        self.assertEqual(code, 0, err)
        self.assertEqual(out, "")

    def test_a_delete_push_passes_without_a_readback(self):
        code, out, _ = self.bash("git push origin --delete gone")
        self.assertEqual(code, 0)
        self.assertEqual(out, "")


if __name__ == "__main__":
    unittest.main()
