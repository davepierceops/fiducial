---
review: package 3a — generator framework, claude-code and bundle targets
delta: 19f6760..c859ca7 (branch pkg-3a-generator)
read: 2026-11-04, by a reviewer subagent at the frontier tier that wrote none of it (changes-required), then a re-read at the solid tier over the amendment a1af273..c859ca7 (ready-with-findings); G-1/G-2 docstring fixes applied by the decision session without a further read
---

# Review: package 3a — generator framework, `claude-code` and `bundle` targets

Delta: `origin/main` 19f6760 .. `origin/pkg-3a-generator` a1af273 (four commits).
Read in worktree `/tmp/rev-3a`; `bin/tests/run`: 616 tests, 8 skipped (all pre-existing skips in `test_directive_trd.py` / `test_land.py`), OK. The coder's "610 OK" is a count discrepancy only (observed).
Planned passes: continuity, quality, skepticism. All three ran.

Verdict: changes-required

Two blocking findings (F-1, F-2), both one-line fixes; the rest is non-blocking or a ruling for the human. The architecture is right: targets are one module each, hooks are real scripts tested by subprocess against real git repos, the tier map is the only place a model name lives, `rules/` and `process/` are byte-untouched (`git diff 19f6760 HEAD -- rules process` is empty, observed).

---

## Verdict (continuity): ready-with-findings

### Trace: the 34 `enforce:` rows → emitted objects

Emitted with the limit lifted (`CLAUDE_MD_LIMIT` patched in-process, same as the coder) into `/tmp/rev-3a-emit`; every claim below is observed from that tree unless marked.

| Rows | Block says | Emitted | Match |
|---|---|---|---|
| R0164, R0203, R0564 (deny) | 11 + 14 + 8 `Tool(pattern)` entries | `settings.json` `permissions.deny`, 33 entries, row order, verbatim | yes |
| R0583, R0934, R1408 (hook, PreToolUse, `Edit\|Write`) | `bin/hooks/{decision-log-append-only, intake-branch-guard, review-artifact-immutable}` | `settings.json` `hooks.PreToolUse[0]` matcher `Edit\|Write`, three commands rewritten to `.claude/hooks/<name>` | yes (but see F-1 on the path) |
| R0196, R1605, R1414 (hook, PostToolUse, `Edit\|Write`) | `store-lint --check {generated-filename, citations, verdict-lines}` | `hooks.PostToolUse[0]`, three commands, args preserved | yes |
| R0720 (hook, PostToolUse, `Bash`) | `push-readback` | `hooks.PostToolUse[1]` matcher `Bash` | yes |
| R0091, R1156 (hook, `scope: agent`) | `lane-guard --lane specs` / `--lane tests` | `hooks:` in `architect-agent.md` / `test-designer-agent.md` frontmatter, PreToolUse, `Edit\|Write`; absent from `settings.json`; the "finding, not an edit" sentence is in both bodies (prose of the hook row) and in no other agent | yes |
| R0259 (`field: model`) | — | `model:` on all 8 agent files from `tiers.json` via the claude-code column; R0259's prose appears nowhere | yes |
| R0939, R1031, R1056, R1141 (`field: description`) | — | `description:` of coder, release-manager, reviewer (Human note appended, DEC-001270), test-designer | yes |
| 17 skill rows | `skill: gate\|release\|build\|intake\|[release, review]` | nothing emitted as a row; agent `skills:` lists only skills a document provides; the rest are stderr notes | yes, by design; see F-10 on `review` |

Also observed: the 11 process documents at this HEAD each become `.claude/skills/<stem>/SKILL.md` (`project-setup` and `named-queries` excluded); `gate` would carry `disable-model-invocation: true` (fixture-verified; no `gate.md` exists yet). No row carries `paths:`, so no `.claude/rules/` — correct.

### SPEC.md §7 and the DEC entries

