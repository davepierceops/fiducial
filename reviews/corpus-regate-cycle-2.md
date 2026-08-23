# Review: the corpus — Pass 1 re-gate confirmation — cycle 2

Verdict: changes-required
Reviewed: 30 files @ df35ea7 for the confirmation pass (enumerated below), and the 51-file corpus set @ df35ea7 for the five corpus-wide sweeps
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: every file PR #130 changed, excluding `bin/**` and `docs/**` — enumerated from `git diff --name-only 8cdc0b9 287fa78` and listed below — read whole against all eleven criteria of docs/global-context/review-rubric.md @ df35ea7 and against the current foundation: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, all @ df35ea7. Then each of the 47 findings in reviews/corpus-regate-cycle-1.md and its 19 companion artifacts, resolved against the landed text. Then five sweeps re-run corpus-wide over the 51-file set — duplicate rules, contradictions, term collisions, audience values, retired vocabulary — and two re-run over the 30 changed files only, per directive: path references and role boundaries. Bundle membership, audience values, path-shaped tokens, retired vocabulary, and near-duplicate sentences were all extracted mechanically at df35ea7 and, for the deltas, at 8cdc0b9 over the same paths.
Cross-checked: docs/cycles/pass1-regate-fix-20260822T230000.md and docs/cycles/pass1-regate-fix-2-20260822T232000.md in full, for the dispositions each finding's fix was executed under; reviews/corpus-regate-cycle-1.md and all 19 companion artifacts in full; `git diff 8cdc0b9 287fa78` for every file in scope; `bin/aimeta/repo.py` (`role_slugs`, `_is_role_document`), for the discriminator the widened audience rule relies on; `bin/check-frontmatter --all` and `bin/tests/run`; every `reviews/*.md` filename at df35ea7, for cycle numbering and stem derivation.
Not inspected: `bin/` behaviour beyond reading `role_slugs`/`_is_role_document` and running the two commands above — the audience bundler is still unbuilt, and every bundle membership in this artifact was computed from frontmatter directly, not by running it; the two pre-existing `bin/tests` failures (`test_bn10_bundle_base_yields_exactly_itself`, `test_bn10_transitive_body_references_are_followed_in_this_repo`), excluded by directive and confirmed to be the only two failures at df35ea7; `bin/**` and `docs/**`, excluded from the confirmation pass by directive, so the tooling changes fix-2 made are not reviewed here beyond running them; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/, and every reference within them, excluded by directive; the 21 corpus files PR #130 did not change, which were read only as the other side of a sweep row and did not receive a confirmation pass; whether any rule is *correct* as engineering or product judgment — this role judges coherence and safety as LLM context only; the PRD and TRD instances, which are the Spec Reviewer's and do not exist in this repository; whether decisions D1 through D8 were the right calls, which this cycle treats as settled.
Findings: 12 new — 6 blocking, 6 non-blocking — across 11 companion artifacts, plus 2 of the prior cycle's 47 still open (one of them the twelfth companion artifact's only entry) and 1 reopened differently. This artifact carries the seven sweeps (109 rows: 7 duplicate rules, 5 contradictions, 5 term collisions, 17 audience values, 54 path references, 12 retired-vocabulary terms, 9 role boundaries), the closure table, and the confirmation-pass verdicts; per-file findings are in the twelve artifacts named below.
Prior cycle: reviews/corpus-regate-cycle-1.md (reviewed @ 8402c23)
Dave should inspect: OM-1 and CQR-4 together — decision D5 moved the agreement gate for methodology documents and the corpus now states the answer four different ways, in four files that reach the same bundles. Then RA-4, which is the stem convention still failing to derive six paths already in the tree. Then CG-1 and SA-4, the two places decision D3 left a file half-conformed.

---

## Scope — the 30 files in the confirmation pass

`git diff --name-only 8cdc0b9 287fa78` returns 38 paths. Five are under `bin/`, three under `docs/`; both are excluded by directive. The remaining 30:

LEXICON.md · context-sets/spec-and-change-discipline.md · engagements/assistant.md · engagements/cartographer.md · engagements/critic.md · engagements/sre/README.md · engagements/sre/baseline-measurement.md · engagements/sre/engagement-change-package.md · engagements/sre/implementer.md · engagements/sre/override-log-policy.md · engagements/sre/speed-audit.md · engagements/sre/system-discovery.md · engagements/working-with-dave.md · operating-model.md · policies/commit-and-change-control-policy.md · policies/document-metadata-policy.md · policies/project-setup-requirements.md · prose-criteria.md · roles/chief-of-staff.md · roles/context-quality-reviewer.md · roles/skeptic-risk-agent.md · roles/spec-reviewer-agent.md · roles/test-designer-agent.md · roles/writer.md · skills/conversation-retro.md · skills/directive-authoring.md · skills/evidence-review.md · skills/review-artifact.md · skills/spec-review-cycle.md · skills/test-plan-review.md

