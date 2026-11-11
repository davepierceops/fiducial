<!-- fiducial davepierceops/fiducial @ a8d87bc95afed9f5ac8b54fe2c8863013ce10265 20261111T041154Z -->

Never let a secret value enter context. Reference that a secret exists and where it lives instead.

Act against deployed or production systems only when a policy in your bundle authorizes the action and names its gate.

Follow the human-approved requirements and applicable test plan. For work governed by `SPEC.md`, record its approval in the decision log against the reviewed commit. Use existing guidance for routine implementation decisions; bring unresolved requirements, material review disagreements, and product or risk tradeoffs to the human. The human sets priorities and authorizes publication.

Before the session ends, preserve information needed beyond it in durable records. When facts change, update their current references, report updates you cannot make, and preserve historical records.

Label every claim observed, inferred, told, or unknown, and provide inspectable support. Make assumptions and uncertainty explicit; say what could not be determined rather than guess.

When sources conflict, name them and the disagreement; ask the human to resolve it before relying on either.

Required reviews must be performed by a reviewer who did not author the work.

On a failure from an external system, search current documentation before offering a mechanism from memory, and prefer a probe that distinguishes hypotheses over a diagnosis.

Before composing a command block or execution block, invoke the command-blocks skill; pass that explicit invocation to any subagent composing one. Ordinary internal tool calls do not trigger it.

Use verification-checklists for verification work, and require subagents doing that work to use it too.

Request human code inspection for security-sensitive changes, systems handling private data, high release risk, agent disagreement, weak evidence, surprising behavior, core architecture changes, or hard-to-reverse production impact.

Ask the most important question first, one at a time. Give enough context to answer, recommend an option consistent with prior decisions, and use yes/no when suitable.

Lead with the point. Be concise, preserve important detail, and prefer bullets to paragraphs.

Flag consequences that could change the human’s decision before acting. Keep the explanation concise.

Carry out clear, authorized work without asking for confirmation.

Before proposing a policy decision, check `decisions/log.md` for relevant prior decisions and cite them.

Use frontier for canonical text, review gates, and costly errors that are hard to detect; solid for spec-based implementation and routine review; cheap for mechanical, verifiable work.

Cite a row by its ID in square brackets only if it covers every role, session, and corpus of the citing row.

For a meaningful change, produce a per-change architecture summary naming affected components, external dependencies, boundary changes, risk notes, and testing implications.

Obtain explicit human approval before releasing a change in the consequential class. Approval applies to exposing the change to users, not merging code that remains unexposed. If its classification is uncertain, ask the human before release.

Open one `human-gate` tracker issue for a change when it is ready for the gate. The issue is the canonical record that the gate is pending, one issue per pending change.

Derive the `human-gate` issue from the change package using the gate template, and keep it consistent with that source.

Announce pending gates in chat using the gate notification template. If the issue could not be opened, include its derived body instead of the issue link.

Where the `human-gate` issue could not be opened, hold the change short of release until the issue is opened and linked, and keep the record of the pending gate in the change package until it can be.

Label every pending gate `human-gate`, the same label in every project, so every pending gate can be queried in one place across repositories.

Before work starts, document human-owned acceptance criteria derived from the spec. The Spec Reviewer’s gate applies only to specs.

To close a spec branch, present the reviewed diff for one human ruling approving the spec and accepting its tests as red-gate evidence. Record that ruling and the reviewed SHA in the decision log.

Run quality and skepticism as separate passes, each with its own verdict.

Keep the spec and tests provisional while developing them together. Finalize them only when every testable spec claim has a test asserting it and every test asserts something the spec states.

Bring the spec into line with what was actually built before closing an open spec delta.

Keep verification aligned with approved requirements, and justify changes to checks against those requirements. Support verification claims with the checks performed. Identify relevant simulations and untested assumptions, state what remains unverified, and claim only what the evidence establishes. Claims about state, results, or completeness require checking the underlying source or result.

Keep `decisions/log.md` append-only.

One decision per entry.

To change or reverse a recorded decision, append an entry whose `Supersedes:` names the old decision’s ID.

Ground every retro in concrete evidence from the conversation it covers.

Capture new or materially changed techniques, workflows, beliefs, and engineering practices that transfer beyond the session. Omit nontransferable implementation details and repeated methodology. State when there are no qualifying insights.

Base a retro on the conversation it covers and relevant project evidence.

Submit methodology changes proposed by a retro or synthesis as findings: rule changes go through intake; process changes require a frontier review and human sign-off.

For each review, use the review-artifact skill to produce one artifact covering that read of the delta.

Apply a new review schema only to artifacts written after it lands.

When a review lists instances of a defect class, rule once on the class first, then apply that ruling to each instance.

