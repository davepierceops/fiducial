# Review: rules/R1606.md, R1607.md, R1609.md, R1610.md, R1612.md, rules/retired/, decisions/log.md — tree-fact-rows-nb-read-20260911T230000Z

Verdict: ready-with-findings
Reviewed: rules/, decisions/log.md @ 74ebe0867f698b4c3d3ab3a5846fb68c3cf40d53
Baseline: rules/, decisions/log.md @ e7f5994
Reviewer: Context Quality Reviewer (frontier, fresh session; did not produce the delta)
Date: 2026-09-12
Scope: the diff e7f5994..74ebe08 whole — four replaced bodies (R1606, R1607, R1609, R1610), R1609 re-keyed to both sessions, four rows moved under rules/retired/ with a `retired:` line (R0188, R1220, R1228 by rename; R1283 restored from d44ad52), one added row R1612, seven appended entries DEC-000810–DEC-000870 — read by dimension: continuity of each replaced body against the finding it answers and of the store against the four retired bodies; every changed or new row against every R0264 criterion and against R1605; every entry against the form process/decision-log.md states and against the row it records. Checks run in the assigned worktree: a script diffing each landed body against the fenced block in the producing directive at f39aadd, byte for byte, and each DEC Decision line against its row; `bin/bundle --near` at 0.30 (CLI) and 0.12 (module) for the five changed bodies and the four retired bodies; a citation sweep for the four retired ids over the tree outside docs/history and docs/rule-register; a role/session/corpus containment check of each retired row against its successor; byte diffs of the four retired files against their last in-force revisions; `bin/bundle --keys`; `bin/tests/run`.
Cross-checked: rules/R0264.md and rules/R1605.md @ 74ebe08, process/review-artifact.md @ 38aab41, process/decision-log.md @ 74ebe08, reviews/tree-fact-rows-read-20260911T180000Z.md @ 74ebe08, docs/cycles/tree-fact-rows-nb-20260911T210000Z.md @ 74ebe08 and @ f39aadd, specs/rule-store.md @ 74ebe08 (AC-RS-1, AC-RS-9, AC-RS-10, G2–G4, G11, J3), bin/rulestore/store.py (the `rules/*.md` glob), rules/R1293.md, R0262.md, R1608.md, R0458.md, R1218.md, R1213.md, R0208.md, R0168.md, R0199.md, R0192.md, R1173.md, R0570.md, R1206.md, R0060.md, R1158.md, R1022.md, R1054.md, R0552.md, R0759.md, R1513.md, R1291.md, R0256.md, R0225.md, R1199.md, rules/retired/R0188.md, R1220.md, R1228.md, R1283.md
Not inspected: rendered bundles — `bin/bundle --where` refuses on this branch ("refused: HEAD is not synced with origin/main", observed), so which bundles each changed row lands in is inferred from its keys and `bin/bundle --keys`, not observed; the two docs/cycles directives in the range — read as companions, not reviewed as deliverables; the content of specs/rule-store.md beyond the clauses named above; docs/rule-register/ and docs/history/ — excluded from the citation sweep by the producing directive's own rule and the human's 2026-09-11 ruling recorded in DEC-000800; the retro items behind the prior read's findings — the findings were taken as stated in that artifact.
Findings: 0 blocking, 3 non-blocking, 7 observations
The human should inspect: NB-1 (R1609 no longer constrains what the expected-output line may say — R1220's "observed in the environment the block will run in, or qualitative with no number" did not survive the merge), NB-2 (DEC-000870's re-reading of "deleted" names DEC-000800 and DEC-000840 but not DEC-000830, which says the same of R1220 and R1228), NB-3 (where a retired row's `## Human` note lives once its obligation moves to a successor)

## Continuity

Verdict (continuity): ready-with-findings

Each replaced body against the finding it was changed for [inferred by reading; the finding text taken from reviews/tree-fact-rows-read-20260911T180000Z.md at the base ref]:

- R1606 against R1293 (NB-1 of the prior read). The SHA leaves the enumeration of tree facts; the prohibition is scoped to facts "for the executor to land"; a new sentence classes a pinned ref as a claim to verify, not a fact to land. R1293's expected-state lines — counts, exit codes, blob SHAs — are lines the executor verifies, so they fall outside "to land" and the two rows no longer pull against each other. Answered. Residual wording — see O-1. The prior NB-2 (the executor's obligation stated where the executor never reads it) is answered by moving that obligation out of R1606 into R1607, which renders to both sessions.
- R1607 against the retired R0188 (NB-4 of the prior read). R0188 ("If you cannot execute what you were given as written, stop and surface it rather than proceeding"; verb stop; session execution; eight agent roles) is retired; R1607's closing sentence "Stop on what the tree does not resolve" is now the in-force stop, and its middle clause carries the executor's derivation-with-evidence duty. Reach: every role, session and corpus value R0188 carried, R1607 carries [observed: containment check, no value missing], so no execution bundle that held R0188 loses the stop. The boundary the prior read asked for is now inside one row rather than between two: the tree resolves it, or you stop. Answered. The store's only "cannot execute as written" row is gone with it; that phrase survives in the directive template's STOP CONDITIONS (process/directive-invariants.md:144, observed), which is the executor's other carrier, and the `verb=stop` census falls to 4 [observed: `bin/bundle --keys`].
- R1609 against the retired R1220 and R1228 (NB-3 of the prior read). Session is now `[decision, execution]` [observed], matching every other keyed row in command-blocks. R1228's obligation (valid and non-harmful; re-running compounds no damage) is carried in R1609's first clause at its shortest — the append-marker mechanism is dropped, as a merge may. R1220's blast-radius clause is carried; its expected-output clause is carried only in part — see NB-1. Reach: every key value R1220 and R1228 carried, R1609 carries [observed].
- R1610 against the prior NB-5. The added sentence covers pointer-carried text; the wrapped-vs-one-line failure the prior read ran into is answered in practice — the producing directive carries its five bodies as one-line fenced blocks and every landed body is byte-identical to its block [observed: five of five]. See O-4 for what that leaves unrecorded.