**Excluded, and named so the exclusion is visible:** bin/aimeta/repo.py · bin/tests/test_check_frontmatter.py · bin/tests/test_repo.py · bin/tests/test_scope.py · docs/cycles/pass1-regate-fix-20260822T230000.md · docs/cycles/pass1-regate-fix-2-20260822T232000.md · docs/global-context/review-rubric.md · docs/history/inventory-20260820.md. The rubric and the retired inventory are excluded by the `docs/**` rule even though both are governed files; the rubric was read in full as this cycle's criterion source, and its two cycle-1 findings are resolved in the closure table below.

## Scope — the 51-file sweep set

The prior cycle's 52, less docs/global-context/inventory.md (now docs/history/inventory-20260820.md, per D7), with engagements/critic.md in place of engagements/skeptic.md. Recomputed mechanically at df35ea7 and confirmed at 51: `bin/check-frontmatter --all` matches 36 files from nine globs, plus `docs/global-context/*.md` (3), `engagements/**/*.md` (11), and prose-criteria.md (1). `bin/check-frontmatter --all` exits 0 with no warnings — the `README.md` unmatched-glob warning the prior cycle recorded is gone, the glob having been removed.

---

## Closure — the prior cycle's 47 findings

44 closed · 2 still open · 1 reopened differently.

