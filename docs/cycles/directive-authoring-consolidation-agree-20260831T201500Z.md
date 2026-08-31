You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Land the agreement flips for skills/directive-authoring.md and skills/directive-invariants.md, whose consolidation arc closed clean: both documents' final gates are ready with zero findings (reviews/directive-authoring-cycle-6.md, reviews/directive-invariants-cycle-7.md), and Dave's go is given. This is a frontmatter-only status transition; you change no body text anywhere.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-agree-20260831T201500Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation agreement flips", push with git push origin directive-authoring-consolidation-agree (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-agree", created by: git worktree add --no-track "$TMPDIR/fiducial-da-agree" -b directive-authoring-consolidation-agree origin/main
Before creating it, run git fetch origin, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation-agree, if a branch of that name already exists, or if "$TMPDIR/fiducial-da-agree" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. Judge every remote operation by the refs it reports and its exit status, not by credential-helper noise on stderr; an operation that exits 0 and reports no refs is not a failure. origin/main must contain 5ca6b31d6ff9e2b01c2f566e04389c897067ee1d (git merge-base --is-ancestor, exit 0); if not, stop and report. In the worktree: reviews/directive-authoring-cycle-6.md and reviews/directive-invariants-cycle-7.md must exist, each with "Verdict: ready" on its verdict line; git rev-parse HEAD:skills/directive-authoring.md must be ab43abc6b435d7c7eea220bc44a591fb43bb5799 and HEAD:skills/directive-invariants.md must be 80d572aad5c80eb6531e0b8ff7f5b9ae84571829; both files' frontmatter must read status: in-review with last-reviewed: null. If any of these differs, stop and report.

FLIPS, two invocations, in order, from the worktree:
1. bin/flip-agreed skills/directive-authoring.md --review 'reviews/directive-authoring-cycle-6.md @ afbe7df9924f0449a2f48a408c26c67399595eb8'
2. bin/flip-agreed skills/directive-invariants.md --review 'reviews/directive-invariants-cycle-7.md @ afbe7df9924f0449a2f48a408c26c67399595eb8'
bin/flip-agreed is silent on success; judge each by exit code, then verify by reading both files' frontmatter: status: agreed, last-reviewed naming the artifact and SHA above, audience unchanged, and no body line changed. If either invocation exits non-zero or the frontmatter reads otherwise, stop and report; do not edit frontmatter by hand.

SCOPE, one commit after the directive-file commit: the two frontmatter flips only. git diff --stat must show exactly two files with frontmatter-line changes only; if any body line appears in the diff, stop and report. Commit message: "directive-authoring + directive-invariants: agreed (consolidation cycles 6 and 7)". Push with git push origin directive-authoring-consolidation-agree.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-agree-run.log": bin/check-frontmatter --all (state exit code and count); bin/tests/run for the whole suite. Expected state, and a stop if it differs: check-frontmatter exit 0, 62 files / 14 globs; suite OK, 604 tests, zero failures, zero errors, 7 skipped.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation-agree shows your flip commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-agree" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 5ca6b31d6ff9e2b01c2f566e04389c897067ee1d, the origin/main merge this directive derives from. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the flip commit SHA, and the branch it is on
- the run-log path
- both files' frontmatter verbatim as landed
- check-frontmatter exit code and count, and the suite counts, each with the tree it was observed in; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
