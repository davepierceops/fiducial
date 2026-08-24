# Review: specs/directive-tooling.md — cycle 3

Verdict: changes-required
Reviewed: specs/directive-tooling.md @ 92ac59d
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-23
Scope: Re-gate of a revised PRD, before Dave agrees it — confirmation that each cycle-3 disposition landed as directed, plus a full gate pass over all eight sections: internal consistency, traceability to parent artifacts, NFR dimension coverage, AC testability, risk tolerance, open questions naming what resolves them. Plus the Depth 1 continuity scan that fires automatically on every spec revision.
Cross-checked: docs/cycles/directive-tooling-spec-3-20260823T203821Z.md @ d258434e, reviews/directive-tooling-cycle-2.md @ e1910019, docs/cycles/directive-tooling-spec-2-20260823T195803Z.md @ d5a82172, skills/directive-authoring.md @ 48ad7fd1 and @ 511b4dca (origin/main), reviews/expedited-log.md at origin/main, docs/packages/package-a-spec.md §3.6 (AC-CO-1…AC-CO-12), bin/tests/test_cycle_open.py, bin/cycle-open, docs/global-context/core.md @ 17f75612 (rules 6, 11, 13, 14, 15, Vocabulary), docs/global-context/decision-layer.md rule 14, policies/decision-log-policy.md, policies/document-metadata-policy.md @ a06460a9, decisions/log.md (DEC-000110, DEC-000150, DEC-000160, DEC-000180), OPEN-ITEMS.md, roles/spec-reviewer-agent.md @ ed88dcde, skills/review-artifact.md, specs/prd-template.md, and the 95 files in docs/cycles/.
Not inspected: No TRD and no derived acceptance-criteria artifact exists for this spec, so the Depth 1 spine scan again ran against the PRD alone and could not check PRD→TRD or AC→journey traceability downward. Neither `bin/directive` nor `bin/check-directive` exists — no behaviour the spec claims was executed. `bin/cycle-open`'s runtime behaviour was exercised only through the pre-existing suite, not directly; `bin/tests/test_cycle_open.py` was read for its AC-CO coverage and run as part of `bin/tests/run`, not audited test-by-test against §3.6. `docs/packages/package-a-spec.md` was read at §3.6 and at the AC-CO-12 entry in its later corrections section, not end to end. `decisions/log.md` was read for the DEC-000110→000150→000180 chain and for DEC-000160; it was not read end to end, so a further governing entry may exist. `OPEN-ITEMS.md` was grepped for `cycle-open` and for the directive-execution entry, not read whole. The friction figures carried in §1 and §5 are from the research findings and were not independently recounted; the `docs/cycles/` filename counts in §4 **were** recounted this cycle (see O1). **Reviewer independence:** this artifact was written in the same session that authored the reviewed revision, and by the same author, for the third consecutive cycle. No governed rule requires author/reviewer separation for a spec — `operating-model.md` step 5, mirrored in `CLAUDE.md`, scopes that separation to test authorship versus implementation — but the limitation is structural and is not removed by the reviewer stating it. Both blocking findings below are in text this session wrote or sharpened hours earlier, and the reader has no independent check that a third of the same kind was not missed.
Findings: 2 blocking, 3 non-blocking, 4 observations
Prior cycle: reviews/directive-tooling-cycle-2.md
Dave should inspect: (1) B1 — the migration's preserved contract requires the generator to refuse four ways, and G4 plus AC-DT-04 say it has no refusal path; only you can decide whether G4 yields or the cycle mode drops its refusals; (2) B2 — AC-DT-12 forbids working-tree mutation and AC-DT-15 requires the cycle mode to write a directive file into `docs/cycles/`, so the two criteria cannot both hold; (3) N2 — the two-form M8 rests on Core rule 14 and AC-CO-1, and `skills/directive-authoring.md`'s Naming sentence still admits only one form, so the tool will produce files an agreed skill calls misnamed and nothing schedules the amendment; (4) N3 — `OPEN-ITEMS.md`'s Track guard still anchors on `bin/cycle-open` and AC-DT-16 reaches only `decisions/log.md`; (5) O1 — the dictated figure of 37 non-conforming historical directives is 29 against the two-pattern M8 this cycle adopts.

## Disposition confirmation

Each cycle-3 disposition, and what landed. Verified by reading the revised document against the directive.

