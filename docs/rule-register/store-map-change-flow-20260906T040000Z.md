# Store map — topic `change-flow`

Source file: `operating-model.md` @ fd54448, by way of topic `operating-model` as the store-all pass wrote it.
Directive: docs/cycles/store-fix-1-20260906T040000Z.md, item 6b.

The topic is new with this pass. Every row is `corpus: [software]` and is keyed to the role that performs the
stage. No register id is consumed here that `store-map-operating-model-20260906T020000Z.md` does not already
account for; this map records the landing, not a second consumption.

| store id | order | role | stage |
|---|---|---|---|
| R0464 | 10 | chief-of-staff, writer, copy-editor, critic | define: the seven primary controls |
| R0465 | 250 | — (define rows carry no role key) | define: a meaningful change |
| R0466 | 20 | chief-of-staff | the lighter shape for a trivial or routine change |
| R0467 | 30 | chief-of-staff | each stage completes before the next begins |
| R0470 | 40 | chief-of-staff | define: the per-change stages |
| R0471 | 50 | chief-of-staff | no per-change stage and no implementation against an open spec |
| R0472 | 60 | spec-reviewer-agent | the spec read as a hard gate |
| R0473 | 70 | context-quality-reviewer | the gate on methodology and governed context |
| R0474 | 80 | chief-of-staff | spec edits land ungated on an open branch, gated at its close |
| R0477 | 90 | chief-of-staff | findings route both ways through the decision session |
| R0478 | 100 | test-designer-agent | confirm red while the branch is open |
| R0479 | 110 | chief-of-staff | the test suite is directed under a convergence directive |
| R0480 | 120 | spec-reviewer-agent | the close's read, from the branch point |
| R0481 | 130 | chief-of-staff | the close's diff to Dave; one ruling agrees it |
| R0482 | 140 | chief-of-staff | acceptance criteria before the unit starts |
| R0483 | 150 | architect-agent | the architecture summary from the TRD |
| R0484 | 160 | test-designer-agent | the unit's tests confirmed red |
| R0485 | 170 | coder-agent | implement to green |
| R0486 | 180 | coder-agent, test-designer-agent | implementation and tests by different agents |
| R0487 | 190 | reviewer-agent | the quality pass |
| R0488 | 200 | skeptic-risk-agent | the skeptic pass |
| R0489 | 210 | release-manager-agent | the release package |
| R0490 | 220 | chief-of-staff | the release gate is Dave's |
| R0492 | 230 | chief-of-staff | quality and skepticism are separate passes |
| R0493 | 240 | chief-of-staff, coder-agent, release-manager-agent | define: mechanical checks |

Counts: rows written 24; definitions 3 (R0464, R0470, R0493); retired 0.

Two rows are keyed against item 6b's own role list, and say so in their `## Human`: R0483 to `architect-agent`,
because it plainly binds the role that derives the architecture summary; R0493 to `coder-agent` and
`release-manager-agent` as well as `chief-of-staff`, because its term `mechanical check` is used by R0485 and by
the definition-of-done row R0509.

R0465 is added by `docs/cycles/store-fix-2-20260906T050000Z.md` item 1, which restores it; store fix pass 2 item 7 strips `role`, `session` and `corpus` from every define row, so it carries `term` and nothing else.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 3 define rows (R0464, R0470, R0493), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 4 item 3 brings in R0090, R0091 and R0094 from the dissolved `spec-and-change-discipline`, orders
260–280, corpus narrowed to `[software]`: propose a spec edit rather than making it; edit specs and nothing else
under a spec-editing directive; pin the spec branch's SHA in a directive issued while its delta is open. Item 9's
sweep retires R0480 as a duplicate of `convergence`'s R1481, which also names the role that gated the spec, and
gives R0481 the "nothing else closes it" clause from `convergence`'s R1486a, which retires into it. R0017/R0471
and R0091/R1156 are kept as pairs: running no per-change stage against an open spec is wider than implementing
nothing against one, and the C097 mirror rows are deliberately two. Topic count: 25 rows before, 27 after.

Store fix pass 5 item 1d keeps R0493 in this topic as the `mechanical check` define and restates its body to the
directive's words: "Mechanical checks are lint, type, and static-analysis checks; they pass as part of green."
No disposition changes.
