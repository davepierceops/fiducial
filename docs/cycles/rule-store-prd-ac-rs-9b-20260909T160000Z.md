# Rule-store PRD: revise AC-RS-9 — human files stay, no count

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Write this directive verbatim to docs/cycles/rule-store-prd-ac-rs-9b-20260909T160000Z.md, commit it alone with a
message naming the package it opens, push the branch rule-store-prd-ac-rs-9b to origin with a plain push
(git push origin rule-store-prd-ac-rs-9b — never with -u), and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "wt/<n>", created by: git worktree add --no-track "wt/<n>" -b
<n> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-rule-store-prd-ac-rs-9b", created by:
git worktree add --no-track "$TMPDIR/fiducial-rule-store-prd-ac-rs-9b" -b rule-store-prd-ac-rs-9b origin/main

Before creating it: fetch origin, list worktrees, and stop and report if any
worktree holds the branch rule-store-prd-ac-rs-9b or the path already exists.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
68a5f02a3768b73bb555b5f535a94a06d6ace6bf. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/rule-store.md, process/decision-log.md and the last three entries of
  decisions/log.md, read from the base ref
  68a5f02a3768b73bb555b5f535a94a06d6ace6bf

TASK

You are the Coder. Land one agreed revision of the rule-store PRD and the
decision-log entry that records it. Two commits after the directive's, in this
order, each pushed with a plain push to origin rule-store-prd-ac-rs-9b. Touch
nothing else. Do not open a pull request.

1. In specs/rule-store.md, in AC-RS-9, replace exactly this text:

FENCE NOTE: the inner fence is `~~~` because this directive is itself fenced.

~~~text
`docs/history/corpus-<sha>/` holds the old corpus byte-identical to that SHA — the 62 in-scope files less `skills/directive-invariants.md`, a tool input that moves to `process/directive-invariants.md`
~~~

   with exactly this text, verbatim, the human's ruling of 2026-09-09:

~~~text
`docs/history/corpus-<sha>/` holds the old corpus byte-identical to that SHA — the agent-facing in-scope files at that SHA less `skills/directive-invariants.md`, a tool input that moves to `process/directive-invariants.md`; the `[human]` files OQ-3 names stay as files
~~~

   Change no other character of the file. Commit with the message
   `prd: rule-store — AC-RS-9 keeps the human files as files (agreed 2026-09-09)`
   using `--no-verify`, as 7097188 did: the retired frontmatter hook may still
   be installed in this clone and the PRD carries no lifecycle fields by ruling.
   Record the commit's full SHA; item 2 needs it.

2. Append one entry to decisions/log.md, at the end, in the form
   process/decision-log.md states, editing no existing entry. Its ID is the
   last entry's number plus ten. Its lines, with `<sha>` being item 1's full
   commit SHA and `<id>` the computed ID:

~~~markdown
## DEC-<id> — Rule-store PRD revised: AC-RS-9 moves the agent-facing corpus only
Date: 2026-09-09
Decision: specs/rule-store.md is agreed at <sha>. AC-RS-9 names no count: the old corpus moved to docs/history/ is the agent-facing in-scope files at the baseline SHA less skills/directive-invariants.md; the [human] files OQ-3 names stay as files.
Context: the 62 in-scope files at 4a118f5 include 8 [human] documents — specs, vendor notes, the voice template, README.md — that OQ-3 keeps as files and G10 reads from the root at release; moving them with the corpus contradicted both. DEC-000680 stands as history; this entry names the current agreed SHA.
~~~

   Commit with the message `decisions: rule-store PRD agreed at <sha>`, using
   `--no-verify` for the same reason.

Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-rule-store-prd-ac-rs-9b"`) and report
that it is gone.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the last commit and before removing the worktree:

~~~sh
{
  grep -c 'the `\[human\]` files OQ-3 names stay as files' specs/rule-store.md
  grep -c 'the 62 in-scope files less' specs/rule-store.md
  git diff --stat origin/main..HEAD | tail -1
  git diff --numstat origin/main..HEAD -- specs/rule-store.md
  tail -6 decisions/log.md
  git log --oneline origin/main..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/rule-store-prd-ac-rs-9b-verify.log"
~~~

Expected: 1; 0; a diff-stat naming specs/rule-store.md, decisions/log.md and
the directive file only; a numstat line of `1    1    specs/rule-store.md`; the new
entry as the log's tail, its Decision line naming item 1's commit SHA; 3
commits.

STOP CONDITIONS

Pinned to the reviewed ref 68a5f02a3768b73bb555b5f535a94a06d6ace6bf. Cannot execute as written: stop
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

    Rule-store PRD: revise AC-RS-9 — human files stay, no count — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    ROUTE AND MODEL — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    FIRST ACT — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    DISPOSITION PROMPT — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    COMPANIONS — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    VERIFICATION — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    STOP CONDITIONS — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    REPORT — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    CLAIM LABELS — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
    SOURCE MANIFEST — skills/directive-invariants.md @ abd4293a4c7ed40e59ad63d53a7afa7df5c1e71a
