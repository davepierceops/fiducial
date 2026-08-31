---
status: in-review
last-reviewed: null
audience: [all-decision-roles, human]
---

# Skill: Conversation Retrospective

This procedure runs in a decision session.

## Purpose

Produce one retrospective per LLM conversation about a software project,
in a fixed schema, grounded in evidence from that conversation. The
retrospectives form a per-project corpus for later synthesis into
methodology changes and published writing.

Retros are an input to change, not a change mechanism. A methodology revision
surfaced by a retro or a synthesis takes the full review cycle, whatever
lighter path it would otherwise be eligible for.

## Use when

Each route below runs this procedure unchanged. The routes are not the whole
of when a retro is owed: the Decision Layer's rule 12 states that obligation,
the condition under which a session may skip it, and the ordering when a baton
is also owed. Rule 12 governs whether a retro is owed; this document governs
how to produce one.

- Dave directs a retro explicitly.
- The Chief of Staff recommends ending the session and Dave acks.
- The conversation is closing — Dave signals the end of the chat. Run the
  retro.

## Principles

- **Durable over incidental.** Capture techniques, workflows, belief
  changes, and engineering practices that transfer. Omit implementation
  details that do not.
- **New or evolved only.** Emphasize ideas that are new or materially
  changed in the session. Restating standing methodology is noise.
- **Structurally identical.** Every retro uses the schema below.

## Producing a retro touches no remote

Producing a retro reads nothing from and writes nothing to any remote,
GitHub included. Every input is the conversation itself and the local tree.

The finished retro is handed to Dave in the chat that produced it, and that
is where this procedure ends.

Placing a retro into the repository is a separate step, taken afterward by a
decision session as a command block that writes and commits the file in a
local tree. Producing a retro never places one, and never asks a connector to.

## Standing preferences

Every retro answers one question explicitly: which preferences did Dave state
this session that he has also stated in earlier sessions?

- A repeated preference is a candidate standing rule and is recorded in its
  own schema section.
- A correction Dave made once, inside this session, is evidence and stays in
  the Evidence section. The two are never merged.
- Naming a candidate is this procedure's act. Encoding one into governed text
  is a decision, and Dave's.

## Storage

- Retros live in the project repo at `retros/`, sibling to the project's
  review artifacts. They are local project history and never travel to
  the methodology repo.
- The header block in the retro schema below is synthesis metadata
  (project, dates, source pointer), not governance metadata. It serves
  corpus tooling and carries no lifecycle semantics.
- Retros and syntheses predating adoption of this skill are grandfathered
  as-is. Data, not governed documents.

## Filenames

A retro is `retro-<timestamp>.md`; a synthesis is
`retro-synthesis-<timestamp>.md`. The timestamp is taken at generation time in
ISO 8601 basic format, UTC, with the `Z` designator required and both date and
time components present: `<YYYYMMDD>T<HHMMSS>Z`.

Match a filename against these two forms only to tell a retro from a synthesis.
Read nothing else from it: the schema header is the canonical identity of a
retro.

## Dates

- `date:` is the session's last interaction, not the moment the retro was
  written. Derive it from the last dated artifact the session touched, as
  recorded in the local tree — the merge commit of a pull request, a commit, a
  review artifact. Where the session touched no dated artifact, take it from
  the `source:` pointer.
- `generated:` is when the retro was written, in the timestamp form above.
- Where the session touched no dated artifact and `source:` is null,
  `generated:` stands in for `date:` and the retro states the substitution.
- Where the two disagree, they are both correct and both stated.

## Retro schema

```markdown
---
project: <project slug>
date: <YYYY-MM-DD; the session's last interaction>
generated: <YYYYMMDDTHHMMSSZ; when this retro was written>
source: <conversation pointer: title, URL, or export filename; null if none>
---

# Retro — <project> — <date>

## Context
<one paragraph: what the conversation was about, what was attempted>

## Evidence
<numbered, concrete observations of what happened; quotes or close
paraphrases of pivotal moments; no interpretation here>

## Interpretation
<what the evidence suggests; each item references the evidence numbers
it rests on>

## Standing preferences
<preferences Dave stated this session that he has stated in earlier
sessions too, each as a candidate standing rule and each naming where it
was stated before; empty-with-a-statement if none>

## Durable insights
<techniques, workflow changes, belief changes that transfer beyond this
session; empty-with-a-statement if none>

## Candidate methodology changes
<specific proposed edits to methodology documents, if any, phrased as
inputs to a future review cycle — not as decisions>
```

## Synthesis

- **Project synthesis:** performed over a project's `retros/` directory.
  Output is a synthesis document in the same directory, named in the synthesis
  filename form above, never overwriting source retros.
- **A synthesis names what it covered.** Its header carries a `covers:` list
  of the filename of every retro it read. A retro named in no synthesis's
  `covers:` list is unsynthesized; the next synthesis computes its input set by
  comparing those lists against the files in that directory whose names match
  the retro filename form above — not against the directory listing — and
  states the count it read.
- **Cross-project synthesis:** a read operation, not a storage
  arrangement — concatenate the relevant `retros/` directories from
  local clones as needed. No shared corpus repo.
- Synthesis outputs feeding methodology changes are packaged as findings
  for a review cycle.

## Output

- One Markdown file per conversation, handed in the chat that produced it:
  delivered as a downloadable artifact where the client supports it;
  otherwise exactly one fenced Markdown block containing the entire document
  and nothing else.
