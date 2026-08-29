You are the Spec Reviewer Agent, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Run the cycle-3 confirmation over specs/directive-tooling-trd.md and its test suite @ 3a945c9381674b73d556d901a7becb349354fb9a on branch directive-tooling-trd (PR #227, base main @ 79228c0dc7e1e25586701a054cda99eb9bb68059). You authored none of it.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-conf3-20260828T1900.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: cycle-3 confirmation for directive-tooling TRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-conf3", created by: git worktree add "$TMPDIR/fiducial-dt-conf3" directive-tooling-trd
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-trd and local directive-tooling-trd must be at 3a945c9381674b73d556d901a7becb349354fb9a. If either has moved, stop and report.

SCOPE — confirmation of the cycle-2 fixes, nothing else:
1. For each cycle-2 finding F-1, F-2, F-3 (reviews/directive-tooling-trd-cycle-2.md, read whole): confirm the fix landed as dispositioned in docs/cycles/directive-tooling-trd-conv2-20260828T1830.md (read whole). For F-1, run the two rewritten tests against the stubs yourself (DIRECTIVE_TOOLING_BIN as an absolute path — the round-2 report records that a relative path misresolves in this sandbox) and confirm each fails on behavior, not import.
2. The round-2 executor's disclosed extras — the two "four → three" docstring corrections and the TestOpenQuestions class-docstring update — are the same defect class as F-1's named fix; confirm they are accurate against the TRD, and treat them as accepted unless one misstates the document.
3. Verify by running: bin/tests/run (424 pre-existing green, skip count 7, all failures/errors confined to the three new modules) and bin/check-frontmatter --all (exit 0). Record both in the artifact.
4. New findings only where a cycle-2 fix did not land or introduced a defect. Do not reopen the design; do not re-litigate deferred observations O-1 through O-4, which survive to implementation by prior disposition.

ARTIFACT: reviews/directive-tooling-trd-cycle-3.md per skills/review-artifact.md — Reviewed: specs/directive-tooling-trd.md @ 3a945c9, Scope naming the test suite, Prior cycle: reviews/directive-tooling-trd-cycle-2.md. A clean confirmation is the header and nothing else. Commit it alone with message "Spec Reviewer confirmation cycle 3: directive-tooling TRD — <verdict>", push.

SCOPE OF WRITES: this session creates exactly two files — its directive file and the review artifact — and modifies none. No ref creation or deletion, no merge, no PR.

CLEANUP — after the report is composed and both pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-conf3" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 3a945c9381674b73d556d901a7becb349354fb9a: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; review-artifact commit SHA; the verdict line; per-finding confirmation one line each; suite and frontmatter results; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
