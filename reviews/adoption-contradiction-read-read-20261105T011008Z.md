# Review: Illuminait adoption candidate — contradiction-read-20261105T011008Z

Verdict: changes-required
Reviewed: /private/tmp/illuminait-adoption-initial-plan/candidate @ plan SHA256 d8425b9dd6cc4df91fb1f43770052dc10d3ae18b6f8a56775d7e98be20aaf1c6; emitted store 95e77f71c771de5a216a2c3f4900c0ff21435eed plus uncommitted adopt skill
Baseline: /private/tmp/illuminait-fiducial-adoption @ 9220705453ecc042eedef5dc0ac0da99a78f62c9
Reviewer: independent adopter contradiction reader (adoption_contradictions); wrote none of candidate or adopter
Date: 2026-11-04
Scope: semantic adoption comparison of both harness layouts; every existing inventoried harness file; emitted root context, agent instructions, skill prose and hook configuration; relevant project decisions and local roles/core; proposed candidate append
Cross-checked: SPEC.md §§3.1, 7; docs/plans/subtraction-plan-20261104.md §5; process/review-artifact.md; initial emission /private/tmp/fiducial-pkg5-initial-stage
Not inspected: adopter Python implementation and package 5 tests (separate reviewer); hook implementations as an enforcement audit; unrelated evaluated codebases; live Claude /context, Codex trust or forge settings; old bundles beyond the clauses needed to establish loader conflicts
Findings: 1 blocking contradiction; 3 observations requiring explicit preservation/scope disposition
The human should inspect: C1 proposed loader replacement and DEC-000280 whole-entry supersession; C2–C4 project exceptions; archival versus removal boundaries

All textual locations below are observed from local files. Behavioral consequences are inferred from simultaneous loading, not live-verified. Static comparison is contract-verified only. No target file, branch, label, issue, PR or remote was changed by this read.

## Quality

Verdict (quality): changes-required

### C1 — blocking
Claim: The proposed append leaves two complete standing instruction sources and two Project Status entrypoints active.
Location: existing CLAUDE.md:3–7 and AGENTS.md:3–7; existing decisions/log.md:139–143 (DEC-000280); staged candidate/CLAUDE.md:3–9 and candidate/AGENTS.md:3–9; staged claude-code/.claude/skills/build/SKILL.md:15–25 and codex/.agents/skills/build/SKILL.md:15–25.
Evidence: Observed both root files are identical seven-line legacy loaders. Candidate preserves them before its managed section. DEC-000280 still mandates that pin. Old .fiducial/v2026.09.29/fiducial-bundle-chief-of-staff.md:117,257 requires directive/fresh-session routing, while staged build uses direct subagents. The old Project Status file remains explicitly selected at root line 7 beside new same-named skills.
Consequence: Inferred: a fresh session is told to load the old bundle as complete before using the new context; contradictory orchestration and retro instructions stay live. An empty mechanical conflicts list does not resolve this semantic conflict.
Fix: Human rules to replace exactly the seven-line legacy preamble in each root with a short project-owned preamble, outside the managed marker: “Standing fiducial context is the managed section below and the matching harness agents, skills and hooks in this repository. Project-specific decisions in decisions/log.md and explicitly invoked roles/cartographer.md and roles/synthesist.md remain in force. .fiducial/v2026.09.29/ is historical reference, not a standing loader. Project Status uses the project-status skill in the active harness.” Do not keep its mandatory old-bundle read or old skill pointer. Prepare those exact replacements and independently reread the fresh candidate before append. Append one new adoption DEC superseding DEC-000280 whole-entry: name the final emitted source revision, active local harness paths, CC BY 4.0/Dave prior-work/advisor carve-out attribution, preservation of all project-specific decisions including DEC-000220, and archival .09.29 status. Preserve .09.29 attribution files. Remove only .fiducial/v2026.09.17/ under the already-told user authorization; no additional removal is implied.

## Skepticism

Verdict (skepticism): ready-with-findings

