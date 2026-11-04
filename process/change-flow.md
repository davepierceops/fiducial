---
order: 10
topic: [change-flow]
role: [architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: Change Flow

A delta is the difference between a thing as it stands and as it will stand when
the work is done. Review is charged once per delta, at its close — never per
edit — by a reader that did not produce it [R0462], as one artifact [R1396].

| What changes | Closed by | Who reads |
|---|---|---|
| **Rules** — rows in `rules/` | intake, by its skill [R0944] | Context Quality Reviewer |
| **Process** — prose in `process/` | one read, then the human's approval, recorded in the decision log naming the SHA [R1270] | a session that did not draft it, then the human |
| **Spec** — `SPEC.md` | the spec branch's close: one read of its whole diff with the tests, one ruling [R0481] | Spec Reviewer, then the human |
| **Code** — the implementation | one pull request per unit of work, through the stages below | Reviewer and Skeptic/Risk, then the human at the gate |

Each meaningful change [R0465] runs these in order; the decision session runs
every step but the human's as a subagent.

1. **Spec.** `SPEC.md` is approved [R1513] and the unit's acceptance criteria
   are written from it [R0472]; nothing is built against an open spec [R0017].
2. **Plan.** Plan mode, from a whole read of the spec [R1611]; a reviewer that
   did not write the plan reads it before anything dispatches [R0065].
3. **Build.** A test designer writes the unit's tests and confirms them red
   [R0478]; a different subagent implements to green [R0486, R0485].
4. **Review.** Quality and skepticism, separate passes with separate verdicts
   [R0492], one artifact, one overall verdict [R1414]; a planned pass that did
   not run is recorded with why [R1617]. At triage a finding files-and-lands
   unless the human raises it to blocking [R1614].
5. **Gate.** A routine change merges by its pull request [R0570]; one in the
   consequential class [R0535, R0536] goes through the gate skill, which opens
   its `human-gate` issue and asks for the go [R0534, R0562].
6. **Release.** The human's call [R0490]; done is the definition of done [R0509].

The human, or the Chief of Staff for him, may call for a deep read of anything
at any time, whole rather than diff [R1137, R1138].
