# Review: engagements/sre/baseline-measurement.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/baseline-measurement.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 47 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at 0e07753 (cycle 25), never rubric-reviewed. One of the seven-file `engagements/sre/` set.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md (Evidence classes), operating-model.md, engagements/working-with-dave.md (Infra verification ladder), and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether p50/p95 is the right distribution summary as a matter of engineering judgment; the four failure modes' completeness.
Findings: 3 — 1 blocking, 2 non-blocking
Prior cycle: none
Dave should inspect: none — all three have a single obvious fix.

## SRE-BM-1 — blocking
Claim: Step 4 places the published baseline beside an artifact whose definition is absent from one of this file's own bundles.
Location: engagements/sre/baseline-measurement.md:22-26 ("Publish the baseline — one document, beside the System Map in the engagement working area")
Evidence: Verified by running — both "System Map" and "engagement working area" are defined only in engagements/sre/system-discovery.md, whose `audience:` is `[cartographer, assistant, human]`. This file's `audience:` is `[cartographer, implementer, assistant, human]`, so it reaches the `implementer` bundle (23 files) where system-discovery.md is absent. Criterion 1.
Consequence: An Implementer session running step 4 is told where to put the baseline in terms of two artifacts its bundle does not define, and step 6's re-measurement — the one an Implementer actually performs — depends on finding the published baseline again.
Fix: Covered by SRE-SD-2's `audience:` change. If the definitions move to engagements/sre/README.md instead, this reference resolves there.
Related: SRE-SD-2

## SRE-BM-2 — non-blocking
Claim: The file opens by restating a sentence engagements/sre/README.md states twice in the same bundle.
Location: engagements/sre/baseline-measurement.md:12-15 ("**The baseline is the failing test.** No optimization is implemented until the stopwatch exists, the baseline is captured, and the expected delta is stated in advance.") against engagements/sre/README.md:31-33 and :52
Evidence: Verified by running — engagements/sre/README.md carries `audience: [assistant, cartographer, skeptic, implementer, human]` and is therefore in every bundle this file reaches. The sentence and its following clause are near-verbatim; README says "the baseline distribution is captured," this file says "the baseline is captured." Criterion 6, criterion 10.
Consequence: One rule, three statements, one bundle, already differing by one word. Criterion 10 asks what this file contributes that no other file in the bundle states; the opening paragraph contributes nothing.
Fix: Cut the restatement and open at "The baseline-gate procedure." The six steps are what this file uniquely holds.

## SRE-BM-3 — non-blocking
Claim: The Override section restates the override protocol that engagements/sre/override-log-policy.md holds in every bundle this file reaches.
Location: engagements/sre/baseline-measurement.md:37-40 against engagements/sre/override-log-policy.md:11-30
Evidence: Verified by running — override-log-policy.md carries `audience: [assistant, cartographer, skeptic, implementer, human]` and is in all four of this file's bundles. It already states that the baseline-gate specifically is overridable, that the override is logged, and that the agent proceeds without arguing. This file adds one thing the policy does not state: "The measurement debt is named in the change package." Criterion 4's neighbourhood; recorded against criterion 10.
Consequence: The overridable-set rule now has two homes with slightly different scope — the policy says "for a given change ... with an explicit statement, logged," this file says the same for the baseline-gate — and the one genuinely new clause is buried inside the duplicate.
Fix: Cut the section to its one new sentence: "An override of this gate names the measurement debt in the change package."
