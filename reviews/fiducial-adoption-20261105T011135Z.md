# Fiducial adoption

Evidence class: contract-verified. Claude Code /context and Codex hook trust: not live-verified by this procedure.

Changed paths:

- `.agents/skills/adopt/SKILL.md`
- `.agents/skills/build/SKILL.md`
- `.agents/skills/change-flow/SKILL.md`
- `.agents/skills/decision-log/SKILL.md`
- `.agents/skills/gate/SKILL.md`
- `.agents/skills/intake/SKILL.md`
- `.agents/skills/outline/SKILL.md`
- `.agents/skills/project-status/SKILL.md`
- `.agents/skills/release/SKILL.md`
- `.agents/skills/retro/SKILL.md`
- `.agents/skills/review-artifact/SKILL.md`
- `.agents/skills/spec-template/SKILL.md`
- `.agents/skills/voice/SKILL.md`
- `.claude/agents/architect-agent.md`
- `.claude/agents/coder-agent.md`
- `.claude/agents/context-quality-reviewer.md`
- `.claude/agents/release-manager-agent.md`
- `.claude/agents/reviewer-agent.md`
- `.claude/agents/skeptic-risk-agent.md`
- `.claude/agents/spec-reviewer-agent.md`
- `.claude/agents/test-designer-agent.md`
- `.claude/fiducial-ownership.json`
- `.claude/hooks/_hooklib.py`
- `.claude/hooks/decision-log-append-only`
- `.claude/hooks/intake-branch-guard`
- `.claude/hooks/lane-guard`
- `.claude/hooks/push-readback`
- `.claude/hooks/review-artifact-immutable`
- `.claude/hooks/store-lint`
- `.claude/settings.json`
- `.claude/skills/adopt/SKILL.md`
- `.claude/skills/build/SKILL.md`
- `.claude/skills/change-flow/SKILL.md`
- `.claude/skills/decision-log/SKILL.md`
- `.claude/skills/gate/SKILL.md`
- `.claude/skills/intake/SKILL.md`
- `.claude/skills/outline/SKILL.md`
- `.claude/skills/project-status/SKILL.md`
- `.claude/skills/release/SKILL.md`
- `.claude/skills/retro/SKILL.md`
- `.claude/skills/review-artifact/SKILL.md`
- `.claude/skills/spec-template/SKILL.md`
- `.claude/skills/voice/SKILL.md`
- `.codex/agents/architect-agent.toml`
- `.codex/agents/coder-agent.toml`
- `.codex/agents/context-quality-reviewer.toml`
- `.codex/agents/release-manager-agent.toml`
- `.codex/agents/reviewer-agent.toml`
- `.codex/agents/skeptic-risk-agent.toml`
- `.codex/agents/spec-reviewer-agent.toml`
- `.codex/agents/test-designer-agent.toml`
- `.codex/hooks.json`
- `.codex/hooks/_hooklib.py`
- `.codex/hooks/codex-hook`
- `.codex/hooks/decision-log-append-only`
- `.codex/hooks/intake-branch-guard`
- `.codex/hooks/lane-guard`
- `.codex/hooks/push-readback`
- `.codex/hooks/review-artifact-immutable`
- `.codex/hooks/store-lint`
- `AGENTS.md`
- `CLAUDE.md`

## Inventory

```json
{
  "AGENTS.md": {
    "mode": 420,
    "sha256": "979c7b41aae3547993299bfbc4f561a330661265b1ee3262a3fa5cdd507ce274"
  },
  "CLAUDE.md": {
    "mode": 420,
    "sha256": "979c7b41aae3547993299bfbc4f561a330661265b1ee3262a3fa5cdd507ce274"
  }
}
```

## Independent contradiction read

