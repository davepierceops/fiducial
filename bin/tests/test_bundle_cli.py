"""AC-RS-3/5/6/13/14/15: the rebuilt `bin/bundle`, across the process boundary.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT" and § "ACCEPTANCE CRITERIA", landed at
`d5b643b48cf0285194d29b09f6755db1b8a16b34`.

Exit codes and refusals are part of the contract, so the command runs as a
subprocess against a **real** git repository — a bare `origin` and a clone
holding the fixture store (`bin/tests/helpers.py:rs_store_files`: three rules,
one definition, one `process/` document, one retired row). Nothing here is
mocked; AC-RS-6's "HEAD is not equal to origin/main after a fetch" is only
meaningful against real refs.

WHERE THE BINARY COMES FROM. The directive commissioning this suite forbids
touching the old `bin/bundle` — its removal is the Coder's package — while also
requiring a red-gate stub of the new command. So the stub lives at
`bin/tests/stubs/bundle`, beside the two directive-tooling stubs, and
`helpers.rs_bin_dir()` prefers it **while it exists**. The Coder's package
deletes it, and the lookup falls through to the real `bin/bundle` with no edit
to this file (DEC-000440: a Test Designer edits tests only).
`$RULESTORE_BUNDLE_BIN` overrides both.
"""

from __future__ import annotations

import pathlib
import re
import unittest

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

#: AC-RS-6: `fiducial-bundle-<name>-<timestamp>Z.md`, the timestamp ISO 8601
#: basic and UTC.
BUNDLE_NAME_RE = re.compile(r"^fiducial-bundle-(?P<name>.+)-\d{8}T\d{6}Z\.md$")

#: AC-RS-3: `--keys` prints `<key>=<value> <count>`.
KEYS_LINE_RE = re.compile(r"^[a-z][a-z0-9-]*=\S+ \d+$")

#: AC-RS-5: `--near` prints `<id> <score to two places>`.
NEAR_LINE_RE = re.compile(r"^\S+ \d+\.\d{2}$")

EXIT_OK = 0
EXIT_REFUSED = 2


class BundleCliTestCase(unittest.TestCase):
    def setUp(self):
        self.origin, self.clone = make_store_repo(self)
        self.env = base_env()
        self.out = temp_dir(self, "rulestore-out-")

    # ------------------------------------------------------------- utilities

    def bundle(self, *args, cwd=None):
        return run_bundle(*args, cwd=cwd or self.clone, env=self.env)

    def bundle_path(self, out):
        """The path the command printed, checked before anything reads it."""
        printed = out.strip()
        self.assertTrue(printed, "the command printed no path on stdout")
        path = pathlib.Path(printed)
        self.assertTrue(path.is_file(), printed)
        return path

    def written(self):
        return sorted(p.name for p in self.out.iterdir())

    def dirty_the_store(self):
        """An uncommitted edit under `rules/` — AC-RS-6's unsynced tree."""
        write(self.clone, "rules/R0001.md",
              (self.clone / "rules/R0001.md").read_text() + "\nAn uncommitted line.\n")

    def put_origin_ahead(self):
        """Leave the clone one commit behind `origin/main`, working tree clean."""
        write(self.clone, "rules/R0004.md",
              "---\nid: R0004\norder: 50\ntopic: [core]\nrole: [writer]\n"
              "verb: require\nterm: null\n---\n\nA later rule.\n")
        commit(self.clone, "store: a later rule", env=self.env)
        git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)
        git(self.clone, "reset", "--hard", "-q", "HEAD~1", env=self.env, check=True)


