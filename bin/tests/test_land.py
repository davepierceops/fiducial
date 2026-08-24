"""AC-LAND-T*: `bin/land` — the report contract and the divergence guard.

Contract: `specs/bin-land-trd.md` §5.2 (shape and serialization), §5.3 (the key
table and the one emission rule), §5.4 (AC-LAND-T01, T01a, T02, T03), §6 (the
eleven failure modes), §7 (the exit mapping).

Substrate, per TRD §4.1: **no mocked git.** Every case builds a real repository
with `git init` and a real bare repository served over `file://` as its
`origin`, so fetch, push and `ls-remote` drive the actual upload-pack /
receive-pack transport. The one exception is FM-1's `resolve` arm, which needs a
`git` that fetches and then fails `ls-remote`; that is a shim on a temporary
`PATH`, the mechanism TRD §4.2 B2 already names, and it is declared as
mock-verified where it is used.

Two boundaries this module does **not** represent, stated so the suite does not
overclaim:

- **B5, the repository's own pre-commit hook.** FM-6 is induced with a
  throwaway `exit 1` hook, which proves the tool does not pass `--no-verify`
  and that a hook refusal surfaces as FM-6's report. It does **not** prove
  anything about *this* repository's frontmatter hook, which the substrate
  never installs (TRD §4.2 B5).
- **B1's provider half.** `file://` exercises the wire protocol, not GitHub.

TRD §8's "Required integration points" asks for the bare-remote helpers to live
in `bin/tests/helpers.py` and for `land` to join `CLI_NAMES` and
`CLI_MINIMAL_ARGS`. Neither is done here: this module was written under a
directive that confines its edits to `bin/tests/test_land.py`, `bin/land`, and
new modules under `bin/aimeta/`. The helpers below are therefore local, and
moving them plus registering the CLI is left as stated work for the Coder.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import unittest

from tests.helpers import (
    DOCUMENTED_EXIT_CODES,
    base_env,
    commit,
    git,
    make_repo,
    no_traceback,
    run_cli,
    temp_dir,
    write,
)

# --------------------------------------------------------------- the contract

#: TRD §5.2: the five contract keys plus `detail`, always present, on every path.
TOP_LEVEL_KEYS = sorted(
    ["branch", "head", "prior_head", "files", "verification", "detail"]
)

#: TRD §5.2: the two of Core's four classes PRD G6 permits the tool to emit.
CLASSES = ("observed", "unknown")

#: TRD §5.3: "Nine tokens and no others."
STAGE_TOKENS = (
    "fetch",
    "resolve",
    "base-object",
    "guard",
    "base",
    "stage",
    "commit",
    "push",
    "verify",
)

SHA_RE = re.compile(r"\A[0-9a-f]{40}\Z")

ZEROS = "0" * 40


# ------------------------------------------------------------ substrate (§4.1)


def remote_url(bare):
    """A `file://` URL, not a bare path: git takes local shortcuts for a path."""
    return "file://%s" % pathlib.Path(bare).resolve()


def make_bare_remote(case, parent, name="origin.git"):
    """A bare repository to serve as `origin` over `file://` (TRD §4.1)."""
    path = pathlib.Path(parent) / name
    path.mkdir(parents=True, exist_ok=True)
    git(path, "init", "-q", "--bare", "-b", "main", check=True)
    return path


def remote_ref_sha(bare, branch, env=None):
    """The SHA the bare repo holds for `branch`, or None — the read-back oracle."""
    rc, out, _ = git(
        bare, "rev-parse", "--verify", "--quiet", "refs/heads/%s" % branch, env=env
    )
    return out.strip() or None


def install_hook(hooks_dir, name, script):
    """Drop an executable hook. Used for FM-6 (local) and FM-7/FM-8 (remote)."""
    path = pathlib.Path(hooks_dir)
    path.mkdir(parents=True, exist_ok=True)
    hook = path / name
    hook.write_text(script, encoding="utf-8")
    hook.chmod(0o755)
    return hook


def git_shim_path(case, failing):
    """A PATH whose `git` fails one subcommand and execs the real one otherwise.

    Mock-verified, and only where a real substrate cannot produce the state:
    FM-1's `resolve` arm needs `fetch` to succeed and `ls-remote` to fail
    against the same origin, which no reachable `file://` remote does.
    """
    real = shutil.which("git")
    if real is None:  # pragma: no cover - environment sanity
        raise AssertionError("cannot build a git shim without git on PATH")
    directory = temp_dir(case, "aimeta-land-shim-")
    shim = directory / "git"
    shim.write_text(
        "#!/bin/sh\n"
        'if [ "$1" = "%s" ]; then\n'
        '  echo "shim: refusing %s" >&2\n'
        "  exit 128\n"
        "fi\n"
        'exec "%s" "$@"\n' % (failing, failing, real),
        encoding="utf-8",
    )
    shim.chmod(0o755)
    return directory


class Substrate:
    """A repo on `main`, one seed commit, and a bare `file://` origin holding it."""

    def __init__(self, case, name="proj"):
        self.case = case
        self.sandbox = temp_dir(case, "aimeta-land-")
        self.env = base_env()
        self.bare = make_bare_remote(case, self.sandbox)
        self.repo = make_repo(case, name=name, parent=self.sandbox)
        write(self.repo, "seed.md", "seed\n")
        self.main_sha = commit(self.repo, "seed", env=self.env)
        git(
            self.repo,
            "remote",
            "add",
            "origin",
            remote_url(self.bare),
            env=self.env,
            check=True,
        )
        git(self.repo, "push", "-q", "origin", "main", env=self.env, check=True)

    # -- setup moves ------------------------------------------------------

    def seed_remote_branch(self, branch, relpath="remote.md", text="remote work\n"):
        """Advance `branch` at the remote from a *second* clone.

        Deliberately not from `self.repo`: the point of several cases is that
        the landing base is remote state this repo has never held.
        """
        other = self.sandbox / ("other-%s" % branch)
        git(
            self.sandbox,
            "clone",
            "-q",
            remote_url(self.bare),
            str(other),
            env=self.env,
            check=True,
        )
        for key, value in (
            ("user.email", "tests@example.invalid"),
            ("user.name", "AI Methodology Tests"),
            ("commit.gpgsign", "false"),
        ):
            git(other, "config", key, value, env=self.env, check=True)
        git(other, "checkout", "-q", "-b", branch, env=self.env, check=True)
        write(other, relpath, text)
        git(other, "add", "-A", env=self.env, check=True)
        git(other, "commit", "-q", "--no-verify", "-m", "remote work", env=self.env,
            check=True)
        git(other, "push", "-q", "origin", branch, env=self.env, check=True)
        return git(other, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()

    def track_remote_branch(self, branch):
        """Fetch and stand on a local branch at the remote branch's head."""
        git(self.repo, "fetch", "-q", "origin", env=self.env, check=True)
        git(
            self.repo,
            "checkout",
            "-q",
            "-b",
            branch,
            "origin/%s" % branch,
            env=self.env,
            check=True,
        )

    def local_commit(self, relpath, text, message="local work"):
        write(self.repo, relpath, text)
        return commit(self.repo, message, env=self.env)

    def head(self):
        return git(self.repo, "rev-parse", "HEAD", env=self.env, check=True)[1].strip()

    def branch_sha(self, branch):
        rc, out, _ = git(
            self.repo, "rev-parse", "--verify", "--quiet", "refs/heads/%s" % branch,
            env=self.env,
        )
        return out.strip() or None

    def current_branch(self):
        return git(
            self.repo, "rev-parse", "--abbrev-ref", "HEAD", env=self.env, check=True
        )[1].strip()

    def land(self, *args, env=None):
        return run_cli("land", *args, cwd=self.repo, env=env or self.env)


