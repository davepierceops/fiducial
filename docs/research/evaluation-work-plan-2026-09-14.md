# Fiducial evaluation: working decisions and plans

This is a local discussion draft. Accepted work will be transferred to GitHub Issues; proposed approaches below are not yet decisions or commitments.

## Required final deliverable

Explicitly confirmed by the user: finish this walkthrough with a concrete set of GitHub-ready issues and milestones. Milestones group related issues around a meaningful outcome. Each accepted piece of work needs an actionable issue, and milestone assignments must be explicit. The final grouping remains to be discussed; evaluation sections A–F are traceability labels, not automatically milestone names.

For each issue, prepare a title, problem/evidence, intended outcome, scoped work, acceptance criteria, dependencies where applicable, and proposed milestone. For each milestone, prepare a title, outcome/description, and included issues. Do not invent deadlines or treat unaccepted suggestions as commitments.

GitHub Issues and Milestones will be the canonical ongoing task/status record. The README should link to live milestone and issue views rather than maintain a duplicated checklist of outstanding tasks. This local document is a staging record for the discussion and issue preparation, not the intended permanent backlog. Relevant user-facing limitations can still be explained briefly beside adoption instructions and linked to their issues.

## Agreed direction from the conversation

- Improve the README now, with an early status/known-limitations summary pointing to GitHub Issues as the canonical work tracker.
- Discuss the evaluation and develop granular plans before choosing the work to undertake.

## A. Writing adoption and author customization

Disposition: accepted outcome; implementation details under discussion.

Observed problem: released writing bundles embed Dave's voice and publication preferences while the README describes drafting in the adopter's voice. The voice template is not part of the advertised starting path. Adding a second voice file alone leaves conflicting author-specific instructions in the bundle.

Agreed outcome: an adopter can use the writing roles through downloaded files and chat, without cloning or editing the repository, with their own voice and publication preferences shared consistently across the three roles. Dave can continue using his existing configuration.

Agreed additional requirement: when an adopter has not supplied an author profile, the agent prompts for writing samples and creates an initial profile from them.

Agreed fallback: if the author has no writing samples available, the agent helps create a provisional profile through a short conversation.

Agreed review behavior: reviewing a newly generated profile is recommended, not required. Present the opportunity to review, but if the author declines and says to proceed, use the initial profile and begin the requested work without another approval prompt. Skipping review does not mean the author approved every inferred preference; the profile remains provisional and editable.

Agreed refinement behavior: learn from the author's edits without interrupting the writing. Apply explicit preferences immediately. Collect inferred patterns as suggested profile updates for an optional review at the end; do not silently promote those patterns into standing preferences.

Proposed details for profile setup (not yet agreed): request two or three representative pieces the user identifies as their own desired voice; distinguish observed writing patterns from inferred preferences; ask about audience, goals, and publication/disclosure preferences that samples do not establish; return the profile as a reusable file for all three roles. Scope the setup so it runs once per author profile rather than independently in every writing role.

Proposed implementation packages (derived from the agreed behavior; not yet filed as GitHub Issues):

1. Inventory author-specific content across the writer, copy-editor, and critic bundles, including rules and selected process documents. Distinguish personal preferences from shared role behavior.
2. Define the shared author-profile format and precedence rules. Separate author identity, audience, voice, mechanics, and publication preferences from shared role obligations. Specify how partial profiles work and how tentative inferences are represented. Preserve the ability to draft from conversation without an outline.
3. Update the source and bundle assembly so the public bundles and chosen profile form one consistent instruction set. Preserve Dave's configuration through an explicitly documented path.
4. Implement first-use profile setup: use a supplied profile; otherwise request samples and draft one, with a short conversational fallback when samples are unavailable. Recommend review, honor a request to skip it, and return a reusable profile. Make the profile/template available through the supported download path and document the setup steps.
5. Implement refinement: apply explicit author preferences immediately; collect edit-derived patterns without interrupting the task; offer inferred profile changes for optional review at the end. Preserve which preferences were explicit and which remain tentative.
6. Check all three generated roles for leaked personal defaults, missing profile instructions, and unresolved dependencies. Exercise supplied-profile, samples, no-samples, skipped-review, and refinement paths with a deliberately different author profile. Verify reuse across separate writer/editor/critic sessions. Distinguish mechanical checks from observed LLM behavior.

