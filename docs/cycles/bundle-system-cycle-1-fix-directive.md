# Bundle-system PRD cycle 1 — Editor fix Directive

Date: 2026-09-02
Documents in scope:
- specs/bundle-system.md @ cf3b87e08cf6257ee09c7066a3a53ed2adafcd15

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-system-cycle-1-fix-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-bundle-cycle-1-fix", created by: git worktree add --no-track "$TMPDIR/fiducial-bundle-cycle-1-fix" -b bundle-cycle-1-fix origin/main

## Decisions

Dispositions of reviews/bundle-system-cycle-1.md, ruled by Dave 2026-09-02
in the decision session. Finding text, locations, and Fix lines are in that
artifact; read it whole before editing. Intent below is binding; wording is
the Editor's except where dictated. Edit only specs/bundle-system.md; a
finding whose fix lives in another file is recorded as queued, never
applied here.

### B-1 — modify (ruled by Dave)
Finding: the audience value critic names two role documents; the critic
bundle emits 28 files against a five-file target, unreachable by tagging.
Resolution: the PRD states the collision and its ruled resolution — the
SRE engagement's critic role is renamed sre-critic (file basename and the
audience value on the engagement files that carry it), landing in the
tagging package, not this revision — and adds one sentence making role
basenames unique corpus-wide, so a future collision is a detectable
defect. Placement is the Editor's (near G5 or in the AC set).
Dictated wording: the uniqueness rule carries the phrase "role-document
basenames are unique across roles/ and engagements/", fitted to the
sentence.

### R-2 — apply (pre-ruled, topic-walk ruling 13 T30)
Finding: the lore home is ruled but the PRD does not state it.
Resolution: G11 and AC-BS-12 absorb the ruling: the lore home is the
tooling-facts artifact; entries are dated, falsifiable, and classified
(lost response / never dispatched / caller error / tool defect).
Dictated wording: the four classification labels, verbatim.

### N-1 through N-8 — accept
Finding: as filed in the artifact.
Resolution: apply each finding's Fix line as written there. For N-6, cite
DEC-000320, DEC-000330, DEC-000340 in the OQ-5, OQ-6, OQ-10 resolutions
respectively. For N-4, the refuses wording (G1, AC-BS-1) wins and J1
conforms. For N-7, AC-BS-9's first sentence conforms to the
every-audience rule its third sentence states.
Dictated wording: none beyond the artifact's Fix lines.

### O-1, O-2, O-3, O-5 — accept
Finding: as filed.
Resolution: apply each Fix line where it edits this document. O-1: goal
numbering runs in order (renumber so G11 precedes G12; sweep the document
for every reference to a renumbered goal). O-5: if its fix edits the
template rather than this document, record as queued instead.
Dictated wording: none.

### O-4 — modify: queued, not applied
Finding: copy-editor and critic role files lack order:.
Resolution: no edit here — the fix lives in role files; record it as
queued to the tagging package.
Dictated wording: none.

### O-6 — no action
Recorded by the artifact; the sentence it flags is already satisfied.

## Deferred / out of scope

- The tagging package: the sre-critic rename and seven audience retags,
  the outline.md human-value removal (DEC-000340), order: on copy-editor
  and critic, and any template-side fix from O-5 — a later directive;
  tracked by the cycle and OPEN-ITEMS.
- A decision-log entry for the sre-critic ruling — the next flush.
- The confirmation-scoped re-gate over this fix — a later directive.

## Execution notes

- Edit specs/bundle-system.md only; the document is status draft and stays
  draft.
- Leave the document conformant to specs/prd-template.md and LEXICON.md
  (the touch rule).
- A changed fact changes everywhere it appears within this file — after
  the edits, sweep the whole document for text the fixes made stale
  (renumbered goals especially); name any stale text outside this file in
  the report instead of editing it.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin bundle-cycle-1-fix, without -u.
- Do not open a pull request; push the branch and report. The decision
  session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
49daa469982a4fea206dcdef253e5e516ce863ef. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/bundle-system.md @ cf3b87e08cf6257ee09c7066a3a53ed2adafcd15
- reviews/bundle-system-cycle-1.md @ 42636f35f4407ffacc37626ab8f0240fb0c70740
- specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67
- decisions/log.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276

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
   "$TMPDIR/fiducial-bundle-cycle-1-fix-frontmatter.log", exit status
   reported.
2. Read the revised document once against each disposition above and
   state, per finding, where its resolution landed (section or line) or
   that it was recorded as queued, labelled observed.
3. grep for every goal number G1 through G12 in the revised document,
   captured beside the log; confirm the numbering is sequential and every
   cross-reference names an existing goal.

STOP CONDITIONS

Pinned to the reviewed ref 49daa469982a4fea206dcdef253e5e516ce863ef. Cannot execute as written: stop
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

    Bundle-system PRD cycle 1 — Editor fix Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