| Disposition | Landed | Where |
| --- | --- | --- |
| B1 — two forms, mode-determined; M8 a two-pattern check; neither governed source amended; no retrofit | yes | §4 M8 row; §4 paragraph following the M-table; §6 AC-DT-06 M8 clause; §8 Q8 |
| B2 — name §3.6 and AC-CO-1…AC-CO-12 as the governing contract; state that the generalize disposition preserves it intact under the cycle mode; name `bin/tests/test_cycle_open.py` as the test surface | yes | §4 "The governing contract for what moves" and "The disposition of that contract"; §6 AC-DT-15. See B1 and B2 below — naming the contract is what exposed the two blocking conflicts |
| N1 — prerequisite discharged; remove the framing from §1, §4 G6, M3 row, §7, AC-DT-13; cite the amended skill by path and content-commit SHA; write the AC-DT-06 test; close the Q4 sequencing item | yes | §1 (qualification paragraph removed, "That disposition is governed text" added); §4 G6; §4 M3 row (qualification now `none`); §7 "Not accepted"; §6 AC-DT-06 and AC-DT-13; §8 Q4 and Q7 |
| N2 — G11's manifest locates each sourced section's extent, not only its source; state the mechanism | yes, and the first attempt at it was wrong | §4 G11; §5 first bullet; §6 AC-DT-05. The mechanism as first written measured marker-to-next-marker over invariant sections only, which counts the author's middle inside the preceding section's extent; it was corrected before the gate to mark and enumerate **every** region including the author slot |
| N3 — supersession by new entry; no log edit this cycle | yes, for the decision log; not for `OPEN-ITEMS.md` | §4 "One landing requirement follows from G0"; §6 AC-DT-16. See N3 below |
| O1 — record the cycle-1 O1 disposition where the spec carries the question | yes | §8 Q4, "The governed home is settled with it" |
| O2, O3, O4 — no action | n/a | `specs/bin-land.md` unmodified; the AC-CO-3 pointer untouched. See O2 below |

## B1 — blocking
Claim: The contract this cycle names as preserved requires the generator to refuse in at least four cases, and G4 and AC-DT-04 state that the generator has no refusal path.
Location: specs/directive-tooling.md §4 "Relationship to `bin/cycle-open`", "The disposition of that contract"; §4 Functional goals, G4; §6 AC-DT-04, AC-DT-15.
Evidence: Verified by reading. `docs/packages/package-a-spec.md` §3.6 gives `bin/cycle-open` four refusal paths: AC-CO-1 exits 2 when neither `--cycle` nor `--name` is given, AC-CO-2 "Refuses to overwrite an existing directive (exit 3)", AC-CO-5 refuses a dirty in-scope document with exit 3, AC-CO-6 refuses an untracked or non-existent path with exit 1, and AC-CO-12 refuses an absolute `--out` with exit 2. `bin/tests/test_cycle_open.py` encodes them. The revised §4 states those criteria are "neither superseded nor split" and that the cycle mode "satisfies it unchanged ... the same refusals", and AC-DT-15 requires the suite to pass with none of the twelve retired. Against that, G4 reads "It refuses no directive and blocks no author ... `bin/check-directive` is where refusal lives," and AC-DT-04 reads "The generator exits 0 for every invocation that produces a skeleton, and rejects no content. **It has no refusal path.**" AC-DT-04's first clause survives the conflict — an invocation that refuses produces no skeleton — and "rejects no content" survives, because the AC-CO refusals are about preconditions rather than content. The final sentence does not survive, and neither does G4's "refuses no directive," which AC-CO-2 contradicts in the same words.
Consequence: An implementer cannot satisfy both AC-DT-04 and AC-DT-15. Dropping the refusals reds `bin/tests/test_cycle_open.py`, which AC-DT-15 defines as a failed migration; keeping them makes AC-DT-04 false and makes G4 false of the tool the spec licenses. A Test Designer working from §6 writes an AC-DT-04 case asserting no non-zero exit path exists and an AC-DT-15 case asserting four of them do. This is cycle-2 B1 one layer over: naming the absorbed governance surfaced a second place where the absorbed tool and the specified tool disagree, and this one is in the goals rather than in a table row.
Fix: G4 and AC-DT-04 are scoped to what they were actually protecting — the generator refuses no *directive content* and gates no author's judgment — with the precondition refusals the cycle mode inherits named as permitted and traced to AC-CO-1, -2, -5, -6, and -12. Alternatively Dave rules that the cycle mode drops them, in which case B2's "preserved intact" is not the disposition and AC-DT-15 must name which criteria are retired. §7's "Not accepted" list, which does not currently mention refusal, gains whichever line results.
Related: B2.

