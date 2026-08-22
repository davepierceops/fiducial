# Review: engagements/working-with-dave.md — cycle 3

Verdict: changes-required
Reviewed: engagements/working-with-dave.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all eleven criteria of the review rubric @ 8402c23, judged against the current foundation. Confirmation pass within the Pass 1 reconciliation re-gate; the added question is whether the file still holds after the corpus moved.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, docs/global-context/review-rubric.md, engagements/sre/README.md, engagements/sre/implementer.md, engagements/sre/override-log-policy.md, engagements/sre/engagement-change-package.md, engagements/sre/speed-audit.md, policies/document-metadata-policy.md — all @ 8402c23. Bundle membership computed mechanically over every `audience:` value in the corpus at 8402c23.
Not inspected: the infra verification ladder's fitness as engineering judgment (out of this role's remit); whether `bin/bundle --audience` exists or would produce the membership computed here — the bundler is unbuilt, and membership was computed from frontmatter directly.
Findings: 1 — 1 blocking
Prior cycle: reviews/working-with-dave-cycle-2.md (reviewed @ cb3e75a)
Dave should inspect: WD-1. The fix is a one-word frontmatter edit, but which way it goes is a decision about what the Implementer is allowed to touch.

## WD-1 — blocking
Claim: The file's `audience:` omits `implementer`, so the non-negotiable client guardrail does not reach the only engagement role that writes and lands changes.
Location: engagements/working-with-dave.md:4 (`audience: [assistant, cartographer, skeptic, human]`); guardrail at engagements/working-with-dave.md:33-36.
Evidence: Verified by running — bundle membership computed over every in-scope file's `audience:` at 8402c23. The `implementer` bundle resolves to 23 files and does not contain engagements/working-with-dave.md. The `implementer` role was created at 0e07753 (cycle 25); this file was last reviewed at cb3e75a (cycle 7, 2026-08-21), before that role existed. Criterion 1, criterion 11.
Consequence: An Implementer session receives engagements/sre/override-log-policy.md, which states that "Every ceremonial element of this engagement pack — the baseline-gate, the change-package shape, any procedural step — is trivially overridable by Dave," and receives no statement of what is *not* overridable. The one rule in the corpus marked "not negotiable, not overridable" — zero write access to the client's cloud and systems — is absent from the bundle of the role most likely to reach for a write. engagements/sre/implementer.md's "applies are executed by humans or the client's own CI" is a weaker, procedural statement of a different thing and does not carry the prohibition.
Fix: Add `implementer` to this file's `audience:`. Alternatively, if the guardrail is meant to be stated once per bundle rather than inherited, state it in engagements/sre/implementer.md — but not both.
Related: SRE-IMP-1, SRE-OLP-1