```json
{
  "plan_sha256": "8ac08d165cc00b489eea9d1c6a22e743b6a0962a796af7d8493e07edb449f2ab",
  "reviewer": "independent adopter contradiction reader (adoption_contradictions), diff-only follow-up; no human approval",
  "findings": [
    {
      "id": "C1",
      "file": "CLAUDE.md",
      "line": 3,
      "staged_file": "candidate/CLAUDE.md",
      "staged_line": 3,
      "claim": "Proposed resolution: exact replacement of both old root loaders resolves collision; human ruling and matching whole-entry DEC-000280 supersession still required. Retain .09.29 archival; only .09.17 removal authorized."
    },
    {
      "id": "C2",
      "file": "roles/fiducial-bundle-core.md",
      "line": 63,
      "staged_file": "candidate/CLAUDE.md",
      "staged_line": 3,
      "claim": "Proposed preservation: explicitly invoked experimental evaluation roles/core contracts remain unchanged and unmigrated; preserve roles/** byte-for-byte; human ruling required."
    },
    {
      "id": "C3",
      "file": "decisions/log.md",
      "line": 111,
      "staged_file": "claude-code/.claude/skills/retro/SKILL.md",
      "staged_line": 69,
      "claim": "Proposed preservation: DEC-000220 human untracked-retro timing and non-stop condition remain; new procedure lands only its own requested output; human ruling required."
    },
    {
      "id": "C4",
      "file": "decisions/log.md",
      "line": 20,
      "staged_file": "claude-code/.claude/skills/build/SKILL.md",
      "staged_line": 13,
      "claim": "Proposed preservation: DEC-000040 consulting scope remains; SPEC/build applies when software is built; DEC-000030 fallback retained; human ruling required."
    }
  ]
}

```

## Human rulings

```json
{
  "gate": "https://github.com/davepierceops/illuminait/issues/25",
  "go": true,
  "human": "Dave Pierce",
  "plan_sha256": "8ac08d165cc00b489eea9d1c6a22e743b6a0962a796af7d8493e07edb449f2ab",
  "review_sha256": "8fbce9f599b74a21ccd1e7e36aba3d69f04e9bb89402cb16660aa542aeb4f6d5",
  "rulings": {
    "C1": "Approved: replace the two legacy root loaders with the reviewed scoped preamble and managed emitted context; supersede DEC-000280 preserving attribution and project clauses.",
    "C2": "Approved: preserve explicitly invoked experimental evaluation roles, their core contract and task-specific decisions; roles/** unchanged.",
    "C3": "Approved: preserve DEC-000220; existing human-authored untracked retros remain at Dave’s chosen commit timing; new retro skill lands only its own requested output.",
    "C4": "Approved: preserve consulting/evaluation scope; SPEC.md/build applies when software is built. Retain DEC-000030 and the v2026.09.29 archive; remove only v2026.09.17."
  }
}
```

## Exact legacy edits

```json
[
  {
    "after": "# Agent instructions\n\nStanding fiducial context is the managed section below and the matching harness agents, skills and hooks in this repository. Project-specific decisions in decisions/log.md and explicitly invoked roles/cartographer.md and roles/synthesist.md remain in force. .fiducial/v2026.09.29/ is historical reference, not a standing loader. Project Status uses the project-status skill in the active harness.\n",
    "before": "# Agent instructions\n\nBefore doing anything else, read whole the fiducial bundle for your role from `.fiducial/v2026.09.29/` — `fiducial-bundle-<role>.md`; the role is named by the directive or by the person directing you. The bundle is the complete standing instruction set for this repository; nothing here restates it.\n\nPinned bundle release: fiducial v2026.09.29 (https://github.com/davepierceops/fiducial/releases/tag/v2026.09.29). Adopting a newer release is a deliberate change recorded in `decisions/log.md`.\n\nProject Status skill: `.fiducial/v2026.09.29/skills/project-status/SKILL.md`.\n",
    "path": "CLAUDE.md"
  },
  {
    "after": "# Agent instructions\n\nStanding fiducial context is the managed section below and the matching harness agents, skills and hooks in this repository. Project-specific decisions in decisions/log.md and explicitly invoked roles/cartographer.md and roles/synthesist.md remain in force. .fiducial/v2026.09.29/ is historical reference, not a standing loader. Project Status uses the project-status skill in the active harness.\n",
    "before": "# Agent instructions\n\nBefore doing anything else, read whole the fiducial bundle for your role from `.fiducial/v2026.09.29/` — `fiducial-bundle-<role>.md`; the role is named by the directive or by the person directing you. The bundle is the complete standing instruction set for this repository; nothing here restates it.\n\nPinned bundle release: fiducial v2026.09.29 (https://github.com/davepierceops/fiducial/releases/tag/v2026.09.29). Adopting a newer release is a deliberate change recorded in `decisions/log.md`.\n\nProject Status skill: `.fiducial/v2026.09.29/skills/project-status/SKILL.md`.\n",
    "path": "AGENTS.md"
  }
]
```

