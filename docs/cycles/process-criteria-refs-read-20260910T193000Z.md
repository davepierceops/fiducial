# Frontier read: process-criteria-refs delta

ROUTE AND MODEL

Route: fresh session
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/process-criteria-refs-read-20260910T193000Z.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-process-criteria-refs-read", created by: git worktree add --no-track "$TMPDIR/fiducial-process-criteria-refs-read" -b process-criteria-refs-read origin/process-criteria-refs

Holder check, before the worktree is created: fetch origin process-criteria-refs, run git worktree list, and stop and report if any worktree holds branch process-criteria-refs-read or the path already exists. Push every commit with: git push origin process-criteria-refs-read — no upstream is set. After the report is composed and every push is verified landed, remove the worktree without force and without retry, and state the outcome in the report's final line; the log this directive names lives outside the worktree, so nothing is left untracked in it.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
b3a8f008884bc47ca9447f784afe29be16ec367f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- process/review-artifact.md @ 38aab413b615b65c2059356557d27bc585b0de3e — the artifact schema
- docs/cycles/process-criteria-refs-20260910T160000Z.md @ 71c438af26f21b0601b20f6107a99d62194edf27 — the directive that made the delta; its TASK states the four intended edits
- rules/R1604.md @ 88d4b5b8eaed45b58edb95e21436f9aed99d7474, rules/R0821.md @ c7df7ea768478006cb9ef4eee706c2dac8c90cbb, rules/R1594.md @ 5171731294b05d11cd244412a8a28a485b2ba845 — the rows the retired wording relied on

TASK

You did not produce this delta. This is the one frontier read a process delta gets before the human signs it off. The delta is the diff c1bb43787bab745005254d74d90307b299d01004..b3a8f008884bc47ca9447f784afe29be16ec367f over process/outline.md and process/voice.md, made because the Public Prose Criteria no longer exist as a document in any bundle — the criteria reach the writing roles as rows, and R1604 is the read-first row.

Read the diff whole against the rows it now leans on, three passes, each with its own Verdict line:

- Continuity: does anything the delta did not change still name the Public Prose Criteria, "the Criteria", or its claims taxonomy as a document — across process/, rules/, README.md and docs/ (skipping docs/cycles and docs/history, which are records), and in the rendered writer, copy-editor and critic bundles under the release manifest at the reviewed ref? Does each retired phrase's meaning survive through a row that renders in the same bundles as the two documents — R1604 for the read-first instruction, R0821 for the four claim tiers, R1594 for definition at first use — checking those rows' role and corpus keys against the two documents' frontmatter?
- Quality: does the landed text match the four edits the directive's TASK dictates, no more and no less; is the re-wrap clean; does the precedence sentence in voice.md still say what it said before — this document wins over a criteria row where both speak?
- Skepticism: is anything in the two documents now unmoored — a term, a tier name, an obligation — that a Writer, Copy Editor or Critic reading only its bundle could no longer resolve?

Every finding: location, evidence, label defect / suggestion / accepted risk, and a release-impact label; a bracketed row ID in a process document is unlocatable to a bundle reader and is a known defect across process/ not in scope here — do not raise it as a finding on this delta. Write exactly one review artifact in the schema to reviews/process-criteria-refs-read-20260910T193000Z.md — confirm the path is absent first — with Baseline c1bb437 and Reviewed b3a8f00. Commit it alone; push. Edit nothing else; open no pull request.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Captured with tee to "$TMPDIR/process-criteria-refs-read.log", outside the worktree:
- git diff --stat c1bb437..b3a8f00 — report the file list;
- grep -rn -i "public prose criteria\|the Criteria" process/ rules/ README.md docs/ --exclude-dir=cycles --exclude-dir=history — report the hit count and every hit;
- grep -c "^Verdict" on the artifact — expected 4, one overall and one per pass.

STOP CONDITIONS

Pinned to the reviewed ref b3a8f008884bc47ca9447f784afe29be16ec367f. Cannot execute as written: stop
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

    Frontier read: process-criteria-refs delta — process/directive-invariants.md @ 77625d370db5963b85695fba51a86faea7c1f4f2
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
