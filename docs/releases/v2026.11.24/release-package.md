# Fiducial v2026.11.24 — change package

Status: prepared; not approved, not published. Classification: consequential (Dave, 2026-11-24). Waits for his explicit go.
Candidate: `35713889a46f4defda57b705ff43a8694aadff12` (main, PR #455 merge). Baseline: published v2026.11.10, `a8d87bc95afed9f5ac8b54fe2c8863013ce10265`.
Proposed tag: `v2026.11.24`. Date basis: America/Los_Angeles, as for v2026.11.10. At preparation it was 2026-11-24 15:57 Pacific, which is 2026-11-24 23:57 UTC; generation ran after UTC midnight, so the bundle header timestamps read 20261125. `process/named-queries.md` does not say which zone; on a UTC reading the tag is `v2026.11.25`. The tag appears only in the printed `gh release create` command, not in the bundles, so renaming costs nothing. Observed: the tag is absent on origin (`bin/release` checks it).

Intent: publish the batch merged since v2026.11.10 so the downloadable bundles and tagged adoption source carry it: adopter preflight and hook/skill-reference fixes, generator and release-tool hardening, the `+local` header marker, the gate fallback, SLO conditionality on Production SLOs, and the repeatable `probe` skill.

Acceptance criteria: told, from the approvals in `decisions/log.md`: DEC-001770 (#441), DEC-001780/001790/001800 (#443), DEC-001810 to 001840 (#447, decisions only), DEC-001860 to 001910 and 001920 (#448 decisions, #451 implementation), DEC-001930 (#452), DEC-001940 to 001970 (#455). #445 adds two redacted review artifacts (Wayfinder adoption); no decision entry covers it that I found (unknown whether one is needed; it changes no bundle content). Release contract: exactly twelve bundles named in `process/named-queries.md` plus README.md, each headed with the candidate SHA, no `+local` marker.

Test plan: the existing suite at the candidate, from a full-history clone; asset audit of the staged output; grep for the batch's wording. Spec-close review artifacts are the per-change reads: `reviews/adopter-hook-portability-read-20261111T060428Z.md`, `reviews/generator-hook-defects-reread2-20261111T180211Z.md`, `reviews/batch-rulings-20261123-read-2-20261124T164451Z.md`, `reviews/followups-442-read-20261124T172909Z.md`, `reviews/probe-skill-read-3-20261124T222600Z.md`.

Implementation summary: observed from `git diff --stat a8d87bc..3571388` (38 files outside reviews/docs/decisions, +1,975/-76). Adopter refuses destinations that became directories or are not writable before its first write (#412); push read-back keeps slash branch names and reads Codex `cmd` payloads (#415); emitted skills reference each other in the harness's own form and emission fails on a dangling reference (#416); store refuses a rule with no instruction or an HTML-comment-only body; `bin/release` names the repository in its printed command, checks bundles for selected and retired text, scopes cleanliness to generation inputs and blocks on gitignored inputs; bundle header carries `+local.<hex>` when rendered from uncommitted inputs (release assets never do); gate fallback (DEC-001820) in R0558 and `process/gate.md`; SLO clauses in R0129, R0502, R0863, R1032, R1041, R1107, R1143, R1183, the checklist and the spec template conditional on a Production SLOs subsection; new `process/probe.md`, emitted as a `probe` skill to Claude Code and Codex; release and adopt processes require citing the latest probe report.

Test results: observed, `bin/tests/run` at `3571388` in a full-history, non-shallow clone with a clean tree: `Ran 464 tests in 195.000s`, `OK`, exit 0; no skip lines in the log (`tests.log`; baseline was 349). Observed: `bin/release --tag v2026.11.24 --out <tmp>` exit 0, twelve bundles generated; the printed publication command was not run (`generation.log`). Evidence-sufficiency: sufficient for the contract that local generation, adoption and hook code behave as tested; insufficient for any live-harness claim (below).

Asset audit (observed; `asset-audit.json`, `SHA256SUMS`, `assets/`): names equal the twelve `process/named-queries.md` entries plus README.md; all twelve headers read `davepierceops/fiducial @ 35713889a46f4defda57b705ff43a8694aadff12`; no `+local` marker; README sha256 `58b4be16...fcfaa` equals the candidate blob. README is attached from the repository root by the printed command, so it is not in the generated output directory; the copy in `assets/` is a byte-equal copy. Not re-run: the per-row source-coverage audit of v2026.11.10; `bin/release` itself now refuses a bundle lacking a selected row or carrying retired text, and it exited 0.

Grep evidence in the staged bundles (observed):
- "Production SLOs" appears in all twelve bundles (1 to 6 hits each); the change-package line reads `SLO status and error budget consumption: <affected Top K journeys where the spec has Production SLOs; otherwise N/A>` in chief-of-staff, release-manager, reviewer and skeptic bundles. The old unconditional template line is absent from all twelve (0 hits); test-designer's "and SLO verification for each affected Top K user journey" is now "where the spec has a Production SLOs subsection, add SLO verification ...".
- "cannot be opened": the gate fallback ("If the issue cannot be opened, present its derived body in chat ... The human's explicit go in chat then releases the change") is in chief-of-staff (2 hits) and release-manager (1). The old step 2 "Before presenting the change, confirm that the issue is open and linked" and old step 1 text are absent, replaced by "Where the issue can be opened, confirm ...".
- Probe: chief-of-staff bundle contains `# Process: Probe` (line 1232) and the probe-report citation in the release template (line 390) and the adoption step (line 770).

Verification boundary status and updates: this release adds a live-verified evidence class (the probe) and changes how a consequential change is authorized. Nothing live is verified. Contract-verified only: file generation, adoption/hook code paths under test, bundle content. Unverified: native skill loading and invocation in a fresh Claude Code or Codex session; hook trust and enforcement; that the `probe` skill works when run; that the Codex deny rules enforce (see #453). The first probe runs after adoption of this release (DEC-001970; #439 stays open). Release-impact label: deferred; named path is the probe run per harness after adoption.

SLO status and error budget consumption: N/A (DEC-001900; fiducial's `SPEC.md` has no Production SLOs subsection).

Review findings: per-change reads listed under the test plan, each with Dave's approval in the log. Dispositions are in those DEC entries and issues #440, #450, #453, #454. Combined non-author read of the whole `a8d87bc..3571388` delta and this package: `reviews/release-candidate-20261124-read-20261125T221408Z.md`, changes-required on B1 only (the gate was not opened for a false reason). B1 is fixed by opening #456. N2 (the DEC-001850 reword) is carried in Known gaps and #364, and N3 and N6 are corrected here. N1 is added to the gate request. N4, N5 and N7 and observations O1 and O2 are filed to #450. O3 (tag date basis) is for Dave.

Known gaps:
- #453: Codex list-form deny rules gap (deferred; the Codex probe cannot show deny enforcement for that form).
- #454: filed from probe read 2 (N2); open.
- #450: non-blocking findings from batch-rulings, followups-442 and probe reads (F1, F3, F5, F6 and two observations); open.
- Native loading, adherence and hook enforcement unverified (carried from v2026.11.10).
- From the v2026.11.10 list, selective citation labels moved into #362 (#358 closed as its duplicate on 2026-11-23). `process/named-queries.md` "A release is cut on the human's go" is not reworded per DEC-001850 (#364 open); it ships in the bundles and is accurate for this consequential release. Release impact: deferred.
- No probe report exists; the `adoptions/` folder does not exist yet.
- Fiducial's own installed context is pinned to v2026.11.10 (DEC-001760) and does not yet carry this batch; #446 (reopened 2026-11-25 after the PR #451 merge closed it) and #449 stay open until self-adoption after release.
- Test suite needs full git history; ZIP or shallow-clone verification is insufficient.
- Date-basis ambiguity for the tag (above).

Operational notes: publishing attaches README plus twelve bundles; existing adopters are not updated automatically and may stay pinned to v2026.11.10. Adoption of the new tag is a separate reviewed step and the first probe follows it. Bundle sizes changed (chief-of-staff about 11,278 whitespace-delimited words against the 9,421 reported at v2026.11.10, mostly the new probe process); a size measurement, not an effectiveness claim.

Human gate: #456 (`human-gate`), opened 2026-11-25 by REST. The earlier "not opened" stated the session's instruction, not unreachability, so the DEC-001820 fallback did not apply (combined read B1).

## Release readiness

User-visible behavior: adopters on the new tag get the preflight refusals, correct push read-back and skill references, the `+local` marker on locally rendered bundles, the gate fallback and conditional SLO fields, and a `probe` skill. Bundle consumers get regenerated bundles. Nothing changes in running systems; fiducial is a methodology repo.

Live/browser verification status: N/A for browser. Probe: none run; no report exists under `adoptions/` for this repository or either harness. First probe is planned after adoption (DEC-001970).

Operational risks: (1) DEC-001820 changes how a consequential change is authorized, and its fallback is contract-checked text only; (2) the probe skill is unexercised, so its checks and throwaway-target guard (DEC-001940) are unproven; (3) the Codex deny gap (#453); (4) adoption changes (preflight) are tested locally, not against a real adopted repository; (5) no combined delta read.

Rollback or mitigation path: consumers stay pinned to v2026.11.10. If the batch proves unsuitable, correct or revert through reviewed change and cut a new tag; do not move or delete the published tag. Adoption rollback uses the reviewed reconciliation and inventory.

Release recommendation and human decision points: **needs the human decision**. Not a "do not ship": no blocking defect found, tests pass, assets audit clean. Points for Dave: (a) explicit go or no-go (consequential; required); (b) accept the deferred gaps above, notably #453 and the unverified probe, as release risks; (c) whether the per-change reads suffice or a combined non-author read of the delta is wanted first; (d) tag date basis (`v2026.11.24` Pacific vs `v2026.11.25` UTC); (e) whether #445 needs its own decision entry.