class Landing:
    """One invocation of `bin/land`, plus the substrate it ran against."""

    def __init__(self, sub, rc, out, err, **facts):
        self.sub = sub
        self.rc = rc
        self.out = out
        self.err = err
        self.facts = facts

    def __getitem__(self, key):
        return self.facts[key]


# ------------------------------------------------------------- the case set
#
# TRD §5.4 AC-LAND-T01's enumeration: the success path and every failure mode
# of §6 except FM-10. FM-9 is absent from this list and has no builder; see
# `TestUnreachableCases` for why.

BRANCH = "feat"


def build_success_created(case):
    """Success, G1's first arm: `<branch>` absent at the remote, HEAD on `main`."""
    sub = Substrate(case)
    write(sub.repo, "work.md", "landed\n")
    before = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, local_head=before, base=sub.main_sha,
                   prior_branch="main")


def build_success_existing(case):
    """Success, G1's second arm: `<branch>` present, HEAD already on it."""
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    sub.track_remote_branch(BRANCH)
    write(sub.repo, "work.md", "landed\n")
    before = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, local_head=before, base=remote_sha,
                   prior_head=remote_sha)


def build_fm1_fetch(case):
    """FM-1 at step 2: `git fetch origin` cannot reach the remote."""
    sub = Substrate(case)
    missing = sub.sandbox / "no-such-remote.git"
    git(sub.repo, "remote", "set-url", "origin", remote_url(missing), env=sub.env,
        check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err)


