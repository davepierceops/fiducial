# Amendment C — prose-criteria-rows: record the amendment-B rulings, widen R1605's reach

ROUTE AND MODEL

Route: fresh session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/prose-criteria-rows-20260909T190000Z-amend-c.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-prose-criteria-rows-c", created by: git worktree add --no-track "$TMPDIR/fiducial-prose-criteria-rows-c" -b prose-criteria-rows-c origin/prose-criteria-rows

Holder check, before the worktree is created: fetch origin prose-criteria-rows, run git worktree list, and stop and report if any worktree holds branch prose-criteria-rows-c or the path already exists. Work on prose-criteria-rows-c; push every commit with: git push origin prose-criteria-rows-c — no upstream is set. The decision session lands it on prose-criteria-rows.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
88d4b5b8eaed45b58edb95e21436f9aed99d7474. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- rules/R1605.md and rules/R0246.md @ 88d4b5b
- docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md @ 88d4b5b

TASK

Record of rulings (decision session, 2026-09-09), given in chat to the session that executed amendment B and never before written to a file. These supersede amendment B where they differ:

- R1013 cites four structure rows, not five: [R0835, R0844, R0846, R0849]. R0845 is a definition row with no role, session, or corpus key; it is not a defect and cannot co-render.
- R1605's session is [decision, execution]: it governs the session that dictates a row body and the session that gates it.
- A store-born row's source: is path:1 @ <7-character SHA>, the store's dominant form; the two 40-character rows are the outliers, not the model.

Edit, one commit:

1. R1605's role becomes every role R0246 carries plus context-quality-reviewer, in the order R0246 lists them with context-quality-reviewer last. Report the resulting list.
2. R1605's source: becomes this directive's path at the SHA you reported in the first act, in the form above.
3. Nothing else changes. Commit message: "rules: R1605 reaches every role that writes a citation; amendment C records the rulings behind 88d4b5b". Push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/prose-criteria-rows-c.log" — expected OK.
- git diff --stat 88d4b5b..HEAD 2>&1 | tee -a "$TMPDIR/prose-criteria-rows-c.log" — report the file list; two files is the intent.
- For each of R1013's five citations, and for R1605 against every row in topic intake and against R0246: does R1605's constraint hold? Report the table.

STOP CONDITIONS

Pinned to the reviewed ref 88d4b5b8eaed45b58edb95e21436f9aed99d7474. Cannot execute as written: stop
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

## Decisions

The record above; nothing further.

## Deferred / out of scope

- F-6 (R0835's second sentence), O-10 (the two 40-character source SHAs), the process delta, the parallel-row sweep, the bin/bundle branch-render gap — loose-end tracker.

## Execution notes

Remove the worktree after the report is composed and every push is verified landed, without force and without retry, and state the outcome as the report's final line.

SOURCE MANIFEST

- # heading — author region
- ROUTE AND MODEL, FIRST ACT, BASE VERIFICATION, COMPANIONS, SANDBOX, VERIFICATION, STOP CONDITIONS, REPORT, CLAIM LABELS — process/directive-invariants.md @ 2383eae
- WORKING-TREE DISPOSITION, TASK, Decisions, Deferred, Execution notes — author regions
