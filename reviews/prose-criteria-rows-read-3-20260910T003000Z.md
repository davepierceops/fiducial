# Review: rules delta 8cd16fe..fbc76c4 (branch prose-criteria-rows-c) — prose-criteria-rows-read-3-20260910T003000Z

Verdict: ready-with-findings
Reviewed: prose-criteria-rows-c @ fbc76c4593bc43fd50339ec004bc9016aa22876a
Baseline: prose-criteria-rows @ 8cd16fed025e264f91fcb7c8fc03cc19b2495cd8
Reviewer: Context Quality Reviewer — fresh execution session, sandboxed, worktree `fiducial-prose-criteria-rows-read-3` on branch `prose-criteria-rows-read-3`. I did not produce this delta and no session that did is this one; this satisfies R0462, which reviews/prose-criteria-rows-read-2-20260909T230000Z.md records itself as failing (its O-7).
Date: 2026-09-09
Scope: the whole diff 8cd16fe..fbc76c4 — six files across four commits (4faa17a, 88d4b5b, 9da58a1, fbc76c4): `docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md` and `-amend-c.md` added, `rules/R1605.md` added, `rules/R0038.md`, `rules/R1013.md` and `rules/R1604.md` modified. Read by dimension. Every bracketed citation in the store checked against R1605's constraint at the reviewed ref; R1605 given the near-duplicate shortlist against all 455 rows.
Cross-checked: the two amendment files @ fbc76c4; reviews/prose-criteria-rows-read-20260909T200000Z.md @ 78b0894 (origin/prose-criteria-rows-read); reviews/prose-criteria-rows-read-2-20260909T230000Z.md @ 2fb5a7d (origin/prose-criteria-rows-read-2); R0246, R0264, R0266, R0284, R0944, R0950; R0835, R0844, R0845, R0846, R0849, R0853, R0821; R0186, R0212, R0244, R0474, R0535, R0580, R1018, R1199, R1200; bin/bundle and bin/rulestore/query.py @ fbc76c4.
Not inspected: the rendered role bundles. `bin/bundle --where` still refuses on a branch, so every reach and co-render claim below is read from frontmatter keys against `select()` in bin/rulestore/query.py, not from a rendered bundle — the same instrument, and the same limit, as both earlier reads. Also not inspected: F-6 (R0835's second sentence), O-10 (the two 40-character source SHAs), the process delta at outline.md:12, outline.md:30 and voice.md:11, the parallel-row sweep, and the bin/bundle branch-render gap — all on the loose-end tracker and out of this directive's scope.
Findings: 0 blocking, 1 non-blocking, 3 observations
The human should inspect: F-7 — the constraint R1605 creates does not catch the citation that motivated it. R0038's `[R0821]`, the defect the first read raised as F-2, would pass R1605's test if it returned, because R0038 carries no value on any of the three keys R1605 names. The delta is sound; the row's reach is narrower than its own sentence claims.

## Pass: Resolution

Verdict (resolution): ready

All five findings the directive names are resolved as the amendments rule. Amendment C states it supersedes amendment B where they differ, and where the two disagree the landed state follows C.

**F-1 is resolved (observed).** R1013's body at fbc76c4 reads "Check the piece against every tell in [R0853] and every structure defect in [R0835, R0844, R0846, R0849], and report each occurrence at its location." Four IDs, R0845 absent — amendment C's ruling, not amendment B's five-ID list. R0845 is `verb: define`, `term: [declared series, explicitly declared series]`, and carries no `role`, `session` or `corpus` key; read at fbc76c4, it is neither an obligation nor co-renderable, so its exclusion is correct on both grounds C gives. The four rows that remain each carry `role: [writer, copy-editor, critic]`, `session: [decision]`, `corpus: [writing]` and each answers to "structure defect": restatement (R0835), landing for a cold reader (R0844), skimmable structure and early key terms (R0846), venue-independent prose (R0849). The reach the first read measured as lost — R0844, R0846, R0849 — is restored.

**F-2 is resolved (observed).** `git diff 28dfdb0..fbc76c4 -- rules/R0038.md` is a single body line, deleting "the four tiers the Public Prose Criteria name" and the comma before it; the sentence ends "— relayed, demonstrated, grounded, opinion." and the remainder of the row is byte-identical to 28dfdb0, frontmatter included. No citation remains. This is amendment B's ruling executed literally, and the cleaner of the two fixes F-2 offered.

**F-3 is resolved (observed).** R1605 exists and its body is byte-identical to the text amendment B dictates. It states the convention as a row rather than leaving it undeclared. What it does not do is close the gap F-3 named in full; see F-7 and O-9.

**F-4 is resolved (observed).** Amendment C is committed at 9da58a1 and records all three rulings F-4 said existed only in chat: R1013 cites four rows not five, with the reason; R1605's session is `[decision, execution]`, with the reason; a store-born row's `source:` is `path:1 @ <7-character SHA>`. F-4's optional second half is also done — R1605's `source:` now reads `docs/cycles/prose-criteria-rows-20260909T190000Z-amend-c.md:1 @ 9da58a1`, and 9da58a1 is the commit that added that file and nothing else (`git diff --name-status 88d4b5b..9da58a1` lists one path). The provenance chain closes: the document R1605 cites is the document that states the `session` value R1605 carries. See O-13 for the one divergence C settles only by implication.

**F-5 is resolved (observed).** R1605's `role` is now `[chief-of-staff, writer, copy-editor, critic, context-quality-reviewer]` — R0246's four roles in R0246's order, with context-quality-reviewer appended, exactly as amendment C item 1 rules. The selection F-5 used to demonstrate the gap now returns both rows: `--where role=chief-of-staff session=decision` matches R0246 (`role` contains chief-of-staff, `session` contains decision) and matches R1605 (same, on a session superset). The authoring roles carry the constraint; the gating role still does. R1605 also still co-renders with R0264 — R0264's `role: [context-quality-reviewer]`, `session: [execution]`, `corpus: [software, writing]` are all values R1605 carries, and adding role values only widens what returns it.

## Pass: Continuity

Verdict (continuity): ready

**Near-duplicate shortlist for R1605, run independently (observed).** Swept all 455 rows at fbc76c4 for citation, cross-reference, bracket, ID-resolution and bundle-rendering language. Ten candidates: R0186, R0212, R0244, R0266, R0474, R0535, R0580, R1018, R1199, R1200 — the same ten the self-review reached, arrived at from the sweep and not from its list. Read whole: R0186, R0266 and R1018 are finding-citation rules (cite the location, the intake criterion, the Voice line); R0244 and R0580 concern DEC IDs in `decisions/log.md`, a different reference space with its own resolution mechanism; R0212 defines how a directive is cited, by path and SHA; R0474 cites a branch and pins a SHA; R1199 and R1200 concern capturing command output. R0535's "cites it from other topics" describes why the consequential class is stated in one place, not how a row references another. **R1605 restates no surviving row.** The test matters more than it did at 88d4b5b, because the widened `role` puts R1605 into four bundles it did not previously render in: of the ten candidates, R0244 (chief-of-staff, writer, copy-editor, critic; decision) and R0186 (all roles) are the two that now share a bundle with it, and neither states a row-to-row citation rule. R0264's "contributes something no rule already in its bundles does" holds across the widened set.

**Every bracketed citation in the store satisfies R1605's constraint (observed).** Swept `rules/` at fbc76c4 for `[Rnnnn]`: exactly one citing row, R1013, carrying five citations. R0038's citation is gone; R1605 cites nothing and holds vacuously. Checked each citation by parsing both rows' `role`, `session` and `corpus` lists and testing that every value the citing row carries the cited row carries too.

| Citing | Cited | role | session | corpus | Result |
|---|---|---|---|---|---|
| R1013 `[critic] [decision] [writing]` | R0853 | ✓ | ✓ | ✓ | HOLDS |
| | R0835 | ✓ | ✓ | ✓ | HOLDS |
| | R0844 | ✓ | ✓ | ✓ | HOLDS |
| | R0846 | ✓ | ✓ | ✓ | HOLDS |
| | R0849 | ✓ | ✓ | ✓ | HOLDS |
| R0038 | — | | | | cites no row |
| R1605 | — | | | | cites no row; holds vacuously |

No citation dangles: every cited ID resolves to a row present at fbc76c4. The three IDs the earlier delta retired stay retired — `grep -rn 'R1161\|R0953\|R1001' rules/ process/` returns zero hits.

**Allocation and shape are clean (observed).** Row count 455 — 454 at 8cd16fe plus R1605, no deletions in this range. R1605 is the highest ID in the store and was absent at 8cd16fe. Order 60 is the tail of the `intake` topic, previous maximum 50 (R0950), no collision. Filename matches the `id:` field for all 455 rows. R1604's only change in this range is its `source:` value, from a 40-character SHA with no line component to `:1 @ ca9fd54` — O-5's and O-10's form question settled for this row in the direction amendment C rules. R0038 and R1013 changed one body line each and nothing above the closing `---`. No row outside the four the directive names was touched.

## Pass: Record

Verdict (record): ready

**The committed record now describes the delta that landed (observed).** Read the four directive files for this package at fbc76c4 — `prose-criteria-rows-20260909T190000Z.md`, `-amend-a.md`, `-amend-b.md`, `-amend-c.md` (see O-12) — against the tree they sit in. Amendment C's three ruled edits each landed as written: item 1, the role list, verbatim in the ruled order; item 2, the `source:` value, at the SHA C's own first act produced; item 3, "nothing else changes" — `git diff --stat 88d4b5b..fbc76c4` is two files, 108 insertions, 2 deletions, and the 106 insertions are amendment C itself. The content commit message on fbc76c4 is byte-identical to the string C prescribes. The first-act commit 9da58a1 carries the amendment file alone under a message naming the package it opens.

**The gap F-4 raised is closed rather than papered over (observed).** A reader arriving at this branch and finding amendment B's five-ID list now finds amendment C in the same directory, stating that it supersedes B where they differ and giving the reason for each correction. R0170's requirement — that nothing surviving the session rests on chat alone — is met for all three rulings. What the record does not do is restate the correction to B's prescribed commit message; that is O-13.

## Pass: Quality

Verdict (quality): ready-with-findings

R1605 tested against every criterion in R0264 at its landed keys. It is readable in a bundle with no other file open: the body names no file, defines its own idea inline before using the compound, and needs neither R0264 nor the intake topic around it to make sense. It carries `topic`, `role`, `session` and `corpus` values that all already exist in the store — the five role values and both session values are in use on rows this delta did not touch. It names the session kinds it binds. It speaks no model name. It contributes what no surviving row does. It states an obligation. It has one trigger, stated in the body: "A row cites another row". It is a row, not a document's form. It is not a negation or a ban. Two criteria are strained rather than failed and are already recorded as O-8 (the uncoined "co-render") and O-9 (a constraint a tool could enforce); this read reaches the same conclusion on both and adds nothing to them.

The criterion it does not cleanly pass is "it is consistent with every rule in force" — read against its own second clause rather than against another row. See F-7.

The three edited rows are minimal and correct. R0038's is a pure deletion off the 28dfdb0 text. R1013's changes only the bracket list. R1604's changes only the `source:` value.

## F-7 — non-blocking
Claim: R1605 tests a citation against three named keys, but a bundle is selected on any key and a citing row may carry none of the three, so the constraint does not guarantee the co-rendering its own sentence gives as its purpose — and it would not have caught the citation that produced it.
Location: rules/R1605.md:14
Evidence: the body reads "…only where every value the citing row carries on role, session, and corpus the cited row carries too, so the cited row renders in every bundle the citing one does." Two ways the test and the purpose come apart, both read at fbc76c4. **First, the vacuous pass.** 78 of 455 rows carry no `role` key at all; R0038 is one, carrying only `topic`, `order`, `verb`, `condition`, `source`, `term`. A row carrying no value on role, session or corpus satisfies "every value the citing row carries" for any cited row whatever, because it carries none — so R0038 citing R0821 passes R1605's test. It also cannot co-render with R0821 under any selection: `select()` in bin/rulestore/query.py refuses a row missing the queried key (`if not values or value not in values`), so no `--where role=…`, `session=…` or `corpus=…` returns R0038, and no `--where topic=lexicon` returns R0821, whose topic is `public-prose-criteria`. That is exactly the pairing the first read raised as F-2 and the delta resolved by deleting the citation. The constraint written to prevent its recurrence does not reach it. **Second, the omitted key.** `parse_where` in bin/rulestore/query.py accepts any `k=v`, and bin/bundle's `--where` passes it straight through, so `--where topic=critic` is a legal bundle. It returns R1013 and not R0835, R0844, R0846 or R0849, whose topic is `public-prose-criteria` — five citations that pass the constraint and still do not co-render. Verified by reading `select()` and `parse_where` at fbc76c4 and by testing the key lists directly; not verified against a rendered bundle, per `Not inspected`.
Consequence: no citation in the store violates R1605 today, and none of the five that exist is at risk — R1013 is keyed and the four cited rows carry its values. The exposure is forward. The constraint reads as a guarantee of co-rendering and is a guarantee only for a citing row that carries at least one of the three keys, and only for selections over those three. A keyless row — a Lexicon definition, most of the 78 — can acquire a citation to anything at all and pass intake with the constraint applied honestly. R0264 requires that a row be consistent with every rule in force and that disagreement be raised as a defect; here the disagreement is inside one row, between the test its second clause states and the outcome its third clause promises, which is a harder defect to notice than a disagreement between two rows.
Fix: two directions for the decision session, neither taken here. Quantify rather than enumerate — state the rule over every selector key the store selects on, so a new key does not silently fall outside it — and say what a citing row carrying no selector key may do: either forbid it a citation outright, which reads straight and matches R0845's exclusion from R1013, or state that such a row cites nothing it cannot co-render with by topic. The second direction is O-9's: a test would decide the question per citation rather than per key, and would not need the enumeration at all.
Related: F-2, F-3, O-9

## Pass: Skepticism

Verdict (skepticism): ready-with-findings

The delta does what amendment C tells it to do, exactly, and what amendment C tells it to do is what the earlier findings asked for. Both blocking findings this read was pointed at are genuinely closed rather than argued away: F-4 by a committed amendment that names its own supersession, F-5 by the widening that makes the demonstrating selection return both rows. I looked for the failure modes that a correction-of-a-correction invites and did not find them — no row outside the named four moved, no citation dangles, no order collides, the ID is highest-plus-one, the source form now agrees with 451 of 455 rows, and the commit messages match the strings the amendments prescribe.

Where this read differs from its predecessor is F-7, and the difference is a consequence of position rather than of care. The self-review checked every citation in the store against R1605 and reported, correctly, that all of them hold. That is the right check and it passes. The question it did not ask is whether holding is the same thing as co-rendering, and the case that separates them is the one the reviewing session had itself deleted an hour earlier. Nothing about that is self-serving; it is simply hard to re-open a defect you have just closed. It is the argument for this read existing, and the only claim in this artifact that the earlier two could not have been expected to reach.

**Supplementary, not a step this directive names:** `bin/tests/run` at fbc76c4 in the assigned worktree — result stated in the report accompanying this artifact, with the log path. The one `ResourceWarning` from `bin/tests/test_check_directive.py:943` is the pre-existing unclosed-handle noise the first read recorded; it is unrelated to this delta. Reported as evidence, not as a gate. No test in the suite resolves a bracketed ID, so the suite passing says nothing about F-7 either way — O-9's point, restated where it bites.

## O-11 — observation
Claim: R1605 is now the only `intake`-topic row that reaches any role but the Context Quality Reviewer or any session but execution, so four role bundles acquire the intake topic as a single row.
Location: rules/R1605.md:5-6, against rules/R0264.md, R0266.md, R0284.md, R0944.md, R0950.md
Evidence: read the keys of all six `intake` rows at fbc76c4. R0264, R0266, R0284, R0944 and R0950 each carry `role: [context-quality-reviewer]` and `session: [execution]`, at orders 10 through 50. R1605 carries five roles and `session: [decision, execution]` at order 60. A `--where role=writer session=decision` selection therefore returns R1605 and no other intake row, and `sort_key` places it by the `intake` topic's position in the sequence list regardless.
Consequence: cannot be stated concretely, which is why this is an observation. R1605's body is self-contained — it names neither intake nor R0264 — so a Writer meeting it alone can follow it, and R0246 gives that Writer a reason to hold it. Whether a lone row under a topic heading named for work that role never does reads as misplaced is a question about the rendered bundle, and `bin/bundle --where` refuses on a branch, so this read could not look. Worth a look once the branch merges.
Fix: none proposed. If it reads badly, the constraint may want a topic whose reach already spans the authoring and gating roles — which was the second half of F-5's Fix, and remains available.

## O-12 — observation
Claim: this directive names "the three directive files" for this package; there are four.
Location: this directive's TASK region; `docs/cycles/` at fbc76c4
Evidence: `ls docs/cycles/ | grep prose-criteria-rows` at fbc76c4 lists `prose-criteria-rows-20260909T190000Z.md`, `-amend-a.md`, `-amend-b.md`, `-amend-c.md`, plus this read's own directive file. The first read records two directive files in 28dfdb0..8cd16fe — the original and amendment A — and this delta adds two more. Neither the whole package nor this delta's share of it comes to three.
Consequence: none to the delta. The record pass above was run over all four, which is the superset either reading would want, so the count does not change what was checked.
Fix: none. Recorded because a count in a directive is a claim, and this one is off by one.

## O-13 — observation
Claim: amendment C settles the commit-message divergence F-4 raised only by implication.
Location: docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md and `-amend-c.md` @ fbc76c4, against the message on 88d4b5b
Evidence: F-4 listed three divergences between amendment B and the tree at 88d4b5b, the third being that B prescribes the content commit message "…R1013 cites five structure rows…" while 88d4b5b reads "…four structure rows…". Amendment C rules the four-ID list explicitly and gives the reason, but does not name the message. Read both amendments whole.
Consequence: a reader who reaches the divergence through the commit log rather than through the row has to carry C's ruling back to B's message themselves. The inference is one step and unambiguous, which is why this is an observation and not a finding.
Fix: none proposed. The substantive ruling is recorded; the message follows from it.
