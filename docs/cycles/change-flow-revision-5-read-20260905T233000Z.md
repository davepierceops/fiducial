# Land change-flow revision 5 and read the whole document

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to
docs/cycles/change-flow-revision-5-read-20260905T233000Z.md in that worktree,
commit it alone with a message naming the package it opens
(`process: change-flow revision 5 — directive`), push the branch
change-flow-r5 to origin with a plain `git push origin change-flow-r5`, never
with `-u`, and report the SHA. Do this before reading anything else and before
touching any other file. Base verification below runs before this act.

FENCE NOTE: the author-written regions (TASK, VERIFICATION) fence with tildes
so they survive transport inside a paste block; the generator's regions keep
their backtick fences and the paste block carrying this directive is opened
with four backticks for that reason. Treat a tilde fence exactly as a backtick
fence.

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
worktree at "$TMPDIR/fiducial-change-flow-r5", created by:
git worktree add --no-track "$TMPDIR/fiducial-change-flow-r5" -b change-flow-r5 origin/change-flow-r4

BASE VERIFICATION

Before anything else, fetch origin/change-flow-r4 and origin/main and confirm
the base — the branch change-flow-r4, not main — is at the reviewed ref
13ee4c7c4c5d969f21464fb452456da4ca60c471, and that origin/main is at
69c0a9fdec47f6949764a7d98b7560f819d7783b, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/change-flow-read-4-20260905T225000Z.md @ 13ee4c7c4c5d969f21464fb452456da4ca60c471
  — the fourth read; this session checks closure of its F-1 through F-9 and
  reads the whole document fresh. Earlier reads are context only
- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — whole
- docs/rule-register/rule-register-20260904T210000Z.md @ 45b02c7b88a0e08f4872713aa39f840a59117423
  — every row revision 5 cites by `R` id; do not read it whole
- docs/rule-register/rule-clusters-20260904T223000Z.md @ acdfef73fc04bed73d6f854b3f66fe8df5411519
  — the clusters each cited row belongs to, because the closing section now
  names obligations by representative row and resolves them through this
  artifact
- skills/review-artifact.md @ 5d593a742b6726861b7f57a6d93cc31851b2408b — the
  schema, as amended by the document's own verdict-line rule

TASK

Two acts, two commits, in order, on the branch change-flow-r5, cut from the
branch change-flow-r4. This is the fifth read of process/change-flow.md and a
whole-document read. You did not draft the revision; the decision session
did. No new rulings since the fourth read; every fourth-read finding was the
decision session's to fix.

ACT 1 — land revision 5. Overwrite process/change-flow.md with the following,
verbatim. Commit it alone with the
message `process: change-flow — revision 5 after the fourth read`. Push.
Report the SHA.

~~~markdown
---
order: 10
session: [decision, execution]
corpus: [software, methodology]
---

# Process: Change Flow

**Status of this draft:** revision 5, 2026-09-05, after four frontier reads
(reviews/change-flow-read-20260905T195000Z.md through
reviews/change-flow-read-4-20260905T225000Z.md) and Dave's rulings on the
first read's F-2, F-4, F-8, F-11 and the third read's F-2. Gate: one frontier read over the whole
document — not the diff, because the diff-only rule below is this document's
own proposal and binds only after sign-off — then Dave's sign-off, recorded as
a decision-log entry naming the SHA. Rows are cited by register id until the
store assigns ids; the Store package maps them. Every standing row this
document changes is named in the closing section "What this document changes
or retires".

## The principle

**Review is charged once per delta, and a delta should be no larger than one
reviewer can read whole.**

A delta is the accumulated difference between a thing as it stands and the
thing as it will stand when the work is done. Review attaches to the delta at
its close — never to a document, never to an edit. A typo fix is a one-row
delta and closes in one commit. A rebuild is one delta too; if a reader
finds it cannot be read whole, that summons a second reader (below) — the
norm's enforcement — and the Chief of Staff plans the next delta of that
shape as more than one. What sets the depth of the review is the size and reach of the delta, not
the number of documents it touched.

