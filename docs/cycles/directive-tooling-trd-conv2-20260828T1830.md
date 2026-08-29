You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Carry out convergence round 2: apply the three cycle-2 findings to branch directive-tooling-trd. All three are mechanical; the dispositions below are complete.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-conv2-20260828T1830.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: convergence round 2 for directive-tooling TRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-conv2", created by: git worktree add "$TMPDIR/fiducial-dt-conv2" directive-tooling-trd
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before any edit: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-trd and local directive-tooling-trd must be at d6ed0c7dcf58a2dcaeb98b45dceab859c9cc931a. If either has moved, stop and report.

READ before editing, from the worktree: reviews/directive-tooling-trd-cycle-2.md (the findings, whole); specs/directive-tooling-trd.md §3.3 (both region tables and their counts — the ground truth for F-1's assertions and F-2's fix); bin/tests/test_directive_trd.py whole; the five docstring sites F-3 names.

DISPOSITIONS:
- F-1 accept: rewrite the two Q5 tests in test_directive_trd.py from skips into running behavioral tests asserting the ruling's two consequences. One asserts ROUTE AND MODEL is a committed region in both modes' manifests and the author-region count stays exactly two per mode (AC-DT-18's guard against a third author slot). One asserts the lint's element set is exactly M1–M8 — a well-formed directive with route and model entirely absent still exits 0, and no output names a ninth element. Rename both from test_q5_* to names stating what they assert; their docstrings cite Dave's Q5 ruling (c), 2026-08-28, recorded in docs/cycles/directive-tooling-trd-conv1-20260828T1745.md. Both must be red against the stubs (run with DIRECTIVE_TOOLING_BIN=bin/tests/stubs and confirm each fails on behavior, not import); state each test's red in the report. The skip count drops from 8 to 6 — Q2, Q4, Q6, AC-DT-16 remain, honestly.
- F-2 accept: specs/directive-tooling-trd.md :420 (locate by content, not line number): the sentence "Cycle mode's region 5 is a committed region…" describes ## Decisions, which now sits at row 6; row 5 is the WORKING-TREE DISPOSITION author region. Correct the row number and re-read the surrounding paragraph against both tables so the sentence you leave agrees with the table, the count line, and the F-A3 subsection's numbering. This is the only TRD edit.
- F-3 accept: correct the five stale docstrings the artifact names (AC-DT-14's "no route-and-model region"; AC-DT-09's "an annotated tag satisfies §3.6's mechanism"; AC-DT-10's "the TRD names no other"; AC-DT-02's "F-8" framing; the OQ-Q5 citation) to state the amended TRD. Assertions are untouched — the artifact confirms every assertion already agrees with the TRD; if you find one that does not, stop and report rather than changing it.

SCOPE: specs/directive-tooling-trd.md (F-2's one sentence region) and bin/tests/test_directive_trd.py plus the five docstring sites (which may span the other two test modules). Nothing else; no ref creation or deletion, no merge, no PR. Frontmatter stays exactly: status: draft, last-reviewed: null, audience: [human].

AFTER EDITS: run bin/tests/run — 424 pre-existing green, no collection failure, skip count 7 total (6 in test_directive_trd + the pre-existing conditional one); state the new modules' counts. Run bin/check-frontmatter --all — exit 0. Commit everything with message "directive-tooling TRD: convergence round 2 — cycle-2 F-1..F-3". Push.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-conv2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref d6ed0c7dcf58a2dcaeb98b45dceab859c9cc931a: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; fix commit SHA; the two rewritten tests' names and their red-on-stub results; the corrected F-2 sentence as it now reads; the five docstring corrections one line each; suite state; check-frontmatter exit code; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
