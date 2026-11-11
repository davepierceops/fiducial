"""bin/release, across the process boundary (DEC-000660).

Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 6 (the
tool) and item 8 (this suite). Runs against the fixture repository
(`bin/tests/helpers.py:rs_store_files`), whose `process/named-queries.md`
lists three bundles — writer, critic, coder-agent — each `role=<slug>`.
"""

from __future__ import annotations

import os
import pathlib
import re
import shlex
import shutil
import tempfile
import unittest

from tests.helpers import (
    BIN_DIR,
    REPO_ROOT,
    base_env,
    commit,
    git,
    make_repo,
    make_store_repo,
    no_traceback,
    rs_row,
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
        self.point_origin_at_github(clone)

    def point_origin_at_github(self, clone=None, url="https://github.com/acme/fid.git"):
        """Make `remote.origin.url` a GitHub URL while fetches still reach the
        local bare origin: `url.<local>.insteadOf <github url>` rewrites it."""
        clone = clone or self.clone
        local = git(clone, "config", "--get", "remote.origin.url",
                    env=self.env, check=True)[1].strip()
        git(clone, "config", "url.%s.insteadOf" % local, url, env=self.env, check=True)
        git(clone, "remote", "set-url", "origin", url, env=self.env, check=True)

    def commit_and_push(self, files, message="chore: seed"):
        for relpath, text in files.items():
            write(self.clone, relpath, text)
        commit(self.clone, message, env=self.env)
        git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)


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


class TestReleaseGhLine(ReleaseCliTestCase):
    """#381 C1: the printed `gh release create` line names its repository."""

    def gh_tokens(self, args=None):
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))
        last = out.strip().splitlines()[-1]
        self.assertTrue(last.startswith("gh release create"), last)
        return shlex.split(last)

    def test_c1_the_line_carries_dash_r_owner_repo_from_the_origin_url(self):
        self.add_readme_and_push()
        tokens = self.gh_tokens()
        self.assertIn("-R", tokens)
        self.assertEqual(tokens[tokens.index("-R") + 1], "acme/fid")

    def repoint(self, url):
        """Serve `url` from the same local origin, whatever URL was set before."""
        for key in git(self.clone, "config", "--name-only", "--get-regexp", r"^url\..*\.insteadof$",
                       env=self.env)[1].split():
            git(self.clone, "config", "--unset-all", key, env=self.env)
        git(self.clone, "config", "url.%s.insteadOf" % self.origin, url, env=self.env, check=True)
        git(self.clone, "remote", "set-url", "origin", url, env=self.env, check=True)

    def test_c1_each_github_url_form_yields_the_same_owner_repo(self):
        forms = ("https://github.com/acme/fid.git", "https://github.com/acme/fid",
                 "git@github.com:acme/fid.git", "ssh://git@github.com/acme/fid.git")
        for url in forms:
            with self.subTest(url=url):
                self.setUp()
                self.add_readme_and_push()
                self.repoint(url)
                tokens = self.gh_tokens()
                self.assertIn("-R", tokens)
                self.assertEqual(tokens[tokens.index("-R") + 1], "acme/fid")

    def test_c1_the_line_does_not_depend_on_the_directory_it_ran_from(self):
        self.add_readme_and_push()
        nested = self.clone / "rules"
        code, out, err = run_cli("release", "--tag", TAG, "--out", str(self.out),
                                 cwd=nested, env=self.env)
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))
        tokens = shlex.split(out.strip().splitlines()[-1])
        self.assertIn("-R", tokens)
        self.assertEqual(tokens[tokens.index("-R") + 1], "acme/fid")

    def test_c1_a_remote_that_is_not_a_github_url_is_refused(self):
        # The fixture origin is a local path: fetch succeeds, the URL is no GitHub URL.
        write(self.clone, "README.md", "Fiducial.\n")
        commit(self.clone, "docs: add README", env=self.env)
        git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(err.strip().splitlines()), 1, err)
        self.assertEqual(out, "")
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def test_c1_a_host_that_only_looks_like_github_is_refused(self):
        for url in ("https://gitlab.com/acme/fid.git", "https://github.com.example.invalid/acme/fid.git",
                    "https://example.invalid/github.com/acme/fid.git"):
            with self.subTest(url=url):
                self.setUp()
                write(self.clone, "README.md", "Fiducial.\n")
                commit(self.clone, "docs: add README", env=self.env)
                git(self.clone, "push", "-q", "origin", "main", env=self.env, check=True)
                self.repoint(url)
                code, out, err = self.release("--tag", TAG, "--out", str(self.out))
                self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
                self.assertEqual(out, "")
                self.assertFalse(self.out.exists())

    def test_c1_the_url_refusal_comes_after_the_fetch_refusal(self):
        self.add_readme_and_push()
        self.repoint("https://gitlab.com/acme/fid.git")
        git(self.clone, "config", "--unset-all", "url.%s.insteadOf" % self.origin, env=self.env, check=True)
        git(self.clone, "remote", "set-url", "origin", "/nonexistent/origin.git",
            env=self.env, check=True)
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED)
        self.assertEqual(err.strip(), "refused: could not fetch origin/main")