Candidate acceptance criteria, pending discussion:

- A new adopter can follow the documented setup with the advertised files and capabilities.
- All three writing roles use the same selected author's preferences.
- Public default instructions do not impose Dave's identity, audience, site, or disclosure wording.
- Missing profile information triggers the agreed fallback behavior.
- Starting without a profile prompts for writing samples and offers an initial profile derived from them.
- An author without samples can create a provisional profile through a short conversation.
- Declining profile review and asking to proceed begins the requested work without another approval prompt; inferred preferences are not recorded as explicitly approved.
- An explicit preference is applied immediately; patterns inferred from edits are collected for optional end-of-task review without interrupting writing or silently becoming standing rules.
- Dave's own writing configuration remains available and coherent.
- The writer can draft from conversation when no outline exists; the README states this consistently.

## B. Rule references and bundle completeness

Disposition: selective IDs and editorial citation review agreed; detailed implementation proposed below.

Two distinct observed problems: generated process text retains citations while the renderer omits rule IDs; some referenced rule bodies are absent from the selected role altogether. For example, change-flow names the definition of done in R0509, but the chief-of-staff bundle does not include that row.

Agreed design: authors/reviewers decide which citations express a necessary instructional dependency and which serve only provenance. Agent-facing text retains the former. The bundler mechanically labels the targets of retained references and rejects missing targets. Unreferenced rules remain unlabelled. The agent consuming the bundle does not decide which references matter.

Author's rationale, recorded during discussion: removing row IDs was intentional to minimize context tokens, including the repeated cost across role bundles. The selective-ID decision preserves this goal while allowing IDs that support necessary references.

Agreed editorial approach: retain an ID only for a rule referenced elsewhere in the same bundle; omit labels for unreferenced rules. Assess missing references for whether that role needs the instruction, include necessary canonical content once, and remove references that serve only source provenance from agent-facing output. Do not automatically pull every other role's obligations into a bundle.

Proposed implementation packages:

1. Inventory citations in active rules and process documents, recording the citing instruction, target, and affected named bundles. Classify each as necessary instruction, provenance-only, or inappropriate for the role. Record unresolved editorial choices rather than guessing.
2. Revise the corpus: remove provenance-only references from delivered text while retaining source provenance; make role-specific process text sufficient; fix selection for necessary targets without importing unrelated role obligations or hand-maintaining copies of their text.
3. Define and implement reference parsing and selective labelling. Cover single references, grouped references, and existing suffixed IDs such as R1395b. Specify handling of examples/code blocks and references inside pulled definitions. Determine labels from the final included content, and render each needed target label once.
4. Validate before writing: a retained reference whose target is absent causes a clear refusal naming the source and missing target; no partial bundle is published. Apply the check to every named release bundle through the shared generation path.
5. Verify with fixtures for referenced/unreferenced rules, grouped and suffixed references, missing targets, and references introduced by definitions. Audit all twelve real bundles and measure the actual size change. Check a sample bundle read for intelligibility separately from mechanical validity.

Acceptance criteria derived from the agreement:

- Every retained instructional reference resolves to included content carrying the referenced ID.
- An unreferenced rule receives no ID label.
- Provenance-only references are absent from agent-facing output and remain recoverable in the source/history.
- The same canonical rule is not duplicated to satisfy multiple references.
- Missing targets fail generation with an actionable diagnostic and no partial output.
- Necessary cross-role context is selected deliberately; blanket dependency expansion is not the fix.

