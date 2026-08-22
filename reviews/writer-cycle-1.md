# Review: roles/writer.md — cycle 1

Verdict: changes-required
Reviewed: roles/writer.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 15 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at eea66dd (cycle 26), never rubric-reviewed.
Cross-checked: docs/global-context/core.md (Standing 2, 4; Evidence 6), docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, prose-criteria.md, roles/context-quality-reviewer.md, roles/skeptic-risk-agent.md, engagements/skeptic.md, and every other role document under roles/ for the session-kind declaration — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether the retirement of the writing pipeline was correct — that is docs/cycles/pass1-cycle-26-writing-retire-20260822T220000.md's decision and this review does not re-open it; the archived pipeline documents under docs/history/writing/.
Findings: 3 — 2 blocking, 1 non-blocking
Prior cycle: none
Dave should inspect: WR-2 — which Skeptic the Writer is offering, and whether the Writer may name a reviewer whose document it has never been given.

## WR-1 — criterion 10, answered first
The file lands in the `writer` bundle (19 files at 8402c23) and contributes the Writer's operating rules — draft-in-the-document-pane, Dave's edits as voice evidence, the criteria-proposal loop, the stop-at-done rule — none of which prose-criteria.md states. It earns its place. The findings below are repairs, not a retirement case.

## WR-2 — blocking
Claim: The closing instruction names two reviewers, one of them ambiguously, and neither document is in this file's bundle.
Location: roles/writer.md:15 ("When Dave says the piece is done, state that a Skeptic and a Context Quality Reviewer are available for it, and stop.")
Evidence: Verified by running — the `writer` bundle resolves to 19 files and contains neither roles/context-quality-reviewer.md (`audience: [context-quality-reviewer, chief-of-staff, human]`), roles/skeptic-risk-agent.md (`[skeptic-risk-agent, chief-of-staff, human]`), nor engagements/skeptic.md (`[skeptic, human]`). Two live documents are titled Skeptic and hold different authority: roles/skeptic-risk-agent.md:9-11 is "a stage with gate force," engagements/skeptic.md:12-14 is advisory with explicitly no gate. Criterion 1, criterion 11.
Consequence: The instruction is the last thing the Writer does, and it is unexecutable as written: the session cannot say what either reviewer would do, and "a Skeptic" resolves to two different answers with different force. Criterion 11 names "boundaries two roles could both claim" as a defect; this is that, delivered as an instruction.
Fix: Name which Skeptic, and state in one line what each pass checks. If the Writer is meant to offer them, the offer has to carry enough for Dave to choose.

## WR-3 — blocking
Claim: The file never states its session kind.
Location: roles/writer.md:7-9 — the opening, where every other role document declares it.
Evidence: Verified by running — all nine other files under roles/ declare a session kind in their first two lines (roles/chief-of-staff.md:9 "operates as a decision session"; roles/coder-agent.md:9, roles/reviewer-agent.md:9, roles/test-designer-agent.md:9 "You run in an execution session"; roles/context-quality-reviewer.md:9, roles/spec-reviewer-agent.md:9 "runs as an execution session"; roles/architect-agent.md:9 and roles/release-manager-agent.md:9 name both). This file names none. Criterion 7.
Consequence: The mechanics described — a document pane, chat alongside it, Dave editing directly, an iterative criteria-proposal loop — are decision-session mechanics, so the answer is inferable; criterion 7 exists because inferable is not stated. Concretely, the session kind decides whether docs/global-context/decision-layer.md reaches the Writer, and the Writer's register rules would be different if it did.
Fix: State it. On the evidence of the file's own mechanics, "The Writer runs as a decision session."

## WR-4 — non-blocking
Claim: The publication rule restates Core and is stated a second time in the same bundle.
Location: roles/writer.md:14 ("Nothing publishes on agent judgment. Dave reads every word before anything publishes.") against docs/global-context/core.md:14 (Standing 2: "Dave decides. You propose. Agreement, release, prioritization, and publication are his.") and prose-criteria.md:19-22 ("Dave reviews every word before publication. Agents draft under direction; nothing publishes on agent judgment.")
Evidence: Verified by running — docs/global-context/core.md carries `audience: [all-roles, human]` and prose-criteria.md carries `audience: [writer, human]`; both are in the 19-file `writer` bundle with this file. Criterion 4.
Consequence: One rule in three places in one bundle, two of them near-verbatim. Criterion 4 is explicit that a rule Core states is removed here.
Fix: Cut the line from this file. Whether it also comes out of prose-criteria.md is PC-2.
Related: PC-2
