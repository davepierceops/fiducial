# CLAUDE.md rule review — human rulings

Baseline: fb310dd9c1ea56e4fa2e1b9b671a50c128fdec0f, after PR #423. Dave requested a one-by-one review of remaining CLAUDE.md rules. This records actual rulings; further rules have not been decided. Collect approved source edits on intake/claude-rule-pruning, then independently review and regenerate derived context together before landing. Installed context is unchanged during this collection.

- R0164: Dave answered “y” to keeping the secrets principle as written. No source change.
- R0203: Dave answered “yes” to replacing only the principle with: “Act against deployed or production systems only when a policy in your bundle authorizes the action and names its gate.” The deny patterns, selectors and Human note remain unchanged. This shortens the existing restriction without changing the DEC-001220 enforcement arrangement.

- R0166: Dave answered “yes” to removing only “Propose; do not decide.” Retain: “Approval, release, prioritization, and publication are the human's.” The removed blanket instruction conflicted with the routine implementation decisions R0458 permits.

- R0168: Dave answered “y” to retiring the rule entirely, with no replacement and no move to a skill. The previously proposed rewrite is rejected. Generic scope advice does not earn standing context; R0458 already covers escalation and routine implementation decisions. At batch finalization, archive the unchanged original under rules/retired/ with the actual retirement decision ID allocated at merge (AC-RS-10); do not invent a successor or preallocate a decision ID.

- R0170: Dave answered “y” to keeping the durable-records rule as written. No source change. Its session-end requirement covers persistent work beyond the specific decision-log and tracker records.

- R0172: Dave answered “yes” to keeping “Support every claim with inspectable evidence.” unchanged. No source change; inspectable support is distinct from labeling a claim.

- R0174: Dave rejected retirement and said the observed/inferred/told/unknown labels are useful and should stay. Preserve the labeling obligation. He requested a semantic overlap survey of R0021, R0172, R0174 and related rows to consider consolidation; no consolidated wording or additional retirement is approved. The prior R0172 keep ruling remains in force while its possible consolidation is discussed.

- R0186: Dave answered “agreed” to preserving finding classification in the review skill and retiring R0186 from standing context after that move. The complete original sentence (including demonstration and location) is preserved in process/review-artifact.md, with a Classification field distinct from severity and a requirement to cite authorization for accepted risk. The existing row remains live until batch finalization assigns the retirement decision ID. This agreement concerns the R0186 move; the latest two consolidated claim/verification rows remain proposals awaiting an explicit ruling.

- Claim/evidence consolidation: Dave answered “y” to adopting the two final proposed rows. This replaces the earlier separate R0172 keep wording and R0174 keep-as-a-row proposal while preserving the provenance labels. R0172 now carries the approved claims/basis wording; R0110 carries the approved verification/limits wording, with the union of the replaced rows' role/session/corpus scopes. The thirteen overlapping live rows are archived to these successors: R0174, R0179 and R0455 → R0172; R0021, R0177, R0111, R0783, R0461, R0161, R0181, R0182, R0190 and R0192 → R0110. R0186's separately approved skill move and retirement remain as recorded above. Specialized role rows and definitions are unchanged. This removes the standing requirement to assign exactly one of the six evidence classes; it does not rewrite specialized procedures that still use those terms.

Approved R0172 wording:

> Label every claim observed, inferred, told, or unknown, and provide inspectable support. Make assumptions and uncertainty explicit; say what could not be determined rather than guess.

Approved R0110 wording:

> Support verification claims with the checks performed. Identify relevant simulations and untested assumptions, state what remains unverified, and claim only what the evidence establishes. Claims about state, results, or completeness require checking the underlying source or result.

- R0180: Dave answered “y” to retiring “Read governed text before emitting anything it governs.” without replacement. The rule is general and vague; specific spec, decision-log and Voice reading obligations remain. Preserve the original in rules/retired/ at batch finalization, using the actual retirement decision ID allocated at merge.

- R0183: Dave answered “y” to replacing the conflicting-sources rule with: “When sources conflict, name them and the disagreement; ask the human to resolve it before relying on either.” All selectors remain unchanged.

- R0191, R0730 and R0725: Dave answered “yes” to retiring all three retry/readback procedure rows without replacement, hook or skill. The historical contention detector and prescribed retry procedure no longer earn standing context; the consolidated evidence rule remains the requirement for claims of success. Preserve the original rows in rules/retired/ at batch finalization with the retirement decision ID allocated at merge. This approves removing the instructions; it does not claim universal connector idempotency or change existing hooks.

- R0193: Dave answered “yes” to replacing the consistency rule with: “When a fact changes, update its current references and report any you cannot update. Preserve historical records.” All selectors remain unchanged.

- R0196: Dave approved dropping the blanket filename convention after explicitly confirming that the Chief of Staff would lose its general filename rule. No shortened global replacement. Keep prescribed review, retro and adoption artifact naming in their skills/tooling; arbitrary generated files no longer acquire a Fiducial-wide timestamp requirement. The review skill now states its timestamp format directly. During batch finalization, remove the blanket prose from roots and agent outputs while preserving the existing generated-filename hook for reviews/retros; do not silently lose its registration by retiring the hook-bearing row. This ruling changes the broad naming policy, not the specific artifact conventions or existing enforcement scope.

- R0207: Dave answered “y” to retiring the artifact-terminology rule without replacement. Specific artifact names remain in their skills; the blanket ban on generic words is removed. Preserve the original row under rules/retired/ at batch finalization with the actual retirement decision ID allocated at merge.

- R0457: Dave answered “y” to retiring the documentation-update row into revised R0193, which covers current references to changed facts. The original row is archived unchanged except for retired: R0193.

