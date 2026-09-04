# document-metadata-policy cycle 22 — confirmation re-gate Directive

Date: 2026-09-04
Documents in scope:
- policies/document-metadata-policy.md @ d185baf33fdf41905e1789db388eaa2498410884

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/document-metadata-policy-cycle-22-directive.md, commit it alone with a
message naming the re-gate it opens, push with git push origin document-metadata-policy-cycle-22 (no -u), verify by git ls-remote origin document-metadata-policy-cycle-22, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-document-metadata-policy-cycle-22", created by: git worktree add --no-track "$TMPDIR/fiducial-document-metadata-policy-cycle-22" -b document-metadata-policy-cycle-22 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch document-metadata-policy-cycle-22, if a branch of that name already exists locally or on origin (git ls-remote origin document-metadata-policy-cycle-22 returns a ref), or if "$TMPDIR/fiducial-document-metadata-policy-cycle-22" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

No findings are disposed here; this directive opens the cycle-22
confirmation-scoped re-gate over the cycle-21 fix. The cycle-21 dispositions are
recorded in docs/cycles/document-metadata-policy-cycle-21-fix-directive.md: DMP21-5
accepted on Dave's ruling that `converging` reaches documents under `specs/` only;
DMP21-6 and DMP21-7 accepted as the reviewer's proposed cuts.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review. One document, one cycle, one verdict. Scope is confirmation, not a
fourth full-depth read: cycle 21 read the document whole at aadfe40a and this
cycle confirms only that its three dispositions landed and introduced nothing
new. Three confirmations:

1. Each disposition is realized exactly as the fix directive dictates, verified
   against the diff aadfe40a6a396c456b2bfb53763cf322fcc793c8..d185baf33fdf41905e1789db388eaa2498410884
   of the one file — DMP21-5 at the three bullets, DMP21-6 at the doc-only
   Sequence, DMP21-7 at the consistency-sweep definition — and no hunk falls
   outside the five locations that directive names.
2. Criterion 12 over the text the fix touched: the revised `converging` bullets
   against LEXICON.md's Converging entry, operating-model.md's Converging stage,
   and DEC-000360 — record agreement or disagreement. The three files the fix
   directive names as riders (roles/chief-of-staff.md:33,
   skills/spec-review-cycle.md:126 and :135, skills/review-artifact.md:80) are
   known to say "document"; note them in Not inspected or Dave should inspect,
   not as findings — they are recorded riders for those files' cycles.
3. No new contradiction between the revised text and the text it cites, over
   the fix's diff only.

Findings against text the fix did not touch are out of scope; cycle 21's pass on
criteria 1-11 stands and the artifact says so in Scope. Finding ids take this
cycle's prefix: DMP22-n.

LOOP START (told — the decision session's statement, Dave's to override): the
agreement bar is ready or ready-with-findings with zero blocking findings; on
that verdict the next directive is the flip citing this artifact at
d185baf33fdf41905e1789db388eaa2498410884. A blocking finding returns to the
decision session for triage.

ARTIFACT. Produce reviews/document-metadata-policy-cycle-22.md per
skills/review-artifact.md, verdict first, its Reviewed: line naming
policies/document-metadata-policy.md @ d185baf33fdf41905e1789db388eaa2498410884
in full, stating in its own scope that it reviewed that document at that SHA,
and its Prior cycle: line naming reviews/document-metadata-policy-cycle-21.md @
fe14d8adba1217a5e1930311e828fd0c271f1012. A confirmation pass that finds nothing
is the header and nothing else, Verdict: ready. Before writing, confirm the path
is absent at the base ref (git cat-file -e
8a0bf2f4378acefe03dede7c3f48bda6970ca92e:reviews/document-metadata-policy-cycle-22.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only. Commit the artifact alone after the directive's own commit.

## Deferred / out of scope

- The agreement flip — the decision session's next directive on a ready or
  ready-with-findings verdict.
- The three "document"-wording riders above — recorded for their files' next
  cycles at the next OPEN-ITEMS flush; not this gate's findings.
- The suite's accepted-red baseline and the 61→62 in-scope count — tree facts,
  not this document's; record the current count from bin/check-frontmatter
  --all and nothing more.
- The Context Quality Reviewer corpus pass — a queued program; this is one
  document's re-gate.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin document-metadata-policy-cycle-22 — no -u; the sandbox refuses the .git/config
  write. Process substitution (<(...)) is refused by the sandbox; use temp
  files. A compound command after a cd can be rejected whole and silently by the
  sandbox's ~/.ssh deny rule (told — executors' reports); use absolute paths and
  one git command per invocation, and confirm each commit landed with git log
  before proceeding.
- Inner fences in this directive are ~~~ so it travels inside one paste block;
  write them to the file as they are.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-document-metadata-policy-cycle-22" (no --force). If it fails, report the
  failure; do not retry. Your report's final line states whether the worktree
  was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
8a0bf2f4378acefe03dede7c3f48bda6970ca92e. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ d185baf33fdf41905e1789db388eaa2498410884
- docs/cycles/document-metadata-policy-cycle-21-fix-directive.md @ efc4998a6b1476a18fe1bf4c7c8431bf652edfc1 — the decision record for the three dispositions.
- reviews/document-metadata-policy-cycle-21.md @ fe14d8adba1217a5e1930311e828fd0c271f1012 — the prior cycle, whole.
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- skills/review-artifact.md @ 5d593a742b6726861b7f57a6d93cc31851b2408b
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41 — the Converging entry and the touch rule.
- operating-model.md @ 2fbb092b2544475021c2a4e7a9c68c4ddcb9d727 — the Converging stage of the spec lifecycle only.
- decisions/log.md @ 9cca04849c14d3f49a8ff0e171932e7590073158 — DEC-000360 only.

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
   "$TMPDIR/fiducial-document-metadata-policy-cycle-22-frontmatter.log", exit status reported (expected 0)
   and the file count stated, labelled observed.
2. git diff --stat 8a0bf2f4378acefe03dede7c3f48bda6970ca92e..HEAD in the worktree:
   exactly two added files — this directive and the review artifact; state it,
   labelled observed.
3. The artifact's Reviewed: line names the document at
   d185baf33fdf41905e1789db388eaa2498410884 character-for-character; state it,
   labelled observed.
4. git diff --stat aadfe40a6a396c456b2bfb53763cf322fcc793c8..d185baf33fdf41905e1789db388eaa2498410884 -- policies/document-metadata-policy.md:
   one file, 23 insertions and 24 deletions, 4 hunks (told — the fix session's
   report); state what you observe.

STOP CONDITIONS

Pinned to the reviewed ref 8a0bf2f4378acefe03dede7c3f48bda6970ca92e. Cannot execute as written: stop
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

    document-metadata-policy cycle 22 — confirmation re-gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