Record every planned review pass. Mark unrun passes `not-run` with a reason, and treat a missing verdict as unverified.

# Process: Spec Template

The form of `SPEC.md`, one per project: what is being built, why, how, and
when it is done. The Chief of Staff drafts it with the human by interview; the
Architect drafts its design section; a Spec Reviewer reads it before the human
approves it, and it is in force only from that approval [R0166]. A unit's
acceptance criteria derive from it [R0472]. Keep each section short.

1. **Problem and intent** — the problem, who has it, and why it is worth building
   now.
2. **Users and use cases** — who uses this and the concrete situations in which
   they do.
3. **User journeys** — the Top K journeys, each with its actor, its trigger, the
   sequence of actions and system responses, and the expected outcome.
4. **Goals and non-goals** — functional goals as concrete outcomes rather than
   feature lists; non-functional goals for each dimension — performance,
   reliability, scalability, security, maintainability, usability,
   observability, portability and compatibility, compliance — or `N/A` where the
   dimension is not a constraint; then the non-goals. An exclusion specific to
   one non-functional dimension is a note inside that dimension, not a non-goal.
5. **User outcomes and measurement** — the signals, quantitative or qualitative,
   confirming the change produced real user value: the metric or signal, the
   baseline where known, and the mechanism observing it — telemetry, user
   feedback, manual review. The definition of done gates correctness; this does
   not.
6. **Definition of done** — the acceptance criteria: the written conditions the
   work must meet to be accepted, concrete enough to derive test cases from.
   They may live here or in the unit's own artifact, and derive from this
   document either way.
7. **Design** — what the Architect's design obligations require [R0863]: the
   system's structure and the implementation approach; its components and the
   interfaces between them; its external dependencies; the failure modes it is
   likely to have; the NFR dimensions of section 4 as concrete technical
   targets, or `N/A`; and its deployment assumptions, including whether deploy
   and release are separate events. Two subsections are standing:
   - **User journeys and SLOs** — for each Top K journey of section 3, the SLO,
     the measurement mechanism, and the alerting threshold; a journey with no
     SLO is named unverified and recorded as an open question.
   - **Verification boundaries** — for each material standing boundary where
     the system meets what it does not control, and for each per-change
     boundary movement made permanent: the production surface; how it is
     represented — live, contract, mock, or assumed; its evidence class; the
     deferred-verification path, if any.
   Per-change technical design lives in the per-change architecture summary
   [R0862b], not here.
8. **Risk tolerance** — what risk is acceptable for this product and what is not;
   it feeds the release gate and the consequential-change classification.
9. **Open questions** — product and technical, each naming what would resolve it.

## Skeleton

~~~markdown
---
audience: [human]
---

# SPEC: <project name>

## 1. Problem and intent
## 2. Users and use cases
## 3. User journeys
## 4. Goals and non-goals
### Functional goals
### Non-functional goals
### Non-goals
## 5. User outcomes and measurement
## 6. Definition of done
## 7. Design
### User journeys and SLOs
### Verification boundaries
## 8. Risk tolerance
## 9. Open questions
~~~

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

# Process: Intake

Carry a proposed change to governed context from proposal through review and
landing.
The judgment governing the proposal and its ruling is [R0166, R0462]; the
intake rubric is [R0264, R0266, R1621].

For chief-of-staff and coder-agent in software and writing decision and execution sessions, when creating or changing a vendor-specific artifact:

A durable rule lives in the store, never only in vendor tooling. An adapter is derived from it: update the store first, keep the adapter short, note every deliberate deviation.

The intake steps below apply to chief-of-staff and context-quality-reviewer in software and writing decision and execution sessions.

1. **Proposal.** Collect the proposed wording or diff, its reason and evidence,
   and the affected rows or process documents.
2. **Candidate.** Create an `intake/<proposal-slug>` branch and apply the
   candidate change there. This is the branch observable used by R0934's
   governed-path hook.
3. **Review.** Give the candidate diff and proposal to a Context Quality
   Reviewer subagent, using the rubric cited above and the separation in
   [R0462]. For a process delta, use the process read and sign-off path
   [R1270]. The reviewer writes the artifact in
   `process/review-artifact.md`'s form.
4. **Disposition.** Bring the proposal and artifact to the human for any
   outstanding ruling [R0166]. Apply the review dispositions in
   `process/change-flow.md`. Record each intake in its review
   artifact: the changes it lands, or the candidates refused and
   the rows against which they were refused.
5. **Landing.** Commit the approved change and its intake artifact on the
   intake branch, push plainly, and open the pull request. At merge, the
   decision session appends the ruling by `process/decision-log.md`; report
   the landed changes or refusal with the read-back evidence [R0172].

