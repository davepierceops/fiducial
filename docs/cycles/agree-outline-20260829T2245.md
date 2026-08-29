You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: doc-only agreement of skills/outline.md — one log entry, then one frontmatter-only flip — as two commits.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit 9d3fe853655880c27542292c277b60c91e4037dd (git merge-base --is-ancestor 9d3fe853655880c27542292c277b60c91e4037dd origin/main exits 0); if not, stop and report. Record origin/main's SHA for your report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-agree-outline", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-agree-outline" -b agree-outline origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named agree-outline, stop and report. Do not touch the main tree's checkout.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/agree-outline-20260829T2245.md in the worktree, commit it alone with message "Directive: doc-only agreement of skills/outline.md", push with git push origin agree-outline, and report the SHA.

PRECONDITION: skills/outline.md in the worktree reads status: draft and last-reviewed: null; if not, stop and report.

EDIT 1 — reviews/expedited-log.md. Append the following line verbatim as the last entry of the file, after the last existing entry (the roles/critic.md entry), changing nothing else:

- 2026-08-29 — skills/outline.md @ cfe9977a1c88d91b17d7bb05f76c2ccc513edf64 — new: the Writer's outline procedure — topics inventory with author prioritization, thesis, tier-tagged claims list, section plan on request only; agreed via doc-only cycle (DEC-000230)

Commit reviews/expedited-log.md alone with message "expedited-log: skills/outline.md agreed via doc-only cycle". git push origin agree-outline.

EDIT 2 — the flip. Run bin/flip-agreed once, as a single standalone invocation (never inside a loop), for skills/outline.md with the review pointer exactly:
reviews/expedited-log.md @ cfe9977a1c88d91b17d7bb05f76c2ccc513edf64
The tool commits on its own. Verify before pushing that the flip commit touches only skills/outline.md and only its frontmatter (git show --stat and git show on the commit; the diff is status: draft → status: agreed and last-reviewed: null → last-reviewed: reviews/expedited-log.md @ cfe9977a1c88d91b17d7bb05f76c2ccc513edf64, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. git push origin agree-outline.

Run bin/check-frontmatter --all from the worktree (must exit 0). Do not open a pull request. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-agree-outline" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; log-entry commit SHA; flip commit SHA and its stat; origin/main SHA verified; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
