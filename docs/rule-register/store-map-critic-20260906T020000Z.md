# Store map — topic `critic`

Source file: `roles/critic.md` @ fd54448. Register rows R1000–R1029 (30 rows).
Directive: docs/cycles/store-all-topics-20260906T020000Z.md.

| register id | source file | disposition | store id |
|---|---|---|---|
| R1000 | roles/critic.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R1001 | roles/critic.md | written | R1001 |
| R1002 | roles/critic.md | written | R1002 |
| R1003 | roles/critic.md | retired-ruling (store-fix-1 item 4: describes) | — |
| R1004 | roles/critic.md | written | R1004 |
| R1005 | roles/critic.md | written | R1005 |
| R1006 | roles/critic.md | written | R1006 |
| R1007 | roles/critic.md | written | R1007 |
| R1008 | roles/critic.md | written | R1008 |
| R1009 | roles/critic.md | written | R1009 |
| R1010 | roles/critic.md | written | R1010 |
| R1011 | roles/critic.md | written | R1011 |
| R1012 | roles/critic.md | written | R1012 |
| R1013 | roles/critic.md | written | R1013 |
| R1014 | roles/critic.md| merged into R1013 (fix 3 item 2) | R1013 |
| R1015 | roles/critic.md | written | R1015 |
| R1016 | roles/critic.md | written | R1016 |
| R1017 | roles/critic.md | written | R1017 |
| R1018 | roles/critic.md | written | R1018 |
| R1019 | roles/critic.md | written | R1019 |
| R1020 | roles/critic.md | written | R1020 |
| R1021 | roles/critic.md | written | R1021 |
| R1022 | roles/critic.md | written | R1022 |
| R1023 | roles/critic.md | written | R1023 |
| R1024 | roles/critic.md | written | R1024 |
| R1025 | roles/critic.md | merged into R1009 | R1009 |
| R1026 | roles/critic.md | written | R1026 |
| R1027 | roles/critic.md | written | R1027 |
| R1028 | roles/critic.md | written | R1028 |
| R1029 | roles/critic.md | written | R1029 |

Counts: rows consumed 30; rows written 29; definitions 3; merged away 1 (R1025 into R1009, cluster C035 — the file's only intra-file pairing); split 0; retired 0.

Store fix pass 2 item 7 strips `role`, `session` and `corpus` from 1 define row (R1010), which now carry `term` and nothing else — the bundle tool pulls them by scanning selected bodies for their terms.

Store fix pass 2 item 8 re-keys R1029, the run-at-tier row, to `role: [chief-of-staff]`: it binds whoever summons the session, not the role that runs in it. The topic's other two checks — a short-form or runs-as-a-session define — find nothing here that store fix pass 1 item 4 did not already retire.

Store fix pass 3 item 2 merges R1014 into R1013: both are checks of the AI-smell pass, run together on that one trigger.
