# Review: skills/directive-authoring.md — cycle 1

Verdict: ready-with-findings
Reviewed: skills/directive-authoring.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. Surfaced by the reconciliation re-gate's scope enumeration as a file with no review artifact under its own stem; it is not one of the nine first-cycle files the directive names. The file was created at 1bbd5b7 as the successor to skills/directive-dispatch.md, which carries nine review artifacts under the old stem — so this is cycle 1 of the stem and, in substance, the tenth look at the material.
Cross-checked: docs/global-context/core.md (Vocabulary — Directive, Directive file, Execution block, Instruction, Companion document), docs/global-context/decision-layer.md (13, 14, 16), LEXICON.md (Spec state), roles/chief-of-staff.md (Open spec deltas), context-sets/spec-and-change-discipline.md (Open spec delta), skills/spec-review-cycle.md (Hard constraints) — all @ 8402c23.
Not inspected: the nine prior `directive-dispatch` artifacts as a decision record — their dispositions were not re-opened here; whether the retired document's residue was carried across correctly at 1bbd5b7.
Findings: 2 — 2 non-blocking
Prior cycle: none under this stem. reviews/directive-dispatch-cycle-1.md through -cycle-9.md review skills/directive-dispatch.md, the retired predecessor. See DA-2.
Dave should inspect: DA-2 — the stem-renumbering question recurs across the corpus and is worth settling once.

## DA-1 — non-blocking
Claim: The mid-delta rule is stated here and in three other files, and this file is not its home.
Location: skills/directive-authoring.md:20-21 ("Mid-delta directives derive from the spec branch, not the default branch, and pin its SHA.")
Evidence: Verified by running — a corpus-wide sweep for `spec branch` returned the same rule at roles/chief-of-staff.md:101-104, context-sets/spec-and-change-discipline.md:54-57, and skills/spec-review-cycle.md:35-37, plus this file. All four are in the `chief-of-staff` bundle at 8402c23. Criterion 4's neighbourhood — Core is not the other home, so recorded against criterion 10, "contributes something no other file in that bundle states."
Consequence: One rule, four wordings, one bundle. context-sets/spec-and-change-discipline.md:54 says the directive "derives from" the spec branch; roles/chief-of-staff.md:101 says it "cites" and "pins"; this file says "derive from ... and pin." They agree today. Nothing keeps them agreeing, and the reader holding all four cannot tell which is authoritative.
Fix: Pick the one home — context-sets/spec-and-change-discipline.md states the open-delta model and is the natural one — and cut the other three to nothing.

## DA-2 — non-blocking
Claim: The review-artifact stem convention loses the review history of a renamed document, and this file is the live instance.
Location: skills/directive-authoring.md as a whole — the file has nine cycles of review history that its own stem cannot reach.
Evidence: Verified by running — `reviews/directive-dispatch-cycle-1.md` through `-cycle-9.md` exist at 8402c23; no `reviews/directive-authoring-cycle-*.md` did before this artifact. skills/review-artifact.md:46-55 derives the artifact path from "the reviewed document's basename," which changes when the document is renamed. The same break exists for skills/review-artifact.md itself (split from spec-review-cycle.md at 1bbd5b7). Criterion 11 — an underspecified condition, resolved here by inference.
Consequence: A reader deriving the path mechanically, as the convention promises, finds cycle 1 and concludes the document is unreviewed. It has been reviewed nine times.
Fix: In skills/review-artifact.md, state what a rename does to the cycle number — carry the count forward, or restart it and name the predecessor stem in the `Prior cycle` line. This artifact does the latter; the convention does not require it.
Related: RA-2
