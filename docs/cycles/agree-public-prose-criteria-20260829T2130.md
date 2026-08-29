You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. One task: doc-only agreement of public-prose-criteria.md — one log entry, then one frontmatter-only flip — as two commits.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/agree-public-prose-criteria-20260829T2130.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: doc-only agreement of public-prose-criteria.md", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-agree-ppc", created by: git worktree add --no-track "$TMPDIR/fiducial-agree-ppc" -b agree-public-prose-criteria origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named agree-public-prose-criteria, stop and report. Do not touch the main tree.

BASE VERIFICATION: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Confirm origin/main contains commit 650a151e255f22b3eb3f6726735437ef0d1d8bf0 (git merge-base --is-ancestor 650a151e255f22b3eb3f6726735437ef0d1d8bf0 origin/main exits 0); if not, stop and report. Confirm public-prose-criteria.md in the worktree reads status: draft and last-reviewed: null; if not, stop and report. Record origin/main's SHA in your report; branch from it wherever it stands.

EDIT 1 — reviews/expedited-log.md. Append the following line verbatim as the last entry of the file, after the last existing entry, changing nothing else:

- 2026-08-29 — public-prose-criteria.md @ dcb64275d2c69eac7623d3969acf2881343ac4e9 — new: the author-independent prose criteria applied to any author under this method, split from prose-criteria.md; agreed via doc-only cycle (DEC-000240)

Commit reviews/expedited-log.md alone with message "expedited-log: public-prose-criteria.md agreed via doc-only cycle". Push.

EDIT 2 — the flip. Read bin/flip-agreed's usage first (run it with --help or read its header). Then run it once, as a single standalone invocation (never inside a loop), for public-prose-criteria.md with the review pointer exactly:
reviews/expedited-log.md @ dcb64275d2c69eac7623d3969acf2881343ac4e9
If the tool commits, that is the flip commit. If it only edits the file, commit public-prose-criteria.md alone with message "public-prose-criteria.md: agreed". Either way, verify before pushing that the flip commit touches only public-prose-criteria.md and only its frontmatter (git show --stat and git show on the commit; the diff is status: draft → status: agreed and last-reviewed: null → last-reviewed: reviews/expedited-log.md @ dcb64275d2c69eac7623d3969acf2881343ac4e9, nothing else). If the tool fails, or the diff is anything else, stop and report; do not edit frontmatter by hand and do not retry with different flags. Push.

Run bin/check-frontmatter --all from the worktree (must exit 0). Open a pull request from agree-public-prose-criteria to main titled "Agree public-prose-criteria.md (doc-only cycle)" — if gh cannot reach the API (a known sandbox failure), skip the PR, say so in the report, and the decision session opens it. Never merge anything.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-agree-ppc" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; log-entry commit SHA; flip commit SHA and its stat; origin/main SHA branched from; PR number or the gh failure; check-frontmatter exit code; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
