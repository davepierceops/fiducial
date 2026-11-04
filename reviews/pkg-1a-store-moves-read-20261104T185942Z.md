---
review: package 1a — store subtraction, the moves
delta: 28366d4..27845c3 (branch pkg-1a-store-moves)
read: 2026-11-04, by a reviewer subagent that wrote none of it; first read over 28366d4..96f320e, re-read over 96f320e..27845c3
---

# Review: package 1a — store subtraction, the moves

Delta: `origin/main` (28366d4) .. `origin/pkg-1a-store-moves` (96f320e), two commits (7d23929 schema + reconcile script; 96f320e the moves).
Governing texts read: plan §1a, `docs/research/sort-table-20261103.md` (per-topic tables), `decisions/log.md` DEC-001150–DEC-001450 (DEC-001460 does not exist in the log).
Ruler: my own re-derivation script (`/tmp/rev-1a-check.py`, throwaway), not the coder's `reconcile_sort.py`; the coder's script was read and run separately for the Quality pass.

Verdict: changes-required

Passes planned: Continuity, Quality, Skepticism. All three ran.

## Verdict (Continuity): changes-required

What I re-derived (observed, from the table's per-topic sections plus the DECs, independently of the coder's script):

- Expected sort per row: table sort, overridden by DEC-001310 on ten rows (R0022–R0026, R0113, R1602, R1153, R1543, R0489 → retired) and by DEC-001230 + plan §1a on R1408 (→ hook). I asserted 110 other DEC-named rows agree with the table before trusting it; all do.
- Tree state matches expectation for all 461 table rows and all 465 base row files: 75 retired, 34 `enforce:` (hook 9, deny 3, agent 5, skill 17), 20 re-topiced, 229 stays byte-identical, 103 out-of-scope byte-identical, 4 pre-retired rows untouched, 0 deleted, 0 ids in both `rules/` and `rules/retired/`, 0 new ids. Every number in the coder's report reproduces. 65 table-retired + 10 DEC-retired = 75.
- `git diff --name-status -M` shows 75 renames (similarity ≥ 92%) and 54 modifications, no `D`, no `A`. `rules/` at the plan's base 3c686e0 is byte-identical to 28366d4 (`git diff --stat 3c686e0..28366d4 -- rules` is empty), so the acceptance line's base and the review's base are the same tree.
- Bodies: every surviving and retired row's body is byte-identical to base. Frontmatter: every row is reconstructible byte-exact from base by removing the one `enforce:`/`retired:` line and/or substituting the `topic:`/`order:` lines; no other key changed on any row.
- Re-topic: applied to exactly the 20 surviving rows whose base topic is `directive-invariants`, `convergence`, `trd` or `prd-template` (the 11/7/2 the coder lists). No harness row sits in a retiring topic, so none needed it. Retired rows keep their old topic (correct: they are out of the store). Orders: appended after each receiving topic's max in steps of 10 (change-flow 280–340, chief-of-staff 530–540), `spec` numbered 10–110 preserving `trd` relative order then `prd-template`; no order collision in any topic; the store's dominant step is 10 (290 of 355 adjacent pairs). Convention followed.
- Successors: every `retired:` value is what the table note names, or the DEC where the two differ (R0489→R1031, R1296→worktrees, R1491→none, R1246→none, R0872/R1541/R0046/R0871→spec-template.md, R0474→subagents). No value contradicts a DEC. Placement of the new line (after `id:`) matches the four pre-existing retired rows.
- Blast radius: `git diff --stat 28366d4..96f320e -- . ':!rules'` touches only `bin/rulestore/store.py`, `bin/tests/reconcile_sort.py`, `bin/tests/test_rulestore.py`, `bin/tests/test_rulestore_store.py`, `specs/rule-store.md` (one sentence in §4). Nothing else.
- The two deferred merges (R1533+R0472+R0759; R1513+R1542) are correctly left as `stays`: DEC-001310 names no survivor. R1513, R1533, R1542 are re-topiced to `spec`; R0472 and R0759 stay where they were.

