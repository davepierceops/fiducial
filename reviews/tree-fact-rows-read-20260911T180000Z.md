# Review: rules/R1606.md–R1611.md, rules/R1283.md, decisions/log.md — tree-fact-rows-read-20260911T180000Z

Verdict: ready-with-findings
Reviewed: rules/, decisions/log.md @ 6b35460ba1858854e3d024b6e8331123860a1476
Baseline: rules/, decisions/log.md @ d44ad52
Reviewer: Context Quality Reviewer (frontier, fresh session; did not produce the delta)
Date: 2026-09-11
Scope: the diff d44ad52..6b35460 whole — six added rows R1606–R1611, the deletion of R1283, seven appended entries DEC-000740–DEC-000800 — read by dimension: continuity against the store at 6b35460, every new row against every R0264 criterion, every citation against R1605, every entry against the form process/decision-log.md states and against the row it records. Checks run: `bin/bundle --near` (default 0.30 and 0.12 thresholds) plus concept greps for the near-duplicate shortlist; a script diffing each row body against its dictated block at 4502c64 (whitespace-normalised) and against its DEC Decision line (verbatim); a dangling-citation sweep over rules/; a grep for R1283 tree-wide; `bin/bundle --keys` for key reach.
Cross-checked: rules/R0264.md, rules/R1605.md, process/review-artifact.md @ 38aab41, process/decision-log.md @ 6b35460, docs/cycles/tree-fact-rows-20260911T003000Z.md and docs/cycles/tree-fact-rows-fix-20260911T170000Z.md @ 6b35460, rules/R0458.md, R1228.md, R0180.md, R0181.md, R0174.md, R0188.md, R0212.md, R1291–R1293.md, R1312.md, R1218.md, R1220.md, docs/rule-register/ (grep only), retros/retro-20260904T180000Z.md, 20260907T173826Z, 20260908T042500Z, 20260908T160110Z, 20260909T171500Z, 20260910T032500Z, 20260910T223000Z (item counts only)
Not inspected: rendered bundles — `bin/bundle --where` refuses off main ("refused: HEAD is not synced with origin/main", observed), so which bundles each new row lands in is inferred from its keys and `bin/bundle --keys`, not observed; `bin/tests/run` — not named by the directive, not run; the content of the retro Evidence items the DEC Context lines cite — only that the labels resolve to numbered items in retros of the named dates was checked; the two docs/cycles directives in the diff — read as companions, not reviewed as deliverables.
Findings: 0 blocking, 5 non-blocking, 8 observations
The human should inspect: NB-1 (R1606 against R1293 — a wording-scope ruling on "dictate"), NB-3 (R1609's session key, which the producing directive dictated), NB-5 (whether R1610's "byte for byte" admits the whitespace normalisation this very delta needed)

## Continuity

Verdict (continuity): ready-with-findings

Near-duplicate shortlist and judgment, one line per new row [observed: `bin/bundle --near` at 0.30 returned no neighbour for any of the six; at 0.12 and by concept grep the shortlist below; inferred: the distinct/restatement calls]:

- R1606 — nearest R1291, R1292 (pointer vs inline carriage of dictated wording), R1293 (expected-state lines read from the tree), R0256 (self-contained directive). Distinct: none of them says what may be dictated and what must be derived. Tension with R1293 — see NB-1.
- R1607 — beside R0458 as the directive names, plus R0188 (stop when you cannot execute as written) and R0168. R1607/R0458 distinct: R0458 escalates an unclear product, risk, or release decision and carves out "a routine implementation decision that existing guidance resolves"; R1607 resolves a precondition the tree resolves. Same spirit in the carve-out, different object (guidance vs tree; decision vs precondition), different verb (escalate vs stop). Not a restatement. Boundary with R0188 — see NB-4.
- R1608 — replaces R1283; beside R1312 (state route as fresh or existing) and R0212 (defines directive, route line). Replacement, not restatement: R1283 admitted either route and said how an existing session is identified; R1608 mandates fresh for every new directive, confines the existing-session route to amendments, and adds supersession. R1312 and R0212 still describe the route line's form and remain consistent, since the existing-session value survives for amendments. R1284's prohibition ("never by the tree or branch it holds", merged into R1283 per docs/rule-register/store-map-directive-invariants-20260906T020000Z.md:18) is preserved implicitly by "the session whose stopped report it answers" [inferred].
- R1609 — beside R1228 as the directive names, plus R1220 (expected output "as observed in the environment the block will run in") and R1218 (no placeholders; ask the unknown value above the block). Distinct: R1228 states the property a block has; R1609 states the test that establishes it before handover. R1218 and R1609 agree — the value is asked above the block and bound before the run.
- R1610 — nearest R1293, R0176 (a passing check proves the check), R1024 (critic: verify no text differs). Distinct: no row in force names the byte-level diff against the directive's own block. Runnability as stated — see NB-5.
- R1611 — beside R0180 and R0181 as the directive names, plus R1101/R1116 (spec-reviewer entry read), R0896 (read a pasted report yourself). Distinct: R0180 implies the read in general; R1611 contributes the spine list (PRD, TRD, the agreeing DEC entries), "whole", and the classification of a spec-answered question as a read defect. A specialisation with new content, not a restatement.

