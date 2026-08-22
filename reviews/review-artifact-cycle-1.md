# Review: skills/review-artifact.md — cycle 1

Verdict: changes-required
Reviewed: skills/review-artifact.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. Surfaced by the reconciliation re-gate's scope enumeration as a file with no review artifact under its own stem; it is not one of the nine first-cycle files the directive names. The file was created at 1bbd5b7, split out of skills/spec-review-cycle.md, which carries nine artifacts under its own stem.
Cross-checked: docs/global-context/core.md (Evidence 10; Acting 14), LEXICON.md (Release impact labels), docs/global-context/review-rubric.md, roles/context-quality-reviewer.md, engagements/skeptic.md, skills/boundary-audit.md, skills/evidence-review.md, skills/test-plan-review.md, roles/skeptic-risk-agent.md, roles/release-manager-agent.md — all @ 8402c23; plus every `reviews/*.md` filename at 8402c23, read mechanically for stem collisions.
Not inspected: whether the header fields are the right fields (settled across the spec-review-cycle cycles); the 200-odd existing artifacts, which this document explicitly does not retrofit.
Findings: 3 — 1 blocking, 2 non-blocking
Dave should inspect: RA-1 — the stem convention's failure mode is now demonstrated in the tree, not hypothetical, and the fix is a convention change.

## RA-1 — blocking
Claim: The filename convention collides in the live tree: three distinct documents map to the stem `README`.
Location: skills/review-artifact.md:46-55 (Filenames)
Evidence: Verified by running — at 8402c23 the tree contains `vendors/README.md` and `engagements/sre/README.md`, and `reviews/README-cycle-1.md` through `-cycle-3.md` review the retired repository-root `README.md` while `reviews/README-cycle-4.md` reviews `vendors/README.md` and says so in a prose "Filename note" it had to add. `engagements/sre/README.md` has no artifact; under the convention as written its first would be `reviews/README-cycle-5.md`, which would read as the fifth cycle of a document never reviewed. This re-gate's directive works around it by dictating `sre-<basename>` stems, which the convention does not authorize. Criterion 11 — the convention leaves the collision case to the writer's judgment.
Consequence: The convention's stated purpose is that "the path a reader needs is derivable from the document path without looking it up." For any basename that repeats, it is not derivable in either direction: from the artifact you cannot tell which document, and from the document you cannot tell which artifact. The file anticipates one repetition case (a stem ending in `-cycle` or a digit) and rules it harmless; it does not anticipate this one, which is not.
Fix: State the disambiguation rule. `<parent-dir>-<basename>` for any basename that is not unique in the corpus is the smallest change and matches what the directive already improvised.

## RA-2 — non-blocking
Claim: The convention says nothing about what a rename or a split does to the cycle number, and two live documents are in that state.
Location: skills/review-artifact.md:46-49
Evidence: Verified by running — skills/directive-authoring.md succeeded skills/directive-dispatch.md at 1bbd5b7, which has nine artifacts; this file was split out of skills/spec-review-cycle.md at the same SHA, which has nine. Under a mechanical reading both start at cycle 1, and this artifact and reviews/directive-authoring-cycle-1.md both do so while naming the predecessor in prose because the convention gave no rule. Criterion 11.
Consequence: `n` is described as "the cycle number," which a reader will take as the number of times the document has been reviewed. For a renamed document it is not, and nothing in the convention says so.
Fix: One sentence: on rename or split, restart at 1 and name the predecessor stem in `Prior cycle`. That is what practice already does; stating it makes the number honest.
Related: DA-2

## RA-3 — non-blocking
Claim: The Gap labels section restates a definition LEXICON already gives.
Location: skills/review-artifact.md:39-43 against LEXICON.md:70-80 (Release impact labels)
Evidence: Inferred by reading. This file says "`accepted-risk` is applied only where Dave's go or the release process has already accepted the gap; otherwise the gap is `blocking`." LEXICON says "**`accepted-risk`** — Dave or the release process has explicitly accepted the gap" and "A gap awaiting Dave's judgment is blocking." LEXICON is in all six bundles this file reaches. Criterion 10 — the paragraph contributes nothing the bundle does not already state.
Consequence: Two homes for one rule; the wordings differ ("has already accepted" against "has explicitly accepted") in a way that would matter if they ever drift apart.
Fix: Cut the paragraph. The `blocking`/`non-blocking`/`observation` distinction, which is this schema's own and is stated in the Findings section, is unaffected.