Provenance: DEC-001300, DEC-001320; R0944, R0934; retained judgment cited above.

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

# Process: Command Blocks

Use before composing human-run shell commands or instructions for another agent session; ordinary internal tool calls do not trigger this skill.

Applies to chief-of-staff in decision and execution sessions, for software and writing.

## Compose and hand over the block

A paste block is copied whole and pasted whole, without assembly. There are two kinds. A command block contains shell commands the human runs as given, not agent instructions; describe it as “run,” not “executed.” An execution block contains instructions an agent session carries out, not shell commands.

A block runs verbatim as pasted, with no manual step inside the fence: a manual step goes in prose outside it.

A command producing evidence captures its output to a named file with `tee` or equivalent, and the block or its surrounding instruction names the path; where a block's output is consumed in the moment and never cited, say so where the block is defined.

Name the remote and the ref in every sync or remote command a block runs, rather than leaning on branch-upstream configuration or an implied default. `origin` counts: it is a remote name.

Nothing downstream acts on the tree a sync produced until that sync's exit status has been checked; a bad sync fails loudly, with a non-zero exit.

A block pushes a branch, never the default branch; the decision session merges that branch through a pull request.

A block renders copyable whole in the surface that delivers it, with that surface's copy control intact; avoid constructs known to break the surface in use — a heredoc (`<<'EOF'`) suppresses the desktop copy control, so a multi-paragraph commit message is written as repeated `-m` flags.

Fence a block nested inside a paste block with `~~~`, preceded by a one-line fence note stating that the inner fence is `~~~` and why.

Where a human must relay output between blocks, send one block per turn: wait for the output, then compose the next.

A block carries no construct that can end the shell it is pasted into — `exit`, `exec`, `logout`, `|| { …; exit; }`, and `set -e` are known instances, not the extent of the rule; guard a precondition by branching (`if…elif…else…fi`) instead, so a failed check prints and the block ends without ending the session.

One purpose per block, and no placeholders in it: ask an unknown value as a question above the block rather than leaving a token for the reader to substitute.

Before handing over a block: every command in it is valid and non-harmful, and re-running it compounds no damage; it has been run end-to-end against a local stand-in for the remote, guard and re-run paths included, with any substituted value bound; its expected output is stated in one line below it — what was observed in the environment the block will run in, or qualitatively, what to look for, with no number — and its blast radius above it where it is destructive.

Write an execution block so the executor needs only the block and the repository, with no dependency on the conversation that produced it.

When handing off an execution block, put the block first, with no preceding prose.

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

# Process: Retro

Run a retro when the human asks for one.

A retro is `retro-<timestamp>.md`, a synthesis `retro-synthesis-<timestamp>.md`,
the timestamp taken at generation time as `<YYYYMMDD>T<HHMMSS>Z`. Match a filename
against those two forms only to tell one from the other; the frontmatter is a
retro's canonical identity. Retros live in the project's own repo at `retros/`.
Its inputs are R1244's; its outputs land by the last step below.

A project synthesis runs over one project's `retros/` directory and writes into
it under the synthesis filename form, overwriting no source retro; its header
carries a `covers:` list naming every retro it read. The next synthesis computes
its input set by comparing earlier syntheses' `covers:` lists against that
directory's files matching the retro filename form, and states the count it read.
A cross-project synthesis concatenates the relevant `retros/` directories.

## The schema

~~~markdown
---
project: <project slug>
date: <YYYY-MM-DD; the session's last interaction>
generated: <YYYYMMDDTHHMMSSZ; when this retro was written>
source: <conversation pointer: title, URL, or export filename; null if none>
---

# Retro — <project> — <date>

## Context
<one paragraph: what the conversation was about, what was attempted>

## Evidence
<numbered, concrete observations of what happened; quotes or close
paraphrases of pivotal moments; no interpretation here; a correction the
human made inside the session belongs here>

## Interpretation
<what the evidence suggests; each item references the evidence numbers
it rests on>

## Recurring preferences
<preferences the human stated in this and earlier sessions, with evidence
of where they were expressed; empty-with-a-statement if none>

## Durable insights
<techniques, workflow changes, belief changes that transfer beyond this
session; empty-with-a-statement if none>

## Questions for follow-up
<problems worth investigating, with supporting evidence and unresolved
questions; empty-with-a-statement if none>
~~~

`date:` is the session's last interaction, taken from the last dated artifact the
session touched as recorded in the local tree — a merge commit, a commit, a
review artifact. Where the session touched none, take it from the `source:`
pointer; where `source:` is null too, `generated:` stands in and the retro states
the substitution. Where the two disagree, both are correct and both are stated.

## Landing

