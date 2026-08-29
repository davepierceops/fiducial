You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: a one-line edit to roles/copy-editor.md, then its doc-only agreement — one content commit, one log entry, one frontmatter-only flip — as three commits.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit 3e116999ffcf553c743d8a6d47ed37c8ccea93bc (git merge-base --is-ancestor 3e116999ffcf553c743d8a6d47ed37c8ccea93bc origin/main exits 0); if not, stop and report. Record origin/main's SHA for your report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-agree-copy-editor", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-agree-copy-editor" -b agree-copy-editor origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named agree-copy-editor, stop and report. Do not touch the main tree's checkout.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/agree-copy-editor-20260829T2215.md in the worktree, commit it alone with message "Directive: edit and doc-only agreement of roles/copy-editor.md", push with git push origin agree-copy-editor, and report the SHA.

PRECONDITION: roles/copy-editor.md in the worktree reads status: draft and last-reviewed: null, and its "## Correct — as tracked changes" list ends with the line "- platform-specific formatting, per the Criteria's venue rule"; if not, stop and report.

EDIT 1 — roles/copy-editor.md. Insert exactly one line immediately after the line "- platform-specific formatting, per the Criteria's venue rule", changing nothing else:

- speech introduced by a bare colon — quote it, per the Criteria's many-languages rule

Confirm with git diff that the change is one added line and no other change (frontmatter untouched: the file is draft, so no status flip applies). Commit roles/copy-editor.md alone with message "roles/copy-editor: bare-colon speech joins the Correct list". Read the commit's full SHA with git rev-parse HEAD; call it CONTENT_SHA in the steps below and state it in the report. git push origin agree-copy-editor.

EDIT 2 — reviews/expedited-log.md. Append the following line verbatim as the last entry of the file, after the last existing entry (the roles/writer.md entry), with CONTENT_SHA written out in full in place of the token, changing nothing else:

- 2026-08-29 — roles/copy-editor.md @ CONTENT_SHA — new writing role: proofread and copyedit as tracked changes, four checklist passes as anchored comments, Google developer documentation style guide as base authority under the Voice document; agreed via doc-only cycle (DEC-000230)

Commit reviews/expedited-log.md alone with message "expedited-log: roles/copy-editor.md agreed via doc-only cycle". git push origin agree-copy-editor.

EDIT 3 — the flip. Run bin/flip-agreed once, as a single standalone invocation (never inside a loop), for roles/copy-editor.md with the review pointer exactly:
reviews/expedited-log.md @ CONTENT_SHA
with CONTENT_SHA written out in full. The tool commits on its own. Verify before pushing that the flip commit touches only roles/copy-editor.md and only its frontmatter (git show --stat and git show on the commit; the diff is status: draft → status: agreed and last-reviewed: null → last-reviewed: reviews/expedited-log.md @ CONTENT_SHA, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. git push origin agree-copy-editor.

Run bin/check-frontmatter --all from the worktree (must exit 0). Do not open a pull request. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-agree-copy-editor" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; CONTENT_SHA and the content commit's stat; log-entry commit SHA; flip commit SHA and its stat; origin/main SHA verified; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
