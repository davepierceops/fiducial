# Directive: bin/land — spec/test convergence, round 2

Role: none established. Orchestrator driving two subagents; constraints inline.
Route: fresh execution session. Model tier: frontier.
Base: main @ 57a2e60683b8f5b44bbd536e343800636e1a0099.

Continues docs/cycles/bin-land-converge-2-20260824T033000Z.md @ b55ff614,
whose round 1 stopped at triage. Its Step A (registry) and Step C (red-gate)
are complete; do not redo them.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-converge-3-20260824T041500Z.md in the clone stated
   below, commit it on branch bin-land-converge-3, push plain, verify by
   ls-remote, and report the SHA read back from git.

Clone, not worktree — the sandbox denies writes to a checkout's .git directory:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-bin-land-converge-3"
    cd "$TMPDIR/fiducial-bin-land-converge-3"
    git rev-parse origin/main
    # must print 57a2e60683b8f5b44bbd536e343800636e1a0099 — if not, STOP and surface
    git checkout -b bin-land-converge-3 57a2e60683b8f5b44bbd536e343800636e1a0099

Fallback if $TMPDIR is unset: /tmp/claude-501/fiducial-bin-land-converge-3. All
repository work happens there. Do not touch /Users/dave/code/fiducial.

Sandbox companions — read both at main 57a2e606, follow as told except their
worktree language, which this directive overrides. Their keychain-noise note
covers fetch and push; round 1 observed the same noise on clone and ls-remote.
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## Dave's decisions — the three that stopped round 1

Stated inline; this directive is their origin.

**D-F2 — FM-9 is unreachable; strike it.** Round 1 established by construction
that a remote post-receive resetting the ref lands as FM-8, because step 10's
ls-remote check runs first. §4.3 already argued this; round 1 observed it.
Remove FM-9 and §4.1's mutation helper, whose only stated purpose was inducing
it. **Renumbering is authorised for this one change** — prior directives forbade
it to prevent churn, not on principle, and Dave lifts that here. Renumber
cleanly and sweep every reference. OQ-6 is not resolved by this and stays open:
FM-9 is struck as unreachable under the verification the tool performs today,
not because the fetched-bytes question is settled. Record that distinction in
the document so a future OQ-6 resolution knows it may reinstate the mode.

**D-F6 — FM-7 keeps exit 1. OQ-10 closes as no.** The report already names the
failure precisely, so a caller needing to distinguish it has a better source
than an integer, and a distinct code for one mode of ten is an asymmetry needing
a real caller that does not exist. Close OQ-10 with that reasoning.

**D-F5 — FM-5 and FM-6 get distinct stage tokens; add a tenth.** The empty-
staged case gets its own token. Dave's reasoning, for the document to carry in
its own words: the consumer of this report is an LLM agent, attempting a landing
with nothing staged will not be a rare case, and a policy rejection and an empty
commit are different situations an agent must respond to differently. §5.3's
nine-token closure is deliberately reopened to ten — record why, so the
reopening reads as a decision rather than drift.

## Round 2 — close everything

Dispatch the architect with the three decisions above plus the five findings
round 1 left open. Then re-dispatch the test designer against the revised spec.
Iteration bound: three further rounds. Report at three whether or not converged.

Findings to close, from round 1's report:

- **F1** — AC-LAND-T01 enumerates by failure mode, but conditional rows split a
  mode, and so do conditional stage tokens (FM-1's "fetch / resolve", FM-5's
  "stage or commit"). Make T01's unit a **terminal path**, and state that
  conditional rows and conditional tokens are what split a mode. This is wider
  than cycle-8's N2 stated; N2 closes as part of it.
- **F3** — Report.build cannot determine the terminal path the emission rule is
  keyed to. Round 1 found the rule circular on the FM-8/FM-9 pair. D-F2 removes
  that pair; confirm the rule is now well-formed on every remaining path and
  state how build determines the path. If it is still circular anywhere, that is
  a design question — STOP and surface.
- **F4** — §3.1/§3.7 say T01 is written without a landing; §5.4 says it is
  written against stdout. Two boundaries, both asserted. Resolve to one and say
  which. With FM-9 gone, end-to-end can reach every path.
- **F7** — §5.2 leaves five value domains open: detail.git_status's type,
  head.value's domain, branch.value's domain, whether a leaf carries exactly
  value+class, and whether non-ASCII is escaped. Close all five. Where closing
  one requires a behavioural choice rather than a drafting choice, STOP and
  surface that one rather than deciding it.
- **F8** — detail.local_head and detail.branch_head are established by a command
  §3.2 step 5 does not list; step 5 runs only merge-base --is-ancestor, which
  prints nothing. Mechanical fix.

The architect drafts its own wording throughout. Do not paste this directive's
phrasing into the document.

## What the test designer does in round 2

Revise bin/tests/test_land.py against the revised spec: T01's cases re-cut by
terminal path, FM-9's cases removed, the tenth stage token covered, the five
closed value domains asserted. Fix the two weak tests round 1 self-reported —
test_t01a_no_traceback_on_a_usage_error (cannot fail against any stub using the
standard argparse idiom) and test_t03_nothing_was_staged (passes by accident;
the stub's checkout -B leaves the index empty rather than refusing). Re-run the
red-gate and report test by test.

The throwaway stub stays a stub. Extend it only as far as keeping the red
behavioural requires.

## The constraint that matters most

**This loop takes no design decisions beyond the three above.** A question the
spec does not answer stops the loop and comes to Dave. Do not resolve an
ambiguity because resolving it would let the round finish. Dave's standing
instruction: get to done, do not cycle — which means close everything closeable
in one pass, and surface immediately rather than iterating around a question.

## Do not
- implement bin/land beyond the stub. The Coder is a separate agent, later.
- modify specs/bin-land.md, specs/trd-template.md, or any PRD acceptance
  criterion or goal.
- resolve OQ-6 or touch §4.3 beyond what D-F2's strike requires.
- flip either document's frontmatter or set last-reviewed. Dave flips spec and
  tests together, later.
- modify the adapters or duplicate role content into .claude/agents/.
- reintroduce a second home for emission scope. §5.3's table is the single home;
  its prose is non-normative.
- let the architect see the test designer's code or reasoning, or the reverse.
- register land in helpers.CLI_NAMES — round 1 flagged that it triggers
  AC-X-3/4/6/7 and OQ-9. Out of scope; leave the helpers where they are.
- touch bin/tests/run's two known AC-BN-10 bundle failures.
- create context-sets/base.md. Round 1 found it absent though CLAUDE.md requires
  it. Real, tracked separately, not this session's work.
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 57a2e60683b8f5b44bbd536e343800636e1a0099
- either adapter failing to resolve in the registry
- the emission rule still circular on any path after FM-9 is struck
- an F7 value domain whose closure is a behavioural choice
- any further finding needing a design decision
- three rounds elapsed without convergence — report, do not continue

## Before pushing
bin/check-frontmatter --all must exit 0. bin/tests/run: report the count and
confirm the only non-test_land failures are the two known ones.

Push plain, verify by ls-remote, read specs/bin-land-trd.md and
bin/tests/test_land.py back at the pushed head, report the head SHA and every
commit SHA read back from git.

## Report
What was done, not what this file says. All SHAs. Per round: what the architect
changed, what the test designer found. The renumbering sweep — every reference
updated, listed. The red-gate result test by test, including the two weak tests.
Whether the spec and the tests now agree, stated plainly. Every question that
stopped the loop. Any seam where you extended beyond this directive, named as
such. Every claim labelled observed / inferred / told / unknown.