The retro lands itself, and a synthesis lands the same way (DEC-001260). The
last step commits `retros/retro-<timestamp>.md` on a branch, pushes, opens the
pull request, merges it as a routine change, and reads main back: the
merge commit's SHA, fetched, is the evidence the retro landed [R0172].

# Process: Project Setup

An adoption precondition is something that must be true about a repository
before the methodology governs work in it. These live in the forge's
configuration and the agent runner's, outside git, where no hook can enforce
them: the human confirms them once per repository, before the decision session
begins work in it. The Chief of Staff confirms they hold, once per session, and
says so; report one that does not rather than working around it.

1. **Branch protection on the default branch**, in the forge's configuration: no
   force-push; no branch deletion; changes land only through a pull request; no
   bypass, including for administrators. The last carries the others, and it is
   what makes "agents may push and merge" safe to say. Where the forge cannot
   enforce it — a private repository under GitHub Free refuses branch
   protection — the fallback is the second precondition alone plus every
   landing by pull request, never a push to the default branch, recorded in the
   project's decision log as an accepted-risk entry naming the plan that would
   restore the forge layer; the entry is re-examined when the repository moves
   to one [R0564].
2. **A force-push deny in the agent runner** [R0564], holding in every permission
   mode, including the modes that otherwise skip prompting.

# Process: Decision Log

Each project keeps one log at `decisions/log.md`, and the methodology repo keeps
its own for methodology decisions. An entry takes this form, and carries no
author field:

```markdown
## DEC-000070 — <short title>
Date: <YYYY-MM-DD>
Decision: <the ruling, one or two sentences>
Context: <the problem it settled, briefly>
Supersedes: DEC-000030   (omit if none)
```

IDs are `DEC-NNNNNN`, running in steps of ten from `DEC-000010`, unique within the
log and never reused. Take the last entry's number and add ten; append-only
guarantees that the last entry holds the highest ID [R0583, R0592, R1603].

Entries are appended by the decision session at merge, from the landed work's
report, and ids are allocated then — never by the subagent that did the work —
so concurrent packages never take the same id.

Supersession is whole-entry: a new entry whose `Supersedes:` names an old one
replaces all of it, so where the old entry carried several rulings the new one
restates every ruling that survives. A ruling the new entry does not restate is
gone.

Where two entries land on the same number, renumber the later ones by plus one
within the gap — `DEC-000410` to `DEC-000411`, `DEC-000412` — never by another
ten. That renumbering is the one edit the append-only rule admits, and it changes
a number, never a decision.

# Process: Adopt

Reconcile the store's current harness context into a repository, including a
repository already using fiducial; use the same procedure for upgrades.
The source of truth and reconciliation ruling are DEC-001630; project
preconditions are in `project-setup`, review separation is [R0462], and gate
classification and authority are [R0534, R0535].

1. **Prepare without changing the target.** Read the target's spec, decisions,
   and `project-setup` preconditions. Record the store SHA and dirty diff, target
   SHA, environment and egress boundary. Extract the single `python` fence below
   to a temporary `adopt.py` (Python 3.11+). Run `python3 adopt.py prepare STORE
   TARGET STAGE`, with absolute paths and a new staging directory outside both
   repositories. This inventories both layouts, including nested `AGENTS.md`
   and `AGENTS.override.md`, stages `--emit claude-code` and `--emit codex`, and
   writes `plan.json` and a proposed `candidate/` tree. Nothing is installed.
2. **Independent contradiction read.** Give a subagent that wrote none of the
   candidate the complete inventory, both staging trees, the candidate diff,
   and relevant target decisions/spec. It reads every inventoried file, including
   nested overrides (which may shadow root instructions), `.codex/config.toml`,
   settings, hooks, rules, agents and skills. Report contradictions by existing
   file/line and staged file/line, their consequence, and proposed disposition;
   do not infer compatibility from a mechanical merge. Its ordinary review
   artifact uses `review-artifact`. Also write `review.json` with `plan_sha256`
   (SHA256 of `plan.json` bytes), `reviewer`, and `findings`: an array of objects
   with unique `id`, `file`, positive integer `line`, `staged_file`, positive
   integer `staged_line`, and `claim`. An empty array explicitly means no
   contradictions found. A planned read that did not run remains a gap [R1617].
