# Review: process/review-artifact.md — process-sweep-read-20260907T060000Z

Verdict: changes-required
Reviewed: process/review-artifact.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/review-artifact.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 66 lines, with all four bracketed ids — R1395a, R1396, R1408, R1414 — resolved to their files under rules/ at the base ref, and the seven rows under topic `review-artifact-schema` listed to check what the document leaves to rows.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; rules/R0489.md, for where a ship recommendation is required and where the schema would put it; decisions/log.md @ a00deba DEC-000490.
Not inspected: whether existing artifacts under reviews/ conform to the swept form — R1408 forbids retrofitting them, so conformance of the back catalogue is not a defect in this document. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 2 — 1 blocking, 1 non-blocking
The human should inspect: RA-01. The mapping table it names is the only place in the corpus that told an agent where a role document's required output goes in this schema, and the sweep cut it whole.

## Verdict (citations): ready

All four resolve. `[R1396]` at line 10 states the sentence it carries word for word — "one read over one delta, one artifact — whatever the review procedure". `[R1395a]` and `[R1408]` at the same position stand in for two sentences the sweep cut from exactly there: "Written in the execution session that runs the review" and the whole no-retrofit paragraph. `[R1414]` at line 40 states the overall-plus-per-pass verdict rule, the three admitted values, the most-severe ordering, and the gloss on `ready` — the sentence relies on nothing R1414 does not say.

The triage half — "triaged in a decision session" in the baseline — left this document without a citation here. It is carried by R1395b, cited in process/change-flow.md at the same ref, so it is not lost from the corpus; the pair R1395a/R1395b is split across the two documents rather than dropped.

## Verdict (loss): changes-required

See RA-01. Everything else the diff cut is covered. The filename rule keeps both halves of the stem convention and the digit-suffix case, dropping only the reasons for them ("so a reader derives the artifact's path from the document's path without looking it up"; "a special case would cost more than the repetition does"). `Not inspected` stays required, losing only the sentence explaining why. The `Evidence` verified-by-running-vs-inferred-by-reading distinction survives inside the form block and the observation test survives in prose. "No prose." is now the positive rule "Write prose only where judgment does not compress". "What this schema governs" and "What this document changes" are the document's record of itself and its scope framing — criteria 4 and 5 — and go correctly.

## Verdict (residue): ready

Every sentence is a form, a condition on the form, or an act. The per-entry-log carve-out at line 11 is a recognition condition an agent needs in order not to apply the header block per line, and stays.

## Verdict (keys): ready-with-findings

See RA-02.

## Verdict (loadable): ready

Both surviving headings carry their content. The "## Prose" heading was removed and its rule folded into the Findings section, with nothing referring back to it. Both form blocks are intact and no sentence points at a section that is gone.

## RA-01 — blocking
Claim: The table routing each role's or policy's required output to a field of this schema was cut whole, and nothing in the new text or in a cited row replaces it.
Location: process/review-artifact.md — absent; baseline process/review-artifact.md @ 7549f7e, the block beginning "Where a role or a policy names a required output, this is where it goes:"
Evidence: Read against the diff. The cut table mapped seven required outputs to fields: sign-off and the overall ship call to `Verdict`; required changes to `blocking` entries; advisory items to `non-blocking`; required follow-ups to the finding's `Fix`; risks and verification gaps to `Consequence` and `Not inspected`; evidence inspected and scope reviewed to `Scope` and `Cross-checked`; what the human should inspect to that field. The sentence under it — "The entry field is `Fix`, not `Recommendation`." — was cut with it. R0489 requires "a ship recommendation" in the release package; no surviving sentence and none of R1395a, R1396, R1408, R1414 says where a recommendation lands in an artifact. The sweep report is not committed, so whether this is among its six intake candidates could not be checked.
Consequence: An agent holding a role document that demands a recommendation, required follow-ups, or a statement of risks and verification gaps now has to guess which of the schema's fields receives each. The form block constrains the fields available, so the likely failure is silent omission — a required output that has no obvious field simply does not get written — rather than a malformed artifact. That is the harder failure to detect, because the artifact still validates against the form.
Fix: Restore the mapping as a table or as one sentence per row of it. At minimum restore the two lines that resolve a real naming collision — required follow-ups go in the finding's `Fix`, and the overall ship call goes in `Verdict` — since role documents use the words "recommendation" and "follow-up" and this schema uses neither.
Related: RA-02

## RA-02 — non-blocking
Claim: `release-manager-agent` is in the role list but performs no act in the document since the mapping table was cut.
Location: process/review-artifact.md:3 — `role: [spec-reviewer-agent, context-quality-reviewer, reviewer-agent, skeptic-risk-agent, release-manager-agent, copy-editor, critic]`
Evidence: Read by inspection. The role list is unchanged from the baseline. In the baseline the Release Manager's connection to this document was the table's first row — the overall ship call, which is R0489's output, landing in `Verdict`. With the table gone, no sentence in the document names an act the Release Manager performs, and the surviving text is about running a review and filing findings, which is not its role.
Consequence: The document is selected into the Release Manager's bundle and gives it nothing to do. Under the sweep's ninth criterion, a role listed with no act is what the per-document role decision is meant to remove; leaving it costs a document in a bundle that has no use for it.
Fix: Restoring the mapping table (RA-01) restores the act and the key is right as it stands. If the table is not restored, drop `release-manager-agent` from the list.
Related: RA-01