No row in force restates a retired row [observed: `--near` at 0.12 over the store of 471 rows; the top neighbour of each retired body is its named successor — R1220→R1609 0.30, R1228→R1609 0.24, R1283→R1608 0.27 — and every other neighbour scores below 0.20; inferred: R0188's nearest, R0168 at 0.19 ("If the work needs more than that, say so and stop"), fires on scope, not on inability to execute, and R0199 at 0.15 fires on concurrent mutation; distinct].

The retired rows are outside the store [observed: `FileRowSource.rows()` returns 471 rows, none with a path under rules/retired/ and none with id R0188, R1220, R1228 or R1283; bin/rulestore/store.py:252 globs `rules/*.md` non-recursively; `bin/bundle --keys` prints no `retired=` key; `bin/tests/run` passes test_ac_rs_1_nothing_under_rules_retired_is_returned and test_ac_rs_6_a_retired_row_is_never_bundled]. Each retired file is byte-identical to its last in-force revision plus one line, `retired: <successor id>`, inserted after `id:` [observed: diff against e7f5994 for R0188, R1220, R1228 and against d44ad52 for R1283]; the value names a successor row id, one of the two forms AC-RS-10 admits.

No row in force and no process document cites any of the four retired ids [observed: bracketed-citation grep over rules/ excluding retired/ and over process/ both empty; the tree-wide sweep outside docs/history and docs/rule-register finds them only in docs/cycles/, reviews/, decisions/log.md and rules/retired/].

R1612 against R0262 and the decision layer [inferred]: R0262 governs a file path written to the human's filesystem; R1612 governs a pull request handed for merging. Same form (a paste block, one item, nothing else), different object and trigger; neither implies the other. Nearest by `--near`: R0262 0.24, R0570 0.21 (open a pull request and merge it — says nothing of the handover), R1206 0.17 (a block pushes a branch; the decision session merges through a pull request). No row in force mentions a URL [observed: grep]. Not a restatement.

R1605: none of the five changed or new rows carries a bracketed citation [observed: `grep '\[R'` empty], so co-rendering is satisfied vacuously.

Placement [observed]: R1612 takes order 205 in decision-layer, between R0262 (200) and R0100 (210) — see O-3. R1609 keeps 270 in command-blocks, whose 210 and 260 are now vacant. Its `source:` names line 121 of the producing directive at f39aadd, which is the first and only line of the row's fenced block [observed].

## Quality

Verdict (quality): ready-with-findings

Every changed or new row against every R0264 criterion; a row passes a criterion unless named here [observed for keys, citations, paths, model names, terms; inferred for readability, contribution, consistency, trigger]:

- Keys: every role, session, corpus and topic value on the five rows already exists in `bin/bundle --keys` [observed]; R1609's new session value is the topic's majority value. Model names: none. File paths: none. Form vs row: all five are rows. Tool-enforced: none — no tool performs R1609's run, R1610's diff or R1612's handover.
- Trigger: R1609 states its own ("Before handing over a block"); R1606 and R1610 carry it in the imperative's object, as before; R1607's three clauses fire on one act — reading the tree for what the directive left open — and are one checklist row rather than three; R1612 in its object (a pull request handed for merging). One each.
- Terms: "paste block" in R1612 is a Lexicon term (R0208, observed). "tree fact" remains defined by enumeration in R1606, as the prior read's O-3 noted; unchanged.
- Session kind bound: R1606 no longer states an execution-session obligation; R1607 states the executor's and is keyed to both; R1609 now keyed to both. The prior read's NB-2 and NB-3 are closed on this criterion.
- Consistency with every rule in force: R1606 against R1293 — see continuity and O-1. R1607 against R0458: unchanged from the prior read (different object, different verb). R1609 against R1218: agree — the value is asked above the block and bound before the run.
- Merges state the rule at its shortest: R1609 does, and in one place shorter than its sources warrant — NB-1. R1607 folds R0188 into one sentence.
- Negation/ban: R1606's "dictate no tree fact" is unchanged in kind; no new negation or ban.
- The `## Human` sections R1220 and R1228 carried do not appear on R1609 — NB-3.
- `source:` on the four amended rows — O-2.

Decision-log entries DEC-000810–DEC-000870 against process/decision-log.md [observed by script and reading]: seven entries; ids run 810 through 870 in steps of ten from DEC-000800, the last entry on e7f5994; 87 ids in the log, all unique; each carries `## DEC-NNNNNN — <title>`, `Date: 2026-09-11`, `Decision:`, `Context:`, no `Supersedes:`, no author field. For DEC-000810, -820, -850 and -860 the topic in parentheses equals the row's `topic:` and the text after "is amended to:" or "is agreed:" equals the landed body byte for byte. For DEC-000830 the text after "is amended to:" is the landed body byte for byte followed by one retirement sentence — O-5. DEC-000840 records the retirement and names R1607 as the carrier, matching the diff. DEC-000870 records the human's restoration ruling and re-reads "deleted" as "retired" — for two of the three entries that say it: NB-2. Context lines name the prior read's findings as the producing directive dictated (810: NB-1 and NB-2; 820: NB-2 and NB-4; 830: NB-3; 840: NB-4; 850: NB-5; 860: the human's stated preference). Decision lines run one or two sentences each.

