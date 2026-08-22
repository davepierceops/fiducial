# Review: LEXICON.md — cycle 13

Verdict: ready-with-findings
Reviewed: LEXICON.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate; the added question is whether the corpus now uses terms LEXICON does not fix.
Cross-checked: docs/global-context/core.md (Vocabulary; Evidence 6), docs/global-context/decision-layer.md, operating-model.md, prose-criteria.md, roles/writer.md, roles/skeptic-risk-agent.md, engagements/skeptic.md, roles/release-manager-agent.md, skills/conversation-retro.md, engagements/sre/override-log-policy.md — all @ 8402c23; plus the tree at 2b9c856.
Not inspected: whether the spec-state terms are the right model for concurrency (settled in earlier cycles); the retired-terms tombstones, which were checked for currency and are current.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/LEXICON-cycle-12.md (reviewed @ 2b9c856)
Dave should inspect: LX-1 — resolving it was already decided once (2026-08-20, recorded in docs/global-context/inventory.md) and never executed; the decision may simply need re-issuing.

## LX-1 — non-blocking
Claim: A second claims taxonomy entered the corpus at eea66dd and LEXICON does not reconcile it, leaving `inferred` with two definitions and `tier` with two senses.
Location: LEXICON.md as a whole — the omission. The colliding text is prose-criteria.md:53-67 (Claims taxonomy: relayed / demonstrated / inferred / opinion) against docs/global-context/core.md:22 (Evidence 6: observed / inferred / told / unknown).
Evidence: Verified by running — prose-criteria.md and docs/global-context/core.md are both in the `writer` bundle (19 files, computed over `audience:` at 8402c23), so both definitions of `inferred` reach one session. Core defines it as "you reasoned to it"; prose-criteria defines it as "grounded in experience, observation, or data below the bar for proof," which is a strictly different set. Separately, `tier` means model tier in docs/global-context/decision-layer.md:14 and docs/global-context/review-rubric.md:38, and claim tier in prose-criteria.md:41 and :65. LEXICON was last reviewed at 2b9c856, before eea66dd created this pairing. Criterion 11 as it applies to LEXICON's own job — "terms with a fixed meaning across this methodology."
Consequence: A Writer session holds two four-item ladders, one of which reuses a word from the other with a different boundary, and must decide by inference which governs a given sentence. docs/global-context/inventory.md:164 records the resolution Dave already reached on 2026-08-20 — "Prose ladder is provenance under other names → `prose-criteria.md` adopts the core's" — which was never carried out.
Fix: Either execute the recorded decision (prose-criteria adopts Core's four classes) or add a Lexicon entry fixing the two ladders as distinct axes and renaming the collision, and add a `tier` entry distinguishing model tier from claim tier.
Related: PC-1
