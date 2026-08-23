# Review: context-sets/testing-and-verification.md — cycle 3

Verdict: ready-with-findings
Reviewed: context-sets/testing-and-verification.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: context-sets/testing-and-verification.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed context-sets/testing-and-verification.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; LEXICON.md for the evidence classes; policies/verification-boundary-policy.md for the mock-boundary checklist, boundary types and the complementary-cuts statement; context-sets/production-grade-software.md; roles/test-designer-agent.md and roles/skeptic-risk-agent.md; specs/trd-template.md sections 2 and 4; policies/document-metadata-policy.md Required and Conditional fields.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/testing-and-verification-cycle-2.md

## TV-1 — non-blocking
Claim: The frontmatter carries `depends-on:`, a key no governed document defines.
Location: context-sets/testing-and-verification.md:6 (`depends-on: []`)
Evidence: Verified by running. The same grep and the same reading of policies/document-metadata-policy.md's field lists recorded under PGS-1; this file is one of exactly three carriers.
Consequence: As PGS-1 — an undefined key sitting in governed frontmatter, tolerated by enforcement and unexplained by any policy.
Fix: As PGS-1 — define the key in the metadata policy or drop it here.
Related: PGS-1, SCD-1