## Skepticism

Verdict (skepticism): ready

What was verified by running rather than by reading: the five body identities against the producing directive's fenced blocks and the four DEC row identities (script at "$TMPDIR/nb-verbatim.py", output in the run log); the four retired files against their last in-force revisions; the store's exclusion of rules/retired/ by module call and by the two named tests; the citation sweep; the key containment of each retired row in its successor; the key census; the test suite (511 tests, OK, 7 skipped). What this read cannot claim: that any changed row renders in any particular bundle. `bin/bundle --where` refuses on any branch not synced with origin/main [observed on this branch], so every bundle-membership statement above is inferred from the rows' own keys and `bin/bundle --keys`, and becomes observable only after the merge to main. The four retired rows' absence from every query is observed at the module and test level, not at the rendered-bundle level, for the same reason. The delta's bodies and keys were dictated by the producing directive as the human's rulings; this read reports against them and did not relitigate them. The two commits after the package (b743c78, 74ebe08) diverge from the producing directive's "delete", "six entries" and "exactly two commits"; the divergence is the human's ruled restoration under AC-RS-10 and is recorded in DEC-000870 — O-6.

## NB-1 — non-blocking
Claim: R1609 carries R1220's expected-output line but not R1220's constraint on what that line may say, so a number observed only against the local stand-in can now be stated as the block's expected output.
Location: rules/R1609.md:14; rules/retired/R1220.md:14
Evidence: inferred by reading. R1220: "State a block's expected output in one line below the block, saying what was observed in the environment the block will run in, or saying it qualitatively — what to look for, with no number". R1609: "it has been run end-to-end against a local stand-in for the remote … its expected output is stated in one line below it". The merged row names the stand-in as the environment the block was run in and places no condition on the content of the expected-output line. DEC-000830 records R1609 as carrying R1220's obligation.
Consequence: an author who ran the block against a stand-in and observed "3 files" writes "expected: 3 files"; the human's environment prints 4; the author obeyed every clause of R1609, and the row that would have forbidden the number — a number not observed where the block will run — is retired. R0264: "if it merges other rows, it states the rule at its shortest, not the sum of its sources" — shortest, but not shorter than the obligation.
Fix: the human's ruling — either the clause is restored to R1609 in a form of the human's choosing (for instance "its expected output is stated in one line below it, as observed where it will run or qualitatively with no number"), or the human confirms the drop as intended and DEC-000830 stands.

