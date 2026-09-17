# criteria rows read: intake read over the rules delta 8127f1e..9b8f599

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; the tree it names is the one it is written to. Landings in this
directive use bin/land, agent-facing under DEC-000950 on the reviewed branch.

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/criteria-rows-read-20260917T033521Z.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-criteria-rows-read", created by: git worktree add --no-track "$TMPDIR/fiducial-criteria-rows-read" -b criteria-rows-read origin/criteria-rows

Order of operations: fetch origin criteria-rows, create the worktree first,
then perform FIRST ACT inside it. Holder check, before the worktree is
created: run git worktree list, and stop and report if any worktree holds
branch criteria-rows-read or the path already exists.

Landing, for FIRST ACT and for the review artifact: run bin/land from the
worktree root — bin/land criteria-rows-read "<message>" <path> — with the one
file each commit carries as its path. bin/land fetches, resolves the base
from origin, stages, commits, pushes once, reads the result back, and creates
criteria-rows-read at origin on the first landing; its stdout is a JSON
report with every fact labelled observed or unknown, and exit 0 means the
landing was verified. Paste each report verbatim into your report. bin/land
performs FIRST ACT's commit and push; run no git commit and no git push by
hand. A non-zero exit is a stop: report the JSON and the stderr diagnostic
and do nothing else to the remote. No upstream is set. The decision session
opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
9b8f5991cc5f543fd569f36b02e37c26960c9c79. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/review-artifact.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the artifact's form
- rules/R0264.md and rules/R1605.md, at the base ref — the intake checklist and the co-render constraint
- reviews/process-criteria-refs-read-20260910T193000Z.md, at the base ref — the read whose findings F1 and F3 this delta answers
- docs/cycles/criteria-rows-20260917T030541Z.md, at the base ref — the directive that produced the delta; the third commit on the branch is a command-block fix of R1015's condition line, ruled by the human after the executor reported the directive had left it out

TASK

Run the intake read over the rules delta 8127f1e..9b8f599: the diff whole,
organised by dimension, not by file. You did not produce this delta. It
replaces the body of R1015 so it cites [R0853] where it named a criteria
document, and R1015's condition line the same way; replaces the body of
R1171 so the voice harvest names the prose-criteria rows in the bundle; and
appends DEC-000950, which makes bin/land agent-facing.

1. Continuity: does R1015 now answer F1 and R1171 answer F3 of the 2026-09-10
   read; does no row or process document in force still name a criteria
   document — confirm by grep -rn -i "the Criteria" over rules/, process/
   and README.md at the reviewed ref, reporting the count; does the [R0853]
   citation in R1015 co-render under R1605 — R0853 must reach every bundle
   R1015 reaches, established by the rows' own keys since bin/bundle refuses
   on a branch; does DEC-000950 contradict any entry in force, DEC-000920
   and DEC-000330's restated rulings included.
2. Quality and skepticism, as your bundle states them for a rules delta:
   each changed row against every R0264 criterion, the criterion named in
   any finding; DEC-000950 against the form process/decision-log.md states
   and against what it claims — read specs/bin-land.md §3 and §8 and say
   whether J1 and J2 are a sufficient usage statement for an executor that
   has only the directive and the tool's --help.
3. State the pre-merge boundary: bin/bundle --where refuses on a branch; use
   bin/bundle --keys and the rows' own keys for reach.
4. Write exactly one review artifact to
   reviews/criteria-rows-read-20260917T033521Z.md, confirming the path is absent at
   the reviewed ref before writing, with the header the form states,
   Baseline 8127f1e, one overall Verdict: line and one Verdict (<pass>):
   line per pass, values ready, ready-with-findings, or changes-required.
   Land it alone with bin/land.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/criteria-rows-read.log" — expected OK, with the same skips the base shows.
- grep -rn -i "the Criteria" rules/ process/ README.md 2>&1 | tee -a "$TMPDIR/criteria-rows-read.log" — expected no output; report the count.
- Both bin/land JSON reports, verbatim.

STOP CONDITIONS

Pinned to the reviewed ref 9b8f5991cc5f543fd569f36b02e37c26960c9c79. Cannot execute as written: stop
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

None; this directive rules on nothing. Findings are for the decision
session's triage.

## Deferred / out of scope

- Any edit to the reviewed rows or the log — a finding, not a fix.
- The pull request — the decision session's.

## Execution notes

Remove the worktree after the report is composed and both landings are
verified by their reports, without force and without retry, and state the
outcome as the report's final line. The log at
"$TMPDIR/criteria-rows-read.log" is outside the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    criteria rows read: intake read over the rules delta 8127f1e..9b8f599 — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
