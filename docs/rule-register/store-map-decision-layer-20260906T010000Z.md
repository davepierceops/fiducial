# Store map — topic `decision-layer`

Derived artifact. One line per register id whose `file` column is
`docs/global-context/decision-layer.md`.

Inputs, at the revisions the directive names:

- `docs/global-context/decision-layer.md` @ fd5444870b40d4fd93cc63d833d6d40358246fba — the source text, 38 lines
- `docs/rule-register/rule-register-20260904T210000Z.md` @ 45b02c7b88a0e08f4872713aa39f840a59117423 — the 40 rows
- `docs/rule-register/rule-clusters-20260904T223000Z.md` @ acdfef73fc04bed73d6f854b3f66fe8df5411519 — C062, C063, C109, C110
- `docs/rule-register/topic-digest-20260905T181500Z.md` @ 0bd149ce85f8519e2e9d681d3827b74bef237f43 — card 16
- `decisions/log.md` @ d81c41a6ab60288764d8a3898cd66b354b3c664b — DEC-000380, DEC-000400

| register id | disposition | store id |
|---|---|---|
| R0223 | retired — container rule (load after Core) | — |
| R0224 | retired — container rule (never given to an execution session) | — |
| R0225 | written | R0225 |
| R0226 | written | R0226 |
| R0227 | written | R0227 |
| R0228 | written | R0228 |
| R0229 | written | R0229 |
| R0230 | written | R0230 |
| R0231 | written | R0231 |
| R0232 | written | R0232 |
| R0233 | written | R0233 |
| R0234 | written | R0234 |
| R0235 | written | R0235 |
| R0236 | written | R0236 |
| R0237 | written | R0237 |
| R0238 | written | R0238 |
| R0239 | written | R0239 |
| R0240 | written | R0240 |
| R0241 | written | R0241 |
| R0242 | written | R0242 |
| R0243 | written | R0243 |
| R0244 | written | R0244 |
| R0245 | written | R0245 |
| R0246 | written | R0246 |
| R0247 | written | R0247 |
| R0248 | split into R0248a, R0248b | R0248a, R0248b |
| R0249 | written | R0249 |
| R0250 | written | R0250 |
| R0251 | written | R0251 |
| R0252 | written | R0252 |
| R0253 | merged into R0252 | R0252 |
| R0254 | written | R0254 |
| R0255 | written | R0255 |
| R0256 | written | R0256 |
| R0257 | written | R0257 |
| R0258 | written | R0258 |
| R0259 | written | R0259 |
| R0260 | written | R0260 |
| R0261 | written | R0261 |
| R0262 | written | R0262 |

Rows consumed: 40.
Store rows written: 38.
Definitions among them: 4 — R0231 (landmine), R0233 (cannot-execute is Core's stop), R0243 (loose-end tracker), R0247 (the document under review).
Rows retired: 2 — R0223 and R0224, both container rules under ruling 3.

## Arithmetic

40 register rows, less 2 retired, less 1 merged away (R0253 into R0252), plus 1
added by the one split (R0248 into R0248a and R0248b) = 38 row files.

The digest's card 16 also reaches 38, by a different route: it retires nothing
and collapses cluster C062 (R0236, R0237, R0239) to one distinct rule. Under the
merge rulings in force, C062 does not collapse — R0236 and R0237 carry different
conditions, and R0239 sits on a different source line — so all three are written,
and the two retirements, the one merge and the one split account for the
difference.

## Cross-file cluster-mates, not merged here

Each is written by its own topic's run; this run writes `decision-layer` only.

| cluster | decision-layer row | cluster-mates |
|---|---|---|
| C062 (intra-file) | R0236, R0237, R0239 | — |
| C063 | R0250 | R0305 (engagements/sre-critic.md:10), R1240 (skills/conversation-retro.md:24) |
| C109 | R0235 | R0932 (roles/chief-of-staff.md:155) |
| C110 | R0260 | R0999 (roles/copy-editor.md:116) |
