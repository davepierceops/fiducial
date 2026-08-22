# Review: engagements/sre/engagement-change-package.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/engagement-change-package.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 31 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at 0e07753 (cycle 25), never rubric-reviewed. One of the seven-file `engagements/sre/` set.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md (Evidence classes), operating-model.md (Change package), engagements/working-with-dave.md, docs/batons/baton-20260822T212629.md (for the recorded session-kind fiat), and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether seven items is the right size for a lean package; the archived Comfy package shape.
Findings: 3 — 2 blocking, 1 non-blocking
Prior cycle: none
Dave should inspect: SRE-ECP-3 — the baton records this session-kind call as a deliberate fiat ("pick one, it'll probably be wrong"). The finding is that the fiat and the `audience:` disagree, which is a different question from whether the fiat was right.

## SRE-ECP-1 — blocking
Claim: Item 3 requires citing the baseline, and the baseline procedure is absent from one of this file's two execution bundles.
Location: engagements/sre/engagement-change-package.md:17-18 ("**Expected delta** — the pre-stated measurement claim, citing the baseline (or the logged override that waived it)")
Evidence: Verified by running — this file's `audience:` is `[implementer, skeptic, assistant, human]`. engagements/sre/baseline-measurement.md carries `audience: [cartographer, implementer, assistant, human]` and is therefore absent from the `skeptic` bundle (23 files). Criterion 1.
Consequence: An engagement Skeptic reviewing a change package is required by item 3 to check a claim against a baseline whose form — per-stage p50/p95, date range, run count, known confounds — its bundle never describes. The Skeptic's own infra checklist includes "a single timing proves a distribution," which is precisely the check that needs the baseline's shape.
Fix: Add `skeptic` to engagements/sre/baseline-measurement.md's `audience:`.

## SRE-ECP-2 — blocking
Claim: The map-correction rule names an artifact absent from both of this file's execution bundles.
Location: engagements/sre/engagement-change-package.md:29-31 ("if the change contradicts the System Map, the package includes the map correction")
Evidence: Verified by running — "System Map" is defined only in engagements/sre/system-discovery.md (`audience: [cartographer, assistant, human]`), absent from both the `implementer` and `skeptic` bundles that receive this file. Criterion 1, criterion 11 — the condition triggering the rule cannot be evaluated.
Consequence: The Implementer assembling the package and the Skeptic reviewing it are both bound by a rule whose trigger condition neither can evaluate, and whose output — a "map correction" — neither has a form for.
Fix: Covered by SRE-SD-2's `audience:` change, or by lifting the System Map definition into engagements/sre/README.md.
Related: SRE-SD-2, SRE-IMP-2

## SRE-ECP-3 — non-blocking
Claim: The file declares one session kind and its `audience:` delivers it to a decision-session role.
Location: engagements/sre/engagement-change-package.md:9 ("This skill runs in an execution session.") and :4 (`audience: [implementer, skeptic, assistant, human]`)
Evidence: Verified by running against the corpus at 8402c23 — of the three role slugs, engagements/sre/implementer.md:9 states the Implementer "runs as an execution session" and engagements/skeptic.md:11 states the engagement Skeptic "runs as an execution session," but engagements/assistant.md:9 states "The Assistant runs as a decision session and receives the decision layer." The baton at docs/batons/baton-20260822T212629.md records this session-kind call as resolved by fiat in favour of execution. Criterion 7.
Consequence: Criterion 7 requires the file to say nothing only the other kind needs. It is delivered to a decision session that is told, in its first line, that the file is not for it. In practice the Assistant drafts the Improvement Proposal the package cites (engagements/sre/speed-audit.md:33-34), so it plausibly does need the shape — meaning either the declaration or the audience is wrong, and the reader cannot tell which.
Fix: If the Assistant needs the package shape, declare the file for both kinds as engagements/sre/README.md and override-log-policy.md do. If it does not, drop `assistant` from `audience:`.
