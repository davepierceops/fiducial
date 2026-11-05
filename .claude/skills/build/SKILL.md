---
name: build
description: Take a unit of work from the spec read through implementation, review, and release preparation.
---
<!-- fiducial:begin -->
# Process: Build

Take a unit of work from the spec read through implementation, review, and
release preparation.
Use `process/change-flow.md` for the delta's close and
`process/review-artifact.md` for its review record.

Invoke the verification-checklists skill for applicable verification work, and
pass that invocation explicitly to the relevant subagents; apply its role-specific
sections.

1. **Spec read.** Start with [R1611, R1513]; select the unit and its acceptance
   criteria [R0472].
2. **Plan.** Enter plan mode from that read, then take the plan through review
   [R0065, R0462] before dispatching its work.
3. **Tests.** Run a test-designer subagent for the unit [R0478]. Pass its tests
   and evidence to a different coder subagent for implementation; the agent
   that wrote the tests does not implement the unit.
4. **Implementation.** The coder works from the spec, plan, and test evidence
   [R0485]. Collect its implementation summary and mechanical results for the
   review.
5. **Review.** Send the diff and evidence to Reviewer and Skeptic/Risk
   subagents [R0065, R0462], using quality [R0487], skepticism [R0488, R0492],
   and the applicable continuity read [R1104, R1105]. The review record uses
   [R1414, R1617], and dispositions use [R1614].
6. **Release preparation.** Assemble `process/release.md`'s change package and
   readiness review [R0509]. Use the classification [R0535, R0536] to route a
   consequential change to `process/gate.md` before release [R0534, R0562].

Provenance: DEC-001300, DEC-001390; R0486; R1611, R0065, R0492, R1617 and the retained judgment cited above.
<!-- fiducial:end -->
