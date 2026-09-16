# Fiducial: evaluation for a first public introduction

Reviewed September 14, 2026. Repository revision: `8ea66f527cf0114441b34976b09a8326fccbf3c2`. Latest public release checked: `v2026.09.10`, built from `a460d69eab3d4362d358fbc44c9a3e293fc085aa`.

**My judgment:** Fiducial has a substantive idea, useful engineering discipline, and evidence of sustained use. Its public presentation undersells the interesting parts while overstating the ease and generality of adoption. A practiced AI practitioner could find a lot to respect here, but currently has to reconstruct the product from its working materials. The most consequential improvements involve the shipped bundles and the adoption path as well as the README.

This is an assessment of likely practitioner reactions, not a user study. I mapped the repository, inspected the rule-store implementation and generated all twelve role bundles through its selection/rendering functions, read the central software and writing workflows and substantial rule groups, examined the directive and landing implementations and their test design, ran the full test suite, and sampled specs, reviews, retrospectives, and decisions around the recent migration. I did not read every historical artifact line by line, execute an actual multi-session software project, test writing fidelity with an LLM, or exercise production credentials, deployment, or forge protection. The repository has 1,372 Markdown files; an exhaustive historical review would be a separate undertaking.

## 1. What I think this project actually is

Fiducial is an opinionated operating method for a human directing LLM work. It is distributed as role-specific Markdown instructions, assembled from a versioned store of individual rules. Its central concern is whether the human can distinguish a plausible result from an adequately supported result, across sessions and handoffs.

There are three useful layers:

| Layer | What is present | Why it matters |
|---|---|---|
| Working method | Roles, authority boundaries, spec/test coordination, evidence classes, review and release procedures; corresponding author/editor/critic procedures | Makes delegation and acceptance explicit |
| Context construction | Individual rules with keys, process documents, term-based definitions, named queries, generated release bundles | Gives instructions provenance and lets roles receive selected context |
| Supporting tools | Bundle/release generation, directive generation and linting, verified Git landing | Moves some repetitive and checkable work into executable code |

The human or host application supplies session creation, tool access, and execution. A bundle instructs a session how to behave; the repository does not supply an autonomous orchestration service that makes all twelve roles run when someone downloads a file.

That description belongs near the top of the README. “Rules for getting real work out of LLM agents” identifies a concern, but leaves the project's concrete form and working relationship unclear.

The connection between software and writing is more interesting than the opening makes it sound. In software, implementation should remain accountable to the agreed specification and evidence. In writing, prose should remain accountable to the author's intended claims and voice. In both, drafting and evaluation are separated, artifacts preserve intent across sessions, and the human retains the consequential judgments. Explain that shared purpose before asking the reader to accept the two paths as one product.

## 2. What a practiced practitioner is likely to appreciate

