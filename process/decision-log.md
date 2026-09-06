---
order: 110
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Decision Log

**Status of this draft:** proposal for Dave's correction, 2026-09-06. Written
under the gate DEC-000380 sets for a process document: one frontier read against
the rows it cites, then Dave's sign-off, recorded as a decision-log entry naming
the SHA. It is drawn from `policies/decision-log-policy.md` @ fd54448 and from
the store rows R0585, R0586, R0589 and R0591, which retire into it. The rules
with teeth stay rows and are not restated here: **R0583** (append to
`decisions/log.md`; never edit or delete an entry already there), **R1603** (one
decision per entry), and **R0592** (change or reverse a decision by appending a
new entry whose `Supersedes:` names the old ID).

## The principle

**The log is the one place a decision resolves to.**

A decision made once is found and honored rather than silently re-litigated. Its
ID is the resolvable handle: `grep DEC-000070 decisions/log.md` lands on the
entry. A cited decision with no defined path back to its definition is the defect
this log removes.

Each project keeps one log, at `decisions/log.md`. The methodology repo keeps its
own, for methodology decisions. One file, not one file per entry — the single
file *is* the index.

## The entry form

```markdown
## DEC-000070 — <short title>
Date: <YYYY-MM-DD>
Decision: <the ruling, one or two sentences>
Context: <the problem it settled, briefly>
Supersedes: DEC-000030   (omit if none)
```

- **Date** is `YYYY-MM-DD`.
- **Decision** states the ruling in one or two sentences.
- **Context** carries the *why* — the problem the decision settled — so a reader
  can consult the entry without reopening the session it came from.
- **Supersedes** names the old ID, and is omitted where the entry supersedes
  nothing.
- There is **no author field**. Every entry records a decision of Dave's, so a
  "who" would say the same thing on every line.

## Assigning an ID

IDs are `DEC-NNNNNN`, running in steps of ten from `DEC-000010`, unique within
that log and never reused.

Read the log — you are opening it to append anyway — take the last entry's
number, and add ten. Append-only guarantees the last entry holds the highest ID,
so last-plus-ten is always the next free number.

## Resolving a collision

If two entries ever land on the same number, from concurrent appends, renumber
the later ones by **plus one within the gap** — `DEC-000410` to `DEC-000411`,
`DEC-000412` — never by another ten. The step of ten exists for exactly this:
there is always room to bump a collision without disturbing its neighbours.

Renumbering a colliding entry is the one edit the append-only rule admits, and it
changes a number, never a decision.

## What this does not decide

- **What is worth an entry.** A decision of Dave's that governs later work goes
  in the log; the judgment of which decisions those are is his and the Chief of
  Staff's, not this document's.
- **Whether a decision is still live.** That is answered by searching its ID in
  later `Supersedes:` lines — the Lexicon's `live decision` (R0594).
