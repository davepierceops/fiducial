# OPEN-ITEMS flush 2026-09-04 (templates cycle 3, fold ruling, corpus-pass program, riders)

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-flush-20260904T160000Z.md, commit it alone with a
message naming the flush it lands, push with git push origin open-items-flush-20260904 (no -u), verify by git ls-remote origin open-items-flush-20260904, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush-20260904", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260904" -b open-items-flush-20260904 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-flush-20260904, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-flush-20260904 returns a ref), or if "$TMPDIR/fiducial-open-items-flush-20260904" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
d1864d00ce52e2b0c8a9b11d657194351e5413b5. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ a5c66510af7d85186217a103b29e09f1da13a52e — the only file this directive edits.

TASK

This directive lands the record of the 2026-09-03/04 decision session; it decides nothing. Every ruling below is Dave's, carried from that session. Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. Four edits, each an exact anchor and dictated text. Locate each anchor once (each occurs exactly once at the base; if an anchor occurs zero or more than one time, stop and report). Do not edit anything else. Indentation below is the file's own; the four-space margin is this directive's formatting only. Where the target paragraph is hard-wrapped, rewrap the inserted text at the paragraph's line width and do not reflow lines outside the sentences you touch.

Edit 1 — "Queued next" paragraph, fold ruling. Immediately after the text "seven baseline paragraphs);" insert, separated by one space on each side:

    (Dave ruled 2026-09-03: fold — no cycle now; these two residues, plus the §5 paragraph that still describes engagements/critic.md and its shared value in the present tense after the #309 rename, ride into the PRD's next substantive opening, the selection build)

Edit 2 — "Queued next" paragraph, templates cycle DONE. Immediately after the text "AC-BS-5 (cycle-1 O-5);" insert, separated by one space on each side:

    (DONE 2026-09-04 — both templates, cycle 3, on Dave's 2026-08-28 ruling: Editor pull request #311, Spec Reviewer gate #312 with both verdicts ready and zero findings, flips #313, merge commit d1864d00ce52e2b0c8a9b11d657194351e5413b5; artifacts reviews/prd-template-cycle-3.md and reviews/trd-template-cycle-3.md; pointers reviews/prd-template-cycle-3.md @ 6d05d0156511527bb00e27e1e905e6cbbdebe695 and reviews/trd-template-cycle-3.md @ 473c1c81b004db9c981e48c516d9961fc8454e26)

Edit 3 — the section heading line reading exactly:

    ## PRD and TRD templates carry the wrong audience — directed fix

becomes:

    ## ~~PRD and TRD templates carry the wrong audience — directed fix~~ — RESOLVED

and, in the same section, after the paragraph ending "A directed change awaiting its review cycle, not a candidate." add a blank line and then:

    **RESOLVED** 2026-09-04 by templates audience cycle 3 (pull requests #311, #312, #313; merge d1864d00ce52e2b0c8a9b11d657194351e5413b5). Both skeleton blocks read `audience: [human]`; both templates agreed at cycle 3.

Edit 4 — append at the end of the file, after its final line, a blank line and then the following two sections verbatim:

    ## Context Quality Reviewer corpus pass — queued program

    Dave, 2026-09-04: yes, queue it. The tree at d1864d00ce52e2b0c8a9b11d657194351e5413b5 (observed by the decision session): of 62 in-scope documents, about 25 have been read whole by a reviewer with a per-document artifact; 26 read `agreed` on diff-only reconciliation passes (16 cite reviews/agreeing-clusters-cycle-2.md, whose own "Not inspected" line excludes the unedited bodies of all 26 documents; the rest cite converging-model, corpus-regate, or rule-divergence-rulings, each likewise scoped to a diff); 8 reached `agreed` through the expedited or doc-only path with no reviewer. No whole-corpus quality read has happened. The program: one full-depth Context Quality Reviewer gate per document (Spec Reviewer for specs/), in bundle order, the 16 agreeing-clusters documents first as the floor every session loads; a document returning ready with zero findings needs only its pointer updated; batch flips per the nine-flip precedent. Sequenced after the document-metadata-policy cycle and after the selection build, because each gate should receive the AC-BS-6 duplicate check's output for its document as an input rather than rediscover duplicates from memory. Parallelism: gates are read-only and each writes one new file, so they cannot conflict; the decision session proposed a fan-out through subagents in one Claude Code session, each in its own worktree and branch with its own directive file, merged additively into one integration branch. Unruled: whether an execution session may spawn sub-sessions at all — nothing governs it, Core 15 and the disposition rule assume one session per tree, and it multiplies the ungated-directive risk. Dave has not chosen between fan-out and independent executors; ask alone when the program opens.

    ## Semantic deduplication has run once, as a sample, and is stale

    Recorded 2026-09-04 (observed by the decision session). The only corpus-wide dedup is the 2026-08-25 pair docs/rule-register/rule-register-20260825T1435.md (878 rows, extraction only, at f9a7a5e8) and docs/rule-register/rule-clusters-20260825T1600.md (220 rows clustered into 77 clusters by one session in one sitting; 658 rows never compared to anything). The
