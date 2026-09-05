---
order: 10
session: [decision, execution]
corpus: [software, methodology]
---

# Process: Change Flow

**Status of this draft:** revision 2, 2026-09-05, after the frontier read at
reviews/change-flow-read-20260905T195000Z.md and Dave's rulings on its
findings F-2, F-4, F-8, F-11. Gate: one frontier read over the diff since the
last read, then Dave's sign-off, recorded as a decision-log entry naming the
SHA. Rows are cited by register id until the store assigns ids; the Store
package maps them.

## The principle

**Review is charged once per delta, and a delta is whatever one reviewer can
read whole.**

A delta is the accumulated difference between a thing as it stands and the
thing as it will stand when the work is done. Review attaches to the delta at
its close — never to a document, never to an edit. A typo fix is a one-row
delta and closes in one commit. A rebuild is one delta too, if one reader can
read it whole; if not, it is more than one, and the reader is the one who says
so. What sets the depth of the review is the size and reach of the delta, not
the number of documents it touched.

This is the rule the corpus already stated twice in narrower forms — for spec
branches (DEC-000170: "the gate is charged once at reconciliation, not once
per edit") and for rules (DEC-000380: one intake act per row) — stated once,
for everything.

## Three kinds of thing change

Each has one delta shape and one closing act. This document adds no gate to
these; it states the ones that exist.

| What changes | The delta | Closed by | Who reads |
|---|---|---|---|
| **Rules** — rows in `rules/` | the proposed rows | **intake**: one commit | Context Quality Reviewer |
| **Process** — prose in `process/` | the edited document | **one frontier read** against the rows it cites, then Dave's sign-off, recorded in the decision log naming the SHA (DEC-000380) | a frontier session that did not draft it, then Dave |
| **Specs** — a project's PRD, TRD, acceptance criteria | a spec branch with commits on it | **reconciliation**: one read, one ruling, one pull request | Spec Reviewer, then Dave |
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
  and no pull request lands without one. There is no trivial-change exemption:
  what made small changes expensive was a cycle, and an agent reading a
  one-line diff is seconds, so nothing is bought by skipping it and DEC-000300
  refused the lane. The reviewer's rules are not written here: an established,
  published code-review standard is adopted whole and enters the store through
  intake as rows whose `source` names that external document. Until those rows
  land, the Reviewer role's rows (`roles/reviewer-agent.md` at store time) are
  in force; the intake commit that lands the standard retires them, each with
  `retired:` naming its successor, and conforms the human-review boundary's
  rows in the same commit.
- **Skepticism** — where is this lying to us? False confidence, mocked-boundary
  and live-integration gaps, config and deploy risk, release overclaims, over
  the whole evidence chain (R0488).

**Quality and skepticism are always two passes** (R0492, R0517): a change can
pass one and fail the other, so the second question is asked after the first
has been answered, and each pass carries its own verdict line. What the delta's
class decides is whether they are two *sessions*:

- **Routine** — one reader, one session; the skeptic pass follows the quality
  pass as a separate section over the same diff, no re-read.
- **Consequential** — two readers, two sessions. Two triggers, either one
  sufficient: the delta touches the commit-and-change-control policy's
  consequential class (R0534–R0547); or the reader finds the delta exceeds
  what one session can read whole and says so in the verdict, at which point a
  second session is summoned. When unsure, treat as consequential (R0536).

**Scan depth follows the delta's reach.** This changes R1105, R1136 and R1137,
which made Depths 2 and 3 available only on demand: on a spec delta's close,
Depth 1 (the spine) always runs (R1104); a delta whose diff touches a policy or
boundary document gets Depth 2 in the same read; Depth 3 over the methodology
is now intake's job and runs on the rules store, not on demand. A scan nobody
asked for is the point; a scan nobody knew to ask for was the defect.

**Dimensions are an open set.** The three above are the ones the corpus has
today. A new one — a reliability review, a security review, whatever the next
year shows is missing — is added by intake, not by editing this document: its
rules land as rows keyed `dimension: [security]` with the other keys naming
the delta kinds it applies to, and a read includes every dimension that has a
row matching the delta. The query is a selection over rows with `dimension`
set; the `--keys` listing DEC-000400 specifies is pending the Store and Tool
packages, and until it lands the intake session names the dimensions in force.

Two separations hold whatever the delta's size (R0462, R0463): whoever produced
the delta does not read it; whoever drafted a document does not gate it.

**A deep read, on demand, at any time.** Dave — or the Chief of Staff on his
behalf — may call for a full read of anything, at any point, whether or not a
delta is closing: every dimension, two sessions, continuity at its widest
reach, over the whole thing rather than a diff. It is a directive like any
other, with the object named (a spec, a project's code, the rules store); its
verdict is input to Dave. The Chief of Staff proposes one at milestone moments
without being asked; the row that grants it is keyed so it shows on the list of
things Dave can call for.

The read's output is a review artifact in the review-artifact schema, with one
verdict per pass. Findings are triaged by the decision session; blocking
findings reopen the delta, which then closes again with one more read over
the diff since the last read — not over the whole delta again. (Working rule;
it is revised if a reopened delta's second read ever misses a contradiction the
first read would have caught.)

## The spec lifecycle, restated

A spec has two states and no status field: its branch is **open** (has commits
the default branch does not) or **closed** (agreed; the default branch is the
version of record).

1. **Open.** A spec branch is cut, `spec/<tranche-slug>` (R0004). While it is
   open, Dave edits the spec freely with no per-edit gate (R0007); the Test
   Designer writes the spec's test suite against it and confirms the suite red
   on bad logic, not on an absent import (R0016, R1152); findings flow both
   ways through the decision session. Nothing is *implemented* against an open
   spec, and none of the per-change stages runs against one (DEC-000360,
   R0470: draft/in-review nothing; converging tests only; agreed
   implementation — the three values, with "converging" now meaning "open").
   At most two deltas are open at once, over disjoint spec territory; a
   document appearing in one open delta's diff may not appear in a second
   (R0012, R0013); nothing decomposes from an open spec (DEC-000170).
2. **Close.** When spec and tests cohere, one read over the whole diff plus
   the tests (the Spec Reviewer, R0480), then Dave reads that diff and rules
   once (R0481). The ruling is recorded in the decision log naming the
   reviewed SHA; the reconciliation pull request lands the branch. Agreement
   attaches to the version of record at that SHA (R0011).
3. **Reopen.** A revision of an agreed spec opens a new delta on a new branch
   and closes the same way. There is no smaller path: a one-line spec fix is a
   one-line delta, read in a minute.

What retires: the `converging` status and its two frontmatter transitions
(DEC-000360's mechanism, not its substance; R0476); the expedited and doc-only
paths; per-document cycle numbering and `last-reviewed` pointers (DEC-000380).

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
