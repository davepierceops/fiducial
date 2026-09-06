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

import unittest

from rulestore.store import FileRowSource, RowShapeError
from tests.helpers import base_env, git, make_store_repo, rs_row, rs_store_files


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
            ["process/change-flow.md", "rules/R0001.md", "rules/R0002.md",
             "rules/R0003.md", "rules/R0100.md"],
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


if __name__ == "__main__":
    unittest.main()
