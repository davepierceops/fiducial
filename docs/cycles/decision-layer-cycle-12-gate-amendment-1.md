AMENDMENT 1 — Decision Layer gate directive (c3e21dafcc92025e09e48937707e30dac0a8b05b)

Target session: the session holding the worktree at "$TMPDIR/fiducial-decision-layer-cycle-12-gate" on branch decision-layer-cycle-12-gate. Route: existing session. Model: unchanged.

Your stop is accepted and correct. The directive's cycle number was wrong: reviews/decision-layer-cycle-12.md and cycle-13 exist from 2026-08-23; the next free number is 14. The review's content stands as reviewed; only its landing was wrong. Everything in the original directive not amended here still binds.

FIRST ACT

Write this amendment verbatim to docs/cycles/decision-layer-cycle-12-gate-amendment-1.md in the assigned worktree, commit it alone, push the branch, and report the SHA. Do not edit the committed directive file.

THEN

1. Restore the overwritten record and re-land the review, in one commit:
   git checkout 3e89a2117e35f34746aff005c19bc3c6227bf8f4 -- reviews/decision-layer-cycle-12.md
   then write the review artifact to reviews/decision-layer-cycle-14.md with these corrections and no others: the header names cycle 14; the Prior cycle line reads reviews/decision-layer-cycle-13.md; any other internal self-reference to cycle 12 becomes cycle 14. Disclose every corrected line in the report. Commit both paths together with a message naming the restoration and the re-landing.
2. Verify by running, output captured beside the earlier logs: git diff 3e89a2117e35f34746aff005c19bc3c6227bf8f4 HEAD --stat — expected: exactly three paths across the branch (the directive file, this amendment file, reviews/decision-layer-cycle-14.md), and reviews/decision-layer-cycle-12.md absent from the diff. If cycle-12 appears in that diff, stop and report.
3. Push the branch; judge by the refs ls-remote reports. Do not use -u.
4. Remove the worktree; report removal status.
5. Report: the amendment commit SHA, the restore-and-reland commit SHA, the branch tip from ls-remote, the diff-stat line, every corrected self-reference, and the verdict line restated verbatim. Label every claim.

Do not open a pull request; the decision session opens it, into decision-layer-human-review.
