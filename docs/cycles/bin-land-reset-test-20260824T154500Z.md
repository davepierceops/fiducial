# Directive: bin/land — close the untested reset

Role: Test Designer Agent. Route: fresh execution session. Model tier: frontier.
Base: main @ 48aa1b577b46d924201c6f3fa097b11a52a7c66b.

The implementing session found one surviving mutation: deleting §3.2 step 7's
`git reset --mixed <base>` leaves all 440 tests green. That reset is what keeps
a file staged before the invocation out of the commit — AC-LAND-02, agreed.
Confirmed by direct probe: without it, a pre-staged unrelated.txt joins
wanted.txt in the commit. No case in the agreed suite pre-populates the index,
so the line ships untested.

You write the case that closes it. The Coder does not test its own work, which
is why this is a separate session.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-reset-test-20260824T154500Z.md in the clone stated
   below, commit it on branch bin-land-reset-test, push plain, verify by
   ls-remote, and report the SHA read back from git.

Clone, not worktree — the sandbox denies writes to a checkout's .git directory:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-bin-land-reset-test"
    cd "$TMPDIR/fiducial-bin-land-reset-test"
    git rev-parse origin/main
    # must print 48aa1b577b46d924201c6f3fa097b11a52a7c66b — if not, STOP and surface
    git checkout -b bin-land-reset-test 48aa1b577b46d924201c6f3fa097b11a52a7c66b
    git merge --no-ff origin/bin-land-implement -m "Merge bin-land-implement"

The implementation lives on origin/bin-land-implement at
1373cb53f2fe9a9acd74c9c24120eb54050d21bb, not yet merged to main. You need it —
the test runs against the real tool. Verify that SHA is in your history after
the merge; if not, STOP and surface.

If the clone path already exists, append a distinguishing suffix rather than
removing what is there. Do not touch /Users/dave/code/fiducial.

Sandbox companions — read both at main 48aa1b57, follow as told except their
worktree language, which this directive overrides:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## What to write

One test case in bin/tests/test_land.py: stage a file the caller did not name,
invoke the tool with a different path, assert the resulting commit contains
exactly what was asked for and not the pre-staged file. Assert whatever else
AC-LAND-02 requires — read the agreed criterion and derive the assertions from
it, not from this paragraph.

Match the module's existing shape. It is an agreed artifact; a case that reads
foreign to the nineteen beside it is a defect even if it passes.

## The red-gate — this is the part that matters

A test written against working code passes on arrival and proves nothing. Yours
must be shown able to fail on the thing it exists to catch:

1. Remove step 7's reset from bin/aimeta/land.py.
2. Run the suite. Your new case must fail, and fail on the pre-staged file
   appearing in the commit — not on an error, an exception, or a missing file.
3. Restore the line, byte-identical. Verify with `git diff` that
   bin/aimeta/land.py is unchanged from the merged implementation.
4. Run the suite again. Everything green.

Report all four steps and both suite counts. If your case does not fail at step
2, it does not close the hole — say so rather than landing it.

## Record the amendment

specs/bin-land-trd.md and bin/tests/test_land.py were agreed together, recorded
in reviews/expedited-log.md at b31b75af. Adding a case changes the agreed suite,
so append one entry to that log recording the amendment: the date, the case
added, the criterion it covers, that the implementation is unchanged, and the
mutation evidence from the red-gate above. Match the log's existing format —
read it, do not invent a shape. The test file carries no frontmatter and nothing
is re-flipped; this entry is the record.

## Do not
- modify bin/aimeta/land.py, bin/aimeta/report.py, or bin/land, other than the
  temporary removal and byte-identical restoration in the red-gate above. The
  implementation is correct; only the test is missing.
- modify specs/bin-land-trd.md or specs/bin-land.md. Both agreed. A defect in
  either is a finding you surface.
- modify any existing assertion, fixture, helper, or case. You add one case; the
  nineteen and their supporting structure stay as they are.
- add a case to §5.4's enumeration or claim this is a twentieth terminal path.
  It is not — it is a property of an existing success path.
- weaken, skip, or xfail any test.
- register land in helpers.CLI_NAMES.
- touch the two known AC-BN-10 bundle failures.
- flip any document's frontmatter.
- merge to main, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 48aa1b577b46d924201c6f3fa097b11a52a7c66b
- 1373cb53f2fe9a9acd74c9c24120eb54050d21bb absent from history after the merge
- your case not failing at red-gate step 2
- bin/aimeta/land.py not byte-identical after restoration
- AC-LAND-02 requiring something you cannot assert
- the log's format not accommodating an amendment entry

## Before pushing
bin/check-frontmatter --all must exit 0. Final suite: 441 tests, 2 failures,
1 skip — the two known bundle ones.

Push plain, verify by ls-remote, read bin/tests/test_land.py and
bin/aimeta/land.py back at the pushed head. Report the head SHA and every commit
SHA, each read back from git.

## Report
What was done, not what this file says. All SHAs. The case as written. All four
red-gate steps with their suite counts. The log entry as landed. Any seam where
you extended beyond this directive, named as such. Every claim labelled
observed / inferred / told / unknown.
