# Directive: bin/land TRD — Spec Reviewer re-gate, cycle 4

Role: Spec Reviewer Agent. Base: main @ 2246d503ebd3dbf75ca0bd87ff190846d5b8cf31.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-4-20260824T004500Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-4, push, and report the SHA
   read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-trd-review-4 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-4); throwaway scratch
repositories outside it are permitted for evidence-gathering probes. Created:

    git fetch origin
    git rev-parse origin/main
    # must print 2246d503ebd3dbf75ca0bd87ff190846d5b8cf31 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-4" -b bin-land-trd-review-4 2246d503ebd3dbf75ca0bd87ff190846d5b8cf31

Sandbox constraints — read both companions at main 2246d503, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u`;
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate re-check of specs/bin-land-trd.md at main 2246d503 — cycle 4,
   the re-gate over the cycle-3 revision. The document blob is unchanged since
   ff13c838acdfc62324ce6b5d6b0e8e67b5e8cb18. Confirm each disposition in the
   cycle-3 decision record is discharged as decided:
   docs/cycles/bin-land-trd-3-20260824T000622Z.md @
   381dffb7a21462eb0d7c9cc210d19f70984c8319 — D-O2 (§6's "Established" column
   rewritten to one stated rule, all eleven rows), D-B1 (FM-7/FM-8 files
   entries, match null, class unknown, sourced from step 8), D-N1 (branch-
   existed qualifier removed), D-O1 (emitted-not-dropped; "Emitted on" is a
   floor). Nothing was rejected. Plus the full gate re-run and the continuity
   scan per roles/spec-reviewer-agent.md; artifact shape per
   skills/review-artifact.md. Write reviews/bin-land-trd-cycle-4.md, verdict
   first.

3. Assess the three deltas the cycle-3 executor introduced beyond the
   directive's stated scope and named in its report. Enter each as a finding,
   an observation, or a stated clean check:
   a. FM-11's §6 cell gained prior_head "created" — one row beyond D-N1's
      stated three (FM-2, FM-3, FM-4).
   b. AC-LAND-T01 extended to test the FM-7/FM-8 files shape.
   c. §5.2's files rules restated beside the empty-files claim.

4. Rule deliberately on one item the cycle-3 executor named and left
   unresolved: §3.7's step-5 return clause scopes branch_head more loosely
   than §3.2 step 5 and §5.3 do. Read with D-O1's emitted-not-dropped floor,
   it would place branch_head on FM-4 through FM-9 wherever a local <branch>
   exists. The executor took the tighter scoping for the §6 cells and left
   §3.7 unedited, flagging it as a design question. Rule which it is:
   contradiction against §3.2/§5.3, wording ambiguity, or correct as written.

5. Cross-check at minimum, each at main 2246d503: specs/bin-land.md,
   specs/trd-template.md, reviews/bin-land-trd-cycle-3.md,
   docs/cycles/bin-land-trd-3-20260824T000622Z.md,
   docs/global-context/core.md. State Not inspected explicitly.

6. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

7. Land the artifact as a second commit on bin-land-trd-review-4; push plain;
   verify by ls-remote and by reading the file back at the pushed head; report
   the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-4.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session

STOP and surface rather than improvise: origin/main not at
2246d503ebd3dbf75ca0bd87ff190846d5b8cf31 at fetch; any instruction
unexecutable as written; concurrent tree mutation in the assigned worktree.

Report: what was done, not what this file says; all SHAs read back from git;
the check-frontmatter result; the artifact's verdict line and its
Dave-should-inspect list; every claim labelled observed / inferred / told /
unknown.
