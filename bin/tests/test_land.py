r"""AC-LAND-T*: `bin/land` — the report contract and the divergence guard.

Contract: `specs/bin-land-trd.md` §5.2 (shape, serialization, and the value
domains), §5.3 (the key table, the token table, and the one emission rule),
§5.4 (AC-LAND-T01, T01a, T01b, T02, T03), §6 (the failure modes — FM-1 through
FM-8, then FM-10, then FM-11, with nothing at 9), §7 (the exit mapping, and the
diagnostic-code table that is this repository's single statement of which
refusal carries which code).

**The unit is the terminal path, not the failure mode** (§5.4). The nineteen
cases below are derived from §5.3's two tables plus §5.4's splitting rule; the
derivation is written out above `CASES`.

Substrate, per TRD §4.1: **no mocked git.** Every case builds a real repository
with `git init` and a real bare repository served over `file://` as its
`origin`, so fetch, push and `ls-remote` drive the actual upload-pack /
receive-pack transport.

Verification boundary, per TRD §5.4: **end to end.** Each case is a real
invocation of `bin/land` as a process, and the stdout asserted on is that
process's own. Nothing here calls `Report.build` with synthetic facts: two of
AC-LAND-T01's assertions can be made no other way — that stdout carries no text
outside the object is a claim about what the tool writes, and AC-LAND-T02 binds
an exit status, which exists only where a process ran. The separate property
§3.1 and §3.7 buy from the `land.py`/`report.py` split — that every report shape
is constructible without a landing — is architectural and is not this module's
boundary.

Evidence classes, per §4.2, where they differ case by case:

- **B1, the remote git service — contract-verified.** `file://` exercises the
  git wire protocol and the exit-status contract for real; the provider is not
  exercised. Nothing here proves live credentials, provider availability,
  provider-side ref policies, or behaviour under a concurrent push.
- **FM-1's `resolve` case — mock-verified.** It needs a remote read that fails
  after a fetch that succeeded, which one bare repository cannot produce; it is
  induced with a `git` shim on a temporary `PATH`, the mechanism §4.2's B2
  already uses `fake_path_dir` for. Declared again at the point of use.
- **FM-6's two cases — B5 stays *assumed*, and these do not raise it.** The
  `pre-commit` hook installed into the substrate repository is a **stand-in that
  refuses**, not this repository's own (§4.2 B5). What these cases establish is
  the report's shape and status on that path — a property of the tool rather
  than of the hook. They establish nothing about whether this repository's
  `pre-commit` hook refuses the commits it exists to refuse, whether it refuses
  them by exiting non-zero, or whether its own diagnostics stay off stdout.
- **FM-7's two cases — a stand-in for a provider-side refusal.** The push is
  refused by a `pre-receive` hook installed into the bare repository. That is
  the receive-pack refusal contract exercised for real, and it stands in for the
  provider-side ref policy §4.2's B1 lists under "does not prove". §5.4 names
  only FM-6's hook and FM-1's shim as needing something the plain substrate does
  not supply; this is a third, and it is declared here rather than passed off as
  substrate. Reported as a finding.
- **FM-8's two cases** mutate the bare repository between the push and the
  verification, with a `post-receive` hook that restores the prior ref. §4.1
  names that mutation as a required substrate helper, so it is substrate rather
  than a stand-in.

**The diagnostic codes are asserted by identity, not by presence.** §7 now
carries a twelve-row table and calls it "this document's single statement of
which refusal carries which code", normative over every other passage. So
`assert_diagnostic` asserts *which* code a refusal put on stderr, and
`DIAGNOSTIC_CODES` below transcribes the table's twelve. That closed OQ-12, and
what it bought is AC-LAND-T01b: before it, a criterion could have asserted only that
*some* bracketed code was there, and would have passed two implementations whose
codes disagreed.

Two counts differ from the nineteen, and §7 states both rather than leaving them
to be discovered. **Twelve codes over seventeen refusal paths**: the five
`detail.prior_branch` pairs share a code apiece, because that condition records
a side effect of a step that *succeeded* rather than a cause of the refusal, and
the session's repair is the same on both members. **The two success paths carry
no code at all**, there being no situation to answer. The tests here assert what
§7 states and not a finer discrimination it declined: both members of a shared
pair assert the *same* code, and no case asserts that a code appears on one path
alone.

The success-path assertion is deliberately the weaker of the two available.
T01b says stderr "carries no bracketed code at all" — **not** that stderr is
empty, and this module does not strengthen it. `git push` and `git fetch` write
progress and can write a credential-helper line to stderr on a landing that
worked perfectly, and a test demanding an empty stream would fail on the
environment rather than on the tool.

**The non-ASCII fixture, and why it stands beside the nineteen.** §5.2 now
settles what it once left open, in the decision that retired OQ-11: a non-ASCII
character in any value is written as a `\uXXXX` escape, the object being
serialized with `ensure_ascii=True`, so stdout is pure ASCII on every path
whatever a value carries. Every one of the nineteen cases above puts only ASCII
into its report, so not one of them can witness that rule — a stream that is
ASCII because nothing else went into it asserts nothing.
`TestT01NonAsciiValuesAreEscaped` therefore runs the success path once more with
a non-ASCII character in `branch`, and asserts the rule on the **process's raw
stdout bytes**, which is the only place the rule lives: a decoded string cannot
witness it, because the escaped form and the raw form decode to the same string.

It is **not a twentieth terminal path.** §5.4's enumeration is a fixed
nineteen, individuated by the report §5.3 gives each path; this is one of those
same paths exercised with different input, and `CASES` is untouched by it.

`branch` is the carrier, and a `files` path is deliberately **not** a second
one. §5.2 names both as caller-supplied text that can put a non-ASCII character
into the object, but macOS normalizes unicode filenames — NFD against NFC — so
an assertion routed through a filename can fail for a reason that belongs to the
platform rather than to the tool, and a red that means two things means neither.
`branch` comes straight from the invocation's argument (§3.7), is established on
every path a report is emitted at all (§5.3), and never touches the filesystem,
so nothing normalizes it. The residue is named rather than papered over: the
escape rule is asserted on one of the two carriers §5.2 names, and a defect that
escaped `branch` correctly while writing a `files` path raw would pass here.

TRD §8's "Required integration points" asks for the bare-remote helpers to live
in `bin/tests/helpers.py` and for `land` to join `CLI_NAMES` and
`CLI_MINIMAL_ARGS`. Neither is done here: this module is written under a
directive that confines its edits to `bin/tests/test_land.py` and the throwaway
stubs. The helpers below are therefore local, and moving them plus registering
the CLI is stated work for the Coder.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import unittest

from tests.helpers import (
    DOCUMENTED_EXIT_CODES,
    base_env,
    bracket_codes,
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

#: TRD §5.3's token table: "Ten tokens and no others." Step 8 carries two —
#: `nothing-staged` for FM-5's empty staged set, `commit` for FM-6's hook
#: refusal — which is why the token and not the step number is what is read.
STAGE_TOKENS = (
    "fetch",
    "resolve",
    "base-object",
    "guard",
    "base",
    "stage",
    "nothing-staged",
    "commit",
    "push",
    "verify",
)

#: TRD §7's diagnostic-code table: "Twelve codes, and no others." Transcribed
#: in the table's own row order, which is the sequence's order rather than
#: alphabetical, so this list can be read against §7 line by line.
#:
#: The table is normative over every other passage of the TRD by its own words,
#: so this is the only place in this module a code string is written down; each
#: `Case` names one of these and never a literal of its own.
DIAGNOSTIC_CODES = (
    "fetch-failed",          # step 2's fetch did not complete        — FM-1
    "remote-read-failed",    # step 3's read of the remote failed     — FM-1
    "no-base-at-remote",     # read succeeded, named neither ref      — FM-11
    "base-object-missing",   # resolved base absent from the odb      — FM-2
    "head-diverged",         # local HEAD carries a commit the base does not
    "branch-diverged",       # the local `<branch>` does, and step 6 would rewrite it
    "base-checkout-failed",  # step 6 could not put `<branch>` at the base — FM-4
    "path-not-found",        # a named path does not exist            — FM-5
    "nothing-staged",        # the staged set is empty                — FM-5
    "commit-refused",        # a repository hook refused the commit   — FM-6
    "push-rejected",         # step 9's push was rejected             — FM-7
    "remote-head-mismatch",  # `ls-remote` disagreed with the push    — FM-8
)

SHA_RE = re.compile(r"\A[0-9a-f]{40}\Z")

ZEROS = "0" * 40

BRANCH = "feat"

#: The throwaway `land` stub's relocated home — see
#: `docs/cycles/bin-land-stub-relocate-20260824T091500Z.md`. Not `BIN_DIR`
#: itself: the stub is deliberately not an invocable tool under `bin/` top
#: level, so `run_cli` is pointed at it explicitly rather than by default.
STUB_DIR = pathlib.Path(__file__).resolve().parent / "fixtures" / "stub"

#: Every value the nineteen cases put into a report is ASCII. That is a fact
#: about the enumeration, not a limit on the suite: §5.2's escape rule is
#: asserted by `TestT01NonAsciiValuesAreEscaped`, whose fixture carries a
#: non-ASCII `branch`. See the module docstring.
MESSAGE = "land the work"

#: §5.2: "A non-ASCII character in any value is written as a `\uXXXX` escape."
#: U+03C0 is the carrier for two reasons. It has no canonical decomposition, so
#: no normalization form of it differs from any other and nothing in the
#: platform can turn it into a different sequence of code points; and it is a
#: legal character in a git ref name, so a branch argument carrying it is a
#: branch the tool can really be asked to land on.
NON_ASCII = "\u03c0"

#: The six characters §5.2 requires in the stream in place of the character.
#: Matched case-insensitively at the point of use: JSON admits either case in a
#: `\uXXXX` escape, and §5.2 fixes the form and not the case, so asserting
#: lowercase would be asserting something the document does not say.
NON_ASCII_ESCAPE = "\\u03c0"

#: The branch argument the non-ASCII fixture invokes with.
NON_ASCII_BRANCH = "feat-" + NON_ASCII


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


def index_entries(repo, env=None):
    """`git ls-files --stage` — the index itself, not a diff against a HEAD.

    AC-LAND-T03 asserts the index was never written. A diff against HEAD cannot
    say that: a tool that moved HEAD *and* wrote the index shows an empty diff.
    """
    rc, out, err = git(repo, "ls-files", "--stage", env=env, check=True)
    return out


def land_raw(sub, *args, env=None, timeout=90):
    r"""Invoke the stub `land` and return `(rc, stdout_bytes, stderr_bytes)`.

    `helpers.run_cli` runs the process with `text=True`, which decodes stdout
    before a test can look at it. §5.2's ASCII rule is a property of the
    **bytes**, and a decoded string cannot witness it: `"feat-\u03c0"` is what
    the escaped form and the raw form both decode to, so a test handed the
    string has already lost the difference it exists to assert. This runs the
    same script the same way, in the same working tree and environment, and
    declines the decode.

    Local rather than in `helpers.py`, for the reason the module docstring
    gives about the other helpers here: this module's directive confines its
    edits. Moving it is stated work for the Coder.
    """
    proc = subprocess.run(
        [str(STUB_DIR / "land"), *[str(a) for a in args]],
        cwd=str(sub.repo),
        env=env if env is not None else sub.env,
        capture_output=True,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout, proc.stderr


def git_shim_path(case, failing):
    """A PATH whose `git` fails one subcommand and execs the real one otherwise.

    Mock-verified, and only where a real substrate cannot produce the state:
    FM-1's `resolve` arm needs `fetch` to succeed and `ls-remote` to fail
    against the same origin, which no reachable `file://` remote does (§5.4).
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


