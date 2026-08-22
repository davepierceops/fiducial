# Review: engagements/assistant.md — cycle 1

Verdict: changes-required
Reviewed: engagements/assistant.md @ 1bbd5b7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 39 lines, against all eleven criteria of the review rubric @ 1bbd5b7. Includes a rule-by-rule comparison against the Decision Layer.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, engagements/cartographer.md, engagements/skeptic.md, engagements/quiet-notes.md, policies/document-metadata-policy.md, docs/batons/baton-20260822T153848.md — all @ 1bbd5b7.
Not inspected: `engagements/comfy/**` (its own cycle, per the directive); `bin/bundle`'s handling of a file with no frontmatter (not run — the consequence below is stated as inference, not as observed behaviour); whether the Assistant role as practised matches this text (no session record was consulted).
Findings: 11 — 6 blocking, 4 non-blocking, 1 observation
Prior cycle: none
Dave should inspect: AS-3 (this file instructs an execution session in Decision Layer rules that the Decision Layer says execution sessions never receive) and AS-4 (it instructs the agent to maintain state that Decision Layer rule 9 forbids maintaining).

## Criterion 10 first

**Disposition: retain-with-changes — but the residue is small, and Dave should
see how small before agreeing to keep the file.**

The directive asks four questions of each engagement file.

**Is this a role, a skill, a standing instruction to a session, or history?**
A **role**. It titles itself one, it describes a standing posture rather than a
procedure, and `engagements/working-with-dave.md` @ 1bbd5b7 already selects for
it by name in its `audience:` list.

**What `audience:` follows?** `[assistant, human]`. `assistant` is an
established value — working-with-dave.md carries `audience: [assistant,
cartographer, skeptic, human]`, so the selector this file needs already exists
and already points at it. The file just does not carry its half.

**Does a role document already carry it?** No role document under `roles/` is
named Assistant, so there is no collision of the kind `engagements/skeptic.md`
has. But **the Decision Layer carries most of the content.** Six of the eight
substantive rules in this file are Decision Layer rules in different words —
see AS-5 through AS-10.

**What survives the cuts.** Two things: the completion-nudge practice, in
particular "want a skeptic pass?" when work is about to leave the building; and
the quiet-notes practice. Everything else is either already in the foundation or
contradicts it. That is a genuine contribution to a bundle — an engagement has a
client, a boundary, and work that leaves the building, and no foundation file
knows that — but it is roughly ten lines, not thirty-nine.

**Retain-with-changes**, with the understanding that the changes remove most of
the file. If Dave prefers, the surviving ten lines fold into
`engagements/working-with-dave.md`, which every engagement role already loads;
that would be **merge-into** and is a defensible alternative. The reviewer's
recommendation is retain, because the completion-nudge rule is the Assistant's
and not the Cartographer's or the Skeptic's, and working-with-dave is loaded by
all three.

## AS-1 — blocking
Claim: the file carries no frontmatter at all, so it has no `audience:` and cannot be selected into any bundle.
Location: engagements/assistant.md:1 (the file opens with `# Role: Assistant`; there is no `---` block)
Evidence: verified by reading the file's first line. Verified by reading engagements/working-with-dave.md @ 1bbd5b7, which does carry frontmatter, including `assistant` as an audience value — so within the same directory one file is selectable and this one is not.
Consequence: criterion 2, the selector criterion, fails outright. Under the baton's settled rule @ 1bbd5b7 — agents receive `bin/bundle <audience>` output and never the repository — a file with no `audience:` reaches no agent. The Assistant role, described as "the role Dave uses most," is currently unreachable by the mechanism that delivers roles. This consequence is inferred from the settled selection rule, not observed by running the compiler.
Fix: add frontmatter — `status: draft`, `last-reviewed: null`, `audience: [assistant, human]`. `order:` is not needed; the file's position relative to working-with-dave.md in a bundle does not change its meaning.
Related: CA-1, SK-1, QN-1 — the same defect in all four single engagement files.

## AS-2 — blocking
Claim: `engagements/**` is absent from the document-metadata policy's in-scope set, so nothing checks the frontmatter these files need.
Location: engagements/assistant.md (whole file), against policies/document-metadata-policy.md @ 1bbd5b7 lines 24–35
Evidence: verified by running `git show 1bbd5b7:policies/document-metadata-policy.md | sed -n '20,55p'`. The in-scope list is `policies/**`, `roles/**`, `context-sets/**`, `boundaries/**`, `skills/**`, `specs/**`, `vendors/**`, `operating-model.md`, `README.md`, `LEXICON.md`. `engagements/**` appears in neither the in-scope nor the out-of-scope list. The policy states "Enforcement (hooks) checks exactly the in-scope set."
Consequence: this is why AS-1 was possible and went unnoticed. Four files that must carry `audience:` to function sit outside the only mechanism that checks whether they do — and `engagements/working-with-dave.md` carries correct frontmatter by hand, verified by nobody. Adding frontmatter to these four files without extending the glob fixes today's instance and leaves the hole open.
Fix: add `engagements/**` to the in-scope set in policies/document-metadata-policy.md. That is an edit to a policy outside this cycle's scope and outside this cycle's no-edit instruction, so it is raised here as a finding for the policy's own cycle. Note the baton's sequencing rule: the metadata policy's scope is already being revisited in the document-metadata-policy cycle, which is where this belongs.
Related: CA-2, SK-2, QN-2.

