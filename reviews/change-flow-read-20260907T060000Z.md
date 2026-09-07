# Review: process/change-flow.md — process-sweep-read-20260907T060000Z

Verdict: changes-required
Reviewed: process/change-flow.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/change-flow.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names — citations, loss against the diff, residue against the sweep's ten criteria, role keys, bundle-loadability — over all 79 lines, with every one of the 38 bracketed ids resolved to its file under rules/ at the base ref.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md (the ten criteria); decisions/log.md @ a00deba DEC-000380, DEC-000460, DEC-000490; rules/R0003.md and rules/R0013.md when searching for a row stating the two-tranche cap.
Not inspected: process/voice.md; the sweep session's report, which is not committed anywhere on this branch, so the LOSS test's third limb — "listed in the sweep report's six intake candidates" — could not be applied and every cut obligation below is reported without that check.
Findings: 3 — 2 blocking, 1 non-blocking
The human should inspect: CF-01 and CF-02 together. Both are the same shape — an obligation that survived the sweep with no row behind it, carrying a citation to rows that state the obligation the sweep cut instead. The two-tranche cap (CF-02) is the one the directive asks about by name.

## Verdict (citations): changes-required

37 of the 38 bracketed ids resolve to a row whose body says what the citing sentence relies on. The exceptions are CF-01 and CF-02.

The citation principle applied throughout: where a row states the clause it is attached to, the citation passes; where the sweep cut a restatement and put the row's id in its place at that position, the citation is doing the work criterion 7 of the sweep asks for and passes; where the surviving clause is an obligation the cited row does not state, it fails. On that last test [R0534, R0535, R0536] at line 41 passes — the clause it carries ("the delta's class decides whether those two run in one session or two") is stated word for word by R0492, cited alongside, and R0535 is what "the class" resolves to. So does [R1137, R1138] at line 48: R1138's "propose a deep read at milestone moments without being asked" is the row standing in for the sentence the sweep cut two paragraphs down.

## Verdict (loss): changes-required

See CF-03. The rest of the diff's cuts are covered. Checked and found carried: the two separations, by R0462's single body ("an artifact you produced or a document you drafted"), so dropping R0463 loses nothing; the interface-contract clause of the red gate, by R0478's "fail on bad logic — not merely on an absent import"; the no-implementation and no-per-change-stage-against-an-open-spec pair, by R1468's closing sentence; the tests' acceptance being recorded in the close's artifact, by R1126's last bullet; findings routing through the decision session, by R0474's second bullet; Depth 1 at the close and Depth 2 on reach, by R1104 and R1105, which is where the old text's "This changes R1104 and R1136" paragraph landed. "Nothing decomposes from an open spec" left this document but is process/decomposition.md step 2 at the same ref, so it is not lost from the corpus.

## Verdict (residue): ready

Every sentence is an act, an order, a condition, a form, or an explanation an agent needs to act. The delta definition in the opening paragraph is the recognition condition for everything below it and stays. The four-kinds table is a form. No persuasion, self-record, or human-reader organization survives: "The principle", "Record", "What this document changes or retires", and "What this document does not decide" are all gone.

## Verdict (keys): ready

Nine roles, each performing an act: architect-agent (the architecture summary from the TRD), chief-of-staff (calling a deep read on the human's behalf), coder-agent (implement to green), context-quality-reviewer (named in the table's rules row), release-manager-agent (the release package), reviewer-agent and skeptic-risk-agent (named in the table's code row and carrying the quality and skepticism passes), spec-reviewer-agent (reads the branch's whole diff), test-designer-agent (starts on the entry read). Copy-editor, critic, and writer were dropped and the document has no act for them; corpus is `[software]` alone, so that is right.

## Verdict (loadable): ready-with-findings

See CF-04. No heading lost its content, the four-kinds table refers to no column it does not have, and "the one read above" at the per-change stages resolves to the section above it.

