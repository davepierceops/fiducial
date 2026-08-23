# Review: context-sets/production-grade-software.md — cycle 3

Verdict: ready-with-findings
Reviewed: context-sets/production-grade-software.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: context-sets/production-grade-software.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed context-sets/production-grade-software.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; context-sets/testing-and-verification.md for the evidence list and the boundary-sensitive cut; policies/verification-boundary-policy.md for boundary types; LEXICON.md for Top K; policies/document-metadata-policy.md Required and Conditional fields, for the frontmatter keys this file carries.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/production-grade-software-cycle-2.md

## PGS-1 — non-blocking
Claim: The frontmatter carries `depends-on:`, a key no governed document defines.
Location: context-sets/production-grade-software.md:6 (`depends-on: []`)
Evidence: Verified by running. `grep -rn "depends-on"` over policies/, docs/global-context/, skills/, roles/, LEXICON.md and operating-model.md returns no match outside the three context-set files that carry it. policies/document-metadata-policy.md enumerates required fields (`status`, `last-reviewed`, `audience`, `session`), conditional fields (`superseded-by`, `order`) and an excluded list; `depends-on` appears in none of the three. `bin/check-frontmatter --all` exits 0, so enforcement tolerates the key without sanctioning it.
Consequence: A reader or a future bundler meeting `depends-on:` has no governed statement of its semantics. The value is empty today, so nothing acts on it; were one ever populated, nothing states what the dependency would mean or what would honour it, and the key reads as governed metadata when it is not.
Fix: Either define `depends-on:` in the metadata policy's conditional-fields list with its semantics, or drop the key from the three context sets that carry it.
Related: SCD-1, TV-1
