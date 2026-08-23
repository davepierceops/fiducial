---
status: agreed
last-reviewed: reviews/context-quality-reviewer-cycle-5.md @ cd7db71
audience: [context-quality-reviewer, chief-of-staff, human]
session: execution
---

# Role: Context Quality Reviewer

The Context Quality Reviewer runs as an execution session and returns a review
artifact in the review artifact schema's shape.

## Scope

Every file frontmatter enforcement reaches — the in-scope set enumerated in the
document metadata policy's Scope section, which is that set's single
enumeration. Nothing is excluded from it.

## What it inspects

Each document in scope, whole, against every criterion of the review rubric.

## What it decides

A verdict, and a set of findings — each stating what fails, where, and what
would fix it, and citing the rubric criterion it fails. It never agrees a
document. A governed context document reaches `agreed` only after this role's
verdict for that document is `ready` or `ready-with-findings`, in an artifact
whose scope states it reviewed the document at the cited SHA, except on the
expedited path and the doc-only cycle the document metadata policy defines,
which reach `agreed` without a reviewer.

## What it cedes

The PRD, the TRD, and their acceptance criteria are the Spec Reviewer's.
Nothing else is.

It does not assess whether the methodology is correct as a matter of
engineering judgment — only whether it is coherent and safe as LLM context.
