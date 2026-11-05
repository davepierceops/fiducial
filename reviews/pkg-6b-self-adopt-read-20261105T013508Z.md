# Review: pkg-6b-self-adopt — read-20261105T013508Z

Verdict: ready
Reviewed: pkg-6b-self-adopt @ 83209bb3d8b1a22f2b199aa148a48bd16aee5f7e
Baseline: pkg-6b-self-adopt @ 33ff36411f231c611152e4473a2b6f1262ca2561
Reviewer: independent mechanical reviewer (pkg6b_reviewer); authored none of the reviewed delta
Date: 2026-11-04
Scope: the entire package 6b delta: adopted roots, both harness trees, ownership, settings preservation, four authorized removals, README, independent contradiction read and identical adoption/execution reports. Observed, contract-verified: all 62 plan writes match installed bytes and modes; all 61 ownership entries are present, including 23 whole-file hash/mode checks; all eight Codex agent TOMLs parse. Final plan SHA256 is 25395afa28497ae0cbb3f28270ac81addf0ddfbcf36608bc198ca93f95c75b6a, with matching review/approval hashes. Fresh emission from a separate local clone pinned to the baseline with canonical origin exactly matches the reviewed Claude Code tree (30 files) and Codex tree (31 files), including modes; writer bundle emission produces one Markdown file. Observed, contract-verified: direct installed-hook probes reject both rules/ and process/ outside intake/* with status 2, allow them on a committed temporary intake/* branch with status 0, and allow README paths in both cases. Claude Edit and Codex apply_patch payloads were exercised; no mutation tool ran, and the checked rule hash stayed unchanged. Independent build_plan against the installed target returns no writes or conflicts. README has 116 lines; all repository paths named in prose, links and example commands exist. It describes the evidence model, adopter versus standalone bundles, writing roles, Claude chat, all three emit targets and intake. Exactly the two stale agents and two placeholder READMEs are deleted; all eight original settings denies survive. Governing source, SPEC.md, bin/release and decisions/log.md are unchanged; OQ1 remains open. The two report copies are byte-identical, and git diff --check passes.
Cross-checked: SPEC.md in full; subtraction plan, especially packages 5–7 and the 6a/6b split; approving and related DEC entries including DEC-001100, DEC-001110, DEC-001140, DEC-001220–001320, DEC-001390–001460 and DEC-001510–001560; process/adopt.md and process/review-artifact.md; emitter interface and shared selection/rendering behavior; installed intake scripts and Codex dispatcher; final stage /private/tmp/fiducial-pkg6b-stage-final; independent contradiction review; /private/tmp/fiducial-pkg6b-tests-final.log, which records 303 tests passing in 97.554 seconds. The full suite was not redundantly rerun. Independent probe/render/install check summaries are under /private/tmp/fiducial-pkg6b-review-*-20261105.json.
Not inspected: live Claude Code /context loading, Codex project-hook trust and actual harness-driven enforcement, forge configuration or label service behavior, force-deny behavior in every runner permission mode, production behavior, or the package 7 whole-revision close. These are not claimed by local file/schema/render/hook subprocess evidence. Forge setup and labels are told by the parent session, as the execution report states. The actual empty-plan apply is the parent's independently recorded observation; this reviewer independently recomputed the empty plan. Existing 287-line emitted-root guidance and previously reported adopter limitations are baseline conditions, not new defects. Live loading/trust is explicitly unverified with deferred release impact in the package report; fresh-session observation remains the stated follow-up trigger.
Findings: none

## Quality

Verdict (quality): ready

## Skepticism

Verdict (skepticism): ready

## Continuity

Verdict (continuity): ready
