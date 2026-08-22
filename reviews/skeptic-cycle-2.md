# Review: engagements/skeptic.md — cycle 2

Verdict: changes-required
Reviewed: engagements/skeptic.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, skills/review-artifact.md, roles/skeptic-risk-agent.md, engagements/sre/README.md, engagements/sre/engagement-change-package.md, engagements/working-with-dave.md — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether the infra false-confidence checklist is the right list as a matter of engineering judgment.
Findings: 2 — 1 blocking, 1 non-blocking
Prior cycle: reviews/skeptic-cycle-1.md (reviewed @ 1bbd5b7)
Dave should inspect: SK-2 — whether an engagement has a release gate or does not is a statement two files answer differently, and only one can stand.

## SK-1 — blocking
Claim: The Output section requires a schema that is not in this file's bundle.
Location: engagements/skeptic.md:26-29 ("The review artifact follows the review-artifact schema, including its verdict values.")
Evidence: Verified by running — the `skeptic` bundle resolves to 23 files at 8402c23 and does not contain skills/review-artifact.md, whose `audience:` is `[spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, chief-of-staff, human]`. skills/review-artifact.md was created at 1bbd5b7 — the same SHA this file was reviewed at in cycle 1 — so no foundation change caused this; it was missed. Criterion 1, criterion 3.
Consequence: An engagement Skeptic session is told to emit an artifact in a schema it has not been given, including "its verdict values," which are `ready | ready-with-findings | changes-required` and appear nowhere in its bundle. The session either invents a shape or asks for a file it was told not to need.
Fix: Add `skeptic` to skills/review-artifact.md's `audience:`. Stating the schema inline here would duplicate it into a second home and is the worse option.

## SK-2 — non-blocking
Claim: The file states that an engagement has no release gate; another file in the same bundle states that it has one.
Location: engagements/skeptic.md:12-14 ("An engagement has no release gate: Dave and the client's CI hold the levers.") against engagements/sre/README.md:36-38 ("Ownership becomes guest posture ... The client's humans hold the release gate on their own systems.")
Evidence: Inferred by reading; both files verified present in the `skeptic` bundle by mechanical computation over `audience:` at 8402c23. The two are reconcilable — "no gate *this methodology holds*" versus "a gate the client holds" — but neither says so, and the words "release gate" carry a defined meaning from operating-model.md:145-160, which is also in the bundle. Criterion 11.
Consequence: A session that reads both is left to infer which reading is meant, and criterion 11 makes that inference a defect. The practical risk is a Skeptic treating its own verdict as terminal because "there is no gate."
Fix: In this file, write "this methodology holds no release gate over an engagement; the client's own gate governs, and your verdict is input to Dave's decision." That keeps one statement and removes the contradiction without touching the README.