### F-1 (blocking, observed) — 56 of 75 `retired:` values are neither a decision id nor a row id, against the spec sentence this delta edits

`specs/rule-store.md` §4 (the sentence the coder amended in 7d23929) says a retired row carries "a `retired:` line naming the decision or the replacing id"; AC-RS-10 in the same file says "`retired:` naming a decision id or a successor row id"; the coder's own new test is named `test_ac_rs_10_…`. The four pre-existing retired rows all name a row id. This delta lands:

| value | rows |
|---|---|
| `none` | 32 (R0003 R0008 R0012 R0013 R0054 R0058 R0202 R1246 R1286 R1287 R1290 R1291 R1292 R1293 R1302 R1304 R1305 R1306 R1307 R1308 R1310 R1311 R1313 R1314 R1340 R1341 R1344 R1347 R1350 R1491 R1613 R1615) |
| `process/spec-template.md` | 7 (R0046 R0561 R0757 R0758 R0871 R0872 R1541) |
| `subagents` | 6 (R0474 R0896 R1106 R1395a R1395b R1476) |
| `SPEC.md` | 2 (R0085 R0470) |
| `command-blocks` | 2 (R0256 R0060) |
| `harness-managed subagent worktrees` | 2 (R1295 R1296) |
| `PreToolUse path guard` / `… allow-list` | 2 (R1288 R1289) |
| `subagents and --resume` | 1 (R1608) |
| mixed list with a non-id | 2 (R0212 `[R0208, SPEC.md]`, R1126 `[SPEC.md, R0083, R1396]`) |

The values are faithful to the table/DEC wording (plan §1a: "naming its successor as the table or its DEC states"), so this is not a wrong ruling applied; it is the plan's wording and the spec's form disagreeing, and the delta resolving it silently in the plan's favour while leaving the spec sentence claiming otherwise. Nothing executes on it today (`FileRowSource` never reads `rules/retired/`), but the store's own AC is now false for 56 files and the delta is the one that made it so.

Smallest fix, no ruling needed: every one of the 56 has a governing DEC, so name it — `none` rows → the DEC that retired them (DEC-001160 for the class-1 rows, DEC-001200 for R0003/R0008/R0012/R0013/R1491, DEC-001330 R0202, DEC-001370 R0054, DEC-001260 R1246/R1613, DEC-001160 R0058); `subagents` → DEC-001180; spec-template rows → DEC-001210; `SPEC.md`/R0085/R0470 → DEC-001190; command-blocks pair → DEC-001160; worktrees pair → DEC-001170; R1288/R1289/R1608 → DEC-001160; R0212 → `[R0208, DEC-001160]`, R1126 → `[R0083, R1396, DEC-001190]`. Where the table names a row id beside the free text (R0474 → R0007 per table; the DEC says only "subagents"), either form satisfies the spec. Update `RETIRED_SUCCESSOR` in `reconcile_sort.py` to match. This satisfies the plan ("as … its DEC states"), the §4 sentence and AC-RS-10 at once. The alternative — a ruling amending AC-RS-10 and §4 to admit free text — is the human's call and outside 1a's blast radius ("the schema paragraph only"), so I do not recommend it here.

### F-2 (non-blocking, inferred) — class-4 successors are per-row table notes, not the DEC's class-level successor

DEC-001190 names one successor for all eight class-4 rows ("SPEC.md's definition of done, the red gate and plan mode"); the delta gives each its table note instead (R1468 `[R0017, R0083]`, R1101 `R1107`, R1126 `[SPEC.md, R0083, R1396]`, R1158 `R0083`, R0085 `SPEC.md`, R0086 `R0862b`, R0483 `R0862b`, R0470 `SPEC.md`). None contradicts the DEC — R0083 is the red gate, R0862b is the plan — and R1101→R1107 and R1468→R0017 are more useful pointers than the class text. Defensible; recorded so the decision session knows the DEC was read as "not differing" rather than as overriding. Applying F-1 settles the non-id ones.

## Verdict (Quality): ready-with-findings

