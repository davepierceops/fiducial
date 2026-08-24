# Review: specs/directive-tooling.md — cycle 2

Verdict: changes-required
Reviewed: specs/directive-tooling.md @ dcfd966
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-23
Scope: Re-gate of a revised PRD, before Dave agrees it — confirmation that each cycle-1 disposition landed as directed, plus a full gate pass over all eight sections: internal consistency, traceability to parent artifacts, NFR dimension coverage, AC testability, risk tolerance, open questions naming what resolves them. Plus the Depth 1 continuity scan that fires automatically on every spec revision.
Cross-checked: docs/cycles/directive-tooling-spec-2-20260823T195803Z.md @ d5a82172, reviews/directive-tooling-cycle-1.md @ cfb25014, specs/prd-template.md, roles/spec-reviewer-agent.md @ ed88dcde, skills/review-artifact.md, docs/global-context/core.md @ 17f75612, docs/global-context/decision-layer.md @ ee7b9daf, skills/directive-authoring.md @ 27ca4560, skills/spec-review-cycle.md, policies/document-metadata-policy.md @ a06460a9, specs/bin-land.md @ 87ae153a, docs/packages/package-a-spec.md §3.6, docs/research/gh-write-friction-20260823T184149Z.md @ 49bd6ff4, docs/cycles/pass2-held-fix-20260823T180753Z.md @ b9444973, decisions/log.md (DEC-000110, DEC-000150, DEC-000160, DEC-000170, DEC-000180), OPEN-ITEMS.md, bin/cycle-open, bin/tests/test_cycle_open.py, bin/tests/helpers.py, and the 95 files in docs/cycles/.
Not inspected: No TRD and no derived acceptance-criteria artifact exist for this spec, so the Depth 1 spine scan again ran against the PRD alone and could not check PRD→TRD or AC→journey traceability downward. Neither `bin/directive` nor `bin/check-directive` exists — no behaviour claimed in the spec was executed. `bin/cycle-open` was read and its reference graph traced (34 in-repo references); its runtime behaviour was exercised only through the pre-existing suite, not directly. `decisions/log.md` was read for the DEC-000110→000150→000180 supersession chain and for DEC-000160 and DEC-000170; it was not read end to end, so a further governing entry may exist. `docs/packages/package-a-spec.md` was read at §3.6 only. The directive corpus was counted by filename but its contents were not re-measured; the friction figures in §1 and §5 are carried from the research findings, not independently recounted. Cycle-1 finding O1 carried **no disposition** in the cycle-2 directive — see O1 below — so no change was made against it and it was re-checked only for whether it is still true. **Reviewer independence:** this artifact was written in the same session that authored the reviewed revision, and by the same author, which is the second consecutive cycle in that posture. No governed rule requires author/reviewer separation for a spec — `operating-model.md` step 5, mirrored in `CLAUDE.md`, scopes that separation to test authorship versus implementation — but the limitation is structural and is not removed by the reviewer stating it. It bears more weight this cycle than last: the two blocking findings below are defects in text this session wrote hours earlier, and the reader has no independent check that a third of the same kind was not missed.
Findings: 2 blocking, 3 non-blocking, 4 observations
Prior cycle: reviews/directive-tooling-cycle-1.md
Dave should inspect: (1) B1 — element M8 rejects the filenames the spec's own generator would produce in its cycle mode, which is a contradiction G0 creates and only you can settle, by exempting the class or by changing the convention; (2) B2 — `bin/cycle-open` is governed by a committed spec and twelve acceptance criteria (`docs/packages/package-a-spec.md` §3.6, AC-CO-1…AC-CO-12) that this document names nowhere while licensing a migration over them; (3) N3 — three committed records name `bin/cycle-open` by name as the tool bearing a decided obligation, and the decision-log policy supersedes entries rather than editing them, so the migration needs a disposition you own; (4) O1 — cycle-1 finding O1 received no disposition in the cycle-2 directive; it was not executed, and it has grown more load-bearing since; (5) O2 — DEC-000110, which the cycle-1 review and the cycle-2 directive both treat as governing, is superseded twice over.

## Disposition confirmation

Each cycle-2 disposition, and what landed. Verified by reading the revised document against the directive.