def build_fm1_resolve(case):
    """FM-1 at step 3: the fetch succeeds and the remote read fails.

    Mock-verified: a `git` shim on a temporary PATH. No reachable `file://`
    remote produces a working `fetch` and a failing `ls-remote`.
    """
    sub = Substrate(case)
    shim = git_shim_path(case, "ls-remote")
    env = base_env(PATH="%s%s%s" % (shim, os.pathsep, os.environ.get("PATH", "")))
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, "land the work", "work.md", env=env)
    return Landing(sub, rc, out, err)


def build_fm2(case):
    """FM-2: `ls-remote` names a base whose object the local repo does not have.

    Induced by narrowing `remote.origin.fetch` to `main`, the cause TRD §3.2
    step 4 records as *observed* — the tool asserts no cause, so any of the
    three produces the same refusal.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    git(sub.repo, "config", "remote.origin.fetch",
        "+refs/heads/main:refs/remotes/origin/main", env=sub.env, check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha)


def build_fm3_head_diverged(case):
    """FM-3, first check: local HEAD carries a commit the base does not.

    §3.2 step 5 short-circuits here, so `<branch>`'s SHA is never read and
    `detail.branch_head` is absent — a claim under §5.3's emission rule.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    local_head = sub.local_commit("extra.md", "only here\n")
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm3_branch_diverged(case):
    """FM-3, second check: the local `<branch>` diverges, HEAD is elsewhere.

    This is AC-LAND-T03's given. `detail.branch_head` is established here and
    only here.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    sub.track_remote_branch(BRANCH)
    branch_tip = sub.local_commit("unpushed.md", "not at the remote\n")
    git(sub.repo, "checkout", "-q", "main", env=sub.env, check=True)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head, branch_head=branch_tip)


def build_fm4(case):
    """FM-4: a locally-modified file whose committed content differs base vs HEAD."""
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH, relpath="seed.md",
                                        text="the remote version\n")
    write(sub.repo, "seed.md", "the local edit\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "seed.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm5_stage(case):
    """FM-5 stopping at step 7: a named path does not exist, so `git add` fails."""
    sub = Substrate(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "absent.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_branch="main")


def build_fm5_commit(case):
    """FM-5 stopping at step 8: nothing is staged, so `git commit` fails."""
    sub = Substrate(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_branch="main")


def build_fm6(case):
    """FM-6: a repository hook refuses the commit.

    Boundary: this is a throwaway `exit 1` hook, not this repository's
    frontmatter hook. It proves the tool does not pass `--no-verify` and that
    a hook refusal reaches FM-6's report; TRD §4.2 B5 stays **assumed**.
    """
    sub = Substrate(case)
    install_hook(sub.repo / ".git" / "hooks", "pre-commit",
                 "#!/bin/sh\necho 'hook refuses' >&2\nexit 1\n")
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_branch="main")


def build_fm7(case):
    """FM-7: the remote's `pre-receive` rejects the push. The local commit stays."""
    sub = Substrate(case)
    install_hook(sub.bare / "hooks", "pre-receive",
                 "#!/bin/sh\necho 'receive refuses' >&2\nexit 1\n")
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_branch="main", committed_paths=["work.md"])