R1283: no row in force cites it [observed: `grep -rn R1283 rules/` empty at 6b35460; a sweep of every bracketed `[Rnnnn` in rules/ finds no id without a file]. Citations outside rules/ and docs/history: three files under docs/rule-register/ (five lines: store-map-directive-invariants-20260906T020000Z.md:17,18,105; store-fix-2-20260906T050000Z.md:489; rule-register-20260904T210000Z.md:1291), plus DEC-000800 and the two producing directives — see O-1.

R1605: none of the six rows carries a bracketed citation [observed: zero `[R` matches in the six files], so co-rendering is satisfied vacuously.

Placement [observed]: directive-invariants ran to 590 (R1298); R1606/R1607/R1608/R1610 take 600/610/620/630 in dictated sequence. command-blocks ran to 260 (R1228); R1609 takes 270. chief-of-staff ran to 500 (R0937); R1611 takes 510. `source:` values use the store's `path:line @ 7-char-sha` form, and each named line is the first line of the row's dictated block at 4502c64 [observed by script].

## Quality

Verdict (quality): ready-with-findings

Every new row against every R0264 criterion; a row passes a criterion unless named below [observed for keys, citations, paths, model names; inferred for readability, contribution, consistency, trigger]:

- Keys: every role, session, corpus, and topic value on the six rows already exists in `bin/bundle --keys` [observed]. Model names: none. File paths: none — R1611 names the PRD, TRD and decision-log entries by kind, not path. Form vs row: all six are rows. Tool-enforced: none — no tool in the tree performs R1610's diff or R1609's dry run.
- Trigger: R1609 and R1611 state theirs ("Before handing over a block", "Before directing against a spec"); R1606, R1608, R1610 carry it in the imperative's object (a directive being written, routed, verified), in the style R1293 and R1298 already use; R1607 in its subject (a precondition met). One trigger each.
- Terms: R1606 enumerates what a tree fact is inline and the Lexicon has no such term — see O-3.
- Session kind bound: R1606 (NB-2) and R1609 (NB-3).
- Consistency with every rule in force: R1606 against R1293 (NB-1); R1607 against R0188 (NB-4).
- Merges: R1608 states R1283's surviving obligation at its shortest and adds the amendment semantics; it does not sum its sources.
- Negation/ban: R1606's "dictate no tree fact" is paired with a positive obligation the store did not already carry; the incident sits in DEC-000740's Context and the source directive, not in the row — consistent with how R1293 and R1298 were landed.

Decision-log entries DEC-000740–DEC-000800 against process/decision-log.md [observed by script and reading]: seven entries; ids run 740, 750, 760, 770, 780, 790, 800 in steps of ten from DEC-000730, the last entry on d44ad52; 80 ids in the log, all unique; each carries `## DEC-NNNNNN — <title>`, `Date: 2026-09-11`, `Decision:`, `Context:`, no `Supersedes:` (none applies — R1283 was a row, not an entry), no author field. For each of the six row entries, the topic in parentheses equals the row's `topic:` and the text after "is agreed: " equals the row body byte for byte. DEC-000800 records the deletion and names R1608 as the carrier, matching the diff. Sentence count — see O-7.

## Skepticism

Verdict (skepticism): ready-with-findings