| Disposition | Landed | Where |
| --- | --- | --- |
| B1 — generalize; state relationship, license one implementation, state migration scope, remove "no generator exists" | yes | §1 para 3; §4 "Relationship to `bin/cycle-open`" G0 and Migration scope; §5 baseline restated; AC-DT-14 added |
| B2 — mandatory always; unconditional lint check of exactly one of two forms; close Q3 and Q7; AC-DT-06 unconditional; J3 stays | yes | §1 "Dictated disposition"; §4 M3 row; §6 AC-DT-06; §8 Q3 and Q7 closed; §3 J3 retained and tightened |
| B3 — cite DEC-000110/000160/000180 where they govern; close or narrow Q5; every governing decision cited by ID | yes, with a correction | §4 G0 (DEC-000180 carried, DEC-000110 recorded as superseded), §2 and G5 (DEC-000160), M5 row, §8 Q5 narrowed. See O2 |
| N1 — skeleton carries the claim-label requirement as an instruction to the executor; restate AC-DT-11 | yes | §6 AC-DT-11; §4 G10 final sentence |
| N2 — Q1 open, resolved-by Dave at TRD stage; AC-DT-02 decidable independent of Q1, or pinned | yes, by restatement | §6 AC-DT-02 (over the declared source manifest); §8 Q1 |
| N3 — name the attribution mechanism or drop the signal; relabel the inference | yes, by naming | §4 G11; §5 first bullet. See N2 below — the named mechanism is under-specified |
| O2 — no edit to `specs/bin-land.md`; one sequencing note | yes | §4 Non-goals, "Naming vocabulary", sequencing note. `specs/bin-land.md` unmodified |
| O3, O4 — no action | n/a | see O4 below |

## B1 — blocking
Claim: Element M8 rejects the filenames the spec's own generator produces in its cycle mode, so G0's single generator would emit directives that G6's lint refuses.
Location: specs/directive-tooling.md §4, M-table row M8; §4 "Relationship to `bin/cycle-open`" G0; §6 AC-DT-06, AC-DT-14.
Evidence: Verified by reading and by running. M8 requires "The directive filename conforms to `docs/cycles/<descriptor>-<timestamp>.md`, timestamp in ISO 8601 basic," derived from `skills/directive-authoring.md` Naming and Core rule 14. `docs/packages/package-a-spec.md` §3.6 AC-CO-1 requires `bin/cycle-open` to write `docs/cycles/cycle-<N>-directive.md` for `--cycle N` or `docs/cycles/<SLUG>-directive.md` for `--name SLUG` — neither carries a timestamp. `ls docs/cycles` returns 95 entries, of which 58 match M8's pattern and 37 do not, the non-matching set including `cycle-1-directive.md` through `cycle-8-directive.md` and every `<slug>-directive.md`. Core rule 14 itself admits the conflict — "Where a convention names it, follow the convention" — while `skills/directive-authoring.md` states the timestamp form unconditionally; the two governed sources already disagree, which is pre-existing, and G0 is what pulls the disagreement inside one tool.
Consequence: A directive generated by `bin/directive --cycle N`, per AC-DT-14 and AC-CO-1, is written to a path `bin/check-directive` fails at M8, at the executor's first act, on a well-formed directive. Under J3 the executor then stops and surfaces, and the cycle costs an invocation for a defect the generator was told to produce. AC-DT-06 requires a failing fixture per element with no exemption stated, and AC-DT-14 requires the cycle mode to exist, so the AC set as written demands both halves of the contradiction. This is not a fixture-authoring nuisance: it is the one place the spec's two tools meet, and they disagree.
Fix: §4 records the naming conflict explicitly and M8 carries the class exception — either M8 reads "conforms to `<descriptor>-<timestamp>.md`, or to the convention a governed document names for the directive's class," with the cycle convention cited, or the cycle convention is changed to timestamps and the change named as a prerequisite of the migration the way §1 names the `skills/directive-authoring.md` amendment. Whichever way, AC-DT-06's M8 fixture set covers both forms, and §8 records which was chosen and by whom.
Related: B2, N3.