**The evidence discipline is specific enough to use.** The distinction between a test and the confidence claim drawn from it is excellent. Mock, contract, live, browser, and production evidence have declared boundaries. “A headless DOM is not browser rendering” and “Never claim live behavior from mocked evidence” describe recognizable failure modes. The confidence ledger connects a claim, its evidence, its remaining boundary, and the verification that could close the gap. These are stronger public examples than a list of job titles. See [verification rules](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/rules/R0145.md) and [the skeptic's evidence-chain pass](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/rules/R1073.md).

**Independent test authorship has real substance here.** The requirement that tests fail on wrong behavior, rather than a missing import, is concretely represented by intentionally incorrect stubs and test evidence. The spec/test convergence procedure gives the test designer a way to report an unstated contract instead of silently inventing it. The quality reviewer is separately responsible for adequacy. This is a thoughtful attempt to prevent the same agent from making the problem, implementation, and evidence agree by construction. It remains susceptible to shared assumptions across agents, which should be acknowledged when describing its benefits. See [red-gate stubs](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/bin/tests/stubs/README.md) and [spec test suite](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/process/spec-test-suite.md).

**The tools express the method instead of merely describing it.** `bin/land` separates Git operations from report construction, avoids shell interpolation, guards against orphaning local work, and reads remote state after a push. Its tests exercise real repositories and local bare remotes, with the provider-specific boundary explicitly described. Directive generation and linting share a reader for committed invariant text. The rule-store modules keep selection, term matching, and rendering separate from storage. These are credible implementation choices.

**The project records its own mistakes.** The reviews include an example of stale test arguments making checks vacuous, followed by corrective work. Retrospectives report unnecessary ceremony, bad handoffs, mistaken assumptions, and failed tool interactions. This gives the repository much more evidentiary value than a polished collection of ideal prompts. A selected, explained trail through these records could be a very persuasive demonstration. See [the bundle-tool skeptic review](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/reviews/bundle-tool-skeptic-20260906T150000Z.md). Its findings are historical; several were fixed and should not be presented as current defects.

**The writing workflow has tangible deliverables.** The copy editor is instructed to return tracked changes in the author's DOCX; the critic returns anchored comments while preserving the prose. The critic enumerates claims before consulting the author's list, reducing one source of anchoring. The current README hides these useful details behind “edits prose” and “reads a draft.”

## 3. Where that practitioner will hesitate

**The evidence for the method's effectiveness is mostly its own use.** The repository demonstrates implementation, reviews, and evolution. I did not find a repeatable comparative evaluation showing that loading these bundles reduces unsupported claims, improves completion, preserves voice, or lowers total human effort versus a simpler starting configuration. The 511-test suite measures software behavior, not the effect of the instructions on an LLM. The README's “a set of rules that fixes that” goes beyond the evidence I could verify. “Designed to make unsupported claims and unfinished work visible” would be credible.

**The workload imposed by the method is material.** Current generated bundles range from about 4,550 to 9,560 whitespace-delimited words. The chief-of-staff bundle has 178 selected rules, seven process documents, and 57 definition rows. The writer bundle has 106 selected rules, three process documents, and 47 definitions. These are word counts, not tokenizer measurements. Role selection is useful, but relevance and context cost still need attention: the writer receives Git-push instructions, release classification, decision-log obligations, and extensive software definitions. Whether a model reliably ignores those in a document-only session requires testing.

**Local operating preferences and general engineering principles are mixed together.** The core contains valuable evidence obligations alongside preferences about response shape, file naming, one-question-at-a-time interaction, session rotation, and copy controls. Some instructions encode a particular application's behavior, such as the categorical heredoc/copy-control statement in the command-block rules. Writing rules include Dave's audience and disclosure policy. A practitioner will want to know which choices are essential to the method, which are configurable preferences, and which depend on a host application's capabilities.

**The archive makes evolution visible but the current entry points are ambiguous.** There are 347 review files, 335 cycle files, and 46 retrospectives. Their volume alone proves neither quality nor waste. The rule-store PRD explicitly says the earlier document model led one policy through 22 review cycles, and the migration deliberately removed machinery. That is a good story of simplification. However, current root-level files and adapters still describe removed mechanisms. Preserve the records, but clearly distinguish active instructions from historical evidence.

**Operational guarantees need careful boundaries.** Branch protection helps preserve Git history and govern merges. It does not establish that a change is correct or that runtime tool use is safe. The README's “safe only because” sentence compresses too much into that one control. Similarly, downloading a Markdown file does not itself configure an agent runner, grant appropriate capabilities, or guarantee full-context loading. The README should name the required setup without predicting success across every harness.

## 4. Concrete findings to address

### A. Writing adoption currently contradicts the promise of “your voice”

The latest released writer bundle explicitly instructs the model to write in Dave's voice and includes `Process: Voice — Dave`. It also carries preferences about Dave's audience, repository citations, and LLM disclosure. The same personalization is present in the current source. The root [voice template](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/voice-template.md) says to replace the file before using a writing bundle, but the quick start never mentions it and the template is not a release asset.

This is more than missing explanation: merely uploading a separate voice document leaves the embedded Dave-specific rules in place. Provide a real customization path that removes or replaces all author-specific instructions and generates a consistent bundle. Until then, describe the writing bundles as Dave's configuration and point to the template as a starting aid, with its limits stated.

Also correct the role table's claim that the writer requires an agreed outline: [R1163](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/rules/R1163.md) allows drafting from the conversation when none exists, as the quick start already says.

### B. Generated bundles are not fully self-contained at their rule references

The renderer emits rule bodies without their IDs. Process documents retain citations such as `[R0509]`. A bundle reader cannot reliably map those references back to the right instruction even when the instruction is included.

There is a separate selection problem: some cited instructions are absent altogether. My audit found 15 distinct referenced rule IDs absent from the chief-of-staff bundle and 28 from the coder bundle. For example, the chief-of-staff bundle includes `process/change-flow.md`, which says completion depends on the definition of done in R0509; R0509 is selected only for the release manager and is absent from the chief-of-staff bundle. The generator pulls definitions by term, not obligations by citation.

Choose a consistent contract: preserve resolvable identifiers and include required dependencies, or rewrite process text so it is genuinely sufficient on its own. Adding IDs alone would fix only half the problem. Test the final generated artifacts for each supported role, including whether each citation is necessary and appropriate for that role. Do not indiscriminately pull every cited role's obligations into every bundle.

Sources: [renderer](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/bin/rulestore/render.py#L20), [change flow](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/process/change-flow.md), [R0509](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/rules/R0509.md). The September 10 retro already recognizes the ID-rendering issue; this evaluation confirms it in current output and quantifies missing membership separately.

### C. Adoption prerequisites are omitted by the standard bundle query

`process/project-setup.md` has no `role` key. Every named release query selects by role, so none includes that document. It requires both default-branch protection and a runner-level force-push denial. The README covers the former but does not describe the latter as setup. R0564's agent-facing body says never to force-push; its human rationale contains the two-layer enforcement explanation and is deliberately stripped during rendering.

Put the complete prerequisites in the human quick-start documentation, and ensure the coordinating role has the setup procedure it is expected to confirm. This is a selection/packaging issue, not an argument that every role should receive setup administration instructions. See [project setup](https://github.com/davepierceops/fiducial/blob/8ea66f527cf0114441b34976b09a8326fccbf3c2/process/project-setup.md).

### D. Old entry points still give actionable, obsolete guidance

`MANIFEST.md` describes the earlier context-set bundle system and points to `bin/check-frontmatter`, which is gone. Its tombstone labels the history below it, not all the obsolete instructions above it. `.claude/agents/architect.md` points to removed `roles/`, `context-sets/`, and `policies/` files. `COLLAB-STATE.md` also reads as current state while describing older conventions.

Retire or repair those entry points and label their status where a reader first encounters them. The review corpus can remain intact. Several stale-reference issues are already recorded in `OPEN-ITEMS.md`; recognition is useful, but a new reader encounters the stale file first.

### E. Definition selection and instruction conflicts need artifact-level checks

The writing bundles name the tiers “relayed, demonstrated, grounded, opinion,” but omit R0038, whose term is “claim strength.” Even that row explains the axis more than it specifies the evidence threshold for each tier. The current glossary repeats labels such as `mock-verified` and `reconciliation` through distinct rows. These are symptoms of the difference between lexical term matching and semantic sufficiency.

I also found a release-decision ambiguity worth resolving: R0490 tells the chief of staff every release is the human's call, while the definition of a consequential change says routine changes flow to release on evidence without explicit human go/no-go. This may have an intended interpretation, but a new session should not have to invent it. Make the distinction between standing authorization and an explicit per-release decision clear.

### F. The tool tests are useful; broader validation remains needed

The full suite ran successfully under Python 3.14.7 and Git 2.55.0: **511 tests, 7 skips, 142.994 seconds**. Six skips in the directive TRD suite cite unresolved decisions or governance assertions, and one landing test marks a case outside its report enumeration. These are not seven observed implementation failures. One ResourceWarning reported an unclosed test file. No checked-in GitHub Actions workflows were present.

The stock starter downloads worked, and the real `bin/bundle` command successfully fetched public origin/main and generated a chief-of-staff bundle. The selection audit used the processing functions directly for all twelve roles; it did not bypass the CLI and then claim its freshness gate had been tested.

A small synthetic probe also found that `FileRowSource` accepts an empty rule body despite the non-empty-body acceptance criterion. No shipped rule has an empty body. This is a latent validation defect, lower priority than the actual bundle/adoption problems above.

The source-generation workflow deliberately requires successful network fetch and HEAD equal to origin/main. That makes release provenance conservative but also means a local unpushed fork change or an old release checkout cannot be previewed through the normal CLI. Document this constraint; consider a clearly marked development-preview mode if authoring friction warrants it.

## 5. How I would improve the README

Preserve the direct tone and the compact opening. The current “What this is” paragraph already has the thesis; the problem is that it appears after the download instructions and uses a guarantee the project has not established.

Put these elements in this order:

1. **Concrete identity and purpose:** a method for directing and reviewing LLM work, delivered as role-specific Markdown bundles.
2. **Why you made it:** the recurring gap between confident completion reports and inspectable evidence; the need to retain intent and decisions across sessions. Proposed wording should receive your confirmation as personal motivation.
3. **One concrete outcome:** an evidence-backed change package, or a DOCX returned with tracked edits and anchored criticism. Let readers picture the result.
4. **Who benefits and what they must supply:** experienced users willing to run separate sessions and maintain durable project artifacts; tool-capable hosts for Git or DOCX work.
5. **Direct starter links:** two real clickable links, plus the current writing-profile limitation. Remove the URL template from the quick start.
6. **A short end-to-end workflow:** who does the next step, who starts sessions, what passes between them, and what the human decides.
7. **Evidence and current status:** link a curated worked trail; distinguish tool verification from observed LLM effectiveness.
8. **Customization, tooling, repository map, and the full role reference.** These are valuable after the reader understands the purpose.

Avoid leading with the organization chart. “Chief of staff,” “skeptic,” and “release manager” become useful when readers see the handoffs and artifacts they name. Also avoid adding an imposing manifesto: a roughly hundred-word explanation and a small example can do most of the introductory work.

The accompanying `README-draft.md` is a complete proposed replacement grounded in the current implementation. It openly names the writing limitation; it does not assume the recommended product fixes have happened. Its “Why I built it” section is proposed author copy, inferred from the repository's records, for your confirmation.

## 6. What would make the project substantially more persuasive

**First, fix the public contract.** Align the writing promise with the shipped profile, make bundle references sufficient and resolvable, deliver complete setup instructions, and clear stale active entry points. Rewrite the README alongside this work.

**Then add one annotated example.** Choose a small real software change with an acceptance criterion, a bad-behavior red result, implementation, a skeptical finding, its resolution, and the final release decision. Explain what changed because of the method, and where human intervention remained necessary. The repository already contains raw material; readers need a selected route through it. A separate writing example should show draft, tracked copy edits, critic comments, and the author's accepted result.

**Measure the cost and benefit of the method.** A useful first evaluation would compare a fixed simple baseline against Fiducial on several representative tasks over repeated runs. Hold model and tool access constant; record the bundle SHA. Score unsupported completion claims, defects escaping review, human corrections, total turns, elapsed time, and tokens. Use deliberate traps such as a stale fixture or green mock test with an untested live boundary. For writing, test unsupported claims added, intended claims lost, and fidelity to an author-specific profile. Have outcomes assessed without revealing which configuration produced them where practical.

Those measurements would support an appropriately bounded effectiveness claim. They could also identify which rules deserve context space and which review steps earn their cost.

**My recommendation for sharing today:** share Fiducial with peers as an evolving, inspectable method developed through real use. There is enough substance to invite serious discussion now. For someone adopting it cold, the generality of the writing starter and the completeness of the generated bundles need attention first.

## Reproduction files

- `test-results.txt`: the full local test-run output.
- `audit_bundles.py`: rerunnable corpus-selection audit; accepts the path to a clone.
- `bundle-audit.json`: results at the reviewed commit, including sizes and missing referenced rules.
- `README-draft.md`: proposed replacement copy; no repository files or remote state were changed.
