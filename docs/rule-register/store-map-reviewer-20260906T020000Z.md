# Store map — topic `reviewer`

Source file: `roles/reviewer-agent.md` @ fd54448. Register rows R1046–R1056 (11 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1046 | roles/reviewer-agent.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R1047 | roles/reviewer-agent.md | written | R1047 |
| R1048 | roles/reviewer-agent.md | written | R1048 |
| R1049 | roles/reviewer-agent.md| merged into R1048 (fix 3 item 2) | R1048 |
| R1050 | roles/reviewer-agent.md| merged into R1048 (fix 3 item 2) | R1048 |
| R1051 | roles/reviewer-agent.md| merged into R1048 (fix 3 item 2) | R1048 |
| R1052 | roles/reviewer-agent.md| merged into R1048 (fix 3 item 2) | R1048 |
| R1053 | roles/reviewer-agent.md| merged into R1048 (fix 3 item 2) | R1048 |
| R1054 | roles/reviewer-agent.md | written | R1054 |
| R1055 | roles/reviewer-agent.md | written | R1055 |
| R1056 | roles/reviewer-agent.md | written | R1056 |

Counts: rows consumed 11; rows written 11; definitions 1 (R1046); merged away 0; split 0; retired 0.

Every row of this topic carries a `## Human` line recording that it is in force
until an adopted, published code-review standard replaces it, per
process/change-flow.md's Quality bullet: the standard enters the store through
intake as rows whose `source` names that external document, and the intake
commit that lands it retires these rows. No `retired:` key is written here —
the directive fixes the frontmatter to ten keys.

Store fix pass 3 item 2 merges R1049-R1053 into R1048: the six checks share one trigger — the review pass over a change — and R1047 already requires them in one pass over the whole of it.
