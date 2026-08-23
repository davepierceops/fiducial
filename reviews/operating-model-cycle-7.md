# Review: operating-model.md — cycle 7

Verdict: ready-with-findings
Reviewed: operating-model.md @ edd8015
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ edd8015, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle 2; the added question is whether instruction 1 of the part-3 directive closed OM-1 and whether its sweep for other clauses extending the Spec Reviewer to non-spec documents was complete.
Cross-checked: docs/global-context/core.md (Acting 13), docs/global-context/decision-layer.md, LEXICON.md, docs/global-context/review-rubric.md, roles/spec-reviewer-agent.md, roles/context-quality-reviewer.md, skills/spec-review-cycle.md, policies/document-metadata-policy.md, policies/commit-and-change-control-policy.md, context-sets/spec-and-change-discipline.md — all @ edd8015; plus `git diff f46264b 219b0e7 -- operating-model.md`, docs/cycles/pass1-regate-fix-3-20260823T004500.md (D9, instruction 1), and reviews/operating-model-cycle-6.md. A corpus-wide grep for "Context Quality Reviewer" and for "Spec Reviewer" over the 51-file set was run at edd8015.
Not inspected: whether the change flow's nine stages are the right nine, or whether the two-tier release gate is the right shape — settled in earlier cycles and not re-opened here; whether the working thesis is true as a matter of engineering judgment; the PRD and TRD instances the change flow presupposes, which do not exist in this repository.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/operating-model-cycle-6.md
Dave should inspect: none. OM-2 is the tail of OM-1 and takes three words.

## OM-2 — non-blocking
Claim: Step 1's sentence now assigns methodology and governed context documents to the Context Quality Reviewer, and the role attribution closing the same line still names only the Spec Reviewer.
Location: operating-model.md:126 ("1. **Specs agreed** — PRD/TRD written, reviewed by the Spec Reviewer Agent (hard gate), and agreed by Dave. Methodology and other governed context documents are gated by the Context Quality Reviewer. *(PM/EM/Owner + Architect + Spec Reviewer)*")
Evidence: Verified by running. `git diff f46264b 219b0e7 -- operating-model.md` replaces "The same gate covers any canonical document, methodology documents included." with the Context Quality Reviewer sentence, and changes :103 from "the Spec Reviewer that gates it" to "the reviewer that gates it"; it does not touch the parenthetical. A corpus-wide grep for "methodology documents included" over the 51-file set returns nothing, so OM-1 itself is closed and instruction 1's sweep found the one other clause there was. What remains is inside the line the fix edited: the italic role list is the file's own convention for naming who acts at a stage — every one of the nine stages carries one — and stage 1 now has two gates and one named reviewer. operating-model.md carries `audience: [all-roles, human]` and is in all fourteen bundles; roles/context-quality-reviewer.md is in two. Criterion 11 (the boundary is stated in the prose and unstated in the attribution a reader consults for it) and Core Acting 13, "A changed fact changes everywhere it appears — in this document and in every other."
Consequence: Small, and confined to one line. A reader who takes the role list as the stage's roster — which is what it is for, and which is how the other eight stages read — gets "Spec Reviewer" for a methodology document and has to override it from the sentence above. The concrete exposure is a Chief of Staff session composing a cycle directive from the change flow: the sentence routes correctly, the roster does not, and nothing marks which of the two is the summary.
Fix: Add the role to the list: *(PM/EM/Owner + Architect + Spec Reviewer + Context Quality Reviewer)*.
Related: OM-1