REFUSING_PRE_COMMIT = "#!/bin/sh\necho 'stand-in hook refuses' >&2\nexit 1\n"

REFUSING_PRE_RECEIVE = "#!/bin/sh\necho 'receive refuses' >&2\nexit 1\n"

#: Restores the prior ref after receive-pack has already answered, so the push
#: exits 0 and the ref the tool reads back is not the one it wrote (FM-8).
RESETTING_POST_RECEIVE = (
    "#!/bin/sh\n"
    "while read old new ref; do\n"
    '  if [ "$old" != "%s" ]; then\n'
    '    git update-ref "$ref" "$old"\n'
    "  fi\n"
    "done\n" % ZEROS
)


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
        """Fetch and stand on a local branch at the remote branch's head.

        This is what puts HEAD *on* `<branch>` before the invocation, which is
        the state §5.3's `detail.prior_branch` row excludes.
        """
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
        return run_cli(
            "land", *args, cwd=self.repo, env=env or self.env, script_dir=STUB_DIR
        )


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


def _on_branch(case):
    """Remote `<branch>` exists and local HEAD stands on it at its head.

    Step 6 then moves HEAD off nothing, so §5.3's `detail.prior_branch` row is
    not established — the second of every `prior_branch` split below.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    sub.track_remote_branch(BRANCH)
    return sub, remote_sha


# =============================================================================
# The case set: AC-LAND-T01's enumeration, derived (§5.4).
# =============================================================================
#
# §5.4 fixes the unit: a terminal path is one end state of §3.2's sequence,
# individuated by the report §5.3 gives it. The success path and each *detected*
# failure mode contribute one, and contribute more wherever §5.3 makes the
# report depend on state within the mode. Exactly two things do that:
#
#   (a) a conditional row in §5.3's key table — `detail.branch_head` (FM-3 only,
#       "there only where the local `<branch>` is the ref whose check refused")
#       and `detail.prior_branch` (FM-5..FM-8 and success, "there only where it
#       found HEAD on some branch other than `<branch>`");
#   (b) a conditional token in §5.3's token table — FM-1 (`fetch` / `resolve`)
#       and FM-5 (`stage` / `nothing-staged`).
#
# Nothing else splits a mode: `prior_head` reading `created` rather than a SHA
# is the same terminal path, because the established set and the shape are the
# same. So:
#
#   success  x prior_branch          = 2
#   FM-1     x token                 = 2
#   FM-2                             = 1
#   FM-3     x branch_head           = 2
#   FM-4                             = 1
#   FM-5     x token x prior_branch  = 4
#   FM-6     x prior_branch          = 2
#   FM-7     x prior_branch          = 2
#   FM-8     x prior_branch          = 2
#   FM-11                            = 1
#                                   ----
#                                     19   — §5.4's stated count.
#
# Outside the enumeration, per §5.4 itself: FM-10 (killed mid-sequence, emits
# nothing) and the usage-error path (emits no report; AC-LAND-T01a's).
# There is no FM-9: §6 struck it as unreachable and deliberately left the hole.


def build_success_head_moved(case):
    """Success, HEAD moved off `main` onto `<branch>`, so `prior_branch` holds.

    `<branch>` is absent at the remote here, which is G1's first arm and makes
    `prior_head` read `created`. That is *not* what splits this case from the
    next one (§5.4: a value difference is one terminal path); the split is
    `detail.prior_branch`.
    """
    sub = Substrate(case)
    write(sub.repo, "work.md", "landed\n")
    before = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, local_head=before, base=sub.main_sha,
                   prior_head="created", prior_branch="main")


def build_success_head_on_branch(case):
    """Success, HEAD already on `<branch>`: step 6 moved HEAD off nothing."""
    sub, remote_sha = _on_branch(case)
    write(sub.repo, "work.md", "landed\n")
    before = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, local_head=before, base=remote_sha,
                   prior_head=remote_sha)


def build_fm1_fetch(case):
    """FM-1 at step 2: `git fetch origin` cannot reach the remote."""
    sub = Substrate(case)
    missing = sub.sandbox / "no-such-remote.git"
    git(sub.repo, "remote", "set-url", "origin", remote_url(missing), env=sub.env,
        check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err)


def build_fm1_resolve(case):
    """FM-1 at step 3: the fetch succeeds and the remote read fails.

    Mock-verified (§5.4): a `git` shim on a temporary PATH. No reachable
    `file://` remote produces a working `fetch` and a failing `ls-remote`.
    """
    sub = Substrate(case)
    shim = git_shim_path(case, "ls-remote")
    env = base_env(PATH="%s%s%s" % (shim, os.pathsep, os.environ.get("PATH", "")))
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md", env=env)
    return Landing(sub, rc, out, err)


def build_fm2(case):
    """FM-2: `ls-remote` names a base whose object the local repo does not have.

    Induced by narrowing `remote.origin.fetch` to `main`, the cause TRD §3.2
    step 4 records as *observed* — the tool asserts no cause, so any of the
    three it names produces the same refusal.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    git(sub.repo, "config", "remote.origin.fetch",
        "+refs/heads/main:refs/remotes/origin/main", env=sub.env, check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
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
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm3_branch_diverged(case):
    """FM-3, second check: the local `<branch>` diverges, HEAD is elsewhere.

    This is AC-LAND-T03's given. `detail.branch_head` is established here and
    on no other path.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    sub.track_remote_branch(BRANCH)
    branch_tip = sub.local_commit("unpushed.md", "not at the remote\n")
    git(sub.repo, "checkout", "-q", "main", env=sub.env, check=True)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head, branch_head=branch_tip)


def build_fm4(case):
    """FM-4: a locally-modified file whose committed content differs base vs HEAD.

    Step 6 is the step that failed, so `detail.prior_branch` is established on
    no FM-4 path and the mode is one terminal path.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH, relpath="seed.md",
                                        text="the remote version\n")
    write(sub.repo, "seed.md", "the local edit\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "seed.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm5_stage_head_moved(case):
    """FM-5 at step 7 — a named path does not exist — with HEAD moved off `main`."""
    sub = Substrate(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "absent.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_head="created", prior_branch="main")


def build_fm5_stage_head_on_branch(case):
    """FM-5 at step 7 with HEAD already on `<branch>`: no `prior_branch`."""
    sub, remote_sha = _on_branch(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "absent.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm5_nothing_staged_head_moved(case):
    """FM-5 at step 8 — the staged set is empty — with HEAD moved off `main`.

    §5.3's token table gives this stop `nothing-staged`, not `commit`: a hook
    refusing a commit and a commit with nothing in it are the two situations a
    session must answer differently.
    """
    sub = Substrate(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE)
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_head="created", prior_branch="main")


def build_fm5_nothing_staged_head_on_branch(case):
    """FM-5 at step 8 with HEAD already on `<branch>`: no `prior_branch`."""
    sub, remote_sha = _on_branch(case)
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE)
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm6_head_moved(case):
    """FM-6: a repository hook refuses the commit, HEAD moved off `main`.

    Boundary (§4.2 B5): a **stand-in** hook that refuses, not this repository's
    own. What this establishes is the report's shape and status on that path.
    B5 stays *assumed*.
    """
    sub = Substrate(case)
    install_hook(sub.repo / ".git" / "hooks", "pre-commit", REFUSING_PRE_COMMIT)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_head="created", prior_branch="main")


