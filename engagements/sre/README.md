---
status: draft
last-reviewed: null
audience: [assistant, cartographer, critic, implementer, human]
---

# Engagement Pack

This file is for decision sessions and execution sessions within an engagement.

This pack adapts the parent operating model for client engagement work:
brownfield SRE work inside a system the client owns, runs, and is responsible
for.

## What an engagement inverts

### The system precedes the spec

The parent model is spec-first. An engagement starts inside a running system
that is partly undocumented and partly hidden. Discovery therefore precedes
specification, and the artifact chain is:

**System Map** (discovered) → **Measurement Baseline** (the instrumented truth
about where time goes) → **Improvement Proposal** (a change with a stated
expected delta) → **change package**.

The Cartographer builds the map; system discovery is what produces it.

### The red-gate becomes the baseline-gate

**The baseline is the failing test.** No optimization is implemented until the
stopwatch exists, the baseline distribution is captured, and the expected delta
is stated in advance. Baseline measurement is what produces the Measurement
Baseline.

### Ownership becomes guest posture

Changes land as pull requests through the client's own gates; nothing is
pushed. An engagement has no release gate. Release is the client's concern, not
this role's; do not inquire into or reason about the client's release timing.

### Ceremony has a floor and an override log

The engagement runs the minimum ceremony that preserves the evidence chain: the
baseline-gate, a lean change package, and clean-context Critic review where one
is requested. A Critic read is advisory; its verdict is input to Dave and gates
nothing. Every ceremonial element is trivially overridable by Dave, the
override is logged, and the log is reviewed at the engagement review.

## Artifacts

- **System Map** — pipeline narrative, stage table, claim provenance, unknowns,
  and the proposed measurement plan; one document in the engagement working
  area, small enough to read in one sitting.
- **Measurement Baseline** — per-stage p50 and p95, the total, the date range,
  the run count, and known confounds; one document beside the System Map.
- **Improvement Proposal** — one screen: target stage with its baseline cite,
  the change, the expected delta stated in advance, effort estimate and blast
  radius with rollback path, and draft acceptance criteria; in the engagement
  working area.
- **engagement working area** — the client-hosted repository designated at
  kickoff. Every engagement artifact lives here.
- **baseline-gate** — the standing condition that a Measurement Baseline
  covering the affected stage exists and the expected delta is stated before
  an optimization is implemented.
- **A record with no fixed filename, created on first use, kept in the
  engagement working area** — the shape the override log and the Assistant's
  loose-end record both take.
