# Directive: bin/land TRD — Spec Reviewer re-gate, cycle 8

Role: Spec Reviewer Agent. Route: fresh execution session. Model tier: frontier.
Base: main @ 49a71eb6dbd8018b4119e3ec9e405fd0e8cdade0.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-8-20260824T020500Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-8, push plain, verify by
   ls-remote, and report the SHA read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-trd-review-8 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-8); throwaway scratch repositories
outside it are permitted for evidence-gathering probes. Created:

    git fetch origin
    git rev-parse origin/main
    # must print 49a71eb6dbd8018b4119e3ec9e405fd0e8cdade0 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-8" -b bin-land-trd-review-8 49a71eb6dbd8018b4119e3ec9e405fd0e8cdade0

Sandbox constraints — read both companions at main 49a71eb6, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u`;
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate re-check of specs/bin-land-trd.md at main 49a71eb6 — cycle 8,
   the re-gate over the cycle-7 revision (document blob unchanged since
   d8506d2a018414731bb1cb74ccc7793230b634f5).

   Confirm each cycle-7 disposition is discharged as decided:
   docs/cycles/bin-land-trd-7-20260824T015000Z.md @
   a6c0f323e85d8c42a62cee63d1c2d08aae71dfc6 — D7-N1, D7-B1, D7-N2, D7-N3, plus
   the two cycle-6 observations. Nothing was rejected.

   Plus the full gate re-run and the continuity scan per
   roles/spec-reviewer-agent.md; artifact shape per skills/review-artifact.md.
   Write reviews/bin-land-trd-cycle-8.md, verdict first.

   Standing context: §5.3's key table is the single home for emission scope,
   confirmed by cycle 6's independent sweep. As of cycle 7 its "Established on"
   column is exact — a ceiling as well as a floor. Test the document against
   both properties, not only against the dispositions.

3. The primary question this cycle: did reversing the emission rule leave a
   passage written against the old direction? A floor and a ceiling forbid
   different things, so a sentence true under the floor can be false under the
   ceiling while reading identically. Sweep the whole document independently for
   any passage that permits, assumes, or tolerates a key appearing outside the
   paths §5.3 names — including passages the cycle-7 executor did not name.
   Report the sweep result explicitly, including "none found". A surviving
   floor-era passage is blocking.

4. Rule deliberately on a seam the cycle-7 executor named and did not close:
   §3.2 step 5 promises the report says which of the two checks refused. The
   executor's position is that this is now satisfied without an edit — under
   D7-B1 and D7-N2, detail.branch_head present implies the second check refused
   and absent implies the first did, since the second only runs after the first
   passes and is skipped where <branch> is absent locally. Its own claim class
   for this was inferred by reading.

   Rule whether a promise satisfied only by inference satisfies it: whether the
   derivation is sound on every path, whether an implementer reading §3.2 step 5
   would arrive at it unaided, and whether the document should state the
   correspondence rather than leave it derivable. State the fix if you conclude
   it should be stated.

5. Assess the four deltas the cycle-7 executor introduced beyond a decision's
   stated scope and named in its report. Enter each as a finding, an
   observation, or a stated clean check:
   a. §5.2's shape example populated for one named path, with a template
      disclaimer.
   b. The cycle-6 O2 citation move on §5.2's prior_head value-domain rule.
   c. "The one absence rule" renamed "the one emission rule" in two places.
   d. The §3.3, §3.4, OQ-2 and OQ-5 rewordings — flagged by the executor
      because they touch an open question's argument text.

6. Independently verify, rather than accepting, the two claims the cycle-7
   executor labelled inferred by reading and on which the ceiling's correctness
   rests:
   a. §5.3's four success-path column entries (base, local_head, remote_head,
      prior_branch) are correct as normative requirements now that the column is
      exact.
   b. §6's eleven cells agree with the twelve table rows in both directions
      under the ceiling — no cell naming a key the table does not establish on
      that path, none omitting one it does.
   Re-derive both by whatever means you judge sound and label the result
   observed or inferred accordingly.

7. Cross-check at minimum, each at main 49a71eb6: specs/bin-land.md,
   specs/trd-template.md, reviews/bin-land-trd-cycle-6.md,
   docs/cycles/bin-land-trd-7-20260824T015000Z.md, docs/global-context/core.md.
   Confirm the TRD still satisfies AC-LAND-06, AC-LAND-07 and AC-LAND-09 as
   floors under the ceiling — the executor's position is that the ceiling
   strengthens AC-LAND-09 rather than threatening it; verify that. State Not
   inspected explicitly.

8. State in the artifact, as its own line, whether this document is ready for
   Dave's agreement, and if not, the shortest path to it. Four cycles have each
   returned exactly one blocking finding while the findings themselves have
   moved from structural to residual; say plainly whether that trend is real or
   whether the document still has a systemic defect. Verdict remains yours —
   ready means ready for Dave's agreement, never agreed.

9. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

10. Land the artifact as a second commit on bin-land-trd-review-8; push plain;
    verify by ls-remote and by reading the file back at the pushed head; report
    the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-8.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session
- treat bin/tests/run's two pre-existing AC-BN-10 bundle failures as in scope;
  they predate this base and belong to the bundle work

STOP and surface rather than improvise: origin/main not at
49a71eb6dbd8018b4119e3ec9e405fd0e8cdade0 at fetch; any instruction unexecutable
as written; concurrent tree mutation in the assigned worktree.

Report: what was done, not what this file says; all SHAs read back from git; the
check-frontmatter result; the section-3 sweep result explicitly; the section-8
readiness statement; the artifact's verdict line and its Dave-should-inspect
list; every claim labelled observed / inferred / told / unknown.
