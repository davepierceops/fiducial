# Review: intake/adopter-preserve-modes — read-20261111T001500Z

Verdict: ready-with-findings
Reviewed: intake/adopter-preserve-modes @ 67e94f2
Baseline: intake/adopter-preserve-modes @ b71922a
Reviewer: independent reviewer-agent (re-read over the amendment only)
Date: 2026-11-11
Scope: `git diff b71922a..67e94f2` (bin/tests/test_remaining_role_pruning_continuation.py only). This is a re-read over the amendment only, not the whole branch. Disposition of the earlier read's F1: resolved, see below.
Cross-checked: reviews/adopter-preserve-modes-read-20261110T235600Z.md (F1); bin/tests/test_review_verification_pruning.py (LANDED precedent); `inputs()` in bin/tests/test_skill_context_extraction.py; `FileRowSource.named_queries_text` in bin/rulestore/store.py; /tmp/411-evidence/411-oracle-after.log (8 OK), /tmp/411-evidence/411-suite-final.log (348 OK).
Not inspected: the rest of the branch (covered by the earlier read); the pre-amendment failure itself (taken from F1, not rerun); a shallow clone lacking 5b2a62f (not constructed).
Findings: 1 non-blocking

## Quality pass

Verdict (quality): ready-with-findings

F1 disposition: resolved. The finalization class now pins to 5b2a62f, so the approved one-sentence change to process/adopt.md no longer reaches the two tests that failed. The check is not weakened.

Verified by running or reading:
- 5b2a62f is the right commit: `git log -1 5b2a62f` gives "Merge pull request #432 from davepierceops/intake/remaining-role-pruning". It is an ancestor of HEAD and a descendant of CHECKPOINT 4157ddd.
- Nothing compared before is dropped. `self.live` is still `inputs(root)` over the same tree layout, and the named-queries read still goes through `FileRowSource`; only the root changed. `git diff 5b2a62f HEAD -- rules process bin/hooks` is process/adopt.md alone (6 insertions, 2 deletions). The row-record, native and bundle assertions therefore see the same data they would have seen at merge time, which is what "the batch as it landed" means.
- `git archive LANDED rules process bin/hooks` covers every path needed: `inputs()` reads `rules/`, `process/` and `bin/hooks` via FileRowSource and the hooks glob, and `named_queries_text()` reads `process/named-queries.md`. `load_tiers()` takes no root. The archive lists nothing outside those three trees.
- The assertions left on REPO_ROOT are the right ones. DEC-001720 in `decisions/log.md` and the `rules/retired/*.md` archives are append-only facts that must stay true of the live tree; pinning them would hide a later deletion.
- Clone depth: no new class of dependence. BASELINE and CHECKPOINT are already resolved with `git archive`, so the class already fails in a clone lacking those commits. 5b2a62f is newer than both, so any history containing them and the branch tip also contains it. The repo here is shallow and all three resolve.
- Reran `cd bin && python3 -m unittest tests.test_remaining_role_pruning_continuation`: 8 OK. Logs show 8 OK and 348 OK.

## F2 — non-blocking
Claim: The shared `setUpClass` still builds `cls.bundles` from the working tree's named-queries text while finalization now reads names from the landed snapshot.
Classification: suggestion
Location: bin/tests/test_remaining_role_pruning_continuation.py:~80 (`named_queries.bundles(FileRowSource(REPO_ROOT)...)`) vs the changed line in `test_live_native_and_all_bundles_equal_preview_with_hooks_unchanged`
Evidence: read; `git diff 5b2a62f HEAD -- process/named-queries.md` is empty, so the two sources agree today. Not demonstrated to fail.
Consequence: If a later approved change edits process/named-queries.md, `self.bundles[name]` is keyed by the working-tree names and the landed loop looks up the landed names, so the test could fail with a KeyError or a name-count mismatch. That is the same class of failure F1 described.
Fix: Read the checkpoint's named-queries text in the shared `setUpClass` (`FileRowSource(cls.checkpoint_root)`), or leave it and accept the risk until that file changes.
