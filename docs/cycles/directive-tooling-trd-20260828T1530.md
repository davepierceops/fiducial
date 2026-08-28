You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Author the draft TRD for bin/directive and bin/check-directive, the two tools the agreed PRD specs/directive-tooling.md specifies.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-tooling-trd-20260828T1530.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: author directive-tooling TRD", push, and report the SHA.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-dt-trd", created by: git worktree add --no-track "$TMPDIR/fiducial-dt-trd" -b directive-tooling-trd origin/main
Before creating it, run git worktree list; if any existing worktree holds a branch named directive-tooling-trd, stop and report. Do not touch the main tree.

BASE VERIFICATION before anything else: git fetch origin (an osxkeychain "failed to store" message is noise; judge the fetch by the refs). origin/main must be at 79228c0dc7e1e25586701a054cda99eb9bb68059. If it has moved, stop and report.

READ before writing, whole, from the worktree: specs/directive-tooling.md (the agreed PRD; note its §4 "The two element sets" table M1–M8 and its §8 questions Q1/Q2/Q4/Q5/Q6/Q9/Q10); specs/trd-template.md; specs/bin-land-trd.md (the sibling precedent for a bin/ tool TRD); reviews/directive-authoring-cycle-3.md (findings F-1, F-2, F-3, deferred to this stage by standing ruling); bin/cycle-open's source and bin/tests/test_cycle_open.py (the migration target G0 preserves).

AUTHOR specs/directive-tooling-trd.md, frontmatter exactly: status: draft, last-reviewed: null, audience: [human]. Dave's standing ruling, 2026-08-28: PRDs and TRDs are audience [human]; do not add role audiences whatever the TRD template prescribes.

SCOPE of the TRD — decide mechanisms for what the PRD routes here, satisfying each stated property:
- Q1 (where invariant text lives, how the generator resolves it) and Q10 (how the skeleton holds G3's invariant): both marked resolved at the TRD stage; decide them jointly, since the PRD notes each choice constrains the other. State the decision and the property it satisfies.
- Q9 (the disposition label's lexical form): resolved at the TRD stage; decide it, satisfying the single-source property, and state which three PRD criteria it unblocks.
- M3's markdown sensitivity beyond the fence exclusion, and G11's marker syntax: decide both.
- Q2, Q4, Q5, Q6: each marked resolved by Dave. For each, present the options and tradeoffs the PRD states, add any the design surfaces, and mark a recommendation — but write the TRD so it stands whichever way Dave rules, or flag the sections that cannot. Do not present these as decided.
- Architecture, module boundaries, the G0 migration plan honoring AC-CO-1..12 and AC-DT-14/15/16, error and exit-status model within Q6's bounds, test strategy against the fixture-repository substrate §6 mandates.
- Address F-1, F-2, and F-3 from reviews/directive-authoring-cycle-3.md as this stage's obligations; record a per-finding disposition in the report. If any is not a TRD-stage matter on reading, say so with the reason rather than absorbing it.

The four removal categories that bind the PRD bind this document from birth: no provenance tags, no changelog prose, no closed questions, no per-citation SHAs in the body. Substance only, in the agreed PRD's register.

AFTER WRITING: run bin/check-frontmatter --all from the worktree; it must exit 0. Commit specs/directive-tooling-trd.md alone with message "directive-tooling TRD: initial draft". Push. Open a pull request from directive-tooling-trd to main titled "directive-tooling TRD" — and never merge it; merging is not this session's to do under any circumstance.

CLEANUP — after the report is composed and all pushes are verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-dt-trd" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed, so the session can be closed without leaving a claim on the branch.

STOP CONDITIONS, pinned to reviewed ref 79228c0dc7e1e25586701a054cda99eb9bb68059: on any failed command, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; TRD commit SHA; PR number; per-question disposition for Q1/Q2/Q4/Q5/Q6/Q9/Q10 (decided vs recommended-for-Dave, one line each); F-1/F-2/F-3 dispositions; check-frontmatter exit code; anything observed that this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
