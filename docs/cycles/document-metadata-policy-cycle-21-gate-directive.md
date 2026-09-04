# document-metadata-policy cycle 21 — Context Quality Reviewer gate Directive

Date: 2026-09-04
Documents in scope:
- policies/document-metadata-policy.md @ aadfe40a6a396c456b2bfb53763cf322fcc793c8

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/document-metadata-policy-cycle-21-gate-directive.md, commit it alone with a
message naming the gate it opens, push with git push origin document-metadata-policy-cycle-21-gate (no -u), verify by git ls-remote origin document-metadata-policy-cycle-21-gate, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-document-metadata-policy-cycle-21-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-document-metadata-policy-cycle-21-gate" -b document-metadata-policy-cycle-21-gate origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch document-metadata-policy-cycle-21-gate, if a branch of that name already exists locally or on origin (git ls-remote origin document-metadata-policy-cycle-21-gate returns a ref), or if "$TMPDIR/fiducial-document-metadata-policy-cycle-21-gate" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

No findings precede this gate; nothing is disposed here. This directive opens
the review, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted the revision's directive, not the document). One document, one
cycle, one verdict. Full-depth review of policies/document-metadata-policy.md @
aadfe40a6a396c456b2bfb53763cf322fcc793c8 — the document whole, all twelve
criteria of docs/global-context/review-rubric.md, and LEXICON.md conformance —
not a confirmation pass. The last whole-document read was cycle 19; cycle 20
confirmed fixes only.