3. **Human rulings before append.** Present that report and complete candidate
   diff. For an exact removal/replacement of legacy instructions, prepare a JSON
   array of `{ "path": "CLAUDE.md", "before": "exact old text", "after": "replacement" }`
   edits, then re-run prepare in a new stage with that file as its fourth argument.
   Each `before` must match exactly once. The new plan must receive an independent
   read too. Structural conflicts (an occupied agent or hook name, incompatible
   frontmatter, malformed ownership, edited managed content) require a concrete
   human resolution and a fresh prepare; the helper never guesses. The human
   rules on every contradiction, even one accepted as a risk. Record the actual
   rulings, not an agent's proposed ruling, in `approval.json`: `plan_sha256`,
   `review_sha256` (SHA256 of `review.json` bytes), `human` (name), `go`: `true`,
   `gate` (issue reference, or `routine` when so classified), and `rulings`
   (finding-id to nonempty ruling text). For a consequential adoption, invoke
   `gate` with this package before installation. A file saying `go` records the
   human's response; it cannot supply that response. The first real Illuminait
   run uses this gate, with the report brought to the human before append.
4. **Create/append.** After those rulings, run `python3 adopt.py apply STAGE
   REVIEW_JSON APPROVAL_JSON`. It rechecks the inventory, writes missing files,
   and replaces only owned material. Use `python3 adopt.py labels OWNER/REPO`
   to create missing `human-gate` and the four release-impact labels defined in
   `process/verification-checklists.md`;
   existing label metadata is preserved. Read the labels back. The labels command
   touches GitHub, and is run only within the same authorization as installation.
   No command here commits, pushes, merges, applies infrastructure or destroys it.
5. **Evidence and landing.** The helper saves the inventory, independent read,
   rulings, changed paths, and verification boundary in the target's
   `docs/fiducial-adoption-<timestamp>.md`. Add environment, store/target SHAs,
   dirty source diff, forge-label read-back, project-setup confirmation, and
   actual gate decision to that report. Preserve its timestamp and content when
   a repeat run has no changes; the helper then writes no new report. Inspect the
   complete diff and repeat prepare/apply in a stand-in to establish no diff on
   rerun. Append the adoption ruling to target `decisions/log.md` through
   `decision-log`; remove a superseded `.fiducial/` tree only when the human has
   explicitly approved its removal, recording the removed pin. Open the target's
   own PR; retain a report copy in fiducial `reviews/`. Landing uses `release` and
   the human's merge decision. Keep Claude Code loading **contract-verified**
   until the human opens a fresh session at that target and runs `/context`;
   give him a pasteable command block with the real target path and expected
   output: the repository's `CLAUDE.md` listed as a loaded instruction source.
   Record the observed line when supplied. Codex hook trust is also a live
   boundary; emitted files alone do not prove enforcement.

## Ownership and deterministic create/append

The executable procedure below is part of this skill, not a separately installed
runtime. Tests extract and execute this fence. `.claude/fiducial-ownership.json`
records ownership for both layouts. Markdown uses `<!-- fiducial:begin -->` and
`<!-- fiducial:end -->` as whole lines outside code fences; YAML frontmatter
stays first and is replaced only when owned and unchanged. JSON uses recorded
key/list contributions, never HTML comments: unrelated values and pre-existing
identical entries remain the repository's. Generated TOML agents and executable
hooks use exact file hashes; a collision or later local edit is refused rather
than concatenating invalid configuration or displacing a shebang. An existing
Markdown or JSON file keeps its permissions; a new file takes the generated
ones. Upgrades remove obsolete owned contributions; ambiguous removals need a
human resolution.
Keep the manifest in the adoption PR. Work on an idle branch: checks protect
against changes since review, but installation is not a transaction against a
concurrent editor or a filesystem failure; inspect and revert the adoption diff
if an I/O failure interrupts it.

