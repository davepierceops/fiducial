---
audience: [human]
---

# PRD: Fiducial as a Rule Store

Supersedes `specs/bundle-system.md` (agreed at 4d6373a6). Drafted 2026-09-04 against `main` at 4a118f5b57f5192a7bb668346f718a5cc188b745; revised 2026-09-07 against `main` at 8d21cd3d52acfd064c98717833397cbcf92c7c17 to state what was built.

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
Trigger: a row landed, was retired, or was re-keyed; or a new project needs its first bundle. Steps: one command names a query; the tool refuses on an unsynced tree; writes one file to `~/Downloads` under the ruled name. Outcome: the bundle is the query's rows in order, then the process documents the query selects, then the definitions the rows use, under a one-line header naming repository, HEAD and generation time (DEC-000630, DEC-000640).

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

### The model
A row is one rule, one file, under `rules/`; the filename is the id. It is `id`, an instruction body, and zero or more key-value pairs — any key, any value. Two keys are fixed because the tool cannot work without them: `id`, and the body. Every value is a list of words, a bare word being a list of one; `id` is text and `order` is a number, and that is the whole type system. Selection is a query over keys: a row matches when every named key holds the value. `topic` carries the grouping the file used to do, and `order` is a row's position within its topic. `source` points at where a row came from. A row with `term` and none of `role`, `session` or `corpus` is a definition (DEC-000420): never selected by a query, carried into a bundle by term. An optional `## Human` section carries rationale and is never rendered to an agent. A row is one obligation and stands alone; ids are assigned once, never reused, never renumbered; a retired row moves to `rules/retired/` with a `retired:` line naming the decision or the replacing id, and is never deleted.

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

### Functional goals
- **G1 — One command.** `bin/bundle --where <query> --name <name>` on a synced clone writes one file to `~/Downloads` named `fiducial-bundle-<name>-<timestamp>Z.md` (DEC-000200, DEC-000290, DEC-000320 filename clause); an unsynced tree is refused.
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
- **G12 — Definitions by term.** A bundle carries every definition a selected row uses, found by term, transitively, rendered last under one heading; a session never needs the store to read its bundle.

### Non-functional goals
Performance: generation in seconds; the shortlist over the store in under 30 s. Reliability: refuse over emit. Scalability: the model holds at a thousand rows and a second corpus by adding a value, not a mechanism. Security: no secret enters a row or a bundle. Maintainability: the tool changes when a new *kind* of thing is needed, never when a new value is. Portability: Python standard library and git; a bundle is Markdown. Compliance: N/A.

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

## 6. Acceptance criteria

- **AC-RS-1 — Row shape.** Every file under `rules/` parses to `id`, a non-empty body, and a dictionary; every value is a list of words after normalization; `order` is an integer where present; any other typed value is a defect.
- **AC-RS-2 — Query.** `bin/bundle --where k=v [k=v ...]` returns exactly the rows where every named key contains the value; a missing key is a non-match; the result is ordered as G3 states.
- **AC-RS-3 — Keys computed.** `bin/bundle --keys` lists every key in use with its values and counts, computed from the store at invocation; no key list exists anywhere else.
- **AC-RS-4 — Storage boundary.** The processing package imports one row-source interface; the file-backed implementation is the only place that names `rules/`, reads a directory, parses frontmatter, or opens a file; the processing tests construct rows in memory and pass without a filesystem, with one named exception: a guard test over the real `process/named-queries.md`.
- **AC-RS-5 — Intake refusal.** `bin/bundle --near "<text>"` returns the rows whose normalized body scores above threshold against the text; a proposal that scores as a restatement is refused by intake with the existing id, and the refusal is recorded.
- **AC-RS-6 — One command, header, refusal.** One file, the ruled name and directory; the header is the one line G6 states; non-zero exit with a reason on an unsynced tree, an unreachable origin, a malformed query, a malformed row, a `--name` that would escape `--out`, or a directory that is not the store, and nothing written.
- **AC-RS-7 — Ruled sets.** The writer, copy-editor, and critic queries return rows whose `source` lies in exactly these files of the old corpus, and no other: for `writer`, `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, `roles/writer.md`, `public-prose-criteria.md`, `voice.md`, `skills/outline.md`; for `copy-editor` and `critic`, the same set less `skills/outline.md` with the role's own document in place of `roles/writer.md`. No writing bundle carries another writing role, the command-blocks skill, or an engineering-only context set.
- **AC-RS-8 — No lifecycle fields.** No file under `rules/` or `process/` carries `status` or `last-reviewed`; `check-frontmatter`, `flip-agreed`, `install-hooks`, `migrate-frontmatter`, and `reviews/expedited-log.md` are absent from the tree; no hook is installed by any tool in the tree.
- **AC-RS-9 — History.** Every row's `source` resolves to a file and line at the named SHA; `docs/history/corpus-<sha>/` holds the 62 files byte-identical to that SHA; `git log --all` shows no rewritten ref.
- **AC-RS-10 — Retirement.** A retired row lives under `rules/retired/` with `retired:` naming a decision id or a successor row id; a query never returns a retired row; a retired id is never reassigned.
- **AC-RS-11 — Process gate.** Every file under `process/` cites rows by id only; a decision-log entry names each process document's agreed SHA; no process document restates a row's body.
- **AC-RS-12 — Releases.** `bin/release` on a synced clone with `README.md` at the root refuses whole on any failure and otherwise writes one `fiducial-bundle-<slug>.md` per list entry and prints the `gh release create` command naming the tag, the target SHA, `README.md` and every asset; a release carries those files and nothing else.
- **AC-RS-13 — Named queries and sequence.** `process/named-queries.md` is the only place a bundle or the render order is defined; the tool reads both from it; a bundle's rows, process documents and definitions render in the three bands G3 states.

## 7. Risk tolerance

- **A wrong bundle is worse than none** — unchanged. Refusal over emission.
- **The query mechanism, the header and the render order are a public interface**; changing them is consequential and takes the explicit go. Adding a value to a key, or a line to the named-queries list, is routine.
- **Intake is one session's judgment.** Accepted: a bad row lands and is found by use. The mitigation is cheapness — fixing it is one commit, not a cycle — and the intake record, which says who let it in and against what shortlist.
- **The migration wrote hundreds of rows in one directive.** Accepted with a check, met: the row count was read against the clustering pass, every `source` resolves, and a sample was read back against source by the decision session.
- **Files may become tedious.** Accepted; G7 makes the swap one layer.

## 8. Open product questions

- **OQ-1 — Named queries.** Resolved: the list, in `process/named-queries.md`, the one place a bundle's definition lives (DEC-000650).
- **OQ-2 — Engagement material.** Resolved: none written as rows now; `engagements/` waits for the next engagement and is written then through intake (DEC-000430).
- **OQ-3 — Human-only documents.** Confirmed: `[human]` files — specs, vendor notes, the voice template, `README.md` — are not rows and not process; they stay files under `specs/`, `docs/` and the root, agreed by the human and gated by nothing else.
- **OQ-4 — Decision-log numbering.** Confirmed: continues (`process/decision-log.md`).
