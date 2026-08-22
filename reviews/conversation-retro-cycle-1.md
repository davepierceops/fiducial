# Review: skills/conversation-retro.md — cycle 1

Verdict: changes-required
Reviewed: skills/conversation-retro.md @ 5136960
Reviewer: Context Quality Reviewer
Date: 2026-08-22
Scope: the whole file, frontmatter and body, against all eleven criteria of docs/global-context/review-rubric.md @ 5136960; the prescribed filename convention checked against the retro filenames actually in the tree.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, policies/document-metadata-policy.md, skills/spec-review-cycle.md — all @ 5136960.
Not inspected: the contents of the four retros in `retros/` — only their filenames were read; `docs/global-retro-inbox.md`; whether any synthesis document exists; `writing/retros/`.
Findings: 2 blocking, 4 non-blocking, 2 observations
Dave should inspect: CR-1 — the filename form is a corpus-wide convention and two shapes are already present in `retros/`.

Disposition (criterion 10): **retain-with-changes.** The mandate to run a retro is decision-layer rule 12; the schema, storage rules, synthesis procedure and output shape are not stated in any role or foundation file. That is a real procedure and it earns its place. The Principles section is where the restatement is.

## CR-1 — blocking
Claim: the prescribed filename convention contradicts Core rule 14 and the two most recent retros in the repository.
Location: skills/conversation-retro.md:62.
Evidence: verified by running `git ls-tree -r --name-only 5136960 | grep -i retro`. `retros/` holds `retro-20260807-194436.md`, `retro-20260811-121500.md`, `retro-20260821T170302.md`, `retro-20260822T153848.md`. The two most recent use ISO 8601 basic; the two oldest use the dashed date-time split this file prescribes. Core rule 14 @ 5136960 fixes the form as `<descriptor>-<timestamp>`, "timestamp in ISO 8601 basic format (`20260820T161541`)".
Consequence: criterion 9. An agent following this skill emits `retro-<YYYYMMDD>-<HHMMSS>.md`, a form both Core and current practice have moved off. The corpus already carries two naming shapes with no rule that resolves them, and the file states filenames are "opaque, collision-free handles only", so nothing else in the repo will catch the split.
Fix: `retro-<timestamp>.md`, timestamp in ISO 8601 basic — matching Core rule 14 and the two most recent retros.

## CR-2 — blocking
Claim: two of the five Principles restate decision-layer rule 12.
Location: skills/conversation-retro.md:33-34 and :40-42.
Evidence: verified by reading `docs/global-context/decision-layer.md` @ 5136960 rule 12: "End non-trivial sessions with a retro. Evidence separate from interpretation; near-empty is a valid result." Against :33-34, "Separate Evidence from Interpretation explicitly", and :40-42, "a near-empty retro is a valid and useful result".
Consequence: criterion 4. Both clauses of rule 12 are restated in a file the same decision session already receives alongside decision-layer. The separation is additionally enforced structurally by the schema's own `## Evidence` and `## Interpretation` sections at :87-93, so the file states it twice internally as well.
Fix: cut both principles. The schema carries the separation; rule 12 carries the near-empty permission.

## CR-3 — non-blocking
Claim: the random-string prohibition restates Core rule 14, and its escape hatch defeats criterion 9.
Location: skills/conversation-retro.md:69-71.
Evidence: verified by reading Core @ 5136960 rule 14: 'Never "random" strings, hashes, or UUIDs.'
Consequence: criterion 4 for the prohibition, criterion 6 for the trailing "LLMs repeat 'random' strings and collide", and criterion 9 for what follows it: "If timestamp precision is unavailable, emit `retro.md` and rename on save" sanctions a filename with no timestamp at all, and "rename on save" is a manual step the file cannot enforce.
Fix: cut all three sentences. Core rule 14 states the prohibition; a retro that cannot get a timestamp is a condition to surface, not to name around.

## CR-4 — non-blocking
Claim: the file never states its session kind, and the audience carries a decision-session procedure into every execution bundle.
Location: skills/conversation-retro.md:4, whole body.
Evidence: verified by reading. The mandate for this skill is decision-layer rule 12, and `docs/global-context/decision-layer.md` @ 5136960 states "Execution sessions never receive this file." The skill is `audience: [all-roles, human]` and names no session kind anywhere.
Consequence: criterion 7. Every execution bundle receives a procedure whose triggering rule is, by design, absent from it. An execution session reading "a working conversation on a project has concluded" has no rule telling it not to act.
Fix: state the session kind in one line — this file governs decision sessions.

## CR-5 — non-blocking
Claim: a named external project appears in a grandfather clause.
Location: skills/conversation-retro.md:57.
Evidence: verified by running `git grep -n -i "Catchable" 5136960 -- skills/conversation-retro.md` — one hit, "Pre-adoption corpora (e.g., Catchable's existing retros)".
Consequence: criteria 1 and 8. An agent reading this in a bundle has no way to know what Catchable is, and no way to tell whether its own project's pre-existing retros fall under the clause. The exemption is stated by example rather than by property, so it is unusable by anyone who is not already inside that example.
Fix: state the clause by property — retros predating adoption of this skill are data, not governed documents — and drop the named instance.

## CR-6 — non-blocking
Claim: three path-shaped references carry rules the reader cannot resolve.
Location: skills/conversation-retro.md:19, :28, :52.
Evidence: verified by running a markdown-path grep over the file at 5136960: `policies/document-metadata-policy.md` at :19 and :52, `skills/spec-review-cycle.md` at :28.
Consequence: criteria 1 and 3. Line 19's rule turns on which doors the metadata policy opens ("the expedited path or the doc-only cycle"); line 28's turns on which chats that skill governs. Neither is decidable from this file. Line 52's is the lighter case — it names the policy the exemption is from.
Fix: state each rule inline: retro-surfaced revisions take the full cycle regardless of eligibility for a lighter path; do not run retros on reviewer-gated cycle chats, whose decision record is the cycle directive. `retros/` and `retro.md` are output destinations, not cross-references, and stay.

## CR-7 — observation
Claim: two trailing justifications argue for rules already stated.
Location: skills/conversation-retro.md:43-44, :66-67.
Evidence: verified by reading — "so the corpus concatenates cleanly for synthesis" and "because no tooling reads filenames, replacement is a pure rename".
Consequence: criterion 6. Both are arguments for rules the same file states as rules.
Fix: cut.

## CR-8 — observation
Claim: the trigger condition is underspecified.
Location: skills/conversation-retro.md:24.
Evidence: verified by reading — "a working conversation on a project has concluded (or reached a natural boundary)".
Consequence: criterion 11. "Natural boundary" gives the agent no test, so whether a retro is owed is left to its judgment. Decision-layer rule 12's "non-trivial" is the condition that actually governs.
Fix: drop the parenthetical and rely on rule 12, or name the boundary.
