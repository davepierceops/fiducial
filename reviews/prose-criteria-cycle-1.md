# Review: prose-criteria.md — cycle 1

Verdict: changes-required
Reviewed: prose-criteria.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 150 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — the file was moved to the repository root and edited by directive at eea66dd (cycle 26) and has never been rubric-reviewed at any path.
Cross-checked: docs/global-context/core.md (Standing 2; Evidence 5-7), docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md, docs/global-context/inventory.md (rows C3, C6 and the 2026-08-20 parked resolution), roles/writer.md, policies/document-metadata-policy.md — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether the criteria produce good prose — that is Dave's voice and Dave's call, and this role does not judge it; the archived writing pipeline under docs/history/writing/; whether `davepierceops/fiducial` is the right public repository to cite.
Findings: 5 — 2 blocking, 3 non-blocking
Prior cycle: none
Dave should inspect: PC-1. The resolution was already decided on 2026-08-20 and recorded; it needs re-issuing or reversing, not re-deciding from scratch.

## PC-0 — criterion 10, answered first
The file lands in the `writer` bundle (19 files at 8402c23) and is the sole source of every public-prose rule in the corpus — voice, register, the many-languages constraint, naming and attribution, discoverability, disclosure, the AI prose-smell tell list. Nothing else in the bundle states any of it. It earns its place, and cycle 26's decision that it is the writing pipeline's yield is borne out. The findings below are repairs.

## PC-1 — blocking
Claim: The Claims taxonomy is a second four-item evidence ladder in a bundle that already carries Core's, and it reuses `inferred` with a different boundary.
Location: prose-criteria.md:53-67 (Claims taxonomy: relayed / demonstrated / inferred / opinion) against docs/global-context/core.md:22 (Evidence 6: observed / inferred / told / unknown)
Evidence: Verified by running — docs/global-context/core.md (`audience: [all-roles, human]`) and this file are both in the 19-file `writer` bundle, so one session holds both. Core defines `inferred` as "you reasoned to it"; this file defines it as "grounded in experience, observation, or data below the bar for proof," which admits observation Core would label *observed*. `relayed` covers what Core calls *told*; `demonstrated` and `opinion` have no Core counterpart. docs/global-context/inventory.md:164 records the disposition Dave reached on 2026-08-20 — "C3 — core keeps the single provenance ladder... Prose ladder is provenance under other names → `prose-criteria.md` adopts the core's" — and inventory.md:176 lists it as a follow-up. It was never carried out. Criterion 4, criterion 11.
Consequence: Core rule 6 says an assertion's class must be stated and that an unlabelled one is treated as *unknown*. A Writer session holding two ladders that share a word must decide by inference which governs a sentence, and the wrong choice is exactly the tier-blurring this file calls a defect at :66-67.
Fix: Execute the recorded decision — adopt Core's four classes and drop this ladder — or, if the prose ladder is genuinely a different axis, say so here in one sentence and rename `inferred` so the collision is gone.
Related: LX-1

## PC-2 — blocking
Claim: The Trust model section restates Core's publication rule, which roles/writer.md also restates in the same bundle.
Location: prose-criteria.md:19-22 ("Dave reviews every word before publication. Agents draft under direction; nothing publishes on agent judgment.") against docs/global-context/core.md:14 (Standing 2) and roles/writer.md:14
Evidence: Verified by running — all three files are in the 19-file `writer` bundle. Core Standing 2 states "Agreement, release, prioritization, and publication are his." Criterion 4.
Consequence: One rule, three homes, one bundle. Criterion 4 exists because a restated rule drifts; the drift is already visible — Core says publication is Dave's decision, this file says Dave reviews every word, and those are not the same claim.
Fix: Cut the section. If "every word, not merely the decision to publish" is a rule Core does not carry, state that one clause and nothing else.
Related: WR-4

## PC-3 — non-blocking
Claim: The file never states its session kind.
Location: prose-criteria.md:7-16 — the opening, where the Scope section stands in for it.
Evidence: Verified by running — the file declares its subject-matter scope but no session kind, and the corpus convention is that every governed file states one (docs/global-context/core.md:9 "every agent session"; operating-model.md:9 "both session kinds"; roles/*.md uniformly). roles/writer.md, the other file in its bundle pair, also omits it, so the pair as a whole is silent. Criterion 7.
Consequence: Whether docs/global-context/decision-layer.md reaches a Writer session is unanswered by either of the two files that define the role, and the decision layer's register rules would materially change how a Writer talks to Dave.
Fix: Resolve with WR-3; one declaration in roles/writer.md covers both if this file states that it is read by the Writer role as defined there.
Related: WR-3

## PC-4 — non-blocking
Claim: Several entries are instructions to the person maintaining the criteria, not to the agent reading them.
Location: prose-criteria.md:26-28 ("Revisit the register when that shift happens"), :112-114 ("Length and structure are per-piece decisions, not criteria — revisit only if problems recur"), :141-142 ("The tell list is open; add tells as they are noticed"), :131-134 (Venue and portability, "Once the site exists it is canonical")
Evidence: Inferred by reading, each entry read in place at 8402c23. Criterion 5 ("Agent instruction, not authoring principle") and criterion 6 ("Instructions, not rationale"). None of the four is executable by a drafting session: the agent cannot revisit the register, decide that problems recurred, or stand up a site.
Consequence: Roughly a tenth of the file is addressed past the reader. The tell-list entry is the sharpest case — an agent told the list is open may reasonably add to it mid-draft, which is a criteria edit made on agent judgment.
Fix: Move the maintenance instructions out, or rewrite each as the rule it implies — "propose a criteria line when a draft shows a tell the list does not name" is an agent instruction; "add tells as they are noticed" is not.

## PC-5 — non-blocking
Claim: The file carries no `order:` and its position relative to roles/writer.md in the bundle is left to the bundler.
Location: prose-criteria.md:1-5 (frontmatter)
Evidence: Verified by running — of the 19 files in the `writer` bundle, eight carry `order:` (core 0, decision-layer 1, LEXICON 2, operating-model 3, the three context sets 4-6, working-with-dave 10) and this file and roles/writer.md carry none. roles/writer.md:9 says the criteria are "in this bundle" and instructs the Writer to "read them on every invocation," which is a statement about position. Criterion 2: "the file carries `audience:` ... and `order:` where its position in a bundle matters."
Consequence: A role document that tells the reader to read another file in the bundle depends on that file being present and findable; without `order:` the sequence is whatever the unbuilt bundler happens to emit.
Fix: Give both files an `order:` — the role document before the criteria it points at.
