You are the Context Quality Reviewer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Second confirmation gate over skills/directive-authoring.md (cycle 6) and skills/directive-invariants.md (cycle 7) at the consolidation branch's amendment-d tip. You edit nothing but the two artifacts. You do not agree either document and do not flip any status. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-gate-3-20260831T194500Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation confirmation gate 2 (cycles 6 and 7)", push with git push origin directive-authoring-consolidation-gate-3 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-gate-3", created by: git worktree add --no-track "$TMPDIR/fiducial-da-gate-3" -b directive-authoring-consolidation-gate-3 6a30ff19f2394642e4f387c518262486da6f8826
Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation-gate-3, if a branch of that name already exists, or if "$TMPDIR/fiducial-da-gate-3" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-authoring-consolidation. Judge every remote operation by the refs it reports and its exit status, not by credential-helper noise on stderr; an operation that exits 0 and reports no refs is not a failure. origin/directive-authoring-consolidation must be exactly 6a30ff19f2394642e4f387c518262486da6f8826; if it is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be ab43abc6b435d7c7eea220bc44a591fb43bb5799 and HEAD:skills/directive-invariants.md must be 80d572aad5c80eb6531e0b8ff7f5b9ae84571829; if either differs, stop and report.

READ before writing, whole: the prior artifacts and the amendment record via git show 7e055d7393d96deabd5c50c6ca01e52047e306e4:reviews/directive-authoring-cycle-5.md, git show 7e055d7393d96deabd5c50c6ca01e52047e306e4:reviews/directive-invariants-cycle-6.md, and git show cd4135c2dd82a76688590b385d6a8f3c86a01b2c:docs/cycles/directive-authoring-consolidation-d-20260831T190000Z.md; and from the worktree: roles/context-quality-reviewer.md; docs/global-context/review-rubric.md; skills/review-artifact.md; skills/directive-authoring.md and skills/directive-invariants.md (the two documents under review, at 6a30ff1); bin/aimeta/mdmask.py and the unfenced_labelled_statements check in bin/tests/test_directive.py, read and run.

TASK. Write two artifacts in the review-artifact schema exactly, one commit. This is a confirmation gate: state per accepted finding whether amendment d resolves it, in one observation entry, then re-run the named cross-checks. New decisions are not taken here; anything new the amendment introduced is a finding with its criterion cited, and nothing else is re-litigated.

Artifact 1: reviews/directive-authoring-cycle-6.md. Reviewed: skills/directive-authoring.md @ 6a30ff19f2394642e4f387c518262486da6f8826. Prior cycle: reviews/directive-authoring-cycle-5.md. Confirm cycle-5 F-1 (E1: the eligibility gloss, by-title) as resolved or not.

Artifact 2: reviews/directive-invariants-cycle-7.md. Reviewed: skills/directive-invariants.md @ 6a30ff19f2394642e4f387c518262486da6f8826. Prior cycle: reviews/directive-invariants-cycle-6.md. Confirm cycle-6 F-1 (E2: the exit-status exception sentence) as resolved or not, including that the no-refs fetch and the ref-reporting push both fall inside the exception as worded.

Cross-checks, named on each Cross-checked line with results, all run: the disposition-prompt fence against the authoring skill's first bullet, flow method, expected equal at 669 bytes each; the shipped unfenced_labelled_statements over both documents, expected no hits; criterion 12 between the amended Stop conditions sentence and the Base verification sentence (the first says what a failed command is not; the second says which output to believe — state that they compose rather than conflict, or file the divergence). Not inspected is required and explicit. Verdict is ready, ready-with-findings, or changes-required — never "agreed". A clean confirmation pass is the header and nothing else.

SCOPE, one commit: reviews/directive-authoring-cycle-6.md and reviews/directive-invariants-cycle-7.md only. Do not edit skills/, specs/, docs/global-context/, policies/, roles/, bin/, or any existing file. Commit message: "Review: skills/directive-authoring.md cycle 6; skills/directive-invariants.md cycle 7 (confirmation 2)". Push with git push origin directive-authoring-consolidation-gate-3.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-gate-3-run.log": bin/check-frontmatter --all (state exit code and count, and the tree it was observed in). Expected state, and a stop if it differs: exit 0, 61 files / 14 globs. The bin/ test suite is not run by this directive; report it as not run.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation-gate-3 shows your artifact commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-gate-3" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 6a30ff19f2394642e4f387c518262486da6f8826. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any precondition not met, a document you were told to read that is absent, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the artifact commit SHA, and the branch it is on
- the run-log path
- both artifacts' header blocks verbatim
- per confirmed item (cycle-5 F-1; cycle-6 F-1), resolved or not, one line each
- each named cross-check result in one line
- check-frontmatter exit code and count, with the tree it was observed in
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
