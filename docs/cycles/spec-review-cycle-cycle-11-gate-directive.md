# Spec-review-cycle skill cycle 11 — Context Quality Reviewer gate Directive

Date: 2026-09-02
Documents in scope:
- skills/spec-review-cycle.md @ 7600590f900fd195eeb0763e87f36bbf4ec1f092

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/spec-review-cycle-cycle-11-gate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-spec-review-cycle-11-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-spec-review-cycle-11-gate" -b spec-review-cycle-11-gate origin/main

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens the review, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither document nor revision). Full-depth review of
skills/spec-review-cycle.md @ 7600590f900fd195eeb0763e87f36bbf4ec1f092
against docs/global-context/review-rubric.md and LEXICON.md conformance,
including whether the five ruled changes recorded in
docs/cycles/spec-review-cycle-cycle-11-editor-directive.md (SR-1 through SR-5)
are faithfully realized in the document. Intent was binding, wording was the
Editor's; a wording choice is not a finding unless it breaks a rubric
criterion, the lexicon, or a ruled intent. Two cross-checks in scope: the new
Convergence section against context-sets/spec-and-change-discipline.md (the
red-gate and open-spec-delta rules) for contradiction; and the new re-gate
forms against the two directives that ran a confirmation-scoped re-gate
(companions below) for whether the skill now describes what was practised.

LOOP START, stated here per SR-2 (told — the decision session's statement,
Dave's to override): the agreement bar for this cycle is a verdict of ready or
ready-with-findings with zero blocking findings; cadence is one full-depth gate
(this directive), then a fix directive if findings warrant one, then one
confirmation-scoped re-gate over the fix, then the flip.

ARTIFACT. Produce reviews/spec-review-cycle-cycle-11.md per
skills/review-artifact.md, verdict first. Before writing it, confirm the path
is absent at the base ref (git cat-file -e 759b6217618e06ff7a1cd32c550c6f4df7289f25:reviews/spec-review-cycle-cycle-11.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to skills/spec-review-cycle.md or any governed file.

## Deferred / out of scope

- Findings triage, any resulting fix directive, the re-gate, and the
  agreement flip — the decision session's next steps after this report;
  tracked by the cycle.
- The document's status flip to agreed — a later frontmatter-only
  status-transition commit after Dave agrees; not this session.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin spec-review-cycle-11-gate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
759b6217618e06ff7a1cd32c550c6f4df7289f25. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/spec-review-cycle.md @ 7600590f900fd195eeb0763e87f36bbf4ec1f092
- docs/cycles/spec-review-cycle-cycle-11-editor-directive.md @ 9a2e82b3388c71eb30b65da8d7e2202fbf65b9e4
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- LEXICON.md @ 17960bb7570e1a0abe6ca0492e35f95a15d627cf
- context-sets/spec-and-change-discipline.md @ cac23b8c9e6f3335e930acb7ceb024bd4959c8a9
- policies/document-metadata-policy.md @ 1d6213baf82bd2a9eeb4c10e9dc9b8fb78025390
- docs/cycles/conversation-retro-cycle-4-regate-directive.md @ c0c20b68296e7db03d45f5101559c1d91241945b
- docs/cycles/bundle-system-cycle-2-regate-directive.md @ 34dd22a7944e06b9e4772ddffd905c4088406743

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
   "$TMPDIR/fiducial-spec-review-cycle-11-gate-frontmatter.log", exit status
   reported.
2. The artifact's header states the reviewed document and SHA above, and its
   verdict line is first; state both, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref 759b6217618e06ff7a1cd32c550c6f4df7289f25. Cannot execute as written: stop
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

    Spec-review-cycle skill cycle 11 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
