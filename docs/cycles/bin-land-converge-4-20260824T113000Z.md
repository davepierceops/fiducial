# Directive: bin/land — close OQ-11 and OQ-12

Role: none established. Orchestrator driving two subagents; constraints inline.
Route: fresh execution session. Model tier: frontier.
Base: main @ 9ad80c2c5f3186eb7dcaa56ec920825fb1e32e7e.

Final convergence session. Both remaining open questions have Dave's answers;
this session lands them in the spec and the tests, and nothing else.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-converge-4-20260824T113000Z.md in the clone stated
   below, commit it on branch bin-land-converge-4, push plain, verify by
   ls-remote, and report the SHA read back from git.

Clone, not worktree — the sandbox denies writes to a checkout's .git directory:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-bin-land-converge-4"
    cd "$TMPDIR/fiducial-bin-land-converge-4"
    git rev-parse origin/main
    # must print 9ad80c2c5f3186eb7dcaa56ec920825fb1e32e7e — if not, STOP and surface
    git checkout -b bin-land-converge-4 9ad80c2c5f3186eb7dcaa56ec920825fb1e32e7e

Fallback if $TMPDIR is unset: /tmp/claude-501/fiducial-bin-land-converge-4. All
repository work happens there. Do not touch /Users/dave/code/fiducial.

Sandbox companions — read both at main 9ad80c2c, follow as told except their
worktree language, which this directive overrides:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## Dave's decisions

Stated inline; this directive is their origin.

**D-OQ12 — the bracketed diagnostic codes are fixed in the spec.** §7 requires a
stable bracketed code per refusal and names none, so two correct implementations
could emit different codes and every existing test would pass either way. Name
one code per terminal path in §7. The tests assert them. Dave's reasoning, for
the document to carry in its own words: this report's consumer is an LLM agent,
the bracketed code is the most prominent thing it can match on, and a code set
invented by the implementer and documented afterward is an interface nobody
agreed to. Close OQ-12.

**D-OQ11 — non-ASCII is escaped.** Report values are serialized with
`ensure_ascii=True`, so stdout is pure ASCII and non-ASCII characters appear as
`\uXXXX` escapes. Dave's reasoning: a script's stdout must not depend on the
ambient locale being UTF-8; the escaped form has no failure mode where the raw
form can emit mangled bytes or fail outright, and both parse to identical data.
Close OQ-11. Update §5.2's pointer, which currently says the question is open.

## What to do

2. **Dispatch the architect** with both decisions. It drafts its own wording.
   For D-OQ12 it authors the code set: one per terminal path, consistent in
   form, each obviously readable as the situation it names. §5.4's nineteen
   terminal paths are the enumeration; a code per path, not per failure mode —
   modes split by conditional rows and conditional tokens, and the code has to
   discriminate what the agent must respond to differently. If the architect
   concludes some paths genuinely warrant a shared code, that is a design
   question — STOP and surface rather than deciding it.

3. **Dispatch the test designer** against the revised spec. It asserts the exact
   code on every terminal path, and asserts the ASCII property of stdout. The
   escaping assertion needs a fixture carrying a non-ASCII branch name or path;
   add one.

4. Re-run the red-gate. Both new assertion sets must fail behaviourally against
   the stub — the stub emits a fabricated exit code and its own diagnostic text,
   so codes should mismatch, and it must not be adjusted to make them pass.
   Extend the stub only as far as keeping the red behavioural, per the standing
   rule. Report test by test.

Iteration bound: two rounds. Report at two whether or not converged.

## The constraint that matters most

**This session takes no design decisions beyond the two above.** Both open
questions now have answers; there should be nothing left to decide. If a
question surfaces, stop and surface it — do not resolve it to finish the round.
Dave's standing instruction is to get to done, which means close these two
cleanly rather than opening a third.

## Do not
- implement bin/land beyond the stub. The Coder is the next session.
- modify specs/bin-land.md, specs/trd-template.md, or any PRD acceptance
  criterion or goal.
- resolve OQ-6 or any other open question. Nine were open; these two close, the
  rest stay.
- reopen FM-9, renumber any failure mode, or close the hole at 9.
- flip either document's frontmatter or set last-reviewed. Dave flips spec and
  tests together after this session, and that decision is his alone.
- move, guard, or delete the stub. It stays at bin/tests/fixtures/stub/ with
  both deliberate defects intact.
- modify the adapters or duplicate role content into .claude/agents/.
- reintroduce a second home for emission scope.
- let the architect see the test designer's code or reasoning, or the reverse.
- register land in helpers.CLI_NAMES.
- touch bin/tests/run's two known AC-BN-10 bundle failures.
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 9ad80c2c5f3186eb7dcaa56ec920825fb1e32e7e
- either adapter failing to resolve in the registry
- a terminal path the architect judges should share a code with another
- any assertion that cannot be made fail behaviourally against the stub
- two rounds elapsed without convergence — report, do not continue

## Before pushing
bin/check-frontmatter --all must exit 0. bin/tests/run: report the count and
confirm the only non-test_land failures are the two known ones.

Push plain, verify by ls-remote, read specs/bin-land-trd.md and
bin/tests/test_land.py back at the pushed head, report the head SHA and every
commit SHA read back from git.

## Report
What was done, not what this file says. All SHAs. The full code set as landed,
path by path. The red-gate result for both new assertion sets, test by test.
Whether OQ-11 and OQ-12 are both closed in §9, and the open-question count
before and after. Whether the spec and the tests agree, stated plainly. Any
question that stopped the session. Any seam where you extended beyond this
directive, named as such. Every claim labelled observed / inferred / told /
unknown.