class TestBundleWhere(BundleCliTestCase):
    """AC-RS-6: one file, the ruled name and directory, the header, the path."""

    def test_ac_rs_6_a_query_writes_exactly_one_file_under_the_ruled_name(self):
        """AC-RS-6: one file in `--out`, named `fiducial-bundle-<name>-<ts>Z.md`."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        self.assertEqual(len(self.written()), 1, self.written())
        match = BUNDLE_NAME_RE.match(self.written()[0])
        self.assertIsNotNone(match, self.written()[0])
        self.assertEqual(match.group("name"), "role-writer")

    def test_ac_rs_6_the_written_path_is_printed_on_stdout(self):
        """AC-RS-6: the command prints the path it wrote, and exits 0."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        printed = self.bundle_path(out)
        self.assertEqual(printed.parent.resolve(), self.out.resolve())

    def test_ac_rs_6_the_default_name_joins_every_key_value_pair(self):
        """AC-RS-6: `<name>` defaults to the query's pairs joined `k-v` with `-`."""
        code, _out, err = self.bundle(
            "--where", "role=writer", "corpus=writing", "--out", str(self.out)
        )
        self.assertEqual(code, EXIT_OK, err)
        match = BUNDLE_NAME_RE.match(self.written()[0])
        self.assertIsNotNone(match, self.written()[0])
        self.assertEqual(match.group("name"), "role-writer-corpus-writing")

    def test_ac_rs_6_an_explicit_name_replaces_the_default(self):
        """AC-RS-6: `--name <name>` names the file instead of the query."""
        code, _out, err = self.bundle(
            "--where", "role=writer", "--name", "writing-desk", "--out", str(self.out)
        )
        self.assertEqual(code, EXIT_OK, err)
        match = BUNDLE_NAME_RE.match(self.written()[0])
        self.assertIsNotNone(match, self.written()[0])
        self.assertEqual(match.group("name"), "writing-desk")

    def test_ac_rs_6_the_default_directory_is_the_downloads_folder(self):
        """AC-RS-6: `--out` defaults to `~/Downloads`."""
        code, _out, err = self.bundle("--where", "role=writer")
        self.assertEqual(code, EXIT_OK, err)
        downloads = pathlib.Path(self.env["HOME"]) / "Downloads"
        written = [p.name for p in downloads.iterdir()] if downloads.is_dir() else []
        for name in written:
            (downloads / name).unlink()
        self.assertEqual(len(written), 1, written)
        self.assertIsNotNone(BUNDLE_NAME_RE.match(written[0]), written[0])

    def test_ac_rs_6_the_header_stamps_repo_head_generated_and_the_rows(self):
        """AC-RS-6: the header's fields, with the full HEAD SHA and each blob."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        lines = self.bundle_path(out).read_text().splitlines()
        head = git(self.clone, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()
        blob = git(self.clone, "rev-parse", "HEAD:rules/R0001.md",
                   env=self.env, check=True)[1].strip()
        self.assertEqual(lines[0], "# fiducial-bundle")
        self.assertIn("- HEAD: %s" % head, lines)
        self.assertIn("- Rows:", lines)
        self.assertIn("  - R0001 (%s)" % blob, lines)
        self.assertTrue(any(line.startswith("- Repo: ") for line in lines), lines[:8])
        self.assertTrue(
            any(re.match(r"^- Generated: \d{8}T\d{6}Z$", line) for line in lines),
            lines[:8],
        )

    def test_ac_rs_15_the_bundle_holds_the_selected_rows_in_order(self):
        """AC-RS-15: a `process/` document interleaves with rules by `order`."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        text = self.bundle_path(out).read_text()
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        self.assertEqual(
            headings, ["## R0001", "## process/change-flow.md", "## R0002",
                       "## Definitions"]
        )

    def test_ac_rs_13_a_used_term_pulls_its_definition_into_the_bundle(self):
        """AC-RS-13: R0001's body uses "tranche", so R0100 joins the bundle."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        text = self.bundle_path(out).read_text()
        self.assertIn("- Definitions:", text)
        self.assertIn("**tranche** — A tranche is one concurrent workstream of build "
                      "work.", text)

    def test_ac_rs_14_no_human_content_reaches_the_bundle(self):
        """AC-RS-14 (G4): the `## Human` section is nowhere in the output."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        text = self.bundle_path(out).read_text()
        self.assertNotIn("## Human", text)
        self.assertNotIn("DEC-000170", text)

    def test_ac_rs_6_a_retired_row_is_never_bundled(self):
        """AC-RS-1/AC-RS-6: `rules/retired/` is outside the store."""
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        text = self.bundle_path(out).read_text()
        self.assertNotIn("R0900", text)