## B2 — blocking
Claim: AC-DT-12 forbids either tool from mutating the working tree, and AC-DT-15 requires the cycle mode to write a directive file and a bundle directory into it.
Location: specs/directive-tooling.md §6 AC-DT-12 and AC-DT-15; §4 Non-functional goals, Security.
Evidence: Verified by reading. AC-DT-12: "No code path in either tool invokes `gh`, writes to a remote, **mutates the working tree or the index**, or reads a credential. Verifiable statically over the source." AC-CO-1 requires the tool to write `docs/cycles/cycle-<N>-directive.md`; AC-CO-7 requires it to write the reviewed-revision bundle and `BUNDLE.txt` under `--out`; AC-CO-11 states the boundary the absorbed tool actually keeps — "The tool writes only the directive and the bundle directory. It does not stage, commit, or modify any document." The Security NFR in the same document already states the reconcilable version — the generator "writes its skeleton and its source manifest to stdout or to a named output path and touches nothing else" — so §4 and §6 disagree with each other independently of the migration, and AC-DT-15 is what makes the disagreement unavoidable. G11 compounds it by requiring the manifest to be "part of the skeleton written to the directive file," which presumes a file write.
Consequence: The static check AC-DT-12 licenses fails on any conforming implementation, because a conforming implementation writes files. Read strictly, AC-DT-12 forbids the generator from doing the one thing §2's J1 has it do. An implementer must silently pick the NFR's reading over the AC's, which is the class of undeclared choice cycle-2 B2 was raised about.
Fix: AC-DT-12 states the boundary the Security NFR states — no remote write, no credential read, no `gh`, no staging, no commit, and no modification of any file other than the skeleton it was invoked to write and, where the TRD lands them, the bundle outputs — with AC-CO-11 cited as the inherited statement of the same rule. The lint's half of AC-DT-12 is unaffected and should be stated separately, since the lint genuinely writes nothing.
Related: B1.

## N1 — non-blocking
Claim: The M2 row's Derived-from column cites two rules stricter than M2's own check, and this document's own citations exercise both gaps.
Location: specs/directive-tooling.md §4, M-table row M2; §4 "Relationship to `bin/cycle-open`", final paragraph; §1, "Two citation notes".
Evidence: Verified by reading and by running. M2 requires a citation to name "a path present at the reviewed ref, and a SHA that resolves to a **commit touching that path**." Its Derived-from column cites `policies/document-metadata-policy.md`, "The version of a document at reference time is the SHA of the last commit touching the file" — which is strictly narrower than "a commit touching that path." §4's closing paragraph separately asserts that `cycle-open`'s docstring principle, "the full id of the last commit touching the path ... never invented, never abbreviated," is "the same principle ... M2 states for citations"; M2 states neither fullness nor lastness. Both gaps are live in this document: §1 cites `skills/directive-authoring.md` @ `48ad7fd1`, which is a commit touching the path but is not the last one (`511b4dca` is, a frontmatter-only status transition — verified by `git log -1 -- skills/directive-authoring.md` at origin/main), and every SHA the document cites a companion by is abbreviated to eight characters — the single full-length SHA in the file is the blob hash AC-DT-09 quotes as a fixture case.
Consequence: A lint built from the M-table as written passes a directive citing a companion by an abbreviated SHA of an arbitrary touching commit, while AC-DT-15 requires the same binary's cycle mode to emit full last-commit SHAs under AC-CO-4. The tool would then hold two different standards for the same kind of citation, and §4's paragraph asserts they are one standard. Non-blocking because M2 is decidable and useful as written and no criterion depends on the stronger reading; the defect is that the document claims a strictness it does not specify.
Fix: Either M2's element text states the strictness its sources state — full SHA, last commit touching the path — and AC-DT-09 gains the corresponding fixtures, or §4's closing paragraph and M2's Derived-from column are narrowed to the principle M2 actually inherits, which is "never invented." §1's own citation note already records the deliberate exception and should be reconciled with whichever way this goes.