## B2 — blocking
Claim: The spec licenses a migration of `bin/cycle-open`'s skeleton emission without naming the committed spec and the twelve acceptance criteria that govern that emission today.
Location: specs/directive-tooling.md §4 "Relationship to `bin/cycle-open`", G0 and the Migration scope paragraph; §6 AC-DT-14.
Evidence: Verified by reading. `docs/packages/package-a-spec.md` §3.6 specifies `bin/cycle-open`'s full CLI and carries AC-CO-1 through AC-CO-12; `bin/tests/test_cycle_open.py` implements them and references `AC-CO-` 34 times. AC-CO-3 fixes the skeleton's structure — heading, `Date:` line, `Documents in scope:` list, `## Decisions` with a commented placeholder carrying `Finding: / Resolution: / Dictated wording:`, `## Deferred / out of scope`, `## Execution notes` — and AC-CO-4 fixes the SHA rule. Those are exactly the behaviours the Migration scope paragraph moves. The revised spec names `bin/cycle-open`, its docstring, and `render_directive` at `:115`, and names neither `docs/packages/package-a-spec.md` nor any AC-CO identifier. AC-DT-14 asserts the post-migration state — "`bin/` contains exactly one directive-skeleton generator" — without stating what becomes of the criteria that currently govern the generator being absorbed.
Consequence: The document that licenses the migration does not trace to the artifact the migration invalidates, so an implementer at the TRD/AC stage inherits an undeclared choice: satisfy AC-CO-1…AC-CO-12 unchanged from inside `bin/directive`, supersede them with AC-DT-* and let a committed spec go stale against shipped code, or split them. The first is the only option that keeps `bin/tests/test_cycle_open.py` green, and it is also the option that carries AC-CO-1's filename convention into the tool — which is B1. This is the cycle-1 B1 defect one layer down: the document now checks what tool exists and still does not check what governs it.
Fix: §4's Migration scope paragraph cites `docs/packages/package-a-spec.md` §3.6 and states the disposition of AC-CO-1…AC-CO-12 — carried, superseded, or split — at the level a PRD carries it, which is at minimum naming which acceptance-criteria artifact is authoritative after the migration. AC-DT-14 gains the corresponding criterion: the pre-existing cycle-open test suite passes against the new path, or the criteria it encodes are explicitly retired by name.
Related: B1, N3.

## N1 — non-blocking
Claim: AC-DT-06 requires an M3 conformance test that AC-DT-13 and §7 forbid a conforming implementation to satisfy, and §3 J3 states the outcome unconditionally.
Location: specs/directive-tooling.md §6 AC-DT-06 and AC-DT-13; §7 "Not accepted", final clause; §3 J3, final sentence; §1 "Dictated disposition" and the prerequisite paragraph following it.
Evidence: Inferred by reading, against the document's own text. AC-DT-06 requires, for M3, four fixture outcomes with no precondition stated. AC-DT-13 states "until `skills/directive-authoring.md` states the unconditional two-branch rule, a lint enforcing M3 fails this criterion," and §7 lists "any lint enforcement of M3 before the governed text states it" as not accepted. §1 states the prerequisite, and the M-table's qualification column repeats it. So the ordering is stated in four places and absent from the one place a Test Designer derives tests from.
Consequence: A Test Designer working from §6 writes the M3 suite and an implementer makes it pass, and the result violates G6 and §7 without either party reading a section that says so. The defect is a missing cross-reference rather than an undecided question — unlike cycle-1 B2, the content of M3 is now decided — which is why this is non-blocking rather than blocking. J3's unconditional sentence is the same gap in prose: it describes what M3 does once enforceable, in a section that does not say M3 is not yet enforceable.
Fix: AC-DT-06 carries the precondition inline for M3 — the criterion applies once the amendment lands, and until then the M3 fixtures exist and are expected to be unenforced. J3 gains the same qualifier in one clause.

## N2 — non-blocking
Claim: The attribution mechanism G11 introduces does not recover the split §5's first signal measures, because naming a source file per section does not locate that section's extent in the landed file.
Location: specs/directive-tooling.md §4 G11; §5, first bullet, "Attribution mechanism"; §6 AC-DT-05.
Evidence: Inferred by reading. G11 requires the manifest to record, "for each invariant section, the committed path it was read from." §5 claims "The manifest names each generator-supplied section, so the split is recoverable from the committed artifact with no tooling beyond reading it." Recovering a byte share requires knowing where each named section begins and ends in the landed file; nothing in G11, G1, G3, or AC-DT-05 requires the skeleton's invariant sections to be delimited, headed, or otherwise locatable, and AC-DT-05's testable content is that the manifest is present in the file and names a path per section.
Consequence: The signal cycle-1 N3 called uncomputable is still uncomputable, by a narrower margin. The fix moved the gap from "no mechanism" to "a mechanism resting on an unstated property," which is the harder kind to notice: §5 now asserts recoverability in terms that read as settled. A measurement section that overstates observability is the specific thing the role's own criterion reaches.
Fix: G11 requires the manifest to locate each section as well as source it — a heading name the skeleton is required to emit, or an explicit delimiter — and AC-DT-05 states that requirement in testable form. Alternatively §5 states the weaker signal the current mechanism actually supports: the count of generator-supplied sections rather than their byte share.

