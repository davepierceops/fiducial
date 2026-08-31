You are the Executor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Land the agreement flip for skills/directive-invariants.md: a frontmatter-only status-transition commit made by the repository's own tool. You edit no file by hand. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-agree-20260830T1030Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-invariants agreement flip", push with git push origin directive-invariants-agree (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-di-agree", created by: git worktree add --no-track "$TMPDIR/fiducial-di-agree" -b directive-invariants-agree origin/directive-invariants-gate-4
Before creating it, run git fetch origin directive-invariants-gate-4, then git worktree list; if any existing worktree holds branch directive-invariants-agree, or if "$TMPDIR/fiducial-di-agree" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-invariants-gate-4. Judge each fetch by the refs it reports, not by credential-helper noise on stderr. origin/directive-invariants-gate-4 must be exactly 9d3d20db19870d383ab1903ac929afce182d3333; if it is anything else, stop and report. Confirm reviews/directive-invariants-cycle-4.md exists in the worktree and that git rev-parse --verify 3f0a96e4f97015ed3091e3d666b64fbc22895eec^{commit} succeeds. Confirm skills/directive-invariants.md at HEAD has status: draft and last-reviewed: null.

TASK. From the worktree root, with nothing staged, run exactly:
bin/flip-agreed skills/directive-invariants.md --review 'reviews/directive-invariants-cycle-4.md @ 3f0a96e4f97015ed3091e3d666b64fbc22895eec'
The tool stages, commits, and self-verifies; it is silent on success and exits 0. Record its exit code and every line it prints. If the exit code is non-zero, stop and report the output verbatim; do not re-run, do not pass different flags, do not edit the file by hand. Do not run flip-agreed with --no-commit.

READ-BACK after the tool exits 0: git show --stat HEAD (expected: subject "docs(skills/directive-invariants.md): status -> agreed", one file changed); git show HEAD -- skills/directive-invariants.md (expected: the diff touches only the frontmatter lines status and last-reviewed — status: agreed, last-reviewed: reviews/directive-invariants-cycle-4.md @ 3f0a96e4f97015ed3091e3d666b64fbc22895eec — and nothing below the closing ---). If the diff touches any body line, stop and report; do not amend. Then bin/check-frontmatter --all, output to "$TMPDIR/fiducial-di-agree-run.log": expected exit 0, 61 files / 14 globs.

Push with git push origin directive-invariants-agree. Verify by git ls-remote origin directive-invariants-agree showing the flip commit SHA.

GH: never invoke gh. The decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-di-agree" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 3f0a96e4f97015ed3091e3d666b64fbc22895eec: on any failed command, any precondition not met, any non-zero exit from flip-agreed, any read-back that differs from the expected, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; flip commit SHA; branch name; run-log path; flip-agreed's exit code and full output; the flip commit's subject and the frontmatter diff verbatim; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
