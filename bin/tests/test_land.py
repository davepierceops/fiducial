"""AC-LAND-T*: `bin/land` — the report contract and the divergence guard.

Contract: `specs/bin-land-trd.md` §5.2 (shape, serialization, and the value
domains), §5.3 (the key table, the token table, and the one emission rule),
§5.4 (AC-LAND-T01, T01a, T02, T03), §6 (the failure modes — FM-1 through FM-8,
then FM-10, then FM-11, with nothing at 9), §7 (the exit mapping).

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

Not tested, deliberately: whether a non-ASCII character in a report value is
escaped in the serialization. §5.2 does not settle it and the question is open
with Dave. Every value any case here puts into a report is ASCII, so no
assertion in this module depends on which answer is right.

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

SHA_RE = re.compile(r"\A[0-9a-f]{40}\Z")

ZEROS = "0" * 40

BRANCH = "feat"

#: Every value any case puts into a report is ASCII. See the module docstring:
#: whether non-ASCII is escaped is open in §5.2 and is not tested here.
MESSAGE = "land the work"


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


class Case:
    """One terminal path, with what §5.3's tables and §7 state for it.

    `established` names the contract fields other than `files` that §5.3's key
    table establishes on this path; `detail_keys` is the **exact** key set of
    `detail` there, the column being a ceiling as well as a floor; `files` is
    the entry list the key table gives it; `stage` is the token, or None on the
    success path, which no row names; `exit_code` is §7's mapping.
    """

    def __init__(self, mode, builder, stage, exit_code, established, detail_keys,
                 files=()):
        self.mode = mode
        self.builder = builder
        self.stage = stage
        self.exit_code = exit_code
        self.established = tuple(established)
        self.detail_keys = tuple(detail_keys)
        self.files = list(files)


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
        ("base", "local_head", "prior_branch", "remote_head"), _MATCHED),
    "success-head-on-branch": Case(
        "success", build_success_head_on_branch, None, 0,
        ("branch", "head", "prior_head", "verification"),
        ("base", "local_head", "remote_head"), _MATCHED),
    "fm1-fetch": Case(
        "FM-1", build_fm1_fetch, "fetch", 3,
        ("branch",), ("stage", "git_status")),
    "fm1-resolve": Case(
        "FM-1", build_fm1_resolve, "resolve", 3,
        ("branch",), ("stage", "git_status")),
    "fm2": Case(
        "FM-2", build_fm2, "base-object", 3,
        _RESOLVED, ("stage", "base", "git_status")),
    "fm3-head-diverged": Case(
        "FM-3", build_fm3_head_diverged, "guard", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status")),
    "fm3-branch-diverged": Case(
        "FM-3", build_fm3_branch_diverged, "guard", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status", "branch_head")),
    "fm4": Case(
        "FM-4", build_fm4, "base", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status")),
    "fm5-stage-head-moved": Case(
        "FM-5", build_fm5_stage_head_moved, "stage", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch")),
    "fm5-stage-head-on-branch": Case(
        "FM-5", build_fm5_stage_head_on_branch, "stage", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status")),
    "fm5-nothing-staged-head-moved": Case(
        "FM-5", build_fm5_nothing_staged_head_moved, "nothing-staged", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch")),
    "fm5-nothing-staged-head-on-branch": Case(
        "FM-5", build_fm5_nothing_staged_head_on_branch, "nothing-staged", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status")),
    "fm6-head-moved": Case(
        "FM-6", build_fm6_head_moved, "commit", 3,
        _RESOLVED,
        ("stage", "base", "local_head", "git_status", "prior_branch")),
    "fm6-head-on-branch": Case(
        "FM-6", build_fm6_head_on_branch, "commit", 3,
        _RESOLVED, ("stage", "base", "local_head", "git_status")),
    "fm7-head-moved": Case(
        "FM-7", build_fm7_head_moved, "push", 1,
        _COMMITTED,
        ("stage", "base", "local_head", "git_status", "prior_branch"), _UNMATCHED),
    "fm7-head-on-branch": Case(
        "FM-7", build_fm7_head_on_branch, "push", 1,
        _COMMITTED,
        ("stage", "base", "local_head", "git_status"), _UNMATCHED),
    "fm8-head-moved": Case(
        "FM-8", build_fm8_head_moved, "verify", 4,
        _COMMITTED,
        ("stage", "base", "local_head", "remote_head", "prior_branch"), _UNMATCHED),
    "fm8-head-on-branch": Case(
        "FM-8", build_fm8_head_on_branch, "verify", 4,
        _COMMITTED,
        ("stage", "base", "local_head", "remote_head"), _UNMATCHED),
    "fm11": Case(
        "FM-11", build_fm11, "resolve", 3,
        _RESOLVED, ("stage",)),
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

    def assert_diagnostic(self, landing):
        """§7: a bracket-coded diagnostic on stderr on every failure path.

        The code's identity is not asserted — §7 fixes the convention and names
        no code per failure mode — only that one is there, which is the whole of
        what the document states.
        """
        self.assertTrue(bracket_codes(landing.err),
                        "no bracketed diagnostic code on stderr: %r" % landing.err)

    def check(self, landing, name):
        """The whole of AC-LAND-T01 for one case, plus §7's exit code."""
        spec = CASES[name]
        report = self.parse(landing)
        self.assert_value_domains(report)
        self.assert_emission(report, spec.established, spec.detail_keys)
        self.assert_files(report, spec.files)
        self.assert_exit(landing, spec.exit_code, name)
        if spec.stage is None:
            self.assertNotIn("stage", report["detail"],
                             "the success path carries a stage token")
        else:
            self.assert_stage(report, spec.stage)
            self.assert_diagnostic(landing)
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

    def test_t01_exit_status_and_diagnostic_follow_section_7(self):
        """§7's exit mapping, and a bracket-coded diagnostic on every failure.

        The code's identity is not asserted: §7 fixes the convention and names
        no code per failure mode.
        """
        for name in CASE_NAMES:
            with self.subTest(case=name):
                spec = CASES[name]
                landing = spec.builder(self)
                self.assert_exit(landing, spec.exit_code, name)
                if spec.stage is not None:
                    self.assert_diagnostic(landing)

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
