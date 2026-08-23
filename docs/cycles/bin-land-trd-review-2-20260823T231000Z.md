# Directive: bin/land TRD — Spec Reviewer re-gate, cycle 2

Role: Spec Reviewer Agent. Base: main @ be52de1661f80dc1923390f76b808056df638be6.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-2-20260823T231000Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-2, push, and report the SHA
   read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-trd-review-2 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-2); throwaway scratch
repositories outside it are permitted for evidence-gathering probes. Created:

    git fetch origin
    git rev-parse origin/main
    # must print be52de1661f80dc1923390f76b808056df638be6 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-2" -b bin-land-trd-review-2 be52de1661f80dc1923390f76b808056df638be6

Sandbox constraints — read both companions at main be52de16, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u` —
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate re-check of specs/bin-land-trd.md @ be52de16 — cycle 2, the
   re-gate over the cycle-1 revision. Confirm each of the twelve cycle-1
   dispositions is discharged as the cycle-1 directive decided:
   docs/cycles/bin-land-trd-1-20260823T221914Z.md @ 3de6098b is the decision
   record. Assess the four items the revision's executor flagged: the §3.7
   placement of B6's interfaces, AC-LAND-T01a as a new criterion, the
   exact-ref-selection extension at §3.2 step 3, and the step-4
   refuse-without-asserted-cause extension. Plus the full gate re-run and the
   continuity scan per roles/spec-reviewer-agent.md; artifact shape per
   skills/review-artifact.md. Write reviews/bin-land-trd-cycle-2.md, verdict
   first.

3. Cross-check at minimum, each at main be52de16: specs/bin-land.md,
   specs/trd-template.md, reviews/bin-land-trd-cycle-1.md,
   docs/global-context/core.md. State Not inspected explicitly.

4. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

5. Land the artifact as a second commit on bin-land-trd-review-2; push plain;
   verify by ls-remote and by reading the file back at the pushed head; report
   the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-2.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session

STOP and surface rather than improvise: origin/main not at
be52de1661f80dc1923390f76b808056df638be6 at fetch; any instruction unexecutable
as written; concurrent tree mutation in the assigned worktree (a file this
session did not change moving, HEAD moving, an index lock).

Report: what was done, not what this file says; all SHAs read back from git;
the check-frontmatter result; the artifact's verdict line and its
Dave-should-inspect list; every claim labelled observed / inferred / told /
unknown.
