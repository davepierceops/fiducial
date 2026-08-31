# Review: skills/conversation-retro.md — cycle 3

Verdict: changes-required
Reviewed: skills/conversation-retro.md @ 08e54f6be9fdd3df6104e29f9966606fa2b427cb
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-31
Scope: skills/conversation-retro.md, read whole at 08e54f6be9fdd3df6104e29f9966606fa2b427cb, frontmatter and body, against all twelve criteria of docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d and against LEXICON.md @ 54cc0d21de8f4913a8530715e7e559b9d8b1751f; and against the five ruled changes RS-1..RS-5 recorded in docs/cycles/conversation-retro-cycle-1-editor-directive.md @ e41d63f7c4bc39c76007b466ad065119bed3dafe. Bundle membership computed by running bin/bundle. This artifact reviewed skills/conversation-retro.md and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, policies/document-metadata-policy.md, roles/chief-of-staff.md, roles/context-quality-reviewer.md, skills/review-artifact.md, decisions/log.md (DEC-000290), bin/bundle, bin/check-frontmatter — all at 54cc0d21de8f4913a8530715e7e559b9d8b1751f; the retros/ directory listing at the same commit.
Not inspected: the contents of the retros in retros/ — only their filenames were read; retros/retro-synthesis-20260831T163000.md and OPEN-ITEMS.md as sources of the rulings, which this review takes as told from the Editor directive rather than re-deriving; specs/ documents, which are the Spec Reviewer's gate; whether any rule here is correct as engineering or product judgment, which this role cedes; docs/history/, docs/cycles/ beyond the Editor directive, and reviews/ beyond the two prior cycles' headers.
Findings: 6 blocking, 4 non-blocking, 1 observation
Prior cycle: reviews/conversation-retro-cycle-2.md
Dave should inspect: F-1 and F-3 — the revision names a Chief of Staff act ("session rotation") and a closing act ("the stop signal") that exist in no governed document; whether to define them, or to drop the trigger, is a methodology decision. F-2 — the trigger set and Decision Layer rule 12 disagree, and which of the two moves is yours.

## F-1 — blocking
Claim: the second trigger names a Chief of Staff act that no governed document defines or assigns, so the trigger cannot be recognized by the role expected to fire it.
Location: skills/conversation-retro.md:28.
Evidence: verified by running `grep -rn -i "rotat" --include='*.md'` over the governed set (policies, roles, skills, context-sets, boundaries, docs/global-context, engagements, LEXICON.md, operating-model.md) at 54cc0d2 — the only hit is this line. roles/chief-of-staff.md @ 54cc0d2 enumerates the role's acts and contains no rotation trigger and no ack step; its nearest act is line 119, "When work needing the currently-loaded expensive context is done, says so and recommends ending the session." Read in OPEN-ITEMS.md:1340 and retros/retro-synthesis-20260831T163000.md (T23) that the rotation trigger is an open item whose own status line reads "no rotation trigger and no autonomous-run skill exist" — inferred by reading that the act is unbuilt, not merely unnamed here.
Consequence: criteria 1, 11 and 12. A Chief of Staff session reading its own role document has no act called "session rotation" to perform, so trigger 2 never fires; a session reading this skill instead infers a duty its role document does not grant. The rubric's criterion 11 names exactly this — language implying authority the methodology does not grant — and criterion 1 forbids a file that assumes the reader can open another one, which here would not help since no other file states it.
Fix: either define the rotation act and its ack in roles/chief-of-staff.md in the same change package, and state the trigger here in the words that document uses; or restate the trigger in terms of the act that already exists ("the Chief of Staff recommends ending the session and Dave acks"); or drop trigger 2 until the act is governed.
Related: F-3.

