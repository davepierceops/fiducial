# Fiducial v2026.11.10 — context consolidation release package

Status: superseded as the current reference by [candidate-refresh.md](candidate-refresh.md), which covers the candidate carrying the #411 fix. Historical status follows. HOLD for #411. The preparation and independent review below cover the previous candidate only; publication is not approved or performed. Date: 2026-11-10 (America/Los_Angeles).

Current handoff: [session-handoff.md](session-handoff.md). The earlier publish recommendation is superseded by the requirement to fix #411 first. Retain the assets and reviews below as evidence for `5b2a62f`; regenerate and reassess them at the corrected candidate.

## Intent and release boundary

Intent: publish the completed context-consolidation batches as one versioned revision, so the downloadable role bundles and tagged adoption source include the approved changes already on main.

Observed candidate: `5b2a62f3b17aca1d859a43032b9ca2295c185391`, independently read from GitHub main and the clean source clone. Proposed tag: `v2026.11.10`. Baseline: published `v2026.11.04`, source `0ca563ee53c309840be4ab94dda74f9b075149ba`. The candidate is fixed; evidence documents created for this assessment are outside its source tree.

Observed: the release delta contains PRs #423, #424, #426, #429 and #432 plus self-adoption provenance and retrospective records. No additional backlog implementation is included. Local permission cleanup and GitHub issue closures from this conversation are not distribution assets.

Told: the user authorized preparation of this release package and a publish recommendation, not publication. Existing DEC-001680–001720 approve the five batches and their merges/self-adoptions; none grants this publication approval.

Inferred classification: consequential, because this is the first tagged publication of the new command-blocks and verification-checklists skill surfaces and their loading arrangement. The gate also follows this repository's explicit human-publication procedure in process/named-queries.md. This classification does not reopen the approved implementation decisions.

## Acceptance criteria and prior review coverage

Acceptance criteria: the approved individual ruling sets remain the content contract. Publish exactly twelve named role bundles plus README.md from the candidate; verify source identity and complete selected-content coverage; retain the reviewed native enforcement artifacts; report inherited defects and unverified behavior explicitly; obtain publication approval before creating the tag/release.

The approved subtraction SPEC and specs/rule-store.md AC-RS-10/12/13/14/15/16/16a/19 supply retirement, release-asset, selection, provenance, native-emission and adoption contracts. Later decisions explicitly amend their affected scopes. The original spec-close evidence is reviews/pkg-7-close-read-20261105T024910Z.md and reviews/pkg-7-close-amendment-read-20261105T033515Z.md; #417 records completed merge/publication of that earlier revision. No fresh spec or policy redesign is introduced here.

| Batch | Approval | Acceptance/test and independent review evidence |
|---|---|---|
| #423 — procedural skill extraction | DEC-001680 | docs/skill-context-extraction-evidence-20261105T220112Z.md; reviews/skill-context-extraction-read-20261105T215920Z.md |
| #424 — standing-rule pruning and skill-definition closure | DEC-001690 | docs/claude-rule-pruning-evidence-20261106T070025Z.md, including finalization addendum; reviews/claude-rule-pruning-finalization-read-20261106T073713Z.md |
| #426 — definition pruning | DEC-001700 | docs/claude-definition-pruning-evidence-20261106T194838Z.md; reviews/claude-definition-pruning-read-20261106T195037Z.md and ...195317Z.md |
| #429 — role/review/release consolidation | DEC-001710 | docs/review-verification-pruning-evidence-20261106T220757Z.md; reviews/review-verification-pruning-read-20261106T220413Z.md and ...amendment-read-20261106T222105Z.md |
| #432 — remaining approved role consolidation | DEC-001720 | docs/remaining-role-pruning-final-evidence-20261108T054145Z.md; reviews/remaining-role-pruning-final-evidence-read-20261108T055033Z.md |

Observed: prior tests and reads establish approved source/output contracts and adoption readback at their named revisions. They are not themselves approval to publish this combined revision. The combined independent release review is `reviews/release-consolidation-quality-read-20261110T230826Z.md`: overall, quality, skepticism and continuity are **ready-with-findings**. Quality/continuity and skepticism were performed by separate non-author reviewers. Its three non-blocking findings cover native behavior, inherited defects and stale spec status; all are carried in the risk table below. No new source blocker was identified.

## Implementation and architecture summary

Observed: instructions move from always-loaded roots into explicit on-demand skills; redundant rules/definitions retire into preserved history; role and workflow instructions consolidate; build owns the execution sequence and release owns one change package. Already approved writing changes through R1167 remain included; later writing work is deferred under DEC-001720.

