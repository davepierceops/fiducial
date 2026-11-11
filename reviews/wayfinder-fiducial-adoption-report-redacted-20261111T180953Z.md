# Fiducial adoption

Redacted copy for the public store. The adopting repository is private; its file paths, line numbers, and descriptions of its contents are replaced with `[redacted: private target detail]`. The unredacted report is in the adopting repository at `docs/fiducial-adoption-20261111T180953Z.md`. Nothing else is changed.

Evidence class: contract-verified. Claude Code /context and Codex hook trust: not live-verified by this procedure.

Changed paths:

- `.agents/skills/adopt/SKILL.md`
- `.agents/skills/build/SKILL.md`
- `.agents/skills/change-flow/SKILL.md`
- `.agents/skills/command-blocks/SKILL.md`
- `.agents/skills/decision-log/SKILL.md`
- `.agents/skills/gate/SKILL.md`
- `.agents/skills/intake/SKILL.md`
- `.agents/skills/outline/SKILL.md`
- `.agents/skills/project-status/SKILL.md`
- `.agents/skills/release/SKILL.md`
- `.agents/skills/retro/SKILL.md`
- `.agents/skills/review-artifact/SKILL.md`
- `.agents/skills/spec-template/SKILL.md`
- `.agents/skills/verification-checklists/SKILL.md`
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
- `.claude/skills/command-blocks/SKILL.md`
- `.claude/skills/decision-log/SKILL.md`
- `.claude/skills/gate/SKILL.md`
- `.claude/skills/intake/SKILL.md`
- `.claude/skills/outline/SKILL.md`
- `.claude/skills/project-status/SKILL.md`
- `.claude/skills/release/SKILL.md`
- `.claude/skills/retro/SKILL.md`
- `.claude/skills/review-artifact/SKILL.md`
- `.claude/skills/spec-template/SKILL.md`
- `.claude/skills/verification-checklists/SKILL.md`
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
{}
```

## Independent contradiction read

```json
{
  "plan_sha256": "15e4e360ee6906c30193eb145284fbe82aaaa19950778998a186965a2b98136c",
  "reviewer": "independent subagent contradiction reader (adopt step 2); wrote none of the candidate",
  "findings": [
    {
      "id": "F1",
      "file": "[redacted: private target detail]",
      "line": "[redacted: private target detail]",
      "staged_file": ".claude/skills/command-blocks/SKILL.md",
      "staged_line": 24,
      "claim": "The target has an automated job that pushes straight to the default branch; the staged context, and the project-setup fallback that applies because the forge refuses branch protection, require every landing by pull request and never a push to the default branch. The accepted-risk decision-log entry that fallback requires does not exist in the target."
    },
    {
      "id": "F2",
      "file": "[redacted: private target detail]",
      "line": "[redacted: private target detail]",
      "staged_file": ".claude/skills/change-flow/SKILL.md",
      "staged_line": 27,
      "claim": "The target changes its code by executing a directive directly and reporting; the staged change flow routes every meaningful software change through the build skill, which starts from an approved SPEC.md the target does not have, then tests, pull request and review passes."
    },
    {
      "id": "F3",
      "file": "[redacted: private target detail]",
      "line": "[redacted: private target detail]",
      "staged_file": "CLAUDE.md",
      "staged_line": 36,
      "claim": "The target has its orchestrating session report results from subagent verdicts without reading the underlying material itself; staged CLAUDE.md requires claims about results to be checked against the underlying source or result."
    },
    {
      "id": "F4",
      "file": "[redacted: private target detail]",
      "line": "[redacted: private target detail]",
      "staged_file": "CLAUDE.md",
      "staged_line": 14,
      "claim": "The directive tells the agent to resolve a directive-versus-convention disagreement itself by following the convention and noting it; staged CLAUDE.md says to name the conflict and ask the human before relying on either source."
    },
    {
      "id": "F5",
      "file": "[redacted: private target detail]",
      "line": "[redacted: private target detail]",
      "staged_file": ".claude/skills/command-blocks/SKILL.md",
      "staged_line": 34,
      "claim": "A human-run procedure in the target has a commit block carrying a placeholder the human must substitute; the staged command-blocks skill says a block carries no placeholders and runs verbatim as pasted."
    }
  ]
}

