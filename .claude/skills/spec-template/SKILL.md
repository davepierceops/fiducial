---
name: spec-template
description: "The form of `SPEC.md`, one per project: what is being built, why, how, and when it is done."
---
<!-- fiducial:begin -->
# Process: Spec Template

The form of `SPEC.md`, one per project: what is being built, why, how, and
when it is done. The Chief of Staff drafts it with the human by interview; the
Architect drafts its design section; a Spec Reviewer reads it before the human
approves it, and it is in force only from that approval [R1513]. A unit's
acceptance criteria derive from it [R0472]. Keep each section short.

1. **Problem and intent** — the problem, who has it, and why it is worth building
   now.
2. **Users and use cases** — who uses this and the concrete situations in which
   they do.
3. **User journeys** — the Top K journeys, each with its actor, its trigger, the
   sequence of actions and system responses, and the expected outcome.
4. **Goals and non-goals** — functional goals as concrete outcomes rather than
   feature lists; non-functional goals for each dimension — performance,
   reliability, scalability, security, maintainability, usability,
   observability, portability and compatibility, compliance — or `N/A` where the
   dimension is not a constraint; then the non-goals. An exclusion specific to
   one non-functional dimension is a note inside that dimension, not a non-goal.
5. **User outcomes and measurement** — the signals, quantitative or qualitative,
   confirming the change produced real user value: the metric or signal, the
   baseline where known, and the mechanism observing it — telemetry, user
   feedback, manual review. The definition of done gates correctness; this does
   not.
6. **Definition of done** — the acceptance criteria: the written conditions the
   work must meet to be accepted, concrete enough to derive test cases from.
   They may live here or in the unit's own artifact, and derive from this
   document either way.
7. **Design** — what the Architect's design obligations require [R0863]: the
   system's structure and the implementation approach; its components and the
   interfaces between them; its external dependencies; the failure modes it is
   likely to have; the NFR dimensions of section 4 as concrete technical
   targets, or `N/A`; and its deployment assumptions, including whether deploy
   and release are separate events [R0497]. Two subsections are standing:
   - **User journeys and SLOs** — for each Top K journey of section 3, the SLO,
     the measurement mechanism, and the alerting threshold; a journey with no
     SLO is named unverified and recorded as an open question.
   - **Verification boundaries** — for each material standing boundary where
     the system meets what it does not control, and for each per-change
     boundary movement made permanent: the production surface; how it is
     represented — live, contract, mock, or assumed; its evidence class; the
     deferred-verification path, if any.
   Per-change technical design lives in the per-change architecture summary
   [R0862b], not here.
8. **Risk tolerance** — what risk is acceptable for this product and what is not;
   it feeds the release gate and the consequential-change classification.
9. **Open questions** — product and technical, each naming what would resolve it.

## Skeleton

~~~markdown
---
audience: [human]
---

# SPEC: <project name>

## 1. Problem and intent
## 2. Users and use cases
## 3. User journeys
## 4. Goals and non-goals
### Functional goals
### Non-functional goals
### Non-goals
## 5. User outcomes and measurement
## 6. Definition of done
## 7. Design
### User journeys and SLOs
### Verification boundaries
## 8. Risk tolerance
## 9. Open questions
~~~
<!-- fiducial:end -->
