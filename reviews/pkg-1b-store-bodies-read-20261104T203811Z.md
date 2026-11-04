---
review: package 1b — store subtraction, the bodies
delta: 5374b0a..d5f1eb3 (branch pkg-1b-store-bodies)
read: 2026-11-04, by a reviewer subagent that wrote none of it; first read over 5374b0a..c8e4125, re-read over c8e4125..138e2b4; the two re-read nits applied at d5f1eb3 by the decision session
---

# Review: package 1b — store subtraction, the bodies

Delta: `origin/main` (5374b0a) .. `origin/pkg-1b-store-bodies` (c8e4125). 54415fc is DEC-001470 (the decision session's; skipped). Package commits: 7562ca4 (A), 32ae6bb (B), ee300a8 (C), 8253904 (D), 7573a28 (E), c8e4125 (F).
Governing texts read: plan §1b (and DEC-001470's widening for the two merge losers), SPEC.md §4 and §7, `decisions/log.md` DEC-001070–DEC-001470, the sort table's per-topic notes for every changed row, the coder's report as relayed.
Method: every A/B/C/F hunk read against its ruling; every D block parsed as YAML; both reconcile modes and `bin/tests/run` run in the worktree; two bundles rendered through `bin/rulestore` (`query.select` + `terms.pull_definitions` + `render.render`) for `role=chief-of-staff session=decision` (146 rows, 37 definitions) and `role=coder-agent session=execution` (96 rows, 37 definitions) and read.

Verdict: changes-required

Passes planned: Continuity, Quality, Skepticism. All three ran.

## Verdict (Continuity): changes-required

What checks out (observed unless marked):

- Changed-row set. 88 row files differ from 5374b0a: 85 modified, 2 added (R1616, R1617), 3 renamed to `rules/retired/` (R0759, R1533, R1542 — the widening DEC-001470 grants, each with `retired:` naming its survivor). Every one of the 88 is in one of the six package commits; no row changed outside them. The 103 out-of-scope rows (topics writer, copy-editor, critic, voice, public-prose-criteria) are byte-identical to 5374b0a — my own per-topic diff and `reconcile_sort.py` default mode (`out-of-scope, identical:103`) agree. Outside `rules/`: only `bin/tests/reconcile_sort.py` and `decisions/log.md` (DEC-001470) change. Blast radius held.
- Rows the rulings name, bodies versus entries: R0199 (DEC-001170: subagent + working tree — done literally; see F-7), R1478 (DEC-001180: session → subagent), R1479/R1480 (contain no "session"; correctly untouched), R0004/R0006/R0007/R0017 (DEC-001200: tranche gone — R0007's only "tranche" was in `condition:`, fixed in F), R0863 (DEC-001210: design section), R0205 (DEC-001330: the one sentence, verbatim), R1606 (DEC-001340: the entry's sentence, with "agreed wording" → "approved wording" under DEC-001360; see F-5), R1611 (DEC-001300: verbatim intent), R0065 (DEC-001390: "every review — a plan before it dispatches as much as a diff"), R1244 (DEC-001260: input half kept, write prohibition gone), R0611 (DEC-001360: reworded, `term: [approved]`), R0264 (DEC-001380).
- R0264: the four removed bullets are exactly the four DEC-001380 names — "refers to no file by path", "every value taken from the values that key already holds", "names the session kind it binds", "speaks in tiers, never in model names" — and twelve bullets remain, matching "the twelve judgment criteria stay". The closing paragraph is untouched.
- The five rows the coder flagged as unlisted (R0129, R0139, R0500, R0535, R1183): each is "the TRD" / "standing TRD" → "the spec" / "the spec's design section" / "the spec's targets" and nothing else. Vocabulary only. Three more A rows have no table reword note and the coder's relayed report does not list them: R0009 ("brought to full agreement with" → "brought into line with" — avoids the `agree` grep; same meaning), R0064 (Human note only: "A directive's parts" → "The methodology's own artifacts"), R1450 (drops the example "a PRD read raising a TRD question"). Also vocabulary only; R0876 is named by DEC-001310 and the class-6 rule. None adds or drops an obligation.
- The table's other pruned/reworded rows: R0472, R0478, R0492, R1485, R1489, R1104, R1107, R1116, R1122, R1155, R0760, R0862b, R0798, R0799, R0045, R0055, R0200, R0207, R0220, R0252, R1196 each do what their note says. R1116's dropped bullet "it is consistent with the TRD, where one exists" is the one-document collapse; R1104's rewrite to an internal-consistency scan covers it. R0220 also drops "The two are never the same object", which is correct once only one object remains.
- Approve sweep (C): ten rows, all surviving-row bodies or Human notes where the word was the act DEC-001360 renames; `rules/retired/` untouched as the entry requires. R0611's `term:` change is the one frontmatter edit the ruling implies.
- R0043 and R0044: byte-identical to 5374b0a (the decision session's ruling: leave both).
- The merges carry DEC-001310's content: R1513 keeps R1542's "in force only from [the] ruling, recorded in the decision log naming the reviewed SHA" and gains `architect-agent`; R0472 keeps R0759's "owned by the human" and R1533's "derived from the spec". What they drop is in F-2 and F-3.
- Condition lines (F): the eight are vocabulary (tranche, agreed, directive, execution session, PRD, TRD) — none changes the trigger, except R0091's "working under a directive to edit specs" → "editing specs", which widens the trigger to any spec edit; correct for a hook keyed on the agent, not the directive.

### F-1 (blocking, observed) — R0055 still carries `term: [decomposition doc, …]` after its body dropped the decomposition doc; every bundle renders a retired artifact as a definition heading

`rules/R0055.md` line 8: `term: [decomposition doc, change package, change packages, acceptance criteria, spec, specs]`. The A rewrite removed "the decomposition doc" from the body (per the table note), but the `term:` key was not touched. `render.render` heads each definition with its first term, so both rendered bundles carry `**decomposition doc** — What a session derives work from is a change package, the acceptance criteria, or the spec — \`SPEC.md\`.` (chief-of-staff line 813, coder line 398). The store now defines a term its body never states — the retired mechanism SPEC.md §4 names (`decomposition.md`) resurfaces by name in every bundle — and the `--bodies` grep cannot see it because "decomposition" is not in its pattern set. Smallest fix: drop `decomposition doc` from R0055's `term:` list (first term becomes `change package`). Whether the row should also lose `acceptance criteria` as an alias is F-3's question.

### F-2 (non-blocking, observed) — R0472's merge drops a scope clause no ruling names

At 5374b0a R0472 ended "…the Spec Reviewer has gated; that gate reaches specs and nothing else." The merged body is "…derived from the spec and owned by the human." The table note is "pruned: PRD/TRD -> SPEC.md; AC adequacy is judgment"; DEC-001310 says "merge into one row about the spec". Neither asks to drop the limit on the Spec Reviewer's gate, and no surviving row states it (R1056 states the inverse — spec documents are the Spec Reviewer's — not the ceiling). R1533's clause "whether they live in the [spec] itself or in the unit's own artifact" is also gone; that one is permissive, not an obligation. Smallest fix: either append "; that gate reaches specs and nothing else" to R0472, or have the coder's report state the drop as deliberate for the decision session to ratify.

### F-3 (non-blocking, observed) — retiring R0759 moves the only definition of "acceptance criteria" into a role-limited `require` row

R0759 was a lexicon `define` row with no `role:` (reaches every bundle) and `term: [acceptance criteria, acceptance criterion]`. Its content survives in R0472, which is `verb: require`, `topic: [change-flow]`, `role: [chief-of-staff, spec-reviewer-agent]`. Term lookup still resolves because R0055 lists `acceptance criteria` as an alias, but R0055's body does not define it (see F-1), so the coder and test-designer bundles now carry the words "acceptance criteria" (R0478, R1041, R0055) with no definition that says what they are or who owns them. DEC-001310 names "one row about the spec" and the sort kept R0759's content, so this is a consequence of the ruling rather than a divergence from it; flagging because the Definitions band lost something. Smallest fix if wanted: `term: [acceptance criteria, acceptance criterion]` on R0472 — but R0472 is role-keyed, so that only half-restores it; the decision session may prefer to accept the loss.

### F-4 (non-blocking, observed) — two table-marked "pruned" rows are unchanged and the relayed report does not say so

R0889 (table: "pruned: connector held by one decision session; judgment on what is running") and R0229 (table: "pruned; pasted output rarer under subagents") are byte-identical to 5374b0a. No DEC entry names either, and neither note states a wording to drop, so leaving them is defensible — but the report should say they were read and left, so the decision session does not assume the prune landed. Smallest fix: one line in the report.

### F-5 (non-blocking, observed) — R1606 drops its pinned-ref sentence; "covered" is half true

Dropped: "A ref pinned for the executor to verify is a claim, read from the tree and cited, not a dictated fact." DEC-001340's wording omits it, so dropping is "no more than the entry". But R1607 (rendered next to it) covers the executor's side only; the dictator's obligation — a pinned ref is a cited claim — is now nowhere, and the plan itself pins refs (`spec: SPEC.md @ 2c0d491`, `base: main @ 3c686e0`). Smallest fix: none required by the entry; the decision session should know the sentence is gone rather than folded.

## Verdict (Quality): ready-with-findings

What checks out (observed):

- All 34 fenced blocks parse as YAML mappings (`yaml.safe_load`): 9 hook blocks keyed `event`/`matcher`/`command` (R0091 and R1156 with `scope: agent` first), 3 deny blocks keyed `deny:` list, 5 agent blocks `field: description|model`, 17 skill blocks `skill: gate|release|intake|build`. Fence language `yaml` throughout. Shape is consistent within each kind.
- Event/matcher pairs: PreToolUse Edit|Write for the four refusals (R0583, R0934, R1408, lane-guard ×2); PostToolUse Edit|Write for the three store-lint checks, which is DEC-001250's word ("one `PostToolUse` lint over `rules/` and `reviews/`"); PostToolUse Bash for push-readback (DEC-001350: after any `git push`). Each fits what the row enforces; see F-6 and F-8 for the two where the event choice has a cost.
- `bin/hooks/<name>` names: `lane-guard --lane specs|tests`, `store-lint --check citations|generated-filename|verdict-lines`, `decision-log-append-only`, `review-artifact-immutable`, `intake-branch-guard`, `push-readback`. Five scripts, two with sub-selectors; every Human note states the exact observable the script checks (path, branch name, diff shape, ref SHA), so package 3a can write each without guessing. R1605's comment carries the four DEC-001380 criteria for `store-lint`.
- Every hook and deny Human note contains the boundary sentence ("matches the tool call, not intent" / "A deny matches tool calls, not intent") and names what the check refuses and that it refuses nothing else. R0564's note carries the DEC-001230 Free-tier sentence; R0203's names the Codex `PreToolUse` fallback (DEC-001220).
- Deny patterns: middle-of-command wildcards (`Bash(git push * --force*)`, `Bash(gcloud * deploy*)`) are supported by Claude Code's Bash glob matcher per current third-party documentation (inferred from one source; package 3a's fixture should confirm against Anthropic's own page, which is what R1616 now asks).
- R1616 and R1617 against R0264's twelve: one trigger each in `condition:` and body ("On a failure from an external system"; "writing or reading a review artifact" — two moments, but the DEC-001440 wording binds both the writer and the reader, so one rule); each states an obligation, defines no term, names no path, cites no model, contributes what no row does; `source: decisions/log.md:DEC-0014x0` follows the precedent set by the DEC-001060 row. Orders 430 (core) and 320 (review-artifact-schema) collide with nothing. R1616's role list is the nine software roles and `corpus: [software]`, matching "every software role"; R1617's is the four reviewer roles plus Chief of Staff, matching the entry.
- `--bodies` grep: patterns are `\bagree`, `\bdirective`, `\btranche`, `\bPRD\b`, `\bTRD\b`, `\bexecution session` (case-sensitive); the two exceptions (R0963 "pronoun agreement", R1173 the author's "agreement") are explicit, each with a reason, both out-of-scope rows, and an unused exception is itself a failure. It also checks every `enforce:` row carries its block with the keys its kind needs and that hook commands start `bin/hooks/`. Run: 385 surviving rows, 2 hits both allowed, 34 blocks checked, 0 problems, exit 0. My own case-insensitive grep over the same six words plus `PRDs|TRDs` finds nothing beyond `source:` lines naming the old template files. `bin/tests/run`: 520 tests, OK, 8 skipped.

### F-6 (non-blocking, inferred) — R1408's "a file that already exists under `reviews/`" refuses a reviewer's own in-progress edits

The Human note defines the observable as existence under `reviews/`. A reviewer writing an artifact into the repo writes it once and edits it several times before committing; the hook as described refuses every edit after the first `Write`, and refuses the "ready on re-read" correction the 1a review recorded. The intent (DEC-001230: existing artifacts are not rewritten to a later schema) is about landed records. Smallest fix: in the note, "a file tracked at HEAD under `reviews/`" (or on the default branch), so an untracked or uncommitted artifact stays editable. Package 3a reads this note to write the script; it should be settled here.

### F-7 (non-blocking, observed) — R0199's "As a subagent," narrows the trigger below the condition DEC-001170 kept

DEC-001170's context: "worktrees were made by hand, so the condition R0199 guards still arises" — that was the human's own Mac session, which is also where an execution block runs (SPEC.md §4, DEC-001420). The row is keyed `session: [execution]` on the nine software roles, so "As a subagent" adds nothing the keys do not and lets a non-subagent executor read itself out. The entry does say "reworded from execution session to subagent and working tree", so the coder followed it literally; DEC-001330 offers "or the session that runs it". Smallest fix: drop the opener — "If a file you did not change moves in your working tree, HEAD moves, or an index lock appears, stop and report rather than recover." Same pattern, less sharp, in R0200 ("happen elsewhere, in a subagent") and R0252 ("any subagent left running" — a subagent cannot outlive the session that hands the baton; what can is a Codex or Mac session running an execution block). One ruling covers all three.

### F-8 (non-blocking, inferred) — R1414's verdict-lines lint at PostToolUse fires on every partial write of a review artifact

A review artifact is written in pieces; a PostToolUse lint on Edit|Write under `reviews/` reports "Verdict: lines missing" after each intermediate write. PostToolUse output is advisory, so this is noise, not a refusal, and DEC-001250 names PostToolUse, so the block is as ruled. The sort table's class 10 said "PostToolUse/Stop"; a Stop-time check fits verdict-lines better. Smallest fix: none in 1b; a note for 3a to make the script tolerate a file that has no `Verdict:` line at all (still being drafted) and fail only on a wrong enum or a wrong overall verdict.

### F-9 (non-blocking, observed) — R0506's block names one skill where DEC-001290 names two readers

DEC-001290: "R0506 becomes a shared report template the review skill also reads." The block is `skill: release`. Smallest fix: a comment line in the block (`# shared with review (DEC-001290)`) so the shape stays one scalar and 3a/4 do not miss the second reader.

### F-10 (non-blocking, observed) — the `--bodies` check is not in the unittest suite

`bin/tests/run` discovers unittest modules; nothing in `bin/tests/*.py` calls `check_bodies`, so a later commit that reintroduces "agreed" or drops a hook block passes `bin/tests/run`. The acceptance line is met as written (a grep exists and is green). Smallest fix: a four-line test that imports `reconcile_sort.check_bodies(root)` and asserts `problems == []`.

### F-11 (non-blocking, observed) — R0564's deny set misses the refspec force form

`git push origin +main` force-pushes and matches none of the six patterns. Smallest fix: add `Bash(git push * +*)`. (Also noting `--force-with-lease` is denied too, which "never force-push" covers.)

## Verdict (Skepticism): ready-with-findings

What I looked for: a fenced block that reads wrongly in a bundle; a `condition:` edit that changes a trigger; a body that now says something false in the human's own session; what a wrong body here does downstream.

- Fenced blocks in a rendered bundle: `render.render` emits `row.body`, and the block is in the body (the store's `_split_human` leaves it there), so the blocks reach the bundle text. For a hook with prose (R0196, R0583, R1408, R1414, R1605, R0091, R1156) the block follows its sentence and reads as an annotation. See F-12 for the two block-only rows.
- Condition edits: all eight vocabulary; R0091's widening is right for a hook. None is a meaning change.
- No body now contradicts the store in context: the Definitions band renders R0611 as `**approved**`, R0200 as a decision session that writes "plans, subagent prompts", R0220 as a baton-only handoff. The bundles still carry process documents with the old vocabulary (`spec/<tranche-slug>`, "closed, agreed", "PRD, TRD") — package 2's territory, named here only so nobody reads the rendered bundle as 1b's failure.

### F-12 (non-blocking, observed) — the `bundle` target renders R0934 and R0720 as orphan YAML

In the chief-of-staff/decision bundle, R0934 renders as a bare block (lines 108–112) between R0893's handoff sentence and R0940's "say so and recommend ending the session", with no prose saying what it is; R0720 does the same in every software bundle. SPEC.md §7 keeps `bundle` for Claude chat, where a hook cannot run, so a chat session reads three lines of YAML it cannot act on. The rows are as DEC-001320/DEC-001350 rule ("no prose row is kept"); the fix belongs to package 3a's `bundle` emitter (skip `enforce:` rows, or render the Human note's first sentence in their place). Flagging so 3a's acceptance says so; nothing above 1b catches it otherwise.

### F-13 (non-blocking, inferred) — store-lint's "refers to no file by path" now collides with bodies this package wrote

R1605's block tells 3a that `store-lint` carries "a row refers to no file by path". Surviving bodies now name `SPEC.md` (R0055, R1104, R1513, R1611), `decisions/log.md` (R0583, unchanged from main), and the Human notes name `rules/`, `process/`, `reviews/`, `specs/`. Once 3a emits the lint and package 6 self-adopts, the next `rules/` edit fails on rows this package landed unless the check exempts `SPEC.md` (the document DEC-001090 names) and `enforce:` rows' blocks and notes. Smallest fix: one more comment line in R1605's block stating the exemptions, so the script's author inherits the decision rather than discovering it.

### F-14 (non-blocking, inferred) — R0934's `intake/*` branch proxy will refuse the subtraction's own packages after self-adoption

The Human note makes the observable "a branch named `intake/*`". DEC-001320 says governed paths are editable only inside the intake skill, and a branch name is the only thing a hook can see, so the choice is sound. Its consequence: after package 6 installs the emitted tree in fiducial, a package-style branch (`pkg-*`) editing `rules/` is refused, including a package 7 fix-up. Either that is wanted (every store edit goes through intake) or the plan's package 6 needs to say how fiducial's own packages pass. Nothing in 1b to change; the decision session should rule before 3a hard-codes the pattern.

## Disposition

Blocking: F-1 (one `term:` line). Everything else is for the decision session to ratify or carry to 3a: F-2, F-3, F-5 are content the merges and the R1606 rewrite dropped that no entry asked to drop; F-6, F-8, F-13, F-14 are what the hook notes will make 3a build; F-7 is the subagent-wording hazard the brief asked about; F-4, F-9, F-10, F-11 are small.

Worktree `/tmp/rev-1b` removed after this review; rendered bundles under `/tmp/rev-1b-out/` (throwaway).

File: `/home/claude/sort/review-1b.md`

Verdict (Continuity): changes-required
Verdict (Quality): ready-with-findings
Verdict (Skepticism): ready-with-findings

## Re-read over c8e4125..138e2b4

Verdict (re-read): ready-with-findings

Observed, in a fresh `/tmp/rev-1b` at 138e2b4 (removed after):

1. Diff touches exactly R0055, R0199, R0200, R0208, R0252, R0472, R0506, R0564, R1408, R1606 and the R0205 move (`R080 rules/R0205.md → rules/retired/R0205.md`). Nothing else — no file outside `rules/`. 384 live, 83 retired.
2. Restorations against their entries: R0472 regains "the Spec Reviewer's gate reaches specs and nothing else" (the 5374b0a clause, no more); R0199 drops "As a subagent," (DEC-001170's condition, keys unchanged); R0200 "in the session that runs it" and R0252 "any session still running an execution block" are DEC-001330's alternate wording; R1408's note and block comment say "tracked at HEAD", untracked passes; R0564 adds `Bash(git push origin +*)` and `Bash(git push * +*)`; R0506 `skill: [release, review]` (DEC-001290's two readers; the only list-valued skill block — 3a must accept a scalar or a list). R1606's restored sentence reads "A ref pinned for the subagent to verify is a claim, read from the tree and cited; a tree fact dictated for it to land is the defect" — the first clause is the 5374b0a sentence; the second is new wording that restates the row's own rule, adds no obligation (F-15).
3. R0208 keeps `verb: define`, `term: [paste block, …, execution block, execution blocks]`, and renders as `**paste block** — A paste block is copied whole…`; the body now carries DEC-001330's sentence whole ("shell commands the human runs as given"; "instructions a session carries out"). "The human" names who runs it, as the entry does; the obligation is unchanged.
4. `rules/retired/R0205.md` carries `retired: R0208`; `grep R0205 rules/R*.md process/ bin/rulestore` finds no citation. Its `term:` was set to `null` (F-16).
5. Re-rendered chief-of-staff/decision bundle (146 rows, 37 definitions): no Definitions heading names a retired mechanism; "decomposition", "execution session", "directive" survive only inside rendered process documents (package 2). `--bodies`: 0 problems; `bin/tests/run`: OK (8 skipped).

### F-15 (non-blocking, observed) — R1606's restored sentence adds a clause the original did not have
"; a tree fact dictated for it to land is the defect" is not in 5374b0a's body or DEC-001340. It restates the first sentence, so no obligation changes; smallest fix is to end the sentence at "cited" if the decision session wants the restoration byte-faithful.

### F-16 (non-blocking, observed) — retired R0205 has `term: null` where every other retired row keeps its term list
The 1a convention (23 retired rows, e.g. R0202 `[execution session, …]`, R0054) leaves frontmatter as it was apart from `retired:`. R0205's `[decision layer, execution layer, shell layer]` was cleared with no ruling naming it; the terms are now defined nowhere, live or retired. Smallest fix: restore the line. Separately: DEC-001330 ruled "R0205 stays as one sentence"; retiring it under DEC-001310's principle needs its own entry at merge so the log does not contradict itself.