```

## Human rulings

```json
{
  "gate": "routine",
  "go": true,
  "human": "Dave Pierce",
  "plan_sha256": "15e4e360ee6906c30193eb145284fbe82aaaa19950778998a186965a2b98136c",
  "review_sha256": "1db975ed96ab92ddb6276f74bf63e3503e11c012455eb0d9eb79cd8499d72fa6",
  "rulings": {
    "F1": "Accepted risk (2026-11-11, chat). Dave: \"Yes, because this is a private repo on a free GitHub account, I wish to overrule the requirement that is not possible in a free GitHub private account. I mean, free GitHub private repo.\" The unattended job keeps pushing to main; everything else lands by pull request; the branch-protection precondition is overruled for this repository.",
    "F2": "Accepted risk (2026-11-11, chat, \"y\" to option 1). In wayfinder, directives stay the specification; the SPEC-first build flow applies only once a SPEC.md exists.",
    "F3": "Accepted risk (2026-11-11, chat, \"y\" to option 1). The pipeline's verify subagent is the source check for the orchestrator's claims.",
    "F4": "Accepted risk (2026-11-11, chat, \"yes\" to option 1). The directive's follow-the-convention-and-note-it rule is the standing resolution for directive-versus-convention conflicts; every other source conflict goes to Dave.",
    "F5": "Accepted risk (2026-11-11, chat, \"y\" to option 1). The procedure is left unchanged in the adoption PR."
  }
}
```

## Exact legacy edits

```json
[]
```

## Run record

Added by the decision session after apply. Labels: observed, inferred, told, unknown.

- Environment (observed): Anthropic cloud sandbox, Linux, Python 3.13.18; clones at `/home/claude/wayfinder` and `/home/claude/davepierceops/fiducial`; staging at `/home/claude/adopt-work/stage-1`, outside both. This was not run on the machine where wayfinder normally runs.
- Egress boundary (observed): git and the GitHub API through the session proxy; nothing else was contacted by the helper.
- Store (observed): `davepierceops/fiducial` at tag `v2026.11.10`, `a8d87bc95afed9f5ac8b54fe2c8863013ce10265`, clean tree, no dirty diff.
- Target (observed): `davepierceops/wayfinder` at `1222d888c8bf6863bc5c77487a65bbeaca7e2d29` on `main`, clean before apply; applied on branch `adopt/fiducial-v2026.11.10`.
- Plan (observed): `plan.json` sha256 `15e4e360ee6906c30193eb145284fbe82aaaa19950778998a186965a2b98136c`; `review.json` sha256 `1db975ed96ab92ddb6276f74bf63e3503e11c012455eb0d9eb79cd8499d72fa6`; 66 paths written, 0 conflicts, 0 legacy edits.
- Independent read (observed): by a subagent that wrote none of the candidate; verdict `changes-required`, five findings, all ruled by the human as accepted risk. Its review artifact is `wayfinder-adoption-read-20261111T181610Z.md`, handed to the human in chat; a copy belongs in fiducial `reviews/` and has not been placed there.
- Gate decision (told, by the human in chat, 2026-11-11): go, classified routine; no `human-gate` issue opened. Rulings are recorded in `decisions/log.md` as DEC-000010 through DEC-000060.
- Installed tree (observed): every installed file is byte-identical to the reviewed candidate.
- Rerun (observed): prepare then apply against a copy of the applied tree gave 0 changed paths, 0 conflicts, and wrote no new report.
- Forge labels (observed): `human-gate`, `blocking`, `deferred`, `accepted-risk`, `not-material` created on `davepierceops/wayfinder` and read back from the API alongside the ten existing labels.
- Project setup, precondition 1 (observed): not met. GitHub returned HTTP 403 for branch protection and rulesets on this private repository. Overruled by the human; see DEC-000020.
- Project setup, precondition 2 (observed, contract level): `.claude/settings.json` carries the force-push deny rules. The independent read notes forms the patterns do not match, such as `git -C <dir> push --force` (inferred). Not checked in a live runner.
- Unverified: that Claude Code loads `CLAUDE.md` in a session at this repository (needs `/context` in a fresh session); that hooks run under `claude -p --permission-mode bypassPermissions`; Codex hook trust; whether Codex is used here at all (unknown).

## Live loading check

Added after merge (PR #1, merge commit `9a2df72056f76614de04ca8289dbdc7e16a53f0d`).

- Told (pasted by the human, 2026-11-11): a fresh Claude Code v2.1.318 session at `~/code/wayfinder`, model `claude-fable-5-1`, `/context all`.
- Observed in that paste, under "Memory files · /memory": `CLAUDE.md: 1.2k tokens`, the only memory file listed. The line carries no path.
- Observed in that paste, under "Custom agents · .claude/agents/", Project: the eight adopted agents.
- Observed in that paste, under "Skills · /skills", Project: fourteen of the fifteen adopted skills; `gate` is absent, consistent with its `disable-model-invocation: true` (inferred).
- Evidence class for Claude Code loading of `CLAUDE.md`, agents, and skills in an interactive session: live-verified on that machine and version.
- Still unverified: that hooks fire, in interactive sessions or under `claude -p --permission-mode bypassPermissions`; the force-push deny in a live runner; Codex loading and hook trust.
