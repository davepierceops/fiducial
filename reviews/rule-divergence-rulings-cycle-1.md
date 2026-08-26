# Review: branch rule-divergence-rulings — cycle 1

Verdict: changes-required
Reviewed: LEXICON.md, operating-model.md, context-sets/testing-and-verification.md, docs/global-context/core.md, docs/global-context/decision-layer.md, docs/global-context/review-rubric.md, policies/source-of-truth-policy.md, roles/test-designer-agent.md, skills/test-plan-review.md @ 21b60b3
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-26
Scope: `git diff d1086a5..21b60b3 -- docs/global-context context-sets policies roles skills LEXICON.md operating-model.md` — eight cluster commits (C001–C008) gated as one reconciliation rather than nine per-document cycles, which is why this artifact's stem names the branch and not a document (Dave's decision, 2026-08-25); all twelve rubric criteria applied to the edited text of each of the nine documents, and criterion 12 applied across the governed corpus; gating whether the edits carry out rulings C001–C008 recorded in docs/cycles/rule-divergence-rulings-20260825T1900.md, not whether those rulings are right.
Cross-checked: every row cited by clusters C001–C008 in docs/rule-register/rule-clusters-20260825T1600.md, at its location in the tree at 21b60b3; the register docs/rule-register/rule-register-20260825T1435.md; a corpus-wide grep sweep per ruling over the frontmatter in-scope set (policies/, roles/, context-sets/, boundaries/, skills/, specs/, vendors/, docs/global-context/, engagements/, operating-model.md, LEXICON.md, prose-criteria.md) for red-gate strength, release-impact-label enumerations, the `blocking` definition, retro triggers, directive parts, changed-fact propagation, clean-pass format, and canonical/derived conflict handling; the document metadata policy's revision lifecycle and Scope; the review-artifact schema; the Context Quality Reviewer role's scope and cession; `bin/check-frontmatter --all`, run.
Not inspected: the correctness of rulings C001–C008 themselves (out of scope by directive); the nine documents' unedited text outside the passages the rulings reach; the commit-by-commit history within d1086a5..21b60b3 (the tree at 21b60b3 was reviewed, not each intermediate state); MANIFEST.md, OPEN-ITEMS.md, retros/, docs/history/, and prior review artifacts, all outside the frontmatter in-scope set; C003's inlining of the behavioural-red wording in five places, excluded as a finding by directive.
Findings: 3 blocking, 6 non-blocking, 2 observations
Dave should inspect: B1 and B2 — both are wording choices inside the C001 exception you dictated, and picking the wording is yours. N2 — the C007 reconciliation you directed produces a second copy of a Core rule, which rubric criterion 4 forbids; whether the policy keeps its sentence is yours.

## B1 — blocking
Claim: Core's new canonical/derived exception stops the whole session, while the source-of-truth policy stops only the conflicted item, so the two now order different acts on the same conflict.
Location: docs/global-context/core.md:25 (register R0018, R0019) against policies/source-of-truth-policy.md:52–58 (register R0494, R0495, R0496, R0497)
Evidence: Verified by reading both passages at 21b60b3. Core rule 9 reads "a conflict between a canonical document and an artifact derived from it stops the session and waits for Dave." The policy's numbered hard stop reads "1. Stop work on the conflicted item. 2. Surface the conflict to Dave explicitly in the current response... 3. Wait for Dave to resolve it." Ruling C001 directed that the policy's text stays.
Consequence: An execution session carrying a directive with six instructions, one of which hits a canonical/derived conflict, abandons the remaining five under Core and completes them under the policy. C001 was raised because Core and the policy ordered different acts on this conflict; after the edit they still do, on the stop's scope rather than on whether to stop.
Fix: Make Core's exception state the scope the policy states — stop work on the conflicted item and surface it — or amend the policy's step 1 to match Core. One clause, either file; which one is Dave's.

## B2 — blocking
Claim: Core's new exception tells the agent to "wait for Dave," which an execution session cannot do, and Core states the executable form of that instruction three times elsewhere.
Location: docs/global-context/core.md:25
Evidence: Verified by reading core.md at 21b60b3. Core governs both session kinds (rule set header: "Rules for every agent session"). Its Vocabulary defines an execution session as "an LLM agent session carrying out a directive against a working tree" — no channel to Dave mid-session. Core rule 11 reads "Cannot execute as written → stop and surface"; rule 12 "report only what the operator reported"; rule 15 "stop and report rather than recover." The added exception is the only place Core tells a session to wait.
Consequence: An execution session reading the exception literally has no defined next act — it cannot wait, and the rule does not tell it to report and end. It resolves the gap by inference, which is what rubric criterion 11 forbids; two sessions hitting the same conflict end differently, one reporting and one idling out the directive.
Fix: State the executable form for the execution case — stop and surface the conflict in the report — and keep "wait for Dave" for the decision session, or write it as "stops and surfaces it for Dave's resolution," which both kinds can carry out.

