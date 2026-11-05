# Skill context extraction — change package and execution evidence

Intent: reduce standing context by moving the agreed command/execution-block procedure and detailed verification checklists into on-demand skills, before further #403 pruning.
Acceptance criteria: the approved scope in docs/plans/skill-context-extraction-20261105T214701Z.md; SPEC.md one-source and harness derivation requirements remain unchanged.
Test plan: independent extraction contracts plus the full existing suite. Spec continuity is covered by reviews/skill-context-extraction-read-20261105T215920Z.md; no new spec delta was opened.
Implementation summary: 27 exact instruction bodies move to two processes; their original rows are archived with successor triggers R1626/R1627. Only R0456 is semantically retired, in favor of unchanged R0021. No generator, hook or security-setting code changes. Build/release route applicable verification work to the skill. All twelve standalone bundles retain applicable procedures and explicit role scopes.
Source: badcff7090fdb9d91399a0255ba2885d842e9f20. Baseline: 5ff8a5edc63111637b1bd9a5c1e605e76afbea69.
Test results: contract-verified. `PYTHONPATH=bin python3 -m unittest tests.test_skill_context_extraction -v`: 7 pass. `bin/tests/run`: 310 pass, no skips, 93.920 seconds. Pre-implementation run had six expected failures and one unchanged-security invariant pass. The sole existing-test update changes expected process sequence count 12→14. Both new skills pass skill-creator quick_validate.py in both harness layouts (four validations); missing PyYAML was installed only into an isolated temporary validator environment. All twelve standalone bundles generated. These checks sufficiently establish local content/output continuity; they do not prove live model behavior.
Verification boundary updates: no production integration or fixture boundary changed. Local source/emission/adoption claims are contract-verified. Native selection, invocation, loading, adherence and hook trust/enforcement are unverified/deferred; fresh-session harness exercise is required before claiming those behaviors. Re-run on relevant harness-loading changes; adopting decision session owns follow-up.
SLO status and error budget consumption: N/A; no deployed user journey or production surface was exercised.
Review findings: independent frontier quality, skepticism and continuity verdicts ready; no findings or adoption contradictions. Complete 62-file inventory, both staged layouts, eleven-path candidate and source delta read in the linked review.
Known gaps: native behavior above is deferred. The extraction regression tests require the approved baseline Git object locally; shallow clones and source-only archives need that history before running them. Tests do not fetch it. No CI workflow exists in this repository.
Operational notes: generated self-adoption is on the isolated intake branch. Main and other repositories remain unchanged. Required pull-request protection, administrator enforcement, no force pushes/deletions and five existing methodology labels were read back. Existing target-specific denies are preserved.
Human gate: N/A for consequential release classification; final human process sign-off under intake/R1270 and merge remain pending. Dave's go authorized implementation and preparing this review branch; it does not record final sign-off. No release tag or publication.
Release recommendation: needs the human decision.

## Adoption evidence

Contract-verified: applied the exact reviewed plan with SHA256 40f8f0a2fe0a5a59a4921cb9222a3638fdb4cbf9b730e8f7530606408819205f; all eleven planned path bytes and modes match. Fresh prepare after application has no conflicts and no writes. An isolated copy of all inventoried target context also applied the plan and repeated without any file changes; its human/reviewer fields were explicitly simulated test fixtures. The real branch application records Dave's actual go and its limited scope, and the independent review hash.

Adoption report: docs/fiducial-adoption-20261105T215428Z.md; retained copy: reviews/skill-context-adoption-20261105T215428Z.md.

## Context measurements

Counts are physical lines and whitespace-delimited words, not model tokens. Each installed root changes from 295 to 243 lines and 4,177 to 3,258 words (919 fewer words, 22.0%). Raw generated roots omit the two ownership-marker lines and six marker words. Native agent bodies are byte-identical. No procedure body is preloaded through native skill metadata.

