# Review: Fiducial self-adoption — read-20261105T184649Z

Verdict: ready
Reviewed: stage/plan.json @ 31ecc88cfed5f12264c10a9694368020a64209bd4f3aa4b921f0f87ba4f37907
Baseline: /Users/dave/code/fiducial @ 9c6fd4e6ba8df62f6b62c601d50910f0bfe0b88f
Reviewer: independent adoption_review agent; Reviewer and Skeptic/Risk passes; solid general-purpose model tier
Date: 2026-11-05
Scope: all 63 inventoried target harness files, both complete staged harness trees, the three planned writes and complete candidate diff; root AGENTS.md, SPEC.md, adopt skill including executable procedure, process/review-artifact.md, process/project-setup.md; relevant approving and adoption decisions DEC-001140, DEC-001530–001660.
Cross-checked: environment.json, protection.json, labels.txt; reviews/pkg-7-close-read-20261105T024910Z.md F4/F5; DEC-001590 and DEC-001650–001660. Identical hook/agent bytes were read once and their other instances checked by hashes; Markdown copies were compared after ownership markers and empty lines; Codex agent instructions were parsed and read.
Not inspected: native fresh-session Claude loading, native hook event delivery, Codex hook trust, production systems, complete rules-store deep read, current remote issue disposition, or untracked retrospective content. No installation, target write, remote mutation, tests of native execution, or release approval was performed.
Findings: none introduced by candidate; preexisting tracked gaps retained below.

## Quality

Verdict (quality): ready

Observed, contract-verified: source HEAD is 0ca563ee53c309840be4ab94dda74f9b075149ba, locally tagged v2026.11.04; target HEAD is the baseline above. Source working tree is clean. Candidate changes only the source-provenance comment on line 2 of AGENTS.md and CLAUDE.md and their two managed-section hashes in .claude/fiducial-ownership.json. All operative prose, agents, skills, hooks, settings and permissions remain unchanged. Recomputing build_plan from the actual target and both stages produced identical writes and zero structural conflicts; all inventory hashes still match. Evidence: candidate.diff and review-evidence.json adjacent to this review artifact.

Observed, contract-verified: inventory contains no nested AGENTS.md, AGENTS.override.md or .codex/config.toml. Existing .claude/settings.local.json contains local permission allowances and sandbox settings; candidate preserves it. Existing extra denies in .claude/settings.json are preserved. The candidate is an overlay of planned writes, not a complete replacement tree.

## Skepticism

Verdict (skepticism): ready

Inferred: classify this exact adoption as routine under the exhaustive consequential-class definition in AGENTS.md: it changes provenance only, with no security, authorization, architecture, integration, fixture, exposure or verification-class movement. This is a classification recommendation, not human approval. The adopt skill still requires an actual human response recorded in approval.json before apply; the request to adopt is not represented here as a new reviewed-plan go.

Observed from DEC-001590 and DEC-001650–001660, unverified at native runtime, release-impact deferred: fresh-session Fiducial loading and harness-driven enforcement remain preexisting gaps. Future path: human opens a fresh target session and supplies /context; independently exercise native hooks and Codex trust. No live-loading or enforcement claim is made by this review. A prior Illuminait loading result does not cross this target boundary.

Observed, contract-verified by code read: existing push-readback reads only tool_input.command and truncates refs/heads/codex/name to name (.codex/hooks/push-readback:77,103; identical Claude script). Existing F4/#415 already records this defect; retain manual remote SHA read-back for any later push. This provenance update neither fixes nor worsens it. Evidence does not establish native hook firing.

## Continuity

Verdict (continuity): ready

Observed, contract-verified: adoption from tagged source matches DEC-001610; preservation and independent contradiction read match DEC-001630; existing ownership and extra denies remain intact. No new target-versus-staged semantic contradiction was found across the inventoried corpus. review.json therefore has an explicitly empty findings array.

Observed, contract-verified by text read: preexisting F5/#416 concerns emitted skills referring to source-only process paths; those paths exist in this self-adopting target. DEC-001650 leaves this non-blocking follow-up in place; the candidate does not change it. Its release impact for this provenance update is not-material, without disposing its portability risk elsewhere.

Assumption: installation will remain confined to this exact hash-bound plan on an idle branch and will receive the skill-required human ruling. The review covers staged content and static compatibility only; it does not approve installation, merging, or release. No unresolved contradiction is silently reconciled by this report.
