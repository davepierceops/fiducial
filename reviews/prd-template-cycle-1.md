# Review: specs/prd-template.md — cycle 1

Verdict: changes-required
Reviewed: specs/prd-template.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 153 lines, against all eleven criteria of the review rubric @ 1bbd5b7.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, specs/trd-template.md, policies/document-metadata-policy.md, roles/spec-reviewer-agent.md — all @ 1bbd5b7.
Not inspected: any instantiated project PRD (none exists in this repo, and instantiated specs are out of the frontmatter scope); the behaviour of `bin/bundle` against this file's frontmatter; whether the Top K bound of 9 is the right product judgment (that is not this role's call — see the role's "What it cedes").
Findings: 12 — 8 blocking, 3 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: PRD-1 (who should actually receive this template in a bundle) and PRD-8 (whether the authoring checklist moves to the Spec Reviewer's role document or is deleted outright).

## Criterion 10 first

**Disposition: retain-with-changes.**

This template is **agent context, not a human-facing form.** The instantiated
PRD is out of the frontmatter scope, but the template itself is read by an
agent drafting a PRD and by the Spec Reviewer gating one. It contributes
something no other file states: the required section list for a PRD and the
shape of a Top K journey entry. That earns its place.

It does not earn its place in *every* bundle. `audience: [all-roles, human]`
selects it into a Coder's bundle and a Test Designer's bundle, neither of which
ever writes or gates a PRD.

**Proposed `audience:` — `[chief-of-staff, spec-reviewer-agent, human]`.**
No `order:`; the file's position relative to others in those bundles does not
matter.

Everything below is the edit list an executor can apply.

## PRD-1 — blocking
Claim: `audience: [all-roles, human]` selects an authoring template into every agent's bundle, including agents that never author or gate a PRD.
Location: specs/prd-template.md:4
Evidence: verified by reading the frontmatter against the audience values in use — enumerated by running `git grep -h -A5 '^audience:' 1bbd5b7 -- '*.md'` and tallying, which shows `all-roles` on 27 files and role-specific values (`chief-of-staff`, `spec-reviewer-agent`) already established.
Consequence: a Coder Agent's bundle carries 153 lines of PRD-authoring form it will never act on, displacing context it needs, and inviting it to treat PRD authorship as in its lane.
Fix: replace with `audience: [chief-of-staff, spec-reviewer-agent, human]`.

## PRD-2 — blocking
Claim: §3 restates the Top K definition and the PRD-defines/TRD-inherits rule that LEXICON already states, and carries it into every instantiated PRD where it will drift.
Location: specs/prd-template.md:43–59 ("Define the **Top K** journeys … These journeys are inherited by the TRD, which defines SLOs for each.")
Evidence: verified by reading LEXICON.md @ 1bbd5b7, "Service levels": "**Top K** — the K most important user journeys of a product. The list is defined once, in the PRD; the TRD sets SLO targets against it and does not redefine it."
Consequence: two definitions of Top K in the same bundle. When the bound (1–9) or the inheritance rule changes in LEXICON, every PRD instantiated from this template still carries the old text, and the drift is invisible because instantiated PRDs live in project repos this repo's enforcement does not reach.
Fix: cut lines 43–51 and line 59 down to a section heading plus the per-journey field list (actor, trigger, steps, expected outcome), which is the only part LEXICON does not state. Let the term carry its LEXICON meaning.
Related: PRD-3, TRD-2.

## PRD-3 — blocking
Claim: the authoring checklist repeats §3's Top K rules a second time within this same document.
Location: specs/prd-template.md:113–114
Evidence: verified by reading — lines 113–114 restate the actor/trigger/steps/outcome fields and the "K is between 1 and 9" bound already stated at 43–57.
Consequence: three copies of the same rule (LEXICON, §3, checklist) in one bundle; a corrective edit that catches two of three produces a document that contradicts itself.
Fix: delete both checklist lines with the rest of the checklist (PRD-8).
Related: PRD-2.

## PRD-4 — blocking
Claim: "Claude drafts, Dave verifies" names a vendor's product inside a governed, vendor-neutral document.
Location: specs/prd-template.md:22
Evidence: verified by running a name sweep over the file; also verified by reading operating-model.md @ 1bbd5b7, whose Agents section says agents "may … write specifications" without naming any vendor, and whose Must-not list forbids storing durable policy only in vendor-specific tooling.
Consequence: the rule stops being true the moment a different agent runner drafts the PRD, and it is copied into every instantiated PRD, which then reads as a vendor commitment the methodology does not make.
Fix: "Agents draft; Dave verifies." The preceding clause on line 21–22 already says this, so the sentence can simply be cut.

## PRD-5 — blocking
Claim: "GitHub Issues" names a vendor in a rule that is about derived artifacts, not about that vendor.
Location: specs/prd-template.md:27
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Source of truth", which writes the same rule as "tracker issues (currently GitHub Issues)" — hedged as a current choice, not stated flat as this line does.
Consequence: an instantiated PRD in a project using any other tracker states a false fact about itself, and the reader cannot tell whether the tracker choice is methodology or accident.
Fix: "tracker issues".
Related: TRD-4.

## PRD-6 — blocking
Claim: the source-of-truth rule is restated from operating-model.md rather than left to it.
Location: specs/prd-template.md:26–29
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Source of truth": "Specifications are canonical. Everything downstream of them … is a **derived artifact** … If a derived artifact conflicts with a canonical one … it is a **hard stop**."
Consequence: the rule now has two homes, one of which is copied into every instantiated PRD. When the hard-stop condition changes, the copies do not.
Fix: cut lines 26–29. The one thing worth keeping — that the PRD is the parent of the TRD and the source ACs derive from — survives in a single sentence with no rule attached.
Related: TRD-3.

## PRD-7 — blocking
Claim: the Authorship section restates Dave's ownership list from operating-model.md and Core rule 2.
Location: specs/prd-template.md:19–22
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Dave / Owns" (product direction, user value, prioritization, acceptance criteria, …) and core.md @ 1bbd5b7 Standing rule 2 ("Dave decides. You propose. Agreement, release, prioritization, and publication are his.").
Consequence: an agent in a bundle reads the ownership list twice, in two wordings, and the shorter one here omits risk tolerance and release decisions — so the copy is already lossy relative to its source.
Fix: cut the section. If a line is needed, "The PRD is not in force until Dave agrees" is the only content not already in Core.

## PRD-8 — blocking
Claim: the Authoring checklist is the Spec Reviewer's output shape, stated in a document the Spec Reviewer is not the owner of.
Location: specs/prd-template.md:108–122
Evidence: verified by reading roles/context-quality-reviewer.md @ 1bbd5b7 ("Role documents govern the review: what must be inspected and what must be reported" — skills/review-artifact.md) and roles/spec-reviewer-agent.md @ 1bbd5b7.
Consequence: what the Spec Reviewer must confirm now lives in the template, so a change to the Spec Reviewer's obligations has to be made in two places; and the checklist is carried into every instantiated PRD, where a project-local copy of a gate's criteria is exactly the drift this repo exists to prevent.
Fix: move the eleven items into roles/spec-reviewer-agent.md as that role's PRD inspection list, and delete the section here. Dave's call on whether they move or are dropped as already implied by the required-sections list.

## PRD-9 — non-blocking
Claim: "the Spec Reviewer should confirm" states a hard gate in permissive language.
Location: specs/prd-template.md:110
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Change flow" step 1: "reviewed by the Spec Reviewer Agent (**hard gate**)".
Consequence: an agent reading "should" can conclude the gate is advisory and proceed to step 2 without it — criterion 11, wording that lets the agent decide what is Dave's.
Fix: if the section survives PRD-8, "must confirm". If it moves to the role document, the role document states the obligation and this wording disappears.

## PRD-10 — non-blocking
Claim: three path-shaped references assume the reader can open another file.
Location: specs/prd-template.md:29 (`policies/source-of-truth-policy.md`), :128–129 (`policies/document-metadata-policy.md`), and :113/:59 which point at "the TRD" by section number ("PRD section 3" convention is used from the other side at trd-template.md:59).
Evidence: verified by running a path sweep over the file.
Consequence: an agent that received only a bundle cannot resolve them and has no way to know what it is missing.
Fix: state what is needed inline, or drop the reference. Both cited policies' relevant rules are already stated inline immediately around the citation, so the citations are removable without loss.

## PRD-11 — non-blocking
Claim: the skeleton preamble restates the document-metadata rules.
Location: specs/prd-template.md:128–131 ("`status: agreed` requires a non-null `last-reviewed`; the document's version is its git SHA — no per-document version numbers.")
Evidence: verified by reading policies/document-metadata-policy.md @ 1bbd5b7, "Versioning" and the status-transition rules.
Consequence: the metadata schema now has a second statement, copied into project repos where the policy's enforcement does not reach — so a schema change silently strands every instantiated PRD.
Fix: cut the two sentences; the skeleton block below them already shows the frontmatter shape, which is the part a copier needs.

## PRD-12 — observation
Claim: "downstream tracking artifacts" uses **track** in a form LEXICON retired, under a carve-out LEXICON also states.
Location: specs/prd-template.md:27
Evidence: verified by reading LEXICON.md @ 1bbd5b7, "Retired terms": "**Track** — retired 2026-08-21" and, immediately after, "*Not covered by this retirement:* **track**, **tracking**, and **tracker** in the ordinary sense of keeping or consulting a record".
Consequence: none for the agent. Recorded because the cycle directive instructs that every use of a retired term be flagged, and because the count matters for the sweep; on LEXICON's current text this use is licensed and is not a defect.
Fix: none required. The line changes anyway under PRD-5.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.

## Sweep counts

- Rules restated from the foundation: **3** (PRD-2, PRD-6, PRD-7)
- Output-shape lists with a home elsewhere: **1** (PRD-8)
- Path-shaped references: **2** (line 29, line 129)
- Vendor and model names: **2** (Claude, line 22; GitHub, line 27)
- Retired terms: **0 defects**, 1 carve-out use recorded (PRD-12)
- SLO / Top K copies: **3** (§3 body; checklist line 113; checklist line 114)
