You are the Context Quality Reviewer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Gate over two documents revised together on one branch: skills/directive-authoring.md at its consolidation revision (cycle 4) and skills/directive-invariants.md at its cycle-4 riders plus amendment b (cycle 5). You edit nothing but the two artifacts. You do not agree either document and do not flip any status. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-gate-20260831T173000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation gate (cycles 4 and 5)", push with git push origin directive-authoring-consolidation-gate (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-da-gate" -b directive-authoring-consolidation-gate c1983fe7a9c5b46c59b4e8f9e8b925408188419f
Before creating it, run git fetch origin directive-authoring-consolidation, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation-gate, if a branch of that name already exists, or if "$TMPDIR/fiducial-da-gate" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin, git fetch origin directive-authoring-consolidation. Judge every remote operation by the refs it reports, not by credential-helper noise on stderr. origin/directive-authoring-consolidation must be exactly c1983fe7a9c5b46c59b4e8f9e8b925408188419f; if it is anything else, stop and report. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be 43538c1bbc782f19b53e884bd46e08b67db5713b and HEAD:skills/directive-invariants.md must be f6ca0a6482a60d967e3bc647a3c04adeaec19179; if either differs, stop and report.

READ before writing, whole: the prior artifacts via git show 9d4458fe9aec0a66b7f9d682f76912aa352bc351:reviews/directive-authoring-cycle-3.md and git show 9d3d20db19870d383ab1903ac929afce182d3333:reviews/directive-invariants-cycle-4.md; the decision records via git show 9cb11060498171782ccf378e3320d6829eeb0e07:docs/cycles/directive-authoring-consolidation-20260831T150000Z.md and git show b2b8bfa:docs/cycles/directive-authoring-consolidation-b-20260831T172000Z.md; and from the worktree: roles/context-quality-reviewer.md; docs/global-context/core.md; docs/global-context/decision-layer.md; docs/global-context/review-rubric.md; skills/review-artifact.md; skills/directive-authoring.md and skills/directive-invariants.md (the two documents under review, read at c1983fe; the authoring skill last changed at 759344c, the invariants document at c1983fe); specs/directive-tooling-trd.md §3.2, §3.3, §3.4, §3.5, §9 OQ-Q4 and OQ-10; reviews/directive-invariants-cycle-2.md O-3; bin/aimeta/invariants.py, bin/aimeta/mdmask.py, and the unfenced_labelled_statements check in bin/tests/test_directive.py, read and run to distinguish what each document states from what ships.

TASK. Write two artifacts in the review-artifact schema exactly, one commit.

Artifact 1: reviews/directive-authoring-cycle-4.md. Reviewed: skills/directive-authoring.md @ 759344c315d26ab1fe7336f9f0d13de0fe46af38 — the commit that landed its revision; the document is byte-identical at the branch tip c1983fe, which is what you read. Prior cycle: reviews/directive-authoring-cycle-3.md. Two parts. (1) Confirmation: for cycle 3's F-1 (both cycle-mode filenames) and F-3 (the delegation's holder named; the sole-tree form's canonical sentence exists), state whether the revision resolves each, in one observation entry. (2) Full pass over the whole document against all twelve rubric criteria. Every bullet the consolidation added is new text; a defect in one is a finding with its criterion cited. One cross-check you name and report either way: the first bullet names its holder as "the Directive Invariants document" by title rather than by path, on the decision record's stated reading of criterion 3; state whether the document as written satisfies criterion 3 and, if you read criterion 3 the other way, file it as a finding with your reading — the decision session records the ruling, you do not resolve it.

Artifact 2: reviews/directive-invariants-cycle-5.md. Reviewed: skills/directive-invariants.md @ c1983fe7a9c5b46c59b4e8f9e8b925408188419f. Prior cycle: reviews/directive-invariants-cycle-4.md. Two parts. (1) Confirmation: for cycle 4's F-1, O-1, O-2, O-3, and for cycle 2's O-3 (the pronoun), state whether the revision resolves each, in one observation entry; the two amendment-b edits (the Report region's environment bullet; Base verification's every-remote-operation sentence) are confirmed as landed matching the decision record. (2) Full pass over the whole document at c1983fe against all twelve criteria; anything the revision or the amendment introduced is a finding with the criterion cited.

Cross-checks for artifact 2, named on its Cross-checked line with results: the disposition-prompt fence against skills/directive-authoring.md's first bullet, byte equality after flowing, command and result verbatim (expected: equal, 655 bytes each); the per-region placeholder list against the actual {{…}} tokens in each region body; the disposition label's parts against TRD §3.4; the shipped unfenced_labelled_statements check over both documents (expected: no hits in either). Criterion 12 is cross-checked between the two documents in both artifacts: where one states a fact the other also states, they agree. Not inspected is required and explicit in both. Verdict is ready, ready-with-findings, or changes-required — never "agreed". A clean pass is the header and nothing else.

SCOPE, one commit: reviews/directive-authoring-cycle-4.md and reviews/directive-invariants-cycle-5.md only. Do not edit skills/, specs/, docs/global-context/, policies/, roles/, bin/, or any existing file. Commit message: "Review: skills/directive-authoring.md cycle 4; skills/directive-invariants.md cycle 5 (consolidation gate)". Push with git push origin directive-authoring-consolidation-gate.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-gate-run.log": bin/check-frontmatter --all (state exit code and count, and the environment). Expected state, and a stop if it differs: exit 0, 61 files / 14 globs — reviews/ is outside the in-scope set. The bin/ test suite is not run by this directive; report it as not run.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation-gate shows your artifact commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-gate" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref c1983fe7a9c5b46c59b4e8f9e8b925408188419f. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any precondition not met, a document you were told to read that is absent, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the artifact commit SHA, and the branch it is on
- the run-log path
- both artifacts' header blocks verbatim
- findings count by severity, per artifact
- per confirmed item (cycle-3 F-1, F-3; cycle-4 F-1, O-1, O-2, O-3; cycle-2 O-3; amendment b's two edits), resolved or not, one line each
- each named cross-check result in one line
- check-frontmatter exit code and count, with the environment
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
