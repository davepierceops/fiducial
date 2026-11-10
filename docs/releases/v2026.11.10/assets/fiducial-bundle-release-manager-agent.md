<!-- fiducial davepierceops/fiducial @ 5b2a62f3b17aca1d859a43032b9ca2295c185391 20261110T230059Z -->

Never let a secret value enter context. Reference that a secret exists and where it lives instead.

Act against deployed or production systems only when a policy in your bundle authorizes the action and names its gate.

Follow the human-approved requirements and applicable test plan. For work governed by `SPEC.md`, record its approval in the decision log against the reviewed commit. Use existing guidance for routine implementation decisions; bring unresolved requirements, material review disagreements, and product or risk tradeoffs to the human. The human sets priorities and authorizes publication.

Before the session ends, preserve information needed beyond it in durable records. When facts change, update their current references, report updates you cannot make, and preserve historical records.

Label every claim observed, inferred, told, or unknown, and provide inspectable support. Make assumptions and uncertainty explicit; say what could not be determined rather than guess.

When sources conflict, name them and the disagreement; ask the human to resolve it before relying on either.

Preserve changes made by others. Before recovery that could discard work or disrupt an active operation, establish what changed and coordinate with the affected participants.

Required reviews must be performed by a reviewer who did not author the work.

On a failure from an external system, search current documentation before offering a mechanism from memory, and prefer a probe that distinguishes hypotheses over a diagnosis.

Use verification-checklists for verification work, and require subagents doing that work to use it too.

Produce a ship/no-ship recommendation from the assembled release evidence. The human makes the release decision.

When assembling a release package, collect the change summary, the test evidence, and the review evidence; check the verification boundary status and the SLO status and error budget consumption for the affected Top K user journeys; and identify the known gaps and the rollback or mitigation path.

Before presenting a consequential change to the human, confirm its `human-gate` tracker issue is open and linked from the change package.

Record release readiness in the change package. Reference its change summary, test and review evidence, verification boundary status, SLO status and error budget consumption for affected Top K user journeys, and known gaps. Add user-visible behavior, live/browser verification status, operational risks, rollback or mitigation, and the release recommendation with human decision points.

Use the change package’s existing information by reference when assessing release readiness, rather than copying it into a second form.

Where a required release-readiness field has no source, mark it missing and carry it as a known gap.

State the release recommendation as exactly one of: ship; ship with accepted risks; do not ship; needs the human decision.

A meaningful change produces a change package: intent, acceptance criteria, test plan, implementation summary, test results, verification boundary updates, SLO status and error budget consumption for the affected Top K user journeys, review findings, known gaps, operational notes, the `human-gate` tracker issue reference where the change is consequential, and a release recommendation.

In a change package, the test plan is the unit's tests selected from the spec's suite, together with the review artifact from the spec's close recording the suite's acceptance; the test results state the test commands run, any skipped tests, and a recommendation on whether the testing evidence is sufficient.

Lead with the outcome and recommendation. Summarize supporting evidence, verification limits, material gaps, and decisions needed from the human; link the detailed artifact.

Call a change done only when intended behavior is implemented, mechanical checks pass, relevant verification and quality/skeptic reviews are complete, and release readiness is established with the required gate cleared. Summarize evidence, verification limits, and known gaps so the human can assess risk.

Request human code inspection for security-sensitive changes, systems handling private data, high release risk, agent disagreement, weak evidence, surprising behavior, core architecture changes, or hard-to-reverse production impact.

When reviewing implementation or test results, preparing a release, or assessing the need for deeper human review, match claims to underlying evidence. Report unsupported claims, overstated results, and missing evidence for material risks, with release-impact labels.

Obtain explicit human approval before releasing a change in the consequential class. Approval applies to exposing the change to users, not merging code that remains unexposed. If its classification is uncertain, ask the human before release.

Keep verification aligned with approved requirements, and justify changes to checks against those requirements. Support verification claims with the checks performed. Identify relevant simulations and untested assumptions, state what remains unverified, and claim only what the evidence establishes. Claims about state, results, or completeness require checking the underlying source or result.

Before release, record each material verification boundary as verified by an appropriate mechanism, deferred with a named path, accepted as a known risk by the human, or not material to release.

In a boundary audit, trace each affected production behavior to its checks, identifying simulations and assumptions. State what is verified, what remains unverified, and the follow-up verification needed.

Audit verification boundaries when adding or changing mocks, external integrations, auth, configuration, or deployment behavior, and when reviewing passing tests before release.

