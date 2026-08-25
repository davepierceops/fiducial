"""The landing sequence: `specs/bin-land-trd.md` §3.2, step by step.

One invocation runs the eleven steps in order and stops at the first that
fails. Each step returns either the facts it established or a stop; the
sequence accumulates the facts and hands them, with the stop, to
`report.Report.build`. Nothing here formats, and nothing here decides what the
report carries — §5.3's key table decides that, and `report.py` reads it.

Two properties of this module are load-bearing rather than incidental:

- **No behaviour keys on the content of git's stderr, in either direction**
  (PRD G4). Every decision below reads an exit status, an established SHA, or
  a ref name selected by exact match. git's stderr is captured for a
  diagnostic and is never matched, parsed, or branched on. That is the half of
  AC-LAND-04 a static scan of this file verifies, and it is the half that
  cannot go stale when a message changes.
- **One write, and never a second.** There is exactly one `git push` in this
  file, on one path, and no failure path issues a write of any kind. There is
  no retry, no backoff, no force, no ref deletion, and no merge (PRD G7, §8).
"""

from __future__ import annotations

from . import report, repo

#: §7: a missing or rejected credential must fail fast rather than block on a
#: prompt no agent session can answer.
GIT_ENV = {"GIT_TERMINAL_PROMPT": "0"}

#: §3.2 step 3 reads both refs in one `ls-remote`, so §8's stated count of
#: remote reads before the write is one on both of G1's arms.
MAIN_REF = "refs/heads/main"

#: PRD G1, first arm: the branch did not exist at the remote, so this landing
#: created it and there is no prior head to name.
CREATED = "created"


class SequenceError(Exception):
    """A git failure at a step §6 enumerates no failure mode for.

    §6 claims to be complete over the failure modes the design produces, and
    §5.3's token table is closed at ten. An implementation that met a git
    failure outside both and squeezed it into the nearest enumerated token
    would be putting a code on stderr that named a situation the tool had not
    observed — which is the one thing a report carrying only *observed* and
    *unknown* must never do. So it is raised instead, and `cli.run`'s backstop
    turns it into a diagnostic of its own and a non-zero exit with no report.

    Every use of this is recorded as a finding against §6 rather than treated
    as a designed path. All of them are states the §4.1 substrate cannot
    produce; see the report for this change.
    """


class StepResult:
    """What a step of §3.2 returns: the facts it established, or a stop (§3.7).

    `stage` is the token §5.3's token table assigns the stop, carried on the
    stop so the report can say where the sequence halted. `git_status` is the
    failing invocation's exit status, and is `None` where the stop is a
    comparison rather than a subprocess. `note` is git's own diagnostic, kept
    for the human-readable half of the stderr line and never read for a
    decision.
    """

    def __init__(self, ok, facts=None, stage=None, git_status=None, note=None):
        self.ok = ok
        self.facts = facts or {}
        self.stage = stage
        self.git_status = git_status
        self.note = note


def _stop(stage, git_status=None, note=None, **facts):
    return StepResult(False, facts, stage=stage, git_status=git_status, note=note)


def _ok(**facts):
    return StepResult(True, facts)


def _debracket(text):
    """git's own words, with its brackets removed.

    git writes `[rejected]` and `[new branch]` on stderr, and the bracketed
    token is this repository's diagnostic-code convention. The tool's own
    diagnostic is the only bracketed token it writes, so a git message worth
    surfacing is surfaced without its brackets rather than passed through.
    """
    collapsed = " ".join((text or "").split())
    return collapsed.replace("[", "").replace("]", "")