class ReleaseToolCopy:
    """A scratch copy of `bin/` whose `bundle` can be made to emit a bad file.

    `bin/release` runs the `bundle` that sits beside it, so a copy of the tool
    directory with a wrapping `bundle` is the seam for generator defects: the
    wrapper runs the real command, then (per environment) deletes text from the
    file it wrote or appends text to it. `SABOTAGE_BUNDLE` limits that to one
    `--name`. Nothing in the repository is touched.
    """

    WRAPPER = """#!/usr/bin/env python3
import os, pathlib, subprocess, sys
here = pathlib.Path(__file__).resolve().parent
proc = subprocess.run([sys.executable, str(here / "bundle_real"), *sys.argv[1:]],
                      capture_output=True, text=True)
sys.stderr.write(proc.stderr)
if proc.returncode:
    sys.exit(proc.returncode)
path = pathlib.Path(proc.stdout.strip())
name = sys.argv[sys.argv.index("--name") + 1] if "--name" in sys.argv else None
only = os.environ.get("SABOTAGE_BUNDLE")
if only is None or only == name:
    text = path.read_text()
    for old in filter(None, os.environ.get("SABOTAGE_REMOVE", "").split("\\x1e")):
        text = text.replace(old, "")
    text += os.environ.get("SABOTAGE_APPEND", "")
    path.write_text(text)
print(proc.stdout.strip())
"""

    @classmethod
    def make(cls, case):
        tool = temp_dir(case, "release-tool-")
        shutil.rmtree(tool)
        shutil.copytree(BIN_DIR, tool, ignore=shutil.ignore_patterns("tests", "hooks", "__pycache__"))
        os.replace(tool / "bundle", tool / "bundle_real")
        (tool / "bundle").write_text(cls.WRAPPER)
        (tool / "bundle").chmod(0o755)
        return tool