This is the rule the corpus already stated twice in narrower forms — for spec
branches (DEC-000170: "the gate is charged once at reconciliation, not once
per edit") and for rules (DEC-000380: one intake act per row) — stated once,
for everything.

## Four kinds of thing change

Each has one delta shape and one closing act. This document adds no gate to
these; it states the ones that exist.

| What changes | The delta | Closed by | Who reads |
|---|---|---|---|
| **Rules** — rows in `rules/` | the proposed rows | **intake**: one commit | Context Quality Reviewer |
| **Process** — prose in `process/` | the edited document | **one frontier read** against the rows it cites, then Dave's sign-off, recorded in the decision log naming the SHA (DEC-000380) | a frontier session that did not draft it, then Dave |
| **Specs** — a project's PRD, TRD, acceptance criteria | a spec branch with commits on it | **reconciliation**: one read, one ruling recorded in the decision log naming the SHA, one pull request | Spec Reviewer, then Dave |
| **Code** — a project's implementation | a unit of work's branch, landing as one pull request | **change package**: one read over the package; every pull request gets a code review by an agent, without exception | Reviewer and Skeptic/Risk, then Dave at the release gate |

A delta is bounded by its tranche and never spans two (R0008). It may be
closed early, at will; frequent small closes are the norm and the tranche
boundary is a deadline, not a target (DEC-000170).

## The one read

At close, a reviewer reads the whole delta — the diff from the point the delta
opened to the revision under review, plus whatever the delta produced (tests,
evidence, a change package). The read is organised by **dimension**, not by
document:

- **Continuity** — does the delta contradict anything it did not change? For a
  spec delta this is the continuity scan (R1104, R1105, R1133–R1137); for a
  rules delta it is the near-duplicate shortlist plus judgment; for a code
  delta it is the architecture summary against the TRD.
- **Quality** — is this good? Maintainability, correctness, consistency, test
  adequacy, over the diff and the mechanical results (R0487). For a code delta
  this dimension **is a code review, and every pull request gets one, by an
  agent** — no human diff-read by default (the human-review boundary stands),
  and no pull request lands without one. There is no trivial-change exemption,
  for the reason DEC-000300 refused the analogous lane: what made small
  changes expensive was a cycle, an agent reading a one-line diff is seconds,
  and a lane defined by the party it benefits widens. DEC-000300's trigger
  carries: the next concrete case that fits no route reopens the question
  rather than being worked around. The reviewer's rules are not written here: an established,
  published code-review standard is adopted whole and enters the store through
  intake as rows whose `source` names that external document. Until those rows
  land, the Reviewer role's rows (`roles/reviewer-agent.md` at store time) are
  in force; the intake commit that lands the standard retires them, each
  carrying its successor's id under the retirement key (`retired:` being the
  form intake would normalize to, per DEC-000400, not a reserved key), and
  conforms the human-review boundary's
  rows in the same commit.
- **Skepticism** — where is this lying to us? False confidence, mocked-boundary
  and live-integration gaps, config and deploy risk, release overclaims, over
  the whole evidence chain (R0488).

**Every dimension is a pass with its own verdict line**, continuity included.
Quality and skepticism are always two passes (R0492, R0517): a change can
pass one and fail the other, so the second question is asked after the first
has been answered. What the delta's class decides is whether quality and
skepticism are two *sessions*; continuity runs in the first session either
way:

- **One session** — the routine case. A single session holds both roles,
  is bound by both role documents' rows (R0487, R0488), and runs as the
  Reviewer first and then as the Skeptic, over the same diff, no re-read; its
  artifact carries both passes.
- **Two sessions** — on either of two triggers. First, the delta touches the
  commit-and-change-control policy's consequential class (R0534–R0547); when
  unsure, treat as consequential (R0536). Second, the **size call**: the
  reader finds the delta exceeds what one session can read whole and says so
  in the verdict, and a second session is summoned for the skeptic pass. The
  size call sets the number of sessions only; it does not make a change
  consequential for release purposes, and R0535's exhaustive list is unchanged
  by it.

**Scan depth follows the delta's reach.** This changes R1104 and R1136:
Depth 1 (the spine) always runs, its trigger moved from every spec revision to
the delta's close, because review is charged once per delta; a delta whose
diff touches a policy or boundary document gets Depth 2 in the same read, no
longer only through R1105's on-demand route. Depth 3 — everything against
everything, R1137 — is unchanged until the rules store exists, at which point
intake's sweep succeeds it over the methodology; the deep read below is its
equivalent for anything else. A scan nobody
asked for is the point; a scan nobody knew to ask for was the defect.

**Dimensions are an open set.** The three above are the ones the corpus has
today. A new one — a reliability review, a security review, whatever the next
year shows is missing — is added by intake, not by editing this document: its
rules land as rows keyed on the dimension — `dimension: [security]` being the
form intake would normalize to, per DEC-000400, not a reserved key — with the
other keys naming the delta kinds it applies to, and a read includes every
dimension that has a row matching the delta. The listing of keys in use that
DEC-000400 specifies is pending the Store and Tool packages; until it lands
the intake session names the dimensions in force.

Two separations hold whatever the delta's size (R0462, R0463): whoever produced
the delta does not read it; whoever drafted a document does not gate it.

