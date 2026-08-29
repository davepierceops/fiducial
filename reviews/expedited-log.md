# Expedited Review Log

One line per expedited or doc-only agreement, per the "Expedited return to
`agreed`" and "Doc-only cycle" sections of
`policies/document-metadata-policy.md`. Documents agreed either way
carry `last-reviewed: reviews/expedited-log.md @ <sha>`; the SHA selects the
entry.

Append-only. Entries are not edited or removed when the document they describe
is later revised, superseded, or deleted — this is a record of agreements, not
a description of current state. Newest last.

This file is a dated record: each entry states a fact about one agreement on
one date. It carries no totals, rates, or rollups, and nothing derived from it
belongs in canonical policy text.

Format — one Markdown list item per entry:

`- <YYYY-MM-DD> — <document path> @ <sha> — <what changed, one clause>`

Where the document is new — which the doc-only cycle admits and the expedited
path does not — nothing changed, so the last clause states what the document
is instead.

The SHA is authoritative. The date and the one-clause summary are reader
convenience — both are derivable from the commit it names, and on any conflict
`git show` wins. They are written out anyway because a log of bare paths and
hashes is a log nobody reads, and this file is a dated record, which is where
derived facts are allowed to live.

## Entries

- 2026-08-06 — policies/decision-log-policy.md @ 01fb1030e06dffa555ff6482eeda9a90f9e2b461 — founding decision-log policy, agreed via doc-only cycle (DEC-000020)
- 2026-08-07 — policies/document-metadata-policy.md @ 1f5b7153dc3140f500ceb5575f459f1098b23de0 — LEXICON.md added to in-scope set; owner override of doc-only condition 3, no review cycle (DEC-000060)
- 2026-08-07 — roles/chief-of-staff.md @ 81df6ddf0829fd23d4c7fe3a3516c8e0c4c9d245 — execution-report handling, sharpened pre-staging, decomp spec-SHA pin, directive-register compression; agreed via doc-only cycle (DEC-000070)
- 2026-08-11 — LEXICON.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — policies/remote-write-verification-policy.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — roles/chief-of-staff.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/command-blocks.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/directive-dispatch.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-11 — skills/spec-review-cycle.md @ c9e87ad253b5b9c2b67f4721d00e3d231c3326b3 — agreed via Dave's merge review of PR #67 (https://github.com/davepierceops/ai/pull/67)
- 2026-08-17 — engagements/comfy/README.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: engagement pack mapping doc (client-facing); agreed via Dave's merge review of PR #71 (https://github.com/davepierceops/ai/pull/71), preceded by clean-context spec review
- 2026-08-17 — engagements/comfy/policies/client-credentials-policy.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: zero-write rule with Dave-granted carve-outs; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/policies/override-log-policy.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: "I say override" protocol and retro-reviewed log; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/roles/cartographer.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: read-only discovery role with provenance discipline; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/roles/chief-of-staff-engagement.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: parent CoS amended for engagement state sources; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/roles/implementer.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: proposal-gated builder with infra evidence classes; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/roles/skeptic-engagement.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: standing clean-context review gate, lean output; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/skills/baseline-measurement.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: the baseline-gate procedure; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/skills/engagement-change-package.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: seven-item lean change package; agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/skills/speed-audit.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: the engagement play incl. Improvement Proposal definition (client-facing); agreed via Dave's merge review of PR #71
- 2026-08-17 — engagements/comfy/skills/system-discovery.md @ 9a8b8b0508c8f2aef5d388d9804906e3ad803293 — new: System Map procedure; agreed via Dave's merge review of PR #71
- 2026-08-23 — skills/directive-authoring.md @ 48ad7fd1e827a7c92660fd2cd9ebc5871c1dbc21 — working-tree disposition made mandatory for every directive
- 2026-08-23 — skills/directive-authoring.md @ 83b60511f4cc6e0346b08e4e111a7c17a14bc0d9 — numbered cycle-directive form licensed alongside the timestamp form
- 2026-08-23 — skills/directive-authoring.md @ 6179221a013e8006e573d6a35a4dca75dd966ccb — timestamp form requires date and time components both present
- 2026-08-23 — skills/directive-authoring.md @ b4a0fa581ba5c64ac5a0e5374b5604e979a73653 — disposition must be its own labelled statement, mechanically distinguishable from incidental mention of trees or commands
- 2026-08-23 — skills/directive-authoring.md @ 7853525aedf831bcc07da3264c3af7a91825b048 — exactly one labelled disposition statement per directive
- 2026-08-24 — specs/bin-land-trd.md @ b31b75af12648585d7ac86f7c0d11ad85f883f5f — agreed via the expedited path, together with bin/tests/test_land.py at the same commit, on spec/test convergence rather than a ninth reviewer cycle
  - Evidence: four convergence rounds (`docs/cycles/bin-land-converge-1-20260824T031500Z.md`, `-2-20260824T033000Z.md`, `-3-20260824T041500Z.md`, `-4-20260824T113000Z.md`) opened the spec and the tests together so findings flowed both ways; a mechanical check parsed §7's twelve-code diagnostic table out of the spec and confirmed every code is asserted in `bin/tests/test_land.py`; the behavioural red-gate ran 440 tests, 137 failures, 1 skip, with every `test_land` failure behavioural against the stub (the only non-`test_land` failures are the two known, accepted AC-BN-10 bundle failures).
  - Why expedited rather than a review artifact: the last reviewer-gated cycle, `reviews/bin-land-trd-cycle-8.md`, returned changes-required; everything after it was spec/test convergence, not review. `policies/document-metadata-policy.md` frames the expedited path for small doc-only changes, not a 1,400-line TRD — Dave took it deliberately anyway, judging that forcing a ninth reviewer pass to satisfy a pointer would be ceremony over evidence already stronger, per `docs/cycles/bin-land-agree-20260824T124500Z.md`.
  - Open at agreement, not closed by it: OQ-1, OQ-2, OQ-3, OQ-4, OQ-6, OQ-7, OQ-9.
