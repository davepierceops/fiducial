# document-metadata-policy cycle 21 — fix Directive

Date: 2026-09-04
Documents in scope:
- policies/document-metadata-policy.md @ aadfe40a6a396c456b2bfb53763cf322fcc793c8

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/document-metadata-policy-cycle-21-fix-directive.md, commit it alone with a
message naming the fix it carries, push with git push origin document-metadata-policy-cycle-21-fix (no -u), verify by git ls-remote origin document-metadata-policy-cycle-21-fix, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix", created by: git worktree add --no-track "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix" -b document-metadata-policy-cycle-21-fix origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch document-metadata-policy-cycle-21-fix, if a branch of that name already exists locally or on origin (git ls-remote origin document-metadata-policy-cycle-21-fix returns a ref), or if "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

Findings disposition for reviews/document-metadata-policy-cycle-21.md (verdict
changes-required; DMP21-5 blocking, DMP21-6 and DMP21-7 non-blocking). Three
items are listed below, and three is the count; all three are accepted, wording
dictated. Line numbers are at aadfe40a6a396c456b2bfb53763cf322fcc793c8
(observed). A confirmation-scoped re-gate follows in a later directive.

### DMP21-5 — accept (converging is a spec status)
Finding: the policy states `converging` as a status any in-scope document may
hold (lines 71-73, 134-138, 139-145); LEXICON.md, DEC-000360 and
operating-model.md state it as a spec document's status, and no governed file
owns an exit gate for a non-spec document.
Resolution: Dave ruled 2026-09-04 (told — the decision session): `converging`
reaches documents under `specs/` only. Narrow this file to match. Three edits,
each replacing the whole bullet named:
- lines 71-73, the `converging` definition bullet, with the first dictated
  wording;
- lines 134-138, the entry-and-exit bullet, with the second;
- lines 139-145, the revision-re-entry bullet, with the third.
Nothing else in the file changes for this item: line 70's status list, line 82's
`last-reviewed` bullet, lines 128-133, and the build-gating rule under "Agent
behavior" already read correctly for a spec-only status. Then sweep the whole
document for any remaining sentence that states or presupposes a non-spec
document holding `converging` (Core 13) and report what you find, labelled
observed; do not edit beyond the three bullets without stopping.
Dictated wording (lines 71-73): `converging` = of a document under `specs/` only: its first reviewer gate has run and, on Dave's say, the spec is edited freely while tests are written against it; nothing in it is agreed. No other document holds this status.
Dictated wording (lines 134-138): **Dave's.** A spec enters `converging` after its first reviewer gate has run, whatever the verdict, on Dave's say. A content edit to a `converging` spec changes neither its status nor its `last-reviewed`. The spec leaves `converging` only by the agreement flip, on Dave's ruling at the exit gate.
Dictated wording (lines 139-145): **Dave's.** A revision of an `agreed` spec — flipped to `in-review` by its edit — may enter `converging` under the same entry rule: a reviewer gate has run on the revision, whatever its verdict; Dave says so; and the transition is a frontmatter-only status transition from `in-review` to `converging`. It leaves `converging` the same way the first interval does. A revision whose tests do not change takes the ordinary route from `in-review` to `agreed`.

### DMP21-6 — accept (doc-only Sequence: duplicate "touches only that document")
Finding: lines 284 and 286 both state the one-document-per-commit rule; the
second is singular where the first now admits several commits.
Resolution: the reviewer's proposed cut, as dictated. Replace the paragraph at
lines 286-288 with the dictated wording. Line 284 stands.
Dictated wording: A companion tracked path (a `decisions/log.md` entry, an `OPEN-ITEMS.md` update) lands in its own commit, per the expedited path's "no other tracked path" rule.

### DMP21-7 — accept (consistency sweep restates Core 13)
Finding: lines 259-260, "It extends the within-document consistency check
already required to the document's neighbours.", restates a rule Core already
states and reaches further than this sentence claims.
Resolution: the reviewer's proposed cut. Delete that one sentence; the
definition before it and the sentence after it stand. Re-wrap the paragraph at
the column the surrounding text uses.
Dictated wording: none — a cut.

## Deferred / out of scope

- The confirmation-scoped re-gate over this fix, then the agreement flip — the
  decision session's next directives.
- Riders from DMP21-5, for other files' next cycles, recorded at the next
  OPEN-ITEMS flush: roles/chief-of-staff.md:33, skills/spec-review-cycle.md:126
  and :135, and skills/review-artifact.md:80 say "document" where the status is
  spec-only. Do not edit them here.
- docs/rule-register/rule-register-20260825T1435.md:413 quoting a superseded
  sentence — a derived artifact pinned by its own header; not touched.
- LEXICON.md, operating-model.md, decisions/log.md — read for DMP21-5 only; do
  not edit. No decision-log entry is written: the ruling conforms this file to
  DEC-000360 and the Lexicon as already recorded.

## Execution notes

- One content commit after the directive's own commit, touching
  policies/document-metadata-policy.md only. The document is in-review with
  last-reviewed null; the pre-commit hook leaves both as they are — never bypass
  it.
- Apply the three items in the order given. Dictated wording is used verbatim;
  wrap prose at the column the surrounding text uses and keep each bullet's
  indentation.
- Nothing else in the file changes. The Lexicon touch rule applies; if it would
  require a further edit, stop and report rather than make it.
- Inner fences in this directive are ~~~ so it travels inside one paste block;
  write them to the file as they are.
- Write citations bare — no backticks or quotes around a path in a path @ sha
  citation.
- Push with git push origin document-metadata-policy-cycle-21-fix — no -u; the sandbox refuses the .git/config
  write. Process substitution (<(...)) is refused by the sandbox; use temp files.
  A compound command after a cd can be rejected whole and silently by the
  sandbox's ~/.ssh deny rule (told — executors' reports); use absolute paths and
  one git command per invocation, and confirm each commit landed with git log
  before proceeding.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix" (no --force). If it fails, report the
  failure; do not retry. Your report's final line states whether the worktree
  was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
47b0c55399c711634f1421295f208622e63a16d4. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ aadfe40a6a396c456b2bfb53763cf322fcc793c8
- reviews/document-metadata-policy-cycle-21.md @ fe14d8adba1217a5e1930311e828fd0c271f1012 — DMP21-5, DMP21-6, DMP21-7.
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
   "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix-frontmatter.log", exit status reported (expected 0).
2. grep -n "converging" policies/document-metadata-policy.md in the worktree,
   output captured to "$TMPDIR/fiducial-document-metadata-policy-cycle-21-fix-grep.log"; state every hit, labelled
   observed, and for each whether it now reads spec-only or is status-neutral.
3. grep -c "touches only that document" policies/document-metadata-policy.md in
   the worktree; expected 1; state the count, labelled observed.
4. grep -c "within-document consistency check" policies/document-metadata-policy.md
   in the worktree; expected 0; state the count, labelled observed.
5. git diff --stat of the content commit: exactly one file; state it, labelled
   observed. Then git show of that commit, read whole: each dictated wording
   present verbatim, and no hunk outside the five locations the three items name
   (lines 71-73, 134-138, 139-145, 259-260, 286-288 at the reviewed ref) — state
   the hunk count, labelled observed.
6. head -5 of the document in the worktree: status in-review, last-reviewed null,
   audience unchanged; state each, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref 47b0c55399c711634f1421295f208622e63a16d4. Cannot execute as written: stop
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

    document-metadata-policy cycle 21 — fix Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
