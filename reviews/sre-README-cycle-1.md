# Review: engagements/sre/README.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/README.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 54 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — the file was produced by directive at 0e07753 (cycle 25) and has never been rubric-reviewed. Reviewed as one of the seven-file `engagements/sre/` set, with one artifact per file.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, docs/global-context/review-rubric.md, and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23. The predecessor text under docs/history/engagements/comfy/ was not consulted; this is a review of the file, not of the generalization.
Not inspected: whether brownfield SRE work is correctly characterized as a matter of engineering judgment; the accuracy of the four inversions against any actual engagement.
Findings: 3 — 1 blocking, 2 non-blocking
Prior cycle: none. `reviews/README-cycle-1.md` through `-cycle-4.md` review two other documents that share this basename; the `sre-` stem prefix used here is dictated by the re-gate directive, not by the artifact convention.
Dave should inspect: SRE-RM-1 — the fix is an `audience:` change on two other files, and which files land in which engagement bundle is a decision about what each role is trusted with.

## SRE-RM-1 — blocking
Claim: The file names two procedures the reader cannot reach, in bundles where those procedures are absent.
Location: engagements/sre/README.md:27 ("The Cartographer builds the map; the system-discovery skill is the procedure.") and :32-33 ("The baseline-measurement skill is the procedure.")
Evidence: Verified by running — bundle membership computed over `audience:` at 8402c23. This file lands in four bundles: `assistant` (26 files), `cartographer` (24), `skeptic` (23), `implementer` (23). engagements/sre/system-discovery.md carries `audience: [cartographer, assistant, human]` and is therefore absent from the `skeptic` and `implementer` bundles. engagements/sre/baseline-measurement.md carries `audience: [cartographer, implementer, assistant, human]` and is absent from the `skeptic` bundle. Criterion 3 (the references are file-shaped — "the system-discovery skill" is the basename) and criterion 1 (the reader is assumed able to reach another file).
Consequence: An Implementer session is told the baseline-gate is the red-gate of an engagement and that "the system-discovery skill is the procedure," and its bundle contains no such procedure. A Skeptic session is told the same about both procedures and has neither. The file's whole function is to point at the four inversions and say where each is carried out; in two of four bundles the pointer dangles.
Fix: Either add `skeptic` and `implementer` to system-discovery.md's `audience:` and `skeptic` to baseline-measurement.md's, or state in this file what the two procedures require rather than naming them.

## SRE-RM-2 — non-blocking
Claim: The Key principles list restates the four sections immediately above it.
Location: engagements/sre/README.md:47-54 against :19-45
Evidence: Inferred by reading, both sections read whole at 8402c23. Principle 2 restates "The system precedes the spec"; principle 3 restates "The red-gate becomes the baseline-gate" verbatim ("The baseline is the failing test," stated twice in this file, at :31 and :52); principle 4 restates "Ownership becomes guest posture"; principle 5 restates "Ceremony has a floor and an override log." Principle 1 restates operating-model.md:28, which is in all four of this file's bundles. Criterion 6.
Consequence: Every rule in the file is stated twice, in one short document, and one of them is stated a third time in engagements/sre/baseline-measurement.md:12. Criterion 6 exists because a restated rule is where drift starts.
Fix: Cut the Key principles list. Nothing in it is absent from the four sections above.

## SRE-RM-3 — non-blocking
Claim: "Skeptic" is used without saying which of the two documents named Skeptic is meant, in bundles where neither is present.
Location: engagements/sre/README.md:43-45 ("clean-context Skeptic review where one is requested")
Evidence: Verified by running — engagements/skeptic.md (`audience: [skeptic, human]`) is absent from the `cartographer` and `implementer` bundles; roles/skeptic-risk-agent.md is absent from all four of this file's bundles. Both documents are titled Skeptic and hold different authority: the engagement Skeptic is advisory (engagements/skeptic.md:12-14), the Skeptic/Risk Agent is a stage with gate force (roles/skeptic-risk-agent.md:9-11). Criterion 11.
Consequence: A Cartographer or Implementer session reading "clean-context Skeptic review" has no document defining what it would receive or what force the verdict carries.
Fix: Write "the engagement Skeptic" here, and either add `cartographer` and `implementer` to engagements/skeptic.md's `audience:` or state in one line what an engagement Skeptic review is.
