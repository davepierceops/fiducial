# tracker migration: seven decision-log entries recording the 2026-09-14/16 rulings

Provenance: issued by the fiducial decision session for the repository owner,
davepierceops; the tree it names is the one it is written to, and the branch it
continues is a package branch, not main.

ROUTE AND MODEL

Route: fresh session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/tracker-migration-20260916T192443Z.md, commit it alone with a
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
worktree at "wt/<n>", created by: git worktree add --no-track "wt/<n>" -b
<n> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
~~~

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-tracker-migration", created by: git worktree add --no-track "$TMPDIR/fiducial-tracker-migration" -b tracker-migration origin/tracker-migration

Order of operations: fetch origin tracker-migration, create the worktree first,
then perform FIRST ACT inside it. The branch already exists on origin with one
commit past main; this session continues it. Holder check, before the worktree
is created: run git worktree list, and stop and report if any worktree holds
branch tracker-migration or the path already exists. Push every commit with:
git push origin tracker-migration — no upstream is set. The decision session
opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
1a41ea75d37b10280d3601abb0e16c8f60e001a2. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/decision-log.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the entry form and the numbering rule
- docs/research/repository-evaluation-2026-09-14.md, at the base ref — the evaluation the entries record as agreed
- docs/research/evaluation-work-plan-2026-09-14.md, at the base ref — the plan whose agreed items the entries record; its sections D, E item 3, B and F2 are the rulings entries 4 through 7 carry
- decisions/log.md, at the base ref — read whole: the Supersedes derivation below depends on it

TASK

Intent: record in decisions/log.md the rulings the human made on 2026-09-14,
2026-09-15 and 2026-09-16 that today exist only in chat, in issue bodies, and
in the two research documents the base commit landed. Seven entries, one
ruling each, appended in the form process/decision-log.md states, numbered by
its rule from the last entry on the base, dated 2026-09-16. Each entry's
title, Decision line and Context line are dictated below in a fenced block;
land each verbatim as the text after the heading, with the heading composed
as the form states from the derived number and the dictated title. Where an
entry's block ends with a Supersedes derivation, read decisions/log.md whole,
name in a Supersedes: line the entry that governs the thing being changed if
one exists, and omit the line if none does; report the outcome either way,
with the evidence. A Supersedes target that cannot be settled from the log is
reported, not guessed; it is not a stop.

1. Title: The loose-end tracker is GitHub Issues

~~~text
Decision: The loose-end tracker for fiducial is the repository's GitHub Issues and Milestones on davepierceops/fiducial; an open item is an issue, and a pending gate keeps its human-gate label there. OPEN-ITEMS.md is retired: its open residue is filed as issues under #370 and the file moves to docs/history/ once every open entry has a destination.
Context: the human's ruling, 2026-09-16, confirming the direction recorded in docs/research/evaluation-work-plan-2026-09-14.md and #370; two trackers had claimed the same items since #355–#375 were filed.
~~~

Supersedes derivation: an entry deciding where the loose-end tracker lives,
if any.

2. Title: The 2026-09-14 evaluation and its work plan are agreed; #355–#375 are the derived work

~~~text
Decision: docs/research/repository-evaluation-2026-09-14.md and docs/research/evaluation-work-plan-2026-09-14.md are the record of the 2026-09-14 evaluation session, baseline 8ea66f527cf0114441b34976b09a8326fccbf3c2; issues #355 through #375 and their milestones are the work agreed from them. A plan item the work plan marks proposed or not yet agreed is issue text, not a decision, until an entry here says otherwise.
Context: the session ran outside the change flow and left no directive, review artifact or entry; the human handed the two files over on 2026-09-16 and they landed at 1a41ea75d37b10280d3601abb0e16c8f60e001a2.
~~~

3. Title: README agreed at 10471df

~~~text
Decision: README.md is agreed at 10471df5096fc5d5e236423a424b8eaddb998361, the version pull requests #376 and #377 landed; it links GitHub Issues and Milestones as the live roadmap and carries no duplicated task list.
Context: the rewrite closed #369 on 2026-09-15 with the human's own read as its gate; README.md is outside the four delta kinds process/change-flow.md gates, so no read was owed, and this entry is its record.
~~~

4. Title: Harness adapters are thin pointers to a pinned local bundle

