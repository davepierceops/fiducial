# Remote-write verification policy cycle 8 — Context Quality Reviewer gate Directive

Date: 2026-09-02
Documents in scope:
- policies/remote-write-verification-policy.md @ 21e0c1e729a689bf7e4687f7e5910f86f972ac48

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/remote-write-verification-policy-cycle-8-gate-directive.md, commit it alone with a
message naming the gate it opens, push with git push origin remote-write-cycle-8-gate (no -u), verify by git ls-remote origin remote-write-cycle-8-gate, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-remote-write-cycle-8-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-remote-write-cycle-8-gate" -b remote-write-cycle-8-gate origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch remote-write-cycle-8-gate, if a branch of that name already exists locally or on origin (git ls-remote origin remote-write-cycle-8-gate returns a ref), or if "$TMPDIR/fiducial-remote-write-cycle-8-gate" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens the review, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither document nor revision). Full-depth review of
policies/remote-write-verification-policy.md @ 21e0c1e729a689bf7e4687f7e5910f86f972ac48
against docs/global-context/review-rubric.md and LEXICON.md conformance,
including whether the five ruled changes recorded in
docs/cycles/remote-write-verification-policy-cycle-8-editor-directive.md (RW-1
through RW-5) are faithfully realized in the document. Intent was binding,
wording was the Editor's; a wording choice is not a finding unless it breaks a
rubric criterion, the lexicon, or a ruled intent. Three items the Editor
flagged for this gate (told — the Editor's report): "never sent" standing in
for the ruling's "never dispatched" under the Lexicon's retirement of the term;
rule 7 treating a confirmed tool defect as a first-instance stop rather than a
counted failure; and rule 5 carrying the literal bin/check-frontmatter --all.
Rule on each as a finding or a non-finding, stated either way. Two
cross-checks in scope: rules 3 through 7 against docs/global-context/core.md
rule 12 for contradiction or redundancy that leaves the two documents saying
different things; and rule 5 against policies/document-metadata-policy.md's
Scope section for whether the citation resolves to what it names.

LOOP START (told — the decision session's statement, Dave's to override): the
agreement bar for this cycle is a verdict of ready or ready-with-findings with
zero blocking findings; cadence is one full-depth gate (this directive), then a
fix directive if findings warrant one, then one confirmation-scoped re-gate
over the fix, then the flip.

ARTIFACT. Produce reviews/remote-write-verification-policy-cycle-8.md per
skills/review-artifact.md, verdict first. Before writing it, confirm the path
is absent at the base ref (git cat-file -e 8d044d7457c36bb30cb898ab3037a9d2c0fce1a6:reviews/remote-write-verification-policy-cycle-8.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to policies/remote-write-verification-policy.md or any
governed file.

## Deferred / out of scope

- Findings triage, any resulting fix directive, the re-gate, and the
  agreement flip — the decision session's next steps after this report;
  tracked by the cycle.
- The document's status flip to agreed — a later frontmatter-only
  status-transition commit after Dave agrees; not this session.
- Closing the two OPEN-ITEMS entries the cycle folds in — the flush after the
  flip.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin remote-write-cycle-8-gate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-remote-write-cycle-8-gate"
  (no --force). If it fails, report the failure; do not retry. Your report's
  final line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
8d044d7457c36bb30cb898ab3037a9d2c0fce1a6. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/remote-write-verification-policy.md @ 21e0c1e729a689bf7e4687f7e5910f86f972ac48
- docs/cycles/remote-write-verification-policy-cycle-8-editor-directive.md @ 0ba2c84c148248f5d310c86003a1fd55b036ac66
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 7b52f6ba0e50f6987993fc29e465dbab6e8d25b8
- skills/spec-review-cycle.md @ 0911b06042f62aabb5de9d5fa49547e93b1eeed8
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5

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
   "$TMPDIR/fiducial-remote-write-cycle-8-gate-frontmatter.log", exit status
   reported.
2. The artifact's header states the reviewed document and SHA above, and its
   verdict line is first; state both, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref 8d044d7457c36bb30cb898ab3037a9d2c0fce1a6. Cannot execute as written: stop
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

    Remote-write verification policy cycle 8 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