Affected components: rule/process store, native skill-definition closure in three emitter modules, generated native roots/agents/skills, and standalone bundles. External dependencies are Git/GitHub for release transport and Claude/Codex/chat hosts for consuming context. No new deployed service, schema, credentials or data migration is introduced.

Observed: release script, rule parser, standalone renderer and hook implementations are unchanged from the published baseline; the executable adopter helper is unchanged (two surrounding prose references changed). Native hook/config bytes and modes are equal across fresh baseline/candidate emissions. This does not establish native enforcement or model adherence.

Boundary change in intended behavior: procedural content now relies on applicable skill invocation rather than constant root loading. Existing native-loading/adherence boundaries remain explicitly unverified; local file and test evidence does not cross them. Potential failure: an agent can omit a procedure despite correct files. Observe fresh sessions and inspect the resulting work; revert the coordinated source/generated context through normal review if the change causes unacceptable omissions.

## Fresh checks and artifacts

Test plan: rerun the full existing suite at the fixed candidate with required history present; stage the official named downloads through bin/release; inspect every selected row/definition against staged bundle content; compare fresh native outputs against the released baseline; retain hashes and read back current remote candidate/release state. These checks exercise existing acceptance contracts, without writing implementation-mirroring new tests.

Observed generation: bin/release completed from the clean candidate source with explicit proposed tag and an external output directory. It fetched origin/main and generated the twelve bundles. README was copied byte-for-byte from that candidate into the staging directory. No printed publication command was executed.

Staged downloads: `docs/releases/v2026.11.10/assets/` (13 files), copied with hash verification from the original `/tmp/fiducial-release-20261110/assets/` generation. Durable audit: `asset-audit.json` and `SHA256SUMS` beside this package. `generation.log` retains the generator result. The manifest is evidence, not a fourteenth release asset. These local preparation artifacts are outside the fixed candidate commit and are not silently included in tagged source.

Observed asset checks:

- Exact asset-name set equals the twelve entries in process/named-queries.md plus README.md.
- Every bundle header names davepierceops/fiducial and the complete candidate SHA; README equals the candidate Git blob.
- Every nonempty selected rule/process body and pulled definition is present in its respective bundle, respecting omission of enforcement blocks. These are output/content checks using the source query and block parser, not independent verification of every semantic selection decision.
- Both native layouts generated successfully. Eight Claude hook/config files and nine Codex hook/config files match baseline bytes and modes.
- The two independent reviewers separately read all 13 hashes/headers/README and checked native enforcement equality.

Observed first suite run: 339 tests, one failure, in 125.929 seconds; repeat adoption produced writes when none were expected (`tests-initial.log`). During that run the preparation session changed the source clone's origin from the local clone path to GitHub. Inferred hypothesis: differing provenance between successive emissions caused the failure; that root cause is not proven by a passing rerun. No implementation/test change was made.

Observed targeted recheck with stable origin: the affected real-emission/repeat-adoption test passed, 1 test in 5.523 seconds (`adoption-repeat-recheck.log`). Fresh full stable-source rerun: **339 tests passed in 124.128 seconds, exit 0, no skips reported** (`tests-stable.log`). `test-source-state.json` verifies identical before/after candidate SHA, GitHub origin and clean working state. This closes the current test-result gap without claiming the first-run cause is proven.

## Measured user-visible changes

Observed measurements compare fresh generation from the release baseline and candidate, not historical intermediate batches. Counts are physical lines and whitespace-delimited words, not tokens or measured cost.

- Native roots: each 293 → 45 generated lines and 4,171 → 585 words (about 86% fewer root words). Installed ownership wrappers add their own lines/words.
- Chief of Staff standalone bundle: 10,868 → 9,421 words.
- Ten of twelve standalone bundles shrink. Architect grows 3,733 → 3,875; Writer grows 4,905 → 5,021. Complete per-role figures and source coverage counts are in asset-audit.json.
- No measured claim of improved model outcomes, lower total billed tokens, or stronger live enforcement is made.

## Known gaps, release impact and mitigations

Inferred release dispositions below are proposed for the human's publication decision. `deferred` records unfinished verification/work; it is not already accepted risk. No current source defect has been silently waived. Existing non-blocking/file-and-land classifications are evidence of prior dispositions, not automatic new publication approval.

