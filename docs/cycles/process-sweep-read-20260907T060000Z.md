# Process sweep, read: one frontier read of ten swept process documents against the rows they cite

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/process-sweep-read-20260907T060000Z.md, commit it alone with a
message naming the package it opens, push the branch process-sweep-read to origin with a plain
`git push origin process-sweep-read`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-process-sweep-read", created by:
git worktree add --no-track "$TMPDIR/fiducial-process-sweep-read" -b process-sweep-read origin/process-sweep

BASE VERIFICATION

Before anything else, fetch origin/process-sweep and origin/main and confirm the base — the
branch process-sweep, not main — is at the reviewed ref
fd6888ca2472e4d020f913fc4b0463e0a617efc4, and that the branch's merge base with origin/main is
7549f7efed0ed961536bf61620d621ebe6fbb81b. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- every file under process/ except voice.md, read from the base ref
  fd6888ca2472e4d020f913fc4b0463e0a617efc4 — the ten documents under review, 482 lines
- the same ten files at 7549f7efed0ed961536bf61620d621ebe6fbb81b, the
  sweep's base — what each was before; read `git diff
  7549f7efed0ed961536bf61620d621ebe6fbb81b..fd6888ca2472e4d020f913fc4b0463e0a617efc4 -- process/`
- docs/cycles/process-sweep-20260907T040000Z.md, read from the base ref
  fd6888ca2472e4d020f913fc4b0463e0a617efc4 — the ten criteria the sweep applied; you judge against
  them
- every row a document cites in brackets — `grep -ho '\[R[0-9, R]*\]'
  process/*.md` lists them; read each from rules/ at the base ref
- process/review-artifact.md at the base ref — the form your artifacts
  take (it is also one of the ten; read it first, then use it)
- decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11 — DEC-000380
  (the process gate this read is), DEC-000460, DEC-000490

TASK

You are the frontier read the process gate names (DEC-000380): one read, by
a session that did not draft the text, of each swept process document
against the rows it cites, before the human signs it off. Ten documents,
ten artifacts, ten verdicts. You edit nothing under process/ or rules/;
findings go in the artifacts.

For each document, in the sweep's order (change-flow, review-artifact,
retro, trd-template, prd-template, decomposition, outline, decision-log,
project-setup, spec-test-suite), answer these and only these:

1. CITATIONS. Every bracketed id resolves to a row whose body says what the
   citing sentence relies on. A citation to a row that says something else
   is a finding, blocking. A sentence that restates a cited row's body
   instead of citing it is a finding, non-blocking.
2. LOSS. Read the diff. Every obligation, condition, or sequence the old
   text stated is either in the new text, cited to a row that states it,
   or listed in the sweep report's six intake candidates. Anything else
   that was cut is a finding, blocking, with the cut sentence quoted.
3. RESIDUE. Every sentence in the new text passes the sweep's ten criteria:
   an act, an order, a condition, a form, or an explanation an agent needs
   to act. A sentence that is persuasion, self-record, or organization for
   a human reader is a finding, non-blocking, with the sentence quoted.
4. KEYS. The role list names exactly the roles that perform an act in the
   document. A role listed with no act, or an act whose role is missing,
   is a finding, non-blocking.
5. LOADABLE. The document reads correctly as a bundle member: no forward
   reference to a section that was cut, no heading whose only content
   moved, no table that lost a column it refers to.

One artifact per document at
reviews/<stem>-read-20260907T060000Z.md, in the review-artifact form,
verdict ready, ready-with-findings, or changes-required. A clean document
says so in the header and carries no findings. Do not pad.

Commits, in order, pushed after each: the directive (FIRST ACT), then one
per artifact in the order above. Do not open a pull request. Remove the
worktree at the end (`git worktree remove
"$TMPDIR/fiducial-process-sweep-read"`) and report that it is gone.
reviews/ is outside the frontmatter hook's in-scope set; if the hook fires,
stop and report.

Report also carries: the ten verdicts in one table; every blocking finding
in one line with its Fix; and the two-tranche cap — which the sweep left in
prose with no row — as its own line: where it now lives, and whether it
reads as an obligation there.

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
  ls reviews/*-read-20260907T060000Z.md | wc -l
  grep -h '^Verdict' reviews/*-read-20260907T060000Z.md
  git -C "$TMPDIR/fiducial-process-sweep-read" diff --stat origin/process-sweep..HEAD | tail -1
  git -C "$TMPDIR/fiducial-process-sweep-read" log --oneline origin/process-sweep..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/process-sweep-read-verify.log"
~~~

Expected: 10; the verdict lines; a diff-stat touching reviews/ and the
directive file only; 11 commits.

STOP CONDITIONS

Pinned to the reviewed ref fd6888ca2472e4d020f913fc4b0463e0a617efc4. Cannot execute as written: stop
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

    Process sweep, read: one frontier read of ten swept process documents against the rows they cite — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
