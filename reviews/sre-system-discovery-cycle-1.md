# Review: engagements/sre/system-discovery.md — cycle 1

Verdict: changes-required
Reviewed: engagements/sre/system-discovery.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 43 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. First-cycle review — produced by directive at 0e07753 (cycle 25), never rubric-reviewed. One of the seven-file `engagements/sre/` set.
Cross-checked: docs/global-context/core.md (Vocabulary — decision session, execution session; Evidence 6), docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/cartographer.md, engagements/working-with-dave.md, and the other six files of the `engagements/sre/` set — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: whether the five-step procedure is the right procedure for mapping a client pipeline; the "Terraform or equivalent" retention, recorded in the baton as deliberate.
Findings: 2 — 2 blocking
Prior cycle: none
Dave should inspect: SRE-SD-1 — the baton records that a session-kind conflict in this pack was already resolved by fiat once; this is a second one, and it is a direct contradiction rather than an ambiguity.

## SRE-SD-1 — blocking
Claim: This file and engagements/cartographer.md state incompatible session kinds for the same work.
Location: engagements/sre/system-discovery.md:9-12 ("This skill runs in an execution session. ... Executed by the Cartographer.") against engagements/cartographer.md:9 ("The Cartographer runs as a decision session.")
Evidence: Verified by running — both files are in the `cartographer` bundle (24 files, computed over `audience:` at 8402c23), so one session holds both statements. docs/global-context/core.md:41-43 defines the two kinds as mutually exclusive roles in the flow and states that a decision session "does not carry out the changes a directive specifies; that work happens in an execution session." engagements/cartographer.md further describes work that is decision-session-shaped throughout — "Dave asks; you dig; you answer," "hand that to Dave — he decides." Criterion 7.
Consequence: Criterion 7 requires the file to be for decision sessions, execution sessions, or both, and to say nothing only the other kind needs. Here two files in one bundle answer differently for the same role doing the same procedure, and the reader cannot resolve it: the Cartographer is either receiving the decision layer or it is not, and steps 3 and 5 ("The unknowns become the question list for Dave," "Render the map") are decision-session acts while the header says execution.
Fix: Pick one. If the Cartographer is a decision session, this file says so and step 1's reading work is decision-session reading. If the procedure genuinely runs in an execution session, say that it is executed *for* the Cartographer by an execution session and that the Cartographer is the decision session that triages the result.

## SRE-SD-2 — blocking
Claim: The file is the sole definition of two terms the pack uses corpus-wide, and its `audience:` withholds it from two of the four bundles that use them.
Location: engagements/sre/system-discovery.md:4 (`audience: [cartographer, assistant, human]`); definitions at :34-40 (Output — the System Map and "the engagement working area — a client-hosted repository designated at kickoff")
Evidence: Verified by running — "System Map" appears in engagements/sre/README.md:24, implementer.md:29-31, engagement-change-package.md:30-31, speed-audit.md:34; "engagement working area" appears in engagements/assistant.md:16, override-log-policy.md:22, baseline-measurement.md:24. Neither term is in LEXICON. This file is absent from the `skeptic` (23 files) and `implementer` (23 files) bundles. Criterion 1, criterion 10.
Consequence: An Implementer session must escalate on contradiction with the System Map and must state where the change package's evidence lives, holding no definition of either. A Skeptic session reviews a change package that cites the map correction, holding no definition of the map.
Fix: Add `skeptic` and `implementer` to this file's `audience:`, or lift the two definitions into engagements/sre/README.md, which every engagement bundle receives. Do not do both.
Related: SRE-IMP-2, SRE-ECP-2
