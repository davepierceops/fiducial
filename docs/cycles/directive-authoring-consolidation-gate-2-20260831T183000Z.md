You are the Context Quality Reviewer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Confirmation gate over skills/directive-authoring.md (cycle 5) and skills/directive-invariants.md (cycle 6) at the consolidation branch's amendment-c tip. You edit nothing but the two artifacts. You do not agree either document and do not flip any status. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-gate-2-20260831T183000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation confirmation gate (cycles 5 and 6)", push with git push origin directive-authoring-consolidation-gate-2 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-gate-2", created by: git worktree add --no-track "$TMPDIR/fiducial-da-gate-2" -b directive-authoring-consolidation-gate-2 efaad5f6a4db5c6005b81f2af9f1bd53a1063872
Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation-gate-2, if a branch of that name already exists, or if "$TMPDIR/fiducial-da-gate-2" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-authoring-consolidation. Judge every remote operation — fetch, push, ls-remote — by the refs it reports, not by credential-helper noise on stderr. origin/directive-authoring-consolidation must be exactly efaad5f6a4db5c6005b81f2af9f1bd53a1063872; if it is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be ceb6a0dc5c34efa682d35f732169f5d5e119d5dc and HEAD:skills/directive-invariants.md must be bb54dcb55d3db29c4d4629698218be0810101f5a; if either differs, stop and report.

READ before writing, whole: the prior artifacts and the amendment record via git show cd6c8347f7f4b3475c5bfeddf74aee47324e4bc7:reviews/directive-authoring-cycle-4.md, git show cd6c8347f7f4b3475c5bfeddf74aee47324e4bc7:reviews/directive-invariants-cycle-5.md, and git show 68af089d66fcbadb43aa59d6c18292464149a948:docs/cycles/directive-authoring-consolidation-c-20260831T181500Z.md; and from the worktree: roles/context-quality-reviewer.md; docs/global-context/review-rubric.md; skills/review-artifact.md; skills/directive-authoring.md and skills/directive-invariants.md (the two documents under review, at efaad5f); bin/aimeta/mdmask.py and the unfenced_labelled_statements check in bin/tests/test_directive.py, read and run.

TASK. Write two artifacts in the review-artifact schema exactly, one commit. This is a confirmation gate: for each artifact, state per accepted finding whether amendment c resolves it, in one observation entry, then re-run the named cross-checks. New decisions are not taken here; anything new the amendment introduced is a finding with its criterion cited, and nothing else is re-litigated.

Artifact 1: reviews/directive-authoring-cycle-5.md. Reviewed: skills/directive-authoring.md @ efaad5f6a4db5c6005b81f2af9f1bd53a1063872. Prior cycle: reviews/directive-authoring-cycle-4.md. Confirm cycle-4 F-1 (E1: ", which is their one definition") and F-2 (E2: "eligible") as resolved or not.

Artifact 2: reviews/directive-invariants-cycle-6.md. Reviewed: skills/directive-invariants.md @ efaad5f6a4db5c6005b81f2af9f1bd53a1063872. Prior cycle: reviews/directive-invariants-cycle-5.md. Confirm cycle-5 F-1 (E4: the Stop conditions exception sentence) and F-2 (E5: the one-axis bullet with the sandbox clause) as resolved or not, and cycle-5 O-4 as moved by E1/E3 (the fence's exclusivity claim narrowed to the one-definition form the preamble states).

Cross-checks, named on each Cross-checked line with results, all run: the disposition-prompt fence against the authoring skill's first bullet, flow method, expected equal at 669 bytes each; the shipped unfenced_labelled_statements over both documents, expected no hits; criterion 12 between the two documents on the label-lead bound (both now "eligible") and on the exclusivity claim (both now single-definition, agreeing with the invariants preamble and TRD §3.4). Not inspected is required and explicit. Verdict is ready, ready-with-findings, or changes-required — never "agreed". A clean confirmation pass is the header and nothing else.

SCOPE, one commit: reviews/directive-authoring-cycle-5.md and reviews/directive-invariants-cycle-6.md only. Do not edit skills/, specs/, docs/global-context/, policies/, roles/, bin/, or any existing file. Commit message: "Review: skills/directive-authoring.md cycle 5; skills/directive-invariants.md cycle 6 (confirmation)". Push with git push origin directive-authoring-consolidation-gate-2.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-gate-2-run.log": bin/check-frontmatter --all (state exit code and count, and the tree it was observed in). Expected state, and a stop if it differs: exit 0, 61 files / 14 globs. The bin/ test suite is not run by this directive; report it as not run.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation-gate-2 shows your artifact commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-gate-2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref efaad5f6a4db5c6005b81f2af9f1bd53a1063872. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any precondition not met, a document you were told to read that is absent, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the artifact commit SHA, and the branch it is on
- the run-log path
- both artifacts' header blocks verbatim
- per confirmed item (cycle-4 F-1, F-2; cycle-5 F-1, F-2, O-4), resolved or not, one line each
- each named cross-check result in one line
- check-frontmatter exit code and count, with the tree it was observed in
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