Remaining implementation detail: settle the reference grammar and how role-specific process text/selection supplies required content. These details do not reopen the agreed editorial/mechanical division.

Size probe over the reviewed corpus, adding compact `[R####] ` labels: chief-of-staff gains 1,884 characters when every included rule/definition is labelled, versus 249 when only the 31 already-included citation targets are labelled. Coder gains 1,184 versus 80; writer 1,225 versus 8. These are character counts, not token counts, and exclude content needed to resolve currently missing instructions. Results: `label-size-comparison.json`. Tokenization and actual agent comprehension have not been measured.

## C. Adoption prerequisites and setup delivery

Disposition: chief-of-staff ownership and setup flow agreed; implementation details proposed below.

Observed problem: process/project-setup.md has no role selector and therefore appears in none of the standard named bundles. The README states only part of its prerequisites.

Agreed behavior:

- Include the setup procedure in the chief-of-staff bundle and explain the prerequisites in the software quick start.
- The chief of staff guides a new software user through establishing or verifying default-branch protection and the runner-level force-push prohibition before directing repository writes.
- Planning and discussion may proceed while setup is incomplete.
- Where verification is unavailable, state what cannot be checked and give specific instructions for the user to check it.

Proposed implementation packages:

1. Reconcile the setup process, relevant rules, and README into one consistent set of requirements. Distinguish repository protection from agent-runner configuration and distinguish those controls from correctness/release evidence.
2. Select project-setup for the chief-of-staff bundle and check its dependencies under B's reference contract. Keep administration instructions out of roles that do not need them.
3. Define the onboarding sequence: identify the target repository and runner; inspect available configuration; report requirements as verified, user-reported, unmet, or unknown; help resolve unmet requirements before directing repository writes. Do not treat inaccessible configuration as proof of either presence or absence.
4. Supply concise, specific manual verification guidance where the session cannot inspect configuration. Keep host-specific steps separate from portable requirements; verify any documented runner recipe against its actual capability.
5. Document the setup path and test complete, incomplete, and uninspectable setups. Check that planning proceeds, unmet prerequisites prevent directed repository writes, and user-reported checks are accurately described.

Acceptance criteria derived from the agreement:

- The generated chief-of-staff bundle includes sufficient setup instructions and resolves retained references.
- The quick start names both repository-level and runner-level prerequisites.
- The chief of staff guides setup before directing repository writes and permits planning while setup is incomplete.
- Unverifiable configuration is reported explicitly with actionable manual checks.

Open implementation question: define what verification evidence can be reused and what must be refreshed when the repository, runner, or permissions change, without unnecessary repeated onboarding.

## D. Obsolete active entry points

Disposition: retain thin pointer adapters and retire obsolete manifest/state documents agreed; implementation details proposed below.

Observed problem: MANIFEST.md and COLLAB-STATE.md present obsolete guidance/state, and .claude/agents adapters point at removed source paths. Historical artifacts should remain distinguishable from current entry points.

Agreed adapter design: retain harness-specific entry files such as CLAUDE.md and AGENTS.md as thin pointers telling the agent where to read the substantive instructions. The adapters do not maintain copies of the rules. The user's intent is portable canonical bundles with harness-specific discovery pointers, not removal of adapters.

Agreed retirement: move MANIFEST.md and COLLAB-STATE.md into clearly labelled history because they describe the superseded arrangement. Preserve the historical record and stop presenting them as current entry points.

Proposed implementation packages:

1. Inventory existing and intended adapter entry points. Specify where each is installed and which locally available role bundle it points to; avoid assuming every harness recognizes the same filename.
2. Replace references to removed roles/, context-sets/, and policies/ files with pointers to the supported bundle location. Keep adapter content to locating and reading that bundle; leave durable behavior in the canonical rules and generated bundle.
3. Document how the adopting project installs or generates the pointer and pins its bundle release. Make missing-bundle behavior explicit so an unresolved pointer cannot silently be treated as loaded context.
4. Verify each supported adapter's target exists and run a small adoption check to establish that the intended harness actually reads the bundle. Separate path checks from observed harness behavior.
5. Retire MANIFEST.md and COLLAB-STATE.md into clearly labelled history. Update active references to those files as needed, preserve historical references as historical evidence, and sweep remaining supported entry points for stale guidance.

