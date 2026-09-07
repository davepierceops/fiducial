---
order: 40
role: [spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, copy-editor, critic]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Review Artifact

The form a review emits: one read over one delta, one artifact [R1395a, R1396,
R1408].

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

A per-entry log of agreements is not an artifact in this sense; its shape
is set by the policy that mandates it.

A review artifact goes in `reviews/`, its filename beginning with the reviewed
document's stem and then the discriminator in the repo-wide generated-filename
convention. The stem of a file in a subdirectory of `engagements/` or `roles/` is
`<parent-dir>-<basename>`; every other file's is its basename without the
extension, and where it already ends in a digit the rule applies unchanged.

## Header

Every artifact opens with this block, clean pass or not.

~~~markdown
# Review: <document path> — <descriptor>-<timestamp>

Verdict: ready | ready-with-findings | changes-required
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

The header's `Verdict:` is the overall call and each pass section opens with its
own `Verdict (<pass>):` line [R1414]. `Cross-checked` and `The human should
inspect` are omit-if-none; `Baseline` is required where the artifact reviews a
range — a delta's whole diff, or a reconciliation — and names the revision the
diff starts from, and a review of one revision omits it; the rest are required,
`Not inspected` included. A pass that finds nothing, or that confirms a prior
read's findings were fixed, is this header and nothing else.

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
