---
name: decision-log
description: "Each project keeps one log at `decisions/log.md`, and the methodology repo keeps its own for methodology decisions."
---
<!-- fiducial:begin -->
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

Entries are appended by the decision session at merge, from the landed work's
report, and ids are allocated then — never by the subagent that did the work —
so concurrent packages never take the same id.

Supersession is whole-entry: a new entry whose `Supersedes:` names an old one
replaces all of it, so where the old entry carried several rulings the new one
restates every ruling that survives. A ruling the new entry does not restate is
gone.

Where two entries land on the same number, renumber the later ones by plus one
within the gap — `DEC-000410` to `DEC-000411`, `DEC-000412` — never by another
ten. That renumbering is the one edit the append-only rule admits, and it changes
a number, never a decision.

## Rules

Append to `decisions/log.md`; never edit or delete an entry already there.

One decision per entry.

Change or reverse a recorded decision by appending a new entry whose `Supersedes:` names the old ID, leaving the old entry in place as the historical record.

### Definitions

**decision session** — A decision session triages, decides, and produces the artifacts that direct and record work — plans, subagent prompts, session records, tracker updates. It reads freely and writes those artifacts; the changes a plan specifies happen elsewhere, in the session that runs it. The boundary is role in the flow, not capability: a decision session may hold a clone and may commit.
<!-- fiducial:end -->
