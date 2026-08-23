# Review: engagements/working-with-dave.md — cycle 4

Verdict: ready-with-findings
Reviewed: engagements/working-with-dave.md @ df35ea7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ df35ea7, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle; the added questions are whether the `audience:` addition and the guardrail rewrite close WD-1 and what decision D3 did to a file declared for execution sessions.
Cross-checked: docs/global-context/core.md (Vocabulary — decision session, execution session), docs/global-context/decision-layer.md, LEXICON.md (Evidence classes), operating-model.md, docs/global-context/review-rubric.md, engagements/assistant.md, engagements/cartographer.md, engagements/critic.md, engagements/sre/README.md, engagements/sre/implementer.md, engagements/sre/override-log-policy.md, engagements/sre/baseline-measurement.md — all @ df35ea7; plus docs/cycles/pass1-regate-fix-20260822T230000.md (D1, D3, D4, instructions 3, 7, 11). Bundle membership computed mechanically over every `audience:` value in the 51-file set at df35ea7.
Not inspected: the infra verification ladder's fitness as engineering judgment, which is outside this role's remit; whether making the client guardrail overridable is the right call — D1 settled it and this review does not re-open it.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/working-with-dave-cycle-3.md
Dave should inspect: none.

## WD-2 — non-blocking
Claim: The file declares itself for execution sessions and its `audience:` delivers it to the Assistant, which runs as a decision session.
Location: engagements/working-with-dave.md:10 ("This file is for execution sessions within an engagement.") and :4 (`audience: [assistant, cartographer, critic, implementer, human]`)
Evidence: Verified by running. engagements/assistant.md:9 states "The Assistant runs as a decision session and receives the decision layer." Of the four role slugs in this file's audience at df35ea7, `cartographer`, `critic`, and `implementer` are execution-session roles and `assistant` is not. PR #130 added `implementer` to close WD-1 and, under D3, moved the Cartographer from decision to execution, so the mismatch is now confined to one slug where before it was two — but the declaration line was not touched. docs/cycles/pass1-regate-fix-20260822T230000.md D4 states the rule this file does not meet: "Audiences are never narrowed to resolve a session-kind mismatch; the file states who runs it and who reads it." The pack's other files were conformed under that rule; engagements/sre/README.md:9 and engagements/sre/override-log-policy.md:9 both read "This file is for decision sessions and execution sessions within an engagement." Criterion 7.
Consequence: The Assistant is the role that runs completion nudges, drafts Improvement Proposals, and schedules the engagement review, and it receives the corpus's client guardrail and its infra verification ladder inside a file whose first line says it is not for it. The guardrail is the rule D1 just made overridable-by-Dave-only-and-logged; the role most likely to be in the room when Dave says "override" is told the file carrying it addresses someone else. Nothing breaks, but criterion 7 exists because an agent that has to decide whether a rule is addressed to it will sometimes decide wrong.
Fix: State both kinds, as the pack's two other cross-kind files do: "This file is for decision sessions and execution sessions within an engagement." Nothing in the ladder or the guardrail is execution-only.
