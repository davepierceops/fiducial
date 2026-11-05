---
audience: [human]
---

# SPEC: Fiducial as a Rule Store

Reconciled 2026-11-04 from the rule-store PRD and the bundle-system PRD (DEC-001410) into the spec-template form (`process/spec-template.md`); the generator is its design section. The bundle-system PRD is at `docs/history/bundle-system.md`. Where the earlier text and the tree disagreed, the tree won.

## 1. Problem and intent

Fiducial's rules were held in 62 governed files, and the file was a bag of rules: a bundle that needed one rule got the whole file; a rule that had to be cited from a second file was restated; every file carried a lifecycle — status, review pointer, cycle number, agreement flip — that certified the *container* while an agent acted only on the *content*. One policy took 22 review cycles to agree. The machinery was an artifact of how the project grew from June, not a requirement of the methodology.

Ruled (the human, 2026-09-04): the methodology and the repository keep the name `fiducial`; history is preserved; the store becomes rows — one rule, one record, selected by key-value query — and gating moves from documents to content: one intake gate, at the row, and nothing else certifies a rule. Documents that describe sequences stay prose with a lighter gate.

The product is the same as before — the bundle any session loads as its first act, the governed text it needs and nothing else, from one command — now assembled from rows instead of files.

## 2. Users and use cases

- **The human, operator.** Regenerates bundles after a rule changes; uploads one per project; cuts a release. One command, one directory.
- **Agent sessions, any model, any harness.** Load a bundle first. Need the rows for their role, in order, with a header that says what it was made from and how old it is.
- **The Context Quality Reviewer, as intake.** Receives a proposed rule, shapes it, checks it against the store, lands it. Needs the store queryable and a mechanical shortlist of near-duplicates.
- **Methodology authors** — the human in chat, a retro, a finding. Propose a rule in a sentence and expect it to land through intake without a cycle.
- **Writers who are not repository users.** Have a document and a chat and nothing else; download the one file named for the role from the latest release and paste it; never see git.
- **Adopting projects.** State in one place which bundle their sessions load and at which release tag, and obtain it by the same URL; changing methodology changes the tag the project points at, not the project.

## 3. User journeys

### J1 — the human regenerates a bundle
Trigger: a row landed, was retired, or was re-keyed; or a new project needs its first bundle. Steps: one command names a query; the tool renders the local tree as it stands — uncommitted edits included, offline, on any branch (DEC-000940) — and writes one file to `~/Downloads` under the ruled name. Outcome: the bundle is the query's rows in order, then the process documents the query selects, then the definitions the rows use, under a one-line header naming repository, HEAD and generation time (DEC-000630, DEC-000640).

### J2 — a rule enters through intake
Trigger: anyone proposes a rule. Steps: a Context Quality Reviewer session reads the proposal against the store; shapes it into one instruction an agent can act on; runs the shortlist and reads the candidates; sets keys normalized to the keys in use; lands one commit. Outcome: either one new row exists, or the proposal is refused with the id of the row that already says it.

### J3 — a rule changes
Trigger: a row is wrong, too loose, too strict. Steps: the same act as J2 over the existing row; a row whose meaning changes keeps its id; a row whose obligation is replaced is retired with a pointer to its successor. Outcome: no history is lost and no second row says the old thing.

### J4 — a session judges its bundle's freshness
Trigger: the session is about to cite a path, a rule, or a count from the bundle. Steps: it reads the header's HEAD; where it can reach the repository it computes commits behind the default branch from that HEAD; where it cannot, it states the generation time as the bound on what it knows. Outcome: a stale bundle is named as stale before anything is cited from it, and a directive derived from it pins the bundle's HEAD as the revision it read.

### J5 — a role is added
Trigger: a new role. Steps: rows carry the role's value under `role`; one line in `process/named-queries.md` names the bundle and its query (DEC-000650). Outcome: `bin/bundle --where role=<new>` works, and the next release attaches the bundle, with no tool edit.

