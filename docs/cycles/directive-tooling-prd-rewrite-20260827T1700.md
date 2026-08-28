# Decision record: directive-tooling PRD rewrite

Base: main @ ed46f40429e478189b1e6cabf5528b99df70d3a0. Written and pushed from
the decision session over the repository connector; no execution session.

## Ruling

Dave, 2026-08-27, in the decision session: `specs/directive-tooling.md` at
`3e064f6` (agreed) is replaced whole by a rewrite carrying substance only.
Dave read the rewrite in the artifact pane and said "ship".

## What the rewrite removes

- The preamble indexing every cycle directive and SHA.
- Per-sentence provenance tags (`*told*`, `*observed*`) and the cycle-by-cycle
  changelog prose ("previously read X; the cycle-N gate found Y").
- Closed §8 questions Q3, Q7, Q8; one line points at `docs/cycles/` for the
  rulings.
- SHAs on citations of governed files; the TRD pins them.

## What the rewrite keeps

§1 problem statement and incident; G0–G11; the M1–M8 table; the judgment-only
set; NFRs; non-goals; §5 outcomes; AC-DT-01 through AC-DT-19 under their
existing identifiers; §7 accepted and not-accepted risks; §8 Q1, Q2, Q4, Q5,
Q6, Q9, Q10 with their resolvers.

## Status

The rewrite lands as `status: draft`, `last-reviewed: null`. It returns to
`agreed` only through the Spec Reviewer gate and Dave's agreement; the gate
directive is issued separately and cites this commit.
