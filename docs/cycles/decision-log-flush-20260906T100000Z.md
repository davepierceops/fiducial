# Decision-log flush: the rebuild's rulings, DEC-000420 through DEC-000510

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Write this directive verbatim to docs/cycles/decision-log-flush-20260906T100000Z.md, commit it alone with a
message naming the package it opens, push the branch decision-log-flush to origin with a plain
`git push origin decision-log-flush`, never with `-u`, and report the SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-decision-log-flush", created by:
git worktree add --no-track "$TMPDIR/fiducial-decision-log-flush" -b decision-log-flush origin/main

BASE VERIFICATION

Before anything else, fetch origin/main and confirm the base is at the reviewed ref
a184967413681950a2e8ffa2ab3e16be552f7158. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — the log; its
  last entry is DEC-000410
- process/change-flow.md @ 81310de105b0f0b4133117fa4c209baea9d84b09 — the
  document entry 5 records as agreed
- docs/cycles/store-all-topics-20260906T020000Z.md, read from the base ref
  a184967413681950a2e8ffa2ab3e16be552f7158 — the register-to-store rulebook the
  entries' Context lines point at

TASK

Append ten entries to decisions/log.md, one commit each, in the order below,
using the entry form the log already uses (`## DEC-NNNNNN — <short title>`,
`Date:`, `Decision:`, `Context:`, `Supersedes:` only where stated). Ids are
DEC-000420 through DEC-000510 in steps of ten. Every date is 2026-09-05. The
Decision line is used verbatim; write the Context line in one or two
sentences from the pointer given. Edit no existing entry and no other file.

1. DEC-000420 — Definitions are rows selected by term
   Decision: A definition is a row carrying a `term` key and no role,
   session, or corpus key. The bundle tool includes a definition when a
   selected row's body uses one of its terms, and scans the pulled
   definitions' bodies the same way, transitively.
   Context: the PRD's G12; a definition keyed to roles either duplicates
   across bundles or goes missing from one.

2. DEC-000430 — Engagement material waits for the next engagement
   Decision: No engagement material is written as rows now. `engagements/`
   stays as it is until the next engagement needs it, and is written then
   through intake.
   Context: resolves the rule-store PRD's OQ-2; the 153 register rows from
   the engagement files were left untouched by the store migration.

3. DEC-000440 — A Test Designer edits tests only; a spec writer edits specs only
   Decision: A Test Designer edits tests and nothing else; a spec change it
   needs is a finding to the decision session. A spec writer edits specs and
   nothing else; a test change it needs is a finding to the decision session.
   Context: register cluster C097; the positive wording Dave chose over the
   two prohibitions the source files carried.

4. DEC-000450 — Two register rows merge only on the same obligation and the same keys
   Decision: Two register rows become one store row only when they state the
   same obligation and would carry the same keys. Any difference in keys
   splits them, however close the wording.
   Context: the rule the store migration and every fix pass merged under;
   a merged row states the rule at its shortest, not the sum of its sources.

5. DEC-000460 — process/change-flow.md agreed at 81310de
   Decision: process/change-flow.md is agreed at
   81310de105b0f0b4133117fa4c209baea9d84b09, the first document under the
   process gate DEC-000380 names. It supersedes DEC-000360's mechanism — the
   converging status and its transitions — and not its substance;
   DEC-000370 stands. Every pull request gets an agentic code review with no
   trivial-change exemption; quality and skepticism are always two passes,
   in one session or two by class or by a size call; the Reviewer rows stay
   in force until an adopted published code-review standard replaces them
   in the same commit.
   Supersedes: DEC-000360
   Context: five frontier reads (reviews/change-flow-read-*.md), then Dave's
   agreement on 2026-09-05.

6. DEC-000470 — `all` is not a role value
   Decision: No row carries `role: [all]`. Every row's role list is decided
   for that row; the roles in use are the twelve role-document slugs at
   fd54448.
   Context: a blanket role list defeats selection by query, which is the
   store's whole mechanism.

7. DEC-000480 — Corpus values are software and writing
   Decision: The `corpus` key takes the values `software` and `writing`.
   `methodology` is not a value until a row needs it.
   Context: the register's methodology rows all keyed to a role and a
   session already; a third corpus value had nothing to select.

8. DEC-000490 — Templates and schemas are process documents
   Decision: A template or a schema is a `process/` document selected by
   key, not a set of rows. Rows are written only where an agent performs an
   act: the TRD, PRD, voice, outline, review-artifact, retro, decision-log
   entry form, and project setup are process documents.
   Context: a document's form is prose; rows that restated a template's
   sections were the restatement problem in another shape.

9. DEC-000500 — One decision per decision-log entry
   Decision: A decision-log entry records exactly one decision. Two decisions
   made together are two entries.
   Context: Dave's ruling of 2026-09-06 when the rebuild's entries were
   listed for the flush; an entry carrying several rulings cannot be
   superseded one at a time.

10. DEC-000510 — The intake checklist is the store's construction rule
    Decision: R0264, the intake checklist, is the rule every row is judged
    by on entry and the rule the store was built under. Its criteria are
    rows in topic intake, not decisions; a change to a criterion goes
    through intake like any row.
    Context: the criteria were ruled one at a time across the fix-pass reads
    of 2026-09-05 and 2026-09-06 and are recorded here once, as one rule.

Commit messages: `decisions: DEC-0004NN — <short title>`. Push after every
commit. Do not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-decision-log-flush"`) and report that
it is gone. decisions/log.md is outside the frontmatter hook's in-scope set;
if the hook fires, stop and report.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the last commit and before removing the worktree:

~~~sh
{
  grep -c '^## DEC-' decisions/log.md
  grep '^## DEC-' decisions/log.md | tail -11
  grep -c '^Supersedes: DEC-000360' decisions/log.md
  git -C "$TMPDIR/fiducial-decision-log-flush" log --oneline origin/main..HEAD | wc -l
  git -C "$TMPDIR/fiducial-decision-log-flush" diff --stat origin/main..HEAD | tail -1
} 2>&1 | tee "$TMPDIR/decision-log-flush-verify.log"
~~~

Expected: 51 entries (41 at the base plus ten); the last eleven headings
from DEC-000410 through DEC-000510; 1; 11 commits; a diff-stat touching
decisions/log.md and the directive file only.

STOP CONDITIONS

Pinned to the reviewed ref a184967413681950a2e8ffa2ab3e16be552f7158. Cannot execute as written: stop
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

    Decision-log flush: the rebuild's rulings, DEC-000420 through DEC-000510 — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
