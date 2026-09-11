# tree-fact-rows NB fix: four bodies amended, three rows retire, one row added

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; the tree it names is the one it is written to, and the branch it
creates is a package branch, not main.

ROUTE AND MODEL

Route: fresh session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/tree-fact-rows-nb-20260911T210000Z.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-tree-fact-rows-nb", created by: git worktree add --no-track "$TMPDIR/fiducial-tree-fact-rows-nb" -b tree-fact-rows-nb origin/main

Order of operations: fetch origin main, create the worktree first, then
perform FIRST ACT inside it. Holder check, before the worktree is created: run
git worktree list, and stop and report if any worktree holds branch
tree-fact-rows-nb or the path already exists. Push every commit with: git push
origin tree-fact-rows-nb — no upstream is set. The decision session opens the
pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
e7f5994d444258de49f761086bf1c394d4cea533. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/tree-fact-rows-read-20260911T180000Z.md, at the base ref — the read whose findings NB-1 through NB-5 this package answers
- rules/R0264.md @ 8c34f936577ffc62d78adfb4f5c0ce864fdcc8e7 — the intake checklist
- process/decision-log.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the entry form
- rules/R1606.md, R1607.md, R1609.md, R1610.md, R1220.md, R1228.md, R0188.md, R0262.md, at the base ref — the rows this package edits, retires, or sits beside

TASK

Intent: the fix package for findings NB-1 through NB-5 of the tree-fact-rows
intake read, ruled by the human on 2026-09-11. Four row bodies are replaced,
three rows retire into rows that now carry their obligation, and one row is
added. Every body below is agreed prose in a fenced block: land it as the
row's body, one line, exactly as fenced. Every key not stated here is
unchanged; every id, order and source you need is derived from the tree and
reported with its evidence.

1. R1606 — body replaced (NB-1 and NB-2); keys unchanged:

~~~text
Dictate intent, acceptance criteria, and prose the human agreed; dictate no tree fact for the executor to land — an id, a key value, a position, which rows carry a term, a tool's existence, a count. A ref pinned for the executor to verify is a claim, read from the tree and cited, not a dictated fact.
~~~

2. R1607 — body replaced (NB-2 and NB-4); keys unchanged:

~~~text
A precondition the tree resolves with no judgment call and no change of intent is resolved and reported, not stopped on; a fact derived from the tree — an id, a position, a key value — is reported with the evidence it was derived from. Stop on what the tree does not resolve.
~~~

3. R1609 — body replaced (NB-3); `session` becomes `[decision, execution]`;
   other keys unchanged:

~~~text
Before handing over a block: every command in it is valid and non-harmful, and re-running it compounds no damage; it has been run end-to-end against a local stand-in for the remote, guard and re-run paths included, with any substituted value bound; its expected output is stated in one line below it, and its blast radius above it where it is destructive.
~~~

4. R1610 — body replaced (NB-5); keys unchanged:

~~~text
Verify dictated text by diffing the landed file against the directive's own fenced block, byte for byte; a heading, a count, or the executor's report is not the check. Text carried by pointer is diffed against its source.
~~~

5. Retire: delete rules/R1220.md and rules/R1228.md (their obligation is
   R1609's) and rules/R0188.md (its obligation is R1607's). Before deleting,
   grep the tree outside docs/history and docs/rule-register for each id and
   report the list; a citation in a row or a process document is a stop.

6. New row — topic `decision-layer`, role `[chief-of-staff]`, session
   `[decision]`, corpus `[software, writing]`, verb `require`, condition and
   term null; placed after R0262 in that topic:

~~~text
Hand a pull request to the human for merging as its URL, alone in a paste block with nothing else in it.
~~~

Decision-log entries, one per ruling, appended in the form
process/decision-log.md states, numbered by its rule from the last entry on
the base, dated 2026-09-11. Each Decision line is the row id, its topic in
parentheses, then "is amended to:" or "is agreed:" followed by the fenced
body verbatim; for a retirement, "is deleted; <surviving row> carries its
obligation". Titles:

   R1606 distinguishes a pinned ref from a dictated tree fact
   R1607 carries the executor's derivation and the stop boundary
   R1609 is the one pre-handover check for a block — R1220 and R1228 retire into it
   R0188 retires into R1607
   R1610 covers text carried by pointer
   A pull request handed for merging is its URL alone

Six entries. Each Context line is one clause naming the finding it answers —
NB-1 through NB-5 of reviews/tree-fact-rows-read-20260911T180000Z.md — or,
for the last, "the human's stated preference, 2026-09-11".

Commits: exactly two after the directive commit — one carrying the four
edits, the three deletions and the new row, message "rules: NB-1–NB-5 fixes;
R1220, R1228, R0188 retire; merge-URL row"; one carrying the six entries,
message "decisions: entries for the tree-fact-rows-nb package". Push after
each.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/tree-fact-rows-nb.log" — expected OK.
- git diff --stat e7f5994..HEAD 2>&1 | tee -a "$TMPDIR/tree-fact-rows-nb.log" — report the file list; the intent is four modified rows, three deleted, one added, decisions/log.md, plus this directive.
- For each of the five fenced bodies: diff the landed row body against the fenced block in this directive at its committed SHA, byte for byte; report five results, expected identical.
- bin/bundle --keys 2>&1 | tee -a "$TMPDIR/tree-fact-rows-nb.log" — expected exit 0.

STOP CONDITIONS

Pinned to the reviewed ref e7f5994d444258de49f761086bf1c394d4cea533. Cannot execute as written: stop
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
not stopped on.

## Deferred / out of scope

- The pull request and the intake read — the decision session's, after this
  lands.

## Execution notes

Remove the worktree after the report is composed and every push is verified
landed, without force and without retry, and state the outcome as the
report's final line. The log at "$TMPDIR/tree-fact-rows-nb.log" is outside
the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    tree-fact-rows NB fix: four bodies amended, three rows retire, one row added — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