## F-2 — blocking
Claim: the trigger set is declared closed and conflicts with Decision Layer rule 12, which states a broader obligation with exceptions this file does not carry.
Location: skills/conversation-retro.md:24-30.
Evidence: verified by reading docs/global-context/decision-layer.md:31 @ 54cc0d2 — "End every session with a retro. Evidence separate from interpretation; near-empty is a valid result. A session that produced no artifact and made no decision may skip it. A reviewer-gated cycle conversation runs no retro unless directed; its cycle directive is its decision record. When a baton is also owed, the baton goes first; the retro follows and never delays it." The file under review states "Three triggers reach this procedure" and conditions the third on Dave signalling the end of the chat.
Consequence: criterion 12. Rule 12 attaches the obligation to session end unconditionally; this file attaches it to Dave's signal, and its list is exhaustive by its own words. A decision session that ends without an explicit signal is owed a retro by rule 12 and reaches no trigger here. The file also omits rule 12's skip condition (no artifact, no decision) and its baton-first ordering, so a session working from this file alone gets the obligation without its two limits. Core rule 9 requires the disagreement surfaced, not resolved by picking one.
Fix: reconcile the two in one change package — either state the trigger set so it matches rule 12's condition and carries its exceptions by reference to the same wording, or amend rule 12. The reviewer does not choose which document moves.
Related: F-7.

## F-3 — blocking
Claim: "the stop signal" is an undefined term used as an instruction.
Location: skills/conversation-retro.md:29-30.
Evidence: verified by running `grep -rn -i "stop signal" --include='*.md' .` at 54cc0d2 — two hits: this line, and retros/retro-triage-board.md:275, which is corpus data and not a governed document. The term is absent from LEXICON.md, docs/global-context/core.md and every file in the governed set.
Consequence: criteria 1 and 11, and the LEXICON touch rule. The instruction "close with the stop signal" directs an act whose definite article asserts a fixed, known referent that does not exist. An agent reading the bundle cannot perform it and cannot look it up, because there is nothing to look up.
Fix: define the signal inline in one clause, or add it to LEXICON.md in the same change package, or cut the clause and end the trigger at "Run the retro."
Related: F-1.

## F-4 — blocking
Claim: the audience selector places a decision-session-only procedure in every execution-session bundle.
Location: skills/conversation-retro.md:4 (frontmatter `audience: [all-roles, human]`), against line 9.
Evidence: verified by running `bin/bundle --audience coder-agent` and `bin/bundle --audience reviewer-agent` at 54cc0d2 — this document's heading appears in both. bin/bundle:188 returns membership unconditionally when `all-roles` is present. roles/coder-agent.md and roles/reviewer-agent.md both carry `session: execution` (verified by reading their frontmatter). The document's own first line states "This procedure runs in a decision session," and docs/global-context/decision-layer.md:10 states execution sessions never receive that file.
Consequence: criteria 7 and 10. Every execution-session bundle carries 159 lines that say nothing that kind of session needs, and the file cannot contribute anything to those bundles that it earns its place with. Criterion 7 requires the file to say nothing only the other kind needs; here the whole file is that.
Fix: change `audience:` to `[all-decision-roles, human]`, which bin/bundle already resolves by reading each role's `session:` field. If the file must stay on the all-roles floor for another reason, that reason belongs in the file and the criterion 7 conflict must be dispositioned.

## F-5 — blocking
Claim: the Dates rule names a remote-hosted artifact as the primary source for `date:`, against the absolute no-remote rule stated fifty lines above it.
Location: skills/conversation-retro.md:92-95, against 44-47.
Evidence: verified by reading both sections at 08e54f6. Line 46-47 states "Producing a retro reads nothing from and writes nothing to any remote, GitHub included. Every input is the conversation itself and the local tree." Line 93-94 states "Derive it from the last dated artifact the session touched — a merged pull request, a commit, a review artifact." RS-1's resolution in docs/cycles/conversation-retro-cycle-1-editor-directive.md:64-66 is binding intent: "Remove or rewrite any text implying the retro session touches a remote."
Consequence: criterion 12, against a ruled intent of this same revision. A merged pull request's merge date is canonically held by the forge; the ordinary way to obtain it is a GitHub API read, which the section above forbids absolutely. An agent following the Dates rule literally breaches the rule the revision was chiefly ordered to install. The local merge commit does carry the date, but nothing in the text says to read it there.
Fix: name the local artifact, not the remote one — "the merge commit of a pull request" — or add the clause "as recorded in the local tree" to the derivation list.