- 2026-08-24 — bin/tests/test_land.py @ 7cc7e48d20829da0bb720add243293c72f1c1335 — one case appended to the agreed suite, `TestLand02StagingIsAuthoritativeOverTheIndex`, covering AC-LAND-02's first arm where the index is pre-populated before the invocation
  - Amendment, not a new agreement: the suite was agreed with `specs/bin-land-trd.md` at b31b75af above, on spec/test convergence. This adds one case and one module-docstring paragraph recording it beside the existing non-ASCII fixture; no existing assertion, fixture, helper, or case is touched, `CASES` is untouched, and the case is not a twentieth terminal path — it is `success-head-moved`'s path run with a pre-populated index, so §5.4's enumeration of nineteen stands.
  - The implementation is unchanged: `bin/aimeta/land.py` is byte-identical to the merged implementation at 1373cb53f2fe9a9acd74c9c24120eb54050d21bb — blob 7c28ed36110b6c7388833ed33d940ee19ad181a2 both before the red-gate below and after it, `git diff` empty.
  - Mutation evidence, why the case exists: §3.2 step 7's `git reset --mixed <base>` survived the agreed suite. With the case added and the reset present, 441 tests, 2 failures, 1 skip (the two known AC-BN-10 bundle failures). With the reset and its guard deleted, 441 tests, 3 failures, 1 skip — the third `test_land02_a_path_staged_beforehand_is_not_in_the_commit`, failing on the committed set, `['unrelated.md', 'work.md'] != ['work.md']`: a behavioural failure on the pre-staged file appearing in the commit, not an error, and no other case in the suite moved. Line restored byte-identical, 441 tests, 2 failures, 1 skip.
- 2026-08-29 — public-prose-criteria.md @ dcb64275d2c69eac7623d3969acf2881343ac4e9 — new: the author-independent prose criteria applied to any author under this method, split from prose-criteria.md; agreed via doc-only cycle (DEC-000240)
- 2026-08-29 — voice.md @ a7e21331070ed5e554d7482b72a4bc50d57e5437 — new: the author-specific half split from prose-criteria.md — purpose and audience, register, profanity, vocabulary, mechanics, repo citation, venue, disclosure wording; agreed via doc-only cycle (DEC-000240)
- 2026-08-29 — roles/writer.md @ 5109df2fc8e7faa8eadcd98105be2bc51d346a1a — rewritten as agent instructions: binds to the Public Prose Criteria and the Voice document by name, outlines via the Outline skill, harvests voice rules at session close, offers the Copy Editor then the Critic; agreed via doc-only cycle (DEC-000230, DEC-000250)
- 2026-08-29 — roles/copy-editor.md @ a67c1a1e412fe0a5e93180abd6fc6ece527d46cf — new writing role: proofread and copyedit as tracked changes, four checklist passes as anchored comments, Google developer documentation style guide as base authority under the Voice document; agreed via doc-only cycle (DEC-000230)
