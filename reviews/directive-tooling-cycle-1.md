# Review: specs/directive-tooling.md — cycle 1

Verdict: changes-required
Reviewed: specs/directive-tooling.md @ bd09720
Reviewer: Spec Reviewer Agent (execution session)
Date: 2026-08-23
Scope: Gate review of a PRD at initial authorship, before Dave agrees it — all eight required sections, internal consistency, traceability to parent artifacts, NFR dimension coverage, AC testability, risk tolerance, open questions naming what resolves them. Plus the Depth 1 continuity scan that fires automatically on every spec revision.
Cross-checked: specs/prd-template.md @ 39b04d90, roles/spec-reviewer-agent.md @ ed88dcde, skills/review-artifact.md @ 70cab3d3, docs/global-context/core.md @ 17f75612, docs/global-context/decision-layer.md @ ee7b9daf, LEXICON.md @ a9eee071, skills/directive-authoring.md @ 27ca4560, policies/document-metadata-policy.md @ a06460a9, roles/context-quality-reviewer.md, operating-model.md, specs/bin-land.md @ 87ae153a, reviews/bin-land-cycle-1.md @ 6cbf83c2, docs/research/gh-write-friction-20260823T184149Z.md @ 49bd6ff4, docs/cycles/directive-tooling-spec-20260823T194242Z.md @ c5398a42, docs/cycles/pass2-held-fix-20260823T180753Z.md @ b9444973, decisions/log.md (DEC-000110, DEC-000160, DEC-000180), OPEN-ITEMS.md, bin/cycle-open, bin/ and bin/tests/.
Not inspected: No TRD and no derived acceptance-criteria artifact exist for this spec, so the Depth 1 spine scan ran against the PRD alone and could not check PRD→TRD or AC→journey traceability. Neither `bin/directive` nor `bin/check-directive` exists — no behaviour claimed in the spec was executed, and the spec was not checked against code. `bin/cycle-open` was read for overlap (B1) but its full behaviour was not exercised; only its skeleton renderer and its module docstring were inspected. `decisions/log.md` was searched for "directive" and the three matching entries read; the log was not read end to end, so a fourth governing entry may exist. The historical directive corpus was not re-measured; the friction figures the spec carries in §1 and §5 are carried from the research findings, not independently recounted. **Reviewer independence:** this artifact was written in the same session that authored the reviewed document. No governed rule requires author/reviewer separation for a spec — the only separation rule in the corpus (`operating-model.md` step 5, mirrored in `CLAUDE.md`) is scoped to test authorship versus implementation — but the limitation is structural and is not removed by the reviewer stating it.
Findings: 3 blocking, 3 non-blocking, 4 observations
Prior cycle: none
Dave should inspect: (1) B1 — `bin/cycle-open` already emits a directive skeleton, and whether `bin/directive` generalizes it, replaces it, or sits beside it is a question only you can settle; it changes what this spec is for; (2) B3 and §8 Q5 — DEC-000110 fixes route and model by class for one directive class, which partly answers a question the spec poses as fully open; (3) §8 Q7 — whether the working-tree requirement is a named directory or a named directory plus the creating command, which is the one open question blocking a testable M3; (4) O2 — the naming disposition this spec carries contradicts `specs/bin-land.md` §8 Q2, which is still live and which this cycle was forbidden to touch; (5) O1 — `OPEN-ITEMS.md` still proposes a governed document, not tooling, as the fix for this same gap.

## B1 — blocking
Claim: `bin/cycle-open` already generates directive skeletons, and the spec both asserts that no generator exists and states no relationship between it and the proposed `bin/directive`.
Location: specs/directive-tooling.md §5, first bullet; §4 "`bin/directive` — the generator", G1–G4; §2.
Evidence: Verified by reading and by running. `bin/cycle-open`'s module docstring reads "Open a spec-review cycle: directive skeleton + reviewed-revision bundle," and its `render_directive` function emits a heading, a date, a `Documents in scope` list of `path @ sha` pairs, a `## Decisions` placeholder, `## Deferred / out of scope`, and `## Execution notes`. Its docstring further states "Every SHA is the full id of the last commit touching the path, read from git — never invented, never abbreviated" — the same read-from-committed-state principle the spec states as G1. `decisions/log.md` DEC-000110 refers to "`bin/cycle-open`'s generated skeleton (`:116`)", and DEC-000180 records that it "emits Route and Model and no Track". The spec's §5 baseline reads "100% author-composed today (*observed* — no generator exists; `bin/` holds `aimeta`, `bundle`, `bundle-methodology`, `check-frontmatter`, `cycle-open`, `flip-agreed`, `install-hooks`, `migrate-frontmatter`, `tests`)" — the parenthesis that supports the claim contains the counter-example.
Consequence: The spec's §5 baseline is false as written, so the first measurement in the document has no valid starting point. Worse, an implementer at the TRD/AC stage has three defensible readings and the spec licenses none: generalize `bin/cycle-open` to every directive class, build `bin/directive` beside it and accept two skeleton generators that will drift from each other, or replace it and inherit the reviewer-gated cycle format DEC-000110 fixes. The third silently changes a format a committed decision governs. G1's "read, never hardcode" also cannot be assessed as novel until it is known whether it restates what `cycle-open` already does for SHAs.
Fix: §2 or §4 states what `bin/directive` is relative to `bin/cycle-open` — generalization, replacement, or sibling — and §5's baseline is restated against what `cycle-open` already generates rather than against nothing. If the answer is "generalization", DEC-000110's fixed-by-class route and model become a constraint on the generator and belong in §4.
Related: B3, O1.