- §7 "refuses a row whose block is missing": `Enforced.__init__` raises `EmitError` (claude_code.py:87); tested.
- DEC-001220 "emits the one-line principle into CLAUDE.md": R0164/R0203 prose is CLAUDE.md lines 3 and 5. The coder generalised this to *every* hook/deny row's prose (R0196, R0564, R0583, R1408, R1414, R1605 all appear in CLAUDE.md). Reasonable derivation, not ruled; costs ~12 lines. Noted under the 200-line escalation.
- DEC-001240: lane hooks in the agent's own frontmatter, finding sentence in the two agent definitions — done.
- DEC-001250/001380: one script, three `--check` names, R0264's four criteria inside `citations` — done (soundness in Quality).
- DEC-001270: tiers → model names in the emitter only; `test_no_row_names_a_model_only_the_map_does` greps the store — done.
- DEC-001320/001350: block-only rows R0934/R0720 render in bundles as their Human note (render.py `row_text`) — see F-6: this is a ruling, not a derivation.
- DEC-000940: `--emit` drops the sync check; `--where` keeps it (tested both ways) — done.
- Plan §3a "harness trees carry no timestamp": confirmed; `generated` is used only by the bundle target. The CLAUDE.md header carries the store HEAD SHA, so a re-run over a *different* store commit changes line 1 even when no row changed. Idempotent over the same store — the claim as stated holds; the adopter (package 5) will see a one-line diff per fiducial commit. Non-finding, worth knowing.

### `--emit bundle` equals `--where`

`--where` refuses in my worktree (detached HEAD is "not synced with origin/main"), so I could not diff the two over the real store from here. `test_emit_bundle_is_byte_identical_to_where_for_a_writing_role` does it in a synced fixture clone through the real CLI, comparing bytes below the header; both paths call the same `render.render`. Contract-verified; I accept it.

What the writer bundle *contains* is a different matter (F-7): every `enforce:` row that has prose still prints its fenced yaml block into the chat bundle — deny patterns, `event:/matcher:/command:`, `field: model`. Issue #399 named only the block-only rows; the orphan-yaml problem it describes applies to all of them.

### The 3b interface (writing `codex.py` from the docstring alone)

The docstring is good on the shape (`EmitInputs` → `Emission`, `takes_query`, `tiers` column, `hooks` map, the four `enforce:` kinds and their block fields). Writing `codex.py` from it, I would be missing:

1. **The standing selection.** "AGENTS.md from the same selection as CLAUDE.md" — the query (`role=chief-of-staff session=decision`, minus `paths:` rows) is `CLAUDE_MD_QUERY` in `claude_code.py`, and step 1 of "ADDING A TARGET" forbids importing from anything but `query`, `terms`, `render`, `blocks`. So 3b must copy it.
2. **Everything else shared**: `Enforced`/`read_enforced` (block reading + refusal), `text_of`/`render_rows` (what a row prints), `first_sentence`, `NOT_A_SKILL`, `NO_MODEL_INVOCATION`, the agent-scoped/repo-level split, the description-plus-Human-note rule, the placeholder description. All live in `claude_code.py` (~150 lines) under the same import ban. 3b either copies them (two sources of truth for what a row prints) or breaks the rule.
3. The signatures of `query.select(rows, where, sequences)`, `query.sort_key(row, sequences)`, `terms.pull_definitions(selected, all_rows)` — named but not shown; 3b reads the modules. Acceptable.
4. `tests.helpers.emit_store_files` does not exist; it is `tests.emit_fixtures.emit_store_files` (docstring line 92, observed).

See F-8 for the fix (a harness-neutral `emit/common.py` the docstring blesses).

### Derived decisions vs rulings

