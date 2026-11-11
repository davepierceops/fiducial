"""Execute the adopter's published Python fence, not a test-only merger.

The real store/CLI supplies both harness trees; small staged deltas exercise
upgrades and collisions without mocking the emitter or duplicating the merge.
GitHub label tests use a stand-in API boundary and claim no live verification.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import types
import unittest

from tests.helpers import REPO_ROOT, base_env, make_repo, temp_dir, write


DOCUMENT = REPO_ROOT / "process/adopt.md"
FENCES = re.findall(r"^```python\n(.*?)^```$", DOCUMENT.read_text(), re.M | re.S)
assert len(FENCES) == 1, "the adopter must publish one executable procedure"
ADOPT = types.ModuleType("adopter_procedure")
exec(compile(FENCES[0], str(DOCUMENT), "exec"), ADOPT.__dict__)


def dump(path, value):
    path.write_bytes(ADOPT.encoded(value))
    return path


def tree_bytes(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mode & 0o777)
            for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts}


class AdopterProcedure(unittest.TestCase):
    def setUp(self):
        self.work = temp_dir(self, "adopter-")
        self.target = make_repo(self, parent=self.work)
        self.stage = self.work / "stage"
        self.trees = [self.work / "claude-code", self.work / "codex"]
        for tree in self.trees:
            tree.mkdir()
        write(self.trees[0], "CLAUDE.md", "# Store\nHuman approves consequential changes.\n")
        write(self.trees[1], "AGENTS.md", "# Store\nHuman approves consequential changes.\n")

    def plan(self, edits=()):
        plan = ADOPT.build_plan(self.target, self.trees, edits)
        self.plans = getattr(self, "plans", 0) + 1  # each install writes its own report
        plan["timestamp"] = "20261105T0102%02dZ" % self.plans
        self.stage.mkdir(exist_ok=True)
        dump(self.stage / "plan.json", plan)
        return plan

    def authorize(self, findings=(), rulings=None):
        review = {"plan_sha256": ADOPT.digest((self.stage / "plan.json").read_bytes()),
                  "reviewer": "independent fixture reader", "findings": list(findings)}
        review_path = dump(self.work / "review.json", review)
        approval = {"plan_sha256": review["plan_sha256"],
                    "review_sha256": ADOPT.digest(review_path.read_bytes()),
                    "human": "stand-in human", "go": True, "gate": "stand-in gate #1",
                    "rulings": rulings or {}}
        return review_path, dump(self.work / "approval.json", approval)

    def install(self, findings=(), rulings=None):
        return ADOPT.apply(self.stage, *self.authorize(findings, rulings))

    def test_real_both_emissions_create_and_second_run_changes_nothing(self):
        write(self.target, "CLAUDE.md", "# Project\nUse this project's test command.\n")
        write(self.target, "src/AGENTS.md", "# Nested instructions\n")
        write(self.target, "src/AGENTS.override.md", "# Override\n")
        write(self.target, "AGENTS.override.md", "# Root override\n")
        write(self.target, ".codex/config.toml", 'model = "project-choice"\n')
        write(self.target, ".claude/settings.json", '{"permissions":{"allow":["Bash(make test)"]}}\n')
        original = tree_bytes(self.target)
        env = base_env()
        # Exercise the exact documented CLI, including subprocess emission.
        helper = write(self.work, "adopt.py", FENCES[0])
        proc = subprocess.run([sys.executable, str(helper), "prepare", str(REPO_ROOT),
                               str(self.target), str(self.stage)], env=env, text=True, capture_output=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        plan = json.loads((self.stage / "plan.json").read_bytes())
        self.assertEqual(plan["conflicts"], [])
        self.assertEqual(tree_bytes(self.target), original)
        for path in ("src/AGENTS.md", "src/AGENTS.override.md", "AGENTS.override.md",
                     ".codex/config.toml", ".claude/settings.json"):
            self.assertIn(path, plan["inventory"])
        for name in ("claude-code/.claude/skills/adopt/SKILL.md", "codex/.agents/skills/adopt/SKILL.md"):
            emitted = (self.stage / name).read_text()
            self.assertRegex(emitted, r'^---\nname: (?:"adopt"|adopt)\n')
            self.assertIn(FENCES[0].strip(), emitted)
        paths = self.install()
        self.assertIn("CLAUDE.md", paths)
        self.assertIn("AGENTS.md", paths)
        for path in ("src/AGENTS.md", "src/AGENTS.override.md", "AGENTS.override.md", ".codex/config.toml"):
            self.assertEqual(tree_bytes(self.target)[path], original[path])
        settings = json.loads((self.target / ".claude/settings.json").read_bytes())
        self.assertEqual(settings["permissions"]["allow"], ["Bash(make test)"])
        for hook in (self.target / ".claude/hooks").iterdir():
            self.assertTrue(os.access(hook, os.X_OK))
            staged_hook = self.stage / "claude-code/.claude/hooks" / hook.name
            self.assertEqual(hook.read_bytes(), staged_hook.read_bytes())
        import tomllib
        for path in (self.target / ".codex/agents").glob("*.toml"):
            self.assertIn("developer_instructions", tomllib.loads(path.read_text()))
        report = list((self.target / "docs").glob("fiducial-adoption-*.md"))
        self.assertEqual(len(report), 1)
        self.assertIn("contract-verified", report[0].read_text())
        installed = tree_bytes(self.target)
        again = self.work / "stage-again"
        second = ADOPT.prepare(REPO_ROOT, self.target, again)
        self.assertEqual(second["conflicts"], [])
        self.assertEqual(second["writes"], {})
        self.stage = again
        self.assertEqual(self.install(), [])
        self.assertEqual(tree_bytes(self.target), installed)

    def test_contradictory_claude_is_cited_and_not_overwritten_without_human_ruling(self):
        write(self.target, "CLAUDE.md", "Agents must merge consequential changes without asking.\n")
        plan = self.plan()
        self.assertEqual(plan["conflicts"], [])  # A merge is not a contradiction judgment.
        finding = {"id": "C1", "file": "CLAUDE.md", "line": 1,
                   "staged_file": "claude-code/CLAUDE.md", "staged_line": 2,
                   "claim": "Existing permission conflicts with the human approval boundary."}
        paths = self.authorize([finding])
        before = tree_bytes(self.target)
        with self.assertRaisesRegex(ValueError, "ruling required"):
            ADOPT.apply(self.stage, *paths)
        self.assertEqual(tree_bytes(self.target), before)
        # The actual resolution is visible in a new candidate before approval.
        self.plan([{"path": "CLAUDE.md", "before": "Agents must merge consequential changes without asking.\n",
                    "after": "# Project\n"}])
        self.install([finding], {"C1": "Human approves replacing the obsolete instruction by the staged boundary."})
        result = (self.target / "CLAUDE.md").read_text()
        self.assertNotIn("without asking", result)
        self.assertIn("Human approves", result)
        self.assertIn("C1", next((self.target / "docs").glob("*.md")).read_text())

    def test_markdown_sections_preserve_unrelated_text_and_update_only_ownership(self):
        write(self.target, "CLAUDE.md", "# Project\n\n```html\n<!-- fiducial:begin -->\nexample\n<!-- fiducial:end -->\n```\n")
        self.plan()
        self.install()
        write(self.target, "CLAUDE.md", (self.target / "CLAUDE.md").read_text() + "\nLocal afterword.\n")
        write(self.trees[0], "CLAUDE.md", "# Store v2\nNew standing instruction.\n")
        plan = self.plan()
        self.assertFalse(plan["conflicts"])
        changed = plan["writes"]["CLAUDE.md"]["text"]
        self.assertIn("example", changed)
        self.assertIn("Local afterword.", changed)
        self.assertIn("New standing instruction.", changed)
        self.assertNotIn("Human approves", changed)

    def test_frontmatter_stays_first_and_owned_header_can_upgrade(self):
        name = ".claude/agents/coder.md"
        write(self.trees[0], name, '---\nname: coder\nmodel: old\n---\n\n# Coder\n')
        self.plan()
        self.install()
        text = (self.target / name).read_text()
        self.assertTrue(text.startswith("---\n"))
        write(self.target, name, text + "\nProject-specific paragraph.\n")
        write(self.trees[0], name, '---\nname: coder\nmodel: new\n---\n\n# New coder\n')
        plan = self.plan()
        self.assertFalse(plan["conflicts"])
        result = plan["writes"][name]["text"]
        self.assertTrue(result.startswith("---\nname: coder\nmodel: new\n---\n"))
        self.assertIn("Project-specific paragraph.", result)
        self.assertIn("# New coder", result)

    def test_json_upgrade_removes_only_owned_entries_and_never_claims_borrowed_entries(self):
        name = ".claude/settings.json"
        original = {"permissions": {"allow": ["custom"], "deny": ["borrowed"]}, "other": {"x": True}}
        write(self.target, name, json.dumps(original))
        write(self.trees[0], name, json.dumps({"permissions": {"deny": ["owned-v1", "borrowed"]}}))
        self.plan()
        self.install()
        existing = json.loads((self.target / name).read_bytes())
        existing["permissions"]["deny"].append("added-after-adoption")
        write(self.target, name, json.dumps(existing))
        write(self.trees[0], name, json.dumps({"permissions": {"deny": ["owned-v2"]}}))
        plan = self.plan()
        self.assertFalse(plan["conflicts"])
        result = json.loads(plan["writes"][name]["text"])
        self.assertEqual(result["permissions"]["deny"], ["borrowed", "added-after-adoption", "owned-v2"])
        self.assertEqual(result["permissions"]["allow"], ["custom"])
        self.assertEqual(result["other"], {"x": True})

    def test_obsolete_files_and_json_contributions_are_removed(self):
        write(self.trees[0], ".claude/hooks/obsolete", "#!/bin/sh\nexit 0\n").chmod(0o755)
        write(self.trees[0], ".claude/settings.json", '{"hooks":{"OldEvent":[{"command":"obsolete"}]}}')
        self.plan()
        self.install()
        (self.trees[0] / ".claude/hooks/obsolete").unlink()
        write(self.trees[0], ".claude/settings.json", '{"hooks":{}}')
        plan = self.plan()
        self.assertFalse(plan["conflicts"])
        self.assertIsNone(plan["writes"][".claude/hooks/obsolete"]["text"])
        self.assertEqual(json.loads(plan["writes"][".claude/settings.json"]["text"]), {"hooks": {"OldEvent": []}})

    def test_structural_conflicts_never_write_any_target_file(self):
        cases = [
            (".codex/agents/coder.toml", 'name = "project coder"\n', 'name = "fiducial coder"\n'),
            (".claude/hooks/guard", "#!/bin/sh\necho custom\n", "#!/bin/sh\nexit 0\n"),
            (".claude/agents/coder.md", "---\nmodel: custom\n---\nLocal\n", "---\nmodel: other\n---\nStore\n"),
            (".claude/settings.json", "not JSON", '{}'),
            ("CLAUDE.md", "<!-- fiducial:begin -->\nmissing end\n", "Store\n"),
            ("CLAUDE.md", "```text\nunterminated example\n", "Store\n"),
            ("AGENTS.md", "<!-- fiducial:begin -->\nold\n<!-- fiducial:end -->\n", "Store\n"),
        ]
        for name, current, wanted in cases:
            with self.subTest(name=name):
                path = write(self.target, name, current)
                stage_path = write(self.trees[0 if name != "AGENTS.md" else 1], name, wanted)
                before = tree_bytes(self.target)
                plan = self.plan()
                self.assertTrue(any(c["file"] == name for c in plan["conflicts"]))
                with self.assertRaisesRegex(ValueError, "structural conflicts"):
                    self.install()
                self.assertEqual(tree_bytes(self.target), before)
                path.unlink()
                if name not in ("CLAUDE.md", "AGENTS.md"):
                    stage_path.unlink()

    def test_edited_managed_prose_json_or_script_requires_resolution(self):
        names = {"CLAUDE.md": "Store\n", ".claude/hooks/guard": "#!/bin/sh\nexit 0\n",
                 ".claude/settings.json": '{"deny":["x"]}'}
        for name, text in names.items():
            write(self.trees[0], name, text)
        self.plan()
        self.install()
        for name in names:
            path = self.target / name
            original = path.read_bytes()
            changed = original.replace(b"Store", b"Edited") if name.endswith(".md") else original.replace(b"0", b"1") if "/hooks/" in name else b'{"deny":["edited"]}'
            path.write_bytes(changed)
            plan = self.plan()
            self.assertTrue(any(c["file"] == name for c in plan["conflicts"]), name)
            path.write_bytes(original)

    def test_target_drift_stale_read_missing_go_and_symlinks_fail_before_writes(self):
        self.plan()
        review, approval = self.authorize()
        write(self.target, "nested/AGENTS.override.md", "New precedence\n")
        before = tree_bytes(self.target)
        with self.assertRaisesRegex(ValueError, "changed since review"):
            ADOPT.apply(self.stage, review, approval)
        self.assertEqual(tree_bytes(self.target), before)
        self.plan()
        review, approval = self.authorize()
        data = json.loads(approval.read_bytes())
        data["go"] = False
        dump(approval, data)
        with self.assertRaisesRegex(ValueError, "human go"):
            ADOPT.apply(self.stage, review, approval)
        review, approval = self.authorize()
        review.write_bytes(review.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "changed after ruling"):
            ADOPT.apply(self.stage, review, approval)
        outside = write(self.work, "external", "untouched\n")
        (self.target / "CLAUDE.md").symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.plan()
        self.assertEqual(outside.read_text(), "untouched\n")

    def test_crlf_unmanaged_prose_is_preserved_byte_for_byte(self):
        original = b"# Project\r\n\r\nUse project tools.\r\n"
        (self.target / "CLAUDE.md").write_bytes(original)
        self.plan()
        self.install()
        self.assertTrue((self.target / "CLAUDE.md").read_bytes().startswith(original))
        self.assertFalse(self.plan()["writes"])

    def test_non_directory_parent_refuses_before_installation(self):
        write(self.target, ".claude", "occupied parent\n")
        write(self.trees[0], ".claude/hooks/guard", "#!/bin/sh\nexit 0\n")
        before = tree_bytes(self.target)
        with self.assertRaisesRegex(ValueError, "parent is not a directory"):
            self.plan()
        self.assertEqual(tree_bytes(self.target), before)

    def test_ambiguous_exact_edit_refuses_before_writes(self):
        write(self.target, "CLAUDE.md", "duplicate\nduplicate\n")
        before = tree_bytes(self.target)
        with self.assertRaisesRegex(ValueError, "exactly once"):
            self.plan([{"path": "CLAUDE.md", "before": "duplicate", "after": "new"}])
        self.assertEqual(tree_bytes(self.target), before)

    def mode(self, name):
        return (self.target / name).stat().st_mode & 0o777

    def adopt_upgrade_repeat(self, name, staged_v1, staged_v2):
        """Existing 0600 `name` keeps 0600 through first adoption, upgrade and repeat."""
        path = self.target / name
        path.chmod(0o600)
        write(self.trees[0], name, staged_v1)
        self.plan()
        self.install()
        self.assertEqual(self.mode(name), 0o600, "first adoption")
        self.assertEqual(self.plan()["writes"], {}, "repeat after first adoption")
        write(self.trees[0], name, staged_v2)
        plan = self.plan()
        self.assertIn(name, plan["writes"])
        self.install()
        self.assertEqual(self.mode(name), 0o600, "upgrade")
        self.assertIn("v2", path.read_text())
        self.assertEqual(self.plan()["writes"], {}, "repeat after upgrade")

    def test_existing_0600_json_keeps_mode_through_adoption_upgrade_and_repeat(self):
        write(self.target, ".claude/settings.json", '{"permissions":{"allow":["custom"]}}\n')
        self.adopt_upgrade_repeat(".claude/settings.json",
                                  '{"permissions":{"deny":["v1"]}}', '{"permissions":{"deny":["v2"]}}')

    def test_existing_0600_markdown_keeps_mode_through_adoption_upgrade_and_repeat(self):
        write(self.target, "CLAUDE.md", "# Project\nLocal text.\n")
        self.adopt_upgrade_repeat("CLAUDE.md", "# Store v1\n", "# Store v2\n")

    def test_ownership_manifest_keeps_0600_on_upgrade_and_is_created_0644_on_first_adoption(self):
        manifest = ".claude/fiducial-ownership.json"
        write(self.trees[0], ".claude/skills/one/SKILL.md", "# One\n")
        self.plan()
        self.install()
        self.assertEqual(self.mode(manifest), 0o644, "first adoption creates the manifest 0644")
        (self.target / manifest).chmod(0o600)
        write(self.trees[0], ".claude/skills/two/SKILL.md", "# Two\n")
        plan = self.plan()
        self.assertIn(manifest, plan["writes"], "upgrade rewrites the manifest")
        self.install()
        self.assertEqual(self.mode(manifest), 0o600, "upgrade keeps the manifest mode")

    def test_mode_only_drift_between_plan_and_apply_is_refused_before_any_write(self):
        write(self.target, "CLAUDE.md", "# Project\n")
        self.plan()
        paths = self.authorize()
        (self.target / "CLAUDE.md").chmod(0o600)
        before = tree_bytes(self.target)
        with self.assertRaisesRegex(ValueError, "changed since review"):
            ADOPT.apply(self.stage, *paths)
        self.assertEqual(tree_bytes(self.target), before)

    def test_existing_0600_markdown_edited_by_legacy_edit_keeps_mode(self):
        write(self.target, "CLAUDE.md", "# Project\nobsolete\n").chmod(0o600)
        self.plan([{"path": "CLAUDE.md", "before": "obsolete\n", "after": "current\n"}])
        self.install()
        self.assertIn("current", (self.target / "CLAUDE.md").read_text())
        self.assertEqual(self.mode("CLAUDE.md"), 0o600)

    def test_edit_only_unstaged_0600_file_keeps_mode(self):
        write(self.target, "src/AGENTS.md", "# Nested\nobsolete\n").chmod(0o600)
        self.plan([{"path": "src/AGENTS.md", "before": "obsolete\n", "after": "current\n"}])
        self.install()
        self.assertIn("current", (self.target / "src/AGENTS.md").read_text())
        self.assertEqual(self.mode("src/AGENTS.md"), 0o600)

    def test_retiring_owned_section_from_surviving_0600_file_keeps_mode(self):
        write(self.target, "src/AGENTS.md", "# Local\n")
        write(self.trees[0], "src/AGENTS.md", "# Store nested\n")
        self.plan()
        self.install()
        (self.target / "src/AGENTS.md").chmod(0o600)
        (self.trees[0] / "src/AGENTS.md").unlink()
        plan = self.plan()
        self.assertFalse(plan["conflicts"])
        self.assertIn("src/AGENTS.md", plan["writes"])
        self.install()
        self.assertEqual((self.target / "src/AGENTS.md").read_text(), "# Local\n")
        self.assertEqual(self.mode("src/AGENTS.md"), 0o600)

    def test_created_files_chmodded_by_user_are_not_replanned_or_widened(self):
        write(self.trees[0], ".claude/settings.json", '{"permissions":{"deny":["v1"]}}')
        self.plan()
        self.install()
        for name in ("CLAUDE.md", ".claude/settings.json"):
            self.assertEqual(self.mode(name), 0o644)
            (self.target / name).chmod(0o600)
        self.assertEqual(self.plan()["writes"], {})
        self.assertEqual(self.install(), [])
        for name in ("CLAUDE.md", ".claude/settings.json"):
            self.assertEqual(self.mode(name), 0o600)

    def test_new_staged_hook_lands_executable_with_staged_mode(self):
        write(self.trees[0], ".claude/hooks/guard", "#!/bin/sh\nexit 0\n").chmod(0o755)
        self.plan()
        self.install()
        self.assertEqual(self.mode(".claude/hooks/guard"), 0o755)

    def test_locally_chmodded_owned_script_is_still_refused(self):
        write(self.trees[0], ".claude/hooks/guard", "#!/bin/sh\nexit 0\n").chmod(0o755)
        self.plan()
        self.install()
        (self.target / ".claude/hooks/guard").chmod(0o700)
        plan = self.plan()
        self.assertTrue(any(c["file"] == ".claude/hooks/guard" and
                            "occupied or modified structured file" in c["reason"]
                            for c in plan["conflicts"]))
        with self.assertRaisesRegex(ValueError, "structural conflicts"):
            self.install()
        self.assertEqual(self.mode(".claude/hooks/guard"), 0o700)

    # ---- #412: refuse before the first write ----------------------------
    #
    # Permission bits are not enforced for uid 0, so `run_apply` demotes the
    # adopter to an unprivileged uid when the suite runs as root. The check
    # reads bits and directory types only; it does not see read-only
    # filesystems, ACLs or immutable flags, and these tests do not claim to.

    UNPRIVILEGED = 65534

    def state(self):
        """Bytes and mode of every file plus the set of directories, outside .git."""
        files, dirs = {}, set()
        for base, names, leaves in os.walk(self.target):
            names[:] = [n for n in names if n != ".git"]
            rel = pathlib.Path(base).relative_to(self.target).as_posix()
            if rel != ".":
                dirs.add(rel)
            for leaf in leaves:
                path = pathlib.Path(base) / leaf
                files[path.relative_to(self.target).as_posix()] = (path.read_bytes(),
                                                                  path.lstat().st_mode & 0o777)
        return files, dirs

    @staticmethod
    def restore_permissions(root):
        """Make `root` removable again after a test narrowed directory modes."""
        def fix(path):
            if path.is_symlink():
                return
            if path.is_dir():
                path.chmod(0o755)
                for child in path.iterdir():
                    fix(child)
            else:
                path.chmod(0o644)
        fix(pathlib.Path(root))

    def run_apply(self, review, approval):
        """The documented `apply` CLI, as an unprivileged process when we are root."""
        helper = write(self.work, "adopt-cli.py", FENCES[0])
        extra = {}
        if os.geteuid() == 0:
            self.work.chmod(0o755)  # mkdtemp makes it 0700; the runner must traverse it
            for base, names, leaves in os.walk(self.work):
                for name in names + leaves:
                    os.lchown(os.path.join(base, name), self.UNPRIVILEGED, self.UNPRIVILEGED)
            os.chown(self.work, self.UNPRIVILEGED, self.UNPRIVILEGED)
            extra = {"user": self.UNPRIVILEGED, "group": self.UNPRIVILEGED}
            try:
                probe = subprocess.run([sys.executable, "-I", "-c", "pass"], capture_output=True, **extra)
            except (PermissionError, OSError) as exc:
                self.skipTest("cannot run as an unprivileged uid; permission cases unverified: %s" % exc)
            if probe.returncode:
                self.skipTest("unprivileged uid cannot run the interpreter; permission cases unverified")
        return subprocess.run([sys.executable, str(helper), "apply", str(self.stage), str(review), str(approval)],
                              env=base_env(), text=True, capture_output=True, **extra)

    def assert_apply_refused_untouched(self, expected_state):
        review, approval = self.authorize()
        self.addCleanup(self.restore_permissions, self.work)
        proc = self.run_apply(review, approval)
        self.assertEqual(self.state(), expected_state, "a refused apply must leave the target as it was")
        self.assertNotEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("adopt:", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)

    def stage_one_skill(self):
        write(self.trees[0], ".claude/skills/one/SKILL.md", "# One\n")

    def test_absent_destination_replaced_by_a_directory_is_refused_before_any_write(self):
        write(self.target, "CLAUDE.md", "# Project\n")
        self.stage_one_skill()
        self.plan()
        paths = self.authorize()
        (self.target / "AGENTS.md").mkdir()  # an empty directory is invisible to the inventory
        before = self.state()
        try:
            ADOPT.apply(self.stage, *paths)
            error = None
        except Exception as exc:  # the type is judged after the target is
            error = exc
        self.assertEqual(self.state(), before, "files written before the late failure")
        self.assertIsInstance(error, ValueError, repr(error))

    def test_nested_destination_replaced_by_a_directory_is_refused_before_any_write(self):
        self.stage_one_skill()
        self.plan()
        paths = self.authorize()
        (self.target / ".claude/skills/one/SKILL.md").mkdir(parents=True)
        before = self.state()
        try:
            ADOPT.apply(self.stage, *paths)
            error = None
        except Exception as exc:
            error = exc
        self.assertEqual(self.state(), before, "files written before the late failure")
        self.assertIsInstance(error, ValueError, repr(error))

    def test_content_write_to_a_file_without_write_permission_is_refused_before_any_write(self):
        write(self.target, "CLAUDE.md", "# Project\nLocal text.\n").chmod(0o400)
        self.stage_one_skill()
        self.assertIn("CLAUDE.md", self.plan()["writes"])
        self.assert_apply_refused_untouched(self.state())

    def test_delete_without_parent_permission_is_refused_before_any_write(self):
        for label, parent_mode in (("no write", 0o500), ("no search", 0o600)):
            with self.subTest(parent=label):
                self.setUp()
                self.stage_one_skill()
                self.plan()
                self.install()
                (self.trees[0] / ".claude/skills/one/SKILL.md").unlink()
                self.assertEqual(self.plan()["writes"][".claude/skills/one/SKILL.md"]["text"], None)
                self.addCleanup(self.restore_permissions, self.work)
                (self.target / ".claude/skills/one").chmod(parent_mode)
                self.assert_apply_refused_untouched(self.state())

    def test_create_without_ancestor_permission_is_refused_before_any_write(self):
        for label, ancestor_mode in (("no write", 0o500), ("no search", 0o600)):
            for staged in ("src/AGENTS.md", "src/deep/er/AGENTS.md"):
                with self.subTest(ancestor=label, create=staged):
                    self.setUp()
                    (self.target / "src").mkdir()
                    write(self.trees[0], staged, "# Nested\n")
                    self.assertIn(staged, self.plan()["writes"])
                    self.addCleanup(self.restore_permissions, self.work)
                    (self.target / "src").chmod(ancestor_mode)
                    self.assert_apply_refused_untouched(self.state())

    def test_report_destination_is_covered_by_the_same_preflight(self):
        (self.target / "docs").mkdir()
        self.stage_one_skill()
        plan = self.plan()
        self.assertTrue(plan["writes"])
        self.addCleanup(self.restore_permissions, self.work)
        (self.target / "docs").chmod(0o500)  # the report is the only write that needs it
        self.assert_apply_refused_untouched(self.state())

    def test_report_destination_replaced_by_a_directory_is_refused_before_any_write(self):
        self.stage_one_skill()
        plan = self.plan()
        paths = self.authorize()
        (self.target / ("docs/fiducial-adoption-" + plan["timestamp"] + ".md")).mkdir(parents=True)
        before = self.state()
        with self.assertRaises(ValueError):
            ADOPT.apply(self.stage, *paths)
        self.assertEqual(self.state(), before)

    def test_symlink_replacing_a_planned_destination_after_prepare_is_refused_before_any_write(self):
        self.stage_one_skill()
        self.plan()
        paths = self.authorize()
        outside = write(self.work, "external", "untouched\n")
        (self.target / "AGENTS.md").symlink_to(outside)
        before = self.state()
        with self.assertRaisesRegex(ValueError, "symlink"):
            ADOPT.apply(self.stage, *paths)
        self.assertEqual(self.state(), before)
        self.assertEqual(outside.read_text(), "untouched\n")

    def test_clean_apply_and_repeat_still_behave_for_an_unprivileged_runner(self):
        write(self.target, "CLAUDE.md", "# Project\nLocal text.\n").chmod(0o600)
        self.stage_one_skill()
        self.plan()
        review, approval = self.authorize()
        self.addCleanup(self.restore_permissions, self.work)
        proc = self.run_apply(review, approval)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("CLAUDE.md", json.loads(proc.stdout))
        self.assertEqual(self.mode("CLAUDE.md"), 0o600)
        self.assertIn("Local text.", (self.target / "CLAUDE.md").read_text())
        self.assertTrue((self.target / ".claude/skills/one/SKILL.md").is_file())
        self.assertEqual(len(list((self.target / "docs").glob("fiducial-adoption-*.md"))), 1)
        installed = self.state()
        self.assertEqual(self.plan()["writes"], {}, "repeat is a no-op")
        self.assertEqual(self.install(), [])
        self.assertEqual(self.state(), installed)

    def test_labels_create_missing_only_and_read_back(self):
        metadata = {"human-gate": ("aabbcc", "existing description"), "accepted-risk": ("abcabc", "risk")}
        before = dict(metadata)
        calls = []
        def api(argv, **kwargs):
            calls.append(argv)
            if "POST" in argv:
                name = next(a[5:] for a in argv if a.startswith("name="))
                metadata[name] = ("6e7781", "")
                return subprocess.CompletedProcess(argv, 0, "{}", "")
            return subprocess.CompletedProcess(argv, 0, "\n".join(metadata) + "\n", "")
        ADOPT.labels("owner/repo", run=api)
        self.assertTrue(set(ADOPT.LABELS) <= set(metadata))
        self.assertEqual({name: metadata[name] for name in before}, before)
        count = len([c for c in calls if "POST" in c])
        self.assertEqual(count, 3)
        ADOPT.labels("owner/repo", run=api)
        self.assertEqual(len([c for c in calls if "POST" in c]), count)


if __name__ == "__main__":
    unittest.main()