## B3 — blocking
Claim: The definition of done still states the red-gate at its pre-C003 strength, so a change reaches done on a missing-import red.
Location: operating-model.md:209 (register R0211)
Evidence: Verified by reading and by grep sweep over the in-scope set at 21b60b3. The bullet reads "the pre-written tests were confirmed failing, then turned green." C003 reached operating-model.md lines 20, 130 and 137, roles/test-designer-agent.md:26 and skills/test-plan-review.md:37 — the five rows cluster C003 cites. Line 209 states the same rule and is not in that cluster's row list, so the edit did not reach it.
Consequence: A change whose only red was `Cannot find package '@/lib/services/x'` fails the gate at step 4 as line 137 now states it, and satisfies the definition of done at line 209. A Release Manager assembling the package against the definition of done finds every bullet satisfied and ships it. This is the exact failure C003 exists to close, surviving in the one list a release reads.
Fix: Carry the qualifier into the bullet: "the pre-written tests were confirmed failing on bad logic — not just on an absent import — then turned green."

## N1 — non-blocking
Claim: The Coder's red-gate check tests only that a confirmation exists, not that it is behavioural, so the Coder accepts an import-only red without flagging it.
Location: roles/coder-agent.md:21 (register R0592)
Evidence: Verified by reading and by grep sweep at 21b60b3. The line reads "If the Test Designer's red-gate confirmation is absent, flag it rather than proceed." roles/coder-agent.md is not among cluster C003's cited files and was not edited on this branch.
Consequence: The Test Designer now owes a behavioural red, but the one role positioned to catch a weak one — the Coder receiving the handoff — is instructed to check only for presence. A red-gate confirmation that names a missing module passes the Coder unremarked, and the separation C003 protects fails silently at the handoff.
Fix: Widen the condition to absence or import-only: "If the Test Designer's red-gate confirmation is absent, or shows the tests failing only on an absent import, flag it rather than proceed."
Related: B3

## N2 — non-blocking
Claim: The C007 edit makes the source-of-truth policy restate Core rule 13's session-kind split, which rubric criterion 4 forbids.
Location: policies/source-of-truth-policy.md:64–67 against docs/global-context/core.md:32
Evidence: Verified by reading both at 21b60b3. Core rule 13 now reads "An execution session carrying a directive updates every such place within the files the directive permits, and names any place outside them. A decision session names every place and edits none." The policy now reads "An execution session carrying a directive updates the stale derived artifacts within the files its directive permits, and names any outside them; a decision session names the derived artifacts that need updating and edits none." Core is `order: 0` and `audience: [all-roles, human]`; the policy is `audience: [all-roles, human]`, so no bundle carries the policy without Core.
Consequence: One rule now has two committed statements whose wording already differs ("every such place" against "the stale derived artifacts"). The next edit to either drifts them apart, and the corpus grows the class of divergence this branch was cut to remove. Ruling C007 directed the reconciliation, so this is the ruling's cost rather than the executor's error.
Fix: Reduce the policy's paragraph to what is specific to its case — that a canonical change leaves derived artifacts stale — and let Core state who edits and who names; or cut the paragraph and let Core carry it whole.

## N3 — non-blocking
Claim: The behavioural qualifier is inserted between the verb phrase and its parenthetical, garbling the sentence.
Location: roles/test-designer-agent.md:26
Evidence: Verified by reading at 21b60b3. The bullet reads "run tests and confirm they fail on bad logic — not just on an absent import — (red-gate) before handing off to the Coder". An em-dash aside closing immediately before an opening parenthesis strands "(red-gate)" from the noun it labels.
Consequence: The Test Designer's own role document states its single hardest obligation in a sentence that has to be re-read to parse. Rubric criterion 1 requires the file to work read cold inside a bundle by an agent that has never seen the repository, and this is that agent's operative line.
Fix: Move the label to the head of the clause: "run the red-gate before handing off to the Coder — confirm the tests fail on bad logic, not just on an absent import."