def build_fm8(case):
    """FM-8: the push exits 0 and `ls-remote` then disagrees with the pushed head.

    Induced by a remote `post-receive` that resets the ref to its prior value:
    receive-pack has already answered, so the push succeeds, and the ref the
    tool reads back is not the one it wrote.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    sub.track_remote_branch(BRANCH)
    install_hook(
        sub.bare / "hooks",
        "post-receive",
        "#!/bin/sh\n"
        "while read old new ref; do\n"
        '  if [ "$old" != "%s" ]; then\n'
        '    git update-ref "$ref" "$old"\n'
        "  fi\n"
        "done\n" % ZEROS,
    )
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head, remote_head=remote_sha,
                   committed_paths=["work.md"])


def build_fm11(case):
    """FM-11: the remote read succeeds and neither `<branch>` nor `main` is there."""
    sub = Substrate(case)
    empty = make_bare_remote(case, sub.sandbox, name="empty.git")
    git(sub.repo, "remote", "set-url", "origin", remote_url(empty), env=sub.env,
        check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, "land the work", "work.md")
    return Landing(sub, rc, out, err)


#: Every case AC-LAND-T01 enumerates that this substrate can reach.
BUILDERS = [
    ("success-created", build_success_created),
    ("success-existing", build_success_existing),
    ("fm1-fetch", build_fm1_fetch),
    ("fm1-resolve", build_fm1_resolve),
    ("fm2", build_fm2),
    ("fm3-head-diverged", build_fm3_head_diverged),
    ("fm3-branch-diverged", build_fm3_branch_diverged),
    ("fm4", build_fm4),
    ("fm5-stage", build_fm5_stage),
    ("fm5-commit", build_fm5_commit),
    ("fm6", build_fm6),
    ("fm7", build_fm7),
    ("fm8", build_fm8),
    ("fm11", build_fm11),
]

#: §5.3's token table, per case. Absent = no failure, so no `detail.stage`.
EXPECTED_STAGE = {
    "fm1-fetch": "fetch",
    "fm1-resolve": "resolve",
    "fm2": "base-object",
    "fm3-head-diverged": "guard",
    "fm3-branch-diverged": "guard",
    "fm4": "base",
    "fm5-stage": "stage",
    "fm5-commit": "commit",
    "fm6": "commit",
    "fm7": "push",
    "fm8": "verify",
    "fm11": "resolve",
}

#: §7's exit mapping. FM-7's `1` is what §7 states; OQ-10 leaves the constant open.
EXPECTED_EXIT = {
    "success-created": 0,
    "success-existing": 0,
    "fm1-fetch": 3,
    "fm1-resolve": 3,
    "fm2": 3,
    "fm3-head-diverged": 3,
    "fm3-branch-diverged": 3,
    "fm4": 3,
    "fm5-stage": 3,
    "fm5-commit": 3,
    "fm6": 3,
    "fm7": 1,
    "fm8": 4,
    "fm11": 3,
}


# ------------------------------------------------------- shared assertions


class ReportAssertions(unittest.TestCase):
    """§5.2's format and value domains, and §5.3's one emission rule."""

    # -- §5.2 serialization ------------------------------------------------

    def parse(self, landing):
        """`json.loads` on stdout, with §5.2's format rules asserted first."""
        out = landing.out
        self.assertTrue(out, "stdout was empty; stderr=%r" % landing.err)
        self.assertTrue(no_traceback(landing.out, landing.err),
                        "traceback: %s" % landing.err)
        # "stdout carries no text outside that object" (AC-LAND-T01): the whole
        # stream is the object, and `json.loads` refuses trailing data.
        self.assertTrue(out.startswith("{"), "stdout does not open the object: %r"
                        % out[:80])
        self.assertTrue(out.endswith("\n"), "no trailing newline")
        self.assertFalse(out.endswith("\n\n"), "more than one trailing newline")
        try:
            report = json.loads(out)
        except ValueError as exc:
            raise AssertionError("stdout did not parse as JSON (%s): %r" % (exc, out))
        self.assertIsInstance(report, dict, "the parsed value is not an object")
        self.assert_two_space_indent(out)
        self.assert_sorted_keys(out)
        return report

    def assert_two_space_indent(self, text):
        """§5.2: pretty-printed with two-space indentation."""
        for lineno, line in enumerate(text.splitlines()[1:], start=2):
            lead = len(line) - len(line.lstrip(" "))
            self.assertNotIn("\t", line, "line %d is tab-indented" % lineno)
            self.assertEqual(lead % 2, 0,
                             "line %d is indented %d spaces" % (lineno, lead))
        self.assertIn('\n  "', text, "no two-space indented key found")

    def assert_sorted_keys(self, text):
        """§5.2: sorted keys, at every level."""
        orders = []

        def hook(pairs):
            orders.append([key for key, _ in pairs])
            return dict(pairs)

        json.loads(text, object_pairs_hook=hook)
        for order in orders:
            self.assertEqual(order, sorted(order), "keys are not sorted: %r" % order)

    # -- §5.2 value domains ------------------------------------------------

    def assert_leaf(self, leaf, label):
        """Every leaf carries `value` and `class`; `unknown` implies `null`."""
        self.assertIsInstance(leaf, dict, "%s is not a leaf object" % label)
        self.assertEqual(sorted(leaf), ["class", "value"],
                         "%s carries %r" % (label, sorted(leaf)))
        self.assertIn(leaf["class"], CLASSES, "%s class=%r" % (label, leaf["class"]))
        if leaf["class"] == "unknown":
            self.assertIsNone(leaf["value"], "%s is unknown but carries a value"
                              % label)

    def assert_value_domains(self, report):
        """§5.2's whole rule list, on any path."""
        self.assertEqual(sorted(report), TOP_LEVEL_KEYS,
                         "top-level keys are %r" % sorted(report))
        for name in ("branch", "head", "prior_head", "verification"):
            self.assert_leaf(report[name], name)
        self.assertIsInstance(report["detail"], dict, "detail is not an object")
        for key, leaf in sorted(report["detail"].items()):
            self.assert_leaf(leaf, "detail.%s" % key)

        # `prior_head.value` is a 40-hex SHA, `created`, or null.
        prior = report["prior_head"]["value"]
        self.assertTrue(
            prior is None or prior == "created" or bool(SHA_RE.match(str(prior))),
            "prior_head.value=%r" % prior,
        )
        # `verification.value` is complete, incomplete, or null.
        self.assertIn(report["verification"]["value"],
                      ("complete", "incomplete", None),
                      "verification.value=%r" % report["verification"]["value"])
        # `head.value` is a SHA or null; §5.3 says it is the commit step 8 made.
        head = report["head"]["value"]
        self.assertTrue(head is None or bool(SHA_RE.match(str(head))),
                        "head.value=%r" % head)

        # `files` is a list; no `class` on the list, no union type.
        files = report["files"]
        self.assertIsInstance(files, list, "files is not a list")
        for entry in files:
            self.assertIsInstance(entry, dict, "files entry %r" % entry)
            self.assertEqual(sorted(entry), ["class", "match", "path"],
                             "files entry carries %r" % sorted(entry))
            self.assertNotIn("value", entry, "a files entry names its value `value`")
            self.assertIn(entry["class"], CLASSES)
            self.assertIn(entry["match"], (True, False, None),
                          "match=%r" % entry["match"])
            if entry["class"] == "unknown":
                self.assertIsNone(entry["match"],
                                  "%s is unknown but carries a match" % entry["path"])
            self.assertIsInstance(entry["path"], str)

        # §5.3's closed token set.
        if "stage" in report["detail"]:
            self.assertIn(report["detail"]["stage"]["value"], STAGE_TOKENS,
                          "stage=%r" % report["detail"]["stage"]["value"])

    # -- §5.3's one emission rule -----------------------------------------

    def assert_emission(self, report, established, detail_keys):
        """The "Established on" column read as a ceiling as well as a floor.

        `established` names the contract fields (other than `files`) the table
        establishes on this path; every other contract field must be present
        with `value: null` and `class: "unknown"`. `detail_keys` is the exact
        key set of `detail`.
        """
        for name in ("branch", "head", "prior_head", "verification"):
            expected = "observed" if name in established else "unknown"
            self.assertEqual(
                report[name]["class"], expected,
                "%s is %r, expected %r" % (name, report[name]["class"], expected),
            )
            if expected == "unknown":
                self.assertIsNone(report[name]["value"], "%s carries a value" % name)
        self.assertEqual(
            sorted(report["detail"]), sorted(detail_keys),
            "detail keys are %r, expected %r"
            % (sorted(report["detail"]), sorted(detail_keys)),
        )

    def assert_files(self, report, expected):
        """`expected`: list of `(path, match, class)` triples, order-insensitive."""
        got = sorted((e["path"], e["match"], e["class"]) for e in report["files"])
        self.assertEqual(got, sorted(expected), "files=%r" % report["files"])

    def assert_detail(self, report, key, value):
        leaf = report["detail"][key]
        self.assertEqual(leaf["class"], "observed", "detail.%s is unknown" % key)
        self.assertEqual(leaf["value"], value, "detail.%s=%r" % (key, leaf["value"]))

    def assert_exit(self, landing, expected, name):
        self.assertIn(landing.rc, DOCUMENTED_EXIT_CODES,
                      "%s exited %s" % (name, landing.rc))
        self.assertEqual(landing.rc, expected,
                         "%s exited %s; stderr=%r" % (name, landing.rc, landing.err))

    def assert_diagnostic(self, landing):
        """§7: a bracket-coded diagnostic on stderr on every failure path."""
        self.assertTrue(landing.err.strip(), "the failure was silent on stderr")

    def check(self, landing, name, established, detail_keys, files):
        """The whole of AC-LAND-T01 for one case, plus §7's exit code."""
        report = self.parse(landing)
        self.assert_value_domains(report)
        self.assert_emission(report, established, detail_keys)
        self.assert_files(report, files)
        self.assert_exit(landing, EXPECTED_EXIT[name], name)
        if name in EXPECTED_STAGE:
            self.assert_stage(report, EXPECTED_STAGE[name])
            self.assert_diagnostic(landing)
        return report

    def assert_stage(self, report, token):
        """§5.3: `detail.stage` names the step of §3.2 that stopped the sequence."""
        self.assertIn("stage", report["detail"],
                      "the failure report names no stage; detail=%r"
                      % sorted(report["detail"]))
        self.assertEqual(report["detail"]["stage"]["value"], token)


