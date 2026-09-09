# Review: rules delta 8cd16fe..88d4b5b (branch prose-criteria-rows) — prose-criteria-rows-read-2-20260909T230000Z

Verdict: changes-required
Reviewed: prose-criteria-rows @ 88d4b5b8eaed45b58edb95e21436f9aed99d7474
Baseline: prose-criteria-rows @ 8cd16fed025e264f91fcb7c8fc03cc19b2495cd8
Reviewer: the execution session that landed reviews/prose-criteria-rows-read-20260909T200000Z.md at 84e6e40 — **and that also executed this delta**. See O-7: this artifact does not satisfy R0462 and is not an independent gate.
Date: 2026-09-09
Scope: the whole diff 8cd16fe..88d4b5b — five files: docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md added, rules/R1605.md added, rules/R0038.md, rules/R1013.md and rules/R1604.md modified. Two commits, 4faa17a and 88d4b5b. Checked against amendment B's triage of F-1, F-2, F-3; R1605 given the near-duplicate shortlist against all 455 rows at the reviewed ref; every bracketed row citation in the store re-checked against R1605's own constraint.
Cross-checked: docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md @ 88d4b5b; reviews/prose-criteria-rows-read-20260909T200000Z.md @ 78b0894 (fetched from origin/prose-criteria-rows-read); R0264 and the four other `intake`-topic rows; R0246 (proposing a row in a decision session); R0170, R0462; R0835, R0844, R0845, R0846, R0849, R0853; R1601, R1602, R1604; bin/rulestore/query.py.
Not inspected: the rendered bundles — `bin/bundle --where` still refuses on a branch, so every reach and co-render claim below is read from frontmatter keys against `select()` in bin/rulestore/query.py, not from a rendered bundle. `bin/tests/run` was not re-run for this read; it passed at this same tree during the delta's own execution and nothing in this read's scope would change it. Also not inspected: anything on the first read's loose-end tracker — O-3, the process delta, the branch-render gap — all out of scope by this directive.
Findings: 2 blocking, 1 non-blocking, 4 observations
The human should inspect: F-4 first — the committed directive record at 88d4b5b describes a delta that is not the one that landed, and the rulings that produced the landed state exist only in session chat. Then F-5, and then O-7, which is why this artifact should not be the last word on this branch.

## Pass: Resolution

Verdict (resolution): changes-required

**F-2 is fully resolved (observed).** R0038's body now reads "…— relayed, demonstrated, grounded, opinion. It is a property of the assertion, not of where the knowledge came from: claim strength and provenance class are independent axes." The phrase and its preceding comma are gone; the remainder is byte-identical to 28dfdb0; the row carries no citation. The unresolvable `[R0821]` reference F-2 raised is gone rather than repaired, which is the cleaner of the two fixes F-2 offered.

**F-3 is resolved in substance (observed).** R1605 exists, carries the ruled body verbatim, and states the constraint as a row. Every bracketed citation in the store now satisfies it — the check below was run against the reviewed ref and returns `CONSTRAINT HOLDS FOR EVERY CITATION`:

| Citing | Cited | role | session | corpus | Result |
|---|---|---|---|---|---|
| R1013 `[critic] [decision] [writing]` | R0853 | ✓ | ✓ | ✓ | HOLDS |
| | R0835 | ✓ | ✓ | ✓ | HOLDS |
| | R0844 | ✓ | ✓ | ✓ | HOLDS |
| | R0846 | ✓ | ✓ | ✓ | HOLDS |
| | R0849 | ✓ | ✓ | ✓ | HOLDS |
| R0038 | — | | | | cites no row |
| R1605 | — | | | | cites no row; holds vacuously |

R1605's reach is F-5.

**F-1 is resolved in its first half only.** R0845 is correctly absent from R1013's list — it is `verb: define` with `term: [declared series, explicitly declared series]` and carries no `role`, `session`, or `corpus` key, so it is neither a defect nor co-renderable. The four rows that remain all co-render. The second half of F-1's `Fix` was not ruled on; see F-6.

