# Review: skills/directive-invariants.md — cycle 1

Verdict: changes-required
Reviewed: skills/directive-invariants.md @ 7c233c1506dc6111194b5fe603f2fd2f967d4998
Reviewer: Context Quality Reviewer (execution session)
Date: 2026-08-30
Scope: skills/directive-invariants.md, whole, at the reviewed SHA, against all twelve criteria of docs/global-context/review-rubric.md. Its in-scope status was confirmed against the document metadata policy's Scope section (`skills/**`).
Cross-checked: skills/directive-authoring.md; specs/directive-tooling-trd.md §3.3, §3.4 and §3.9, plus §3.6's M4/M5 derivations read to ground two findings; docs/global-context/core.md rules 6, 11 and 15; policies/document-metadata-policy.md (Scope, `audience:`, `session:`); bin/aimeta/invariants.py and bin/aimeta/directive.py, run and read to distinguish what the document states from what the compiler does.
Not inspected: the `bin/` test suite — not run by this directive, and reported as not run, so no claim is made about whether the byte-equality test specs/directive-tooling-trd.md §3.3 names exists or passes. Also not inspected: the PRD; the acceptance-criteria documents (AC-DT-*, AC-CO-*) named throughout the TRD; `decisions/log.md`; specs/directive-tooling-trd.md §§1–3.2, 3.5, 3.7, 3.8, and 4–9 except the §3.6 passages named above; bin/check-directive and bin/aimeta/elements.py beyond one grep for the preamble-marker tolerance; any generated skeleton — `bin/directive` was not invoked; every governed file other than those named on the Cross-checked line.
Findings: 3 blocking, 9 non-blocking, 3 observations
Prior cycle: none
Dave should inspect: F-1, which of two readings of the disposition match rule is authoritative; F-2, where the closed placeholder set is fixed, given that the document names a source that does not fix it; F-9, whether the exclusive-assignment narrowing must carry its disclosure here as well as in the TRD.

## F-1 — blocking
Claim: The match rule's phrase "exactly that literal" resolves to the colon-bearing fence above it, which specifies a rule neither the TRD nor the shipped compiler implements.
Location: skills/directive-invariants.md:183–191 (`## Disposition label`)
Evidence: Verified by running. The section's only preceding fence holds `WORKING-TREE DISPOSITION:` (line 186), and the match rule at lines 189–191 reads "an eligible line whose leading content, after stripping, is exactly that literal, followed by a colon anywhere later on the same line" — leading content `WORKING-TREE DISPOSITION:` plus a further colon. `bin/aimeta/invariants.py` does not do this: `label()` is `label_literal().rstrip(":").rstrip()`, and `matches_label()` tests `line.startswith(label)` then `":" in line[len(label):]`. Constructing `invariants.Document` over the reviewed text and calling it returned `label_literal() == 'WORKING-TREE DISPOSITION:'`, `label() == 'WORKING-TREE DISPOSITION'`, and `matches_label('WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.') == True`. specs/directive-tooling-trd.md §3.4 states the same as the code: "the label is the literal `WORKING-TREE DISPOSITION`" for the match, with `WORKING-TREE DISPOSITION:` fixed separately as the literal the generator emits.
Consequence: The document is the single source the TRD assigns this rule to, and it is the text a second implementation — or an agent applying the rule by hand — would compile. Applied as written, the canonical sole-tree statement `WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.` carries no colon after the colon-bearing literal, so it fails the match, and every sole-tree directive fails M3 while the shipped lint passes it. The two readings disagree on a live form the document itself supplies as a worked example at line 79.
Fix: Separate the two parts the way §3.4 does — fence the emitted literal as `WORKING-TREE DISPOSITION:` and state the match rule against the bare token, e.g. "leading content, after stripping, is exactly `WORKING-TREE DISPOSITION`, followed by a colon anywhere later on the same line" — so the sentence no longer takes its antecedent from a fence that carries the colon.

