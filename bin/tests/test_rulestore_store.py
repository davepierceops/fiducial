"""AC-RS-1/4/14/15: `FileRowSource` against a real repository on disk.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`. DEC-000410
puts filesystem traversal, filename conventions, frontmatter parsing and file
I/O inside the storage layer; this module is the only one in the rule-store
suite that exercises that layer, and `bin/tests/test_rulestore_boundary.py`
asserts nothing else is allowed to.

The fixture store is `bin/tests/helpers.py:rs_store_files` — three rules, one
definition (`term`, no `role`), one `process/` document, one retired row —
committed into a real git repository, because the blob SHA the bundle header
carries is a git object and cannot be mocked into existence.
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
import unittest

from rulestore import named_queries
from rulestore.store import FileRowSource, RowShapeError
from tests.helpers import (
    REPO_ROOT,
    base_env,
    git,
    make_store_repo,
    rs_process,
    rs_row,
    rs_store_files,
    temp_dir,
)


def by_id(rows):
    return {r.id: r for r in rows}


class FileRowSourceTestCase(unittest.TestCase):
    def setUp(self):
        self.origin, self.clone = make_store_repo(self)
        self.rows = FileRowSource(self.clone).rows()


class TestFileRowSource(FileRowSourceTestCase):
    """AC-RS-1: what the storage layer returns, and what it leaves out."""

    def test_ac_rs_1_every_rule_and_process_document_is_returned(self):
        """AC-RS-1: every `rules/*.md` and every `process/*.md` becomes a row."""
        self.assertEqual(
            sorted(r.path for r in self.rows),
            ["process/change-flow.md", "process/named-queries.md",
             "rules/R0001.md", "rules/R0002.md", "rules/R0003.md", "rules/R0100.md"],
        )

    def test_ac_rs_1_nothing_under_rules_retired_is_returned(self):
        """AC-RS-1: "nothing under `rules/retired/` is returned"."""
        self.assertNotIn("R0900", by_id(self.rows))
        self.assertNotIn("rules/retired/R0900.md", [r.path for r in self.rows])

    def test_ac_rs_15_kinds_name_the_two_roots(self):
        """AC-RS-15 (DEC-000490): `rules/` rows are "rule", `process/` "process"."""
        kinds = {r.path: r.kind for r in self.rows}
        self.assertEqual(kinds["rules/R0001.md"], "rule")
        self.assertEqual(kinds["process/change-flow.md"], "process")

    def test_ac_rs_1_a_rows_blob_is_its_git_blob_at_head(self):
        """AC-RS-1/AC-RS-6: the header's blob is the file's git object at HEAD."""
        env = base_env()
        observed, expected = {}, {}
        for relpath in ("rules/R0001.md", "process/change-flow.md"):
            expected[relpath] = git(self.clone, "rev-parse", "HEAD:%s" % relpath,
                                    env=env, check=True)[1].strip()
            observed[relpath] = next(r for r in self.rows if r.path == relpath).blob
        self.assertEqual(observed, expected)

    def test_ac_rs_1_frontmatter_normalizes_to_lists_and_an_integer_order(self):
        """AC-RS-1: values are lists of words; `order` is an int; `id` is not a key."""
        row = by_id(self.rows)["R0001"]
        self.assertEqual(row.order, 10)
        self.assertEqual(row.keys["role"], ["writer", "critic"])
        self.assertEqual(row.keys["topic"], ["core"])
        self.assertNotIn("id", row.keys)
        self.assertNotIn("order", row.keys)

    def test_ac_rs_1_a_null_value_carries_no_key(self):
        """AC-RS-1: `term: null` is an absent key, not a key holding "null"."""
        self.assertNotIn("term", by_id(self.rows)["R0001"].keys)

    def test_ac_rs_13_a_definition_carries_a_term_and_no_role(self):
        """AC-RS-13 (DEC-000420): the definition row's shape, as it is on disk."""
        row = by_id(self.rows)["R0100"]
        self.assertEqual(row.keys["term"], ["tranche", "tranches"])
        self.assertNotIn("role", row.keys)

    def test_ac_rs_14_the_body_stops_at_the_human_section(self):
        """AC-RS-14 (G4): `body` is everything above `## Human`, stripped."""
        row = by_id(self.rows)["R0001"]
        self.assertEqual(row.body,
                         "Open one tranche per delta, and close it at the end.")
        self.assertNotIn("## Human", row.body)

    def test_ac_rs_14_the_human_section_is_carried_on_the_row(self):
        """AC-RS-14: two forms, one row — the human form is parsed, not dropped."""
        self.assertEqual(by_id(self.rows)["R0001"].human,
                         "DEC-000170: the branch is the state.")

    def test_ac_rs_14_a_row_with_no_human_section_carries_none(self):
        """AC-RS-14: `human` is None, not the empty string, when there is none."""
        self.assertIsNone(by_id(self.rows)["R0002"].human)

    def test_ac_rs_15_a_process_document_carries_its_path_and_stem_id(self):
        """AC-RS-15: a `process/` document has no `id:`; its path is its identity."""
        row = next((r for r in self.rows if r.path == "process/change-flow.md"), None)
        self.assertIsNotNone(row)
        self.assertEqual(row.kind, "process")
        self.assertEqual(row.id, "change-flow")

    def test_s2_a_human_heading_at_any_atx_level_still_splits_the_row(self):
        """S2: `### Human` (not just `## Human`) still separates the two
        forms — a mis-levelled heading must not publish the human form."""
        files = dict(rs_store_files())
        files["rules/R0001.md"] = files["rules/R0001.md"].replace(
            "## Human", "### Human"
        )
        _origin, clone = make_store_repo(self, files=files)
        row = by_id(FileRowSource(clone).rows())["R0001"]
        self.assertEqual(row.human, "DEC-000170: the branch is the state.")
        self.assertNotIn("### Human", row.body)
        self.assertNotIn("DEC-000170", row.body)


