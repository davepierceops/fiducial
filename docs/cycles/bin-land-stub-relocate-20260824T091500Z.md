# Directive: bin/land — relocate the throwaway stub out of bin/

Role: Coder Agent. Route: fresh execution session. Model tier: Sonnet 5.
Branch: bin-land-converge-3, continued — not a new branch, and not off main.
Branch head at dispatch: 98c50006fbcb797b5cac3b240ca7850f7e430220.

This is mechanical relocation. Nothing about the spec, the tests' assertions, or
the tool's design is in scope.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-stub-relocate-20260824T091500Z.md in the clone stated
   below, commit it, push plain, verify by ls-remote, and report the SHA read
   back from git.

Clone, not worktree — the sandbox denies writes to a checkout's .git directory:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-stub-relocate"
    cd "$TMPDIR/fiducial-stub-relocate"
    git checkout bin-land-converge-3
    git rev-parse HEAD
    # must print 98c50006fbcb797b5cac3b240ca7850f7e430220 — if not, STOP and surface

Fallback if $TMPDIR is unset: /tmp/claude-501/fiducial-stub-relocate. All
repository work happens there. Do not touch /Users/dave/code/fiducial.

Sandbox companions — read both at branch head, follow as told except their
worktree language, which this directive overrides:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## Why

The throwaway stub currently sits at bin/land, bin/aimeta/land.py and
bin/aimeta/report.py. Round 2 gave it an unguarded `git add -A` followed by a
branch reset, to keep a test failing behaviourally. That is correct as a test
fixture and dangerous as a file in bin/: agents work in this repository
continuously, bin/ is where the real tools live, and an agent reaching for
bin/land because the TRD describes it would find something that stages
everything in the working tree and moves a branch.

Dave's decision: the stub moves out of bin/ before this branch merges. The
Coder still deletes it wholesale later; this only removes the trap in the
interim.

## What to do

2. Relocate all three stub files to a fixtures location under bin/tests/ —
   bin/tests/fixtures/stub/ unless the existing test layout makes another path
   obviously better. Pick the layout, state what you picked and why. The only
   hard constraint: nothing that looks like an invocable tool remains anywhere
   under bin/ top level.

3. Update every reference in bin/tests/test_land.py so the suite invokes the
   stub at its new path. The tests execute the CLI as a subprocess, so the
   executable bit and any interpreter line must survive the move.

4. Confirm the stub's THROWAWAY headers survive intact and still name the Coder
   as the one who deletes them.

## The check that proves this worked

Run bin/tests/run before and after. It must report **434 tests, 115 failures,
1 skip** both times, with the same tests failing for the same reasons. A
different count in either direction means the relocation changed behaviour,
which it must not — STOP and surface rather than adjusting a test to make the
number match.

bin/check-frontmatter --all must exit 0.

## Do not
- modify specs/bin-land-trd.md, specs/bin-land.md, or any other document.
- change any test assertion, fixture, or helper beyond the path references the
  move requires.
- change the stub's behaviour, including the unguarded `add -A` and the branch
  reset. Those defects are what keep two reds behavioural. Guarding them would
  be implementing past the stub.
- delete the stub. That is the Coder's job in the implementing session.
- register land in helpers.CLI_NAMES.
- touch bin/tests/run's two known AC-BN-10 bundle failures.
- flip any document's frontmatter.
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- branch head not at 98c50006fbcb797b5cac3b240ca7850f7e430220 at checkout
- the suite counts differing from 434/115/1 before the move — that means the
  branch is not in the state this directive assumes
- the counts differing after the move
- any reference you cannot update without changing what a test asserts

## Before pushing
Push plain, verify by ls-remote, read bin/tests/test_land.py back at the pushed
head, and confirm no file under bin/ top level is an invocable stub. Report the
head SHA and the commit SHA, each read back from git.

## Report
What was done, not what this file says. All SHAs. The path you chose and why.
The before and after suite counts. Confirmation that bin/ holds no stub. Any
seam where you extended beyond this directive, named as such. Every claim
labelled observed / inferred / told / unknown.
