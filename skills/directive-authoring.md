---
status: in-review
last-reviewed: null
audience: [chief-of-staff, human]
---

# Skill: Directive Authoring

This procedure runs in a decision session.

## Writing the directive file

- **Every directive states its working-tree disposition** — either an
  exclusive assignment (a named directory plus the command creating it) or an
  explicit sole-tree declaration. A prohibition is not a disposition. The
  disposition is stated as its own labelled statement, exactly one per
  directive, mechanically distinguishable from incidental mention of trees or
  commands elsewhere in the file; the label's fixed form, the canonical
  sole-tree sentence, and a worked example of each form are stated in the
  Directive Invariants document and nowhere else. Two sessions sharing a tree
  mutate each other's preconditions; prefer not splitting work across trees.
- **The disposition label leads the disposition statement and no other
  unfenced line.**
- **The route line names one session** — a fresh session, or an existing
  session named by the directive it landed, never by the tree or branch it
  holds.
- **Pin STOP conditions to the reviewed ref**, not the head of the branch the
  directive lands on — the directive's own commit moves that head.
- **No blanket constraint may contradict an explicit instruction in the same
  file.** Read the constraint block against the instruction list before sending.
- **Scope Do-not lists and base guards to the blast radius.** Where a required
  consistency fix reaches outside it, name that file as explicitly permitted.
  A guard on the base names the files the work touches, never a directory.
- **Carry dictated wording as a pointer** — the source's path and SHA plus its
  field or section, never restated — unless the directive is itself the
  wording's origin, in which case it carries it inline and downstream artifacts
  point at it.
- **An expected-state line is read from the tree at the reviewed ref** —
  counts, exit codes, blob SHAs — never carried from a session report or from
  memory.
- **A directive that assigns a worktree instructs the holder check**: before
  creating it, fetch the base and list worktrees; if any worktree holds the
  branch, or the path exists, stop and report. Entries marked prunable are not
  the session's.
- **A directive that assigns a worktree instructs its removal** from the main
  tree, after the report is composed and every push is verified landed,
  without force and without retry; the report's final line states the outcome.
- **A push instruction names the remote and the branch and sets no upstream.**
- **Every directive states that the pre-commit hook is never bypassed.**

## Naming

A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in
ISO 8601 basic format with date and time components both present (as
`20260820T161541`) — except a directive generated in cycle mode, which is
`docs/cycles/cycle-<n>-directive.md` for a numbered cycle or
`docs/cycles/<slug>-directive.md` for a named one, the slug a single path
component.
