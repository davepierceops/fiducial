"""Checkpoint contracts for the 44 approved remaining-role rulings.

Real source and emitter checks, including a preview of the five removals whose
retirement decision is allocated only at merge. The preview is not installed
context, an archive record, or evidence of native agent/hook behavior.
"""
from __future__ import annotations

import dataclasses
import io
import json
import pathlib
import re
import subprocess
import tarfile
import tempfile
import unittest

from rulestore import named_queries
from rulestore.emit import blocks, targets
from rulestore.store import FileRowSource
from tests.helpers import REPO_ROOT
from tests.test_skill_context_extraction import inputs

BASELINE = "2be5327e9704b0066eed7e8ef44302aa55179b18"
SUCCESSORS = {"R0943": "R0110", "R0950": "R1621"}
PENDING = set("R0940 R0499 R0284 R1091 R1485".split())
REVISED = set("""R0091 R0264 R0481 R0485 R0500 R0809 R0863 R1031 R1044 R1056
R1088 R1090 R1107 R1116 R1122 R1133 R1143 R1155 R1156 R1620 R1621""".split())


def checkpoint_preview(current):
    """Apply only the approved pending live removals, without inventing DEC IDs."""
    rows = []
    for row in current.rows:
        if row.kind == "rule" and row.id in PENDING:
            continue
        if row.kind == "process" and row.id == "intake":
            row = dataclasses.replace(row, body=row.body.replace(
                "[R0264, R0266, R0284, R1621]", "[R0264, R0266, R1621]"))
        rows.append(row)
    return dataclasses.replace(current, rows=rows)