def build_fm6_head_on_branch(case):
    """FM-6 with HEAD already on `<branch>`: no `prior_branch`. Same stand-in."""
    sub, remote_sha = _on_branch(case)
    install_hook(sub.repo / ".git" / "hooks", "pre-commit", REFUSING_PRE_COMMIT)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm7_head_moved(case):
    """FM-7: the remote refuses the push. The local commit stays (PRD §7).

    The refusal is a `pre-receive` hook in the bare repository — a stand-in for
    the provider-side ref policy §4.2's B1 lists under "does not prove".
    """
    sub = Substrate(case)
    install_hook(sub.bare / "hooks", "pre-receive", REFUSING_PRE_RECEIVE)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=sub.main_sha, local_head=local_head,
                   prior_head="created", prior_branch="main")


def build_fm7_head_on_branch(case):
    """FM-7 with HEAD already on `<branch>`: no `prior_branch`."""
    sub, remote_sha = _on_branch(case)
    install_hook(sub.bare / "hooks", "pre-receive", REFUSING_PRE_RECEIVE)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head)


def build_fm8_head_moved(case):
    """FM-8: the push exits 0 and `ls-remote` then disagrees, HEAD off `main`.

    `<branch>` exists at the remote and no local branch of that name does, so
    step 5's second check is skipped and step 6 moves HEAD off `main`.
    """
    sub = Substrate(case)
    remote_sha = sub.seed_remote_branch(BRANCH)
    install_hook(sub.bare / "hooks", "post-receive", RESETTING_POST_RECEIVE)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head, remote_head=remote_sha,
                   prior_branch="main")


def build_fm8_head_on_branch(case):
    """FM-8 with HEAD already on `<branch>`: no `prior_branch`."""
    sub, remote_sha = _on_branch(case)
    install_hook(sub.bare / "hooks", "post-receive", RESETTING_POST_RECEIVE)
    write(sub.repo, "work.md", "landed\n")
    local_head = sub.head()
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err, base=remote_sha, prior_head=remote_sha,
                   local_head=local_head, remote_head=remote_sha)


def build_fm11(case):
    """FM-11: the remote read succeeds and neither `<branch>` nor `main` is there."""
    sub = Substrate(case)
    empty = make_bare_remote(case, sub.sandbox, name="empty.git")
    git(sub.repo, "remote", "set-url", "origin", remote_url(empty), env=sub.env,
        check=True)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = sub.land(BRANCH, MESSAGE, "work.md")
    return Landing(sub, rc, out, err)


def build_non_ascii_branch(case):
    """The success path, invoked with a non-ASCII character in `branch`.

    Not a twentieth terminal path (§5.4's enumeration is a fixed nineteen, and
    `CASES` is untouched): it is `success-head-moved`'s path run again with
    different input, so that §5.2's escape rule has something to bite on.

    `branch` is the carrier because it comes straight from the invocation's
    argument (§3.7) and §5.3's key table establishes it on every path a report
    is emitted at all, so no stop can take the character back out of the
    report. It also never touches the filesystem, which is what a `files` path
    could not say on macOS — see the module docstring.

    Returns the raw streams rather than a `Landing`: the decode is the caller's,
    and which decode it uses is load-bearing here.
    """
    sub = Substrate(case)
    write(sub.repo, "work.md", "landed\n")
    rc, out, err = land_raw(sub, NON_ASCII_BRANCH, MESSAGE, "work.md")
    return sub, rc, out, err


class Case:
    """One terminal path, with what §5.3's tables and §7 state for it.

    `established` names the contract fields other than `files` that §5.3's key
    table establishes on this path; `detail_keys` is the **exact** key set of
    `detail` there, the column being a ceiling as well as a floor; `files` is
    the entry list the key table gives it; `stage` is the token, or None on the
    success path, which no row names; `exit_code` is §7's exit mapping; `code`
    is the bracketed diagnostic code §7's table assigns this refusal, or None on
    the two success paths, which §7 gives no row because a landing that worked
    emits no diagnostic and so no code.

    `code` is **keyword-only and has no default** on purpose. Every one of the
    nineteen must name its row of §7's table explicitly, including the two that
    name `None`, so that a case added or a row misread is a visible omission
    rather than a silent inherited default.
    """

    def __init__(self, mode, builder, stage, exit_code, established, detail_keys,
                 files=(), *, code):
        self.mode = mode
        self.builder = builder
        self.stage = stage
        self.exit_code = exit_code
        self.established = tuple(established)
        self.detail_keys = tuple(detail_keys)
        self.files = list(files)
        self.code = code


#: Contract fields established on a landing that reached the commit but not a
#: comparison (FM-7, FM-8), and on the success path.
_COMMITTED = ("branch", "prior_head", "head", "verification")
_RESOLVED = ("branch", "prior_head")

#: `files` per §5.3: observed entries on success; one `match: null` entry per
#: committed path on FM-7 and FM-8; no entries anywhere else.
_MATCHED = [("work.md", True, "observed")]
_UNMATCHED = [("work.md", None, "unknown")]

