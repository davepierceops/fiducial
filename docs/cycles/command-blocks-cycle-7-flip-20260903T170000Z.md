# Command blocks cycle 7 — agreement flip

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/command-blocks-cycle-7-flip-20260903T170000Z.md, commit it alone with a
message naming the flip it lands, push with git push origin command-blocks-cycle-7-flip (no -u), verify by git ls-remote origin command-blocks-cycle-7-flip, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-command-blocks-cycle-7-flip", created by: git worktree add --no-track "$TMPDIR/fiducial-command-blocks-cycle-7-flip" -b command-blocks-cycle-7-flip origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch command-blocks-cycle-7-flip, if a branch of that name already exists locally or on origin (git ls-remote origin command-blocks-cycle-7-flip returns a ref), or if "$TMPDIR/fiducial-command-blocks-cycle-7-flip" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a179cc3e6fb7e9721c26f5cc1b266ab3ad0181e6. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/command-blocks.md @ 1c86595f0bcd89c6ddb6ae38ed637f1e5b180d8c — the document being flipped; at the base it reads status: in-review, last-reviewed: null (told).
- reviews/command-blocks-cycle-7.md @ e890d6cb225f5cb9f79155943fdfe376bbebb26c — the gate artifact, verdict ready, findings none, reviewing the document at the SHA above.
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5 — the agreement flip's status-transition rule.

TASK

One agreement flip. The gate verdict is ready with no findings, which meets the cycle's stated agreement bar; Dave's agreement is the decision session's to record (the flush), not yours. The flip is one frontmatter-only commit made by the tool.

Precondition: in the worktree, the document's frontmatter reads exactly status: in-review and last-reviewed: null. If it does not, stop and report before running anything.

From the worktree:

    bin/flip-agreed skills/command-blocks.md --review "reviews/command-blocks-cycle-7.md @ 1c86595f0bcd89c6ddb6ae38ed637f1e5b180d8c"

The tool makes the commit itself and self-verifies. If it exits non-zero, stop and report its output — do not edit frontmatter by hand and do not retry. After it exits 0: git show --stat HEAD must list exactly skills/command-blocks.md with 2 insertions and 2 deletions, and git show HEAD must change only the status line (in-review → agreed) and the last-reviewed line (null → the pointer given). State both, labelled observed.

Then run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-command-blocks-cycle-7-flip-fm.log" and state its exit status (expected 0).

Push with git push origin command-blocks-cycle-7-flip (no -u) and verify by git ls-remote origin command-blocks-cycle-7-flip: the tip must be the flip commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-command-blocks-cycle-7-flip" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

STOP CONDITIONS

Pinned to the reviewed ref a179cc3e6fb7e9721c26f5cc1b266ab3ad0181e6. Cannot execute as written: stop
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

    Command blocks cycle 7 — agreement flip — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
