# Fiducial

Fiducial gives agents the context and evidence standards a harness cannot
supply: human intent, an approved spec, review, consequential gates, a decision
log, and retros. The harness runs sessions, tools, and subagents. Fiducial's
store holds the judgment rules; its generator emits the forms each harness
loads.

The central question is what a claim establishes. A passing parser test
supports the parser's contract. It does not establish that a live service
accepted credentials. Reports carry the evidence class, the verification
boundary, the remaining gap, and the check that would close it. Independent
review examines both the work and that evidence chain. Humans own intent,
risk decisions, and consequential approval.

## Adopt into a repository

Use [the adoption procedure](process/adopt.md) for a new repository or an
upgrade. Start by reading its spec and decisions and confirming the
[project setup preconditions](process/project-setup.md).

The procedure contains the executable Python helper. With Python 3.11+, Git,
and a pinned local copy of this store, follow it to:

1. Inventory the repository's existing harness files and emit both harness
   trees into a separate staging directory. Nothing is installed yet.
2. Have an independent reviewer read the existing files, staged context,
   and complete candidate diff for contradictions.
3. Bring the report and proposed resolutions to the human. Record the actual
   rulings and approval before running the helper's apply step.
4. Inspect the installed diff, retain the ownership manifest and adoption
   report, check a repeat run, and open the adopting repository's PR.

The helper creates missing files and merges its own marked sections and
recorded JSON contributions while preserving unrelated repository context.
It refuses structural conflicts and locally edited managed content. Re-run
this procedure deliberately after a store update; do not copy generated
files over an existing harness setup by hand.

Generated files and executable hook probes provide contract evidence. Confirm
loading in a fresh Claude Code session with `/context`; Codex hook trust and
actual harness enforcement also require a live session. The adoption report
keeps those boundaries explicit.

## Standalone bundles

Writing roles remain available as single Markdown bundles: [writer](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-writer.md),
[copy-editor](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-copy-editor.md),
and [critic](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-critic.md).
Load the complete bundle into a fresh chat or project. The writer develops a
draft; separate copy-editor and critic sessions propose edits and comments;
the author decides what stays. These bundles contain my voice and publication
preferences. The [voice procedure](process/voice.md) describes that context;
adapting the source requires regenerating the bundle.

Claude chat can load the [Chief of Staff bundle](https://github.com/davepierceops/fiducial/releases/latest/download/fiducial-bundle-chief-of-staff.md)
as a project file. Start with a problem and work toward an approved
[SPEC.md](SPEC.md), using the [spec template](process/spec-template.md).
[Build](process/build.md) covers implementation and independent review;
[gate](process/gate.md) and [release](process/release.md) cover approval and
release preparation. The host supplies tool access and subagent execution.
[Project status](process/project-status.md) is a separately invoked skill.
[Command blocks](process/command-blocks.md) supplies the procedure before
composing human-run commands or instructions for another agent session.
[Verification checklists](process/verification-checklists.md) supplies the
applicable role sections for verification planning, execution, reporting and
boundary or release assessment. Harness context carries invocation triggers;
standalone bundles retain the applicable procedures.

Pin repeatable bundle use to a dated [release](https://github.com/davepierceops/fiducial/releases).
The [named queries](process/named-queries.md) define the distributed roles.
Software adoption uses the store checked out at a release tag. Releases
retain all twelve role bundles plus README.md for chat and compatibility
(DEC-001610); Claude chat keeps the Chief of Staff bundle as its project file
(DEC-001620).

## Generate locally

The tooling uses Python's standard library and Git. From this repository:

```sh
bin/bundle --keys
bin/bundle --emit bundle --where role=writer --name writer --out /tmp/fiducial-writer
bin/bundle --emit claude-code --out /tmp/fiducial-claude
bin/bundle --emit codex --out /tmp/fiducial-codex
bin/tests/run
```

Generation reads the local tree, including uncommitted edits, offline on any
branch. An explicit output directory keeps generation separate from
installation. Use the adoption procedure to install harness context.

| Target | Output |
| --- | --- |
| `bundle` | One Markdown file selected by a query; writing roles and Claude chat |
| `claude-code` | `CLAUDE.md` and `.claude/` agents, skills, hooks, and settings |
| `codex` | `AGENTS.md`, `.codex/` agents and hooks, and `.agents/skills/` |

The [rule-store spec](specs/rule-store.md) defines selection, provenance,
emission, and verification boundaries. This repository carries its own
adopted harness context as well as the source that generated it.

## Contribute

Propose a rule change with its reason and evidence through
[intake](process/intake.md). Changes to `rules/` or `process/` are made on an
`intake/*` branch, independently reviewed, and brought to the human for any
outstanding ruling. A rule's meaning changes in place; a replaced obligation
is retired with its successor recorded. Send other improvements by PR.

| Location | Contents |
| --- | --- |
| `rules/` | Judgment rules, enforcement declarations, definitions, and retired rows |
| `process/` | Skill procedures, templates, and bundle queries |
| `bin/` | Generator, hook sources, release tool, and tests |
| `specs/` | Store and generator specification |
| `decisions/log.md` | Recorded human decisions |
| `reviews/`, `retros/` | Evidence and findings at their stated revisions |
| `docs/history/` | Earlier forms and retired mechanisms |

The tests establish tool behavior. Fiducial's comparative effect on agent
outcomes, human effort, cost, and context overhead remains unestablished.
See [current issues](https://github.com/davepierceops/fiducial/issues) and the
[license](LICENSE).
