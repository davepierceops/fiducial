---
order: 20
role: [chief-of-staff, spec-reviewer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: PRD Template

Read in a decision session drafting a PRD and in an execution session gating
one. This document is the form; the obligations an agent performs when it
drafts, gates, or maintains a PRD are rows in the store under topic
`prd-template`.

## What this is

The PRD is the standing product specification: the authoritative description of
*what* is being built and *why*. It is canonical and sits at the top of the spec
spine, above the TRD. It owns product intent, it is Dave's document, and it is
not in force until Dave agrees it.

The PRD is the parent of the TRD and the source acceptance criteria are derived
from.

## Required sections

### 1. Problem and intent

The problem being solved and who has it. Why this is worth building now.

### 2. Users and use cases

Who uses this and the concrete situations in which they do.

### 3. User journeys

The Top K journeys. For each:

- **Actor** — who is doing this.
- **Trigger** — what causes them to start.
- **Steps** — the sequence of actions and system responses.
- **Expected outcome** — what success looks like for the user.

### 4. Goals and non-goals

**Functional goals.** What the product or change must do, as concrete outcomes
rather than feature lists.

**Non-functional goals.** The quality bar the product must meet. Address each
dimension; `N/A` is a valid answer where the dimension is not a constraint for
this product.

- **Performance** — latency, throughput, and response-time targets.
- **Reliability** — uptime, error rate, and fault-tolerance expectations.
- **Scalability** — load handling and growth headroom.
- **Security** — authentication, data protection, and threat model.
- **Maintainability** — ease of change, extension, and debugging.
- **Usability** — accessibility, learnability, and the UX quality bar.
- **Observability** — logging, metrics, alerting, and traceability.
- **Portability and compatibility** — platform, browser, or API version
  constraints.
- **Compliance** — regulatory, legal, or data-residency requirements.

**Non-goals.** What this deliberately does not try to do. An exclusion specific
to one non-functional dimension — "sub-100ms latency is out of scope for v1" —
is a note inside that dimension, not a non-goal here.

### 5. User outcomes and measurement

How we will know the product improved things for users. This is distinct from
acceptance criteria: acceptance criteria gate whether the implementation is
correct; this section names the signals — quantitative or qualitative — that
confirm the change produced real user value. Name the metric or signal, the
baseline where it is known, and the mechanism that observes it: telemetry, user
feedback, manual review.

### 6. Acceptance criteria

The explicit, written conditions a unit of work must meet to be accepted. They
are the source the Test Designer derives test cases from, so they are concrete
enough to test. Per-unit acceptance criteria may live here or in the unit's own
artifact, but they derive from this document either way.

### 7. Risk tolerance

What kind of risk is acceptable for this product and what is not. This feeds the
release gate and the consequential-change classification.

### 8. Open product questions

Standing product unknowns, each naming what would resolve it.

## Skeleton

Copy this into a project PRD.

~~~markdown
---
audience: [human]
---

# PRD: <project name>

## 1. Problem and intent
## 2. Users and use cases
## 3. User journeys
## 4. Goals and non-goals
### Functional goals
### Non-functional goals
### Non-goals
## 5. User outcomes and measurement
## 6. Acceptance criteria
## 7. Risk tolerance
## 8. Open product questions
~~~

The skeleton carries no `status` or `last-reviewed` key: per-document status
retires under DEC-000380, and a document's version is the SHA of the last commit
that touched it.