### J6 — the store changes backing
Trigger: files become tedious. Steps: a database-backed row source replaces the file-backed one behind the storage boundary. Outcome: nothing that selects, orders, renders, retires, or checks rows changes.

### J7 — the human cuts a release
Trigger: the human's go at one SHA of `main`. Steps: `bin/release` on a synced clone generates one bundle per entry in the list and prints the `gh release create` command; the human runs it. Outcome: a release tagged by date carrying `README.md` and one `fiducial-bundle-<slug>.md` per entry, each generated at that SHA (DEC-000660).

## 4. Goals and non-goals

### Functional goals
- **G1 — One command.** `bin/bundle --where <query> --name <name>` writes one file to `~/Downloads` named `fiducial-bundle-<name>-<timestamp>Z.md` (DEC-000200, DEC-000290, DEC-000320 filename clause), rendering the local tree as it stands; only `bin/release` checks origin (DEC-000940).
- **G2 — Each rule once.** One row per distinct rule; intake refuses a restatement with the existing id.
- **G3 — Only what the query names, in the ruled order.** A bundle is exactly the rows matching the query, in three bands: rules by their topic's position in the topic sequence, then topic name, then `order`, then id; the process documents the query selects, by their position in the process sequence; the definitions the selected rows use (DEC-000640).
- **G4 — Two forms, one row.** Agent form is the body; human form is `## Human`; the human form is never lost.
- **G5 — Computed assembly.** Membership is the row's own keys; no list of members anywhere; a new value on a key needs no tool edit; keys in use are computed.
- **G6 — Provenance and staleness.** The header is one line — an HTML comment naming repository, full HEAD and generation time — and nothing else (DEC-000630).
- **G7 — Storage boundary.** Rule-processing logic sees row objects only; file traversal, naming, frontmatter, and I/O live in one storage module; a database-backed module can replace it without touching the processing logic; no database now.
- **G8 — One gate.** Intake is the only gate on a rule; no status field; a row in `rules/` is in force.
- **G9 — Prose stays prose.** Sequence documents live in `process/`, carry `topic:` as their stem, are selected by the same query, cite rows by id, and are gated by one frontier read plus the human's sign-off recorded in the decision log.
- **G10 — Releases and reach.** A release attaches `README.md` and one `fiducial-bundle-<slug>.md` per entry in `process/named-queries.md`, each generated at the release's SHA, tagged `v<YYYY>.<MM>.<DD>`; the asset name carries no timestamp, so `releases/latest/download/` is a stable URL (DEC-000660).
- **G11 — History preserved.** No force-push, no rewrite; the old corpus is moved, never deleted; every row's `source` resolves.
- **G13 — One store, several harnesses.** `bin/bundle --emit <target>` renders the local tree through one emission target into the files one harness loads (design, "Emission targets"); a new target is one module, one registry line, one `tiers.json` column and its tests, and nothing else in `bin/` changes (DEC-001400). Targets today: `bundle`, `claude-code`, `codex`.
- **G12 — Definitions by term.** A bundle carries every definition a selected row uses, found by term, transitively, rendered last under one heading; a session never needs the store to read its bundle.

### Non-functional goals
Performance: generation in seconds; the shortlist over the store in under 30 s. Reliability: refuse over emit. Scalability: the model holds at a thousand rows and a second corpus by adding a value, not a mechanism. Security: no secret enters a row or a bundle. Maintainability: the tool changes when a new *kind* of thing is needed, never when a new value is. Portability: Python standard library and git; a bundle is Markdown any model reads, and no vendor-shaped adapter is required to consume one. Usability: the operator runs one command; a writer downloads one file; an agent reads one header. Observability: the header is the telemetry — what, from where, when — and nothing else is emitted. Compliance: N/A.

### Non-goals
- A database now (G7 forbids it).
- Editing history or the retired corpus.
- Gating rows by anything other than intake.
- Designing the key or topic vocabulary in advance; it is computed from use.
- Keeping any of: `status`, `last-reviewed`, the agreement flip, the expedited and doc-only paths, the frontmatter hook, per-document review cycles.
- A semantic version for the methodology: it cannot be computed, so the date is the version.

