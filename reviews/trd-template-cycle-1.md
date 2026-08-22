# Review: specs/trd-template.md — cycle 1

Verdict: changes-required
Reviewed: specs/trd-template.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 190 lines, against all eleven criteria of the review rubric @ 1bbd5b7.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, specs/prd-template.md, policies/document-metadata-policy.md, policies/verification-boundary-policy.md, roles/architect-agent.md, roles/spec-reviewer-agent.md — all @ 1bbd5b7.
Not inspected: any instantiated project TRD (none exists in this repo); whether the nine required sections are the right technical taxonomy (engineering judgment, ceded per the role); the referenced `boundaries/` files beyond confirming which survive.
Findings: 13 — 9 blocking, 3 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: TRD-6 (`blocking` is listed as a verification class, which contradicts LEXICON — this is a substantive error, not a wording one) and TRD-9 (whether the authoring checklist moves to the Spec Reviewer's role document).

## Criterion 10 first

**Disposition: retain-with-changes.**

Same answer as the PRD template and for the same reason: this is **agent
context, not a human-facing form.** The Architect Agent drafts a TRD from it
and the Spec Reviewer gates one against it. The required-section list and the
section-4 verification-boundary field list are things no other file in those
bundles states.

`audience: [all-roles, human]` is wrong for the same reason it is wrong on the
PRD template: a Coder Agent and a Test Designer never author or gate a TRD.

**Proposed `audience:` — `[architect-agent, spec-reviewer-agent, human]`.**
No `order:`.

One structural point that outranks the individual findings: this template
carries *more* foundation rules than the PRD template does — the release model,
the flag mechanism, the evidence classes, and the change-flow role assignments
are all restated here. A template that carries a rule carries it into every
instantiated TRD, in project repos where this repo's enforcement does not reach.
The instantiated TRD is the worst possible place for a second copy of a rule,
because nothing here can ever correct it.

## TRD-1 — blocking
Claim: `audience: [all-roles, human]` selects an authoring template into every agent's bundle, including agents that never author or gate a TRD.
Location: specs/trd-template.md:4
Evidence: verified by reading the frontmatter; audience values in use enumerated by running a `git grep` tally over `1bbd5b7`, which confirms `architect-agent` and `spec-reviewer-agent` are established values.
Consequence: 190 lines of TRD-authoring form in bundles that cannot act on it.
Fix: replace with `audience: [architect-agent, spec-reviewer-agent, human]`.
Related: PRD-1.

## TRD-2 — blocking
Claim: §2 restates the Top K inheritance rule that LEXICON already states.
Location: specs/trd-template.md:59 ("Inherit the Top K journeys from the PRD (section 3). Do not redefine them here.")
Evidence: verified by reading LEXICON.md @ 1bbd5b7, "Service levels": "The list is defined once, in the PRD; the TRD sets SLO targets against it and does not redefine it."
Consequence: the rule is stated twice in one bundle and copied into every instantiated TRD. The copy also carries a hard-coded cross-document section number ("section 3") that breaks the moment a project reorders its PRD.
Fix: cut line 59. LEXICON's definition of Top K already carries both halves; §2's remaining content (the SLO / measurement / alerting field list) is the part that is genuinely this template's.
Related: PRD-2.

## TRD-3 — blocking
Claim: the source-of-truth rule and its hard stop are restated from operating-model.md.
Location: specs/trd-template.md:41–44
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Source of truth", which states the derived-artifact rule and the hard stop in full.
Consequence: a second home for a hard-stop rule, carried into project repos. A hard stop that exists in two wordings is a hard stop that can be argued about.
Fix: cut lines 41–44. The tree diagram above them already shows the derivation direction.
Related: PRD-6.

## TRD-4 — blocking
Claim: "GitHub Issues" names a vendor twice in rules that are about derived artifacts, not about that vendor.
Location: specs/trd-template.md:38, :41
Evidence: verified by running a name sweep; cross-checked against operating-model.md @ 1bbd5b7, which hedges the same fact as "tracker issues (currently GitHub Issues)".
Consequence: an instantiated TRD in a project on any other tracker states a false fact about itself.
Fix: "tracker issues" in both places.
Related: PRD-5.

## TRD-5 — blocking
Claim: §7 restates the release model — the deploy/release distinction, where the human go/no-go sits, and the flag mechanism with a vendor-neutral interface, an owner, and a removal trigger — all of which operating-model.md states.
Location: specs/trd-template.md:111–121
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Release gate": "*Deploy* (code on prod) and *release* (functionality exposed to users) may be separate events… When deploy and release are separated, the usual mechanism is **feature flags**… Depend on a **vendor-neutral flag interface** (e.g. OpenFeature)… Every flag has an owner and a removal trigger".
Consequence: the release-gate rule now has two homes, and the copy is the one that lands in project repos. If the gate's two-tier structure changes, every instantiated TRD still carries the old shape.
Fix: cut to the one instruction that is genuinely the TRD's own: "State this project's release model: whether deploy and release are separate events, and where the release decision sits relative to commit and deploy." Delete the flag-mechanism paragraph entirely — it is guidance about how to build, which the operating model already gives.

## TRD-6 — blocking
Claim: §4 lists `blocking` as a verification class. It is not one — it is a release impact label, from a different LEXICON list.
Location: specs/trd-template.md:86–89
Evidence: verified by reading LEXICON.md @ 1bbd5b7. "Evidence classes" contains mock-verified, contract-verified, live-verified, browser-verified, production-verified, unverified, deferred verification, accepted risk. "Release impact labels" — a separate list — contains `blocking`, `deferred`, `accepted-risk`, `not-material`. The template's line 89 merges the two lists and adds `blocking` to the wrong one.
Consequence: an Architect instantiating a TRD labels a standing boundary `blocking`, which reads as an evidence claim ("we verified it as blocking") when it is in fact a release judgment about a gap. Two of the nine listed values (`deferred`, `accepted-risk`) appear in both LEXICON lists with different meanings, so the merged list is ambiguous at three of nine positions. This is a substantive error that survives into every instantiated TRD.
Fix: cut the enumeration and name the LEXICON list instead — "its evidence class, per the evidence classes" — so there is one list, in one place. If an inline list is kept, remove `blocking` and state that release impact labels are a separate vocabulary applied at the release decision, not here.

## TRD-7 — blocking
Claim: the enumeration in §4 restates LEXICON's evidence classes, so the class vocabulary has two homes.
Location: specs/trd-template.md:86–89
Evidence: verified by reading LEXICON.md @ 1bbd5b7, "Evidence classes".
Consequence: as TRD-6, plus the ordinary drift case — a class added to LEXICON never reaches the instantiated TRDs.
Fix: as TRD-6.
Related: TRD-6.

## TRD-8 — blocking
Claim: the relationship diagram restates the change flow's stages and their role assignments from operating-model.md.
Location: specs/trd-template.md:30–39
Evidence: verified by reading operating-model.md @ 1bbd5b7, "Change flow" steps 2–5, which assign acceptance criteria to Dave, the architecture summary to the Architect, the test plan to the Test Designer, and implementation to the Coder — the same four assignments the diagram makes.
Consequence: the change flow now has a second, abbreviated statement that omits the red gate, the quality review, the skeptic/risk review, and the release gate. A reader who takes the diagram as the flow is missing four of nine stages, including the mandatory one.
Fix: cut the per-unit-of-work half of the diagram (lines 33–38). The PRD→TRD line is the only part that states this document's own position.

## TRD-9 — blocking
Claim: the Authoring checklist is the Spec Reviewer's inspection list, stated in a document the Spec Reviewer does not own.
Location: specs/trd-template.md:149–161
Evidence: verified by reading roles/context-quality-reviewer.md @ 1bbd5b7 and skills/review-artifact.md @ 1bbd5b7, which put "what must be inspected and what must be reported" in role documents.
Consequence: the gate's criteria live in the artifact being gated, and are copied into project repos. Item 7 ("no value updated in one place and stale in another") is Core rule 13 restated a third time.
Fix: move the seven items into roles/spec-reviewer-agent.md; delete the section here. Dave's call, as with PRD-8.
Related: PRD-8.

## TRD-10 — non-blocking
Claim: five path-shaped references assume the reader can open another file.
Location: specs/trd-template.md:44, :79, :109, :116, :168
Evidence: verified by running a path sweep over the file.
Consequence: an agent holding only a bundle cannot resolve any of them.
Fix: state the needed rule inline or drop the reference. In four of five cases the surrounding text already states the rule, so the citation is removable without loss; line 79's boundary-declaration requirement is the one that needs a sentence of its own if the citation goes.

## TRD-11 — non-blocking
Claim: three vendor names appear as examples of a flag backend.
Location: specs/trd-template.md:119 (OpenFeature), :120 (Flipt, Flagsmith)
Evidence: verified by running a name sweep. operating-model.md @ 1bbd5b7 names OpenFeature once, parenthetically, in the same "e.g." form; it does not name Flipt or Flagsmith.
Consequence: two vendor names that exist nowhere else in the governed set, in a document copied into project repos, dating the template to whatever the flag market looked like when it was written.
Fix: the whole paragraph goes under TRD-5. If any of it survives, cut the backend names and keep "name the backend as a swappable choice".

## TRD-12 — non-blocking
Claim: the skeleton preamble restates the document-metadata rules.
Location: specs/trd-template.md:167–170
Evidence: verified by reading policies/document-metadata-policy.md @ 1bbd5b7; the two sentences here are identical in substance to specs/prd-template.md:128–131.
Consequence: a third statement of the metadata schema, in the place enforcement cannot reach.
Fix: cut both sentences; the skeleton block shows the shape.
Related: PRD-11.

## TRD-13 — observation
Claim: three uses of **track** appear in forms LEXICON retired, all under a carve-out LEXICON also states.
Location: specs/trd-template.md:38 ("tracking only"), :69 ("track it as an open question"), :145 ("Track these as loose ends")
Evidence: verified by running a term sweep, then verified by reading LEXICON.md @ 1bbd5b7, "Retired terms", whose carve-out covers "**track**, **tracking**, and **tracker** in the ordinary sense of keeping or consulting a record".
Consequence: none for the agent. Recorded because the cycle directive instructs that every use be flagged; on LEXICON's current text all three are licensed.
Fix: none required. Line 38 changes anyway under TRD-4.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.

## Sweep counts

- Rules restated from the foundation: **6** (TRD-2 Top K inheritance; TRD-3 source of truth; TRD-5 release model; TRD-5 flag mechanism; TRD-7 evidence classes; TRD-8 change flow)
- Output-shape lists with a home elsewhere: **2** (TRD-9 authoring checklist; §4's verification-boundary field list, whose home is policies/verification-boundary-policy.md)
- Path-shaped references: **5** (lines 44, 79, 109, 116, 168)
- Vendor and model names: **5** (GitHub ×2, lines 38 and 41; OpenFeature, line 119; Flipt and Flagsmith, line 120)
- Retired terms: **0 defects**, 3 carve-out uses recorded (TRD-13)
- SLO / Top K copies: **1** (§2, lines 57–70)