## CF-01 — blocking
Claim: `[R0008]` is attached to a sentence licensing early closure, which R0008 does not state; the obligation R0008 does state was cut from that position.
Location: process/change-flow.md:13-14 — "Close a delta early at will; the tranche boundary is a deadline, not a target [R0008]."
Evidence: Read by inspection, not run. R0008's body at the base ref is "Bound every spec delta to its tranche; a delta never spans two." The baseline at 7549f7e stated the two claims separately and attributed them separately: "A delta is bounded by its tranche and never spans two (R0008). It may be closed early, at will; frequent small closes are the norm and the tranche boundary is a deadline, not a target (DEC-000170)." The sweep merged the pair, kept the DEC-000170 half, and moved R0008's id onto it.
Consequence: An agent resolving R0008 to check whether it may close a delta early finds a rule about tranche spanning and no licence. The licence to close early — a real permission, relied on by the spec lifecycle below — is now ungoverned prose that reads as governed, so intake will not pick it up as a candidate row.
Fix: Restore the clause R0008 states ("a delta is bounded by its tranche and never spans two [R0008]") and leave the early-close licence uncited, or open an intake candidate for it. Either way, no id sits on a clause its row does not state.
Related: CF-02

## CF-02 — blocking
Claim: `[R0012, R0013]` is attached to the two-tranche cap, which neither row states; the claiming rule those rows do state was cut from that position.
Location: process/change-flow.md:63 — "At most two tranches run at once [R0012, R0013]."
Evidence: Read by inspection, plus a search of all 456 files under rules/ at the base ref for any row stating a cap on concurrent tranches — `grep -il 'two tranche\|concurrent' rules/*.md` returns R0003 ("A tranche is one concurrent workstream of build work"), R0013, and R0199 (an unrelated execution-session stop rule). None states a cap. R0012 is "A spec document is claimed when it appears in an open delta's diff"; R0013 is "A document claimed by one open delta is not claimed by a second; keep concurrent deltas over disjoint spec territory." The baseline stated cap and claiming rule as separate clauses and cited the rows on the claiming clause: "At most two tranches execute concurrently, over disjoint spec territory; a document appearing in one open delta's diff may not appear in a second (R0012, R0013)."
Consequence: The number two is now the only limit stated and it appears to be carried by two rows that carry a different limit — disjointness, which admits three tranches over disjoint territory and forbids two over one document. An agent planning concurrency reads a governed cap that does not exist, and the disjointness rule, which is the one with a row behind it, dropped out of this document's prose. process/decomposition.md:22 states the cap the same way but places its citation correctly, on the claim-check clause.
Fix: Restore the disjointness clause under `[R0012, R0013]` and leave "at most two tranches run at once" uncited, listing it as an intake candidate so the cap either gets a row or is dropped.
Related: CF-01

## CF-03 — blocking
Claim: The "Dimensions are an open set" paragraph was cut whole; it carried the rule for how a review acquires a new dimension and the condition deciding which dimensions a given read runs, and neither is in the new text nor stated by any cited row.
Location: process/change-flow.md — absent; baseline process/change-flow.md @ 7549f7e, the paragraph beginning "**Dimensions are an open set.**"
Evidence: Read against the diff. The cut sentences: "A new one — a reliability review, a security review, whatever the next year shows is missing — is added by intake, not by editing this document: its rules land as rows keyed on the dimension ... with the other keys naming the delta kinds it applies to, and a read includes every dimension that has a row matching the delta." and "until it lands the intake session names the dimensions in force." None of the 38 cited ids covers either; R0487 and R0488 state the quality and skepticism passes only. The sweep report is not committed, so whether these are among its six intake candidates could not be checked.
Consequence: The surviving three-bullet list reads as closed. A reader running the one read has no instruction to include a dimension carried by a row but absent from this document, and a session proposing a fourth dimension has no route — the paragraph's whole point was that the route is intake, not an edit to this file.
Fix: Restore the operative clause in one sentence — a read includes every dimension with a row matching the delta, and a new dimension enters by intake rather than by editing this document — or confirm it is one of the sweep's six intake candidates and record that in the sign-off.

## CF-04 — non-blocking
Claim: "the second trigger" refers to an enumeration of triggers that the sweep cut, leaving the ordinal with no first member.
Location: process/change-flow.md:42 — "The **size call** is the second trigger for two"
Evidence: Read against the diff. The baseline enumerated them: "on either of two triggers. First, the delta touches the commit-and-change-control policy's consequential class (R0534–R0547) ... Second, the **size call** ..." The new text replaces the first trigger with the clause "the delta's class decides whether those two run in one session or two" and keeps the ordinal.
Consequence: A reader must infer that the preceding clause was the first trigger. Recoverable, but the ordinal is now a residue of a list that is not there.
Fix: "The **size call** is the other trigger for two", or restore "the delta's class is one trigger" before it.