## 5. User outcomes and measurement

### Baseline at `main` 4a118f5 (observed)
- 62 in-scope files; 54 agent-facing; 1600 extracted rows across them.
- Writer bundle 22 files against a ruled set of 6; copy-editor and critic 21 against 5; chief-of-staff 33; the `all-roles` floor 16.
- The document-metadata policy reached `agreed` at cycle 22; the in-scope set carries 26 documents agreed on diff-only passes and 8 with no reviewer read.
- Corpus-wide dedup at `main` 4a118f5 (Pass 3, docs/rule-register/rule-clusters-20260904T223000Z.md): 1600 rows, 675 clustered into 206 clusters (15 divergent), 925 singletons — **1131 distinct rules**.

### Outcomes
- **Distinct rules.** Baseline: 1131 (Pass 3). Observed: 456 rows once five fix passes retired the lifecycle rules and the restatements (`main` a5d6050); intake holds it there. Observed by `bin/bundle --keys` over the whole store and by the intake log.
- **Bundle size per query.** Baseline: 22 files for the writer, 21 for the copy editor and critic. Target: the rows from the six and five files AC-RS-7 names and nothing else; observed by each selected row's `source`.
- **Cost to change a rule.** Baseline: a review cycle (directive, gate, fix, re-gate, flip — five directives for the last policy change). Target: one intake session, one commit. Observed by counting directives per landed row change.
- **Restatement.** Baseline: the clustering pass's cluster count. Target: zero cross-row restatement in the store; every later intake refusal recorded. Observed by re-running the shortlist over the store.
- **Storage substitution.** Observed: the row-source module has one interface and one file-backed implementation, and the processing tests run against in-memory rows.

## 6. Definition of done

- **AC-RS-1 — Row shape.** Every file under `rules/` parses to `id`, a non-empty body, and a dictionary; every value is a list of words after normalization; `order` is an integer where present; any other typed value is a defect.
- **AC-RS-2 — Query.** `bin/bundle --where k=v [k=v ...]` returns exactly the rows where every named key contains the value; a missing key is a non-match; the result is ordered as G3 states.
- **AC-RS-3 — Keys computed.** `bin/bundle --keys` lists every key in use with its values and counts, computed from the store at invocation; no key list exists anywhere else.
- **AC-RS-4 — Storage boundary.** The processing package imports one row-source interface; the file-backed implementation is the only place that names `rules/`, reads a directory, parses frontmatter, or opens a file; the processing tests construct rows in memory and pass without a filesystem, with one named exception: a guard test over the real `process/named-queries.md`.
- **AC-RS-5 — Intake refusal.** `bin/bundle --near "<text>"` returns the rows whose normalized body scores above threshold against the text; a proposal that scores as a restatement is refused by intake with the existing id, and the refusal is recorded.
- **AC-RS-6 — One command, header, refusal.** One file, the ruled name and directory; the header is the one line G6 states; non-zero exit with a reason on a malformed query, an empty selection, a malformed row, a `--name` that would escape `--out`, or a directory that is not the store, and nothing written.
- **AC-RS-7 — Ruled sets.** The writer, copy-editor, and critic queries return rows whose `source` lies in exactly these files of the old corpus, and no other: for `writer`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `roles/writer.md`, `public-prose-criteria.md`, `voice.md`, `skills/outline.md`; for `copy-editor` and `critic`, the same set less `skills/outline.md` with the role's own document in place of `roles/writer.md`. No writing bundle carries another writing role, the command-blocks skill, or an engineering-only context set.
- **AC-RS-8 — No lifecycle fields.** No file under `rules/` or `process/` carries `status` or `last-reviewed`; `check-frontmatter`, `flip-agreed`, `install-hooks`, `migrate-frontmatter`, and `reviews/expedited-log.md` are absent from the tree; no tool installs a hook into a clone — `--emit` writes hook scripts only under the `--out` it is given.
- **AC-RS-9 — History.** Every row's `source` resolves to a file and line at the named SHA; `docs/history/corpus-<sha>/` holds the old corpus byte-identical to that SHA — the agent-facing in-scope files at that SHA less `skills/directive-invariants.md`, which sits beside it at `docs/history/directive-invariants.md`; the `[human]` files OQ-3 names stay as files; `git log --all` shows no rewritten ref.
- **AC-RS-10 — Retirement.** A retired row lives under `rules/retired/` with `retired:` naming a decision id or a successor row id; a query never returns a retired row; a retired id is never reassigned.
- **AC-RS-11 — Process gate.** Every file under `process/` cites rows by id only; a decision-log entry names each process document's agreed SHA; no process document restates a row's body.
- **AC-RS-12 — Releases.** `bin/release` on a synced clone with `README.md` at the root refuses whole on any failure and otherwise writes one `fiducial-bundle-<slug>.md` per list entry and prints the `gh release create` command naming the tag, the target SHA, `README.md` and every asset; a release carries those files and nothing else.
- **AC-RS-13 — Named queries and sequence.** `process/named-queries.md` is the only place a bundle or the render order is defined; the tool reads both from it; a bundle's rows, process documents and definitions render in the three bands G3 states.

