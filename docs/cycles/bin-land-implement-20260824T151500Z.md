# Directive: bin/land — implement to green

Role: Coder Agent. Route: fresh execution session. Model tier: frontier.
Base: main @ 48aa1b577b46d924201c6f3fa097b11a52a7c66b.

specs/bin-land-trd.md is agreed as of 60ab9ed4. bin/tests/test_land.py is agreed
alongside it. The red-gate is confirmed behavioural: 440 tests, 137 failures,
1 skip, all 135 test_land failures on real behaviour against a deliberately-
wrong stub. Implement bin/land until they are green.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-implement-20260824T151500Z.md in the clone stated below,
   commit it on branch bin-land-implement, push plain, verify by ls-remote, and
   report the SHA read back from git.

Clone, not worktree — the sandbox denies writes to a checkout's .git directory:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-bin-land-implement"
    cd "$TMPDIR/fiducial-bin-land-implement"
    git rev-parse origin/main
    # must print 48aa1b577b46d924201c6f3fa097b11a52a7c66b — if not, STOP and surface
    git checkout -b bin-land-implement 48aa1b577b46d924201c6f3fa097b11a52a7c66b

If that path already exists, append a distinguishing suffix rather than removing
what is there — a prior session found a stale worktree at its assigned path
pointing back at /Users/dave/code/fiducial/.git. Do not touch
/Users/dave/code/fiducial.

Fallback if $TMPDIR is unset: /tmp/claude-501/fiducial-bin-land-implement.

Sandbox companions — read both at main 48aa1b57, follow as told except their
worktree language, which this directive overrides:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## Where the specification is

specs/bin-land-trd.md @ 48aa1b57 is canonical. specs/bin-land.md is the agreed
PRD above it. Read both whole before writing anything — this tool's design took
nine review cycles and four convergence rounds, and the parts that look
arbitrary are load-bearing decisions with recorded reasons.

Read the tests too. They are agreed and they are the specification in executable
form. **Where a test and your reading of the spec disagree, stop and surface.**
Do not adjust a test to match your implementation. Do not adjust an
implementation to satisfy a test you believe is wrong — say so instead.

## What to build

bin/land, plus whatever belongs in bin/aimeta/ alongside the other seven CLIs.
Follow the existing tools' structure — cli.py, repo.py and the rest are shared
and already do work you should not duplicate.

Delete the stub wholesale: bin/tests/fixtures/stub/ and everything under it. It
carries a THROWAWAY header naming you as the one who removes it. Update
bin/tests/test_land.py's script_dir reference so the suite invokes the real tool
at its real path — **that reference is the only change permitted to the test
file**, and it is a path, not an assertion.

## The one constraint the spec does not carry

§7 fixes twelve bracketed diagnostic codes. It does not say whether anything
else may appear in brackets on stderr, and git itself writes [rejected] on a
non-fast-forward push. Dave's decision, stated inline here as its origin:

**The tool's own diagnostic is the only bracketed token it writes.** Captured
git stderr is not passed through into the tool's own stderr. If a git message
needs surfacing, surface it without its brackets, or put it in the report.

## What green means

bin/tests/run reports 440 tests, 2 failures, 1 skip — the two failures being
exactly test_bn10_bundle_base_yields_exactly_itself and
test_bn10_transitive_body_references_are_followed_in_this_repo, which predate
this work and stay out of scope. Every test_land test passes.

bin/check-frontmatter --all exits 0.

A test that passes because it cannot fail is not green. Two tests were self-
reported as passing against the stub for structural reasons — the enumeration
guard and the twelve-codes transcription guard. Both guard the test module
rather than the tool; leave them alone. If you find a third that passes without
exercising anything, name it in the report rather than fixing it.

## Do not
- modify specs/bin-land-trd.md or specs/bin-land.md. Both agreed. A defect in
  either is a finding you surface, not an edit you make.
- modify any assertion, fixture, helper, or case in bin/tests/test_land.py. The
  script_dir path is the sole permitted change.
- register land in helpers.CLI_NAMES — round 1 flagged that it triggers
  AC-X-3/4/6/7 and OQ-9. Out of scope; a separate decision.
- resolve, retire, or reword any open technical question. Seven are open,
  including OQ-6, and they are open deliberately.
- reintroduce FM-9 or close the hole at 9.
- weaken, skip, or xfail any test.
- touch the two known AC-BN-10 bundle failures.
- flip any document's frontmatter.
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 48aa1b577b46d924201c6f3fa097b11a52a7c66b
- a test and the spec disagreeing about what the tool should do
- a test you believe asserts the wrong thing
- a terminal path the spec describes that you cannot reach in implementation
- anything requiring a design decision the spec does not already make

## Before pushing
Push plain, verify by ls-remote, read bin/land back at the pushed head, and
confirm bin/tests/fixtures/stub/ is gone from the remote tree. Report the head
SHA and every commit SHA, each read back from git.

## Report
What was done, not what this file says. All SHAs. The final suite counts. Any
test that passes without exercising the tool, named. Every place the spec was
ambiguous and how you resolved it — or that you stopped instead. Any seam where
you extended beyond this directive, named as such. Every claim labelled
observed / inferred / told / unknown.
