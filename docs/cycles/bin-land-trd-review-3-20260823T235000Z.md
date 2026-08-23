# Directive: bin/land TRD — Spec Reviewer re-gate, cycle 3

Role: Spec Reviewer Agent. Base: main @ 3412e25837a8556e0ae74d65e33037bff06184a0.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-3-20260823T235000Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-3, push, and report the SHA
   read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-trd-review-3 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-3); throwaway scratch
repositories outside it are permitted for evidence-gathering probes. Created:

    git fetch origin
    git rev-parse origin/main
    # must print 3412e25837a8556e0ae74d65e33037bff06184a0 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-3" -b bin-land-trd-review-3 3412e25837a8556e0ae74d65e33037bff06184a0

Sandbox constraints — read both companions at main 3412e258, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u` —
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate re-check of specs/bin-land-trd.md @ 3412e258 — cycle 3, the
   re-gate over the cycle-2 revision. Confirm each disposition in the cycle-2
   decision record is discharged as decided:
   docs/cycles/bin-land-trd-2-20260823T232718Z.md @ f02a1330. Assess the two
   fixes the revision's executor made under its directed §3.7 sweep and named
   in its report: step 10's returns gaining remote_head, and branch as the
   first stated exception to §3.7's leaf rule. Plus the full gate re-run and
   the continuity scan per roles/spec-reviewer-agent.md; artifact shape per
   skills/review-artifact.md. Write reviews/bin-land-trd-cycle-3.md, verdict
   first.

3. Rule deliberately on two pre-existing items the cycle-2 executor named and
   left unresolved — both byte-identical to the original draft at 47758d14;
   assess each on its merits and enter it in the artifact as a finding, an
   observation, or a stated clean check:
   a. prior_head in the branch-absent arm: §3.2 step 3 establishes it as the
      literal "created" and §3.7 has step 3 return it unconditionally, but
      §6's FM-2, FM-3, and FM-4 rows read "prior_head where the branch
      existed", which reads as unknown in the branch-absent arm. Contradiction
      or wording ambiguity — rule which.
   b. files on FM-7 and FM-8: a commit exists on both paths, but §3.7 sources
      files only from step 10, so the report carries []. §5.2's disclaimer
      that [] is not a claim about the commit is scoped to no-commit paths —
      so on exactly the two paths where a commit exists, [] is unqualified.
      FM-7 is PRD §7's accepted-risk state; rule whether the shape as written
      misreports it.

4. Cross-check at minimum, each at main 3412e258: specs/bin-land.md,
   specs/trd-template.md, reviews/bin-land-trd-cycle-2.md,
   docs/cycles/bin-land-trd-2-20260823T232718Z.md,
   docs/global-context/core.md. State Not inspected explicitly.

5. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

6. Land the artifact as a second commit on bin-land-trd-review-3; push plain;
   verify by ls-remote and by reading the file back at the pushed head; report
   the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-3.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session

STOP and surface rather than improvise: origin/main not at
3412e25837a8556e0ae74d65e33037bff06184a0 at fetch; any instruction unexecutable
as written; concurrent tree mutation in the assigned worktree (a file this
session did not change moving, HEAD moving, an index lock).

Report: what was done, not what this file says; all SHAs read back from git;
the check-frontmatter result; the artifact's verdict line and its
Dave-should-inspect list; every claim labelled observed / inferred / told /
unknown.
