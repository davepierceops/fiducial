# Review: release-consolidation — quality-read-20261110T230826Z

Verdict: ready-with-findings
Reviewed: proposed v2026.11.10 source @ 5b2a62f3b17aca1d859a43032b9ca2295c185391; docs/releases/v2026.11.10/release-package.md, release-notes.md and retained evidence/assets as read 2026-11-10
Baseline: published v2026.11.04 source @ 0ca563ee53c309840be4ab94dda74f9b075149ba
Reviewer: reviewer-agent /root/release_quality (quality and continuity; artifact author); skeptic-risk-agent /root/release_risk (separate skepticism pass, explicitly attributed below). Neither authored the source changes or release package.
Date: 2026-11-10
Scope: aggregate source and generated-output delta, approval/review coverage, current test evidence, all thirteen prepared downloads, native enforcement equivalence, publication limitations and continuity. This is a publication-readiness read, not a repeat of every original batch review.
Cross-checked: DEC-001660–001720; SPEC.md; specs/rule-store.md; process/named-queries.md; the five batch evidence/review chains named below; prior adopter and subtraction-close findings; current release package, notes and draft gate-request.md.
Not inspected: fresh native host loading, skill invocation/adherence or live hook trust/enforcement; adoption into another repository; live/browser comparative effectiveness; actual new tag/release transport or postpublication asset readback; production SLO/error-budget health. The reviewers inspected the parent's current full-suite result rather than independently rerunning that suite. GitHub gate/release state reported in the package was not independently reread by the quality reviewer.
Findings: 3 non-blocking (S1 boundary follow-up suggestion, S2 inherited defects, C1 stale current spec status); no demonstrated new source defect or blocking finding.
The human should inspect: the deferred native-behavior boundary and #411/#412/#416 mitigations, and the exact candidate/thirteen-asset boundary, before explicitly accepting residual publication risk. Prior merge approvals are not publication approval.

Observed: this read used the verification-checklists, review-artifact and command-blocks skills. Quality, skepticism and continuity were all completed; no planned review pass is represented as not-run. The two reviewers' scopes and executions remain distinguished below.

## Quality

Verdict (quality): ready-with-findings

Author: reviewer-agent /root/release_quality.

Observed: DEC-001680, DEC-001690, DEC-001700, DEC-001710 and DEC-001720 record the five batches' approved ruling sets and authorized merge/self-adoption scopes. The final source/emitter/hook state has no subsequent change between the last reviewed source pin df8d789 and candidate 5b2a62f. The preceding #419–#422 range contains retrospective/review records and self-adoption provenance/ownership changes under DEC-001670, not another unreviewed policy/tool change.

| Batch | Evidence and independent review cross-checked | Coverage relevant to publication |
|---|---|---|
| #423 | docs/skill-context-extraction-evidence-20261105T220112Z.md; reviews/skill-context-extraction-read-20261105T215920Z.md | Exact procedural extraction, scoped skills, native/bundle output and adoption readback; native behavior explicitly deferred. |
| #424 | docs/claude-rule-pruning-evidence-20261106T070025Z.md; reviews/claude-rule-pruning-finalization-read-20261106T073713Z.md, including post-apply addendum | Approved retirements/successors, process-skill definition closure, all installed writes and empty repeat plan. |
| #426 | docs/claude-definition-pruning-evidence-20261106T194838Z.md; reviews/claude-definition-pruning-read-20261106T195037Z.md and ...195317Z.md | Definition retirements and retained terms; exact installed output and repeat no-op. |
| #429 | docs/review-verification-pruning-evidence-20261106T220757Z.md; reviews/review-verification-pruning-amendment-read-20261106T222105Z.md | Workflow consolidation, corrected original role audience and retained root definitions; inherited #427 disclosed. |
| #432 | docs/remaining-role-pruning-final-evidence-20261108T054145Z.md; reviews/remaining-role-pruning-final-evidence-read-20261108T055033Z.md | Final ruling/retirement state, all 33 installed writes, 66-file inventory/65 generated files, no-op repeat, and the deferred writing-work boundary. |

