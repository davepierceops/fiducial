---
audience: [human]
status: revision 3 — reviewed once (changes-required, all 26 findings disposed), the six rulings owed recorded as DEC-001400–001450; for the human's approval
spec: SPEC.md @ 2c0d491 (DEC-001140)
evidence: docs/research/sort-table-20261103.md @ ea3be2f (DEC-001150)
base: main @ 3c686e0
---

# Plan: the subtraction

Seven packages. Each runs as a subagent — a coder, then a reviewer that did not
write it — in its own worktree (`isolation: worktree`) on its own branch, and
lands as one pull request the human merges. The decision session dictates each
package's intent, acceptance line and blast radius — never ids, orders, counts
or successors, which the subagent derives from the tree and reports (R1606,
R1607). Every claim in a package report carries its evidence class.

Decision-log entries are appended by the decision session at merge, from the
package's report, so concurrent packages never allocate the same id. One
release at the end: main stays releasable throughout because nothing a package
lands is loaded by anyone until package 6 installs the emitted tree in fiducial
and package 5 adopts it elsewhere.

| # | Package | Depends on | Closes |
|---|---|---|---|
| 1a | Store subtraction — the moves | — | — |
| 1b | Store subtraction — the bodies | 1a | — |
| 2 | Process documents | 1b | #389 |
| 3a | Generator: framework, `claude-code` and `bundle` targets | 1b | #358, #366 (partly) |
| 3b | Generator: `codex` target — a Codex session, by execution block | 3a | — |
| 4 | Procedure documents (the skills) | 2 | — |
| 5 | Adopter, and its first run | 3a, 3b, 4 | #359, #360 |
| 6 | Cleanup and self-adoption | 5 | #361, #370, #382 |
| 7 | Close: review, release | 6 | — |

