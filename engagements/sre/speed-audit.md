---
status: draft
last-reviewed: null
audience: [assistant, cartographer, skeptic, implementer, human]
---

# Skill: Speed Audit

This skill runs in a decision session.

The end-to-end engagement play for "make X faster," sized to a one-week
engagement. Composes the other engagement skills; the roles execute their
parts.

## The play

1. **Discover** — the Cartographer maps the pipeline by the system-discovery
   procedure; unknowns go to Dave; Dave decides what to ask the client.
2. **Baseline** — capture per-stage distributions by the baseline-measurement
   procedure. Change nothing yet. This is typically days one and two.
3. **Rank** — order stages by cost at p50 and p95. Present the ranking with the
   evidence.
4. **Propose** — for the top stages, the Assistant drafts Improvement Proposals.
   Dave selects with the client's priorities in mind.
5. **Attack** — the Implementer builds; the Skeptic reviews where a review is
   requested; changes land as pull requests through the client's own gates;
   re-measure after each landing, not in batches.
6. **Write up** — before/after distributions, the remaining ranked
   opportunities, and the recommendation. Written for the client's engineers to
   keep, in their vocabulary, citing their systems.

## The Improvement Proposal

One screen, drafted by the Assistant from the Cartographer's map and the
baseline. The Cartographer does not propose; the Implementer does not
self-authorize.

- target stage, with baseline cite (p50/p95)
- the change
- expected delta, stated in advance
- effort estimate and blast radius, with rollback path
- draft acceptance criteria

**Agreed** means Dave says yes; the proposal records it and the change package
cites it. The acceptance criteria are agreed in the same breath.