Observed: aggregate executable changes are limited to process-skill definition closure in common.py, claude_code.py and codex.py. Hooks, native security configuration, the executable adopter helper, standalone renderer, parser and release script retain baseline behavior. Process/build, release, gate, review-artifact and spec-template changes are covered by the approved scope/review chain. Existing tests cover exact retired originals, scope preservation, current and historical selections, retained security anchors, and definition closure. The definition-closure fixture had a documented meaningful failing preimplementation case; the current guards were not weakened to obtain a green result. Historical Git objects are a real suite dependency.

Observed verification performed independently by the quality reviewer:

- Read all thirteen staged files and checked the exact asset set, SHA256 values and byte counts against asset-audit.json. Checked every bundle's full candidate provenance and word count; checked README against the candidate Git blob. Rechecked all thirteen durable copies under docs/releases/v2026.11.10/assets against the same hashes.
- Compared baseline/candidate fresh native outputs: all eight Claude and nine Codex hook/configuration files have equal bytes and modes. Read the candidate root and verification-checklists skill, including the retained approval/security anchors and procedure definitions.
- Inspected the parent's durable tests-stable.log: 339 tests in 124.128 seconds, OK, with no skips reported. Inspected test-source-state.json: before/after candidate SHA, GitHub origin and clean working state are identical; exit code is zero.
- Inspected the first-run failure and the isolated repeat-adoption rerun (1 test, 5.523 seconds, OK). The parent reports changing origin during the initial run. Provenance drift is a plausible explanation, not a proven diagnosis; the package correctly preserves that distinction.

Observed evidence hashes: tests-stable.log `d435c4140b1d4b22b4e39465493940dc8ba780ddddde249063386fe353cfd519`; test-source-state.json `5342dc6f0260ebe1c9676ae47d6a271a6ec3357e0eff0d7975c68181cd35dd7b`; asset-audit.json `82b2262ad7bf27589f76c70d39aaa0dabbfdf67faefc754321d25b1c7a4034f4`; SHA256SUMS `468de11016026d730167fe2389156db696dfd0617437e2b62e07b6bb1b9d6ffb`.

Observed boundary: the package's selected-body audit uses the source query/block parser, so it is not independent proof of every semantic selection decision. The prior ruling-by-ruling independent reads supply that complementary evidence. Adoption fixtures use stand-in approval records; they verify machinery, not real human authorization or native runtime enforcement. The full suite and aggregate checks are proportionate to packaging already reviewed changes; no new implementation-mirroring tests were needed.

Observed: the notes report actual final-baseline measurements. Ten bundles shrink; Architect grows from 3,733 to 3,875 words and Writer from 4,905 to 5,021. The root reduction is a file-size measurement, not evidence of better model outcomes, lower billed cost or stronger enforcement.

## Skepticism

Verdict (skepticism): ready-with-findings

Author: skeptic-risk-agent /root/release_risk. This completed separate pass was delivered to the artifact author; the findings below preserve its attribution and scope.

Observed by that reviewer: independently executed all thirteen asset hash/header/README checks and byte/mode comparisons of the seventeen native enforcement files; independently read the aggregate diff and confirmed unchanged hooks/configuration, bin/release, store.py and render.py, with native emitter changes limited to process-skill definitions. Cross-checked DEC-001680–001720 and prior batch evidence/reviews. Read the final package/notes, durable 339-test passing result and stable before/after source-state record. The suite itself was run by the parent, not rerun by this reviewer. No newly introduced source defect was demonstrated. The passing stable rerun closes the current result gap without proving the initial failure's cause.

### S1 — non-blocking

Claim: Observed, the on-demand procedure arrangement is locally verified while fresh-session loading, invocation/adherence and native trust/enforcement remain unverified.
Classification: suggestion
Location: docs/releases/v2026.11.10/release-package.md, Implementation and architecture summary / Known gaps; extraction and subsequent batch evidence.
Evidence: Exact generated contents and unchanged seventeen enforcement files were independently checked; prior explicit deferrals were read; no fresh live evidence was supplied.
Consequence: Inferred, an adopted agent can omit a required procedure even when emitted files are correct.
Fix: Carry the explicit deferred risk into the publication gate, invoke installed skills by name and inspect work, and record target-specific checks during adoption. Release impact: deferred, awaiting this publication risk decision; prior merge approval is not acceptance of it for publication.