- **AC-RS-14 — Header and staleness.** A bundle's first line is the one-line header of G6; from it alone a consumer with repository access computes commits behind the default branch, and without it the generation time bounds what it knows (J4).
- **AC-RS-15 — Emission.** `bin/bundle --emit <target> --out DIR` writes the target's files under `DIR` and prints each path; `--emit bundle` needs `--where` and writes the file `--where` writes, byte-identical; `--emit claude-code` takes no query; an unknown target, a missing `--out`, a `--name` with a path separator or `..`, or an `EmitError` exits 2 with one line on stderr and nothing written. A harness target never emits the generation timestamp, so its tree is byte-stable across runs over the same store.
- **AC-RS-16 — Emission targets.** The `claude-code` target emits exactly what the design section's emission table states, and refuses (exit 2) when a hook a block names is not a script under `bin/hooks/`; a skill a row names that no process document provides is a note on stderr, not a refusal.
- **AC-RS-16a — Codex target.** `bin/bundle --emit codex --out DIR` writes `AGENTS.md`, one `.codex/agents/<role>.toml` per role in the tier map (and no others), `.agents/skills/<stem>/SKILL.md`, `.codex/hooks.json`, every `bin/hooks/` script byte-for-byte and executable under `.codex/hooks/`, and the `codex-hook` adapter; the tree is byte-identical across runs; the CLI prints exactly the files written; `AGENTS.md` of 32768 bytes is accepted and 32769 refused with exit 2, one line, and nothing written; a hook block naming a script `bin/hooks/` lacks, an agent-scoped block with no role, or an unsupported deny pattern is a refusal; every real `enforce: deny` pattern blocks and harmless calls pass; the intake, decision-log, review-artifact, lane and push-readback hooks behave under the adapter as under the Claude Code target, and malformed patch or hook input fails closed.
- **AC-RS-17 — Enforcement rows.** A row carrying `enforce:` has exactly one of `hook`, `deny`, `agent`, `skill` and its body ends in the fenced yaml block `emit/blocks.py` parses; any other value is a store defect (AC-RS-1).
- **AC-RS-18 — Tier map.** `bin/rulestore/emit/tiers.json` names, for every harness, a model for each of `frontier`, `solid`, `cheap`, and for every role it lists a tier among those three; a file that fails either is refused. Rows speak in tiers and only the emitter names models (R0259, DEC-001270).
- **AC-RS-19 — Adopting-project route.** A project states in one place which bundle its sessions load and at which release, obtained by the same URL as a writer's, and restates no rule. Not yet evidenced in the tree: the route is documented by `README.md`, which package 6b rewrites.

## 7. Design

### Components