## B2 — blocking
Claim: The spec's central obligation — prevent the motivating incident recurring — rests entirely on element M3, whose applicability and whose content are both open questions, and §3 J3 nonetheless asserts the incident would have been caught.
Location: specs/directive-tooling.md §1 "Dictated motivating incident"; §4 M3; §3 J3, final sentence; §8 Q3 and Q7; §6 AC-DT-06.
Evidence: Inferred by reading, against the document's own text. M3 is the only element in the mechanically-checkable table traceable to the motivating incident. Its applicability condition — "where the directive is parallel" — is Q3, which the spec states is unanswerable today: "Nothing in a directive's text marks it as parallel today". Its content — directory alone, or directory plus creating command — is Q7, which the spec itself calls "the one open question that blocks writing M3 as a test". §3 J3 closes with "This is the journey the motivating incident would have taken," an unconditional claim about a requirement that is doubly undetermined.
Consequence: The document asserts it discharges the obligation the directive placed on it while its own §8 records that the mechanism cannot yet be specified. A reader taking §3 at face value concludes the incident class is addressed; a reader taking §8 at face value concludes it is not. AC-DT-06 requires a failing-fixture test for each of M1–M8, and for M3 that test cannot be written in either dimension — the AC set is internally inconsistent with §8. Recording a gap in §8 does not discharge it while §3 and §4 continue to state the behaviour unconditionally; that is deferral in one section and assertion in another, which is what makes this a finding rather than a clean deferral.
Fix: Either resolve Q7 and Q3 before this document is agreed, or restate M3, J3, and AC-DT-06 conditionally — M3 as the element that will exist once its two open questions resolve, J3 as the journey the incident would take *given* a resolved M3, and AC-DT-06 scoped to M1–M2 and M4–M8 with M3's criterion deferred by name. The spec must not claim in §3 what it defers in §8.
Related: B1.

## B3 — blocking
Claim: The spec cites no decision-log entry, and at least three govern its subject matter — one of which partly answers a question §8 poses as fully open.
Location: specs/directive-tooling.md throughout, and specifically §4 G6, §4 M-table, §8 Q5.
Evidence: Verified by reading. `decisions/log.md` DEC-000110 decides that a reviewer-gated cycle directive "takes **route** (fresh) and **model** (Opus 5) as fixed by its class, stated once in `skills/spec-review-cycle.md` rather than restated per cycle," and calls this "a bounded exception to ... the all-four-every-time rule." DEC-000160 fixes the executor's first act — write to `docs/cycles/`, commit, read the SHA back, report — "to every directive class, reviewer-gated cycle directives included." DEC-000180 records that track is retired and that `bin/cycle-open` emits Route and Model and no Track. §8 Q5 asks whether the directive file is the right lint unit given that this cycle's own file carries neither route nor model tier, and presents the question as entirely open. G6 requires the required-element set to derive from committed governed text and names three sources; the decision log is not among them, and it was not consulted in deriving the M-table.
Consequence: A lint built from the M-table as it stands would, for the reviewer-gated cycle class, either demand elements DEC-000110 explicitly excuses or omit the exception without knowing it exists — the general-statement-contradicts-the-exception failure DEC-000110 was written to prevent. §8 Q5 sends Dave a question the log has already partly answered, which costs a decision round that need not happen. And G6's own standard is not met by the document that states it: the element set was derived from three governed files while a fourth governing source went unread.
Fix: §4 G6 names `decisions/log.md` among its sources. The M-table records, per element, whether a committed decision qualifies it — at minimum DEC-000110 against any route/model element and DEC-000160 against M5. §8 Q5 is narrowed to what DEC-000110 leaves open, or withdrawn if it leaves nothing.
Related: B1, O1.

