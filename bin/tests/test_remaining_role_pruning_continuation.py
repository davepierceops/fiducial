"""Continuation contracts through approved remaining-role ruling81.

Real source and emitter checks, including a preview of the eight removals whose
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
CHECKPOINT = "4157ddd3e1b50ff3b28c31f387e5e9e96793a3a9"
# PR #432 merge commit: the batch as it landed. Finalization compares this
# snapshot, not the working tree, so later approved rules/process changes pass.
LANDED = "5b2a62f3b17aca1d859a43032b9ca2295c185391"
SUCCESSORS = {"R0943": "R0110", "R0950": "R1621", "R1513": "R0166", "R0090": "R0166",
              "R1480": "R1479", "R0954": "R1162", "R1002": "R1162"}
PENDING = set("R0940 R0499 R0284 R1091 R1485 R1249 R0159 R0800".split())
REVISED = set("""R0091 R0264 R0481 R0485 R0500 R0809 R0863 R1031 R1044 R1056
R1088 R1090 R1107 R1116 R1122 R1133 R1143 R1155 R1156 R1620 R1621
R0070 R0106 R0166 R0199 R0259 R0472 R0527 R0583 R0592 R0939 R1162 R1163 R1164
R1165 R1241 R1244 R1270 R1408 R1448 R1473 R1478 R1479 R1605 R1622""".split())
MANIFEST = "docs/plans/remaining-role-pruning-checkpoint-20261108T053045Z.json"
RETRO = {"R1237", "R1241", "R1244", "R1249", "R1270"}
METADATA = {
    "R0199": {"verb": ["require"], "condition": ["recovery could discard work or disrupt an active operation"]},
    "R1478": {"verb": ["require"], "condition": ["editing artifacts assigned to your role"],
              "role": sorted("architect-agent context-quality-reviewer reviewer-agent skeptic-risk-agent spec-reviewer-agent test-designer-agent".split())},
    "R1162": {"topic": ["core"], "role": ["writer", "copy-editor", "critic"]},
    **{row: {"role": ["chief-of-staff", "writer"]} for row in RETRO},
}
METADATA["R1244"]["verb"] = ["require"]
HUMAN_CHANGED = {"R0091", "R1156", "R1622"}


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


class TestRemainingRolePruningContinuation(unittest.TestCase):
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
        # The approved81-ruling checkpoint remains an immutable oracle.
        # Finalization is checked against its removal preview below.
        cls.checkpoint_root = cls.baseline / "checkpoint"
        cls.checkpoint_root.mkdir()
        archive = subprocess.run(["git", "archive", CHECKPOINT, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(cls.checkpoint_root, filter="data")
        cls.current = inputs(cls.checkpoint_root)
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
        manifest = json.loads((REPO_ROOT / MANIFEST).read_text())
        self.assertEqual(manifest["baseline"], BASELINE)
        self.assertEqual(manifest["ruling_count"], 81)
        self.assertEqual(len(manifest["reviewed_rows"]), 86)
        self.assertEqual(set(manifest["rewritten"]), REVISED)
        self.assertEqual(manifest["successors"], SUCCESSORS)
        self.assertEqual(set(manifest["pending_retirement_without_replacement"]), PENDING)
        self.assertIsNone(manifest["retirement_decision"])
        self.assertEqual(set(manifest["reviewed_rows"]), REVISED | set(SUCCESSORS) | PENDING | set(manifest["kept"]) | set(METADATA))
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
            expected_keys = self.old_rows[row_id].keys.copy()
            expected_keys.update(METADATA.get(row_id, {}))
            self.assertEqual(row.keys, expected_keys, row_id)
            if row_id in HUMAN_CHANGED:
                self.assertIn("R1478 supplies the shared editing and finding instruction", row.human)
                self.assertIn("DEC-001240", row.human)
            else:
                self.assertEqual(row.human, self.old_rows[row_id].human, row_id)
            self.assertEqual(blocks.parse(row.body)[0], blocks.parse(self.old_rows[row_id].body)[0], row_id)
        old_processes = {r.id: r for r in self.old.rows if r.kind == "process"}
        current_processes = {r.id: r for r in self.current.rows if r.kind == "process"}
        self.assertEqual(set(old_processes), set(current_processes))
        for name, row in current_processes.items():
            old = old_processes[name]
            self.assertEqual(row.keys, old.keys, name)
            expected = old.body
            if name == "intake":
                expected = expected.replace("[R0264, R0266, R0284, R0950]", "[R0264, R0266, R0284, R1621]")
            elif name in ("build", "spec-template"):
                expected = expected.replace("[R1513]", "[R0166]")
            elif name == "retro":
                expected = expected.replace("## Standing preferences\n<preferences the human stated this session that he has stated in earlier\nsessions too, each as a candidate standing rule and each naming where it\nwas stated before; empty-with-a-statement if none>", "## Recurring preferences\n<preferences the human stated in this and earlier sessions, with evidence\nof where they were expressed; empty-with-a-statement if none>")
                expected = expected.replace("## Candidate methodology changes\n<specific proposed edits to methodology documents, if any, phrased as\nfindings for the delta that would carry them — not as decisions>", "## Questions for follow-up\n<problems worth investigating, with supporting evidence and unresolved\nquestions; empty-with-a-statement if none>")
            self.assertEqual(row.body, expected, name)

    def test_successor_archives_are_exact_and_pending_retirements_remain_original(self):
        for row_id, successor in SUCCESSORS.items():
            archived = (REPO_ROOT / "rules/retired" / (row_id + ".md")).read_text()
            original = (self.baseline / "rules" / (row_id + ".md")).read_text()
            self.assertEqual(archived.replace("retired: " + successor + "\n", "", 1), original, row_id)
            for axis in ("role", "session", "corpus"):
                self.assertTrue(set(self.old_rows[row_id].keys[axis]) <= set(self.rows[successor].keys[axis]))
        for row_id in PENDING:
            self.assertFalse((self.checkpoint_root / "rules/retired" / (row_id + ".md")).exists(), row_id)
            original = (self.baseline / "rules" / (row_id + ".md")).read_text()
            if row_id == "R1249":
                original = original.replace("role: [chief-of-staff, writer, copy-editor, critic]",
                                            "role: [chief-of-staff, writer]")
            self.assertEqual((self.checkpoint_root / "rules" / (row_id + ".md")).read_text(), original, row_id)

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

    def test_root_changes_only_as_approved_and_hooks_remain_exact(self):
        for h, before in self.native["before"].items():
            root = "CLAUDE.md" if h == "claude-code" else "AGENTS.md"
            hook_paths = {p for p in before.files if "/hooks/" in p or p.endswith(("settings.json", "hooks.json"))}
            self.assertTrue(hook_paths)
            for version in ("actual", "preview"):
                after = self.native[version][h]
                expected_root = before.files[root].replace(self.old_rows["R0166"].body, self.rows["R0166"].body)
                expected_root = expected_root.replace(self.old_rows["R1513"].body + "\n\n", "")
                self.assertEqual(after.files[root], expected_root, (version, h))
                self.assertEqual(after.executable, before.executable, (version, h))
                for path in hook_paths:
                    self.assertEqual(after.files[path], before.files[path], (version, h, path))


    def test_shared_editing_duties_and_retro_scope_reach_only_approved_audiences(self):
        editing = self.rows["R1478"].body
        for row_id in HUMAN_CHANGED:
            self.assertEqual(blocks.parse(self.rows[row_id].body)[1], "", row_id)
        for role in METADATA["R1478"]["role"]:
            for corpus in ("software", "writing"):
                text = next(iter(targets()["bundle"].emit(dataclasses.replace(self.preview,
                    where={"role": role, "corpus": corpus, "session": "execution"})).files.values()))
                self.assertIn(editing, text, (role, corpus))
        for row_id in RETRO:
            self.assertEqual(self.rows[row_id].keys["role"], ["chief-of-staff", "writer"])
        for role in ("copy-editor", "critic"):
            text = self.bundles[role]
            for row_id in RETRO:
                self.assertNotIn(self.rows[row_id].body, text, (role, row_id))
        for h, emission in self.native["preview"].items():
            prefix = ".claude" if h == "claude-code" else ".agents"
            retro = emission.files[prefix + "/skills/retro/SKILL.md"]
            self.assertIn("## Recurring preferences", retro)
            self.assertIn("## Questions for follow-up", retro)
            self.assertNotIn("## Candidate methodology changes", retro)
            self.assertNotIn(self.old_rows["R1249"].body, retro)


class TestRemainingRolePruningFinalization(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Reuse the historical source and independently emit the live tree.
        TestRemainingRolePruningContinuation.setUpClass.__func__(cls)
        cls.landed_root = cls.baseline / "landed"
        cls.landed_root.mkdir()
        archive = subprocess.run(["git", "archive", LANDED, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(cls.landed_root, filter="data")
        cls.live = inputs(cls.landed_root)

    def test_final_archives_and_sources_match_the_approved_preview(self):
        decision = "DEC-001720"
        self.assertIn("## " + decision + " —", (REPO_ROOT / "decisions/log.md").read_text())
        for row_id in PENDING:
            self.assertFalse((REPO_ROOT / "rules" / (row_id + ".md")).exists(), row_id)
            original = (self.checkpoint_root / "rules" / (row_id + ".md")).read_text()
            archived = (REPO_ROOT / "rules/retired" / (row_id + ".md")).read_text()
            self.assertEqual(archived, original.replace("---\n", "---\nretired: " + decision + "\n", 1), row_id)
        def records(source):
            return {(r.kind, r.id): (r.body, r.keys, r.human, r.order) for r in source.rows}
        # This also guards every deferred Writer/Copy Editor/Critic row:
        # finalization may remove approved rows, not continue policy choices.
        self.assertEqual(records(self.live), records(self.preview))
        self.assertEqual({r.id for r in self.live.rows if r.kind == "rule"},
                         set(self.old_rows) - PENDING - set(SUCCESSORS))

    def test_live_native_and_all_bundles_equal_preview_with_hooks_unchanged(self):
        for harness in ("claude-code", "codex"):
            actual = targets()[harness].emit(self.live)
            expected = self.native["preview"][harness]
            self.assertEqual(actual.files, expected.files, harness)
            self.assertEqual(actual.executable, expected.executable, harness)
            baseline = self.native["before"][harness]
            self.assertEqual(actual.executable, baseline.executable, harness)
            for path, body in baseline.files.items():
                if "/hooks/" in path or path.endswith(("settings.json", "hooks.json")):
                    self.assertEqual(actual.files[path], body, (harness, path))
        names = named_queries.bundles(FileRowSource(self.landed_root).named_queries_text())
        self.assertEqual(len(names), 12)
        for name, tokens in names:
            where = dict(token.split("=", 1) for token in tokens)
            actual = next(iter(targets()["bundle"].emit(dataclasses.replace(
                self.live, where=where, name=name)).files.values()))
            self.assertEqual(actual, self.bundles[name], name)


if __name__ == "__main__":
    unittest.main()
