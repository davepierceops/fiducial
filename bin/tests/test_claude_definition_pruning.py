"""Local source/output contracts for the approved definition-pruning batch.

The Git baseline must already exist locally. These checks exercise the real
store and emitters, including every named standalone bundle; they do not prove
native loading, agent adherence, live tracker access or installation state.
"""
from __future__ import annotations

import dataclasses
import io
import json
import pathlib
import subprocess
import tarfile
import tempfile
import unittest

from rulestore import named_queries, query
from rulestore.emit import targets
from rulestore.store import FileRowSource
from tests.helpers import REPO_ROOT
from tests.test_skill_context_extraction import inputs

BASELINE = "cb0194aee512f48f3046e5ba9be445d85f97fbd3"
LANDED = "1df9a4ec813e5cec756665123d8a5298c7597cef"
RETIRED = set("R0108 R1200 R0497 R0173 R0027 R0028 R0208 R0043 R0055 R0611 R0760 R0761 R1601 R1625".split())
REVISED = {"R0535", "R0780", "R0045", "R0166"}
ROOT_DEFINITIONS = {"R0535", "R0780", "R0045", "R0064"}


class TestClaudeDefinitionPruning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="fiducial-definition-contract-")
        cls.addClassCleanup(cls.tmp.cleanup)
        cls.baseline = pathlib.Path(cls.tmp.name)
        archive = subprocess.run(["git", "archive", BASELINE, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(cls.baseline, filter="data")
        cls.old = inputs(cls.baseline)
        landed = cls.baseline / "landed"
        landed.mkdir()
        archive = subprocess.run(["git", "archive", LANDED, "rules", "process", "bin/hooks"],
                                 cwd=REPO_ROOT, check=True, capture_output=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive)) as stream:
            stream.extractall(landed, filter="data")
        cls.landed_rows = {r.id: r for r in inputs(landed).rows if r.kind == "rule"}
        cls.current = inputs(REPO_ROOT)
        cls.old_rows = {r.id: r for r in cls.old.rows if r.kind == "rule"}
        cls.rows = {r.id: r for r in cls.current.rows if r.kind == "rule"}
        cls.processes = {r.id: r for r in cls.current.rows if r.kind == "process"}
        cls.native = {name: targets()[name].emit(cls.current)
                      for name in ("claude-code", "codex")}
        cls.bundles = {}
        for name, tokens in named_queries.bundles(FileRowSource(REPO_ROOT).named_queries_text()):
            where = dict(token.split("=", 1) for token in tokens)
            cls.bundles[name] = next(iter(targets()["bundle"].emit(
                dataclasses.replace(cls.current, where=where, name=name)).files.values()))

    def test_only_approved_rows_change_and_archives_preserve_original_records(self):
        manifest = json.loads((REPO_ROOT / "docs/plans/claude-definition-pruning-finalization-20261106.json").read_text())
        self.assertEqual(manifest["baseline"], BASELINE)
        self.assertEqual(set(manifest["retired"]), RETIRED)
        self.assertEqual(manifest["moved_to_skill"], {"R0208": "command-blocks"})
        self.assertEqual(set(manifest["shortened"] + manifest["revised"]), REVISED)
        self.assertEqual(manifest["pending"], ["R0064"])
        # Preserve PR #426's exact approved delta without prohibiting later
        # approved changes. Archive and output guards below remain live.
        self.assertEqual(set(self.old_rows) - set(self.landed_rows), RETIRED)
        self.assertEqual(set(self.landed_rows) - set(self.old_rows), set())
        changed = {r for r in self.landed_rows if self.landed_rows[r].body != self.old_rows[r].body}
        self.assertEqual(changed, REVISED)
        for row_id in self.landed_rows:
            self.assertEqual(self.landed_rows[row_id].keys, self.old_rows[row_id].keys, row_id)
        decision = manifest["retirement_decision"]
        self.assertRegex(decision, r"^DEC-\d{6}$")
        self.assertIn("## " + decision + " —", (REPO_ROOT / "decisions/log.md").read_text())
        for row_id in RETIRED:
            with self.subTest(row=row_id):
                self.assertFalse((REPO_ROOT / "rules" / (row_id + ".md")).exists())
                original = (self.baseline / "rules" / (row_id + ".md")).read_text()
                archived = (REPO_ROOT / "rules/retired" / (row_id + ".md")).read_text()
                self.assertEqual(archived.replace("retired: " + decision + "\n", "", 1), original)
        # The one citation of the retired deploy definition must not dangle.
        self.assertNotIn("[R0497]", self.processes["spec-template"].body)

    def test_retired_definitions_do_not_reappear_in_native_or_standalone_context(self):
        outputs = {f"{harness}/{path}": text for harness, emission in self.native.items()
                   for path, text in emission.files.items()}
        outputs.update({"bundle/" + name: text for name, text in self.bundles.items()})
        self.assertTrue(self.bundles)
        for path, text in outputs.items():
            for row_id in RETIRED:
                with self.subTest(path=path, row=row_id):
                    self.assertNotIn(self.old_rows[row_id].body, text)
        for harness, emission in self.native.items():
            root = emission.files["CLAUDE.md" if harness == "claude-code" else "AGENTS.md"]
            for row_id in ROOT_DEFINITIONS:
                self.assertIn(self.rows[row_id].body, root, (harness, row_id))
            # Skills must still be selected by the standing invocation rules.
            for row_id in ("R1626", "R1627"):
                self.assertEqual(self.rows[row_id].body, self.old_rows[row_id].body)
                self.assertIn(self.rows[row_id].body, root)

    def test_paste_block_guidance_is_in_the_skill_not_standing_agent_context(self):
        paragraph, = [p for p in self.processes["command-blocks"].body.split("\n\n")
                      if p.startswith("A paste block is copied whole")]
        self.assertIn("without assembly", paragraph)
        self.assertIn("There are two kinds.", paragraph)
        for harness, emission in self.native.items():
            prefix = ".claude" if harness == "claude-code" else ".agents"
            self.assertIn(paragraph, emission.files[prefix + "/skills/command-blocks/SKILL.md"])
            for path, text in emission.files.items():
                if path in ("CLAUDE.md", "AGENTS.md") or "/agents/" in path:
                    self.assertNotIn(paragraph, text, (harness, path))
        # Every standalone audience that actually selects this process receives
        # the paragraph; other audiences do not acquire the procedure by accident.
        for name, tokens in named_queries.bundles(FileRowSource(REPO_ROOT).named_queries_text()):
            where = dict(token.split("=", 1) for token in tokens)
            selected = query.select(self.current.rows, where, self.current.sequences)
            expected = any(r.kind == "process" and r.id == "command-blocks" for r in selected)
            self.assertEqual(paragraph in self.bundles[name], expected, name)


if __name__ == "__main__":
    unittest.main()
