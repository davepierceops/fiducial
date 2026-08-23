---
status: agreed
last-reviewed: reviews/expedited-log.md @ 48ad7fd1e827a7c92660fd2cd9ebc5871c1dbc21
audience: [chief-of-staff, human]
---

# Skill: Directive Authoring

This procedure runs in a decision session.

## Writing the directive file

One self-contained directive per session.

- **Every directive states its working-tree disposition** — either an
  exclusive assignment (a named directory plus the command creating it) or an
  explicit sole-tree declaration. A prohibition is not a disposition. Two
  sessions sharing a tree mutate each other's preconditions; prefer not
  splitting work across trees.
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
