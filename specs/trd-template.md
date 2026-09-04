---
status: in-review
last-reviewed: null
audience: [architect-agent, spec-reviewer-agent, human]
---

# Technical Requirements Document (TRD) — Template

This template is read in a decision session drafting a TRD and in an execution
session gating one.

## What this is

The TRD is the **standing technical specification** for the project. It is
canonical: it is the authoritative description of *how* the system is built,
sitting directly beneath the PRD (which owns *what* is built and *why*).

The TRD is slow-moving. It changes when the architecture changes, not once per
feature. Per-feature technical design does **not** live here — it lives in the
per-change **architecture summary** the Architect Agent produces for each unit
of work.

## Authorship

- **Drafted by:** the Architect Agent.
- **Agreed by:** Dave (PM/EM/Owner). The TRD is not in force until Dave agrees.
- **Maintained by:** whoever holds the Architect role for a change that alters
  standing architecture updates this document as part of that change.

## Relationship to other artifacts

```
PRD  (product, standing)        ← what / why, Dave owns
  └─ TRD (technical, standing)   ← how, Architect drafts / Dave agrees   [THIS DOC]
```

The TRD is the durable technical anchor. Tracker issues are **derived** from it,
via the per-change architecture summary.

---

## Required sections

A complete TRD must contain the following. Keep each section as short as it can
be while still being a real answer; this is an anchor, not an essay.

### 1. System overview
The shape of the system in a few sentences: major components and how they fit.
What kind of system this is (service, app, PWA, CLI, etc.).

### 2. User journeys and SLOs

For each of the PRD's Top K journeys, define:

- **SLO**: the service level objective — what "good enough" looks like for this
  journey in production. Examples: p95 latency, success rate, error budget.
- **Measurement mechanism**: how the SLO is observed (telemetry, synthetic
  checks, user-facing error rates, etc.).
- **Alerting threshold**: at what point a breach triggers action.

SLOs here are the technical instantiation of the user outcomes the PRD defines.
If a journey has no SLO, name it explicitly as unverified and record it as an
open question.

### 3. Architecture and boundaries
- Components and their responsibilities.
- Interfaces between components.
- External dependencies (APIs, providers, data stores, auth, browser/PWA
  surfaces).
- The important **boundaries** — the points where this system meets something
  it does not control. Declare each durable boundary: name the production
  surface, how it is currently represented, and what verifying it would take.

### 4. Verification boundaries (standing)
This is the TRD's link to the evidence model. For each material standing
boundary, name:
- the production surface,
- how it is currently represented (live / contract / mock / assumed),
- its evidence class,
- the deferred-verification path, if any.

This section instantiates the durable boundary types that apply to *this*
system. Per-change boundary movement is recorded in the change's architecture
summary and boundary audit, not here — but if a change makes a boundary
movement permanent, reflect it here.

### 5. Data and state
Key data shapes, persistence, ownership, and lifecycle. Where state lives and
who is authoritative for it.

### 6. Failure modes and recovery
For the system as a whole: how it fails, how failure is detected, what the user
sees, and how it recovers or is rolled back. (Per-change failure analysis lives
in the change package; this is the standing picture.)

### 7. Operational concerns
Observability, configuration/secrets, quotas/billing exposure, deployment
assumptions, and anything required to operate the system responsibly.

State this project's **release model**: whether deploy and release are separate
events, and where the release decision sits relative to commit and deploy. If
they are separate, name the flag mechanism as a flag backend chosen in the TRD
and swappable.

### 8. Constraints, NFRs, and non-goals

Technical constraints the design must respect. This section is the technical
instantiation of the PRD's non-functional goals. For each NFR dimension defined
in the PRD, state the concrete technical target or constraint here, or
explicitly mark it N/A for this system:

- **Performance**: specific latency/throughput targets and how they are enforced.
- **Reliability**: uptime targets, error budgets, retry/fallback strategies.
- **Scalability**: load model, bottlenecks, growth headroom.
- **Security**: auth mechanism, data protection approach, threat surface.
- **Maintainability**: modularity decisions, dependency constraints, debt policy.
- **Usability**: technical constraints serving UX goals (e.g. bundle size, TTI).
- **Observability**: what is instrumented, how, and where it surfaces.
- **Portability / Compatibility**: runtime, platform, and API version constraints.
- **Compliance**: technical controls required by regulatory or legal NFRs.

Also state explicit technical non-goals — things this architecture deliberately
does not attempt. Prefer boring, understandable designs.

### 9. Open technical questions
Standing unknowns that need resolution. Each should name what would resolve it.
Keep them as loose ends rather than relying on memory.

---

## Skeleton (copy this into a project TRD)

```markdown
---
status: draft
last-reviewed: null
audience: [human]
---

# TRD: <project name>

## 1. System overview
## 2. User journeys and SLOs
## 3. Architecture and boundaries
## 4. Verification boundaries (standing)
## 5. Data and state
## 6. Failure modes and recovery
## 7. Operational concerns
## 8. Constraints, NFRs, and non-goals
## 9. Open technical questions
```