- `bin/tests/run` in the worktree: 519 tests, OK, 8 skipped (observed). Tests added: 5 in `test_rulestore.py` (61→66), 3 in `test_rulestore_store.py` (15→18) = 8, as claimed.
- `store.py`: `_check_enforce` runs after every key is normalised; rejects a fifth value (`native`, `prose`, `hooks`, `harness:hook`, `""` all tested), rejects a two-item list (`[hook, deny]`), accepts the four values case-insensitively, and treats `null` as absent. Error names id and key. Through `FileRowSource` a rules file with `enforce: native` raises `RowShapeError` naming the row (tested). `enforce: hook` is an ordinary selectable key (tested). The `rules/retired/` row is not returned by the source (tested — though that half was already true at base; the test's `retired:` text assertion reads back the fixture it wrote, so it proves little beyond the helper).
- The spec sentence says what the code does: exactly one of four values, anything else a defect, absence = judgment row. `keys.py` is a census with no registry, so the plan's mention of it needed no edit (observed).
- `reconcile_sort.py` read on its own terms: reads only the per-topic tables (stops at "Classes for ruling"); DEC overrides and successors are explicit tables with their entry named; retired rows must differ from base by exactly one added `retired:` line, harness rows by one added `enforce:` line, re-topiced rows by `topic:`/`order:` only, everything else byte-identical; deletion/duplication/stray-id checks against `git ls-tree` at base; order collisions per receiving topic; loads the store and prints the `role=chief-of-staff session=decision` count. Ran with `--base 28366d4`: exit 0, 0 mismatches, 145 rows for the query (observed; I reproduced 145 through `query.select` directly). Its summary numbers match mine.

### F-3 (non-blocking, observed) — small looseness in the schema check and the script

- `enforce: []` is silently a judgment row (the dialect skips an empty list on every key before `_check_enforce` runs). Consistent with the store's treatment of every other key, so not a defect of this change; noting it because a generator reading `enforce:` later will not see such a row.
- `test_dec_001400_an_absent_enforce_is_a_judgment_row` passes `enforce: null`, not an absent key; the absent case is covered by `assertNotIn("enforce", rows["R0001"].keys)` in the store test, so coverage is there under the wrong name.
- `only_added_key` / `only_changed_keys` in the script accept the added line anywhere in the file, not only inside the frontmatter. No row trips it today (my byte-exact reconstruction confirms), but the check is weaker than its docstring.
- `DEFAULT_BASE` is `28366d4`, the plan's acceptance names `3c686e0`; equivalent for `rules/` (identical trees, observed), but the script's default will not be the plan's SHA when someone reads the plan.

Smallest fix: none required; a one-line test rename and a frontmatter bound on the two helpers if the script is kept past 1a.

## Verdict (Skepticism): ready-with-findings

What would make this delta wrong that the checks above miss: a body edited while the frontmatter check looked only at keys; a key other than the four changed; a retired row still reaching a bundle; a surviving row now pointing at a retired one; the move landing a row somewhere the renderer cannot place it.

- Bodies and other frontmatter: covered by the byte-exact reconstruction in Continuity — zero rows deviate.
- `bin/bundle --where … --out /tmp/rev-1a-out` refused ("HEAD is not synced with origin/main"), as the task anticipated. Used the store's query code directly: `FileRowSource(...).rows()` loads 399 rows (386 rules + 13 process), zero of them from `rules/retired/`; `query.select` for `role=chief-of-staff session=decision` returns 145 rows, none retired; the 16 `enforce:` rows in that selection are all live rows that 1b rewrites, as the plan intends.
- No surviving `rules/R*.md` body cites a retired id in `[Rnnnn]` form (observed by grep over every live row).

### F-4 (non-blocking, observed) — `spec` has no position in the render sequence until package 2

`process/named-queries.md`'s sequence block does not name `spec`, so its 11 rows render after every named topic, alphabetically ("a topic neither block names sorts after the last named one"), and the block still names `convergence`, `directive-invariants`, `trd`, `prd-template`. Nothing is released between 1a and 2 and the plan assigns `named-queries.md` to package 2, so this is a hand-off note, not a defect of 1a: package 2 must add `spec` to the sequence (the natural slot is beside `change-flow`).

### F-5 (non-blocking, observed) — two process documents cite eleven now-retired ids

`process/change-flow.md` cites R0008, R1395b, R0474, R1491, R1602, R0470, R0483, R0489; `process/spec-test-suite.md` cites R1101, R0474 (twice), R1153. Both are process documents, outside 1a's blast radius and rewritten/retired by package 2, but a bundle generated between 1a and 2 would carry citations to rows no bundle contains. Hand-off to package 2; no action in 1a.

### F-6 (non-blocking, observed) — a pre-retired row now points at a retired row

`rules/retired/R1283.md` (retired before base) carries `retired: R1608`; this delta retires R1608 with the free-text successor of F-1. Harmless chain, untouched as it should be; worth knowing if anyone ever resolves successors transitively.

## Summary

The mechanical half is right: every row is where its ruling puts it, every body and every unrelated key is byte-identical to base, nothing is deleted, nothing outside the blast radius moved, the schema change does what the spec sentence says and is tested, and the reconcile script is honest on its own terms. The one change required is the form of 56 `retired:` values (F-1): they follow the plan's wording but break the store spec's AC-RS-10 and the very sentence this delta edits; naming the governing DEC id where no successor row exists satisfies all three texts and needs no ruling.

Review file: `/home/claude/sort/review-1a.md`

- Verdict (Continuity): changes-required
- Verdict (Quality): ready-with-findings
- Verdict (Skepticism): ready-with-findings

## Re-read over 96f320e..27845c3

Verdict: ready

One commit (27845c3). Worktree recreated from origin/pkg-1a-store-moves and removed after.

1. Scope (observed): the diff is 57 `rules/retired/*.md` files plus `bin/tests/reconcile_sort.py` and `bin/tests/test_rulestore.py`. In `rules/` every changed line is a `retired:` line (grep of the diff for any other `+`/`-` line is empty); bodies and other keys untouched. Nothing else in the tree.
2. Values (observed): all 79 retired files match `^(R\d{4}[ab]?|DEC-\d{6})$`. This package's 75: 26 row ids, 49 DEC ids, as claimed (the other 4 row ids are the pre-retired rows). Every DEC id named is a `## DEC-` heading in `decisions/log.md`; every row id named is a live `rules/R*.md` — the one exception is pre-existing R1283→R1608 (F-6, untouched, as it should be).
3. The eight re-pointed rows (observed against the table note; inferred on defensibility): R0474→R0007 (note: "R0007 + subagents"), R0896→R0229 (note names R0229), R1395a→R1396, R1395b→R1614, R1106→R1107 (each note names that id beside "subagents"), R0212→R0208 (note: "R0208 … + SPEC.md"), R1468→R0017 (note: "R0017 + R0083"), R1126→R0083 (note: "SPEC.md DoD + R0083 + R1396"; R0083 is the red gate DEC-001190 names). All eight name a row the table's own note names and none contradicts its DEC. None wrong.
4. F-3 fixes (observed): the "absent" test now passes no `enforce` key at all, and a separate test covers `enforce: null`; `only_added_key` now requires the added line at line 2, directly after `id:` on line 1 of the frontmatter, with the rest of the file equal to base. `bin/tests/run`: 520 OK, 8 skipped. `reconcile_sort.py --base 28366d4`: 0 mismatches, 145 rows for role=chief-of-staff session=decision.

### F-7 (non-blocking, observed) — the script checks the value's shape, not its existence
`RETIRED_VALUE_RE` admits any `Rnnnn`/`DEC-nnnnnn`; nothing in the script checks the row is live or the DEC is in the log. I checked both by hand (all resolve). Smallest fix: one lookup against the live ids and the log's headings where the regex is applied (lines 363, 461). Not required for 1a.

F-1 closed. F-3 closed. F-2, F-4, F-5, F-6 stand as non-blocking hand-offs.
