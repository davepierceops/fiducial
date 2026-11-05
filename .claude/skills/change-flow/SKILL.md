---
name: change-flow
description: A delta is the whole of what one piece of work changes.
---
<!-- fiducial:begin -->
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
2. **Plan.** Plan mode, from a whole read of the spec [R1611]; a reviewer that
   did not write the plan reads it before anything dispatches [R0065].
3. **Build.** A test designer writes the unit's tests and confirms them red
   [R0478]; a different subagent implements to green [R0486, R0485].
4. **Review.** Quality, skepticism and continuity passes, each its own verdict
   [R0492] under one overall verdict [R1414]; a planned pass that did not run
   is recorded with why [R1617]. A non-blocking finding files-and-lands unless
   the human raises it [R1614]; `changes-required` means the delta has not closed; one more read over the
   diff since then closes it.
5. **Merge.** Every pull request merges [R0570], with an agent review on each
   [R0065].
6. **Release.** A routine change flows to release on its evidence under standing
   authorization [R0535]. A consequential change [R0535, R0536] goes through the
   gate skill — its `human-gate` issue, the human's explicit go [R0534, R0562,
   R0490] — before release. Done is the definition of done [R0509].

The human, or the Chief of Staff for him, may call a deep read of anything,
whole not diff, at any time [R1137, R1138].

## Rules

Before a unit's work starts, its acceptance criteria are written, derived from the spec and owned by the human; the Spec Reviewer's gate reaches specs and nothing else.

At a spec branch's close, put the reviewed diff to the human: one ruling by the human approves the spec and accepts the tests as its red-gate evidence, recorded in the decision log naming the reviewed SHA; nothing else closes it.

Take the release decision to the human; a change is released only on her call at that gate.

Run quality and skepticism as separate passes, each with its own verdict.

When a spec document needs an edit, propose it rather than making it. The licence to edit a spec freely while its branch is open is the owner's alone.

Treat neither the spec nor its tests as final until they cohere: every testable claim the spec makes has a test asserting it, and every test asserts something the spec states.

Give the human the pull request's whole diff, tests included, to read before she rules on it.

Bring the spec into line with what was actually built before closing an open spec delta.

### Definitions

**red-gate** — A red-gate is a test run that fails on wrong behavior. A run that fails only because the module under test does not exist yet is not one.
<!-- fiducial:end -->
