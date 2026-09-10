# Re-read: prose-criteria-rows at 88d4b5b, over the diff since 8cd16fe

ROUTE AND MODEL

Route: existing session — the one that landed docs/cycles/prose-criteria-rows-read-20260909T200000Z.md at 84e6e40
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/prose-criteria-rows-read-2-20260909T230000Z.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-prose-criteria-rows-read-2", created by: git worktree add --no-track "$TMPDIR/fiducial-prose-criteria-rows-read-2" -b prose-criteria-rows-read-2 origin/prose-criteria-rows

Holder check, before the worktree is created: fetch origin prose-criteria-rows, run git worktree list, and stop and report if any worktree holds branch prose-criteria-rows-read-2 or the path already exists. Push every commit with: git push origin prose-criteria-rows-read-2 — no upstream is set.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
88d4b5b8eaed45b58edb95e21436f9aed99d7474. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md @ 88d4b5b — the triage of your read's findings
- your own artifact, reviews/prose-criteria-rows-read-20260909T200000Z.md @ 78b0894, fetched from origin/prose-criteria-rows-read

TASK

One read over the diff 8cd16fe..88d4b5b — the delta since your read. Check that F-1, F-2 and F-3 are resolved as amendment B triages them and that the diff introduces nothing your read did not cover; the constraint row R1605 is new text and gets the near-duplicate shortlist. Write exactly one review artifact to reviews/prose-criteria-rows-read-2-20260909T230000Z.md — confirm the path is absent first — with one overall Verdict: line and one per pass. Commit it alone, push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- git diff --stat 8cd16fe..88d4b5b 2>&1 | tee "$TMPDIR/prose-criteria-rows-read-2.log" — report the file list.
- grep -c '^Verdict' on the artifact — report the count.

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
- the overall verdict and each pass verdict

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

## Decisions

None; amendment B holds the rulings.

## Deferred / out of scope

- Everything on the loose-end tracker from the first read: O-3, the process delta, the bin/bundle branch-render gap.

## Execution notes

Remove the worktree after the report is composed and every push is verified landed, without force and without retry, and state the outcome as the report's final line.

SOURCE MANIFEST

- # heading — author region
- ROUTE AND MODEL, FIRST ACT, BASE VERIFICATION, COMPANIONS, SANDBOX, VERIFICATION, STOP CONDITIONS, REPORT, CLAIM LABELS — process/directive-invariants.md @ 2383eae
- WORKING-TREE DISPOSITION, TASK, Decisions, Deferred, Execution notes — author regions