```python
import copy
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

BEGIN = "<!-- fiducial:begin -->"
END = "<!-- fiducial:end -->"
MANIFEST = ".claude/fiducial-ownership.json"
LAYOUTS = (".claude", ".codex", ".agents")
LABELS = ("human-gate", "blocking", "deferred", "accepted-risk", "not-material")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def safe(root, name):
    parts = pathlib.PurePosixPath(name).parts
    require(parts and not name.startswith("/") and all(p not in ("..", ".git") for p in parts),
            "unsafe path: " + name)
    path = root
    for index, part in enumerate(parts):
        path = path / part
        require(not path.is_symlink(), "symlink: " + str(path))
        require(index == len(parts) - 1 or not path.exists() or path.is_dir(),
                "parent is not a directory: " + str(path))
    require(path.resolve().is_relative_to(root.resolve()), "path escapes target")
    return path


def inventory(root):
    result = {}
    for base, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d != ".git")
        for name in sorted(files + [d for d in dirs if (pathlib.Path(base) / d).is_symlink()]):
            path = pathlib.Path(base) / name
            rel = path.relative_to(root).as_posix()
            if rel.split("/")[0] in LAYOUTS or name in ("CLAUDE.md", "AGENTS.md", "AGENTS.override.md"):
                safe(root, rel)
                require(path.is_file(), "not a regular file: " + rel)
                result[rel] = {"sha256": digest(path.read_bytes()),
                               "mode": path.stat().st_mode & 0o777}
    return result


def frontmatter(text):
    if not re.match(r"^---\r?\n", text):
        return "", text
    match = re.match(r"^---\r?\n.*?\r?\n---\r?\n", text, re.S)
    require(match is not None, "unterminated frontmatter")
    return text[:match.end()], text[match.end():]


def section(text):
    # Ignore examples, including this very skill's embedded marker strings.
    marks, offset, fence = [], 0, None
    for line in text.splitlines(keepends=True):
        bare = line.rstrip("\r\n")
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", bare)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            fence = match[1]
        elif bare in (BEGIN, END):
            marks.append((bare, offset, offset + len(line)))
        offset += len(line)
    require(not fence, "unterminated code fence")
    require(not marks or [m[0] for m in marks] == [BEGIN, END], "ambiguous fiducial markers")
    return (marks[0][1], marks[1][2]) if marks else None


def markdown(current, wanted, old):
    header, body = frontmatter(current)
    bounds = section(body)
    if old:
        require(header == old["header"], "managed frontmatter edited")
        require(bounds and digest(body[bounds[0]:bounds[1]].encode()) == old["section"],
                "managed prose edited or missing")
    else:
        require(not bounds, "untracked fiducial markers")
    if wanted is None:
        body = body[:bounds[0]] + body[bounds[1]:]
        require(not header or not body.strip(), "shared frontmatter retirement needs a ruling")
        return (None if not body.strip() else body), None
    new_header, new_body = frontmatter(wanted)
    owns_header = old["owns_header"] if old else not current
    require(header == new_header or owns_header, "frontmatter collision")
    block = BEGIN + "\n" + new_body.strip("\n") + "\n" + END + "\n"
    require(section(block) == (0, len(block)), "generated prose has conflicting markers or fence")
    if bounds:
        body = body[:bounds[0]] + block + body[bounds[1]:]
    else:
        body += ("\n" if body and not body.endswith("\n") else "") + block
    return new_header + body, {"kind": "markdown", "header": new_header,
                              "owns_header": owns_header, "section": digest(block.encode())}


def json_merge(current, wanted, old):
    data = json.loads(current or "{}")
    require(isinstance(data, dict), "JSON root must be an object")
    before = copy.deepcopy(data)
    for kind, keys, value in (old or {}).get("contributions", []):
        parent = data
        for key in keys[:-1]:
            require(isinstance(parent, dict) and key in parent, "owned JSON path missing")
            parent = parent[key]
        key = keys[-1]
        require(isinstance(parent, dict) and key in parent, "owned JSON value missing")
        if kind == "item":
            require(isinstance(parent[key], list) and parent[key].count(value) == 1,
                    "owned JSON list contribution edited")
            parent[key].remove(value)
        else:
            require(parent[key] == value, "owned JSON scalar edited")
            del parent[key]
    contributions = []
    def add(target, source, keys):
        require(isinstance(source, dict), "generated JSON root must be an object")
        for key, value in source.items():
            path = keys + [key]
            if isinstance(value, dict):
                target.setdefault(key, {})
                require(isinstance(target[key], dict), "JSON object collision: " + str(path))
                add(target[key], value, path)
            elif isinstance(value, list):
                target.setdefault(key, [])
                require(isinstance(target[key], list), "JSON list collision: " + str(path))
                for item in value:
                    if item not in target[key]:
                        target[key].append(item)
                        contributions.append(["item", path, item])
            elif key in target:
                require(target[key] == value, "JSON scalar collision: " + str(path))
            else:
                target[key] = value
                contributions.append(["value", path, value])
    if wanted is not None:
        add(data, json.loads(wanted), [])
    text = current if before == data and current else encoded(data).decode()
    state = {"kind": "json", "contributions": contributions} if wanted is not None else None
    return text, state


def build_plan(target, staged, edits=()):
    snapshot = inventory(target)
    manifest_path = safe(target, MANIFEST)
    prior = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"version": 1, "files": {}}
    require(prior.get("version") == 1, "unknown ownership version")
    desired = {}
    for tree in staged:
        for name in inventory(tree):
            require(name != MANIFEST and name not in desired, "duplicate/reserved staged path: " + name)
            path = safe(tree, name)
            desired[name] = (path.read_bytes().decode("utf-8"), path.stat().st_mode & 0o777)
    require("CLAUDE.md" in desired and "AGENTS.md" in desired, "stage both harnesses")
    edited = {}
    for edit in edits:
        name = edit["path"]
        require(name in snapshot and name != MANIFEST, "edit is outside inventoried context")
        text = edited.get(name, safe(target, name).read_bytes().decode("utf-8"))
        require(edit["before"] and text.count(edit["before"]) == 1, "edit must match exactly once: " + name)
        edited[name] = text.replace(edit["before"], edit["after"], 1)
    writes, owned, conflicts = {}, {}, []
    names = set(desired) | set(prior["files"]) | set(edited)
    for name in sorted(names):
        try:
            path = safe(target, name)
            current = path.read_bytes().decode("utf-8") if path.exists() else ""
            mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
            text = edited.get(name, current)
            old = prior["files"].get(name)
            wanted, new_mode = desired.get(name, (None, mode))
            if path.exists() and name.endswith((".md", ".json")):
                new_mode = mode
            if wanted is None and not old:
                result, state = text, None
            elif name.endswith(".md"):
                result, state = markdown(text, wanted, old)
            elif name.endswith(".json"):
                result, state = json_merge(text, wanted, old)
            else:
                # TOML and scripts remain valid, whole-file objects with hash ownership.
                require((old and old["kind"] == "file" and digest(text.encode()) == old["sha256"]
                         and mode == old["mode"]) or (not old and not path.exists()),
                        "occupied or modified structured file")
                result = wanted
                state = ({"kind": "file", "sha256": digest(wanted.encode()), "mode": new_mode}
                         if wanted is not None else None)
            if state:
                owned[name] = state
            if result != current or (result is not None and mode != new_mode):
                writes[name] = {"text": result, "mode": new_mode}
        except (ValueError, OSError, KeyError, TypeError) as exc:
            conflicts.append({"file": name, "reason": str(exc)})
    manifest = encoded({"version": 1, "files": owned}).decode()
    if not manifest_path.exists() or manifest_path.read_text() != manifest:
        writes[MANIFEST] = {"text": manifest,
                          "mode": manifest_path.stat().st_mode & 0o777 if manifest_path.exists() else 0o644}
    return {"target": str(target.resolve()), "inventory": snapshot, "writes": writes,
            "conflicts": conflicts, "edits": list(edits)}


def prepare(store, target, stage, edits=()):
    require(not stage.exists(), "use a fresh staging directory")
    require(not stage.resolve().is_relative_to(target.resolve()) and
            not stage.resolve().is_relative_to(store.resolve()), "stage outside both repositories")
    stage.mkdir(parents=True)
    trees = []
    for harness in ("claude-code", "codex"):
        tree = stage / harness
        subprocess.run([str(store / "bin/bundle"), "--emit", harness, "--out", str(tree)],
                       cwd=store, check=True)
        trees.append(tree)
    plan = build_plan(target, trees, edits)
    plan["timestamp"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (stage / "plan.json").write_bytes(encoded(plan))
    for name, item in plan["writes"].items():
        if item["text"] is not None:
            path = safe(stage / "candidate", name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(item["text"].encode("utf-8"))
            path.chmod(item["mode"])
    return plan


def apply(stage, review_path, approval_path):
    plan_bytes = (stage / "plan.json").read_bytes()
    plan = json.loads(plan_bytes)
    review_bytes = review_path.read_bytes()
    review, approval = json.loads(review_bytes), json.loads(approval_path.read_bytes())
    require(not plan["conflicts"], "resolve structural conflicts and prepare again")
    require(review["plan_sha256"] == approval["plan_sha256"] == digest(plan_bytes), "stale review/approval")
    require(approval["review_sha256"] == digest(review_bytes), "review changed after ruling")
    require(review["reviewer"] and approval["human"] and approval["gate"] and approval["go"] is True,
            "independent read and explicit human go required")
    ids = []
    for finding in review["findings"]:
        require(all(finding.get(k) for k in ("id", "file", "staged_file", "claim")) and
                type(finding.get("line")) is int and finding["line"] > 0 and
                type(finding.get("staged_line")) is int and finding["staged_line"] > 0,
                "contradiction needs file/line citations in both trees")
        ids.append(finding["id"])
    require(len(ids) == len(set(ids)) and set(ids) == set(approval["rulings"]) and
            all(isinstance(v, str) and v.strip() for v in approval["rulings"].values()),
            "human ruling required for every contradiction")
    target = pathlib.Path(plan["target"])
    require(inventory(target) == plan["inventory"], "target changed since review; prepare again")
    # Validate every destination before the first write, including the report.
    report_name = "docs/fiducial-adoption-" + plan["timestamp"] + ".md"
    report_path = safe(target, report_name)
    require(not plan["writes"] or not report_path.exists(), "report timestamp already used")
    for name in plan["writes"]:
        safe(target, name)
    if not plan["writes"]:
        return []
    report = ("# Fiducial adoption\n\nEvidence class: contract-verified. Claude Code /context and Codex hook trust: "
              "not live-verified by this procedure.\n\nChanged paths:\n\n" +
              "\n".join("- `" + n + "`" for n in sorted(plan["writes"])) +
              "\n\n## Inventory\n\n```json\n" + encoded(plan["inventory"]).decode() +
              "```\n\n## Independent contradiction read\n\n```json\n" + review_bytes.decode() +
              "\n```\n\n## Human rulings\n\n```json\n" + encoded(approval).decode() +
              "```\n\n## Exact legacy edits\n\n```json\n" + encoded(plan["edits"]).decode() + "```\n")
    for name, item in plan["writes"].items():
        path = safe(target, name)
        if item["text"] is None:
            path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(item["text"].encode("utf-8"))
            path.chmod(item["mode"])
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    return sorted(plan["writes"])


