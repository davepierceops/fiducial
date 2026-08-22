# Cycle 25 Directive — fiducial — engagements/comfy archive-and-generalize

Date: 2026-08-22
Route: fresh
Model: frontier
Reviewed state: davepierceops/fiducial main @ 83fcfc4
Baton: docs/batons/baton-20260823T003000.md

## Intent

Retire engagements/comfy/ as a governed location. Preserve the twelve originals as history. Produce a generalized engagement pack at engagements/sre/ from the seven files that state something no existing governed file states, conformed to docs/global-context/review-rubric.md (all eleven criteria).

## Instructions

1. Archive. `git mv engagements/comfy docs/history/engagements/comfy`. Do not edit any archived file; frontmatter, paths, and retired vocabulary stay as they are — the archive is a record.

2. Create engagements/sre/ containing exactly seven files, each derived from the archived original named:

   | New file | Derived from |
   |---|---|
   | README.md | engagements/comfy/README.md |
   | override-log-policy.md | engagements/comfy/policies/override-log-policy.md |
   | implementer.md | engagements/comfy/roles/implementer.md |
   | baseline-measurement.md | engagements/comfy/skills/baseline-measurement.md |
   | engagement-change-package.md | engagements/comfy/skills/engagement-change-package.md |
   | speed-audit.md | engagements/comfy/skills/speed-audit.md |
   | system-discovery.md | engagements/comfy/skills/system-discovery.md |

   Flat directory; no policies/, roles/, skills/ subdirectories.

3. Do not create generalized copies of engagements/comfy/roles/cartographer.md, roles/skeptic-engagement.md, roles/chief-of-staff-engagement.md, policies/client-credentials-policy.md, or override-log.md. Their successors are engagements/cartographer.md, engagements/skeptic.md, engagements/assistant.md, and engagements/working-with-dave.md respectively; override-log.md is engagement data.

4. Every new file carries frontmatter `status: draft`, `last-reviewed: null`, and `audience:` drawn only from: assistant, cartographer, skeptic, implementer, human. Map the originals' slugs: chief-of-staff-engagement → assistant; skeptic-engagement → skeptic; drop `client`; drop `all-roles`. Where the original said `all-roles`, list the engagement slugs explicitly.

5. Conform each new file to the rubric:
   - Remove every client-specific reference: the name Comfy, "Comfy-hosted", the specific engagement goal. "Terraform or equivalent", p50/p95, pipeline stages, and infrastructure vocabulary are engagement-shape, not client-shape; keep them.
   - Remove every path-shaped reference to another file (criterion 3). Where the referenced file's content is needed, state it; where the reference was to a role or skill by name, name the role or skill in prose.
   - Remove rules Core, the Decision Layer, or an existing engagements/*.md file already states (criterion 4): the secrets rule, zero-write-access guardrail, plan/apply/serving/delta verification ladder, provenance tags, "could not determine beats a guess", escalation-terminates-at-Dave, read-only-no-interviews. In implementer.md the "Evidence classes for infrastructure work" section is removed entirely; working-with-dave.md states the ladder.
   - Cut rationale and trailing justification (criterion 6). Keep the stated rule.
   - State session kind in the first line of the body (criterion 7): README and override-log-policy govern both kinds; implementer runs as an execution session; the four skills run in a decision session except baseline-measurement step 6 and system-discovery, which run in execution sessions — state per file as the content requires.
   - Replace retired vocabulary: "dispatch" → "hand to"; "Skeptic dispatch" → "Skeptic routing"; no "track", "sync block", "prompt".
   - Override-log-policy: the log's location becomes "the engagement working area" (no fixed path); the Skeptic verdict is input to Dave, not a gate, so the overridable set is the baseline-gate, the change-package shape, and any procedural step.
   - engagement-change-package.md item 6: "Skeptic verdict, where one was requested" — the generalized Skeptic is summoned, not standing.
   - README: rewrite the "What an engagement inverts" and "Key principles" sections for the generic case; drop "The crew" (the four files name themselves) and "Metadata convention" (Pass 2 handles scope). Audience: the four slugs plus human.

6. Do not edit any file outside engagements/sre/ and the git mv in instruction 1. If a consistency fix appears required elsewhere, stop and report it; do not make it.

7. Run `bin/check-frontmatter --all` and capture output to docs/cycles/comfy-archive-and-generalize-20260822T195900-check.txt; commit it. A failure inside docs/history/ is expected and is not a stop condition; a failure inside engagements/sre/ is.

## Stop conditions

- Working tree at start is not at 83fcfc4 or a descendant with no intervening edits under engagements/.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- An instruction cannot be carried out as written.

## Report

Triageable by the next decision session: directive path and SHA first; then per new file, one line naming what was removed under criteria 3, 4, and 6; then every judgment made that the directive did not dictate, one line each; then the PR URL.