Candidate acceptance criteria:

- Each supported adapter points to the intended bundle and contains no duplicated policy corpus.
- An adopter can install the adapter and referenced bundle using the documented workflow.
- No supported entry point requires a removed source path.
- Missing bundle content is reported rather than treated as successfully loaded.
- MANIFEST.md and COLLAB-STATE.md no longer present obsolete guidance as current; their historical content remains available.

## E. Definitions and instruction consistency

Disposition: next material for discussion; no approach agreed.

Split into three independently actionable candidates:

1. Definition selection: wording can name a concept without matching its registered term, so necessary definitions can be omitted. The writing claim tiers and R0038 are the concrete example. Coordinate with B: proposed explicit references for essential definitions, resolved and selectively labelled under the agreed citation contract; incidental term matching can remain supplementary, subject to review.
2. Definition content: define the evidence requirements for the four writing claim tiers and reconcile repeated glossary labels without losing distinct meanings. This needs editorial decisions as well as selection fixes.
3. Release authority: agreed — routine releases have standing human authorization once the required checks and reviews pass; consequential releases require explicit human approval. Human authority does not imply a fresh approval prompt for every routine release.

Proposed release-authority implementation plan:

- Inventory active statements about release authority, routine/consequential classification, and approval in rules, process documents, and the README. Preserve the distinction between merge, deployment, and exposure.
- Reconcile R0490 and the consequential-change definition with the agreed distinction. Update other active statements that impose an unconditional per-release approval gate. Keep the existing consequential-change classification unless a separate decision changes it.
- Describe standing authorization and explicit approval consistently in the chief-of-staff and release-manager bundles. Passing checks alone does not turn a consequential release into a routine one.
- Check scenarios: routine change with required evidence may proceed without another approval; routine change missing required evidence does not qualify; consequential exposure waits for explicit approval even when checks pass; a merge that does not expose functionality is not automatically the release event.
- Review the generated role bundles for contradictory approval instructions after the edits.

Release-authority acceptance criteria: all active instructions agree on the two authorization paths; routine releases do not solicit redundant approval; consequential releases do not proceed without explicit approval; required checks/reviews remain prerequisites.

User-proposed alternative: treat every dependency in a rule/row as a potential defect to examine. Look for shorter, self-contained wording that removes the need to refer elsewhere. The concern is the overall weight of the methodology, not only missing definitions.

Revised proposed sequencing: review dependencies and simplify the corpus before introducing additional definition-dependency machinery. The agreed B contract still governs references retained after editorial review; the explicit-definition-dependency proposal is not accepted.

Proposed simplification audit:

1. Inventory explicit ID citations and implicit dependencies (named documents, criteria, gates, defined terms, and assumptions about other instructions), distinguishing active rules from process descriptions and historical evidence.
2. For each candidate, ask whether the dependency is incidental provenance, unnecessary indirection, an artifact of splitting one obligation across rows, duplicated guidance, or a necessary shared contract.
3. Propose shorter self-contained wording, consolidation, retirement of redundant text, or retention of a justified dependency. A dependency is an audit trigger, not an automatic defect verdict.
4. Compare original and proposed obligations: trigger, actor, required behavior, scope, exceptions, authority, and evidence requirements. Identify any semantic change for a human decision rather than disguising it as shortening.
5. Compare complete generated bundles, including definitions pulled or no longer needed and any repetition introduced. Optimize total delivered context and comprehensibility, not just individual row length or source-file count.
6. Start with a representative batch and present original/proposed wording, dependency removed or retained, semantic differences, and measured size change before expanding the method across the corpus. Include examples where shared definitions should remain to expose the tradeoff.