## N2 — non-blocking
Claim: M8's second admitted form is licensed by Core rule 14 and AC-CO-1 and not by `skills/directive-authoring.md`'s Naming sentence, so the generator will produce filenames an agreed governed document calls wrong, and nothing schedules the fix.
Location: specs/directive-tooling.md §4, M8 row and the two paragraphs following the M-table; §8 Q8.
Evidence: Verified by reading. `skills/directive-authoring.md` at origin/main, "Naming": "A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format." It states no exception. Core rule 14 states the same form "when no stated convention names the file" and adds "Where a convention names it, follow the convention," so the yield clause exists in Core and was dropped when the skill specialised the rule. The revised §4 records this accurately and says closing it "is Dave's call in that file and not this document's to make," and §8 Q8 declines to reopen it.
Consequence: Every directive `bin/directive --cycle N` produces is, on the face of an agreed skill an author is instructed to follow, misnamed — and the lint the same spec specifies will pass it. The spec's own record of the conflict is what keeps this non-blocking rather than blocking; what makes it a finding at all is that no item anywhere now carries the amendment. `OPEN-ITEMS.md` does not name it, §8 does not open a question for it, and Q8 marks the matter closed, so the residual has no owner in any committed artifact except this review entry.
Fix: `skills/directive-authoring.md`'s Naming section gains Core rule 14's yield clause, by expedited amendment as the working-tree rule was. If Dave prefers to leave the skill alone, §8 carries the residual as an open question with a named resolver so it is tracked rather than merely recorded.

## N3 — non-blocking
Claim: AC-DT-16 re-anchors the migrated obligation in `decisions/log.md` and leaves the third record — `OPEN-ITEMS.md`'s Track guard — pointing at `bin/cycle-open`.
Location: specs/directive-tooling.md §4, "One landing requirement follows from G0"; §6 AC-DT-16.
Evidence: Verified by reading. The paragraph names three committed records that bind the obligation to `bin/cycle-open`: DEC-000150, DEC-000180, and `OPEN-ITEMS.md`'s section headed "`bin/cycle-open` and the retirement of Track" (present at `OPEN-ITEMS.md:1085`, with the DEC-000150 reference at `:1099`). AC-DT-16 requires a new decision-log entry superseding DEC-000180 and requires nothing of `OPEN-ITEMS.md`. The cycle-3 directive's N3 disposition named the log entry only, so this is faithful execution of what was dictated and not a defect in execution; the cycle-2 finding it answers named both records.
Consequence: After the migration lands and AC-DT-16 is satisfied, a reader tracing the Track guard from `OPEN-ITEMS.md` still arrives at a binary that no longer emits a directive skeleton. That is the slow failure cycle-2 N3 described, reduced from three records to one rather than to none. `OPEN-ITEMS.md` is not append-only, so unlike the log it can simply be edited, which makes the omission cheap to close and easy to forget.
Fix: AC-DT-16 gains a second clause, or a sibling criterion states it: the migration does not land until `OPEN-ITEMS.md`'s Track-guard section names `bin/directive`'s cycle mode. Neither is in this cycle's change scope.

## O1 — observation
Claim: The dictated count of non-conforming historical directive files is 37; the count against the two-pattern M8 this cycle adopts is 29.
Location: specs/directive-tooling.md §4, third paragraph following the M-table; docs/cycles/directive-tooling-spec-3-20260823T203821Z.md @ d258434e, B1.
Evidence: Verified by running, at the revision under review. `docs/cycles/` holds 95 markdown files: 59 match `<descriptor>-<timestamp>.md` with an ISO 8601 basic timestamp, 7 match `cycle-<N>-directive.md`, and 29 match neither — mostly `<slug>-directive.md` and `<slug>-<YYYY-MM-DD>-directive.md`. The dictated 37 is the cycle-2 count against the single-pattern M8, computed before the second form was admitted and before this cycle's directive file was added.
Consequence: None to the disposition, which is that the corpus is not retrofitted either way. Recorded because Core rule 13 requires a changed number to change where it appears, and because the revision states both figures with their provenance rather than silently substituting one — a reader comparing the spec to the directive that dictated it will see the discrepancy and should find it explained.
Fix: None to this document.