def labels(repo, run=subprocess.run):
    require(re.fullmatch(r"[\w.-]+/[\w.-]+", repo), "expected OWNER/REPO")
    def names():
        return set(run(["gh", "api", "--paginate", "repos/" + repo + "/labels", "--jq", ".[].name"],
                       check=True, text=True, capture_output=True).stdout.splitlines())
    existing = names()
    for name in LABELS:
        if name not in existing:
            run(["gh", "api", "--method", "POST", "repos/" + repo + "/labels",
                 "-f", "name=" + name, "-f", "color=6e7781"], check=True, text=True, capture_output=True)
    require(set(LABELS) <= names(), "label read-back incomplete")


if __name__ == "__main__":
    try:
        command, *args = sys.argv[1:]
        if command == "prepare" and len(args) in (3, 4):
            edits = json.loads(pathlib.Path(args[3]).read_text()) if len(args) == 4 else []
            plan = prepare(*(pathlib.Path(a).resolve() for a in args[:3]), edits=edits)
            print(json.dumps({"conflicts": plan["conflicts"], "changed_paths": sorted(plan["writes"])}))
        elif command == "apply" and len(args) == 3:
            print(json.dumps(apply(*(pathlib.Path(a).resolve() for a in args))))
        elif command == "labels" and len(args) == 1:
            labels(args[0])
        else:
            raise ValueError("usage: prepare STORE TARGET STAGE [EDITS_JSON] | apply STAGE REVIEW_JSON APPROVAL_JSON | labels OWNER/REPO")
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print("adopt: " + str(exc), file=sys.stderr)
        sys.exit(2)
