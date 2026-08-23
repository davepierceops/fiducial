# Review: roles/writer.md — cycle 2

Verdict: ready-with-findings
Reviewed: roles/writer.md @ df35ea7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ df35ea7, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle; the added question is whether the rewritten closing instruction resolves WR-2 without pointing the Writer at a pass that no longer exists in the form offered.
Cross-checked: docs/global-context/core.md (Standing 2, 4), docs/global-context/decision-layer.md, LEXICON.md (Claim axes), operating-model.md, prose-criteria.md, roles/context-quality-reviewer.md (Scope), roles/skeptic-risk-agent.md, engagements/critic.md, docs/global-context/review-rubric.md — all @ df35ea7; plus docs/cycles/pass1-regate-fix-20260822T230000.md (D2, D5, instructions 5, 18). Bundle membership computed mechanically over every `audience:` value in the 51-file set at df35ea7.
Not inspected: whether the four operating rules are the right rules for drafting in Dave's voice — that is Dave's voice and Dave's call; the retirement of the writing pipeline, which is cycle 26's decision.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/writer-cycle-1.md
Dave should inspect: WR-5 — whether a Context Quality Reviewer pass over public prose is a thing that exists is a scope decision, and the two documents now answer it differently.

## WR-5 — non-blocking
Claim: The closing instruction offers a Context Quality Reviewer pass over a piece of public prose, and the Context Quality Reviewer's Scope rule — rewritten in the same pull request — excludes it.
Location: roles/writer.md:17 ("state that a Critic read (advisory, reads the piece against the Public Prose Criteria) and a Context Quality Reviewer pass (checks it as LLM context, if it will be bundled) are available") against roles/context-quality-reviewer.md:14-17 ("Every governed non-code file: the frontmatter in-scope set plus `docs/global-context/*.md`, `engagements/**/*.md`, `prose-criteria.md`; excluding history, batons, cycles, reviews, retros, trackers, the decision log, and vendor-tooling files.")
Evidence: Verified by running. Both sentences were written by PR #130 — instruction 18 for this line, instruction 9 for the Scope rule. The Scope rule is an enumeration of repository locations; a piece of public prose is in none of them. This file states why at :16: "The published text lives in Dave's own document, owned by Dave. The repository never holds prose." So the object of the offered pass is by construction outside the reviewable set. The old Scope statement, which the same PR replaced, was a list of document *classes* ending "and the writing documents," which did reach it. Criterion 11 — a boundary two documents answer differently, delivered as an instruction. The `writer` bundle is 19 files and contains neither roles/context-quality-reviewer.md nor engagements/critic.md, so the Writer cannot check either claim against its source.
Consequence: The last thing a Writer session does is offer Dave two passes. One of them is offered on terms its own role document does not license, and the hedge "if it will be bundled" does not rescue it — a piece that will be bundled is still not in the frontmatter in-scope set, `docs/global-context/`, `engagements/`, or `prose-criteria.md`. Dave is offered a review no role is scoped to run.
Fix: Either widen the Scope rule to name public prose that will be bundled, or narrow the offer here to the Critic read and drop the Context Quality Reviewer clause. The Critic half is correct as written — engagements/critic.md is advisory and the Public Prose Criteria are in this bundle.
Related: CQR-3
