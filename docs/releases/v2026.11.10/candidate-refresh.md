# v2026.11.10 candidate refresh — 2026-11-11 UTC

Status: candidate regenerated with the #411 fix. Publication is not approved and not performed. Gate: #433.

This file is the current reference for the candidate. `release-package.md`, `gate-request.md` and `session-handoff.md` describe the previous candidate `5b2a62f3b17aca1d859a43032b9ca2295c185391` and are kept as history; files suffixed `-5b2a62f` are that candidate's evidence, including its failing first test run and targeted recheck.

Independent read of this refresh: `release-candidate-20261111-read-20261111T042500Z.md` (ready-with-findings; its blocking finding F1, a stale review claim in the release notes, and F2–F4 are corrected in the commit that added it).

## Candidate

- Observed: candidate is main at `a8d87bc95afed9f5ac8b54fe2c8863013ce10265`, read back from origin after PRs #434 and #435 merged. Clean tree, HEAD equal to `origin/main` before and after the test run (`test-source-state.json`).
- Observed: `git diff 5b2a62f a8d87bc -- rules process bin/hooks bin/rulestore bin/bundle bin/release README.md` changes one file, `process/adopt.md` (8 insertions, 3 deletions). The rest of the delta is tests, reviews, the plan, the self-adoption refresh of fiducial's own installed context, and DEC-001730/001740.
- Told: Dave approved the #411 fix, the manifest fix in the same change, and the triage of the non-blocking findings (DEC-001730, DEC-001740). Neither entry approves publication.

## What #411 changed

- An existing Markdown or JSON file, including `.claude/fiducial-ownership.json`, keeps its mode through adoption; a new file takes the generated mode.
- Observed before the fix: existing 0600 `.claude/settings.json` and `CLAUDE.md` became 0644, and a repeat run with no content change re-widened them.
- Observed after: ten regressions in `bin/tests/test_adopt.py`; five failed on the unfixed code and pass now, five guard existing behaviour.
- Reads, each by an agent that wrote none of the work: `reviews/adopter-preserve-modes-read-*` and `reviews/adopter-preserve-modes-adoption-read-20261111T040500Z.md` on main.

## Fresh evidence at the candidate

- Observed: `bin/release --tag v2026.11.10` completed from the clean candidate and generated twelve bundles (`generation.log`); README.md was copied from the candidate and equals its Git blob. The printed publication command was not run.
- Observed: full suite, 349 tests, OK, exit 0 (`tests-stable.log`, SHA256 `967dc760aa9d058d063ceeb83b2c252dcffb53942caa64f249bb6cbc643a983a`). The count is ten higher than the previous candidate's 339: the ten new adopter tests.
- Observed: 13 assets match `SHA256SUMS` (SHA256 of the manifest: `25a3a26bbb4dbe41e906bf7e11d533eacd8f1eaa1dd6fcfef6643c0ebdec1ffb`).
- Observed (`asset-audit.json`): the asset-name set is the twelve named bundles plus README.md; every bundle header names the candidate SHA; no asset mentions the previous candidate SHA.
- Observed: compared with the previous candidate's audited assets, README.md is byte-identical; eleven bundles differ only in the header line's commit and generation timestamp; `fiducial-bundle-chief-of-staff.md` additionally carries the `process/adopt.md` change and nothing else.
- Inferred, not re-run: the previous candidate's per-row source-body coverage audit and the native hook/config equality check against v2026.11.04 carry forward, because selection, renderer, hooks and every selected body other than `process/adopt.md` are unchanged between the two candidates. The audit script itself was not available to re-run.
- Observed: the two remaining-role-pruning finalization tests now compare the #432 merge commit `5b2a62f` to the approved preview instead of the working tree; they assert that batch as landed, not this candidate's `process/`.
- Observed: the self-adoption refresh on main wrote five files byte-identical to its staged candidate, and a repeat prepare planned no changes (`reviews/fiducial-adopter-preserve-modes-adoption-report-20261111T040241Z.md` on main).

## Known gaps

Unchanged from `release-package.md`'s table except:

- #411: fixed at this candidate. No longer a publication blocker.
- #412: still open, `deferred`. One more observed case recorded there: a read-only (0400) file that needs a content write fails partway through apply.
- Not verified here: non-POSIX filesystems; adoption into a real target repository with restrictive modes; native skill loading, adherence and hook enforcement (unchanged boundary).
- This run used a Linux sandbox clone with fetched history; the previous candidate's evidence was produced on Dave's Mac.

## Open before publication

- The tag name. `v2026.11.10` is the proposed tag from the earlier package; the date form names the release day, and it is now 2026-11-11 UTC. The tag is chosen at the publication decision.
- Explicit publication approval on #433, then the prepublication checks in `release-package.md`: candidate still equals main, tag absent, read back tag SHA and asset digests after publishing.