# ------------------------------------------------- AC-LAND-T01, case by case


class TestT01SuccessPath(ReportAssertions):
    def test_t01_case_success_branch_created(self):
        """AC-LAND-T01 / §5.3, success path, G1 first arm, HEAD moved off `main`."""
        landing = build_success_created(self)
        report = self.check(
            landing,
            "success-created",
            established=("branch", "head", "prior_head", "verification"),
            detail_keys=("base", "local_head", "prior_branch", "remote_head"),
            files=[("work.md", True, "observed")],
        )
        self.assertEqual(report["branch"]["value"], BRANCH)
        self.assertEqual(report["prior_head"]["value"], "created")
        self.assertEqual(report["verification"]["value"], "complete")
        self.assertEqual(report["head"]["value"],
                         remote_ref_sha(landing.sub.bare, BRANCH))
        self.assertEqual(report["head"]["value"], landing.sub.head())
        self.assert_detail(report, "base", landing["base"])
        self.assert_detail(report, "local_head", landing["local_head"])
        self.assert_detail(report, "prior_branch", "main")
        self.assert_detail(report, "remote_head", report["head"]["value"])

    def test_t01_case_success_branch_existing_head_already_on_branch(self):
        """AC-LAND-T01 / §5.3, success path, G1 second arm, no `prior_branch`.

        This is the row condition on `detail.prior_branch`: step 6 found HEAD
        already on `<branch>`, so it moved HEAD off nothing.
        """
        landing = build_success_existing(self)
        report = self.check(
            landing,
            "success-existing",
            established=("branch", "head", "prior_head", "verification"),
            detail_keys=("base", "local_head", "remote_head"),
            files=[("work.md", True, "observed")],
        )
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])
        self.assertEqual(report["verification"]["value"], "complete")
        self.assertEqual(report["head"]["value"],
                         remote_ref_sha(landing.sub.bare, BRANCH))
        self.assert_detail(report, "base", landing["base"])


