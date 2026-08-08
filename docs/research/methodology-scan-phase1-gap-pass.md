---
status: draft
last-reviewed: null
audience: [research-agent, human]
purpose: A bounded second discovery pass against the existing catalog as a known-set, to distinguish real saturation from a budget-limited first pass. Variant of Phase 1.
depends-on: []
---

# Directive: External Methodology Scan — Phase 1 Gap-Pass

## Intent

A bounded second discovery pass over the seed traditions, run against the
existing catalog as a known-set, to surface distinct-and-adoptable practices the
first pass missed. Same traditions, same blindness, different queries.

## Inputs

- `methodology-scan-catalog.md`, provided in the working directory — the
  **known-set**. Every practice in it is already found. Do not re-add it.

## Blindness constraint

The catalog is now an allowed input. The methodology corpus is not.

- Do not fetch, open, or reference any document under `davepierceops/ai`, any
  context bundle, or any project methodology text.
- The provided catalog is the only prior input. It was produced blind and holds
  no project methodology; using it as a known-set leaks nothing.
- If the methodology corpus is in your context, this is the wrong session. Stop
  and report that.

## Novelty criterion — same-mechanism

A candidate is new only if no existing catalog entry shares its **mechanism** —
the change it would translate into. Same practice in different words is a
duplicate. Different wording is not novelty; a different mechanism is.

- Check every candidate against the known-set by mechanism, not by phrasing.
- When unsure whether a candidate duplicates an existing entry, record it and
  mark `possible-dup of <id>`. Do not silently drop it; do not silently merge.

## Query diversification

The first pass's queries are visible in the catalog's sources. Do not repeat
them. Reach the same traditions from different angles:

- failure-mode framings (how a tradition prevents a specific failure),
- primary-source framings (standard numbers, canonical authors, seminal papers),
- alternative vocabulary for the same practice.

Saturation under one query framing is not saturation of the tradition.

## Discipline

Same bar as the first pass:

- One atomic practice per entry; provenance required; stated claim separated
  from inference; source quality flagged; no adoption judgment.
- Match the entry schema of the provided catalog exactly. Continue entry IDs
  from the catalog's last ID so a later merge does not collide.
- Snippet-first. Fetch a full page only when a mechanism cannot be captured
  otherwise.
- **Distinct-and-adoptable, not more count.** A shallow or near-duplicate entry
  is noise the next phase has to wade through. Reject it rather than pad.

## Budget and stop

- Hard ceiling: **15 web searches.**
- Stop early when diversified queries across the traditions stop yielding
  mechanism-distinct practices.
- Checkpoint: write output after every ~5 new entries.

## Output

- Write new entries to `./methodology-scan-catalog-gap.md` — separate from the
  source catalog, so the yield stays inspectable.
- End with a **yield report**:
  - new mechanism-distinct entries added (count),
  - candidates rejected as duplicates by mechanism (count),
  - per tradition: new finds, or none,
  - searches used,
  - traditions where diversified queries still returned only known practices —
    these are genuinely saturated.

## Dispatch

- **Route:** fresh session.
- **Model floor:** Sonnet. The dedup-by-mechanism judgment is the load-bearing
  work here; Haiku is below the floor.
- **Track:** Track B. Wherever this directive says *write*, the executor writes
  to the working directory; the operator lands the result.
- **Isolation:** run from a scratch directory that contains only this directive
  and `methodology-scan-catalog.md`, and nothing from the methodology repo —
  blindness stays structural.
- **Attended posture:** confirm the first checkpoint write appears before
  stepping away; review the yield report on return.
