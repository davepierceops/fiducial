# Decision Layer cycle 15 — confirmation-scoped re-gate Directive

Date: 2026-09-02
Documents in scope:
- docs/global-context/decision-layer.md @ 999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/decision-layer-cycle-15-regate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-decision-layer-cycle-15-regate", created by: git fetch origin decision-layer-human-review && git worktree add --no-track "$TMPDIR/fiducial-decision-layer-cycle-15-regate" -b decision-layer-cycle-15-regate origin/decision-layer-human-review

## Decisions

This is a re-gate. It disposes nothing and takes no new decision; Dave has
ruled cycle 14's DL-1 blocking and its fix is on the branch. Confirm three
things, NOT a fresh full read — cycle 14 read the document whole:

1. DL-1 is resolved as ruled: rule 13's final sentence owes a baton to a
   successor decision session only, consistent with Core's Baton entry.
2. The document's only delta from the cycle-14 reviewed ref
   3e89a2117e35f34746aff005c19bc3c6227bf8f4 is that one rule-13 line —
   confirm by running git diff between the two revisions of the file.
3. No new contradiction between the changed line and the governed text it
   touches (Core's vocabulary, the Lexicon). Do not re-derive cycle 14's
   findings; DL-2 and DL-4 stand as recorded there.

ARTIFACT. Produce reviews/decision-layer-cycle-15.md per
skills/review-artifact.md, verdict first; state the confirmation scope in
the Scope line; Prior cycle is reviews/decision-layer-cycle-14.md. Expected
verdicts: ready or ready-with-findings if the confirmations hold;
changes-required only on a failed confirmation or a new blocking
contradiction. This session creates exactly two files — this directive file
and the review artifact — and modifies nothing. Before writing the
artifact, confirm by listing that reviews/decision-layer-cycle-15.md does
not exist at the base; if it exists, stop and report.

## Deferred / out of scope

- Cycle 14's DL-2 (pane naming) — rider for the Decision Layer's next
  cycle; DL-4 — the Spec Reviewer's queue.
- The agreement flip and the merge to main — the decision session's next
  steps.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin decision-layer-cycle-15-regate, without -u.
- Do not open a pull request; the decision session opens it, into
  decision-layer-human-review, not main.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec on branch decision-layer-human-review. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/global-context/decision-layer.md @ 999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec
- reviews/decision-layer-cycle-14.md @ ce409907e29de97ff956986ddc9b74c5de3e64ae
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d

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
   "$TMPDIR/fiducial-decision-layer-cycle-15-regate-frontmatter.log", exit
   status reported.
2. The confirmation diff (git diff 3e89a2117e35f34746aff005c19bc3c6227bf8f4
   999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec --
   docs/global-context/decision-layer.md) captured beside it; the changed
   lines stated.
3. The review artifact's verdict line stated verbatim in the report, with
   each confirmation stated pass/fail and its evidence class.

STOP CONDITIONS

Pinned to the reviewed ref 999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec on branch decision-layer-human-review. Cannot execute as written: stop
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

    Decision Layer cycle 15 — confirmation-scoped re-gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