class TestT01FailureModes(ReportAssertions):
    def test_t01_case_fm1_remote_read_fails_at_fetch(self):
        """AC-LAND-T01 / §6 FM-1 at step 2: only `branch` and the stop are established."""
        landing = build_fm1_fetch(self)
        report = self.check(
            landing, "fm1-fetch",
            established=("branch",),
            detail_keys=("stage", "git_status"),
            files=[],
        )
        self.assertEqual(report["branch"]["value"], BRANCH)
        self.assertNotEqual(report["detail"]["git_status"]["value"], 0)

    def test_t01_case_fm1_remote_read_fails_at_resolve(self):
        """AC-LAND-T01 / §6 FM-1 at step 3: same shape, `resolve` token.

        Mock-verified via a `git` shim; see `git_shim_path`.
        """
        landing = build_fm1_resolve(self)
        self.check(
            landing, "fm1-resolve",
            established=("branch",),
            detail_keys=("stage", "git_status"),
            files=[],
        )

    def test_t01_case_fm2_base_object_absent_locally(self):
        """AC-LAND-T01 / §6 FM-2: `prior_head` and `base` established, nothing beyond."""
        landing = build_fm2(self)
        report = self.check(
            landing, "fm2",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "git_status"),
            files=[],
        )
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])
        self.assert_detail(report, "base", landing["base"])

    def test_t01_case_fm3_first_check_refuses_without_branch_head(self):
        """AC-LAND-T01 / §6 FM-3, first check: `detail.branch_head` is **absent**.

        §5.3's emission rule makes that absence a claim: the guard stopped
        before `<branch>`'s SHA was read.
        """
        landing = build_fm3_head_diverged(self)
        report = self.check(
            landing, "fm3-head-diverged",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "git_status"),
            files=[],
        )
        self.assertNotIn("branch_head", report["detail"])
        self.assert_detail(report, "local_head", landing["local_head"])

    def test_t01_case_fm3_second_check_refuses_with_branch_head(self):
        """AC-LAND-T01 / §6 FM-3, second check: `detail.branch_head` established."""
        landing = build_fm3_branch_diverged(self)
        report = self.check(
            landing, "fm3-branch-diverged",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "branch_head", "git_status"),
            files=[],
        )
        self.assert_detail(report, "branch_head", landing["branch_head"])
        self.assert_detail(report, "local_head", landing["local_head"])

    def test_t01_case_fm4_base_establishment_fails(self):
        """AC-LAND-T01 / §6 FM-4: step 6 failed, so no `prior_branch`."""
        landing = build_fm4(self)
        report = self.check(
            landing, "fm4",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "git_status"),
            files=[],
        )
        self.assertNotIn("prior_branch", report["detail"])

    def test_t01_case_fm5_named_path_does_not_exist(self):
        """AC-LAND-T01 / §6 FM-5 stopping at step 7 — the `stage` token."""
        landing = build_fm5_stage(self)
        report = self.check(
            landing, "fm5-stage",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "git_status", "prior_branch"),
            files=[],
        )
        self.assert_detail(report, "prior_branch", "main")

    def test_t01_case_fm5_staged_set_is_empty(self):
        """AC-LAND-T01 / §6 FM-5 stopping at step 8 — the `commit` token."""
        landing = build_fm5_commit(self)
        self.check(
            landing, "fm5-commit",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "git_status", "prior_branch"),
            files=[],
        )

    def test_t01_case_fm6_hook_refuses_the_commit(self):
        """AC-LAND-T01 / §6 FM-6. Boundary: a throwaway hook, not B5's real one."""
        landing = build_fm6(self)
        self.check(
            landing, "fm6",
            established=("branch", "prior_head"),
            detail_keys=("stage", "base", "local_head", "git_status", "prior_branch"),
            files=[],
        )

    def test_t01_case_fm7_push_fails_leaving_a_local_commit(self):
        """AC-LAND-T01 / §6 FM-7: `head` observed, `verification` incomplete,
        `files` carrying one unknown entry per committed path."""
        landing = build_fm7(self)
        report = self.check(
            landing, "fm7",
            established=("branch", "prior_head", "head", "verification"),
            detail_keys=("stage", "base", "local_head", "git_status", "prior_branch"),
            files=[("work.md", None, "unknown")],
        )
        self.assertEqual(report["verification"]["value"], "incomplete")
        self.assertEqual(report["head"]["value"], landing.sub.head())
        self.assertIsNone(remote_ref_sha(landing.sub.bare, BRANCH),
                          "the push was rejected but the ref moved")

    def test_t01_case_fm8_ls_remote_disagrees_with_the_pushed_head(self):
        """AC-LAND-T01 / §6 FM-8: `remote_head` established, no `git_status`."""
        landing = build_fm8(self)
        report = self.check(
            landing, "fm8",
            established=("branch", "prior_head", "head", "verification"),
            detail_keys=("stage", "base", "local_head", "remote_head"),
            files=[("work.md", None, "unknown")],
        )
        self.assertEqual(report["verification"]["value"], "incomplete")
        self.assertNotEqual(report["head"]["value"],
                            report["detail"]["remote_head"]["value"])
        self.assert_detail(report, "remote_head", landing["remote_head"])

    def test_t01_case_fm11_remote_read_names_no_base(self):
        """AC-LAND-T01 / §6 FM-11: `prior_head` is `created` and nothing further."""
        landing = build_fm11(self)
        report = self.check(
            landing, "fm11",
            established=("branch", "prior_head"),
            detail_keys=("stage",),
            files=[],
        )
        self.assertEqual(report["prior_head"]["value"], "created")


