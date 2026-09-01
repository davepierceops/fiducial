# Retro-skill cycle 4 — confirmation-scoped re-gate Directive

Date: 2026-08-31
Documents in scope:
- skills/conversation-retro.md @ ac286022bb01a0f04e5c402f6b9e379213ff5030

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/conversation-retro-cycle-4-regate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-retro-cycle-4-regate", created by: git worktree add --no-track "$TMPDIR/fiducial-retro-cycle-4-regate" -b retro-cycle-4-regate origin/main

## Decisions

This is a re-gate. A re-gate disposes nothing and takes no new decision; the
dispositions of cycle 3 are ruled and stand. Nothing is disposed here.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored
nothing under review. Confirmation-scoped re-gate, NOT a fourth full-depth
read: cycle 3 read the document whole, and Dave has bound the scope to
confirming that its dispositions landed. Confirm exactly three things, by
reading and by running where the artifacts permit:

1. Each cycle-3 disposition is realized as ruled in
   docs/cycles/conversation-retro-cycle-3-fix-directive.md — F-1 through
   F-9 landed at the locations the fix report names, F-10 untouched in both
   files. Intent was binding; wording was the Editor's except where the
   directive dictated it, and dictated phrases are confirmed present.
2. The two Editor judgment calls the fix disclosed hold against the rubric:
   (a) the Decision Layer rule-12 reference is carried by document name, not
   by path — criterion 3 and criterion 4 both satisfied, and criterion 1
   holds because the two documents share every bundle they appear in
   (confirm by running bin/bundle); (b) the F-6 filename match is narrowed
   to telling a retro from a synthesis, consistent with the retained line
   that the schema header is a retro's canonical identity.
3. No new contradiction between the document and the governed text it
   cites, over the text the fix touched (ac28602's diff). Do not re-derive
   findings cycle 3 dispositioned; do not re-open dispositioned conflicts.

A finding outside these three confirmations is out of scope unless it is a
new blocking contradiction introduced by the fix, in which case file it.

ARTIFACT. Produce reviews/conversation-retro-cycle-4.md per
skills/review-artifact.md, verdict first; state the confirmation scope in the
Scope line and independence in the Reviewer line; Prior cycle is
reviews/conversation-retro-cycle-3.md. Expected verdicts: ready or
ready-with-findings if the three confirmations hold; changes-required only on
a failed confirmation or a new blocking contradiction. This session creates
exactly two files — this directive file and the review artifact — and
modifies nothing. Review only: no edits to skills/conversation-retro.md or
any governed file.

## Deferred / out of scope

- Findings triage and the agreement flip — the decision session's next
  steps after this report; the flip is a separate directive after Dave
  agrees.
- F-10's policy-side correction — policies/document-metadata-policy.md next
  cycle; not this session's to assess.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin <branch>, without -u; the sandbox denies the
  upstream-config write and the noise is avoidable.
- Do not open a pull request; push the branch and report. The decision
  session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
b785309d4aa734058483a116e86cdc5238da3180. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/conversation-retro.md @ ac286022bb01a0f04e5c402f6b9e379213ff5030
- reviews/conversation-retro-cycle-3.md @ 7ff78ef4174e55c425ea092660f8b0ab3e24be95
- docs/cycles/conversation-retro-cycle-3-fix-directive.md @ 909f22b432173e013be902ed119a125d6d9b875f
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- docs/global-context/decision-layer.md @ 5aa0b9a20f42a59fdf8e9f479ccb2e4372de1f9b

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
   "$TMPDIR/fiducial-retro-cycle-4-regate-frontmatter.log", exit status
   reported.
2. The review artifact's verdict line stated verbatim in the report, with
   each of the three confirmations stated pass/fail and its evidence class,
   and findings by severity if any.

STOP CONDITIONS

Pinned to the reviewed ref ac286022bb01a0f04e5c402f6b9e379213ff5030 (the document commit) on main at b785309d4aa734058483a116e86cdc5238da3180. Cannot execute as written: stop
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

    Retro-skill cycle 4 — confirmation-scoped re-gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