class TestReleaseBodyCheck(ReleaseCliTestCase):
    """#381 C2: each generated bundle is checked against its selection and
    against the retired rows, reading the file that was generated."""

    def setUp(self):
        super().setUp()
        self.tool = ReleaseToolCopy.make(self)

    def stage(self, extra_files):
        files = dict(rs_store_files())
        files.update(extra_files)
        _origin, self.clone = make_store_repo(self, files=files)
        self.out = self.clone.parent / "release-out"
        self.add_readme_and_push(self.clone)

    def release_with(self, **sabotage):
        env = dict(self.env)
        env.update(sabotage)
        return run_cli("release", "--tag", TAG, "--out", str(self.out),
                       cwd=self.clone, env=env, script_dir=self.tool)

    def assert_refused_naming(self, result, *names):
        code, out, err = result
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        for name in names:
            self.assertIn(name, err)
        self.assertEqual(out, "")
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists(), "a refused release must leave no output directory")

    def test_c2_a_selected_row_missing_from_the_generated_file_refuses(self):
        self.stage({})
        result = self.release_with(SABOTAGE_BUNDLE="writer",
                                   SABOTAGE_REMOVE="Open one tranche per delta, and close it at the end.")
        self.assert_refused_naming(result, "writer", "R0001")

    def test_c2_a_row_missing_from_a_later_bundle_still_refuses_the_whole_release(self):
        self.stage({})
        result = self.release_with(SABOTAGE_BUNDLE="coder-agent",
                                   SABOTAGE_REMOVE="Run the red gate before any implementation.")
        self.assert_refused_naming(result, "coder-agent", "R0003")

    def test_c2_a_retired_rows_text_in_the_generated_file_refuses(self):
        self.stage({"rules/retired/R0900.md": rs_store_files()["rules/retired/R0900.md"]})
        result = self.release_with(SABOTAGE_BUNDLE="critic",
                                   SABOTAGE_APPEND="\nA retired row is never bundled.\n")
        self.assert_refused_naming(result, "critic", "R0900")

    def test_c2_process_text_is_excluded_only_for_a_process_document_the_bundle_includes(self):
        """change-flow carries the sentence; the coder-agent bundle does not
        include change-flow, so the sentence there is a retired row's text."""
        sentence = "Every pull request gets an agentic code review."
        self.stage({"rules/retired/R0901.md": rs_row(
            "R0901", sentence, retired="R0001", order=7, topic=["core"], role=["writer"],
            session=["decision"], corpus=["writing"], verb="require", term=None)})
        result = self.release_with(SABOTAGE_BUNDLE="coder-agent", SABOTAGE_APPEND="\n%s\n" % sentence)
        self.assert_refused_naming(result, "coder-agent", "R0901")

    def test_c2_text_a_retired_row_shares_with_an_included_process_document_passes(self):
        sentence = "Every pull request gets an agentic code review."
        self.stage({"rules/retired/R0901.md": rs_row(
            "R0901", sentence, retired="R0001", order=7, topic=["core"], role=["writer"],
            session=["decision"], corpus=["writing"], verb="require", term=None)})
        code, out, err = self.release_with()
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))

    def test_c2_text_a_retired_row_shares_with_a_selected_live_row_passes(self):
        self.stage({"rules/retired/R0902.md": rs_row(
            "R0902", "State the obligation at its shortest.", retired="R0002", order=8,
            topic=["core"], role=["writer"], session=["decision"], corpus=["software"],
            verb="require", term=None)})
        code, out, err = self.release_with()
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))

    def test_c2_a_selected_row_that_renders_nothing_is_exempt(self):
        self.stage({"rules/R0300.md": rs_row(
            "R0300", "```yaml\nhook: bin/hooks/lane-guard\n```", order=35, enforce="hook",
            topic=["core"], role=["writer"], session=["decision"], corpus=["writing"],
            verb="require", term=None)})
        code, out, err = self.release_with()
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))

    def test_c2_a_clean_fixture_release_still_succeeds_through_the_copy(self):
        self.stage({})
        code, out, err = self.release_with()
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(len(list(self.out.iterdir())), 3)


class TestReleaseRealStore(unittest.TestCase):
    """#381 C3: the real store passes the body check for all twelve bundles."""

    def test_c3_a_release_of_the_real_store_succeeds_with_twelve_bundles(self):
        env = base_env()
        parent = temp_dir(self, "release-real-")
        origin = parent / "origin.git"
        git(parent, "init", "--bare", "-q", "-b", "main", str(origin), env=env, check=True)
        git(origin, "fetch", "-q", str(REPO_ROOT), "HEAD:refs/heads/main", env=env, check=True)
        clone = parent / "clone"
        git(parent, "clone", "-q", str(origin), str(clone), env=env, check=True)
        self.assertTrue((clone / "README.md").is_file())
        git(clone, "config", "url.%s.insteadOf" % origin, "https://github.com/acme/fid.git",
            env=env, check=True)
        git(clone, "remote", "set-url", "origin", "https://github.com/acme/fid.git", env=env, check=True)
        out_dir = parent / "release-out"
        code, out, err = run_cli("release", "--tag", TAG, "--out", str(out_dir),
                                 cwd=clone, env=env, timeout=300)
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))
        bundles = sorted(p.name for p in out_dir.glob("fiducial-bundle-*.md"))
        self.assertEqual(len(bundles), 12, bundles)


