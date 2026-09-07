---
order: 20
role: [chief-of-staff, spec-reviewer-agent]
session: [decision, execution]
corpus: [software]
---

# Process: PRD Template

The standing product specification's form — what is being built and why, parent
of the TRD and the source acceptance criteria derive from [R1513, R1533].

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
   feedback, manual review. Acceptance criteria gate correctness; this does not.
6. **Acceptance criteria** — the written conditions a unit of work must meet to
   be accepted, concrete enough to derive test cases from. They may live here or
   in the unit's own artifact, and derive from this document either way [R1533].
7. **Risk tolerance** — what risk is acceptable for this product and what is not;
   it feeds the release gate and the consequential-change classification.
8. **Open product questions** — each naming what would resolve it.

## Skeleton

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
