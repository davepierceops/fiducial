# Process delta: outline.md and voice.md stop naming the Public Prose Criteria as a document

ROUTE AND MODEL

Route: fresh session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/process-criteria-refs-20260910T160000Z.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

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
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-process-criteria-refs", created by: git worktree add --no-track "$TMPDIR/fiducial-process-criteria-refs" -b process-criteria-refs origin/main

Holder check, before the worktree is created: fetch origin main, run git worktree list, and stop and report if any worktree holds branch process-criteria-refs or the path already exists. Work on process-criteria-refs; push every commit with: git push origin process-criteria-refs — no upstream is set. The decision session lands it on main through a pull request after a frontier read. After the report is composed and every push is verified landed, remove the worktree from the main tree, without force and without retry, and state the outcome in the report's final line; this directive leaves nothing untracked in the worktree, so a non-force removal succeeds.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
c1bb43787bab745005254d74d90307b299d01004. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/outline.md @ 38aab413b615b65c2059356557d27bc585b0de3e
- process/voice.md @ 38aab413b615b65c2059356557d27bc585b0de3e

TASK

A process delta over two documents: the Public Prose Criteria no longer exist as a document in any bundle — since pull request #343 the criteria reach the writing roles as rows, and R1604 is the read-first row — so these two documents stop naming it. Four edits, dictated here; this directive is the wording's origin. Nothing else in either file changes, and no other file changes. One commit; push.

1. process/outline.md, the sentence "Read the Public Prose Criteria and the Voice document in this bundle first." — delete the sentence. Rejoin the paragraph so no double space or stray line break remains.

2. process/outline.md, in the Claims list item, the phrase "carrying its tier from the Criteria's claims taxonomy — relayed, demonstrated, grounded, opinion." becomes:

   carrying its tier — relayed, demonstrated, grounded, opinion.

3. process/voice.md, the two sentences "The author the Public Prose Criteria in this bundle are applied to. Read with the Criteria; where the two speak to the same thing, this document wins." become:

   The author the prose-criteria rows in this bundle are applied to. Where a criteria row and this document speak to the same thing, this document wins.

4. process/voice.md, the line "The methodology's own governed vocabulary, defined at first use per the Criteria." becomes:

   The methodology's own governed vocabulary, defined at first use.

Re-wrap only the lines the edit touches, to the file's existing wrap width. Commit message: "process: outline.md and voice.md stop naming the Public Prose Criteria as a document". The target text is quoted here unwrapped; in the files it wraps across line breaks, so match it with a line break standing for a space. If any of the four targets is still not found, stop and report which.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named for this package, captured with tee to $TMPDIR/process-criteria-refs-verify.log — outside the worktree, so it leaves nothing untracked there:
- git diff --stat origin/main..process-criteria-refs shows this directive and the two process documents and nothing else;
- grep -n -i "criteria" process/outline.md process/voice.md in the worktree returns only the "prose-criteria rows" and "criteria row" wording edit 3 introduces, and no "Public Prose Criteria" or "the Criteria" anywhere in either file.

STOP CONDITIONS

Pinned to the reviewed ref c1bb43787bab745005254d74d90307b299d01004. Cannot execute as written: stop
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

    Process delta: outline.md and voice.md stop naming the Public Prose Criteria as a document — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
    SOURCE MANIFEST — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
