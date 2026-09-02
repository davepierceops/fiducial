# Flush 2026-09-02 — sre-critic entry, item-2 close, tagging package Directive

Date: 2026-09-02
Documents in scope:
- OPEN-ITEMS.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276
- decisions/log.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276

ROUTE AND MODEL

Route: fresh
Model: solid

FIRST ACT

Write this directive verbatim to docs/cycles/open-items-flush-20260902T132457Z-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-flush-20260902b", created by: git worktree add --no-track "$TMPDIR/fiducial-flush-20260902b" -b open-items-flush-20260902b origin/main

## Decisions

All content below is ruled by Dave in the decision session (2026-09-02:
bundle-system cycle 1 triage, agreement at cycle 2). This directive lands
the record; it decides nothing.

### FL-1 — accept: one decision-log entry, dictated verbatim
Resolution: append to decisions/log.md, after the last entry, exactly:

    ## DEC-000350 — Audience value critic is the writing Critic's alone; the SRE engagement role becomes sre-critic
    Date: 2026-09-02
    Decision: The SRE engagement's critic role document is renamed
    sre-critic (basename, and therefore audience value), and the
    engagement files tagged critic are retagged sre-critic; the rename
    lands in the bundle-system tagging package. Role-document basenames
    are unique across roles/ and engagements/; a future collision is a
    detectable defect.
    Context: Owner decision (Dave), 2026-09-02, disposing
    reviews/bundle-system-cycle-1.md finding B-1: the value critic named
    two role documents, emitting a 28-file critic bundle against a
    five-file target. The uniqueness rule is stated in
    specs/bundle-system.md, agreed at cycle 2.

Dictated wording: the entry above, verbatim, indentation removed (it is
indented here only to survive this directive's formatting).

### FL-2 — accept: OPEN-ITEMS closures and queue updates
Resolution: in OPEN-ITEMS.md, wording the executor's where not quoted:
1. Queue item 2 (bundle PRD): append "AGREED 2026-09-02 at cycle 2
   (reviews/bundle-system-cycle-2.md; reviewed document SHA
   7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4; flip pull request #283).
   Build packages remain queued."
2. specs/directive-tooling-trd.md rider queue: append the pointer the
   previous flush's FL-3.4 stopped on, into this pile: "directive-tooling
   TRD lines ~808-810 quote old Decision Layer rule 14 verbatim — the
   TRD's own B3/G6 defect class; recorded as DL-4 in
   reviews/decision-layer-cycle-14.md."
3. New queued package, beside the other queued cycles — "Tagging package
   (bundle-system PRD): the sre-critic rename and engagement retags per
   DEC-000350; skills/outline.md human-value removal per DEC-000340;
   order: on the copy-editor and critic role files (cycle-1 O-4). After
   the rename lands, one PRD conform touch folds the two wording residues
   from pull request #282 (the six-further-files count includes the role
   file itself; §1's five measured ways against §5's seven baseline
   paragraphs)."
4. New queued entry — "prd-template cycle: the skeleton's [all-roles,
   human] audience default would violate the agreed PRD's AC-BS-5
   (cycle-1 O-5)."
5. Tooling-facts pile: append "Process substitution (<(...)) is refused
   by the executor sandbox; use temp files. Observed by two executors
   2026-09-02."

## Deferred / out of scope

- The tagging package, the prd-template cycle, and every other queued
  cycle — later directives.
- The six unlogged decisions from the 15-hour session — reconstruction
  still owed; their entry stands untouched.

## Execution notes

- Touch only OPEN-ITEMS.md and decisions/log.md; one commit carrying
  both, after the directive's own commit.
- decisions/log.md is append-only: add the entry at the end; edit nothing
  above it. Before appending, read the last entry's ID and confirm it is
  DEC-000340; if it is not, stop and report.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin open-items-flush-20260902b, without -u.
- Do not open a pull request; the decision session opens it.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
0e1cd5f113949d9f44893b41ad51066a18671963. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276
- decisions/log.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276
- reviews/bundle-system-cycle-1.md @ 42636f35f4407ffacc37626ab8f0240fb0c70740
- reviews/bundle-system-cycle-2.md @ 46d3e7035b681a9d1f6a2c9e80ac63bd4877c560

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

1. grep -c "^## DEC-" decisions/log.md before and after the append; after
   equals before plus one; DEC-000350 confirmed present by grep. Output
   captured to "$TMPDIR/fiducial-flush-20260902b-verify.log".
2. bin/check-frontmatter --all, exit status reported, captured beside it.
3. git diff origin/main --stat: exactly OPEN-ITEMS.md, decisions/log.md,
   and this directive file.

STOP CONDITIONS

Pinned to the reviewed ref 0e1cd5f113949d9f44893b41ad51066a18671963. Cannot execute as written: stop
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

    Flush 2026-09-02 — sre-critic entry, item-2 close, tagging package Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