CASES = {
    "success-head-moved": Case(
        "success", build_success_head_moved, None, 0,
        ("branch", "head", "prior_head", "verification"),
        ("base", "local_head", "prior_branch", "remote_head"), _MATCHED,
        code=None),  # §7: a successful landing emits no diagnostic, so no code
    "success-head-on-branch": Case(
        "success", build_success_head_on_branch, None, 0,
        ("branch", "head", "prior_head", "verification"),
        ("base", "local_head", "remote_head"), _MATCHED,
        code=None),  # §7: a successful landing emits no diagnostic, so no code
    "fm1-fetch": Case(
        "FM-1", build_fm1_fetch, "fetch", 3,
        ("branch",), ("stage", "git_status"),
        code="fetch-failed"),
    "fm1-resolve": Case(
        "FM-1", build_fm1_resolve, "resolve", 3,
        ("branch",), ("stage", "git_status"),
        # §7 is finer than §5.3 here: `resolve` serves FM-1 and FM-11 both, and
        # a session answers "could not reach the remote" differently from
        # "reached it and found neither ref".
        code="remote-read-failed"),
    "fm2": Case(
        "FM-2", build_fm2, "base-object", 3,
        _RESOLVED, ("stage", "base", "git_status"),
        code="base-object-missing"),
    "fm3-head-diverged": Case(
        "FM-3", build_fm3_head_diverged, "guard", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status"),
        # §7's second finer-than-the-token split: `guard` serves both of FM-3's
        # checks, and `detail.branch_head` is what separates them on stdout.
        # This is the first check, so no `branch_head`.
        code="head-diverged"),
    "fm3-branch-diverged": Case(
        "FM-3", build_fm3_branch_diverged, "guard", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status", "branch_head"),
        # The second check — `branch_head` present, per §5.3's conditional row.
        code="branch-diverged"),
    "fm4": Case(
        "FM-4", build_fm4, "base", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status"),
        code="base-checkout-failed"),
    "fm5-stage-head-moved": Case(
        "FM-5", build_fm5_stage_head_moved, "stage", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch"),
        # Shared pair 1 of 5: the same code as its `head-on-branch` twin. §7
        # shares it because `prior_branch` is a side effect of a step that
        # succeeded, not a cause of the refusal.
        code="path-not-found"),
    "fm5-stage-head-on-branch": Case(
        "FM-5", build_fm5_stage_head_on_branch, "stage", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status"),
        code="path-not-found"),
    "fm5-nothing-staged-head-moved": Case(
        "FM-5", build_fm5_nothing_staged_head_moved, "nothing-staged", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch"),
        # Shared pair 2 of 5. The code and the token coincide in spelling here
        # and nowhere else; they are still different channels.
        code="nothing-staged"),
    "fm5-nothing-staged-head-on-branch": Case(
        "FM-5", build_fm5_nothing_staged_head_on_branch, "nothing-staged", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status"),
        code="nothing-staged"),
    "fm6-head-moved": Case(
        "FM-6", build_fm6_head_moved, "commit", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch"),
        code="commit-refused"),  # shared pair 3 of 5
    "fm6-head-on-branch": Case(
        "FM-6", build_fm6_head_on_branch, "commit", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status"),
        code="commit-refused"),
    "fm7-head-moved": Case(
        "FM-7", build_fm7_head_moved, "push", 1,
        _COMMITTED,
        ("stage", "base", "local_head", "git_status", "prior_branch"), _UNMATCHED,
        code="push-rejected"),  # shared pair 4 of 5
    "fm7-head-on-branch": Case(
        "FM-7", build_fm7_head_on_branch, "push", 1,
        _COMMITTED,
        ("stage", "base", "local_head", "git_status"), _UNMATCHED,
        code="push-rejected"),
    "fm8-head-moved": Case(
        "FM-8", build_fm8_head_moved, "verify", 4,
        _COMMITTED,
        ("stage", "base", "local_head", "remote_head", "prior_branch"), _UNMATCHED,
        code="remote-head-mismatch"),  # shared pair 5 of 5
    "fm8-head-on-branch": Case(
        "FM-8", build_fm8_head_on_branch, "verify", 4,
        _COMMITTED,
        ("stage", "base", "local_head", "remote_head"), _UNMATCHED,
        code="remote-head-mismatch"),
    "fm11": Case(
        "FM-11", build_fm11, "resolve", 3,
        _RESOLVED, ("stage",),
        # The other half of the `resolve` split: the read succeeded and named
        # neither `<branch>` nor `main`.
        code="no-base-at-remote"),
}

