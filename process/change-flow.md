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