## N3 — non-blocking
Claim: Three committed records name `bin/cycle-open` by name as the bearer of a decided obligation, and the spec states no disposition for them under a migration that moves the obligation to another binary.
Location: specs/directive-tooling.md §4 "Relationship to `bin/cycle-open`", G0 and the DEC-000180 bullet.
Evidence: Verified by reading. `decisions/log.md` DEC-000180 records "Consequence for tooling: `bin/cycle-open` (TP-1, shelved) emits Route and Model and no Track"; DEC-000150 records "`bin/cycle-open` (TP-1) must emit Route, Model, and Track"; `OPEN-ITEMS.md` carries a section headed "`bin/cycle-open` and the retirement of Track" holding the guard DEC-000180 refers to. `policies/decision-log-policy.md` supersedes whole entries rather than editing them — the mechanism DEC-000150 and DEC-000180 both invoke explicitly — so those references cannot simply be rewritten. Core rule 13 requires a changed fact to change everywhere it appears. The spec transfers the obligation ("That obligation transfers to the cycle mode of `bin/directive`") and says nothing about the records that state it against the old name.
Consequence: After the migration, three committed records name a binary that no longer performs the behaviour they assign it, and the only statement to the contrary is a PRD paragraph. A later reader tracing the Track guard from `OPEN-ITEMS.md` arrives at `bin/cycle-open` and finds nothing; the guard DEC-000180 placed against resurrecting a retired field loses its anchor. That is a slow failure, not a loud one, which is why it belongs in the spec rather than in the implementation.
Fix: §4 states, at PRD level, that the migration requires a new decision-log entry recording the transfer and an `OPEN-ITEMS.md` update re-anchoring the Track guard, and names them as consequences of G0 rather than as implementation detail. Neither is in this cycle's change scope.
Related: B2.

## O1 — observation
Claim: Cycle-1 finding O1 carried no disposition in the cycle-2 directive, so it was neither executed nor rejected, and the gap it names has grown more load-bearing since.
Location: reviews/directive-tooling-cycle-1.md O1; docs/cycles/directive-tooling-spec-2-20260823T195803Z.md @ d5a82172, Task 1 disposition list; OPEN-ITEMS.md, "Directive-execution mechanics are oral tradition"; specs/directive-tooling.md §8 Q4.
Evidence: Verified by reading. The cycle-2 directive dispositions B1, B2, B3, N1, N2, N3, O2, O3, and O4 by name. O1 appears nowhere in it. Per the directive's stop conditions — no reinterpretation, no silent partial execution — this session made no change against O1 and surfaced the omission in its report rather than inventing a disposition. The finding itself is still true at `dcfd966`: `OPEN-ITEMS.md`'s still-open paragraph proposes `skills/directive-execution.md` as the canonical home for branch naming, the pre-PR gate, and STOP semantics, and the spec cites neither the entry nor the proposed file.
Consequence: None to the correctness of what landed. Recorded because the omission is asymmetric with the rest of the cycle: `skills/spec-review-cycle.md` step 4 requires one decision entry per finding "including rejections — a rejection recorded nowhere is a decision lost," and O1 is now the one cycle-1 finding with no recorded decision. It also matters more than it did: §1 and Q4 now carry a **mandatory** amendment to `skills/directive-authoring.md`, and whether that amendment lands there or in the proposed `skills/directive-execution.md` is precisely what O1 raised.
Fix: The next directive disposes of O1 explicitly, in either direction.

