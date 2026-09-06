---
order: 40
role: [spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, copy-editor, critic]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Review Artifact

The shape of what a review emits. Written in the execution session that runs the
review, triaged in a decision session. This document is the form; the
obligations an agent performs when it runs a review or triages its findings are
rows in the store under topic `review-artifact-schema`.

## What this schema governs

It governs the artifact, not the review. Role documents govern the review —
what must be inspected and what must be reported. The unit is the read at a
delta's close: one read over one delta, one artifact, whatever the review
procedure.

Where a role or a policy names a required output, this is where it goes:

| Required by the role or policy | Field here |
|---|---|
| Sign-off; recommendation (the overall ship call) | `Verdict` |
| Required changes | entries marked `blocking` |
| Advisory items | entries marked `non-blocking` |
| Required follow-ups | the finding's `Fix` |
| Risks, verification gaps | `Consequence`, and `Not inspected` |
| Evidence inspected; scope reviewed | `Scope`, `Cross-checked` |
| What Dave should inspect | `Dave should inspect` |

The entry field is `Fix`, not `Recommendation`.

A per-entry log of agreements is not an artifact in this sense — its shape is
defined by the policy that mandates it, and the header block below would be
absurd applied per line.

The schema binds artifacts written after it lands. Existing artifacts are not
retrofitted: they are the review record of documents already agreed, and
rewriting a record of what happened to match a later format would be the drift
this repo exists to prevent.

## Filenames

A review artifact goes in `reviews/`, its filename beginning with the reviewed
document's stem, so a reader derives the artifact's path from the document's
path without looking it up. The discriminator after the stem follows the
repo-wide generated-filename convention.

Where the reviewed file sits in a subdirectory of `engagements/` or `roles/`,
its stem is `<parent-dir>-<basename>`; every other file's stem is its basename
without the extension. Where the stem already ends in a digit, the rule applies
unchanged and repeats; a special case would cost more than the repetition does.

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
Dave should inspect: <the few items that need his judgment, or omitted>
~~~

The header carries one overall `Verdict:` line, and each pass section opens with
its own `Verdict (<pass>):` line — continuity, quality, skepticism, and any
further dimension in force. Every verdict is `ready`, `ready-with-findings`, or
`changes-required`, and the overall verdict is the most severe of the pass
verdicts on that order. `ready` means ready for Dave's agreement; the value is
never the word `agreed`, because agreement is Dave's act, not the reviewer's.

`Cross-checked` and `Dave should inspect` are omit-if-none — a clean pass should
not have to write lines of `none`. `Baseline` is required where the artifact
reviews a range — a read over a delta's whole diff, or a reconciliation — and
names the revision the diff starts from; a review of one revision omits it. The
rest are required, `Not inspected` included: that one is required precisely
because omitting it is how an unbounded claim gets made by accident.

A pass that finds nothing, or that confirms a prior read's findings were fixed,
is this header and nothing else. No prose.

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

`Related` is omit-if-none; the other four entry fields are required.

`Evidence` distinguishing *verified by running* from *inferred by reading* is not
optional. An entry whose `Evidence` line cannot be filled in is an observation,
not a finding.

`Consequence` is the field that does the work. An entry that cannot state
concretely what goes wrong is an observation.

Order `blocking` entries by weight, heaviest first: the schema has one bucket for
a design hole and a wrong sentence, so the ordering is what carries the
difference.

## Prose

Permitted where judgment genuinely does not compress — a material disagreement
between reviewers, or a risk that needs an argument rather than an assertion. It
is not the default, and it never replaces the verdict line.

## What this document changes

Two things, against the schema as `skills/review-artifact.md` stated it at
fd54448.

The verdict rule is the one process/change-flow.md amended: one overall
`Verdict:` in the header, one per pass section, the overall being the most
severe. The source carried a single verdict for a single-pass read.

The `Prior cycle` field is dropped. It existed to point at the previous review
artifact for the same document, under a per-document cycle numbering that
retires with per-document review cycles (DEC-000380). Review attaches to a
delta, not to a document, so there is no predecessor artifact for the schema to
name.
