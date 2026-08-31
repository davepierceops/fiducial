# Retro-skill cycle 1 — Context Quality Reviewer gate Directive

Date: 2026-08-31
Documents in scope:
- skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/conversation-retro-cycle-1-gate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-retro-cycle-1-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-retro-cycle-1-gate" -b retro-cycle-1-gate origin/main

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens the review, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither document nor revision). Full-depth review of
skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb
against docs/global-context/review-rubric.md and LEXICON.md conformance,
including whether the five ruled changes recorded in
docs/cycles/conversation-retro-cycle-1-editor-directive.md (RS-1 through RS-5)
are faithfully realized in the document. Intent was binding, wording was the
Editor's; a wording choice is not a finding unless it breaks a rubric
criterion, the lexicon, or a ruled intent.

ARTIFACT. Produce reviews/conversation-retro-cycle-1.md per
skills/review-artifact.md, verdict first. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to skills/conversation-retro.md or any governed file.

## Deferred / out of scope

- Findings triage, any resulting fix directive, and the agreement flip — the
  decision session's next steps after this report; tracked by the cycle.
- The document's status flip to agreed — a later frontmatter-only
  status-transition commit after Dave agrees; not this session.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
54cc0d21de8f4913a8530715e7e559b9d8b1751f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- docs/cycles/conversation-retro-cycle-1-editor-directive.md @ e41d63f7c4bc39c76007b466ad065119bed3dafe

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
   "$TMPDIR/fiducial-retro-cycle-1-gate-frontmatter.log", exit status
   reported.
2. The review artifact's verdict line stated verbatim in the report, with
   findings by severity if any.

STOP CONDITIONS

Pinned to the reviewed ref 08e54f6be9fdd3df6104e29f9966606fa2b427cb (the document commit) on main at 54cc0d21de8f4913a8530715e7e559b9d8b1751f. Cannot execute as written: stop
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

    Retro-skill cycle 1 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
