# Directive — Pass 1 re-gate: confirmation cycle 4

Date: 2026-08-23
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ babda5b plus this directive's own merge, which adds one file under docs/cycles/ and nothing else.

Read first, in full: roles/context-quality-reviewer.md, docs/global-context/review-rubric.md, docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/sre/README.md. Then reviews/corpus-regate-cycle-4.md and its two companion artifacts, and docs/cycles/pass1-regate-fix-5-20260823T020500.md.

## Scope

Confirmation pass: engagements/sre/speed-audit.md and engagements/sre/baseline-measurement.md, whole. Sweeps: contradictions and role boundaries over the seven engagements/sre/ files plus engagements/cartographer.md, assistant.md, critic.md.

## Instructions

1. Fetch origin; verify HEAD is the stated starting state.
2. Read every file in scope whole.
3. SA-6 and SRE-BM-6: closed / still open / reopened-differently, citing landed text.
4. Confirmation pass per file, all eleven criteria. New findings carry new IDs.
5. Sweeps as scoped; one table each; delta against cycle 4.
6. Known and out of scope; do not report: all-decision-roles selecting nothing until the bundler lands; the unbuilt bundler; the two pre-existing bin/tests failures; baton delivery having no home in Core; references in docs/history/, docs/batons/, docs/cycles/, reviews/, retros/.
7. Artifacts per skills/review-artifact.md, verdict first, Not inspected required: reviews/corpus-regate-cycle-5.md; per-file artifacts only where a file has a new or still-open finding. If the pass is clean and both sweeps show zero open rows, the reconciliation artifact's verdict is `ready` and it says so in one line under the header.
8. Commit on branch p1-regate-confirm-4, push, open a pull request against main titled "Pass 1 re-gate: confirmation cycle 4" via the REST API with curl. Do not merge. No edits. No status flip. Report the SHA read back from git.

## Report shape

Closure, one line each. Confirmation pass: clean or findings, one line per finding. Sweeps, one line each with delta. Branch, SHA, PR number. Verdict. Anything that could not be executed as written.