class TestBundleRefusals(BundleCliTestCase):
    """AC-RS-6: non-zero exit with a reason, and nothing written."""

    def assert_refused(self, code, out, err):
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(self.written(), [])
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)

    def test_ac_rs_6_a_malformed_query_is_refused(self):
        """AC-RS-6: a `--where` token that is not `k=v` refuses, writing nothing."""
        code, out, err = self.bundle("--where", "role", "--out", str(self.out))
        self.assert_refused(code, out, err)

    def test_ac_rs_6_an_empty_query_value_is_refused(self):
        """AC-RS-6: an empty value is malformed, not a query for the empty string."""
        code, out, err = self.bundle("--where", "role=", "--out", str(self.out))
        self.assert_refused(code, out, err)

    def test_ac_rs_6_an_uncommitted_change_under_rules_is_refused(self):
        """AC-RS-6: an unsynced tree refuses — a bundle must be reproducible."""
        self.dirty_the_store()
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assert_refused(code, out, err)

    def test_ac_rs_6_a_head_behind_origin_main_is_refused(self):
        """AC-RS-6: "HEAD is not equal to origin/main after a fetch"."""
        self.put_origin_ahead()
        code, out, err = self.bundle("--where", "role=writer", "--out", str(self.out))
        self.assert_refused(code, out, err)

    def test_ac_rs_6_an_empty_selection_is_refused(self):
        """AC-RS-6: "An empty selection is refused, not written"."""
        code, out, err = self.bundle("--where", "role=nobody", "--out", str(self.out))
        self.assert_refused(code, out, err)


class TestBundleKeysAndNear(BundleCliTestCase):
    """AC-RS-3 and AC-RS-5: the two modes that need no sync, run on a dirty tree."""

    def setUp(self):
        super().setUp()
        self.dirty_the_store()

    def test_ac_rs_3_keys_lists_every_key_value_with_its_count(self):
        """AC-RS-3: `<key>=<value> <count>`, computed from the store, sorted."""
        code, out, err = self.bundle("--keys")
        self.assertEqual(code, EXIT_OK, err)
        lines = out.strip().splitlines()
        self.assertTrue(lines, out)
        for line in lines:
            self.assertRegex(line, KEYS_LINE_RE)
        self.assertEqual(lines, sorted(lines))
        self.assertIn("role=writer 2", lines)
        self.assertIn("topic=core 2", lines)

    def test_ac_rs_3_keys_excludes_the_two_typed_keys(self):
        """AC-RS-3: `id` and `order` are not keys in use."""
        code, out, err = self.bundle("--keys")
        self.assertEqual(code, EXIT_OK, err)
        prefixes = {line.split("=", 1)[0] for line in out.strip().splitlines()}
        self.assertNotIn("id", prefixes)
        self.assertNotIn("order", prefixes)

    def test_ac_rs_5_near_prints_each_row_with_its_score(self):
        """AC-RS-5: `<id> <score to two places>`, highest first, no sync needed."""
        code, out, err = self.bundle("--near", "a tranche is one concurrent workstream")
        self.assertEqual(code, EXIT_OK, err)
        lines = out.strip().splitlines()
        self.assertTrue(lines, out)
        for line in lines:
            self.assertRegex(line, NEAR_LINE_RE)
        scores = [float(line.rsplit(" ", 1)[1]) for line in lines]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertEqual(lines[0].split(" ", 1)[0], "R0100")


if __name__ == "__main__":
    unittest.main()