| Finding | File | State | The landed text |
| --- | --- | --- | --- |
| LX-1 | LEXICON.md | closed | LEXICON.md:79-95 adds **Claim strength**, **Provenance class**, and **Tier** — "used on two axes, never interchangeably. A **model tier** is frontier, solid general-purpose, or cheap. A **claim tier** is one of the four claim-strength tiers above." Per D6 the ladders stand as distinct axes. |
| INV-1 | inventory.md | closed | `git mv` to docs/history/inventory-20260820.md, per D7. It carries no bundle. |
| INV-2 | inventory.md | closed | Moot per INV-1; the 45 path rows and 34 dead targets left the corpus with the file. |
| INV-3 | inventory.md | closed | Moot per INV-1. The corpus-wide model-name sweep now returns zero occurrences outside `vendors/`. |
| INV-4 | inventory.md | closed | Moot per INV-1. |
| RR-1 | review-rubric.md | closed | docs/global-context/review-rubric.md:13-14 — "A criterion is a test for a stated rule and may name it; criterion 4 does not apply to this file." The exemption RR-1 asked for, stated. |
| RR-2 | review-rubric.md | closed | Rubric:9-11 now reads "Criteria every file in the Context Quality Reviewer's scope, as that role's Scope rule states it"; the role states the scope as one mechanical rule. One home, one citation. |
| SK-1 | skeptic.md | closed | `critic` added to skills/review-artifact.md:4. The `critic` bundle is 24 files and contains the schema. |
| SK-2 | skeptic.md | closed | engagements/critic.md:12-14 and engagements/sre/README.md:39-40 now carry the same statement. See DR-23 for what the duplication costs. |
| WD-1 | working-with-dave.md | closed | `implementer` added to engagements/working-with-dave.md:4; the `implementer` bundle is 24 files and contains it. D1 also reversed the premise: the guardrail is now overridable by Dave only, logged. |
| DMP-1 | document-metadata-policy.md | closed | :90-95 — values are the basename slug of any role document under `roles/` or `engagements/`, plus three reserved. All 17 distinct audience values in the 51-file set resolve; `bin/check-frontmatter --all` exits 0. |
| DMP-2 | document-metadata-policy.md | closed | `README.md` removed from the gate-document class (:138-153) and from the in-scope globs (:24-34). |
| DMP-3 | document-metadata-policy.md | closed | :278-279 — "Bundle membership is declared by the document's `audience` value; no reader selects it." No retired role name survives anywhere in the set. |
| PSR-1 | project-setup-requirements.md | closed | :46 — "The in-scope set is the one the document metadata policy defines." The prose enumeration and the dead root readme are gone. |
| CQR-1 | context-quality-reviewer.md | closed | :14-17, the scope as a rule rather than an enumeration. `writing/` is gone; prose-criteria.md and the global-context documents are named. See CQR-3 for the residue. |
| CQR-2 | context-quality-reviewer.md | closed | Per D5: :32-33 — "The PRD, the TRD, and their acceptance criteria are the Spec Reviewer's. Nothing else is," matched by roles/spec-reviewer-agent.md:33-35. See CQR-4 and OM-1 for what the move left unstated. |
| DA-1 | directive-authoring.md | closed | The mid-delta bullet is deleted; context-sets/spec-and-change-discipline.md:53-55 is the one home; roles/chief-of-staff.md:101 and skills/spec-review-cycle.md:36-38 cite it by title. |
| DA-2 | directive-authoring.md | closed | skills/review-artifact.md:53-54 — "On a rename or a split the cycle number restarts at 1, and `Prior cycle` names the predecessor stem." |
| RA-1 | review-artifact.md | closed | skills/review-artifact.md:50-51 states the disambiguation rule. It is narrower than the practice; that is RA-4, a new finding, not a failure to land this one. |
| RA-2 | review-artifact.md | closed | Same sentence as DA-2. |
| RA-3 | review-artifact.md | closed | The Gap labels paragraph is cut. LEXICON.md:64-77 is the one home; roles/skeptic-risk-agent.md:101 and skills/evidence-review.md:45-46 instruct the labelling without redefining it. |
| SRE-RM-1 | sre/README.md | closed | :27 "system discovery is what produces it" and :33-34 "Baseline measurement is what produces the Measurement Baseline" — the basename references are gone, and the Artifacts list at :49-67 states what each procedure yields. |
| SRE-RM-2 | sre/README.md | closed | The Key principles list is deleted. "Manage the proof, not the code" now appears once in the corpus, at operating-model.md:28. |
| SRE-RM-3 | sre/README.md | closed | :45-47 — "clean-context Critic review where one is requested. A Critic read is advisory; its verdict is input to Dave and gates nothing." Named, and its force stated inline. |
| SRE-BM-1 | sre/baseline-measurement.md | closed | :25-26 cites "the Artifacts list," which lives in engagements/sre/README.md — present in all four engagement bundles. |
| SRE-BM-2 | sre/baseline-measurement.md | closed | The opening restatement is cut; the file opens at "The baseline-gate procedure." Per DR-16 the reversed home is engagements/sre/README.md:31, and the sentence now appears once. |
| SRE-BM-3 | sre/baseline-measurement.md | closed | :33-35 reduced to "An override of this gate names the measurement debt in the change package" — the one clause the override policy does not state. |
| SRE-ECP-1 | sre/engagement-change-package.md | closed | The Measurement Baseline's shape — "per-stage p50 and p95, the total, the date range, the run count, and known confounds" — is in engagements/sre/README.md:54-55, which the `critic` bundle carries. |
| SRE-ECP-2 | sre/engagement-change-package.md | closed | The System Map is defined at engagements/sre/README.md:51-53, in all four engagement bundles. |
| SRE-ECP-3 | sre/engagement-change-package.md | closed | :9-10 — "Produced in an execution session by the Implementer. The Assistant reads it; it does not produce one." Per D4 the audience was not narrowed. |
| SRE-IMP-1 | sre/implementer.md | closed | Per D1 the guardrail is overridable by Dave only and logged; engagements/working-with-dave.md is now in the `implementer` bundle, and engagements/sre/override-log-policy.md:34 adds "Only Dave overrides. The client's humans do not; the agent does not." |
| SRE-IMP-2 | sre/implementer.md | closed | Same as SRE-ECP-2 — the System Map is defined in the README the bundle carries. |
| SRE-OLP-1 | sre/override-log-policy.md | closed | Per D1, the reversal. Exclusions now bounds the overrider rather than the overridable set, and the guardrail is inside it by design. |
| SRE-OLP-2 | sre/override-log-policy.md | closed | :29 — "the engagement review (not a conversation retro)." |
| SA-1 | sre/speed-audit.md | **still open** | :18-21 still reads "by the system-discovery procedure" and "by the baseline-measurement procedure"; neither `audience:` changed, and the fix chosen (lift the artifact definitions into the README) does not reach a procedure reference. Narrowed by the new reader clause. reviews/sre-speed-audit-cycle-2.md. |
| SA-2 | sre/speed-audit.md | closed | :38 — "**Dave's go:** the proposal records it and the change package cites it." The redefinition of `agreed` is gone; four ordinary-word uses remain, recorded as TC-5. |
| SA-3 | sre/speed-audit.md | **reopened differently** | :9-10 names the Implementer and Critic as readers, closing the step-5 half. D3 made the Cartographer an execution-session role in the same pull request, and step 1 assigns it the whole of its work; the reader clause does not name it. Carried as SA-4 in reviews/sre-speed-audit-cycle-2.md. |
| SRE-SD-1 | sre/system-discovery.md | closed | Per D3: :9-10 — "This skill runs in an execution session, executed by the Cartographer," matching engagements/cartographer.md:9. See CG-1 for the body that was not conformed. |
| SRE-SD-2 | sre/system-discovery.md | closed | The System Map and the engagement working area are defined at engagements/sre/README.md:51-61, which every engagement bundle receives; the `audience:` was correctly left alone. |
| WR-2 | writer.md | closed | :17 names the Critic and states what each pass checks — "advisory, reads the piece against the Public Prose Criteria" and "checks it as LLM context, if it will be bundled." See WR-5 for the second half of that sentence. |
| WR-3 | writer.md | closed | :10 — "The Writer runs as a decision session." |
| WR-4 | writer.md | closed | The publication line is cut. Core Standing 2 is the home; prose-criteria.md:19 keeps only the clause Core does not carry. |
| PC-1 | prose-criteria.md | closed | Per D6: `inferred` → **Grounded** at :62, plus :67-68 "This ladder is claim strength — how firmly a sentence may assert — not provenance; provenance is stated per Core." A corpus sweep for `inferred` returns only Core's class and LEXICON's naming of it. |
| PC-2 | prose-criteria.md | closed | :19 reduced to "Dave reads every word of a piece before it publishes" — the one clause Core does not carry, which is exactly what PC-2's fix permitted. |
| PC-3 | prose-criteria.md | **still open** | The file states no session kind, and the conditional cycle 1 attached — that this file say it is read by the Writer role as defined in roles/writer.md — was not met. Narrowed by WR-3 and by `order:`. reviews/prose-criteria-cycle-2.md. |
| PC-4 | prose-criteria.md | closed | All four author-addressed passages rewritten as agent instructions: :25-26, :100-101, :129-133, :144-145. |
| PC-5 | prose-criteria.md | closed | `order: 11` here, `order: 10` on roles/writer.md — the role document before the criteria it points at. |

