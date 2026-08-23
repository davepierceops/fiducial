# Review: LEXICON.md — cycle 15

Verdict: ready-with-findings
Reviewed: LEXICON.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: LEXICON.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed LEXICON.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; policies/verification-boundary-policy.md and context-sets/testing-and-verification.md for the evidence classes; policies/release-readiness-policy.md and roles/skeptic-risk-agent.md for the release-impact labels; prose-criteria.md for the claim-strength ladder; docs/global-context/decision-layer.md rule 15 and docs/global-context/review-rubric.md criterion 8 for model tiers; specs/prd-template.md and specs/trd-template.md for Top K.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/LEXICON-cycle-14.md

## LX-1 — non-blocking
Claim: The file states no session kind, which criterion 7 requires of every file in scope.
Location: LEXICON.md:8-12 (the header paragraphs, where every other file in the corpus places its session-kind line)
Evidence: Inferred by reading. Read whole at cd7db71; every other of the 49 files reviewed this cycle carries an explicit session-kind sentence ("Rules for execution sessions", "governs both session kinds", "This file governs no session"). LEXICON.md carries none — its opening states only "Terms with a fixed meaning across this methodology" and the touch rule.
Consequence: A bundle reader cannot tell from the file whether its definitions bind decision sessions, execution sessions, or both. The `audience: [all-roles, human]` value implies both, but criterion 7 tests the file's text, not its selector, and an agent that reads the selector as scoping the vocabulary could treat a term as not binding on its session kind.
Fix: Add one sentence to the opening — "This file governs both session kinds" — matching the register operating-model.md and policies/document-metadata-policy.md use.
