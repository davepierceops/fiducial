---
order: 42
topic: [release]
role: [chief-of-staff, release-manager-agent, reviewer-agent, skeptic-risk-agent]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Release

Assemble the change package, release readiness review, and report from the
work's evidence.
The completion standard is [R0509]; verification is governed by the
verification and verification-boundaries rows and the verification-checklists
skill (apply its role-specific sections and explicitly invoke it for relevant
subagents), and the gate by
`process/gate.md` [R0534, R0535, R0562].

Assemble each readiness field from the change package wherever it already
states that item; supply user-visible behavior and the rollback or mitigation
path for the readiness review. Where a required field has no source, mark it
missing and carry it as a known gap.

## Change package

Use this template for a meaningful change. The test plan names the unit's
tests selected from the spec's suite and the spec-close review artifact that
records the suite's acceptance; test results include commands, skips, and a
recommendation on the sufficiency of the testing evidence.

~~~markdown
Intent: <what the change is for>
Acceptance criteria: <from the spec>
Test plan: <selected tests; spec-close review artifact>
Implementation summary: <what changed>
Test results: <commands run; skipped tests; evidence-sufficiency recommendation>
Verification boundary updates: <changes and evidence>
SLO status and error budget consumption: <affected Top K user journeys>
Review findings: <artifacts and dispositions>
Known gaps: <explicit gaps>
Operational notes: <operating implications>
Human gate: <issue reference where consequential; otherwise N/A>
Release recommendation: <one of the recommendations below>
~~~

## Release readiness review

~~~markdown
Change summary: <from the change package>
User-visible behavior: <release-specific account>
Test evidence: <from the change package>
Review findings: <from the change package>
Verification boundary status: <from the change package>
SLO status and error budget consumption: <affected Top K user journeys>
Live/browser verification status: <where relevant; otherwise N/A>
Operational risks: <from the evidence>
Rollback or mitigation path: <release-specific path>
Known gaps: <including missing source fields>
Recommendation and human decision points: <recommendation; points needing a ruling>
~~~

The recommendation is exactly one of: `ship`; `ship with accepted risks`;
`do not ship`; `needs the human decision`.

## Shared report

Use this reply template for substantial implementation, review, or release
work. Reviewers use it alongside the artifact in `process/review-artifact.md`;
it reports on the package or artifact rather than replacing either.

~~~markdown
Role: <the role reporting>
Intent: <what the work was for>
Evidence: <what was inspected or run; results and pointers>
Boundary: <what the evidence covers>
Gaps: <what remains unknown or unverified>
Recommendation: <the role's recommendation>
Human decision points: <what needs a ruling; none if none>
~~~

Provenance: DEC-001290; R0502, R0503, R1032, R1041, R1042, R1044, R1045, R0506; retained judgment cited above.
