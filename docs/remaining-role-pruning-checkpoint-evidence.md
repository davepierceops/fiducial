# Remaining role-pruning checkpoint evidence

Observed: the checkpoint covers 44 approved rulings over 45 non-writing-role single-role rows. All 331 tests pass. The independent source review is ready with no unresolved findings. This checkpoint is not merged or installed; five approved retirements await merge-time decision allocation.

Baseline: `2be5327e9704b0066eed7e8ef44302aa55179b18`.
Reviewed source/manifest/measurements: `02de3817b1c7c283f37c0095ec2877adcc3ec8da`.
Test and resumption commit: `e0fd0f2a84b2f1424968533651778a2621a492f6`.
Branch: `intake/remaining-role-pruning`.

## Changes and independent review

- 21 revised row bodies, 17 retained rows, two completed successor retirements and five pending no-successor retirements.
- Existing selectors, Human notes, enforcement blocks, hook configurations and executable maps remain unchanged.
- The Context Quality Reviewer independently checked the complete source delta, approved rulings, scope and all generated outputs. The only defect found during the read was R0264's obligation-only uniqueness criterion; it was corrected to allow definitions and independently re-read.
- Source artifact: `reviews/remaining-role-pruning-checkpoint-read-20261107T020520Z.md`.
- Test amendment received a separate independent read; its artifact accompanies this checkpoint.

## Executed verification

`bin/tests/run` completed with exit 0: **331 tests in 114.760 seconds**, no failures or skips reported. The retained complete output is `docs/plans/remaining-role-pruning-checkpoint-tests.log`, SHA-256 `3db407f13fc14e4eb6d3a0b7dfbb5470cb810ccd98fb7abda39ba85cee7041e5`.

The initial 326-test run failed one historical assertion: PR429's exact source delta was being compared with every future tree. That assertion now uses PR429's landed snapshot. Live archive integrity, roots, hook bytes, scope and procedure checks remain active. Five new checkpoint contracts check exact approved changes, metadata/bindings, successor archives, the pending-retirement distinction, preview removals and citations, and preserved root/hook output. The independent reviewer separately ran all ten tests in the two changed test files successfully.

All 66 store-lint check applications over the 22 changed live rule/process files produced no findings. `git diff --check` passed. No emitter, hook implementation or dependency changes were made.

## Generated context

Each stage includes 77 output records: Claude Code and Codex native files plus all 12 named bundles. The independent reviewer reproduced every recorded metric, hash and executable flag. Provenance is held constant so the comparison measures content, not changing timestamps or commit IDs.

| Surface | Baseline words | Actual checkpoint | Approved-removal preview |
|---|---:|---:|---:|
| Claude Code agent files, total | 5,659 | 5,207 | 5,155 |
| Codex agent files, total | 5,442 | 5,024 | 4,976 |
| Skills, each harness | 10,386 | 10,379 | 10,361 |

The actual checkpoint reduces agent text by 8.0% for Claude Code and 7.7% for Codex. The full approved-removal preview reduces it by 8.9% and 8.6%. Both root instruction files are byte-identical to baseline under common provenance, as are all hook/settings files and executable flags. Nine software/workflow bundles shrink; the three writing bundles remain byte-identical. No pending retired body reappears in another preview output.

The preview filters R0940, R0499, R0284, R1091 and R1485 and removes R0284 from the intake citation. It is an in-memory emitter input, not a fake archive or a claim of completed retirement. Actual sources preserve these five originals until a valid decision reference is assigned at merge. The generator comparison is reproducible using the manifest, `inputs` from `tests.test_skill_context_extraction`, and `checkpoint_preview` from `tests.test_remaining_role_pruning`; emit both native targets and the named queries with common provenance. Metrics are in `docs/plans/remaining-role-pruning-checkpoint-measurements.json`.

## Verification limits and next step

Local tests establish source and emitted-file contracts, including test fixtures that exercise adoption logic. They do not establish native harness loading, agent adherence, live hook enforcement, or adoption of this checkpoint. Main and installed context were left unchanged. No deployment or other-repository write was performed.

Before merge, allocate the actual retirement decision, archive the five original rows, update the intake citation, review the final amendment and run appropriate checks. Any installed-context update follows the adopt skill against a pinned final source. This checkpoint does not claim merge or release readiness.

Resume with shared workflow R0090 using `docs/plans/remaining-role-pruning-resume.md`. Remaining groups: 58 shared rows, 72 writing-role-only rows, and 37 definitions. Continue human rulings one at a time; deeper risk-tier, Jev, review-policy, SLO and tracker work remain separate.
