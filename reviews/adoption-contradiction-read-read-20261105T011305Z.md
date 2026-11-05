# Review: Illuminait adoption candidate — follow-up-read-20261105T011305Z

Verdict: ready-with-findings
Reviewed: /private/tmp/illuminait-adoption-reviewed-plan/candidate @ plan SHA256 8ac08d165cc00b489eea9d1c6a22e743b6a0962a796af7d8493e07edb449f2ab; source bb2ebcb4ea140deb40d7148d7dbffcae56806fe2
Baseline: /private/tmp/illuminait-adoption-initial-plan/candidate @ plan SHA256 d8425b9dd6cc4df91fb1f43770052dc10d3ae18b6f8a56775d7e98be20aaf1c6
Reviewer: independent adopter contradiction reader (adoption_contradictions)
Date: 2026-11-04
Scope: diff-only follow-up to reviews/adoption-contradiction-read-read-20261105T011008Z.md; exact root loader replacements, changed source headers, and proposed adoption DEC dispositions C1–C4
Cross-checked: /private/tmp/illuminait-adoption-proposed-decision.md @ SHA256 628c865a83476ab60d93eaaeacc04eb98373e5804eee971593b45e6e07f777b1; target 9220705453ecc042eedef5dc0ac0da99a78f62c9; original removal scope (.09.17 only)
Not inspected: adopter Python hardening and ownership hash updates (separate package review); unchanged instructions already covered by initial read; live harness loading, hook trust or forge enforcement
Findings: no remaining blocking semantic collision in this candidate if proposed decision is approved and appended; 4 observations recording proposed dispositions and residual obligations
The human should inspect: both exact loader replacements and proposed DEC-000440 line 5, including the unchanged project exceptions; no human approval is recorded by this review

Observed: candidate file comparison found only root replacements/source-header changes, adopt skill changes in both layouts, and ownership metadata changes; no file removals. The root replacements match the initial read's C1 remedy. All other emitted context, agents, skills and hook configurations are byte-identical to the previous candidate apart from the excluded adopt/ownership changes. Target git status remains clean. Static comparison is contract-verified; effects on session behavior are inferred. This read changed no target or remote.

## Quality

Verdict (quality): ready-with-findings

### C1 — observation
Claim: The staged root replacement resolves the demonstrated duplicate standing loader, subject to human approval and append of the matching decision.
Location: original CLAUDE.md:3–7 and AGENTS.md:3–7; refreshed candidate/CLAUDE.md:3–5 and candidate/AGENTS.md:3–5; proposed adoption decision:5,7.
Evidence: Observed the seven-line mandatory .09.29 loader and old Project Status pointer are replaced in both roots by the scoped preamble, before the managed marker; headers name bb2ebcb4ea140deb40d7148d7dbffcae56806fe2. Proposed DEC-000440 supersedes DEC-000280 whole-entry and restates prior-work, CC BY 4.0, advisor carve-out and surviving project clauses.
Consequence: Inferred: after installation, roots no longer order loading of the old complete bundle before the new context. Without the proposed DEC append, the old active pin would remain contradictory in the decision log.
Fix: Human explicitly rules on C1; preserve the reviewed replacements, append the approved DEC with its actual gate/report references, retain .09.29 archival material/attribution, and remove only the already-authorized .09.17. The candidate plan does not itself append the DEC or perform archival removals; these remain bounded adoption-PR obligations. No installation or human approval has occurred.

## Skepticism

Verdict (skepticism): ready-with-findings

