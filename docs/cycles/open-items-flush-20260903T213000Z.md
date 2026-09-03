# OPEN-ITEMS flush 2026-09-03 (tagging package)

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-flush-20260903T213000Z.md, commit it alone with a
message naming the flush it lands, push with git push origin open-items-flush-20260903b (no -u), verify by git ls-remote origin open-items-flush-20260903b, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush-20260903b", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260903b" -b open-items-flush-20260903b origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-flush-20260903b, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-flush-20260903b returns a ref), or if "$TMPDIR/fiducial-open-items-flush-20260903b" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
42e34ba5054513cf2b9f14e2b5e666f8de73eecb. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ 9728e9b710cb351381739464d90486a0d3c1432c — the only file this directive edits.
- docs/cycles/tagging-package-20260903T203000Z.md @ ddf3b37ae5c785c9035b92b0e461a742b4c6ac1b — the tagging package this flush records; its instruction 1 names the H1 rider.

TASK

This directive lands the record of the tagging package (pull request #309) and one rider; it decides nothing. Every ruling below is Dave's, carried from the 2026-09-03 decision session and the artifact named under COMPANIONS. Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. Two edits, each an exact anchor and exact insertion; the wording is dictated. Locate each anchor once in the file (it occurs exactly once at the base; if an anchor occurs zero or more than one time, stop and report). Do not edit anything else in the file. Indentation below is the file's own; the four-space margin is this directive's formatting only.

Edit 1 — the "Queued next" paragraph. Immediately after the sentence ending "copy-editor and critic role files (cycle-1 O-4)." and before "After the rename lands,", insert, separated by one space on each side:

    (DONE 2026-09-03 — pull request #309, merge commit 42e34ba5054513cf2b9f14e2b5e666f8de73eecb; all three rulings landed, frontmatter-only, no document flipped, bin/tests/run OK. Bundles after the retag: critic 21 files, sre-critic 23 — expected until the selection build lands. skills/review-artifact.md's audience value critic was retagged sre-critic as an inferred extension of DEC-000350 — the file cites the review-artifact schema, which the SRE critic uses, and AC-BS-4 excludes skills from the writing Critic's set; Dave told, no objection, not separately ruled. Rider for engagements/sre-critic.md's next cycle: its H1 still reads "# Role: Critic" — the package left the body untouched by instruction.)

Preserve the paragraph's existing hard-wrap style: rewrap the inserted text at the paragraph's line width; do not reflow lines outside the sentences you touch.

Edit 2 — the bullet beginning:

    - **`review-artifact.md` lists `critic` in its audience**;

ends today with "not a review artifact." Append to that same line, after that period and one space:

    Closed by tagging 2026-09-03 (pull request #309): the value now reads `sre-critic`, so the skill no longer reaches the writing Critic; see the Queued-next tagging entry for the basis.

Then: git diff --stat of the content commit must list exactly OPEN-ITEMS.md; state its insertion and deletion counts, labelled observed (the decision session's dry run of the same edits produced 11 insertions and 2 deletions in its own tree; a wrap difference may move those numbers — report yours, do not make them match). Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-open-items-flush-20260903b-fm.log" and state its exit status (expected 0; OPEN-ITEMS.md is out of scope for it, so this checks only that the tree is still clean). Never bypass the pre-commit hook.

Push with git push origin open-items-flush-20260903b (no -u) and verify by git ls-remote origin open-items-flush-20260903b: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-flush-20260903b" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref 42e34ba5054513cf2b9f14e2b5e666f8de73eecb. Cannot execute as written: stop
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

    OPEN-ITEMS flush 2026-09-03 (tagging package) — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
