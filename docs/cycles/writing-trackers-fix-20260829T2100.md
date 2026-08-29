Continuation of docs/cycles/writing-trackers-20260829T2000.md @ d85ec0c, in the same worktree "$TMPDIR/fiducial-writing-trackers" on branch writing-trackers. The stop was correct: the six files below were landed by PR #230 without the required last-reviewed key. Fix that, then resume the original directive from its check step.

FIRST ACT — directive file. Write this entire continuation verbatim to docs/cycles/writing-trackers-fix-20260829T2100.md in the worktree, commit it alone with message "Directive: writing-trackers continuation — add last-reviewed to six migrated files", push, and report the SHA.

PRECONDITION: git status in the worktree shows OPEN-ITEMS.md as the only modified tracked file, with the 16-insertion 2-deletion diff from the original directive's EDIT 2. If anything else is modified, stop and report.

EDIT 3 — frontmatter only. In each of these six files, insert the line
last-reviewed: null
immediately after the line beginning "status:" inside the frontmatter, changing nothing else in any file:
- public-prose-criteria.md
- roles/copy-editor.md
- roles/critic.md
- skills/outline.md
- voice-template.md
- voice.md
Commit the six files alone — OPEN-ITEMS.md stays unstaged — with message "frontmatter: add last-reviewed: null to six files migrated at PR #230". Push.

RESUME the original directive at "Run bin/check-frontmatter --all from the worktree (must exit 0)" and carry out every step after it exactly as written there: the OPEN-ITEMS.md commit and push, the pull request, the CLEANUP, and the REPORT — with one addition to the report: the frontmatter commit SHA.

STOP CONDITIONS unchanged: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.
