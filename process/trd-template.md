---
order: 30
role: [architect-agent, spec-reviewer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: TRD Template

Read in a decision session drafting a TRD and in an execution session gating
one. This document is the form; the obligations an agent performs when it
drafts, gates, or maintains a TRD are rows in the store under topic `trd`.

## What this is

The TRD is the standing technical specification for the project. It is
canonical: the authoritative description of *how* the system is built, sitting
directly beneath the PRD, which owns *what* is built and *why*.

The TRD is slow-moving. It changes when the architecture changes, not once per
feature. Per-feature technical design does not live here — it lives in the
per-change architecture summary the Architect Agent produces for each unit of
work. The TRD is the durable technical anchor; tracker issues are derived from
it, by way of that summary.

The Architect Agent drafts it. Dave agrees it, and it is not in force until he
has. Whoever holds the Architect role for a change that alters standing
architecture updates this document as part of that change.

## Required sections

Keep each section as short as it can be while still being a real answer. This is
an anchor, not an essay.

### 1. System overview

The shape of the system in a few sentences: its major components, how they fit
together, and what kind of system it is — service, app, PWA, CLI.

### 2. User journeys and SLOs

For each of the PRD's Top K journeys:

- **SLO** — what "good enough" looks like for this journey in production: p95
  latency, success rate, error budget.
- **Measurement mechanism** — how the SLO is observed: telemetry, synthetic
  checks, user-facing error rates.
- **Alerting threshold** — the point at which a breach triggers action.

SLOs here are the technical instantiation of the user outcomes the PRD defines.
Where a journey has no SLO, name it explicitly as unverified and record it as an
open question.

### 3. Architecture and boundaries

- Each component and what it is responsible for.
- The interfaces between components.
- External dependencies: APIs, providers, data stores, auth, browser and PWA
  surfaces.
- The boundaries where the system meets something it does not control. Declare
  each durable one: the production surface, how it is currently represented, and
  what verifying it would take.

### 4. Verification boundaries (standing)

The TRD's link to the evidence model. For each material standing boundary:

- the production surface,
- how it is currently represented — live, contract, mock, or assumed,
- its evidence class,
- the deferred-verification path, if any.

This section instantiates the durable boundary types that apply to *this*
system. Per-change boundary movement is recorded in the change's architecture
summary and boundary audit, not here; where a change makes a boundary movement
permanent, it is reflected here.

### 5. Data and state

Key data shapes, their persistence, ownership, and lifecycle. Where state lives
and who is authoritative for it.

### 6. Failure modes and recovery

For the system as a whole: how it fails, how a failure is detected, what the
user sees, and how it recovers or is rolled back. Per-change failure analysis
lives in the change package; this is the standing picture.

### 7. Operational concerns

Observability, configuration and secrets, quota and billing exposure, deployment
assumptions, and anything else required to operate the system responsibly.

State the project's release model: whether deploy and release are separate
events, and where the release decision sits relative to commit and deploy. Where
they are separate, name the flag mechanism as a flag backend chosen in the TRD
and swappable.

Name the mechanism that routes a go/no-go response back into the workflow.

### 8. Constraints, NFRs, and non-goals

The technical constraints the design must respect — the technical instantiation
of the PRD's non-functional goals. For each NFR dimension the PRD defines, state
the concrete technical target or constraint here, or mark it explicitly `N/A`
for this system:

- **Performance** — specific latency and throughput targets, and how they are
  enforced.
- **Reliability** — uptime targets, error budgets, retry and fallback
  strategies.
- **Scalability** — the load model, the bottlenecks, the growth headroom.
- **Security** — the auth mechanism, how data is protected, the threat surface.
- **Maintainability** — modularity decisions, dependency constraints, debt
  policy.
- **Usability** — the technical constraints serving UX goals: bundle size, time
  to interactive.
- **Observability** — what is instrumented, how, and where it surfaces.
- **Portability and compatibility** — runtime, platform, and API version
  constraints.
- **Compliance** — the technical controls regulatory or legal NFRs require.

State the explicit technical non-goals — what this architecture deliberately
does not attempt. Prefer boring, understandable designs.

### 9. Open technical questions

Standing unknowns that need resolution, each naming what would resolve it. Keep
them as loose ends rather than relying on memory.

## Skeleton

Copy this into a project TRD.

~~~markdown
---
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
~~~

The skeleton carries no `status` or `last-reviewed` key: per-document status
retires under DEC-000380, and a document's version is the SHA of the last commit
that touched it.
