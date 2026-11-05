# Subtraction release readiness

Date: 2026-11-04 (America/Los_Angeles)
Role: decision session assembling the release evidence; the human decides release.
Recommendation: **needs the human decision**.

## Change package

Intent: remove obsolete prose orchestration while retaining role context, independent review, the evidence model and human authority.
Acceptance criteria: SPEC.md §6, assessed by the whole-delta read and same-reader amendment read. Twelve items are met; item 12's human merge remains required before release, not waived.
Test plan: run bin/tests/run; inspect sort/archive preservation, emitter and hook contracts, adopter reports and bounded human loading evidence; inspect the approved continuity amendment and independently regenerated candidate. No runtime implementation changes in package 7 require new test cases; source/context changes require the real-store checks. This close's review artifacts are the suite-acceptance evidence.
Implementation summary: packages 1–6 retire obsolete rules/tools, consolidate the spec/procedures, add three emission forms and staged adoption, and adopt both layouts in Fiducial. Package 7 appends missing rulings, resolves OQ1–3, restores two retained execution-block obligations and the skill definition, reconciles current documentation, and installs five independently reviewed generated updates.
Test results: baseline bin/tests/run: 303 passed in 96.523s; amended source: 303 passed in 94.126s, no failures or skips. The independent whole-delta reader ran 148 targeted tests; the amendment reader separately checked four rules and both emissions. Contract evidence is sufficient for the declared local behavior; forge mocks and mocked release publication prove only their fixtures.
Verification boundary updates: see the boundary table below; no new live-harness or production claim is made.
SLO status and error budget consumption: N/A for the root SPEC's text repository and small Python tool. No measured journey SLO/error budget is recorded; no production-verified claim or production traffic change is asserted.
Review findings: first close read changes-required; F1–F3 resolved by the human-approved amendment. Amendment quality, skepticism and continuity are each ready-with-findings. F4 is #415; F5 is #416, both non-blocking file-and-land.
Known gaps: human merge; human release/risk ratification; deferred runtime and comparative evidence; tracked non-blocking follow-ups below.
Operational notes: source is pinned by the release tag; each repository upgrades through reviewed adoption. Preserve its ownership manifest and project exceptions. A raw copy over managed files is not the upgrade procedure.
Human gate: https://github.com/davepierceops/fiducial/issues/417
Release recommendation: needs the human decision.

## Release readiness review

**Change summary.** The revision supplies one rule/procedure store, three generated forms, a reviewed adopter, and reversible retirement of obsolete orchestration. The close adds no new runtime mechanism and does not alter bin/release.

**User-visible behavior.** Software projects adopt from tagged source, generating Claude Code/Codex files and reconciling their own context. Ordinary Claude chat continues to load the Chief of Staff bundle as a project file; writing roles retain standalone bundles. Existing twelve-bundle downloads remain available. New execution-block obligations and the skill definition are present in the installed roots.

**Test evidence.** See reviews/pkg-7-baseline-evidence-20261105T023533Z.md, reviews/pkg-7-close-read-20261105T024910Z.md and reviews/pkg-7-close-amendment-read-20261105T033515Z.md. The reviewed amendment source is 15da4ad0b8780b60600cbb522825f5f4bded8683. Its staged plan is d6600cc35af4efc93a0d85e365b33c5767853be420aa85044dca0a7f55426667. Installed bytes/modes match every reviewed write; a second prepare from that same pin has no writes or conflicts, recorded in reviews/pkg-7-regeneration-evidence-20261105T033230Z.md. The full suite was not repeated after exact installation of the already-reviewed generated text.

**Review findings.** The fresh frontier reader authored none of packages 1–7. It read 3c686e0..8dddcd2, then only the approved amendment and candidate. All blocking close findings are resolved. Existing artifacts remain immutable historical records; the amendment artifact supplies the later disposition. #415 is in Reliable bundle generation; #416 is in Software adoption and release authority, both read back open after filing.

**Verification boundary status.** Every met checklist item is supported by contract evidence; the following table bounds the exceptions and operational claims.