| Coder's decision | Judgment |
|---|---|
| Refusal at 337 lines, escalated | Correct per plan §3a. Recommendation under Skepticism. |
| Role → tier map in `tiers.json`: frontier for architect, spec-reviewer, reviewer, skeptic, context-quality-reviewer; solid for coder, test-designer, release-manager | **A ruling.** R0259 gives the criterion, not the table; the release-manager's ship/no-ship recommendation is arguably a "review gate" (frontier). The human should confirm the eight assignments once; the file is the right home. |
| Agent file iff the role has a tier | Derivation, sound (chat roles get bundles, not agents). |
| `tools:` by slug: reviewer/skeptic → Read, Grep, Glob; others get Edit, Write, Bash | **A ruling**, and the coder's own concern. No row or DEC says a reviewer is read-only. Recommendation under Skepticism. |
| Agent bodies = all of the role's rows | Derivation from DEC-001270 "judgment rules ... emitted into the agent file's body", but the result duplicates CLAUDE.md ~80% per agent (F-4). |
| Placeholder description for roles with no description row | Derivation; note the four frontier roles (architect, spec-reviewer, skeptic, context-quality-reviewer) all get the placeholder, which is what Claude Code uses to route delegation (F-9). |
| `named-queries.md` not a skill | Derivation; sound (it is the generator's own input). Plan said only `project-setup`; one-line note in the report is enough. |
| Hook commands relative `.claude/hooks/<name>` | Derivation; wrong against the harness facts (F-1). |
| Block-only hook rows render their Human note in bundles | **A ruling.** It breaks the bundle contract "no `## Human` content anywhere" (render.py's own docstring before this delta; S2 of the bundle-tool skeptic read). #399 offered two options; the coder took the one that changes a standing invariant for every bundle, not the one that doesn't (F-6). |
| `PATH_EXEMPT` list and the path heuristic | Derivation; the heuristic is unsound in the direction that matters (F-5). |
| Lane-guard test-path patterns | Derivation; fine. |

---

## Verdict (quality): changes-required

### Hook scripts, both directions

Probed by subprocess with hand-built JSON in a scratch repo (`/tmp/rev-probe`), in addition to the suite. Observed:

- **intake-branch-guard**: blocks `rules/**` and `process/**` (including `rules/retired/`) off `intake/*`; passes on `intake/x`; a branch named `intake` (no slash) and `intake-foo` are both blocked — correct, the row says `intake/*`. Relative `file_path` resolves against the hook's `cwd`; tested. Bash writes (`sed -i`, `git mv`) bypass it — inherent to "matches the tool call", stated in the row.
- **lane-guard**: `specs` admits exactly `SPEC.md` and `specs/**` (matches R0091's Human note); `tests` admits the usual test trees. A path with spaces is handled. A file outside any git repo gets the absolute path matched against the patterns — conservative, blocks; fine.
- **review-artifact-immutable**: blocks a write to a `reviews/` file tracked at HEAD, passes an untracked one, passes a brand-new file under `reviews/`. Matches the block's comment exactly. Workflow note (F-11): "tracked at HEAD" means a reviewer who commits a draft and then re-reads is blocked from amending it on their own branch; `reviews/pkg-1a-...md` carries two overall `Verdict:` lines precisely because a re-read amended it.
- **decision-log-append-only**: an append passes (Write and Edit forms); a Write that changes or drops an entry is blocked; an Edit in the middle is blocked; an append that also fixes a typo in the last entry is blocked ("new_string does not begin with old_string") — correct per R0583, and this is the "R0583 edit-of-last-entry" concern: the hook is right, the workflow has to accept it (a typo in a landed entry is a new entry with `Supersedes:`). A prepend disguised as an edit of the first entry is blocked. The uniqueness check at line 54 is redundant with the Edit tool's own uniqueness rule; harmless.
- **push-readback**: landed push passes and prints the SHA; a push the remote did not take fails loudly; multiple refspecs each read back; `HEAD:refs/heads/x` resolves; `-u`/`2>&1 | grep` handled; `--delete` skipped. Two gaps:
  - `git -C <dir> push ...` is **not detected** (exit 0, nothing printed — observed). `PUSH_RE` requires `git` immediately followed by `push`. This is the form the plan's own environment section and the subagent briefs use (`git -C /home/claude/fiducial ...`), so the hook would silently miss the pushes this repo actually makes. F-2.
  - `git push origin HEAD` fails loudly with "couldn't find remote ref HEAD" (observed): `dst` should resolve `HEAD` to the current branch. Loud, not silent, so non-blocking (F-12).
  - A push with no upstream and no refspec: `git push` itself fails; the hook then fetches `origin <branch>`, which fails if the branch is not on the remote → loud failure. Fine.
- **store-lint**:
  - `generated-filename`: new file under `retros/`/`reviews/` without `YYYYMMDDTHHMMSSZ` fails; tracked files pass whatever their name. Correct per R0196's note.
  - `verdict-lines`: the enum is hard-coded as three values (store-lint:35). The ruling that arrived mid-review adds `not-run` between `ready-with-findings` and `changes-required`; package 2 is editing R1414. As it stands the hook will reject every artifact that uses the new value, and the index-based severity ordering must place `not-run` third. F-3. Run over the real `reviews/`: the 11 most recent artifacts pass except `pkg-1a-store-moves-read-20261104T185942Z.md` (two overall `Verdict:` lines — the re-read pattern, F-11) and `ac-rs-8-9-read-...` (three). All pre-schema `*-cycle-N.md` artifacts fail, as expected and as R1408 permits.
  - `citations` over all 384 rows under `rules/`: **zero failures**. Too clean: `PATH_RE`'s lookbehind `(?<![\w/`.])` excludes a backtick, so any path written as `` `src/main.py` `` — which is how rows write paths — is never seen. Only two bare path tokens exist in the whole store (both `decisions/log.md`, exempt). The test case uses a bare `src/main.py`, so the suite does not notice. F-5. The other three R0264 criteria are carried (key-value vocabulary, role⇒session, model names); `MODEL_NAME_RE` includes `sonnet`, which will fire on a writing-corpus row about the poetic form — unlikely, noted.
  - Partial-write concern (#399): `verdict-lines` is PostToolUse and exit 2 only feeds stderr to the model; a reviewer drafting an artifact in pieces gets a lint complaint per piece until the verdict lines exist. Not blocking the write, just noise. A `Stop` hook would be quieter; the human's call, no finding.

### Tests

Real: `test_hooks.py` runs each script as a subprocess from a *copied* hooks directory, with JSON on stdin, against a real `git init` repo with a bare origin for push-readback; no mocking of git or of the scripts. `test_emit_*` run `bin/bundle` through the CLI against a fixture store repo and also exercise the real store (`TestClaudeCodeOverTheRealStore` accepts either under-limit or a refusal with the count). Gaps the suite does not cover: `git -C`, `git push origin HEAD`, backticked paths in the citations lint, the agent-body/CLAUDE.md overlap, and anything about whether Claude Code actually parses the emitted frontmatter (Skepticism).

### Single source for model names

Yes. `tiers.json` only; `test_emit_tiers.py` greps every row body for `opus|sonnet|haiku` and the emitter never reads the codex column.

### Hard-coded things that belong elsewhere

- `READ_ONLY_MARKERS`/`READ_ONLY_TOOLS`/`WRITING_TOOLS` (claude_code.py:57-59): a policy with no row behind it (escalation 2).
- `tiers.json` `roles`: a policy table, correctly in the map, but unruled.
- `"Fiducial's %s role."` placeholder (claude_code.py:371).
- `PATH_EXEMPT` (store-lint:46): the exemptions #399 asked for; a list, fine, but `docs/`, `specs/`, `rules/`, `process/` as *prefixes* exempt entire trees — once F-5 is fixed this list will be what decides, so the human may want to see it.
- `LANES["tests"]` (lane-guard:17): a heuristic over an adopter's layout; acceptable in the script.

---

## Verdict (skepticism): changes-required

### CLAUDE.md as the model would read it (337 lines)

Composition, observed: 131 one-line rows, each followed by a blank line (262 lines), 36 definitions at two lines each (72), header and `## Definitions` (3). Nothing in it is multi-line prose; the count is separators and definitions. By topic: core 29, decision-layer 16, change-control 11, command-blocks 11, verification 11, verification-boundaries 9, lexicon 9, chief-of-staff 9, change-flow 8, review-artifact-schema 7, retro 5, decision-log-policy 3, remote-write 3, commit-control 2, and singletons.

What the model could read from the repo instead (SPEC.md §4 usability goal), for *fiducial itself*: the 36 definitions (lexicon rows), and every topic whose process document is emitted as a skill — retro, review-artifact-schema, decision-log-policy, change-flow, and after package 4 change-control (gate), intake, release. For an *adopter* the repo has no store, but it does have those skills. Lines that are plainly wrong in CLAUDE.md: "Run the Critic at the frontier tier", "Run the Writer at the frontier tier" (R1029, R1176; CLAUDE.md:79-81) — operator instructions for chat roles.

Measured options (counts from the real store):

| Rule | Lines |
|---|---|
| As emitted | 337 |
| A. Render rows as a list, no blank separator between rows | 207 |
| B. A topic whose process document is a skill spills out of CLAUDE.md into that `SKILL.md` (rows appended below the document, one source still — the emitter does the appending) | 274 (172 with A) |
| C. B + drop the chat-role tier rows + spill `verification` and `verification-boundaries` (the reviewer/test-designer rows; the chief of staff meets them at the gate, where the gate skill can carry them) | 222 (143 with A) |

**Recommendation for the human's ruling:** A is a format change and reaches 207 on its own — but it is close to the limit and makes the limit a formatting artefact; rule on whether the 200 lines means lines or volume. The content rule I would propose is B: *"a row whose topic names an emitted skill is read when the skill is invoked, not standing; the emitter appends those rows to the skill's `SKILL.md` under a `## Rules` heading."* It is derivable from the tree (topic → process document → skill), needs no `paths:` on any row, keeps one source, and after package 4 lands gate/intake/release it removes the change-control and intake rows too. `.claude/rules/<topic>.md` without `paths:` is loaded unconditionally by Claude Code, so spilling there changes the line count and not the context — I would not use it for this. Option C's verification spill is a judgment the human should make: those rows bind the chief of staff at release, and a reviewer that cannot see them in CLAUDE.md sees them in its agent file.

Recorded so it isn't lost: the R0259-family "Run at the solid general-purpose model tier" line (CLAUDE.md:77) is the chief of staff's own tier row; harmless, but the model cannot act on it.

### Each agent file, as that agent

- **architect-agent**: would know its lane (hook + sentence) and its model; would not know what an architect *does* — description is the placeholder, and the body opens with twelve-role rows about secrets and production. The role-specific rows arrive after ~90 lines that are already in CLAUDE.md (observed: 91 of 110 non-blank body lines duplicate CLAUDE.md). Same shape for every agent: 85–105 duplicated lines each (F-4).
- **reviewer-agent**: description is R1056's prohibition plus its Human note; a routing description that says only what not to do. Body 165 lines, 105 duplicated. Tools: cannot run `bin/tests/run`, cannot write `reviews/<slug>-<ts>.md` — yet R1414 and R1408 in its own body tell it how to write one.
- **skeptic-risk-agent, spec-reviewer-agent, context-quality-reviewer**: placeholder descriptions; same tools problem.
- **coder-agent / test-designer-agent**: fine; the test-designer's lane hook and sentence are present. No `skills:` yet (build does not exist); the stderr note says so.
- **release-manager-agent**: fine as a writing role; its `gate`, `release`, `review` skills are notes until package 4.

### The reviewer `tools:` problem

Facts: no row says a reviewer is read-only; R1408/R1414/R1605/R0196 all presume the reviewer writes an artifact under `reviews/`; this package's own acceptance has the reviewer run `bin/tests/run`; a review that cannot run the tests it is judging is weaker evidence than one that can (R0074 territory).

**Recommendation:** give every agent the same tool list and enforce the reviewer's lane the way R0091/R1156 already enforce the architect's and test-designer's: a `scope: agent` PreToolUse hook `lane-guard --lane reviews` (admits `reviews/**` only) on the four reviewer roles, carried as a row with `enforce: hook` through intake, so the policy lives in the store, not in `READ_ONLY_MARKERS`. Bash stays so the reviewer can run tests; the known caveat (Bash can write files) is the same one every hook here already accepts. A `disallowedTools: [Edit]` would additionally stop in-place edits but not a `Write` of a tracked file, which R1408's hook already stops; I would not add it. The alternative — the caller writes the artifact from the reviewer's report — makes the artifact a copy made by the party being reviewed, which R0065/R0462 argue against. Until the row exists, the smallest 3a-local change is `tools_for` returning `WRITING_TOOLS` for everyone and a note in the report; the human rules.

### settings.json in this repo's own workflow

- `pkg-*` branches editing `bin/`, `docs/plans/`, `reviews/`: not governed by intake-branch-guard — pass. A package that *does* touch `rules/` or `process/` (1a, 1b, 2, 4) would be blocked after package 6 installs the tree; the plan says so (§6 acceptance) and 2 and 4 land before 6. Consistent.
- A new review artifact `reviews/<slug>-<ts>.md`: immutable-guard passes (untracked); generated-filename passes (timestamp); verdict-lines complains until the verdict lines exist (noise), passes after.
- A DEC append at merge: passes in both tool forms. A fix to a landed entry: blocked, by design.
- Hook commands as emitted (`.claude/hooks/x`): they fire only if the session's cwd is the repo root; from a subdirectory the command is not found, the hook exits non-2, and Claude Code treats that as a non-blocking error — i.e. the guard silently does not guard. That is the worst failure mode available here, and no test can see it (F-1).
- `git -C` pushes: no readback (F-2), silent.

### What would make this delta wrong that no test catches

1. Claude Code's frontmatter parser rejecting `tools: [Read, Grep, Glob]` (the docs' examples use a comma-separated string) or the nested `hooks:` mapping in agent frontmatter — every agent file would then load without tools or without its lane guard, silently. Contract-verified against the coder's reading of the docs only; the package 6 live check is where this is proven. Label it so in the report.
2. The relative hook path (F-1) — same silent mode.
3. The citations lint passing everything (F-5) — the store's new rows go unlinted and the green looks like compliance.
4. The verdict enum (F-3) — the first artifact to use `not-run` is rejected by the lint the human just ruled it into.
5. The Human-note substitution in `render.py` (F-6): bundles that the bundle-tool tests certified as "no `## Human` content" now carry it for two rows; no existing test asserts the old invariant over those rows.

---

## Findings

- **F-1 (blocking)** `bin/rulestore/emit/claude_code.py:53,123` — hook commands are emitted as `.claude/hooks/<name>`, relative to the session's cwd. Claude Code sets `$CLAUDE_PROJECT_DIR` for hook commands and a session started in a subdirectory would not find the script; a not-found command is a non-blocking hook error, so the guard silently stops guarding. Fix: `HOOKS_DIR = '"$CLAUDE_PROJECT_DIR"/.claude/hooks'` in the emitted command (keep the file path `.claude/hooks/<name>` for the copy), and assert the prefix in `test_settings_hooks_carry_the_repo_level_hook_rows...`. Inferred from the harness facts given; not live-run.
- **F-2 (blocking)** `bin/hooks/push-readback:15` — `PUSH_RE` requires `git` directly before `push`; `git -C /path push origin x` (and `git --git-dir=... push`) passes silently with no readback (observed). Fix: `r"(^|[;&|]\s*|\s)git(\s+(-C\s+\S+|--\S+|-\S))*\s+push(\s|$)"`, and take the `-C` value as the repo root when present; add the test case.
- **F-3 (blocking, given the ruling that arrived)** `bin/hooks/store-lint:35` — `VERDICTS` has three values; R1414 now takes four with `not-run` between `ready-with-findings` and `changes-required`. Fix: `VERDICTS = ("ready", "ready-with-findings", "not-run", "changes-required")`; the index ordering then gives the right "most severe". Add a test that an overall `not-run` over passes `[ready, not-run]` passes and `ready-with-findings` over `[not-run]` fails. Coordinate with package 2's row edit so the hook and the row land with the same enum.
- **F-4 (non-blocking)** `claude_code.py:353-390` — each agent body carries every row of the role, 85–105 lines of which are the CLAUDE.md selection the subagent also loads (observed via line-set intersection). Fix: subtract the standing selection (`standing`) from `own` before rendering, and say so in the module docstring; agent files drop to roughly 20–60 lines of role-specific rows.
- **F-5 (non-blocking)** `bin/hooks/store-lint:52-55` — `PATH_RE`'s lookbehind/lookahead exclude a backtick, so backticked paths — the store's convention — are never matched; the check passes all 384 rows and the only tokens it sees are two bare `decisions/log.md`. Fix: drop the backtick from both assertions (or strip backticks before matching) and re-run over the store to size `PATH_EXEMPT` honestly; add a test with a backticked path.
- **F-6 (non-blocking; ruling)** `bin/rulestore/render.py:22-34` — block-only hook rows print their `## Human` note into every bundle, ending the "no `## Human` content anywhere" contract that the bundle-tool reads certified. #399 offered "render as Human note, or skip"; skipping keeps the contract. Recommend: print nothing for a block-only row (or print `prose` only for every `enforce:` row, which also fixes F-7), and record whichever the human picks as a DEC entry since it amends a landed contract.
- **F-7 (non-blocking)** `bin/rulestore/emit/bundle.py` / `render.py` — `enforce:` rows with prose print their fenced block into the chat bundle (deny patterns, `event:/matcher:/command:`, `field: model` — observed in the writer bundle). Fix: in `row_text`, for any row with `enforce:`, return `blocks.parse(row.body)[1]` (the prose), falling back to nothing.
- **F-8 (non-blocking)** `bin/rulestore/emit/__init__.py:85-88` and `claude_code.py` — the pieces every harness target needs (`CLAUDE_MD_QUERY`, `Enforced`, `read_enforced`, `text_of`, `render_rows`, `first_sentence`, `NOT_A_SKILL`, `NO_MODEL_INVOCATION`) live in `claude_code.py`, which the docstring forbids 3b to import. Fix: move them to `emit/common.py`, name it in the import allow-list, and point `claude_code.py` at it. Also docstring line 92: `tests.helpers.emit_store_files` → `tests.emit_fixtures.emit_store_files`.
- **F-9 (non-blocking)** `claude_code.py:371` — four of eight agents (architect, spec-reviewer, skeptic-risk, context-quality-reviewer) get `description: Fiducial's <role> role.`; Claude Code routes delegation on this field. Not 3a's to invent; carry to the human as "four roles have no `field: description` row" — the fix is four rows through intake.
- **F-10 (non-blocking; not 3a's)** R0506's block names skill `review`; no process document is or is planned to be `review.md` (`review-artifact.md` is the stem the emitter would produce), so the note "names skill 'review'; no process document provides it" is permanent. Carry to package 4 or an intake row fix.
- **F-11 (non-blocking; workflow)** `bin/hooks/review-artifact-immutable` — "tracked at HEAD" blocks a reviewer amending its own committed draft on its own branch (the re-read pattern that produced `reviews/pkg-1a-...`'s second `Verdict:` line, which `verdict-lines` also rejects). The hook matches its row; the row's observable may be the wrong one (tracked on the default branch, or in `merge-base`, would fit the intent "already landed"). A ruling, through intake, not a 3a change.
- **F-12 (non-blocking)** `bin/hooks/push-readback:69-75` — `git push origin HEAD` reads back remote `HEAD` and fails loudly. Fix: when `dst == "HEAD"`, use `current_branch(root)`.
- **F-13 (non-blocking)** `claude_code.py:376` — `tools:` emitted as a YAML flow list; the harness docs' examples show a comma-separated string. Cannot verify from here; label the agent files contract-verified and make the package 6 live check cover one agent's tool list and one agent's frontmatter hook.

## The two escalations

1. **337 lines.** Refusal is correct and the count is honest. Rule on (a) whether the limit is lines or volume — if lines, rendering rows as a list (option A) reaches 207 by format alone; (b) the content rule — I recommend B, "a topic with an emitted skill spills into that skill," derivable from the tree and self-correcting as package 4 lands more skills; with A it gives 172 today; (c) separately, drop the chat-role tier rows (R1029, R1176, and the chief of staff's own R0262-family line) from the standing context. `.claude/rules/` without `paths:` does not reduce context, only the file's line count; I would not use it for this.
2. **Reviewer tools.** Same tools for every agent; the reviewer's lane enforced like the architect's — a `scope: agent` `lane-guard --lane reviews` row on the four reviewer roles through intake. Bash stays for tests. This also removes `READ_ONLY_MARKERS` from the emitter, which is where a policy should not live.

---

File: `/home/claude/sort/review-3a.md`

Verdict: changes-required
Verdict (continuity): ready-with-findings
Verdict (quality): changes-required
Verdict (skepticism): changes-required

## Re-read over a1af273..c859ca7

Worktree `/tmp/rev-3a2` (removed after); `bin/tests/run`: 635 tests, OK, skipped=8 (observed). Diff touches only `bin/` (13 files; nothing outside, observed).

Verdict: ready-with-findings

Fixes confirmed by running them (observed unless marked):
- F-1: settings.json and agent `hooks:` commands are `"$CLAUDE_PROJECT_DIR"/.claude/hooks/<name> [args]` for all 7 repo-level and both lane hooks; scripts emitted mode 755.
- F-2/F-12: push-readback against a temp bare repo (hook run by hand, JSON on stdin). Landed pushes read back and exit 0 for `git -C <dir> push origin main` (cwd `/`), `git push origin HEAD`, bare `git push` (upstream set), and `git -C work push origin HEAD` from the parent dir. Rejected push (remote moved): `git push origin HEAD` and `git -C <dir> push` both exit 2 naming the remote SHA vs local. A non-push command passes. `-c k=v` and `--git-dir`-style flags handled by the regex (inferred from the diff).
- F-3: `not-run` accepted at rank 3. Overall `not-run` over [ready, not-run] passes; `ready-with-findings` over a `not-run` pass fails; `changes-required` over a `not-run` pass fails; `not-run` over a `changes-required` pass fails; each with the "most severe" message.
- F-5: backtick dropped from the lookbehind. A scratch row with `` `src/main.py` ``, `` `src/a/b.py` `` and bare `src/x.py` fails on all three. Over all 384 real rows: zero failures, now meaningful (backticked tokens are seen; the only ones in the store are `reviews/`, `decisions/log.md`, `rules/`, `specs/`, `retros/`, `process/`, all exempt).
- F-11: `on_default_branch`. Landed file on origin/main blocks; draft committed on a branch passes; new file passes; with no origin/main, local `main` governs; with neither, falls back to tracked-at-HEAD (blocks both). Correct.
- Rulings: CLAUDE.md is 289 lines, blank lines kept, stderr `warning: CLAUDE.md is 289 lines, over the 200-line guidance; emitted anyway` (no `note:` prefix, bin/bundle:260), exit 0. The four spilled topics (change-flow, decision-log, retro, review-artifact) carry 23 distinct rule lines under `## Rules` in their SKILL.md; 0 of them in CLAUDE.md. All 8 agents: `tools: [Read, Grep, Glob, Edit, Write, Bash]`; `hooks:` only in architect (`--lane specs`) and test-designer (`--lane tests`); `--lane reviews` exists in lane-guard (`^reviews/`) with no row yet (as intended). F-6/F-7: bundle `row_text` now prints prose-only for any `enforce:` row, nothing for block-only, no Human anywhere.

Findings:
- G-1 (non-blocking, 3b) `bin/rulestore/emit/claude_code.py:~125-137`: the spill grouping itself (standing rows -> `topic_stem(first topic, stems)` with `stems` = `sequences[1]` filtered to emitted documents) is inline in `ClaudeCodeTarget.emit`, and the "warning:" note-prefix convention (bin/bundle:260) and the agent-body subtraction are in neither `emit/__init__.py` nor `common.py`. A 3b author can write the target from the docstring plus `common.py` except for the spill: AGENTS.md has no skills to spill into, so for codex the question is whether the rows stay in AGENTS.md; that is undocumented. Smallest fix: add `common.split_standing(standing, documents, sequences) -> (kept, {stem: rows})` and two docstring lines (notes beginning `warning:` print without `note:`; a harness with no skill directory keeps spilled rows standing, or state the ruling). Observed (docstring and common.py read) / inferred (what 3b needs).
- G-2 (nit) `emit/__init__.py` docstring says only `project-setup` is not a skill; `common.NOT_A_SKILL` also has `named-queries`. One-line fix.

Not re-checked: F-9, F-10, F-13 (deliberately untouched). F-13 stays a package 6 live check.

File: /home/claude/sort/review-3a.md
