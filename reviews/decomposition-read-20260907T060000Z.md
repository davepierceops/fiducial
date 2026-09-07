# Review: process/decomposition.md — process-sweep-read-20260907T060000Z

Verdict: ready-with-findings
Reviewed: process/decomposition.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/decomposition.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 39 lines, with both bracketed ids — R0012, R0013 — resolved to their files under rules/ at the base ref, and each of the eight steps compared against the baseline's eight.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; process/change-flow.md at the same ref, which states the same two-tranche cap; process/spec-test-suite.md, which is the one act step 2 admits against an open spec; rules/R0003.md and rules/R0199.md, reached while searching for a row stating the cap.
Not inspected: any decomposition doc under docs/packages/. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 1 — 0 blocking, 0 non-blocking, 1 observation
The human should inspect: DC-01, which is the two-tranche cap the directive asks about. This document places its citation correctly; process/change-flow.md does not, and CF-02 in that artifact is the blocking half of the same issue.

## Verdict (citations): ready

Both resolve and both sit on a clause that relies on them. `[R0012, R0013]` in step 4 annotates "check the claim on the documents it would touch", and R0012 is what makes a document claimed ("A spec document is claimed when it appears in an open delta's diff") while R0013 is the rule the check enforces ("A document claimed by one open delta is not claimed by a second; keep concurrent deltas over disjoint spec territory"). The two clauses that follow the semicolon — the cap and "never two deltas over one tranche" — sit outside the citation; the second is carried by R0013 through the claiming rule, and the first is DC-01. The placement here is the correct one, and it is what makes the same sentence in process/change-flow.md a finding there rather than here.

## Verdict (loss): ready

Every obligation and sequence in the baseline's eight steps survives. Step 2 keeps the closed-spec restriction, the test-suite directive as the one admitted act against an open spec, the reconciliation proposal where a delta is open, and the default-branch-SHAs-only rule that the baseline stated as a consequence of the ungated-text reasoning it cut. Step 4 keeps the claim check, the cap, the no-two-deltas-over-one-tranche rule, and the serial-or-cross-project fallback. Step 5 keeps "before any agentic work begins" and both properties of a package — smallest independently executable unit, dependency order. Step 7 keeps all five contents of the doc. Step 8 keeps the one-approval terminator. The handover paragraph keeps the derive-from-the-doc-not-the-spec rule, the acceptance criteria and boundaries the directive must state, the dedicated-session rule for a full spec, and the staleness re-check. Two cut sentences were checked and found covered: "Two deltas editing one document, with the result merged, is refused rather than tooled for" is R0013, cited; and "Acceptance criteria are a separate execution-time input, not part of what a decomposition doc pins" is carried by step 7's closed enumeration of what the doc contains together with the handover paragraph putting acceptance criteria in the directive. The "What this does not decide" section holds two open questions and two restatements of steps 3 and 6, and goes correctly.

## Verdict (residue): ready

Every sentence is an act, an order, or a condition. "The principle" and its bolded thesis, "A proposal derives from whole-spec comprehension, not a fragment", the ungated-text reasoning in step 2, and the four "What this does not decide" items are all gone. The opening two sentences are the document's scope and the doc-carries-no-directives rule, both of which an agent acts on.

## Verdict (keys): ready

`[chief-of-staff]`, unchanged, with `session: [decision]`. Every act in the document — read, decompose, propose, check the claim, flag, write, stop, hand over — is the Chief of Staff's, and no act names another role as its performer. The Test Designer appears in step 2 as the recipient of a directive, not as a party this document directs; process/spec-test-suite.md directs that work and keys the same single role.

## Verdict (loadable): ready

The sweep removed every heading and kept every step, so nothing points at a heading that is gone. The eight steps run in order, the handover paragraph follows them, and the document reads whole. Step 2's baseline pointer to `process/spec-test-suite.md` became "the test-suite directive to a Test Designer"; the sibling document is in the same bundle and its title says the same thing, so the reference still resolves.

## DC-01 — observation
Claim: The two-tranche cap is stated as an obligation in this document and in process/change-flow.md, and no row in the store states it.
Location: process/decomposition.md:22 — "at most two run at once, never two deltas over one tranche"
Evidence: Verified by searching rules/ at the base ref rather than by reading alone. `grep -il 'two tranche\|concurrent' rules/*.md` over all 456 rows returns three files: R0003, "A tranche is one concurrent workstream of build work" — a definition with no cap; R0013, the disjointness rule, which forbids two deltas over one document and says nothing about how many may run; and R0199, an unrelated execution-session stop rule. Reading the store's change-flow and lexicon rows turned up no other candidate. The baseline stated the cap the same way and cited the same two rows on the same claim-check clause, so the sweep neither introduced nor removed the gap — it carried it forward.
Consequence: The cap reads as an obligation and is one in force by practice, but it lives only in prose, in two documents, with no row behind it. Nothing enforces it and nothing surfaces it to a session that loads a bundle without these two documents. It is the kind of obligation the sweep's own instruction says to list as an intake candidate rather than to write a row for.
Fix: Either land a row stating the cap, at which point both documents cite it, or rule that disjointness (R0013) is the real constraint and drop the number from both. No edit to this document is needed until that ruling.
Related: CF-02 in reviews/change-flow-read-20260907T060000Z.md