## Execution evidence and boundary

Observed: source `bb2ebcb4ea140deb40d7148d7dbffcae56806fe2`, target base `9220705453ecc042eedef5dc0ac0da99a78f62c9`; source committed and clean when staged. Both emitters ran locally on macOS using Python and Git. Network access required the authenticated local GitHub CLI outside the sandbox; the connector lacked Illuminait access. No credentials were read or recorded.

Observed: Dave approved C1–C4 and publication after confirming this is Fiducial package 5's first real adopter run. Gate: https://github.com/davepierceops/illuminait/issues/25, read back open with `human-gate`. Automatic approval review initially rejected publication; the subsequent explicit approval authorized this payload and publication succeeded.

Observed: independent procedure verdict `ready-with-findings` in Fiducial `reviews/pkg-5-adopter-read-20261105T011244Z.md`; contradiction reread `ready-with-findings` in `reviews/adoption-contradiction-read-read-20261105T011305Z.md`. C1 replaces both legacy loaders exactly as reviewed. C2–C4 preserve experimental evaluation roles/core, Dave's untracked-retro timing, and consulting scope. DEC-000440 supersedes DEC-000280 with attribution and project clauses restated. The v2026.09.29 tree remains historical reference; only v2026.09.17 is removed. Existing decisions and roles remain unchanged.

Observed: baseline full suite passed 290 tests; implementation full run passed 301. Two subsequent hardening tests are included in the final committed focused run: all 13 adopter tests passed, also independently rerun by the reviewer. These tests cover contract behavior and mocked label operations, not live harness loading. Logs: `/private/tmp/fiducial-pkg5-baseline.log`, `/private/tmp/fiducial-pkg5-full.log`, `/private/tmp/fiducial-pkg5-focused.log`.

Observed, contract-verified: a fresh prepare from the exact pinned source produced zero writes/conflicts. The independent reader checked all 62 inventory entries and both emitted trees against the approved plan. Actual second apply returned no writes; before/after hashes and modes of every target file matched, including reports. No new report was created.

Observed, live-verified for GitHub metadata only: the adopter label step and read-back confirmed human-gate, blocking, deferred, accepted-risk, not-material; all existed and were unchanged. Private Free-tier branch protection remains unavailable; DEC-000030 records the accepted-risk fallback and PR-only landing. Emitted force-push patterns are present; every runner permission mode was not live-tested.

Known gaps: https://github.com/davepierceops/fiducial/issues/411 (existing shared-file permissions) and https://github.com/davepierceops/fiducial/issues/412 (empty-directory drift), both nonblocking/file-and-land. Neither condition exists in this idle isolated target. The original clone's untracked budgets and retros were untouched.

## Human live check

Evidence class: **contract-verified** until Dave runs this fresh session. The isolated worktree holds the proposed files before merge. The command prints actual provenance before opening Claude Code:

```sh
cd /private/tmp/illuminait-fiducial-adoption && sed -n '5p' CLAUDE.md && claude '/context'
```

Expected first line: `<!-- fiducial davepierceops/fiducial @ bb2ebcb4ea140deb40d7148d7dbffcae56806fe2 -->`. Then `/context` should list this repository's CLAUDE.md under Memory files; record observed output, not an assumed token count. Claude documentation: https://code.claude.com/docs/en/memory and https://code.claude.com/docs/en/cli-reference. Codex project hook trust is a separate unverified live boundary. No automated Claude call was made.

## Release and rollback

Intent: replace general harness loading while preserving project decisions. Acceptance: independent rulings, both trees installed, no-op rerun, labels present, report retained. SLOs: N/A for text/config adoption. Recommendation: needs the human decision at merge and human live check. Revert the adoption commit to undo tracked installation; existing labels were unchanged. No agent merges or releases this PR.
