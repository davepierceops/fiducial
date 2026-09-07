# Process sweep, fix: five blocking findings restored verbatim, the two-tranche cap removed

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Write this directive verbatim to docs/cycles/process-sweep-fix-20260907T080000Z.md, commit it alone with a
message naming the package it opens, push the branch process-sweep-fix to origin with a plain
`git push origin process-sweep-fix`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-process-sweep-fix", created by:
git worktree add --no-track "$TMPDIR/fiducial-process-sweep-fix" -b process-sweep-fix origin/process-sweep-read

BASE VERIFICATION

Before anything else, fetch origin/process-sweep-read and origin/main and confirm the base — the
branch process-sweep-read, not main — is at the reviewed ref
e4a6e9965a926ed1a9f824656946ee55e330d14b, and that the branch's merge base with origin/main is
7549f7efed0ed961536bf61620d621ebe6fbb81b. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/change-flow-read-20260907T060000Z.md,
  reviews/review-artifact-read-20260907T060000Z.md,
  reviews/outline-read-20260907T060000Z.md, read from the base ref
  e4a6e9965a926ed1a9f824656946ee55e330d14b — the findings, each with Location and Fix
- process/change-flow.md, process/review-artifact.md, process/outline.md,
  process/decomposition.md, read from the base ref e4a6e9965a926ed1a9f824656946ee55e330d14b — the four files you edit
- the same four files at 7549f7efed0ed961536bf61620d621ebe6fbb81b — the
  pre-sweep text the restored sentences come from; read `git show
  7549f7efed0ed961536bf61620d621ebe6fbb81b:process/<file>`

TASK

Apply five blocking findings from the frontier read, each by restoring the
sentence the finding names from the pre-sweep text, or splitting a sentence
as the finding says, and remove the two-tranche cap. One commit per item.
Change nothing else: no rewording, no new sentences, no citation added or
removed except where an item says. Two of the read's blocking findings are
discharged by the human's ruling of 2026-09-07 and are not applied: RE-01
(retro — the rule is dropped) and CF-03 (change-flow — the dimensions
sentence stays cut). Do not touch process/retro.md.

1. CF-01 — process/change-flow.md, the sentence carrying [R0008]. Restore
   the clause "a delta is bounded by its tranche and never spans two" so
   that [R0008] sits on it; the early-close licence ("Close a delta early
   at will; the tranche boundary is a deadline, not a target") stays,
   uncited.
2. CF-02 — process/change-flow.md, "At most two tranches run at once
   [R0012, R0013]". Delete the cap sentence. In its place restore the
   disjointness clause from the pre-sweep text under [R0012, R0013].
3. CAP — process/decomposition.md, line 22, "at most two run at once,
   never two deltas over one tranche". Delete "at most two run at once";
   "never two deltas over one tranche" and its citation stay. (The human
   ruled 2026-09-07 that the cap is dropped; DEC-000170 is superseded in
   a later package.)
4. RA-01 — process/review-artifact.md. Restore the role-output-to-field
   mapping table from the pre-sweep text in full, including the sentence
   "The entry field is `Fix`, not `Recommendation`."
5. OU-01 — process/outline.md, the sentence carrying [R1164]. Split it:
   the trigger sentence (the outline is produced on the author's ask, in
   the shape R1164 states) carries [R1164]; the reading-order sentence
   ("Read the Public Prose Criteria and the Voice document first") stands
   alone, uncited.
6. OU-02 — process/outline.md, the claims list. Restore onto its
   governing sentence: "A claim the prose makes that is absent here is a
   finding; a claim here the prose drops is a finding."

Commits `process: fix <finding-id> — <one clause>`, pushed after each. Do
not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-process-sweep-fix"`) and report
that it is gone. process/ is outside the frontmatter hook's in-scope set;
if the hook fires, stop and report.

Report: the six diffs, each quoted in full; the four files' line counts
after.

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
  wc -l process/change-flow.md process/review-artifact.md process/outline.md process/decomposition.md
  grep -c 'never spans two' process/change-flow.md
  grep -c 'two tranches\|two run at once' process/change-flow.md process/decomposition.md
  grep -c 'not `Recommendation`' process/review-artifact.md
  grep -c 'is a finding' process/outline.md
  git -C "$TMPDIR/fiducial-process-sweep-fix" diff --stat origin/process-sweep-read..HEAD | tail -1
  git -C "$TMPDIR/fiducial-process-sweep-fix" log --oneline origin/process-sweep-read..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/process-sweep-fix-verify.log"
~~~

Expected: four line counts (change-flow, review-artifact and outline a few
lines above the sweep's 79, 66, 39; decomposition at 39); 1; 0 and 0; 1;
1 or more; a diff-stat touching the four process files and the directive
only; 7 commits.

STOP CONDITIONS

Pinned to the reviewed ref e4a6e9965a926ed1a9f824656946ee55e330d14b. Cannot execute as written: stop
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

    Process sweep, fix: five blocking findings restored verbatim, the two-tranche cap removed — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
