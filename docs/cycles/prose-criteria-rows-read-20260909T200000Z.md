# Intake read: prose-criteria-rows at 8cd16fe

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/prose-criteria-rows-read-20260909T200000Z.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-prose-criteria-rows-read", created by: git worktree add --no-track "$TMPDIR/fiducial-prose-criteria-rows-read" -b prose-criteria-rows-read origin/prose-criteria-rows

Holder check, before the worktree is created: fetch origin main and origin prose-criteria-rows, run git worktree list, and stop and report if any worktree holds branch prose-criteria-rows-read or the path already exists. Push every commit with: git push origin prose-criteria-rows-read — no upstream is set.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
8cd16fed025e264f91fcb7c8fc03cc19b2495cd8. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

Also confirm origin/main is at 28dfdb0560cafcda026c70cd1c7697751b3eac26, the branch point; if it has moved, stop and report.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/review-artifact.md @ 8cd16fe — the artifact schema
- docs/cycles/prose-criteria-rows-20260909T190000Z.md @ ca9fd54 and docs/cycles/prose-criteria-rows-20260909T190000Z-amend-a.md @ 69e720b — the directive and amendment that produced the delta; its Decisions section states the rulings
- rules/R1604.md, rules/R1013.md, rules/R0038.md @ 8cd16fe
- rules/R1161.md, rules/R0953.md, rules/R1001.md @ 28dfdb0 — the retired rows, from the branch point
- rules/R0853.md, rules/R0835.md, rules/R0821.md @ 8cd16fe — the rows the re-citations point at
- process/voice.md and process/outline.md @ 8cd16fe

TASK

Run the intake read over the rules delta 28dfdb0..8cd16fe: the diff whole, organised by dimension, not by file. You did not produce this delta.

1. Continuity: the near-duplicate shortlist for R1604 against the store, plus judgment — does the merged row restate any surviving row, and does retiring the three leave any role without the read-first rule it had? Confirm R0853, R0835, R0821 actually hold what R1013 and R0038 now cite them for. Note that process/outline.md:12 carries a fourth read-first instruction and process/voice.md:11 names the criteria as a document; both are known, out of this delta's scope, and belong to a process delta already tracked — record them as observations, not findings against this delta.
2. Quality and skepticism, as your bundle states them for a rules delta.
3. One verification claim you cannot make: bin/bundle --where refuses on any branch (HEAD must equal origin/main), so the rendered bundles are not checkable pre-merge. Use bin/bundle --keys and the rows' own keys for reach; state the boundary in the artifact.
4. Write exactly one review artifact to reviews/prose-criteria-rows-read-20260909T200000Z.md — confirm the path is absent at the reviewed ref before writing — with one overall Verdict: line and one Verdict (<pass>): line per pass, values ready, ready-with-findings, or changes-required. Commit it alone, push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- git diff --stat 28dfdb0..8cd16fe 2>&1 | tee "$TMPDIR/prose-criteria-rows-read-verify.log" — expected 8 files: two directive files, one row added, three deleted, two modified.
- grep -rn 'R1161\|R0953\|R1001' rules/ process/ 2>&1 | tee -a "$TMPDIR/prose-criteria-rows-read-verify.log" — expected no hits.
- grep -c '^Verdict' on the artifact — expected: the overall line plus one per pass you ran; report the number.
- git diff --stat origin/prose-criteria-rows..HEAD — expected 2 files: this directive and the artifact.

STOP CONDITIONS

Pinned to the reviewed ref 8cd16fed025e264f91fcb7c8fc03cc19b2495cd8. Cannot execute as written: stop
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
- the overall verdict, each pass verdict, and the finding count by label

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

## Decisions

None; this directive rules nothing. The delta's rulings are in its own directive's Decisions section.

## Deferred / out of scope

- process/outline.md:12 and process/voice.md:11 — process delta, loose-end tracker.
- bin/bundle branch-render mode — loose-end tracker.

## Execution notes

Remove the worktree after the report is composed and every push is verified landed, without force and without retry, and state the outcome as the report's final line.

SOURCE MANIFEST

- # heading — author region
- ROUTE AND MODEL — process/directive-invariants.md @ 2383eae
- FIRST ACT — process/directive-invariants.md @ 2383eae
- WORKING-TREE DISPOSITION — author region (form per process/directive-invariants.md @ 2383eae)
- BASE VERIFICATION — process/directive-invariants.md @ 2383eae, plus one author line
- COMPANIONS — process/directive-invariants.md @ 2383eae
- TASK — author region
- SANDBOX — process/directive-invariants.md @ 2383eae
- VERIFICATION — process/directive-invariants.md @ 2383eae
- STOP CONDITIONS — process/directive-invariants.md @ 2383eae
- REPORT — process/directive-invariants.md @ 2383eae, plus one author line
- CLAIM LABELS — process/directive-invariants.md @ 2383eae
- Decisions, Deferred, Execution notes — author regions
