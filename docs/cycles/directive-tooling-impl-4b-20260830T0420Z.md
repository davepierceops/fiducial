You are the Coder, an execution session on davepierceops/fiducial, clone at ~/code/fiducial, continuing directive-tooling implementation package 4. The previous run stopped on test_x5; the decision session has diagnosed it and this directive carries the fix. The worktree and the uncommitted forwarder edit are your starting state.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-impl-4b-20260830T0420Z.md in the worktree named below, commit it ALONE — stage only the directive file, not the pending edits — with message "Directive: directive-tooling implementation package 4b (no-optional-locks)", push with git push origin directive-tooling-impl-4 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in the existing worktree at "$TMPDIR/fiducial-dt-impl-4", on branch directive-tooling-impl-4, which the previous run created and left in place. Do not create a worktree. If git worktree list does not show that path on that branch, stop and report.

BASE VERIFICATION before anything else: git fetch origin. The worktree's HEAD must equal origin/directive-tooling-impl-4, whose tip is 3610f483a9f55710b5b115997163db4a092c4d1c (the package-4 directive-file commit). git status must show modifications to bin/cycle-open, bin/directive and bin/aimeta/directive.py and nothing else. If any of that differs, stop and report.

DIAGNOSIS, carried as the decision record: git status refreshes the index's cached stat data and rewrites .git/index when it does, even with no logical change. bin/aimeta/invariants.py's dirtiness check (FM-G3 / invariants-dirty) runs git status --porcelain in the methodology home, so every invariants load may rewrite the home's .git/index; test_x5 snapshots the whole sandbox including the home and caught it once cycle-open forwarded into that path. The behaviour was latent in bin/directive since package 1. TRD §3.9's "reading is not writing" claim is held by making the read not write: git's --no-optional-locks option makes status skip the index refresh. The test is not changed.

SCOPE, one commit carrying the pending forwarder edit plus this fix.
- bin/aimeta/invariants.py: the git status invocation used for the dirtiness check runs with --no-optional-locks (as git --no-optional-locks status --porcelain -- <path>, the option before the subcommand). Audit every other git invocation the invariants load and the lint make against the methodology home or the invoking repository (invariants.py, elements.py, repo.py as reached from them); any that can write index state gets the same option; pure object reads (cat-file, diff-tree, log, rev-parse, show) need nothing. State in the report which invocations you changed and which you left, with the reason.
- The forwarder edit from the previous run stays exactly as made.
- Do not touch bin/tests/, skills/, specs/, docs/global-context/, policies/, roles/.
- Commit message: "directive-tooling: bin/cycle-open forwards to bin/directive (migration step 4); git status reads use --no-optional-locks". Push with git push origin directive-tooling-impl-4.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-dt-impl-4-run.log": bin/tests/run for the whole suite, and bin/check-frontmatter --all (state exit code and count).
Expected state, and a stop if it differs: test_cross_cutting.py green for all three names, test_x5 included; test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py green except its 6 skips; test_check_directive.py 84/84; the only reds in the suite, if any, the three pre-existing cases outside directive tooling (test_scope sc1 and sc3, test_check_frontmatter cf13). Any other red is a stop: report it, do not adjust a test.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and the push is verified landed (git ls-remote origin directive-tooling-impl-4 shows your implementation commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-impl-4" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 3c0963128dd55eda28789de32f54eb0b937d638c: on any failed command, any precondition not met, test_x5 still red after the option is applied, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; implementation commit SHA; branch name; run-log path; the git invocations changed and left, with reasons; the full text of bin/cycle-open and bin/directive as committed; pass/fail/skip counts for the whole suite and for each of the five files named above; the named red cases with the one-line reason each; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