**A deep read, on demand, at any time.** Dave — or the Chief of Staff on his
behalf — may call for a full read of anything, at any point, whether or not a
delta is closing: every dimension, two sessions, continuity at its widest
reach (Depth 3's equivalent, R1137), over the whole thing rather than a
diff. It is a directive like any other, with the object named (a spec, a
project's code, the rules store); its verdict is input to Dave. The Chief of
Staff proposes one at milestone moments without being asked. How Dave sees
the list of things he can call for is the Store package's to design.

The read's output is a review artifact in the review-artifact schema, amended
by this document in one respect: the header's single `Verdict:` line is the
overall call, and each pass section opens with its own `Verdict (<pass>):`
line — continuity, quality, skepticism, and any further dimension in force —
and the overall verdict is the most severe of the pass verdicts, on the order
ready, ready-with-findings, changes-required. Findings are triaged by the decision session; blocking
findings reopen the delta, which then closes again with one more read over
the diff since the last read — not over the whole delta again. (Working rule;
it is revised if a reopened delta's second read ever misses a contradiction the
first read would have caught.)

## The spec lifecycle, restated

A spec has two states and no status field: its branch is **open** (has commits
the default branch does not) or **closed** (agreed; the default branch is the
version of record).

1. **Open.** A spec branch is open from the commit that cuts it,
   `spec/<tranche-slug>` (R0004). While it is open, Dave edits the spec freely
   with no per-edit gate (R0007). The Test Designer begins once the **entry read** has run and Dave has said
   to proceed (DEC-000360's entry condition, kept: R0015 restated without the
   status flip). The entry read is the Spec Reviewer's, over the spec as it
   stands at that commit, emitting a review artifact whatever its verdict; it
   is charged separately from the delta's one read, because a test suite
   written against a spec nobody has read is what DEC-000360 ordered against.
   From then on the Test Designer
   writes the spec's test suite against the spec as it stands (R0016, R1152),
   holding enough of the interface contract to make the tests fail on bad
   logic rather than on an absent import (R0084), and runs that red-gate while
   the branch is open so its result is the close's evidence (R0087, R0478);
   findings flow both ways through the decision session. Nothing is
   *implemented* against an open spec (R0017), and none of the per-change
   stages runs against one (R0470). At most two tranches execute concurrently, over disjoint spec territory; a
   document appearing in one open delta's diff may not appear in a second
   (R0012, R0013); nothing decomposes from an open spec (DEC-000170).
2. **Close.** When spec and tests cohere, the Spec Reviewer reads the
   branch's whole diff plus the tests (R0480, restated: the diff runs from the
   branch point, not from a status transition); then Dave reads that diff and
   makes one ruling that agrees the spec and accepts the tests as its red-gate
   evidence (R0481, restated: the ruling is recorded in the decision log
   naming the reviewed SHA, not as a frontmatter flip; the tests' acceptance
   is recorded in the close's review artifact, to which the Test Designer
   hands the red-gate result, R1158). The reconciliation
   pull request lands the branch. Agreement attaches to the version of record
   at that SHA (R0011).
3. **Reopen.** A revision of an agreed spec opens a new delta on a new branch
   and opens and closes the same way, the entry read included (R0019's
   re-entry condition, restated). There is no smaller path: a one-line spec fix is a
   one-line delta, read in a minute.

What retires here: the `converging` status and both its frontmatter
transitions (DEC-000360's mechanism; its substance — the entry condition, the
test-only licence, the red-gate as close evidence — is kept above); the
expedited and doc-only paths; per-document cycle numbering and `last-reviewed`
pointers (DEC-000380). The rows are listed in the closing section, which
distinguishes rows *retired* from rows *restated* in the open/closed
vocabulary.

## The per-change stages, unchanged in substance

Once a spec is closed, each meaningful change against it runs the per-change
stages (R0470 for the span and the precondition; R0482–R0490 for the stages):
acceptance criteria; an architecture summary derived from the TRD; the unit's
tests confirmed red; implement to green with mechanical checks; then **the one
read** — quality and skepticism as two passes, one session or two by class;
then the release package and Dave's release gate. Mechanical checks are
evidence folded into green, not a review step (R0493).

A change is done when the definition of done holds (R0508–R0519); the read is
one line of it, not a separate lifecycle.

## What this document changes or retires

The lists below name **obligations** by the register row that states them.
The register is not deduplicated, so the Store package resolves each named
row to every register row stating the same obligation — the clusters artifact
is what that resolution reads — and treats the whole cluster as the list says.
That is how the lists are complete without a word search over the register.

Standing obligations this document amends, each with the change, for the
Store package to map and for the decision-log entry that agrees this document
to supersede:

- R1104, R1135 — Depth 1's trigger moves from every spec revision to the
  delta's close. R1136 — Depth 2 by the delta's reach, no longer only on
  demand through R1105.
- skills/review-artifact.md — one overall `Verdict:` plus one verdict line per
  pass, overall being the most severe.

**Restated** in the open/closed vocabulary — the obligation is unchanged, the
words `converging`, `status`, or `flip` are replaced: R0015 (entry condition),
R0016, R0017, R0087, R0478, R1152 (the test-only licence and the red-gate),
R0480, R0481, R1158 (the close, without the frontmatter flip), R0470 (the
precondition on the per-change stages), R0019's re-entry condition (carried by
the reopen step).