## Sweep (a) — Duplicate rules

Corpus-wide over the 51-file set. A rule stated in two or more files whose bundles overlap. Re-run mechanically as a 4-gram near-duplicate scan over all 1,026 sentences of the set, then read; boilerplate session-kind declarations and pointer lines ("in the shape the review-artifact skill states") are not rules and are excluded.

| # | Rule | Locations | State |
| --- | --- | --- | --- |
| DR-2r | Reconciliation charges the reviewer gate once over the whole delta, not once per edit | LEXICON.md:31-36 (the term) · policies/commit-and-change-control-policy.md:117-124 (the mechanism) | As proposed. Down from four locations; roles/spec-reviewer-agent.md and skills/spec-review-cycle.md now cite by title. |
| DR-19r | A recommendation is a next step, never a ship call; signal no-ship with `blocking` | roles/skeptic-risk-agent.md:124-126 · skills/evidence-review.md:38-39 | Deliberate. Part 1 consolidated to the role; fix-2 instruction 7 reversed it because skills/evidence-review.md reaches the `reviewer-agent` and `release-manager-agent` bundles, which the role document does not. Verified: the role's coverage is 2 bundles, the skill's is 3. |
| DR-20r | Retros carry no lifecycle metadata | policies/document-metadata-policy.md:36-41 (out of scope, `retros/` now named) · skills/conversation-retro.md:45-47 (the retro header is synthesis metadata) | Resolved as proposed. The exemption moved to the enumerating policy; what remains in the skill is a statement about its own schema, not the exemption. |
| DR-22 | Filename convention `<descriptor>-<timestamp>`, no random strings, hashes, or UUIDs | docs/global-context/core.md:33 · docs/global-context/review-rubric.md:44-46 | Exempted, per the rubric's new line 13. RR-1 closed. |
| DR-23 | An engagement has no release gate; release is the client's concern; do not reason about the client's release timing | engagements/critic.md:12-13 · engagements/sre/README.md:39-40 | **New.** Verbatim in both; both in the 24-file `critic` bundle. Dictated by instruction 12. CR-1. |
| DR-24 | Every claim about state, results, verification, or completeness carries a provenance class | docs/global-context/core.md:22 · LEXICON.md:87-88 | **New.** Both `all-roles`, so both in all fourteen bundles. LX-2. |
| DR-25 | "It changes when the architecture changes, not once per feature" | roles/architect-agent.md:29-30 · specs/trd-template.md:18-19 | **New to the sweep, pre-existing in the tree.** Verbatim; both in the `architect-agent` bundle. Neither file is in this cycle's confirmation-pass scope, so no finding is raised; recorded so the next cycle over either has it. |

**7 rows. Prior cycle: 22. Delta −15.** Sixteen of the prior cycle's rows were consolidated to one home, two (DR-2r, DR-19r) stand as deliberate two-home splits, DR-22 was exempted rather than moved, and three rows are new. Every consolidation was checked for delivery regression — whether the surviving home reaches every bundle the deleted restatement reached. Fifteen of sixteen are clean. The exception is DR-6: "Decomposition requires a closed delta" moved from context-sets/spec-and-change-discipline.md (`all-roles`, 14 bundles) to roles/chief-of-staff.md (1 bundle). No finding is raised — decomposition is that role's act and no other role performs it — but it is the same shape as the regression fix-2 had to reverse for DR-19, and it is recorded here rather than discovered later.

## Sweep (b) — Contradictions

Corpus-wide over the 51-file set. Two files (or two passages of one file) stating incompatible rules.

| # | Statement A | Statement B | Why incompatible |
| --- | --- | --- | --- |
| CN-9 | roles/context-quality-reviewer.md:27-28 — "A document reaches `agreed` only after this role's verdict is `ready`." | policies/document-metadata-policy.md:120-123 (the expedited path "drops the reviewer-gated cycle") and :200-205 (a co-authored document "reaches `agreed` on his sign-off, with no separate reviewer") | Unconditional against two named exceptions. The clause that used to reconcile them lived in roles/spec-reviewer-agent.md and was deleted when D5 moved the gate. Both files are in the `context-quality-reviewer` and `chief-of-staff` bundles. **Open.** CQR-4. |
| CN-10 | operating-model.md:126 — "The same gate covers any canonical document, methodology documents included." | roles/spec-reviewer-agent.md:33-35, skills/spec-review-cycle.md:14-16, roles/context-quality-reviewer.md:32-33 — the Spec Reviewer's gate reaches the PRD, the TRD, and their acceptance criteria "and nothing else" | Direct. D5 was executed in three files and not in the fourth, which is `all-roles` and reaches all fourteen bundles. **Open.** OM-1. |
| CN-11 | engagements/cartographer.md:9-10 — an execution session whose report returns to the Assistant | engagements/cartographer.md:21, :27-29, :30-31 — "Dave asks; you dig; you answer"; "hand that to Dave — he decides"; "you give him the questions worth asking" | Within one file: two session kinds and two recipients for one output. D3 rewrote the declaration and left the body. **Open.** CG-1. |
| CN-12 | engagements/sre/baseline-measurement.md:9-10 — "This skill runs in a decision session, except step 6" | Its `audience:` delivers it to `cartographer` and `implementer`, both execution-session roles at df35ea7 | D4 requires the file to state who runs it and who reads it; this is the one file in the pack where that was not applied, and D3 widened the mismatch from one role to two. **Open.** SRE-BM-4. |
| CN-13 | engagements/sre/speed-audit.md:9-10 — "The Implementer and Critic read it for their step-5 assignments" | engagements/cartographer.md:9 — an execution-session role, in this file's `audience:`, assigned the whole of step 1 | The reader clause enumerates two of the three execution roles. Written under instruction 8, before instruction 7 moved the third. **Open.** SA-4. |

