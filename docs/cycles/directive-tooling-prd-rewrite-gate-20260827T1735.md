# Directive: Spec Reviewer gate — directive-tooling PRD rewrite, cycle 21

Role: Spec Reviewer Agent. Reviewed ref: branch directive-tooling-prd-rewrite
@ 0b5a6d4e917bf3471952bc85db4e1214fb52673f (PR #225, base main @
ed46f40429e478189b1e6cabf5528b99df70d3a0).

1. First act — write this directive file verbatim to
   docs/cycles/directive-tooling-prd-rewrite-gate-20260827T1735.md in the
   worktree stated below, commit, push plain (never -u) to
   origin directive-tooling-prd-rewrite, verify by
   `git ls-remote origin directive-tooling-prd-rewrite`, and report the SHA
   read back from git.

WORKING TREE — exclusive assignment. This session works only in
$TMPDIR/fiducial-dt-prd-gate, created:

    git fetch origin
    git rev-parse origin/directive-tooling-prd-rewrite
    # must print 0b5a6d4e917bf3471952bc85db4e1214fb52673f — if not, STOP and surface
    git worktree add --no-track "$TMPDIR/fiducial-dt-prd-gate" -b directive-tooling-prd-rewrite 0b5a6d4e917bf3471952bc85db4e1214fb52673f

If the add fails for any reason, stop and report; do not retry with different
flags, do not delete or create any ref to recover. Any tree mutation you did
not intend, including your own, is a stop condition.

Companions — read all before reviewing:
- specs/directive-tooling.md @ 0b5a6d4e — the document under review.
- docs/cycles/directive-tooling-prd-rewrite-20260827T1700.md @ 0b5a6d4e — the
  decision record: what the rewrite removes and keeps, by Dave's ruling.
- specs/directive-tooling.md @ 3e064f6 (main history) — the prior agreed text,
  for the loss check in step 3.
- specs/prd-template.md, roles/spec-reviewer-agent.md, skills/review-artifact.md
  — template, role, artifact schema.
- skills/directive-authoring.md, docs/global-context/core.md,
  docs/global-context/decision-layer.md, docs/packages/package-a-spec.md §3.6
  and §8.2, decisions/log.md (DEC-000160, DEC-000180), specs/bin-land.md §4 G6
  — the governed sources the document cites.

2. Run the gate review per roles/spec-reviewer-agent.md: template conformance,
   internal consistency, and consistency with every governed source cited.

3. Loss check. Diff the reviewed text against 3e064f6 and report, as findings,
   any requirement, acceptance-criterion clause, fixture, bound, or open
   question whose substance was in the prior text and is absent from the
   rewrite. Cite the prior line and the section where the rewrite should
   carry it. Substance only: Dave's ruling in the decision record removes
   provenance tags, cycle changelog prose, closed §8 questions, and
   per-citation SHAs by design, and their absence is not a finding. A finding
   that asks for any of those back is outside this gate.

4. Write reviews/directive-tooling-cycle-21.md per skills/review-artifact.md,
   verdict first, Prior cycle: reviews/directive-tooling-cycle-20.md. Run
   bin/check-frontmatter --all; it must exit 0 before the push.

5. Commit the review artifact as a second commit on
   directive-tooling-prd-rewrite; push plain to origin
   directive-tooling-prd-rewrite; verify by ls-remote and by reading the
   artifact back at the pushed head; report both commit SHAs and the head.

Do not:
- modify specs/directive-tooling.md or any file other than the directive file
  and reviews/directive-tooling-cycle-21.md — findings go in the artifact,
  never in the document
- merge, open a PR, force-push, or delete any ref

STOP and surface rather than improvise: origin/directive-tooling-prd-rewrite
not at 0b5a6d4e917bf3471952bc85db4e1214fb52673f at fetch; the worktree add
failing; any instruction unexecutable as written; concurrent tree mutation (a
file this session did not change moving, HEAD moving, an index lock).

Report: what was done, not what this file says; all SHAs read back from git;
the check-frontmatter result; the verdict line; findings by severity, the
loss-check findings marked as such; every claim labelled observed / inferred /
told / unknown.