- **`bin/bundle`** — the one command. Modes: `--where k=v ...` (one bundle file to `--out`, default `~/Downloads`, named `fiducial-bundle-<name>-<timestamp>Z.md`), `--keys`, `--near "TEXT"`, and `--emit TARGET --out DIR [--where ...] [--name N]`.
- **`bin/rulestore/`** — `store` (row source: the file-backed implementation, the only module that names `rules/`), `query` (selection and the G3 ordering), `render` (the bundle text and header), `terms` (definitions pulled by term), `near` (the shortlist), `keys` (the census), `named_queries` (reads the two sequence blocks of `process/named-queries.md`).
- **`bin/rulestore/emit/`** — the emission targets; see below.
- **`bin/hooks/`** — the hook scripts the `enforce: hook` rows' blocks invoke.
- **`bin/release`** — one bundle per `process/named-queries.md` list entry plus `README.md`, generated at one SHA.
- **`process/named-queries.md`** — the bundle list and the render sequence; the only place either lives.

Interfaces: rows reach the processing code as `rulestore.store.Row` objects only (G7); an emission target receives one `EmitInputs` and returns one `Emission` (files, executable subset, notes) or raises `EmitError`, and touches neither the filesystem nor git.

### Emission targets

The registry is `emit.targets()`; adding a target is the four steps in `emit/__init__.py`'s docstring. Three targets exist: `bundle`, `claude-code` and `codex`.