## F-2 — blocking
Claim: The document sources its closed placeholder set to "the TRD's §3.3 tables", which fix no placeholder for the cycle heading region, so three placeholders the document uses have no authority behind them.
Location: skills/directive-invariants.md:20–21 (preamble) and 34–38 (`## Heading (cycle)`)
Evidence: Verified by running and by reading. A parse of the reviewed file found ten distinct placeholders: `title`, `heading`, `date`, `scope_list`, `route`, `model`, `directive_path`, `reviewed_ref` (twice), `companion_list`, `manifest`. specs/directive-tooling-trd.md §3.3's general-mode table has a Placeholders column naming seven — `title`, `route`, `model`, `directive_path`, `reviewed_ref`, `companion_list`, `manifest`. The cycle-mode table has no Placeholders column at all; its fourth column is Note, and its row 1 names none. `grep` of `bin/aimeta/directive.py` shows the three unaccounted names bound only in code: `Region(invariants.HEADING_CYCLE, ("heading", "date", "scope_list"))` at line 101, with `cycle_values(*, heading, date, scope_list, ...)` at line 138.
Consequence: The set is load-bearing — the document states at line 21 that "an unrecognised placeholder is a refusal, never a pass-through", and `substitute()` raises `[invariants-placeholder-unknown]` at exit-code precondition for any name outside it. The document points at a source that names seven of the ten, so the closed set has two partial definitions and no complete one; a maintainer editing `§Heading (cycle)` against the cited authority cannot tell whether `{{scope_list}}` is admitted, and a reviewer checking the document against §3.3 finds three placeholders the tables do not sanction.
Fix: Either state the closed set in this document, per region, or amend the sentence to name the actual authority for each mode — and have §3.3's cycle table carry a Placeholders column naming `{{heading}}`, `{{date}}` and `{{scope_list}}` on row 1. Resolving which document gains the column is not this review's to decide; the disagreement is surfaced.

## F-3 — blocking
Claim: The document cannot be applied by a reader who has only the bundle: it names four external sources by path or section for facts it does not state, and it compiles a match rule over two terms it never defines.
Location: skills/directive-invariants.md:10–13 (`bin/aimeta/invariants.py`, `bin/directive`, `bin/check-directive`), :20 ("the TRD's §3.3 tables"), :189 ("an eligible line", "after stripping")
Evidence: Inferred by reading, with the path existence checked by running: all three named paths exist at the reviewed SHA, so the sentence is accurate — the defect is that it is a path-shaped reference, which criterion 3 makes a defect on its face, and this file's subject is region text rather than paths, so the criterion's exemption for scope definitions and glob configurations does not reach it. "The TRD's §3.3 tables" is not path-shaped but is the same defect under criterion 1: the closed set it names is not stated here, and neither is the region table. "Eligible line" and "after stripping" are specs/directive-tooling-trd.md §3.5's terms, defined by `mdmask.py`'s masking rules and nowhere in this file.
Consequence: The file carries `audience: [chief-of-staff, human]`, so it lands in the chief-of-staff bundle and is read there by an agent that has never seen the repository. That agent is asked at line 189 to apply a rule to "an eligible line" and to its "leading content, after stripping" without being told which lines are eligible or what stripping removes — the rule is inapplicable as delivered. Separately, the three `bin/` paths tell a bundle reader to go and read code that is not in the bundle.
Fix: State in this file what the reader must have: the eligibility and stripping rules the match depends on (or enough of them to apply the rule), and the closed placeholder set. Replace the `bin/` paths with a statement of the property they were cited for — that the label, the marker syntax and every region's text have one definition — without naming the modules.

