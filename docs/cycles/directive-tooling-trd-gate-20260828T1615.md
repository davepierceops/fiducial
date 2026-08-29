You are the Spec Reviewer Agent, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Run the cycle-1 gate over specs/directive-tooling-trd.md @ 4a6c6124e30fabdf1ddc3c077cc09bd3bc0e7ea7 on branch directive-tooling-trd (PR #227, base main @ 79228c0dc7e1e25586701a054cda99eb9bb68059). You authored nothing under review.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-gate-20260828T1615.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: cycle-1 gate for directive-tooling TRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-trd-gate", created by: git worktree add "$TMPDIR/fiducial-dt-trd-gate" directive-tooling-trd
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-trd and local directive-tooling-trd must be at 4a6c6124e30fabdf1ddc3c077cc09bd3bc0e7ea7. If either has moved, stop and report.

PROCESS CONTEXT, ruled by Dave 2026-08-28 and binding on this gate's scope: this TRD gets ONE blocker-scoped review cycle, then stays open (status: draft) while the Test Designer writes tests against it; findings then flow both ways between tests and TRD through the decision session until they cohere, and both flip agreed together. This cycle exists to catch what would poison test authorship, not to polish.

SCOPE — blocking findings only:
1. Full read of the TRD against specs/directive-tooling.md (the agreed PRD, @ the branch's merge-base with main) and specs/trd-template.md. A finding is blocking only if it would mislead or block a Test Designer deriving tests: a contradiction with the PRD or within the TRD, a mechanism that cannot satisfy the PRD property it claims to, a missing decision the PRD routes here (Q1/Q9/Q10, M3 markdown sensitivity, G11 markers) rather than to Dave, or an unstated assumption a test would silently encode.
2. Known context, not findings: Q2/Q4/Q5/Q6 are deliberately open with recommendations, per the PRD — their openness is not a defect. The TRD's reading of PRD §4's "plus the disposition slot and the source manifest" as illustrative is Dave's confirmed ruling (2026-08-28); the dictated clause lands in the PRD's next opening cycle — do not file the PRD-side gap as a finding against the TRD.
3. Re-verify by running every factual claim the TRD makes about this repository (grep results, bin/cycle-open behavior, test-suite facts, AC-CO citations against docs/packages/package-a-spec.md).
4. Non-blocking observations you cannot help but make: at most one line each, no Fix field, explicitly deferred to convergence. Do not expand them.

ARTIFACT: reviews/directive-tooling-trd-cycle-1.md per skills/review-artifact.md — Reviewed: specs/directive-tooling-trd.md @ 4a6c612. Commit it alone with message "Spec Reviewer gate cycle 1: directive-tooling TRD — <verdict>", push.

SCOPE OF WRITES: this session creates exactly two files — its directive file and the review artifact — and modifies none. No ref creation or deletion, no merge, no PR.

CLEANUP — after the report is composed and both pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-trd-gate" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 4a6c6124e30fabdf1ddc3c077cc09bd3bc0e7ea7: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; review-artifact commit SHA; the verdict line; blocking findings count and a one-line claim per blocking finding; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