| Target | Query | Emits |
| --- | --- | --- |
| `bundle` | required | `fiducial-bundle-<name>-<generated>.md`, rendered exactly as `--where` renders it |
| `claude-code` | none | `CLAUDE.md` (the judgment rows of `role=chief-of-staff session=decision` in bundle order, plus the principle prose of the selection's `enforce: hook\|deny` rows, then definitions; rows with `paths:`, `enforce: agent\|skill` rows and process documents are excluded; a row whose first topic names an emitted skill spills to that skill under `## Rules`; over `CLAUDE_MD_LIMIT` lines it warns and still emits); `.claude/rules/<topic>.md` (one per first topic of rows carrying `paths:`); `.claude/agents/<role>.md` (one per role in `tiers["roles"]`: description from the role's `field: description` rows, model from its tier, a shared `tools` list, the skills its `enforce: skill` rows name, its `scope: agent` hooks, body the role's rows minus what `CLAUDE.md` carries); `.claude/skills/<stem>/SKILL.md` (one per process document except `project-setup` and `named-queries`; `gate` carries `disable-model-invocation: true`); `.claude/settings.json` (`permissions.deny` from `enforce: deny` blocks, `hooks` from repo-level `enforce: hook` blocks); `.claude/hooks/<name>` (every script under `bin/hooks/`, executable, block commands rewritten to `"$CLAUDE_PROJECT_DIR"/.claude/hooks/<name>`) |
| `codex` | none | `AGENTS.md` (the standing selection as `CLAUDE.md` has it, refused over `AGENTS_MD_LIMIT` = 32768 bytes); `.codex/agents/<role>.toml` (one per role in `tiers["roles"]`, model from its tier through the `codex` column); `.agents/skills/<stem>/SKILL.md` (one per process document, as for `claude-code`); `.codex/hooks.json` (repo-level `enforce: hook` blocks and each `enforce: deny` block as a `PreToolUse` hook, Codex having no deny rules; agent-scoped hooks are scoped by the runtime `agent_type`); `.codex/hooks/<name>` (every script under `bin/hooks/`, executable, unchanged) and `.codex/hooks/codex-hook` (the adapter that turns `apply_patch` commands into per-file `Write` payloads for those scripts). No `.codex/config.toml`: standalone agents are discovered directly |

Each target reads only its own column of `tiers.json` (`codex`: `gpt-6-astra`, `gpt-6.1-sol`, `gpt-6-luna` for frontier, solid, cheap).

### The hooks

| Script | Event, matcher | Enforces |
| --- | --- | --- |
| `intake-branch-guard` | `PreToolUse` `Edit\|Write` | R0934 (DEC-001320): an edit under `rules/` or `process/` passes only on an `intake/*` branch |
| `decision-log-append-only` | `PreToolUse` `Edit\|Write` | R0583 (DEC-001230): `decisions/log.md` is append-only |
| `review-artifact-immutable` | `PreToolUse` `Edit\|Write` | R1408 (DEC-001230): a landed review artifact is not rewritten |
| `lane-guard` | `PreToolUse` `Edit\|Write`, agent-scoped | R0091, R1156 (DEC-001240): a lane-bound agent edits its lane (`--lane specs\|tests\|reviews`) only |
| `push-readback` | `PostToolUse` `Bash` | R0720 (DEC-001350): after a `git push`, fetch and print the ref's SHA; fail on mismatch |
| `store-lint` | `PostToolUse` `Edit\|Write` | DEC-001250, DEC-001380: `--check citations\|generated-filename\|verdict-lines` (R1605 with R0264's lintable criteria, R0196, R1414) |

Every script reads one JSON object on stdin; exit 0 passes, exit 2 blocks (`PreToolUse`) or reports (`PostToolUse`) with the reason on stderr, and a failure of the script itself is also exit 2. Each imports only `_hooklib.py` beside it and the standard library.

### The tier map

`tiers.json`: `harnesses.<harness>.{frontier,solid,cheap}` model names (`claude-code`: `opus`, `sonnet`, `haiku`) and `roles.<role>` tiers (frontier: architect-agent, spec-reviewer-agent, reviewer-agent, skeptic-risk-agent, context-quality-reviewer; solid: coder-agent, test-designer-agent, release-manager-agent). One file, read by the emitters, never a row.

### The row model
A row is one rule, one file, under `rules/`; the filename is the id. It is `id`, an instruction body, and zero or more key-value pairs — any key, any value. Two keys are fixed because the tool cannot work without them: `id`, and the body. Every value is a list of words, a bare word being a list of one; `id` is text and `order` is a number, and that is the whole type system. Selection is a query over keys: a row matches when every named key holds the value. `topic` carries the grouping the file used to do, and `order` is a row's position within its topic. `source` points at where a row came from. A row with `term` and none of `role`, `session` or `corpus` is a definition (DEC-000420): never selected by a query, carried into a bundle by term. An optional `## Human` section carries rationale and is never rendered to an agent. A row that leaves the store for the harness carries `enforce:` naming the mechanism it becomes — exactly one of `hook`, `deny`, `agent` or `skill` (DEC-001400) — and any other value is a defect; a row without it is a judgment row. A row is one obligation and stands alone; ids are assigned once, never reused, never renumbered; a retired row moves to `rules/retired/` with a `retired:` line naming the decision or the replacing id, and is never deleted.

```
---
id: R0412
role: [chief-of-staff, writer]
session: [decision, execution]
corpus: software
topic: [evidence]
verb: require
condition: null      # or the trigger, plain words
order: 20            # position within the topic; lower first
source: docs/global-context/core.md:24 @ fd54448   # where it came from; null if new
---
Read governed text before emitting anything it governs.

## Human
Why: a session holds nothing but the documents it is given, so they must be right at handoff.
```

### The storage boundary
The store is plainly rows — records selected by key, joined by term, counted, ordered — and a filesystem is an unusual place to keep rows. It is the right place today for reasons that have nothing to do with rows: git gives every row a history, a diff, a pull request and a SHA, so a rule's provenance, its review and its agreement are the repository's own machinery rather than something built; a row is readable and editable with nothing but a text editor; and the tree is what every session and every adopting project already knows how to fetch. Those are the properties the methodology depends on, and none of them is a property of files as storage.

What files are bad at is what a store gets asked to do as it grows: query across hundreds or thousands of rows, hold a second corpus, run the near-duplicate shortlist quickly, answer "which rows changed since this release". At some size that pushes toward a database, and the mistake to avoid is having that move rewrite the logic that selects, orders, renders, retires and checks rows — logic that has nothing to do with where the bytes live. So the two are kept apart from the start: one narrow interface hands out row objects, one storage module owns the traversal, the filenames, the frontmatter and the I/O, and everything that reasons about rules is written and tested against rows built in memory. Substituting the backing store is then one layer's change, made when the tedium is real.

The other half of the ruling is that no database is introduced now to satisfy the abstraction. The boundary buys the option; exercising it early would be infrastructure ahead of need, carrying operational weight — a service to run, a schema to migrate, credentials to hold — for a store that fits in a directory. The goal is substitution, not premature infrastructure.

### External dependencies

Python standard library and git; `origin` for the release's sync check; `gh` for the release command the human runs. No third-party module (AC-X-2 of the test suite).

### Failure modes

The tool refuses over emitting: a malformed query or row; for `bin/release`, an unsynced or dirty tree and an unreachable origin; an empty selection; a `--name` that would escape `--out`; a directory that is not the store; an emission target's `EmitError`. Each is exit 2, one line on stderr, nothing written. A hook that cannot run is exit 2, never a silent pass.

### Deployment assumptions

Deploy and release are separate events: merging to `main` changes the store; a release is cut only on the human's go at one SHA of `main` (J7). A harness tree emitted by `--emit` is committed into the adopting repository and regenerated by the same command.

### User journeys and SLOs

N/A as measured targets: neither source document set an SLO for J1-J7 and the tree measures none. Each journey is therefore named unverified, and the gap is recorded as an open question (section 9). The nearest mechanical evidence: J1 and J7 by the AC-RS-6 and AC-RS-12 refusals under test; J2 by AC-RS-5; J4 by AC-RS-14.

### Verification boundaries

Derived from the tree, not stated by either source document:

| Boundary | Representation | Evidence class | Deferred path |
| --- | --- | --- | --- |
| `origin` (fetch, tag existence) | live in `bin/release` only (`--where` and `--emit` do not touch it); `git` stubbed by local repositories in tests | test with real git against a stand-in remote | none |
| GitHub release creation | assumed: the tool prints the `gh release create` command and the human runs it | none in-tree | the human's read-back of the release |
| Claude Code loading the emitted tree | contract: the emitter's output is tested against the documented file forms | tests over the emission; no in-tree live load | the package 6b self-adoption run |
| Codex loading its tree | contract: emission and hook behaviour tested in a stand-in repository; the tests make no model call and never claim a model honoured an instruction | tests over the emission and the executable hooks; live discovery and trust acceptance reported with the package that landed the target, not in-tree | an adopting repository must trust the project hooks; the 6b self-adoption run |

## 8. Risk tolerance

- **A wrong bundle is worse than none** — a session proceeds confidently on a stale or over-full text. Refusal over emission.
- **The query mechanism, the header and the render order are a public interface**; changing them is consequential and takes the explicit go. Adding a value to a key, or a line to the named-queries list, is routine.
- **Intake is one session's judgment.** Accepted: a bad row lands and is found by use. The mitigation is cheapness — fixing it is one commit, not a cycle — and the intake record, which says who let it in and against what shortlist.
- **The migration wrote hundreds of rows in one directive.** Accepted with a check, met: the row count was read against the clustering pass, every `source` resolves, and a sample was read back against source by the decision session.
- **Files may become tedious.** Accepted; G7 makes the swap one layer.

## 9. Open questions

- **OQ-1 — Named queries.** Resolved: the list, in `process/named-queries.md`, the one place a bundle's definition lives (DEC-000650).
- **OQ-2 — Engagement material.** Resolved: none written as rows now; `engagements/` waits for the next engagement and is written then through intake (DEC-000430).
- **OQ-3 — Human-only documents.** Confirmed: `[human]` files — specs, vendor notes, `README.md` — are not rows and not process; they stay files under `specs/`, `docs/` and the root, agreed by the human and gated by nothing else.
- **OQ-4 — Decision-log numbering.** Confirmed: continues (`process/decision-log.md`).
- **OQ-5 — SLOs.** None of J1-J7 has an SLO, a measurement mechanism or an alerting threshold; each is unverified. Resolved by the human ruling which journeys warrant one.
