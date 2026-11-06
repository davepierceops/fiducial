---
order: 42
topic: [release]
role: [chief-of-staff, release-manager-agent, reviewer-agent, skeptic-risk-agent]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Release

Assemble one change package containing the evidence and release-readiness
assessment, and report its outcome.
The completion standard is [R0509]; verification is governed by the
verification and verification-boundaries rows and the verification-checklists
skill (apply its role-specific sections and explicitly invoke it for relevant
subagents), and the gate by
`process/gate.md` [R0534, R0535].

Assess release readiness in the package's readiness section, referencing its
existing evidence instead of copying it. Supply the user-visible behavior and
rollback or mitigation path. Where a required field has no source, mark it
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
Verification boundary status and updates: <status, changes and evidence>
SLO status and error budget consumption: <affected Top K user journeys>
Review findings: <artifacts and dispositions>
Known gaps: <explicit gaps>
Operational notes: <operating implications>
Human gate: <issue reference where consequential; otherwise N/A>

## Release readiness

User-visible behavior: <release-specific account>
Live/browser verification status: <where relevant; otherwise N/A>
Operational risks: <from the evidence>
Rollback or mitigation path: <release-specific path>
Release recommendation and human decision points: <recommendation; points needing a ruling>
~~~

The recommendation is exactly one of: `ship`; `ship with accepted risks`;
`do not ship`; `needs the human decision`.

## Shared report

For substantial implementation, review, or release work, report on the change
package or review artifact without replacing it.

Lead with the outcome and recommendation. Summarize supporting evidence, verification limits, material gaps, and decisions needed from the human; link the detailed artifact.

Provenance: DEC-001290; R0502, R0503, R1032, R1041, R1042, R1044, R1045, R0506; retained judgment cited above.
