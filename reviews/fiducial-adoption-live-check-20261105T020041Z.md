# Illuminait adoption: human-run Claude Code loading check

Evidence class: live-verified for CLAUDE.md loading and project agent/skill discovery only.
Provenance: Dave supplied a screenshot of Claude Code on codex/fiducial-adoption / PR #26, then pasted expanded /context all output in the Fiducial packages 5/6b Codex chat. The session followed the supplied fresh-session check. This is human-supplied runtime evidence, not an agent-run Claude probe.

Observed in the supplied output:

```text
Custom agents · .claude/agents/
Project
reviewer-agent: 88 tokens
release-manager-agent: 61 tokens
spec-reviewer-agent: 61 tokens
architect-agent: 60 tokens
context-quality-reviewer: 58 tokens
skeptic-risk-agent: 51 tokens
test-designer-agent: 41 tokens
coder-agent: 24 tokens

Memory files · /memory
CLAUDE.md: 8.6k tokens

Skills · /skills
Project
adopt, decision-log, project-status, spec-template, build, release,
outline, intake, review-artifact, voice, change-flow, retro
```

The names and token values above are transcribed from the output; skill names are compacted into a list. The output reports 48.3k total tokens, including 29.2k system-tool tokens, 5.6k system-prompt tokens, 8.6k memory-file tokens, and 2.9k skill tokens across project, plugin and built-in sources. These counts are observations of this session, not budgets or expected constants.

Observed in the local adopted tree: eight emitted agent files match the runtime names. Thirteen project skill files exist; the twelve shown match the model-invocable set. The remaining gate skill has disable-model-invocation: true at the start of its YAML frontmatter. Official Claude documentation states this keeps its description out of context while allowing manual invocation: https://code.claude.com/docs/en/skills#control-who-invokes-a-skill. Inferred: its absence from this context listing is expected, not an installation defect. Manual gate invocation has not been tested here.

At read-back before recording this evidence, Illuminait PR #26 remained open at a0e8611f26f4a88f7a180502362d97f1080c78b1, with emitted source bb2ebcb4ea140deb40d7148d7dbffcae56806fe2. Fiducial package 5 PR #413 remained open at 33ff36411f231c611152e4473a2b6f1262ca2561. The expanded output names CLAUDE.md but does not print its absolute path, source hash or full content; location is supported by the preceding screenshot and supplied command context. It does not prove byte-for-byte runtime contents or compliance with every instruction.

Disposition: the pending Claude Code loading check in docs/fiducial-adoption-20261105T011135Z.md (and its Fiducial reviews/ copy) is now satisfied for root memory loading and the displayed agent/skill discovery. Earlier reports remain dated snapshots. This note adds the new evidence without rewriting them.

Still unverified: actual hook firing through Claude tool calls, deny enforcement across permission modes, agent execution/instruction adherence, manual gate invocation, Codex project hook trust and live Codex loading in this target, and live loading in Fiducial's separate package 6b checkout. No broader enforcement or production claim follows from /context.

No implementation, configuration, decision-log entry, merge or release is changed by recording this evidence.
