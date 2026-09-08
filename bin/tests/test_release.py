"""bin/release, across the process boundary (DEC-000660).

Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 6 (the
tool) and item 8 (this suite). Runs against the fixture repository
(`bin/tests/helpers.py:rs_store_files`), whose `process/named-queries.md`
lists three bundles — writer, critic, coder-agent — each `role=<slug>`.
"""

from __future__ import annotations

import pathlib
import tempfile
import unittest

from tests.helpers import (
    base_env,
    commit,
    git,
    make_repo,
    make_store_repo,
    no_traceback,
    rs_store_files,
    run_cli,
    temp_dir,
    write,
)

EXIT_OK = 0
EXIT_REFUSED = 2

TAG = "v2026.09.07"


class ReleaseCliTestCase(unittest.TestCase):
    def setUp(self):
        self.origin, self.clone = make_store_repo(self)
        self.env = base_env()
        self.out = self.clone.parent / "release-out"

    def release(self, *args, cwd=None):
        return run_cli("release", *args, cwd=cwd or self.clone, env=self.env)

    def add_readme_and_push(self, clone=None):
        clone = clone or self.clone
        write(clone, "README.md", "Fiducial.\n")
        commit(clone, "docs: add README", env=self.env)
        git(clone, "push", "-q", "origin", "main", env=self.env, check=True)


class TestReleaseRefusals(ReleaseCliTestCase):
    def test_refuses_without_readme(self):
        """Refuses, nothing written, when README.md is absent at the root."""
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_readme_is_uncommitted(self):
        """S13: an uncommitted README.md refuses too, not only rules/ or process/."""
        self.add_readme_and_push()
        write(self.clone, "README.md", "An uncommitted edit.\n")
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_out_already_exists(self):
        """Refuses when --out already exists, before any bundle generation."""
        self.add_readme_and_push()
        self.out.mkdir()
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)

    def test_refuses_whole_when_a_list_entry_selects_nothing(self):
        """A list entry whose query selects no rows exits 2 with nothing
        left under --out — the release is refused whole, not partly cut."""
        files = dict(rs_store_files())
        files["process/named-queries.md"] = files["process/named-queries.md"].replace(
            "coder-agent  role=coder-agent\n",
            "coder-agent  role=coder-agent\nnobody       role=nobody\n",
        )
        origin, clone = make_store_repo(self, files=files)
        self.add_readme_and_push(clone)
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=clone, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_whole_when_two_list_entries_share_a_name(self):
        """S15: two entries named alike would collapse to one asset and name
        it twice in the `gh` line — refuse before anything is written."""
        files = dict(rs_store_files())
        files["process/named-queries.md"] = files["process/named-queries.md"].replace(
            "writer       role=writer\n",
            "writer       role=writer\nwriter       topic=core\n",
        )
        origin, clone = make_store_repo(self, files=files)
        self.add_readme_and_push(clone)
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=clone, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertIn("writer", err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_named_queries_is_absent(self):
        """The tenth refusal: an absent process/named-queries.md gets its own
        message, distinct from an empty bundle list."""
        files = dict(rs_store_files())
        del files["process/named-queries.md"]
        origin, clone = make_store_repo(self, files=files)
        self.add_readme_and_push(clone)
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=clone, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertIn("no process/named-queries.md under", err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_outside_a_git_repository(self):
        """F4: outside a git repository entirely."""
        outside = temp_dir(self, "release-outside-")
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=outside, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(err.strip(), "refused: not inside a git repository")
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_neither_rules_nor_process_exist(self):
        """F4: a git repository that is not the rule store."""
        repo = make_repo(self)
        write(repo, "README.md", "Not the rule store.\n")
        commit(repo, "seed", env=self.env)
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=repo, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(str(repo), err.strip())
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_rules_is_uncommitted(self):
        """F4: an uncommitted change under rules/ refuses (S13's widened check)."""
        self.add_readme_and_push()
        write(self.clone, "rules/R0001.md",
              rs_store_files()["rules/R0001.md"] + "\nAn uncommitted line.\n")
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_fetch_cannot_reach_origin(self):
        """F4/S8's shape: a fetch that cannot reach origin refuses distinctly."""
        self.add_readme_and_push()
        git(self.clone, "remote", "set-url", "origin", "/nonexistent/origin.git",
            env=self.env, check=True)
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(err.strip(), "refused: could not fetch origin/main")
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_head_is_not_origin_main(self):
        """F4: HEAD one commit behind origin/main after the fetch."""
        self.add_readme_and_push()
        write(self.clone, "rules/R0004.md",
              "---\nid: R0004\norder: 50\ntopic: [core]\nrole: [writer]\n"
              "verb: require\nterm: null\n---\n\nA later rule.\n")
        commit(self.clone, "store: a later rule", env=self.env)
        git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)
        git(self.clone, "reset", "--hard", "-q", "HEAD~1", env=self.env, check=True)
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(err.strip(), "refused: HEAD is not origin/main")
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_refuses_when_tag_already_exists_on_origin(self):
        """F4: the one guard against re-cutting a released tag."""
        self.add_readme_and_push()
        git(self.clone, "tag", TAG, env=self.env, check=True)
        git(self.clone, "push", "-q", "origin", TAG, env=self.env, check=True)
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(err.strip(), "refused: tag %s already exists on origin" % TAG)
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_cleanup_leaves_no_scratch_directory_after_a_failing_release(self):
        """F4: the `finally` actually removes the scratch tree it wrote at
        least one asset into — not merely that --out was never created."""
        files = dict(rs_store_files())
        files["process/named-queries.md"] = files["process/named-queries.md"].replace(
            "coder-agent  role=coder-agent\n",
            "coder-agent  role=coder-agent\nnobody       role=nobody\n",
        )
        origin, clone = make_store_repo(self, files=files)
        self.add_readme_and_push(clone)
        before = set(pathlib.Path(tempfile.gettempdir()).glob("fiducial-release-*"))
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=clone, env=self.env,
        )
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        after = set(pathlib.Path(tempfile.gettempdir()).glob("fiducial-release-*"))
        self.assertEqual(before, after)