## F-6 — blocking
Claim: the unsynthesized set RS-3 requires to be computable is not computable as specified, because the comparison set is the directory and the directory holds files that are not retros.
Location: skills/conversation-retro.md:141-147.
Evidence: verified by running `ls retros/` at 54cc0d2 — the directory holds 31 files, of which retro-synthesis-20260831T163000.md, retro-triage-board.md, board-dispositions-20260831T213000Z.md, retro-notes-20260824T2020.md, github-mcp-reliability-retro.md and 0-retro-20260831T0000-fiducial-agreeing-clusters.md are not retros in the schema this file defines. The rule states the next synthesis "computes its input set by comparing those lists against the directory." Line 140-142 also places synthesis output in that same directory, and no filename is prescribed for a synthesis document anywhere in the file.
Consequence: criterion 11 — an underspecified condition — and RS-3's ruled intent. A synthesis run against the directory treats prior syntheses, the triage board and the dispositions file as unsynthesized retros, and states a count that includes them; the count the rule requires it to state is therefore wrong on the first run. Because a synthesis lands in the directory it reads, the error compounds each cycle.
Fix: state the comparison set as the files matching the retro filename form this document prescribes, not the directory; and prescribe the synthesis document's filename so it is mechanically distinguishable from a retro.

## F-7 — non-blocking
Claim: the file restates a Decision Layer rule.
Location: skills/conversation-retro.md:32-33.
Evidence: verified by reading docs/global-context/decision-layer.md:31 @ 54cc0d2, whose fourth sentence is "A reviewer-gated cycle conversation runs no retro unless directed; its cycle directive is its decision record." Lines 32-33 here say the same thing in near-identical words.
Consequence: criterion 4. The restatement is also partial — it copies one of rule 12's four clauses and not the other three — which is what makes F-2's mismatch read as authoritative rather than as a gap. A reader in a decision bundle has both files and gets one rule stated twice, differently scoped.
Fix: cut lines 32-33, or resolve F-2 and F-4 first, since a move to `all-decision-roles` makes the restatement plainly redundant and a decision to keep the all-roles floor may make it necessary.
Related: F-2, F-4.

## F-8 — non-blocking
Claim: rules carry trailing justifications and a "never X" restatement.
Location: skills/conversation-retro.md:25, 63-66, 97-99.
Evidence: verified by reading at 08e54f6. Line 25, "All three run it unchanged; none is a separate mechanism" — the second clause restates the first as a negation. Lines 63-66, "The two are never merged: the schema catches in-session corrections on its own, and repetition across sessions is what it would otherwise miss" — the clause after the colon argues for the rule. Lines 97-99, "Where the two disagree, they are both correct and both stated. A retro written days after its session carries the session's date and its own generation time" — the second sentence illustrates the first without adding a rule.
Consequence: criterion 6. Three added passages carry argument where the criterion requires the instruction alone; the pattern is what the criterion exists to stop accreting.
Fix: cut the clause after the semicolon at line 25, the clause after the colon at line 64, and the sentence at lines 98-99.

## F-9 — non-blocking
Claim: the `date:` derivation has no rule for the case where both its sources are absent.
Location: skills/conversation-retro.md:92-95, against 108.
Evidence: verified by reading at 08e54f6. Line 94-95: "Where the session touched no dated artifact, take it from the `source:` pointer." Line 108 defines `source:` as "conversation pointer: title, URL, or export filename; null if none."
Consequence: criterion 11 — an underspecified condition. A retro of a conversation that touched no dated artifact and has a null `source:` has no rule for a required schema field, and the agent decides. Given the file's own point that `date:` is not generation time, the obvious fallback is the one the rule was written to forbid.
Fix: state the fallback in one clause — the session's date as stated in the conversation, or `generated:` with the substitution declared in the retro.

