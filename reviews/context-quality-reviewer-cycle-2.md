# Review: roles/context-quality-reviewer.md — cycle 2

Verdict: changes-required
Reviewed: roles/context-quality-reviewer.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md, roles/spec-reviewer-agent.md, skills/spec-review-cycle.md, skills/review-artifact.md, prose-criteria.md — all @ 8402c23; plus the tree at ed926db (the prior cycle's reviewed SHA) and at eea66dd.
Not inspected: whether the rubric's eleven criteria are the right eleven — this file cites the rubric, it does not define it.
Findings: 2 — 1 blocking, 1 non-blocking
Prior cycle: reviews/context-quality-reviewer-cycle-1.md (reviewed @ ed926db)
Dave should inspect: CQR-2 — whether the Spec Reviewer's hard gate or this role's rubric cycle is what actually gates a methodology document is a decision, not a wording fix.

## CQR-1 — blocking
Claim: The Scope section names a document class that no longer exists and omits three that do.
Location: roles/context-quality-reviewer.md:12-17 ("...the engagement documents, and the writing documents.")
Evidence: Verified by running — `writing/` existed at ed926db, the SHA of the prior cycle, and was removed at eea66dd, which retired the writing pipeline. At 8402c23 no path under `writing/` exists. The documents that replaced it — prose-criteria.md at the repository root and roles/writer.md — are named by neither this Scope list nor its category terms, since "the role documents" covers roles/writer.md but nothing covers root-level prose-criteria.md. The list also omits docs/global-context/review-rubric.md and docs/global-context/inventory.md, both governed files at 8402c23. Criterion 3, criterion 11.
Consequence: A Context Quality Reviewer session reading this file as its scope statement is told to review a directory that is not there, and is given no instruction covering prose-criteria.md — which is why prose-criteria.md and the rubric itself have never been reviewed.
Fix: Replace "and the writing documents" with the public prose criteria; add the review rubric and the rule inventory to the list, or state the scope as a rule ("every governed non-code file") rather than an enumeration that must be maintained.

## CQR-2 — non-blocking
Claim: The file cedes the PRD and TRD to the Spec Reviewer but says nothing about the Spec Reviewer's hard gate over the same methodology documents this role reviews, leaving a boundary two roles could both claim.
Location: roles/context-quality-reviewer.md:27-31 ("What it cedes")
Evidence: Inferred by reading. roles/spec-reviewer-agent.md:27-31 states its gate review triggers on "initial authorship of any canonical document ... any canonical document, PRD and TRD and the methodology documents equally" and that this is a hard gate. roles/spec-reviewer-agent.md:110-112 and skills/spec-review-cycle.md:16-17 do resolve the overlap — "The Context Quality Reviewer runs rubric cycles; the Spec Reviewer runs spec cycles" — but neither of those documents is in the `context-quality-reviewer` bundle's role slot, and this file, which is, states only the PRD/TRD carve-out. Criterion 11, criterion 1.
Consequence: A Context Quality Reviewer reading only its own role document cannot tell whether its verdict is the gate on a methodology document or an input to someone else's, and criterion 11 makes exactly that inference a defect.
Fix: State here, in one sentence, that the Spec Reviewer holds the agreement gate over canonical documents and this role's rubric cycle is a separate pass whose verdict feeds it.