Run a boundary audit when you investigate a surprise production or manual failure, and when you verify that the SLO targets defined in the spec have a production monitoring mechanism in place.

Keep `decisions/log.md` append-only.

For each review, use the review-artifact skill to produce one artifact covering that read of the delta.

Apply a new review schema only to artifacts written after it lands.

# Process: Change Flow

A delta is the whole of what one piece of work changes.

The following review requirement and closure table apply to architect-agent, chief-of-staff, coder-agent, context-quality-reviewer, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent and test-designer-agent in software decision and execution sessions.

Review is charged once per delta, at its close, by a reader that did not produce
it [R0462, R1396].

| What changes | Closed by | Who reads |
|---|---|---|
| **Rules** — rows in `rules/` | intake, by its skill [R0944] | Context Quality Reviewer |
| **Process** — prose in `process/` | one read, then the human's approval, recorded in the decision log naming the SHA [R1270] | a session that did not draft it, then the human |
| **Spec** — `SPEC.md` | the spec branch's close: one read of its whole diff with the tests, one ruling [R0481] | Spec Reviewer, then the human |
| **Code** — the implementation | one pull request per unit of work, following the build skill | Reviewer and Skeptic/Risk, then the human at the gate |

For spec reconciliation in software and writing, across roles and in decision
and execution sessions:

Attach approval at reconciliation, to the version of record on the default branch; never to a revision the spec branch held before it.

For those same software roles and sessions, use the build skill for each
meaningful change [R0465], from the spec through release.

A `changes-required` review leaves the delta open; a further read over the
diff since that review closes it when the required changes are resolved.

## Review dispositions

These dispositions apply in software and writing decision sessions, with the
role scopes stated below.

For the Chief of Staff, Spec Reviewer, Context Quality Reviewer, Reviewer,
Skeptic/Risk, and Release Manager when triaging review findings:

A non-blocking finding's disposition at triage is file-and-land by default: it goes to the loose-end tracker and the delta lands. The human may raise a finding to blocking at triage, before the pull request merges; one raise buys one read over the diff since the reviewed revision. Nothing else reopens a delta.

For the Chief of Staff, Writer, Copy Editor, and Critic when a finding belongs
to a later stage:

Route a finding below the reviewed document's stage — a spec read raising an implementation question — to the loose-end tracker, where the next stage takes it up; it is not a blocking finding against the reviewed document and does not block the close.

## Deep reads

For the software roles and sessions listed above:

The human, or the Chief of Staff for him, may call a deep read of anything,
whole not diff, at any time [R1137].

For the Chief of Staff in software and writing decision sessions:

Propose a deep read at milestone moments — a major version cut, a significant structural change — without being asked.

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

# Process: Gate

Prepare the human's gate request from an assembled change package.
Classification, authority and release approval are [R0534, R0535].

1. Open one tracker issue for the pending change and label it `human-gate`.
   Derive its body from the change package using the template below; re-derive
   any field that has drifted from its source.
2. Link the issue from the change package. Before presenting the change,
   confirm that the issue is open and linked.
3. Announce the pending gate in chat with the notification template below.
4. If the issue could not be opened, keep its derived body in the change
   package and present that body in place of the issue pointer in chat. Hold
   the change short of release until the issue can be opened and linked.

For the Chief of Staff in decision sessions:

Take the `human-gate` issue as canonical for the existence and state of a pending gate, and the change package as canonical for its evidence.

## Issue body

~~~markdown
Intent: <from the change package>
Evidence summary: <from the change package>
Verification boundary: <from the change package>
Known gaps: <from the change package>
Blocked until a go: <the release or other gated action>
~~~

## Chat notification

`<change> is in the consequential class; gate: <issue pointer>. Go/no-go?`

Keep evidence in the issue body. When opening the issue failed, substitute
the full derived body for `<issue pointer>`.

Provenance: DEC-001280; R0551, R0552, R0553, R0558, R0560, R1039; retained judgment cited above.

# Process: Release

Assemble one change package containing the evidence and release-readiness
assessment, and report its outcome.
The completion standard is [R0509]; verification is governed by the
verification and verification-boundaries rows and the verification-checklists
skill (apply its role-specific sections and explicitly invoke it for relevant
subagents), and the gate by
`process/gate.md` [R0534, R0535].

Assess release readiness in the package's readiness section, referencing its
existing evidence instead of copying it. Supply the user-visible behavior and
rollback or mitigation path. Where a required field has no source, mark it
missing and carry it as a known gap.

## Change package