## F-10 — non-blocking
Claim: policies/document-metadata-policy.md asserts this file excludes its own revisions from the expedited path; this file excludes something else.
Location: skills/conversation-retro.md:18-20, against policies/document-metadata-policy.md:184-185.
Evidence: verified by reading both at 54cc0d2. The policy states "A document may exclude its own revisions from this path, and the retro skill does." This file states "A methodology revision surfaced by a retro or a synthesis takes the full review cycle, whatever lighter path it would otherwise be eligible for" — a rule about revisions this procedure surfaces, in any document, not about revisions of this document.
Consequence: criterion 12. The policy's cross-reference misdescribes what this file says; a reader checking the policy's claim against this file does not find it. The operational harm is bounded — policies/document-metadata-policy.md:163 lists skills/conversation-retro.md in the gate-document class, which makes it ineligible independently — so the defect is a false cross-reference rather than an open route.
Fix: either add the self-exclusion this file is said to state, or correct the policy's sentence to cite the gate-document list. One of the two moves; the reviewer does not choose.

## O-1 — observation
Claim: existing retro filenames do not conform to the revised filename rule, and the grandfather clause already covers them.
Location: skills/conversation-retro.md:83-85, 78-79.
Evidence: verified by running `ls retros/` at 54cc0d2 — of 26 files named `retro-*`, four carry the `Z` designator the revised rule requires; the rest are dashed date-time splits, `T`-forms without `Z`, or truncated `T`-forms such as retro-20260826T2130.md. Line 78-79 states retros predating adoption of this skill are grandfathered as-is.
Consequence: none. Recorded so the next cycle does not re-derive it as a finding, as cycle 1's CR-1 did against the pre-revision rule.

## Ruled-change realization — RS-1 through RS-5

Assessed against docs/cycles/conversation-retro-cycle-1-editor-directive.md @ e41d63f7c4bc39c76007b466ad065119bed3dafe. Intent binding, wording the Editor's.

| Ruled change | Where it landed | Realized |
| --- | --- | --- |
| RS-1 — no remote; landing is a separate command-block step; connector path retired | lines 44-54 (new section), 156-159 (Output rewritten) | Yes, with F-5 — the added Dates rule reintroduces a remote-named source. |
| RS-2 — `date:` is the session's last interaction; add `generated:`; timestamp per DEC-000290 | lines 83-85 (filename form), 90-99 (new Dates section), 106-107 (schema fields), 75 (`date` → `dates`) | Yes. The timestamp form matches DEC-000290 @ 54cc0d2 word for word. F-9 is a gap in the derivation, not a departure from intent. |
| RS-3 — a synthesis names what it covered, so the unsynthesized set is computable | lines 141-147 | Partially — the `covers:` list landed; the computation it exists to enable does not work against the directory as written. See F-6. |
| RS-4 — surface preferences repeated across sessions, held separate from in-session corrections, as candidate standing rules | lines 56-68 (new section), 124-127 (new schema section) | Yes. The separation from in-session corrections is stated explicitly and the schema carries its own section. The retired term "prompt" was correctly avoided. |
| RS-5 — state the three triggers as one skill's "Use when" set | lines 22-30 | Partially — all three are stated and declared one mechanism, but two of the three name acts that exist nowhere governed (F-1, F-3) and the set conflicts with Decision Layer rule 12 (F-2). |

Verification run: bin/check-frontmatter --all, exit status 0, one NOTE line — "in-scope: [scope-summary] 62 file(s) matched, from 14 configured glob(s)". Run in the assigned worktree, inside the sandbox.
