---
order: 44
topic: [build]
role: [architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: Build

Take a unit of work from the spec read through implementation, review, and
release.
Use `process/change-flow.md` for the delta's close and
`process/review-artifact.md` for its review record.

Invoke the verification-checklists skill for applicable verification work, and
pass that invocation explicitly to the relevant subagents; apply its role-specific
sections.

Follow this sequence for each meaningful change [R0465] in software decision
and execution sessions, using subagents for the work and the human for
required approvals.

1. **Spec read.** Start from an approved `SPEC.md` [R1513]; select the unit
   and derive its acceptance criteria from the spec [R0472].
2. **Plan.** Enter plan mode from that read, then take the plan through review
   [R0462] before dispatching its work.
3. **Tests.** A test-designer subagent writes the unit’s tests and confirms
   they fail on bad logic [R0478]. Pass its tests
   and evidence to a different coder subagent for implementation; the agent
   that wrote the tests does not implement the unit.
4. **Implementation.** The coder works from the spec, plan, and test evidence
   to turn the tests green [R0485]. Collect its implementation summary and
   mechanical results for the review.
5. **Review.** Send the diff and evidence to Reviewer and Skeptic/Risk
   subagents [R0462], using quality [R1048], skepticism [R1058, R0492],
   and the applicable continuity read [R1104, R1105]. Record each pass’s
   verdict under one overall verdict [R1414]; record a planned pass that did
   not run and why [R1617]. Apply `process/change-flow.md`'s review dispositions.
6. **Merge.** Each pull request receives an agent review before merge.
7. **Release.** Assemble `process/release.md`'s change package and readiness
   review. A routine change may release on its evidence under standing
   authorization [R0535]. For a consequential change, use the gate skill for
   its `human-gate` issue and the human’s explicit go before release [R0534,
   R0535]. Completion is governed by the definition of done [R0509].

Provenance: DEC-001300, DEC-001390; R0486; R1611, R0065, R0492, R1617 and the retained judgment cited above.
