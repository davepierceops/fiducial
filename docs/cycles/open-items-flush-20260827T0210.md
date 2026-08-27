OPEN-ITEMS flush, 2026-08-27. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE. Create the tree with `git worktree add --no-track "$TMPDIR/open-items-flush" -b open-items-flush-20260827 origin/main` from the main clone and work only there. If the add fails for any reason, stop and report; do not retry with different flags.
Write this entire block, verbatim, to docs/cycles/open-items-flush-20260827T0210.md. Commit with message "docs/cycles: land open-items-flush directive". Push with `git push origin open-items-flush-20260827`. Verify with `git ls-remote origin open-items-flush-20260827`. Report "landed <path> as <sha>" using the SHA read back from git.

REVIEWED REF: d0d792f3b1854b7f57d06f39dd0c350447df7585 (main). OPEN-ITEMS.md is a tracker, outside the frontmatter set; no status flips, no gate. This directive is the origin of every word below; copy it exactly.

STOP CONDITIONS — stop and report, do not recover:
- `git rev-parse origin/main` is not d0d792f before your first content commit.
- Any tree mutation you did not intend, including your own.
- Any push fails.

EDIT 1 — header. Replace the line `Last updated: 2026-08-24` with `Last updated: 2026-08-27`.

EDIT 2 — strike one item. Find the heading line exactly `## \`bundle base\` red — stale AC after the decision-log citation`. Wrap its text in `~~` so it reads `## ~~\`bundle base\` red — stale AC after the decision-log citation~~`. Immediately after that heading and its blank line, insert:

**RESOLVED** by PR #221 (`448e93e7`), 2026-08-27: `bin/tests/test_bundle.py` was deleted along with `bin/bundle-methodology` under DEC-000210, because its tests exercised the positional closure mode removed under AC-BA-7. Directive `docs/cycles/retire-bundle-methodology-20260827T0120.md` @ `c695d881`; gate `reviews/retire-bundle-methodology-cycle-1.md` @ `32371f14` (RBM-1). Suite 441/2-failing → 424/0.

**Original entry, kept for the record:**

(then the existing body follows unchanged.)

EDIT 3 — append at end of file, after a `---` separator, the following nine entries verbatim, each separated by `---`:

## `bin/bundle` output format does not match DEC-000210

**Source:** CoS session 2026-08-26, on regenerating the CoS bundle. `bin/bundle --audience <value> --out DIR` writes `bundle-<value>-<stamp>.md` with a `# bundle-<value>` header. DEC-000210 carries forward from DEC-000190 the filename `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md`, the `Source: @ <repo HEAD>` line, the per-file blob short-SHA, and the `<!-- FILE n/N: path @ sha -->` separators. The separators and blob SHAs match; the filename and header do not.

**What's needed:** a change to `bin/bundle`'s ACs (AC-BA-*), as a package under the bundle-system PRD. Until then, the bundle uploaded per project is the `bundle-chief-of-staff-*` file `bin/bundle` emits.

## Bundle-system PRD draft is uncommitted