## F-4 — blocking
Claim: The only committed directive record for this delta describes a different delta from the one that landed, and the rulings that produced the landed state exist nowhere but session chat.
Location: docs/cycles/prose-criteria-rows-20260909T190000Z-amend-b.md @ 88d4b5b, against rules/R1013.md:14 and rules/R1605.md:6 at the same ref
Evidence: read the committed amendment whole at 88d4b5b and diffed its instructions against the tree it sits in. Three divergences. (a) The amendment rules R1013's body verbatim as `[R0835, R0844, R0845, R0846, R0849]` — five IDs; the landed body carries four, R0845 absent. (b) The amendment rules R1605 `session [decision]`; the landed row carries `session: [decision, execution]`. (c) The amendment prescribes the content commit message "…R1013 cites five structure rows…"; the actual message on 88d4b5b reads "…four structure rows…". The corrections that produced the landed state — drop R0845, widen the session key, keep the source form — were issued as a reply in the execution session and were never written to a file. `git diff --name-status 8cd16fe..88d4b5b` lists one directive file, `amend-b`; there is no amendment C. Verified by running the diff and reading both files; the absence of a further directive file is observed from the name-status listing.
Consequence: R0170 requires that anything which must survive the session exist as an artifact before the session ends, and that chat never be the sole record of a decision. Three rulings — one of them the correction of a defect that would have made the delta violate the rule it creates — have no committed record. A reader arriving at this branch, or at `main` after it merges, finds a directive that says R1013 cites five rows and a row that cites four, with nothing on disk explaining the gap. The natural reading is that the executor disobeyed the directive. The store's own provenance chain also breaks: R1605's `source:` points at `amend-b.md:1 @ 4faa17a`, a document that does not state the `session` value R1605 actually carries.
Fix: write the reply-ruling to a committed file — an amendment C at this branch's tip recording the three corrections and naming 88d4b5b as the commit they produced — and, if the store wants the provenance exact, repoint R1605's `source:` at it. Not done here; this is a decision-session act, and R0166 leaves it there.
Related: F-5

## Pass: Continuity

Verdict (continuity): changes-required

**Near-duplicate shortlist for R1605 (observed).** Swept all 455 rows at the reviewed ref for citation, cross-reference, bracket, and bundle-rendering language. Ten candidates: R0186, R0212, R0244, R0266, R0474, R0535, R0580, R1018, R1199, R1200. None states a row-to-row citation rule. The closest two are R0244 ("check decisions/log.md for an entry that already governs it and cite it by ID") and R0580 ("A DEC ID is a decision's resolvable handle") — both concern DEC IDs in `decisions/log.md`, a different reference space with a different resolution mechanism. R0186, R0266, and R1018 are finding-citation rules: cite the location, cite the criterion, cite the Voice line. R0212 defines how a directive is cited, by path and SHA. **R1605 restates no surviving row** — R0264's "contributes something no rule already in its bundles does" is satisfied.

**R1605 co-renders with the intake gate (observed).** R0264, the row listing the intake criteria, carries `role: [context-quality-reviewer]`, `session: [execution]`, `corpus: [software, writing]`. R1605 carries the same role and corpus and a session superset, so any selection returning R0264 returns R1605. The half of the ruling about the gating session holds. The half about the authoring session does not; see F-5.

**Nothing in the diff falls outside the first read's coverage (observed).** Five files, all four rules rows named in F-1, F-2, F-3 or the source-form observation O-5. No row outside that set changed; no row was deleted; the three retirements from the earlier delta are untouched and no citation of R1161, R0953, or R1001 has reappeared. R1604's only change is the `source:` value.