What was verified by running rather than by reading: the row-body identities above (script at "$TMPDIR/verbatim.py", results in this session's log); the absence of R1283 from rules/; the absence of dangling citations; the key census. What this read cannot claim: that any new row renders in any particular bundle — `bin/bundle --where` refuses on any branch not synced with origin/main, so reach is inferred from keys alone and is first observable after the merge. The delta's own producing directive dictated R1609's `session: [decision]` and R1607's twelve-role key set; those are rulings the read reports against, not derivations the executor chose.

## NB-1 — non-blocking
Claim: R1606 and R1293 pull opposite ways on whether a directive carries counts and SHAs, and neither row scopes the other.
Location: rules/R1606.md:14; rules/R1293.md:14
Evidence: inferred by reading. R1293 ("Read every expected-state line a directive carries — counts, exit codes, blob SHAs — from the tree at the reviewed ref") requires such lines and governs how they are read; R1606 says "dictate no tree fact — an id, a key value, a position, which rows carry a term, a tool's existence, a count, a SHA". Both are topic directive-invariants, role chief-of-staff, session decision, so both render in the same bundle. The directive that produced R1606 itself carries a base SHA, "six rows", and expected file counts, as this read's directive does.
Consequence: an author holding both rows either strips BASE VERIFICATION and VERIFICATION of their SHAs and counts to obey R1606, breaking R1293 and the invariants form, or reads "dictate" as "instruct to land" without any row saying so. R0264 requires the disagreement raised and left unresolved.
Fix: the human's ruling on the scope of "dictate" — for instance a `## Human` note on R1606 stating that an expected-state line the author read from the tree is not a dictated fact — or a wording amendment; not the reviewer's to make.

## NB-2 — non-blocking
Claim: R1606's second sentence binds the executor, but the row renders only to chief-of-staff in decision sessions.
Location: rules/R1606.md:14
Evidence: observed keys `role: [chief-of-staff]`, `session: [decision]`; the sentence "The executor derives each fact it needs from the tree and reports the derivation with its evidence" states an obligation on the execution session. No execution-session row states "report the derivation with its evidence"; R1607 ("resolved and reported") and R0174 (claim labels) are the nearest. Criterion: "it names the session kind it binds, and says nothing only the other kind needs".
Consequence: the executor's half of the arrangement is stated where the executor never reads it; an execution session that lands an id or an order without reporting the derivation breaks no row in its bundle.
Fix: a ruling — either the sentence is context for the author and stands, or the executor's obligation becomes its own row keyed to execution, or R1606 is keyed to both sessions.

## NB-3 — non-blocking
Claim: R1609 is keyed `session: [decision]` where every other chief-of-staff row in command-blocks is `[decision, execution]`.
Location: rules/R1609.md:5
Evidence: observed — 12 of 14 command-blocks rows carry `[decision, execution]`, the other two are term rows with no session key; R1609 alone carries `[decision]`. The key was dictated by docs/cycles/tree-fact-rows-20260911T003000Z.md ("Row 4 — topic `command-blocks`, role `[chief-of-staff]`, session `[decision]`"). Criterion: "it names the session kind it binds".
Consequence: an execution session handing a block to the human — a case the topic anticipates, since R1213 and R1220 bind execution too — renders R1228 and R1220 but not the rule that the block was run end-to-end first.
Fix: the human confirms `[decision]` as intended, or the row takes the topic's `[decision, execution]`.

## NB-4 — non-blocking
Claim: R1607 and R0188 fire on overlapping events with opposite verbs, and neither names the boundary.
Location: rules/R1607.md:14; rules/R0188.md:14
Evidence: inferred by reading. R0188 (verb stop, session execution, eight roles): "If you cannot execute what you were given as written, stop and surface it rather than proceeding." R1607 (verb require, both sessions, twelve roles): "A precondition the tree resolves with no judgment call and no change of intent is resolved and reported, not stopped on." Every R0188 role is in R1607's role list, so both render together in every execution bundle for those eight roles.
Consequence: a companion named at a SHA the tree does not hold, or a path that moved, is "cannot execute as written" under R0188 and "a precondition the tree resolves" under R1607; the executor picks a row rather than following one. This delta's own producing directive stopped on a citation R1607 would arguably have resolved — the stop the fix directive then had to answer.
Fix: a ruling on which row is the outer one — a `## Human` note on R1607 naming R0188 as the case where the tree does not resolve it, or a wording amendment to either.

## NB-5 — non-blocking
Claim: R1610's check, run as written, fails on the very delta that lands it.
Location: rules/R1610.md:14
Evidence: verified by running. The producing directive carries the six bodies as four-space-indented blocks wrapped at ~72 columns, not fenced blocks; each row file holds its body on one line. A byte-for-byte diff differs on every row; the bodies match only after whitespace normalisation (script result: six of six normalised matches). R1291 also carries pointer-only wording that has no fenced block in the directive to diff against.
Consequence: a decision session obeying R1610 literally either reports every wrapped dictation as a mismatch or normalises silently; either way the check the row demands is not the one that runs.
Fix: a ruling — either row bodies are dictated in fenced, unwrapped blocks from now on, or the row says the diff is taken after whitespace normalisation, or the row admits pointer-carried wording is diffed against its source.

## O-1 — observation
Claim: R1283 remains cited under docs/rule-register/ in three files, five lines.
Location: docs/rule-register/store-map-directive-invariants-20260906T020000Z.md:17,18,105; docs/rule-register/store-fix-2-20260906T050000Z.md:489; docs/rule-register/rule-register-20260904T210000Z.md:1291
Evidence: observed by grep. The human ruled 2026-09-11 that these are dated derived records and stand as written; DEC-000800's Context records "three citations", which counts files.
Consequence: none — recorded, not a finding.
Fix: none.

## O-2 — observation
Claim: R1607's role list is copied from R0458 and matches the twelve-role set R0174 carries.
Location: rules/R1607.md:5
Evidence: observed — identical strings.
Consequence: none.
Fix: none.

## O-3 — observation
Claim: "tree fact" is defined by enumeration inside R1606 and has no Lexicon row.
Location: rules/R1606.md:14
Evidence: observed — no `term:` in rules/ contains "tree fact"; the enumeration ("an id, a key value, a position, which rows carry a term, a tool's existence, a count, a SHA") is illustrative in the style R1293 uses for "expected-state line". Criterion "states what its terms mean nowhere — the Lexicon does" is not clearly breached by an illustrative dash-list.
Consequence: if the term is meant to be load-bearing in NB-1's resolution, a define row would carry it.
Fix: none unless the human wants the term in the Lexicon.

## O-4 — observation
Claim: R1608's "that directive" has no antecedent in its sentence.
Location: rules/R1608.md:14
Evidence: observed — "An amendment goes to the session whose stopped report it answers, supersedes named instructions in that directive" — the directive is the one that produced the stopped report, inferable but unstated. Prose is human-agreed.
Consequence: a first-time reader resolves it by inference; no wrong reading is available.
Fix: none unless the human wants "in the directive that report answers".

## O-5 — observation
Claim: the DEC Context evidence labels resolve to the retros of the named dates.
Location: decisions/log.md:790,795,800,805,810,815
Evidence: observed — retros/retro-20260909T171500Z.md labels its evidence E2–E17; the 09-10, 09-07 and 09-08 retros number theirs 1–19, 1–20, and 1–15/1–9; "09-04 #314" appears in both 09-04 retros. Two retro files carry 09-08 in the filename and one of them is dated 2026-09-07 in its frontmatter, so "09-08 E11" and "09-08 F1" resolve by filename, not by the `date:` field. Item content not inspected.
Consequence: none for the rows; a later reader of the log resolves "09-08" by filename.
Fix: none.

## O-6 — observation
Claim: R1284's prohibition survives R1283's deletion only implicitly.
Location: rules/R1608.md:14
Evidence: observed in docs/rule-register/store-map-directive-invariants-20260906T020000Z.md:18 that R1284 ("never by the tree or branch it holds") was merged into R1283; R1608 identifies the amendment's session by "the stopped report it answers", which excludes tree and branch by construction.
Consequence: none observed.
Fix: none.

## O-7 — observation
Claim: three Decision lines run to three sentences against the form's "one or two".
Location: decisions/log.md:789,799,814
Evidence: observed — DEC-000740, DEC-000760, DEC-000790 carry "Rnnnn (topic) is agreed:" followed by a two-sentence body, as the fix directive dictated.
Consequence: none — the form's count reads as guidance on the ruling's length, and the extra sentence is the verbatim body the fix directive required.
Fix: none.

## O-8 — observation
Claim: rendered bundle reach is not checkable pre-merge.
Location: bin/bundle
Evidence: observed — `bin/bundle --where role=chief-of-staff session=decision` prints "refused: HEAD is not synced with origin/main" on this branch; `bin/bundle --keys` and `--near` run.
Consequence: every bundle-membership claim in this artifact is inferred from keys, and becomes observable only after the merge to main.
Fix: none; stated so the decision session weighs the inference as such.
