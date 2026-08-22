# Review: skills/evidence-review.md — cycle 1

Verdict: changes-required
Reviewed: skills/evidence-review.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the procedure checked against the three role documents its `audience:` names and against Core's evidence rules.
Cross-checked: roles/reviewer-agent.md, roles/skeptic-risk-agent.md, roles/release-manager-agent.md, docs/global-context/core.md, LEXICON.md, operating-model.md, skills/spec-review-cycle.md — all @ 5136960.
Not inspected: whether a "boundary ledger" exists as an artifact in any project repository — only this repository was searched; `boundaries/human-review-boundary.md` content.
Findings: 2 blocking, 3 non-blocking, 1 observation
Dave should inspect: ER-1 — which role owns which recommendation, since two roles in the audience have opposite authority over it.

Disposition (criterion 10): **retain-with-changes.** This is the strongest of the four short skills. The claim-matching sequence — enumerate the claims being made, match each to evidence, then identify the unsupported, the overbroad, and the materially missing — is stated in no role and in no foundation file. `roles/skeptic-risk-agent.md` states the posture and a false-confidence checklist; Core rules 5-10 state the evidence discipline. Neither states this procedure. It earns its place.

## ER-1 — blocking
Claim: the Output gives the same recommendation slot to two roles the methodology grants opposite authority.
Location: skills/evidence-review.md:4, with :38 and :49.
Evidence: verified by reading `roles/skeptic-risk-agent.md` @ 5136960: "Your output is findings and their labels, and a recommended next step. You do not emit a ship recommendation; that call is the Release Manager's. To signal that a change should not ship, mark the gap `blocking`." Verified by reading `roles/release-manager-agent.md` @ 5136960: "produce release recommendation", with the vocabulary ship / ship with accepted risks / do not ship / needs Dave decision. Both roles are in this file's `audience:`. Step 7 reads "Produce a recommendation"; the Output reads "recommended next step" and "risk level", unqualified.
Consequence: criterion 11 — a boundary two roles could both claim. A skeptic-risk agent following this skill is instructed to produce a recommendation with nothing here telling it which kind, and the file it would need to know that is its role document rather than this one. The failure is silent in the direction that matters: a skeptic that emits a ship-shaped recommendation has crossed a line the methodology draws explicitly, and the skill gave it no signal.
Fix: state that the recommendation is a next step and never a ship call, and that the ship call belongs to the Release Manager alone.
Related: RR-2.

## ER-2 — blocking
Claim: "risk level" is a required output with no defined scale anywhere in the repository.
Location: skills/evidence-review.md:48.
Evidence: verified by running `git grep -n -i "risk level" 5136960` — exactly one hit, this line. LEXICON.md @ 5136960 defines evidence classes and release impact labels; neither is a risk level, and no third vocabulary exists.
Consequence: criteria 1 and 11. The agent must emit a field whose values it has to invent, and it must do so inside a bundle where nothing defines them. Two agents produce two scales; a reader downstream cannot compare them, and cannot tell whether "medium" here means what "medium" meant in the last package. It also invites a soft substitute for the labels LEXICON does define, which are the ones the release decision actually consumes.
Fix: replace with LEXICON's release impact labels, which are the defined vocabulary for exactly this judgment, or delete the field.

## ER-3 — non-blocking
Claim: the SLO / Top K statement appears twice within this file, and is one of eleven copies across the repository.
Location: skills/evidence-review.md:36-37 and :47.
Evidence: verified by running `git grep -c -i "Top K" 5136960 -- roles/ skills/ operating-model.md docs/global-context/` — this file returns 2, the highest of any skill alongside test-plan-review.md; full counts recorded in BA-4.
Consequence: criterion 4. `operating-model.md` item 7 is the home. The internal duplication is the sharper half: step 6 and Output bullet 4 state the same requirement in different words within forty lines.
Fix: cut both; rely on operating-model item 7.
Related: BA-4, CP-3, RR-4, TP-3.

## ER-4 — non-blocking
Claim: "boundary ledger" is an input the repository never defines.
Location: skills/evidence-review.md:26.
Evidence: verified by running `git grep -n -i "boundary ledger" 5136960` — exactly one hit, this line. The repository's term is "verification boundary": `operating-model.md` control surface 5 and change package item 6, `roles/release-manager-agent.md` "check verification boundary status", `roles/skeptic-risk-agent.md` "verification boundary declarations".
Consequence: criterion 1. An agent in a bundle is told to take "boundary ledger entries" as an input to a required procedure and no file it can reach says what a boundary ledger is, where it lives, or what an entry looks like. The nearest real artifact is the boundary audit, which this file does not name.
Fix: "verification boundary declarations", matching `roles/skeptic-risk-agent.md`, or the boundary audit's output if that is what is meant.

## ER-5 — non-blocking
Claim: the file never states its session kind.
Location: whole file.
Evidence: verified by reading. `roles/reviewer-agent.md` and `roles/skeptic-risk-agent.md` @ 5136960 open "You run in an execution session"; `roles/release-manager-agent.md` states both kinds. The skill states neither.
Consequence: criterion 7. Compounds ER-1: the audience spans roles that run in different kinds for this work, and the file distinguishes neither the kind nor the authority.
Fix: one line stating the kind.

## ER-6 — observation
Claim: "what Dave should inspect" restates a field the review artifact schema defines.
Location: skills/evidence-review.md:49.
Evidence: verified by reading `skills/spec-review-cycle.md` @ 5136960, "Review artifact schema": the header carries `Dave should inspect`, and the mapping table has the row "What Dave should inspect | `Dave should inspect`".
Consequence: criterion 4, bounded. The schema governs review artifacts in `reviews/` — reviews of documents — and an evidence review of a change package is not one of those, so the overlap is in wording rather than in scope. Recorded because it is the second home for the same requirement and the two will drift if one is edited.
Fix: none required. If a future cycle gives evidence reviews an artifact schema, this field belongs there, not here.
