# Review: engagements/skeptic.md — cycle 1

Verdict: changes-required
Reviewed: engagements/skeptic.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 44 lines, against all eleven criteria of the review rubric @ 1bbd5b7. Includes a side-by-side comparison against roles/skeptic-risk-agent.md, which shares its name and its core question.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/assistant.md, engagements/cartographer.md, roles/skeptic-risk-agent.md, skills/review-artifact.md, policies/document-metadata-policy.md — all @ 1bbd5b7.
Not inspected: `engagements/comfy/**` (its own cycle, per the directive); `bin/bundle`'s handling of a file with no frontmatter (not run — the consequence in SK-1 is inferred from the settled selection rule, not observed); whether the ten infra false-confidence items are technically correct as infrastructure claims (engineering judgment, ceded per the role — the reviewer checked them for duplication, not for truth).
Findings: 9 — 5 blocking, 3 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: SK-3. Two documents in this repository are named Skeptic, share a core question, and grant contradictory authority — one is a hard gate in the change flow, the other declares itself never a blocker. Which governs a session called "Skeptic" is not derivable from either file.

## Criterion 10 first

**Disposition: retain-with-changes — conditional on SK-3 being settled first.**

The directive's four questions:

**Role, skill, standing instruction, or history?** A **role**, but an unusual
one: summoned rather than standing. It is invoked at a point, for one artifact,
and ends. That is closer to a skill in shape, but its content is a posture and a
question rather than a procedure, so a role is the right class.

**What `audience:` follows?** `[skeptic, human]`. The value exists:
`engagements/working-with-dave.md` @ 1bbd5b7 carries `audience: [assistant,
cartographer, skeptic, human]`, and a tally across 1bbd5b7 shows `skeptic` on
two files. Note it must be `skeptic`, not `skeptic-risk-agent` — the two are
distinct audience values in use, and conflating them is the mechanical form of
SK-3.

**Does a role document already carry it?** **Partly, and contradictorily.**
`roles/skeptic-risk-agent.md` @ 1bbd5b7 carries the same core question in
different words, an eighteen-item false-confidence checklist, a required
posture, and a review-inputs list. It does **not** carry the ten infra-specific
items in this file (terraform plan/apply, IAM propagation, per-project capacity,
runbook drift), and those are this file's genuine contribution. It also grants
the opposite authority.

