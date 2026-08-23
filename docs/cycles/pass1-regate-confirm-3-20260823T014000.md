# Directive — Pass 1 re-gate: confirmation cycle 3

Date: 2026-08-23
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ 9759ed3 plus this directive's own merge, which adds one file under docs/cycles/ and nothing else.

Read first, in full: roles/context-quality-reviewer.md, docs/global-context/review-rubric.md, docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md. Then reviews/corpus-regate-cycle-3.md and its six companion artifacts, and docs/cycles/pass1-regate-fix-4-20260823T013000.md.

## Scope

Confirmation pass: every file PR #139 changed (`git diff --name-only c8e95d1 9759ed3`, excluding docs/**). Sweeps: contradictions and role boundaries corpus-wide over the 51-file set.

## Instructions

1. Fetch origin; verify HEAD is the stated starting state.
2. Read every file in scope whole.
3. Per finding in reviews/corpus-regate-cycle-3.md and companions (6): closed / still open / reopened-differently, citing landed text. SRE-BM-5's disposition is D13 (the Cartographer re-measures).
4. Confirmation pass per changed file, all eleven criteria. New findings carry new IDs.
5. Sweeps as scoped; one table each; row-count delta against cycle 3.
6. Known and out of scope; do not report: all-decision-roles selecting nothing until the bundler lands; the unbuilt bundler; the two pre-existing bin/tests failures; baton delivery having no home in Core; references in docs/history/, docs/batons/, docs/cycles/, reviews/, retros/; structural path references in policies/document-metadata-policy.md and roles/chief-of-staff.md; DR-25.
7. Artifacts per skills/review-artifact.md, verdict first, Not inspected required: reviews/corpus-regate-cycle-4.md; per-file artifacts only where a changed file has a new or still-open finding.
8. Commit on branch p1-regate-confirm-3, push, open a pull request against main titled "Pass 1 re-gate: confirmation cycle 3" via the REST API with curl. Do not merge. No edits. No status flip. Report the SHA read back from git.

## Report shape

File count. Closure counts, one line per non-closed finding. Confirmation pass: clean count; files with new findings, one line each. Sweeps, one line each with delta. Branch, SHA, PR number. Largest remaining problem, one line, or "none". Anything that could not be executed as written.