## N4 — non-blocking
Claim: A spec quotes operating-model.md line 137 verbatim as evidence, and the C003 edit changed that line, so an `observed`-labelled quotation no longer matches its source.
Location: specs/directive-tooling.md:155
Evidence: Verified by reading both at 21b60b3. The spec reads: `- Code. \`operating-model.md\` line 137: "The red-gate at step 4 is mandatory."` under a heading that labels the four bullets "*observed* in committed text, and each half checks out". operating-model.md:137 now reads "The red-gate at step 4 is mandatory and behavioral: the tests demonstrably fail". The quotation is unpinned — no SHA — unlike the sibling bullets, which cite `@ ed88dcde` and `@ a06460a9`.
Consequence: A reader checking the citation at HEAD finds the quoted string absent from the named line, and an evidence claim the spec labels *observed* fails the check it invites. specs/ was outside the ruling directive's permitted files, so Core rule 13 as newly reworded required the executing session to name this place rather than edit it.
Fix: The Spec Reviewer's to dispose of, not this role's — the PRD and TRD are ceded. Surfaced here because the C003 edit is what stales the quote. Either pin the citation with a SHA, as the sibling bullets do, or re-quote line 137 as it now reads.

## N5 — non-blocking
Claim: The Claude adapter states the red-gate at its pre-C003 strength.
Location: CLAUDE.md:31
Evidence: Verified by grep sweep over the repository root and vendors/ at 21b60b3. The line reads "Work spec-first: specs and ACs before tests, tests confirmed failing before implementation." CLAUDE.md is an adapter, outside the frontmatter in-scope set the document metadata policy's Scope enumerates, and outside the ruling directive's permitted files.
Consequence: The adapter is the file a Claude-based tool loads first, and it now states a rule the corpus has strengthened. An agent working from the adapter alone confirms a missing-import red and believes it satisfied spec-first discipline. The source-of-truth policy's adapter discipline puts the adapter downstream of the methodology, so this is drift in the direction the policy names.
Fix: Carry the qualifier into the adapter line, in a change the adapter's own path permits.
Related: B3, N1

## N6 — non-blocking
Claim: Core rule 13's new decision-session branch bars a decision session from editing any place stating a changed fact, including the artifacts Core's own Vocabulary says it writes.
Location: docs/global-context/core.md:32 against docs/global-context/core.md:38 and docs/global-context/decision-layer.md:28
Evidence: Verified by reading at 21b60b3. Rule 13 ends "A decision session names every place and edits none." Core's Vocabulary reads that a decision session "produces the artifacts that direct and record work: directives, session records, tracker updates. It reads freely and writes these artifacts." Decision Layer rule 9 reads "A loose-end tracker is a record, not derived state," and the spec-and-change-discipline context set requires the tracker be updated at defined checkpoints.
Consequence: A decision session that corrects a count in a tracker it maintains, then finds the old count stated two lines below, is told by rule 13 to name the second place and edit neither — including the artifact it is the designated author of. It resolves the conflict by inference, and two sessions resolve it differently.
Fix: Bound the prohibition to what it means: a decision session edits the artifacts it authors and names every place outside them.

## O1 — observation
Claim: All nine documents flipped `status: agreed` to `in-review` with `last-reviewed: null`, which the ruling directive's DO-NOT list forbade and the document metadata policy requires.
Location: frontmatter of all nine reviewed documents
Evidence: Verified by reading the diff and by running `bin/check-frontmatter --all`, which exits 0 over 54 in-scope files. The ruling directive states "Do not flip any `status:`"; the metadata policy's revision lifecycle states "When an `agreed` document is edited, the same commit flips `status: in-review` and resets `last-reviewed: null`" with "No exceptions for trivial edits **on the way out**."
Consequence: None here — the policy governs, the flips are correct, and the executor was right to make them. Recorded because the directive and the policy gave opposite instructions on the same act, and the next directive author should not repeat the phrasing.

## O2 — observation
Claim: The canonical/derived conflict rule is now stated in three places, one of them a pointer.
Location: docs/global-context/core.md:25, policies/source-of-truth-policy.md:45–60, operating-model.md:38
Evidence: Verified by grep sweep at 21b60b3. operating-model.md:38 reads "A conflict between a derived artifact and a canonical one is handled per the Source of Truth policy" — a pointer, not a restatement, and so not a criterion-4 defect. Core and the policy both state the rule directly.
Consequence: None on its own; the pointer is the shape criterion 4 asks for. It is the third surface B1's wording fix has to leave true, and is recorded so the fix is not applied to two of three.
