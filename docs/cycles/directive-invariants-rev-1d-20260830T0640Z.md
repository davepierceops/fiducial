You are the Editor, the execution session holding worktree "$TMPDIR/fiducial-di-rev-1" on branch directive-invariants-rev-1. This directive amends docs/cycles/directive-invariants-rev-1c-20260830T0630Z.md @ bbb9d1280afe3459443b7eed69b0732026ac1997 in one respect only: its FIRST ACT is already discharged as bbb9d1280afe3459443b7eed69b0732026ac1997, and its HEAD precondition is re-pinned to that SHA. No other session holds this branch or this worktree; the assignment is yours alone.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-rev-1d-20260830T0640Z.md in the existing worktree, commit it alone with message "Directive: directive-invariants cycle 1 revision (amendment d, re-pin)", push with git push origin directive-invariants-rev-1 (no -u), and report the SHA. Never bypass the pre-commit hook. Do not rewrite the rev-1c file.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in the worktree at "$TMPDIR/fiducial-di-rev-1", which already exists and was created by: git worktree add --no-track "$TMPDIR/fiducial-di-rev-1" -b directive-invariants-rev-1 origin/main
Reuse it. Before writing, confirm: git status --porcelain in it is empty, and its HEAD is bbb9d1280afe3459443b7eed69b0732026ac1997. If either differs, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION: re-run git fetch origin; if origin/main has moved past d5778195970015e9b65e81f8b3ba4152ab113c3c, apply the rev-1b guard's enumerated list to the new commits; stop if any is touched.

Then carry out rev-1b @ 2c422c67e208bf7d978b95140d05d2e7551f7e03 as amended by rev-1c @ bbb9d1280afe3459443b7eed69b0732026ac1997, unchanged: the fifteen decisions, one content commit with rev-1b's commit message, the push, rev-1b's VERIFICATION block and expected state, the GH clause, and STOP CONDITIONS pinned to 7c233c1506dc6111194b5fe603f2fd2f967d4998.

CLEANUP — after the report is composed and all pushes are verified landed (git ls-remote origin directive-invariants-rev-1 shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-rev-1" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

REPORT: per rev-1c, with every directive-file SHA on the branch listed in order. Label every claim observed, inferred, told, or unknown.
