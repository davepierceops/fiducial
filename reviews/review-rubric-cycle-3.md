# Review: docs/global-context/review-rubric.md — cycle 3

Verdict: ready-with-findings
Reviewed: docs/global-context/review-rubric.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: docs/global-context/review-rubric.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed docs/global-context/review-rubric.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md and operating-model.md, all @ cd7db71, as the standing foundation every file is read against; roles/context-quality-reviewer.md Scope, which this file's preamble defers to for its own applicability; policies/document-metadata-policy.md Scope and Required fields, for criteria 2 and 3; docs/global-context/core.md rules 6 and 14, for criteria 8 and 9; LEXICON.md Retired terms and Tier, for criterion 8; skills/review-artifact.md, which carries the shape of what this rubric's application emits.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/review-rubric-cycle-2.md

## RR-1 — non-blocking
Claim: The title scopes the rubric to "Pass 1", but the rubric governs the current pass and every later one, so the title states a bound the body does not.
Location: docs/global-context/review-rubric.md:8 — "# Review Rubric — Fiducial Assembly, Pass 1 (prose)"
Evidence: Inferred by reading. The body states its own scope with no pass restriction: "Criteria every file in the Context Quality Reviewer's scope, as that role's Scope rule states it, is examined against." roles/context-quality-reviewer.md likewise binds the role to "every criterion of the review rubric" with no pass qualifier. This cycle is a Pass 2 re-gate and applies the file unchanged.
Consequence: Two effects, both on criterion 1's amnesiac bundle reader. "Fiducial Assembly" names a programme the reader cannot resolve from inside the bundle. And "Pass 1" invites an agent reviewing in a later pass to treat the rubric as spent — the body overrides it, but only for a reader who gets past the title.
Fix: Retitle to the durable scope, e.g. "# Review Rubric — Governed Context Documents (prose)", and let the body carry applicability as it already does.