class TestT01AcrossEveryCase(ReportAssertions):
    """The format half of AC-LAND-T01, asserted once over the whole enumeration."""

    def test_t01_every_case_parses_and_holds_the_value_domains(self):
        """AC-LAND-T01 / §5.2: parseable, exact key set, domains, on every path."""
        for name, builder in BUILDERS:
            with self.subTest(case=name):
                landing = builder(self)
                report = self.parse(landing)
                self.assert_value_domains(report)

    def test_t01_stage_tokens_are_the_nine_and_the_right_one(self):
        """§5.3's token table: closed set, and the token of the step that stopped."""
        for name, builder in BUILDERS:
            with self.subTest(case=name):
                landing = builder(self)
                report = self.parse(landing)
                expected = EXPECTED_STAGE.get(name)
                if expected is None:
                    self.assertNotIn("stage", report["detail"],
                                     "the success path carries a stage token")
                else:
                    self.assert_stage(report, expected)


class TestT01aUsageError(ReportAssertions):
    """AC-LAND-T01a — the usage-error path emits no report."""

    def setUp(self):
        self.sub = Substrate(self)

    def test_t01a_missing_arguments_write_nothing_to_stdout(self):
        """AC-LAND-T01a: stdout empty, stderr non-empty, exit 2."""
        rc, out, err = self.sub.land()
        self.assertEqual(out, "", "a usage error wrote to stdout: %r" % out)
        self.assertTrue(err.strip(), "the usage error was silent on stderr")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_t01a_missing_message_writes_nothing_to_stdout(self):
        """AC-LAND-T01a: a branch with no message is still a usage error."""
        rc, out, err = self.sub.land(BRANCH)
        self.assertEqual(out, "", "a usage error wrote to stdout: %r" % out)
        self.assertTrue(err.strip())
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_t01a_no_traceback_on_a_usage_error(self):
        """§7/AC-X-6: the usage error is a diagnostic, never a traceback."""
        rc, out, err = self.sub.land()
        self.assertTrue(no_traceback(out, err), "traceback: %s" % err)


