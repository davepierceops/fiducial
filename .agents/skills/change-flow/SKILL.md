---
name: "change-flow"
description: "A delta is the whole of what one piece of work changes."
---
<!-- fiducial:begin -->
# Process: Change Flow

A delta is the whole of what one piece of work changes.

The following review requirement and closure table apply to architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent and test-designer-agent in software decision and execution sessions.

Review is charged once per delta, at its close, by a reader that did not produce
it [R0462, R1396].

| What changes | Closed by | Who reads |
|---|---|---|
| **Rules** — rows in `rules/` | intake, by its skill [R0944] | Context Quality Reviewer |
| **Process** — prose in `process/` | one read, then the human's approval, recorded in the decision log naming the SHA [R1270] | a session that did not draft it, then the human |
| **Spec** — `SPEC.md` | the spec branch's close: one read of its whole diff with the tests, one ruling [R0481] | Spec Reviewer, then the human |
| **Code** — the implementation | one pull request per unit of work, following the build skill | Reviewer and Skeptic/Risk, then the human at the gate |

For spec reconciliation in software and writing, across roles and in decision
and execution sessions:

Attach approval at reconciliation, to the version of record on the default branch; never to a revision the spec branch held before it.

For those same software roles and sessions, use the build skill for each
meaningful change [R0465], from the spec through release.

A `changes-required` review leaves the delta open; a further read over the
diff since that review closes it when the required changes are resolved.

## Review dispositions

These dispositions apply in software and writing decision sessions, with the
role scopes stated below.

For the Chief of Staff, Spec Reviewer, Context Quality Reviewer, Reviewer,
Skeptic/Risk, and Release Manager when triaging review findings:

A non-blocking finding's disposition at triage is file-and-land by default: it goes to the loose-end tracker and the delta lands. The human may raise a finding to blocking at triage, before the pull request merges; one raise buys one read over the diff since the reviewed revision. Nothing else reopens a delta.

For the Chief of Staff, Writer, Copy Editor, and Critic when a finding belongs
to a later stage:

Route a finding below the reviewed document's stage — a spec read raising an implementation question — to the loose-end tracker, where the next stage takes it up; it is not a blocking finding against the reviewed document and does not block the close.

## Deep reads

For the software roles and sessions listed above:

The human, or the Chief of Staff for him, may call a deep read of anything,
whole not diff, at any time [R1137].

For the Chief of Staff in software and writing decision sessions:

Propose a deep read at milestone moments — a major version cut, a significant structural change — without being asked.

## Rules

Before a unit's work starts, its acceptance criteria are written, derived from the spec and owned by the human; the Spec Reviewer's gate reaches specs and nothing else.

At a spec branch's close, put the reviewed diff to the human: one ruling by the human approves the spec and accepts the tests as its red-gate evidence, recorded in the decision log naming the reviewed SHA; nothing else closes it.

Run quality and skepticism as separate passes, each with its own verdict.

When a spec document needs an edit, propose it rather than making it. The licence to edit a spec freely while its branch is open is the owner's alone.

Treat neither the spec nor its tests as final until they cohere: every testable claim the spec makes has a test asserting it, and every test asserts something the spec states.

Give the human the pull request's whole diff, tests included, to read before she rules on it.

Bring the spec into line with what was actually built before closing an open spec delta.

### Definitions

**spec branch** — A spec branch is the branch a spec's edits land on. The branch existing, with commits on it, is the state; there is no status value for it and no register recording it.

**open spec delta** — An open spec delta is the interval during which a spec branch carries edits the default branch does not; the branch is open for exactly that interval, and it ends when the spec closes at approval. A revision of an approved spec opens a new delta on a new branch.

**reconciliation** — Reconciliation is the close of an open spec delta: the spec is brought into line with what was actually built.

**meaningful change** — A meaningful change is any change that warrants a change package — any change affecting behavior, interfaces, tests, dependencies, boundaries, or documentation of substance. A typo fix, a comment edit, or mechanical formatting is not meaningful in this sense.

**blocking** — A `blocking` gap is one the governing policies prohibit releasing with.

**decision session** — A decision session triages, decides, and produces the artifacts that direct and record work — plans, subagent prompts, session records, tracker updates. It reads freely and writes those artifacts; the changes a plan specifies happen elsewhere, in the session that runs it. The boundary is role in the flow, not capability: a decision session may hold a clone and may commit.

**version** — A document's version, at the moment it is referenced, is the SHA of the last commit that touched the file.

**red-gate** — A red-gate is a test run that fails on wrong behavior. A run that fails only because the module under test does not exist yet is not one.
<!-- fiducial:end -->
