# Review: engagements/critic.md — cycle 2

Verdict: ready-with-findings
Reviewed: engagements/critic.md @ edd8015
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: the whole file, all eleven criteria of the review rubric @ edd8015, judged against the current foundation. Confirmation pass within the Pass 1 re-gate confirmation cycle 2; the added question is whether instruction 8 closed CR-1 and DR-23 under D12 — the no-release-gate rule lives once, in engagements/sre/README.md, and this file cites it by title.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, skills/review-artifact.md, roles/skeptic-risk-agent.md, engagements/sre/README.md, engagements/sre/engagement-change-package.md, engagements/sre/speed-audit.md, engagements/sre/implementer.md, engagements/assistant.md, engagements/working-with-dave.md — all @ edd8015; plus docs/cycles/pass1-regate-fix-3-20260823T004500.md (D12, instruction 8), reviews/critic-cycle-1.md, and a corpus-wide grep for "no release gate" and "Release is the client" over the 51-file set at edd8015. Bundle membership computed mechanically over every `audience:` value in that set.
Not inspected: whether the infra false-confidence checklist is the right list as a matter of engineering judgment; whether Critic is the right name — D2 settled it.
Findings: 1 — 1 non-blocking
Prior cycle: reviews/critic-cycle-1.md
Dave should inspect: none.

## CR-2 — non-blocking
Claim: The citation D12 called for names the cited document by filename rather than by title, and the document it points at is titled "Engagement Pack".
Location: engagements/critic.md:12 ("An engagement has no release gate, per the engagement README.")
Evidence: Verified by running. A corpus-wide grep over the 51-file set at edd8015 returns "An engagement has no release gate" in two files and the full rule — "Release is the client's concern, not this role's; do not inquire into or reason about the client's release timing" — in one, engagements/sre/README.md:39-40, so DR-23's duplication is genuinely gone and CR-1 is closed. The target's own first heading is `# Engagement Pack` (engagements/sre/README.md:7); nothing in it calls itself "the engagement README". docs/cycles/pass1-regate-fix-3-20260823T004500.md D12 says the rule "lives once, in engagements/sre/README.md; engagements/critic.md cites it by title," and instruction 8 dictated the replacement wording verbatim, so this is the cost of the dictated fix rather than a departure from it. Bundle membership computed over `audience:` at edd8015: this file carries `audience: [critic, human]`, engagements/sre/README.md carries `audience: [assistant, cartographer, critic, implementer, human]`, and the `critic` bundle resolves to 24 files containing both — so the reference resolves, and this is a naming defect, not a delivery one. Criterion 3 ("A path-shaped reference is a defect") applied as cycle 2's sweep (e) applied it to un-backticked file-shaped references, and criterion 1.
Consequence: Small. A Critic session reading its own role document is told the rule lives in "the engagement README" and finds, in the same bundle, a document headed "Engagement Pack" — the right file under a name it does not use. The cost is that the corpus now identifies one document two ways, and criterion 3's whole point is that a bundle reader has titles and not paths; "README" is a filename.
Fix: Cite the title: "An engagement has no release gate, per the Engagement Pack." The rest of the line — "Your verdict is input to Dave's decision, not a gate on anything" — is this file's own and stays.
Related: CR-1