| Generated path | Lines before → after | Words before → after |
|---|---:|---:|
| `claude-code/.claude/agents/architect-agent.md` | 54 → 54 | 531 → 531 |
| `claude-code/.claude/agents/coder-agent.md` | 76 → 76 | 687 → 687 |
| `claude-code/.claude/agents/context-quality-reviewer.md` | 62 → 62 | 722 → 722 |
| `claude-code/.claude/agents/release-manager-agent.md` | 55 → 55 | 778 → 778 |
| `claude-code/.claude/agents/reviewer-agent.md` | 132 → 132 | 1459 → 1459 |
| `claude-code/.claude/agents/skeptic-risk-agent.md` | 114 → 114 | 1450 → 1450 |
| `claude-code/.claude/agents/spec-reviewer-agent.md` | 76 → 76 | 847 → 847 |
| `claude-code/.claude/agents/test-designer-agent.md` | 97 → 97 | 907 → 907 |
| `claude-code/.claude/skills/command-blocks/SKILL.md` | 0 → 38 | 0 → 508 |
| `claude-code/.claude/skills/verification-checklists/SKILL.md` | 0 → 46 | 0 → 655 |
| `claude-code/CLAUDE.md` | 293 → 241 | 4171 → 3252 |
| `codex/.agents/skills/command-blocks/SKILL.md` | 0 → 38 | 0 → 508 |
| `codex/.agents/skills/verification-checklists/SKILL.md` | 0 → 46 | 0 → 655 |
| `codex/.codex/agents/architect-agent.toml` | 4 → 4 | 513 → 513 |
| `codex/.codex/agents/coder-agent.toml` | 4 → 4 | 649 → 649 |
| `codex/.codex/agents/context-quality-reviewer.toml` | 4 → 4 | 699 → 699 |
| `codex/.codex/agents/release-manager-agent.toml` | 4 → 4 | 750 → 750 |
| `codex/.codex/agents/reviewer-agent.toml` | 4 → 4 | 1397 → 1397 |
| `codex/.codex/agents/skeptic-risk-agent.toml` | 4 → 4 | 1402 → 1402 |
| `codex/.codex/agents/spec-reviewer-agent.toml` | 4 → 4 | 814 → 814 |
| `codex/.codex/agents/test-designer-agent.toml` | 4 → 4 | 868 → 868 |
| `codex/AGENTS.md` | 293 → 241 | 4171 → 3252 |

Across both generated layouts, total disk text increases from 5,113 to 5,189 lines and 44,371 to 44,931 words. This is expected on-demand skill framing and routing: the claim is reduced standing root context, not reduced total generated bytes or billed tokens. The new skill files contain 508 and 655 words each including discovery metadata; body loading remains task-dependent.

## Release readiness

Change summary and user-visible behavior: the same procedural obligations load when their explicit skill trigger applies; global honesty, evidence-class and approval principles stay loaded. R0456's duplicate sentence disappears. No further pruning is included; #403 remains open.
Test evidence and review findings: above; source/output contracts pass, independent review ready.
Verification boundary status and live/browser verification: native behavior is deferred/unverified; browser and production verification are N/A.
Operational risks: skill invocation is now necessary for these procedures. Root triggers and build/release routing are present, but real-session adherence has not been exercised.
Rollback or mitigation path: revert the source and generated-adoption changes together through a reviewed PR; do not hand-edit only the root files.
Recommendation and human decision points: needs the human decision — sign off the reviewed process delta and authorize merge. No release publication is requested.

## Local run evidence

These logs were inspected during execution; the durable findings and commands are recorded above.
- `/private/tmp/fiducial-skill-context-evidence/tests-red-refined-20261105T215035Z.txt` — SHA256 `0f70952f7819ea018d0b7c2b0f5dce80243c0bf1e3ef9e821d8b4142f068a625`
- `/private/tmp/fiducial-skill-context-evidence/implementation-focused-20261105T215215Z.txt` — SHA256 `65bcfad624841d124925f20c1dbcbd8b44d77a30b8b8c5f993b62259a004fd8f`
- `/private/tmp/fiducial-skill-context-evidence/suite-20261105T215408Z.txt` — SHA256 `412a5a65d2eaf52af0dce5f3ac3ed12887c6939fc68269ab9076db44da6830e8`
- `/private/tmp/fiducial-skill-context-evidence/skill-validation-20261105T215637Z.txt` — SHA256 `46ea1751c6eb065c33b99e17737c9ab79b8f93d27435284292367281ae956a7e`
- `/private/tmp/fiducial-skill-context-evidence/stand-in-20261105T215750Z.json` — SHA256 `aa447ed65c0cf3cbf6075504d922c454769c1e08d22c70f87ac76ab63a9ff18c`
- `/private/tmp/fiducial-skill-context-evidence/candidate-sizes.json` — SHA256 `06918044e836fb14dc6a41d5f37edd199771e9d9d8db86d8e5077fe81e0defec`
