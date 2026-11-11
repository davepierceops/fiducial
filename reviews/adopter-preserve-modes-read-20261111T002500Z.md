# Review: intake/adopter-preserve-modes — read-20261111T002500Z

Verdict: ready
Reviewed: intake/adopter-preserve-modes @ 4bcece9
Baseline: intake/adopter-preserve-modes @ ad141ec
Reviewer: independent reviewer-agent (re-read over the amendment only)
Date: 2026-11-11
Scope: `git diff ad141ec..4bcece9` (process/adopt.md, one statement in `build_plan`; bin/tests/test_adopt.py, one new test) and the surrounding `build_plan`, `inventory`, `apply` and the prose at adopt.md:89-91. A re-read over the amendment only, not the whole branch. It closes Context Quality F1 from reviews/adopter-preserve-modes-read-20261110T235500Z.md: the manifest now keeps its mode, so the unqualified sentence "An existing Markdown or JSON file keeps its permissions; a new file takes the generated ones." is accurate for it.
Cross-checked: /tmp/411-evidence/411-manifest-before.log (new test fails: 420 != 384, "upgrade keeps the manifest mode"); /tmp/411-evidence/411-manifest-after.log (23 OK); /tmp/411-evidence/411-suite-final2.log (349 OK). Reran `python3 -m unittest tests.test_adopt` at 4bcece9: 23 OK.
Not inspected: the rest of the branch (earlier reads); the full suite (taken from the log, not rerun).
Findings: none

Checks:
- Existing manifest keeps its mode, a new one is 0644: observed in the statement and in the test (0644 after first adoption, 0600 kept after upgrade).
- Drift between plan and apply: `inventory()` walks `.claude`, which is in `LAYOUTS`, so the manifest's mode is in `plan["inventory"]`, and `apply` refuses on inventory mismatch. Inferred by reading; the existing mode-only drift test covers the mechanism on CLAUDE.md, not the manifest itself.
- Repeat run: the write is still gated on text inequality, so unchanged text plans no manifest write. Observed in the existing repeat tests, which still pass.
- Failure reason: the before log fails at the 0600 assertion only, which is the old hard-coded 0644.
