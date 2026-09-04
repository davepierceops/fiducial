# OPEN-ITEMS flush — CS7-1 ruled

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-flush-20260904T233000Z.md, commit it alone with a
message naming the flush it carries, push with git push origin open-items-flush-20260904c (no -u), verify by git ls-remote origin open-items-flush-20260904c, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush-20260904c", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260904c" -b open-items-flush-20260904c origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-flush-20260904c, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-flush-20260904c returns a ref), or if "$TMPDIR/fiducial-open-items-flush-20260904c" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
8ec74bc629260056f62ada78f77c3ccb9b1fe1ea. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ e9b79cd12a0b3c0b530ef36b2869da6e95aac6b3 — the one anchor named below and the two lines on either side of it.

TASK

Tracker flush recording Dave's CS7-1 ruling of 2026-09-04. Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. One edit, and one is the count: an anchor and an insertion, dictated verbatim. The anchor is a whole line and must occur exactly once at the base ref; if it occurs zero or two-plus times, stop and report before editing. The four-space margin is this directive's formatting only. After the edit, read the inserted span back byte-for-byte against the text below, not by heading; report it as matched or not.

Edit 1 — the CS7-1 sentence in the Chief of Staff cycle-7 entry. Anchor, the line reading exactly (three leading spaces):

       in one document yields, which one is the ruling. Rider to the role's next

Replace that line with these two lines verbatim (three leading spaces each), so the sentence beginning "Rider to the role's next" continues onto the original following line "cycle: CS7-2, ..." unchanged:

       in one document yields, which one is the ruling. RULED 2026-09-04, the
       role yields: a first connector timeout is noise — read state and re-create once, per the remote-write policy's rules 6 and 7; the contention check is on the second failure, per rule 2. Rule 2 stands unchanged; no decision-log entry. One-sentence rider for roles/chief-of-staff.md @ 0154e2ab4a6db29fc84da47100b62ceca5c85a57, lines 51-54, at the role's next cycle, alongside CS7-2. Rider to the role's next

Then: grep -c "RULED 2026-09-04, the" OPEN-ITEMS.md must print 1; grep -c "which one is the ruling. Rider" OPEN-ITEMS.md must print 0; state both, observed. git diff --stat of the content commit must list exactly OPEN-ITEMS.md; state its insertion and deletion counts, labelled observed (expected 2 insertions, 1 deletion; report yours). Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-open-items-flush-20260904c-fm.log" and state its exit status (expected 0). Never bypass the pre-commit hook; OPEN-ITEMS.md is out of its scope and no frontmatter changes.

Push with git push origin open-items-flush-20260904c (no -u) and verify by git ls-remote origin open-items-flush-20260904c: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-flush-20260904c" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref 8ec74bc629260056f62ada78f77c3ccb9b1fe1ea. Cannot execute as written: stop
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

    OPEN-ITEMS flush — CS7-1 ruled — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
