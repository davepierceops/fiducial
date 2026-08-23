# Directive — Pass 1 re-gate: confirmation cycle

Date: 2026-08-23
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ 287fa78 plus this directive's own merge, which adds one file under docs/cycles/ and nothing else. Every in-scope file is read at HEAD.

Read first, in full: roles/context-quality-reviewer.md (this session's role), docs/global-context/review-rubric.md, docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md. Then reviews/corpus-regate-cycle-1.md and docs/cycles/pass1-regate-fix-20260822T230000.md and docs/cycles/pass1-regate-fix-2-20260822T232000.md — the findings and the dispositions the fixes executed.

## Context

The reconciliation re-gate at 8402c23 produced 47 findings. PR #130 (merge 287fa78) executed the dispositions across 38 files. This cycle confirms: did each fix land as dictated, did it close the finding, and did it introduce anything new.

## Scope

Confirmation pass: every file PR #130 changed, excluding bin/** and docs/**. Enumerate the set from `git diff --name-only 8cdc0b9 287fa78` and record it in the artifact.

Sweeps, re-run corpus-wide over the same 52-file set the prior cycle enumerated (less docs/global-context/inventory.md, now history; plus engagements/critic.md in place of engagements/skeptic.md): duplicate rules, contradictions, term collisions, audience values, retired vocabulary. Path references and role boundaries are re-run only over the changed files.

## Instructions

1. Fetch origin; verify HEAD is the stated starting state.
2. Read every file in scope whole. Do not skim.
3. Per finding in reviews/corpus-regate-cycle-1.md and its 19 companion artifacts: state closed / still open / reopened-differently, citing the landed text. A finding whose disposition the directive reversed (D1, D3, D5, D6, DR-16, DR-19) is closed if the reversed disposition landed.
4. Confirmation pass per changed file: all eleven criteria at the current foundation. New findings carry new IDs.
5. Re-run the sweeps named in Scope; one table each. State row-count delta against the prior cycle.
6. Known and out of scope; do not report: all-decision-roles selecting nothing until the bundler lands; the unbuilt audience bundler; the two pre-existing bin/tests failures; the engagements/sre/README.md Ceremony section header naming the override log; baton delivery having no home in Core; references in docs/history/, docs/batons/, docs/cycles/, reviews/, retros/.
7. Artifacts per skills/review-artifact.md, verdict first, Not inspected required:
   - reviews/corpus-regate-cycle-2.md: header, enumerated scope, per-finding closure table, sweep tables, one line per confirmation-pass file.
   - reviews/<stem>-cycle-<n>.md only for a changed file with at least one new or still-open finding; n one more than the highest existing for that stem; engagements/sre stems are sre-<basename>; engagements/critic.md's stem is critic, cycle 1, Prior cycle naming skeptic-cycle-2.
8. Commit on branch p1-regate-confirm, push, open a pull request against main titled "Pass 1 re-gate: confirmation cycle" via the REST API with curl. Do not merge. No edits to any document. No status flip. Report the SHA read back from git.

## Report shape

File count in scope. Closure: closed / still open / reopened counts, then one line per non-closed finding. Confirmation pass: clean count; files with new findings, one line each. Sweeps: one line each with row count and delta. Branch, SHA, PR number. Then the single largest remaining problem, one line, or "none". Then anything that could not be executed as written.
