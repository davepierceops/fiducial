---
order: 90
role: [chief-of-staff, writer, copy-editor, critic]
session: [decision]
corpus: [software, writing]
---

# Process: Retro

**Status of this draft:** proposal for Dave's correction, 2026-09-06. Written
under the gate DEC-000380 sets for a process document: one frontier read against
the rows it cites, then Dave's sign-off, recorded as a decision-log entry naming
the SHA. It is drawn from `skills/conversation-retro.md` @ fd54448 and from the
store rows that carried the retro's form, which retire into it.

## What this document is

The retro's **form** — its frontmatter, its sections, its filename, its dates,
and the mechanics of a synthesis over a corpus of them. What an agent *does*
while producing one — ground it in evidence, keep it durable and new, touch no
remote, hand it over, name a repeated preference and stop — is rows in the store
under topic `retro`.

A retro is an input to change, never a change itself: a methodology change it
proposes is a finding for the delta that would carry it.

## Frontmatter

Four fields, and no others:

| field | value |
|---|---|
| `project` | the project slug |
| `date` | the session's last interaction, `YYYY-MM-DD` |
| `generated` | when the retro was written, `YYYYMMDDTHHMMSSZ` |
| `source` | the conversation pointer — title, URL, or export filename — or null where there is none |

This header is synthesis metadata. It serves corpus tooling and carries no
lifecycle semantics.

## The dates

- `date:` is the session's last interaction, not the moment the retro was
  written. Derive it from the last dated artifact the session touched, as
  recorded in the local tree — a pull request's merge commit, a commit, a review
  artifact.
- Where the session touched no dated artifact, take `date:` from the `source:`
  pointer. Where `source:` is null as well, `generated:` stands in for it and the
  retro states the substitution.
- `generated:` is when the retro was written.
- Where the two disagree, both are correct and both are stated.

## The sections

In this order, every time:

1. **Context** — one paragraph: what the conversation was about and what was
   attempted.
2. **Evidence** — numbered, concrete observations of what happened, quoting or
   closely paraphrasing pivotal moments. No interpretation here. A correction
   Dave made once, inside the session, is evidence and stays here.
3. **Interpretation** — what the evidence suggests, each item naming the evidence
   numbers it rests on.
4. **Standing preferences** — preferences Dave stated this session that he has
   stated in earlier sessions too, each as a candidate standing rule naming where
   it was stated before. Say so where there are none.
5. **Durable insights** — techniques, workflow changes, and belief changes that
   transfer beyond the session. Say so where there are none.
6. **Candidate methodology changes** — proposed edits, phrased as findings for
   the delta that would carry them, never as decisions taken.

## The schema

~~~markdown
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
findings for the delta that would carry them — not as decisions>
~~~

## Filenames

A retro is `retro-<timestamp>.md`; a synthesis is
`retro-synthesis-<timestamp>.md`. The timestamp is taken at generation time in
the standing generated-filename form: ISO 8601 basic, UTC, `Z` designator, both
date and time components present — `<YYYYMMDD>T<HHMMSS>Z`.

Match a filename against these two forms only to tell a retro from a synthesis.
Read nothing else from it: the frontmatter is a retro's canonical identity.

## Storage

Retros live in the project's own repo at `retros/`, sibling to its review
artifacts. They are local project history and stay in that repo. A retro is
placed there as a separate later step, taken by a decision session as a command
block that writes and commits the file in a local tree.

A retro or synthesis written before this document was adopted stands as it was
written: it is data, not a governed document.

## Synthesis

- A **project synthesis** runs over one project's `retros/` directory and writes
  its output into the same directory under the synthesis filename form,
  overwriting no source retro.
- A synthesis's header carries a `covers:` list naming the filename of every
  retro it read.
- The next synthesis computes its input set by comparing earlier syntheses'
  `covers:` lists against the files in that directory whose names match the retro
  filename form — not against the directory listing — and states the count it
  read.
- A **cross-project synthesis** is a read operation, not a storage arrangement:
  concatenate the relevant `retros/` directories from local clones as needed.
  There is no shared corpus repo.

## What this document does not decide

Dave's, when reached:

- What invites a retro. The old end-of-session obligation is gone and nothing
  replaced it; until he rules, a retro runs when he asks for one in the moment.
- Whether the corpus ever gains tooling of its own, or stays a directory of
  Markdown files read by hand.