| Boundary | Evidence and limit | Release impact and follow-up |
| --- | --- | --- |
| Store, sorting, archive preservation, generation and local hook behavior | Contract-verified local tests and independent audits; original rows/archives preserved. Hook subprocesses do not establish native invocation. | Native invocation remains deferred; test in the actual trusted adopting harness before relying on enforcement. Human opening that session owns the check; rerun after harness/adapter changes and stop relying on a failed guard. |
| Human Claude Code loading | Live-verified only for the prior Illuminait root loading and eight-agent/twelve-invocable-skill discovery in reviews/fiducial-adoption-live-check-20261105T020041Z.md. | Deferred: instruction adherence, manual gate invocation, deny behavior across permission modes, amended-context loading and Fiducial target loading. Human's next fresh session is the trigger; do not broaden the old observation. |
| Codex loading and trust | Package 3b review records bounded live discovery and invocation-only trust override; local adapter tests are contract-verified. | Deferred: ordinary project trust and enforcement in each adopted target. The adopting operator verifies trust after installation; configuration discovery alone is insufficient. |
| Claude-chat comparison | Unverified: no comparison with a new format ran. DEC-001620 selects the existing bundle workflow. | Deferred until a different chat format is proposed; that proposal's owner must supply the comparison. No comparative performance claim is made. |
| Reviewer independence | Author independence observed; executor-family independence unverified. | Accepted-risk under DEC-001600; human must ratify at release. A different-family read would close that gap if required. |
| Push readback, #415 | Contract probe found cmd/command normalization and qualified-ref defects. | Deferred, non-blocking. Manually fetch/read the complete remote ref after pushes; hook-maintenance owner fixes both cases with local-bare-origin tests. |
| Cross-skill procedure paths, #416 | Contract emission finds process/ references absent from fresh target trees. Runtime recovery unverified. | Deferred, non-blocking. Use the installed equivalent skill by name; next emitter-portability change must check both layouts. |
| Release generation/publication | Contract-verified real generator/local Git; mock-verified gh publication boundary. | Human publication and GitHub read-back remain unverified until release. The command's success, repeat, unmerged-close and failed-fetch paths were rehearsed; no real tag/release was created. |

**SLO status and error budget consumption.** N/A as above; no live SLO or remaining error-budget value is available or implied.

**Live/browser verification status.** No browser behavior is part of this revision. The bounded Claude/Codex evidence above is retained; no new live invocation test is claimed. Illuminait PR https://github.com/davepierceops/illuminait/pull/26 was read back open, unmerged, at 2e0f7f97955bf865cb5f8b1a1f72555e3567b5bd during package 7. The real-run/report criterion is met without claiming its merge.

**Operational risks.** The 200-line limit is now guidance by explicit DEC-001640: current raw roots are 293 lines and installed roots 295 lines. Further context pruning is #403. Existing non-blocking follow-ups remain: #398 successor-target validation; #399 residual lint timing; #400 acceptance-criteria visibility/body checks; #405 project-status invocation guidance; #410 dead test helpers; #411 shared-file mode preservation; #412 newly occupied destination directories. Treat #411/#412 as deferred installer limitations: review modes and destination types before apply, use an idle branch, inspect the resulting diff and recover by reverting the adoption commit if needed. #364 release-authority wording and #381 release CLI repository/body-check improvements also remain; this package keeps the human release boundary and supplies --repo explicitly. These are tracked gaps, not promises that the fixtures establish universal enforcement.

**Rollback or mitigation path.** Before merge, decline or amend the PR. After merge, revert through a new PR; never rewrite history. After release, consumers retain the previous source tag or downloaded bundle until they deliberately upgrade. An adopted repository reverts its adoption commit to restore its prior files/ownership, or reruns reviewed adoption from the chosen previous tag. Keep published versions immutable; publish a subsequent correction instead of replacing assets. Inspect any partial installation before retrying.

**Known gaps.** SPEC §6 item 12 remains unchecked until the human merges this close PR; it is a required pre-release condition, not accepted risk. Release publication and accepted-risk ratification remain the human's. #370's broader historical source-to-issue migration is not certified by this revision's archive check. Open roadmap work outside the release claim remains open; this close does not imply all tracker issues are resolved. No productivity, model-compliance, cost-saving or context-efficiency outcome has been measured.

**Recommendation and human decision points.** Needs the human decision. The implementation and source reconciliation are ready-with-findings; merge the PR only after accepting the close record, then decide release and ratify the executor-family risk and stated deferred boundaries. This report supplies neither merge nor release approval. No agent publishes the release.

## Release contents and human command

DEC-001610 requires a date-tagged source repository for software adoption and the existing thirteen attached files: README.md plus twelve role bundles. DEC-001620 keeps the chat Chief of Staff bundle; DEC-001630 keeps the store as source. bin/release already emits the required assets. It must generate them from the eventual merged main SHA, not from an earlier review or intake SHA. No harness archive is required.

The final handoff supplies the exact gh release create block with --repo, a verified ancestor guard, a fresh detached origin/main worktree, freshly generated assets and this report as release notes. It leaves the user's original checkout and untracked retro untouched. The dated tag is v2026.11.04 (human's local date); the publication command is for the human after merge and release approval.

Rehearsal evidence: /private/tmp/fiducial-pkg7-release-command-evidence.json. Real Git and bin/release ran against a disposable bare origin. The gh stand-in validated repository, target SHA, notes-file presence and all thirteen assets. Success returned 0; repeating stopped with 2 on the existing tag; a missing merge stopped with 1; failed fetch stopped with 128. Exactly one mocked publication occurred. Operator checkout, required ancestor and notes path were explicit fixture substitutions; no live GitHub publication was tested. The human's release output is consumed immediately to confirm publication; its release URL and assets are the durable forge record.

A retro of this revision is owed.