~~~text
Decision: CLAUDE.md, AGENTS.md and any other harness entry file are kept as thin pointers that tell the agent where the substantive instructions are — a pinned local bundle — and carry no restated rules. This reverses the removals at 8e26700 and 23c1a57, which deleted the adapters rather than thinning them; the package that lands them is #360.
Context: docs/research/evaluation-work-plan-2026-09-14.md section D, agreed adapter design; it settles the executor-context question open since 2026-09-11, when the decision session found Claude Code executors had carried no repository standing context since 8e26700.
~~~

Supersedes derivation: an entry deciding the removal or the shape of CLAUDE.md
or AGENTS.md, if any.

5. Title: Routine releases run on standing authorization; consequential ones wait for explicit approval

~~~text
Decision: A routine release has the human's standing authorization once the required checks and reviews pass and needs no fresh approval prompt; a consequential release waits for the human's explicit go. Passing checks does not make a consequential change routine, and a merge that exposes nothing is not the release event. The row edits that state this consistently — R0490 and the consequential-class definition among them — land under #364 as an intake delta; the classification itself is unchanged by this entry.
Context: docs/research/evaluation-work-plan-2026-09-14.md section E item 3, agreed; the evaluation found R0490 and the consequential-class definition read as contradicting each other.
~~~

Supersedes derivation: an entry deciding that every release is the human's
call, if any.

6. Title: Bundles label a rule's ID only where another bundle member cites it

~~~text
Decision: A rendered bundle carries a rule's ID only when a retained reference elsewhere in the same bundle cites it; unreferenced rules render unlabelled as today. Authors decide which citations are necessary instruction and which are provenance only, and the bundler labels the targets of the former and refuses to render when a retained target is absent. The specification and tooling change lands under #358 as a spec delta on the rule-store PRD.
Context: docs/research/evaluation-work-plan-2026-09-14.md section B, agreed; the evaluation found process text citing rule IDs the renderer omits and 15 cited rules absent from the chief-of-staff bundle.
~~~

Supersedes derivation: an entry deciding that rendered rows carry no IDs, if
any.

7. Title: Ordinary bundle generation renders the local tree; only release generation checks its inputs against origin

~~~text
Decision: bin/bundle renders local files as they stand — uncommitted edits included, offline, on any branch — with input validation kept; the fetch and the HEAD-equals-origin/main refusal move to the release path, where cleanliness is checked over the files that generate the release assets and nothing else. The specification and tooling change lands under #366 as a spec delta on the bundle-system PRD.
Context: docs/research/evaluation-work-plan-2026-09-14.md section F2, agreed; the sync refusal blocked every pre-merge bundle check on a delta branch, recorded on the loose-end tracker on 2026-09-10.
~~~

Supersedes derivation: an entry deciding that bin/bundle refuses when HEAD
differs from origin/main, if any.

Commits: exactly one after the directive commit, carrying the seven entries,
message "decisions: seven entries — tracker home, the 2026-09-14 evaluation,
README, adapters, release authority, selective IDs, local rendering". Push
after it.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

- bin/tests/run 2>&1 | tee "$TMPDIR/tracker-migration.log" — expected OK, with the same skips the base shows.
- git diff --stat 1a41ea7..HEAD 2>&1 | tee -a "$TMPDIR/tracker-migration.log" — report the file list; the intent is decisions/log.md plus this directive and nothing else.
- For each of the seven fenced blocks: diff the landed entry's lines after its heading against the fenced block in this directive at its committed SHA, byte for byte, a Supersedes: line excepted where one was derived; report seven results, expected identical.
- grep -c '^## DEC-' decisions/log.md 2>&1 | tee -a "$TMPDIR/tracker-migration.log" — report the count observed on the base and after; the intent is a difference of seven, with the numbers running in tens from the base's last.

STOP CONDITIONS

Pinned to the reviewed ref 1a41ea75d37b10280d3601abb0e16c8f60e001a2. Cannot execute as written: stop
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

The rulings in TASK; nothing further. A Supersedes target the log resolves is
derived and reported, not stopped on.

## Deferred / out of scope

- Filing the open residue of OPEN-ITEMS.md as issues, and moving it and the
  other root state files to docs/history/ — #370 and #361, after this lands.
- The definition row for the loose-end tracker — its own intake delta.
- The pull request — the decision session's, after this lands.

## Execution notes

Remove the worktree after the report is composed and every push is verified
landed, without force and without retry, and state the outcome as the
report's final line. The log at "$TMPDIR/tracker-migration.log" is outside
the worktree.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    tracker migration: seven decision-log entries recording the 2026-09-14/16 rulings — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
