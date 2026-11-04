"""`bin/bundle --emit bundle`: today's bundle through the target registry
(the plan, §3a; SPEC.md §7).

Two things are held: `--emit bundle` writes the bytes `--where` writes for
the same query (the header's timestamp aside), and an `enforce:` row
prints its prose and never its block or Human note (issue #399). The sync refusal is
dropped from `--emit` (DEC-000940): a dirty tree and a HEAD behind origin
both emit.
"""

from __future__ import annotations

import pathlib
import re
import unittest

from tests.emit_fixtures import emit_store_files
from tests.helpers import (
    base_env,
    commit,
    git,
    make_store_repo,
    no_traceback,
    run_bundle,
    temp_dir,
    write,
)

HEADER_RE = re.compile(r"^<!-- fiducial \S+ @ \S+ \d{8}T\d{6}Z -->$")


def sans_header(text):
    lines = text.splitlines()
    assert HEADER_RE.match(lines[0]), lines[0]
    return "\n".join(lines[1:])


class EmitBundleTestCase(unittest.TestCase):
    def setUp(self):
        self.origin, self.clone = make_store_repo(self, files=emit_store_files())
        self.env = base_env()
        self.out_where = temp_dir(self, "emit-where-")
        self.out_emit = temp_dir(self, "emit-bundle-")

    def bundle(self, *args):
        return run_bundle(*args, cwd=self.clone, env=self.env)

    def only_file(self, out):
        files = sorted(out.iterdir())
        self.assertEqual(len(files), 1, files)
        return files[0]


class TestEmitBundleRegression(EmitBundleTestCase):
    def test_emit_bundle_is_byte_identical_to_where_for_a_writing_role(self):
        """`--emit bundle --where role=writer` and `--where role=writer` write
        the same name shape and the same bytes below the header line."""
        code, _, err = self.bundle("--where", "role=writer", "--out", str(self.out_where))
        self.assertEqual(code, 0, err)
        code, out, err = self.bundle(
            "--emit", "bundle", "--where", "role=writer", "--out", str(self.out_emit)
        )
        self.assertEqual(code, 0, err)
        via_where = self.only_file(self.out_where)
        via_emit = self.only_file(self.out_emit)
        self.assertEqual(pathlib.Path(out.strip()), via_emit)
        self.assertRegex(via_emit.name, r"^fiducial-bundle-role-writer-\d{8}T\d{6}Z\.md$")
        self.assertEqual(sans_header(via_emit.read_text()), sans_header(via_where.read_text()))
        self.assertTrue(HEADER_RE.match(via_emit.read_text().splitlines()[0]))

    def test_emit_bundle_honours_name(self):
        code, _, err = self.bundle(
            "--emit", "bundle", "--where", "role=writer", "--name", "desk",
            "--out", str(self.out_emit),
        )
        self.assertEqual(code, 0, err)
        self.assertRegex(self.only_file(self.out_emit).name, r"^fiducial-bundle-desk-")

    def test_issue_399_a_block_only_hook_row_is_skipped_entirely(self):
        """R0720 has no prose, only a block: the writer bundle carries
        neither its yaml nor its Human note (bundles carry no Human content)."""
        code, _, err = self.bundle(
            "--emit", "bundle", "--where", "role=writer", "--out", str(self.out_emit)
        )
        self.assertEqual(code, 0, err)
        text = self.only_file(self.out_emit).read_text()
        self.assertNotIn("After a `git push` it fetches the remote", text)
        self.assertNotIn("bin/hooks/push-readback", text)
        self.assertNotIn("event: PostToolUse\nmatcher: Bash", text)
        self.assertNotIn("## Human", text)

    def test_an_enforce_row_with_prose_prints_the_prose_and_not_the_block(self):
        code, _, err = self.bundle(
            "--emit", "bundle", "--where", "role=writer", "--out", str(self.out_emit)
        )
        self.assertEqual(code, 0, err)
        text = self.only_file(self.out_emit).read_text()
        self.assertIn("Append to `decisions/log.md`", text)
        self.assertNotIn("bin/hooks/decision-log-append-only", text)
        self.assertNotIn("```", text)
        self.assertNotIn("deny:", text)
        self.assertNotIn("field: model", text)
        self.assertIn("Never let a secret value enter context.", text)
        self.assertNotIn("Read(./.env)", text)

    def test_where_renders_the_same_way(self):
        """The rule lives in the shared renderer, so `--where` and
        `--emit bundle` cannot disagree on it."""
        code, _, err = self.bundle("--where", "role=writer", "--out", str(self.out_where))
        self.assertEqual(code, 0, err)
        text = self.only_file(self.out_where).read_text()
        self.assertNotIn("After a `git push` it fetches the remote", text)
        self.assertNotIn("bin/hooks/", text)
        self.assertNotIn("```", text)


