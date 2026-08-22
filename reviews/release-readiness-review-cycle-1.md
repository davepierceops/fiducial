# Review: skills/release-readiness-review.md — cycle 1

Verdict: changes-required
Reviewed: skills/release-readiness-review.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the post-cycle-20 procedure compared against roles/release-manager-agent.md sentence by sentence, and against the cycle-20 diff that produced it.
Cross-checked: roles/release-manager-agent.md, roles/skeptic-risk-agent.md, operating-model.md, docs/global-context/core.md, LEXICON.md, policies/commit-and-change-control-policy.md (the `human-gate` lines only) — all @ 5136960.
Not inspected: `policies/release-readiness-policy.md`, named in the metadata policy's ineligible-for-expedited list but not read this cycle; whether any release package has been assembled against this procedure.
Findings: 1 blocking, 3 non-blocking, 1 observation
Dave should inspect: RR-1 — cycle 20 split contents from method across two files; which half stays where is his call, and one sentence is all that currently distinguishes them.

Disposition (criterion 10): **merge-into `roles/release-manager-agent.md`.** After cycle 20's trim, three of the four steps restate that role document and the Output restates its assembly sentence. Step 3 is the only rule here the role does not state. A file contributing one sentence beyond a document in the same bundle does not clear criterion 10; the sentence should move and the file should go. Retire is the equivalent disposition if Dave prefers the role document unchanged — but then step 3's rule is lost, which is the outcome to avoid.

## RR-1 — blocking
Claim: cycle 20 moved the release package contents into the role document and left the assembly method stated in both files; three of four steps and the Output now restate `roles/release-manager-agent.md`.
Location: skills/release-readiness-review.md:30-45, against roles/release-manager-agent.md.
Evidence: verified by running `git show 5136960 -- skills/release-readiness-review.md`, which shows the cycle-20 diff replacing a nine-step contents procedure and a four-value recommendation vocabulary with the present four-step method. Verified by reading `roles/release-manager-agent.md` @ 5136960, which states: "This package is assembled from the change package where the change package states it, not written fresh. Two items are release-only and you supply them: user-visible behavior, and the rollback or mitigation path." Step 1 is that first clause; step 2 is the second, naming the same two items. Step 4 restates the role's responsibility bullet at :23, "confirm the `human-gate` tracker issue is open and linked for consequential changes, before presenting to Dave". The Output, "the assembled package, plus the evidence behind the recommendation", restates the same assembly sentence plus the role's "produce release recommendation".
Consequence: criteria 4 and 10. The role document and the skill are in the same bundle — `roles/release-manager-agent.md` is `audience: [release-manager-agent, chief-of-staff, human]` and this skill is `audience: [release-manager-agent, skeptic-risk-agent, human]`, overlapping on the role that actually runs it. What survives here that the role does not state is step 3 alone: that a required item with no source is reported as a known gap rather than filled. The cycle-20 trim removed the half that was not duplicated and kept the half that was.
Fix: move step 3's rule into `roles/release-manager-agent.md`, beside the assembly sentence it qualifies, and retire this file. If Dave prefers to keep the skill, the reverse cut is required — the role keeps the contents and loses the two method sentences, and the skill keeps the method.

## RR-2 — non-blocking
Claim: the `audience:` names a role forbidden to produce this file's output.
Location: skills/release-readiness-review.md:4, with :45.
Evidence: verified by reading `roles/skeptic-risk-agent.md` @ 5136960: "Your output is findings and their labels, and a recommended next step. You do not emit a ship recommendation; that call is the Release Manager's."
Consequence: criteria 2 and 11. The Output is the assembled release package and the evidence behind its recommendation — the artifact the skeptic-risk agent is explicitly barred from producing. Putting the assembly procedure in that role's bundle invites exactly the crossing the role document forbids, and nothing in this file warns of it.
Fix: drop `skeptic-risk-agent` from the audience.
Related: ER-1.

## RR-3 — non-blocking
Claim: after the trim the procedure cannot be followed from this file alone.
Location: skills/release-readiness-review.md:30-31.
Evidence: verified by reading: "The Release Manager's role document states what the release package contains. This is how it is assembled." Step 1 then says "Take each item the release package requires" — an item list stated only in the other document.
Consequence: criteria 1 and 3. The reference is by role rather than by path, so it evades a path grep, but it is the same defect: the reader is sent to a document this file does not carry and cannot open. The two happen to share a bundle because their audiences overlap on `release-manager-agent`; nothing states that as a requirement, and the skeptic-risk bundle receives this skill without the release-manager role at all.
Fix: lands with RR-1 under either disposition.

## RR-4 — non-blocking
Claim: the SLO / Top K input is one of eleven copies of the same statement.
Location: skills/release-readiness-review.md:25.
Evidence: verified by running `git grep -c -i "Top K" 5136960 -- roles/ skills/ operating-model.md docs/global-context/`; full counts recorded in BA-4.
Consequence: criterion 4. `operating-model.md` item 7 is the home; `roles/release-manager-agent.md` required output 6 states it again; this is the third statement reaching the same agent.
Fix: cut.
Related: BA-4, CP-3, ER-3, TP-3.

## RR-5 — observation
Claim: the file never states its session kind, though the work spans both.
Location: whole file.
Evidence: verified by reading `roles/release-manager-agent.md` @ 5136960: "You assemble the release package in an execution session; you present it at the release decision in a decision session." The skill states neither kind.
Consequence: criterion 7. This is the one file among the seven where the kind genuinely splits mid-procedure — assembly is execution, presentation is decision — so leaving it unstated costs more here than elsewhere.
Fix: state both kinds and which steps belong to which; goes with RR-1 if the content moves.