#: Deterministic order for the tests that run the whole enumeration.
CASE_NAMES = sorted(CASES)


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
        """§5.2: a leaf carries **exactly** `value` and `class`, and no other key."""
        self.assertIsInstance(leaf, dict, "%s is not a leaf object" % label)
        self.assertEqual(sorted(leaf), ["class", "value"],
                         "%s carries %r" % (label, sorted(leaf)))
        self.assertIn(leaf["class"], CLASSES, "%s class=%r" % (label, leaf["class"]))
        if leaf["class"] == "unknown":
            self.assertIsNone(leaf["value"], "%s is unknown but carries a value"
                              % label)

    def assert_value_domains(self, report, branch=BRANCH):
        """§5.2's whole rule list, on any path."""
        self.assertEqual(sorted(report), TOP_LEVEL_KEYS,
                         "top-level keys are %r" % sorted(report))
        for name in ("branch", "head", "prior_head", "verification"):
            self.assert_leaf(report[name], name)
        self.assertIsInstance(report["detail"], dict, "detail is not an object")
        for key, leaf in sorted(report["detail"].items()):
            self.assert_leaf(leaf, "detail.%s" % key)
            # §5.2: an unestablished `detail` key is absent rather than
            # present-and-unknown, so every `detail` key a report carries, it
            # carries with `class: "observed"`.
            self.assertEqual(leaf["class"], "observed",
                             "detail.%s is present and unknown" % key)

        # `branch.value` is the argument, as a string; never null, always
        # observed, there being no path on which the tool failed to establish it.
        self.assertEqual(report["branch"]["class"], "observed",
                         "branch is not observed")
        self.assertEqual(report["branch"]["value"], branch,
                         "branch.value=%r" % report["branch"]["value"])

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
        # `head.value` is a 40-character SHA or null.
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
            self.assertNotIn("value", entry, "a files entry names its value `match`")
            self.assertIn(entry["class"], CLASSES)
            self.assertIn(entry["match"], (True, False, None),
                          "match=%r" % entry["match"])
            if entry["class"] == "unknown":
                self.assertIsNone(entry["match"],
                                  "%s is unknown but carries a match" % entry["path"])
            self.assertIsInstance(entry["path"], str)

        # §5.3's closed token set: ten tokens and no others.
        if "stage" in report["detail"]:
            self.assertIn(report["detail"]["stage"]["value"], STAGE_TOKENS,
                          "stage=%r" % report["detail"]["stage"]["value"])


    # -- §5.3's one emission rule -----------------------------------------

    def assert_git_status_domain(self, report):
        """§5.2: `detail.git_status.value` is a JSON **number**, and an integer.

        Never a string, and it has no `null` branch — §5.3's emission rule
        leaves an unestablished `detail` key absent rather than unknown. Kept
        out of `assert_value_domains` so that a report violating it fails this
        rule's own case rather than pre-empting the emission assertions.
        """
        if "git_status" not in report["detail"]:
            return
        status = report["detail"]["git_status"]["value"]
        self.assertNotIsInstance(status, bool,
                                 "git_status is a boolean: %r" % status)
        self.assertIsInstance(status, int,
                              "git_status is not a JSON number: %r" % status)

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

    def assert_diagnostic(self, landing, code):
        """AC-LAND-T01b: stderr carries the code §7's table assigns this refusal.

        The identity, not merely the presence. §7's table is "this document's
        single statement of which refusal carries which code" and is normative
        over every other passage, so there is a right answer per path and this
        asserts it. Presence alone was the old assertion and the state OQ-12
        named: it passed two implementations whose codes disagreed, which is the
        whole of what was wrong with it.

        **No assertion that every bracketed token on the stream is one of §7's
        twelve.** That stronger form was written first and removed, and the
        reason is worth
        keeping rather than leaving as a silent omission: `git push` writes
        ` ! [rejected]  feat -> feat (fetch first)` on a non-fast-forward
        refusal, and `bracket_codes` extracts `rejected` from it (*observed*,
        run against this module's own substrate). `aimeta/repo.py`'s `run`
        captures git's stderr rather than letting it through (*observed*), so
        that line does not reach the tool's stream on its own — but nothing in
        §7 forbids an implementation from quoting git's captured diagnostic into
        its own, and one that did would fail a closed-set assertion here while
        violating no word of the document. §7 states which code a refusal
        carries; it does not close the stream. Asserting that it does would be
        settling something the spec leaves open, which is not this module's to
        settle. Reported as a finding.

        What is asserted instead is the closed set read **through** §7's twelve:
        of the codes on the stream, exactly one is from the table, and it is
        this path's. A token the table does not name — git's `rejected`, or
        anything a future diagnostic carries — is ignored, because §7 says
        nothing about it. Two of the table's own codes on one refusal is a
        different matter and does fail: §7's table gives each refusal one row,
        so a tool naming two of the twelve for one stop contradicts the table
        rather than merely adding to the stream.
        """
        found = bracket_codes(landing.err)
        self.assertTrue(
            found,
            "no bracketed diagnostic code on stderr, expected [%s]: %r"
            % (code, landing.err),
        )
        from_table = sorted({c for c in found if c in DIAGNOSTIC_CODES})
        self.assertEqual(
            from_table, [code],
            "stderr names %r of §7's twelve; this refusal's row is [%s]. The "
            "whole of what stderr carried was %r: %r"
            % (from_table, code, found, landing.err),
        )

    def assert_no_diagnostic_code(self, landing):
        """AC-LAND-T01b: a successful landing carries no bracketed code at all.

        **Not** that stderr is empty, and this is the restraint T01b states
        rather than a weakness in the assertion. §7's table is the seventeen
        refusal paths' and carries no row for a landing that worked, so what is
        asserted is that the tool emitted no diagnostic of its own. `git push`
        and `git fetch` write progress, and a credential helper can write a line
        of its own, on a landing that worked perfectly; a test demanding an empty
        stream would fail on the environment rather than on the tool, and a red
        that means the environment is not a red about the tool.

        The bracket form is safe here where a closed-set assertion on the
        refusal paths was not: the git commands a *successful* landing runs
        write ` * [new branch]  feat -> feat` and `   <sha>..<sha>  feat -> feat`
        to stderr, and `bracket_codes` extracts nothing from either — the space
        in `new branch` puts it outside `BRACKET_CODE_RE` (*observed*, run
        against this module's own substrate) — and `aimeta/repo.py`'s `run`
        captures that output anyway (*observed*).
        """
        found = bracket_codes(landing.err)
        self.assertEqual(
            found, [],
            "a successful landing put the bracketed code(s) %r on stderr; §7's "
            "table is the refusal paths' and gives a landing that worked no row, "
            "there being no situation to answer: %r" % (found, landing.err),
        )

    def check(self, landing, name):
        """AC-LAND-T01 for one case, plus §7's exit mapping and T01b's code.

        T01b rides here as well as in its own sweep, which is how this module
        already carries `detail.stage` and the exit status: the per-case test
        asserts everything true of its own path, and the sweep states the
        property over the enumeration. On the two success paths that means
        asserting stderr carries no bracketed code, which is the only assertion
        in this module that a tool doing nothing at all would satisfy.
        """
        spec = CASES[name]
        report = self.parse(landing)
        self.assert_value_domains(report)
        self.assert_emission(report, spec.established, spec.detail_keys)
        self.assert_files(report, spec.files)
        self.assert_exit(landing, spec.exit_code, name)
        if spec.stage is None:
            self.assertNotIn("stage", report["detail"],
                             "the success path carries a stage token")
            self.assert_no_diagnostic_code(landing)
        else:
            self.assert_stage(report, spec.stage)
            self.assert_diagnostic(landing, spec.code)
        return report

    def assert_stage(self, report, token):
        """§5.3: `detail.stage` names the stop the sequence made."""
        self.assertIn("stage", report["detail"],
                      "the failure report names no stage; detail=%r"
                      % sorted(report["detail"]))
        self.assertEqual(report["detail"]["stage"]["value"], token)


# ------------------------------------------------- AC-LAND-T01, case by case


class TestT01SuccessPath(ReportAssertions):
    """The two success terminal paths, split by §5.3's `prior_branch` row."""

    def test_t01_case_success_head_moved_off_another_branch(self):
        """AC-LAND-T01 / §5.3: `detail.prior_branch` established, G1's first arm."""
        landing = build_success_head_moved(self)
        report = self.check(landing, "success-head-moved")
        self.assertEqual(report["prior_head"]["value"], "created")
        self.assertEqual(report["verification"]["value"], "complete")
        self.assertEqual(report["head"]["value"],
                         remote_ref_sha(landing.sub.bare, BRANCH))
        self.assertEqual(report["head"]["value"], landing.sub.head())
        self.assert_detail(report, "base", landing["base"])
        self.assert_detail(report, "local_head", landing["local_head"])
        self.assert_detail(report, "prior_branch", "main")
        self.assert_detail(report, "remote_head", report["head"]["value"])

    def test_t01_case_success_head_already_on_the_branch(self):
        """AC-LAND-T01 / §5.3: step 6 moved HEAD off nothing, so no `prior_branch`.

        This is the row's condition, and the ordinary second landing of a
        session that used the tool for its first (§3.3).
        """
        landing = build_success_head_on_branch(self)
        report = self.check(landing, "success-head-on-branch")
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])
        self.assertEqual(report["verification"]["value"], "complete")
        self.assertEqual(report["head"]["value"],
                         remote_ref_sha(landing.sub.bare, BRANCH))
        self.assert_detail(report, "base", landing["base"])
        self.assert_detail(report, "local_head", landing["local_head"])
        self.assert_detail(report, "remote_head", report["head"]["value"])


