# Review: docs/global-context/decision-layer.md — cycle 12

Verdict: changes-required
Reviewed: docs/global-context/decision-layer.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: docs/global-context/decision-layer.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed docs/global-context/decision-layer.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; docs/global-context/core.md Vocabulary entries for Handoff and Baton (core.md:54-55); LEXICON.md Retired terms, which routes 'what a decision session hands its successor decision session' to *baton*; skills/directive-authoring.md and skills/command-blocks.md for rules 14 and 16; roles/chief-of-staff.md, the principal decision-session role this layer governs.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 1 blocking, 0 non-blocking
Prior cycle: reviews/decision-layer-cycle-11.md
Dave should inspect: DL-1 — the sentence this cycle was directed to restore is the sentence that collides with Core's baton/handoff boundary. The obligation is restorable, but not in this wording; the scoping is Dave's call.

## DL-1 — blocking
Claim: Rule 13's appended sentence makes every session-end handoff emit a baton, which contradicts Core's rule that a baton passes between decision sessions only.
Location: docs/global-context/decision-layer.md:32 — "Every session end that hands responsibility forward emits one."
Evidence: Verified by running (`grep -rn -i "baton\|handoff"` over the governing set) and inferred by reading. docs/global-context/core.md:54 defines **Handoff** as "transfer of unfinished responsibility between sessions or roles" and states "handing a directive to an execution session is one mechanism by which a handoff is carried out." docs/global-context/core.md:55 defines **Baton** and states "A baton passes between decision sessions only; a directive hands work to an execution session. The two never blur." The appended sentence's phrase "hands responsibility forward" is Core's definition of a handoff almost verbatim, so read against Core it asserts that a handoff to an execution session emits a baton.
Consequence: A decision session that ends by handing a directive to an execution session — the ordinary case this repo runs on, and the case Core names explicitly — reads rule 13 as requiring it to also emit a baton. Core forbids exactly that blur. The two files give opposite answers to the same question, and rule 13 is the one the decision session has in front of it, because Core's Vocabulary entry is a definition while rule 13 is an instruction.
Fix: Scope the sentence to the successor-decision-session case Core defines, e.g. "Every decision session that ends with unfinished responsibility for a successor decision session emits one." That restores the obligation without reaching handoffs to execution sessions.
