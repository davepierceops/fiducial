# Review: process/prd-template.md — process-sweep-read-20260907T060000Z

Verdict: ready-with-findings
Reviewed: process/prd-template.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/prd-template.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 56 lines, with both bracketed ids — R1513, R1533 — resolved to their files under rules/ at the base ref, and each of the eight template sections compared field by field against the baseline.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; process/trd-template.md at the same ref, which was swept the same way and shares the nine NFR dimensions; decisions/log.md @ a00deba DEC-000490.
Not inspected: any project PRD written against this template. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied.
Findings: 1 — 0 blocking, 1 non-blocking
The human should inspect: nothing that changes the document's substance. The one finding is a role key, shared with the TRD template.

## Verdict (citations): ready

Both resolve, and both sit on clauses that rely on them. `[R1513]` carries the sentence the sweep cut from the baseline's second paragraph — "It owns product intent, it is the human's document, and it is not in force until the human agrees it" — which is R1513's body almost word for word, so the id stands in its place at the position it was cut from. `[R1533]` supports the clause it annotates in the opening line ("the source acceptance criteria derive from") and appears a second time in §6 carrying its other limb — that per-unit criteria may live in the PRD or in the unit's own artifact and derive from the PRD either way — which is again R1533's body exactly. No id sits on a clause its row does not state.

## Verdict (loss): ready

Every obligation and required-content item survives. §3 keeps all four journey fields — actor, trigger, the sequence of actions and system responses, expected outcome. §4 keeps the concrete-outcomes-not-feature-lists form for functional goals, all nine non-functional dimensions, the `N/A` answer, the non-goals, and the rule that a dimension-specific exclusion is a note inside that dimension rather than a non-goal; only the worked example goes. §5 keeps the metric or signal, the baseline-where-known, all three observing mechanisms, and the distinction from acceptance criteria, compressed to "Acceptance criteria gate correctness; this does not." §6 keeps the written-conditions definition and the concrete-enough-to-derive-tests-from constraint. §7 and §8 keep their content. The nine per-dimension definitions collapse into the dimension names alone, which is the same compression the TRD template took and is the sweep's eighth criterion applied. "Copy this into a project PRD" is carried by the "## Skeleton" heading and the block; the `status`/`last-reviewed` note is the document's record of what retired under DEC-000380 and goes correctly under criterion 4. One attribution thins rather than disappears: the baseline said acceptance criteria "are the source the Test Designer derives test cases from" and the new text says "concrete enough to derive test cases from", dropping the Test Designer — who is governed by R0478 and R1468 elsewhere, so the obligation is not lost.

## Verdict (residue): ready

Every sentence is a form or a content requirement on a section of it. "What this is", the canonicity and spec-spine framing, and "Read in a decision session drafting a PRD" are all gone, the last carried by the `session:` key.

## Verdict (keys): ready-with-findings

See PT-01.

## Verdict (loadable): ready

The eight numbered items match the skeleton block's eight headings exactly, in order and by title, and §4's three sub-headings — Functional goals, Non-functional goals, Non-goals — match the three parts §4's prose names, in the same order. Nothing refers to a heading that was cut.

## PT-01 — non-blocking
Claim: Neither role in the list performs an act the document describes, since the sweep cut the sentence that gave both of them one.
Location: process/prd-template.md:3 — `role: [chief-of-staff, spec-reviewer-agent]`
Evidence: Read by inspection against the diff. The role list is unchanged from the baseline. In the baseline both acts were in the opening line — "Read in a decision session drafting a PRD and in an execution session gating one" — the drafting half being the Chief of Staff's and the gating half the Spec Reviewer's. The sweep cut that line, correctly, since `session: [decision, execution]` carries the same information. The new text names no role anywhere in its body and describes no act performed by a named party; it is a form and a list of content requirements throughout. Unlike process/trd-template.md, which at least names the Architect, this document names nobody.
Consequence: Under the sweep's ninth criterion the list should name the roles that perform an act the document describes, and neither can be checked against the text. The key is defensible on the ground that a template is selected into the bundle of whoever drafts or gates against it, but that ground is not stated in the document, so the human cannot confirm the list from the document he is signing off.
Fix: Accept the key on the drafts-or-gates-against-this-form ground and record that reasoning in the sign-off, or restore one clause naming the two acts. The same choice applies to process/trd-template.md's `spec-reviewer-agent`; both should be settled the same way.
Related: TT-02 in reviews/trd-template-read-20260907T060000Z.md