## O2 — observation
Claim: DEC-000110, which the cycle-1 review treated as governing and which the cycle-2 directive instructed be cited, is superseded twice over; the revision records that, and the disposition's premise shifted as a result.
Location: decisions/log.md DEC-000110, DEC-000150 ("Supersedes: DEC-000110"), DEC-000180 ("Supersedes: DEC-000150"); reviews/directive-tooling-cycle-1.md B3; specs/directive-tooling.md §4 G0, DEC-000110 bullet.
Evidence: Verified by reading. Cycle-1 B3 stated "DEC-000110 decides that a reviewer-gated cycle directive takes **route** (fresh) and **model** (Opus 5) as fixed by its class" and built its consequence on that — "a lint built from the M-table as it stands would, for the reviewer-gated cycle class, either demand elements DEC-000110 explicitly excuses or omit the exception." DEC-000150 reverses that half explicitly, and DEC-000180 supersedes DEC-000150 while carrying the reversal forward: route and model are class **defaults**, stated per dispatch and overridable, not fixed by class. So there is no class exemption for a lint to carry, and the consequence B3 described cannot arise. The revision cites DEC-000110 as dead and DEC-000180 as live, which is the accurate reading of "cite where they govern."
Consequence: None adverse to the revision — the correction is in it. Recorded because a disposition was accepted partly on a premise that does not hold, and because the same misreading is easy to repeat: DEC-000110's text is emphatic and its supersession is recorded only in the two later entries, not on its own face.
Fix: None to this document. A decision-log convention that marks superseded entries in place would prevent the recurrence, which is a matter for `policies/decision-log-policy.md` and not for this spec.

## O3 — observation
Claim: The format contract the cycle mode must satisfy points at a section that no longer exists.
Location: docs/packages/package-a-spec.md §3.6 AC-CO-3; skills/spec-review-cycle.md.
Evidence: Verified by reading. AC-CO-3 requires "The skeleton matches the format in `skills/spec-review-cycle.md`." That document at its current revision has sections Purpose, Use when, Hard constraints, Inputs, Procedure, and Reconciliation, and states no directive format; grep for "Cycle <n> Directive" across `skills/` returns nothing. The format now lives only in AC-CO-3's own enumeration and in `bin/cycle-open`'s code.
Consequence: Pre-existing, and not a defect in the reviewed document. Recorded because it bears directly on B2: an implementer told to move the skeleton emission and to keep AC-CO-3 satisfied is following a reference into an empty target, and the authoritative statement of the format they must preserve is the code they are replacing.
Fix: None to this document.

## O4 — observation
Claim: The two carried-forward observations from cycle 1 remain true, and the pre-existing test failures are unchanged.
Location: reviews/directive-tooling-cycle-1.md O3 and O4; specs/directive-tooling.md frontmatter; bin/tests/test_bundle.py.
Evidence: Verified by running. The spec is still `status: draft` in `specs/`, so `policies/document-metadata-policy.md`'s build-gating rule still requires Dave's explicit per-task confirmation before either tool is implemented. `bin/tests/run` at this cycle's head exits 1 with exactly the two AC-BN-10 failures in `bin/tests/test_bundle.py`, the same pair `docs/cycles/pass2-held-fix-20260823T180753Z.md` @ `b9444973` records as accepted and the cycle-2 directive restates as pre-existing (*told*). This cycle changed three markdown files and no code.
Consequence: None. Recorded so the non-zero suite exit in this cycle's report is not read as a regression, and so the build-gating constraint is not discovered at implementation time.
Fix: None to this document.

## On what the revision got right, and what that does not cover

Every cycle-1 disposition landed, and the two that were easiest to execute
shallowly were not. N1's fix could have been a one-word edit to AC-DT-11; instead
the criterion was re-scoped to the tools' own claims and the reason quoted text is
exempt is stated, which is the distinction G10 was already making and the AC had
widened past. N2's fix could have deferred AC-DT-02 until Q1 resolves; instead the
criterion was rewritten over a manifest the generator declares, so it is decidable
now and stays decidable whichever way Q1 goes. B3's instruction was to cite three
decisions, and the revision found that one of the three does not govern and said
so rather than citing it as if it did.

The document is also now right about its own scope in a way it was not: §4's
migration paragraph enumerates what it does *not* claim about `bin/cycle-open`,
and §8 marks Q3 and Q7 closed with the reasoning that closed them rather than
deleting them.

What sends this to `changes-required` is what the generalization pulled in with
it. G0 is the right disposition and it is stated cleanly, but absorbing a tool
means inheriting that tool's governance, and the document inherited the tool
without it: a committed spec and twelve acceptance criteria are unnamed, three
decision records point at a binary whose obligation is being moved, and the
filename convention the absorbed tool is required to follow is one the new lint is
required to reject. The last of those is not a paperwork gap. It is the two tools
this PRD specifies, disagreeing at the only point they touch.
