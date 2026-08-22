# Review: the corpus — Pass 1 reconciliation re-gate — cycle 1

Verdict: changes-required
Reviewed: 52 governed non-code files @ 8402c23 (enumerated below)
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: every file in the enumerated set, read whole, against all eleven criteria of docs/global-context/review-rubric.md @ 8402c23 and against the current foundation — docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, all @ 8402c23. Then seven corpus-wide reconciliation sweeps asking what no single-file cycle could ask: what collides, duplicates, or contradicts across the set. Bundle membership was computed mechanically from every `audience:` value in the set; path references, audience values, and retired vocabulary were extracted mechanically and resolved against the tree at 8402c23.
Cross-checked: docs/batons/baton-20260822T212629.md in full; docs/cycles/pass1-cycle-26-writing-retire-20260822T220000.md ("Decision"); skills/review-artifact.md; roles/context-quality-reviewer.md; the tree at ed926db, 2a722bb, cb3e75a, 1bbd5b7, e922926, a97c931, 0e07753, eea66dd, for dating each confirmation-pass finding against the change that caused it; every filename under reviews/ at 8402c23, for cycle numbering and stem collisions.
Not inspected: `bin/` behaviour, including whether the audience bundler that these findings assume would produce the membership computed here — it is unbuilt, and membership was computed from frontmatter directly rather than by running it; the two pre-existing `bin/tests` failures; docs/history/**, docs/batons/**, docs/cycles/**, reviews/**, retros/**, OPEN-ITEMS.md, BACKLOG*.md, decisions/log.md, CLAUDE.md, AGENTS.md, and the retired root README.md, all excluded by the directive; whether any rule is *correct* as engineering or product judgment — this role judges coherence and safety as LLM context only; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository; the content of the archived predecessors under docs/history/, which were not consulted when reviewing their successors.
Findings: 47 across 19 companion artifacts — 21 from the confirmation pass, 26 from the nine first-cycle reviews; 22 blocking, 25 non-blocking. This artifact carries the seven sweeps (178 rows: 22 duplicate rules, 8 contradictions, 10 term collisions, 17 audience values, 101 path references, 12 retired-vocabulary terms, 8 role boundaries) and the confirmation-pass verdicts; per-file findings are in the artifacts named below.
Prior cycle: none for the corpus as a set. Twenty-six single-file cycles precede it; each file's own prior cycle is named in its artifact.
Dave should inspect: RS-1 (the `all-roles` / `all-decision-roles` selector, which is the mechanism behind eleven of these findings); DR-1 and the `engagements/sre` bundle-membership cluster; TC-1 (the two claims ladders, already decided once on 2026-08-20 and never executed); and the scope discrepancy in "Departures from the directive" at the end — three files the directive treats as reviewed have never been reviewed.

---

## Scope — the enumerated set

The corpus is every non-code governed file: everything `bin/check-frontmatter --all` matches (36 files, from the ten globs the metadata policy declares), plus `docs/global-context/*.md` (4), `engagements/**/*.md` (11), and `prose-criteria.md` (1). The latter three groups are outside the frontmatter scope by a known policy gap, not by intent. 52 files.

Excluded per the directive: docs/history/**, docs/batons/**, docs/cycles/**, reviews/**, retros/**, OPEN-ITEMS.md, BACKLOG*.md, decisions/log.md, README.md, CLAUDE.md, AGENTS.md. The root README.md glob matches nothing at 8402c23; `bin/check-frontmatter --all` reports it as `WARN [unmatched-glob]`, which is a known and excluded item.

**Frontmatter-matched (36):**

LEXICON.md · boundaries/human-review-boundary.md · context-sets/production-grade-software.md · context-sets/spec-and-change-discipline.md · context-sets/testing-and-verification.md · operating-model.md · policies/commit-and-change-control-policy.md · policies/decision-log-policy.md · policies/document-metadata-policy.md · policies/project-setup-requirements.md · policies/release-readiness-policy.md · policies/remote-write-verification-policy.md · policies/source-of-truth-policy.md · policies/verification-boundary-policy.md · roles/architect-agent.md · roles/chief-of-staff.md · roles/coder-agent.md · roles/context-quality-reviewer.md · roles/release-manager-agent.md · roles/reviewer-agent.md · roles/skeptic-risk-agent.md · roles/spec-reviewer-agent.md · roles/test-designer-agent.md · roles/writer.md · skills/boundary-audit.md · skills/command-blocks.md · skills/conversation-retro.md · skills/directive-authoring.md · skills/evidence-review.md · skills/review-artifact.md · skills/spec-review-cycle.md · skills/test-plan-review.md · specs/prd-template.md · specs/trd-template.md · vendors/README.md · vendors/claude-code/environment-config.md

**docs/global-context (4):** core.md · decision-layer.md · inventory.md · review-rubric.md

**engagements (11):** assistant.md · cartographer.md · skeptic.md · working-with-dave.md · sre/README.md · sre/baseline-measurement.md · sre/engagement-change-package.md · sre/implementer.md · sre/override-log-policy.md · sre/speed-audit.md · sre/system-discovery.md

**root (1):** prose-criteria.md

---

## Sweep (a) — Duplicate rules

A rule stated in two or more files. "One home" proposes where it should live; it is a proposal, not a resolution.

| # | Rule | Locations | Proposed one home |
| --- | --- | --- | --- |
| DR-1 | Mid-delta directives derive from / cite the spec branch and pin its SHA, not the default branch | context-sets/spec-and-change-discipline.md:54-57 · roles/chief-of-staff.md:101-104 · skills/directive-authoring.md:20-21 · skills/spec-review-cycle.md:35-37 | context-sets/spec-and-change-discipline.md — it states the open-delta model the rule belongs to. All four are in the `chief-of-staff` bundle. |
| DR-2 | The reviewer gate fires once over the whole delta at reconciliation, not once per edit | LEXICON.md:32-38 · policies/commit-and-change-control-policy.md:117-131 · roles/spec-reviewer-agent.md:33-36 · skills/spec-review-cycle.md:80-95 | LEXICON.md defines *Reconciliation*; the mechanism belongs in policies/commit-and-change-control-policy.md. The role and skill should cite, not restate. |
| DR-3 | Whoever produces an artifact does not approve/review it | operating-model.md:106-110 · roles/spec-reviewer-agent.md:11-13 · skills/test-plan-review.md:14 · engagements/sre/implementer.md:37 | operating-model.md — it already states it as one of two mandatory separations. |
| DR-4 | A test that passes before implementation is a broken test, not a head start | context-sets/testing-and-verification.md:21 · roles/test-designer-agent.md:26 | context-sets/testing-and-verification.md. Verbatim duplicate; both files are in the `test-designer-agent` bundle. |
| DR-5 | Concurrency comes from disjoint territory, never from merging convergent edits; at most two tranches | LEXICON.md:36-40 · context-sets/spec-and-change-discipline.md:58-64 · roles/chief-of-staff.md:106-110 | context-sets/spec-and-change-discipline.md. LEXICON should carry the term only. |
| DR-6 | Decomposition requires a closed delta; decomposing from ungated spec is prohibited | context-sets/spec-and-change-discipline.md:50-52 · roles/chief-of-staff.md:95-100 | roles/chief-of-staff.md — decomposition is that role's act. |
| DR-7 | Branch protection lives in the forge, cannot be verified from the repo, is confirmed by a human at adoption | policies/commit-and-change-control-policy.md:105-110 · policies/project-setup-requirements.md:23-41 | policies/project-setup-requirements.md — it is an adoption precondition by its own framing. |
| DR-8 | The grandfather disposition list: absent document does not qualify; no list means the clause does not apply | policies/document-metadata-policy.md:83-91 · policies/project-setup-requirements.md:66-74 | policies/document-metadata-policy.md — the clause is defined there. |
| DR-9 | An empty `reviews/expedited-log.md` must exist before the first expedited agreement | policies/document-metadata-policy.md:186-187 · policies/project-setup-requirements.md:58-63 | policies/project-setup-requirements.md. |
| DR-10 | The frontmatter in-scope set | policies/document-metadata-policy.md:24-35 (globs, read at runtime by `bin/aimeta/scope.py`) · policies/project-setup-requirements.md:45-52 (prose) | policies/document-metadata-policy.md. The prose copy has already drifted — see PSR-1. |
| DR-11 | Durable policy never lives only in vendor-specific tooling | operating-model.md:100-102 · policies/source-of-truth-policy.md:29-42 | policies/source-of-truth-policy.md. |
| DR-12 | A derived artifact conflicting with a canonical one is a hard stop | operating-model.md:33-40 · policies/source-of-truth-policy.md:51-64 | policies/source-of-truth-policy.md. |
| DR-13 | "When unsure which tier applies, treat the change as consequential and ask" | operating-model.md:155-157 · policies/commit-and-change-control-policy.md:20-22 | policies/commit-and-change-control-policy.md — it holds the exhaustive list. |
| DR-14 | `accepted-risk` is applied only where Dave or the release process has already accepted the gap; otherwise `blocking` | LEXICON.md:70-77 · skills/review-artifact.md:39-43 | LEXICON.md. See RA-3. |
| DR-15 | Manage the proof, not the code | operating-model.md:28 · engagements/sre/README.md:49-50 | operating-model.md, which is in every engagement bundle. See SRE-RM-2. |
| DR-16 | The baseline is the failing test | engagements/sre/README.md:31 · engagements/sre/README.md:52 · engagements/sre/baseline-measurement.md:12 | engagements/sre/baseline-measurement.md. Three statements, two of them in one file. See SRE-BM-2. |
| DR-17 | Every ceremonial element is trivially overridable by Dave, and the override is logged | engagements/sre/README.md:41-45 · engagements/sre/README.md:53 · engagements/sre/override-log-policy.md:11-30 · engagements/sre/baseline-measurement.md:37-40 | engagements/sre/override-log-policy.md. See SRE-BM-3, SRE-OLP-1. |
| DR-18 | Changes land as pull requests through the client's own gates; nothing is pushed | engagements/sre/README.md:36-38 · engagements/sre/README.md:53 · engagements/sre/implementer.md:35-36 · engagements/sre/speed-audit.md:26-28 | engagements/sre/README.md, stated once. |
| DR-19 | A recommendation is a next step, never a ship call; the ship call is the Release Manager's; signal no-ship by marking the gap `blocking` | skills/evidence-review.md:32-36 · roles/skeptic-risk-agent.md:124-128 | roles/skeptic-risk-agent.md — it is that role's constraint. |
| DR-20 | Retros are state/tracker-class artifacts, exempt from the document metadata policy | skills/conversation-retro.md:41-48 (asserted) · policies/document-metadata-policy.md:37-42 (Out of scope — does not name `retros/`) | policies/document-metadata-policy.md. The exemption is true by default (`retros/` matches no in-scope glob) but is claimed by the wrong document and is not recorded in the list that enumerates the exempt classes. |
| DR-21 | A record with no fixed filename, created on first use, kept in the engagement working area | engagements/assistant.md:14-20 (loose-end / quiet notes) · engagements/sre/override-log-policy.md:20-26 (override log) | Two different records, one convention. State the convention once in engagements/sre/README.md. |
| DR-22 | Filename convention `<descriptor>-<timestamp>`, no random strings, hashes, or UUIDs | docs/global-context/core.md:33 (Acting 14) · docs/global-context/review-rubric.md:44-46 (criterion 9) | docs/global-context/core.md. The rubric criterion is a test for the rule; see RR-1 for whether that exempts it from criterion 4. |

## Sweep (b) — Contradictions

Two files stating incompatible rules or definitions. Not resolved here.

| # | Statement A | Statement B | Why incompatible |
| --- | --- | --- | --- |
| CN-1 | engagements/cartographer.md:9 — "The Cartographer runs as a decision session." | engagements/sre/system-discovery.md:9-12 — "This skill runs in an execution session. ... Executed by the Cartographer." | docs/global-context/core.md:41-43 defines the two kinds as mutually exclusive roles in the flow. Both files are in the `cartographer` bundle, so one session holds both. See SRE-SD-1. |
| CN-2 | policies/document-metadata-policy.md:91-93 — "`audience:` values are `roles/` file slugs plus `all-roles` and `human`. Any other value fails enforcement." | Eleven files carry `assistant`, `cartographer`, `skeptic`, or `implementer`, none of which is a `roles/` slug at 8402c23 | The rule declares those files non-conformant. They pass only because `engagements/**` is outside the enforced set. See DMP-1 and sweep (d). |
| CN-3 | engagements/skeptic.md:12 — "An engagement has no release gate." | engagements/sre/README.md:36-38 — "The client's humans hold the release gate on their own systems." | Both in the `skeptic` bundle; "release gate" carries a defined meaning from operating-model.md:145-160, also in that bundle. Reconcilable, but neither file reconciles them. See SK-2. |
| CN-4 | engagements/sre/engagement-change-package.md:9 — "This skill runs in an execution session." | engagements/assistant.md:9 — "The Assistant runs as a decision session," and `assistant` is in that file's `audience:` | The file is delivered to a session it declares itself not for. Recorded in docs/batons/baton-20260822T212629.md as a deliberate fiat; the fiat and the `audience:` still disagree. See SRE-ECP-3. |
| CN-5 | engagements/sre/speed-audit.md:9 — "This skill runs in a decision session." | engagements/sre/implementer.md:9 and engagements/skeptic.md:11 — both roles run as execution sessions, and both slugs are in speed-audit's `audience:`; step 5 assigns them work | Same shape as CN-4, in the other direction. See SA-3. |
| CN-6 | engagements/sre/override-log-policy.md:13-15 — every ceremonial element, including "any procedural step," is trivially overridable | engagements/working-with-dave.md:33-36 — zero write access to the client's systems, "not negotiable, not overridable" | Compatible only if the guardrail is not a ceremonial element, which neither file says. In the `implementer` bundle the second statement is absent entirely. See SRE-IMP-1, SRE-OLP-1, WD-1. |
| CN-7 | roles/spec-reviewer-agent.md:27-36 — a hard gate on "any canonical document, PRD and TRD and the methodology documents equally"; Dave does not agree one without its sign-off | policies/document-metadata-policy.md:191-236 (Doc-only cycle) — a co-authored document "reaches `agreed` on his sign-off, with no separate reviewer" | Reconciled: roles/spec-reviewer-agent.md:44-46 names two bounded exceptions and cedes their statement to the metadata policy. Listed so the sweep is visibly complete; **not** an open contradiction. |
| CN-8 | roles/skeptic-risk-agent.md:9-11 — the change-flow Skeptic review is "a stage with gate force" | engagements/skeptic.md:12-14 — the engagement Skeptic's "verdict is therefore input to Dave's decision, not a gate on anything" | Reconciled in roles/skeptic-risk-agent.md's own first sentence, which names the other role and its force. Listed for completeness; **not** an open contradiction. The unresolved part is the shared name — see TC-3. |

## Sweep (c) — Term collisions

A term used with a meaning LEXICON does not give it, a term LEXICON defines that a file uses differently, or a term two files use for different things.

| # | Term | Sense A | Sense B | LEXICON at 8402c23 |
| --- | --- | --- | --- | --- |
| TC-1 | **inferred** | docs/global-context/core.md:22 — one of four evidence classes: "you reasoned to it" | prose-criteria.md:60-63 — one of four claim tiers: "grounded in experience, observation, or data below the bar for proof" | Defines neither ladder. Both files are in the `writer` bundle. The 2026-08-20 disposition (docs/global-context/inventory.md:164) resolved this and was never executed. See PC-1, LX-1. |
| TC-2 | **tier** | docs/global-context/decision-layer.md:14 and docs/global-context/review-rubric.md:38 — model tier: frontier / solid general-purpose / cheap | prose-criteria.md:41, :53-67 — claim tier: relayed / demonstrated / inferred / opinion | Not defined. Both senses reach the `writer` bundle. |
| TC-3 | **Skeptic** | roles/skeptic-risk-agent.md — a change-flow stage with gate force; audience slug `skeptic-risk-agent` | engagements/skeptic.md — advisory to Dave, no gate; audience slug `skeptic` | Not defined. roles/writer.md:15 offers "a Skeptic" without saying which, and neither document is in the `writer` bundle. See WR-2, SRE-RM-3. |
| TC-4 | **retro** | skills/conversation-retro.md — one document per LLM conversation, fixed schema, stored at `retros/`, decision session | engagements/sre/override-log-policy.md:28-30 — "the engagement retro — a short end-of-engagement review run by Dave" | Not defined. skills/conversation-retro.md is `all-roles`, so both senses reach all four engagement bundles. See SRE-OLP-2. |
| TC-5 | **agreed** | policies/document-metadata-policy.md:69-71 — a frontmatter status, "the repo's standing verb," reached only through a gated path, requiring a non-null `last-reviewed` | engagements/sre/speed-audit.md:41-43 — "**Agreed** means Dave says yes" about an ungoverned Improvement Proposal | Not defined as a term, though the status value is used throughout. The metadata policy is in all four engagement bundles. See SA-2. |
| TC-6 | **boundary** | policies/verification-boundary-policy.md — the point where evidence stops | boundaries/human-review-boundary.md — a governed document class, and a scope limit on human diff-reading | Defines the *evidence classes* and *release impact labels* but not "boundary" itself. A third sense appears at roles/chief-of-staff.md:87 ("the boundaries the execution session must not cross"). All three reach every `all-roles` bundle. |
| TC-7 | **claim / claimed** | docs/global-context/core.md:21-23 — an assertion about state, results, verification, or completeness | LEXICON.md:42-46 — "**Claimed** — of a spec document: appearing in an open delta's diff" | LEXICON defines the narrow spec sense only; the evidence sense, used far more often, is Core's. A reader meeting "claimed" in LEXICON's Spec state section after reading Core's Evidence section has no marker that the word changed axis. |
| TC-8 | **"needs Dave decision"** | roles/release-manager-agent.md:52-57 — a valid ship recommendation | LEXICON.md:72-73 — "A gap awaiting Dave's judgment is blocking; 'requires Dave decision' is not a label" | Different slots — a recommendation is not a gap label — but the near-identical phrasing is asserted valid in one file and invalid in the other, both in the `release-manager-agent` bundle. |
| TC-9 | **System Map**, **Measurement Baseline**, **Improvement Proposal**, **engagement working area**, **baseline-gate** | Used across all seven `engagements/sre/` files and engagements/assistant.md | Each defined in exactly one file, and in three cases that file is absent from bundles where the term is used | Defines none of them. See SRE-SD-2, SRE-IMP-2, SRE-BM-1, SRE-ECP-2. |
| TC-10 | **red-gate**, **change package**, **meaningful change**, **consequential class**, **human-gate**, **gate document** | Load-bearing terms used across 6-14 files each | Each defined once, in operating-model.md, policies/commit-and-change-control-policy.md, or policies/document-metadata-policy.md | Defines none of them. All the defining files carry `all-roles`, so the definitions do reach every bundle; recorded because LEXICON's stated job is "terms with a fixed meaning across this methodology" and these are the corpus's most-used terms. |

## Sweep (d) — Audience values

Every distinct `audience:` value in the 52-file set, with its file count. Computed mechanically over the frontmatter at 8402c23. No file in the set lacks `audience:`.

| Value | Files | Is it a `roles/` slug? | Flags |
| --- | --- | --- | --- |
| `human` | 52 | reserved | Carried by every file. Ignored by the bundler per the 2026-08-20 decision. |
| `all-roles` | 17 | reserved | Expands to every bundle — including `writer` and the five engagement bundles. See RS-1 below. |
| `chief-of-staff` | 14 | yes | — |
| `assistant` | 9 | **no** — engagements/assistant.md | Not a `roles/` slug; contradicts policies/document-metadata-policy.md:91-93. See CN-2. |
| `cartographer` | 7 | **no** — engagements/cartographer.md | Same. Not a retired role: engagements/cartographer.md is live at 8402c23. |
| `implementer` | 6 | **no** — engagements/sre/implementer.md | Same. Introduced at 0e07753. |
| `skeptic` | 6 | **no** — engagements/skeptic.md | Same. Collides in name with `skeptic-risk-agent`; see TC-3. |
| `reviewer-agent` | 5 | yes | — |
| `spec-reviewer-agent` | 5 | yes | — |
| `context-quality-reviewer` | 4 | yes | — |
| `release-manager-agent` | 4 | yes | — |
| `skeptic-risk-agent` | 4 | yes | — |
| `architect-agent` | 3 | yes | — |
| `writer` | 2 | yes — roles/writer.md | prose-criteria.md and roles/writer.md only. Introduced at eea66dd. |
| `all-decision-roles` | **1** | reserved-in-intent, not reserved in policy | docs/global-context/decision-layer.md only. **Flagged: used by exactly one file.** The reservation gap is a known and excluded item; the bundle consequence is RS-1. |
| `coder-agent` | **1** | yes | roles/coder-agent.md only. **Flagged: used by exactly one file.** Harmless — `all-roles` supplies the rest of the bundle. |
| `test-designer-agent` | **1** | yes | roles/test-designer-agent.md only. **Flagged: used by exactly one file.** Same. |

**No audience value names a retired role.** `editor`, `section-writer`, `instruction-reviewer`, and `orchestrator` appear in no `audience:` in the set. `cartographer` and `skeptic` name live engagement roles, not retired ones.

**RS-1 — the selector is the mechanism behind eleven of this re-gate's findings.** Two values do the opposite of what their names suggest:

- `all-roles` (17 files — Core, LEXICON, the operating model, all three context sets, all eight policies, the human-review boundary, command-blocks, conversation-retro) expands to *every* bundle. The `writer` bundle is 19 files, 17 of them engineering governance: the verification-boundary policy, the testing context set, the commit-and-change-control policy, the spec templates' parent rules. The five engagement bundles carry the same load. Every one of those files satisfies criterion 10 ("lands in at least one bundle") trivially and satisfies criterion 1 ("written to be read inside a generated bundle") only for the engineering bundles it was written for.
- `all-decision-roles` (1 file — the Decision Layer) expands to a bundle nothing else selects. The consequence is concrete: **docs/global-context/decision-layer.md is in no role's bundle.** The `chief-of-staff` bundle (31 files) does not contain it, nor does `assistant` (26) or `cartographer` (24) — the three decision-session roles in the corpus. Every register, pace, and block rule a decision session runs on is delivered to nobody.

The reservation of `all-decision-roles` in the metadata policy is a known and excluded item. Its delivery consequence is not, and is recorded here.

## Sweep (e) — Path-shaped references, corpus-wide

101 distinct path-shaped tokens, no rows omitted. Every backticked token containing a directory separator or a file extension was extracted mechanically over the 52 in-scope files at 8402c23 and resolved against the tree.

**Cited only from docs/global-context/inventory.md — 45 rows.** One file is the source of nearly half the corpus's path references and of every dead one but two; see INV-2 in reviews/inventory-cycle-1.md.

| Reference | At 8402c23 | Location |
| --- | --- | --- |
| `AGENTS.md` | exists | docs/global-context/inventory.md:113 |
| `CLAUDE.md` | exists | docs/global-context/inventory.md:113 |
| `assistant.md` | exists as engagements/assistant.md (cited as bare basename) | docs/global-context/inventory.md:43 +3 |
| `base.md` | renamed-to docs/global-context/core.md + decision-layer.md (a97c931) | docs/global-context/inventory.md:63 +5 |
| `bin/bundle --audience` | template/command, not a path | docs/global-context/inventory.md:175 |
| `bin/bundle --audience <name>` | template/command, not a path | docs/global-context/inventory.md:148 |
| `bin/bundle-methodology --out ~/Downloads` | template/command, not a path | docs/global-context/inventory.md:187 |
| `bin/session-tar` | MISSING | docs/global-context/inventory.md:177 |
| `collab-workflow.md` | deleted (never in this repo) | docs/global-context/inventory.md:121 +1 |
| `command-blocks.md` | exists as skills/command-blocks.md (cited as bare basename) | docs/global-context/inventory.md:78 +12 |
| `commit-and-change-control-policy.md` | exists as policies/commit-and-change-control-policy.md (cited as bare basename) | docs/global-context/inventory.md:136 |
| `context-sets/base.md` | renamed-to docs/global-context/core.md + decision-layer.md (a97c931) | docs/global-context/inventory.md:30 +5 |
| `conversation-retro.md` | exists as skills/conversation-retro.md (cited as bare basename) | docs/global-context/inventory.md:177 |
| `core.md` | exists as docs/global-context/core.md (cited as bare basename) | docs/global-context/inventory.md:151 |
| `davepierceops/ai` | repo name, not a path | docs/global-context/inventory.md:12 +2 |
| `davepierceops/writing` | repo name, not a path | docs/global-context/inventory.md:13 +2 |
| `decision-layer.md` | exists as docs/global-context/decision-layer.md (cited as bare basename) | docs/global-context/inventory.md:151 |
| `directive-dispatch.md` | renamed-to skills/directive-authoring.md (1bbd5b7) | docs/global-context/inventory.md:83 +5 |
| `editor.md` | deleted (eea66dd) | docs/global-context/inventory.md:40 +8 |
| `engagements/` | exists | docs/global-context/inventory.md:186 +1 |
| `engagements/assistant.md` | exists | docs/global-context/inventory.md:33 |
| `engagements/cartographer.md` | exists | docs/global-context/inventory.md:58 |
| `engagements/comfy/*` | glob | docs/global-context/inventory.md:140 |
| `engagements/skeptic.md` | exists | docs/global-context/inventory.md:66 |
| `engagements/working-with-dave.md` | exists | docs/global-context/inventory.md:32 +1 |
| `machinery-criteria.md` | deleted (eea66dd) | docs/global-context/inventory.md:173 |
| `policies/decision-log-policy.md` | exists | docs/global-context/inventory.md:127 |
| `policies/remote-write-verification-policy.md` | exists | docs/global-context/inventory.md:108 |
| `prose-criteria.md` | exists | docs/global-context/inventory.md:164 +2 |
| `roles/chief-of-staff.md` | exists | docs/global-context/inventory.md:29 +5 |
| `section-writer.md` | deleted (eea66dd) | docs/global-context/inventory.md:79 |
| `skills/command-blocks.md` | exists | docs/global-context/inventory.md:75 |
| `skills/directive-dispatch.md` | renamed-to skills/directive-authoring.md (1bbd5b7) | docs/global-context/inventory.md:77 |
| `spec-and-change-discipline.md` | exists as context-sets/spec-and-change-discipline.md (cited as bare basename) | docs/global-context/inventory.md:40 +5 |
| `spec-review-cycle.md` | exists as skills/spec-review-cycle.md (cited as bare basename) | docs/global-context/inventory.md:65 |
| `working-with-dave.md` | exists as engagements/working-with-dave.md (cited as bare basename) | docs/global-context/inventory.md:34 +9 |
| `writing-20260820-161541.tar.gz` | MISSING | docs/global-context/inventory.md:13 |
| `writing/editor.md` | deleted (eea66dd) | docs/global-context/inventory.md:112 +2 |
| `writing/machinery-criteria.md` | deleted (eea66dd) | docs/global-context/inventory.md:123 +1 |
| `writing/prose-criteria.md` | renamed-to prose-criteria.md (eea66dd) | docs/global-context/inventory.md:61 +1 |
| `writing/roles/editor.md` | deleted (eea66dd) | docs/global-context/inventory.md:29 +1 |
| `writing/roles/reviewer.md` | deleted (eea66dd) | docs/global-context/inventory.md:64 +2 |
| `writing/roles/section-writer.md` | deleted (eea66dd) | docs/global-context/inventory.md:139 |
| `writing/roles/skeptic.md` | deleted (eea66dd) | docs/global-context/inventory.md:64 |
| `writing/section-writer.md` | deleted (eea66dd) | docs/global-context/inventory.md:85 +2 |

**Cited from elsewhere — 56 rows.**

| Reference | At 8402c23 | Location(s) |
| --- | --- | --- |
| `.claude/settings.json` | exists | vendors/claude-code/environment-config.md:66 |
| `.claude/settings.local.json` | exists | vendors/claude-code/environment-config.md:93 |
| `/` | extraction artifact — the slash between two adjacent backticked tokens, not a reference | docs/global-context/inventory.md:152 +2 |
| `<reviews/path.md> @ <sha>` | template/command, not a path | policies/document-metadata-policy.md:80 |
| `BACKLOG-v2.md` | exists | policies/document-metadata-policy.md:40 +1 |
| `COLLAB-STATE.md` | exists | policies/document-metadata-policy.md:40 |
| `LEXICON.md` | exists | docs/global-context/inventory.md:15 +16 |
| `MANIFEST.md` | exists | policies/document-metadata-policy.md:39 +3 |
| `MERGE-NOTES-v0.4.md` | exists | policies/document-metadata-policy.md:41 |
| `OPEN-ITEMS.md` | exists | docs/global-context/inventory.md:122 +4 |
| `README.md` | deleted (e922926) | policies/document-metadata-policy.md:34 +1 |
| `REVIEW-*.md` | glob | policies/document-metadata-policy.md:41 |
| `bin/check-frontmatter --staged` | template/command, not a path | policies/project-setup-requirements.md:54 |
| `bin/install-hooks` | exists | policies/project-setup-requirements.md:53 |
| `bin/state` | MISSING | roles/chief-of-staff.md:24 |
| `boundaries/**` | glob | policies/document-metadata-policy.md:29 |
| `boundaries/human-review-boundary.md` | exists | policies/document-metadata-policy.md:150 |
| `context-sets/**` | glob | policies/document-metadata-policy.md:28 |
| `davepierceops/fiducial` | repo name, not a path | docs/global-context/inventory.md:153 +1 |
| `decisions/log.md` | exists | policies/decision-log-policy.md:20 +1 |
| `docs/cycles/` | exists | roles/chief-of-staff.md:30 |
| `docs/cycles/<descriptor>-<timestamp>.md` | template/command, not a path | skills/directive-authoring.md:33 |
| `docs/packages/<tranche>-decomposition.md` | template/command, not a path | roles/chief-of-staff.md:70 |
| `grep DEC-000070 decisions/log.md` | template/command, not a path | policies/decision-log-policy.md:38 |
| `operating-model.md` | exists | docs/global-context/inventory.md:124 +3 |
| `policies/**` | glob | policies/document-metadata-policy.md:26 |
| `policies/commit-and-change-control-policy.md` | exists | policies/document-metadata-policy.md:138 |
| `policies/document-metadata-policy.md` | exists | docs/global-context/inventory.md:130 +1 |
| `policies/project-setup-requirements.md` | exists | policies/document-metadata-policy.md:142 |
| `policies/release-readiness-policy.md` | exists | policies/document-metadata-policy.md:140 |
| `policies/source-of-truth-policy.md` | exists | docs/global-context/inventory.md:124 +1 |
| `policies/verification-boundary-policy.md` | exists | policies/document-metadata-policy.md:141 |
| `retro-<timestamp>.md` | template/command, not a path | skills/conversation-retro.md:56 |
| `retros/` | exists | docs/global-context/inventory.md:129 +3 |
| `reviews/` | exists | policies/document-metadata-policy.md:78 +1 |
| `reviews/**` | glob | policies/document-metadata-policy.md:41 |
| `reviews/<stem>-cycle-<n>.md` | template/command, not a path | skills/review-artifact.md:48 |
| `reviews/expedited-log.md` | exists | policies/document-metadata-policy.md:175 +2 |
| `reviews/expedited-log.md @ <sha>` | template/command, not a path | policies/document-metadata-policy.md:178 |
| `reviews/spec-review-cycle-cycle-1.md` | exists | skills/review-artifact.md:53 |
| `roles/` | exists | policies/document-metadata-policy.md:92 |
| `roles/**` | glob | policies/document-metadata-policy.md:27 |
| `roles/release-manager-agent.md` | exists | policies/document-metadata-policy.md:146 |
| `roles/reviewer-agent.md` | exists | policies/document-metadata-policy.md:145 |
| `roles/skeptic-risk-agent.md` | exists | policies/document-metadata-policy.md:147 |
| `roles/spec-reviewer-agent.md` | exists | policies/document-metadata-policy.md:144 |
| `settings.json` | exists as .claude/settings.json (cited as bare basename) | vendors/claude-code/environment-config.md:10 |
| `skills/**` | glob | policies/document-metadata-policy.md:30 |
| `skills/conversation-retro.md` | exists | docs/global-context/inventory.md:112 +2 |
| `skills/spec-review-cycle.md` | exists | docs/global-context/inventory.md:64 +2 |
| `spec/*` | glob | roles/chief-of-staff.md:32 |
| `spec/<tranche-slug>` | template/command, not a path | LEXICON.md:22 +1 |
| `specs/` | exists | policies/document-metadata-policy.md:158 +3 |
| `specs/**` | glob | policies/document-metadata-policy.md:31 |
| `vendors/**` | glob | policies/document-metadata-policy.md:32 |
| `~/.ssh/**` | glob | vendors/claude-code/environment-config.md:34 |

**Reading of sweep (e).** Criterion 3 makes any path-shaped reference a defect. Four dead targets survive outside inventory.md: `README.md` (policies/document-metadata-policy.md:34 and :152 — DMP-2), `bin/state` (roles/chief-of-staff.md:24, stated honestly as not yet existing), and `settings.json` cited as a bare basename (vendors/claude-code/environment-config.md:10, a file that governs no session). Everything else that resolves does so, and the remaining live references cluster in three places where they are structural rather than incidental: policies/document-metadata-policy.md (a policy *about* paths, 30 rows), roles/chief-of-staff.md (a read-sequence over named artifacts, 7 rows), and vendors/claude-code/environment-config.md (a configuration record, 5 rows). Those three were accepted by their own cycles and no foundation change has invalidated them; they are not re-opened here. The concentration finding is INV-2: docs/global-context/inventory.md is the source of 45 of 101 rows and of every dead target but four.

**Not captured by this sweep.** File-shaped references that are not backticked — "the system-discovery skill," "the baseline-measurement skill," "the review-artifact schema," "the testing and verification context set," "the instruction-writing criteria" — are criterion 3 defects that a mechanical path sweep cannot see. Those found by reading are recorded in sweep (g) and in SRE-RM-1, SK-1, SA-1.

## Sweep (f) — Retired vocabulary, corpus-wide

Every term LEXICON retires, every retired role name, and vendor and model names outside `vendors/`. Extracted mechanically over the 52 files at 8402c23.

| # | Term | Live occurrences outside its own tombstone | Verdict |
| --- | --- | --- | --- |
| RV-1 | **dispatch** | docs/global-context/inventory.md:70, :77, :83-86, :159, :171 (8 lines) | All in one file, all as historical citation of the retired `directive-dispatch.md`. Defect only because inventory.md is bundled — INV-3. LEXICON.md:109 is the tombstone. |
| RV-2 | **sync block** | docs/global-context/inventory.md:78, :159, :172 | Same. LEXICON.md:112 is the tombstone. |
| RV-3 | **track** (the retired directive sense) | docs/global-context/inventory.md:101-102, :187 ("Track A/B is retired") | Same. LEXICON.md:115 is the tombstone; LEXICON.md:118 carves out the ordinary sense, which is what policies/source-of-truth-policy.md:25 and every "tracker issue" use. No misuse found outside inventory.md. |
| RV-4 | **prompt** | docs/global-context/inventory.md:50, :82 | Same. docs/global-context/core.md:45 is the instruction not to use it; LEXICON.md:89-105 is the tombstone with the approval-prompt carve-out. No misuse found. |
| RV-5 | **editor** (retired role) | docs/global-context/inventory.md — 16 lines | Same; all citations of `writing/roles/editor.md`, deleted at eea66dd. INV-2, INV-3. |
| RV-6 | **section-writer** (retired role) | docs/global-context/inventory.md:79, :85, :102, :139, :190 | Same. |
| RV-7 | **instruction-reviewer** (retired role) | none | Clean. |
| RV-8 | **orchestrator** (retired role) | **policies/document-metadata-policy.md:280** — "Orchestrators may select context by `audience`." | **Live defect in a live policy.** The only retired-role occurrence outside inventory.md. No `roles/orchestrator*.md` exists at 8402c23. See DMP-3. |
| RV-9 | **cartographer as a methodology role** | none — every occurrence is the engagement Cartographer (engagements/cartographer.md and the sre set) | Clean. The role is live in the engagement layer; it is not a `roles/` document and that is the CN-2 audience question, not a retirement question. |
| RV-10 | Model names — Opus, Sonnet, Haiku, Claude, GPT, Gemini | **docs/global-context/inventory.md:86** ("Opus / Sonnet / Haiku by work class") — the only occurrence in the corpus | Criterion 8. The row recording the decision to speak in tiers is written in model names, in a bundled file. INV-3. |
| RV-11 | Vendor names outside `vendors/` | operating-model.md:35 and policies/source-of-truth-policy.md:24 — "tracker issues (currently GitHub Issues)"; operating-model.md:164 — "(e.g. OpenFeature)"; engagements/sre/implementer.md:10, system-discovery.md:16, working-with-dave.md:21 — "Terraform or equivalent" | All six are hedged and deliberate. "currently GitHub Issues" and "e.g. OpenFeature" are named as the current instance of a swappable choice, which is what policies/source-of-truth-policy.md:29-42 requires. "Terraform or equivalent" is recorded in docs/batons/baton-20260822T212629.md as a deliberate engagement-shape retention. Criterion 8 restricts *model* selection to tiers and does not reach these. Recorded, not flagged. |
| RV-12 | `vendors/claude-code/environment-config.md` and `vendors/README.md` | "Claude Code" throughout | In `vendors/`, by design, and both carry `audience: [human]` so neither enters a bundle. Clean. |

## Sweep (g) — Boundaries two roles could both claim (criterion 11)

Across the full role set: the ten `roles/` documents, the three top-level engagement roles, and engagements/sre/implementer.md.

| # | Boundary | Role A | Role B | State at 8402c23 |
| --- | --- | --- | --- | --- |
| BD-1 | Reviewing a governed methodology document | roles/context-quality-reviewer.md — rubric review of "every governed instruction document" | roles/spec-reviewer-agent.md — a hard gate on "any canonical document ... the methodology documents equally" | **Open in the role documents.** Resolved in roles/spec-reviewer-agent.md:110-112 and skills/spec-review-cycle.md:16-17, neither of which states it in roles/context-quality-reviewer.md, which cedes only the PRD and TRD. See CQR-2. |
| BD-2 | "A Skeptic" for a finished piece of prose | roles/skeptic-risk-agent.md (gate force) | engagements/skeptic.md (advisory) | **Open.** roles/writer.md:15 names one without saying which; neither document is in the `writer` bundle. See WR-2, TC-3. |
| BD-3 | Assessing state and proposing the next step | roles/chief-of-staff.md:11-24 (decision session, activation behaviour) | engagements/assistant.md (decision session, completion nudges, quiet notes) | **Not open in the corpus** — no bundle contains both, and the domains are disjoint. Recorded because the two role documents describe the same posture in different words, which is where a future merge or a shared bundle would collide. |
| BD-4 | Building the change | roles/coder-agent.md (execution session, implements to spec and test plan) | engagements/sre/implementer.md (execution session, implements to an Improvement Proposal) | **Not open** — disjoint bundles, different upstream artifact. Recorded for the same reason as BD-3. |
| BD-5 | Who may override a procedural step | engagements/sre/override-log-policy.md — Dave may override "any procedural step"; the agent logs and proceeds without arguing | engagements/working-with-dave.md — the client guardrail is "not negotiable, not overridable" | **Open, and delivered broken.** The second document is absent from the `implementer` bundle. This is the largest single finding of the re-gate. See SRE-IMP-1, SRE-OLP-1, WD-1, CN-6. |
| BD-6 | Reviewing the Implementer's own diff | engagements/sre/implementer.md:37 — "does not review its own diff" | engagements/skeptic.md — summoned only, and absent from the `implementer` bundle | **Open.** The Implementer is told not to review its own diff and its bundle names no one who will. engagements/sre/speed-audit.md:26-28, which is in the bundle, says "the Skeptic reviews where a review is requested" — leaving who requests it, and what happens when nobody does, to inference. |
| BD-7 | Proposing an improvement | engagements/sre/speed-audit.md:34-36 — "The Cartographer does not propose; the Implementer does not self-authorize"; the Assistant drafts | engagements/cartographer.md:23-25 — "hand that to Dave — he decides" | **Closed, and well.** The one place in the engagement pack where a boundary is stated explicitly in both directions. Recorded so the sweep is visibly complete. |
| BD-8 | Emitting a ship recommendation | roles/skeptic-risk-agent.md:124-128 — does not emit one | roles/release-manager-agent.md:52-57 — owns it | **Closed.** Both state it; skills/evidence-review.md:32-36 restates it, which is DR-19. |

## Confirmation pass — one line per file

43 files. 33 clean, 10 with findings. A clean line means the file was read whole against all eleven criteria at 8402c23 and nothing in it fails at the current foundation; cross-file matters are in the sweeps above and are not counted against the file here.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| LEXICON.md | ready-with-findings | 1 non-blocking | reviews/LEXICON-cycle-13.md |
| boundaries/human-review-boundary.md | ready | none | — |
| context-sets/production-grade-software.md | ready | none | — |
| context-sets/spec-and-change-discipline.md | ready | none | — |
| context-sets/testing-and-verification.md | ready | none | — |
| docs/global-context/core.md | ready | none | — |
| docs/global-context/decision-layer.md | ready | none | — |
| docs/global-context/inventory.md | changes-required | 2 blocking, 2 non-blocking | reviews/inventory-cycle-1.md |
| docs/global-context/review-rubric.md | ready-with-findings | 2 non-blocking | reviews/review-rubric-cycle-1.md |
| engagements/assistant.md | ready | none | — |
| engagements/cartographer.md | ready | none | — |
| engagements/skeptic.md | changes-required | 1 blocking, 1 non-blocking | reviews/skeptic-cycle-2.md |
| engagements/working-with-dave.md | changes-required | 1 blocking | reviews/working-with-dave-cycle-3.md |
| operating-model.md | ready | none | — |
| policies/commit-and-change-control-policy.md | ready | none | — |
| policies/decision-log-policy.md | ready | none | — |
| policies/document-metadata-policy.md | changes-required | 2 blocking, 1 non-blocking | reviews/document-metadata-policy-cycle-14.md |
| policies/project-setup-requirements.md | ready-with-findings | 1 non-blocking | reviews/project-setup-requirements-cycle-2.md |
| policies/release-readiness-policy.md | ready | none | — |
| policies/remote-write-verification-policy.md | ready | none | — |
| policies/source-of-truth-policy.md | ready | none | — |
| policies/verification-boundary-policy.md | ready | none | — |
| roles/architect-agent.md | ready | none | — |
| roles/chief-of-staff.md | ready | none | — |
| roles/coder-agent.md | ready | none | — |
| roles/context-quality-reviewer.md | changes-required | 1 blocking, 1 non-blocking | reviews/context-quality-reviewer-cycle-2.md |
| roles/release-manager-agent.md | ready | none | — |
| roles/reviewer-agent.md | ready | none | — |
| roles/skeptic-risk-agent.md | ready | none | — |
| roles/spec-reviewer-agent.md | ready | none | — |
| roles/test-designer-agent.md | ready | none | — |
| skills/boundary-audit.md | ready | none | — |
| skills/command-blocks.md | ready | none | — |
| skills/conversation-retro.md | ready | none | — |
| skills/directive-authoring.md | ready-with-findings | 2 non-blocking | reviews/directive-authoring-cycle-1.md |
| skills/evidence-review.md | ready | none | — |
| skills/review-artifact.md | changes-required | 1 blocking, 2 non-blocking | reviews/review-artifact-cycle-1.md |
| skills/spec-review-cycle.md | ready | none | — |
| skills/test-plan-review.md | ready | none | — |
| specs/prd-template.md | ready | none | — |
| specs/trd-template.md | ready | none | — |
| vendors/README.md | ready | none | — |
| vendors/claude-code/environment-config.md | ready | none | — |

## First-cycle reviews — one line per file

Nine files, each a full first-cycle review with criterion 10 answered first. All nine were produced by directive and had never been rubric-reviewed at any cycle.

| File | Verdict | Findings | Artifact |
| --- | --- | --- | --- |
| engagements/sre/README.md | changes-required | 1 blocking, 2 non-blocking | reviews/sre-README-cycle-1.md |
| engagements/sre/baseline-measurement.md | changes-required | 1 blocking, 2 non-blocking | reviews/sre-baseline-measurement-cycle-1.md |
| engagements/sre/engagement-change-package.md | changes-required | 2 blocking, 1 non-blocking | reviews/sre-engagement-change-package-cycle-1.md |
| engagements/sre/implementer.md | changes-required | 2 blocking | reviews/sre-implementer-cycle-1.md |
| engagements/sre/override-log-policy.md | changes-required | 1 blocking, 1 non-blocking | reviews/sre-override-log-policy-cycle-1.md |
| engagements/sre/speed-audit.md | changes-required | 1 blocking, 2 non-blocking | reviews/sre-speed-audit-cycle-1.md |
| engagements/sre/system-discovery.md | changes-required | 2 blocking | reviews/sre-system-discovery-cycle-1.md |
| roles/writer.md | changes-required | 2 blocking, 1 non-blocking | reviews/writer-cycle-1.md |
| prose-criteria.md | changes-required | 2 blocking, 3 non-blocking | reviews/prose-criteria-cycle-1.md |

---

## The single largest reconciliation problem

**The `implementer` bundle contains the rule that every procedural element of the engagement pack is trivially overridable, and does not contain the one rule in the corpus marked "not negotiable, not overridable."** engagements/working-with-dave.md carries `audience: [assistant, cartographer, skeptic, human]`; the `implementer` role was created at 0e07753, eleven days after that file's last review, and was never added. The role that writes code against a client's systems is therefore the only engagement role that never receives "You have zero write access to the client's cloud and systems," while receiving engagements/sre/override-log-policy.md's instruction that overrides are logged and not argued with. No single-file cycle could see it: each of the two files is internally correct.

## Departures from the directive

Two things could not be executed as written. Neither blocked the work; both change what the report means.

1. **The never-reviewed set is twelve files, not nine.** The directive names `engagements/sre/` (7), roles/writer.md, and prose-criteria.md, and its Context says "three documents were produced by directive without ever being reviewed." A mechanical check of every `reviews/*.md` filename at 8402c23 against every in-scope file's stem finds four more with no artifact under any stem: **docs/global-context/review-rubric.md** and **docs/global-context/inventory.md** (never reviewed at any path), and **skills/directive-authoring.md** and **skills/review-artifact.md** (created at 1bbd5b7 as the products of cycle 22's revision, reviewed nine times each under their predecessors' stems — `directive-dispatch` and `spec-review-cycle` — and never under their own). All four were handled in the confirmation pass and carry cycle-1 artifacts, since their stems have no prior. They are counted in the confirmation-pass table above, not in the first-cycle table, because the directive's first-cycle instruction names nine specific files and this session did not widen it. The review rubric being among the never-reviewed is worth stating plainly: the document that defines the eleven criteria has never been examined against them until now.

2. **The tree is at 31aa0c3, not 8402c23.** Instruction 1 says to verify the tree is at 8402c23 with no later edits. HEAD is one commit later: 31aa0c3, the merge of PR #127, which adds `docs/cycles/pass1-regate-directive-20260822T220500.md` and nothing else. `git diff --name-status 8402c23 31aa0c3` returns that single addition, which is under `docs/cycles/` and therefore outside the scope this directive defines. Every file in the enumerated set is byte-identical at both SHAs, so every reading and every sweep in this artifact holds at 8402c23 as the directive requires. Recorded rather than silently absorbed, per Core rule 11.

Also noted, and not acted on: the review-artifact filename convention has no rule for a basename that repeats, and this cycle needed one — `engagements/sre/README.md` collides with `vendors/README.md` and with the retired root `README.md`, all three mapping to the stem `README`. The directive dictates `sre-<basename>` for the seven engagement files, which resolved it here; the convention itself does not authorize that form. See RA-1.

No document was edited. No status was flipped. No finding was resolved.
