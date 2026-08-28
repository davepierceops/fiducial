You are the Spec Reviewer Agent, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Carry out the cycle-23 confirmation gate over specs/directive-tooling.md @ d3ab472517068a4c13796bd2b7de964755995b2f on branch directive-tooling-prd-rewrite (PR #225, base main @ ed46f40429e478189b1e6cabf5528b99df70d3a0). You authored nothing under review.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-prd-rewrite-gate-20260828T0950.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: cycle-23 confirmation gate for directive-tooling PRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-prd-gate2", created by: git worktree add "$TMPDIR/fiducial-dt-prd-gate2" directive-tooling-prd-rewrite
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-prd-rewrite, stop and report. Do not touch the main tree.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-prd-rewrite and local directive-tooling-prd-rewrite must be at d3ab472517068a4c13796bd2b7de964755995b2f. If either has moved, stop and report.

SCOPE — confirmation, not a full re-review:
1. For each cycle-21 finding B1–B4, N1–N5, O2–O4: confirm the fix landed as dispositioned. Dispositions are in docs/cycles/directive-tooling-prd-rewrite-fix-20260828T0940.md (read whole); findings and Fix fields are in reviews/directive-tooling-cycle-21.md (read whole). O3 is accept-in-part: resolution mechanism restored, quote-whole obligation deliberately not — its absence is not a finding.
2. O1: confirm frontmatter is exactly status: draft, last-reviewed: null, audience: [human], unchanged from 0b5a6d4e. The audience value is Dave's recorded ruling; do not re-litigate it.
3. Register check over the diff 80e5337..d3ab472: no reintroduced provenance tags, cycle-by-cycle changelog prose, closed questions, or per-citation SHAs.
4. Internal consistency of the edited sections only (§1, §4, §5, §6 preamble, AC-DT-06, AC-DT-13, G10, §7, Q9), including the executor's disclosed choices: the nested pairing of the two M3 fence residuals in §7, the §7 Accepted ordering, and the literal fixture paths in AC-DT-06's M8 set.
5. Re-verify by running any restored factual claim against its source where the source is in this repository.
New findings only where an edit introduced a defect or a dispositioned fix did not land. Do not reopen matters cycle 21 did not raise.

ARTIFACT: reviews/directive-tooling-cycle-23.md per skills/review-artifact.md — Reviewed: specs/directive-tooling.md @ d3ab472; Prior cycle: reviews/directive-tooling-cycle-21.md (cycle 22 was the fix cycle and produced no review artifact). A clean confirmation is the header and nothing else. Commit it alone with message "Spec Reviewer gate cycle 23: directive-tooling PRD — <verdict>", push.

SCOPE OF WRITES: this session creates exactly two files — its directive file and the review artifact — and modifies none. No ref creation or deletion, no merge.

CLEANUP — after the report is composed and both pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-prd-gate2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed, so the session can be closed without leaving a claim on the branch.

STOP CONDITIONS, pinned to reviewed ref d3ab472517068a4c13796bd2b7de964755995b2f: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; review-artifact commit SHA; the verdict line; finding count by severity if any; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