class TestFileRowSourceDefects(unittest.TestCase):
    """AC-RS-1: a value the dialect cannot type is a defect, named and raised."""

    def test_ac_rs_1_a_non_integer_order_raises_row_shape_error(self):
        """AC-RS-1: `order: twenty` names the id and the key it came from."""
        files = dict(rs_store_files())
        files["rules/R0002.md"] = rs_row(
            "R0002", "State the obligation at its shortest.",
            order="twenty", topic=["core"], role=["writer"], verb="require", term=None,
        )
        _origin, clone = make_store_repo(self, files=files)
        with self.assertRaises(RowShapeError) as caught:
            FileRowSource(clone).rows()
        message = str(caught.exception)
        self.assertIn("R0002", message)
        self.assertIn("order", message)

    def test_s4_a_rules_file_with_no_frontmatter_raises_row_shape_error(self):
        """S4: a rules/ file with no frontmatter block is a defect, not a
        silently-accepted row keyed by its filename stem."""
        files = dict(rs_store_files())
        files["rules/R0777.md"] = "A rules/ row holding only prose.\n"
        _origin, clone = make_store_repo(self, files=files)
        with self.assertRaises(RowShapeError) as caught:
            FileRowSource(clone).rows()
        self.assertIn("rules/R0777.md", str(caught.exception))

    def test_s4_a_duplicate_id_across_rules_and_process_raises_row_shape_error(self):
        """S4: an id shared across the two roots is a defect, not two rows."""
        files = dict(rs_store_files())
        files["process/R0001.md"] = rs_process(
            "# Duplicate.\n\nA process document sharing rules/R0001's id.",
            order=15,
        )
        _origin, clone = make_store_repo(self, files=files)
        with self.assertRaises(RowShapeError) as caught:
            FileRowSource(clone).rows()
        self.assertIn("R0001", str(caught.exception))

    def test_dec_001400_an_enforce_value_outside_the_four_raises_row_shape_error(self):
        """DEC-001400: `enforce: native` on a rules/ file is refused by the source."""
        files = dict(rs_store_files())
        files["rules/R0002.md"] = rs_row(
            "R0002", "State the obligation at its shortest.",
            order=30, enforce="native", topic=["core"], role=["writer"],
            verb="require", term=None,
        )
        _origin, clone = make_store_repo(self, files=files)
        with self.assertRaises(RowShapeError) as caught:
            FileRowSource(clone).rows()
        message = str(caught.exception)
        self.assertIn("R0002", message)
        self.assertIn("enforce", message)

    def test_dec_001400_a_rules_file_carrying_enforce_hook_is_a_row_keyed_on_it(self):
        """DEC-001400: `enforce: hook` is an ordinary key — selectable, counted."""
        files = dict(rs_store_files())
        files["rules/R0002.md"] = rs_row(
            "R0002", "State the obligation at its shortest.",
            order=30, enforce="hook", topic=["core"], role=["writer"],
            verb="require", term=None,
        )
        _origin, clone = make_store_repo(self, files=files)
        rows = by_id(FileRowSource(clone).rows())
        self.assertEqual(rows["R0002"].keys["enforce"], ["hook"])
        self.assertNotIn("enforce", rows["R0001"].keys)

    def test_ac_rs_10_a_retired_row_carries_retired_and_is_outside_the_store(self):
        """AC-RS-10: `rules/retired/R*.md` carries `retired:` naming its
        successor; the source never returns it, whatever its keys say."""
        files = dict(rs_store_files())
        files["rules/retired/R0901.md"] = rs_row(
            "R0901", "A retired row with a successor.",
            retired="R0002", order=6, topic=["core"], role=["writer"],
            session=["decision"], corpus=["writing"], verb="require", term=None,
        )
        _origin, clone = make_store_repo(self, files=files)
        rows = FileRowSource(clone).rows()
        self.assertNotIn("R0901", by_id(rows))
        text = (clone / "rules" / "retired" / "R0901.md").read_text()
        self.assertIn("\nretired: R0002\n", text)