## AS-3 — blocking
Claim: the file instructs an execution session in Decision Layer rules, which the Decision Layer states execution sessions never receive.
Location: engagements/assistant.md:7–13, :17–21, :34–39 (the register rules), against engagements/working-with-dave.md:7 @ 1bbd5b7
Evidence: verified by reading. engagements/working-with-dave.md @ 1bbd5b7 states "This file is for execution sessions within an engagement." engagements/assistant.md:3 states "Load with `working-with-dave.md`", placing it in the same session kind. docs/global-context/decision-layer.md @ 1bbd5b7 states in its opening line: "Rules for decision sessions. Loads after Core and adds to it. **Execution sessions never receive this file.**"
Consequence: criterion 7. Either the Assistant is an execution session, in which case it is being handed the decision layer's register through a side door and the Decision Layer's exclusion is defeated; or the Assistant is a decision session, in which case working-with-dave.md's opening sentence is wrong about it and the Assistant should receive the Decision Layer directly and need none of the restatements in AS-5 through AS-10. The file does not say which, and the two readings produce different bundles.
Fix: state the session kind explicitly in the file. The reviewer's reading of the content — Dave says what he wants, you hand him the how, you nudge at completion, you never report unasked status — is that the Assistant is a **decision session** in an engagement, and that working-with-dave.md's blanket "for execution sessions" is the sentence that is wrong. That is Dave's call, not this role's, and it decides whether AS-5 through AS-10 are cuts or confirmations.

## AS-4 — blocking
Claim: the file instructs the agent to maintain a running status list, which Decision Layer rule 9 forbids.
Location: engagements/assistant.md:23–26 ("Keep quietly — A running list of what's in flight and what's done — render it when asked")
Evidence: verified by reading docs/global-context/decision-layer.md @ 1bbd5b7 rule 9: "**State is computed, never maintained.** Do not create status files or registers derivable from existing artifacts; if gathering state is tedious, propose a script. A loose-end tracker is a record, not derived state."
Consequence: a direct contradiction, not a restatement. What is in flight and what is done is derivable from the artifacts — branches, pull requests, commits — which is exactly the register rule 9 names. An agent holding both rules has to pick one, and the rubric's criterion 11 is precisely about not leaving that to inference. Note the second half of the same section (the quiet-notes list) is *not* a contradiction: rule 9's own carve-out says a loose-end tracker is a record, and quiet notes are that.
Fix: cut the running-list bullet. Answering "where are we" by computing it from the artifacts is what rule 9 already directs, and needs no instruction here.

## AS-5 — blocking
Claim: the "Defining property" section restates Decision Layer rules 7 and 8.
Location: engagements/assistant.md:7–13
Evidence: verified by reading docs/global-context/decision-layer.md @ 1bbd5b7 rule 7: "**He says what; you deliver how.** The first response to a request is the artifact — a block, a draft, a path — not a plan for it." And rule 8: "**Hand him the block, never the task.**" The file's lines 7–9 say the same in the same order, down to "a ready-to-run command block, a complete artifact, or a concrete path" against rule 7's "a block, a draft, a path".
Consequence: the defining rule of the role has two homes in one bundle. The engagement copy is the one that will drift, because the Decision Layer is reviewed as a foundation file and this is not.
Fix: cut lines 7–13. If AS-3 resolves toward "decision session", the Decision Layer already delivers this and the section is pure duplication; if it resolves toward "execution session", the rule has to be stated somewhere for execution sessions and this is the wrong file to decide that in.
Related: AS-9.

## AS-6 — non-blocking
Claim: the landmine bullet restates Decision Layer rule 3.
Location: engagements/assistant.md:14
Evidence: verified by reading decision-layer.md @ 1bbd5b7 rule 3: "**Warn once, then do it.** If you see a landmine, say so in one line while handing him what he asked for."
Consequence: a second wording of the same rule; the file's version drops "Do not gate on it or re-open a decision he has made," which is the operative half.
Fix: cut.

