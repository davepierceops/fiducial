You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task, three commits on a continuation of the triage branch: the doc-only agreement of public-prose-criteria.md (log entry, then flip), then one content edit to roles/critic.md.

SYNC FIRST: from the main tree, git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/agree-voice-r2 exists and its tip is 7c5c86b37f821dfef4b37548353862f61ee7f94e; if not, stop and report.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-agree-criteria-2", created after the fetch above by: git worktree add --no-track "$TMPDIR/fiducial-agree-criteria-2" -b agree-criteria-r2 origin/agree-voice-r2
Before creating it, run git worktree list; if any existing worktree holds a branch named agree-criteria-r2, stop and report. Do not touch the main tree's checkout. All pushes go to origin agree-criteria-r2.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/agree-criteria-r2-20260830T0010.md in the worktree, commit it alone with message "Directive: doc-only agreement of public-prose-criteria.md (revision 2) and Critic count fix", push, and report the SHA.

PRECONDITIONS: public-prose-criteria.md reads status: in-review and last-reviewed: null, and git log -1 --format=%H -- public-prose-criteria.md yields 5fe2c8dcef755633e996e68d8df4637198f24142; roles/critic.md reads status: agreed with last-reviewed: reviews/expedited-log.md @ 4e4eeba8455d6be80ba320ee238253ef4042e271, and its AI-smell bullet contains the exact text "the Criteria's two structure defects — a point restated from the other\n  side, and a clause that explains the move it sits in — and report each the\n  same way." (line-wrapped as in the file). If any differs, stop and report.

EDIT 1 — reviews/expedited-log.md. Append the following line verbatim as the last entry of the file, after the last existing entry (the voice.md revision 2 entry), changing nothing else:

- 2026-08-29 — public-prose-criteria.md @ 5fe2c8dcef755633e996e68d8df4637198f24142 — Structure and length gains one cut from the voice-inbox §4 triage: scene-setting clauses go, stance carries on the verb; agreed via doc-only cycle (DEC-000240)

Commit reviews/expedited-log.md alone with message "expedited-log: public-prose-criteria.md revision 2 agreed via doc-only cycle". Push.

EDIT 2 — the flip. Run bin/flip-agreed once, as a single standalone invocation (never inside a loop), for public-prose-criteria.md with the review pointer exactly:
reviews/expedited-log.md @ 5fe2c8dcef755633e996e68d8df4637198f24142
The tool commits on its own. Verify before pushing that the flip commit touches only public-prose-criteria.md and only its frontmatter (git show --stat and git show; the diff is status: in-review → status: agreed and last-reviewed: null → last-reviewed: reviews/expedited-log.md @ 5fe2c8dcef755633e996e68d8df4637198f24142, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. Push.

EDIT 3 — roles/critic.md. In the AI-smell bullet, replace the phrase "the Criteria's two structure defects — a point restated from the other side, and a clause that explains the move it sits in — and report each the same way" with "the Criteria's structure defects and report each the same way", re-wrapping only the lines of that sentence to the file's width. In the frontmatter, set status: in-review and last-reviewed: null. Change nothing else. Commit roles/critic.md alone with message "critic: AI-smell pass names the Criteria's structure defects without a count (content edit; in-review, doc-only cycle owed)". Read the full SHA with git rev-parse HEAD; call it CRITIC_SHA. Push.

Run bin/check-frontmatter --all from the worktree (must exit 0; roles/critic.md is in-review by design). Do not open a pull request. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-agree-criteria-2" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not rebase, do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; log-entry commit SHA; flip commit SHA and its stat; CRITIC_SHA with its stat and the AI-smell sentence as it now reads; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