**5 rows, all new and all open. Prior cycle: 8 rows, of which 6 were open (CN-1 through CN-6) and 2 were recorded as reconciled (CN-7, CN-8). Delta −3 rows, −1 open.** CN-1 closed by D3, CN-2 by the widened audience rule, CN-3 by D8, CN-4 and CN-5 by D4, CN-6 by D1. CN-7 remains not-open — the narrowed Spec Reviewer gate no longer reaches the documents the doc-only path covers. CN-8 remains not-open, and the shared name behind it is gone with D2.

## Sweep (c) — Term collisions

Corpus-wide over the 51-file set. A term used with a meaning LEXICON does not give it, a term LEXICON defines that a file uses differently, or a term two files use for different things.

| # | Term | Sense A | Sense B | LEXICON at df35ea7 |
| --- | --- | --- | --- | --- |
| TC-5 | **agreed** | policies/document-metadata-policy.md:72-73 — a frontmatter status, "the repo's standing verb," reached only through a gated path and requiring a non-null `last-reviewed` | engagements/sre/implementer.md:9 and :17, engagement-change-package.md:17, speed-audit.md:39 — the ordinary word, of an Improvement Proposal and its acceptance criteria, neither of which is a governed document | Not defined. **Still open, relocated.** SA-2 removed the redefinition; four uses remain, and the metadata policy is `all-roles` so it reaches all four engagement bundles. |
| TC-6 | **boundary** | policies/verification-boundary-policy.md — the point where evidence stops | boundaries/human-review-boundary.md — a governed document class and a scope limit on human diff-reading; a third sense at roles/chief-of-staff.md:77 | Defines the evidence classes and release impact labels, not "boundary." **Unchanged.** |
| TC-7 | **claim / claimed** | docs/global-context/core.md:21-23 — an assertion about state, results, verification, or completeness | LEXICON.md:38-39 — "**Claimed** — of a spec document: appearing in an open delta's diff" | **Improved.** LEXICON.md:79-95 now names the two claim axes explicitly, and the spec sense is marked "of a spec document." The two remain one word on three axes in one file. |
| TC-8 | **"needs Dave decision"** | roles/release-manager-agent.md:57 — a valid ship recommendation | LEXICON.md:69-70 — "A gap awaiting Dave's judgment is blocking; 'requires Dave decision' is not a label" | **Unchanged.** Different slots; near-identical phrasing asserted valid in one file and invalid in the other, both in the `release-manager-agent` bundle. Neither file is in this cycle's confirmation-pass scope. |
| TC-10 | **red-gate**, **change package**, **meaningful change**, **consequential class**, **human-gate**, **gate document** | Load-bearing terms used across 6-14 files each | Each defined once, in operating-model.md, policies/commit-and-change-control-policy.md, or policies/document-metadata-policy.md | **Unchanged.** All the defining files carry `all-roles`, so the definitions reach every bundle; recorded because LEXICON's stated job is "terms with a fixed meaning across this methodology." |

**5 rows. Prior cycle: 10. Delta −5.** TC-1 and TC-2 closed by D6 and the Claim axes section; TC-3 closed by D2; TC-4 closed by the "engagement review (not a conversation retro)" edit; TC-9 closed by the README's Artifacts list, which puts every engagement term in every engagement bundle.

## Sweep (d) — Audience values

Every distinct `audience:` value in the 51-file set, with its file count, computed mechanically at df35ea7. No file lacks `audience:`. Every value is legal under the rule as it now reads: the basename slug of a role document under `roles/` or `engagements/`, plus three reserved values.