class TestRemainingRolePruning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="fiducial-role-checkpoint-")
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.baseline = pathlib.Path(cls.tmp.name)
        archive = subprocess.run(["git", "archive", BASELINE, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(cls.baseline, filter="data")
        cls.old = inputs(cls.baseline)
        cls.current = inputs(REPO_ROOT)
        cls.preview = checkpoint_preview(cls.current)
        cls.old_rows = {r.id: r for r in cls.old.rows if r.kind == "rule"}
        cls.rows = {r.id: r for r in cls.current.rows if r.kind == "rule"}
        cls.native = {version: {h: targets()[h].emit(source) for h in ("claude-code", "codex")}
                      for version, source in (("before", cls.old), ("actual", cls.current),
                                              ("preview", cls.preview))}
        cls.bundles = {}
        for name, tokens in named_queries.bundles(FileRowSource(REPO_ROOT).named_queries_text()):
            where = dict(token.split("=", 1) for token in tokens)
            cls.bundles[name] = next(iter(targets()["bundle"].emit(
                dataclasses.replace(cls.preview, where=where, name=name)).files.values()))

    def test_manifest_matches_rulings_and_keeps_definition_rows_eligible(self):
        manifest = json.loads((REPO_ROOT / "docs/plans/remaining-role-pruning-checkpoint.json").read_text())
        self.assertEqual(manifest["baseline"], BASELINE)
        self.assertEqual(manifest["ruling_count"], 44)
        self.assertEqual(len(manifest["reviewed_rows"]), 45)
        self.assertEqual(set(manifest["rewritten"]), REVISED)
        self.assertEqual(manifest["successors"], SUCCESSORS)
        self.assertEqual(set(manifest["pending_retirement_without_replacement"]), PENDING)
        self.assertIsNone(manifest["retirement_decision"])
        self.assertEqual(set(manifest["reviewed_rows"]), REVISED | set(SUCCESSORS) | PENDING | set(manifest["kept"]))
        self.assertEqual(set(manifest["expected_bodies"]), REVISED)
        for row_id, body in manifest["expected_bodies"].items():
            self.assertEqual(self.rows[row_id].body, body, row_id)
        rubric = self.rows["R0264"].body
        self.assertEqual(len(re.findall(r"(?m)^- ", rubric)), 12)
        # A definition must be able to satisfy the uniqueness criterion;
        # requiring every row to add an obligation would contradict this.
        self.assertIn("Add something absent from its existing bundles.", rubric)
        self.assertIn("State an obligation or define a needed term", rubric)
        self.assertNotIn("Add an obligation", rubric)

    def test_only_approved_source_changes_and_all_selectors_and_bindings_survive(self):
        self.assertEqual(set(self.old_rows) - set(self.rows), set(SUCCESSORS))
        self.assertEqual(set(self.rows) - set(self.old_rows), set())
        self.assertEqual({r for r in self.rows if self.rows[r].body != self.old_rows[r].body}, REVISED)
        for row_id, row in self.rows.items():
            self.assertEqual(row.keys, self.old_rows[row_id].keys, row_id)
            self.assertEqual(row.human, self.old_rows[row_id].human, row_id)
            self.assertEqual(blocks.parse(row.body)[0], blocks.parse(self.old_rows[row_id].body)[0], row_id)
        old_processes = {r.id: r for r in self.old.rows if r.kind == "process"}
        current_processes = {r.id: r for r in self.current.rows if r.kind == "process"}
        self.assertEqual(set(old_processes), set(current_processes))
        for name, row in current_processes.items():
            old = old_processes[name]
            self.assertEqual(row.keys, old.keys, name)
            expected = old.body.replace("[R0264, R0266, R0284, R0950]",
                                        "[R0264, R0266, R0284, R1621]") if name == "intake" else old.body
            self.assertEqual(row.body, expected, name)

    def test_successor_archives_are_exact_and_pending_retirements_remain_original(self):
        for row_id, successor in SUCCESSORS.items():
            archived = (REPO_ROOT / "rules/retired" / (row_id + ".md")).read_text()
            original = (self.baseline / "rules" / (row_id + ".md")).read_text()
            self.assertEqual(archived.replace("retired: " + successor + "\n", "", 1), original, row_id)
            for axis in ("role", "session", "corpus"):
                self.assertTrue(set(self.old_rows[row_id].keys[axis]) <= set(self.rows[successor].keys[axis]))
        for row_id in PENDING:
            self.assertFalse((REPO_ROOT / "rules/retired" / (row_id + ".md")).exists(), row_id)
            self.assertEqual((REPO_ROOT / "rules" / (row_id + ".md")).read_bytes(),
                             (self.baseline / "rules" / (row_id + ".md")).read_bytes(), row_id)

    def test_preview_removes_approved_prose_and_resolves_active_citations(self):
        actual_ids = {r.id for r in self.current.rows if r.kind == "rule"}
        preview_ids = {r.id for r in self.preview.rows if r.kind == "rule"}
        self.assertEqual(actual_ids - preview_ids, PENDING)
        self.assertEqual(len(self.bundles), 12)
        outputs = {f"{h}/{path}": text for h, emission in self.native["preview"].items()
                   for path, text in emission.files.items()}
        outputs.update({"bundle/" + name: text for name, text in self.bundles.items()})
        for path, text in outputs.items():
            for row_id in PENDING | set(SUCCESSORS):
                self.assertNotIn(self.old_rows[row_id].body, text, (path, row_id))
        for row in self.preview.rows:
            for citation in re.findall(r"\[([^\]\n]+)\]", row.body):
                for row_id in re.findall(r"\bR\d{4}[a-z]?\b", citation):
                    self.assertNotIn(row_id, PENDING | set(SUCCESSORS), (row.id, row_id))

    def test_root_context_and_hooks_are_unchanged_in_actual_and_preview_outputs(self):
        for h, before in self.native["before"].items():
            root = "CLAUDE.md" if h == "claude-code" else "AGENTS.md"
            hook_paths = {p for p in before.files if "/hooks/" in p or p.endswith(("settings.json", "hooks.json"))}
            self.assertTrue(hook_paths)
            for version in ("actual", "preview"):
                after = self.native[version][h]
                self.assertEqual(after.files[root], before.files[root], (version, h))
                self.assertEqual(after.executable, before.executable, (version, h))
                for path in hook_paths:
                    self.assertEqual(after.files[path], before.files[path], (version, h, path))


if __name__ == "__main__":
    unittest.main()
