You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: append a recorded requirement to OPEN-ITEMS.md.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/open-items-bundle-release-req-20260828T1900.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: record bundle-release requirement in OPEN-ITEMS", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-req", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-req" -b open-items-bundle-release-req origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named open-items-bundle-release-req, stop and report. Do not touch the main tree.

BASE VERIFICATION: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Record origin/main's SHA in your report; branch from it wherever it stands.

EDIT: in OPEN-ITEMS.md, find the section "## Bundle-system PRD draft is uncommitted". Immediately after its existing text, append the following block verbatim, and change nothing else in the file:

**Recorded requirement for the PRD's cycle 1 (Dave, via the writing workstream decision session, 2026-08-28):** bundles are distributed through GitHub Releases. `bin/bundle` generates one bundle file per audience; a release attaches those files pinned to the repository SHA they were generated from; a consumer downloads one file and never touches the repository. No generated bundle is ever committed to the tree. Consequences the PRD must state: new audience values (`writer`, `copy`, `critic` are coming) must be accepted without a code change; whether a release carries every audience's bundle or a stated subset is the PRD's decision; every writing bundle carries the Public Prose Criteria document, the per-author Voice document, and a Voice template for new authors, mechanism the PRD's call; release cadence and ownership are open, unconstrained by the writing workstream. Nothing here changes DEC-000210 — this adds a delivery surface downstream of `bin/bundle`.

Also update the file's "Last updated:" line to 2026-08-28.

AFTER: run bin/check-frontmatter --all from the worktree (must exit 0). Commit OPEN-ITEMS.md alone with message "OPEN-ITEMS: bundle-release requirement from writing workstream". Push. Open a pull request from open-items-bundle-release-req to main titled "OPEN-ITEMS: bundle-release requirement" — if gh cannot reach the API (a known sandbox failure), skip the PR, say so in the report, and the decision session opens it. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-req" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; OPEN-ITEMS commit SHA; origin/main SHA branched from; PR number or the gh failure; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
