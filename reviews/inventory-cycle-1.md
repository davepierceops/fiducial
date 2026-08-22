# Review: docs/global-context/inventory.md — cycle 1

Verdict: changes-required
Reviewed: docs/global-context/inventory.md @ 8402c23
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-22
Scope: the whole file, all 191 lines, all eleven criteria of the review rubric @ 8402c23, criterion 10 answered first. Surfaced by the reconciliation re-gate's scope enumeration as a governed file with no review artifact at any cycle; it is not one of the nine first-cycle files the directive names. Counts were taken mechanically over the file at 8402c23.
Cross-checked: docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md, docs/global-context/review-rubric.md, roles/chief-of-staff.md, policies/document-metadata-policy.md — all @ 8402c23; plus the existence of every path the file cites, checked against the tree at 8402c23.
Not inspected: whether the 2026-08-20 triage dispositions recorded here were correctly taken — this review does not re-open Dave's calls; whether `davepierceops/ai` @ aff41f4 or `davepierceops/writing` @ 15d3d71 still resolve, neither being reachable from this repository.
Findings: 4 — 2 blocking, 2 non-blocking
Prior cycle: none
Dave should inspect: INV-1. The disposition — keep in a bundle, move out of `docs/global-context/`, or retire to `docs/history/` — is a call, not a wording fix, and it decides whether the other three findings need fixing at all.

## INV-1 — blocking
Claim: The file declares itself not a governed document, and is nonetheless delivered as standing context to the Chief of Staff.
Location: docs/global-context/inventory.md:4 (`audience: [chief-of-staff, human]`) and :9 ("Triage artifact, not a governed document.")
Evidence: Verified by running — the `chief-of-staff` bundle resolves to 31 files at 8402c23 and contains docs/global-context/inventory.md, because `audience:` is the selector and this file names the bundle. Criterion 10, criterion 2.
Consequence: 191 lines of superseded triage — including rows whose disposition was "discard," decisions later reversed in the same file, and follow-up lists addressed to a repository that no longer exists under that name — arrive as governing context in every Chief of Staff session. Criterion 10 asks whether the file "contributes something no other file in that bundle states"; what it contributes is provenance for rules the bundle already states in their agreed form, plus a large volume of text that contradicts them.
Fix: Decide the disposition. If it is history, `git mv` it to `docs/history/` and the remaining findings are moot. If it is a live triage register, remove `chief-of-staff` from `audience:` so it stops entering bundles, and fix INV-2 through INV-4.

## INV-2 — blocking
Claim: The file is built out of path-shaped references, and 34 distinct cited paths do not exist at 8402c23.
Location: throughout; the Sources block at :11-13 and the Follow-ups sections at :169-181 are the densest.
Evidence: Verified by running — a mechanical sweep of backticked path-shaped tokens over the corpus at 8402c23 resolved each against the tree. Dead targets cited by this file include `context-sets/base.md`, `collab-workflow.md`, `command-blocks.md` (bare), `directive-dispatch.md`, `machinery-criteria.md`, `spec-and-change-discipline.md` (bare), `working-with-dave.md` (bare), `writing/roles/editor.md`, `writing/roles/reviewer.md`, `writing/roles/skeptic.md`, `writing/roles/section-writer.md`, `writing/section-writer.md`, `writing/machinery-criteria.md`, `writing/prose-criteria.md`, `bin/bundle --audience`, `bin/session-tar`, `davepierceops/ai`, `davepierceops/writing`, `writing-20260820-161541.tar.gz`. This file is the source of the large majority of dead path references in the whole corpus. Criterion 3, criterion 1.
Consequence: Every row is sourced by a path, and for a reader inside a bundle the paths are unopenable in principle and, for these 34, unresolvable in fact. The file's evidentiary value — "here is where this rule came from" — is the part that has decayed.
Fix: If the file stays live, cite by SHA-pinned historical path and say so, or drop the source column. Do not repair the paths in place; they refer to two repositories that were merged away.

## INV-3 — non-blocking
Claim: The file carries retired vocabulary and vendor model names as live text.
Location: :70 ("## D. Blocks and dispatch"), :78 (D5 Sync block), :82 (D9), :86 (D13 "Opus / Sonnet / Haiku"), :101-102 ("retired Track B text"), :187 ("Track A/B is retired").
Evidence: Verified by running — a corpus-wide sweep for the terms LEXICON retires (`dispatch`, `sync block`, `track`, `prompt`) and for vendor and model names outside `vendors/` returned this file as the only in-scope location for `dispatch` other than LEXICON's own tombstone, and the only in-scope location for `Opus`, `Sonnet`, or `Haiku` anywhere. Criterion 8.
Consequence: The rubric's criterion 8 says model selection speaks in tiers and "Track does not appear." The row that records the decision to speak in tiers is itself written in model names, and the file is in a live bundle, so the retired vocabulary is delivered alongside the retirement.
Fix: Covered by INV-1's disposition. A historical artifact is permitted to contain the vocabulary it retired; a bundled one is not.

## INV-4 — non-blocking
Claim: The file is a record of decisions, not instructions to an agent, and several sections address the author rather than the reader.
Location: :161-166 ("Parked — resolved 2026-08-20"), :169-181 ("Follow-ups in ..."), :183-191 ("Observations for Dave (not rows)").
Evidence: Inferred by reading. Criterion 5 ("Agent instruction, not authoring principle") and criterion 6 ("Instructions, not rationale"). No sentence in these sections is an instruction to the agent reading the bundle; the Observations section is explicitly addressed to Dave and asks him questions.
Consequence: An agent given this file inside a bundle has no action available from two-thirds of it, and the material that does read as a rule is superseded by the agreed documents in the same bundle.
Fix: Covered by INV-1's disposition.
