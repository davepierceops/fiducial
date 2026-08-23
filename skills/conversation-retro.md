---
status: agreed
last-reviewed: reviews/conversation-retro-cycle-2.md @ cd7db71
audience: [all-roles, human]
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

- a decision session on a project has ended and its durable lessons should be
  captured
- Dave directs a retro explicitly

Do not run a retro on a reviewer-gated cycle conversation unless directed —
its decision record is the cycle directive.

## Principles

- **Durable over incidental.** Capture techniques, workflows, belief
  changes, and engineering practices that transfer. Omit implementation
  details that do not.
- **New or evolved only.** Emphasize ideas that are new or materially
  changed in the session. Restating standing methodology is noise.
- **Structurally identical.** Every retro uses the schema below.

## Storage

- Retros live in the project repo at `retros/`, sibling to the project's
  review artifacts. They are local project history and never travel to
  the methodology repo.
- The header block in the retro schema below is synthesis metadata
  (project, date, source pointer), not governance metadata. It serves
  corpus tooling and carries no lifecycle semantics.
- Retros predating adoption of this skill are grandfathered as-is. Data, not
  governed documents.

## Filenames

`retro-<timestamp>.md`, the timestamp in ISO 8601 basic format, taken at
generation time.

Filenames are opaque, collision-free handles only — never parse them for
meaning. The schema header is the canonical identity of a retro.

## Retro schema

```markdown
---
project: <project slug>
date: <YYYY-MM-DD>
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

## Durable insights
<techniques, workflow changes, belief changes that transfer beyond this
session; empty-with-a-statement if none>

## Candidate methodology changes
<specific proposed edits to methodology documents, if any, phrased as
inputs to a future review cycle — not as decisions>
```

## Synthesis

- **Project synthesis:** performed over a project's `retros/` directory.
  Output is a synthesis document in the same directory, clearly marked
  as synthesis, never overwriting source retros.
- **Cross-project synthesis:** a read operation, not a storage
  arrangement — concatenate the relevant `retros/` directories from
  local clones as needed. No shared corpus repo.
- Synthesis outputs feeding methodology changes are packaged as findings
  for a review cycle.

## Output

- One Markdown file per conversation, delivered as a downloadable
  artifact where the client supports it; otherwise exactly one fenced
  Markdown block containing the entire document and nothing else.