(#383 closed under DEC-001200 on 2026-11-04, before this plan.)

## Environment

What a subagent in this harness can reach, observed in this session: the clone
at `/home/claude/fiducial` with a push credential for `origin`; `gh api` (REST)
against `davepierceops/fiducial`, and against any other repo only after it is
attached to the session with push access; `pip`, `npm` and GitHub. What it
cannot: GitHub GraphQL (`gh pr list`, `gh issue list` fail — use `gh api`),
unauthenticated `api.github.com` (rate-limited on a shared address), arbitrary
web hosts from the shell, the human's machine, and a nested Claude Code
session. Remote git prints `fatal: failed to store: 100001` on stderr; it is
noise, and success is judged by refs read back. Anything that needs the
human's machine — a live `/context` check, an apply — is a command block to
the human with its expected output stated (SPEC.md §4).

## Rulings recorded before 1a dispatches

Six rulings the review surfaced, each the human's, each a DEC entry
(DEC-001400 to DEC-001450, 2026-11-04). Stated here as ruled.

- **R-a (DEC-001400).** `enforce:` takes four values, `hook|deny|agent|skill`;
  SPEC.md §7 is amended to say so.
- **R-b (DEC-001410).** `specs/rule-store.md` and `specs/bundle-system.md`
  reconcile in package 6 into one `specs/rule-store.md` in the spec-template
  form, the generator as its design section.
- **R-c (DEC-001420).** SPEC.md open question 4: the Codex emitter is in this
  revision as package 3b, built by a Codex session handed an execution block,
  and live-verified there.
- **R-d (DEC-001430).** A new row in `core`: on a failure from an external
  system, search current documentation before offering a mechanism from
  memory, and prefer a probe that distinguishes hypotheses over a diagnosis.
  Package 1b lands it.
- **R-e (DEC-001440).** A new row in `review-artifact-schema`: a review
  artifact names every pass that was planned, and a pass that did not run —
  a subagent killed by a usage cap, say — is recorded with why, never read as
  a clean verdict. Package 1b lands it.
- **R-f (DEC-001450).** A review artifact over a delta is named by the delta's
  branch slug. Package 2 applies it to `review-artifact.md`.

## 1a. Store subtraction — the moves

**Intent.** Apply the sort table's mechanical half to `rules/`: every row
sorted `retired` moves to `rules/retired/` with a `retired:` line naming its
successor as the table or its DEC states (where the table and a DEC entry
differ, as on R0489, the DEC governs); every row sorted `harness:*` gains
`enforce: hook|deny|agent|skill` and keeps its body for 1b to rewrite — except
R1408, which is `enforce: hook`, not `deny`, because a path deny cannot tell an
existing `reviews/` file from a new one. A surviving row whose topic's process
document retires is re-topiced: `directive-invariants` survivors to
`chief-of-staff`, `convergence` survivors to `change-flow`, `trd` and
`prd-template` survivors to a new topic `spec`; the subagent reports each
move. The store's schema (`bin/rulestore/keys.py`, `store.py`) admits
`enforce:` and its four values, with tests. SPEC.md §6 item 1 ("every row
carries a recorded sort") is satisfied by the table under DEC-001150; a row
carries a field only when it leaves.

**Acceptance.** `bin/tests/run` green. A reconciliation script, committed under
`bin/tests/`, reads the table and the tree and reports: every in-scope row's
location and `enforce:`/`retired:` state matches its ruled sort; every
out-of-scope row byte-identical to `3c686e0`; no row deleted. The report also
states the post-move row count for the query `role=chief-of-staff
session=decision` (package 3 needs it).

**Blast radius.** `rules/**`, `bin/rulestore/**`, `bin/tests/**`,
`specs/rule-store.md` (the schema paragraph only). Nothing else.

## 1b. Store subtraction — the bodies

**Intent.** The judgment half, read by the reviewer and the human. Every row the
table marks reworded or pruned gets the body its ruling states (DEC-001170
through DEC-001390 name them); each duplicate pair keeps the survivor
DEC-001310 names, merged where the entry says merge; `agree`/`agreed` →
`approve`/`approved` across all surviving rows. Every `enforce: hook` row's
body becomes its fenced block — the event, the matcher, and a command — per
SPEC.md §7; for R0934 and R0720 the prose body is replaced outright
(DEC-001320, DEC-001350). The hook commands follow one convention: the block
invokes `bin/hooks/<name>` (package 3 writes the scripts and the emitter
copies them), so the logic has one home and the row names the check. The
store lint (DEC-001250, DEC-001380) is one script, `bin/hooks/store-lint`,
and R1605, R0196 and R1414 each carry a block invoking it with the check they
name; R0264's four lintable criteria become checks in that script and leave
R0264's body. `enforce: deny` rows carry a fenced block naming the deny
pattern. `enforce: agent` rows carry the field they become (`description` or
`model`); `enforce: skill` rows carry the skill name.

**Acceptance.** `bin/tests/run` green. The reviewer reads every changed body
against the DEC entry that ruled it and reports any divergence; a grep proves
no surviving row body contains `agree`, `directive`, `tranche`, `PRD` or
`TRD` except inside `rules/retired/` and the lexicon rows that define a
surviving term.

**Blast radius.** `rules/**` bodies only; `bin/tests/**` for the grep.

## 2. Process documents

**Intent.** `process/directive-invariants.md`, `decomposition.md` and
`spec-test-suite.md` move to `docs/history/` with a one-line header naming the
DEC entry that retired each. `prd-template.md` and `trd-template.md` fold into
`process/spec-template.md`: the PRD's eight sections plus a design section
carrying what R0863 requires, the standing verification-boundary section, and
the SLO targets for the Top K journeys. `change-flow.md` is rewritten around
the subagent model — spec, plan, build, review, gate, release — at no more than
half its current length, citing no retired row. `retro.md` ends with the retro
landing itself and the synthesis the same way (DEC-001260). `decision-log.md`
states whole-entry supersession and that entries are appended at merge.
`project-setup.md` loses the branch-protection precondition's absolute form
and gains the Free-tier fallback that DEC-001230's Human note states (closes
#389). `named-queries.md` drops the queries for retired topics and adds none.
`review-artifact.md` names an artifact by its delta's branch slug (DEC-001450).

**Acceptance.** No file under `process/` cites a row under `rules/retired/` or
a document under `docs/history/` — a grep proves it. `voice.md` and
`outline.md` byte-identical to `3c686e0`. No process document restates a row
that stays in the store (SPEC.md §4) — the reviewer checks by reading and
names any it finds.

**Blast radius.** `process/**` except `voice.md` and `outline.md`;
`docs/history/**`.

## 3a. Generator: framework, `claude-code` and `bundle` targets

**Intent.** `bin/bundle` keeps its query model and gains `--emit <target>`,
with the target interface written so a further target plugs in as one module
(3b adds `codex`). Two targets here:

- `claude-code`: `CLAUDE.md` from the rows keyed to the chief-of-staff role and
  the decision session — the standing context, nothing the model can read
  from the repo; if the selection exceeds 200 lines the emitter refuses and
  reports the count, and the human decides what spills to `.claude/rules/`.
  `.claude/rules/<topic>.md` for rows carrying `paths:` (the field is
  admitted; none carry it yet). `.claude/agents/<role>.md` with `description:`
  and `model:` from the `enforce: agent` rows, `tools:` from the role's rows,
  `hooks:` in the agent's own frontmatter for its write guards (R0091, R1156 —
  Claude Code scopes frontmatter hooks to that agent; verified 2026-11-04),
  and the role's judgment rows as the body. `.claude/skills/<name>/SKILL.md`
  from every surviving process document except `project-setup.md` (SPEC.md
  §7: one process document, one skill). `.claude/settings.json` with
  `permissions.deny` from the `enforce: deny` blocks and `hooks` from the
  repo-level `enforce: hook` blocks — R0934's hook passes an edit under
  `rules/` or `process/` only on a branch named `intake/*`, which is the
  observable the intake skill provides; R0720's fetches after `git push` and
  prints the remote ref. `bin/hooks/*` scripts are written by this package and
  copied into the emitted tree.
- `bundle`: today's form, unchanged, for the writing roles and Claude chat.

The tier map (frontier / solid / cheap → a model name per harness) is one
file the emitters read, never a row. The `origin/main` sync check is dropped
from ordinary emission (DEC-000940). The two checks meant by "no
contradictions": no emitted file contradicts another, and every path an
emitted file names exists.

**Acceptance.** `bin/tests/run` green, with a fixture for every row carrying
`enforce:` — the twelve hook/deny rows (R0164, R0203, R0564, R0583, R1408,
R0091, R1156, R1605, R0196, R1414, R0934, R0720), the five agent rows, the
skill rows — and a stub process document for the skill emitter. Every hook
and deny, emitted into a stand-in repo, blocks what its row says and nothing
else, exercised by a test. The emitted `CLAUDE.md` is under 200 lines or the
emitter refused. The target interface is documented in the module docstring
well enough that 3b needs nothing from this conversation. The `/context`
live check is not this package's: it is a command block to the human in
package 6.

**Blast radius.** `bin/bundle`, `bin/rulestore/**`, `bin/hooks/**`,
`bin/tests/**`, the tier map file. Does not touch `rules/` or `process/`.

## 3b. Generator: `codex` target

**Intent.** Handed to a Codex session on the human's machine as an execution
block (DEC-001130's secondary path, DEC-001420), written from 3a's landed
interface and self-contained. The `codex` target emits `AGENTS.md` from the
same selection as `CLAUDE.md`, refusing over 32 KiB; `.codex/agents/<role>.toml`
with `developer_instructions` from the role's rows; `.agents/skills/<name>/SKILL.md`
per process document; `.codex/hooks.json` carrying the deny blocks as
`PreToolUse` hooks, since Codex has no deny rules. The Codex session settles
from inside Codex whether an agent's tools or a hook can be scoped per agent;
if not, the agent file's first line says the write guard is advisory there.

**Acceptance.** Live-verified: the Codex session emits into a stand-in repo,
starts itself in it, and reports that `AGENTS.md`, each agent, each skill and
the hooks loaded, with the evidence in its PR. `bin/tests/run` green with the
target's fixtures. A reviewer subagent here reads the PR against 3a's interface
and this section.

**Blast radius.** The `codex` target module, its fixtures and tests. Nothing
else in `bin/`.

## 4. Procedure documents (the skills)

**Intent.** The skills are process documents — one source — and package 3
emits them. This package writes the new ones under `process/`: `gate.md`
(DEC-001280; emitted with `disable-model-invocation: true`), `release.md`
(DEC-001290: its templates and the shared report template), `intake.md`
(DEC-001300: the proposal, the `intake/*` branch the R0934 hook keys on, the
reviewer subagent, the artifact of R0944, the landing), and `build.md`
(R1611's spec read → plan → the plan's reviewer (R0065 widened) → test
designer and coder as separate subagents (R0486) → reviewer and skeptic → the
gate if consequential). `skills/project-status/SKILL.md` moves to
`process/project-status.md`; the `skills/` directory retires.

**Acceptance.** Each document ends with a provenance line citing the DEC
entries and row ids it derives from; its body restates no row that stays in
the store; package 3's emitter, run over the real documents, produces a
`SKILL.md` per document and the reviewer reads each against its DEC entry.

**Blast radius.** `process/**` (new files and `project-status.md` only),
`skills/**` (removed).

## 5. Adopter, and its first run

**Intent.** `process/adopt.md`, emitted as the `adopt` skill: inventory the
target repo's harness files in both layouts (SPEC.md §3.1); emit fiducial's
shapes to a staging directory with package 3's generator; a subagent reads
staging against the repo's files and reports contradictions by file and line;
the human rules; the create step writes missing files and creates the
`human-gate` and four R0030 labels in the target; the append step merges
fiducial's sections under `<!-- fiducial:begin -->` … `<!-- fiducial:end -->`
so a re-run replaces its own section and nothing else; the report is written
to the target under `docs/fiducial-adoption-<timestamp>.md`. Then one real run
against `davepierceops/illuminait` — attached to the session with push access
first — with its contradiction report brought to the human before the append.
That run is the revision's first consequential act and goes through the gate
skill, which is the skill's own first run.

**Acceptance.** On the stand-in repo in tests, a second run makes no diff.
The real run's report is in the Illuminait repo by its own PR and a copy is
under `reviews/` here. The live check — a fresh Claude Code session in that
repo loads the emitted `CLAUDE.md` — is a command block to the human with
the expected `/context` line stated; until he runs it the claim is
contract-verified, labelled so.

**Blast radius.** `process/adopt.md`, `bin/tests/test_adopt*.py`,
`reviews/**`. In the Illuminait repo, by its own PR: `CLAUDE.md`, `AGENTS.md`,
`.claude/**`, `.codex/**`, `.agents/**`, `.fiducial/**` (removed — DEC-000910
superseded), `decisions/log.md` (append: the adoption entry), the adoption
report.

## 6. Cleanup and self-adoption

**Intent.** Remove `bin/directive`, `bin/check-directive`, `bin/land`,
`bin/cycle-open`, and `bin/aimeta/` whole — nothing under `bin/rulestore/`,
`bin/bundle` or `bin/release` imports it (verified in review); the four test
files that do (`test_scope.py`, `test_repo.py`, `test_frontmatter.py`,
`test_check_directive.py`) and their logs go with it. Run the generator
against fiducial itself and commit the result: `CLAUDE.md`, `AGENTS.md`,
`.claude/**` regenerated (the two stale agent files and both placeholder
READMEs replaced), `.codex/**`, `.agents/**`. Archive the root residue to
`docs/history/`: `BACKLOG-v2.md`, `COLLAB-STATE.md`, `MANIFEST.md`,
`MERGE-NOTES-v0.4.md`, `REVIEW-NOTES-v0.2.md`, `REVIEW-NOTES-v0.3.md`,
`REVIEW-v0.4.md`, `OPEN-ITEMS.md`, `ACCEPTED-RISKS.md`, `voice-inbox.md`.
Retire `specs/bin-land*.md` and `specs/directive-tooling*.md` to
`docs/history/` with their DEC pointers; apply R-b to the two live specs.
`bin/release` gains the harness trees as assets if open question 1 resolves
that way (package 7 records it). Rewrite `README.md` for fiducial as it now
is — adopter, skills, two delivery paths — in the adopted vocabulary.

**Acceptance.** `bin/tests/run` green. A grep for each removed tool's name
across `bin/`, `process/`, `README.md` and the emitted tree returns only
`docs/history/` and `decisions/log.md`. Every path the README names exists.
The emitted hooks run in fiducial: an edit under `rules/` off an `intake/*`
branch is blocked, demonstrated in the report. From this merge on, every
change to `rules/` or `process/` goes through the intake skill.

**Blast radius.** `bin/directive`, `bin/check-directive`, `bin/land`,
`bin/cycle-open`, `bin/aimeta/**`, the four tests and logs named,
`bin/release`, `.claude/**`, `.codex/**`, `.agents/**`, `CLAUDE.md`,
`AGENTS.md`, the ten root files named, `docs/history/**`, `README.md`,
`specs/**`.

## 7. Close

**Intent.** The decision session records the open-question DEC entries first:
OQ1 (bundle release or tagged store — answered by what package 5's run
wanted), OQ2 (where chat-Chief-of-Staff loads from), OQ3 (the store as
source, confirmed or revisited), and R-c for OQ4. Then one fresh subagent
that wrote none of the packages reads the whole delta `3c686e0..<tip>`
against SPEC.md §6 item by item and against the sort table, and returns a
review artifact with one verdict per pass (quality, skepticism, continuity).
The decision session triages; the human raises or lets land (DEC-001000);
the human merges. Then the release under the form OQ1's entry states.

**Acceptance.** Every SPEC.md §6 checkbox is checked with a pointer to its
evidence; the review artifact's overall verdict is `ready` or
`ready-with-findings`; every DEC entry owed by packages 1–6 and the four
open questions is in the log.

## Sequencing notes

- 1a and 1b are serial by construction: 1b's diff is prose only, which is what
  the reviewer and the human read; 1a's is proven by the script.
- 2 and 3a both depend on 1b and can run concurrently: disjoint blast radii,
  and DEC entries are appended at merge. 3b runs on the human's machine while
  4 runs here.
- 4 depends on 2 only; 3a's fixture carries a stub document, and 4's
  acceptance runs the real emitter. Critical path: 1a → 1b → 3a → 3b → 5 → 6 → 7.
- 3a is the most code and the only package where a wrong answer is expensive
  and hard to detect: frontier tier for its reviewer.
- 6 is where the R0934 hook starts governing this repo; nothing before it is
  blocked by it, and everything after it goes through intake.
- A package whose subagent dies on the usage cap is resumed, not restarted; a
  review pass that never ran is listed as a gap, not silently absent
  (DEC-001440).

## Review disposition

One read, 2026-11-04 (`/home/claude/sort/plan-review.md`, not committed):
changes-required. Blocking F-1, F-3, F-4, F-10, F-19 fixed above (1b's fenced
blocks and the two prose-free rows; R-b and package 6 for `specs/`; skills as
process documents with one source; `bin/release` owned by 6 with OQ1 recorded
first in 7; the branch-name and agent-frontmatter mechanisms). Non-blocking
F-2, F-5–F-9, F-11–F-18, F-20–F-26 fixed above. The reviewer's answers to the
plan's three questions are adopted: 1a/1b split by kind; the Codex gap stated
in the emitter and labelled in the adopter's report; §6 gaps closed as listed.