`~/Downloads/bundle-system-prd-draft-20260825T023000.md`, status draft, on Dave's disk only. DEC-000210 cites it as the decision's context and names the `bundle-methodology` removal (now landed, PR #221) as a package under it.

**What's needed:** commit it under `specs/`, then the spec-review cycle.

## `CLAUDE.md` carries a derived copy of governed rules

**Source:** pass-2b gate, `reviews/pass-2b-rulings-cycle-1.md` @ `32371f14` (F1), 2026-08-26. The adapter's "Required behavior" list restates ten rules from `operating-model.md` and is now stale on the C018 wording. It also says guidance lives under `/ai/` (the repo was renamed) and points at `context-sets/base.md` and `context-sets/collab-workflow.md`, whose presence in the current corpus is unverified. Deliberately not edited by the pass-2b directive: adapters are outside the governed set.

**What's needed:** cut the file to what an adapter is — a pointer at the bundle or the reading list, no restated rules. Outside the frontmatter set, so a plain commit; fix the stale paths in the same commit.

## `specs/directive-tooling.md` names a retired binary

**Source:** `reviews/retire-bundle-methodology-cycle-1.md` @ `32371f14` (RBM-4), 2026-08-26. Line ~2051 lists `bundle-methodology` in a `bin/` inventory marked observed; the binary is gone as of PR #221. The spec is `agreed`, so the fix is a cycle. Bundle with the stale AC-CO-3 pointer and the three findings `skills/directive-authoring.md` defers to the TRD stage, so the document opens once.

## Corpus dedup, Passes 1–2b — closed

Record only. Pass 1 extracted 878 rules (`docs/rule-register/rule-register-20260825T1435.md`); Pass 2 clustered 220 of them into 77 clusters (`docs/rule-register/rule-clusters-20260825T1600.md`). Rulings: C001–C008 (`rule-divergence-rulings`, PR #211); the 69 agreeing clusters (`docs/cycles/agreeing-clusters-collapse-20260826T2120.md`, `agreeing-clusters-collapse-2-20260826T2200.md`, PRs #215–#217); Pass 2b, the eleven agreeing clusters found divergent on reading (`docs/cycles/pass-2b-rulings-20260827T0025.md` @ `94c01bf7`, PRs #218–#220 — three edits, eight accepted as consistent). Net corpus change was about −70 lines; Pass 2's "a quarter of the corpus restates itself" did not hold — the clustering over-matched.

## Candidate methodology changes from the dedup sessions

Each is a full cycle on a gate document; none is decided.

- **Rubric criteria 3, 4, 6, 11, 12 are absence tests.** Restate affirmatively (e.g. 4 → "every rule is stated in exactly one governed file, and this file is that one"). Dave's concern: negated framing primes the forbidden thing and yields uncitable "I didn't see one" findings. Run the same audit over `docs/global-context/core.md` and `decision-layer.md`.
- **Multi-document review artifacts.** A gate over a branch is now practice (PRs #211, #215, #218, #221) but `skills/spec-review-cycle.md` and `skills/review-artifact.md` are written for one document, one stem. Write the case in: artifact stem names the branch; `Reviewed:` lists the documents; `Baseline:` carries the pre-change ref.
- **Bundle invariant.** A rule may be deleted from file A only if the home B's audience covers A's; otherwise the duplicate is legitimate. Lives only in a collapse directive today; belongs in the rubric.
- **Decision-layer 3, "landmine".** Add a test: something Dave would act on differently, or be surprised by, if unnamed. Expected tool behaviour and items already on the tracker or baton are not landmines. Observed 2026-08-26: the label was being spent on nothing, training the reader to skip it.
- **Executor STOP wording.** State the tree-mutation stop on intent, not cause: "any tree mutation you did not intend, including your own." Used in the pass-2b directives; the gate executor stopped correctly under it.

## Executor self-recovery — tracked behaviour defect

Two instances: the agreeing-clusters gate executor ran `git checkout <sha> -- .`, staged branch content by mistake, reset itself, and continued (2026-08-26); the pass-2b executor's `git worktree add -b … origin/<ref>` failed on a sandbox `.git/config` write-deny, and it deleted the stray ref and retried with `--no-track` (2026-08-26). Neither damaged anything; both flagged honestly; both should have stopped. Under the intent-based STOP wording above the pass-2b gate executor did stop on the same failure. Operating note: in the sandbox, create worktrees with `--no-track`, or check out an existing local branch.

## Worktree and branch pile

About 31 `$TMPDIR` worktrees registered against `~/code/fiducial`. Branches to delete, all merged: `log-dec-200-210`, `rule-extraction-pass1`, `rule-dedup-pass2`, `rule-divergence-rulings`, `rule-divergence-rulings-gate`, `rule-divergence-rulings-cycle-2`, `rule-divergence-rulings-gate-2`, `flip-rule-divergence-rulings`, `flip-directive-tooling`, `untag-specs-audience`, `agreeing-clusters`, `agreeing-clusters-gate`, `flip-agreeing-clusters`, `pass-2b-rulings`, `pass-2b-rulings-gate`, `flip-pass-2b-rulings`, `retire-bundle-methodology`, `retire-bundle-methodology-gate`, `open-items-flush-20260827`. One command block from the CoS; the `retros/` untracked files in the main clone are Dave's and are not touched.

## Corpus defects carried from prior batons

- Four untriaged finding classes against agreed `specs/bin-land-trd.md`: completeness gap, coverage gaps, unverified boundary conditions, open questions.
- DEC-000140 sweep still owed.
- `roles/architect-agent.md` session-kind self-contradiction; C053 touched the file — re-check before opening a cycle.
- Six methodology decisions from the 15-hour session not yet in `decisions/log.md`.
- Writing corpus: the GitHub connector cannot see `davepierceops/writing` (404); `prose-criteria.md` audience tag defect.

VERIFY: `git diff --stat origin/main -- OPEN-ITEMS.md` shows one file; `bin/check-frontmatter --all` exits 0; the file's first 8 lines and its final entry match this directive on read-back.

COMMIT AND PUSH: one commit, message "OPEN-ITEMS: flush 2026-08-27 — strike 1, add 9". Push with `git push origin open-items-flush-20260827`. Verify with `git ls-remote origin open-items-flush-20260827`.

DO NOT: edit any other file; open a pull request; merge; delete branches or worktrees.

REPORT:
1. Directive path and landed SHA.
2. Commit SHA with `git diff --stat`.
3. check-frontmatter result.
Label every claim observed, inferred, told, or unknown.
