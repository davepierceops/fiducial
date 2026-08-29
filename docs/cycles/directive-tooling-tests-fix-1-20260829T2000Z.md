You are the Test Designer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Apply one ruled fix to three tests in bin/tests/test_directive.py. You do not touch implementation code, the TRD, the PRD, or any other test.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-tests-fix-1-20260829T2000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-tooling test fix 1 (mask before counting)", push the branch to origin, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-tests-fix", created by: git worktree add --no-track "$TMPDIR/fiducial-dt-tests-fix" -b directive-tooling-tests-fix-1 origin/main
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-tests-fix-1, or if "$TMPDIR/fiducial-dt-tests-fix" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). origin/main must be at e84145b75bd705d0831e0a1d4acd67396d8a3c10. If it has moved, stop and report.

READ before writing, whole, from the worktree: bin/tests/test_directive.py; bin/tests/helpers.py (the directive-tooling section — invariants_sections()'s "Working-tree disposition prompt" fence is the source of the counted lines); specs/directive-tooling.md §6 AC-DT-03 and AC-DT-05; specs/directive-tooling-trd.md §3.2 (condition 2 and 3), §3.3 ("Uniqueness and partition"), §3.5.

DECISION RECORD. Finding, from the implementation package 1 report (docs/cycles/directive-tooling-impl-1-20260829T1400Z.md @ 76c6a8b4f4aa6cf0b72d320e01930d46464f33aa, merged via PR #231 at e84145b7): three tests count label lines and marker lines over raw text without applying §3.5's mask, so the prompt region's fenced worked examples — which AC-DT-03 requires the skeleton to carry — are counted alongside the one author-region slot. AC-DT-03 as agreed counts "unfenced" statements; the tests dropped the word. Dave's ruling, 2026-08-29: option (a) — the tests apply the mask before counting. Option (b), indenting the fixture's fenced examples, was rejected. The generator is not changed.

SCOPE — exactly three tests, one commit:
1. test_ac_dt_03_the_author_region_is_the_label_over_a_blank_slot: count label lines over eligible lines only (eligible_lines is already defined in the file and used by unfenced_labelled_statements). The assertions on the slot line and the blank line below it stay.
2. test_ac_dt_05_every_marker_appears_in_the_file_exactly_once: apply is_marker over eligible lines only.
3. test_ac_dt_05_the_markers_partition_the_whole_file: same; the partition is decided over eligible lines, and the file's first line remains the first region's marker.
Each test's docstring gains one sentence stating that counting is over §3.5's eligible lines, per AC-DT-03's "unfenced" and this ruling. No other test, helper, fixture, or comment changes. Commit message: "directive-tooling: AC-DT-03/05 tests count over eligible lines (ruling 2026-08-29)". Push.

VERIFICATION, from the worktree, output to "$TMPDIR/fiducial-dt-tests-fix-run.log": bin/tests/run for the whole suite, and bin/check-frontmatter --all (must exit 0; state the count).
Expected state, and a stop if it differs: the three named tests green; test_directive.py red on exactly six cases — the five that drive cycle mode (each failing with [cycle-mode-unavailable]) and test_ac_dt_14_bin_holds_exactly_one_directive_skeleton_generator — and no others; test_check_directive.py entirely red on the absent binary; the 424 pre-existing tests green. Any red outside that set is a stop: report it, do not widen the edit.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-tooling-tests-fix-1 shows your fix commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-tests-fix" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref e84145b75bd705d0831e0a1d4acd67396d8a3c10: on any failed command, any precondition not met, any of the three tests that cannot be made green by masking alone, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; fix commit SHA; branch name; run-log path; the diff of the three tests, in full; pass/fail/skip counts for the whole suite and for test_directive.py; the named red test_directive.py cases with the one-line reason each; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
