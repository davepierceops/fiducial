# Store map — topic `coder-agent`

Source file: `roles/coder-agent.md` @ fd54448. Register rows R0938–R0943 (6 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R0938 | roles/coder-agent.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R0939 | roles/coder-agent.md | written | R0939 |
| R0940 | roles/coder-agent.md | written | R0940 |
| R0941 | roles/coder-agent.md | written | R0941 |
| R0942 | roles/coder-agent.md | written | R0942 |
| R0943 | roles/coder-agent.md | written | R0943 |

Counts: rows consumed 6; rows written 6; definitions 1 (R0938); merged away 0; split 0; retired 0.

Store fix pass 4 item 3 brings in R0106 at order 70, keyed `[coder-agent, test-designer-agent]`: a write path
maintains the entity's derived fields as every other write path does, and the package is not done until they are
enumerated and each is checked. R0107 merges into it. Topic count: 5 rows before, 6 after.
