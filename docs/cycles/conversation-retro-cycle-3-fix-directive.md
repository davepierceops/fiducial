# Retro-skill cycle 3 — Editor fix Directive

Date: 2026-08-31
Documents in scope:
- skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/conversation-retro-cycle-3-fix-directive.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-retro-cycle-3-fix", created by: git worktree add --no-track "$TMPDIR/fiducial-retro-cycle-3-fix" -b retro-cycle-3-fix origin/main

## Decisions

Dispositions of reviews/conversation-retro-cycle-3.md, ruled by Dave
2026-08-31 in the decision session. Finding text and locations are in that
artifact; read it whole before editing. Intent below is binding; wording is
the Editor's except where dictated.

### F-1 — modify
Finding: trigger 2 names a Chief of Staff act ("session rotation") no
governed document defines.
Resolution: restate trigger 2 in terms of the act roles/chief-of-staff.md
already grants — the Chief of Staff recommends ending the session and Dave
acks. Use no rotation term. When a later Chief of Staff role cycle lands a
rotation trigger, that cycle conforms this line; do not anticipate it here.
Dictated wording: the trigger's act is "the Chief of Staff recommends ending
the session and Dave acks" — carry this phrase, fitted to the sentence.

### F-2 — accept
Finding: the closed trigger set conflicts with Decision Layer rule 12.
Resolution: the skill defers; rule 12 does not move. State the triggers as
the routes that reach this procedure, not an exhaustive definition of when a
retro is owed; carry rule 12's obligation, its skip condition (no artifact,
no decision), and its baton-first ordering by reference to
docs/global-context/decision-layer.md rule 12, not by restatement. Drop the
closed-set wording.
Dictated wording: none.

### F-3 — accept
Finding: "the stop signal" is undefined repo-wide.
Resolution: cut the clause; the third trigger ends at running the retro.
Dictated wording: none.

### F-4 — accept
Finding: audience: [all-roles, human] places a decision-session-only
procedure in every execution-session bundle.
Resolution: set audience: [all-decision-roles, human].
Dictated wording: the frontmatter value is [all-decision-roles, human].

### F-5 — accept
Finding: the Dates rule names a merged pull request — a remote-held
artifact — as a date: source, against the no-remote rule.
Resolution: name the local artifact: the merge commit of a pull request, as
recorded in the local tree. The derivation list reads only from the
conversation and the local tree.
Dictated wording: none.

### F-6 — accept
Finding: the unsynthesized-set computation reads the whole retros/
directory, which holds non-retro files.
Resolution: the comparison set is the files matching the retro filename form
this document prescribes, not the directory listing. Prescribe the synthesis
document's filename — retro-synthesis-<timestamp>, timestamp per DEC-000290 —
so a synthesis is mechanically distinguishable from a retro; existing files
are grandfathered as-is, consistent with the document's existing grandfather
line.
Dictated wording: none.

### F-7 — accept
Finding: lines 32-33 restate one clause of Decision Layer rule 12.
Resolution: cut the restatement; F-2's by-reference carry replaces it.
Dictated wording: none.

### F-8 — accept
Finding: trailing justifications at lines 25, 63-66, 97-99.
Resolution: the three cuts the artifact's Fix line specifies.
Dictated wording: none.

### F-9 — accept
Finding: no rule when both date: sources are absent.
Resolution: state the fallback in one clause — generated: stands in for
date:, and the retro declares the substitution.
Dictated wording: none.

### F-10 — defer
Finding: policies/document-metadata-policy.md misdescribes this file's
expedited-path self-exclusion.
Resolution: no edit in this session, to either file. The policy-side
one-line correction is queued to that policy's next cycle; the decision
session records the rider at the next OPEN-ITEMS flush. Recorded for audit.
Dictated wording: none.

### O-1 — no action
Recorded by the artifact so the next cycle does not re-derive it.

## Deferred / out of scope

- F-10's policy-side correction — policies/document-metadata-policy.md next
  cycle; rider recorded at the next OPEN-ITEMS flush by the decision session.
- The re-gate over this fix, its triage, and the agreement flip — later
  directives; tracked by the cycle.

## Execution notes

- Edit skills/conversation-retro.md only; the document is already
  status: in-review with last-reviewed: null and stays so.
- Leave the document conformant to docs/global-context/review-rubric.md and
  to LEXICON.md (the touch rule).
- A changed fact changes everywhere it appears within this file — after the
  edits, sweep the whole document for text the cuts and rewordings have made
  stale, and fix within this file; name any stale text outside it in the
  report instead of editing it.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Do not open a pull request; push the branch and report. The decision
  session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
d2d193dce7eb503b08428123bd522214ff1b1c87. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb
- reviews/conversation-retro-cycle-3.md @ 7ff78ef4174e55c425ea092660f8b0ab3e24be95
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- docs/global-context/decision-layer.md @ 5aa0b9a20f42a59fdf8e9f479ccb2e4372de1f9b
- roles/chief-of-staff.md @ 2d13aea33acb47ab6d89fdf5cfae03fe86eacb2f

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, before the final push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-retro-cycle-3-fix-frontmatter.log", exit status
   reported.
2. Read the revised document once against each disposition above and state,
   per finding, where its resolution landed (section or line) or that the cut
   removed the cited text, labelled observed.
3. bin/bundle --audience coder-agent run once; state whether this document's
   heading appears in the output, labelled observed. Expected: absent.

STOP CONDITIONS

Pinned to the reviewed ref d2d193dce7eb503b08428123bd522214ff1b1c87. Cannot execute as written: stop
and report. Concurrent tree mutation: stop and report. On any failed command,
any precondition not met, or any tree mutation you did not intend, including
your own — stop and report; do not retry with different flags, and do not
delete or create any ref to recover. A remote operation that exits successfully
is not a failed command, whatever a credential helper writes to stderr.

REPORT

- the directive file's commit SHA
- every commit SHA this session landed, in order, and the branch they are on
- what was verified, how, and where the run log is
- every count reported, with the tree it was observed in — the clone's main
  tree, or the worktree the directive assigns; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status — or, under the sole-tree form, that no worktree
  existed

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Retro-skill cycle 3 — Editor fix Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    Decisions — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Deferred / out of scope — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Execution notes — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
