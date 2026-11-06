---
name: verification-checklists
description: Use when planning, performing or reporting verification, declaring or updating verification boundaries, or assessing deployment and release evidence, including error-budget conditions.
---
<!-- fiducial:begin -->
# Process: Verification Checklists

Use when planning, performing or reporting verification, declaring or updating verification boundaries, or assessing deployment and release evidence, including error-budget conditions.

Applies in decision and execution sessions. Sections apply to software unless they explicitly include writing. Apply each section’s role scope and conditions when the relevant work occurs.

## Verification planning, failure analysis and production assessment

Applies to chief-of-staff, test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent, release-manager-agent.

Treat a verification claim made against an exhausted or critical error budget as materially weaker than the same claim made with headroom, and say so wherever the claim bears on a release.

A production-verified claim states which SLO was checked and its current status — healthy, degraded, or exhausted — the error budget remaining where that is known, and whether error budget state was a factor in the release decision.

A production-verified claim never stands in for pre-deploy checks on a known high-risk path; run those checks as well.

For a meaningful change, be able to produce a confidence ledger — for each claim, the evidence, the boundary that evidence does not cross, and the deferred verification that would close it — kept no heavier than it takes to prevent false confidence.

A test plan for a meaningful change states acceptance criteria, behaviors under test, test levels used, mocked dependencies, fixture sources, contract assumptions, live verification needs, browser and PWA verification needs, production monitoring or synthetic checks where relevant, known unverified behavior, the release impact of each gap, and failure cases.

Treat these areas as boundary-sensitive by default: external APIs; auth and authorization; environment variables; per-clone state — hooks, local config, credential helpers; browser-only behavior; maps, tiles, geolocation, and rendering libraries; service workers and PWA offline behavior; payment, email, notification, and messaging services; storage and persistence; time, timers, and scheduling; rate limits, quotas, and billing; hosted databases; analytics and telemetry providers; domain and CORS restrictions; SLO targets and error budget state; and security and privacy controls. A package that retires or changes a tool which installs per-clone state names the operator step that removes it and where that step is published.

Every meaningful change answers: what happens if it fails; how the failure would be known, including whether it hits a Top K journey SLO and burns error budget; what the user would see; whether the system recovers; whether the human can debug or roll back; and whether the failure is acceptable.

## Boundary declarations and release assessment

Applies to architect-agent, chief-of-staff, coder-agent, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent.

State in a boundary declaration its boundary name, production surface, representation mechanism, verification class, verified claims, unverified claims, deferred verification path, release impact, cadence — how often the verification is re-run — failure response, and the owner or trigger for follow-up.

Create or update a boundary declaration when you add a mock, change a fixture for external data, add or change an external integration, add browser, PWA or service-worker behavior, change authentication or authorization behavior, change production environment or config assumptions, change monitoring or synthetic checks, discover that a test passed despite unverified production behavior, or ship with a known unverified dependency.

Put boundary information in one of these: the spec's standing verification-boundary section, a feature-specific verification ledger, inline test comments for a small or local boundary, a change package, a release-readiness review, or a pre-release checklist.

Declare durable or repeated boundaries in the spec's standing verification-boundary section or verification ledger; drift from it is a continuity finding.

Choose when a boundary's verification runs — manually before release, in a dedicated CI job, on a schedule, or after deploy as synthetic monitoring — by the risk of the boundary, not by a fixed schedule.

Verify a boundary material to user-visible behavior or release risk before release.

Verify a boundary that can drift after deployment by production monitoring.

## Release-impact labels

Applies to all roles in software and writing.

At the release decision, apply this labeling requirement:

Mark every known, unresolved boundary gap with one of the four release-impact labels — `blocking`, `deferred`, `accepted-risk`, `not-material`. `not-material` is a label, not an exemption from labelling.

For a gap labelled `blocking`:

Resolve a gap labelled `blocking` before release.

For a gap awaiting the human’s judgment:

A gap awaiting the human's judgment is not blocking by that fact alone: label it by its release impact, and let it reach him through the release package. "Requires the human decision" is not a label.

## Definitions

**mock** — A mock is a claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unverified.

**production-verified** — Production-verified evidence supports ongoing dependency health, real-world failure modes, regressions after deploy, availability, live user impact, SLO target compliance against the spec's targets for each Top K user journey, and error budget consumption.

**accepted risk** — Accepted risk is an explicit decision — the human's, or the release process's — to proceed despite a known gap.

**meaningful change** — A meaningful change is any change that warrants a change package — any change affecting behavior, interfaces, tests, dependencies, boundaries, or documentation of substance. A typo fix, a comment edit, or mechanical formatting is not meaningful in this sense.

**blocking** — A `blocking` gap is one the governing policies prohibit releasing with.

**boundary-sensitive** — Boundary-sensitive means do not overclaim here. It does not mean the area must be overtested.

**not-material** — A `not-material` gap is known but not relevant to the release decision.
<!-- fiducial:end -->
