---
name: "review-artifact"
description: "The form a review emits: one read over one delta, one artifact [R1396, R1408]."
---
<!-- fiducial:begin -->
# Process: Review Artifact

The form a review emits: one read over one delta, one artifact [R1396, R1408].

The artifact format applies to spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, copy-editor and critic in software and writing decision and execution sessions. The finding-classification instruction below applies to all roles in those sessions and corpora.

Where a role or a policy names a required output, this is where it goes:

| Required by the role or policy | Field here |
|---|---|
| Sign-off; recommendation (the overall ship call) | `Verdict` |
| Required changes | entries marked `blocking` |
| Advisory items | entries marked `non-blocking` |
| Required follow-ups | the finding's `Fix` |
| Risks, verification gaps | `Consequence`, and `Not inspected` |
| Evidence inspected; scope reviewed | `Scope`, `Cross-checked` |
| What the human should inspect | `the human should inspect` |

The entry field is `Fix`, not `Recommendation`.

A per-entry log of dispositions is not an artifact in this sense; its shape
is set by the policy that mandates it.

A review artifact goes in `reviews/`, named `<stem>-<descriptor>-<timestamp>.md`
using generation time in UTC as `<YYYYMMDD>T<HHMMSS>Z`. Over one document, the
stem is the document's: for a file in a subdirectory of `engagements/` or
`roles/`, `<parent-dir>-<basename>`; for every other file, its basename without
the extension, and where it already ends in a digit the rule applies unchanged.
Over a delta — a branch's whole diff — the stem is the delta's branch slug and
the descriptor is `read`: `reviews/<branch-slug>-read-<timestamp>.md`
(DEC-001450).

## Header

Every artifact opens with this block, clean pass or not.

~~~markdown
# Review: <document path, or the delta's branch> — <descriptor>-<timestamp>

Verdict: ready | ready-with-findings | not-run | changes-required
Reviewed: <path> @ <sha, short or full>
Baseline: <path> @ <sha, short or full>
Reviewer: <role, agent, or human>
Date: <YYYY-MM-DD>
Scope: <what was inspected>
Cross-checked: <other documents consulted for consistency, or omitted>
Not inspected: <stated explicitly — "nothing" is a claim, not a default>
Findings: <none | count by severity>
The human should inspect: <the few items that need his judgment, or omitted>
~~~

The header's `Verdict:` is the overall call and each pass section — quality,
skepticism, continuity — opens with its own `Verdict (<pass>):` line [R1414].
A pass that was planned and did not run has its section too: its line reads
`Verdict (<pass>): not-run`, followed by one line saying why [R1617].

For architect-agent, chief-of-staff, and the seven artifact-format roles above, when writing a review artifact:

The overall verdict is the most severe pass verdict: `ready`, `ready-with-findings`, `not-run`, then `changes-required`. `ready` means ready for human approval, not already approved.

`Cross-checked` and `The human should inspect` are omit-if-none; `Baseline` is
required where the artifact reviews a range — a delta's whole diff — and names
the revision the diff starts from, and a review of one revision omits it; the
rest are required, `Not inspected` included. A pass that finds nothing, or that
confirms a prior read's findings were fixed, is this header and nothing else.

## Findings

One entry per finding, after the header.

Flag only what you can demonstrate, cite the location, and label each finding defect, suggestion, or accepted risk.
A finding labeled accepted risk cites the recorded authorization to accept it.
Classification describes the kind of finding; the entry heading continues to
state its severity. Observations are not findings and omit Classification.

~~~markdown
## <finding id> — <blocking | non-blocking | observation>
Claim: <one sentence stating the finding or observation>
Classification: <defect | suggestion | accepted risk>
Location: <path:line, or section name>
Evidence: <what was checked; verified by running vs. inferred by reading>
Consequence: <what goes wrong, concretely>
Fix: <what would resolve it>
Related: <other finding ids that are the same defect elsewhere, if any>
~~~

`Related` is omit-if-none. `Classification` is required for findings and omitted
for observations. `Claim`, `Location`, `Evidence`, `Consequence` and `Fix` are
required. An entry whose
`Evidence` cannot be filled in, or whose `Consequence` cannot state concretely
what goes wrong, is an observation rather than a finding. Order `blocking`
entries by weight, heaviest first. Write prose only where judgment does not
compress — a material disagreement between reviewers, or a risk needing an
argument — and never in place of a verdict line.

## Rules

For each review, use the review-artifact skill to produce one artifact covering that read of the delta.

Apply a new review schema only to artifacts written after it lands.

When a review lists instances of a defect class, rule once on the class first, then apply that ruling to each instance.

Record every planned review pass. Mark unrun passes `not-run` with a reason, and treat a missing verdict as unverified.

### Definitions

**accepted risk** — Accepted risk is an explicit decision — the human's, or the release process's — to proceed despite a known gap.

**blocking** — A `blocking` gap is one the governing policies prohibit releasing with.
<!-- fiducial:end -->