## O2 — observation
Claim: The format contract this cycle elevates to "preserved intact" points, in its own text, at a section that no longer exists.
Location: docs/packages/package-a-spec.md §3.6 AC-CO-3; skills/spec-review-cycle.md; specs/directive-tooling.md §4, "The disposition of that contract".
Evidence: Verified by reading. AC-CO-3 requires "The skeleton matches the format in `skills/spec-review-cycle.md`," and that document states no directive format. Carried unchanged from cycle-2 O3, which the cycle-3 directive dispositions as "no action in this cycle; the stale AC-CO-3 pointer is outside this blast radius and is tracked by the decision session."
Consequence: Pre-existing and correctly held out of scope, but it now bears more weight than it did: the revision names AC-CO-3 as one of the criteria the cycle mode satisfies unchanged, so an implementer told to preserve the format follows the reference into an empty target and falls back to `bin/cycle-open`'s code as the authoritative statement of what they are replacing. Recorded so the decision session's tracking of it is not lost between cycles.
Fix: None to this document.

## O3 — observation
Claim: AC-DT-16 is a precondition on a decision-session act, not a property of either tool, and cannot be satisfied by the party the other criteria address.
Location: specs/directive-tooling.md §6 AC-DT-16.
Evidence: Inferred by reading. Every other criterion in §6 is a property of `bin/directive` or `bin/check-directive` verifiable by running or by static inspection. AC-DT-16 requires an entry in `decisions/log.md`, which `policies/decision-log-policy.md` scopes to decision sessions — "appending to the log is decision-session work." The criterion states its own oddity in its final sentence.
Consequence: None adverse; the requirement is dictated and the alternative — leaving the transfer unrecorded — is what N3 exists to prevent. Recorded because an implementation session working the AC list will find one entry it cannot discharge, and because a release gate reading §6 as a checklist will read a red where the correct state is "waiting on a decision session."
Fix: None required. If §6 gains a convention for criteria that bind someone other than the implementer, AC-DT-16 is its first member.

## O4 — observation
Claim: The carried-forward constraints from cycles 1 and 2 remain true, and the pre-existing test failures are unchanged.
Location: specs/directive-tooling.md frontmatter; bin/tests/test_bundle.py.
Evidence: Verified by running, at the revision under review. The spec is still `status: draft` in `specs/`, so `policies/document-metadata-policy.md`'s build-gating rule still requires Dave's explicit per-task confirmation before either tool is implemented. `bin/check-frontmatter --all` exits 0. `bin/tests/run` exits 1 with exactly the two AC-BN-10 failures in `bin/tests/test_bundle.py` — the same pair `docs/cycles/pass2-held-fix-20260823T180753Z.md` @ `b9444973` records as accepted and the cycle-3 directive restates as pre-existing (*told*) — out of 399 tests; `bin/tests/test_cycle_open.py` is green, which matters this cycle because AC-DT-15 now names it. This cycle changed one markdown file and added two, and no code.
Consequence: None. Recorded so the non-zero suite exit in this cycle's report is not read as a regression, and so the build-gating constraint is not discovered at implementation time.
Fix: None to this document.

## On what the revision got right, and why it still fails the gate

The three findings this cycle was directed to answer are answered, and two of
them are answered better than the directive required. B2 asked the document to
name `docs/packages/package-a-spec.md` §3.6 and its twelve criteria; the revision
names them, states which of the absorbed behaviours each one fixes, and makes the
pre-existing test suite an acceptance criterion rather than a promise. N2's
mechanism was written wrong the first time — marker-to-next-marker over invariant
sections alone, which sweeps the author's middle into the preceding section's
extent and computes the generator's share as everything — and the error was caught
and corrected before this gate rather than shipped and flagged. N1's dispositions
landed in all five places named, and §1 records, unprompted, that the SHA it was
told to cite is the content commit and not the file's last-touching commit, which
is the distinction M2 is about.

What sends this to `changes-required` is the same mechanism that sent cycle 2
there, one level in. Naming the absorbed governance is what makes the absorbed
tool's actual behaviour visible, and the actual behaviour contradicts two things
this document says about the tool it specifies: that the generator has no refusal
path, and that neither tool mutates the working tree. `bin/cycle-open` refuses
four ways and writes two kinds of file, by committed criteria this cycle promoted
to "preserved intact." Neither conflict is a paperwork gap. G4 is load-bearing —
§7 accepts adopting the generator ahead of the lint precisely because generation
is ungated — and AC-DT-12 is the criterion that keeps either tool from becoming a
write path. Both need Dave to say where the line falls now that a writing,
refusing generator is inside the boundary they draw.