Potential failure of indiscriminate self-containment: copying the same substantial definition into multiple instructions can enlarge bundles and create divergent copies. Preserve necessary shared contracts when they are clearer and smaller as shared content; avoid shortening by deleting meaningful conditions or replacing precise requirements with vague language.

## F1. Reject empty rule bodies

Disposition: fix agreed.

Observed problem: FileRowSource accepts a rule whose instruction body is empty, contrary to the non-empty-body acceptance criterion. No shipped rule was empty in the reviewed corpus.

Implementation plan:

1. Validate the agent-facing rule body after frontmatter parsing and separation of the Human rationale. Reject an empty or whitespace-only instruction body with a RowShapeError identifying the file/rule. Human rationale alone is not an instruction body.
2. Add regression cases for empty, whitespace-only, and rationale-only bodies, plus a valid body with rationale. Check the CLI reports the invalid row clearly and writes no bundle.
3. Run the relevant storage/CLI tests and validate the current corpus still loads. Keep this fix scoped to rule bodies; do not silently impose a new requirement on process-document forms.

Acceptance criteria: empty instruction bodies fail with a locatable diagnostic; human-only content does not satisfy the requirement; valid rules remain accepted; bundle generation fails without publishing a partial output.

## F2. Local bundle previews

Disposition: ordinary local generation and input-scoped release checks agreed. A separate preview mode is unnecessary for the agreed behavior.

Observed constraint: normal bundle generation requires a successful origin/main fetch, HEAD equal to origin/main, and no uncommitted rule/process changes. This prevents normal CLI inspection of proposed local edits before landing them.

Agreed generation behavior: normal bundle generation renders local files as they stand, including uncommitted edits, without fetching or requiring synchronization with origin/main. It works offline and on feature branches, retaining input validation. This provides the accepted preview capability without a separate mode.

Agreed release behavior: unrelated uncommitted files must not block generation of release bundles. Cleanliness checks apply only to files directly used in generating the release assets. Uncommitted changes to actual generation inputs block release generation; unrelated work does not.

Proposed implementation plan:

1. Separate rendering local content from checks appropriate to publishing a release. Remove the clean-tree refusal from ordinary bundle generation while retaining input validation, including missing-reference and empty-body checks.
2. Remove mandatory fetch and origin/main equality checks from ordinary rendering. Keep release-revision verification in the release path, separate from local generation.
3. Make provenance accurate for local edits: a HEAD SHA alone does not identify modified source contents. Choose a compact indication of local modifications and a content identity where useful; do not imply a modified bundle was generated solely from the named commit. Keep provenance overhead consistent with the token-minimization goal.
4. Replace bin/release's whole-tree dirty check with a check scoped to the actual generation inputs for the release assets. Derive that set from the generation path rather than assuming every file under rules/, process/, or the repository matters. Include selected rules, pulled definitions, applicable process documents, and query/order configuration actually used. README.md is also an input when attached as a release asset. Specify the treatment of executable generator code so modified code cannot silently produce assets attributed solely to a committed revision.
5. Account for added/deleted/re-keyed inputs: an input-set change that alters selection or output must not escape the check merely because a formerly selected file is absent from the new selection. Compare the effective inputs/output against the release revision as needed.
6. Test modified tracked rules, new local rules, local deletions, clean input, and malformed input for ordinary generation. For release, test unrelated uncommitted files (allowed), modifications to selected content/definitions/query configuration (blocked), and additions/deletions/re-keying affecting output (blocked). Verify offline ordinary generation and accurate provenance.

Acceptance criteria: normal generation accepts valid local edits without remote synchronization; local output does not misrepresent its source revision; malformed input still fails clearly; unrelated uncommitted files do not block release generation; uncommitted changes to effective release-generation inputs do block it; release assets retain accurate revision provenance.

