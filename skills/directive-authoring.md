---
status: agreed
last-reviewed: reviews/directive-authoring-cycle-2.md @ cd7db71
audience: [chief-of-staff, human]
---

# Skill: Directive Authoring

This procedure runs in a decision session.

## Writing the directive file

One self-contained directive per session.

- **Exclusive working trees for split directives.** Two sessions sharing a tree
  mutate each other's preconditions. Prefer not splitting; where unavoidable,
  state the tree assignment in each directive.
- **Pin STOP conditions to the reviewed ref**, not the head of the branch the
  directive lands on — the directive's own commit moves that head.
- **No blanket constraint may contradict an explicit instruction in the same
  file.** Read the constraint block against the instruction list before sending.
- **Scope Do-not lists to the blast radius.** Where a required consistency fix
  reaches outside it, name that file as explicitly permitted.
- **Carry dictated wording as a pointer** — the source's path and SHA plus its
  field or section, never restated — unless the directive is itself the
  wording's origin, in which case it carries it inline and downstream artifacts
  point at it.

## Naming

A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in
ISO 8601 basic format.