| Value | Files | Legal under the current rule? | Change since the prior cycle |
| --- | --- | --- | --- |
| `human` | 51 | reserved | −1 (inventory.md left the set) |
| `all-roles` | 17 | reserved | unchanged |
| `chief-of-staff` | 13 | yes — `roles/chief-of-staff.md` | −1 (inventory.md) |
| `assistant` | 9 | yes — `engagements/assistant.md` (`# Role:`) | unchanged |
| `critic` | 7 | yes — `engagements/critic.md` (`# Role:`) | replaces `skeptic` (6); +1 from skills/review-artifact.md, closing SK-1 |
| `cartographer` | 7 | yes — `engagements/cartographer.md` (`# Role:`) | unchanged |
| `implementer` | 7 | yes — `engagements/sre/implementer.md` (`# Role:`) | +1 from engagements/working-with-dave.md, closing WD-1 |
| `reviewer-agent` | 5 | yes | unchanged |
| `spec-reviewer-agent` | 5 | yes | unchanged |
| `context-quality-reviewer` | 4 | yes | unchanged |
| `release-manager-agent` | 4 | yes | unchanged |
| `skeptic-risk-agent` | 4 | yes | unchanged |
| `architect-agent` | 3 | yes | unchanged |
| `writer` | 2 | yes | unchanged |
| `coder-agent` | 1 | yes | unchanged. Used by one file; `all-roles` supplies the rest of the bundle. |
| `test-designer-agent` | 1 | yes | unchanged. Same. |
| `all-decision-roles` | 1 | reserved, and now reserved *in policy* — :92-95 names it and defines what it selects | unchanged in count. That it still selects nothing until the bundler lands is known and excluded by directive. |

**17 rows. Prior cycle: 17. Delta 0 in count; three rows changed value or membership.** The prior cycle's CN-2 — eleven files carrying values the policy declared illegal — is closed: the rule now admits engagement role slugs, `bin/aimeta/repo.py:role_slugs` was conformed to it, and `bin/check-frontmatter --all` exits 0. RS-1's second half, the `all-decision-roles` delivery consequence, is unchanged and excluded. Its first half is unchanged: `all-roles` (17 files) still expands to every bundle including `writer` and the four engagement bundles, so the `writer` bundle is 19 files of which 17 are engineering governance.

## Sweep (e) — Path-shaped references

Re-run over the 30 changed files only, per directive, and re-run over the same 30 paths at 8cdc0b9 for the delta. Every backticked token containing a directory separator or a file extension, extracted mechanically and resolved against the tree at df35ea7.

**54 distinct tokens. The same extraction over the same 30 files at 8cdc0b9: 50. Delta +4.** One removal, five additions; no other row changed.

| Change | Token | Location | Reading |
| --- | --- | --- | --- |
| removed | `README.md` | was policies/document-metadata-policy.md:34 and :152 | DMP-2 closed. The last dead target outside the retired inventory, other than `bin/state`. |
| added | `docs/global-context/*.md` | roles/context-quality-reviewer.md:15 | Introduced by instruction 9. Criterion 3. CQR-3. |
| added | `engagements/**/*.md` | roles/context-quality-reviewer.md:15 | Same. |
| added | `prose-criteria.md` | roles/context-quality-reviewer.md:15 | Same, and the one of the three a reader inside a bundle cannot resolve — prose-criteria.md is in the `writer` bundle only. CQR-3. |
| added | `engagements/` | policies/document-metadata-policy.md:91 | Introduced by instruction 6. In a policy *about* paths, which the prior cycle accepted as structural and did not re-open; recorded, not flagged. |
| added | `engagements/sre/` | policies/document-metadata-policy.md:92 | Same. |

The three clusters the prior cycle accepted as structural rather than incidental are unchanged and are not re-opened: policies/document-metadata-policy.md (a policy about paths, 30 rows), roles/chief-of-staff.md (a read-sequence over named artifacts, 7 rows, including `bin/state`, stated honestly as not yet existing), and — outside this cycle's scope — vendors/claude-code/environment-config.md. **Not captured by this sweep:** file-shaped references that are not backticked. Two survive in the changed set and are recorded as SA-1: "the system-discovery procedure" and "the baseline-measurement procedure" at engagements/sre/speed-audit.md:18-21. The identical defect was removed from engagements/sre/README.md by the same pull request.

## Sweep (f) — Retired vocabulary

Corpus-wide over the 51-file set. Every term LEXICON retires, every retired role name, and vendor and model names outside `vendors/`. Extracted mechanically at df35ea7.