## F-5 — blocking
Claim: R1605's `role` key confines it to the Context Quality Reviewer, so it never reaches the roles that actually propose row bodies in a decision session — which is half of what the ruling that set its session key said it must govern.
Location: rules/R1605.md:5
Evidence: R1605 carries `role: [context-quality-reviewer]`. R0246 — "A standing rule the human states aloud is proposed as a row in the same turn" — carries `role: [chief-of-staff, writer, copy-editor, critic]`, `session: [decision]`, and is the row governing the act of proposing a row in a decision session. R1270 carries the same four roles for a methodology change a retro proposes. None of those four roles carries R1605; verified by reading the role lists of all three rows at 88d4b5b. The session key was widened to `[decision, execution]` on the stated ground that the constraint "governs the session that dictates a row body and the session that gates it, and it must render in both" — but a `--where role=chief-of-staff session=decision` selection returns R0246 and not R1605, because `select()` requires every named key to match and R1605's role list excludes chief-of-staff. The widened session key changes reach only for the one role R1605 already named.
Consequence: this cycle demonstrates the failure. The decision session dictated R1013's body with `[R0845]` in it — a citation R1605 defines as a defect, to a row that carries none of the three keys. The constraint was not in that session's bundle, and the defect was caught only downstream, at execution, by a script written for the occasion. The next dictated body has the same exposure: the author cannot see the rule, and the only backstop is a reviewer who may not think to run the check.
Fix: extend R1605's `role` to the roles that propose rows — at minimum chief-of-staff, matching R0246 — or move the constraint to a topic whose reach already spans both the authoring and the gating roles. Either changes what bundles R1605 renders in, so it is a decision-session ruling, not a reviewer's edit.
Related: F-4

## F-6 — non-blocking
Claim: The second half of F-1's `Fix` was never ruled on: R0835 is still cited as a container of structure defects while its own second sentence withholds structure from the defect set.
Location: rules/R1013.md:14, against rules/R0835.md:14
Evidence: F-1 asked for a ruling on two things — which rows constitute the structure defects, and "whether R0835's second sentence belongs in a row cited as a defect container." Amendment B ruled the first ("accept", then the corrected four-ID list) and is silent on the second. R0835 at 88d4b5b is unchanged and still reads "Say each point once; cut restatements. Length and structure are the author's call per piece." R1013 at 88d4b5b still opens the list with it. Verified by reading both rows at the reviewed ref and re-reading F-1's Fix field at 78b0894.
Consequence: a Critic following R1013 to the first row in its structure-defect list lands on a sentence saying structure is the author's call. The contradiction R0264 requires be raised as a defect is still in force, one row narrower than before but not removed. In practice a Critic may under-report structural defects on the reasoning that R0835 disclaims the axis.
Fix: rule on whether R0835's second sentence stays. If it stays, R1013's phrase "every structure defect in" may want different wording for that row; if it goes, R0835 becomes a clean restatement rule and the citation reads straight. Left unresolved here per R0264.
Related: F-1

## Pass: Quality

Verdict (quality): ready-with-findings

R1605 tested against every criterion in R0264. It is readable in a bundle with no other file open; refers to no file by path; carries `topic`, `role`, `session`, `corpus` values that all already exist in the store; names its session kinds; speaks no model name; contributes what no surviving row does; states an obligation rather than describing; has one trigger, stated in the body ("A row cites another row"); is a row and not a document's form; is not a negation or a ban. Order 60 is the tail of the `intake` topic with no collision, and the ID is highest-plus-one. Two criteria are strained rather than failed — O-8 and O-9.

The two body edits are minimal and correct: R0038's is a pure deletion off the 28dfdb0 text, R1013's changes only the bracket list. R1604's frontmatter changed on one line and nothing else.

## Pass: Skepticism

Verdict (skepticism): ready-with-findings

The delta does what the reply-ruling told it to do, and the constraint it creates is satisfied by every citation in the store. The exposure is not in the rows — it is in the record (F-4), in the constraint's reach (F-5), and in who is signing this artifact (O-7). Two of those three are things the first read could not have caught, because they were created by the triage rather than by the delta under review. That is the argument for a re-read existing at all, and also the argument that this particular re-read should not be the one that closes the branch.

