# Review: process/decision-log.md — process-sweep-read-20260907T060000Z

Verdict: ready-with-findings
Reviewed: process/decision-log.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/decision-log.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 29 lines, with all three bracketed ids — R0583, R0592, R1603 — resolved to their files under rules/ at the base ref, and the entry form compared field by field against the baseline.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; decisions/log.md @ a00deba, whose entries this form governs and against which the ID arithmetic and the collision rule were checked.
Not inspected: whether every entry in decisions/log.md conforms to the form — the log is data this document governs going forward, not part of this delta. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 1 — 0 blocking, 1 non-blocking
The human should inspect: nothing. DL-01 is a citation placement that costs nothing in substance.

## Verdict (citations): ready-with-findings

See DL-01. All three ids resolve to rows in force and all three rows are the document's governing rules; the finding is where they sit, not whether they belong.

## Verdict (loss): ready

Every obligation survives or is cited. The entry form block is verbatim, including the `(omit if none)` on `Supersedes:`. The four field explanations fold into the block's placeholder text without loss: `Date` as `YYYY-MM-DD`, `Decision` as the ruling in one or two sentences, `Context` as the problem it settled, `Supersedes` as the old ID omitted where there is none. "There is no author field" survives as "carries no author field". The ID arithmetic keeps the form, the step of ten, the start at `DEC-000010`, uniqueness within the log, never-reused, and the last-plus-ten derivation with the append-only guarantee behind it. The collision rule keeps plus-one-within-the-gap, both worked numbers, the never-by-another-ten prohibition, the it-is-the-one-admitted-edit statement, and "changes a number, never a decision". "One file, not one file per entry" is carried by "Each project keeps one log at `decisions/log.md`". Two cut sentences were checked: the three rules the baseline's opening block spelled out — R0583, R1603, R0592 — are now carried by citation rather than restated, which is the sweep's seventh criterion applied exactly; and "Whether a decision is still live ... is answered by searching its ID in later `Supersedes:` lines — the Lexicon's `live decision` (R0594)" leaves the document, but R0594 defines the term in the store and the baseline itself framed it as something this document does not decide.

## Verdict (residue): ready

Every sentence is an act, a condition, or a form. "The principle" and its bolded thesis, "A decision made once is found and honored rather than silently re-litigated", the `grep DEC-000070` illustration, "The step of ten exists for exactly this", and both "What this does not decide" items are gone. The document is now three paragraphs and a form block, and each paragraph does one job: where the log lives and what an entry is, how an ID is assigned, how a collision is resolved.

## Verdict (keys): ready

`[chief-of-staff]`, unchanged, with `session: [decision]`. Every act — keeping the log, appending an entry in the form, taking the last number and adding ten, renumbering a collision — is the Chief of Staff's, and no act in the document names another performer. The human rules; the Chief of Staff records. That division is not stated in the new text and does not need to be: the baseline stated it only in the cut "no author field" reasoning, which the surviving clause carries.

## Verdict (loadable): ready

The sweep removed every heading and kept every rule, so nothing points at a heading that is gone. The form block sits where the first paragraph introduces it ("An entry takes this form"), and the two paragraphs after it read in order — assign an ID, then resolve a collision — which is the order an appending session meets them in.

## DL-01 — non-blocking
Claim: `[R0592]` and `[R1603]` sit on a sentence about where the log lives, which relies on neither.
Location: process/decision-log.md:10-11 — "Each project keeps one log at `decisions/log.md`, and the methodology repo keeps its own for methodology decisions [R0583, R0592, R1603]."
Evidence: Read by inspection against the diff. R0583 is "Append to `decisions/log.md`; never edit or delete an entry already there" and does support the sentence's path claim. R0592 is the supersede-by-appending rule and R1603 is "One decision per entry" — neither says anything about how many logs there are or where they sit. The baseline named all three in an opening block that said what they were: "The rules with teeth stay rows and are not restated here: **R0583** ..., **R1603** ..., and **R0592** ...". The sweep cut that block and moved the three ids onto the document's first surviving sentence, which is the sweep's seventh criterion applied to a block that was already a list of citations rather than a restatement — so the ids are hoisted to the head of the document rather than misattributed to a claim they contradict.
Consequence: The document's substance is intact and both rows stay in force and reachable from it. The cost is that a reader resolving R1603 from this sentence gets a rule about entry contents, and that the sentence's own claim — one log per project, the methodology repo keeping its own — is left with only R0583 behind it, which names the path but not the arrangement. No obligation is falsely presented as governed, which is why this is not blocking.
Fix: Move R0592 and R1603 to the clauses they govern — R1603 onto "An entry takes this form", R0592 onto the `Supersedes:` line's description — or state once, in a clause of its own, that the document's governing rows are R0583, R0592, and R1603.
