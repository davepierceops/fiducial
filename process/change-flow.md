---
order: 10
topic: [change-flow]
role: [architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: Change Flow

A delta is the whole of what one piece of work changes. Review is charged once
per delta, at its close, by a reader that did not produce it [R0462, R1396].

| What changes | Closed by | Who reads |
|---|---|---|
| **Rules** — rows in `rules/` | intake, by its skill [R0944] | Context Quality Reviewer |
| **Process** — prose in `process/` | one read, then the human's approval, recorded in the decision log naming the SHA [R1270] | a session that did not draft it, then the human |
| **Spec** — `SPEC.md` | the spec branch's close: one read of its whole diff with the tests, one ruling [R0481] | Spec Reviewer, then the human |
| **Code** — the implementation | one pull request per unit of work, through the stages below | Reviewer and Skeptic/Risk, then the human at the gate |

Each meaningful change [R0465] runs these in order, by subagents but the human.

1. **Spec.** `SPEC.md` is approved [R1513] and the unit's acceptance criteria
   are written from it [R0472]; nothing is built against an open spec [R0017].
2. **Plan.** Plan mode, from the spec; a reviewer that
   did not write the plan reads it before anything dispatches [R0065].
3. **Build.** A test designer writes the unit's tests and confirms them red
   [R0478]; a different subagent implements to green [R0486, R0485].
4. **Review.** Quality, skepticism and continuity passes, each its own verdict
   [R0492] under one overall verdict [R1414]; a planned pass that did not run
   is recorded with why [R1617]. Apply the review dispositions below;
   `changes-required` means the delta has not closed; one more read over the
   diff since then closes it.
5. **Merge.** Each pull request receives an agent review [R0065] before merge.
6. **Release.** A routine change flows to release on its evidence under standing
   authorization [R0535]. A consequential change [R0534, R0535] goes through the
   gate skill — its `human-gate` issue, the human's explicit go [R0534] —
   before release. Done is the definition of done [R0509].

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

The human, or the Chief of Staff for him, may call a deep read of anything,
whole not diff, at any time [R1137].

For the Chief of Staff in decision sessions:

Propose a deep read at milestone moments — a major version cut, a significant structural change — without being asked.
