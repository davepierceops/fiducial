# OPEN-ITEMS riders 2026-09-04 (flush follow-up)

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-riders-20260904T170000Z.md, commit it alone with a
message naming the riders it lands, push with git push origin open-items-riders-20260904 (no -u), verify by git ls-remote origin open-items-riders-20260904, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-riders-20260904", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-riders-20260904" -b open-items-riders-20260904 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-riders-20260904, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-riders-20260904 returns a ref), or if "$TMPDIR/fiducial-open-items-riders-20260904" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
9230698af46091430b3e91b89eb6ce22306ff17f. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ eaf397b5c058297f42cef8a39b8f2b3fd3c75994 — the only file this directive edits.

TASK

Follow-up to docs/cycles/open-items-flush-20260904T160000Z.md. Its Edit 4 landed incompletely (observed by the decision session at the base ref): the section "Semantic deduplication has run once, as a sample, and is stale" is truncated mid-sentence, and the third section, "Riders recorded 2026-09-04", is absent. This directive completes both; it decides nothing. Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. Two edits. The four-space margin is this directive's formatting only.

Edit 1 — complete the truncated paragraph. The file's final line at the base is the paragraph beginning "Recorded 2026-09-04 (observed by the decision session)." and it ends with exactly the text:

    658 rows never compared to anything). The

If the final line does not end with exactly that text, stop and report. Replace that trailing fragment " The" (space, The) so that the paragraph continues, on the same line, with this text verbatim:

    The collapse cycles edited the clustered rows and gated the diffs; nothing since has re-measured. Per-cycle dedup is rubric criterion 12 over a diff's sentences, which only fires where a cycle fires. AC-BS-6 of the agreed bundle-system PRD promises a check over a bundle's members that reports a restatement as a defect; it is specified and unbuilt. Dave's statement of what is actually needed: every governed line normalized to what it says, and every file checked for any other line that says the same thing. Rider for the selection build: build AC-BS-6 as a computed check — re-extract against the current tree, shortlist candidate pairs mechanically (embedding similarity over the normalized rules), adjudicate each candidate pair by LLM as same, same-with-divergence, or different, and emit a derived cluster artifact with a per-file view; the corpus pass above consumes it. The "twelve words" in the August extraction directive was a table-column width for the register's rule column, not a rule about the corpus, and is not carried forward. Open, Dave's, unruled: whether this is the point to move from files to a rule database as the unit of authoring and selection — the PRD's §5 already names the tension ("a file is a bag of rules"; whole-file tags over-select).

After the edit the final line ends with the text: whole-file tags over-select). — and the file ends with a single newline.

Edit 2 — append at the end of the file, after that completed line, a blank line and then exactly one section, verbatim:

    ## Riders recorded 2026-09-04

    - bin/flip-agreed: on a non-zero exit from git commit it restores the working tree and index without first reading HEAD. Observed 2026-09-04 in Dave's clone on specs/prd-template.md: the commit had landed (0f9581de94640edae16567e522327a00e061f155) while the tool reported commit-failed with empty stderr and restored the tree to in-review/null, leaving HEAD flipped and the tree unflipped; the executor then hand-edited and committed a revert, caught it, stopped, and the decision session had the bad commit dropped by reset before any push (it never reached origin). Root cause of the false non-zero unknown; the decision session's sandbox, without hooks, exits 0 on the same command. Rule: read HEAD before restoring on an apparent commit failure (Core 12); report "commit landed, tree restored" as its own diagnostic.
    - Stale worktree in Dave's clone: $TMPDIR/fiducial-templates-audience-cycle-3-flip on branch templates-audience-cycle-3-flip, tip d3431749d44ca67ea3fc50ac90398cedb7b0f98e, fully merged (#313). git worktree remove failed with "Operation not permitted" deleting .git/worktrees/<name> on a second attempt in the same session; cause unknown. Marked prunable. Not to be deleted unasked.
    - Sandbox lore: a compound command after a cd that trips the ~/.ssh deny rule is rejected whole and silently — no output, nothing executed — and is indistinguishable from a command that ran and printed nothing; confirm each commit with git log before proceeding. A zsh :r modifier inside $VAR:reviews/... mangles the path; brace the variable.
    - bin/check-directive M2 flip-pointer false positive fired again on the templates cycle-3 flip directive, 2026-09-04; classified, not worked around, per precedent.
    - Directive authoring: a directive that enumerates items must state the count it lists or none — the 2026-09-04 flush said "two sections" over three and the third was dropped (observed, pull request #314). Candidate for bin/check-directive or the authoring skill.
    - engagements/sre-critic.md H1 rider stands (recorded 2026-09-03).

Then: grep -c "whole-file tags over-select)." OPEN-ITEMS.md must print 1 and grep -c "Riders recorded 2026-09-04" OPEN-ITEMS.md must print 1; state both, observed. git diff --stat of the content commit must list exactly OPEN-ITEMS.md; state its insertion and deletion counts, labelled observed (expected 10 insertions, 1 deletion; report yours). Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-open-items-riders-20260904-fm.log" and state its exit status (expected 0). Never bypass the pre-commit hook.

Push with git push origin open-items-riders-20260904 (no -u) and verify by git ls-remote origin open-items-riders-20260904: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-riders-20260904" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref 9230698af46091430b3e91b89eb6ce22306ff17f. Cannot execute as written: stop
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

    OPEN-ITEMS riders 2026-09-04 (flush follow-up) — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
