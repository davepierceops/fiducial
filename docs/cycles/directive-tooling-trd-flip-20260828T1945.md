You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: the agreement flip for specs/directive-tooling-trd.md, ruled by Dave 2026-08-28.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-flip-20260828T1945.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-tooling TRD agreement flip", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-trd-flip", created by: git worktree add --no-track "$TMPDIR/fiducial-dt-trd-flip" -b directive-tooling-trd-flip origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named directive-tooling-trd-flip, stop and report. Do not touch the main tree.

BASE VERIFICATION: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Record origin/main's SHA in your report; it must contain commit a031aec0bd760dd1d9dbf2fd1b8db9e2b2d15493 (the PR #227 merge). If specs/directive-tooling-trd.md's frontmatter at origin/main is not exactly status: draft / last-reviewed: null / audience: [human], stop and report.

EDIT — frontmatter only, nothing else in the file:
- status: draft → status: agreed
- last-reviewed: null → last-reviewed: reviews/directive-tooling-trd-cycle-3.md @ 3a945c9
- audience: [human] unchanged.
Verify with git diff that exactly two lines changed and both are inside the frontmatter block.

AFTER: run bin/check-frontmatter --all from the worktree (must exit 0). Commit specs/directive-tooling-trd.md alone with message "directive-tooling TRD: agreement flip — cycle 3 @ 3a945c9". Push. Open a pull request from directive-tooling-trd-flip to main titled "directive-tooling TRD: agreement flip" — if gh cannot reach the API (known sandbox failure), skip the PR, say so, and the decision session opens it. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-trd-flip" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; flip commit SHA; the two-line diff verified; PR number or the gh failure; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
