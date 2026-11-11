<!-- fiducial davepierceops/fiducial @ a8d87bc95afed9f5ac8b54fe2c8863013ce10265 20261111T041158Z -->

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

Review governed instructions for clarity, consistency, completeness, and safety as LLM context.

At intake, require every proposed row to:

- Stand alone within its bundle for an agent unfamiliar with the repository.
- Add something absent from its existing bundles.
- Agree with existing rules; flag conflicts for human resolution.
- State an obligation or define a needed term, rather than describe.
- State one trigger in its body.
- Add something beyond positive rules when phrased negatively.
- Ground any ban in an incident.
- Leave document forms to process documents.
- Express merged rules concisely rather than concatenate them.
- Leave term definitions to the Lexicon.
- Leave mechanically enforced requirements to tools.
- Combine checks triggered together; separate independently triggered checks.

Apply every criterion to every proposal. Pass qualifying rows; recommend retirement of others for human decision.

Cite the intake criterion it fails in every finding you raise.

Record each intake as a review artifact: what landed, or what was refused and against which row.

Cite a row by its ID in square brackets only if it covers every role, session, and corpus of the citing row.

Obtain explicit human approval before releasing a change in the consequential class. Approval applies to exposing the change to users, not merging code that remains unexposed. If its classification is uncertain, ask the human before release.

Keep the spec and tests provisional while developing them together. Finalize them only when every testable spec claim has a test asserting it and every test asserts something the spec states.

Edit only the artifacts assigned to your role. Report needed changes elsewhere as findings.

Bring the spec into line with what was actually built before closing an open spec delta.

Keep verification aligned with approved requirements, and justify changes to checks against those requirements. Support verification claims with the checks performed. Identify relevant simulations and untested assumptions, state what remains unverified, and claim only what the evidence establishes. Claims about state, results, or completeness require checking the underlying source or result.

Keep `decisions/log.md` append-only.

For each review, use the review-artifact skill to produce one artifact covering that read of the delta.

Apply a new review schema only to artifacts written after it lands.

Record every planned review pass. Mark unrun passes `not-run` with a reason, and treat a missing verdict as unverified.

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

## Definitions

**consequential class** — A change is consequential if it affects authentication or authorization; schema or data migrations; security, privacy, or user-data visibility or sharing; irreversible or hard-to-reverse operations; first user exposure of a feature or surface; breaking changes to public interfaces; pricing, billing, or entitlements; verification boundaries (live integrations, external-data fixtures, or verification classes); core architecture in the spec; an architecture summary that moves a boundary; or a Top K journey with 20% or less SLO error budget remaining. Other changes are routine and may release on evidence without explicit human approval.

**verification boundary** — A verification boundary separates what the evidence establishes from what remains unverified.

**spec branch** — A spec branch is the branch a spec's edits land on. The branch existing, with commits on it, is the state; there is no status value for it and no register recording it.

**open spec delta** — An open spec delta is the interval during which a spec branch carries edits the default branch does not; the branch is open for exactly that interval, and it ends when the spec closes at approval. A revision of an approved spec opens a new delta on a new branch.

**mock** — A mock is a claim about our side of the contract, with the other side verified elsewhere or explicitly accepted as unverified.

**reconciliation** — Reconciliation is the close of an open spec delta: the spec is brought into line with what was actually built.

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