| Gap / evidence | Proposed release impact | Practical mitigation and follow-up |
|---|---|---|
| Native skill loading, selection, invocation/adherence and hook trust/enforcement are unverified in a fresh amended target session. | deferred; explicit publication risk decision | Invoke installed skills by name when needed, inspect work/evidence, and record target-specific loading/enforcement checks during the next adoption or meaningful harness change. Owner: adopting session. Correct files cannot prove future model behavior. |
| #411: adoption can change an existing shared file from 0600 to 0644. Executable helper unchanged. | blocking; fix before publication | Defer adoption into repositories with restrictive shared-file modes until the defect is fixed or a separately reviewed preservation procedure is available. A later chmod does not eliminate transient permission widening. Publication itself does not apply adoption anywhere. Owner: adopter-maintenance change. |
| #412: a destination becoming a directory after preparation can cause partial writes. | deferred; explicit publication risk decision | Keep the target idle/exclusive between prepare and apply; inspect planned destination types before apply. If apply fails, stop and inspect/recover partial changes rather than retrying blindly. This mitigation is not a transactional guarantee. Owner: adopter-maintenance change. |
| #416: installed skills retain source process/ references absent from adopted repositories. | deferred; explicit publication risk decision | Follow the corresponding installed skill by name; if it cannot be located, stop that procedure. Automatic runtime recovery is untested. Owner: next emitter-portability change. |
| #415: push-readback misses cmd payloads and truncates qualified refs. | deferred | Explicitly read the actual remote ref after every push. A silent hook result is not confirmation. Owner: next hook-maintenance change. |
| #358: selective citation labels/missing-target rejection unfinished; #365: empty-body validation unfinished. | deferred | Current assets receive source-content checks and reviewer reads; no blanket self-contained-reference or malformed-input safety claim. Owner: separate generator fixes. |
| #366: whole-tree release dirty check and local-edit provenance limitations; #381: printed publication command lacks explicit repository and independent body checks. | not-material to this pinned preparation with stated controls | Use a clean fixed source, verify manifest/body coverage, and use explicit davepierceops/fiducial repository when publishing. Do not run the bare printed command from an arbitrary directory. Source tools remain unchanged. |
| Current SPEC.md still says the earlier subtraction merge is pending; #417 records completion. | not-material to candidate identity; documentation follow-up | Cite #417 and the exact merge/release as completion evidence; preserve the old decision records. Correct current spec wording through its normal reconciliation, not by pretending it was updated here. |
| Four baseline source-lint singleton warnings and the #427 execution-report/verdict-hook mismatch. | not-material to this release delta | Retain their prior evidence/dispositions. No claim of a universally clean lint run or a fabricated reviewer verdict for execution reports. |
| Full suite depends on historical Git objects; no live/browser effectiveness trial. | deferred | Run tests from a clone retaining required history; don't claim source ZIP/shallow-clone test sufficiency. Observe actual adoption/use before making runtime or effectiveness claims. |

SLO status/error-budget consumption: no production service or measured SLO was exercised. specs/rule-store.md explicitly leaves its journey SLOs unverified. No healthy-budget or production-verified claim is made. This package does not alter those boundaries; #428 remains separate.

## Operations, rollback and publication controls

Observed: source staging is isolated and remains at the candidate; original checkout retains the uncommitted reconciliation/evidence files. No user settings were read into release assets, and the local four-permission cleanup is absent from the published Git source.

Proposed publication: tag the exact candidate and attach only the 13 verified downloads, with the release notes in this directory. Recheck candidate main and tag absence immediately before publication. If either changed, stop and reconcile evidence. After publication read back tag SHA, release state and each asset's name/size/digest before claiming completion.

Rollback/mitigation: consumers can remain pinned to v2026.11.04. If the new context proves unsuitable, prepare a reviewed correction/revert and release a new tag, preserving historical tags and evidence. Adoption rollback must use its reviewed reconciliation and inventory; do not overwrite unrelated target context.

Human gate: [#433](https://github.com/davepierceops/fiducial/issues/433), open with `human-gate` label and exact derived body verified by a fresh GitHub read. No GitHub release or tag has been created. The gate follows `.agents/skills/gate/SKILL.md`; publication requires the human's explicit go.

## Release readiness

Recommendation: **needs the human decision**.

Proposed decision: publish the pinned consolidation with the deferred gaps above explicitly accepted for this release, while leaving further backlog and writing-policy work for later. The fresh full-suite result and independent aggregate review are complete. The existing batch “ship” recommendations refer to their authorized merges, not this publication. Public tag, release and upload remain pending the human's go and the immediate prepublication checks.