class TestRowsWithNoInstruction(unittest.TestCase):
    """#365 (A1-A5): a rules/ row must carry an agent-facing body."""

    def load(self, relpath, text):
        files = dict(rs_store_files())
        files[relpath] = text
        _origin, clone = make_store_repo(self, files=files)
        return FileRowSource(clone).rows()

    def assert_refused(self, relpath, text):
        with self.assertRaises(RowShapeError) as caught:
            self.load(relpath, text)
        self.assertIn(relpath, str(caught.exception))

    def test_a1_an_empty_body_is_refused_naming_the_file(self):
        self.assert_refused("rules/R0002.md", rs_row(
            "R0002", "", order=30, topic=["core"], role=["writer"], verb="require", term=None))

    def test_a1_a_frontmatter_only_file_is_refused_naming_the_file(self):
        self.assert_refused(
            "rules/R0002.md",
            "---\nid: R0002\norder: 30\ntopic: [core]\nrole: [writer]\nverb: require\nterm: null\n---\n")

    def test_a1_a_whitespace_only_body_is_refused_naming_the_file(self):
        self.assert_refused(
            "rules/R0002.md",
            "---\nid: R0002\norder: 30\ntopic: [core]\nrole: [writer]\nverb: require\nterm: null\n---\n"
            "\n   \n\t\n\n")

    def test_a1_a_body_that_is_only_a_human_section_is_refused_naming_the_file(self):
        self.assert_refused("rules/R0002.md", rs_row(
            "R0002", "", order=30, topic=["core"], role=["writer"], verb="require", term=None,
            human="DEC-000170: why this row exists."))

    def test_a1_a_human_heading_at_another_level_does_not_hide_an_empty_body(self):
        text = rs_row("R0002", "", order=30, topic=["core"], role=["writer"],
                      verb="require", term=None, human="Why.").replace("## Human", "### Human")
        self.assert_refused("rules/R0002.md", text)

    def test_a2_a_body_with_a_human_section_is_accepted_unchanged(self):
        rows = {r.id: r for r in self.load("rules/R0002.md", rs_row(
            "R0002", "State the obligation at its shortest.", order=30, topic=["core"],
            role=["writer"], verb="require", term=None, human="DEC-000170: why."))}
        self.assertEqual(rows["R0002"].body, "State the obligation at its shortest.")
        self.assertEqual(rows["R0002"].human, "DEC-000170: why.")

    def test_a4_a_definition_row_with_no_body_is_refused(self):
        self.assert_refused("rules/R0100.md", rs_row(
            "R0100", "", order=20, topic=["lexicon"], verb="define", term=["tranche"]))

    def test_a4_a_definition_row_with_a_body_is_accepted(self):
        rows = {r.id: r for r in self.load("rules/R0100.md", rs_row(
            "R0100", "A tranche is one workstream.", order=20, topic=["lexicon"],
            verb="define", term=["tranche"]))}
        self.assertEqual(rows["R0100"].body, "A tranche is one workstream.")

    def test_a4_a_row_whose_body_is_only_an_enforce_block_has_a_body_and_passes(self):
        block = "```yaml\nhook: bin/hooks/lane-guard\n```"
        rows = {r.id: r for r in self.load("rules/R0002.md", rs_row(
            "R0002", block, order=30, enforce="hook", topic=["core"], role=["writer"],
            verb="require", term=None))}
        self.assertEqual(rows["R0002"].body, block)

    def test_a4_process_documents_are_not_newly_constrained(self):
        rows = self.load("process/empty-note.md", rs_process("", order=90, topic=["empty-note"]))
        self.assertIn("process/empty-note.md", [r.path for r in rows])


class TestTheRealStoreStillLoads(unittest.TestCase):
    """A5: the guard against refusing a row the store already holds."""

    def test_a5_the_real_store_loads(self):
        rows = FileRowSource(REPO_ROOT).rows()
        self.assertTrue(rows)
        self.assertTrue(all(r.body for r in rows if r.kind == "rule"))

    def test_a5_all_twelve_bundles_generate(self):
        source = FileRowSource(REPO_ROOT)
        entries = named_queries.bundles(source.named_queries_text())
        self.assertEqual(len(entries), 12, [name for name, _ in entries])
        out = temp_dir(self, "a5-bundles-")
        for name, tokens in entries:
            with self.subTest(bundle=name):
                proc = subprocess.run(
                    [sys.executable, str(REPO_ROOT / "bin" / "bundle"), "--where", *tokens,
                     "--name", name, "--out", str(out)],
                    cwd=str(REPO_ROOT), capture_output=True, text=True, env=base_env())
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertTrue(pathlib.Path(proc.stdout.strip()).is_file())


if __name__ == "__main__":
    unittest.main()