## AS-7 — non-blocking
Claim: the completion-nudge section restates Decision Layer rule 4.
Location: engagements/assistant.md:16–21
Evidence: verified by reading decision-layer.md @ 1bbd5b7 rule 4: "**Offer the next step once.** When work is done, say so and name the next step. A wave-off ends it."
Consequence: duplication — but partial, and this is the file's one genuine contribution. "Including 'want a skeptic pass?' when the work is about to leave the building (a PR, a doc to the client, a change to their systems)" is engagement-specific and appears in no foundation file.
Fix: cut the duplicated half ("say so in one line and offer the natural next step", "Dave waves it off in a word and you drop it. Nudge once, never twice"). Keep the skeptic-pass clause and the definition of leaving the building. That is the sentence worth a bundle slot.

## AS-8 — non-blocking
Claim: the quiet-notes bullet prescribes a fixed filename and a write mechanism, in a file that also has to explain what to do without write access.
Location: engagements/assistant.md:27–32
Evidence: verified by reading; the bullet names `quiet-notes.md`, its line format, and two delivery paths depending on access. Cross-checked against engagements/quiet-notes.md @ 1bbd5b7, which states the same line format a second time.
Consequence: the format is stated twice, in two files, one of which (quiet-notes.md) is reviewed this cycle and recommended for retirement. Criterion 3 also applies: `quiet-notes.md` is a path-shaped reference a bundle reader cannot resolve. The append-directly-or-render-a-block conditional is the right shape and should survive.
Fix: keep the practice and the line format here, since this is the file whose reader performs it; drop the path reference in favour of naming the artifact ("the engagement's quiet-notes record"). This is the half of QN-3's fix that lands in this file.
Related: QN-3.

## AS-9 — non-blocking
Claim: the "Never" list is four Decision Layer rules restated as prohibitions.
Location: engagements/assistant.md:34–39
Evidence: verified by reading decision-layer.md @ 1bbd5b7. Line 35 ("Gate, re-litigate, or 'have you considered'-ing a decision Dave has made") is rule 3's second half. Line 36 ("Produce a plan when a command was asked for") is rule 7. Line 37 ("Ask permission to draft the obvious next artifact — draft it") is rule 5 ("Pre-stage the predictable"). Line 38 ("Report status he didn't ask for") is rule 2's triage clause.
Consequence: criterion 6 names this shape directly — "'Never X' restatements of a stated rule … are cut." Four of them in six lines.
Fix: cut the section.
Related: AS-5.

## AS-10 — non-blocking
Claim: "Load with `working-with-dave.md`" is a path-shaped reference and an instruction the bundle has already carried out.
Location: engagements/assistant.md:3
Evidence: verified by reading. Under the settled rule that agents receive bundle output, a file that is in the bundle alongside this one needs no loading instruction; a reader that does not have it cannot act on the instruction.
Consequence: criterion 1 and criterion 3. Harmless to a human, meaningless to the reader the file is written for.
Fix: cut the clause. The `audience:` values are what pair the two files.
Related: CA-4, SK-5.

## AS-11 — observation
Claim: two uses of **track** appear, both in the carved-out sense.
Location: engagements/assistant.md:17 ("You track when a piece of work finishes"), :30 ("the `quiet-notes.md` tracker")
Evidence: verified by running a term sweep, then verified by reading LEXICON.md @ 1bbd5b7, whose carve-out covers "**track**, **tracking**, and **tracker** in the ordinary sense of keeping or consulting a record". Both uses are that sense. "unprompted" at line 26 is not the retired noun and is not counted.
Consequence: none. Recorded because the cycle directive instructs that every use be flagged.
Fix: none. Line 17 is cut anyway under AS-7 and line 30 is edited under AS-8.

## Note on a directive/LEXICON tension

The directive for this cycle states that every use of *dispatch*, *sync block*,
*track*, and *prompt* is a criterion-4 finding. LEXICON @ 1bbd5b7 states two
explicit carve-outs: *track/tracking/tracker* in the ordinary record-keeping
sense, and *prompt* meaning a tool's approval interrupt. Core rule 9 says two
sources that disagree are surfaced, not resolved by picking one. Uses covered by
a carve-out are recorded here as observations, not defects, and are counted
separately in the sweep. This note appears in all eight artifacts of this cycle.

## Sweep counts

- Rules restated from the foundation: **6** distinct Decision Layer rules — 2 (AS-9), 3 (AS-6, AS-9), 4 (AS-7), 5 (AS-9), 7 (AS-5, AS-9), 8 (AS-5). One further foundation rule is **contradicted** rather than restated: Decision Layer 9 (AS-4).
- Output-shape lists with a home elsewhere: **0**
- Path-shaped references: **2** (line 3, `working-with-dave.md`; line 30, `quiet-notes.md`)
- Vendor and model names: **0**
- Retired terms: **0 defects**, 2 carve-out uses recorded (AS-11)
- SLO / Top K copies: **0**
