---
order: 30
role: [architect-agent, spec-reviewer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: TRD Template

The standing technical specification's form, drafted and maintained by the
Architect [R0871, R1541, R1542, R1543]; per-feature technical design lives in the
per-change architecture summary [R0862b]. Keep each section short.

1. **System overview** — the major components, how they fit together, and what
   kind of system it is: service, app, PWA, CLI.
2. **User journeys and SLOs** — for each of the PRD's Top K journeys, the SLO, the
   measurement mechanism, and the alerting threshold; a journey with no SLO is
   named unverified and recorded as an open question.
3. **Architecture and boundaries** — each component and its responsibility; the
   interfaces between them; the external dependencies — APIs, providers, data
   stores, auth, browser and PWA surfaces; and each durable boundary where the
   system meets what it does not control, with what verifying it would take.
4. **Verification boundaries (standing)** — for each material standing boundary,
   and for each per-change boundary movement made permanent: the production
   surface; how it is represented — live, contract, mock, or assumed; its
   evidence class; the deferred-verification path, if any.
5. **Data and state** — the key data shapes, their persistence, ownership, and
   lifecycle, and who is authoritative for each.
6. **Failure modes and recovery** — how the system fails, how a failure is
   detected, what the user sees, and how it recovers or rolls back.
7. **Operational concerns** — observability, configuration and secrets, quota and
   billing exposure, deployment assumptions; the release model and whether deploy
   and release are separate events [R0497, R0499, R0500]; the mechanism routing a
   go/no-go response back into the workflow.
8. **Constraints, NFRs, and non-goals** — for each NFR dimension the PRD defines
   — performance, reliability, scalability, security, maintainability, usability,
   observability, portability and compatibility, compliance — the concrete
   technical target or constraint, or `N/A`; then the technical non-goals [R1573].
9. **Open technical questions** — each naming what would resolve it.

## Skeleton

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
