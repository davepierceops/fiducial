# Converging model — fix 2 (stale facts in the discipline context set) Directive

Date: 2026-09-02
Documents in scope:
- context-sets/spec-and-change-discipline.md @ dd86a8a99349324a02bb87c8ab373f937de8f7c3

ROUTE AND MODEL

Route: fresh
Model: solid

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-fix-2-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-converging-model-fix-2", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model-fix-2" -b converging-model-fix-2 origin/main

## Decisions

Two changed facts the converging-model fix revision (PR #289) left stale in
a file outside its scope, named by that executor's report (told) and
confirmed by reading at the base ref (observed by the decision session).
Mechanical; no judgment.

### F2-1 — accept
Finding: context-sets/spec-and-change-discipline.md, "The red-gate", says
spec and test discipline governs steps 1 through 5 and the flow continues at
steps 6 through 9. operating-model.md at its reviewed revision numbers the
flow as stages 1–12: spec lifecycle 1–4, per-change 5–12.
Resolution: restate the sentence against the new numbering — the discipline
governs the spec lifecycle (stages 1–4) and the per-change stages through
implement-to-green (5–8); the flow continues through quality review,
skeptic/risk review, release package, and release gate (9–12). Use the word
the operating model uses for the numbered items.
Dictated wording: none.

### F2-2 — accept
Finding: "An open spec delta is not convergence" says converging is "a status
interval before the spec's first agreement"; LEXICON.md and the metadata
policy at their reviewed revisions state that a revision of an agreed spec
may re-enter converging.
Resolution: reword so the sentence distinguishes the two by kind (a delta is
a branch interval on an agreed spec; converging is a status interval, before
first agreement or on a revision that re-enters it) without the retired
"before first agreement" restriction.
Dictated wording: none.

## Deferred / out of scope

- The confirmation-scoped re-gate over the nine-document branch — a later
  directive; then nine flips.

## Execution notes

- Edit context-sets/spec-and-change-discipline.md only, one commit. The
  document is already in-review / null; leave the frontmatter as it is.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin converging-model-fix-2 — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
58650535030fd527e4d5469459570ba2f8cbec37. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- context-sets/spec-and-change-discipline.md @ dd86a8a99349324a02bb87c8ab373f937de8f7c3
- operating-model.md @ bf0fa24d250325f1b63ee138752803288ce34f67
- LEXICON.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
- policies/document-metadata-policy.md @ d96ef65a802fba5735aae432222cab44c976fdc6

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
   "$TMPDIR/fiducial-converging-model-fix-2-frontmatter.log", exit status
   reported.
2. git diff --stat against the base ref, captured to
   "$TMPDIR/fiducial-converging-model-fix-2-diffstat.log"; expected: this
   directive file and context-sets/spec-and-change-discipline.md only.

STOP CONDITIONS

Pinned to the reviewed ref 58650535030fd527e4d5469459570ba2f8cbec37. Cannot execute as written: stop
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

    Converging model — fix 2 (stale facts in the discipline context set) Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
