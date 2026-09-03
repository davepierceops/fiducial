# OPEN-ITEMS flush 2026-09-03

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-flush-20260903T193000Z.md, commit it alone with a
message naming the flush it lands, push with git push origin open-items-flush-20260903 (no -u), verify by git ls-remote origin open-items-flush-20260903, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush-20260903", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260903" -b open-items-flush-20260903 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-flush-20260903, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-flush-20260903 returns a ref), or if "$TMPDIR/fiducial-open-items-flush-20260903" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
9c7ccee3cf25781c4c7ab46c05f4f41f2aca7de2. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ 320f6ca2d13be8ab8c8832f02a347242db5eb230 — the only file this directive edits.
- reviews/command-blocks-cycle-7.md @ e890d6cb225f5cb9f79155943fdfe376bbebb26c — source of riders CB7-1, CB7-2 and the Decision Layer observation.
- reviews/conversation-retro-cycle-5.md @ 890c7b4d704ea33ad86c11612865f00fddc9f502 — source of observation CR5-3.

TASK

This directive lands the record of two closed cycles and four riders; it decides nothing. Every ruling below is Dave's, carried from the 2026-09-03 decision session and the two artifacts named under COMPANIONS. Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. Five edits, each an exact anchor and exact replacement or insertion; the wording is dictated. Apply them by locating each anchor once in the file (it occurs exactly once at the base; if an anchor occurs zero or more than one time, stop and report). Do not edit anything else in the file. Indentation below is the file's own; the four-space margin is this directive's formatting only.

Edit 1 — follow-up 7 of "Retrospective session 2026-08-31 — follow-ups". The line beginning:

    7. **`skills/command-blocks.md` (T19).**

ends today with "a block never pushes the default branch." Append to that same line, after that period and one space:

    LANDED 2026-09-03 — cycle 7 (CB-1, CB-2, CB-3; criteria nine → eleven), pull requests #302–#304; agreed at reviews/command-blocks-cycle-7.md, reviewed document SHA 1c86595f0bcd89c6ddb6ae38ed637f1e5b180d8c, verdict ready. Riders to the skill's next cycle, recorded in the artifact: CB7-1, the never-push rule says "the decision session merges" — narrower than the commit and change control policy, which grants routine open-and-merge to agents without naming a session kind; Dave to inspect, not yet ruled. CB7-2, the one-block-per-turn rule has no conformance criterion, and criteria 1 and 3 have no body rule — predates cycle 7.

Edit 2 — ruling 1 of "Topic walk 2026-08-31 — rulings" (the Decision Layer cycle). The two lines:

       Layer cycle: cycle 14's DL-2, the pane named inconsistently across
       documents. Follow-ups 3, 4, 5, and 11 closed.

become:

       Layer cycle: cycle 14's DL-2, the pane named inconsistently across
       documents; and the command-blocks pointer — the rule binding decision
       sessions to skills/command-blocks.md was deleted at 3e89a21, and nothing
       in the Decision Layer now points a decision session at that skill
       (observed by the Reviewer, reviews/command-blocks-cycle-7.md cross-check
       text). Follow-ups 3, 4, 5, and 11 closed.

Edit 3 — the "Queued next" paragraph. The phrase:

    command-blocks cycle (follow-up 7, three changes), the Chief of Staff role

becomes:

    command-blocks cycle (DONE 2026-09-03 — cycle 7, follow-up 7 above), the Chief of Staff role

Edit 4 — the same paragraph. Immediately after the sentence ending "sense; conform." (the pull request #273 routes rider) and before "Tagging package", insert, separated by one space on each side:

    (DONE 2026-09-03 — cycle 5, CR5-1 and CR5-2, both landed; pull requests #305–#307; agreed at reviews/conversation-retro-cycle-5.md, reviewed document SHA 649809aa28b24f40af38441b93f945dde103cd7e, verdict ready, zero findings. Observation CR5-3 for the metadata policy's cycle, recorded on that entry.)

Preserve the paragraph's existing hard-wrap style: rewrap the inserted text at the paragraph's line width; do not reflow lines outside the sentences you touch.

Edit 5 — the entry "document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)". After its last bullet, which begins "- Rider from pull request #273: the doc-only path sentence" and ends "at the policy's next cycle.", add one bullet:

    - CR5-3 (reviews/conversation-retro-cycle-5.md, observation): the sentence
      "a document may exclude its own revisions from this path, and the retro
      skill does" is false at skills/conversation-retro.md @ 649809aa — the skill
      excludes retro-surfaced methodology revisions from lighter paths, not its
      own revisions; what binds the skill's revisions to the full cycle is this
      policy's condition 3 list. Correct the sentence at the policy's next cycle.

Then: git diff --stat of the content commit must list exactly OPEN-ITEMS.md; state its insertion and deletion counts, labelled observed (the decision session's dry run of the same edits produced 18 insertions and 4 deletions in its own tree; a wrap difference may move those numbers — report yours, do not make them match). Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-open-items-flush-20260903-fm.log" and state its exit status (expected 0; OPEN-ITEMS.md is out of scope for it, so this checks only that the tree is still clean). Never bypass the pre-commit hook.

Push with git push origin open-items-flush-20260903 (no -u) and verify by git ls-remote origin open-items-flush-20260903: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-flush-20260903" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref 9c7ccee3cf25781c4c7ab46c05f4f41f2aca7de2. Cannot execute as written: stop
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

    OPEN-ITEMS flush 2026-09-03 — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
