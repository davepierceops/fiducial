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