class Sequence:
    """§3.2's ordered steps over one working tree. Stops at the first failure."""

    def __init__(self, branch, message, paths, cwd):
        self.branch = branch
        self.message = message
        self.paths = list(paths)
        self.cwd = cwd
        self.branch_ref = "refs/heads/%s" % branch
        self.facts = {}

    # -- the git seam ------------------------------------------------------

    def git(self, *args):
        """`(exit status, stdout text, stderr text)`.

        Arguments are always an argv list through `repo.run`'s `subprocess.run`
        with no shell: a branch name, a commit message and a path are all
        caller-supplied text (§8, Security).
        """
        code, out, err = repo.run(list(args), cwd=self.cwd, env=GIT_ENV)
        return code, out.decode("utf-8", "replace").strip(), err

    @staticmethod
    def _refs(listing):
        """`{ref: sha}` from `ls-remote` output, keyed by the full ref name.

        Selected by exact ref name at the point of use, never by position or by
        line count: `ls-remote`'s patterns match against the tail of the ref on
        slash boundaries, so `main` also matches a branch named `sub/main` and
        the output may carry more lines than patterns given (§3.2 step 3).
        """
        refs = {}
        for line in listing.splitlines():
            sha, tab, ref = line.partition("\t")
            if tab and ref.strip():
                refs[ref.strip()] = sha.strip()
        return refs

    # -- step 2 ------------------------------------------------------------

    def fetch(self):
        """§3.2 step 2. Its exit status is the only thing read (PRD G4)."""
        code, _, err = self.git("fetch", "origin")
        if code != 0:
            return _stop("fetch", code, _debracket(err))
        return _ok()

    # -- step 3 ------------------------------------------------------------

    def resolve(self):
        """§3.2 step 3. One read answers both of G1's arms.

        Whether `<branch>` exists at the remote decides which arm applies, and
        `main`'s head is the base in the branch-absent arm. Either way the base
        SHA comes from this read and never from `refs/remotes/origin/<branch>`,
        which is a cache of a previous fetch.
        """
        code, out, err = self.git(
            "ls-remote", "--heads", "origin", self.branch, "main"
        )
        if code != 0:
            return _stop("resolve", code, _debracket(err))
        refs = self._refs(out)
        if self.branch_ref in refs:
            base = refs[self.branch_ref]
            return _ok(prior_head=base, base=base)
        # The read established that `<branch>` is absent at the remote, which
        # is G1's first arm, whether or not it named a base to land on.
        base = refs.get(MAIN_REF)
        if base is None:
            return _stop("resolve", None, None, prior_head=CREATED)
        return _ok(prior_head=CREATED, base=base)

    # -- step 4 ------------------------------------------------------------

    def base_object(self):
        """§3.2 step 4. Refuses rather than fetching again; the tool never loops.

        No cause is asserted. §3.2 step 4 names three that produce this same
        state, and reporting the state it observed while naming none of them is
        the only thing a report carrying just *observed* and *unknown* can
        honestly do here.
        """
        code, _, err = self.git(
            "cat-file", "-e", "%s^{commit}" % self.facts["base"]
        )
        if code != 0:
            return _stop("base-object", code, _debracket(err))
        return _ok()

    # -- step 5 ------------------------------------------------------------

    def guard(self):
        """§3.2 step 5. Two checks, in order, before any ref moves.

        Order is part of the guard: where the first check refuses the second is
        not evaluated at all and `<branch>`'s local SHA is never read, so
        `detail.branch_head`'s absence is the claim that the first check is the
        one that refused. Either check failing produces one refusal in one
        shape — FM-3, not two failure modes.
        """
        base = self.facts["base"]

        # The read comes first because `detail.local_head` is established on
        # every path this step runs, the one where this check refuses included.
        code, local_head, err = self.git("rev-parse", "HEAD")
        if code != 0:
            raise SequenceError(
                "cannot read local HEAD: %s" % _debracket(err)
            )
        code, _, err = self.git("merge-base", "--is-ancestor", "HEAD", base)
        if code != 0:
            return _stop("guard", code, None, local_head=local_head)

        # The ref step 6 rewrites is `<branch>`, and local HEAD is not it.
        # Without this check, step 6 resets `<branch>` and leaves whatever
        # unpushed commits it carried reachable from no ref at all.
        code, branch_head, _ = self.git(
            "rev-parse", "--verify", "--quiet", self.branch_ref
        )
        if code != 0:
            # No local ref of that name, so there is nothing to orphan. Not a
            # pass being assumed: the check has no subject.
            return _ok(local_head=local_head)
        code, _, err = self.git("merge-base", "--is-ancestor", branch_head, base)
        if code != 0:
            return _stop(
                "guard", code, None, local_head=local_head, branch_head=branch_head
            )
        return _ok(local_head=local_head, branch_head=branch_head)

    # -- step 6 ------------------------------------------------------------

    def establish_base(self):
        """§3.2 step 6, §3.3: `git checkout -B <branch> <base>`.

        Carries every uncommitted modification and untracked file across, which
        is the property that rules out `git reset --hard`. HEAD moves where the
        checkout was on another branch; §3.3 settles that the tool is permitted
        to move it and reports having done so.
        """
        code, current, _ = self.git("rev-parse", "--abbrev-ref", "HEAD")
        # `HEAD` here is git's answer for a detached checkout, which is not a
        # branch HEAD was moved off.
        prior = current if code == 0 and current not in ("HEAD", self.branch) else None

        code, _, err = self.git("checkout", "-B", self.branch, self.facts["base"])
        if code != 0:
            return _stop("base", code, _debracket(err))
        return _ok(prior_branch=prior) if prior else _ok()

    # -- step 7 ------------------------------------------------------------

    def stage(self):
        """§3.2 step 7. Authoritative over the index, then staging.

        The reset is not redundant with step 6: `git checkout -B` does not
        clear a pre-populated index, so without it content staged before the
        invocation survives into the commit and defeats AC-LAND-02. It touches
        the index only — the working tree and untracked files are left exactly
        as they were, which is the property that rules it in, because the tool
        must never discard what it exists to land.
        """
        code, _, err = self.git("reset", "--mixed", self.facts["base"])
        if code != 0:
            raise SequenceError(
                "cannot reset the index to the base: %s" % _debracket(err)
            )
        args = ["add", "--"] + self.paths if self.paths else ["add", "-A"]
        code, _, err = self.git(*args)
        if code != 0:
            return _stop("stage", code, _debracket(err))
        return _ok()

    # -- step 8 ------------------------------------------------------------

    def commit(self):
        """§3.2 step 8. The message is an argv element, never a shell word.

        The repository's hooks run: `bin/land` never passes `--no-verify`. A
        tool on the write path that bypassed the pre-commit hook would be
        landing work the governance never saw, so a hook refusal is a failure
        mode rather than something to work around.

        The staged set is read **before** the commit, so the two stops step 8
        carries are separated by an established fact rather than by reading
        git's account of why it refused. An empty staged set and a hook
        refusal are different situations a session must answer differently.
        """
        code, listing, err = self.git(
            "diff", "--cached", "--name-only", "-z", self.facts["base"]
        )
        if code != 0:
            raise SequenceError(
                "cannot read the staged set: %s" % _debracket(err)
            )
        staged = [path for path in listing.split("\0") if path]

        code, _, err = self.git("commit", "-m", self.message)
        if code != 0:
            token = "commit" if staged else "nothing-staged"
            return _stop(token, code, _debracket(err))

        code, head, err = self.git("rev-parse", "HEAD")
        if code != 0:
            raise SequenceError(
                "cannot read the commit just made: %s" % _debracket(err)
            )
        return _ok(head=head, files=staged)

    # -- step 9 ------------------------------------------------------------

    def push(self):
        """§3.2 step 9. Plain: never `-u`, never `--force`, never `--delete`.

        The exit status is the outcome (PRD G4). On a refusal the local commit
        is left in place deliberately — the work exists and is reachable from
        local HEAD, and undoing it would be a destructive operation the tool
        does not offer (PRD §7, §6).
        """
        code, _, err = self.git("push", "origin", self.branch)
        if code != 0:
            return _stop("push", code, _debracket(err))
        return _ok()

    # -- step 10 -----------------------------------------------------------

    def verify(self):
        """§3.2 step 10. The head check first, the comparison only where it passed.

        That order is why a remote whose content was mutated between the push
        and this step stops at the head check rather than at the comparison:
        under git transport such a mutation moves the branch's head, so it
        surfaces as FM-8 and never as a per-file mismatch. §6 struck the
        per-file mismatch mode as unreachable for that reason, and §4.3 gives
        the argument.
        """
        head = self.facts["head"]
        code, out, err = self.git("ls-remote", "--heads", "origin", self.branch)
        if code != 0:
            raise SequenceError(
                "cannot read the branch head at origin after the push: %s"
                % _debracket(err)
            )
        remote_head = self._refs(out).get(self.branch_ref)
        if remote_head is None:
            raise SequenceError(
                "the push completed and origin names no head for the branch"
            )
        if remote_head != head:
            # The stop is a comparison rather than a failed subprocess, so it
            # carries no git status (§5.3).
            return _stop("verify", None, None, remote_head=remote_head)

        code, _, err = self.git("fetch", "origin", self.branch_ref)
        if code != 0:
            raise SequenceError(
                "cannot fetch back the branch just pushed: %s" % _debracket(err)
            )
        matches = {}
        for path in self.facts["files"]:
            matches[path] = self._blob(head, path) == self._blob(remote_head, path)
        if not all(matches.values()):
            # §4.3: under git's content addressing a commit SHA determines its
            # tree, so once `ls-remote` returns the SHA that was pushed the
            # per-file blob SHAs necessarily agree. Reaching here means that
            # argument is false, and §6 enumerates no mode for it — the row
            # that did was struck as unreachable. Refusing loudly is the only
            # honest answer; inventing a terminal path is not.
            raise SequenceError(
                "a per-file blob comparison mismatched at a head origin "
                "confirmed, which TRD §4.3 argues cannot happen"
            )
        return _ok(remote_head=remote_head, matches=matches)

    def _blob(self, rev, path):
        """The blob SHA of `path` at `rev`, or None where the path is absent."""
        code, sha, _ = self.git("rev-parse", "%s:%s" % (rev, path))
        return sha if code == 0 else None

    # -- the driver --------------------------------------------------------

    #: §3.2's ordered steps. Step 1 is `argparse`, in `bin/land`, and step 11
    #: is the report, which is `bin/land`'s too.
    STEPS = (
        "fetch",
        "resolve",
        "base_object",
        "guard",
        "establish_base",
        "stage",
        "commit",
        "push",
        "verify",
    )

    def run(self):
        for name in self.STEPS:
            result = getattr(self, name)()
            # A stop carries facts too: the step that refuses has established
            # what it read before deciding, and §5.3's table names several of
            # those on the refusal paths.
            self.facts.update(result.facts)
            if not result.ok:
                return report.Report.build(self.branch, self.facts, result)
        return report.Report.build(self.branch, self.facts, None)


def land(branch, message, paths, cwd):
    """§3.7's one entry point. Every terminal state comes back as a `Report`.

    It raises nothing for an expected failure: success and failure alike return
    a report, and `bin/land` serializes what it is handed and maps the report's
    exit code onto its own.
    """
    return Sequence(branch, message, paths, cwd).run()
