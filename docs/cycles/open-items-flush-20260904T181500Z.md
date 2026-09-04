# OPEN-ITEMS flush — document-metadata-policy cycle 21–22 closed

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/open-items-flush-20260904T181500Z.md, commit it alone with a
message naming the flush it carries, push with git push origin open-items-flush-20260904b (no -u), verify by git ls-remote origin open-items-flush-20260904b, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush-20260904b", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260904b" -b open-items-flush-20260904b origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch open-items-flush-20260904b, if a branch of that name already exists locally or on origin (git ls-remote origin open-items-flush-20260904b returns a ref), or if "$TMPDIR/fiducial-open-items-flush-20260904b" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
be2dabc35fa54295af93ac720898aab7c3c8a5b1. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ 56060d52a644c137d944e474d5a93e19e4d810ed — the three anchors named below, and the file's final line.

TASK

Tracker flush closing the document-metadata-policy full cycle (cycles 21-22, pull requests #316-#320). Edit OPEN-ITEMS.md only, in one content commit after the directive's own commit. Four edits, and four is the count; each is an anchor and an insertion, dictated verbatim. Every anchor is a whole line and must occur exactly once at the base ref; if any anchor occurs zero or two-plus times, stop and report before editing. The four-space margin is this directive's formatting only. After each edit, read the inserted span back byte-for-byte against the text below, not by heading; report each as matched or not.

Edit 1 — the bin/ package paragraph in "Queued next". Anchor, the line reading exactly:

    null, the Test Designer's reading of "requires no last-reviewed"). The

Replace that line's trailing " The" (space, The) so the sentence continues on the same line with this text verbatim, after which the original following line "converging follow-up cycle landed as Chief of Staff cycle 7 (ruling 4 above;" continues unchanged:

    (DONE 2026-09-04 — full cycle 21-22: Editor #316, Context Quality Reviewer gate #317 changes-required, fix #318, confirmation re-gate #319 ready with zero findings, flip #320, merge commit be2dabc35fa54295af93ac720898aab7c3c8a5b1; agreed at reviews/document-metadata-policy-cycle-22.md, reviewed document SHA d185baf33fdf41905e1789db388eaa2498410884. The absent-key reading is confirmed and stated in the policy: converging does not require last-reviewed, absent or null. Dave ruled 2026-09-04, at DMP21-5: converging reaches documents under specs/ only, conforming the policy to LEXICON.md and DEC-000360; no decision-log entry, the Lexicon already records the scope. Riders from that ruling, for each file's next cycle: roles/chief-of-staff.md:33, skills/spec-review-cycle.md:126 and :135, and skills/review-artifact.md:80 say "document" where the status is spec-only. The expedited-stretch one-line check (item 9 of the topic-walk rulings) cleared at cycle 21: conditions 1, 2 and 4 each foreclose the 2026-08-24 TRD agreement independently.) The

Edit 2 — the cycle-12 advisory section. Anchor, the line reading exactly:

    ## document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)

Replace it with:

    ## ~~document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)~~ — RESOLVED

and insert, immediately after the blank line that follows it, one new paragraph followed by a blank line:

    RESOLVED 2026-09-04 at cycle 21 (pull request #316): N1 as DMP21-2, N3 as DMP21-3 (the single-document rule is now doc-only condition 6), the #273 rider and CR5-3 together as DMP21-4; agreed at cycle 22.

Edit 3 — the topic-walk item 9. Anchor, the line reading exactly:

       one-line check at `policies/document-metadata-policy.md`'s next cycle.

(three leading spaces). Replace it with:

       one-line check at `policies/document-metadata-policy.md`'s next cycle
       (DONE 2026-09-04, cleared at cycle 21: no finding).

Edit 4 — append riders. The file's final line at the base reads exactly:

    - engagements/sre-critic.md H1 rider stands (recorded 2026-09-03).

and the file ends with a single newline after it. Append these three bullets directly after it, in the same list, verbatim:

    - Executor tracker writes: the 2026-09-04 flush (#314) silently truncated an appended paragraph mid-sentence and its report did not say so. Rule for every directive that appends dictated text: the executor reads each appended span back byte-for-byte against the dictated text, not by heading, and reports matched or not per span. Applied from docs/cycles/open-items-flush-20260904T181500Z.md onward.
    - Dictation defect class: a decision session dictating a sentence adjacent to retained text can restate it — cycle 21's DMP21-2 wording duplicated the companion-path sentence it sat beside and cost a finding (DMP21-6). Before dictating, read the sentence on either side of the insertion point at the reviewed ref.
    - docs/rule-register/rule-register-20260825T1435.md:413 quotes the pre-cycle-21 expedited-path sentence verbatim; a derived artifact pinned to f9a7a5e8 by its own header and out of the in-scope set. Stale, recorded, not touched; the selection build's re-extraction supersedes it.

Then: grep -c "DONE 2026-09-04 — full cycle 21-22" OPEN-ITEMS.md must print 1; grep -c "RESOLVED 2026-09-04 at cycle 21" OPEN-ITEMS.md must print 1; grep -c "cleared at cycle 21: no finding" OPEN-ITEMS.md must print 1; grep -c "Dictation defect class" OPEN-ITEMS.md must print 1; state all four, observed. git diff --stat of the content commit must list exactly OPEN-ITEMS.md; state its insertion and deletion counts, labelled observed (expected 9 insertions, 3 deletions; report yours). Run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-open-items-flush-20260904b-fm.log" and state its exit status (expected 0). Never bypass the pre-commit hook; OPEN-ITEMS.md is out of its scope and no frontmatter changes.

Push with git push origin open-items-flush-20260904b (no -u) and verify by git ls-remote origin open-items-flush-20260904b: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-flush-20260904b" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref be2dabc35fa54295af93ac720898aab7c3c8a5b1. Cannot execute as written: stop
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

    OPEN-ITEMS flush — document-metadata-policy cycle 21–22 closed — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
