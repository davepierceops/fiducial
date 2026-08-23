# Review: LEXICON.md — cycle 14

Verdict: ready-with-findings
Reviewed: LEXICON.md @ df35ea7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ df35ea7, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle; the added question is whether the Claim axes section PR #130 added closes LX-1 without restating a rule Core holds.
Cross-checked: docs/global-context/core.md (Evidence 6; Vocabulary), docs/global-context/decision-layer.md (14), docs/global-context/review-rubric.md (criterion 8), operating-model.md, prose-criteria.md (Claims taxonomy), roles/writer.md, roles/skeptic-risk-agent.md, engagements/critic.md, roles/release-manager-agent.md, skills/conversation-retro.md, context-sets/spec-and-change-discipline.md, engagements/sre/override-log-policy.md — all @ df35ea7; plus docs/cycles/pass1-regate-fix-20260822T230000.md (D6, instructions 19, 20, 22). Bundle membership computed mechanically over every `audience:` value in the 51-file set at df35ea7.
Not inspected: whether the spec-state terms are the right model for concurrency (settled in earlier cycles); the retired-terms tombstones, which were checked for currency against a corpus-wide sweep at df35ea7 and are current — no retired term appears live anywhere in the 51-file set.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/LEXICON-cycle-13.md
Dave should inspect: none.

## LX-2 — non-blocking
Claim: The new Provenance class entry carries Core's obligation clause as well as Core's four class names, which is the restatement criterion 4 forbids.
Location: LEXICON.md:86-88 ("**Provenance class** — where an assertion came from. Four classes, named by Core: *observed*, *inferred*, *told*, *unknown*. Every claim about state, results, verification, or completeness carries one.") against docs/global-context/core.md:22 (Evidence 6: "An assertion about state, results, verification, or completeness is a claim; label it *observed*... State the class; an unlabelled assertion is treated as *unknown*.")
Evidence: Inferred by reading, both texts read whole at df35ea7. The entry's first two sentences are the term definition, which is this file's job and which criterion 4's "a test for a stated rule may name it" logic covers. The third sentence is not a definition; it is Core Evidence 6's obligation, in Core's own enumeration ("state, results, verification, or completeness"), one word shorter. docs/global-context/core.md carries `audience: [all-roles, human]` and this file carries `audience: [all-roles, human]`, so the two are in all fourteen bundles together, always. Criterion 4.
Consequence: Small and slow. One rule, two homes, in every bundle in the corpus — which is the condition criterion 4 exists to prevent, and the mechanism by which criterion 9 drifted from Core Acting 14 once already. The wordings agree today; nothing keeps them agreeing, and this one drops Core's "an unlabelled assertion is treated as *unknown*," so a reader who takes the LEXICON sentence as complete has the obligation without its default.
Fix: Cut the third sentence. "**Provenance class** — where an assertion came from. Four classes, named by Core: *observed*, *inferred*, *told*, *unknown*." is the term; the obligation stays in Core, which is in the same bundle every time.