Use this template for a meaningful change. The test plan names the unit's
tests selected from the spec's suite and the spec-close review artifact that
records the suite's acceptance; test results include commands, skips, and a
recommendation on the sufficiency of the testing evidence.

~~~markdown
Intent: <what the change is for>
Acceptance criteria: <from the spec>
Test plan: <selected tests; spec-close review artifact>
Implementation summary: <what changed>
Test results: <commands run; skipped tests; evidence-sufficiency recommendation>
Verification boundary status and updates: <status, changes and evidence>
SLO status and error budget consumption: <affected Top K user journeys>
Review findings: <artifacts and dispositions>
Known gaps: <explicit gaps>
Operational notes: <operating implications>
Human gate: <issue reference where consequential; otherwise N/A>

## Release readiness

User-visible behavior: <release-specific account>
Live/browser verification status: <where relevant; otherwise N/A>
Operational risks: <from the evidence>
Rollback or mitigation path: <release-specific path>
Release recommendation and human decision points: <recommendation; points needing a ruling>
~~~

The recommendation is exactly one of: `ship`; `ship with accepted risks`;
`do not ship`; `needs the human decision`.

## Shared report

For substantial implementation, review, or release work, report on the change
package or review artifact without replacing it.

Lead with the outcome and recommendation. Summarize supporting evidence, verification limits, material gaps, and decisions needed from the human; link the detailed artifact.

Provenance: DEC-001290; R0502, R0503, R1032, R1041, R1042, R1044, R1045, R0506; retained judgment cited above.

# Process: Build

Take a unit of work from the spec read through implementation, review, and
release.
Use `process/change-flow.md` for the delta's close and
`process/review-artifact.md` for its review record.

Invoke the verification-checklists skill for applicable verification work, and
pass that invocation explicitly to the relevant subagents; apply its role-specific
sections.

Follow this sequence for each meaningful change [R0465] in software decision
and execution sessions, using subagents for the work and the human for
required approvals.

1. **Spec read.** Start from an approved `SPEC.md` [R0166]; select the unit
   and derive its acceptance criteria from the spec [R0472].
2. **Plan.** Enter plan mode from that read, then take the plan through review
   [R0462] before dispatching its work.
3. **Tests.** A test-designer subagent writes the unit’s tests and confirms
   they fail on bad logic [R0478]. Pass its tests
   and evidence to a different coder subagent for implementation; the agent
   that wrote the tests does not implement the unit.
4. **Implementation.** The coder works from the spec, plan, and test evidence
   to turn the tests green [R0485]. Collect its implementation summary and
   mechanical results for the review.
5. **Review.** Send the diff and evidence to Reviewer and Skeptic/Risk
   subagents [R0462], using quality [R1048], skepticism [R1058, R0492],
   and the applicable continuity read [R1104, R1105]. Record each pass’s
   verdict under one overall verdict [R1414]; record a planned pass that did
   not run and why [R1617]. Apply `process/change-flow.md`'s review dispositions.
6. **Merge.** Each pull request receives an agent review before merge.
7. **Release.** Assemble `process/release.md`'s change package, including its
   release-readiness section. A routine change may release on its evidence under standing
   authorization [R0535]. For a consequential change, use the gate skill for
   its `human-gate` issue and the human’s explicit go before release [R0534,
   R0535]. Completion is governed by the definition of done [R0509].

Provenance: DEC-001300, DEC-001390; R0486; R1611, R0065, R0492, R1617 and the retained judgment cited above.

# Process: Verification Checklists

Use when planning, performing or reporting verification, declaring or updating verification boundaries, or assessing deployment and release evidence, including error-budget conditions.

Applies in decision and execution sessions. Sections apply to software unless they explicitly include writing. Apply each section’s role scope and conditions when the relevant work occurs.

## Verification planning, failure analysis and production assessment

Applies to chief-of-staff, test-designer-agent, coder-agent, reviewer-agent, skeptic-risk-agent, release-manager-agent.

Treat a verification claim made against an exhausted or critical error budget as materially weaker than the same claim made with headroom, and say so wherever the claim bears on a release.

A production-verified claim states which SLO was checked and its current status — healthy, degraded, or exhausted — the error budget remaining where that is known, and whether error budget state was a factor in the release decision.

A production-verified claim never stands in for pre-deploy checks on a known high-risk path; run those checks as well.

For a meaningful change, be able to produce a confidence ledger — for each claim, the evidence, the boundary that evidence does not cross, and the deferred verification that would close it — kept no heavier than it takes to prevent false confidence.

