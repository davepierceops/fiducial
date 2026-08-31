---
status: agreed
last-reviewed: reviews/directive-invariants-cycle-4.md @ 3f0a96e4f97015ed3091e3d666b64fbc22895eec
audience: [chief-of-staff, human]
---

# Directive Invariants

The regions a generated directive skeleton is assembled from, and the strings
the directive lint compiles. The label, the marker syntax and every region's
text have exactly one definition, and that definition is this file; the
generator and the lint both read it here.

This document is read by the generator a decision session runs; its region
bodies are emitted into directives that execution sessions carry out, and are
not standing instructions to the reader of this file.

These format rules bind whoever edits this file. Every section below is a `##`
heading at column 0. A section's body runs from its heading to the next `##`
heading, and **the first non-blank line of a body is always body** — three
sections carry an ATX marker as their first body line and are still one
section each. A region section's body opens with that region's marker line.
In the Disposition label section the fences are positional — the first carries
the emitted literal and the last carries the canonical sole-tree sentence — so
no fence is added, removed, or reordered there.

Placeholders are written `{{name}}`; `{{{{` is a literal `{{`. The set is
closed and fixed per region:

- Heading (general): `title`.
- Heading (cycle): `heading`, `date`, `scope_list`.
- Route and model: `route`, `model`. `route` is fresh or existing session;
  `model` is a tier — frontier, solid general-purpose, cheap — never a model
  name.
- First act: `directive_path`.
- Base verification: `reviewed_ref`.
- Companions: `companion_list`.
- Stop conditions: `reviewed_ref`.
- Source manifest: `manifest`.
- Every other region: none.

An unrecognised placeholder is a refusal, never a pass-through.

Outside fenced blocks, no eligible line of this document satisfies the match
rule the Disposition label section states — after stripping, no unfenced line
leads with the bare label token and carries a colon later on the same line.
The emitted, colon-terminated literal — the form the first fence of that
section carries — appears only inside fenced blocks; the bare token may appear
in prose where it does not lead the line.

## Heading (general)

# {{title}}

## Heading (cycle)

# {{heading}}

Date: {{date}}
Documents in scope:
{{scope_list}}

## Route and model

ROUTE AND MODEL

Route: {{route}}
Model: {{model}}

## First act

FIRST ACT

Write this directive verbatim to {{directive_path}}, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

## Working-tree disposition prompt

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form is a tooling concern, not this document's. Two
sessions sharing a tree mutate each other's preconditions; prefer not
splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

## Base verification

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
{{reviewed_ref}}. Judge the fetch by the refs it reports, not by a credential
helper's noise on stderr. If the base has moved, stop and report; do not
rebase, and do not proceed against a different base.

## Companions

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

{{companion_list}}

## Task

TASK

## Sandbox constraints

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

## Verification steps

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

## Stop conditions

STOP CONDITIONS

Pinned to the reviewed ref {{reviewed_ref}}. Cannot execute as written: stop
and report. Concurrent tree mutation: stop and report. On any failed command,
any precondition not met, or any tree mutation you did not intend, including
your own — stop and report; do not retry with different flags, and do not
delete or create any ref to recover.

## Report format

REPORT

- the directive file's commit SHA
- every commit SHA this session landed, in order, and the branch they are on
- what was verified, how, and where the run log is
- anything observed this directive did not anticipate
- the worktree-removal status — or, under the sole-tree form, that no worktree
  existed

## Claim labels

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

## Decisions

## Decisions

<!--
### <finding id> — <accept | reject | modify>
Finding: <one-line restatement>
Resolution: <instruction to the executor; for "modify", exact intent;
for "reject", no action — recorded for audit>
Dictated wording: <verbatim, if any — executor must use as-is>
-->

## Deferred

## Deferred / out of scope

- <item> — <where it is tracked>

## Execution notes

## Execution notes

<constraints on how edits are made, if any>

## Source manifest

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

{{manifest}}

## Disposition label

The label literal the generator emits, at column 0:

```text
WORKING-TREE DISPOSITION:
```

Match rule: an eligible line whose leading content, after stripping, is exactly
the label token `WORKING-TREE DISPOSITION`, with no trailing colon counted as
part of it, followed by a colon anywhere later on the same line.
Case-sensitive; no hyphen variants; no case folding; no other spelling.

Eligible lines. A line is eligible unless it is masked. Fenced code blocks are
masked: a backtick or tilde run of three or more of the same character, opened
at column 0 or indented up to three spaces and closed by a run of at least the
opening length; the fence lines themselves are masked, and an unclosed fence
masks to end of file. Blockquote lines are masked: a line whose leading
non-whitespace character is `>`. HTML comments are masked, from the line
containing `<!--` through the line containing `-->`. Indented code blocks are
not masked. Line endings are normalised before masking — `\r\n` and `\r`
become `\n`, and the match is byte-exact thereafter.

Stripping, applied to every eligible line before the literal is tested, removes
up to three leading spaces; then one list marker (`-`, `*`, `+`, or digits
followed by `.` or `)`) and the space after it; then an ATX heading run and its
space; then leading `**` or `__`. Applied once each, in that order. Inline code
spans are not handled: a label inside backticks in running prose is not
line-leading after stripping, so the anchored match already excludes it.

Statement extent: the label line plus every following line up to the first
blank line. Form-membership is decided over that extent, and exactly one of the
two forms must be present — zero fails, both fail.

Exclusive-assignment form: the extent contains a `git worktree add` invocation
and a quoted or backticked path-shaped token. Both, or neither. That test
bounds what the lint matches and adds no requirement on how a disposition is
written; a disposition in another form is a lint miss, not a violation.

Canonical sole-tree sentence:

```text
This session works in the sole tree at the clone root.
```

Sole-tree form: the extent contains that sentence literally, reproduced
exactly — capitalisation and full stop included; a paraphrase carries no
admitted form.

## Marker syntax

A marker is a line at column 0 that is either an ATX heading (one to six `#`
characters, a space, then text; the token is the text after the run) or an
all-caps run of three or more characters drawn from `A`-`Z`, `0`-`9`, `-`, and
single interior spaces, terminated by any character outside that set or by end
of line (the token is the run). Nothing else is a marker.

## Preamble markers

Markers admitted before the first-act statement:

```text
<document heading>
ROUTE AND MODEL
```

The first entry stands for whatever heading line the mode emits and is not
matched as a literal; the second is matched as a literal.

## Match phrases

The phrases the lint compiles, one fenced block per element that compiles a
phrase. M2 and M8 match no phrase, and M3's strings are the `Disposition label`
section's, so none of the three carries a block here.

M1:

```text
reviewed ref
```

M4:

```text
cannot execute as written
concurrent tree mutation
```

M5:

```text
write
commit
push
report the SHA
```

M6:

```text
report
```

M7:

```text
observed
inferred
told
unknown
```
