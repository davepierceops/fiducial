# Directive: bin/land — spec/test convergence, round 1 (retry)

Role: none established. This session is an orchestrator driving two subagents.
The corpus defines no orchestrator role — roles/orchestrator-agent.md is
superseded and frozen, and roles/chief-of-staff.md explicitly does not execute.
Constraints are stated inline. That the corpus lacks this role is a gap Dave
knows about; do not resolve it by adopting a role you are not.

Route: fresh execution session. Model tier: frontier.
Base: main @ 869121717da6737587625857430cf72b684575ac.

Supersedes docs/cycles/bin-land-converge-1-20260824T031500Z.md @ a0a95c32,
whose Step A is complete and whose Steps B and C never ran.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-converge-2-20260824T033000Z.md in the clone stated
   below, commit it on branch bin-land-converge-2, push plain, verify by
   ls-remote, and report the SHA read back from git.

Clone, not worktree. The sandbox now denies writes to a checkout's .git
directory, so `git worktree add` fails outright — observed by the prior session,
which had to improvise. Every earlier directive in this series said worktree and
is wrong on this point; the sandbox companion documents have not been corrected
yet. Use:

    git clone https://github.com/davepierceops/fiducial.git "$TMPDIR/fiducial-bin-land-converge-2"
    cd "$TMPDIR/fiducial-bin-land-converge-2"
    git rev-parse origin/main
    # must print 869121717da6737587625857430cf72b684575ac — if not, STOP and surface
    git checkout -b bin-land-converge-2 869121717da6737587625857430cf72b684575ac

Fallback path if $TMPDIR is unset: /tmp/claude-501/fiducial-bin-land-converge-2.
All repository work happens in that clone and nowhere else. Do not touch
/Users/dave/code/fiducial.

Sandbox constraints — read both companions at main 8691217, follow as told
except where this directive's clone instruction overrides their worktree
language:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md

## What this session is for

specs/bin-land-trd.md has been through nine review cycles with no tests and no
implementation. Every reviewer claim about what the tool would emit is inferred
by reading, because there is nothing to run. Reading has stopped finding things.

Dave's decision: spec and tests are open simultaneously, neither final, findings
flowing both ways, until the pair coheres. Then both flip to agreed together and
a separate agent implements. This session runs that convergence. It does not
implement bin/land.

## Step A — verify the registry, then dispatch nothing until it resolves

The adapters are installed at .claude/agents/architect.md and
.claude/agents/test-designer.md, on main as of 58e988ae. The prior session could
not use them because Claude Code's project root was .claude/agents rather than
the repo root, putting discovery at .claude/agents/.claude/agents/. This session
was started from the repo root to fix that.

Confirm both `architect` and `test-designer` resolve in the agent registry
before dispatching any work. If either does not, STOP and surface — report what
the registry does list and what path it searched. Do not substitute
general-purpose dispatches: that would give the test designer edit rights over
the spec and the architect write rights over the tests, which is the isolation
this whole design rests on.

## Step B — the convergence loop

Iteration bound: four rounds. Report at four whether or not it converged. Commit
at the end of each round, message naming the round and what moved.

Each round:

1. **Dispatch the test-designer subagent.** Brief it with the TRD and the PRD,
   not with the architect's reasoning. Its job: write bin/tests/test_land.py
   covering the TRD's stage acceptance criteria (AC-LAND-T01, T01a, T02, T03)
   and the report contract — §5.3's key table, §6's eleven failure modes,
   §5.2's value domains. It returns the tests it wrote, plus one finding per
   criterion it could not express as a test, with the reason.

2. **Triage.** Each finding is a spec defect, a test-design problem, or a
   question neither can settle. The third kind stops the loop.

3. **Dispatch the architect subagent** with the spec defects only — not the test
   designer's reasoning, not its test code. Its job: revise
   specs/bin-land-trd.md to close them. Blast radius: that file alone.

4. Re-dispatch the test designer against the revised spec.

Converged when a round produces no spec defects.

**Known finding, hand it to the test designer in round 1.** From
reviews/bin-land-trd-cycle-8.md @ f8190fdf, N2: AC-LAND-T01 enumerates one case
per failure mode, but branch_head and prior_branch are conditional within a
mode, so on six of ten cases "the detail keys the table establishes there" has
no single referent. Dave has decided this closes. The reviewer's proposed shape
— a mode with a conditional key contributes one case per condition — is on the
record; the test designer should reach its own conclusion and the architect
should draft its own wording.

## Step C — the red-gate

A test that fails only because bin/land does not exist proves nothing: a wrong
assertion fails identically to a right one. Per
context-sets/spec-and-change-discipline.md the red must be behavioral.

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
- implement bin/land. The stub is a test fixture; the Coder is a separate agent
  in a later session.
- modify specs/bin-land.md, specs/trd-template.md, or any PRD acceptance
  criterion or goal.
- flip either document's frontmatter or set last-reviewed. The spec stays draft.
  Dave flips spec and tests together, later, and that decision is his alone.
- modify the adapters or duplicate role content into .claude/agents/.
- reintroduce a second home for emission scope. §5.3's table is the single home
  and its prose is non-normative as of cycle 9.
- let the architect see the test designer's reasoning or code, or the reverse.
  You are the only channel; brief each one narrowly.
- renumber any failure mode, open technical question, or §3.2 step.
- touch bin/tests/run's two pre-existing AC-BN-10 bundle failures
  (test_bn10_bundle_base_yields_exactly_itself,
  test_bn10_transitive_body_references_are_followed_in_this_repo).
- merge, open a PR, force-push, or delete any ref.

## STOP and surface rather than improvise
- origin/main not at 869121717da6737587625857430cf72b684575ac
- either adapter failing to resolve in the registry
- a finding neither subagent can settle without a design decision
- the spec and the tests disagreeing about what the tool should do where the
  spec is silent on which is right
- four rounds elapsed without convergence — report, do not continue
- concurrent mutation in the clone

## Before pushing
bin/check-frontmatter --all must exit 0. bin/tests/run: report the count and
confirm the only failures are the two known ones.

Push plain, verify by ls-remote, read specs/bin-land-trd.md and
bin/tests/test_land.py back at the pushed head, report the head SHA and every
commit SHA read back from git.

## Report
What was done, not what this file says. All SHAs. Whether the registry resolved
both adapters, and what tools each subagent actually held. Per round: findings
raised, which were spec defects, what the architect changed. The red-gate result
test by test. Every question that stopped the loop. Any seam where you extended
beyond this directive, named as such. Every claim labelled observed / inferred /
told / unknown.
