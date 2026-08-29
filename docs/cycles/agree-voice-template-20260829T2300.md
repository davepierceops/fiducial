You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: doc-only agreement of voice-template.md — one log entry, then one frontmatter-only flip — as two commits.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit 1a71a81943ef8128c6a24806cdd406c6304084a6 (git merge-base --is-ancestor 1a71a81943ef8128c6a24806cdd406c6304084a6 origin/main exits 0); if not, stop and report. Record origin/main's SHA for your report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-agree-voice-template", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-agree-voice-template" -b agree-voice-template origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named agree-voice-template, stop and report. Do not touch the main tree's checkout.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/agree-voice-template-20260829T2300.md in the worktree, commit it alone with message "Directive: doc-only agreement of voice-template.md", push with git push origin agree-voice-template, and report the SHA.

PRECONDITION: voice-template.md in the worktree reads status: draft and last-reviewed: null; if not, stop and report.

EDIT 1 — reviews/expedited-log.md. Append the following line verbatim as the last entry of the file, after the last existing entry (the skills/outline.md entry), changing nothing else:

- 2026-08-29 — voice-template.md @ 55d4a43e40458c88fa223d16c8e7e9cba53a970d — new: human-facing Voice template a new author fills in, one author's sections as labeled examples that are a snapshot and never a finding; agreed via doc-only cycle (DEC-000240)

Commit reviews/expedited-log.md alone with message "expedited-log: voice-template.md agreed via doc-only cycle". git push origin agree-voice-template.

EDIT 2 — the flip. Run bin/flip-agreed once, as a single standalone invocation (never inside a loop), for voice-template.md with the review pointer exactly:
reviews/expedited-log.md @ 55d4a43e40458c88fa223d16c8e7e9cba53a970d
The tool commits on its own. Verify before pushing that the flip commit touches only voice-template.md and only its frontmatter (git show --stat and git show on the commit; the diff is status: draft → status: agreed and last-reviewed: null → last-reviewed: reviews/expedited-log.md @ 55d4a43e40458c88fa223d16c8e7e9cba53a970d, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. git push origin agree-voice-template.

Run bin/check-frontmatter --all from the worktree (must exit 0). Do not open a pull request. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-agree-voice-template" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; log-entry commit SHA; flip commit SHA and its stat; origin/main SHA verified; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