- R0462: Dave answered “y” to: “Required reviews must be performed by a reviewer who did not author the work.” The verb and condition metadata now match the required-review obligation; role/session/corpus scopes are unchanged. The Human note clarifies that self-checking does not replace independent review. Approval authority remains governed by R0166.

- R0460: Dave answered “agreed” to retiring this separate prohibition into R0110 and adding the positive obligation: “Keep verification aligned with approved requirements, and justify changes to checks against those requirements.” The sentence is prepended to the approved consolidated verification wording. The original R0460 is archived with retired: R0110. This preserves verification against requirements while allowing justified corrections to checks. Dave also stated a preference for eliminating “never”/“don’t” rules; assess the useful positive obligation rather than preserving a prohibition by default.

- R0458/R0166: Dave answered “yes” to combining escalation and authority in R0166: “Use existing guidance for routine implementation decisions. Bring unresolved requirements, material review disagreements, and product or risk tradeoffs to the human. Approval, release, prioritization, and publication remain the human's.” This supersedes the shorter R0166 wording approved earlier in this review. The original R0458 is archived with retired: R0166; scopes are unchanged.

- R0763: Dave answered “yes” to moving the source-of-truth instruction out of standing context into the intake skill. Its exact body is now in process/intake.md. Adoption continues to follow DEC-001630; no duplicate rule text is added there. Archive R0763 at batch finalization with the actual retirement decision ID; ensure the body does not reappear in root or agent output. The installed harness files remain unchanged while the review batch is collected.

- R1616: Dave answered “y” to keeping the external-failure investigation rule unchanged. DEC-001430 records its concrete motivation: two incorrect mechanisms asserted from memory, each settled by a search or probe. No source change.

- R1626: Dave answered “y” to keeping the command-blocks skill trigger unchanged, including explicit delegation and the ordinary internal-tool-call exclusion. No source change.

- R1627: Dave explicitly approved: “Use verification-checklists for verification work, and require subagents doing that work to use it too.” Replace the previous long trigger with this exact wording. Detailed conditions and role-specific sections remain in the verification-checklists skill. At batch finalization, check any definition availability affected by removing the old trigger’s incidental term mentions; keep that detail out of the approved short trigger. No specialized verification rule or definition is retired by this wording change.

- R0880: Dave answered “yes” to retiring the startup instruction without replacement in standing context. Project status remains a separately requested skill. Its body now explicitly states the request/orientation trigger and that starting Chief of Staff alone is not a trigger, so this scope survives the generator’s first-sentence skill-description derivation. Archive the original R0880 at batch finalization with the retirement decision ID allocated at merge.

- R0889: Dave answered “y” to retiring exclusive connector ownership without replacement. Remove the standing requirement to inspect other chats and stop writes merely because another decision session is active. This retires the shared-connector assumption; it does not assert that genuinely conflicting writes are safe. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge.

- R1138: Dave answered “yes” to moving milestone deep-read guidance into change-flow. The exact sentence is added with its Chief of Staff/decision-session scope, and the process no longer cites R1138 as a live dependency. Archive the original standing row at batch finalization with the actual retirement decision ID; verify it does not reappear in generated root or agent bodies.

- R0931: Dave answered “y” to retiring the automatic next-work-item handoff suggestion without replacement. A handoff may still be proposed when a concrete need arises; the rule requiring a suggestion at every major work item is removed. Archive the original at batch finalization with the actual retirement decision ID allocated at merge.

- R0937: Dave answered “yes” to retiring the expensive-context session-ending recommendation without replacement. Concrete context or performance issues may still be raised when they occur; no automatic session-ending nudge remains. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge.

- R1611: Dave answered “y” to retiring the full-spec-and-approval-log reading rule without replacement or a move to a skill. The build skill retains its existing spec-read step and R1513 approval requirement; its active R1611 citation is removed. The historical provenance citation remains. The proposed shorter R1611 wording is not adopted. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge; ensure its body disappears from generated roots and agents.

- R1606: Dave answered “yes” to retiring the plan/subagent tree-fact instruction without replacement or a move to a skill. The consolidated evidence rule already requires checking underlying sources; a separate requirement for the executor to derive repository details does not earn standing context. Remove its active citation from process/intake.md; R1607 remains pending its own review. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge, and ensure its body does not reappear in generated roots or agents.

- R1607: Dave answered “yes” to retiring the tree-resolvable-precondition rule without replacement or a move to a skill. Revised R0166 covers routine decisions and escalation; R0172 covers evidence. The blanket stop instruction is broader than needed because sources beyond the repository may resolve a question. Remove its active citation and the now-empty tree-derived-fields sentence from process/intake.md. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge, and ensure its body does not reappear in generated roots or agents. Preserve the historical R0188 retirement reference.

- R0999: Dave answered “yes” to retiring the solid-tier model instruction without replacement. Its Copy Editor qualification appears only in the Human note, leaving the generated instruction ambiguous; model selection belongs at agent configuration or launch. This ruling does not change agent configuration or select a replacement model. No active process citations were found. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge, and ensure its body does not reappear in generated roots or agents.

- R1029: Dave answered “yes” to retiring the Critic frontier-tier instruction without replacement or a move to a skill. Model selection belongs at agent configuration or launch rather than in standing context. This ruling does not change agent configuration or select a replacement model. No active process citations were found. Archive the original row at batch finalization with the actual retirement decision ID allocated at merge, and ensure its body does not reappear in generated roots or agents.

These are the human's wording/scope rulings, not an independent intake review or a claim that this new batch has landed. Decision-log entries are allocated at merge under the decision-log procedure.