class TestEmitDropsTheSyncRefusal(EmitBundleTestCase):
    """DEC-000940: `--emit` renders the local tree as it stands."""

    def test_a_dirty_tree_emits(self):
        write(self.clone, "rules/R0002.md",
              (self.clone / "rules/R0002.md").read_text() + "\nAn uncommitted line.\n")
        code, _, err = self.bundle(
            "--emit", "bundle", "--where", "role=chief-of-staff", "--out", str(self.out_emit)
        )
        self.assertEqual(code, 0, err)
        self.assertIn("An uncommitted line.", self.only_file(self.out_emit).read_text())

    def test_a_head_behind_origin_emits(self):
        write(self.clone, "rules/R0005.md",
              "---\nid: R0005\norder: 50\ntopic: [core]\nrole: [writer]\n"
              "session: [decision]\ncorpus: [writing]\nverb: require\nterm: null\n---\n\n"
              "A later rule.\n")
        commit(self.clone, "store: a later rule", env=self.env)
        git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)
        git(self.clone, "reset", "--hard", "-q", "HEAD~1", env=self.env, check=True)
        code, _, err = self.bundle(
            "--emit", "bundle", "--where", "role=writer", "--out", str(self.out_emit)
        )
        self.assertEqual(code, 0, err)

    def test_where_still_refuses_a_dirty_tree(self):
        write(self.clone, "rules/R0002.md",
              (self.clone / "rules/R0002.md").read_text() + "\nAn uncommitted line.\n")
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out_where))
        self.assertEqual(code, 2, err)
        self.assertEqual(sorted(self.out_where.iterdir()), [])


class TestEmitRefusals(EmitBundleTestCase):
    def assert_refused(self, code, out, err):
        self.assertEqual(code, 2, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertEqual(sorted(self.out_emit.iterdir()), [])

    def test_an_unknown_target_is_refused_naming_the_targets(self):
        code, out, err = self.bundle("--emit", "cursor", "--out", str(self.out_emit))
        self.assert_refused(code, out, err)
        self.assertIn("bundle", err)
        self.assertIn("claude-code", err)

    def test_bundle_without_a_query_is_refused(self):
        code, out, err = self.bundle("--emit", "bundle", "--out", str(self.out_emit))
        self.assert_refused(code, out, err)

    def test_an_empty_selection_is_refused(self):
        code, out, err = self.bundle(
            "--emit", "bundle", "--where", "role=nobody", "--out", str(self.out_emit)
        )
        self.assert_refused(code, out, err)

    def test_emit_without_out_is_refused(self):
        code, out, err = self.bundle("--emit", "bundle", "--where", "role=writer")
        self.assert_refused(code, out, err)

    def test_a_malformed_query_is_refused(self):
        code, out, err = self.bundle(
            "--emit", "bundle", "--where", "role", "--out", str(self.out_emit)
        )
        self.assert_refused(code, out, err)


if __name__ == "__main__":
    unittest.main()
