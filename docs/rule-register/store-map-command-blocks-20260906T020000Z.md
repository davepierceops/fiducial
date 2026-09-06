# Store map — topic `command-blocks`

Source file: `skills/command-blocks.md` @ fd54448. Register rows R1193–R1235 (43 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1193 | skills/command-blocks.md | retired-DEC-000380 (C004: the file's session scope becomes the `session` key) | — |
| R1194 | skills/command-blocks.md | retired-ruling (ruling 1: core R0208 defines command block and execution block; no distinct obligation here) | — |
| R1195 | skills/command-blocks.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R1196 | skills/command-blocks.md | written | R1196 |
| R1197 | skills/command-blocks.md | merged into R1196 | R1196 |
| R1198 | skills/command-blocks.md | written | R1198 |
| R1199 | skills/command-blocks.md | written | R1199 |
| R1200 | skills/command-blocks.md | written | R1200 |
| R1201 | skills/command-blocks.md | written | R1201 |
| R1202 | skills/command-blocks.md | written | R1202 |
| R1203 | skills/command-blocks.md | merged into R1202 | R1202 |
| R1204 | skills/command-blocks.md | written | R1204 |
| R1205 | skills/command-blocks.md | written | R1205 |
| R1206 | skills/command-blocks.md | written | R1206 |
| R1207 | skills/command-blocks.md | merged into R1206 | R1206 |
| R1208 | skills/command-blocks.md | written | R1208 |
| R1209 | skills/command-blocks.md | merged into R1208 | R1208 |
| R1210 | skills/command-blocks.md | written | R1210 |
| R1211 | skills/command-blocks.md | retired-ruling (store-fix-1 item 5: negation) | — |
| R1212 | skills/command-blocks.md | written | R1212 |
| R1213 | skills/command-blocks.md | written | R1213 |
| R1214 | skills/command-blocks.md | merged into R1213 | R1213 |
| R1215 | skills/command-blocks.md | written | R1215 |
| R1216 | skills/command-blocks.md | written | R1216 |
| R1217 | skills/command-blocks.md | written | R1217 |
| R1218 | skills/command-blocks.md | written | R1218 |
| R1219 | skills/command-blocks.md | written | R1219 |
| R1220 | skills/command-blocks.md | written | R1220 |
| R1221 | skills/command-blocks.md | written | R1221 |
| R1222 | skills/command-blocks.md | written | R1222 |
| R1223 | skills/command-blocks.md | merged into R1221 | R1221 |
| R1224 | skills/command-blocks.md | written | R1224 |
| R1225 | skills/command-blocks.md | merged into R1224 | R1224 |
| R1226 | skills/command-blocks.md | written | R1226 |
| R1227 | skills/command-blocks.md | merged into R1196 | R1196 |
| R1228 | skills/command-blocks.md | written | R1228 |
| R1229 | skills/command-blocks.md | merged into R1199 | R1199 |
| R1230 | skills/command-blocks.md | merged into R1208 | R1208 |
| R1231 | skills/command-blocks.md | merged into R1215 | R1215 |
| R1232 | skills/command-blocks.md | merged into R1202 | R1202 |
| R1233 | skills/command-blocks.md | merged into R1206 | R1206 |
| R1234 | skills/command-blocks.md | merged into R1218 | R1218 |
| R1235 | skills/command-blocks.md | merged into R1220 | R1220 |

Counts: rows consumed 43; rows written 26; definitions 4 (R1195, R1200, R1204, R1217); merged away 15; split 0; retired 2 (R1193 DEC-000380 / C004; R1194 ruling 1).

Notes.

- C046 (Dave's ruling, 2026-09-05) is written as three rows, consecutive orders 210–230, taking the three lowest available ids from the cluster in row order: R1220 (the expected-output line exists), R1221 (that line is observed in the target environment or qualitative; R1223 merged in), R1222 (blast radius above a destructive block). R1235, the conformance-criteria restatement of all three, merges into R1220.
- C085 and C055 are cross-file clusters; under ruling 1 nothing from LEXICON.md, docs/global-context/core.md, or skills/directive-authoring.md appears in these bodies. R1194's whole content is core R0208's definition, so it is not restated here. C085's two intra-file rows (R1202, R1232) merge here; R1232's exit-status half is the obligation already carried by R1205, which stands as its own row because naming the remote and checking the sync's exit status are independent obligations (ruling 10).
- The eleven conformance criteria (lines 102–124) restate the prose rules as a checklist; each restatement merges into the prose row it restates (ruling 2), except R1226 and R1228, whose obligations appear nowhere else in the file and are written. The criterion at lines 112–113 (no ``` fence, nested blocks fenced `~~~`) carries no register id and consumed none.

Amended by `docs/cycles/store-fix-1-20260906T040000Z.md`. Item 4 retired R1195 as a scope statement about the rule set. Item 5 retired R1211 as the negation of R1212. Item 7's tool-owned test retired nothing here: `bin/directive` emits no command block in any template region, and `bin/check-directive`'s M1-M8 test none — read from the generator's general-mode output and from `bin/aimeta/elements.py` at a184967. The fence rules (R1212), the expected-output rules (R1220-R1222) and the blast-radius rule survive as the authoring craft the tools cannot do.
