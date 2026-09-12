# Intake read: tree-fact-rows-nb — four bodies, three retirements, one row, over e7f5994..74ebe08

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; you run as the Context Quality Reviewer, you did not produce
the delta under review, and the branch you push to is a read branch, not main.

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/tree-fact-rows-nb-read-20260911T230000Z.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-tree-fact-rows-nb-read", created by: git worktree add --no-track "$TMPDIR/fiducial-tree-fact-rows-nb-read" -b tree-fact-rows-nb-read origin/tree-fact-rows-nb

Order of operations: fetch origin tree-fact-rows-nb, create the worktree
first, then perform FIRST ACT inside it. Holder check, before the worktree is
created: run git worktree list, and stop and report if any worktree holds
branch tree-fact-rows-nb-read or the path already exists. Push every commit
with: git push origin tree-fact-rows-nb-read — no upstream is set. The
decision session lands it.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
74ebe0867f698b4c3d3ab3a5846fb68c3cf40d53. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/review-artifact.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the artifact's form
- rules/R0264.md and rules/R1605.md, at the base ref — the intake checklist and the co-render constraint
- reviews/tree-fact-rows-read-20260911T180000Z.md, at the base ref — the read whose findings NB-1 through NB-5 this delta answers
- docs/cycles/tree-fact-rows-nb-20260911T210000Z.md, at the base ref — the directive that produced the delta; the two commits after its package are a command-block restoration of four retired rows under rules/retired/, ruled by the human

TASK

Run the intake read over the rules delta e7f5994..74ebe08: the diff
whole, organised by dimension, not by file. You did not produce this delta.
It replaces the bodies of R1606, R1607, R1609 and R1610; re-keys R1609 to
both sessions; retires R1220, R1228 and R0188 into R1609 and R1607, and
R1283 into R1608, all four now under rules/retired/ with a retired: line;
adds R1612; and appends DEC-000810 through DEC-000870.

1. Continuity: does each replaced body still answer the finding it was
   changed for — R1606 against R1293 (NB-1), R1607 against the retired R0188
   (NB-4), R1609 against the retired R1220 and R1228 (NB-3) — and does no
   row in force now restate one of the four retired rows? Confirm the
   retired rows are not returned by any query. Confirm R1612 does not
   restate R0262 or any other decision-layer row.
2. Quality and skepticism, as your bundle states them for a rules delta:
   each changed or new row against every R0264 criterion, the criterion
   named in any finding; the seven decision-log entries against the form
   process/decision-log.md states and against the rows they record.
3. State the pre-merge boundary: bin/bundle --where refuses on a branch;
   use bin/bundle --keys and the rows' own keys for reach.
4. Write exactly one review artifact to
   reviews/tree-fact-rows-nb-read-20260911T230000Z.md — confirm the path is
   absent at the reviewed ref before writing — with the header the form
   states, Baseline e7f5994, one overall Verdict: line and one
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

- git diff --stat e7f5994..74ebe08 2>&1 | tee "$TMPDIR/tree-fact-rows-nb-read.log" — the delta you read; report the file list.
- bin/bundle --keys 2>&1 | tee -a "$TMPDIR/tree-fact-rows-nb-read.log" — expected exit 0.
- bin/tests/run 2>&1 | tee -a "$TMPDIR/tree-fact-rows-nb-read.log" — expected OK.
- git diff --stat 74ebe08..HEAD — expected: this directive and the artifact, nothing else.

STOP CONDITIONS

Pinned to the reviewed ref 74ebe0867f698b4c3d3ab3a5846fb68c3cf40d53. Cannot execute as written: stop
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
report's final line. The log at "$TMPDIR/tree-fact-rows-nb-read.log" is
outside the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Intake read: tree-fact-rows-nb — four bodies, three retirements, one row, over e7f5994..74ebe08 — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
