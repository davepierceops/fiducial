---
status: draft
last-reviewed: null
audience: [assistant, cartographer, critic, implementer, human]
---

# Skill: Speed Audit

Runs in a decision session. The Cartographer, Implementer, and Critic read it
for the steps assigned to them; they do not run the play.

The end-to-end engagement play for "make X faster," sized to a one-week
engagement. Composes the other engagement skills; the roles execute their
parts.

## The play

1. **Discover** — the Cartographer maps the pipeline, producing the System Map;
   unknowns go to the Assistant in the Cartographer's report; the Assistant
   carries to Dave what needs his decision, and Dave decides what to ask the
   client.
2. **Baseline** — capture per-stage distributions, producing the Measurement
   Baseline. Change nothing yet. This is typically days one and two.
3. **Rank** — order stages by cost at p50 and p95. Present the ranking with the
   evidence.
4. **Propose** — for the top stages, the Assistant drafts Improvement Proposals.
   Dave selects with the client's priorities in mind.
5. **Attack** — the Implementer builds; the Critic reviews where a review is
   requested; the Cartographer re-measures against the baseline, after each landing, not in batches.
6. **Write up** — before/after distributions, the remaining ranked
   opportunities, and the recommendation. Written for the client's engineers to
   keep, in their vocabulary, citing their systems.

## The Improvement Proposal

Drafted by the Assistant from the Cartographer's map and the baseline, in the
shape the Artifacts list states. The Cartographer does not propose; the
Implementer does not self-authorize.

**Dave's go:** the proposal records it and the change package cites it. The go
covers the acceptance criteria in the same breath.