class TestReleaseSuccess(ReleaseCliTestCase):
    def setUp(self):
        super().setUp()
        self.add_readme_and_push()

    def test_writes_one_timestamp_free_asset_per_list_entry(self):
        """One fiducial-bundle-<name>.md per list entry, no timestamp in the name."""
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        written = sorted(p.name for p in self.out.iterdir())
        self.assertEqual(
            written,
            ["fiducial-bundle-coder-agent.md", "fiducial-bundle-critic.md",
             "fiducial-bundle-writer.md"],
        )

    def test_a_name_carrying_a_glob_metacharacter_still_produces_one_asset(self):
        """S14: bin/release reads the exact path bin/bundle prints on stdout,
        so a name like `a[b]` no longer defeats a `glob()` lookup."""
        files = dict(rs_store_files())
        files["process/named-queries.md"] = files["process/named-queries.md"].replace(
            "writer       role=writer\n",
            "a[b]         role=writer\n",
        )
        origin, clone = make_store_repo(self, files=files)
        self.add_readme_and_push(clone)
        code, out, err = run_cli(
            "release", "--tag", TAG, "--out", str(self.out), cwd=clone, env=self.env,
        )
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue((self.out / "fiducial-bundle-a[b].md").is_file())

    def test_prints_the_out_dir_then_the_gh_release_create_command(self):
        """Prints the out dir, then a last line starting `gh release create`,
        naming the tag, HEAD, README.md and every asset."""
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, err)
        lines = out.strip().splitlines()
        self.assertEqual(lines[0], str(self.out))
        last = lines[-1]
        self.assertTrue(last.startswith("gh release create"), last)
        self.assertIn(TAG, last)
        head = git(self.clone, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()
        self.assertIn(head, last)
        self.assertIn("README.md", last)
        for name in ("writer", "critic", "coder-agent"):
            self.assertIn(str(self.out / ("fiducial-bundle-%s.md" % name)), last)


if __name__ == "__main__":
    unittest.main()