## O-7 — observation
Claim: This artifact is a self-review: the session writing it also executed the delta it reviews, which R0462 forbids.
Location: this file; the delta at 88d4b5b, commits 4faa17a and 88d4b5b
Evidence: R0462 — "Never approve, review, or gate an artifact you produced or a document you drafted" — is in this role's bundle at `core` order 380. This session wrote R1605, edited R1013, R0038 and R1604, and authored both commits in the reviewed range. The directive routes the re-read to "the session that landed docs/cycles/prose-criteria-rows-read-20260909T200000Z.md at 84e6e40", identifying it by its first read rather than by its authorship of the delta; whether the decision session tracked that these are the same session is unknown to me.
Consequence: every verdict above is a self-assessment. The two blocking findings survived it, which is some evidence the read was not merely self-serving, but a reader cannot distinguish a clean self-review from one that missed what it had a stake in missing. R0462 exists precisely because that distinction cannot be made from the artifact.
Fix: treat this as a working read, not a gate. An independent session should run the read before this branch merges, and this artifact should be an input to it rather than a substitute for it.

## O-8 — observation
Claim: R1605 coins "co-render", a term defined nowhere in the Lexicon.
Location: rules/R1605.md:14
Evidence: swept all 455 rows at the reviewed ref — "co-render" appears in R1605 and nowhere else, and no `lexicon`-topic row mentions rendering at all. R0264 requires that a row "states what its terms mean nowhere — the Lexicon does".
Consequence: cannot be stated concretely, which is why this is an observation: R1605's first sentence defines the idea inline ("so the cited row renders in every bundle the citing one does") before the second sentence uses the compound, so a reader with no other file open can follow it. The exposure is only that a second row wanting the term has nowhere to point.
Fix: none proposed. If the term spreads, it wants a Lexicon row.

## O-9 — observation
Claim: R1605 states a constraint a tool could enforce, which R0264 says belongs to the tool.
Location: rules/R1605.md:14
Evidence: R0264 — "it is not a rule a tool enforces; that rule is the tool's". No tool in the store enforces this one: swept `bin/` for bracketed-ID handling and found only `BRACKET_CODE_RE` in bin/tests/helpers.py, which matches lowercase codes, not row IDs. The check that produced this artifact's constraint table is a throwaway script, not a committed test. F-3's Fix offered the row and the test as alternatives and the decision session took the row.
Consequence: cannot be stated concretely — the row is not currently a tool's rule, so the criterion is not breached today. Recorded because a row and a test are not exclusive: the row states the norm for a human and an agent, and a test would catch the violation the norm forbids. Without the test, the norm is enforced only by a reviewer who thinks to check.
Fix: none here. Worth reconsidering alongside F-5, since both concern how the constraint actually reaches the point of violation.

## O-10 — observation
Claim: the `source:` form is now uniform on the line component but still split on SHA length across the four cycle-sourced rows.
Location: rules/R1604.md:9, rules/R1605.md:10, against rules/R1601.md and rules/R1602.md
Evidence: all four now carry `path:1 @ <sha>`. R1601 and R1602 carry forty-character SHAs; R1604 and R1605 carry seven. Amendment B ruled "the exact form the two other cycle-sourced rows use — short SHA of the same length, and the line component", and the reply confirmed `path:1 @ 7-char SHA` as correct. The two rows named as the model were not changed to match, and are outside this delta's blast radius.
Consequence: the store's dominant form is the seven-character SHA — 451 of 455 rows — so R1604 and R1605 now agree with the store and disagree with the two rows the ruling pointed at. Nothing breaks; all four values resolve by hand.
Fix: none here. If the store wants one form, R1601 and R1602 are the outliers to bring in, in a delta that owns them.