**Retired** — the row's own obligation is a status transition; where the row
also carried something that survives, the restated row carrying it is named:
R0014 (the definition of the `converging` status); R0018 (the exit transition
— its read-and-ruling survive through R0480 and R0481); R0019 (the re-entry
flip — its re-entry condition survives through the reopen step); R0020
(converging as a status interval distinct from a delta — the two are now one);
R0476 (the entry transition). Nothing else is retired by this document.

Unchanged and in force: R0084 (the interface contract the red-gate needs, no
vocabulary to change); R0492 and R0517 — the quality and skeptic passes stay
separate, and the number of sessions was never theirs to set; R1105 and R1137
as written until the store exists; R0535's exhaustive consequential class;
DEC-000170's two-tranche cap and claiming rule; DEC-000300's refusal and its
trigger; DEC-000360's substance.

## What this document does not decide

Dave's, one at a time when reached:

- Which published code-review standard is adopted; the search is queued for the
  Store package's Reviewer rows.
- Whether the Reviewer and Skeptic/Risk stay two role documents once the
  standard's rows land, or the skeptic pass becomes a section of one reader's
  schema. Until ruled, both role documents' rows are in force.
- Whether a project's spec files carry any frontmatter at all once `status` is
  gone (PRD OQ-3 keeps them as files; this document assumes `order` and
  selection keys only).
~~~

ACT 2 — the read. Write reviews/change-flow-read-5-20260905T233000Z.md in the
review-artifact schema as the document amends it: one overall `Verdict:` in
the header, most severe of the passes, and each pass section opening with a
verdict line of its own. The header line reads
"# Review: process/change-flow.md — cycle 5". Review the whole document at
the ACT 1 SHA.

- **Closure.** For each of the fourth read's F-1 through F-9, one line:
  closed (with the line in revision 5 that closes it) or open (with why). A
  finding closed by wording that introduces a new contradiction is open.
- **Continuity**, own verdict line. The closing section names obligations by
  representative row and says the Store package resolves each through the
  clusters artifact. For each named row, find its cluster (or confirm it is a
  singleton) and check that every row in that cluster is treated the same way
  the list says; a cluster member the body relies on but the list retires is
  a finding. Then: does any sentence contradict a decision in decisions/log.md
  the lists do not name?
- **Quality**, own verdict line, and **Skepticism**, own verdict line, as the
  third read framed them.

Two things this read decides that earlier reads did not. First, a verdict of
ready-with-findings is available and should be used if every remaining
finding is one the Store package would close by construction when it maps the
rows — say so per finding. Second, if you find nothing blocking, say so in one
line; a clean pass is a result.

Findings labelled defect, suggestion, or accepted risk, each with the line it
rests on, and severity blocking / non-blocking / observation. Do not edit
process/change-flow.md. Commit the review alone with the
message `reviews: change-flow read 5`. Push. Report both SHAs and the verdicts.
Then remove the worktree with `git worktree remove "$TMPDIR/fiducial-change-flow-r5"`
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
  git -C "$TMPDIR/fiducial-change-flow-r5" diff --stat origin/change-flow-r4..HEAD
  git -C "$TMPDIR/fiducial-change-flow-r5" log --oneline origin/main..HEAD
  grep -c '^## ' process/change-flow.md
  grep -c '^| \*\*' process/change-flow.md
} 2>&1 | tee "$TMPDIR/change-flow-r5-verify.log"
~~~

Expected: diff-stat against origin/change-flow-r4 names three files — this
directive and the review artifact as additions, process/change-flow.md as a
modification; log against origin/main shows exactly fifteen commits (twelve
already on change-flow-r4 plus the three this session lands, the directive
commit included); 7 `##` headings; 4 table rows beginning with a bold cell.

STOP CONDITIONS

Pinned to the reviewed ref 13ee4c7c4c5d969f21464fb452456da4ca60c471. Cannot execute as written: stop
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

    Land change-flow revision 5 and read the whole document — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