class TestT01FailureModes(ReportAssertions):
    """The seventeen detected failure terminal paths of §5.4's enumeration."""

    def test_t01_case_fm1_remote_read_fails_at_fetch(self):
        """§6 FM-1 at step 2: only `branch` and the stop are established."""
        landing = build_fm1_fetch(self)
        report = self.check(landing, "fm1-fetch")
        self.assertNotEqual(report["detail"]["git_status"]["value"], 0,
                            "the failing invocation reported exit 0")

    def test_t01_case_fm1_remote_read_fails_at_resolve(self):
        """§6 FM-1 at step 3: same shape, the `resolve` token.

        Mock-verified via a `git` shim (§5.4); see `git_shim_path`.
        """
        landing = build_fm1_resolve(self)
        report = self.check(landing, "fm1-resolve")
        self.assertNotEqual(report["detail"]["git_status"]["value"], 0)

    def test_t01_case_fm2_base_object_absent_locally(self):
        """§6 FM-2: `prior_head` and `base` established, nothing beyond."""
        landing = build_fm2(self)
        report = self.check(landing, "fm2")
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])
        self.assert_detail(report, "base", landing["base"])

    def test_t01_case_fm3_first_check_refuses_without_branch_head(self):
        """§6 FM-3, first check: `detail.branch_head` is **absent**.

        §5.3's emission rule makes that absence a claim: the guard stopped
        before `<branch>`'s SHA was read.
        """
        landing = build_fm3_head_diverged(self)
        report = self.check(landing, "fm3-head-diverged")
        self.assertNotIn("branch_head", report["detail"])
        self.assert_detail(report, "local_head", landing["local_head"])

    def test_t01_case_fm3_second_check_refuses_with_branch_head(self):
        """§6 FM-3, second check: `detail.branch_head` established."""
        landing = build_fm3_branch_diverged(self)
        report = self.check(landing, "fm3-branch-diverged")
        self.assert_detail(report, "branch_head", landing["branch_head"])
        self.assert_detail(report, "local_head", landing["local_head"])

    def test_t01_case_fm4_base_establishment_fails(self):
        """§6 FM-4: step 6 is the step that failed, so no `prior_branch`."""
        landing = build_fm4(self)
        report = self.check(landing, "fm4")
        self.assertNotIn("prior_branch", report["detail"])
        self.assert_detail(report, "base", landing["base"])

    def test_t01_case_fm5_named_path_absent_head_moved(self):
        """§6 FM-5 at step 7, `stage` token, `prior_branch` established."""
        landing = build_fm5_stage_head_moved(self)
        report = self.check(landing, "fm5-stage-head-moved")
        self.assert_detail(report, "prior_branch", "main")
        self.assertEqual(report["prior_head"]["value"], "created")

    def test_t01_case_fm5_named_path_absent_head_on_branch(self):
        """§6 FM-5 at step 7 with HEAD on `<branch>`: no `prior_branch`."""
        landing = build_fm5_stage_head_on_branch(self)
        report = self.check(landing, "fm5-stage-head-on-branch")
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])

    def test_t01_case_fm5_nothing_staged_head_moved(self):
        """§6 FM-5 at step 8, the `nothing-staged` token, `prior_branch` there.

        §5.3 gives step 8 two tokens; this is the empty staged set, which is not
        FM-6's hook refusal and must not report as it.
        """
        landing = build_fm5_nothing_staged_head_moved(self)
        report = self.check(landing, "fm5-nothing-staged-head-moved")
        self.assert_detail(report, "prior_branch", "main")
        self.assert_files(report, [])

    def test_t01_case_fm5_nothing_staged_head_on_branch(self):
        """§6 FM-5 at step 8 with HEAD on `<branch>`: no `prior_branch`."""
        landing = build_fm5_nothing_staged_head_on_branch(self)
        report = self.check(landing, "fm5-nothing-staged-head-on-branch")
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])

    def test_t01_case_fm6_hook_refuses_the_commit_head_moved(self):
        """§6 FM-6, `commit` token. Boundary: a stand-in hook, not B5's own."""
        landing = build_fm6_head_moved(self)
        report = self.check(landing, "fm6-head-moved")
        self.assert_detail(report, "prior_branch", "main")

    def test_t01_case_fm6_hook_refuses_the_commit_head_on_branch(self):
        """§6 FM-6 with HEAD on `<branch>`: no `prior_branch`. Same stand-in."""
        landing = build_fm6_head_on_branch(self)
        report = self.check(landing, "fm6-head-on-branch")
        self.assertEqual(report["prior_head"]["value"], landing["prior_head"])

    def test_t01_case_fm7_push_fails_head_moved(self):
        """§6 FM-7: `head` observed, `verification` incomplete, `files` unknown.

        PRD §7's accepted risk: the local commit stays, and the report is what
        names the files the session must now resolve.
        """
        landing = build_fm7_head_moved(self)
        report = self.check(landing, "fm7-head-moved")
        self.assertEqual(report["verification"]["value"], "incomplete")
        self.assertEqual(report["head"]["value"], landing.sub.head())
        self.assertIsNone(remote_ref_sha(landing.sub.bare, BRANCH),
                          "the push was rejected but the ref moved")

    def test_t01_case_fm7_push_fails_head_on_branch(self):
        """§6 FM-7 with HEAD on `<branch>`: no `prior_branch`."""
        landing = build_fm7_head_on_branch(self)
        report = self.check(landing, "fm7-head-on-branch")
        self.assertEqual(report["verification"]["value"], "incomplete")
        self.assertEqual(report["head"]["value"], landing.sub.head())
        self.assertEqual(remote_ref_sha(landing.sub.bare, BRANCH),
                         landing["prior_head"],
                         "the push was rejected but the remote ref moved")

    def test_t01_case_fm8_ls_remote_disagrees_head_moved(self):
        """§6 FM-8: `remote_head` established, and no `git_status` — the stop is
        a comparison rather than a failed subprocess."""
        landing = build_fm8_head_moved(self)
        report = self.check(landing, "fm8-head-moved")
        self.assertEqual(report["verification"]["value"], "incomplete")
        self.assertNotEqual(report["head"]["value"],
                            report["detail"]["remote_head"]["value"])
        self.assert_detail(report, "remote_head", landing["remote_head"])
        self.assert_detail(report, "prior_branch", "main")

    def test_t01_case_fm8_ls_remote_disagrees_head_on_branch(self):
        """§6 FM-8 with HEAD on `<branch>`: no `prior_branch`."""
        landing = build_fm8_head_on_branch(self)
        report = self.check(landing, "fm8-head-on-branch")
        self.assertNotEqual(report["head"]["value"],
                            report["detail"]["remote_head"]["value"])
        self.assert_detail(report, "remote_head", landing["remote_head"])

    def test_t01_case_fm11_remote_read_names_no_base(self):
        """§6 FM-11: `prior_head` is `created`, `detail` carries `stage` alone."""
        landing = build_fm11(self)
        report = self.check(landing, "fm11")
        self.assertEqual(report["prior_head"]["value"], "created")


class TestT01AcrossEveryCase(ReportAssertions):
    """The format half of AC-LAND-T01, asserted once over the whole enumeration."""

    def test_t01_the_enumeration_is_the_nineteen_terminal_paths(self):
        """§5.4: "The enumeration ... comes to nineteen cases"."""
        self.assertEqual(len(CASES), 19, "the case set is %d cases" % len(CASES))
        per_mode = {}
        for spec in CASES.values():
            per_mode[spec.mode] = per_mode.get(spec.mode, 0) + 1
        self.assertEqual(
            per_mode,
            {"success": 2, "FM-1": 2, "FM-2": 1, "FM-3": 2, "FM-4": 1, "FM-5": 4,
             "FM-6": 2, "FM-7": 2, "FM-8": 2, "FM-11": 1},
            "the split per failure mode is %r" % per_mode,
        )

    def test_t01_every_case_parses_and_holds_the_value_domains(self):
        """AC-LAND-T01 / §5.2: parseable, exact key set, domains, on every path."""
        for name in CASE_NAMES:
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
                report = self.parse(landing)
                self.assert_value_domains(report)

    def test_t01_git_status_is_a_json_number_wherever_it_is_carried(self):
        """§5.2's fourth closed domain, over the whole enumeration.

        Its own case rather than a line in the domain sweep: a report that gets
        this wrong should fail here, not ahead of the emission assertions.
        """
        for name in CASE_NAMES:
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
                report = self.parse(landing)
                self.assert_git_status_domain(report)

    def test_t01_files_entries_follow_the_key_table(self):
        """§5.3's `files` row, over the whole enumeration.

        Three shapes and no fourth: `class: "observed"` entries on the success
        path; one `match: null`, `class: "unknown"` entry per committed path on
        FM-7 and FM-8, where a commit exists and step 10 produced no
        comparison; and no entries at all on every other path. Its own case
        because the shape of `files` on a *failed* landing is the whole burden
        of the format (§5.2's "what an entry with no match means").
        """
        for name in CASE_NAMES:
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
                report = self.parse(landing)
                self.assert_files(report, CASES[name].files)

    def test_t01_exit_status_follows_section_7s_mapping(self):
        """§7's exit mapping, over the whole enumeration.

        The diagnostic is no longer asserted here. It was, back when the only
        assertion available was that *some* bracketed code was present, and it
        rode along with the exit status because both were §7's and neither had
        much to say. §7 now fixes the codes and AC-LAND-T01b is a criterion of
        its own, so the code assertions live in `TestT01bDiagnosticCodes` — a
        different stream, a different criterion, and a red in one should not
        name the other.
        """
        for name in CASE_NAMES:
            with self.subTest(case=name):
                spec = CASES[name]
                landing = spec.builder(self)
                self.assert_exit(landing, spec.exit_code, name)

    def test_t01_stage_tokens_are_the_ten_and_the_right_one(self):
        """§5.3's token table: closed at ten, and the token of the stop made."""
        self.assertEqual(len(STAGE_TOKENS), 10)
        for name in CASE_NAMES:
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
                report = self.parse(landing)
                expected = CASES[name].stage
                if expected is None:
                    self.assertNotIn("stage", report["detail"],
                                     "the success path carries a stage token")
                else:
                    self.assert_stage(report, expected)