class TestReleaseInputScope(ReleaseCliTestCase):
    """#366 D1/D2/D5: the cleanliness check covers the generation inputs only."""

    def setUp(self):
        super().setUp()
        self.commit_and_push({
            "README.md": "Fiducial.\n",
            "bin/bundle": "#!/bin/sh\n",
            "bin/release": "#!/bin/sh\n",
            "bin/rulestore/mod.py": "X = 1\n",
            "docs/guide.md": "A guide.\n",
            "reviews/old.md": "A review.\n",
        })
        self.point_origin_at_github()

    def assert_blocked_naming(self, *paths):
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_REFUSED, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(any(path in err for path in paths), "%r names none of %r" % (err, paths))
        self.assertTrue(no_traceback(out, err), err)
        self.assertFalse(self.out.exists())

    def assert_not_blocked(self):
        code, out, err = self.release("--tag", TAG, "--out", str(self.out))
        self.assertEqual(code, EXIT_OK, "stdout=%r stderr=%r" % (out, err))

    def test_d1_an_untracked_file_outside_the_input_roots_does_not_block(self):
        write(self.clone, "notes/scratch.txt", "scratch\n")
        write(self.clone, "docs/new.md", "new\n")
        write(self.clone, "tmp-output.log", "log\n")
        self.assert_not_blocked()

    def test_d1_a_modified_tracked_file_outside_the_input_roots_does_not_block(self):
        write(self.clone, "docs/guide.md", "An edited guide.\n")
        write(self.clone, "reviews/old.md", "An edited review.\n")
        self.assert_not_blocked()

    def test_d1_a_deleted_tracked_file_outside_the_input_roots_does_not_block(self):
        (self.clone / "docs" / "guide.md").unlink()
        self.assert_not_blocked()

    def test_d2_a_modified_file_under_rules_blocks_naming_the_path(self):
        write(self.clone, "rules/R0001.md", (self.clone / "rules/R0001.md").read_text() + "\nEdit.\n")
        self.assert_blocked_naming("rules/R0001.md")

    def test_d2_an_untracked_file_under_rules_blocks_naming_the_path(self):
        write(self.clone, "rules/R0200.md", "---\nid: R0200\n---\n\nNew.\n")
        self.assert_blocked_naming("rules/R0200.md")

    def test_d2_an_untracked_file_under_process_blocks_naming_the_path(self):
        write(self.clone, "process/new-note.md", "# New\n")
        self.assert_blocked_naming("process/new-note.md")

    def test_d2_a_deleted_file_under_rules_blocks_naming_the_path(self):
        (self.clone / "rules" / "R0003.md").unlink()
        self.assert_blocked_naming("rules/R0003.md")

    def test_d2_a_renamed_file_under_rules_blocks_naming_a_path(self):
        git(self.clone, "mv", "rules/R0003.md", "rules/R0003b.md", env=self.env, check=True)
        self.assert_blocked_naming("rules/R0003.md", "rules/R0003b.md")

    def test_d2_a_modified_readme_blocks_naming_the_path(self):
        write(self.clone, "README.md", "An edit.\n")
        self.assert_blocked_naming("README.md")

    def test_d2_a_modified_generator_script_blocks_naming_the_path(self):
        for relpath in ("bin/bundle", "bin/release"):
            with self.subTest(path=relpath):
                self.setUp()
                write(self.clone, relpath, "#!/bin/sh\n# edited\n")
                self.assert_blocked_naming(relpath)

    def test_d2_an_untracked_file_under_bin_rulestore_blocks_naming_the_path(self):
        write(self.clone, "bin/rulestore/extra.py", "Y = 2\n")
        self.assert_blocked_naming("bin/rulestore/extra.py")

    def test_d2_a_modified_file_under_bin_rulestore_blocks_naming_the_path(self):
        write(self.clone, "bin/rulestore/mod.py", "X = 2\n")
        self.assert_blocked_naming("bin/rulestore/mod.py")

    def test_d5_release_assets_carry_the_plain_revision(self):
        self.assert_not_blocked()
        head = git(self.clone, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()
        assets = sorted(self.out.glob("fiducial-bundle-*.md"))
        self.assertEqual(len(assets), 3)
        for asset in assets:
            with self.subTest(asset=asset.name):
                first = asset.read_text().splitlines()[0]
                self.assertRegex(first, r"^<!-- fiducial \S+ @ %s \d{8}T\d{6}Z -->$" % head)
                self.assertNotIn("+local", first)


if __name__ == "__main__":
    unittest.main()
