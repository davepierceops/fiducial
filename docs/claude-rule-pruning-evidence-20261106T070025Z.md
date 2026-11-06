# CLAUDE.md pruning — candidate evidence

Reviewed source: `722dc0482fd689c48ce16136926e0f272204a8a0`; baseline: `fb310dd9c1ea56e4fa2e1b9b671a50c128fdec0f` (PR #423). Human rulings: `docs/plans/claude-rule-pruning-rulings-20261105T221134Z.md`. Related issue: #403.

## Status and scope

Observed: the human finished all original standing-rule rulings. The projected result contains 18 standing instructions and 18 pulled definitions. Definitions were not independently pruned. Twenty-three rows have successor archives; 43 more (33 removals and 10 skill moves) await their real merge-time decision ID. R0196/R0564 retain enforcement blocks with no standing prose. The source branch and temporary projection are not yet landable or installed; do not merge until finalization below.

The generated preview is the pinned source with exactly the manifest’s pending rows omitted. The projection archive marker `pending-merge-decision` is deliberately not a valid final retirement ID. No DEC number has been reserved or invented.

## Context measurements

Observed physical lines and whitespace-delimited words, not tokens or billed context. Both generated roots change from **241 to 75 lines** and **3,252 to 1,069 words** (2,183 fewer words; 67.1%). Installed ownership markers add two lines and six words: 243→77 lines and 3,258→1,075 words.

Native agent-only text grows because definitions previously supplied by the root now appear where specialized rules still need them. Root plus any one native agent is nevertheless smaller: 1,889–2,134 fewer words for Claude Code and 1,897–2,137 fewer words for Codex. Retired and moved instruction bodies are absent from every generated root and agent; definitions supporting unchanged specialized rules remain.

| Standalone role | Words before | Words after |
|---|---:|---:|
| chief-of-staff | 11,098 | 10,347 |
| architect-agent | 4,201 | 4,136 |
| spec-reviewer-agent | 5,079 | 4,400 |
| test-designer-agent | 4,336 | 4,274 |
| coder-agent | 4,172 | 4,364 |
| reviewer-agent | 5,859 | 5,181 |
| skeptic-risk-agent | 5,870 | 5,192 |
| release-manager-agent | 6,067 | 5,478 |
| context-quality-reviewer | 3,884 | 4,013 |
| writer | 4,897 | 5,632 |
| copy-editor | 5,580 | 5,722 |
| critic | 5,347 | 5,489 |

Some standalone bundles grow because previously role-limited process documents now carry moved shared instructions, with their original software/role scopes stated inside. This is not a claim of universal bundle or total disk-text reduction. Skill procedures load on demand in native harnesses; real invocation/adherence has not been measured.

## Verification

- Observed: `bin/tests/run` passed 318 tests in 111.887 seconds at 74f619c (complete implementation before the final prose-only scope fix). Seven pruning contracts passed in 16.110 seconds after that scope correction at 722dc04.
- Independent Test Designer authored tests before the definition-closure implementation. A synthetic process-only/transitive-definition test failed before the fix and passes afterward. Historical PR #423 guarantees are checked at their landed SHA, while present-day preservation checks remain.
- Contract checks cover the exact approved retirement set, preserved original bodies/metadata, successor scope unions, all original moved-procedure role/corpus/session combinations, roots and all 16 native agents, definition closure, and all twelve standalone role bundles.
- Existing hook scripts, deny/settings/hook configuration and executable modes match the baseline byte-for-byte. This checks generated artifacts, not live native or forge enforcement.
- 28 of 30 generated skills pass skill-creator quick validation. Both gate skills are rejected solely for the pre-existing `disable-model-invocation` field, which that validator’s whitelist does not recognize; the gate invocation policy is unchanged. No validator dependency was installed for this batch; the existing isolated validation environment was reused.
- Adoption prepare inventoried 67 existing paths and planned 47 writes, with zero mechanical conflicts. No apply or label command was run. Independent review checks the actual candidate/inventory, not only the helper’s merge result.

## Independent review

Observed: `reviews/claude-rule-pruning-read-20261106T070137Z.md` returns ready for quality, skepticism and continuity, with no remaining findings at 722dc04. The independent frontier reviewer reproduced all 65 native generated files and twelve bundles, checked all 67 adoption inventory entries and 47 planned writes, and recorded zero contradictions in the projection-labelled adoption review. Its scope explicitly excludes merge-time decision allocation, installation and final readback.

## Remaining finalization

The intake process requires independent review and human process signoff. After signoff/merge authorization, allocate the actual retirement decision ID from the then-current log, archive the manifest’s pending originals with that ID, and record the allocation. Final archive-integrity checks must reject all pending markers. Verify final generated bodies/security artifacts equal this reviewed projection except for source provenance, prepare the real ownership-preserving self-adoption candidate, complete independent readback/equivalence review, apply and check exact bytes/modes plus a no-op rerun, and run the required final checks before merge. No tagged release or adoption into another repository is included.

Unverified: live model behavior, native skill invocation, current forge enforcement, and any claim of token or cost reduction. The preview proves local source/output contracts only.

## Local evidence hashes

- `/private/tmp/fiducial-pruning-suite.txt` — SHA256 `2b5a59be0e8ff99a1d0175e856306865a5dd2838016baf2324d9fb9a16d92386`
- `/private/tmp/pruning-test-design-final.log` — SHA256 `38c46067a519223da08b3cb7b17f87488c5030951924bdd4cc7bde30c187656b`
- `/private/tmp/fiducial-pruning-amendment-tests.txt` — SHA256 `4e626f155286ae60f6ea5f1c272a88afda12565638e5a76a226b2a63ee8ea461`
- `/private/tmp/fiducial-pruning-skill-validation.txt` — SHA256 `07e7425c410373dedc9915b4e49d3c33eb5aa107f3e208c064b2599d805da0a3`
- `/private/tmp/fiducial-pruning-adoption-preview-v2/plan.json` — SHA256 `3583156bc1f31446cfe186929d1ce59df2e3075f87ff3516aeac4d265536f5c8`
