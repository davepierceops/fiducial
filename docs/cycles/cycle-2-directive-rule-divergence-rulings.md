You are an execution session for davepierceops/fiducial. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin rule-divergence-rulings-gate && git worktree add --no-track -b rule-divergence-rulings-cycle-2 "$TMPDIR/rule-divergence-rulings-cycle-2" origin/rule-divergence-rulings-gate && cd "$TMPDIR/rule-divergence-rulings-cycle-2"
~~~
Write this entire block, verbatim, to docs/cycles/cycle-2-directive-rule-divergence-rulings.md. Commit with message "docs/cycles: land rule-divergence-rulings cycle 2 directive". Push with `git push origin rule-divergence-rulings-cycle-2`. Verify with `git ls-remote origin rule-divergence-rulings-cycle-2`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: 21b60b32303cdd5c89e1574f551485474f515123 (the nine documents); review artifact reviews/rule-divergence-rulings-cycle-1.md @ 1d67b6b762c0d89f87739ff36c20959f7213812b. Prior directive: docs/cycles/rule-divergence-rulings-20260825T1900.md @ 96c19d2.
STOP CONDITIONS — stop and report, do not recover:
- `git diff --stat 21b60b3 -- docs/global-context context-sets policies roles skills LEXICON.md operating-model.md` is non-empty.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — apply Dave's decisions (2026-08-26, decision session; all *told*) on every finding in the cycle-1 review artifact. Read the artifact in full; each finding's Location and Fix locate and shape the edit. Do not touch text outside the findings. Do not flip status. The status flips the pre-commit hook makes on edited files are correct and expected; let them stand.

DECISIONS — one entry per finding; this directive is the decision record.

B1, B2 (core.md:25, C001 exception) — MODIFY. Replace the exception sentence with, verbatim: "A conflict between a canonical document and an artifact derived from it stops work on the conflicted item; surface it." Whole-session stop and "waits for Dave" are both removed. The source-of-truth policy's item-scoped statement is now the one Core agrees with; confirm and leave it.

B3 (operating-model.md:209, definition of done) — ACCEPT reviewer's fix: the bullet requires the tests to have been confirmed failing on bad logic, not only on an absent import, then turned green.

N1 (roles/coder-agent.md:21) — ACCEPT reviewer's fix; align to the behavioural red.

N2 (policies/source-of-truth-policy.md, "Keeping derived artifacts honest") — ACCEPT, cut: remove the sentence that restates Core rule 13. The policy states nothing Core states.

N3 (roles/test-designer-agent.md:26) — ACCEPT reviewer's wording verbatim: "run the red-gate before handing off to the Coder — confirm the tests fail on bad logic, not just on an absent import."

N4 (specs/directive-tooling.md:155) — ACCEPT reviewer's fix: update the quoted pre-edit operating-model line to the current text. This is the only edit outside the nine documents; it is permitted.

N5 (CLAUDE.md:31) — ACCEPT reviewer's fix; align to the behavioural red.

N6 (core.md:32, rule 13 decision-session branch) — ACCEPT reviewer's fix: a decision session edits the artifacts it authors and names every place outside them.

O1, O2 — observations, no action.

VERIFY before committing: run `bin/check-frontmatter --all`; must be green. Re-read every Location in the artifact and confirm the edit matches the decision. For B1/B2, confirm core.md and source-of-truth-policy.md now state the same scope.

COMMIT AND PUSH: one commit, message "cycle 2: rule-divergence-rulings — apply cycle-1 findings". Push with `git push origin rule-divergence-rulings-cycle-2`. Verify with `git ls-remote origin rule-divergence-rulings-cycle-2`.

DO NOT: edit files outside the findings' Locations plus the directive; flip status by hand; edit the register, clusters, or review files; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Content commit SHA with `git diff --stat`.
3. Per-finding line: id, file:line, applied/deviated, and any deviation's reason.
4. `bin/check-frontmatter --all` result.
Label every claim in the report observed, inferred, told, or unknown.