## F-4 — non-blocking
Claim: `## Stop conditions` restates Core rules 11 and 15.
Location: skills/directive-invariants.md:123–129
Evidence: Inferred by reading. The region says "Cannot execute as written: stop and report. Concurrent tree mutation: stop and report." docs/global-context/core.md rule 11 is "**Cannot execute as written → stop and surface.**" and rule 15 is "**Concurrent tree mutation → stop and surface.**" — the same two triggers, with *report* substituted for *surface*. This region's text is emitted verbatim into every generated skeleton, in both modes (specs/directive-tooling-trd.md §3.3, general row 11 and cycle row 13), and specs/directive-tooling-trd.md §3.6 states that the section "is written to contain both, which is how the generator's own output satisfies M4". That is a fact for triage, not a waiver: the restatement is stated as a finding.
Consequence: The file lands in the chief-of-staff bundle alongside Core, which is `audience: [all-roles, human]` and `order: 0`. The bundle then states the same two stop triggers twice, in two wordings — *stop and surface* and *stop and report* — and a reader deciding whether *surface* and *report* name the same act has no basis in either file for saying so.
Fix: Dave's call, because the region is emitted text a lint matches on. Either accept the duplication as the cost of M4's self-satisfaction and record it, or have M4 derive its phrases from Core directly so the region need not carry them.
Related: F-5

## F-5 — non-blocking
Claim: `## Claim labels` restates Core rule 6.
Location: skills/directive-invariants.md:143–145
Evidence: Inferred by reading. The region is "Label every claim observed, inferred, told, or unknown." docs/global-context/core.md rule 6 is "**Every claim carries its class.** ... label it *observed* (you saw it), *inferred* (you reasoned to it), *told* (someone said it), or *unknown*." Same rule, same four class words. This region's text is emitted verbatim into every generated skeleton (specs/directive-tooling-trd.md §3.3, general row 13 and cycle row 15), and the four words are what `## Match phrases` compiles as M7 — a fact for triage, not a waiver; the restatement is stated as a finding.
Consequence: The chief-of-staff bundle states the claim-labelling rule twice. Core's version defines each class; this one does not, so a reader who meets the shorter form first has four bare words and no definitions, and the two versions differ in what they teach.
Fix: As F-4 — Dave's call between accepting the duplication for M7's sake and deriving M7's phrases from Core.
Related: F-4

## F-6 — non-blocking
Claim: The preamble carries rationale for its rules rather than stating them.
Location: skills/directive-invariants.md:9–26
Evidence: Inferred by reading. Three clauses argue rather than instruct: "so the label, the marker syntax and every region's text have one definition rather than two agreeing copies" (12–13); "so the generator copies the marker rather than composing it" (19–20); and "That is the one property of this one file that makes the generated skeleton carry exactly one unfenced labelled statement, and amending it breaks that guarantee for every subsequent skeleton" (24–26), which is a justification plus a warning about consequences of amendment.
Consequence: Criterion 6 exists because rationale in a bundle is context an agent must weigh against the instruction. Here it also invites the wrong action: line 26 tells a reader what breaks if the fencing rule is amended, which reads as an invitation to weigh the amendment, when the rule is not the reader's to amend.
Fix: Cut the three clauses. State the rules: the label appears only inside fenced blocks; a region section's body opens with that region's marker line.

## F-7 — non-blocking
Claim: The preamble's rules are addressed to whoever maintains or parses the file, not to the agent reading it.
Location: skills/directive-invariants.md:15–21
Evidence: Inferred by reading. "Every section below is a `##` heading at column 0. A section's body runs from its heading to the next `##` heading, and **the first non-blank line of a body is always body**" states a schema for a parser. specs/directive-tooling-trd.md §3.3's "The invariants document's own format" fixes exactly this schema, and `bin/aimeta/invariants.py`'s `parse_sections` implements it. Nothing in the paragraph is an instruction the reading agent can carry out.
Consequence: An agent reading the bundle cannot act on the paragraph and must decide for itself whether the schema constrains something it is about to do. Criterion 5 exists to keep that decision from arising.
Fix: Restate the schema as an instruction to whoever edits the file, or drop it here and let the TRD hold it — noting that dropping it interacts with F-3, since the parse rule is one of the few things a bundle reader might legitimately need.

