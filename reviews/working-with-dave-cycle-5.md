# Review: engagements/working-with-dave.md — cycle 5

Verdict: ready-with-findings
Reviewed: engagements/working-with-dave.md @ cd7db71
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-23
Scope: engagements/working-with-dave.md, read whole at cd7db71, against all twelve criteria of the review rubric at main HEAD — docs/global-context/review-rubric.md @ 6392736. This artifact reviewed engagements/working-with-dave.md at cd7db71 and no other document.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md and docs/global-context/review-rubric.md, all @ cd7db71, as the standing foundation every file is read against; engagements/sre/README.md and the four engagement roles that load it (assistant, cartographer, critic, implementer); LEXICON.md evidence classes, against which the infra verification ladder is a separate engagement-local ladder; engagements/sre/override-log-policy.md for the logged override the guardrail permits; policies/document-metadata-policy.md `order:` semantics.
Not inspected: `bin/` behaviour beyond running `bin/check-frontmatter --all` and `bin/tests/run` — the audience bundler is unbuilt, so every bundle membership stated here was computed from `audience:` values directly rather than by running it; whether any rule is correct as engineering or product judgment, which this role cedes; docs/history/, docs/batons/, docs/cycles/, reviews/, retros/ and every reference within them; the PRD and TRD instances, which are the Spec Reviewer's gate and do not exist in this repository.
Findings: 1 — 0 blocking, 1 non-blocking
Prior cycle: reviews/working-with-dave-cycle-4.md

## WWD-1 — non-blocking
Claim: This file and roles/writer.md both carry `order: 10` and both land in the `human` bundle, so neither file's position in that bundle is fixed.
Location: engagements/working-with-dave.md:6 (`order: 10`); the collision is with roles/writer.md:6
Evidence: Verified by running. Bundle membership was computed from every `audience:` value across the 51-file in-scope set: engagements/working-with-dave.md carries `audience: [assistant, cartographer, critic, implementer, human]` and roles/writer.md carries `audience: [writer, human]`; `human` is the shared bundle. The `human` bundle's order values are 0, 1, 2, 3, 4, 5, 6, 10, 10, 11 — 10 twice. It is the only collision in any bundle in the set.
Consequence: policies/document-metadata-policy.md states `order:` is "An integer fixing the document's position within a bundle, lower first." Two files at 10 do not fix a position between themselves, so the `human` bundle's assembly order depends on whatever tiebreak the unbuilt bundler happens to apply. The bundler does not exist yet, so nothing is mis-assembled today; the defect is that the frontmatter states a guarantee it does not deliver, and the tiebreak will be chosen by implementation accident rather than by decision.
Fix: Give one of the two a distinct value — prose-criteria.md already occupies 11, so renumbering roles/writer.md and prose-criteria.md to 11 and 12, or moving this file to 9, both resolve it.
Related: WR-1
