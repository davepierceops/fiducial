You are the Coder, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Implement TRD §3.9 migration step 4: replace bin/cycle-open's body with a forwarder to bin/directive. You do not edit tests, the TRD, the PRD, or skills/directive-invariants.md.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-impl-4-20260830T0410Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-tooling implementation package 4 (forwarder)", push with git push origin directive-tooling-impl-4 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-impl-4", created by: git worktree add --no-track "$TMPDIR/fiducial-dt-impl-4" -b directive-tooling-impl-4 origin/main
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-impl-4, or if "$TMPDIR/fiducial-dt-impl-4" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. origin/main must contain 3c0963128dd55eda28789de32f54eb0b937d638c. If origin/main is beyond it, proceed only if no commit past it touches bin/; otherwise stop and report.

READ before writing, whole, from the worktree: specs/directive-tooling-trd.md §3.9 ("bin/cycle-open survives as a forwarding executable" and step 4) and §8's non-goals; specs/directive-tooling.md AC-DT-14 and AC-DT-15; bin/cycle-open; bin/directive; bin/aimeta/cli.py; bin/tests/test_cycle_open.py (the suite that now drives both names); bin/tests/test_directive.py test_ac_dt_14_bin_holds_exactly_one_directive_skeleton_generator (read its exact assertion on bin/cycle-open's source); bin/tests/test_cross_cutting.py (AC-X-1..7 cover "cycle-open" by name).

SCOPE, one commit.
- bin/cycle-open's body becomes a forwarder: the same shebang and house shape, then argv passed through unchanged to the same entry point bin/directive uses — import the shared main from the aimeta module if bin/directive's main lives there, otherwise move bin/directive's main into bin/aimeta/directive.py so both executables call one function, bin/directive's own body shrinking to the same shape. No argument parsing, no skeleton emission, no string of render_directive's, and no function definitions of its own beyond what the house shape requires; directive_identity, collect_documents, resolve_revisions, write_bundle and the not-ignored warning are deleted from bin/cycle-open, since package 3 copied them into bin/aimeta/directive.py. The executable's exit codes, stdout and stderr are whatever bin/directive produces for the same argv.
- If bin/directive's main moves, bin/directive's behaviour is byte-identical before and after for every argv; the cross-cutting suite and both directive suites are the check.
- Do not touch bin/tests/, skills/, specs/, docs/global-context/, policies/, roles/.
- Commit message: "directive-tooling: bin/cycle-open forwards to bin/directive (migration step 4)". Push with git push origin directive-tooling-impl-4.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-dt-impl-4-run.log": bin/tests/run for the whole suite, and bin/check-frontmatter --all (state exit code and count).
Expected state, and a stop if it differs: test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py green except its 6 skips; test_check_directive.py 84/84; test_cross_cutting.py green for all three names; the only reds in the suite, if any, the three pre-existing cases outside directive tooling (test_scope sc1 and sc3, test_check_frontmatter cf13). Any other red is a stop: report it, do not adjust a test.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-tooling-impl-4 shows your commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-impl-4" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 3c0963128dd55eda28789de32f54eb0b937d638c: on any failed command, any precondition not met, any test whose expectation contradicts the TRD, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; commit SHA; branch name; run-log path; the full text of bin/cycle-open after the change; whether bin/directive's main moved, and where it now lives; pass/fail/skip counts for the whole suite and for each of the five files named above; the named red cases with the one-line reason each; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
