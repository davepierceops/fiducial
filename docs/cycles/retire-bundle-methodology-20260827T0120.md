Retire bin/bundle-methodology under DEC-000210. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE. Create the tree with `git worktree add --no-track "$TMPDIR/retire-bundle-methodology" -b retire-bundle-methodology origin/main` from the main clone and work only there. If the add fails for any reason, stop and report; do not retry with different flags.
Write this entire block, verbatim, to docs/cycles/retire-bundle-methodology-20260827T0120.md. Commit with message "docs/cycles: land retire-bundle-methodology directive". Push with `git push origin retire-bundle-methodology`. Verify with `git ls-remote origin retire-bundle-methodology`. Report "landed <path> as <sha>" using the SHA read back from git.

REVIEWED REF: 0ee38821648ece6def9c1cbba84ca7f089b3d881 (main). Governing decision: decisions/log.md entry DEC-000210 — read it first. It retires bin/bundle-methodology and its tests, not repaired; this directive carries out that removal only. bin/bundle's output format is out of scope here (a later package under the bundle-system PRD).

STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/main` is not 0ee3882 before your first content commit.
- Any tree mutation you did not intend, including your own.
- `bin/tests/run` at 0ee3882 does not report exactly 2 failures, both in bin/tests/test_bundle.py (test_bn10_*). If the baseline differs, stop.
- Any push fails.

BASELINE (record before removing anything): `bin/tests/run 2>&1 | tail -5`, captured to "$TMPDIR/retire-baseline.txt". Expected: 441 tests, failures=2, skipped=2.

REMOVE, with `git rm`:
- bin/bundle-methodology
- bin/tests/test_bundle_methodology.py
- bin/tests/test_bundle.py (its two tests exercise bin/bundle's positional closure mode, removed under AC-BA-7; nothing else in it)

Then grep the whole tree for `bundle-methodology`, `bundle_methodology`, and `test_bundle` (excluding decisions/, docs/cycles/, reviews/, OPEN-ITEMS.md, and this directive). Anything under bin/ that still references the removed files — helpers, the runner, imports — edit so the suite runs clean; report each such edit. Anything outside bin/ — expected: specs/directive-tooling.md and ACCEPTED-RISKS.md — do NOT edit; list each with path:line.

VERIFY: `bin/tests/run 2>&1 | tail -5`, captured to "$TMPDIR/retire-after.txt". Expected: 439 tests, failures=0, skipped=2. `bin/check-frontmatter --all` exits 0. `bin/bundle --audience chief-of-staff | wc -l` unchanged from 3217 — this change must not alter any bundle.

COMMIT AND PUSH: one commit, message "bin: retire bundle-methodology and its tests (DEC-000210)". Push with `git push origin retire-bundle-methodology`. Verify with `git ls-remote origin retire-bundle-methodology`.

DO NOT: edit any governed document; edit bin/bundle; open a pull request; merge; delete branches or worktrees.

REPORT:
1. Directive path and landed SHA.
2. Commit SHA with `git diff --stat`.
3. Baseline and after test lines, verbatim.
4. Edits made under bin/ beyond the three removals, if any, one line each.
5. Surviving references outside bin/, path:line.
6. check-frontmatter result and bundle line count.
Label every claim observed, inferred, told, or unknown.