### C2 — observation
Claim: Proposed decision preserves explicitly invoked experimental evaluation role/core contracts without claiming migration.
Location: original roles/cartographer.md:5–9, roles/synthesist.md:5–9, roles/fiducial-bundle-core.md:63 and decisions/log.md:49–57,134–136; refreshed candidate/CLAUDE.md:3 and candidate/AGENTS.md:3; proposed adoption decision:5.
Evidence: Observed proposed DEC says experimental roles, core-loading contract and task-specific decisions remain unchanged when explicitly invoked and adoption does not migrate evaluation artifacts. Roots identify those roles as explicitly invoked project context.
Consequence: Inferred: old evaluation-specific directives remain scoped to those roles, rather than contradicting general root loading. Their behavior has not been upgraded by this adoption.
Fix: Human explicitly rules on C2; retain that clause and preserve roles/** byte-for-byte. Do not assert retirement of the experimental roles' old core/directive behavior; any future migration is separate work.

### C3 — observation
Claim: Proposed decision preserves Dave's untracked-retro commit timing while limiting new self-landing to its own requested output.
Location: original decisions/log.md:109–112; unchanged staged claude-code/.claude/skills/retro/SKILL.md:67–72 and codex/.agents/skills/retro/SKILL.md:67–72; proposed adoption decision:5.
Evidence: Observed proposed DEC explicitly preserves DEC-000220, human-authored untracked retros and their non-stop-condition status, then limits the new procedure to its own requested retro or synthesis.
Consequence: Inferred: installing the retro skill does not authorize committing Dave's other untracked retros or treating them as a failed precondition.
Fix: Human explicitly rules on C3; retain the clause and leave existing human-authored untracked retros untouched. New self-landing is not a blanket sweep.

## Continuity

Verdict (continuity): ready-with-findings

### C4 — observation
Claim: Proposed decision preserves consulting/evaluation scope and confines software SPEC/build workflow to software built here.
Location: original decisions/log.md:18–21; unchanged staged claude-code/.claude/skills/build/SKILL.md:13–19 and codex/.agents/skills/build/SKILL.md:13–19; proposed adoption decision:5.
Evidence: Observed proposed DEC explicitly retains DEC-000040's consulting/evaluation scope and says the single SPEC.md/build workflow applies when software is built. It also retains DEC-000030's private Free fallback.
Consequence: Inferred: adoption creates no new software-spec requirement for existing consulting/evaluation artifacts and does not manufacture forge branch protection.
Fix: Human explicitly rules on C4; retain those project exceptions and avoid retrospective artifact conversion. Live Claude /context and Codex hook-trust claims stay unverified as proposed DEC line 6 states.

## Concrete gate recommendation

The refreshed candidate plus proposed DEC is ready for the human's C1–C4 ruling. Approving this package would approve the exact replacement of both legacy root loaders; preservation of project roles/core, DEC-000030, DEC-000040 and DEC-000220; whole-entry supersession of DEC-000280 with surviving clauses restated; .09.29 archival retention; and only .09.17 removal under prior authorization. This review is evidence for that ruling, not the ruling itself. Keep the approved decision/report in the adoption PR and record the actual gate result only after received.

Proposed decision snapshot (unapproved):

## Proposed adoption decision (not yet approved)

## DEC-000440 — Adopt emitted Fiducial harness context
Date: 2026-11-04
Decision: Adopt Fiducial from source bb2ebcb4ea140deb40d7148d7dbffcae56806fe2 through managed sections in CLAUDE.md and AGENTS.md and the generated .claude/, .codex/ and .agents/ trees. These replace the mandatory v2026.09.29 bundle loaders and old Project Status pointer; .fiducial/v2026.09.29/ remains historical reference and only .fiducial/v2026.09.17/ is removed. Fiducial remains Dave Pierce's prior work, licensed CC BY 4.0 and carved out of the Illuminait advisor agreement; retained vendored material preserves that attribution. All project-specific decisions remain in force: the private GitHub Free fallback of DEC-000030; DEC-000040's consulting/evaluation scope, with the single SPEC.md/build workflow applying when software is built; and DEC-000220's human-authored untracked retros, committed only when Dave chooses and never a stop condition. The new retro procedure lands only its own requested retro or synthesis. The experimental Cartographer and Synthesist roles, their core-loading contract and task-specific decisions remain unchanged when explicitly invoked; this adoption replaces general harness loading and does not migrate those evaluation artifacts.
Context: The first real adoption run of Fiducial subtraction package 5 stages both harnesses and independently compares them against existing instructions. The proposed dispositions replace the conflicting root loaders and preserve project exceptions. Verification is contract-verified; the human's fresh Claude Code /context check and Codex project hook trust remain unverified. The human merges the adoption PR; the gate ruling and report pointer will be recorded only after they exist.
Supersedes: DEC-000280

