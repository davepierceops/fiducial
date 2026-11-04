---
audience: [human]
status: approved 2026-11-03
---

# SPEC: fiducial, the subtraction

The spec for one revision of fiducial. It is the first document written in the
form it proposes: one spec, holding intent, design and the definition of done.

## 1. Problem and intent

Fiducial was built in June to understand the harness problem space, at a time
when no harness could be assumed. It did that. One thing it taught: the
orchestration — who runs what, in what order, with what handoffs — belongs in
deterministic code around the model, not in instructions to the model. The
harnesses now carry that code (Claude Code, Claude, Codex), and they do it
better than prose can.

Fiducial today still carries it: directives, batons, route-and-model lines,
execution-session choreography, worktree instructions, `bin/land`, and the
bundle as the only loading container. Evidence from the 2026-11-02 Illuminait
session: the decision session ran nine subagents itself, the human saw triage
lines and gates, and the reviews caught defects that would otherwise have
reached the human's first `plan`. A deny rule and a seven-line hook made "no
agent applies" a property of the harness in two minutes.

This revision removes the orchestration from fiducial and keeps what the
harnesses do not do: the evidence model, the gates, the spec, the decision log,
retros, and the context each role needs.

## 2. Users and use cases

- The human, in Claude chat, as Chief of Staff: decides, approves, rules at
  gates. Never carries a message between sessions.
- The decision session: runs execution and review as subagents in the harness
  it is in; returns triage lines, PRs, and gate requests.
- An adopting repo: has whatever harness files it already has; receives
  fiducial's context for its roles without losing its own.
- The writing roles — writer, copy-editor, critic — invoked by name as
  standalone bundles. Out of scope for this revision and unchanged by it.

## 3. User journeys

1. **Adopt.** The human points the adopter at a repo. It reads what exists —
   for Claude Code: `CLAUDE.md`, `.claude/settings.json`, `.claude/rules/`,
   `.claude/agents/`, `.claude/skills/`; for Codex: `AGENTS.md` (root and
   nested, with `AGENTS.override.md`), `.codex/config.toml`,
   `.codex/hooks.json`, `.codex/agents/*.toml`, `.agents/skills/` — compares
   against what the store says the roles in play need, reports contradictions
   for the human's ruling, creates what is missing, appends what is wanted.
   Run again after a store change: same operation.
2. **Build.** The human and the decision session write `SPEC.md` by interview;
   the human approves it. The decision session plans, runs coders and reviewers
   as subagents, and hands the human a PR and a gate request. The human
   approves the merge, the release, or anything else that cannot be taken back.
3. **Review.** A reviewer that did not write the change reads the diff against
   the spec and reports gaps that affect correctness; a skeptic pass carries its
   own verdict. Findings file-and-land unless the human raises one to blocking.
4. **Record.** Every ruling the human makes lands in `decisions/log.md`; a retro
   is written when the human asks and never touches a remote.

## 4. Goals and non-goals

### Functional goals

- Every row is sorted by one test: **if a harness can enforce it
  deterministically, it leaves the store — as a hook, a deny rule, an agent
  file, a skill, or nothing; if it requires judgment, it stays.** The sort is
  recorded per row.
- The orchestration layer retires: the directive package (route-and-model
  line, FIRST ACT, worktree choreography, the M1–M8 lint), the
  execution-session courier rows, and `bin/land`; their process documents
  (`directive-invariants.md`, `decomposition.md`, `spec-test-suite.md`,
  `named-queries.md` as it stands) and tools (`bin/directive`,
  `bin/check-directive`, `bin/land`, `bin/cycle-open`). Retired rows move to
  `rules/retired/` naming what replaced them, per the store's own rule.
