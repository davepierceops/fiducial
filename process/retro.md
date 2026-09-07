---
order: 90
role: [chief-of-staff, writer]
session: [decision]
corpus: [software, writing]
---

# Process: Retro

Run a retro when the human asks for one.

A retro is `retro-<timestamp>.md`, a synthesis `retro-synthesis-<timestamp>.md`,
the timestamp taken at generation time as `<YYYYMMDD>T<HHMMSS>Z`. Match a filename
against those two forms only to tell one from the other; the frontmatter is a
retro's canonical identity. Retros live in the project's own repo at `retros/`,
written and committed there by a decision session as a separate later step.

A project synthesis runs over one project's `retros/` directory and writes into
it under the synthesis filename form, overwriting no source retro; its header
carries a `covers:` list naming every retro it read. The next synthesis computes
its input set by comparing earlier syntheses' `covers:` lists against that
directory's files matching the retro filename form, and states the count it read.
A cross-project synthesis concatenates the relevant `retros/` directories.

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
paraphrases of pivotal moments; no interpretation here; a correction the
human made inside the session belongs here>

## Interpretation
<what the evidence suggests; each item references the evidence numbers
it rests on>

## Standing preferences
<preferences the human stated this session that he has stated in earlier
sessions too, each as a candidate standing rule and each naming where it
was stated before; empty-with-a-statement if none>

## Durable insights
<techniques, workflow changes, belief changes that transfer beyond this
session; empty-with-a-statement if none>

## Candidate methodology changes
<specific proposed edits to methodology documents, if any, phrased as
findings for the delta that would carry them — not as decisions>
~~~

`date:` is the session's last interaction, taken from the last dated artifact the
session touched as recorded in the local tree — a merge commit, a commit, a
review artifact. Where the session touched none, take it from the `source:`
pointer; where `source:` is null too, `generated:` stands in and the retro states
the substitution. Where the two disagree, both are correct and both are stated.
