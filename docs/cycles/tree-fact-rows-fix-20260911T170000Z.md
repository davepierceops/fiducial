# tree-fact-rows fix: R1283 retires; decision-log entries restated one rule each

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; the tree it names is the one it is written to, and the branch it
touches is an unmerged package branch, not main.

ROUTE AND MODEL

Route: fresh session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/tree-fact-rows-fix-20260911T170000Z.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-tree-fact-rows-fix", created by: git worktree add --detach "$TMPDIR/fiducial-tree-fact-rows-fix" origin/tree-fact-rows

Order of operations: fetch origin tree-fact-rows, create the worktree first,
then perform FIRST ACT inside it. Holder check, before the worktree is created:
run git worktree list, and stop and report if any worktree already holds the
path. The worktree is detached; push every commit with: git push origin
HEAD:tree-fact-rows — no upstream is set, and the branch is the package's own,
not main. The decision session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
125f7003cbc4d9c04cd0d4d12281b659f583a116. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/tree-fact-rows-20260911T003000Z.md @ 4502c64dabd3a3b5612750c2a8d2d78db7ad86f0 — the package this fixes
- process/decision-log.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the entry form
- rules/R1606.md through rules/R1611.md, and rules/R1283.md, each at the base ref — the rows the entries record and the row that retires

TASK

Intent: close the two items the tree-fact-rows execution left open — the
retirement of R1283, stopped on citations the human has since ruled do not
need re-pointing, and the six decision-log entries DEC-000740 through
DEC-000790, which as landed do not state the rule each one agrees. The branch
is unmerged, so the entries are rewritten in place, not superseded.

1. Delete rules/R1283.md. The human's ruling, 2026-09-11: files under
   docs/rule-register/ are dated derived artifacts and are never re-pointed;
   a citation of R1283 there does not block the deletion.

2. Rewrite DEC-000740 through DEC-000790 in decisions/log.md, keeping each
   entry's number and Date. Each entry's title is the short title below; its
   Decision line is: the row's id, its topic in parentheses, the words "is
   agreed:", then the row's body verbatim from the row file at the base ref;
   its Context line is the one already there. Nothing else in the log changes.

   DEC-000740 — R1606: dictate intent and agreed prose, never tree facts
   DEC-000750 — R1607: a tree-resolvable precondition is resolved, not stopped on
   DEC-000760 — R1608: every new directive routes to a fresh session
   DEC-000770 — R1609: a block is tested end-to-end, substitution bound
   DEC-000780 — R1610: dictated text is verified by byte-for-byte diff
   DEC-000790 — R1611: read the spec spine whole before directing against it

3. Append one entry, numbered by the log's rule from the last entry on the
   base, dated 2026-09-11:

   R1283 retires into R1608 — Decision: rules/R1283.md is deleted; R1608
   carries the route obligation, and the amendment route is the only
   existing-session route. Context: the 2026-09-09 read that became a
   self-review; the three citations of R1283 under docs/rule-register/ are
   derived records and stand as written.

One commit, message "rules: R1283 retires into R1608; decisions: entries
DEC-000740–000790 state one rule each, DEC entry for the retirement". Push.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/tree-fact-rows-fix.log" — expected OK.
- git diff --stat 125f700..HEAD 2>&1 | tee -a "$TMPDIR/tree-fact-rows-fix.log" — report the file list; the intent is one deleted, decisions/log.md modified, plus this directive.
- For each of the six rewritten entries: extract the body from the Decision line and diff it against the row file's body at the base ref; report six results, expected identical.
- grep -rn "R1283" --include=*.md . | grep -v docs/history | grep -v docs/rule-register 2>&1 | tee -a "$TMPDIR/tree-fact-rows-fix.log" — expected: the two tree-fact-rows directives and the retirement entry only.

STOP CONDITIONS

Pinned to the reviewed ref 125f7003cbc4d9c04cd0d4d12281b659f583a116. Cannot execute as written: stop
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

The rulings in TASK; nothing further. A choice the tree resolves is reported,
not stopped on (R1607 at the base ref).

## Deferred / out of scope

- The pull request for tree-fact-rows and its intake read — the decision
  session's, after this lands.

## Execution notes

Remove the worktree after the report is composed and the push is verified
landed, without force and without retry, and state the outcome as the
report's final line. The log at "$TMPDIR/tree-fact-rows-fix.log" is outside
the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    tree-fact-rows fix: R1283 retires; decision-log entries restated one rule each — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
Model: solid general-purpose
