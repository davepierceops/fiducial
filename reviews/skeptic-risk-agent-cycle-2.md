# Review: roles/skeptic-risk-agent.md — cycle 2

Verdict: changes-required
Reviewed: roles/skeptic-risk-agent.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: roles/skeptic-risk-agent.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed roles/skeptic-risk-agent.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; context-sets/testing-and-verification.md Minimal acceptable practice and Verification classes; context-sets/production-grade-software.md Evidence requirements; LEXICON.md Release impact labels; policies/release-readiness-policy.md; policies/verification-boundary-policy.md Reviewer obligations and Release requirement; roles/release-manager-agent.md, which owns the ship call; engagements/critic.md, the advisory counterpart.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 1 blocking, 0 non-blocking
Prior cycle: reviews/skeptic-risk-agent-cycle-1.md
Dave should inspect: SR-1 — whether manual verification on a material boundary should ever be blocking, and where the line sits, is a risk-tolerance call this role cedes.

## SR-1 — blocking
Claim: The `blocking` gap-label examples name two practices that other governed files sanction as acceptable, so applying this list marks conforming work as not release-ready.
Location: roles/skeptic-risk-agent.md, Gap labels — the `blocking` list, entries "manual verification instead of automated verification" and "incomplete monitoring"
Evidence: Inferred by reading, across four files at cd7db71. context-sets/testing-and-verification.md, Minimal acceptable practice, item 4: "Keep a pre-release checklist for verification not yet automated" — manual verification standing in for automation is named as the minimum acceptable practice, not as a defect. context-sets/production-grade-software.md, Evidence requirements, lists "manual verification checklist" among the evidence a production-grade claim rests on. Against "incomplete monitoring": this same file's `deferred` list names "additional synthetic monitoring" — so monitoring that is not yet complete is exemplified as `deferred` two lines below being exemplified as `blocking`.
Consequence: policies/release-readiness-policy.md states "A gap labelled `blocking` means the change is not release-ready." A Skeptic/Risk session applying this list marks any change relying on a pre-release manual checklist — the methodology's own stated minimum — as not release-ready, and has contradictory guidance for monitoring gaps within a single section. The two lists cannot both be followed, and the file gives no rule for choosing between them.
Consequence is not theoretical: the minimal-acceptable-practice path is the one small projects and early-stage features are told to take, so the collision fires on exactly the changes the lighter path was written for.
Fix: Move "manual verification instead of automated verification" and "incomplete monitoring" to the `deferred` list, or qualify both so they read as blocking only where the boundary is material and undeclared — e.g. "manual verification standing in for automation on a material boundary with no declared deferred path.
