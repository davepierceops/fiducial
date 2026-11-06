# CLAUDE.md definition review — human rulings

Baseline: cb0194aee512f48f3046e5ba9be445d85f97fbd3, after PR #424. Dave requested a one-by-one review of the 18 definitions currently emitted into CLAUDE.md. Collect rulings on intake/claude-definition-pruning; installed context remains unchanged until the reviewed batch is finalized.

- R0108 (test/tests/testing/verification): Dave answered “yes” to retiring this definition without replacement. R0110 already requires verification claims to remain within what the checks establish; the explanatory test-versus-verification distinction does not earn its place. R0110 is unchanged. At batch finalization, archive the original R0108 with the actual retirement decision ID allocated at merge; do not invent a successor or preallocate a decision ID. Verify removal from roots, agents, skills and standalone bundles, preserving other specialized definitions and procedures unless separately approved.

No other definition retirement or generator-selection change is approved yet. The observed generator behavior—term matching in non-emitted enforced rows and transitive definition pulling—is review evidence, not authorization to change it. R0535 is next for discussion.

These are human wording/scope rulings, not an independent intake review or a claim of landing. Formal decision-log entries are allocated at merge under the decision-log procedure.