## NB-2 — non-blocking
Claim: DEC-000870 re-reads "deleted" as "retired" for DEC-000800 and DEC-000840 and leaves DEC-000830, which says "rules/R1220.md and rules/R1228.md are deleted", as written.
Location: decisions/log.md:854; decisions/log.md:834
Evidence: observed. Three of the seven new entries carry "deleted" (lines 834, 839) or record the earlier deletion (line 819, DEC-000800); DEC-000870 names two of them. rules/retired/R1220.md and rules/retired/R1228.md exist at 74ebe08 with `retired: R1609`.
Consequence: a reader of the log reconciling DEC-000830 against the tree finds "deleted" with no entry that re-reads it, and the one entry that re-reads the word excludes it by naming the other two; the log's account of R1220 and R1228 disagrees with the tree where its account of R0188 and R1283 does not.
Fix: the human's ruling — one appended entry extending DEC-000870's reading to DEC-000830, or a ruling that "from this entry on" already governs every earlier "deleted" and the two named ids are examples; not the reviewer's to make. Append-only, so no edit to DEC-000830 or DEC-000870.

## NB-3 — non-blocking
Claim: the `## Human` notes R1220 and R1228 carried now live only under rules/retired/, and R1609, which carries their obligation, has none.
Location: rules/R1609.md; rules/retired/R1220.md:16-18; rules/retired/R1228.md:16-18
Evidence: observed. R1228's note: "*Safe to re-run*, not *idempotent* — a block containing a commit, an issue creation, or an append to a log cannot be idempotent, and demanding it would make the rule unfollowable." R1220's note: "A block satisfying only the expected-output rule ships a destructive command with no blast radius stated." R1609 ends at its body. specs/rule-store.md G4: "the human form is never lost"; J3: "no history is lost and no second row says the old thing." Neither the producing directive nor DEC-000830 mentions the notes.
Consequence: the rationale is preserved in files no query returns and no reader of R1609 is pointed to; a later amendment of R1609 that tightens "re-running it compounds no damage" toward idempotent, or that drops the blast-radius clause as redundant with the expected-output line, is made without the two notes that were written against exactly those moves.
Fix: the human's ruling — carry the two notes into R1609's `## Human` (an edit to the human form, not the body, so no DEC is owed by the row's own rule), or rule that a retired file is the human form's home once its obligation moves and G4 is read as satisfied by the retired file.

## O-1 — observation
Claim: R1606's second sentence exempts a pinned ref by name; counts and exit codes in expected-state lines are exempt only by the qualifier "for the executor to land".
Location: rules/R1606.md:14; rules/R1293.md:14
Evidence: observed wording. "a count" remains in R1606's enumeration; R1293 requires counts and exit codes as expected-state lines.
Consequence: none found — an expected-state line is verified, not landed, and no reading makes the two rows conflict; noted because the prior read's NB-1 turned on this pair and the resolution rests on one qualifier.
Fix: none unless the human wants the second sentence to name the expected-state line as well as the ref.

## O-2 — observation
Claim: the `source:` of each amended row still names the first dictation at 4502c64, whose text the body no longer matches.
Location: rules/R1606.md:11; rules/R1607.md:11; rules/R1609.md:11; rules/R1610.md:11
Evidence: observed — all four name docs/cycles/tree-fact-rows-20260911T003000Z.md @ 4502c64; the producing directive ruled "Every key not stated here is unchanged". AC-RS-9 asks only that the source resolve, which it does.
Consequence: a reader following `source:` reaches the superseded wording; the current body's provenance is DEC-000810–DEC-000850 and docs/cycles/tree-fact-rows-nb-20260911T210000Z.md @ f39aadd, reachable from the log, not from the row.
Fix: none — ruled; recorded so the convention for an amended row's `source:` is a known open point.

## O-3 — observation
Claim: R1612's order 205 is the only order in the store that is not a multiple of ten.
Location: rules/R1612.md:4
Evidence: observed — a sweep of `order:` over rules/ and process/ finds no other; decision-layer holds R0262 at 200 and R0100 at 210, and the directive placed the row "after R0262 in that topic", leaving 201–209.
Consequence: none — order is a position within a topic and no rule or test constrains its spacing; the tool sorts numerically.
Fix: none.

## O-4 — observation
Claim: the practice that answers the prior NB-5 — bodies dictated as one-line fenced blocks — is demonstrated by this delta and recorded in no row or entry.
Location: rules/R1610.md:14; docs/cycles/tree-fact-rows-nb-20260911T210000Z.md:89,95,102,108,121
Evidence: observed — five fenced blocks, one line each, five byte-identical landed bodies; R1610's added sentence covers pointer-carried text only; DEC-000850's Context names NB-5 without stating the practice.
Consequence: a future directive that wraps a fenced body at 72 columns fails R1610 as written in the same way the first tree-fact-rows directive did.
Fix: none unless the human wants the practice stated — a row in directive-invariants, or a `## Human` note on R1610.

## O-5 — observation
Claim: DEC-000830's Decision line carries the row body verbatim followed by one retirement sentence, so the body is a prefix of the text after "is amended to:", not the whole of it.
Location: decisions/log.md:834
Evidence: observed by script — prefix match exact; trailing text "rules/R1220.md and rules/R1228.md are deleted; R1609 carries their obligation."
Consequence: none — the producing directive dictated one entry for the amendment and the two retirements together; a script that checks "text after the verb equals the body" needs the prefix form for this entry.
Fix: none.

## O-6 — observation
Claim: the delta diverges from its producing directive in three counts, each by the human's ruled restoration.
Location: docs/cycles/tree-fact-rows-nb-20260911T210000Z.md:111-113,138-146; decisions/log.md:852-855
Evidence: observed — the directive says delete three rows, six entries, exactly two commits after the directive commit; the range holds three renames into rules/retired/ plus one restored file, seven entries, and four commits after the directive commit (7a70b84, 4f2e1c1, b743c78, 74ebe08). DEC-000870 records the ruling and names AC-RS-10 as its ground.
Consequence: none — anticipated by the read directive; recorded so the count in the log's DEC-000870 ("directed deletion twice") and the commit count are on the record together.
Fix: none.

## O-7 — observation
Claim: rendered bundle reach is not checkable pre-merge.
Location: bin/bundle
Evidence: observed — `bin/bundle --where role=chief-of-staff session=decision` prints "refused: HEAD is not synced with origin/main" on this branch; `bin/bundle --keys` and `--near` run and exit 0.
Consequence: every bundle-membership claim in this artifact is inferred from keys, and becomes observable only after the merge to main.
Fix: none; stated so the decision session weighs the inference as such.
