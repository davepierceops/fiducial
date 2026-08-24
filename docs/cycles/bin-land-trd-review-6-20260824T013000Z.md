# Directive: bin/land TRD — Spec Reviewer re-gate, cycle 6

Role: Spec Reviewer Agent. Route: fresh execution session. Model tier: frontier.
Base: main @ 8f61e20e3bb92410f60f6e6ef5c5dfc2bb36b3c0.

1. First act — write this directive file verbatim to
   docs/cycles/bin-land-trd-review-6-20260824T013000Z.md in the worktree stated
   below, commit it on branch bin-land-trd-review-6, push plain, verify by
   ls-remote, and report the SHA read back from git.

Worktree — exclusive assignment for repository work. This session's repository
work happens only in $TMPDIR/fiducial-bin-land-trd-review-6 (fallback
/tmp/claude-501/fiducial-bin-land-trd-review-6); throwaway scratch repositories
outside it are permitted for evidence-gathering probes. Created:

    git fetch origin
    git rev-parse origin/main
    # must print 8f61e20e3bb92410f60f6e6ef5c5dfc2bb36b3c0 — if not, STOP and surface
    git worktree add "$TMPDIR/fiducial-bin-land-trd-review-6" -b bin-land-trd-review-6 8f61e20e3bb92410f60f6e6ef5c5dfc2bb36b3c0

Sandbox constraints — read both companions at main 8f61e20e, follow as told:
- docs/cycles/pass2-held-fix-20260823T180753Z.md
- docs/cycles/bin-land-flip-20260823T210300Z.md
  (fetch then verify origin/main before any worktree add; never `git push -u`;
  push plain, verify by ls-remote; worktree paths under $TMPDIR)

2. Run the gate re-check of specs/bin-land-trd.md at main 8f61e20e — cycle 6,
   the re-gate over the cycle-5 revision (document blob unchanged since
   9c776bccb9dd5771235f26ef307b4f3c084f308b). This cycle was a structural
   rewrite, not a disposition list: emission scope was collapsed from three
   homes to one, sixteen passages across eight sections. Review it as such.

   Confirm each cycle-5 disposition is discharged as decided:
   docs/cycles/bin-land-trd-5-20260824T005500Z.md @
   3df2c1f605353b908758251b0890e6f1b0ba1c06 — D5-B1, D5-N1, D5-O1. Nothing was
   rejected.

   The governing principle the cycle was run under: §5.3's key table is the
   single home. For every contract field and detail key, the table states —
   exhaustively and in one place — what it is and on which paths it appears.
   Nothing else in the document makes an independent claim about when a key
   appears. Test the document against that principle, not only against the
   three dispositions.

   Plus the full gate re-run and the continuity scan per
   roles/spec-reviewer-agent.md; artifact shape per skills/review-artifact.md.
   Write reviews/bin-land-trd-cycle-6.md, verdict first.

3. The primary question this cycle: did the collapse hold, or did it leave a
   fourth home? Sweep the whole document independently for any passage that
   states or implies which paths carry which key — including passages the
   cycle-5 executor did not name. Report the sweep result explicitly, including
   "none found" if that is the result. A surviving fourth home is blocking.

4. Rule deliberately on the seam the collapse decided, and rule on the merits
   rather than deferring to the decision:

   detail.branch_head is now scoped to FM-3 alone — the divergence refusal where
   the second check refused. The superseded §3.7 clause put it into the facts
   wherever a local <branch> existed, which under the floor rule would have
   carried it onto FM-4 through FM-9 and the success path. The document
   previously carried both readings; the collapse resolved to the table's.
   Dave has accepted the narrow reading (told, this session's decision record).

   Rule whether the narrow scope is correct on the merits: whether a report on
   FM-4 through FM-9 is impoverished by its absence, whether the table's
   condition ("the ref whose check refused") is well-formed and decidable on
   every path, and whether anything else in the document still assumes the wide
   reading. If you conclude the narrow scope is wrong, say so plainly and state
   the fix; Dave's acceptance is not a constraint on your verdict.

5. Assess the five deltas the cycle-5 executor introduced beyond the directive's
   stated scope and named in its report. Enter each as a finding, an
   observation, or a stated clean check:
   a. §5.2's always-present bullet extended to name detail.
   b. §5.3's column extended to name the success path for base, local_head,
      remote_head and prior_branch.
   c. §6's detail.stage column declared derived from §5.3's token table.
   d. FM-4's explicit "No detail.prior_branch" negative removed.
   e. Line 917 rewrapped (cosmetic, carried from cycle 4).

6. Independently verify the executor's mechanical consistency claim rather than
   accepting it: it reports that a script parsed §6's eleven rows and compared
   all twelve keys against §5.3's "Established on" column, finding all ten
   detected modes in agreement and FM-10 emitting nothing. Re-derive that
   comparison yourself, by whatever means you judge sound, and state whether it
   holds. Label the result observed or inferred accordingly.

7. Cross-check at minimum, each at main 8f61e20e: specs/bin-land.md,
   specs/trd-template.md, reviews/bin-land-trd-cycle-4.md,
   docs/cycles/bin-land-trd-5-20260824T005500Z.md, docs/global-context/core.md.
   Confirm the TRD still satisfies AC-LAND-06, AC-LAND-07 and AC-LAND-09 as
   floors after the collapse. State Not inspected explicitly.

8. Run bin/check-frontmatter --all in the worktree; it must exit 0 before the
   artifact is pushed.

9. Land the artifact as a second commit on bin-land-trd-review-6; push plain;
   verify by ls-remote and by reading the file back at the pushed head; report
   the head SHA and both commit SHAs.

Do not:
- modify specs/bin-land-trd.md or any other existing file — findings are
  reported in the artifact, never applied to the document under review; the
  blast radius is this directive file and reviews/bin-land-trd-cycle-6.md only
- merge, open a PR, force-push, or delete any ref — merging is handled from the
  decision session

STOP and surface rather than improvise: origin/main not at
8f61e20e3bb92410f60f6e6ef5c5dfc2bb36b3c0 at fetch; any instruction unexecutable
as written; concurrent tree mutation in the assigned worktree.

Report: what was done, not what this file says; all SHAs read back from git; the
check-frontmatter result; the section-3 sweep result explicitly; the artifact's
verdict line and its Dave-should-inspect list; every claim labelled observed /
inferred / told / unknown.
