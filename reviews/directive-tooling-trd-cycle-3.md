# Review: specs/directive-tooling-trd.md — cycle 3

Verdict: ready
Reviewed: specs/directive-tooling-trd.md @ 3a945c9
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-28
Scope: confirmation of the cycle-2 fixes, and nothing else — each of F-1, F-2
and F-3 checked against the disposition it was given in
`docs/cycles/directive-tooling-trd-conv2-20260828T1830.md`, over the round-2
diff (`git show 3a945c9`) and the amended text and tests at that ref.
**F-1 confirmed by running**: the two Q5 tests are no longer skipped, are
renamed to state what they assert, and cite Dave's Q5 ruling (c) of 2026-08-28
by the decision record's path; run against the stubs with
`DIRECTIVE_TOOLING_BIN` as an absolute path and `bin` on `PYTHONPATH`, each
fails on behavior rather than on import —
`test_route_and_model_are_committed_in_both_modes_and_the_author_count_stays_two`
at `assertIn("Route: fresh", out)` against the stub's `Route: stub`, and
`test_the_lint_checks_exactly_m1_through_m8_with_route_and_model_absent` at
`assert_lint_passes` on `'M1' not found in ''`, its fixture having first been
confirmed to carry no `ROUTE AND MODEL` region (`replace={"route": None}`
drops the `route` block, `helpers.py:839`). The two assert the ruling's two
consequences: committed classification in *both* modes' manifests with the
author count pinned at two per mode, and an element set of exactly M1–M8 with
no M9. `SKIP_Q5` is deleted; no `OQ-Q5` or `SKIP_Q5` reference survives in the
suite or the TRD. **F-2 confirmed by running**, parsing the cycle table out of
the document: the sentence now reads "**Cycle mode's region 6 is a committed
region an author writes into.**" (`:420`), and row 6 is `` `Decisions`
(heading) `` | `§Decisions` while row 5 is `` `WORKING-TREE DISPOSITION` `` |
**author region**, so the sentence agrees with the table, with §3.3's
"Sixteen regions: two author, fourteen committed", and with the F-A3
subsection's "rows 6, 7 and 8 of the cycle table". It is the only TRD edit in
the round. **F-3 confirmed by reading**, each of the five docstrings against
the amended text: (a) `test_directive.py:756-759` now states that the
cycle-mode table carries row 2 from the section general mode's region 2 reads
and that AC-DT-14's clause is discharged by the emission — matching `:373` and
"AC-DT-14's route-and-model clause is satisfied by row 2"; (b)
`test_check_directive.py:373-377` now states that the test and §3.6's
mechanism agree via the unpeeled `cat-file -t` step — matching §3.6 M2's
object-type subsection at `:715-726`; (c) `test_check_directive.py:455-458`
now names the class §3.6 step 5 fixes and its two further members — matching
`:670-673` and FM-L5 at `:1269` verbatim; (d) `test_directive.py:387-389` now
quotes §3.6's bold "AC-DT-02's scan walks the generator's source and nothing
else" — present at `:840`; (e) `test_check_directive.py:539` drops the
`OQ-Q5` citation. No assertion was changed by any of the five, as the round-2
disposition required. **The round-2 executor's three disclosed extras
confirmed accurate against the TRD and accepted**: the two "four → three"
corrections in `test_directive_trd.py`'s module docstring (`:1`, `:7`) and its
`§9 (OQ-Q2, OQ-Q4, OQ-Q6)` contract line are right — §9 carries exactly those
three `OQ-Q` entries (`:1436`, `:1456`, `:1479`), and the "three questions the
PRD routes to Dave" phrasing counts the questions this module carries skips
for, which is the count that sentence always carried (PRD §8 itself lists
seven); the `TestOpenQuestions` class docstring's "Q2, Q4 … skipped with the
reason", with Q5 now asserted directly, matches the class's contents exactly —
its only remaining skips are `SKIP_Q2` and `SKIP_Q4`, the three `SKIP_Q6`
skips living in `TestExitStatusContract`. **Verification runs.**
`bin/tests/run` — **573 tests, 8 failures, 140 errors, 7 skipped**, exit 1.
573 = the 424 pre-existing tests plus the three new modules' 149; every one of
the 148 reported failure and error entries is inside those three modules
(`test_check_directive` 89, `test_directive` 41, `test_directive_trd` 18), no
pre-existing module reports a failure, an error or a collection problem, so
the 424 are green. The skip count is 7, as dispositioned: 6 in
`test_directive_trd` (Q2, Q4, three Q6, AC-DT-16) plus one pre-existing
conditional skip, `test_check_frontmatter.py:1440`'s case-sensitivity guard.
`test_directive_trd`'s entries move 16 → 18 and its skips 8 → 6, which is the
two rewritten tests joining the expected red. Under the full run those two
report as errors rather than failures because no binary exists at
`bin/directive` yet; against the stubs, where a binary answers, both are
behavioral failures as shown above. `bin/check-frontmatter --all` — **exit
0**, `NOTE in-scope: [scope-summary] 55 file(s) matched, from 12 configured
glob(s)`.
Cross-checked: reviews/directive-tooling-trd-cycle-2.md;
docs/cycles/directive-tooling-trd-conv2-20260828T1830.md; bin/tests/helpers.py
(`_dt_blocks`, `directive_body`, `directive_fixture`); bin/tests/test_directive.py
(`parse_manifest`, `cycle_directive`'s `docs/cycles/cycle-7-directive.md`
convention, which the rewritten test follows); bin/tests/stubs/;
specs/directive-tooling.md §8 for the open-question count only.
Not inspected: the TRD's design, reopened by no part of this cycle; cycle-1
observations O-1 through O-4, which survive to implementation by prior
disposition and were not re-examined; the pre-existing suite's own correctness
beyond its exit state; `bin/tests/red-run-*.log`, still the superseded
`fb8e536` evidence noted as deferred in cycle 2; prose quality and template
conformance, this cycle being confirmation-scoped.
Findings: none.
Prior cycle: reviews/directive-tooling-trd-cycle-2.md