## F-8 — non-blocking
Claim: The document does not say which session kind it is for.
Location: skills/directive-invariants.md:1–26 (frontmatter and preamble)
Evidence: Verified by running for the frontmatter, inferred by reading for the prose. The frontmatter is `status: draft`, `last-reviewed: null`, `audience: [chief-of-staff, human]` and nothing else; policies/document-metadata-policy.md permits `session:` on role documents only, so the statement cannot go there. skills/directive-authoring.md, the neighbouring skill, states it in prose in its first line — "This procedure runs in a decision session." This document states nothing equivalent, and its content is split: the region text is emitted into directives that execution sessions carry out, while the file itself is consumed by the generator a decision session runs.
Consequence: A chief-of-staff bundle reader cannot tell whether `## Stop conditions` and `## Claim labels` are rules binding it now or text to be emitted for someone else. Read the first way, an execution session could take the document's region bodies as its own standing instructions; read the second, a decision session could skip them.
Fix: Add the sentence the sibling skill uses, adapted: state that the document is read by a decision session's generator and that its region bodies are emitted into directives execution sessions carry out.

## F-9 — non-blocking
Claim: `## Disposition label` states the exclusive-assignment match test without the disclosure the TRD attaches to it, while the same file carries the broader governed rule six sections earlier.
Location: skills/directive-invariants.md:197–198, against :63–70
Evidence: Inferred by reading. Lines 197–198 give the test as "the extent contains a `git worktree add` invocation and a quoted or backticked path-shaped token. Both, or neither." specs/directive-tooling-trd.md §3.4 states the same test and then, under its own bold heading, that "**That match rule is this document's own narrowing, and is disclosed as one**" — the governed rule "names no subcommand and no quoting", the narrowing "bounds what the lint **matches**; it adds nothing the lint **enforces**", and "No directive is required to write its disposition this way." None of that disclosure appears in the invariants document. The governed rule it narrows is in the same file, at lines 63–70, inside `§Working-tree disposition prompt`'s fence: "a named directory plus the command creating it".
Consequence: A decision session authoring a disposition reads both passages in one file with nothing marking one as a match bound and the other as the requirement, and takes the narrower as the rule — writing a bare unquoted path or a different tree-creating command becomes something the author believes is forbidden rather than something the lint merely fails to match. The TRD's accepted false-stop cost silently becomes an authoring constraint.
Fix: Carry one sentence of the TRD's disclosure into the section — that the test bounds what the lint matches and adds no requirement on how a disposition is written.

## F-10 — non-blocking
Claim: `## Route and model` emits a Model line with no statement that the value is a tier.
Location: skills/directive-invariants.md:42–45
Evidence: Inferred by reading. The region is `ROUTE AND MODEL` / `Route: {{route}}` / `Model: {{model}}`, and no sentence anywhere in the document constrains either value. specs/directive-tooling-trd.md §3.3 states "The lint checks neither value" and keeps both in AC-DT-08's unchecked set. Criterion 8 requires that model selection speak in tiers. Route, model and the execution block are all present, and no `Track:` line is emitted by any region — that half of the criterion passes.
Consequence: A skeleton filled with `Model: claude-opus-4-1` is emitted, passes the lint, and lands as a directive, because nothing in the generator's only source of region text says the slot takes a tier.
Fix: State the constraint in the region body or in the section's prose — the value is a tier, not a model name — so the author filling `{{model}}` reads it in the file the value comes from.

