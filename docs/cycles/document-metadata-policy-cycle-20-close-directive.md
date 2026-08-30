You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: close cycle 20 on policies/document-metadata-policy.md — one docstring fix (DMP20-1), then the agreement flip — as two commits on the cycle-20 branch.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/document-metadata-policy-cycle-20 exists and its tip contains commit 3aa12a53e5cd5c134b54c4f77325f306c4d12ece (git merge-base --is-ancestor 3aa12a53e5cd5c134b54c4f77325f306c4d12ece origin/document-metadata-policy-cycle-20 exits 0); if not, stop and report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dmp-cycle-20-close", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-dmp-cycle-20-close" -b dmp-cycle-20-close origin/document-metadata-policy-cycle-20
Before creating it, run git worktree list; if any existing worktree holds a branch named dmp-cycle-20-close, stop and report. Do not touch the main tree's checkout. All pushes go to origin dmp-cycle-20-close.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/document-metadata-policy-cycle-20-close-directive.md in the worktree, commit it alone with message "Directive: document-metadata-policy cycle 20 close and agreement", push with git push origin dmp-cycle-20-close, and report the SHA.

DECISION RECORD — cycle 20, artifact reviews/document-metadata-policy-cycle-20.md @ 3aa12a53e5cd5c134b54c4f77325f306c4d12ece, verdict ready-with-findings, reviewed revision 9160a865fc7070775fc17e9b50c55bc5610318df:
- DMP20-1 (non-blocking): accepted. Fix below. It does not hold the verdict; the document is agreed at 9160a865 on Dave's go, relayed 2026-08-29.
- The reviewer's suite-baseline note belongs to the directive-tooling workstream; no action here.

PRECONDITION: policies/document-metadata-policy.md in the worktree reads status: in-review and last-reviewed: null, and git log -1 --format=%H -- policies/document-metadata-policy.md yields 9160a865fc7070775fc17e9b50c55bc5610318df; if not, stop and report.

EDIT 1 — bin/tests/test_bundle_audience.py (DMP20-1). Read lines 10–20 and 135–145 before changing anything. In the two docstrings — the AC-BA-1 contract bullet near line 16 and the fixture docstring near line 139 — replace the statement that the governed set includes a repo-root prose-criteria.md with the same statement naming public-prose-criteria.md, voice.md, and voice-template.md, keeping each docstring's wording otherwise. Change no code. Commit the file alone with message "tests: AC-BA-1 docstrings name the writing documents (DMP20-1)". Run python3 -m unittest tests.test_bundle_audience from bin/ (or the suite's own invocation for that module) and confirm all 40 tests OK; if not, stop and report. Push.

EDIT 2 — the flip. Run bin/flip-agreed once, as a single standalone invocation (never inside a loop), for policies/document-metadata-policy.md with the review pointer exactly:
reviews/document-metadata-policy-cycle-20.md @ 9160a865fc7070775fc17e9b50c55bc5610318df
The tool commits on its own. Verify before pushing that the flip commit touches only policies/document-metadata-policy.md and only its frontmatter (git show --stat and git show; the diff is status: in-review → status: agreed and last-reviewed: null → last-reviewed: reviews/document-metadata-policy-cycle-20.md @ 9160a865fc7070775fc17e9b50c55bc5610318df, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. Push.

Run bin/check-frontmatter --all from the worktree (must exit 0). Do not edit any other governed document. Do not open a pull request. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dmp-cycle-20-close" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; docstring commit SHA with the two lines before and after; module test result; flip commit SHA and its stat; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
