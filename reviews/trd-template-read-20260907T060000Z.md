# Review: process/trd-template.md — process-sweep-read-20260907T060000Z

Verdict: ready-with-findings
Reviewed: process/trd-template.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/trd-template.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 59 lines, with all nine bracketed ids — R0497, R0499, R0500, R0862b, R0871, R1541, R1542, R1543, R1573 — resolved to their files under rules/ at the base ref, and each of the nine template sections compared field by field against the baseline.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; process/prd-template.md at the same ref, since the two documents were swept the same way and share the NFR dimension list; rules/R0483.md, for the tracker-issue derivation the baseline stated here.
Not inspected: any project TRD written against this template. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 2 — 0 blocking, 2 non-blocking
The human should inspect: nothing that changes the document's substance. Both findings are placement, not content.

## Verdict (citations): ready-with-findings

Eight of nine resolve cleanly. `[R0871, R1541, R1542, R1543]` on the opening sentence is exact on all three of its claims: R0871 gives the standing, slow-moving specification and the human's agreement, R1541 the Architect's drafting, R1542 the not-in-force-until-agreed condition the sweep cut from the third paragraph, R1543 the maintenance obligation that "maintained by" carries. `[R0862b]` establishes the per-change architecture summary as the home for per-feature design, which is what the clause it sits on relies on. `[R0497, R0499, R0500]` in §7 covers all three limbs — deploy and release as separate events, the flag or canary mechanism separating them, and the vendor-neutral flag interface with an owner and a removal trigger, which is what the baseline's "a flag backend chosen in the TRD and swappable" said. `[R1573]` is TT-01.

One clause left this document without a citation: the baseline's "tracker issues are derived from it, by way of that summary." R0483 states it and process/change-flow.md cites R0483 at the same ref, so it is carried in the corpus and I record no finding.

## Verdict (loss): ready

Every obligation and required-content item survives or is cited. Checked section by section: §2 keeps the SLO, the measurement mechanism, the alerting threshold, and the unverified-journey rule, dropping only the examples of each; §3 keeps every component, interface, dependency class, and the durable-boundary declaration with what verifying it would take; §4 keeps all four per-boundary items and turns the baseline's exclusion ("per-change boundary movement is recorded in the change's architecture summary, not here") into the positive form the sweep's sixth criterion asks for — "each per-change boundary movement made permanent"; §5, §6, and §9 keep their content and lose their reasons; §7 keeps the release model, the flag mechanism by citation, and the go/no-go routing mechanism; §8 keeps all nine NFR dimensions, the `N/A` option, and the technical non-goals. The nine per-dimension definitions in §8 collapse into one general instruction — "the concrete technical target or constraint, or `N/A`" — which is the sweep's eighth criterion applied, not a loss. "Copy this into a project TRD" goes with the "## Skeleton" heading and the block standing in for it. The `status`/`last-reviewed` note is the document's record of what retired under DEC-000380 and goes correctly under criterion 4.

## Verdict (residue): ready

Every sentence is a form or a content requirement on a section of it. "Keep each section short" survives; "This is an anchor, not an essay" does not. "What this is" and its canonicity paragraph are gone.

## Verdict (keys): ready-with-findings

See TT-02.

## Verdict (loadable): ready

The nine numbered items match the skeleton block's nine headings exactly, in order and by title. Nothing refers to a heading that was cut — the baseline's `### 1.` through `### 9.` headings became the numbered list itself.

## TT-01 — non-blocking
Claim: `[R1573]` sits on the clause naming the technical non-goals; R1573 is "Prefer boring, understandable designs", which that clause does not rely on.
Location: process/trd-template.md:38 — "the concrete technical target or constraint, or `N/A`; then the technical non-goals [R1573]."
Evidence: Read by inspection against the diff. In the baseline, §8 ended with two sentences: "State the explicit technical non-goals — what this architecture deliberately does not attempt. Prefer boring, understandable designs." The sweep cut the second and put its row's id at the end of the first, which is the substitution its seventh criterion asks for; the id simply landed on a neighbouring clause rather than its own.
Consequence: An agent resolving R1573 to learn what a technical non-goal is gets a design preference instead. Nothing is lost — R1573 is in force and its substance is carried — but the design preference is now filed where a reader looking for it will not look, and the id misdescribes the clause it annotates. The clause it annotates is a template section requirement, governed by this document rather than by a row, so no obligation is falsely presented as governed.
Fix: Give R1573 its own clause — "; then the technical non-goals, preferring boring, understandable designs [R1573]" — or move the id to a sentence of its own alongside "Keep each section short."

## TT-02 — non-blocking
Claim: `spec-reviewer-agent` is in the role list but performs no act in the document since the sweep cut the sentence that gave it one.
Location: process/trd-template.md:3 — `role: [architect-agent, spec-reviewer-agent]`
Evidence: Read by inspection against the diff. The role list is unchanged. In the baseline the Spec Reviewer's act was the opening line, "Read in a decision session drafting a TRD and in an execution session gating one" — the gating half. The sweep cut that line, correctly, since the `session:` key carries the same information. The Architect keeps a named act ("drafted and maintained by the Architect"); the Spec Reviewer is now named nowhere and no surviving sentence describes gating.
Consequence: Under the sweep's ninth criterion the list should name the roles that perform an act the document describes. As it stands the key is defensible on a different ground — the Spec Reviewer gates a TRD against this form and needs the form selected into its bundle — but that ground is no longer stated anywhere in the document, so the key cannot be checked against the text. process/prd-template.md has the identical defect for both of its roles.
Fix: Either accept the key on the "gated against this form" ground and record that reasoning in the sign-off, or restore one clause naming the gate — the sweep's criterion 9 asks for the reasoning per document, and this is the case where the reasoning is not derivable from the document itself.
Related: PT-01 in reviews/prd-template-read-20260907T060000Z.md
