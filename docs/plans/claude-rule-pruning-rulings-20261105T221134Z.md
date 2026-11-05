# CLAUDE.md rule review — human rulings

Baseline: fb310dd9c1ea56e4fa2e1b9b671a50c128fdec0f, after PR #423. Dave requested a one-by-one review of remaining CLAUDE.md rules. This records actual rulings; further rules have not been decided. Collect approved source edits on intake/claude-rule-pruning, then independently review and regenerate derived context together before landing. Installed context is unchanged during this collection.

- R0164: Dave answered “y” to keeping the secrets principle as written. No source change.
- R0203: Dave answered “yes” to replacing only the principle with: “Act against deployed or production systems only when a policy in your bundle authorizes the action and names its gate.” The deny patterns, selectors and Human note remain unchanged. This shortens the existing restriction without changing the DEC-001220 enforcement arrangement.

- R0166: Dave answered “yes” to removing only “Propose; do not decide.” Retain: “Approval, release, prioritization, and publication are the human's.” The removed blanket instruction conflicted with the routine implementation decisions R0458 permits.

These are the human's wording/scope rulings, not an independent intake review or a claim that this new batch has landed. Decision-log entries are allocated at merge under the decision-log procedure.
