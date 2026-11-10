# Review: intake/adopter-preserve-modes — read-20261110T235600Z

Verdict: changes-required
Reviewed: intake/adopter-preserve-modes @ b71922a
Baseline: main @ 5b2a62f
Reviewer: reviewer-agent
Date: 2026-11-10
Scope: `git diff 5b2a62f..b71922a` (plan, `bin/tests/test_adopt.py`, `process/adopt.md`); acceptance criteria 1-7 of the plan checked against the tree at b71922a; the nine new tests and the shared `plan()` helper change; the two failing tests in `tests.test_remaining_role_pruning_continuation`.
Cross-checked: `.claude/agents/reviewer-agent.md`, `.claude/skills/build/SKILL.md`, `.claude/skills/verification-checklists/SKILL.md`, `process/review-artifact.md`, `/tmp/411-evidence/411-tests-before.log`, `411-tests-after.log`, `411-suite-after.log`, `.claude/skills/adopt/SKILL.md`.
Not inspected: behaviour on filesystems without POSIX modes; a real target repository; the installed `.claude/` and `.agents/` copies after regeneration (a later plan step); the full suite at 5b2a62f (I did not re-run it; I did not check that the two failures are absent there, only that the diff's sole `process/adopt.md` change is what they show). I did not run the full 348-test suite, only `tests.test_adopt`.
Findings: 1 blocking, 1 non-blocking, 1 observation
The human should inspect: how the frozen role-pruning oracle should treat an approved later change to `process/adopt.md` (F1), since fixing it widens the delta beyond the plan's listed files.

## Quality pass

Verdict (quality): changes-required

Acceptance criteria at b71922a:

1. Met. `test_existing_0600_json_keeps_mode_through_adoption_upgrade_and_repeat` covers first adoption, upgrade and repeat; it failed before the fix (before.log) and passes after. I reran `tests.test_adopt`: 22 OK.
2. Met. The same for `.md`, `test_existing_0600_markdown_keeps_mode_through_adoption_upgrade_and_repeat`; failed before, passes after.
3. Met. `adopt_upgrade_repeat` asserts `plan()["writes"] == {}` after first adoption and after upgrade, so the manifest write is covered too; `test_created_files_chmodded_by_user_are_not_replanned_or_widened` failed before, passes after.
4. Met. `test_new_staged_hook_lands_executable_with_staged_mode` asserts 0755. It passes before and after, as the plan expected for a guard. The fix only overrides when `path.exists()` (`process/adopt.md` line 286), so a new path still takes the staged mode.
5. Met. `test_locally_chmodded_owned_script_is_still_refused` asserts the "occupied or modified structured file" conflict and the 0700 mode left intact. The whole-file branch is untouched; the override covers only `.md` and `.json` suffixes.
6. Met. `test_mode_only_drift_between_plan_and_apply_is_refused_before_any_write` chmods after authorization and asserts "changed since review" and a byte-identical tree. `inventory` records mode (line 154), so the guard is real. Guard test; passes before and after.
7. Not met. See F1.

Minimality: the code change is two lines in `build_plan` plus one prose sentence. It is the smallest change that fixes the cause the plan observed, and nothing else moves.

Test meaningfulness: the four tests that fail on unfixed code are the criterion 1, 2 and 3 tests plus the legacy-edit test, so they would fail on bad logic. The remaining five pass on both sides by design (the plan labels criteria 4-6 as guards). Two of them, `test_edit_only_unstaged_0600_file_keeps_mode` and `test_retiring_owned_section_from_surviving_0600_file_keeps_mode`, use paths absent from the staged tree, where `new_mode` already defaults to the existing mode. They guard the override against regressing those paths but cannot detect a missing fix; this is acceptable and is the plan's stated intent. Names match behaviour.

Shared helper: `plan()` now sets a per-call timestamp `20261105T0102NN` from a per-test counter (`self.plans`, fresh per test instance). No test in the file hardcodes the former `20261105T010203Z`, and the counter is needed because several tests now install more than once into one target (distinct report paths). The 22 tests pass, so it is safe for the existing ones.

## F1 — blocking
Claim: Criterion 7 (full suite passes) is not met, and the coder's explanation for the two failures is wrong.
Classification: defect
Location: `bin/tests/test_remaining_role_pruning_continuation.py:220-250` (`test_final_archives_and_sources_match_the_approved_preview`, `test_live_native_and_all_bundles_equal_preview_with_hooks_unchanged`); cause `process/adopt.md` row body.
Evidence: Verified by reading the tests and 411-suite-after.log. `cls.live = inputs(REPO_ROOT)` reads the live source rows, including the edited `process/adopt.md`; `cls.preview` is built from `git archive CHECKPOINT` (4157ddd), a frozen historical oracle plus the PENDING removals. The first test asserts `records(live) == records(preview)`; the second asserts `targets()[h].emit(live).files == emit(preview).files`. The assertion diffs in the log show the only difference as the new sentence "An existing Markdown or JSON file keeps its permissions". Neither test reads the installed `.claude/` or `.agents/` copies. Regenerating them in the later step will therefore not clear the failures.
Consequence: The suite stays red after the planned self-adoption refresh. Any change to a process row after the checkpoint breaks these oracle tests until they are amended. The merge gate and criterion 7 cannot be met as sequenced.
Fix: Decide explicitly, and record it: either amend `checkpoint_preview` (or the live-vs-preview comparison) to account for the approved `adopt` row change, or retire the oracle if its purpose has ended. This edit is outside the plan's file list, so the plan's Change section needs an amendment. Correct the claim in the coder's report.

## F2 — non-blocking
Claim: The plan's sequence does not anticipate the oracle tests, so the plan's scope list is incomplete.
Classification: suggestion
Location: `docs/plans/adopter-preserve-modes-20261110T233500Z.md`, Change and Sequence.
Evidence: Inferred from F1; the plan lists only `process/adopt.md`, `bin/tests/test_adopt.py` and installed-copy regeneration.
Consequence: Whoever resolves F1 edits a file the plan did not authorize.
Fix: Add the test oracle to the plan's Change list when F1 is resolved.
Related: F1

## O1 — observation
Claim: `.claude/skills/adopt/SKILL.md` and `.agents/` copies do not yet carry the new sentence.
Evidence: Read; the plan schedules regeneration at step 5. Not a defect now.

## Continuity pass

Verdict (continuity): ready-with-findings

- Scope: the delta touches only the plan, `bin/tests/test_adopt.py` and `process/adopt.md`. No #412 behaviour (partial adoption after drift) is changed; `writes[MANIFEST]` still hardcodes 0644 (line 309-310 untouched); no `docs/releases`, `rules/`, `.claude/` or `.agents/` file is in the diff.
- Agreement: the new prose sentence matches the code (`path.exists()` and `.md`/`.json`, case-sensitive suffix, new files take generated modes). The prose on whole-file hash ownership and the recorded mode in ownership still matches the unchanged branch. No other line in `process/adopt.md` mentions modes in a way that now disagrees.
- Disagreement found: only F1/F2 (frozen oracle tests versus the edited process row). The installed copies' lag is the planned step 5 (O1).