class TestT02VerificationAndExitAgree(ReportAssertions):
    """AC-LAND-T02 — exit 0 iff `verification.value` is `"complete"`."""

    def test_t02_exit_zero_iff_verification_is_complete(self):
        """AC-LAND-T02, across AC-LAND-T01's enumeration."""
        for name, builder in BUILDERS:
            with self.subTest(case=name):
                landing = builder(self)
                report = self.parse(landing)
                complete = report["verification"]["value"] == "complete"
                self.assertEqual(
                    landing.rc == 0, complete,
                    "%s: rc=%s verification=%r"
                    % (name, landing.rc, report["verification"]),
                )

    def test_t02_a_non_zero_exit_never_claims_a_complete_verification(self):
        """AC-LAND-T02, the direction PRD §7 puts under "Not accepted"."""
        for name, builder in BUILDERS:
            if EXPECTED_EXIT[name] == 0:
                continue
            with self.subTest(case=name):
                landing = builder(self)
                report = self.parse(landing)
                self.assertNotEqual(report["verification"]["value"], "complete",
                                    "%s reported a complete verification" % name)


class TestT03GuardRefusesOnTheNamedBranch(ReportAssertions):
    """AC-LAND-T03 — the guard refuses when `<branch>`, not HEAD, diverges."""

    def setUp(self):
        self.sub = Substrate(self)
        self.remote_sha = self.sub.seed_remote_branch(BRANCH)
        self.sub.track_remote_branch(BRANCH)
        self.branch_tip = self.sub.local_commit("unpushed.md", "not at the remote\n")
        git(self.sub.repo, "checkout", "-q", "main", env=self.sub.env, check=True)
        write(self.sub.repo, "work.md", "landed\n")
        self.head_before = self.sub.head()
        self.rc, self.out, self.err = self.sub.land(BRANCH, "land the work", "work.md")
        self.landing = Landing(self.sub, self.rc, self.out, self.err)

    def test_t03_stops_in_fm3_shape_with_the_branch_tip_named(self):
        """AC-LAND-T03: `detail.stage` is `guard` and `branch_head` is the prior tip."""
        report = self.parse(self.landing)
        self.assert_stage(report, "guard")
        self.assertIn("branch_head", report["detail"],
                      "the refusal does not name the branch tip; detail=%r"
                      % sorted(report["detail"]))
        self.assert_detail(report, "branch_head", self.branch_tip)

    def test_t03_exit_status_is_three(self):
        """AC-LAND-T03: "the exit status is 3"."""
        self.assertEqual(self.rc, 3, "stdout=%r stderr=%r" % (self.out, self.err))

    def test_t03_no_ref_moved_and_no_commit_exists(self):
        """AC-LAND-T03: nothing staged, no ref moved, no commit made."""
        self.assertEqual(self.sub.head(), self.head_before, "local HEAD moved")
        self.assertEqual(self.sub.current_branch(), "main", "HEAD left `main`")
        self.assertEqual(self.sub.branch_sha(BRANCH), self.branch_tip,
                         "the named branch was rewritten")
        self.assertEqual(remote_ref_sha(self.sub.bare, BRANCH), self.remote_sha,
                         "the remote ref moved")

    def test_t03_the_prior_tip_is_still_reachable_from_the_branch(self):
        """AC-LAND-T03: "that prior tip is still reachable from `<branch>`"."""
        rc, out, _ = git(self.sub.repo, "merge-base", "--is-ancestor",
                         self.branch_tip, BRANCH, env=self.sub.env)
        self.assertEqual(rc, 0, "the prior tip was orphaned")

    def test_t03_nothing_was_staged(self):
        """AC-LAND-T03: "stops before anything is staged"."""
        rc, out, _ = git(self.sub.repo, "diff", "--cached", "--name-only",
                         env=self.sub.env)
        self.assertEqual(out.strip(), "", "the index was written: %r" % out)


class TestUnreachableCases(unittest.TestCase):
    """Cases AC-LAND-T01 enumerates that no test on this substrate can produce."""

    def test_t01_case_fm9_per_file_mismatch_is_not_inducible(self):
        """§6 FM-9 against §4.3: unreachable under git transport, so untested.

        §4.3: "under git's content addressing a commit SHA determines its tree,
        so once `ls-remote` returns the same commit SHA the tool pushed, the
        per-file blob SHAs necessarily agree ... It cannot fail where that
        check passed." Step 10 checks `ls-remote` first, so any mutation of the
        bare repository between push and verification surfaces as FM-8. This
        test is a marker for a gap in the criterion, not coverage of it.
        """
        self.skipTest(
            "FM-9 is unreachable end to end: §4.3 proves the per-file comparison "
            "cannot fail where step 10's ls-remote check passed, and §4.1's "
            "mutate-the-bare-repo helper produces FM-8 instead. Reported as a "
            "finding against §4.1/§4.3/§5.4."
        )

    def test_t01_case_fm10_is_outside_the_enumeration_by_construction(self):
        """§6 FM-10: excluded by AC-LAND-T01 itself; recorded so §6 reads whole."""
        self.skipTest(
            "FM-10 emits no report by construction (§3.2 step 11), and "
            "AC-LAND-T01 excludes it from its own enumeration."
        )


if __name__ == "__main__":
    unittest.main()
