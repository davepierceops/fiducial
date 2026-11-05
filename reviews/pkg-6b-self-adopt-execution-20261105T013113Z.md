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
  ".claude/agents/README.md": {
    "mode": 420,
    "sha256": "5bd77c067ced6300209877e813cb635c2944c2a3a5d6ae2d071353d2768ce82a"
  },
  ".claude/agents/architect.md": {
    "mode": 420,
    "sha256": "15581a3f2a3015865e960b64e8eabd94ddc90f418027b26b516f92773d1fe32e"
  },
  ".claude/agents/test-designer.md": {
    "mode": 420,
    "sha256": "44c4650315816f7f32e709adbd5e626a199a0a8731108f1bcc96f8492f1fb9ab"
  },
  ".claude/settings.json": {
    "mode": 420,
    "sha256": "2a0d02b9c78ccdc6c23b501c5a623d28bfaa817429e0681e51b4672bfa3e1490"
  },
  ".claude/skills/README.md": {
    "mode": 420,
    "sha256": "9d709897614e2ab929c88dbcb2beba3e44f9ec0a9261c46a2ab781d908ec90c6"
  }
}
```

## Independent contradiction read

```json
{
  "plan_sha256": "25395afa28497ae0cbb3f28270ac81addf0ddfbcf36608bc198ca93f95c75b6a",
  "reviewer": "independent adopter contradiction reader (adoption_contradictions), package 6b canonical-source metadata follow-up",
  "findings": []
}

```

## Human rulings

```json
{
  "authorization": "User execution block explicitly directs package 6b self-adoption and replacement of the four stale adapter/placeholder files, with human merge; independent semantic read found no new contradiction requiring a ruling. User reconfirmed proceeding on 2026-11-04.",
  "gate": "routine",
  "go": true,
  "human": "Dave Pierce",
  "plan_sha256": "25395afa28497ae0cbb3f28270ac81addf0ddfbcf36608bc198ca93f95c75b6a",
  "review_sha256": "39c2d82b5ccf802ac9abe71f14e646564ddb5eacef76736ea2e4336843815f49",
  "rulings": {}
}
```

## Exact legacy edits

```json
[]
```

## Self-adoption execution evidence

Observed 2026-11-05 UTC on `pkg-6b-self-adopt`, before the implementation
commit. Store and target baseline: `33ff36411f231c611152e4473a2b6f1262ca2561`.
The source was an idle local Git clone pinned to that SHA with canonical origin
`https://github.com/davepierceops/fiducial.git`; its source diff was empty.
The target was idle and its only pre-apply edit was this package's README.
The executable helper was extracted from the single Python fence in
`process/adopt.md` at that SHA. Final reviewed plan SHA256:
`25395afa28497ae0cbb3f28270ac81addf0ddfbcf36608bc198ca93f95c75b6a`.
The plan contained five existing files, 62 writes and no structural conflicts.

Environment: macOS-26.7-arm64-arm-64bit-Mach-O. Python 3.15.2; Git git version 2.55.0.
All preparation, generation, installation, hook probes, and tests run locally.
The coder's execution environment has restricted network access. The parent
session used authenticated GitHub access solely for the forge precondition
and label checks reported below. No infrastructure command was run.

The independently authored review and actual authorization are embedded above.
The parent supplied both JSON files after the independent read, recording the
human's explicit package 6b self-adoption authorization. Installation prepares
an unmerged branch; the human retains the merge decision. Per the explicit
package scope, this change does not append to `decisions/log.md`.

### Scoped legacy cleanup

After applying the reviewed plan, removed exactly the four stale files the
human authorized replacing: `.claude/agents/architect.md`,
`.claude/agents/test-designer.md`, `.claude/agents/README.md`, and
`.claude/skills/README.md`. The emitted agents use the modern names
`.claude/agents/architect-agent.md` and
`.claude/agents/test-designer-agent.md`; the skill directories contain their
actual `SKILL.md` procedures. No additional source rules or process documents
changed. All eight original `.claude/settings.json` deny entries remain,
including the force-push, recursive-removal and credential-read denies;
its mode remains 0644. Ownership is recorded for 61 emitted files in
`.claude/fiducial-ownership.json`.

### Project setup and forge labels

Told by the parent session from its authenticated read-back of this repository:
main has a required pull-request rule, `enforce_admins.enabled=true`,
`allow_force_pushes.enabled=false`, and `allow_deletions.enabled=false`.
The parent ran the extracted helper's `labels davepierceops/fiducial` command,
then read back `human-gate`, `blocking`, `deferred`, `accepted-risk`, and
`not-material`, all present. Existing runner force-push denies were preserved;
both emitted harness layouts include their source-pattern force guards.
The runner's behavior in every permission mode was not live-tested. The
project-setup confirmation here is limited to those observed forge settings
and the configured denies, with the live runner boundary retained.

### Installed intake guard probes

