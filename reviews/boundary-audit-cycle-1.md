# Review: skills/boundary-audit.md — cycle 1

Verdict: changes-required
Reviewed: skills/boundary-audit.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the procedure checked against the three role documents its `audience:` names.
Cross-checked: roles/reviewer-agent.md, roles/skeptic-risk-agent.md, roles/release-manager-agent.md, docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md — all @ 5136960.
Not inspected: `boundaries/human-review-boundary.md`, read only for its existence, not its content; `specs/trd-template.md`, which also mentions a boundary audit; whether any boundary-audit artifact schema is defined outside `skills/`.
Findings: 2 blocking, 2 non-blocking, 2 observations
Dave should inspect: BA-2 — whether an auditing agent may apply `accepted-risk` at all. BA-6 — where output shapes live now that cycle 20 removed them from role documents.

Disposition (criterion 10): **retain-with-changes.** The seven-step sequence — enumerate affected production behaviors, then tested, then mocked, then verified/not-verified per boundary, then deferred path, then label — is not stated in any of the three roles it serves. `roles/skeptic-risk-agent.md` states what to inspect and how to label; it does not state this order. The procedure earns its place. Step 7 and the Output do not.

## BA-1 — blocking
Claim: step 7 offers three gap labels where LEXICON defines four, and the role document it serves states four.
Location: skills/boundary-audit.md:39.
Evidence: verified by reading `LEXICON.md` @ 5136960, "Release impact labels": `blocking`, `deferred`, `accepted-risk`, `not-material`. Verified by reading `roles/skeptic-risk-agent.md` @ 5136960, "Gap labels": "Mark every material gap with one of LEXICON's four release impact labels." Step 7 reads "Mark unresolved gaps as accepted risk, deferred, or blocking."
Consequence: criterion 4. `not-material` is unavailable to an agent following this step, so a gap that is known but irrelevant to the release decision must be forced into one of three labels that all overstate it — most likely `deferred`, which asserts a named future mechanism LEXICON requires and the gap does not have. A skeptic-risk agent receives both this file and its role document and is given two different label sets for the same act. The labels are also written as prose ("accepted risk") rather than LEXICON's code form (`accepted-risk`).
Fix: replace the enumeration with the same reference the role uses — LEXICON's four release impact labels — or state all four in LEXICON's code form.

## BA-2 — blocking
Claim: step 7 instructs the auditing agent to apply a label LEXICON reserves to Dave or the release process.
Location: skills/boundary-audit.md:39.
Evidence: verified by reading `LEXICON.md` @ 5136960: "**`accepted-risk`** — Dave or the release process has explicitly accepted the gap", and "A gap awaiting Dave's judgment is blocking; 'requires Dave decision' is not a label."
Consequence: criterion 11 — language implying authority the methodology does not grant. The step tells the agent to mark *unresolved* gaps as accepted risk. By LEXICON's definition an unresolved gap cannot carry that label, because the label records an acceptance that has not happened. Downstream — in a change package or a release package — the label reads as Dave's decision, and nothing in the artifact distinguishes an acceptance he made from one the auditor assigned.
Fix: state that the auditor applies `blocking`, `deferred`, or `not-material`, and that `accepted-risk` is used only where Dave or the release process has already accepted the gap — otherwise the gap is `blocking`, per LEXICON.

## BA-3 — non-blocking
Claim: a library name appears where the repository already has neutral wording.
Location: skills/boundary-audit.md:35.
Evidence: verified by running a vendor-name grep over the file at 5136960 — one hit, "jsdom", in "Identify which tests use mocks, fixtures, jsdom, fakes, or generated data." `roles/skeptic-risk-agent.md` @ 5136960 states the same idea as "a headless DOM can hide browser failures".
Consequence: criterion 8. One library from one ecosystem is named inside a methodology stated as project-neutral everywhere else, and the neutral phrasing already exists one document away.
Fix: "headless DOM", matching the role.

## BA-4 — non-blocking
Claim: the SLO / Top K output item is one of eleven copies of the same statement.
Location: skills/boundary-audit.md:52-53.
Evidence: verified by running `git grep -c -i "Top K" 5136960 -- roles/ skills/ operating-model.md docs/global-context/`: operating-model.md 1, roles/architect-agent.md 1, roles/release-manager-agent.md 2, roles/skeptic-risk-agent.md 1, roles/spec-reviewer-agent.md 1, roles/test-designer-agent.md 1, skills/boundary-audit.md 1, skills/change-package-creation.md 1, skills/evidence-review.md 2, skills/release-readiness-review.md 1, skills/test-plan-review.md 2.
Consequence: criterion 4, and the cross-file duplication check. `operating-model.md` change package item 7 is the home and is in every bundle these files reach. The copies have already drifted in wording: this one adds "if known" to the error budget state, which none of the others carry, so an agent reading this file has a weaker obligation than one reading the role.
Fix: cut here and rely on operating-model item 7.
Related: CP-3, ER-3, RR-4, TP-3.

## BA-5 — observation
Claim: the file never states its session kind.
Location: whole file.
Evidence: verified by reading. `roles/reviewer-agent.md` and `roles/skeptic-risk-agent.md` @ 5136960 each open "You run in an execution session"; `roles/release-manager-agent.md` states both kinds for its own work. The skill states neither.
Consequence: criterion 7. The kind is inferable from all three roles but is not stated, which is what the criterion asks for.
Fix: one line — this procedure runs in an execution session.

## BA-6 — observation
Claim: the Output is an artifact shape list, and cycle 20 removed shape lists from the role documents without stating where they now live.
Location: skills/boundary-audit.md:41-53.
Evidence: verified by running `git show 5136960` and reading its commit message, which records under the cycle-20 dispositions: "The nine retained roles trimmed to what each inspects and decides: output shapes removed per A2". Verified by running `git grep -l -i "boundary audit" 5136960` — `skills/boundary-audit.md`, `skills/change-package-creation.md`, `specs/trd-template.md`; no file defines a boundary audit artifact schema.
Consequence: criteria 10 and 4. An eight-item output shape is the artifact's schema, not a procedure. Cycle 20 moved shapes out of roles on the ground that roles state what a role inspects and decides; nothing states whether skills are their new home or whether they belong with an artifact schema that does not yet exist.
Fix: Dave's call, not the reviewer's. Recorded so the same question is not rediscovered per skill.
Related: TP-4.
