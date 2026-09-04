# PRD and TRD templates audience cycle 3 — agreement flips

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/templates-audience-cycle-3-flip-20260904T150000Z.md, commit it alone with a
message naming the flips it lands, push with git push origin templates-audience-cycle-3-flip (no -u), verify by git ls-remote origin templates-audience-cycle-3-flip, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-templates-audience-cycle-3-flip", created by: git worktree add --no-track "$TMPDIR/fiducial-templates-audience-cycle-3-flip" -b templates-audience-cycle-3-flip origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch templates-audience-cycle-3-flip, if a branch of that name already exists locally or on origin (git ls-remote origin templates-audience-cycle-3-flip returns a ref), or if "$TMPDIR/fiducial-templates-audience-cycle-3-flip" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
e2dbce5430578e8f58c0a5f2440c298b91630d3f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/prd-template-cycle-3.md @ 02c613bba29ef26a77c36f944b2f814793340f83 — verdict ready, findings none.
- reviews/trd-template-cycle-3.md @ 02c613bba29ef26a77c36f944b2f814793340f83 — verdict ready, findings none.
- docs/cycles/templates-audience-cycle-3-gate-directive.md @ 419cf83ff32f45fbb0faaa85c6d7fa470cf4959a — LOOP START, the agreement bar.

TASK

Two agreement flips, one per document, each its own frontmatter-only commit made by the tool. Both gate verdicts are ready with no findings, which meets the cycle's stated agreement bar (docs/cycles/templates-audience-cycle-3-gate-directive.md, LOOP START); Dave's agreement is the decision session's to record (the flush), not yours.

Precondition: in the worktree, each template's top-level frontmatter reads exactly status: in-review and last-reviewed: null. If either does not, stop and report before running anything.

From the worktree, first:

    bin/flip-agreed specs/prd-template.md --review "reviews/prd-template-cycle-3.md @ 6d05d0156511527bb00e27e1e905e6cbbdebe695"

then, only after it exits 0:

    bin/flip-agreed specs/trd-template.md --review "reviews/trd-template-cycle-3.md @ 473c1c81b004db9c981e48c516d9961fc8454e26"

The tool makes each commit itself and self-verifies. If either exits non-zero, stop and report its output — do not edit frontmatter by hand, do not retry, and do not run the second if the first failed. After each exits 0: git show --stat HEAD must list exactly that template with 2 insertions and 2 deletions, and git show HEAD must change only the status line (in-review → agreed) and the last-reviewed line (null → the pointer given). State both for each flip, labelled observed. Both pointers were probed by the decision session with bin/flip-agreed --no-commit at the base ref and staged exactly that diff (observed). The pointer SHA is each document's own content commit, not the artifacts commit; that is by design.

Then run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-templates-audience-cycle-3-flip-fm.log" and state its exit status (expected 0).

Push with git push origin templates-audience-cycle-3-flip (no -u) and verify by git ls-remote origin templates-audience-cycle-3-flip: the tip must be the second flip commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-templates-audience-cycle-3-flip" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref e2dbce5430578e8f58c0a5f2440c298b91630d3f. Cannot execute as written: stop
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

    PRD and TRD templates audience cycle 3 — agreement flips — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