## N1 — non-blocking
Claim: AC-DT-11 is unsatisfiable for the generator, because G1 requires the skeleton to carry the claim-label instruction, whose text necessarily contains the words *inferred* and *told*.
Location: specs/directive-tooling.md §6 AC-DT-11; §4 G1; §4 G10.
Evidence: Inferred by reading. G1 lists "claim labels" among the invariant sections the skeleton carries, read from committed repo text. Core rule 6 names four classes, so any faithful rendering of that instruction emits the strings `inferred` and `told`. AC-DT-11 reads "Every claim in either tool's output carries the label *observed* or *unknown*, and no output carries *inferred* or *told*" — a statement about output bytes, where G10 makes a narrower statement about the lint's own claims.
Consequence: The criterion fails on a correct implementation. Since the criterion is stated over "either tool's output" rather than over the tools' own claims, a Test Designer deriving from it writes a test that a conforming generator cannot pass, and the natural repair — suppressing the words in the skeleton — would break G1.
Fix: Restate AC-DT-11 over the claims each tool makes about its own findings, not over the bytes it emits, and say explicitly that text quoted from committed sources is out of its scope. G10 already has the right scope; the AC widened it.

## N2 — non-blocking
Claim: AC-DT-02 is not testable while Q1 is open, because "invariant text" has no decidable boundary until where that text lives is settled.
Location: specs/directive-tooling.md §6 AC-DT-02; §4 G1; §8 Q1.
Evidence: Inferred by reading. AC-DT-02 requires that "No invariant text the skeleton emits appears as a literal in the generator's source," and qualifies it "against the set of sections G1 enumerates." G1 enumerates section *names*, not text; Q1 states that where the text lives and how the generator resolves it is unresolved.
Consequence: The Test Designer cannot decide what string set the assertion ranges over, and any set they choose becomes the de facto contract — the same failure mode `reviews/bin-land-cycle-1.md` N1 records for a criterion depending on a deferred format decision. Deferring the location to Q1 is legitimate; carrying a criterion that silently depends on it is what makes this a finding.
Fix: Restate AC-DT-02 as a static property over a named manifest of sources the generator reads — which the generator must expose anyway to satisfy AC-DT-05 — so the criterion becomes testable without pre-empting Q1.

## N3 — non-blocking
Claim: §5's first measurement names no mechanism that could actually attribute bytes, and presents an inference as if it were the research findings' measurement.
Location: specs/directive-tooling.md §5, first bullet.
Evidence: Inferred by reading, cross-checked against `docs/research/gh-write-friction-20260823T184149Z.md` @ 49bd6ff4. The stated mechanism is "measure generator-supplied versus hand-authored bytes over directives authored after adoption," but the author edits the skeleton, and nothing in §4 requires the generator to mark its own output, so the split is unrecoverable from the committed file. Separately, the spec introduces the research figure with "The research findings give the size of the region a generator would fill: write mechanics alone run 13.9% to 43.3%" — the research document measured write-mechanic sentences, and the equation of that region with the generator's region is the spec's own inference, carried under an *observed* label.
Consequence: The first of three user-outcome signals cannot be computed, so the measurement section overstates what will be observable. The mislabelled provenance is the narrower defect but the one the role's own criterion reaches directly: no section may overstate confidence, and an inference presented inside an *observed* citation does.
Fix: Either require the generator to mark its output — a requirement in §4, and a testable one — or replace the signal with one computable from the committed artifact. Relabel the 13.9–43.3% sentence so the measurement is *observed* and the equation with the generator's region is *inferred*.

## O1 — observation
Claim: `OPEN-ITEMS.md` carries a still-open entry naming this exact gap and proposing a governed document, not tooling, as its fix; the spec does not cite it.
Location: OPEN-ITEMS.md, "Directive-execution mechanics are oral tradition — the kickoff restates governed rules"; specs/directive-tooling.md §8 Q1 and Q4.
Evidence: Verified by reading. The entry is marked "**SUPERSEDED IN PART**" but carries a "**Still open:**" paragraph: branch naming, the run-the-tests-and-`check-frontmatter`-before-the-PR gate, and STOP semantics "still have no canonical home, and a `skills/directive-execution.md` is still the proposed fix." The same entry records Dave's own diagnosis from 2026-08-02 — "a per-dispatch restatement is an unversioned derived copy of governed text, and derived copies written fresh drift" — which is the spec's problem statement, reached earlier and independently. The research findings likewise rank a standing governed document first among options and call it a precondition. The spec's §8 Q1 gestures at "a decision already in flight" without naming the entry or the proposed file.
Consequence: Not adverse to the spec's correctness — Q1 and Q4 keep the substance open. Recorded because the strongest corroboration for §1 is an existing repository artifact the spec does not cite, and because the standing proposal is a *document*, which makes "do these tools sit beneath `skills/directive-authoring.md`" (Q4) a live sequencing question rather than a formality.
Fix: §1 cites the open item as prior art for the problem statement; §8 Q4 names `skills/directive-execution.md` as the standing alternative proposal.

