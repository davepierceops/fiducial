# Review: docs/global-context/decision-layer.md — cycle 13

Verdict: ready-with-findings
Reviewed: docs/global-context/decision-layer.md @ 500874a
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: docs/global-context/decision-layer.md, read whole at 500874a, against all twelve criteria of the review rubric at the head of pass2-held-fix-2 — docs/global-context/review-rubric.md @ 500874a. This artifact reviewed docs/global-context/decision-layer.md at 500874a and no other document.
Cross-checked: docs/global-context/core.md @ 500874a — Standing rules 3 and 4, Acting rule 13, and the Vocabulary entries for Handoff (core.md:54) and Baton (core.md:55), against which rule 13's revised final sentence was read; LEXICON.md @ 500874a line 110, which routes "what a decision session hands its successor decision session" to *baton*; skills/conversation-retro.md @ 500874a, Use when, against rule 12; skills/command-blocks.md and policies/decision-log-policy.md @ 500874a, for rules 16 and 10 — both carry `audience: [all-roles, human]` and so land in this file's bundle; roles/chief-of-staff.md @ 500874a, the principal decision-session role this layer governs, which states no competing baton or retro ordering; operating-model.md @ 500874a, which states neither.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 2 — 0 blocking, 1 non-blocking, 1 observation
Prior cycle: reviews/decision-layer-cycle-12.md
Dave should inspect: DL-1 — whether a reviewer-gated cycle conversation owes a retro. Rule 12 and the conversation-retro skill answer differently; which governs is a methodology call this role cedes.

## DL-1 — non-blocking
Claim: Rule 12's retro obligation and the conversation-retro skill's exclusion state different scopes for the same obligation, and neither file says which governs.
Location: docs/global-context/decision-layer.md:31 — rule 12, "End every session with a retro."
Evidence: Verified by running (`grep -rn -i 'retro' --include='*.md' skills roles docs/global-context policies` at 500874a) and inferred by reading. skills/conversation-retro.md, Use when, states: "Do not run a retro on a reviewer-gated cycle conversation unless directed — its decision record is the cycle directive." Rule 12's only stated exception is "A session that produced no artifact and made no decision may skip it." A reviewer-gated cycle conversation produces artifacts and makes decisions, so that exception does not reach it. skills/conversation-retro.md carries `audience: [all-roles, human]`, so both statements load in the same bundle as this file.
Consequence: A decision session ending a reviewer-gated cycle — the class this repository's own pass-1 and pass-2 cycles belong to — has rule 12 requiring a retro and the retro skill forbidding one, with both texts in front of it. Reading the skill as the more specific rule resolves it, but rule 12 does not say so, so the resolution is left to the agent's inference. Rubric criterion 12 makes a disagreement between governed files a defect regardless of whether an agent could reason its way out.
Fix: Name the exclusion in rule 12 — e.g. "...may skip it, as may a reviewer-gated cycle conversation, whose decision record is the cycle directive." Alternatively, state in rule 12 that the retro skill's Use-when conditions determine when a retro is owed. Which of the two is right is a scoping call, not a wording one.

## DL-2 — observation
Claim: Cycle 12's blocking finding is resolved by this cycle's edit to rule 13.
Location: docs/global-context/decision-layer.md:32 — rule 13, final sentence
Evidence: Verified by reading both texts at 500874a and by running `grep -rn "hands responsibility forward" --include='*.md' .`, which now returns only records — reviews/decision-layer-cycle-12.md and two files under docs/cycles/ — and no live governing text. The sentence cycle 12 flagged, "Every session end that hands responsibility forward emits one," now reads "Every session end that hands responsibility to a successor decision session emits one," which restates the scope core.md:55 sets: "A baton passes between decision sessions only; a directive hands work to an execution session. The two never blur." The phrase cycle 12 objected to — Core's definition of *handoff* used to trigger a *baton* — is gone.
Consequence: None outstanding. Recorded so the cycle-12 blocking finding has a disposition in the record.
Fix: None required.