class TestT01NonAsciiValuesAreEscaped(ReportAssertions):
    r"""§5.2: a non-ASCII character in a value is written as a `\uXXXX` escape.

    The rule, in full: "The object is serialized with `ensure_ascii=True`, so
    stdout is pure ASCII on every path, whatever a value carries." It is the
    decision that retired OQ-11, and §5.2's "Why the escaped form and not the
    raw one" gives the reason it is worth asserting rather than left to a
    serializer default: a script's stdout must not depend on the ambient locale
    being UTF-8, and the raw form has failure modes — mangled bytes, or a write
    that fails outright — that the escaped form has in no environment.

    Three cases, because the rule has three separable halves and one case
    asserting all of them would not say which half an implementation got wrong:
    that the stream is ASCII, that the raw UTF-8 form is *not* in it, and that
    the escape carries the character back losslessly. The third is what makes
    the first cost nothing — "an escape and the raw character parse to the same
    string" (§5.2).

    The shape that would otherwise slip past all three — a report that reached
    a pure-ASCII stdout by *dropping* or *replacing* the character rather than
    escaping it — is caught by `fixture_report`, which every case runs first
    and which asserts the character survived into `branch.value`. That is why
    the guard is a method the cases call rather than a case of its own: it is
    load-bearing for each of them, and a green here means nothing without it.

    Boundary: this is the same end-to-end boundary §5.4 fixes for AC-LAND-T01.
    The stdout asserted on is the process's own, and here it is asserted
    **before** any decode, which no in-process call to `Report.build` could
    reproduce — `to_json` returns a `str`, and the bytes are made by the write.
    """

    def setUp(self):
        self.sub, self.rc, self.raw_out, self.raw_err = build_non_ascii_branch(self)
        # latin-1 maps every byte to exactly one code point and can never fail,
        # so a substring search over `self.stream` is a search of the bytes
        # rather than of a decoded string that may have replaced something. On
        # a conforming stream — pure ASCII — it is the same string a correct
        # decode would give.
        self.stream = self.raw_out.decode("latin-1")
        self.landing = Landing(
            self.sub,
            self.rc,
            self.raw_out.decode("utf-8", "replace"),
            self.raw_err.decode("utf-8", "replace"),
        )

    def fixture_report(self):
        """§5.2's format and value domains, plus the guard that makes this real.

        Run at the head of each case rather than as a case of its own. An
        assertion about escaping is worth nothing unless the character actually
        reached a report value: a tool that dropped it, and a fixture that never
        carried it, both leave a stdout that is pure ASCII for a reason that has
        nothing to do with the rule, and the three cases below would then be
        green over nothing. `assert_value_domains` is given the fixture's own
        branch, so `branch.value` is checked against the argument this
        invocation made rather than against the module's `BRANCH` constant.
        """
        report = self.parse(self.landing)
        self.assertFalse(NON_ASCII_BRANCH.isascii(),
                         "fixture: the branch argument is all-ASCII, so nothing "
                         "here can witness §5.2's escape rule")
        # Deliberately ahead of `assert_value_domains`, which asserts the same
        # equality as one line of §5.2's rule list. Read here it is the
        # discriminator the three cases below rest on, and it fails with a
        # message saying so, which is worth the one duplicated assertion.
        self.assertEqual(
            report["branch"]["value"], NON_ASCII_BRANCH,
            "the character did not survive into a report value: branch=%r. "
            "Either the fixture never carried it, or the tool dropped or "
            "replaced it — §5.2 requires `branch.value` to be the argument "
            "\"carried exactly as the argument gave it\". Until this holds, an "
            "ASCII stdout below would be ASCII for the wrong reason."
            % report["branch"]["value"],
        )
        self.assert_value_domains(report, branch=NON_ASCII_BRANCH)
        return report

    def test_t01_stdout_is_pure_ascii_when_a_report_value_is_not(self):
        """§5.2: "stdout is pure ASCII on every path, whatever a value carries"."""
        self.fixture_report()
        offending = sorted({byte for byte in self.raw_out if byte >= 0x80})
        self.assertEqual(
            offending, [],
            "stdout carries %d byte value(s) at or above 0x80 (%s); §5.2 "
            "requires %r to be written as a %s escape so that the stream is "
            "pure ASCII: %r"
            % (len(offending), ", ".join("0x%02x" % b for b in offending),
               NON_ASCII, NON_ASCII_ESCAPE, self.raw_out[:160]),
        )

    def test_t01_the_raw_utf8_form_is_never_written_to_stdout(self):
        """§5.2: `ensure_ascii=True` — the form the section weighed and refused.

        The complement of the case above rather than a restatement of it: that
        one fails on any high byte from any source, this one names the exact
        bytes `ensure_ascii=False` would produce for this character, so a red
        here says *which* form was written and not merely that the stream was
        not ASCII.
        """
        self.fixture_report()
        raw_bytes = NON_ASCII.encode("utf-8")
        self.assertNotIn(
            raw_bytes, self.raw_out,
            "stdout carries the raw UTF-8 bytes %r of %r; §5.2 weighed exactly "
            "this form against the escape and refused it, so that stdout has no "
            "dependence on the ambient locale: %r"
            % (raw_bytes, NON_ASCII, self.raw_out[:160]),
        )

    def test_t01_the_escape_carries_the_character_losslessly(self):
        r"""§5.2: the `\uXXXX` escape is in the stream and parses back whole.

        Both halves, in one case because neither is worth anything alone. The
        escape being present is the property the decision fixed; the round-trip
        is what makes choosing it cost nothing, §5.2 resting the whole decision
        on "both parse to the identical string". The parse is of the **raw**
        stream, so what is shown lossless is the bytes the tool wrote.
        """
        self.fixture_report()
        self.assertIn(
            NON_ASCII_ESCAPE, self.stream.lower(),
            "stdout carries no %s escape for %r; §5.2 requires the escaped form "
            "on every path: %r"
            % (NON_ASCII_ESCAPE, NON_ASCII, self.stream[:200]),
        )
        report = json.loads(self.stream)
        self.assertEqual(
            report["branch"]["value"], NON_ASCII_BRANCH,
            "the escape did not parse back to the character: branch=%r"
            % report["branch"]["value"],
        )


class TestT01aUsageError(ReportAssertions):
    """AC-LAND-T01a — the usage-error path emits no report."""

    def setUp(self):
        self.sub = Substrate(self)

    def test_t01a_missing_arguments_write_nothing_to_stdout(self):
        """AC-LAND-T01a: stdout empty, stderr non-empty, exit 2, no traceback.

        The no-traceback assertion (§7, AC-X-6) rides here rather than standing
        alone: on its own it could not fail against any `argparse` idiom.
        """
        rc, out, err = self.sub.land()
        self.assertEqual(out, "", "a usage error wrote to stdout: %r" % out)
        self.assertTrue(err.strip(), "the usage error was silent on stderr")
        self.assertTrue(no_traceback(out, err), "traceback: %s" % err)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_t01a_missing_message_writes_nothing_to_stdout(self):
        """AC-LAND-T01a: a branch with no message is still a usage error."""
        rc, out, err = self.sub.land(BRANCH)
        self.assertEqual(out, "", "a usage error wrote to stdout: %r" % out)
        self.assertTrue(err.strip(), "the usage error was silent on stderr")
        self.assertTrue(no_traceback(out, err), "traceback: %s" % err)
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))


