---
order: 110
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Decision Log

Each project keeps one log at `decisions/log.md`, and the methodology repo keeps
its own for methodology decisions. An entry takes this form, and carries no
author field:

```markdown
## DEC-000070 — <short title>
Date: <YYYY-MM-DD>
Decision: <the ruling, one or two sentences>
Context: <the problem it settled, briefly>
Supersedes: DEC-000030   (omit if none)
```

IDs are `DEC-NNNNNN`, running in steps of ten from `DEC-000010`, unique within the
log and never reused. Take the last entry's number and add ten; append-only
guarantees that the last entry holds the highest ID [R0583, R0592, R1603].

Where two entries land on the same number, renumber the later ones by plus one
within the gap — `DEC-000410` to `DEC-000411`, `DEC-000412` — never by another
ten. That renumbering is the one edit the append-only rule admits, and it changes
a number, never a decision.
