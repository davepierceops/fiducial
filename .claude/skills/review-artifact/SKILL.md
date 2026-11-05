---
name: review-artifact
description: "The form a review emits: one read over one delta, one artifact [R1396, R1408]."
---
<!-- fiducial:begin -->
# Process: Review Artifact

The form a review emits: one read over one delta, one artifact [R1396, R1408].

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
in the repo-wide generated-filename convention [R0196]. Over one document, the
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
`Cross-checked` and `The human should inspect` are omit-if-none; `Baseline` is
required where the artifact reviews a range — a delta's whole diff — and names
the revision the diff starts from, and a review of one revision omits it; the
rest are required, `Not inspected` included. A pass that finds nothing, or that
confirms a prior read's findings were fixed, is this header and nothing else.

## Findings

One entry per finding, after the header.

~~~markdown
## <finding id> — <blocking | non-blocking | observation>
Claim: <one sentence — what is wrong>
Location: <path:line, or section name>
Evidence: <what was checked; verified by running vs. inferred by reading>
Consequence: <what goes wrong, concretely>
Fix: <what would resolve it>
Related: <other finding ids that are the same defect elsewhere, if any>
~~~

`Related` is omit-if-none; the other four fields are required. An entry whose
`Evidence` cannot be filled in, or whose `Consequence` cannot state concretely
what goes wrong, is an observation rather than a finding. Order `blocking`
entries by weight, heaviest first. Write prose only where judgment does not
compress — a material disagreement between reviewers, or a risk needing an
argument — and never in place of a verdict line.

## Rules

Emit exactly one artifact in this schema per review — one read over one delta, one artifact — whatever the review procedure.

Carry one overall `Verdict:` line in a review artifact's header and one `Verdict (<pass>):` line at the head of each pass section; every verdict is `ready`, `ready-with-findings`, `not-run`, or `changes-required`, and the overall verdict is the most severe of the pass verdicts on that order; `not-run` is a planned pass that did not run. `ready` means ready for the human's approval, never that the document is approved.

Never rewrite an existing review artifact to match a later version of this schema; the schema binds artifacts written after it lands.

Where a review artifact names a defect class and lists its instances, rule on the class once and dispose the instances under that ruling; no instance is triaged on its own ahead of it.

Route a finding below the reviewed document's stage — a spec read raising an implementation question — to the loose-end tracker, where the next stage takes it up; it is not a blocking finding against the reviewed document and does not block the close.

A non-blocking finding's disposition at triage is file-and-land by default: it goes to the loose-end tracker and the delta lands. The human may raise a finding to blocking at triage, before the pull request merges; one raise buys one read over the diff since the reviewed revision. Nothing else reopens a delta.

A review artifact names every pass that was planned; a pass that did not run — a subagent killed by a usage cap, say — is recorded with why, and a missing verdict is never read as a clean one.
<!-- fiducial:end -->
