# Store map — topic `decision-layer`

Source file: `docs/global-context/decision-layer.md` @ fd54448. Register rows R0223–R0262 (40 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0223 | docs/global-context/decision-layer.md | retired-ruling (container rule 4: load order) | — |
| R0224 | docs/global-context/decision-layer.md | retired-ruling (container rule 4: who receives the file) | — |
| R0225 | docs/global-context/decision-layer.md | written | R0225 |
| R0226 | docs/global-context/decision-layer.md | written | R0226 |
| R0227 | docs/global-context/decision-layer.md | written | R0227 |
| R0228 | docs/global-context/decision-layer.md | written | R0228 |
| R0229 | docs/global-context/decision-layer.md | written | R0229 |
| R0230 | docs/global-context/decision-layer.md | written | R0230 |
| R0231 | docs/global-context/decision-layer.md | merged into R0230 | R0230 |
| R0232 | docs/global-context/decision-layer.md | merged into R0230 | R0230 |
| R0233 | docs/global-context/decision-layer.md | merged into R0230 | R0230 |
| R0234 | docs/global-context/decision-layer.md | written | R0234 |
| R0235 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0236 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0237 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0238 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0239 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0240 | docs/global-context/decision-layer.md | merged into R0234 | R0234 |
| R0241 | docs/global-context/decision-layer.md | written | R0241 |
| R0242 | docs/global-context/decision-layer.md | merged into R0241 | R0241 |
| R0243 | docs/global-context/decision-layer.md | merged into R0241 | R0241 |
| R0244 | docs/global-context/decision-layer.md | written | R0244 |
| R0245 | docs/global-context/decision-layer.md | written | R0245 |
| R0246 | docs/global-context/decision-layer.md | written | R0246 |
| R0247 | docs/global-context/decision-layer.md | written | R0247 |
| R0248 | docs/global-context/decision-layer.md | split into R0248a, R0248b | R0248a, R0248b |
| R0249 | docs/global-context/decision-layer.md | written | R0249 |
| R0250 | docs/global-context/decision-layer.md | retired-ruling (conversation-retro owns the use-when row) | — |
| R0251 | docs/global-context/decision-layer.md | retired-ruling (conversation-retro owns the retro's content rules) | — |
| R0252 | docs/global-context/decision-layer.md | written | R0252 |
| R0253 | docs/global-context/decision-layer.md | merged into R0252 | R0252 |
| R0254 | docs/global-context/decision-layer.md | merged into R0252 | R0252 |
| R0255 | docs/global-context/decision-layer.md | merged into R0252 | R0252 |
| R0256 | docs/global-context/decision-layer.md | written (restored by store-fix-1 item 1) | R0256 |
| R0257 | docs/global-context/decision-layer.md| merged into R0256 (fix 3 item 2) | R0256 |
| R0258 | docs/global-context/decision-layer.md | retired-ruling (directive-invariants owns it) | — |
| R0259 | docs/global-context/decision-layer.md | written | R0259 |
| R0260 | docs/global-context/decision-layer.md | merged into R0259 | R0259 |
| R0261 | docs/global-context/decision-layer.md | merged into R0259 | R0259 |
| R0262 | docs/global-context/decision-layer.md | written | R0262 |

Counts: rows consumed 40; rows written 20; definitions 1; merged away 16; split 1 (R0248 → R0248a, R0248b); retired 5 (R0223, R0224, R0250, R0251, R0258).

Amended by `docs/cycles/store-fix-1-20260906T040000Z.md` item 1: R0256 and R0257 restored; R0259 and R0262 renumbered to orders 190 and 200 to seat them.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 1 define row (R0247), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 3 item 2 merges R0257 into R0256: both fire on one trigger — a directive is written — and constrain the same act.

Store fix pass 4 item 3 brings in R0100 at order 210, keyed to the four decision roles: the loose-end tracker's
five checkpoints as one checklist row, merging R0101–R0105 from the dissolved `spec-and-change-discipline`.
Item 9's sweep emitted no pair between this topic and `core`: the operating-model rows store fix pass 1 merged
into core have no surviving decision-layer twin. Topic count: 19 rows before, 20 after.

Store fix pass 5 item 3 gives R0252's body the named told states from `chief-of-staff`'s R0933, which retires
into it: any execution session left running, any worktree held, and whether the connector is released. The text
is the directive's, verbatim.