### C2 — observation
Claim: Experimental project roles retain their older directive/core contract when explicitly invoked; adoption must not imply they were regenerated or migrated.
Location: existing decisions/log.md:49–57 (DEC-000100/110), :134–136 (DEC-000270), roles/cartographer.md:5–9,45–47, roles/synthesist.md:5–9,55–57, roles/fiducial-bundle-core.md:63; staged claude-code/.claude/skills/build/SKILL.md:15–25 and codex/.agents/skills/build/SKILL.md:15–25.
Evidence: Observed no auto-loader of roles/** in the inventoried harness files. Existing DEC-000110 explicitly loads a generated old core beside Cartographer, whose line 63 defines FIRST ACT commit/push. New build dispatches subagents. This is dormant project-specific context, not a second root harness loader once C1 is fixed.
Consequence: Inferred, conditional on invoking these evaluation roles: a broad assertion that all courier behavior was upgraded would be false, and silent core regeneration would displace the approved evaluation contract.
Fix: Record in the adoption DEC: “The experimental Cartographer and Synthesist evaluation roles, their core-loading contract and task-specific project decisions remain unchanged when explicitly invoked; this adoption replaces general harness loading and does not migrate those evaluation artifacts.” Preserve roles/** byte-for-byte and leave their existing DEC entries in force. No role-file edits are proposed. If the human instead wants those roles migrated, that is a separate scoped delta.

### C3 — observation
Claim: The new retro self-landing procedure needs an explicit boundary around Dave's untracked retros.
Location: existing decisions/log.md:109–112 (DEC-000220); staged claude-code/.claude/skills/retro/SKILL.md:67–72 and codex/.agents/skills/retro/SKILL.md:67–72; staged project-status/SKILL.md:26–27,41–43 in both layouts.
Evidence: Observed DEC-000220 reserves Dave's commit timing and excludes untracked retros from stop checks. Staged retro commits its own newly generated path, not every untracked file; staged status explicitly does not commit retros. Therefore no unconditional loaded collision is demonstrated.
Consequence: Inferred ambiguity only: a broad “retro lands itself” adoption summary could be mistaken for permission to sweep Dave's existing untracked files into a commit.
Fix: Preserve DEC-000220 unchanged and state in adoption DEC: “The new retro procedure lands only the retro or synthesis it generates on request; existing human-authored untracked retros remain at Dave's chosen commit timing and are never a stop condition.” Do not commit or remove any existing untracked retro.

## Continuity

Verdict (continuity): ready-with-findings

### C4 — observation
Claim: General software-build skills must not silently repeal the consulting-work scope exception.
Location: existing decisions/log.md:18–21 (DEC-000040); staged claude-code/.claude/skills/build/SKILL.md:13–19 and change-flow/SKILL.md:18–25; equivalent codex/.agents/skills paths and lines.
Evidence: Observed no target SPEC.md found by the repository file sweep. DEC-000040 identifies infrastructure/reliability consulting and requires a PRD only if software is built. New skills use SPEC.md for software implementation. They can coexist when scoped; the mere installed skill is not a new instruction to spec every consulting artifact.
Consequence: Inferred ambiguity only: treating every engagement activity as software implementation would invent an approval precondition absent from the project ruling.
Fix: Preserve DEC-000040 and record in adoption DEC: “The single SPEC.md/build workflow applies when software is built here; this adoption does not require a software spec for the engagement's consulting/evaluation artifacts.” No retrospective conversion of project artifacts is proposed.

## Inventory and preservation evidence

Observed physical recursive sweep excluding .git found only root CLAUDE.md and AGENTS.md in the requested harness inventory. No nested AGENTS.md, AGENTS.override.md, .claude/settings.json, .claude/rules/, .claude/agents/, .claude/skills/, .codex/config.toml, .codex/hooks.json, .codex/agents/*.toml or .agents/skills/ existed in that clone. git ls-files confirmed the same tracked harness inventory. New emitted agent/skill/hook names therefore have no existing harness file collision in this checkout. This does not establish compatibility with unobserved files on Dave's separate clone.

Observed DEC-000030 at decisions/log.md:13–16 explicitly permits directed writes under the private Free-tier branch-protection fallback. Its requirements are force-push denies in every runner permission mode and PR-only main changes. Staged claude-code/.claude/settings.json:29–36 and codex/.codex/hooks.json:17 contain force-push guards; root context requires branch pushes/PRs. Retain DEC-000030. This static read neither proves forge protection exists nor proves every runner mode enforces those guards. Fresh-session loading and hook trust remain live boundaries; do not turn this report into live-enforcement evidence.

Observed candidate plan has no structural conflicts and 62 writes, including ownership metadata; it has no approved root replacements. New adopt skill prose was reread in the later initial-plan stage; its embedded Python remains the separate package reviewer’s scope. Codex and Claude skill bodies match (frontmatter quoting differs); Codex role bodies add scoped-hook notes/procedure paths. No additional contradiction with the inventoried target instructions was found in those additions.

## Proposed human ruling question

“General harness loading means the standing instructions loaded for future ordinary work, separately from explicitly invoked experimental evaluation roles. May the adoption replace both seven-line legacy loaders with the scoped preamble above, supersede DEC-000280 with the final source revision and all surviving attribution/project clauses restated, and record C2–C4's preservation boundaries—keeping roles/**, DEC-000030, DEC-000040 and DEC-000220 in force, keeping .fiducial/v2026.09.29/ as archive, and removing only the already-authorized .fiducial/v2026.09.17/?”

This is a proposed ruling, not a record of human approval. After a go, the exact final preamble/DEC/source revision and any changed emitted material need a fresh staged read; this artifact does not authorize append or remote writes.