### S2 — non-blocking

Claim: Observed, previously demonstrated adoption, reference, validation and readback defects remain in distributed source; the package accurately carries them forward.
Classification: defect
Location: release-package.md, Known gaps; issues #411, #412, #416, #415, #358 and #365; reviews/pkg-5-adopter-read-20261105T011244Z.md and reviews/pkg-7-close-read-20261105T024910Z.md for the adoption/readback/reference probes.
Evidence: Relevant implementation is unchanged in the aggregate diff; the prior evidence and current output read support continued limitations, not newly demonstrated defects.
Consequence: #411 can transiently broaden shared-file read permissions; #412 can leave partial installation; #416 can direct an adopter to absent source paths; #415 can supply no useful remote-equality evidence; #358/#365 lack generic citation and malformed-body guarantees.
Fix: Honor the package's mitigations and separate fixes. Defer adoption of restrictive-mode shared files until preservation is fixed or separately reviewed; a later chmod does not prevent transient widening. Keep adoption targets exclusive and inspect partial failure without claiming transactions. Use corresponding installed skills and directly inspect actual remote refs after pushes. Current exact-asset checks mitigate this candidate, not all future malformed input. Release impact: deferred; #411/#412/#416 explicitly require the publication risk decision, with no new acceptance implied here.

Observed risk dispositions: #366/#381 are not-material to this pinned preparation with clean source, independent asset/body audit and explicit repository selection for future publication. Their source limitations remain. The four baseline singleton warnings and inherited #427 execution-report/verdict mismatch are not-material to this delta; no universally clean lint claim or fabricated execution-report review verdict is made.

Observed assessment boundaries: correctness, usability, security/privacy (#411), reliability/recoverability (#412 and pinned rollback), maintainability/reference integrity, and dependency/provenance risk were assessed. Performance/cost improvement is unmeasured. No production service was exercised, and the package explicitly leaves journey SLOs/error-budget health unverified. No production-verified claim is made.

## Continuity

Verdict (continuity): ready-with-findings

Author: reviewer-agent /root/release_quality.

Observed: the aggregate package traces approved scopes to source, tests, historical independent reads and actual downloads. It retains deferred writing/definition/SLO work instead of reopening it. It distinguishes historical merge readiness from publication readiness and reports inherited defects with release-impact labels and practical limits. The final suite result, notes and retained manifests agree. Administrative addition of this review link/verdict and a subsequent gate reference does not change the reviewed source/asset boundary; any candidate, asset-byte or material scope change needs a new read.

Observed: the draft gate-request.md carries the same candidate, thirteen-asset boundary, current test result and deferred-risk decision. It clearly states that local preparation evidence is outside the candidate and not yet committed, rather than presenting nonexistent remote evidence links. It reserves publication and upload for the human's go and requires immediate prepublication state checks and postpublication readback.

### C1 — non-blocking

Claim: Observed, current SPEC.md still describes the earlier subtraction close/merge as pending, while the release package identifies #417 and published v2026.11.04 as its completed closure.
Classification: defect
Location: SPEC.md frontmatter status and section 6 unchecked final-review/human-merge criterion; release-package.md, Acceptance criteria / Known gaps.
Evidence: The stale text is directly present at the candidate. DEC-001660 records the earlier pre-merge state; the package's current completion evidence is #417 and baseline 0ca563ee53c309840be4ab94dda74f9b075149ba. The quality reviewer did not independently reread the remote gate in this pass.
Consequence: A reader of the current spec can incorrectly infer that the previous revision's close gate is still outstanding. Completion evidence does not repair that current-reference drift.
Fix: Reconcile current spec status through its normal workflow while preserving historical decisions. Until then use the package's explicit discrepancy and actual completion reference. Release impact: not-material to candidate identity or the reviewed consolidation contracts; not represented as corrected here.

Inferred conclusion: the source/output evidence supports presenting this pinned publication for the human decision, with the disclosed deferred risks. No source-policy blocker was identified. Recommendation: needs the human decision. Ready means ready for approval; this artifact neither approves nor performs publication.
