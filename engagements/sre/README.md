---
status: draft
last-reviewed: null
audience: [assistant, cartographer, skeptic, implementer, human]
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

The Cartographer builds the map; the system-discovery skill is the procedure.

### The red-gate becomes the baseline-gate

**The baseline is the failing test.** No optimization is implemented until the
stopwatch exists, the baseline distribution is captured, and the expected delta
is stated in advance. The baseline-measurement skill is the procedure.

### Ownership becomes guest posture

Everything lands as a pull request; nothing is pushed. The client's humans hold
the release gate on their own systems.

### Ceremony has a floor and an override log

The engagement runs the minimum ceremony that preserves the evidence chain: the
baseline-gate, a lean change package, and clean-context Skeptic review where one
is requested. Every ceremonial element is trivially overridable by Dave, the
override is logged, and the log is reviewed at the engagement retro.

## Key principles

1. Manage the proof, not the code — and in an engagement, the first proof is
   the measurement.
2. Discovery precedes specification.
3. The baseline is the failing test.
4. Changes land as pull requests through the client's own gates.
5. Ceremony is minimal, overridable, and every override is logged.