**What survives.** The summoned-only invocation rule, the fresh-session
recommendation, the scope limit ("you do not question whether the work should
exist"), and the infra checklist minus its two duplicated items. That is a real
contribution to an engagement bundle. What does not survive is the output block
and, pending Dave, the authority claim.

**Retain-with-changes.** The changes are a frontmatter block, one cut section,
two cut checklist items, and — first — Dave's resolution of SK-3.

## SK-1 — blocking
Claim: the file carries no frontmatter at all, so it has no `audience:` and cannot be selected into any bundle.
Location: engagements/skeptic.md:1 (the file opens with `# Role: Skeptic`; there is no `---` block)
Evidence: verified by reading the file's first line. Verified by reading engagements/working-with-dave.md @ 1bbd5b7, which carries frontmatter naming `skeptic` as an audience value.
Consequence: criterion 2 fails outright. Under the baton's settled rule @ 1bbd5b7 — agents receive `bin/bundle <audience>` output and never the repository — this file reaches no agent. A session summoned as the engagement Skeptic today receives working-with-dave.md and, if the audience is misread as `skeptic-risk-agent`, the governed role instead — which is the wrong document and the one that makes it a gate. Inferred from the settled selection rule, not observed by running the compiler.
Fix: add frontmatter — `status: draft`, `last-reviewed: null`, `audience: [skeptic, human]`.
Related: AS-1, CA-1, QN-1.

## SK-2 — blocking
Claim: `engagements/**` is absent from the document-metadata policy's in-scope set, so nothing checks the frontmatter this file needs.
Location: engagements/skeptic.md (whole file), against policies/document-metadata-policy.md @ 1bbd5b7 lines 24–35
Evidence: verified by running `git show 1bbd5b7:policies/document-metadata-policy.md | sed -n '20,55p'`. `engagements/**` appears in neither the in-scope nor the out-of-scope list, and the policy states "Enforcement (hooks) checks exactly the in-scope set."
Consequence: the reason SK-1 was possible.
Fix: add `engagements/**` to the in-scope set, in the document-metadata-policy cycle.
Related: AS-2, CA-2, QN-2.

## SK-3 — blocking
Claim: two documents named Skeptic grant contradictory authority, and nothing in either says which governs a session summoned as "the Skeptic."
Location: engagements/skeptic.md:3–5 ("You are not a gate: your verdict is input to Dave's decision, never a blocker") and :42 ("not a blocker"), against roles/skeptic-risk-agent.md @ 1bbd5b7 and operating-model.md @ 1bbd5b7
Evidence: verified by reading all three. operating-model.md @ 1bbd5b7, "Change flow", makes step 7 "**Skeptic/risk review** … *(Skeptic/Risk)*" a stage that "completes before the next begins; no skipping or working ahead." roles/skeptic-risk-agent.md @ 1bbd5b7 states: "To signal that a change should not ship, mark the gap `blocking`" — and LEXICON.md @ 1bbd5b7 defines `blocking` as "must be resolved before release." This file states the opposite in its third line. The two also differ on output: the role document says "You do not emit a ship recommendation; that call is the Release Manager's," while this file's section 4 requires a verdict.
Consequence: criterion 11 in its exact terms — "boundaries two roles could both claim," and "language implying authority the methodology does not grant." A session told it is the Skeptic cannot determine from either document whether marking a gap `blocking` stops a release or is advice Dave may wave off. The failure is silent in the dangerous direction: an engagement Skeptic that believes itself advisory will not mark `blocking`, and a change-flow that expects step 7 to gate will read the absence as a pass.
Fix: Dave's call, and it is a real fork. The reviewer's reading is that the two are genuinely different roles in different contexts — inside this repository's change flow the Skeptic/Risk Agent is a stage with gate force; on a client engagement there is no release gate to be a stage of, because Dave and the client's CI hold the levers (engagements/working-with-dave.md @ 1bbd5b7, "Client guardrail"). If that is right, the fix is to say so: state in this file that an engagement has no release gate and that the verdict is therefore input to Dave, and state in roles/skeptic-risk-agent.md that its gate force is the change flow's. If it is wrong, one of the two files is retired. Either way the two documents must stop being silent about each other.

## SK-4 — blocking
Claim: the "Output — four sections, one screen" block is a review-artifact shape stated outside the schema that governs review-artifact shapes.
Location: engagements/skeptic.md:16–23
Evidence: verified by reading skills/review-artifact.md @ 1bbd5b7, which states: "It governs the **artifact** — the shape of what a review emits. Role documents govern the **review**: what must be inspected and what must be reported." That schema's own field table maps every one of this file's four sections to a named field: "Inspected" to `Scope` and `Not inspected`; "Claims vs evidence" to per-finding `Evidence`; "Gaps and risks" to `Consequence` and gap labels; "Verdict" to `Verdict`. The schema's `Verdict` values are `ready | ready-with-findings | changes-required`; this file's are "looks solid / solid with named risks / here's what I'd check before trusting it".
Consequence: two incompatible verdict vocabularies for the same act of reviewing, in a repository whose review artifacts are triaged by a decision session. A verdict of "looks solid" cannot be triaged alongside `ready-with-findings`, and a reader cannot tell which vocabulary a given artifact used. The schema explicitly does not retrofit existing artifacts, so every artifact this file produces is permanently in the other vocabulary.
Fix: cut the section and state that the artifact follows the review-artifact schema. If the engagement genuinely needs a lighter, one-screen shape — which is a plausible claim under time pressure on a client's keyboard — that variant belongs in skills/review-artifact.md as a named short form, not as a second schema here.

## SK-5 — blocking
Claim: two of the ten infra false-confidence items are already stated in a foundation file that this session loads.
Location: engagements/skeptic.md:29–30 ("plan output proves apply behavior", "apply success proves the system serves")
Evidence: verified by reading engagements/working-with-dave.md @ 1bbd5b7, whose "Infra verification ladder" closes: "Plan output does not prove apply behavior; apply success does not prove the system serves." The two sentences are the same two claims, negated, in the same order.
Consequence: criterion 4 against the foundation. Both files are in the same bundle by construction — this file's own line 3 says to load with it — so a Skeptic session reads the identical rule twice. The ladder is the better statement, because it also names the four verification levels the claims sit between.
Fix: cut the two items. The remaining eight are genuinely this file's and appear in no foundation file and in no role document.

## SK-6 — non-blocking
Claim: "Load with `working-with-dave.md`" is a path-shaped reference and an instruction the bundle has already carried out.
Location: engagements/skeptic.md:3
Evidence: verified by reading, against the settled rule @ 1bbd5b7 that agents receive bundle output and never the repository.
Consequence: criterion 1 and criterion 3.
Fix: cut the clause; the `audience:` values pair the two files.
Related: AS-10, CA-5.

## SK-7 — non-blocking
Claim: the file does not state its session kind, and its invocation model fits neither definition cleanly.
Location: engagements/skeptic.md:3–10, against core.md @ 1bbd5b7 "Vocabulary" and engagements/working-with-dave.md:7 @ 1bbd5b7
Evidence: verified by reading. core.md defines a decision session as one that "triages, decides, and produces the artifacts that direct and record work" and an execution session as one "carrying out a directive against a working tree." This file describes a session summoned into a fresh context, handed a diff and whatever Dave pastes, producing a review artifact and no directive — and working-with-dave.md declares the whole engagement set "for execution sessions."
Consequence: criterion 7. It matters more here than for the Cartographer, because the answer decides whether the session receives the Decision Layer — and Decision Layer rule 12 ("End non-trivial sessions with a retro") and rule 11 ("The thing under review is an artifact, separate from the discussion of it") would both change how this session behaves.
Fix: state it. A summoned reviewer holding a diff and producing an artifact is an execution session under core.md's definition, notwithstanding that no directive file exists — which suggests the definition, not this file, is where the gap is. Raise that against core.md in its own cycle rather than stretching it here.
Related: AS-3, CA-6.

## SK-8 — non-blocking
Claim: the checklist and the role document's checklist overlap without either acknowledging the other.
Location: engagements/skeptic.md:25–38, against roles/skeptic-risk-agent.md @ 1bbd5b7 "False-confidence checklist"
Evidence: verified by reading both. The role document's eighteen items are software-delivery-shaped (mocked API, headless DOM, coverage, fixtures, type checks, mocked auth, SLO with no verification mechanism). This file's ten are infrastructure-shaped (terraform plan/apply, pipeline timing, staging vs production, module defaults, IAM propagation, cross-project capacity, runbook drift). Eight of the ten are genuinely absent from the role document; two are covered by SK-5.
Consequence: lower weight than SK-3 — the lists are complementary, not contradictory. But a session that loads both reads twenty-eight checklist items with no statement of why there are two lists, and a session that loads one has no way to know the other exists.
Fix: whichever way SK-3 resolves, say in one line what each list is for. If the two roles are kept distinct, the infra list is the engagement Skeptic's and should say so.
Related: SK-3.

## SK-9 — observation
Claim: no use of any retired term, no vendor name, and no model name appears in the file.
Location: engagements/skeptic.md (whole file)
Evidence: verified by running a term sweep for *dispatch*, *sync block*, *track*, and *prompt*, and a name sweep for vendor and model names, over the file at 1bbd5b7. Both returned no matches. Note "terraform" is not present as a word — line 29's item says "plan output", generically.
Consequence: none. Recorded because the cycle directive requires both sweeps to be reported per file.
Fix: none.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.
No use of any retired term occurs in this file.

## Sweep counts

- Rules restated from the foundation: **1** (SK-5 — two checklist items restating working-with-dave.md's infra ladder)
- Output-shape lists with a home elsewhere: **1** (SK-4 — the four-section output block; home is skills/review-artifact.md)
- Path-shaped references: **1** (line 3, `working-with-dave.md`)
- Vendor and model names: **0**
- Retired terms: **0**
- SLO / Top K copies: **0**
