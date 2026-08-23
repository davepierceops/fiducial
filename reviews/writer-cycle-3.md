# Review: roles/writer.md — cycle 3

Verdict: ready-with-findings
Reviewed: roles/writer.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: roles/writer.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed roles/writer.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; prose-criteria.md, the criteria this role reads on every invocation; engagements/critic.md for the advisory read offered at completion; docs/global-context/decision-layer.md, the layer this decision-session role runs under; policies/document-metadata-policy.md `order:` semantics.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/writer-cycle-2.md

## WR-1 — non-blocking
Claim: This file and engagements/working-with-dave.md both carry `order: 10` and both land in the `human` bundle, so neither file's position in that bundle is fixed.
Location: roles/writer.md:6 (`order: 10`); the collision is with engagements/working-with-dave.md:6
Evidence: Verified by running. Bundle membership was computed from every `audience:` value across the 51-file in-scope set: roles/writer.md carries `audience: [writer, human]` and engagements/working-with-dave.md carries `audience: [assistant, cartographer, critic, implementer, human]`; `human` is the shared bundle, whose order values are 0, 1, 2, 3, 4, 5, 6, 10, 10, 11. It is the only order collision in any bundle in the set.
Consequence: policies/document-metadata-policy.md states `order:` is "An integer fixing the document's position within a bundle, lower first." Two files at 10 fix nothing between themselves. In the `human` bundle this file is also meant to precede prose-criteria.md at 11, and that relation survives; what does not survive is any stated relation to engagements/working-with-dave.md, leaving it to the unbuilt bundler's tiebreak.
Fix: Give one of the two a distinct value — moving engagements/working-with-dave.md to 9, or this file and prose-criteria.md to 11 and 12, both resolve it.
Related: WWD-1
