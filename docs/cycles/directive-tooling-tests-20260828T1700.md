You are the Test Designer, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Author the test suite for bin/directive and bin/check-directive against specs/directive-tooling-trd.md @ 88f1b9d8d781f21ca6dd679b4f6a80767cc1a205 on branch directive-tooling-trd, and confirm it red. Neither tool exists yet; you are writing the tests they must turn green, and you will not implement either tool.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-tests-20260828T1700.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-tooling test authorship", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-tests", created by: git worktree add "$TMPDIR/fiducial-dt-tests" directive-tooling-trd
Before creating it, run git worktree list; if any existing worktree holds branch directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). Both origin/directive-tooling-trd and local directive-tooling-trd must be at 88f1b9d8d781f21ca6dd679b4f6a80767cc1a205. If either has moved, stop and report.

READ before writing, whole, from the worktree: specs/directive-tooling-trd.md; specs/directive-tooling.md (the agreed PRD — §6's AC-DT-01..19 are what the tests assert); reviews/directive-tooling-trd-cycle-1.md (its five non-blocking observations are deferred, not fixed); bin/tests/test_cycle_open.py and bin/tests/helpers.py (the house test conventions and the fixture-home builder the TRD's §4.1 extends).

PROCESS CONTEXT, ruled by Dave 2026-08-28 and binding: the TRD is deliberately open (status: draft) and stays open. You write tests against it as it stands; where the TRD is wrong, you file a finding — you never edit the TRD. Findings flow to the decision session, which mediates TRD amendments; tests and TRD flip agreed together when they cohere. Producer/approver separation holds: the TRD's author was another session, and the implementer will be a third.

KNOWN DEFECTS, recorded going in — write the tests to the AGREED PRD criterion, not to the TRD's current text, for exactly these two:
1. Cycle mode's region table omits a route-and-model region; AC-DT-14 (agreed) requires the cycle skeleton to carry Route and Model. Write AC-DT-14's test to the criterion; it is expected red against the design until the TRD's first convergence amendment adds the region.
2. The lint's read of the invariants document is not scoped to committed content in the TRD's current text (§3.6 step 4) while the generator's is (§3.2). Test to the TRD as written, and file the asymmetry as a finding with the test that would change if it resolves.

SCOPE:
1. Build the fixture substrate the TRD §4.1 specifies: the fixture repository (a real git repository — F-2's resolution requires committed content), the invariants-document fixture, and the fixture directives §6 of the PRD names — including AC-DT-06's per-element missing-one fixtures, the M3 shape set (i)–(vii) plus the two-statement and neither/both cases, the M8 nine (five passing, four failing), and AC-DT-09's four citation fixtures built on real objects in the fixture repository (blob, tag, non-touching commit, touching commit — the touching/non-touching pair must exercise F-1's diff-tree --root semantics, including a root-commit citation).
2. One test per acceptance criterion AC-DT-01 through AC-DT-19, plus the TRD's own testable decisions (Q1/Q9/Q10 mechanisms, M1/M4–M7 match rules, M3 markdown sensitivity, marker/manifest partition, exit-status contract). House conventions per bin/tests/.
3. TRUE RED-GATE: a missing-module red proves nothing. Provide a minimal stub for each binary with deliberately wrong behavior (e.g. a lint that always exits 0 silently; a generator that emits a skeleton with no manifest and two unfenced labelled statements), run the suite against the stubs, and record per-test that it FAILS on wrong behavior — not on absent imports. Then record the suite's state with stubs removed. Both runs' output to committed log files under bin/tests/, paths stated in the report. The stubs are test fixtures, clearly named as stubs, never a head start on implementation.
4. Tests blocked on the open questions Q2/Q4/Q5/Q6: write them to the TRD's recommendation, marked skip-with-reason naming the question, so the suite is honest about what a ruling would change. AC-DT-16 binds the decision session, not code — represent it as the TRD directs, not as a red test.
5. FINDINGS against the TRD: anything the test-writing surfaces — an untestable claim, a contradiction, a mechanism that cannot satisfy its criterion, a fixture the TRD's text cannot specify — is filed in the report as a numbered finding with the same fields a review artifact entry carries (claim, location, evidence, consequence, what would resolve it). File; do not fix.

Frontmatter on any new governed file: none of your files are governed documents; tests and fixtures carry no frontmatter. Do not touch specs/, docs/global-context/, skills/, policies/, roles/.

AFTER WRITING: run bin/tests/run (the whole suite — the existing 424 must stay green; state the count) and bin/check-frontmatter --all (must exit 0) from the worktree. Commit the test suite and fixtures with message "directive-tooling: test suite, confirmed red per red-run logs". Push.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-tests" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 88f1b9d8d781f21ca6dd679b4f6a80767cc1a205: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; test-suite commit SHA; red-run log paths; per-criterion table (AC-DT-01..19: test name, red-on-stub result, skip-with-reason where applicable); the AC-DT-14 red confirmed; numbered findings against the TRD; existing-suite count still green; check-frontmatter exit code; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
