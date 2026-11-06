"""Real-store contract checks for the approved procedure extraction.

Boundary: contract-verified local source and emitted bytes only. No mocks,
installed harness, live skill invocation, native hook enforcement, or user
adherence are exercised. The approved baseline supplies the unchanged-security
oracle; archived records supply the moved instruction bodies after extraction.
Prerequisite: local Git history must contain the approved BASELINE object. A
shallow clone or source archive without that object cannot run these tests;
no remote fetch or network access is performed by the test.
"""
from __future__ import annotations

import dataclasses
import io
import pathlib
import re
import subprocess
import tarfile
import tempfile
import tomllib
import unittest

from rulestore import named_queries, terms
from rulestore.emit import EmitInputs, load_tiers, targets
from rulestore.store import FileRowSource
from tests.helpers import REPO_ROOT

BASELINE = "5ff8a5edc63111637b1bd9a5c1e605e76afbea69"
EXTRACTED = "fb310dd9c1ea56e4fa2e1b9b671a50c128fdec0f"
COMMAND = "R1196 R1199 R1202 R1205 R1206 R1208 R1212 R1213 R1215 R1218 R1609 R1623 R1624".split()
VERIFY_SIX = "R0140 R0141 R0144 R0145 R0147 R0148 R0074".split()
VERIFY_EIGHT = "R0784 R0789 R0798 R0799 R0802 R0803 R0804".split()
GROUPS = {"command-blocks": COMMAND, "verification-checklists": VERIFY_SIX + VERIFY_EIGHT}


def inputs(root):
    source = FileRowSource(root)
    return EmitInputs(rows=source.rows(),
                      sequences=named_queries.sequences(source.named_queries_text()),
                      tiers=load_tiers(), repo="test/fiducial", head=BASELINE,
                      generated="20261105T000000Z",
                      hooks={p.name: p.read_text() for p in (root / "bin/hooks").glob("*") if p.is_file()})


class TestSkillContextExtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="fiducial-extraction-contract-")
        cls.addClassCleanup(cls.tmp.cleanup)
        baseline = pathlib.Path(cls.tmp.name)
        archive = subprocess.run(["git", "archive", BASELINE, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(baseline, filter="data")
        cls.old = inputs(baseline)
        extracted = baseline / "extracted"
        extracted.mkdir()
        archive = subprocess.run(["git", "archive", EXTRACTED, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(extracted, filter="data")
        cls.extracted_rows = {r.id: r for r in inputs(extracted).rows if r.kind == "rule"}
        cls.current = inputs(REPO_ROOT)
        cls.old_rows = {r.id: r for r in cls.old.rows if r.kind == "rule"}
        cls.rows = {r.id: r for r in cls.current.rows if r.kind == "rule"}
        cls.procedures = {r.id: r for r in cls.current.rows if r.kind == "process"}
        cls.emitted = {name: targets()[name].emit(cls.current) for name in ("claude-code", "codex")}
        cls.old_emitted = {name: targets()[name].emit(cls.old) for name in cls.emitted}
        cls.bundles = {}
        for role, tokens in named_queries.bundles(FileRowSource(REPO_ROOT).named_queries_text()):
            where = dict(token.split("=", 1) for token in tokens)
            cls.bundles[role] = next(iter(targets()["bundle"].emit(
                dataclasses.replace(cls.current, where=where, name=role)).files.values()))

    def record(self, row_id):
        source = FileRowSource(REPO_ROOT)
        path = REPO_ROOT / "rules/retired" / (row_id + ".md")
        self.assertTrue(path.is_file(), row_id + " must be archived")
        return source._row(path, "rule")

    def test_only_authorized_rows_leave_the_live_store_and_archive_keeps_original_bodies(self):
        moved = set(COMMAND + VERIFY_SIX + VERIFY_EIGHT)
        # DEC-001680 authorized this exact extraction. Later approved pruning
        # may retire additional rows; it must not rewrite that historical check.
        self.assertEqual(set(self.old_rows) - set(self.extracted_rows), moved | {"R0456"})
        self.assertTrue(moved.isdisjoint(self.rows))
        for skill, ids in GROUPS.items():
            targets_seen = set()
            for row_id in ids:
                with self.subTest(row=row_id):
                    archived = self.record(row_id)
                    self.assertEqual(archived.body, self.old_rows[row_id].body)
                    for key in ("role", "session", "corpus", "condition"):
                        self.assertEqual(archived.keys.get(key), self.old_rows[row_id].keys.get(key))
                    replacement = archived.keys.get("retired")
                    self.assertTrue(replacement, row_id)
                    targets_seen.update(replacement)
            self.assertEqual(len(targets_seen), 1, skill)
            trigger = self.rows[next(iter(targets_seen)).upper()]
            self.assertIn(skill, trigger.body)
            self.assertNotEqual(trigger.keys.get("topic", [None])[0], skill)
            for key in ("role", "session", "corpus"):
                union = set().union(*(set(self.old_rows[r].keys.get(key) or []) for r in ids))
                if skill == "verification-checklists":
                    # Later approved release labels extend the trigger while
                    # retaining every recipient of the original extraction.
                    union |= set(self.extracted_rows["R0030"].keys.get(key) or [])
                self.assertEqual(set(trigger.keys.get(key) or []), union, (skill, key))
        duplicate = self.record("R0456")
        self.assertEqual(duplicate.keys.get("retired"), ["r0021"])
        self.assertEqual(self.extracted_rows["R0021"].body, self.old_rows["R0021"].body)

    def test_exact_bodies_survive_in_both_skills_but_leave_every_root_and_agent(self):
        for harness, emission in self.emitted.items():
            prefix = ".claude" if harness == "claude-code" else ".agents"
            roots_and_agents = {p: text for p, text in emission.files.items()
                                if p in ("CLAUDE.md", "AGENTS.md") or "/agents/" in p}
            self.assertTrue(roots_and_agents)
            root = emission.files["CLAUDE.md" if harness == "claude-code" else "AGENTS.md"]
            for skill in GROUPS:
                self.assertIn(skill, root, harness)
            for skill, ids in GROUPS.items():
                skill_path = prefix + "/skills/" + skill + "/SKILL.md"
                self.assertIn(skill_path, list(emission.files))
                for row_id in ids:
                    body = self.record(row_id).body
                    self.assertIn(body, self.procedures[skill].body, row_id)
                    self.assertIn(body, emission.files[skill_path], row_id)
                    for path, text in roots_and_agents.items():
                        self.assertNotIn(body, text, (row_id, path))
            for path, text in roots_and_agents.items():
                self.assertNotIn(self.old_rows["R0456"].body, text, path)
            for role in load_tiers()["roles"]:
                suffix = ".md" if harness == "claude-code" else ".toml"
                path = (".claude" if harness == "claude-code" else ".codex") + "/agents/" + role + suffix
                text = emission.files[path]
                if suffix == ".md":
                    front = text.split("---", 2)[1]
                    self.assertNotRegex(front, r"(?m)^skills:.*(?:command-blocks|verification-checklists)")
                else:
                    text = tomllib.loads(text)["developer_instructions"]
                if role in self.old_rows["R0784"].keys["role"]:
                    self.assertIn("verification-checklists", root + text, path)

    def test_standalone_role_bundles_keep_applicable_procedures(self):
        self.assertEqual(len(self.bundles), 12)
        for role, text in self.bundles.items():
            for skill, ids in GROUPS.items():
                applicable = any(role in self.old_rows[r].keys["role"] for r in ids)
                if applicable:
                    for row_id in ids:
                        self.assertIn(self.record(row_id).body, text, (role, row_id))
                    self.assertIn(skill, text, role)
                elif skill != "verification-checklists":
                    for row_id in ids:
                        self.assertNotIn(self.old_rows[row_id].body, text, (role, row_id))
                elif self.old_rows[ids[0]].body in text:
                    # Later release-impact moves make this skill available to
                    # all roles. Availability does not broaden the old sections:
                    # their explicit role scopes remain checked below.
                    self.assertIn("Sections apply to software unless they explicitly include writing", text)
                self.assertNotIn(self.old_rows["R0456"].body, text, role)

    def test_verification_sections_explicitly_preserve_the_two_role_scopes(self):
        self.assertIn("verification-checklists", list(self.procedures))
        text = self.procedures["verification-checklists"].body
        # Each section must state its scope before its first obligation. A
        # shared broad introduction cannot silently widen the first group.
        for ids in (VERIFY_SIX, VERIFY_EIGHT):
            positions = [text.index(self.old_rows[r].body) for r in ids]
            first = min(positions)
            previous = max([text.index(self.old_rows[r].body) + len(self.old_rows[r].body)
                            for r in VERIFY_SIX + VERIFY_EIGHT
                            if text.index(self.old_rows[r].body) < first] or [0])
            headings = list(re.finditer(r"(?m)^#{2,6} .+$", text[:first]))
            section = headings[-1].start() if headings else 0
            scope = text[max(previous, section):first]
            expected = set(self.old_rows[ids[0]].keys["role"])
            for role in expected:
                self.assertIn(role, scope)
            if ids == VERIFY_SIX:
                for role in ("architect-agent", "spec-reviewer-agent"):
                    self.assertNotIn(role, scope)

    def test_required_definitions_are_available_with_each_generated_skill(self):
        for harness, emission in self.emitted.items():
            root = emission.files["CLAUDE.md" if harness == "claude-code" else "AGENTS.md"]
            prefix = ".claude" if harness == "claude-code" else ".agents"
            for skill in GROUPS:
                self.assertIn(skill, list(self.procedures))
                available = root + emission.files[prefix + "/skills/" + skill + "/SKILL.md"]
                for definition in terms.pull_definitions([self.procedures[skill]], self.current.rows):
                    self.assertIn(definition.body, available, (harness, skill, definition.id))

    def test_security_outputs_and_executable_modes_do_not_change(self):
        for harness, emission in self.emitted.items():
            old = self.old_emitted[harness]
            paths = {p for p in old.files if "/hooks/" in p or p.endswith(("settings.json", "hooks.json"))}
            self.assertTrue(paths)
            for path in paths:
                self.assertEqual(emission.files.get(path), old.files[path], (harness, path))
            self.assertEqual(emission.executable, old.executable)

    def test_new_skill_references_do_not_require_absent_source_process_paths(self):
        for harness, emission in self.emitted.items():
            for skill in GROUPS:
                prefix = ".claude" if harness == "claude-code" else ".agents"
                path = prefix + "/skills/" + skill + "/SKILL.md"
                self.assertIn(path, list(emission.files))
                for dependency in re.findall(r"(?<![\w/])process/[a-z0-9-]+\.md", emission.files[path]):
                    self.assertIn(dependency, emission.files, (path, dependency))


if __name__ == "__main__":
    unittest.main()
