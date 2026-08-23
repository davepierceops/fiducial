# Directive — Pass 1 re-gate: confirmation cycle 5

Date: 2026-08-23
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ 0dcd916 plus this directive's own merge, which adds one file under docs/cycles/ and nothing else.

Read first, in full: roles/context-quality-reviewer.md, docs/global-context/review-rubric.md, docs/global-context/core.md, engagements/sre/README.md, engagements/sre/engagement-change-package.md. Then reviews/corpus-regate-cycle-5.md, reviews/sre-baseline-measurement-cycle-5.md, docs/cycles/pass1-regate-fix-6-20260823T031000.md.

## Scope

Confirmation pass: engagements/sre/baseline-measurement.md and engagements/sre/speed-audit.md, whole. Sweep: contradictions over the ten-file engagement set (engagements/sre/* plus cartographer, assistant, critic).

## Instructions

1. Fetch origin; verify HEAD is the stated starting state.
2. Read every file in scope whole.
3. SRE-BM-7: closed / still open / reopened-differently, citing landed text.
4. Confirmation pass per file, all eleven criteria. New findings carry new IDs.
5. Contradiction sweep as scoped; delta against cycle 5.
6. Known and out of scope; do not report: all-decision-roles selecting nothing until the bundler lands; the unbuilt bundler; the two pre-existing bin/tests failures; baton delivery having no home in Core; references in docs/history/, docs/batons/, docs/cycles/, reviews/, retros/.
7. Artifact per skills/review-artifact.md, verdict first, Not inspected required: reviews/corpus-regate-cycle-6.md; a per-file artifact only where a file has a new or still-open finding. If the pass is clean and the sweep shows zero open rows, the verdict is `ready` and one line under the header says the Pass 1 reconciliation re-gate is clean at this SHA.
8. Commit on branch p1-regate-confirm-5, push, open a pull request against main titled "Pass 1 re-gate: confirmation cycle 5" via the REST API with curl. Do not merge. No edits. No status flip. Report the SHA read back from git.

## Report shape

Closure, one line. Confirmation pass: clean or findings. Sweep, one line with delta. Branch, SHA, PR number. Verdict. Anything that could not be executed as written.
