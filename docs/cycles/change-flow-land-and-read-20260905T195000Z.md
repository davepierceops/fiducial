# Land process/change-flow.md and run its one frontier read

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to
docs/cycles/change-flow-land-and-read-20260905T195000Z.md in that worktree,
commit it alone with a message naming the package it opens
(`process: change-flow — directive`), push the branch `change-flow` to origin
with plain `git push origin change-flow` (never `-u`), and report the SHA. Do
this before reading anything else and before touching any other file. Base
verification below runs before this act.

FENCE NOTE: fences in the author-written regions (TASK, VERIFICATION) use
`~~~` so they survive transport inside a paste block; the generator's own
regions keep their ``` fences and the paste block that carries this directive
is opened with four backticks for that reason. Treat `~~~` fences exactly as
```fences.

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
worktree at "$TMPDIR/fiducial-change-flow", created by:
git worktree add --no-track "$TMPDIR/fiducial-change-flow" -b change-flow origin/main

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
69c0a9fdec47f6949764a7d98b7560f819d7783b. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — DEC-000170,
  DEC-000360, DEC-000380 whole; skim the rest for any entry the document
  contradicts
- docs/rule-register/topic-digest-20260905T181500Z.md @ 0bd149ce85f8519e2e9d681d3827b74bef237f43
  — the header and cards 2, 3, 11, 13, 23, 30, 47 (the operating model, the
  spec review cycle, commit control, the Spec Reviewer, spec discipline, the
  Test Designer, the Reviewer)
- docs/rule-register/rule-register-20260904T210000Z.md @ 45b02c7b88a0e08f4872713aa39f840a59117423
  — only the rows the document cites by `R` id; do not read it whole
- skills/review-artifact.md @ 5d593a742b6726861b7f57a6d93cc31851b2408b — the
  schema your review artifact follows

TASK

Two acts, two commits, in order. This is the first document landed under the
gate DEC-000380 defines for process documents: one frontier read, then Dave's
sign-off recorded in the decision log. You are the read. You did not draft the
document; the decision session did.

ACT 1 — land the document. Write the following verbatim to
process/change-flow.md (create the directory). Commit it alone with the message
`process: change-flow — first draft for the frontier read`. Push. Report the
SHA; the review below cites it.

~~~markdown
---
order: 10
session: [decision, execution]
corpus: [software, methodology]
---

# Process: Change Flow

**Status of this draft:** proposal for Dave's correction, 2026-09-05. First
document under the new gate (DEC-000380): one frontier read against the rows it
cites, then Dave's sign-off, recorded as a decision-log entry naming the SHA.
Rows are cited by register id (`R0000`) until the store assigns ids; the Store
package maps them.

## The principle

**Review is charged once per delta, and a delta is whatever one reviewer can
read whole.**

A delta is the accumulated difference between a thing as it stands and the
thing as it will stand when the work is done. Review attaches to the delta at
its close — never to a document, never to an edit. A typo fix is a one-row
delta and closes in one commit. A rebuild is one delta too, and one reader
reads its whole diff once, doing every kind of review the delta needs as
sections of a single read. What sets the depth of the review is the size and
reach of the delta, not the number of documents it touched.

