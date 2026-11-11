# Release preparation handoff — 2026-11-10

- Told: fix issue #411 before publishing. Publication is not authorized. The next session should implement that fix first, then refresh the release candidate and evidence.
- Observed: source main at handoff is `5b2a62f3b17aca1d859a43032b9ca2295c185391`. These reports are being preserved on `codex/release-handoff-20261110`; that branch is an evidence archive, not the release candidate.
- Observed: no #411 implementation or test edits have been made. The pending release gate is [#433](https://github.com/davepierceops/fiducial/issues/433); defect details are in [#411](https://github.com/davepierceops/fiducial/issues/411).

## Completed work and evidence

- Observed: [backlog reconciliation](../../plans/backlog-reconciliation-20261110.md) records five applied closures (#360, #361, #367, #385, #405). Other proposed issue edits remain drafts.
- Observed: four obsolete cycle-open permission entries were removed from the ignored local `.claude/settings.local.json`. The report records the verification. This machine-specific file is intentionally excluded from Git; another clone does not inherit that cleanup.
- Observed: [release package](release-package.md), [notes](release-notes.md), 13 assets, hashes, generation/test logs and source-state record are preserved beside this handoff. They cover the previous candidate only.
- Observed: [independent review](../../../reviews/release-consolidation-quality-read-20261110T230826Z.md) records separate quality/continuity and skepticism passes. Its historical ready-with-findings verdict predates the new #411 prerequisite and does not cover its future fix.
- Observed: the stable full suite passed 339 tests. The first run failed once while source remote configuration changed; that cause remains inferred, not proven. Both logs and the targeted recheck are retained.

## Resume #411

- Observed source locations: the executable adopter is the Python fence in `process/adopt.md`; `bin/tests/test_adopt.py` extracts it. `build_plan` currently takes staged modes for existing shared Markdown/JSON, and `apply` chmods to the planned mode. #411 documents existing 0600 settings becoming 0644.
- Inferred implementation direction: preserve existing shared Markdown/JSON modes during plan generation, retain staged modes for newly generated files and executable scripts, and preserve mode-drift preflight protection. Do not expand this into #412's separate partial-write defect.
- Required workflow: read build, intake and verification-checklists skills; prepare and independently review the plan; use a separate test designer for meaningful failing regressions and a different coder for the fix. Governed process changes use an intake branch and independent Context Quality review. Refresh generated context through the applicable adoption procedure. Preserve existing independent historical reviews.
- Inferred acceptance examples: restrictive shared JSON and Markdown remain restrictive after adoption, upgrade and repeat/no-op; new executable files retain executable modes; post-plan mode changes still reject before application. Independent reviewers should refine the test plan.
- Observed: decisions/log.md currently ends at DEC-001720. Consult the live log before allocating a new decision number. Existing approvals do not approve publication of this next revision.
- Required before publication: finish/review the fix, refresh the candidate assets and full evidence, update #433, and obtain explicit publication approval. The archived 5b2a62f assets must not be presented as containing the fix.

## Verification limits

- Observed: local source/tests/generated-asset checks only; native fresh-session loading, model adherence and hook trust/enforcement remain unverified. Existing package lists the other deferred issues.
- Inferred: temporary clones under /tmp are expendable. This committed report set, source history and GitHub issues provide the durable starting point; do not depend on this chat or temporary clone state.