## O2 — observation
Claim: The naming disposition this spec carries contradicts `specs/bin-land.md` §8 Q2, which is live, and this cycle was forbidden to conform it.
Location: specs/directive-tooling.md §4 Non-goals, "Naming vocabulary"; specs/bin-land.md @ 87ae153a §8 Q2.
Evidence: Verified by reading. `specs/bin-land.md` §8 Q2 states "The binary name `land` is provisional, pending Dave's `LEXICON.md` check," and marks it resolved by Dave. The disposition in this spec — binary names are not methodology vocabulary, no LEXICON entry is created for a binary name — answers that question as a class. Core rule 13 requires that a changed fact be updated everywhere it appears; the directive originating this cycle restricts the change set to three files and forbids modifying anything else, so `specs/bin-land.md` was correctly left alone.
Consequence: Two spec documents now state different things about the same open question, and the older one is the one a reader arrives at from the bin-land review. The condition is deliberate and bounded, not a defect in either document, but it persists until something conforms Q2 — and the disposition's own text says the durable record lands with the bin-land cycle 3 directive, which has not landed.
Fix: None available to this cycle. The bin-land cycle 3 directive discharges Q2, or a separate change conforms it.

## O3 — observation
Claim: Placing this spec at `specs/` puts implementation of both tools under the metadata policy's build-gating rule while the spec is `draft`.
Location: specs/directive-tooling.md frontmatter; policies/document-metadata-policy.md @ a06460a9, "Scope" and "Agent behavior".
Evidence: Verified by running and by reading. `bin/check-frontmatter --all` matched 53 in-scope files at this commit, this document among them, and exited 0. The policy's build-gating rule covers `specs/` documents and forbids building against a `draft` spec "without explicit human confirmation," per-task.
Consequence: None adverse; the placement was directed and is the stricter of the available options. Recorded because a later session directed to implement `bin/directive` needs Dave's explicit per-task confirmation while this spec is `draft`, and that is the kind of constraint discovered at the wrong moment. The same note appears as O2 in `reviews/bin-land-cycle-1.md`; it applies here for the same reason.
Fix: None. Dave confirms per-task when implementation is directed, or agrees the spec first.

## O4 — observation
Claim: The two test failures observed in this cycle are pre-existing and unrelated to this change.
Location: bin/tests/test_bundle.py, `test_bn10_bundle_base_yields_exactly_itself` and `test_bn10_transitive_body_references_are_followed_in_this_repo`.
Evidence: Verified by running. `bin/tests/run` ran 399 tests and exited 1 with exactly two failures, both asserting on `bundle`'s CLI contract — stderr "an ENTRY is no longer accepted; use --audience VALUE or --list". This cycle added three markdown files and no code. `docs/cycles/pass2-held-fix-20260823T180753Z.md` @ b9444973 permits "only the two accepted AC-BN-10 failures", establishing them as known and accepted before this cycle (*told*, per that directive).
Consequence: None for this spec. Recorded so the non-zero exit status in this cycle's report is not read as a regression introduced here.
Fix: None to this document.

## On the two checks most likely to have failed

The role's NFR-coverage and open-question criteria were the two most likely to
fail on a document of this shape, and both pass. Every dimension the PRD template
names is addressed, and the three that genuinely do not apply — Scalability,
Compliance, and a latency target under Performance — are marked N/A or negatively
constrained rather than padded. Every open question in §8 names what resolves it,
and each names a party rather than a process.

The document is also right about the thing it would have been easiest to get
wrong. §4's separation of mechanically checkable elements from judgment-only
rules is the spec's substantive contribution, and the argument that
executability of a working-tree assignment is unknowable at authoring time is
demonstrated rather than asserted — by this session's own failure to create the
assigned tree. That reasoning holds, and it is the reason the spec's narrow claim
about what a lint can establish is the honest one.

What sends this to `changes-required` is not that reasoning. It is that the
document did not check what already exists before proposing to build it: a
generator is already in `bin/`, a governed document is already proposed for the
same gap, and a decision entry already governs part of what the lint would check.
All three are in this repository, and none is cited.