```

Provenance: DEC-001100 (supersedes DEC-000910), DEC-001280; SPEC.md §§3.1, 6, 7;
subtraction plan §5; retained judgment cited above and R0030, R0196, R0462, R1617.

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

**contract-verified** — Contract-verified evidence supports fixture shape, schema expectations, required fields, API assumptions, and compatibility checks. It proves nothing about live credentials, provider availability, provider account state, quota or billing, CORS and domain restrictions, or browser rendering.

**live-verified** — Live-verified evidence supports credentials, provider availability, auth shape, live response shape, real status codes, and quota, billing, and config failures. It proves nothing about all edge cases, future availability, complete UX correctness, or browser rendering unless it was run in a browser.

**production-verified** — Production-verified evidence supports ongoing dependency health, real-world failure modes, regressions after deploy, availability, live user impact, SLO target compliance against the spec's targets for each Top K user journey, and error budget consumption.

**accepted risk** — Accepted risk is an explicit decision — the human's, or the release process's — to proceed despite a known gap.

**meaningful change** — A meaningful change is any change that warrants a change package — any change affecting behavior, interfaces, tests, dependencies, boundaries, or documentation of substance. A typo fix, a comment edit, or mechanical formatting is not meaningful in this sense.

**blocking** — A `blocking` gap is one the governing policies prohibit releasing with.

**boundary-sensitive** — Boundary-sensitive means do not overclaim here. It does not mean the area must be overtested.

**decision session** — A decision session triages, decides, and produces the artifacts that direct and record work — plans, subagent prompts, session records, tracker updates. It reads freely and writes those artifacts; the changes a plan specifies happen elsewhere, in the session that runs it. The boundary is role in the flow, not capability: a decision session may hold a clone and may commit.

**not-material** — A `not-material` gap is known but not relevant to the release decision.

**top k** — Top K means the K highest-priority user journeys listed in SPEC.md.

**track** — Track, tracking and tracker keep their ordinary meaning where they mean keeping or consulting a record — a loose-end tracker, a tracker issue, error budget tracking, SLO tracking. The loose-end tracker is the project's issue tracker — on GitHub, the repository's Issues and Milestones.

**version** — A document's version, at the moment it is referenced, is the SHA of the last commit that touched the file.

**red-gate** — A red-gate is a test run that fails on wrong behavior. A run that fails only because the module under test does not exist yet is not one.