The four changes recorded in docs/cycles/document-metadata-policy-cycle-21-directive.md
(DMP21-1 through DMP21-4) were dictated wording; confirm each is realized
exactly, against the diff from the prior revision
dda60a262c6eb775632ae5fefcf18fbe02d9add5 (the parent revision of the content
commit), and that no hunk falls outside the seven locations that directive
names. The rulings behind them are not open: the absent-key reading of
converging (told — OPEN-ITEMS.md, the bin/ package paragraph in "Queued
next"), cycle-12 N1 and N3 (accepted advisory), and CR5-3 with the #273 rider.
Whether the dictated sentences realize those rulings well is in scope — a
finding against the wording is a finding, and the decision session disposes it.

Two one-line checks travel with this gate, from the tracker (told); record each
as a finding or a one-line clearance in the artifact:

1. Expedited-stretch: a 1,400-line TRD was once agreed on the expedited path
   (retros/retro-20260824T160000.md, evidence item 20). State whether
   conditions 2 and 4 as written now foreclose it.
2. Enforcement admits a well-formed `last-reviewed` pointer on a `converging`
   document (bin/aimeta/frontmatter.py validate(), the last-reviewed branch).
   State whether the policy's text, as revised, needs to say anything about it.

One executor observation is also in scope (told — the Editor's report, pull
request #316): after DMP21-2 and DMP21-3, the doc-only `### Sequence` states
"touches only that document" in two adjacent places — the end of the
two-differences sentence and the opening of the companion-path paragraph. Assess
under criterion 4 or 12 as you judge; a non-blocking finding with a proposed cut
is the expected shape, not a blocking one.

Finding ids take this cycle's prefix: DMP21-n, continuing after DMP21-4.

LOOP START (told — the decision session's statement, Dave's to override): the
agreement bar is a verdict of ready or ready-with-findings with zero blocking
findings; cadence is this full-depth gate, then a fix directive if findings
warrant one, then one confirmation-scoped re-gate over the fix, then one flip
citing the artifact at its reviewed SHA. Non-blocking findings that need no fix
ride as riders on the flip.

ARTIFACT. Produce reviews/document-metadata-policy-cycle-21.md per
skills/review-artifact.md, verdict first, its Reviewed: line naming
policies/document-metadata-policy.md @ aadfe40a6a396c456b2bfb53763cf322fcc793c8
in full, stating in its own scope that it reviewed that document at that SHA,
and its Prior cycle: line naming reviews/document-metadata-policy-cycle-20.md @
3aa12a53e5cd5c134b54c4f77325f306c4d12ece. Cross-checked names everything run or
read. Not inspected is stated explicitly. Before writing, confirm the path is
absent at the base ref (git cat-file -e
0da165a56a7e3990828a904b8f3f273f3dd31d41:reviews/document-metadata-policy-cycle-21.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to the policy or any governed file. Commit the artifact
alone after the directive's own commit.

## Deferred / out of scope

- Findings triage, any fix directive, the re-gate, and the agreement flip — the
  decision session's next steps after this report; tracked by the cycle.
- The suite's accepted-red baseline (cycle 20's "Dave should inspect") — not this
  document's; stays in OPEN-ITEMS.md. Do not run bin/tests/run for it.
- The in-scope file count moving from 61 (cycle 20's record) to 62 — a fact about
  the tree, not this document; record the current count from
  bin/check-frontmatter --all and nothing more.
- bin/aimeta/expedited.py path-blindness — tracked in OPEN-ITEMS.md; a policy
  finding only if the revised text now contradicts it.
- The Context Quality Reviewer corpus pass — a queued program, sequenced after
  this cycle; this gate is one document's, not the program's opening.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin document-metadata-policy-cycle-21-gate — no -u; the sandbox refuses the
  .git/config write. Process substitution (<(...)) is refused by the sandbox;
  use temp files. A compound command after a cd can be rejected whole and
  silently by the sandbox's ~/.ssh deny rule (told — two executors' reports);
  use absolute paths and one git command per invocation, and confirm each
  commit landed with git log before proceeding.
- Inner fences in this directive are ~~~ so it travels inside one paste block;
  write them to the file as they are.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-document-metadata-policy-cycle-21-gate" (no --force). If it fails, report the
  failure; do not retry. Your report's final line states whether the worktree
  was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
0da165a56a7e3990828a904b8f3f273f3dd31d41. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ aadfe40a6a396c456b2bfb53763cf322fcc793c8
- docs/cycles/document-metadata-policy-cycle-21-directive.md @ 0a9a26dac7902c4ad38cd13f3ec3be6f6602e2d1 — the Editor directive; DMP21-1 through DMP21-4 and the seven locations.
- reviews/document-metadata-policy-cycle-20.md @ 3aa12a53e5cd5c134b54c4f77325f306c4d12ece — the prior cycle.
- reviews/document-metadata-policy-cycle-19.md @ fd16aa7758407c86561318c59a713319c18c486a — the last full-depth read.
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- skills/review-artifact.md @ 5d593a742b6726861b7f57a6d93cc31851b2408b
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41
- skills/conversation-retro.md @ abd7c9cde0b71b3639edda22b8e5e2c062514cee — lines 18-20 only, for DMP21-4.
- bin/aimeta/frontmatter.py @ 2e23b8445f10fb0ee680192e856af63da954ea65 — validate(), the last-reviewed branch only, for DMP21-1 and check 2.
- retros/retro-20260824T160000.md @ 361a14d4122df05b53c7c2ebd8ff284309464d0b — evidence item 20 only, for check 1.
- OPEN-ITEMS.md @ 56060d52a644c137d944e474d5a93e19e4d810ed — the entry "document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)" and the entry "bin/aimeta/expedited.py is path-blind" only.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, before the final push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-document-metadata-policy-cycle-21-gate-frontmatter.log", exit status reported
   (expected 0) and the file count stated, labelled observed.
2. git diff --stat 0da165a56a7e3990828a904b8f3f273f3dd31d41..HEAD in the worktree:
   exactly two added files — this directive and the review artifact; state it,
   labelled observed.
3. The artifact's Reviewed: line names the document at
   aadfe40a6a396c456b2bfb53763cf322fcc793c8 character-for-character; state it,
   labelled observed.
4. git diff --stat dda60a262c6eb775632ae5fefcf18fbe02d9add5..aadfe40a6a396c456b2bfb53763cf322fcc793c8 -- policies/document-metadata-policy.md:
   one file, 24 insertions and 15 deletions (told — the Editor's report); state
   what you observe.

STOP CONDITIONS

Pinned to the reviewed ref 0da165a56a7e3990828a904b8f3f273f3dd31d41. Cannot execute as written: stop
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

    document-metadata-policy cycle 21 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    Decisions — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Deferred / out of scope — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Execution notes — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