| # | Term | Live occurrences outside its own tombstone | Verdict |
| --- | --- | --- | --- |
| RV-1 | **dispatch** | none | Clean. Prior cycle: 8 lines, all in inventory.md. |
| RV-2 | **sync block** | none | Clean. Prior cycle: 3 lines, all in inventory.md. |
| RV-3 | **track** (the retired directive sense) | none | Clean. The three surviving hits are LEXICON's tombstone and carve-out, policies/source-of-truth-policy.md:25 ("track and organize work"), and docs/global-context/review-rubric.md:41-42 ("Track does not appear") — all the carved-out ordinary sense or the retirement itself. |
| RV-4 | **prompt** | none | Clean. Two hits: policies/commit-and-change-control-policy.md:95 ("skip prompting" — the carved-out approval sense) and docs/global-context/core.md:45 (the instruction not to use it). |
| RV-5 | **editor** (retired role) | none | Clean. Prior cycle: 16 lines in inventory.md. |
| RV-6 | **section-writer** (retired role) | none | Clean. |
| RV-7 | **instruction-reviewer** (retired role) | none | Clean. |
| RV-8 | **orchestrator** (retired role) | none | **Clean — closed.** policies/document-metadata-policy.md:278-279 replaced the one live occurrence. This was the prior cycle's only live retired-role defect. |
| RV-9 | **skeptic** (the engagement role, retired as a name by D2) | none | Clean. All fourteen occurrences are the Skeptic/Risk Agent, which keeps its name per D2 — role heading, audience slug, and prose references in operating-model.md, boundaries/human-review-boundary.md, policies/verification-boundary-policy.md, context-sets/spec-and-change-discipline.md, roles/spec-reviewer-agent.md, roles/reviewer-agent.md, and three skills' audience lists. |
| RV-10 | Model names — Opus, Sonnet, Haiku, Claude, GPT, Gemini | none outside `vendors/` | **Clean — closed.** The prior cycle's one occurrence (inventory.md:86, "Opus / Sonnet / Haiku by work class") left the corpus with the file. The four surviving hits are all in vendors/claude-code/environment-config.md, which carries `audience: [human]`. |
| RV-11 | Vendor and venue names outside `vendors/` | 7: operating-model.md:35 and policies/source-of-truth-policy.md:24 ("currently GitHub Issues"); operating-model.md:161 ("e.g. OpenFeature"); engagements/sre/implementer.md:10, system-discovery.md:16, working-with-dave.md:21 ("Terraform or equivalent"); prose-criteria.md:132 ("LinkedIn is the interim venue") | All hedged and deliberate. Criterion 8 restricts *model* selection to tiers and does not reach these. **Recorded, not flagged.** Six of the seven are the prior cycle's six; the seventh is a wider regex catching a venue name the prior cycle's did not, not a new occurrence — prose-criteria.md:132 was present at 8402c23. |
| RV-12 | `vendors/**` | "Claude Code" throughout | In `vendors/`, by design; both files carry `audience: [human]` and enter no bundle. Clean. |

**12 rows. Prior cycle: 12. Delta 0 in rows; live defects 1 → 0.** RV-8 was the prior cycle's one live defect and is closed. Six rows moved from "all in inventory.md" to "none" when that file became history.

## Sweep (g) — Role boundaries

Re-run over the 30 changed files only, per directive: the role and skill documents among them, against the full role set.

| # | Boundary | Role A | Role B | State at df35ea7 |
| --- | --- | --- | --- | --- |
| BD-1 | Gating a governed methodology document | roles/context-quality-reviewer.md — "Nothing else is" | roles/spec-reviewer-agent.md — the PRD, TRD, ACs "and nothing else" | **Closed** by D5. Both role documents and skills/spec-review-cycle.md state the same split, in the same words. |
| BD-2 | "A Critic" for a finished piece of prose | roles/skeptic-risk-agent.md (gate force) | engagements/critic.md (advisory) | **Closed** by D2 and by roles/writer.md:17, which names the Critic and states what its read checks. roles/skeptic-risk-agent.md:9-10 names the other role and its force. |
| BD-3 | Assessing state and proposing the next step | roles/chief-of-staff.md:13-24 | engagements/assistant.md | **Not open** — no bundle contains both; domains disjoint. Unchanged. |
| BD-4 | Building the change | roles/coder-agent.md | engagements/sre/implementer.md | **Not open** — disjoint bundles, different upstream artifact. Unchanged. |
| BD-5 | Who may override a procedural step | engagements/sre/override-log-policy.md:13-14 and :34 | engagements/working-with-dave.md:33-37 | **Closed** by D1. The guardrail is overridable by Dave only and logged; Exclusions bounds the overrider — "Only Dave overrides. The client's humans do not; the agent does not." The prior cycle's largest finding. |
| BD-6 | Reviewing the Implementer's own diff | engagements/sre/implementer.md:37-39 | engagements/critic.md | **Closed.** "the diff is reviewed by the client's pull-request gate. A Critic read happens only when Dave requests one; do not request it and do not review your own diff." Who reviews, who requests, and what happens when nobody does are all stated. |
| BD-7 | Proposing an improvement | engagements/sre/speed-audit.md:34-36 | engagements/cartographer.md:27-29 | **Closed, and still well stated in both directions.** |
| BD-8 | Emitting a ship recommendation | roles/skeptic-risk-agent.md:124-126 | roles/release-manager-agent.md | **Closed.** DR-19's two homes are deliberate; see sweep (a). |
| BD-9 | Who gates a methodology document, and what `agreed` requires | operating-model.md:126 (the Spec Reviewer, for any canonical document) | roles/spec-reviewer-agent.md / skills/spec-review-cycle.md / roles/context-quality-reviewer.md (the Context Quality Reviewer, for everything but the spec) — and policies/document-metadata-policy.md (two paths with no reviewer at all) | **New, and open.** Four files, three answers, all reaching the same bundles. OM-1, CQR-4. |

**9 rows. Prior cycle: 8. Delta +1.** Three of the prior cycle's rows were open (BD-1, BD-2, BD-5, BD-6 — four); all four are closed. One row is new and open.

## Confirmation pass — one line per file