## F3. Reconcile skipped tests with current decisions

Disposition: issue accepted. Proposed milestone: Reliable bundle generation (grouping tentative pending final review).

Problem: seven tests were skipped in the evaluation run; some cite decisions or governance conditions whose current disposition needs checking.

Scope: inspect each skip against the current specifications and decision records; enable applicable tests, remove obsolete cases with a recorded reason, and link genuinely deferred cases to outstanding issues. Do not treat every skipped test as an implementation defect.

Acceptance criteria: every remaining skip has a current explicit justification and a linked issue where work is deferred; resolved questions no longer cause unnecessary skips; the resulting suite passes.

## F4. Add automated pull-request checks

Disposition: issue accepted. Proposed milestone: Reliable bundle generation (grouping tentative pending final review).

Scope: add a GitHub Actions workflow that runs the test suite and validates all standard named bundles on pull requests. Include empty-body and reference validation as those checks become available. Choose output locations that do not publish releases or modify the repository.

Acceptance criteria: failing tests or invalid standard bundles produce a failing check; valid changes pass; validation covers the proposed pull-request revision rather than requiring it to equal origin/main; no release is created by these checks.

Dependencies: F1 empty-body validation, B reference validation, and F2 removal of the ordinary-generation main/sync restriction for complete intended coverage. The workflow can be introduced before all checks land, with dependencies made explicit.

## E2. Revisit and reduce the entire glossary

Disposition: user proposes a full glossary review instead of a narrow duplicate-definition issue. Detailed disposition of individual definitions remains open.

Proposed milestone placement: Leaner, self-contained bundles (tentative).

Problem: generated glossaries repeat labels such as mock-verified and reconciliation through distinct definition rows. Repeated labels may reflect complementary explanations or conflicting meanings; they are not automatically redundant.

User's retention criterion: define a word or phrase only when Fiducial uses it in a specific, important way that cannot be inferred from surrounding context or general language. Directive, command block, and baton are examples of likely legitimate definitions. The user suspects many entries may be unnecessary; no numerical reduction target or specific removals have been agreed.

Measured inventory at reviewed revision 8ea66f527cf0114441b34976b09a8326fccbf3c2: 78 definition rows, 72 distinct primary labels (aliases excluded from that label count), 2,294 words of definition bodies, 78 nonblank body lines because each body is a single paragraph. Assembling all entries in current glossary format produces 157 Markdown lines including heading and blank separators. Their source files total 882 lines including metadata and spacing. Actual selected glossaries: chief-of-staff 57 entries/115 lines/1,953 words; writer 47/95/1,519; coder 52/105/1,657. Bundle word counts include rendered labels and heading.

Revised proposed scope: review every definition against the user's retention criterion. Retain necessary specialized meanings; retire ordinary-language explanations and redundant entries; shorten or consolidate where meaning is preserved; distinguish behavioral obligations from definitions and ensure needed obligations remain in appropriate rules. Review both term aliases and transitive selection for unnecessary glossary inclusion. Update retained references and preserve retired rows in history. Duplicate cleanup is part of this issue, not a separate competing rewrite. Coordinate with the broader dependency/shortening pass.

Proposed acceptance criteria: every retained definition has an explicit reason under the retention criterion; ordinary-language entries are retired unless a necessary specialized meaning is demonstrated; required behavioral obligations survive in the appropriate instructions; repeated glossary labels are resolved or justified; history is preserved; final bundles have no broken retained references; before/after definition counts and complete bundle sizes are recorded. A 50% reduction is a hypothesis to test, not an acceptance threshold.

## Remaining material to triage

- E: definition selection, glossary duplication, and release-authority ambiguity (separate candidate issues).
- README and public status presentation.
- Annotated software and writing examples.
- Evaluation of agent outcomes and method overhead.
- Scope of personal preferences and host-specific instructions beyond writing.
- Migration of existing actionable backlog entries into GitHub Issues.