class TestT01bDiagnosticCodes(ReportAssertions):
    """AC-LAND-T01b — every refusal carries §7's code, and success carries none.

    Two cases, because T01b states two properties over two disjoint halves of
    T01's enumeration and they fail for opposite reasons: a refusal that says
    the wrong thing, and a success that says anything at all. Folding them would
    give a criterion satisfied by either, which is the shape §5.4 refuses at
    T01a for the same reason.

    Both are sweeps rather than nineteen more per-case tests, which is how this
    module already handles `detail.stage` and the exit mapping: the per-case
    assertion rides in `check` — so each of the nineteen named cases asserts its
    own code — and the sweep is where the property is stated over the whole
    enumeration at once. §7's shape is asserted at the head of the first sweep,
    exactly as `len(STAGE_TOKENS) == 10` sits at the head of the token sweep.

    Boundary: `bracket_codes` reads stderr as the process wrote it, and stderr
    on these paths is not the tool's alone — git writes to it too. That is why
    the refusal assertion is `in` rather than an equality on the whole list, and
    why the success assertion is about bracketed codes rather than about the
    stream being empty. Neither is a weakening of T01b; both are what T01b says.
    """

    def test_t01b_section_7s_table_is_twelve_codes_over_seventeen_refusals(self):
        """§7: "Twelve codes, and no others", and the five deliberate pairs.

        The transcription guard, and the one case here that is about `CASES`
        rather than about a process. It is the counterpart of
        `test_t01_the_enumeration_is_the_nineteen_terminal_paths`: that one
        pins §5.4's count, this one pins §7's, and both exist so a
        mistranscribed table fails as itself instead of surfacing as nineteen
        confusing behavioural reds.
        """
        self.assertEqual(len(DIAGNOSTIC_CODES), 12,
                         "§7 names twelve codes; this module lists %d"
                         % len(DIAGNOSTIC_CODES))
        self.assertEqual(len(set(DIAGNOSTIC_CODES)), 12, "a code is listed twice")

        refusals = [n for n in CASE_NAMES if CASES[n].code is not None]
        successes = [n for n in CASE_NAMES if CASES[n].code is None]
        self.assertEqual(len(refusals), 17,
                         "§7's table is the seventeen refusal paths'; %d cases "
                         "name a code" % len(refusals))
        self.assertEqual(
            sorted(successes), ["success-head-moved", "success-head-on-branch"],
            "the paths carrying no code are %r; §7 gives no row to exactly the "
            "two success paths" % sorted(successes),
        )
        self.assertEqual(
            sorted({CASES[n].code for n in refusals}), sorted(DIAGNOSTIC_CODES),
            "the codes the cases name are not §7's twelve",
        )

        # "Five pairs of refusal paths share a code, and the coarseness is
        # deliberate" (§7). Asserted as a property of the pairs rather than by
        # listing them: each shared code must be shared by exactly two cases,
        # and those two must differ in nothing but `detail.prior_branch` — which
        # is §5.4's splitting condition and §7's stated reason for sharing.
        by_code = {}
        for name in refusals:
            by_code.setdefault(CASES[name].code, []).append(name)
        shared = {code: names for code, names in by_code.items() if len(names) > 1}
        self.assertEqual(
            len(shared), 5,
            "§7 shares a code across five pairs; %d codes are shared here: %r"
            % (len(shared), sorted(shared)),
        )
        for code, names in sorted(shared.items()):
            with self.subTest(code=code):
                self.assertEqual(len(names), 2,
                                 "[%s] is carried by %r, not by a pair"
                                 % (code, names))
                first, second = (set(CASES[n].detail_keys) for n in sorted(names))
                self.assertEqual(
                    first ^ second, {"prior_branch"},
                    "[%s]'s two paths differ by %r; §7 shares a code only across "
                    "the `detail.prior_branch` condition, which records a side "
                    "effect of a step that succeeded rather than a cause"
                    % (code, sorted(first ^ second)),
                )

    def test_t01b_every_refusal_carries_the_code_section_7_assigns_it(self):
        """AC-LAND-T01b, first half: the seventeen refusal terminal paths.

        Each asserts the code its **own** row names, never that a code appears
        on one path alone — T01b says so in as many words, because five of the
        codes are carried by two paths apiece and an assertion of uniqueness
        would contradict the table it is testing.
        """
        for name in CASE_NAMES:
            spec = CASES[name]
            if spec.code is None:
                continue
            with self.subTest(case=name, code=spec.code):
                landing = spec.builder(self)
                self.assert_diagnostic(landing, spec.code)

    def test_t01b_a_successful_landing_carries_no_bracketed_code(self):
        """AC-LAND-T01b, second half: the two success terminal paths.

        Its own case and not a branch of the sweep above, because the property
        is the opposite one and the way it fails is the opposite too: there, a
        code that is wrong; here, a code at all. A criterion asserting both at
        once would be satisfied by either, which is the reason §5.4 gives for
        splitting T01a off from T01 and it holds here unchanged.

        Nothing precedes the assertion in this case — no report parse, no
        emission check — so that its red is the stderr claim and cannot be
        pre-empted by an unrelated one. That matters more here than anywhere
        else in the module: this is the assertion that would pass against a tool
        writing nothing at all, so it has to be reached to mean anything.
        """
        for name in CASE_NAMES:
            spec = CASES[name]
            if spec.code is not None:
                continue
            with self.subTest(case=name):
                landing = spec.builder(self)
                self.assert_no_diagnostic_code(landing)


class TestT02VerificationAndExitAgree(ReportAssertions):
    """AC-LAND-T02 — exit 0 iff `verification.value` is `"complete"`."""

    def test_t02_exit_zero_iff_verification_is_complete(self):
        """AC-LAND-T02, across AC-LAND-T01's enumeration."""
        for name in CASE_NAMES:
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
                report = self.parse(landing)
                complete = report["verification"]["value"] == "complete"
                self.assertEqual(
                    landing.rc == 0, complete,
                    "%s: rc=%s verification=%r"
                    % (name, landing.rc, report["verification"]),
                )

    def test_t02_a_non_zero_exit_never_claims_a_complete_verification(self):
        """AC-LAND-T02, the direction PRD §7 puts under "Not accepted"."""
        for name in CASE_NAMES:
            if CASES[name].exit_code == 0:
                continue
            with self.subTest(case=name):
                landing = CASES[name].builder(self)
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
        self.index_before = index_entries(self.sub.repo, self.sub.env)
        self.rc, self.out, self.err = self.sub.land(BRANCH, MESSAGE, "work.md")
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

    def test_t03_the_index_was_never_written(self):
        """AC-LAND-T03: "stops before anything is staged".

        Discriminating by construction. `work.md` exists in the tree and is in
        neither HEAD nor the index when the invocation begins, so an index that
        HAD been written is observably different from the one this fixture
        starts with: a tool that staged and then refused fails the assertion,
        and so does one that reset the index on its way to a ref it should never
        have touched. The two fixture checks are what make that true rather than
        assumed — an index that could not have changed would satisfy the
        assertion for the wrong reason.
        """
        self.assertTrue((self.sub.repo / "work.md").exists(),
                        "fixture: there is nothing for a tool to stage")
        self.assertNotIn("work.md", self.index_before,
                         "fixture: work.md was already staged before the invocation")
        after = index_entries(self.sub.repo, self.sub.env)
        self.assertNotIn("work.md", after,
                         "the tool staged before refusing: %r" % after)
        self.assertEqual(after, self.index_before,
                         "the index was rewritten: %r -> %r"
                         % (self.index_before, after))


class TestUnreachableCases(unittest.TestCase):
    """Terminal paths §5.4 places outside AC-LAND-T01's enumeration."""

    def test_t01_case_fm10_is_outside_the_enumeration_by_construction(self):
        """§6 FM-10: excluded by AC-LAND-T01 itself; recorded so §6 reads whole."""
        self.skipTest(
            "FM-10 emits no report by construction (§3.2 step 11), and "
            "AC-LAND-T01 excludes it from its own enumeration."
        )


if __name__ == "__main__":
    unittest.main()
