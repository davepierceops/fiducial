# Store map — topic `intake` (was `context-quality-criteria`)

Source file: `docs/global-context/review-rubric.md` @ fd54448. Register rows R0263–R0285 (23 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md. Topic renamed from `review-rubric` per the directive's TOPIC MAP.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0263 | docs/global-context/review-rubric.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0264 | docs/global-context/review-rubric.md | written | R0264 |
| R0265 | docs/global-context/review-rubric.md | written | R0265 |
| R0266 | docs/global-context/review-rubric.md | written | R0266 |
| R0267 | docs/global-context/review-rubric.md | written | R0267 |
| R0268 | docs/global-context/review-rubric.md | written | R0268 |
| R0269 | docs/global-context/review-rubric.md | written | R0269 |
| R0270 | docs/global-context/review-rubric.md | written | R0270 |
| R0271 | docs/global-context/review-rubric.md | written | R0271 |
| R0272 | docs/global-context/review-rubric.md | written | R0272 |
| R0273 | docs/global-context/review-rubric.md | written | R0273 |
| R0274 | docs/global-context/review-rubric.md | written | R0274 |
| R0275 | docs/global-context/review-rubric.md | written | R0275 |
| R0276 | docs/global-context/review-rubric.md | written | R0276 |
| R0277 | docs/global-context/review-rubric.md | retired-ruling (C019 settled by DEC-000290, owned by core R0196) | — |
| R0278 | docs/global-context/review-rubric.md | written | R0278 |
| R0279 | docs/global-context/review-rubric.md | written | R0279 |
| R0280 | docs/global-context/review-rubric.md | written | R0280 |
| R0281 | docs/global-context/review-rubric.md | written | R0281 |
| R0282 | docs/global-context/review-rubric.md | written | R0282 |
| R0283 | docs/global-context/review-rubric.md | written | R0283 |
| R0284 | docs/global-context/review-rubric.md | written | R0284 |
| R0285 | docs/global-context/review-rubric.md | written | R0285 |

Counts: rows consumed 23; rows written 22; definitions 5; merged away 0; split 0; retired 1 (R0277, C019 strictest form settled by DEC-000290 and carried by core R0196; this file's filename criterion states no obligation R0196 does not carry).

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 1 define row (R0267), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms; and re-verbs 4 `define` rows carrying a null term (R0265, R0271, R0280, R0282), each body restated as the instruction it carries.

Store fix pass 4 item 6 renames the topic to `intake` and rules it down to three rows, keyed
`role: [context-quality-reviewer]`, `session: [execution]`. R0264 becomes the intake checklist under the trigger
"At intake, test the proposed row against every criterion:", carrying the seven surviving criteria (R0265,
R0268, R0269, R0270, R0271, R0272, R0273, R0274, R0275, R0276, R0278, R0279, R0281, R0282, R0283, R0285) and the
nine criteria from Dave's rulings of 2026-09-05 — describes, one trigger, the negation test, the incident test,
form-is-a-process-document, merge-at-its-shortest, the Lexicon holds meanings, tool-owned rules, and the
checklist rule itself. R0266 (cite the criterion each finding fails) and R0284 (name what you cross-checked)
stay, binding the report. Retired `checklist`: R0265, R0268, R0269, R0270, R0271, R0272, R0273, R0274, R0275,
R0276, R0278, R0279, R0281, R0282, R0283, R0285. Retired `describes`: R0267 (the `criterion` define) and R0280
(retirement is Dave's — core's R0166 states it, and R0264's closing line carries it). R0266 still uses the word
"criterion" with no define row behind it; that is recorded, not resolved. Topic count: 21 rows before, 3 after.
