# Directive: bin/land TRD — Spec Reviewer gate, cycle 1

Role: Spec Reviewer Agent. Base: main @ b82dc36407d703df50347fa8ad7f8ef0f80453c1.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-20260823T214500Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-1, push, and report the SHA
   read back from git.

Worktree — exclusive assignment. This session works only in
$TMPDIR/fiducial-bin-land-trd-review-1 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-1), created:

    git fetch origin
    git rev-parse origin/main
    # must print b82dc36407d703df50347fa8ad7f8ef0f80453c1 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-1" -b bin-land-trd-review-1 b82dc36407d703df50347fa8ad7f8ef0f80453c1

Sandbox constraints — read both companions at main b82dc364, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u` —
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate review of specs/bin-land-trd.md @ b82dc364 — the first cycle
   over this document. What must be inspected and reported is governed by
   roles/spec-reviewer-agent.md; the artifact's shape by
   skills/review-artifact.md. Write the artifact to
   reviews/bin-land-trd-cycle-1.md, verdict first.

3. Cross-check at minimum, each at main b82dc364: specs/bin-land.md (the PRD,
   agreed — the spine is two documents now, so PRD→TRD traceability is
   checkable across artifacts for the first time in this series; check it and
   say so), specs/trd-template.md, reviews/bin-land-cycle-4.md, -5.md, -7.md
   (the ridden observations the TRD was directed to address),
   docs/global-context/core.md. State Not inspected explicitly.

4. The TRD's §9 carries OQ-1 through OQ-10. Confirm each names what would
   resolve it, per the role's gate item.

5. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

6. Land the artifact as a second commit on bin-land-trd-review-1; push plain;
   verify by ls-remote and by reading the file back at the pushed head; report
   the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-1.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session

STOP and surface rather than improvise: origin/main not at
b82dc36407d703df50347fa8ad7f8ef0f80453c1 at fetch; any instruction unexecutable
as written; concurrent tree mutation (a file this session did not change
moving, HEAD moving, an index lock).

Report: what was done, not what this file says; all SHAs read back from git;
the check-frontmatter result; the artifact's verdict line and its
Dave-should-inspect list; every claim labelled observed / inferred / told /
unknown.