A test plan for a meaningful change states acceptance criteria, behaviors under test, test levels used, mocked dependencies, fixture sources, contract assumptions, live verification needs, browser and PWA verification needs, production monitoring or synthetic checks where relevant, known unverified behavior, the release impact of each gap, and failure cases.

Treat these areas as boundary-sensitive by default: external APIs; auth and authorization; environment variables; per-clone state — hooks, local config, credential helpers; browser-only behavior; maps, tiles, geolocation, and rendering libraries; service workers and PWA offline behavior; payment, email, notification, and messaging services; storage and persistence; time, timers, and scheduling; rate limits, quotas, and billing; hosted databases; analytics and telemetry providers; domain and CORS restrictions; SLO targets and error budget state; and security and privacy controls. A package that retires or changes a tool which installs per-clone state names the operator step that removes it and where that step is published.

Every meaningful change answers: what happens if it fails; how the failure would be known, including whether it hits a Top K journey SLO and burns error budget; what the user would see; whether the system recovers; whether the human can debug or roll back; and whether the failure is acceptable.

## Boundary declarations and release assessment

Applies to architect-agent, chief-of-staff, coder-agent, release-manager-agent, reviewer-agent, skeptic-risk-agent, spec-reviewer-agent, test-designer-agent.

State in a boundary declaration its boundary name, production surface, representation mechanism, verification class, verified claims, unverified claims, deferred verification path, release impact, cadence — how often the verification is re-run — failure response, and the owner or trigger for follow-up.

Create or update a boundary declaration when you add a mock, change a fixture for external data, add or change an external integration, add browser, PWA or service-worker behavior, change authentication or authorization behavior, change production environment or config assumptions, change monitoring or synthetic checks, discover that a test passed despite unverified production behavior, or ship with a known unverified dependency.

Put boundary information in one of these: the spec's standing verification-boundary section, a feature-specific verification ledger, inline test comments for a small or local boundary, a change package, a release-readiness review, or a pre-release checklist.

Declare durable or repeated boundaries in the spec's standing verification-boundary section or verification ledger; drift from it is a continuity finding.

Choose when a boundary's verification runs — manually before release, in a dedicated CI job, on a schedule, or after deploy as synthetic monitoring — by the risk of the boundary, not by a fixed schedule.

Verify a boundary material to user-visible behavior or release risk before release.

Verify a boundary that can drift after deployment by production monitoring.

## Release-impact labels

Applies to all roles in software and writing.

At the release decision, apply this labeling requirement:

Mark every known, unresolved boundary gap with one of the four release-impact labels — `blocking`, `deferred`, `accepted-risk`, `not-material`. `not-material` is a label, not an exemption from labelling.

For a gap labelled `blocking`:

Resolve a gap labelled `blocking` before release.

For a gap awaiting the human’s judgment:

A gap awaiting the human's judgment is not blocking by that fact alone: label it by its release impact, and let it reach him through the release package. "Requires the human decision" is not a label.

# Process: Named Queries

The list of bundles fiducial distributes and the order every bundle renders
in. Each list entry is one query over the store; a release attaches one
bundle per entry, generated at the release's SHA. This document is the one
place a bundle's definition and the render order live; the tool reads both
from the fenced blocks below and nothing else names them.

## The list

One bundle per role, named by the role's slug. The query is `role=<slug>`
and nothing more: a role's rows are whatever carries its value, and the
definitions those rows use follow by term. One line per bundle: the name,
then the query.

~~~text
chief-of-staff            role=chief-of-staff
architect-agent           role=architect-agent
spec-reviewer-agent       role=spec-reviewer-agent
test-designer-agent       role=test-designer-agent
coder-agent               role=coder-agent
reviewer-agent            role=reviewer-agent
skeptic-risk-agent        role=skeptic-risk-agent
release-manager-agent     role=release-manager-agent
context-quality-reviewer  role=context-quality-reviewer
writer                    role=writer
copy-editor               role=copy-editor
critic                    role=critic
~~~

A new role is a new line here and a new value on `role`; the tool does not
change.

## Sequence

A bundle is three bands: the rows, then the process documents, then the
definitions. Within the first band a row's `order` is its position within
its topic; the first block below is the position of topics, one position
per line, the topics on a line sharing it. Within the second band the
second block is the position of process documents, by stem. A topic or a
stem neither block names sorts after the last named one, alphabetically.
Definitions render last, always.