- Three human-facing forms stay, pruned, because a harness cannot compute
  them: the **command block** (shell the human runs as given — an apply, a
  push from the machine that holds the credential); the **execution block**,
  as the secondary path for an executor the decision session cannot spawn
  (Claude Code on the human's machine, Codex); and the **baton**, carrying
  only what the successor cannot recompute from the tree — rulings not yet
  landed, open questions, what is running. The default is subagents; a block
  is handed only where a subagent cannot reach.
- The spec spine collapses to one `SPEC.md` per project: intent, users,
  journeys, goals, outcomes, definition of done, design, risk tolerance, open
  questions. `prd-template.md` and `trd-template.md` retire into one
  `spec-template.md`. The TRD's standing verification-boundary section and
  SLO targets for the Top K journeys live in the spec's design section.
- Fiducial's vocabulary adopts Anthropic's where the two name the same thing:
  spec, definition of done, approve, reviewer, a check to run, subagent, hook,
  deny rule, skill, agent. Fiducial keeps its own words where Anthropic has
  none: evidence class, verification boundary, consequential class, decision
  log, retro.
- The store stays the source of truth (provisional). The generator emits
  per-harness shapes: `CLAUDE.md` plus `.claude/{rules,agents,skills,settings}`
  for Claude Code; `AGENTS.md` for Codex; a project file for Claude chat. The
  store can mark a row as enforced rather than advised, and the generator
  emits those as hook or deny entries.
- An **adopter** skill exists and has been run once against a real repo
  (`illuminait-io`'s infrastructure repo, or `davepierceops/illuminait`) with
  its contradiction report and its diff kept as evidence.
- The six carried findings from the 2026-11-02 retro are each ruled on and,
  where ruled yes, landed: no agent applies or destroys (enforced, not
  advised); nothing in a human-facing block needs editing before pasting; a
  reviewer that did not write a directive reads it before dispatch — restated
  for the subagent model as: the reviewer reads the plan; on an external
  failure, search current documentation before diagnosing from memory; name
  the build environment's egress boundary in the plan; a subagent run killed
  by a usage cap is a listed review gap, not an absence.

### Non-functional goals

- **Maintainability:** one source of truth per topic; no row restated in a
  process document and no process step restated as a row.
- **Portability:** the same store serves three harnesses; a harness-specific
  fact lives in the generator's emitter for that harness, never in a row.
- **Usability:** `CLAUDE.md` emitted for a repo stays under 200 lines; only
  what the model cannot find by reading the repo.
- Performance, reliability, scalability, security, observability, compliance:
  `N/A` — this is a text repository with a small Python tool.

### Non-goals

- The writing corpus: writer, copy-editor, critic rows and their topics,
  `voice.md`, `outline.md`, the public-prose criteria. Unchanged.
- A new harness. Fiducial does not orchestrate; the harness does.
- Retiring the dated bundle release. Open question 1.

## 5. User outcomes and measurement

- A new repo is adopted in one session with no hand-written harness file.
  Signal: the adopter's run log on the first real repo.
- A build runs spec → subagents → PR → gate with the human carrying nothing
  between sessions. Signal: the next Illuminait retro reports no courier step.
- The store shrinks. Signal: row count and bundle line counts before and after,
  per role. Baseline: 461 rows; chief-of-staff bundle 181 rows.

## 6. Definition of done

- [ ] Every row carries a recorded sort: `stays`, `harness:<hook|deny|agent|skill>`, or `retired:<successor>`.
- [ ] Every row sorted `retired` is under `rules/retired/` with a `retired:` line; none is deleted.
- [ ] Every row sorted `harness:*` has a corresponding emitter in the generator, and the emitted object exists in the generator's test fixtures.
- [ ] `process/` holds no document that governs a retired mechanism; each retired document is in `docs/history/` with the DEC entry that retired it.
- [ ] `process/spec-template.md` exists; `prd-template.md` and `trd-template.md` are retired into it; `specs/*.md` and the PRD rows in topic `prd-template` and `trd` are reconciled to it.
- [ ] The generator emits the three harness shapes from the store, with tests.
- [ ] The adopter skill exists, with its contradiction read and its append step, and has run once against a real repo; the run's report is committed as evidence.
- [ ] `bin/directive`, `bin/check-directive`, `bin/land`, `bin/cycle-open`, and the dead members of `bin/aimeta/` are removed (#382 closes).
- [ ] `.claude/agents/architect.md` and `test-designer.md` are regenerated from the store or removed.
- [ ] `README.md` describes fiducial as it now is, in Anthropic's vocabulary where adopted.
- [ ] Every ruling from the 2026-11-03 session is a DEC entry; DEC-000910 (adapters as thin pointers) is superseded by name.
- [ ] A review by a subagent that wrote none of it reads the whole delta against this spec and returns a verdict; the human approves the merge.
- [ ] The root residue (`BACKLOG-v2.md`, `COLLAB-STATE.md`, `MANIFEST.md`, `MERGE-NOTES-v0.4.md`, `REVIEW-NOTES-*.md`, `REVIEW-v0.4.md`, `OPEN-ITEMS.md`, `ACCEPTED-RISKS.md`, `voice-inbox.md`) is archived under `docs/history/` (#361, #370 close).

## 7. Design

**What stays, by topic.** `core`, `verification`, `verification-boundaries`,
`change-control`, `human-review-boundary`, `commit-control`,
`decision-log-policy`, `review-artifact-schema`, `retro`, `intake`, `lexicon`
(pruned of retired terms), the role topics for the software roles (pruned),
`chief-of-staff` (pruned to judgment). Each row in these still faces the sort.

**What leaves, by topic.** `directive-invariants` (the package; the
execution-block invariants — self-contained, nothing before the block,
pasteable whole — move to `command-blocks`), `command-blocks` keeps only the
human-facing rows, `convergence`, `decision-layer` (the courier half; the
baton rows stay, pruned to R0252's test), `remote-write-verification-policy`
(the hand-run half), `change-flow` (rewritten around the subagent model, much
shorter), `decomposition` (plan mode and the plan reviewer replace it),
`spec-test-suite` (folds into the spec's definition of done and the red gate).

**The sort, mechanically.** One pass over 461 rows by a subagent, producing a
table: id, topic, current body, proposed sort, replacement if any. The human
rules on the sort by class, not by row (R1448); the table is the evidence.

**The store's new field.** `enforce: <hook|deny|none>` on a row; the generator
reads it. A row with `enforce: hook` carries the hook's event and command in a
fenced block; the generator emits it into `.claude/settings.json` and refuses
a row whose block is missing.

**The generator.** `bin/bundle` keeps its query model (role, session, corpus)
and gains emitters: `claude-code` (CLAUDE.md, `.claude/rules/*.md` path-scoped
where a row carries `paths:`, `.claude/agents/<role>.md` with `tools:` and
`model:` frontmatter, `.claude/skills/<process>/SKILL.md` for each surviving
process document, `settings.json` hooks and deny rules), `codex` (`AGENTS.md`
under its 32 KiB default ceiling; `.codex/agents/<role>.toml` with
`developer_instructions`; `.agents/skills/<process>/SKILL.md`;
`.codex/hooks.json` for enforced rows — Codex has no deny-rule file, so a
`deny` row emits as a `PreToolUse` hook there), and `bundle` (today's form,
kept for the writing roles and for Claude chat).

**The adopter.** A skill, because its contradiction read is a judgment. Steps:
inventory the repo's harness files; emit fiducial's shapes to a staging
directory; a subagent reads both and reports contradictions by file and line;
the human rules; the append step merges under a fiducial marker so a re-run
replaces its own section and nothing else. The create path is deterministic.

**Verification boundary.** The adopter is browser- and harness-dependent only
in that Claude Code must load the result; the evidence class for "the emitted
`CLAUDE.md` is honored" is live-verified by one session that runs under it and
reports `/context`. Everything else is contract-verified by the generator's
tests.

## 8. Risk tolerance

- Anything the human cannot take back — a release, a `rules/` deletion, a force
  push — is gated. Retirement is reversible by construction (`rules/retired/`).
- A wrong sort on a row is cheap: it is one row, and the sort is recorded, so it
  can be re-sorted. The human rules on classes and accepts per-row error.
- The adopter writing into a repo the human does not own is consequential;
  its first real run is on a repo the human controls.

## 9. Open questions

1. Does the dated bundle release (`v<YYYY>.<MM>.<DD>`, twelve assets) survive
   for the software roles, or does the adopter read a tagged store directly?
   Resolved by: the first adopter run — whether it wants a tag or a file.
2. Where does the Claude chat Chief of Staff load from once bundles are a
   writing-role form — a project file emitted by the generator, or the same
   bundle? Resolved by: trying both in the next chat session.
3. Does the store stay the source of truth once the generator has three
   emitters? Provisional yes (2026-11-03). Resolved by: the cost of the
   generator rework, observed.
4. Is the Codex emitter in this revision or the next? Resolved by: whether a
   Codex session is planned before the next revision.
