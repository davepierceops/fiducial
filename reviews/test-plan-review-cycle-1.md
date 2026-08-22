# Review: skills/test-plan-review.md — cycle 1

Verdict: changes-required
Reviewed: skills/test-plan-review.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the nine-step procedure compared against roles/test-designer-agent.md's construction responsibilities and against operating-model.md's red-gate and separation-of-duties rules.
Cross-checked: roles/test-designer-agent.md, roles/reviewer-agent.md, roles/coder-agent.md, operating-model.md, docs/global-context/core.md, LEXICON.md — all @ 5136960.
Not inspected: `context-sets/testing-and-verification.md`, which cycle 20 also edited and which carries the mock checklist — not read this cycle; any project's actual test plan.
Findings: 1 blocking, 3 non-blocking, 2 observations
Dave should inspect: TP-1 — whether the Test Designer may run this skill over its own plan, given operating-model's mandatory separation.

Disposition (criterion 10): **retain-with-changes.** The repository has already adjudicated the duplication question in this skill's favour: `roles/test-designer-agent.md` states "These are the construction of a test plan; the test-plan review skill is the review of one, and the two are not competing." The review procedure — map ACs to tests, then find untested criteria, over-testing, and missing negative cases — is a distinct act from constructing the plan and is stated nowhere else. It earns its place. The audience is the problem, not the content.

## TP-1 — blocking
Claim: the role that produces the test plan is in the audience of the skill that reviews it, with no statement that the Reviewer's pass is still required.
Location: skills/test-plan-review.md:4.
Evidence: verified by reading `operating-model.md` @ 5136960 §Responsibilities: "The same underlying model may fill multiple roles, but two separations are mandatory rather than optional: Whoever produces an artifact does not approve it." Verified by reading `roles/test-designer-agent.md` @ 5136960, whose responsibilities are the construction of the plan and which states the two "are not competing". The audience is `[test-designer-agent, reviewer-agent, human]`.
Consequence: criterion 11. The role document's sentence resolves whether the two *activities* overlap; it does not touch the separation rule, which is about who approves. Steps 5 and 9 are approval-shaped — "flag if absent", "Recommend changes" — and with `test-designer-agent` in the audience the agent that wrote the plan receives the procedure for passing judgment on it. Neither file says the Reviewer's pass is still owed, so a Test Designer that self-applies this skill and finds nothing has, from the evidence chain's point of view, produced a review of its own artifact. That is the exact substitution operating-model calls mandatory to prevent.
Fix: state that self-application is a drafting aid and that the gate remains the Reviewer's, or drop `test-designer-agent` from the audience.

## TP-2 — non-blocking
Claim: step 5 restates the red-gate mandate, which is stated in four other places.
Location: skills/test-plan-review.md:35-36.
Evidence: verified by reading `operating-model.md` @ 5136960 change flow step 4, "ACs translated into test code, run, and confirmed to fail before any implementation", and the following paragraph, "The red-gate at step 4 is mandatory"; `roles/test-designer-agent.md`, "run tests and confirm they fail (red-gate) before handing off to the Coder; a test that passes before implementation is a broken test, not a head start"; `roles/coder-agent.md`, "If the Test Designer's red-gate confirmation is absent, flag it rather than proceed."
Consequence: criterion 4. The clause "tests must be run and confirmed failing before the Coder begins" is the rule restated; the check that follows it — "flag if absent" — is this file's own contribution and is not stated elsewhere.
Fix: keep "Check that the plan includes a red-gate step; flag if absent" and cut the restatement of what a red-gate is.

## TP-3 — non-blocking
Claim: the SLO / Top K statement appears twice within this file, and is one of eleven copies across the repository.
Location: skills/test-plan-review.md:37-38 and :50.
Evidence: verified by running `git grep -c -i "Top K" 5136960 -- roles/ skills/ operating-model.md docs/global-context/` — this file returns 2; full counts recorded in BA-4. `roles/test-designer-agent.md` states it a third time for the same agent, as "identify SLO verification needs for affected Top K user journeys".
Consequence: criterion 4. `operating-model.md` item 7 is the home; the internal duplication between step 6 and Output bullet 4 is the sharper half.
Fix: cut both.
Related: BA-4, CP-3, ER-3, RR-4.

## TP-4 — non-blocking
Claim: the Output is an artifact shape list, and cycle 20 removed shape lists from role documents without stating where they now live.
Location: skills/test-plan-review.md:43-54.
Evidence: verified by running `git show 5136960` and reading its commit message: "The nine retained roles trimmed to what each inspects and decides: output shapes removed per A2".
Consequence: criteria 10 and 4. The same open question as BA-6, and the two skills answer it the same way by default rather than by decision. Two of this list's eight bullets — "red-gate coverage (present / absent)" and "SLO verification coverage" — are also the outputs of steps 5 and 6 restated.
Fix: Dave's call on where shapes live. Independent of that, the two bullets duplicating steps 5 and 6 can go.
Related: BA-6.

## TP-5 — observation
Claim: five of nine steps mirror the role's construction responsibilities.
Location: skills/test-plan-review.md steps 3, 4, 5, 6, 7, against roles/test-designer-agent.md responsibilities.
Evidence: verified by reading both @ 5136960. Pairs: step 3 identify mocks and fixtures ↔ "identify mocked dependencies"; step 4 identify live/browser verification needs ↔ "identify live/browser verification needs"; step 5 red-gate ↔ "run tests and confirm they fail (red-gate)"; step 6 SLO verification ↔ "identify SLO verification needs"; step 7 negative/failure cases ↔ "specify failure cases".
Consequence: criterion 4, bounded and already adjudicated. The role's own sentence licenses the pairing, and checking that a plan identifies its mocks is not the same act as identifying them. Recorded so a later cycle does not rediscover this as new duplication, and so the count is on the record if the adjudication is ever revisited.
Fix: none required if TP-1 is fixed. The pairing is deliberate and stated; what makes it safe is that a different agent performs the check.

## TP-6 — observation
Claim: the file never states its session kind.
Location: whole file.
Evidence: verified by reading. `roles/test-designer-agent.md` and `roles/reviewer-agent.md` @ 5136960 each open "You run in an execution session"; the skill states neither.
Consequence: criterion 7.
Fix: one line — this procedure runs in an execution session.