## F-11 — non-blocking
Claim: `## Match phrases` gives five of eight elements with no statement that the other three have no block by design.
Location: skills/directive-invariants.md:223–262
Evidence: Inferred by reading. The section opens "The phrases the lint compiles, one fenced block per element" and then gives M1, M4, M5, M6 and M7. M2, M3 and M8 have no block. specs/directive-tooling-trd.md §3.3 states their absence is not an omission — "M2 and M8 match no phrase at all, and M3's strings are `## Disposition label`'s" — and that sentence is not carried here.
Consequence: The opening sentence says one block per element and then supplies five for eight, so a reader of the file alone reads three missing blocks as an incomplete document, and a maintainer could add blocks for M2, M3 or M8 believing they were dropped — which for M3 would create a second definition of the label strings the whole single-source design exists to prevent.
Fix: Add the TRD's sentence, or narrow the opening to "one fenced block per element that compiles a phrase" plus a line naming the three that do not.

## F-12 — non-blocking
Claim: `## Preamble markers` fences `<document heading>`, which is not a marker token any directive carries, and the file says nothing distinguishing it from the literal beside it.
Location: skills/directive-invariants.md:214–221
Evidence: Verified by running, then read. `invariants.Document.preamble_markers()` over the reviewed text returns `['<document heading>', 'ROUTE AND MODEL']` — the angle-bracket string is returned verbatim, exactly as the literal is. A grep of `bin/` shows the tolerance handled in `bin/aimeta/elements.py:143`, whose docstring reads "`(literal tokens, whether the document heading is tolerated)` — M5", so the special case lives in code. specs/directive-tooling-trd.md §3.6 states the intent: the entry "is written as *the document heading* rather than as any mode's heading text" so that §3.3's three heading forms need no entries of their own. No directive's heading line is the text `<document heading>`.
Consequence: The section presents two entries in one fence as though they were the same kind of thing. A reimplementation compiling the fence as a literal list — which is what the section's shape invites, and what `preamble_markers()` alone would support — would fail M5 on every directive, because no heading matches the string. The one entry whose meaning is not literal is the one carrying no marking.
Fix: Mark the entry as standing for whatever heading a mode emits, in the section's prose or in the fence's own form, so the distinction is in the document rather than only in the code that special-cases it.

## O-1 — observation
Claim: The worked exclusive-assignment example creates a worktree on `main`, which fails whenever `main` is checked out in the primary tree.
Location: skills/directive-invariants.md:76–77
Evidence: Inferred by reading. The example is `git worktree add "wt/<name>" main`. `git worktree add <path> <branch>` checks that branch out in the new tree, and git refuses a branch already checked out elsewhere. The confirming command was not run: creating a scratch repository to probe it was denied by the sandbox, so this entry claims no verified result and is recorded as an observation rather than a finding.
Fix: If the reading holds, the example would take the form this directive's own disposition used — a new branch off a base ref, e.g. `git worktree add --no-track "wt/<name>" -b <branch> origin/main`.

## O-2 — observation
Claim: `{{name}}` appears in the preamble, outside every section.
Location: skills/directive-invariants.md:20
Evidence: Verified by running. The parse found `{{name}}` among the file's `{{...}}` tokens; it sits above `## Heading (general)`, so it is in no section. `bin/aimeta/directive.py` runs substitution per region over `section()` bodies, so the preamble is never passed to `substitute()` and the token cannot trigger the unknown-placeholder refusal. Nothing goes wrong today.
Fix: None needed while substitution stays per-section; noted because a future whole-file pass would refuse on it.

## O-3 — observation
Claim: This document and skills/directive-authoring.md carry the same `audience:`, so a chief-of-staff bundle states the disposition rule twice.
Location: skills/directive-invariants.md:4 and :63–70
Evidence: Verified by running. Both files carry `audience: [chief-of-staff, human]`, and cross-check 1 confirmed the two texts are byte-identical after flowing. specs/directive-tooling-trd.md §3.3 names this as deliberate by-value quotation and prices it with a test asserting byte-equality against the bullet as committed. Whether that test exists at this SHA was not inspected — the `bin/` suite was not run by this directive.
Fix: None while the two agree. Recorded so the duplication is visible to triage, and so the test's existence can be confirmed before the pairing is relied on.