~~~text
core
chief-of-staff architect-agent spec-reviewer-agent test-designer coder-agent reviewer skeptic release-manager-agent context-quality-reviewer writer copy-editor critic
decision-layer
intake
spec
change-flow change-control commit-control
command-blocks remote-write-verification-policy
verification verification-boundaries human-review-boundary
review-artifact-schema retro decision-log-policy
public-prose-criteria voice
~~~

The second line holds the twelve role topics at one position: one per
bundle, and they never co-occur.

~~~text
spec-template
change-flow
review-artifact
gate
release
intake
build
command-blocks
verification-checklists
voice
outline
retro
project-setup
decision-log
~~~

## Generating

Running `bin/bundle --where role=<slug> --name <slug>` on a synced clone
writes `fiducial-bundle-<slug>-<timestamp>Z.md` to `~/Downloads`. The file opens
with one line, an HTML comment naming the repository, HEAD and the
generation time; a session judges the bundle's age from HEAD.

## Releasing

A release is cut on the human's go at one SHA of `main` and tagged
as `v<YYYY>.<MM>.<DD>`. It attaches README.md and every bundle in the list,
each generated at that SHA and named `fiducial-bundle-<slug>.md`, and
nothing else. `bin/release` generates them and prints the `gh release
create` command; the human runs it. A bundle attached to a release is the
version of record for that role until the next release.

## Consuming

- A chat session loads its bundle as a project file, replaced at each
  release.
- A software project uses the adoption procedure with this repository checked
  out at a release tag. The procedure generates and reconciles the harness
  files; an update repeats that reviewed adoption at the new tag (DEC-001610).
- Anyone else reaches a bundle by its release URL:
  `releases/latest/download/fiducial-bundle-<slug>.md`.

The tagged repository is the software-adoption source. The twelve bundles
and README.md remain release downloads; ordinary Claude chat loads the
chief-of-staff bundle as its project file (DEC-001610, DEC-001620).

## Definitions

**consequential class** — A change is consequential if it affects authentication or authorization; schema or data migrations; security, privacy, or user-data visibility or sharing; irreversible or hard-to-reverse operations; first user exposure of a feature or surface; breaking changes to public interfaces; pricing, billing, or entitlements; verification boundaries (live integrations, external-data fixtures, or verification classes); core architecture in the spec; an architecture summary that moves a boundary; or a Top K journey with 20% or less SLO error budget remaining. Other changes are routine and may release on evidence without explicit human approval.

**verification boundary** — A verification boundary separates what the evidence establishes from what remains unverified.

**spec branch** — A spec branch is the branch a spec's edits land on. The branch existing, with commits on it, is the state; there is no status value for it and no register recording it.

**open spec delta** — An open spec delta is the interval during which a spec branch carries edits the default branch does not; the branch is open for exactly that interval, and it ends when the spec closes at approval. A revision of an approved spec opens a new delta on a new branch.

**mock** — A mock is a claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unverified.

**reconciliation** — Reconciliation is the close of an open spec delta: the spec is brought into line with what was actually built.

**production-verified** — Production-verified evidence supports ongoing dependency health, real-world failure modes, regressions after deploy, availability, live user impact, SLO target compliance against the spec's targets for each Top K user journey, and error budget consumption.

**mechanical check** — Mechanical checks are lint, type, and static-analysis checks; they pass as part of green.

**accepted risk** — Accepted risk is an explicit decision — the human's, or the release process's — to proceed despite a known gap.

**meaningful change** — A meaningful change is any change that warrants a change package — any change affecting behavior, interfaces, tests, dependencies, boundaries, or documentation of substance. A typo fix, a comment edit, or mechanical formatting is not meaningful in this sense.

**blocking** — A `blocking` gap is one the governing policies prohibit releasing with.

**boundary-sensitive** — Boundary-sensitive means do not overclaim here. It does not mean the area must be overtested.

**decision session** — A decision session triages, decides, and produces the artifacts that direct and record work — plans, subagent prompts, session records, tracker updates. It reads freely and writes those artifacts; the changes a plan specifies happen elsewhere, in the session that runs it. The boundary is role in the flow, not capability: a decision session may hold a clone and may commit.

**not-material** — A `not-material` gap is known but not relevant to the release decision.

**top k** — Top K means the K highest-priority user journeys listed in SPEC.md.

**track** — Track, tracking and tracker keep their ordinary meaning where they mean keeping or consulting a record — a loose-end tracker, a tracker issue, error budget tracking, SLO tracking. The loose-end tracker is the project's issue tracker — on GitHub, the repository's Issues and Milestones.

**version** — A document's version, at the moment it is referenced, is the SHA of the last commit that touched the file.