Evidence class: contract-verified. The following JSON payloads were sent to
the installed scripts on branch `pkg-6b-self-adopt`. No Edit, Write, or
`apply_patch` tool performed a mutation. Both subprocesses returned 2, and
`rules/R0934.md` had the same SHA256 before and after:
`c11a126c6039a3992ca7882f7a258f515f388be7973800db3e4de2b095e05b72`.

```json
[
  {
    "harness": "claude-code",
    "command": [
      ".claude/hooks/intake-branch-guard"
    ],
    "payload": {
      "hook_event_name": "PreToolUse",
      "tool_name": "Edit",
      "cwd": "/private/tmp/fiducial-pkg-6b-self-adopt",
      "tool_input": {
        "file_path": "/private/tmp/fiducial-pkg-6b-self-adopt/rules/R0934.md",
        "old_string": "probe-only",
        "new_string": "not-applied"
      }
    },
    "returncode": 2,
    "stdout": "",
    "stderr": "intake-branch-guard: rules/R0934.md is governed text (R0934); edit it on an intake/* branch through the intake skill, not on 'pkg-6b-self-adopt'\n"
  },
  {
    "harness": "codex",
    "command": [
      "python3",
      ".codex/hooks/codex-hook",
      "script",
      "[]",
      "intake-branch-guard"
    ],
    "payload": {
      "hook_event_name": "PreToolUse",
      "tool_name": "apply_patch",
      "cwd": "/private/tmp/fiducial-pkg-6b-self-adopt",
      "tool_input": {
        "command": "*** Begin Patch\n*** Update File: rules/R0934.md\n@@\n-probe-only\n+not-applied\n*** End Patch"
      }
    },
    "returncode": 2,
    "stdout": "",
    "stderr": "codex-hook: intake-branch-guard: rules/R0934.md is governed text (R0934); edit it on an intake/* branch through the intake skill, not on 'pkg-6b-self-adopt'\n"
  }
]
```

These probes establish the scripts' refusal for a governed path outside an
`intake/*` branch. They do not establish that a live harness loaded the files,
trusted project hooks, or invoked the hook for an actual tool call.

### Verification and known gaps

- Contract-verified: `bin/tests/run` passed all 303 tests in 99.170 seconds
  on this package's unchanged source; an installed-tree run is recorded below.
- Contract-verified: two emissions each from the pinned source yielded
  byte- and mode-identical Claude Code trees (30 files) and Codex trees
  (31 files). Standalone writer bundle generation succeeded (one file).
- Contract-verified: the README has 116 lines and all 26 named repository
  paths exist. It documents all three emit targets, repository adoption,
  standalone writing roles, Claude chat and intake.
- Contract-verified: repeat prepare against the installed target with the
  same pinned source returned `writes=[]` and `conflicts=[]`. The independent
  no-op read and apply check are recorded below.
- Existing accepted guidance: raw emitted `CLAUDE.md` is 287 lines;
  adoption ownership markers make the installed file 289 lines. The emitter
  warns and emits, as already ruled in package 3a's review and documented in
  `specs/rule-store.md`; this package does not change the source selection.
- Unverified; release impact `deferred`: Claude Code `/context`, Codex project
  hook trust, and actual harness-driven tool enforcement at this repository.
  A fresh session in the eventual checkout must confirm loading and trust;
  subprocess probes are contract evidence only. The human opening that session
  is the trigger for recording its observed result.
- Unverified; release impact `not-material` to this branch preparation:
  behavior of force denies in every runner permission mode. Parent observations
  and preserved configuration establish the setup described above only.
- SPEC open question 1 remains open. `bin/release` was not changed.

To check Claude Code loading, start it in this existing checkout:

```sh
cd /private/tmp/fiducial-pkg-6b-self-adopt
claude
```

Then run `/context` in the fresh session. Expected qualitative result:
`CLAUDE.md` appears as a loaded repository instruction source. This has not
been observed. A later checkout requires its actual path in this check.

The complete candidate and installed diff are reviewable in this package's
Git diff against the baseline. Rollback is to revert this branch's adoption
commit before merging; rerunning adoption uses the recorded ownership.

### Independently checked no-op apply

The parent supplied the independent no-op read and actual approval for
`/private/tmp/fiducial-pkg6b-rerun`. Applying its empty plan printed `[]`.
A snapshot of all 65 installed harness/report files (including ignored hook
bytecode) confirmed identical bytes and modes before and after; no report
was created or rewritten. The evidence below was appended afterward.

```json
{
  "changed_paths": [],
  "files_checked": 65,
  "file_bytes_and_modes_unchanged": true,
  "report_preserved": true,
  "plan_sha256": "80c3ebfb306914d28c73191106fc6854d56571eb47259ad9dc65354de23d9170"
}
```

### Final installed-tree suite

Contract-verified: `bin/tests/run` after installation and the four authorized
removals passed all 303 tests in 97.554 seconds, with no skips or failures.
`git diff --check` passed. Manifest hash and mode records for whole-file
objects match the installed executable hooks and TOML agents. No changes
under `rules/`, `process/`, `bin/` or `decisions/log.md` are included.
