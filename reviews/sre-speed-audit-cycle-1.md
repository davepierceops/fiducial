# Review: engagements/sre/speed-audit.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/speed-audit.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 45 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at 0e07753 (cycle 25), never rubric-reviewed. One of the seven-file `engagements/sre/` set.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/document-metadata-policy.md (the standing verb `agreed`), engagements/cartographer.md, engagements/assistant.md, engagements/skeptic.md, and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether a one-week sizing is right; the six-step play's ordering as a matter of engagement practice.
Findings: 3 — 1 blocking, 2 non-blocking
Prior cycle: none
Dave should inspect: SA-2 — `agreed` is the repo's standing verb with a defined mechanism behind it, and reusing it for a client-side yes is either fine or a real collision; that is a call.

## SA-1 — blocking
Claim: Steps 1 and 2 delegate to two procedures absent from two of this file's four bundles.
Location: engagements/sre/speed-audit.md:17-21 ("the Cartographer maps the pipeline by the system-discovery procedure"; "capture per-stage distributions by the baseline-measurement procedure") and :13-14 ("Composes the other engagement skills")
Evidence: Verified by running — this file lands in the `assistant`, `cartographer`, `skeptic`, and `implementer` bundles. engagements/sre/system-discovery.md is absent from `skeptic` and `implementer`; engagements/sre/baseline-measurement.md is absent from `skeptic`. Criterion 1, criterion 3 — the procedure names are the basenames.
Consequence: This file is the only end-to-end account of the engagement, and in the Skeptic bundle two of its six steps point at nothing. "Composes the other engagement skills" states a dependency on files that are not all there.
Fix: Covered by the `audience:` changes in SRE-SD-2 and SRE-ECP-1.
Related: SRE-SD-2, SRE-ECP-1, SRE-RM-1

## SA-2 — non-blocking
Claim: The file redefines `agreed`, which is the repository's standing verb for a document status with a defined mechanism.
Location: engagements/sre/speed-audit.md:41-43 ("**Agreed** means Dave says yes; the proposal records it and the change package cites it. The acceptance criteria are agreed in the same breath.")
Evidence: Verified by running — policies/document-metadata-policy.md:69-71 defines `agreed` as a frontmatter status meaning "Dave has agreed this document. This is the repo's standing verb; 'approved' is not used," reached only through the review cycle or one of two named lighter paths, and requiring a non-null `last-reviewed`. That policy is in all four bundles this file reaches. The Improvement Proposal is not a governed document and has no frontmatter, so the two senses cannot be reconciled by reading. Criterion 11.
Consequence: A session holding both is told `agreed` means a gated status transition with a recorded artifact, and that it means Dave saying yes in conversation. The second is what an engagement needs; nothing marks it as a different word.
Fix: Say "Dave's go" or "accepted," or state explicitly that an Improvement Proposal is not a governed document and `agreed` here is the ordinary word.

## SA-3 — non-blocking
Claim: The file declares one session kind and assigns work to roles of the other.
Location: engagements/sre/speed-audit.md:9 ("This skill runs in a decision session.") and :4 (`audience: [assistant, cartographer, skeptic, implementer, human]`); step 5 at :26-30
Evidence: Verified by running — engagements/sre/implementer.md:9 and engagements/skeptic.md:11 both state their roles run as execution sessions, and both slugs are in this file's `audience:`. Step 5 assigns the build to the Implementer and the review to the Skeptic. Criterion 7.
Consequence: Two execution-session roles receive a file whose first line says it is not for them, and which contains the only statement of what their step of the play is. Either the declaration is wrong or those two slugs are.
Fix: Declare the file for both session kinds, as engagements/sre/README.md does — the play spans both by construction.
