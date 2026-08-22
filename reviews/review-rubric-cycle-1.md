# Review: docs/global-context/review-rubric.md — cycle 1

Verdict: ready-with-findings
Reviewed: docs/global-context/review-rubric.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria applied to the file that states them, criterion 10 answered first. Surfaced by the reconciliation re-gate's scope enumeration as a governed file with no review artifact at any cycle; it is not one of the nine first-cycle files the directive names. Reviewing the rubric against itself is circular by construction and is noted as such rather than hidden.
Cross-checked: docs/global-context/core.md (Acting 14; Standing 3), docs/global-context/decision-layer.md (14), LEXICON.md (Retired terms), roles/context-quality-reviewer.md, skills/review-artifact.md, policies/document-metadata-policy.md — all @ 8402c23.
Not inspected: whether eleven is the right number of criteria, or whether any criterion is the right criterion — that is Dave's, and this role does not gate the rubric it is judged by.
Findings: 2 — 2 non-blocking
Prior cycle: none
Dave should inspect: RR-1 — whether the rubric is exempt from criterion 4 by design. If it is, saying so costs one sentence and closes the question permanently.

## RR-1 — non-blocking
Claim: Two of the eleven criteria restate rules Core and LEXICON already state, which is the thing criterion 4 forbids.
Location: docs/global-context/review-rubric.md:44-46 (criterion 9) against docs/global-context/core.md:33 (Acting 14); docs/global-context/review-rubric.md:38-39 (criterion 8) against LEXICON.md:115-117 (Track, retired).
Evidence: Inferred by reading, with both texts read at 8402c23. Criterion 9's "Any filename the file prescribes or generates follows the convention, unless a stated convention names the file. No random strings, hashes, or UUIDs" is Core Acting 14 with the ISO 8601 example removed. Criterion 8's "Track does not appear" is LEXICON's tombstone restated as a test. Criterion 4.
Consequence: The rubric is in the `context-quality-reviewer` bundle alongside both Core and LEXICON, so a reviewer session holds each rule twice. More consequentially, a criterion that mirrors a Core rule drifts silently when Core is revised — criterion 9 was already amended once at 089083c to re-align with Core rule 14, which is the drift this predicts.
Fix: State the exemption — a rubric criterion is a test *for* a stated rule and may name it — or replace the restatements with citations to the rule's home. Either resolves it; leaving it unstated does not.

## RR-2 — non-blocking
Claim: The rubric's scope sentence and roles/context-quality-reviewer.md's scope list define the reviewable set differently, and neither matches the set actually reviewed.
Location: docs/global-context/review-rubric.md:9-11 ("Criteria every non-code file in this repository is examined against") against roles/context-quality-reviewer.md:12-17 (an enumeration of ten document classes).
Evidence: Verified by running — "every non-code file in this repository" is 300+ files at 8402c23 including docs/history/, docs/batons/, docs/cycles/, reviews/, and retros/, none of which any cycle has reviewed or should. The role document's enumeration is narrower and, as of eea66dd, names a class (`writing/`) that no longer exists. The set this re-gate actually enumerated is 52 files. Criterion 11 — an underspecified condition the agent must resolve by inference.
Consequence: A reviewer session cannot derive its own scope from either document, so scope arrives only in the directive. That worked across 26 cycles because a decision session set it each time; it is not a property of the governed text.
Fix: State the scope once, in one home, as a rule that resolves mechanically — the frontmatter in-scope set plus the named exceptions — and have the other document cite it rather than re-enumerate.
Related: CQR-1
