# Backlog reconciliation — proposed dispositions

Date: 2026-11-10 (America/Los_Angeles).
Status: five closures approved and applied 2026-11-10; the local obsolete-permission cleanup was subsequently authorized and completed. Other proposed tracker amendments remain drafts. The original assessment below is preserved; see the execution records at the end.
Scope: all 39 open GitHub issues in davepierceops/fiducial, read through the GitHub connector on this date; all had zero comments at the read. Local and fresh remote main both identify `5b2a62f3b17aca1d859a43032b9ca2295c185391`.

Observed facts below come from those issue bodies, the named committed sources and the checks recorded here. Recommendations and proposed dispositions are inferred. Historical test results are identified as recorded evidence, not reruns. Unknown means not established by this assessment. GitHub remains the ongoing tracker under DEC-000880; this file is a dated decision aid, not a replacement backlog.

## Proposed ruling

Inferred recommendation: close five issues, retaining the distinctions between completed work and superseded designs. Keep the other 34 open. Preserve all six milestones; none becomes empty from these closures. Do not resume deferred writing work, redesign policy, or publish a release as part of reconciliation.

| Issue | Proposed state/reason | Observed support |
|---|---|---|
| [#360](https://github.com/davepierceops/fiducial/issues/360) — thin bundle pointers | Closed / not planned: superseded design | DEC-001100 explicitly supersedes DEC-000910; DEC-001630 confirms generated harness context from the store. `process/adopt.md`, native emitters and README implement the replacement. Do not claim the original thin-pointer acceptance criteria passed. |
| [#361](https://github.com/davepierceops/fiducial/issues/361) — obsolete manifest and collaboration state | Closed / completed | Both files are absent from the root, preserved under `docs/history/` with archive notices; DEC-001580 and merged PR #409 record the cleanup. Current README points at supported adoption. The removed-tool reference check passes in a clean clone; the existing clone's separate local residue is retained under #382 below. |
| [#367](https://github.com/davepierceops/fiducial/issues/367) — seven skipped tests | Closed / completed by retirement | The evaluation baseline has six unconditional skips in `test_directive_trd.py` and one `skipTest` in `test_land.py`. All belonged to retired tools; commit `61c1c73` removes those suites under package 6a. An additional conditional root-permission skip in `test_check_directive.py` disappeared with that suite too. Current test source has no such skip calls/decorators; the retained final run records 339 tests, OK, no skips. This does not claim the retired behavior was implemented. |
| [#385](https://github.com/davepierceops/fiducial/issues/385) — bin/land improvements and TRD findings | Closed / not planned: retired mechanism | `bin/land` and its implementation/tests were removed by package 6a; the specifications are historical. DEC-001160, DEC-001200 and DEC-001580 govern the removal. Stacked-branch behavior, help text, the old spec question and four old TRD finding classes are all superseded with that mechanism, not fixed or verified. |
| [#405](https://github.com/davepierceops/fiducial/issues/405) — project-status invocation trigger | Closed / completed | Source commit `a4514cb` restores the explicit request trigger and exclusion of automatic status at Chief of Staff startup. Fresh Claude Code and Codex emission both contain the request-trigger description and startup exclusion in the body. This establishes emitted content, not live skill selection. |

## Exact proposed closure notes

These are ready-to-post drafts, not comments already sent. Preserve the original issue bodies as history.

### #360

Observed: the thin-pointer design recorded here was superseded explicitly by [DEC-001100](https://github.com/davepierceops/fiducial/blob/5b2a62f3b17aca1d859a43032b9ca2295c185391/decisions/log.md#dec-001100--the-store-stays-the-source-the-adopter-reconciles-into-repos), then confirmed by DEC-001630. The supported design generates Claude Code/Codex context from the canonical store and reconciles it through [adoption](https://github.com/davepierceops/fiducial/blob/5b2a62f3b17aca1d859a43032b9ca2295c185391/process/adopt.md). Close as superseded/not planned, not as a successful implementation of thin pointers. Native loading and enforcement limits remain recorded in the adoption evidence; this closure does not waive them. Historical-entry-point retirement is separately covered by #361.

### #361

Observed: [PR #409](https://github.com/davepierceops/fiducial/pull/409) archived MANIFEST.md and COLLAB-STATE.md under docs/history/ with archive notices, and DEC-001580 records that landing. Neither remains a root entry point; current README describes the replacement adoption path. On 2026-11-10, the removed-tool reference check passed in an isolated clean clone at 5b2a62f. The original clone has ignored local permission entries for cycle-open; that separate per-clone residue remains in the proposed #382 follow-up. Close this historical-entry-point issue as completed; this does not certify #370's broader tracker migration.

### #367

Observed: all seven unconditional skips from the evaluation baseline belonged to retired directive/landing suites: six in test_directive_trd.py, one in test_land.py. [Commit 61c1c73](https://github.com/davepierceops/fiducial/commit/61c1c73) removed these with the retired tools; package 6a's review and DEC-001580 record the disposition. The conditional root-only skip in test_check_directive.py was removed as well. Current test source contains no skip decorators/calls, and the retained [final test log](https://github.com/davepierceops/fiducial/blob/5b2a62f3b17aca1d859a43032b9ca2295c185391/docs/plans/remaining-role-pruning-final-tests-20261108T054131Z.log) records 339 tests, OK, without skips. Close as reconciled by retirement, not by implementing the old contracts. The full suite was not rerun for this reconciliation; the separate local failure is recorded under #382.

### #385

Observed: [PR #409](https://github.com/davepierceops/fiducial/pull/409) removed bin/land, its package and associated tests; DEC-001580 records the landing under the subtraction decisions. The stacked-branch arm, help improvements, old spec question and all four deferred TRD finding classes therefore have the same disposition: superseded by retirement, not implementation work to resume. Close as not planned. Historical specs and findings remain preserved; no claim is made that their former acceptance tests passed.

### #405

Observed: [commit a4514cb](https://github.com/davepierceops/fiducial/commit/a4514cb) restored the project-status invocation boundary. Fresh Claude Code and Codex emissions from 5b2a62f on 2026-11-10 both describe the skill as user-requested and retain “Starting a Chief of Staff session alone does not trigger this skill.” Close as completed at the emitted-content boundary. No live automatic-selection or adherence test is claimed.

## Issues that need narrower or updated descriptions

Inferred recommendations in the second column are proposed title/scope amendments. Each row records observed support and the remaining uncertainty. Preserve prior descriptions as dated context rather than silently erasing acceptance criteria.

| Issue | Proposed title / remaining scope | Observed evidence and boundary |
|---|---|---|
| [#359](https://github.com/davepierceops/fiducial/issues/359) | Validate setup guidance for complete, incomplete and uninspectable environments | `process/project-setup.md` now selects Chief of Staff, appears in the generated bundle, and is linked from README. Packaging is delivered; scenario-based onboarding evidence, reusable verification rules and actionable unknown-state guidance are not established here. Keep those requirements. |
| [#363](https://github.com/davepierceops/fiducial/issues/363) | Complete the remaining definition audit | DEC-001700 and #426 completed one definition batch; DEC-001720 and the resume record explicitly leave further definitions unfinished. Keep this as the definition-specific work item under broader #362, with shared ruling records; do not duplicate an audit or treat all glossary work as finished. |
| [#364](https://github.com/davepierceops/fiducial/issues/364) | Verify release-authority consistency and clarify repository publication instructions | R0534/R0535, build and release now state routine/consequential paths. `process/named-queries.md` still says this repository's release is on the human's go and the human runs publication; review-artifact describes ready as ready for human approval. Whether these are deliberate scoped exceptions or unresolved ambiguity needs a ruling, plus the promised scenario and generated-bundle audit. Do not change authority from this assessment. DEC-000920 remains the starting decision. |
| [#366](https://github.com/davepierceops/fiducial/issues/366) | Finish local-output provenance and input-scoped release checks | DEC-001560 and `test_bundle_cli.py`/`test_emit_bundle.py` establish the delivered local/offline rendering change. `bin/release:_dirty_under` still checks the whole working tree; `render.py` still stamps only HEAD and time, without local-edit identity. Retain accurate local provenance, effective release-input discovery, added/deleted/re-keyed inputs and generator-code coverage. |
| [#368](https://github.com/davepierceops/fiducial/issues/368) | Add Fiducial-repository PR validation | No tracked `.github` workflow exists. Keep this repository's requested CI work and its #358/#365/#366 dependencies. #430's rejection of universal required CI for every adopter does not by itself cancel this narrower repository issue. |
| [#373](https://github.com/davepierceops/fiducial/issues/373) | Validate guided SPEC authoring in fresh sessions | PRD/TRD are replaced by SPEC; README and `process/spec-template.md` explicitly support drafting by interview. Retain sparse-idea and partially specified project trials, human ownership, reviewer handoff and advertised-download checks. A template is not behavioral evidence. |
| [#375](https://github.com/davepierceops/fiducial/issues/375) | Complete adopter-facing workflow and assumption audit | `process/build.md` now owns the spec-to-release flow and README directs adopters to it. `change-flow.md` still opens with rule/process taxonomy; #416 shows source-path assumptions remain. Retain the requested adopter-read and cross-bundle assumption audit; replace obsolete PRD/TRD wording with SPEC. |
| [#381](https://github.com/davepierceops/fiducial/issues/381) | Fix release-command portability and validate generated release bodies | Directive fence/title and M2 requests are superseded with their removed tools. The current release command still omits `-R`; the release loop generates/copies assets without the requested independent selected-body check. Preserve these two remaining acceptance criteria. |
| [#382](https://github.com/davepierceops/fiducial/issues/382) | Resolve per-clone retired-tool residue after committed tool removal | Package 6a removed the tools and aimeta, superseding this issue's old “keep those tools” scope. New observation: the removed-tool check fails only in the main checkout on four ignored `.claude/settings.local.json` permissions naming cycle-open (lines 23, 70, 71, 73); it passes in a clean clone. Proposed residual work: review/remove those exact obsolete local entries while preserving unrelated configuration, and decide/document whether the test deliberately scans ignored per-clone files. Do not broadly exclude local files merely to make it green. DEC-000970 governs the per-clone boundary. No configuration changed in this assessment. |
| [#387](https://github.com/davepierceops/fiducial/issues/387) | Resolve remaining historical decision-log clarifications | NB-1 is superseded: R1613 retired under DEC-001260, eliminating “flush package.” NB-2's later-package interpretation and O-1/O-2's attribution/count corrections still lack an identified subsequent ruling. Preserve these as questions; any correction belongs in an appended decision, not an edit to history. |
| [#393](https://github.com/davepierceops/fiducial/issues/393) | Evaluate claim classification using current consolidated sources | The question remains open. Update obsolete row pointers to R0172 (provenance) and the verification-checklists skill (evidence guidance), alongside the public-prose classification. Retirement of source rows did not approve a unified classification. |
| [#399](https://github.com/davepierceops/fiducial/issues/399) | Resolve review-hook behavior on partial artifacts | `render.row_text` and named #399 tests remove orphan enforcement YAML; store-lint now allows SPEC.md and decisions/log.md paths; intake enforcement is installed. R1414 remains PostToolUse on Edit/Write and its missing-verdict behavior remains. Coordinate this specific timing question with #427's broader review/artifact work rather than closing all four bullets together. |
| [#400](https://github.com/davepierceops/fiducial/issues/400) | Decide remaining vocabulary-check and historical-sort follow-ups | R0472 has since been shortened; acceptance criteria are explained in the selected spec-template, not a universal definition row. The old proposed fix requires reassessment, not automatic widening. `reconcile_sort.py --bodies` remains a standalone script mode, and the sort-table notes are historical. Decide what should survive as a current check and record historical corrections without rewriting the original evidence. |

## Keep open with existing scope

Observed: the following requirements remain open in their tracker records. The evidence cited supports retaining them, not a claim that every implementation path was exhaustively audited. Inferred recommendation: preserve current scope and defer priority selection to Dave.

| Issue | Remaining work and support |
|---|---|
| [#355](https://github.com/davepierceops/fiducial/issues/355) | Portable author-profile contract and cross-role integration. README and voice still describe Dave's writing defaults. No completed portability evidence identified. |
| [#356](https://github.com/davepierceops/fiducial/issues/356) | Sample-based profile setup, no-sample fallback and optional review; dependent on #355. Fresh-session behavior remains unestablished. |
| [#357](https://github.com/davepierceops/fiducial/issues/357) | Noninterrupting refinement and explicit/inferred preference separation; dependent on #355. Keep distinct from first-use setup. |
| [#358](https://github.com/davepierceops/fiducial/issues/358) | Selective reference labels and missing-target refusal, under DEC-000930. Current render emits row bodies without selective labels; a synthetic unresolved reference survives rendering. No claim that this isolated renderer probe covers every emitter. |
| [#362](https://github.com/davepierceops/fiducial/issues/362) | Remaining writing/shared prose/voice and corpus audit. Its latest “Landed” section already records #432 accurately. DEC-001720 leaves R1168 and later writing work deferred; no restart proposed. |
| [#365](https://github.com/davepierceops/fiducial/issues/365) | Reject empty/whitespace/rationale-only instruction bodies. Direct current FileRowSource probes accept all three with empty agent bodies. No production mutation performed. |
| [#370](https://github.com/davepierceops/fiducial/issues/370) | Full source-to-disposition mapping of legacy backlogs and nested riders. Archival and this 39-issue assessment do not establish coverage of every source item. SPEC and #417 explicitly preserve this broader gap. |
| [#371](https://github.com/davepierceops/fiducial/issues/371) | Annotated reproducible software and writing walkthroughs. README links procedures rather than the required paired walkthroughs. |
| [#372](https://github.com/davepierceops/fiducial/issues/372) | Comparative outcomes and overhead evaluation. README explicitly says comparative effects remain unestablished. |
| [#374](https://github.com/davepierceops/fiducial/issues/374) | License-text review. No legal assessment or authoritative-text comparison performed in this reconciliation; no disposition beyond retaining the issue. |
| [#398](https://github.com/davepierceops/fiducial/issues/398) | Retirement-target existence/chain checking. `reconcile_sort.py` still validates retired values by shape; no general target lookup was found in that path. Specific newer retirement tests do not establish a general check. |
| [#410](https://github.com/davepierceops/fiducial/issues/410) | Dead test helpers and dependence on archived corpus inputs. Helpers remain; package 6a review F-6 is the detailed evidence. Exact dead-helper count was not recalculated. |
| [#411](https://github.com/davepierceops/fiducial/issues/411) | Preserve existing shared-file permissions during adoption. Current helper still plans generated modes for shared Markdown/JSON and chmods them at apply. Prior 0600 reproduction was not rerun. |
| [#412](https://github.com/davepierceops/fiducial/issues/412) | Reject newly occupied destination directories before any write. Inventory still omits ordinary directories and safe() checks parents without rejecting a final directory. Prior partial-write reproduction was not rerun. |
| [#415](https://github.com/davepierceops/fiducial/issues/415) | Codex cmd normalization and qualified branch readback. Push-readback still reads command and strips qualified refs with rsplit. Native event delivery remains unverified. |
| [#416](https://github.com/davepierceops/fiducial/issues/416) | Resolve cross-procedure references in installed layouts. Build and other generated skills still contain source `process/` paths. No automatic runtime recovery claimed. |
| [#425](https://github.com/davepierceops/fiducial/issues/425) | Repository-specific tracker identity/access context and repeat-adoption preservation. Current adopter label setup remains GitHub-specific; R0064 was explicitly deferred. |
| [#427](https://github.com/davepierceops/fiducial/issues/427) | Broader review/quality/artifact redesign, including gate availability and report-copy/hook mismatch. DEC-001710/001720 and the issue explicitly keep it separate. |
| [#428](https://github.com/davepierceops/fiducial/issues/428) | Coordinated SLO/error-budget/Top K reconsideration. These requirements remain retained pending the separate decision. |
| [#430](https://github.com/davepierceops/fiducial/issues/430) | Risk-tier and proportionate-verification investigation. A project brief, not approved new requirements. |
| [#431](https://github.com/davepierceops/fiducial/issues/431) | Jev reviewer experiment. Exact service/model/access route and its capabilities, cost and reliability remain unknown in the issue. No investigation was run here. |

## Current-reference corrections to prepare after the ruling

Observed: SPEC.md frontmatter still says close approval pending and definition-of-done item 12 says the human merge remains. [Gate #417](https://github.com/davepierceops/fiducial/issues/417) records human completion, PR #418 merged at `0ca563ee53c309840be4ab94dda74f9b075149ba`, and publication of v2026.11.04. The older DEC-001660 is a valid historical pre-merge observation and must remain intact.

Inferred proposed correction: change the current spec status to “subtraction merged and released 2026-11-04; completion recorded in #417”; check item 12 and replace its pending-merge explanation with the completed merge/release evidence. Preserve the reviewed-SHA and verification-limit history. Present the actual diff and append any required reconciliation approval through the existing spec/change workflow; do not manufacture an earlier approval date or reinterpret approval for later releases.

Observed: #362's current “Landed” section already reconciles its earlier checkpoint entries. No correction needed to those historical sections. The 23 prunable worktree registrations and old remote branches reported in status are administrative residue, not additional feature commitments; no deletion is proposed by this file.

## Checks and limits

- Observed: fresh GitHub issue read returned exactly the 39 numbers in this file, with zero comments; fresh branch read returned `5b2a62f3b17aca1d859a43032b9ca2295c185391`.
- Observed: source reads covered current emitters/rendering, store parsing, release dirty check/command, adoption plan/apply, push-readback, lint exceptions, project setup, build/release/gate, relevant decisions, archival records and final #432 evidence.
- Observed: fresh native emissions completed successfully into `/tmp/fiducial-backlog-codex-20261110` and `/tmp/fiducial-backlog-claude-20261110`. Both project-status descriptions contain the user-request trigger; both bodies exclude Chief of Staff startup alone. Their YAML quoting differs; an initial quote-sensitive string check falsely returned false for Claude, and direct content inspection resolved that probe artifact.
- Observed: three temporary FileRowSource probes accepted empty, whitespace-only and Human-only rule bodies; a synthetic renderer probe retained an unresolved reference. These are local contract probes, not complete end-to-end CLI tests.
- Observed: `test_removed_tools.py` failed in the original clone with four ignored local cycle-open permission references, then passed (1 test) in `/tmp/fiducial-backlog-check-20261110`, a clean local clone of the same commit. No local configuration was edited.
- Observed: historical skip inventory was inspected at `8ea66f527cf0114441b34976b09a8326fccbf3c2` and mapped to removal commit `61c1c73`. The retained 339-test log was read; no full-suite rerun was performed and no current full-suite pass is claimed.
- Unknown: live harness selection/adherence/enforcement; exhaustive legacy-backlog migration; acceptance of historical policy interpretations; comparative effectiveness. Nothing here grants release authority or changes a verification boundary.
- Observed: no GitHub issue/comment/milestone write, commit, push, merge, release, or governed-source edit was made for this proposal. Only this dated draft was added locally.

## Execution record — approved closures, 2026-11-10

Told: Dave answered yes to closing the five issues with the drafted notes. This authorizes those closures; it does not approve the remaining scope amendments or local permission edits.

Observed: the approved closure notes were posted verbatim, followed by the state changes below. Fresh independent GETs verified each closed state and reason, exact comment content and unchanged original issue body. The open-issue collection now contains 34 issues.

| Issue | Verified state reason | Published closure note |
|---|---|---|
| #360 | not_planned | https://github.com/davepierceops/fiducial/issues/360#issuecomment-6781494421 |
| #361 | completed | https://github.com/davepierceops/fiducial/issues/361#issuecomment-6781496639 |
| #367 | completed | https://github.com/davepierceops/fiducial/issues/367#issuecomment-6781498514 |
| #385 | not_planned | https://github.com/davepierceops/fiducial/issues/385#issuecomment-6781500403 |
| #405 | completed | https://github.com/davepierceops/fiducial/issues/405#issuecomment-6781502522 |

Observed: automatic approval review rejected the first attempted #360 comment because an added sentence would publicly attribute approval to a private chat. That sentence was removed; only the previously approved closure text was then posted. No rejected text appears in the verified comment.

Observed: local permissions remain unchanged. In plain language, four saved Claude permissions still mention a removed command, and a test scans that local file and flags the old name. The same test passes in a clean clone without the local file. This establishes stale local configuration, not a failure of the removed command or proof that the whole current suite passes. The proposed #382 amendment is still pending; its GitHub body has not been changed.

## Subsequent local cleanup — 2026-11-10

Told: Dave authorized the recommendation to remove the four obsolete permissions and rerun the affected test.

Observed: removed exactly the four `cycle-open` entries from `permissions.allow` in the ignored local `.claude/settings.local.json`. The edit preserved every other byte and the file mode. Parsed JSON before/after comparison and exact file readback verified that no other setting changed.

Observed: `python3 -m unittest discover -s bin/tests -t bin -p test_removed_tools.py` now passes in the original checkout: 1 test, 0.094 seconds, OK. The local failure described above is resolved. This is the affected-test result, not a full-suite run or a live Claude enforcement test.

Observed: the test itself and tracked application/configuration sources were not changed. No additional GitHub issues were closed or edited. The earlier proposal to retain #382 specifically for these four local entries is now outdated; any remaining test-scope discussion or closure of #382 is a separate tracker disposition, not unfinished permission cleanup.
