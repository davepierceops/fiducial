# Review: process/spec-test-suite.md — process-sweep-read-20260907T060000Z

Verdict: ready
Reviewed: process/spec-test-suite.md @ fd6888ca2472e4d020f913fc4b0463e0a617efc4
Baseline: process/spec-test-suite.md @ 7549f7efed0ed961536bf61620d621ebe6fbb81b
Reviewer: frontier read, fresh session, did not draft the swept text
Date: 2026-09-07
Scope: the five questions the directive names, over all 26 lines, with all eight bracketed ids — R0474, R0481, R1101, R1153, R1155, R1158, R1468, R1476 — resolved to their files under rules/ at the base ref, and each of the five steps compared against the baseline's six.
Cross-checked: docs/cycles/process-sweep-20260907T040000Z.md; process/change-flow.md at the same ref, whose spec-lifecycle step 1 cites the same R1101/R1468/R0478/R1158 cluster; process/decomposition.md step 2, which names this document's act as the one thing admitted against an open spec.
Not inspected: any spec branch or test suite. The sweep session's report is not committed on this branch, so the LOSS test's "listed in the sweep report's six intake candidates" limb could not be applied; on this document it made no difference, since nothing was found cut.
Findings: none
The human should inspect: nothing. This is the one clean document of the ten.

## Verdict (citations): ready

All eight resolve, and every one sits on a clause its row states.

`[R1468, R1158]` on the opening sentence: R1468 gives the tests-and-nothing-else act against an open spec branch and the red gate run while open so its result is the close's evidence; R1158 gives the handing of that result to the close. Both limbs of the sentence are covered.

`[R1101]` on step 1: "Read a spec at exactly two points: the entry read, when the branch opens and before the Test Designer starts, and the close" — the ordering the step turns on. `[R0474]` on steps 2 and 3: its third bullet directs the spec's test suite under a directive derived from the open spec and not under a change package, which is what both steps state, and its fourth bullet pins the SHA in any directive issued while the delta is open, which is step 2's second clause. `[R1153]` on step 4: "while its branch is open it takes tests and nothing else" carries both the decomposes-nothing and the admits-no-implementation limbs. `[R1155, R1476]` on step 5: R1155 files a spec finding through the decision session, R1476 routes it there and has it triaged there. `[R0481]` on step 5's tail: the close is one ruling by the human on the reviewed diff, recorded in the decision log naming the SHA — which is exactly the clause it annotates.

No sentence restates a cited row's body in place of citing it.

## Verdict (loss): ready

Every obligation, condition, and step survives or is cited. The six baseline steps become five without dropping anything: step 3's "pin the spec's revision at handoff" merged into step 2, where R0474's fourth bullet covers it. The wait-for-the-entry-read condition keeps all three of its parts — the entry read has run, whatever its verdict, and the human has said to proceed. The derive-from-the-spec-not-a-decomposition-doc rule, the tests-are-the-spec's-suite statement, the not-under-any-change-package clause, the keep-it-to-tests rule, and the triage-in-the-decision-session rule are all present.

Four cut passages were checked and are covered. "There is no decomposition yet; there cannot be one, because the spec is open" is the reason for step 2 and goes under criterion 2. "The Test Designer's work here belongs to the directive, not to a package" restates step 4's own sentence. "Findings return here, not to the execution session that raised them" is R1476, cited. And the one that mattered most to check — "the Test Designer does not edit the spec, and this directive does not authorize an edit to it" — is R1153's "while its branch is open it takes tests and nothing else", cited at step 4. The two remaining "What this does not decide" items are step 5's tail and step 4 respectively, both promoted into the sequence as instructions.

## Verdict (residue): ready

Every sentence is an act, an order, or a condition. "Status of this draft", "The principle" and its bolded thesis, the because-clause explaining why this act does not wait, and the three-item "What this does not decide" section are gone; what those items carried is in the steps. "Everything else in the decomposition procedure waits on the spec closing agreed" survives from the baseline and is the condition that makes this procedure's exception legible, so it stays under criterion 2.

## Verdict (keys): ready

`[chief-of-staff]`, unchanged, with `session: [decision]`. Every act the document orders — direct the directive, derive it, state what the tests are, keep the directive to tests, triage the findings — is the Chief of Staff's in a decision session. The Test Designer is the recipient of the directive and the filer of findings; the acts it performs are governed by R1468, R1153, and R1155 rather than by this document, which directs the session that directs it. No act in the document names a performer absent from the list.

## Verdict (loadable): ready

The sweep removed both headings and kept every step, so nothing points at a heading that is gone. The intro states the scope and the exception, the five steps run in order, and the document reads whole as a bundle member. It names process/decomposition.md's procedure without a path; that document is in the same bundle at the same ref and names this one in return, so the pair resolves in either direction.