30 files. 18 clean, 12 with findings. A clean line means the file was read whole against all eleven criteria at df35ea7 and nothing in it fails at the current foundation; cross-file matters are in the sweeps above and are not counted against the file here.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| operating-model.md | changes-required | 1 blocking | reviews/operating-model-cycle-6.md |
| roles/context-quality-reviewer.md | changes-required | 1 blocking, 1 non-blocking | reviews/context-quality-reviewer-cycle-3.md |
| engagements/cartographer.md | changes-required | 1 blocking | reviews/cartographer-cycle-2.md |
| skills/review-artifact.md | changes-required | 1 blocking | reviews/review-artifact-cycle-2.md |
| engagements/sre/baseline-measurement.md | changes-required | 1 blocking | reviews/sre-baseline-measurement-cycle-2.md |
| engagements/sre/speed-audit.md | changes-required | 2 blocking | reviews/sre-speed-audit-cycle-2.md |
| LEXICON.md | ready-with-findings | 1 non-blocking | reviews/LEXICON-cycle-14.md |
| policies/document-metadata-policy.md | ready-with-findings | 1 non-blocking | reviews/document-metadata-policy-cycle-15.md |
| roles/writer.md | ready-with-findings | 1 non-blocking | reviews/writer-cycle-2.md |
| engagements/working-with-dave.md | ready-with-findings | 1 non-blocking | reviews/working-with-dave-cycle-4.md |
| engagements/critic.md | ready-with-findings | 1 non-blocking | reviews/critic-cycle-1.md |
| prose-criteria.md | ready-with-findings | 1 non-blocking | reviews/prose-criteria-cycle-2.md |
| context-sets/spec-and-change-discipline.md | ready | none | — |
| engagements/assistant.md | ready | none | — |
| engagements/sre/README.md | ready | none | — |
| engagements/sre/engagement-change-package.md | ready | none | — |
| engagements/sre/implementer.md | ready | none | — |
| engagements/sre/override-log-policy.md | ready | none | — |
| engagements/sre/system-discovery.md | ready | none | — |
| policies/commit-and-change-control-policy.md | ready | none | — |
| policies/project-setup-requirements.md | ready | none | — |
| roles/chief-of-staff.md | ready | none | — |
| roles/skeptic-risk-agent.md | ready | none | — |
| roles/spec-reviewer-agent.md | ready | none | — |
| roles/test-designer-agent.md | ready | none | — |
| skills/conversation-retro.md | ready | none | — |
| skills/directive-authoring.md | ready | none | — |
| skills/evidence-review.md | ready | none | — |
| skills/spec-review-cycle.md | ready | none | — |
| skills/test-plan-review.md | ready | none | — |

---

## The single largest remaining problem

**The corpus now answers "who gates a methodology document, and what does `agreed` require" in four different places, three different ways, and all four reach the same bundles.** operating-model.md:126 — `all-roles`, in all fourteen bundles — still says the Spec Reviewer's hard gate "covers any canonical document, methodology documents included," which is the rule D5 reversed. roles/spec-reviewer-agent.md, skills/spec-review-cycle.md, and roles/context-quality-reviewer.md all say the opposite. roles/context-quality-reviewer.md then adds that no document reaches `agreed` without its `ready` verdict, and policies/document-metadata-policy.md — also `all-roles` — describes two paths to `agreed` with no reviewer at all, whose reconciling clause was deleted from roles/spec-reviewer-agent.md when the gate moved and was never given to the role that inherited it. No single-file cycle would find this: each of the four files is internally consistent, and D5 was executed exactly where the directive named. It is the routing decision for every remaining Pass 1 cycle, and it is two sentences of work.

## Departures from the directive

One thing could not be executed as written, and one instruction resolved differently than its wording anticipated.

1. **The sweep set is 51 files, not 52.** The directive says to re-run the sweeps "over the same 52-file set the prior cycle enumerated (less docs/global-context/inventory.md, now history; plus engagements/critic.md in place of engagements/skeptic.md)." Those two operations are a removal and a substitution, so the set is 51. Recomputed mechanically at df35ea7 and confirmed: 36 frontmatter-matched + 3 under `docs/global-context/` + 11 under `engagements/` + prose-criteria.md. Nothing was dropped that the directive intended to keep.

2. **The path-reference delta is stated against the same 30 files, not against the prior cycle's corpus total.** The directive re-runs this sweep over the changed files only, while the prior cycle's 101 rows were corpus-wide and 45 of them came from a file that is now history. A delta against 101 would be meaningless. The same extractor was therefore run over the same 30 paths at 8cdc0b9 — where `engagements/critic.md` reads as `engagements/skeptic.md` — giving 50 rows before and 54 after. That is the honest comparison and it is the one stated in sweep (e).

Also noted, and not acted on: `bin/tests/run` at df35ea7 reports exactly the two pre-existing `test_bn10` failures the directive excludes, and no others; `bin/check-frontmatter --all` exits 0 reporting 36 files matched from 9 globs. Both are recorded as evidence that fix-2's tooling changes hold at this SHA, not as a review of `bin/`, which is out of scope.

No document was edited. No status was flipped. No finding was resolved.
