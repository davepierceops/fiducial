# Remaining role-pruning wrap-up evidence

This checkpoint includes approved rulings 1–81 and stops further Writer, Copy Editor and Critic review at the human's request. Approved writing edits through R1167 are included; R1168 remains undecided. It is unmerged and uninstalled. Eight approved no-successor retirements await merge-time decision references.

Baseline: `2be5327e9704b0066eed7e8ef44302aa55179b18`.
Approved source: `111594c574aeca9fb92f0009848aa41cc886fa07`.
Previous published checkpoint: `8fd292d81bb215a63897380a33e2bc6037eb132b`.
Branch: `intake/remaining-role-pruning`; draft PR #432.

## Scope

The source consolidates approval and role-editing instructions, shortens shared workflow guidance, removes retro instructions from Copy Editor/Critic, and changes retro prompts to record recurring preferences and questions without automatically proposing standing rules. The spec and tests explicitly remain provisional while developed together. The approved missing-document consolidation and four Writer rulings are included. No further writing-role policy is decided here.

The manifest records exact source bodies and authorized selector/Human-note changes. Hook blocks, hook implementations, executable flags and generated hook configuration remain preserved. R0166 intentionally changes root instructions; this checkpoint does not repeat the earlier checkpoint's claim of unchanged roots or writing bundles.

Records:

- Rulings: `docs/plans/remaining-role-pruning-inventory-20261107T001928Z.md`.
- Manifest: `docs/plans/remaining-role-pruning-checkpoint-20261108T053045Z.json`.
- Measurements: `docs/plans/remaining-role-pruning-checkpoint-measurements-20261108T053045Z.json`.
- Resumption and deferred work: `docs/plans/remaining-role-pruning-resume.md`.

## Generated output comparison

All three stages contain 77 output records: both native targets and all 12 named bundles. Identical provenance metadata isolates content changes.

| Surface | Baseline words | Actual checkpoint | Approved-removal preview |
|---|---:|---:|---:|
| Claude Code agents, total | 5,659 | 4,484 | 4,354 |
| Codex agents, total | 5,442 | 4,318 | 4,198 |
| Skills, each harness | 10,386 | 10,192 | 10,135 |
| Root instructions, each harness | 577 | 585 | 585 |

The approved-removal preview reduces native agent text by 23.1% and 22.9%, respectively. Every named bundle shrinks. Root instructions gain eight words from approved R0166 consolidation and retain the four existing definitions. Generated hook/configuration bytes and executable flags remain unchanged.

## Actual source versus approved removals

Successor archives are already applied: R0943→R0110, R0950→R1621, R1513/R0090→R0166, R1480→R1479, and R0954/R1002→R1162.

R0940, R0499, R0284, R1091, R1485, R1249, R0159 and R0800 remain live pending merge-time decision allocation. The preview excludes exactly these eight rows and removes the R0284 intake citation. R1249's body is original but its role audience has the approved ruling-62 narrowing. Its final archive must preserve that current record. Until R1249 is retired, actual source still carries the superseded automatic candidate-rule prompt; the preview represents the approved final policy. No fictional retirement references are used.

## Verification

`bin/tests/run` passed all **337 tests in 119.287 seconds**, exit 0, with no failures or skips reported. The retained log is `docs/plans/remaining-role-pruning-checkpoint-tests-20261108T053045Z.log`, SHA-256 `5433f6f059f2c4e4468ca3729a7d9757876e3a1105d75acdfd847d48b23dcfd4`.

The initial 331-test run exposed five obsolete historical assumptions: old checkpoint wording/removal sets and root exactness, the earlier PR429 root snapshot, and R1513's former live status. Historical exact-delta tests now use their reviewed snapshot; live checks retain exact archive/successor coverage, root content with only the approved consolidation, and hook preservation. Six added continuation contracts check the approved delta, explicit metadata changes, eight-removal preview, active citations, six-role editing guidance and retro audiences. The independent reviewer also ran all 23 tests in the four changed test modules successfully in 25.309 seconds.

Source lint checked all 262 current live rows against the 269-row baseline. Four existing findings reproduce identically in both: singleton topic values in R0067, R0564 and R0720, and singleton `escalate` verb in R0527. There are **no new lint findings**, not a clean lint result. The baseline comparison is retained in `docs/plans/remaining-role-pruning-checkpoint-lint-20261108T053045Z.log` and independently reproduced. `git diff --check` passed.

The independent source and test amendment reads found no new issues, reproduced every generated-output metric/hash/mode, and verified standalone audiences and preserved hooks. The final independent review artifact is recorded alongside this evidence.

## Limits and next work

Local validation establishes source and generated-file contracts. It does not establish native harness loading, agent adherence, live hook execution or installed adoption. Main and installed context remain at the previous merged revision.

Before merge, allocate actual retirement references, archive the eight approved rows, remove the R0284 citation, and review/check the final amendment. Any installed update then follows the adopt skill against the finalized source. This checkpoint does not claim release readiness.

Further Writer/Copy Editor/Critic and shared prose/voice review is deferred under #362; R1168 is undecided. The remaining definition audit is also outstanding. R0073 stays unchanged with its follow-up recorded in #430, coordinated with #427. Jev #431, SLO/Top K #428 and tracker portability #425 remain separate projects.
