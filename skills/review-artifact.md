---
status: in-review
last-reviewed: null
audience: [spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff, critic, human]
---

# Skill: Review Artifact

Review artifacts are written by execution sessions and triaged in decision
sessions.

## What this schema governs

It governs the **artifact** — the shape of what a review emits. Every review
procedure emits exactly one artifact in this shape per cycle. Role documents
govern the **review**: what must be inspected and what must be reported. Where a
role or a policy names a required output, this is where it goes:

| Required by the role / policy | Field here |
| --- | --- |
| Sign-off; Recommendation (the overall ship call) | `Verdict` |
| Required changes | entries marked `blocking` |
| Advisory items | entries marked `non-blocking` |
| Required follow-ups | per-finding `Fix` |
| Risks, verification gaps | `Consequence`, and `Not inspected` |
| Evidence inspected; Scope reviewed | `Scope`, `Cross-checked` |
| What Dave should inspect | `Dave should inspect` |

Note the entry field is `Fix`, not `Recommendation`.

The scope is every review cycle: one document, one cycle, one verdict. A
per-entry log of agreements is not an artifact in this sense — its shape is
defined by the policy that mandates it, and the header block below would be
absurd applied per line.

The schema governs artifacts written after it lands. **Existing artifacts are
not retrofitted** — they are the review record of documents already agreed, and
rewriting a record of what happened to match a later format would be the drift
this repo exists to prevent.

## Filenames

A review artifact is `reviews/<stem>-cycle-<n>.md`, where `<stem>` is the
reviewed document's basename without its extension and `<n>` is the cycle
number. The convention is mechanical on purpose: the path a reader needs is
derivable from the document path without looking it up. Where the stem already
ends in `-cycle` or a digit, apply the rule unchanged and let it repeat —
`reviews/spec-review-cycle-cycle-1.md`. A special case would cost more than the
repetition does.

A file under a subdirectory of engagements/ or roles/ has stem
`<parent-dir>-<basename>`; all others use `<basename>`.

On a rename or a split the cycle number restarts at 1, and `Prior cycle` names
the predecessor stem.

## Header

Every artifact opens with this block, clean pass or not:

```markdown
# Review: <document path> — cycle <n>

Verdict: ready | ready-with-findings | changes-required
Reviewed: <path> @ <sha, short or full>
Baseline: <path> @ <sha, short or full>
Reviewer: <role, agent, or human>
Date: <YYYY-MM-DD>
Scope: <what was inspected>
Cross-checked: <other documents consulted for consistency, or none>
Not inspected: <stated explicitly — "nothing" is a claim, not a default>
Findings: <none | count by severity>
Prior cycle: <path to the previous review artifact, or none>
Dave should inspect: <the few items that need his judgment, or none>
```

`Cross-checked`, `Prior cycle`, and `Dave should inspect` are **omit-if-none** —
a clean pass should not have to write lines of `none`. `Baseline` is
**required when the artifact reviews a range** — an exit gate over a
`converging` document, or a reconciliation — and names the revision the diff
starts from; a review of one revision omits it. The rest are required,
**including `Not inspected`**: that one is required precisely because omitting
it is how an unbounded claim gets made by accident.

`Verdict` is deliberately **not** the word `agreed`. `ready` means ready for
Dave's agreement.

A clean or confirmation pass — one that finds nothing, or that confirms a prior
cycle's fixes — is this header and nothing else. No prose.

## Findings

One entry per finding, after the header:

```markdown
## <finding id> — <blocking | non-blocking | observation>
Claim: <one sentence — what is wrong>
Location: <path:line, or section name>
Evidence: <what was checked; verified by running vs. inferred by reading>
Consequence: <what goes wrong, concretely>
Fix: <what would resolve it>
Related: <other finding ids that are the same defect elsewhere, if any>
```

`Related` is **omit-if-none**; the other four entry fields are required.

`Evidence` distinguishing *verified by running* from *inferred by reading* is
not optional. A finding whose evidence line cannot be filled in is an
observation, not a finding.

`Consequence` is the field that does the work. If you cannot state concretely
what goes wrong, the entry is an observation.

Order `blocking` entries by weight — the schema has one bucket for a design
hole and a wrong sentence, so the ordering is what carries the difference.

## Prose

Permitted where judgment genuinely does not compress — a material disagreement
between reviewers, or a risk that needs an argument rather than an assertion.
It is not the default, and it never replaces the verdict line.
