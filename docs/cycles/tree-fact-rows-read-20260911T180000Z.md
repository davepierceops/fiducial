# Intake read: tree-fact-rows — six rows, one retirement, over d44ad52..6b35460

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; you run as the Context Quality Reviewer, you did not produce
the delta under review, and the branch you push to is a read branch, not main.

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/tree-fact-rows-read-20260911T180000Z.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

Fence note: the inner fences below are `~~~` so this directive pastes whole
inside a `~~~~` block.

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

~~~text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
~~~

Both admitted forms, worked:

~~~text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
~~~

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-tree-fact-rows-read", created by: git worktree add --no-track "$TMPDIR/fiducial-tree-fact-rows-read" -b tree-fact-rows-read origin/tree-fact-rows

Order of operations: fetch origin tree-fact-rows, create the worktree first,
then perform FIRST ACT inside it. Holder check, before the worktree is created:
run git worktree list, and stop and report if any worktree holds branch
tree-fact-rows-read or the path already exists. Push every commit with: git
push origin tree-fact-rows-read — no upstream is set. The decision session
lands it.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
6b35460ba1858854e3d024b6e8331123860a1476. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/review-artifact.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the artifact's form
- rules/R0264.md and rules/R1605.md, at the base ref — the intake checklist and the co-render constraint
- docs/cycles/tree-fact-rows-20260911T003000Z.md and docs/cycles/tree-fact-rows-fix-20260911T170000Z.md, at the base ref — the directives that produced the delta; the second records the human's ruling on the R1283 citations

TASK

Run the intake read over the rules delta d44ad52..6b35460: the diff whole,
organised by dimension, not by file. You did not produce this delta. It adds
six rows — R1606 through R1611 — deletes R1283, and appends DEC-000740
through DEC-000800.

1. Continuity: for each new row, the near-duplicate shortlist against the
   store plus judgment — does it restate a surviving row? R1607 sits beside
   R0458, R1609 beside R1228, R1611 beside R0180 and R0181, R1608 replaces
   R1283; say for each whether the pair is distinct or a restatement. Confirm
   no row in force cites [R1283]. Confirm each new row's citations, if any,
   co-render under R1605. The three citations of R1283 under
   docs/rule-register/ are derived records the human has ruled stand as
   written; record them as an observation, not a finding.
2. Quality and skepticism, as your bundle states them for a rules delta:
   every new row against every R0264 criterion, the criterion named in any
   finding. Check the seven decision-log entries against the form
   process/decision-log.md states and against the rows they record.
3. One verification claim you cannot make: bin/bundle --where refuses on any
   branch, so rendered bundles are not checkable pre-merge. Use bin/bundle
   --keys and the rows' own keys for reach; state the boundary in the
   artifact.
4. Write exactly one review artifact to
   reviews/tree-fact-rows-read-20260911T180000Z.md — confirm the path is
   absent at the reviewed ref before writing — with the header the form
   states, Baseline d44ad52, one overall Verdict: line and one
   Verdict (<pass>): line per pass, values ready, ready-with-findings, or
   changes-required. Commit it alone, push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- git diff --stat d44ad52..6b35460 2>&1 | tee "$TMPDIR/tree-fact-rows-read.log" — the delta you read; report the file list.
- bin/bundle --keys 2>&1 | tee -a "$TMPDIR/tree-fact-rows-read.log" — expected exit 0.
- git diff --stat 6b35460..HEAD — expected: this directive and the artifact, nothing else.

STOP CONDITIONS

Pinned to the reviewed ref 6b35460ba1858854e3d024b6e8331123860a1476. Cannot execute as written: stop
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

None. Findings go in the artifact for the decision session to triage; you
change no row and no entry.

## Deferred / out of scope

- The pull request and the landing — the decision session's.

## Execution notes

Remove the worktree after the report is composed and the push is verified
landed, without force and without retry, and state the outcome as the
report's final line. The log at "$TMPDIR/tree-fact-rows-read.log" is outside
the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Intake read: tree-fact-rows — six rows, one retirement, over d44ad52..6b35460 — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    Provenance — author region
    ROUTE AND MODEL — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    FIRST ACT — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    DISPOSITION PROMPT — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    COMPANIONS — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    TASK — author region
    SANDBOX — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    VERIFICATION — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    STOP CONDITIONS — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    REPORT — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    CLAIM LABELS — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
    Decisions — author region
    Deferred / out of scope — author region
    Execution notes — author region
    SOURCE MANIFEST — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2

ROUTE AND MODEL

Route: fresh session
Model: frontier
