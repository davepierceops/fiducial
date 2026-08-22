# Review: skills/change-package-creation.md — cycle 1

Verdict: changes-required
Reviewed: skills/change-package-creation.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the ten-step procedure mapped item by item against operating-model.md's Change package list, and the `audience:` values checked against their role documents.
Cross-checked: operating-model.md, roles/coder-agent.md, roles/release-manager-agent.md, roles/chief-of-staff.md, docs/global-context/core.md, LEXICON.md — all @ 5136960.
Not inspected: `policies/commit-and-change-control-policy.md` in full — read only the two lines returned by a `human-gate` grep, so the consequential-class list itself was not inspected; whether any project has instantiated a change package against this procedure.
Findings: 2 blocking, 3 non-blocking
Dave should inspect: CP-1 — retire against keep-and-rewrite is a scope call, and the two dropped items must survive either way.

Disposition (criterion 10): **retire.** Merge target if Dave prefers merge-into: `operating-model.md` §Change package. The procedure is that section's contents list restated as imperatives; `operating-model.md` is `audience: [all-roles, human]` and is therefore already in every bundle this skill reaches. What the skill adds beyond the restatement is an Inputs list, a Use when list, and one Output sentence — none of which states a procedure the list does not imply.

## CP-1 — blocking
Claim: the ten-step procedure restates `operating-model.md`'s Change package list, and drops two of its items in the process.
Location: skills/change-package-creation.md:30-43, against operating-model.md §Change package.
Evidence: verified by reading both @ 5136960. Item-for-item: step 1 ↔ item 1 intent; step 2 ↔ item 2 acceptance criteria; step 3 ↔ item 4 implementation summary; step 4 ↔ item 5 test results; step 5 ↔ item 6 verification boundary updates; step 6 ↔ item 7 SLO status and error budget; step 7 ↔ item 8 review findings; step 8 ↔ item 9 known gaps; step 9 ↔ item 11 `human-gate` reference; step 10 ↔ item 12 release recommendation. Operating-model item 3 (test plan) and item 10 (operational notes) have no corresponding step. Both appear in this file's own Inputs list at :26 and :28, so the omission is in the procedure alone.
Consequence: criteria 4 and 10. Every step restates a list item from a file in the same bundle, which is criterion 4 on its face. The restatement has already drifted, which is the concrete harm: an agent that follows these ten steps produces a change package with no test plan and no operational notes, and `operating-model.md`'s Definition of done does not catch it because it checks evidence classes rather than package items.
Fix: retire the file. If Dave prefers to keep a skill at this path, it must state what operating-model does not — how each item is sourced, and what to do when a source is absent — and stop restating the list. Either way the test plan and the operational notes must be reachable from whatever survives.

## CP-2 — blocking
Claim: this is the last vendor-named survivor of a term the rest of the repository states neutrally, and commit 5136960 changed the identical phrase elsewhere without changing it here.
Location: skills/change-package-creation.md:41.
Evidence: verified by running `git grep -n -i "human-gate" 5136960 -- roles/ skills/ operating-model.md policies/`. Every other instruction-layer occurrence reads "tracker issue": operating-model.md:185, policies/commit-and-change-control-policy.md:53, roles/release-manager-agent.md:23, roles/skeptic-risk-agent.md:74, skills/release-readiness-review.md:41. This line alone reads "`human-gate` GitHub issue". Verified by running `git show 5136960 -- skills/release-readiness-review.md`: that commit's diff changes "Confirm `human-gate` GitHub issue is open and linked" to "Confirm the `human-gate` tracker issue is open and linked".
Consequence: criterion 8, and Core rule 13 — "A changed fact changes everywhere it appears." The vendor-neutralization was performed one file at a time and this file was missed, so the methodology now names a specific tracker product in exactly one place. An agent reading this skill is told a GitHub issue is required; an agent reading the role it hands off to is told a tracker issue is.
Fix: "tracker issue". If CP-1 retires the file, the fix lands with the retirement.

## CP-3 — non-blocking
Claim: the SLO / Top K step is one of eleven copies of the same statement.
Location: skills/change-package-creation.md:37-38.
Evidence: verified by running `git grep -c -i "Top K" 5136960 -- roles/ skills/ operating-model.md docs/global-context/`; counts recorded in BA-4.
Consequence: criterion 4. `operating-model.md` item 7 is the home and is in the same bundle.
Fix: cut; goes with CP-1 either way.
Related: BA-4, ER-3, RR-4, TP-3.

## CP-4 — non-blocking
Claim: the `audience:` names a role its own role document forbids from performing the procedure.
Location: skills/change-package-creation.md:4.
Evidence: verified by reading `roles/chief-of-staff.md` @ 5136960: "The Chief of Staff operates as a decision session", and under Constraints, "Does not execute packages, review or test implementation, assess risk, or make architecture decisions."
Consequence: criteria 2, 7 and 11. Steps 3, 4 and 7 require summarizing implementation, test results and review findings — execution-session work the Chief of Staff is barred from. The audience places the procedure in a bundle whose role may not run it, which is a boundary two roles could both claim: nothing here says the Chief of Staff receives this skill to read change packages rather than to write them.
Fix: drop `chief-of-staff` from the audience, or state that it receives the skill as a reader.

## CP-5 — non-blocking
Claim: the consequential-tier call is left to inference, with the governing list and the default both dropped.
Location: skills/change-package-creation.md:41-42.
Evidence: verified by reading `operating-model.md` @ 5136960 §Release gate: "The consequential class is the list the commit and change control policy states. When unsure which tier applies, treat the change as consequential and ask." The step reads only "State whether a `human-gate` GitHub issue is required and, if so, confirm it is open and linked."
Consequence: criterion 11 — an underspecified condition. The agent is told to decide whether the gate applies, with no test to apply and no instruction about what to do when it cannot tell. The treat-as-consequential-and-ask default is precisely the escalation trigger that keeps this call from being the agent's.
Fix: carry the default — when unsure, treat the change as consequential and ask. Goes with CP-1 if the file retires.
