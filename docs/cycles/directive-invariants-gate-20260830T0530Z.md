You are the Context Quality Reviewer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Review skills/directive-invariants.md, cycle 1, against every criterion of the review rubric, and write the review artifact. You edit nothing else. You do not agree the document and do not flip any status.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-invariants-gate-20260830T0530Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-invariants gate cycle 1", push with git push origin directive-invariants-gate (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-di-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-di-gate" -b directive-invariants-gate origin/main
Before creating it, run git worktree list; if any existing worktree holds branch directive-invariants-gate, or if "$TMPDIR/fiducial-di-gate" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. Judge the fetch by the refs it reports, not by credential-helper noise on stderr. origin/main must contain 7c233c1506dc6111194b5fe603f2fd2f967d4998. If origin/main is beyond it, proceed only if no commit past it touches skills/directive-invariants.md, skills/directive-authoring.md, skills/review-artifact.md, specs/directive-tooling-trd.md, docs/global-context/, or roles/context-quality-reviewer.md; otherwise stop and report.

READ before writing, whole, from the worktree: roles/context-quality-reviewer.md; docs/global-context/core.md; docs/global-context/review-rubric.md; skills/review-artifact.md; policies/document-metadata-policy.md (Scope section — confirm skills/directive-invariants.md is in the in-scope set; if it is not, stop and report); skills/directive-invariants.md (the document under review); skills/directive-authoring.md; specs/directive-tooling-trd.md §3.3 and §3.9.

TASK. Review skills/directive-invariants.md at 7c233c1506dc6111194b5fe603f2fd2f967d4998 against all twelve rubric criteria and write reviews/directive-invariants-cycle-1.md in the review-artifact schema exactly: header block, then one entry per finding, Evidence stating verified-by-running or inferred-by-reading, Consequence concrete or the entry is an observation. Not inspected is required and explicit. Prior cycle: none. Verdict is ready, ready-with-findings, or changes-required — never "agreed".

Cross-checks required, each named in the Cross-checked line with its result:
1. The fenced block under "Working-tree disposition prompt" against the first bullet of skills/directive-authoring.md's "Writing the directive file" section. The test is byte equality after flowing: extract both texts, normalize line breaks and runs of whitespace to single spaces with the same command applied to both, and diff. State the command and the result verbatim. Any difference is a finding under criterion 12.
2. The set of ## sections and every {{placeholder}} in the document against the region and placeholder tables of TRD §3.3. A region or placeholder present in one and absent in the other, or named differently, is a finding under criterion 12.
3. The disposition label literal, the match rule, the statement-extent rule, the exclusive-assignment form test, and the canonical sole-tree sentence against TRD §3.3 and against skills/directive-authoring.md. Disagreement is a finding under criterion 12.
4. The Stop conditions and Claim labels regions against Core rules 6, 11, and 15. Where you find a criterion-4 restatement, the finding's Evidence line states that the region text is emitted verbatim into generated skeletons — that is a fact for triage, not a waiver; state the finding.
Context for criterion 3, stated so the finding is well-formed: the document names bin/aimeta/invariants.py, bin/directive, bin/check-directive, and "the TRD's §3.3 tables". State what you find; do not resolve it.

SCOPE, one commit: reviews/directive-invariants-cycle-1.md only. Do not edit skills/, specs/, docs/global-context/, policies/, roles/, bin/, or any existing file. Commit message: "Review: skills/directive-invariants.md cycle 1". Push with git push origin directive-invariants-gate.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-di-gate-run.log": bin/check-frontmatter --all (state exit code and count). Expected state, and a stop if it differs: exit 0, 61 files / 14 globs. The bin/ test suite is not run by this directive; report it as not run.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-invariants-gate shows your commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-di-gate" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 7c233c1506dc6111194b5fe603f2fd2f967d4998: on any failed command, any precondition not met, a document you were told to read that is absent from the tree, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; artifact commit SHA; branch name; run-log path; the artifact's header block verbatim; findings count by severity; the four cross-check results in one line each; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
