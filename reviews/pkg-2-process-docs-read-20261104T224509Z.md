---
review: package 2 — process documents
delta: 19f6760..22ec05b (branch pkg-2-process-docs)
read: 2026-11-04, by a reviewer subagent that wrote none of it; first read over 19f6760..7a24eeb (changes-required), re-read over 7a24eeb..22ec05b (ready-with-findings); F-11 and F-12 applied by the decision session without a further read (DEC-001000)
---

# Review: pkg-2-process-docs — read-20261104

Verdict: changes-required
Reviewed: origin/pkg-2-process-docs @ 7a24eeb
Baseline: origin/main @ 19f6760
Reviewer: reviewer subagent (did not write the package)
Date: 2026-11-04
Scope: the ten package commits 01a6a43..7a24eeb (2b79269 skipped as instructed); every file under process/ and docs/history/; the two test files; the 39 cited rows read whole; the chief-of-staff/decision and coder-agent/execution bundles rendered through bin/rulestore at 7a24eeb and the process band read beside the rows.
Cross-checked: docs/plans/subtraction-plan-20261104.md §2 and the rulings section; SPEC.md §4, §7; DEC-001090, 001160–001210, 001230, 001250–001300, 001360, 001450, 001480–001490, 000600, 000920; issues #389 and #364 via `gh api`; `git show 19f6760:process/change-flow.md`.
Not inspected: bin/hooks/ (does not exist yet — package 3's); the coder's claim of 15 retired citations replaced (not recounted; the end state is what was checked).
Findings: 1 blocking, 9 non-blocking, 3 observations
The human should inspect: F-1 (where the consequential go sits in the six stages — this is what package 4's gate skill will be built from).

Note on the `role: [chief-of-staff]` key on project-setup.md: the coordinator reported mid-read that the human ruled 2026-11-04 that the document renders to the Chief of Staff, DEC appended at merge. Not raised. For the record, observed: no DEC forbids the key; the 2026-09-06 drop is only commit 85f6e43's message and DEC-000600's Context line ("no bundle selects it").

## Continuity

Verdict (continuity): ready-with-findings

Checked, observed:
- All 39 cited ids are files under rules/, none under rules/retired/ (loop over every `R####[a-z]?` in process/*.md).
- No process file names docs/history, directive-invariants, decomposition, spec-test-suite, prd-template or trd-template. Grep for directive, baton, tranche, PRD, TRD, convergence, execution session, courier, frontier, bin/land, cycle-open, FIRST ACT, agree/agreed across process/ (voice/outline excluded): one hit, review-artifact.md:64 "or a reconciliation" (F-6).
- voice.md and outline.md: `git diff 19f6760..7a24eeb` empty for both; also empty against 3c686e0.
- Blast radius: `git diff --stat 19f6760..7a24eeb -- . ':!process' ':!docs/history'` is bin/tests/test_directive_trd.py, bin/tests/test_rulestore.py, decisions/log.md (the last from 2b79269, excluded by the brief). Two of the three amended test files touched. In radius.
- The five docs/history copies are byte-identical to their 19f6760 originals after the one-line header; each header names its DEC (001160; 001190+001460; 001190; 001210; 001210).
- Attribution spot-check: 36 of 39 say what the document attributes to them. The three that do not: R0570 cited for "flows to release on its evidence under standing authorization" (F-2); R1614 generalised from "non-blocking finding" to "a finding" (F-4); R0065 cited for "a reviewer that did not write the plan" (R0065 says Reviewer/Skeptic perform every review, a plan before it dispatches; the did-not-write half is R0462 — acceptable, noted only).
- spec-template.md against R0863: all seven items present or placed (structure/approach, components/interfaces, external dependencies, failure modes, Top K SLO+measurement+alerting, NFR targets; the "special attention" list is a drafting instruction, not a section, and is rightly not a section). R0497 cited for deploy-vs-release. R0862b cited to push per-change design out. Against docs/history/trd-template.md: the SLO subsection (§2) and the standing verification-boundary subsection (§4) are carried verbatim in substance. SPEC.md §4's sentence on where those two live is satisfied.
- Dropped "Data and state" and "Operational concerns": no live row requires either as a spec section. R0074 and R0147 are per-change obligations (verification topic). R0798/R0799 and the verification-boundaries topic require only the standing boundary section, which is carried. R0499/R0500 (spec topic, flags) are live and not cited — observation O-1. R0561 retired under DEC-001210 with no successor sentence naming those sections. Judged: the drop is sound; nothing in the store now asks for them.
- Restatements of a live row's obligation where a cite would do (SPEC.md §4 one source): review-artifact.md:60 restates R1414's last sentence verbatim beside the cite (F-7); project-setup.md:27–28 restates R0564's Human-note sentence (F-8); retro.md:17 restates R1244 beside its cite (minor, folded into F-7's fix). change-flow's six step lines paraphrase cited rows in a few words each; judged as the document's own content (the sequence), not restatement.

## Quality

Verdict (quality): changes-required

- change-flow.md 82 → 41 lines, what the 82 carried that no row carries now: (a) "every pull request gets a code review by an agent, no trivial-change exemption, no human diff-read by default" — survives only in R0570's `## Human` note, which bundles never render; the new table's Code row and step 4 do not say it (F-3). (b) The continuity pass with its own verdict — review-artifact.md:58–59 still names three pass sections (quality, skepticism, continuity) while change-flow step 4 names two; R0492 names two (F-5). (c) "A blocking finding reopens the delta; closes on one more read over the diff since then" — R1614 carries the human-raise case only; what a reviewer's own `changes-required` does is now stated nowhere (F-4). (d) Size call — dropped, the harness's; fine. (e) Mechanical checks (R0493), quality/skeptic criteria (R0487/R0488), spec reopen (R1602 → R0006): all carried by live rows; fine.
- Six-stage order vs R0470's retirement: R0470 (per-change stages in order) retired under DEC-001190 "sequencing is the harness's", yet the plan itself dictates "spec, plan, build, review, gate, release" and package 4's build skill needs an order to encode. Consistent with the plan. But step 5 places a gate at the merge, which R0570 ("No human gate fires at the merge; the gate is the release decision") and R0534's note ("it is the release, not the merge, that the go covers") deny — F-1.
- review-artifact.md naming rule vs DEC-001450: stem = branch slug, matches; descriptor `read` is the doc's addition, consistent with DEC-001480's `reviews/pkg-1b-store-bodies-read-…`. Unrun-pass section vs R1617: matches the row's words except the doc's form "stating why in place of a verdict" collides with R1414's hook as the row describes it (F-9).
- project-setup.md fallback vs DEC-001230's sentence ("on a GitHub Free repo the forge layer is absent and the hook is the only layer"): carried. Vs #389 item 2's proposal (accepted-risk DEC naming the plan that restores the forge layer, runner deny in force, PR-only landings, re-examined on plan change): all four present. The brief's pointer to DEC-000030 for this pattern is wrong — observed, DEC-000030 is the doc-only-cycle narrowing of 2026-08-06 and says nothing about branch protection; the pattern is #389's.
- named-queries.md parsed with bin/rulestore/named_queries.sequences: 10 topic positions, 8 process positions, 12 bundles — the re-derived test constants match. `spec` sits between `intake` and `change-flow`, mirroring `spec-template` before `change-flow` in the process band; spec before flow is the right reading order (the flow's step 1 presumes the spec). Every live topic but `lexicon` is named (lexicon is definitions, rendered last — pre-existing). Plan §2 said "adds none" of the queries — the bundle list is unchanged at 12; adding the new `spec` topic position is the sequence following the store, not a new query. Judged in-plan.
- Observed at the parse: the role line names `architect-agent` and `context-quality-reviewer` as topics; no row at 19f6760 or 7a24eeb carries either topic (O-2, pre-existing).
- spec-template.md frontmatter `session: [decision]` where both retired templates had `[decision, execution]` and R0863/R0862b (the Architect's rows that cite the design section) are `session: [execution]` — F-10.

## Skepticism

Verdict (skepticism): ready-with-findings

- Rendered chief-of-staff/decision: 139 rows, process band spec-template, change-flow, retro, project-setup, decision-log, named-queries (721 lines). Rendered coder-agent/execution: 95 rows, process band change-flow alone (299 lines). Rows render body-only, no ids, so every `[R####]` in a process document is opaque to the bundle reader (pre-existing, DEC-000930 notwithstanding; package 3a's emitter inherits it — O-3).
- Contradictions read beside rows in the chief-of-staff bundle: line 223 renders R0490 unconditioned — "a change is released only on her call at that gate" — eleven screens above change-flow step 6's "a routine change flows to release on its evidence under standing authorization". DEC-000920 ruled the routine case and assigned the row fix to #364, still open (checked via gh api). Not package 2's row, but the doc now cites R0570 for a sentence R0570 does not say, which is what makes the contradiction visible (F-2). R0570's body "the gate is the release decision" renders beside step 5 "Gate … merges" (F-1).
- What a coder subagent reading change-flow alone still has to guess: whether steps 1–2 are per unit or per spec ("Each meaningful change runs these in order" reads as all six per change); what a reviewer's `changes-required` verdict does to the pull request (F-4); whether the consequential go is given before the merge or before the release (F-1); what "plan mode" and "the gate skill" are — neither exists in the tree until package 4, which is acceptable for a document the plan sequences ahead of the skills, but worth one clause each ("the build skill", "the gate skill (package 4)") so the reader knows it is a forward reference, not a missing file.
- Skipped tests: honest. Both skipped tests open `REPO_ROOT / INVARIANTS_RELPATH` = process/directive-invariants.md, which no longer exists; the skip reason names DEC-001160 and package 6's removal. The other eight skips pre-date the package. Suite observed: 520 run, OK, skipped=10 (`bin/tests/run` in the worktree, 89 s). The named-queries constants were re-derived from the file, and the file parses to them.
- The coder's "15 retired citations replaced or dropped" was not recounted; the end state (zero retired citations) was verified instead.

## Findings

## F-1 — blocking
Claim: change-flow.md step 5 locates a gate at the merge; the rows it renders beside locate the human's go at the release.
Location: process/change-flow.md:34–35 ("5. **Gate.** A pull request merges as routine [R0570]; a consequential change [R0535, R0536] goes through the gate skill: its `human-gate` issue, its go.")
Evidence: observed. R0570 body: "No human gate fires at the merge; the gate is the release decision." R0534 Human note: "it is the release, not the merge, that the go covers." Rendered in the chief-of-staff/decision bundle, R0570 at the rows band and step 5 in the process band. Step 6 then says the consequential change "waits for the human's explicit go at the gate" — so the doc itself has the go both at step 5 and step 6.
Consequence: package 4 builds the gate skill from this document; built as written, a consequential change's PR waits on the human before merging, which is the merge-gate R0570 and DEC-000920 removed, and main stops being releasable-by-merge.
Fix: step 5 becomes "**Gate.** Every pull request merges [R0570]; for a consequential change [R0535, R0536] the gate skill opens its `human-gate` issue, and the go recorded there is the release go of step 6." Step 6 then drops "at the gate".

## F-2 — non-blocking
Claim: step 6 cites R0570 for a sentence R0570 does not contain.
Location: process/change-flow.md:36–37
Evidence: observed. R0570 is "open a pull request and merge it; no human gate fires at the merge". The standing-authorization ruling is DEC-000920; its row form is R0535's last sentence ("A change touching none of them is routine and flows to release on evidence, with no explicit human go/no-go"). R0490, rendered in the same bundle, says the opposite unconditionally; #364 (its reconciliation) is open.
Consequence: a reader following the cite finds nothing; a reader who also reads R0490 finds a contradiction the document does not acknowledge.
Fix: cite `[R0535]` (or `(DEC-000920)`) for the routine clause; report to the decision session that #364 is still open and R0490's body still contradicts R0535 — a row fix outside this package.

## F-3 — non-blocking
Claim: "every pull request gets a code review by an agent" is lost from change-flow.md and survives in no rendered text.
Location: process/change-flow.md:17 (the Code table row) and 29–33 (step 4)
Evidence: observed. 19f6760's table row and Quality paragraph said it; at 7a24eeb it is only in R0570's `## Human` note, which render.render never emits. R0067 (human code review is the exception path) is the nearest body text and says the inverse half.
Consequence: a coder-agent bundle reader has the six stages and no statement that the review in step 4 is a code review of the diff on every PR, trivial or not.
Fix: Code table row "Who reads" becomes "Reviewer and Skeptic/Risk on every pull request, then the human at the release" — or the clause moves from R0570's note into its body, which is a 1b-class row edit to report rather than do here.

## F-4 — non-blocking
Claim: step 4 drops R1614's "non-blocking" qualifier and nothing says what a reviewer's `changes-required` verdict does.
Location: process/change-flow.md:32–33
Evidence: observed. R1614: "A non-blocking finding's disposition at triage is file-and-land by default … Nothing else reopens a delta." The doc: "At triage a finding files-and-lands unless the human raises it to blocking." 19f6760 had "A blocking finding reopens the delta, which closes again on one more read over the diff since then"; that sentence is gone and no row carries it.
Consequence: read literally, a reviewer's blocking finding files-and-lands too; a subagent must guess whether `changes-required` blocks the merge.
Fix: "At triage a non-blocking finding files-and-lands unless the human raises it [R1614]; a `changes-required` verdict returns the delta to step 3, and one read over the diff since then closes it."

## F-5 — non-blocking
Claim: review-artifact.md names three pass sections; change-flow.md and R0492 name two.
Location: process/review-artifact.md:58–59; process/change-flow.md:29–30
Evidence: observed. "each pass section — quality, skepticism, continuity —" vs step 4 "Quality and skepticism, separate passes with separate verdicts [R0492]". Continuity has rows only for the spec reviewer (R1104, R1105, R1133).
Consequence: a reviewer subagent reading both does not know whether a code-delta artifact needs a continuity section (and R1617 then makes its absence a recorded gap).
Fix: review-artifact.md:58 says "each pass section the review planned — quality and skepticism [R0492], continuity where the delta is a spec's [R1104] —".

## F-6 — non-blocking
Claim: review-artifact.md still names a retired mechanism.
Location: process/review-artifact.md:64 ("a delta's whole diff, or a reconciliation")
Evidence: observed. The reconciliation pull request was R1491, retired under DEC-001200; the spec close is now R0481's one ruling.
Consequence: one retired word in the acceptance grep's blind spot (the plan's grep covers rows and history paths, not vocabulary).
Fix: delete ", or a reconciliation".

## F-7 — non-blocking
Claim: two process documents restate a cited row's sentence beside the cite.
Location: process/review-artifact.md:60 ("`ready` means ready for the human's approval, never approved" = R1414's last sentence); process/retro.md:17 ("Its inputs are the conversation it covers and the local tree [R1244]")
Evidence: observed; compared to the row bodies.
Consequence: two copies of one obligation (SPEC.md §4, maintainability goal).
Fix: review-artifact.md:60 drop the clause (R1414 is cited on line 59); retro.md:17 "Its inputs are R1244's; its outputs land by the last step below."

## F-8 — non-blocking
Claim: project-setup.md restates R0564's Human-note sentence and tells a bundle reader to consult a note bundles never render.
Location: process/project-setup.md:27–28
Evidence: observed. "The pattern is R0564's Human note: on a Free repo the forge layer is absent and the hook is the only layer." render.render emits row.body only. Also "hook": R0564 is `enforce: deny`; precondition 2 calls it a deny.
Consequence: a Chief of Staff reading its bundle is pointed at text it cannot see; the sentence lives in two places.
Fix: end item 1 at "…moves to one [R0564]." and delete the last sentence.

## F-9 — non-blocking
Claim: the unrun-pass form the document states will fail the R1414 hook as R1414 describes it.
Location: process/review-artifact.md:60–62 ("A pass that was planned and did not run has its section too, stating why in place of a verdict [R1617]")
Evidence: observed. R1414 body: "one `Verdict (<pass>):` line at the head of each pass section; every verdict is `ready`, `ready-with-findings`, or `changes-required`"; its Human note: the hook "fails a write under `reviews/` whose `Verdict:` lines are missing, outside the enum". A section with why in place of a verdict has a missing verdict line. R1617 says only "recorded with why".
Consequence: once package 3 writes `store-lint --check verdict-lines`, every artifact that honestly records an unrun pass is refused, or the hook is written loose enough to admit it and R1414 is wrong about itself.
Fix: inferred, the decision session's call: either the doc states the line form (`Verdict (<pass>): not run — <why>`) and R1414's enum gains `not run` by a 1b-class edit, or R1414's note says the hook checks only sections that carry a verdict line. Report to the decision session before package 3 writes the check.

## F-10 — non-blocking
Claim: spec-template.md renders to no execution-session bundle, though the Architect's design-section rows are execution-session rows.
Location: process/spec-template.md:5 (`session: [decision]`)
Evidence: observed. docs/history/prd-template.md and trd-template.md both carried `session: [decision, execution]`. R0863 and R0862b are `session: [execution]`; 8 architect-agent rows are execution-only.
Consequence: an architect-agent/execution bundle carries R0863 ("when drafting or updating the spec's design section …") and not the document that says what that section is.
Fix: `session: [decision, execution]`.

## Observations

O-1: spec-template.md §7 cites R0497 for deploy-vs-release but not R0499/R0500 (flags, canaries, flag ownership), both live in the `spec` topic; the TRD cited all three. One cite would do.
O-2 (pre-existing): named-queries.md's role line names `architect-agent` and `context-quality-reviewer` as topics; no row carries either topic at 19f6760 or 7a24eeb. Harmless (an unmatched name is an unused position) and not this package's.
O-3 (pre-existing): bundles render row bodies without ids, so every `[R####]` cite in the process band is opaque to the reader; package 3a's emitter should decide whether cites label.

## Decision-log.md, one more

Not a finding against the package's diff, but read for continuity: process/decision-log.md:36–39 still says the same-number renumbering "is the one edit the append-only rule admits". R0583 now carries `enforce: hook` (DEC-001230) with a hook that "refuses an edit to `decisions/log.md` whose diff is not append-only". With ids allocated at merge by the decision session (the new paragraph at 27–29), the collision case this paragraph serves no longer arises. Non-blocking, inferred: delete the paragraph or say the hook refuses it and the human does it by hand.

## Verdicts

Verdict (continuity): ready-with-findings
Verdict (quality): changes-required
Verdict (skepticism): ready-with-findings
Verdict: changes-required

Path: /home/claude/sort/review-2.md

## Re-read over 7a24eeb..22ec05b

Verdict (re-read): ready-with-findings

Scope: `git diff 7a24eeb..22ec05b` — process/change-flow.md, project-setup.md, retro.md, review-artifact.md, spec-template.md, rules/R1414.md; nothing else (observed, `--stat`). Worktree recreated at 22ec05b and removed; clone untouched.
1. Steps 5–6: the gate is now the release. Step 5 cites R0570 and says no human gate fires at the merge; step 6 cites R0535 for the routine clause and R0534/R0562/R0490 for the consequential go before release. Read beside the rendered R0570 (bundle line 249) and R0534, consistent. F-1 closed.
2. F-2 (R0535 cited), F-4 (non-blocking qualifier restored; `changes-required` stated), F-6 ("or a reconciliation" gone), F-7 (both restatements gone), F-8 (note pointer gone, `[R0564]` stands), F-10 (`session: [decision, execution]`): each closed as asked. F-5 closed by the other route — change-flow now names three passes, matching review-artifact.md; the two documents agree, though R0492 still names two (continuity has rows only for spec deltas). Acceptable; noted.
3. R1414: body enum `ready`, `ready-with-findings`, `not-run`, `changes-required` in that severity order, one added clause defining `not-run`; block comment states the same four; frontmatter, hook block, Human note unchanged (observed, the diff is three lines). review-artifact.md: `Verdict (<pass>): not-run` then one line why, header enum matches. All 39+ cites live; no retired vocabulary.
4. Radius: process/ and rules/R1414.md only.
5. `bin/tests/run`: 520 OK, 10 skipped. `reconcile_sort.py --bodies`: hits 2, both allowed (R0963, R1173 — DEC-001110 writing rows), 34 enforce blocks checked, problems 0.
6. Re-rendered chief-of-staff/decision: steps 4–6 read consistently beside R0570 (249), R1414 (349), R1614 (371), R1617 (373). R0490 (223) remains unconditioned beside step 6 — the #364 row fix, outside this package.

## F-11 — non-blocking
Claim: step 5's second sentence restates R0570's body beside its cite ("No human gate fires here; the gate is the release"), the F-7 class.
Location: process/change-flow.md:32
Evidence: observed; R0570 body "No human gate fires at the merge; the gate is the release decision."
Consequence: one obligation in two places; small.
Fix: drop the sentence, or keep it as the document's own structural statement — the human's call; not blocking.

## F-12 — non-blocking
Claim: "`changes-required` reopens it for one more read" clashes literally with R1614's "Nothing else reopens a delta", rendered 116 lines above it.
Location: process/change-flow.md:30
Evidence: observed; inferred that the intent is "the delta has not closed", not a reopen.
Consequence: a reader holding both sentences sees the document claim a reopen path the row denies.
Fix: "`changes-required` means the delta has not closed; one more read over the diff since then closes it."

Verdict (re-read): ready-with-findings