This is the rule the corpus already stated twice in narrower forms — for spec
branches (DEC-000170: "the gate is charged once at reconciliation, not once
per edit") and for rules (DEC-000380: one intake act per row) — stated once,
for everything.

## Three kinds of thing change

Each has one delta shape and one closing act. Nothing else in this document
adds a gate.

| What changes | The delta | Closed by | Who reads |
|---|---|---|---|
| **Rules** — rows in `rules/`, prose in `process/` | the proposed rows or the edited document | **intake**: one commit | Context Quality Reviewer |
| **Specs** — a project's PRD, TRD, acceptance criteria | a spec branch with commits on it | **reconciliation**: one read, one ruling, one pull request | Spec Reviewer, then Dave |
| **Code** — a project's implementation | a unit of work's branch, landing as one pull request | **change package**: one read over the package; every pull request gets a code review by an agent | Reviewer and Skeptic/Risk, then Dave at the release gate |

A delta is bounded by one workstream and never spans two (R0008). It may be
closed early, at will; frequent small closes are the norm and the workstream
boundary is a deadline, not a target (DEC-000170).

## The one read

At close, one reviewer session reads the whole delta — the diff from the point
the delta opened to the revision under review, plus whatever the delta
produced (tests, evidence, a change package). The read is organised by
**dimension**, not by document:

- **Continuity** — does the delta contradict anything it did not change? For a
  spec delta this is the continuity scan (R1104–R1137); for a rules delta it is
  the near-duplicate shortlist plus judgment; for a code delta it is the
  architecture summary against the TRD. The scan's depth is set by the delta's
  reach, not requested separately: a delta that touches only the spine gets a
  spine read; one that touches policy gets policy read too.
- **Quality** — is this good? Maintainability, correctness, consistency, test
  adequacy (stage 9 of R0470). For a code delta this dimension **is a code
  review, and every pull request gets one, by an agent** — no human diff-read
  by default (the human-review boundary stands), and no pull request without
  one. The reviewer's rules are not written here: an established, published
  code-review standard is adopted whole and enters the store through intake
  as rows whose `source` names that external document; the Reviewer role's
  own document is retired in its favour.
- **Skepticism** — where is this lying to us? False confidence, mocked-boundary
  and live-integration gaps, release overclaims (stage 10).

**Dimensions are an open set.** The three above are the ones the corpus has
today. A new one — a reliability review, a security review, whatever the next
year shows is missing — is added by intake, not by editing this document: its
rules land as rows keyed `dimension: [security]`, and a read includes every
dimension whose rows match the delta's kind. `bin/bundle --keys` shows which
dimensions exist; this document never lists them.

Two separations hold whatever the delta's size (R0462, R0463): whoever produced
the delta does not read it; whoever drafted a document does not gate it.

A read of a **consequential** delta — one touching the commit-and-change-control
policy's consequential class (R0534–R0547) — is done by two readers, quality
and skepticism as separate sessions, because a change can pass one and fail the
other (R0492). Every other delta is one reader, three sections.

**A deep read, on demand, at any time.** Dave — or the Chief of Staff on his
behalf — may call for a full read of anything, at any point, whether or not a
delta is closing: every dimension, two readers, continuity at its widest reach,
over the whole thing rather than a diff. It is a directive like any other, with
the object named (a spec, a project's code, the rules store); its verdict is
input to Dave. The Chief of Staff proposes one at milestone moments without
being asked; the row that grants it is keyed so it shows on the list of things
Dave can call for.

The read's output is a review artifact in the review-artifact schema, with one
verdict. There is no fix-round-then-re-gate loop by default: findings are
triaged by the decision session; blocking findings reopen the delta, which then
closes again with one more read over the diff since the last read — not over
the whole delta again.

## The spec lifecycle, restated

A spec has two states and no status field: its branch is **open** (has commits
the default branch does not) or **closed** (agreed; the default branch is the
version of record).

1. **Open.** A spec branch is cut, `spec/<workstream-slug>`. While it is open,
   Dave edits the spec freely with no per-edit gate (R0007); the Test Designer
   writes the spec's test suite against it and confirms the suite red on bad
   logic, not on an absent import (R0016, R1152); findings flow both ways
   through the decision session. Nothing is *implemented* against an open
   spec (DEC-000360: draft/in-review nothing; converging tests only; agreed
   implementation — the three values, with "converging" now meaning "open").
2. **Close.** When spec and tests cohere, one read over the whole diff plus
   the tests (the Spec Reviewer), then Dave reads that diff and rules once.
   The ruling is recorded in the decision log naming the reviewed SHA; the
   reconciliation pull request lands the branch. Agreement attaches to the
   version of record at that SHA (R0011).
3. **Reopen.** A revision of an agreed spec opens a new delta on a new branch
   and closes the same way. There is no smaller path: a one-line spec fix is a
   one-line delta, read in a minute.

What retires: the `converging` status and its two frontmatter transitions
(DEC-000360's mechanism, not its substance); the expedited and doc-only paths;
per-document cycle numbering and `last-reviewed` pointers (DEC-000380).

## The per-change stages, unchanged in substance

Once a spec is closed, each meaningful change against it runs the per-change
stages the operating model names (R0470, stages 5–12): acceptance criteria, an
architecture summary derived from the TRD, the unit's tests confirmed red,
implement to green with mechanical checks, then **the one read** — quality
and skepticism as sections, or two readers where consequential — then the
release package and Dave's release gate. Trivial changes (typo, comment,
formatting) are one-row deltas: they close on the committer's own check and
carry no read.

A change is done when the definition of done holds (R0508–R0519); the read is
one line of it, not a separate lifecycle.

## What this document does not decide

Dave's, one at a time when reached:

- Whether the Reviewer and Skeptic/Risk stay two roles, or become two sections
  of one reader's schema with the second reader summoned only for consequential
  deltas.
- Whether a project's spec files carry any frontmatter at all once `status` is
  gone (PRD OQ-3 keeps them as files; this document assumes `order` and
  selection keys only).
- Whether a reopened delta's read covers the diff since the last read (as
  stated above) or the whole delta again.
~~~

ACT 2 — the read. Write reviews/change-flow-read-20260905T195000Z.md in the
review-artifact schema, reviewing process/change-flow.md at the ACT 1 SHA.
Verdict values as the schema defines them. The read has three sections,
because the document says a read does:

- **Continuity.** Does the document contradict any decision in decisions/log.md
  that it does not name as retired? Does it contradict any surviving rule in
  the seven digest cards named above? For every `R` id it cites, does the
  register row say what the document uses it for? Name each contradiction with
  both locations; a contradiction with a rule the document explicitly retires
  (the `converging` status, the expedited and doc-only paths, per-document
  cycles) is not a finding — it is the point.
- **Quality.** Is the principle stated once and then applied, or restated? Can
  an agent act on each section without this conversation? Where does the
  document say two things? Plain-words test: any sentence Dave would need a
  term defined to read.
- **Skepticism.** Where does "one read" hide a review that will not actually
  happen? Where does "charged once per delta" let a large change through with
  less review than the old flow gave it? Is "two readers for the consequential
  class" enough, and is the class reachable — can a session tell it is in it?

Findings are labelled defect, suggestion, or accepted risk, each with the line
it rests on, per Core rule 10. Do not edit process/change-flow.md; the decision
session triages the findings and Dave rules. Commit the review alone with the
message `reviews: change-flow read`. Push. Report both SHAs and the verdict.
Then remove the worktree with `git worktree remove "$TMPDIR/fiducial-change-flow"`
and report that it is gone.

process/ and reviews/ are outside the frontmatter hook's in-scope set; the hook
should not fire. If it does, stop and report; do not bypass it.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the review commit and before removing the worktree:

~~~sh
{
  git -C "$TMPDIR/fiducial-change-flow" diff --stat origin/main..HEAD
  git -C "$TMPDIR/fiducial-change-flow" log --oneline origin/main..HEAD
  grep -c '^## ' process/change-flow.md
  grep -o 'R[0-9]\{4\}' process/change-flow.md | sort -u | wc -l
} 2>&1 | tee "$TMPDIR/change-flow-verify.log"
~~~

Expected: three files in the diff-stat, all additions — this directive,
process/change-flow.md, the review artifact; exactly three commits; 6 `##`
headings in the document; a count of distinct `R` ids, which the review's
continuity section must state it checked one by one.

STOP CONDITIONS

Pinned to the reviewed ref 69c0a9fdec47f6949764a7d98b7560f819d7783b. Cannot execute as written: stop
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

    Land process/change-flow.md and run its one frontier read — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
