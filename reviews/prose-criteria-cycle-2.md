# Review: prose-criteria.md — cycle 2

Verdict: ready-with-findings
Reviewed: prose-criteria.md @ df35ea7
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ df35ea7, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle; the added question is whether decision D6 — the ladder stays, as a claim-strength axis, with `inferred` renamed `grounded` — closed PC-1 through PC-5.
Cross-checked: docs/global-context/core.md (Standing 2; Evidence 5-7), docs/global-context/decision-layer.md, LEXICON.md (Claim axes), operating-model.md, docs/global-context/review-rubric.md, roles/writer.md, roles/context-quality-reviewer.md, policies/document-metadata-policy.md — all @ df35ea7; plus docs/cycles/pass1-regate-fix-20260822T230000.md (D6, instructions 5, 19) and a corpus-wide sweep for `inferred` over the 51-file set, which returns it only as Core's provenance class and LEXICON's naming of it. Bundle membership computed mechanically over every `audience:` value in that set.
Not inspected: whether the criteria produce good prose — that is Dave's voice and Dave's call, and this role does not judge it; whether `davepierceops/fiducial` is the right public repository to cite; the archived writing pipeline under docs/history/.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/prose-criteria-cycle-1.md
Dave should inspect: none.

## PC-3 — non-blocking (still open from cycle 1, narrowed)
Claim: The file still states no session kind, and the conditional under which cycle 1 would have closed the finding — that this file say it is read by the Writer role as defined in roles/writer.md — was not met.
Location: prose-criteria.md:10-15 (Scope, where the session-kind declaration would sit) and :1-6 (frontmatter, now carrying `order: 11`)
Evidence: Verified by running. `git diff 8cdc0b9 287fa78 -- prose-criteria.md` adds `order: 11` and rewrites seven passages; it adds no session-kind statement and no sentence naming the Writer. roles/writer.md:10 now reads "The Writer runs as a decision session" and :12 reads "Governed by the Public Prose Criteria in this bundle; read them on every invocation" — so the link between the two files is stated in one direction only. Cycle 1's fix said "Resolve with WR-3; one declaration in roles/writer.md covers both **if this file states that it is read by the Writer role as defined there**." WR-3 landed; the conditional did not. The corpus convention holds elsewhere: docs/global-context/core.md:9 names "every agent session," operating-model.md:9 names both kinds, and every one of the ten `roles/` documents declares one. Criterion 7.
Consequence: Materially reduced. The question cycle 1 asked — whether docs/global-context/decision-layer.md reaches a Writer session — is now answered, by roles/writer.md, and the `writer` bundle carries both files with `order: 10` before `order: 11`, so a reader meets the declaration first. What remains is that this file read on its own states no session kind, and criterion 7 is a property of the file, not of the pair. The practical exposure is a session given the criteria without the role document, which the `order:` fix makes unlikely but does not prevent.
Fix: One clause in Scope: "Read by the Writer, which runs as a decision session." That satisfies criterion 7 here without a second declaration of the session kind, since it cites the role rather than restating the rule.
Related: WR-3
