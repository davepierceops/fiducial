# CLAUDE.md pruning — finalization plan

Baseline: `fb310dd9c1ea56e4fa2e1b9b671a50c128fdec0f` (PR #423).
The human completed the standing-rule review on November 5, 2026 (America/Los_Angeles). Exact rulings and their supersessions are in `claude-rule-pruning-rulings-20261105T221134Z.md`. This is the evidence-based pruning follow-up to #403. The older subtraction SPEC’s writing-corpus exclusion is superseded for these explicitly approved shared-rule and skill moves only; unrelated specialized writing rows remain untouched.

## Candidate

The source branch contains approved wording changes, successor retirements, and procedure moves. `claude-rule-pruning-finalization-20261105.json` lists 43 additional retirements (33 deletions without replacement, 10 skill moves) that require a merge-time decision ID. A preview omits exactly these rows from live selection. Original source bodies are preserved; no retirement is implemented as a silent move into an agent.

R0196 and R0564 remain live enforcement registrations with their existing fenced blocks and no standing prose. Hook scripts, deny patterns, configuration and executable modes must match the baseline. The remaining specific review/retro/adoption filename conventions stay in their procedures.

Process selectors now include the original recipients of moved procedures. The pre-existing software workflows retain explicit software/role scopes; moved cross-corpus sections retain their original applicability. R1627 keeps its approved short wording and reaches the recipients of the moved release-impact instructions.

A narrow emitter fix pulls definitions used by process bodies into skills, excluding definitions already supplied by the root and deduplicating those used by spilled rules. This preserves usable on-demand procedures without restoring deleted standing prose or padding approved triggers. Independent tests were designed before that implementation.

## Merge-time retirement bookkeeping

AC-RS-10 requires a real successor row or decision ID. The decision-log procedure allocates IDs at merge; the human ruling log explicitly prohibits preallocation. Therefore the pre-signoff source branch is not a landable final store. Contract tests project the approved live selection using the manifest. A temporary full-tree preview may use the literal `pending-merge-decision` in archived copies, clearly marked as an invalid final archive value; no numeric DEC is invented or reserved.

After the human’s final process signoff and merge authorization, the decision session reads the current default-branch log, allocates the actual decision ID, records the approved batch and remaining historical context, archives exactly the pending originals with that ID, and records it in the manifest. Check that the final emitted bodies and security outputs equal the reviewed preview apart from source provenance. Regenerate and self-adopt through the existing ownership-preserving adopt procedure, with an independent inventory/contradiction read and exact readback. Run final archive-integrity checks and the required suite before merge. No tagged release, unrelated repository adoption, or change to human-approved semantics is authorized by this plan.

## Verification and review

Independent test designer: pruning_test_design; implementation: primary agent. Preliminary frontier scope read: pruning_scope_review, with findings on writing availability and moved condition scopes fixed. Final independent Context Quality Reviewer/frontier read must examine the full source delta and generated preview against the human rulings and intake rubric. The same reader may inspect the adoption candidate because it authored neither.

Checks cover both native harness layouts, every root and agent body, all twelve standalone bundles, original archive preservation, successor scope coverage, exact moved procedure bodies, definition availability, and unchanged security bytes/modes. Evidence is local source/output verification; native skill invocation, model adherence, and live forge/native hook behavior remain unverified. Preview tests do not claim valid final decision allocation or installation.
