# Definition-pruning evidence and release readiness

Date: 2026-11-06. Role: Chief of Staff, with independent test-design and frontier context/adoption review.

## Intent and approved scope

Reduce standing context according to Dave's one-by-one rulings, preserving the behavior he explicitly retained. Baseline: `cb0194aee512f48f3046e5ba9be445d85f97fbd3` (PR #424). Source candidate: `6b473f90c9e7446de1f96207e25a56516378ee0f`. Test amendment: `2e1dd71d3e5f4c2f124c41b51f3ebb61b7aee3ff`.

Acceptance criteria are the exact human rulings in `docs/plans/claude-definition-pruning-rulings-20261106T181925Z.md`, finalized under DEC-001700. The manifest `docs/plans/claude-definition-pruning-finalization-20261106.json` names 14 retired definitions: 13 without replacement and R0208 replaced by the approved single paragraph in command-blocks. R0535, R0780 and R0045 are shortened; R0166 receives the approved authority wording. R0064 is unchanged, with tracker destination/access work tracked separately in #425. The stale R0497 citation is removed while the spec-template deployment-assumptions requirement remains. No generator or hook code changes.

## Observed local verification

- Focused tests: `PYTHONPATH=bin python3 -m unittest tests.test_claude_definition_pruning tests.test_claude_rule_pruning tests.test_skill_context_extraction`: 17 passed in 19.430s.
- Full suite: `bin/tests/run`: 321 passed in 105.226s, exit 0. The independent test agent ran these checks; the root session read back the completion log at `/private/tmp/fiducial-definition-tests.log`.
- New contracts exercise actual source selection, exact archive preservation with valid decision references, preserved metadata and R0064, retired bodies absent from every native output and named bundle, unchanged invocation rules, and the approved paste-block paragraph present in its skill rather than standing agent context.
- PR #424's historical exact-set assertion now checks its landed snapshot, so later approved retirements do not invalidate its history. Its current archive, scope, skill and enforcement checks remain in force.
- All four changed emitted skill files pass the skill-creator validator (command-blocks and spec-template, both harnesses).
- The adopter stages without conflicts. Seven planned writes: CLAUDE.md, AGENTS.md, command-blocks and spec-template skills in both harnesses, and the ownership manifest. Native agent files, hook implementations and settings are unchanged.

## Context measurements

Words use whitespace splitting; these are not token measurements. Line counts include blank lines. Native root numbers below include the two installed ownership-marker lines.

| Context | Before | After |
|---|---:|---:|
| CLAUDE.md lines | 77 | 49 |
| CLAUDE.md words | 1,075 | 580 |
| AGENTS.md lines | 77 | 49 |
| AGENTS.md words | 1,075 | 580 |
| Definitions per root | 18 | 4 |
| Claude agent files, total words (8 files) | 8,560 | 8,560 |
| Codex agent files, total words (8 files) | 8,230 | 8,230 |
| Skills per harness, total words (15 files) | 10,484 | 10,531 |

Roots shrink by 495 words (46.0%). Every root-plus-one-native-agent combination shrinks by the same 495 words. Skills grow by 47 words per harness, reflecting the approved paste-block paragraph and removal of the stale citation. The retired definitions are not redistributed into agent files.

Standalone bundles also shrink:

| Role | Before words | After words | Change |
|---|---:|---:|---:|
| chief-of-staff | 10347 | 9899 | -448 |
| architect-agent | 4136 | 3808 | -328 |
| spec-reviewer-agent | 4400 | 4072 | -328 |
| test-designer-agent | 4274 | 3976 | -298 |
| coder-agent | 4364 | 4066 | -298 |
| reviewer-agent | 5181 | 4883 | -298 |
| skeptic-risk-agent | 5192 | 4894 | -298 |
| release-manager-agent | 5478 | 5066 | -412 |
| context-quality-reviewer | 4013 | 3683 | -330 |
| writer | 5632 | 5251 | -381 |
| copy-editor | 5722 | 5392 | -330 |
| critic | 5489 | 5159 | -330 |

## Installation and environment

The staged source pin is 6b473f9. At staging, only the test amendment was uncommitted; it changes no emitted input. A detached checkout at that source pin is used to repeat preparation with identical provenance. Local execution uses the repository's Python emitter and adoption helper; only Git/GitHub calls cross the network boundary. No credentials enter the context.

Existing branch protection was read back: force pushes and deletion disabled, administrators subject to protection, pull-request review configuration present (required approving count zero). The existing human-gate, blocking, deferred, accepted-risk and not-material labels were read back without mutation. Runner deny mechanisms remain unchanged and are covered by local contract tests; live harness enforcement is not established here.

## Release readiness and boundaries

User-visible behavior: new sessions receive the smaller standing context and the approved paste-block guidance through command-blocks. The normal invocation rules remain unchanged.

Evidence class: contract-verified local source selection, archive integrity and generation. Actual model loading, skill invocation/adherence and live harness enforcement remain unverified; those unchanged-runtime gaps are not-material to this source/context-only landing. Browser/production checks and SLO/error-budget effects are not-material: no application code or deployed service changes. Repository-specific tracker portability is deferred to #425; R0064 remains intact.

Rollback: revert this PR through the normal PR flow, preserving the appended historical decision and immutable review records, then regenerate/adopt from the chosen source. Do not rewrite historical approval or review artifacts.

Human authority: Dave explicitly approved every wording/removal, then authorized finalization by “go” after agreeing to retain R0064. No outstanding wording ruling. A publication or tagged release and adoption into other repositories are outside this batch.

## Finalization evidence

- Independent frontier/context/adoption review: `reviews/claude-definition-pruning-read-20261106T195037Z.md`, ready in all three passes, no findings. Reviewed source and tests through 2e1dd71, all 66 inventory files, 65 emitted files, seven planned writes and every standalone bundle diff.
- Applied the reviewed seven writes and verified exact installed bytes and modes against the plan. Installed CLAUDE.md and AGENTS.md each contain 49 lines and 580 words.
- Same-pin repeat preparation produced zero conflicts and zero writes. The independent reviewer checked its inventory and emitted equivalence before repeat apply. Repeat apply returned `[]`, preserved every adoption report hash and created no new report.
- Adoption report: `docs/fiducial-adoption-20261106T194709Z.md`; retained copy: `reviews/fiducial-definition-adoption-report-20261106T194709Z.md`.
- Original plan SHA256: `3e657857a7d69029e6ee942e1af4627eff44644138231607d1ce216de64b75cc`; review SHA256: `8fb621df9dc19480768c5c66423a669d78e8f929d21bf19b0fdf2624c9864a0e`.
- Repeat plan SHA256: `1b61f823f25b73d81c5a7743fefd2c2dd2f5333e705b1c8a416024af1db7878d`; repeat review SHA256: `7317f9218f633e660f087b2346783ee4bf568967b1d9cad2230ecb12705a28be`.
- PR #426 carries the batch. The source pin in installed context remains 6b473f9 because subsequent commits add only tests and evidence/derived output, not different emitter inputs.

Release recommendation: ship. Human decision points: none outstanding within the approved batch. Remote merge and main-checkout readback are subsequent landing evidence, not claimed by this pre-merge report.
