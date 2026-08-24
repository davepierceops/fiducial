# Directive: bin/land — spec/test convergence, round 1

Role: none established. This session is an orchestrator driving two subagents,
and the corpus defines no orchestrator role — roles/orchestrator-agent.md is
superseded and frozen, and roles/chief-of-staff.md explicitly does not execute.
Its constraints are stated inline below. That the corpus lacks this role is a
gap Dave is aware of; do not resolve it by adopting a role you are not.

Route: fresh execution session. Model tier: frontier.
Base: main @ 15f92ba857ff850577b8440eaa10e6200ab61107.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-converge-1-20260824T031500Z.md in the worktree stated
   below, commit it on branch bin-land-converge-1, push plain, verify by
   ls-remote, and report the SHA read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-converge-1 (fallback
/tmp/claude-501/fiducial-bin-land-converge-1). Created:

    git fetch origin
    git rev-parse origin/main
    # must print 15f92ba857ff850577b8440eaa10e6200ab61107 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-converge-1" -b bin-land-converge-1 15f92ba857ff850577b8440eaa10e6200ab61107

Sandbox constraints — read both companions at main 15f92ba8, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## What this session is for

specs/bin-land-trd.md has been through nine review cycles and has no tests and
no implementation. Every reviewer claim about what the tool would emit is
inferred by reading, because there is nothing to run. Reading has stopped
finding things.

Dave's decision: spec and tests are open simultaneously, neither final, findings
flowing both ways, until the pair coheres. Then both flip to agreed together and
a separate agent implements. This session runs that convergence. It does not
implement bin/land.

## Step A — subagent adapters

.claude/agents/ holds only a README (read it; it is the governing rule). Role
definitions live in roles/ and must not be duplicated into .claude/. Claude Code
needs `name:` and `description:` frontmatter, which the role documents do not
carry and must not gain — that field set belongs to skills, and adding it to
roles is a metadata-scope change outside this session.

Write two thin adapters that carry the frontmatter Claude Code needs and point
at the corpus for content:
- .claude/agents/architect.md → roles/architect-agent.md
- .claude/agents/test-designer.md → roles/test-designer-agent.md

Scope each one's tools to what its job needs and no more. Read settings.json and
settings.local.json first and report what they permit; if per-subagent tool
scoping is not available, STOP and surface before dispatching anything — the
isolation this design rests on would be absent and Dave needs to know that
rather than have it discovered later.

## Step B — the convergence loop

Iteration bound: four rounds. Report at four whether or not it has converged.
Commit at the end of each round with a message naming the round and what moved.

Each round:

1. **Dispatch the test-designer subagent.** Brief it with the TRD and the PRD,
   not with the architect's reasoning. Its job: write tests at
   bin/tests/test_land.py covering the TRD's stage acceptance criteria
   (AC-LAND-T01, T01a, T02, T03) and the report contract — §5.3's key table,
   §6's eleven failure modes, §5.2's value domains. It returns: the tests it
   wrote, and one finding per criterion it could not express as a test, with the
   reason.

2. **Orchestrator triages.** A finding is a spec defect, a test-design problem,
   or a question neither can settle. The third kind stops the loop.

3. **Dispatch the architect subagent** with the spec defects only — not with the
   test designer's reasoning, not with its test code. Its job: revise
   specs/bin-land-trd.md to close them. Blast radius: that file alone.

4. Re-dispatch the test designer against the revised spec.

Converged when a round produces no spec defects.

**Known finding to hand the test designer in round 1**, from
reviews/bin-land-trd-cycle-8.md @ f8190fdf: N2 — AC-LAND-T01 enumerates one case
per failure mode, but branch_head and prior_branch are conditional within a
mode, so on six of ten cases "the detail keys the table establishes there" has
no single referent. Dave has already decided this closes. The reviewer's
proposed shape — a mode with a conditional key contributes one case per
condition — is on the record; the test designer should reach its own conclusion
and the architect should draft its own wording.

## Step C — the red-gate

A test that fails only because bin/land does not exist proves nothing: a wrong
assertion fails identically to a right one. Per
context-sets/spec-and-change-discipline.md, the red must be behavioral.

The test designer writes a deliberately-wrong stub at bin/land — clearly marked
as a stub the Coder replaces, never a partial implementation — sufficient for
the tests to run and fail on bad logic rather than on an absent import. Report
which tests fail for the right reason and which fail only on the stub's absence
of behavior.

## The constraint that matters most

**This loop takes no design decisions.** Nine cycles of churn happened because
new decisions were taken inside cycles meant to dispose findings, each one
falsifying prose written under the previous regime. A question the spec does not
answer stops the loop and comes to Dave. Do not resolve an ambiguity because
resolving it would let the round finish.

That includes: any change to what bin/land does; any new failure mode; any new
acceptance criterion beyond N2's closure; anything touching OQ-6 or §4.3.

## Do not
- implement bin/land. The stub is a test fixture, not an implementation, and the
  Coder is a separate agent in a later session.
- modify specs/bin-land.md, specs/trd-template.md, or any PRD acceptance
  criterion or goal.
- flip either document's frontmatter or set last-reviewed. The spec stays draft.
  Dave flips spec and tests together, later, and that decision is his alone.
- duplicate role content into .claude/agents/.
- reintroduce a second home for emission scope. §5.3's table is the single home
  and its prose is non-normative as of cycle 9.
- let the architect see the test designer's reasoning or code, or the reverse.
  The orchestrator is the only channel and briefs each one narrowly. Isolation
  between them is the point of running them separately.
- renumber any failure mode, open technical question, or §3.2 step.
- touch bin/tests/run's two pre-existing AC-BN-10 bundle failures.
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 15f92ba857ff850577b8440eaa10e6200ab61107 at fetch
- per-subagent tool scoping unavailable
- a finding neither subagent can settle without a design decision
- the spec and the tests disagreeing about what the tool should do, where the
  spec is silent on which is right
- four rounds elapsed without convergence — report, do not continue
- concurrent tree mutation in the assigned worktree

## Before pushing
bin/check-frontmatter --all must exit 0. bin/tests/run: report the count and
which failures are the two known pre-existing ones.

Push plain, verify by ls-remote, read specs/bin-land-trd.md and
bin/tests/test_land.py back at the pushed head, report the head SHA and every
commit SHA read back from git.

## Report
What was done, not what this file says. All SHAs. What the settings files
permit. Per round: findings raised, which were spec defects, what the architect
changed. The red-gate result, test by test. Every question that stopped the loop.
Any seam where you extended beyond this directive, named as such. Every claim
labelled observed / inferred / told / unknown.
