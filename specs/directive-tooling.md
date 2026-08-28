---
status: draft
last-reviewed: null
audience: [human]
---

# PRD: directive tooling — `bin/directive` and `bin/check-directive`

Two tools that together gate the directive artifact class. `bin/directive`
generates a directive skeleton whose invariant text is read from committed
governed files; `bin/check-directive` is a lint the executor runs as part of
its first act, failing a directive that is missing a required element.

The TRD beneath this document decides mechanisms. Where this document routes a
decision to the TRD it states the property the TRD's answer must satisfy.

## 1. Problem and intent

Directives are the only ungated load-bearing artifact class in this
methodology. Specs get the Spec Reviewer, governed documents get the Context
Quality Reviewer, code gets the red-gate; directives ship freehand from a
decision session to an executor. Freehand composition has an irreducible error
rate that worsens with accumulated context — a decision session late in a long
conversation is a degraded author. The countermeasure is structural, not
exhortative: shrink the freehand surface, gate the remainder.

The gap is structural, not an enforcement oversight. The frontmatter in-scope
set in `policies/document-metadata-policy.md` does not reach `docs/cycles/`, and
no role document names directives as its review scope.

**Motivating incident.** A parallel directive stated a working-tree
*prohibition* and no disposition of either admitted form. The executor stopped
correctly; the omission class is the target. The governing rule now reads, in
`skills/directive-authoring.md`: every directive states its working-tree
disposition — either an exclusive assignment (a named directory plus the command
creating it) or an explicit sole-tree declaration — as its own labelled
statement, exactly one per directive; a prohibition is not a disposition.

**Existing tooling.** `bin/cycle-open` already generates a directive skeleton
for one class, the reviewer-gated spec-review cycle. It becomes a mode of
`bin/directive` (§4 G0).

**Measured cost of freehand authorship.** `docs/research/gh-write-friction-20260823T184149Z.md`
found that across the 90 markdown files in `docs/cycles/` it measured,
sentences carrying write-path vocabulary were 16.5% of sentences and 21.8% of
characters — a count of files in a directory, not of directives as a class; in
the six most recent `pass2` directives, write mechanics ran 13.9%–43.3% of each
file; and eight committed directives instructed one merge mechanism while the
most recent instructed its opposite. Those figures describe the invariant text
this effort stops hand-writing.

## 2. Users and use cases

**Decision session** — authors a directive. Runs `bin/directive`, receives a
skeleton whose invariant sections are already filled from committed text, and
writes exactly two regions: the task-specific middle and the content of the
working-tree disposition. This is the actor whose error rate the problem
statement names, and the one least able to self-check.

**Execution session** — receives a directive. Its first act is already to write
the directive file, commit, push, and report the SHA (Core, "Execution block";
DEC-000160). It runs `bin/check-directive` inside that act and stops before any
work if the lint exits non-zero.

**Dave** — consumes a lint failure as a signal that a directive is malformed,
before an executor has spent a cycle discovering it. He runs neither tool.

Use cases:

- Generate a directive skeleton whose invariant text is current with the
  repository rather than with the author's memory of it.
- Fail a malformed directive at the executor's first act, at a cost of one
  invocation rather than one cycle.
- Establish mechanically which required elements a directive carries, and state
  equally mechanically which properties were not checked.

## 3. User journeys

Top K = 3.

### J1 — author a directive from the skeleton

- **Actor**: decision session.
- **Trigger**: Dave directs work that needs an execution session.
- **Steps**: invokes `bin/directive`; receives a skeleton carrying the sandbox
  constraints, stop conditions, the working-tree disposition prompt, the
  verification steps, the report format, and the claim-label instruction — each
  read from committed text — plus a disposition author region carrying the
  label over an empty content slot; fills the task-specific middle and the
  disposition content slot, and nothing else; hands the directive to an
  execution session.
- **Expected outcome**: a directive whose invariant text matches the
  repository's current committed text, with the author's freehand contribution
  confined to two regions. A skeleton whose content slot is filled faithfully
  passes the lint, by construction (G3).

### J2 — the executor's first act clears the lint

- **Actor**: execution session.
- **Trigger**: the session's first act under a directive.
- **Steps**: writes the directive file, runs `bin/check-directive` against it,
  and on exit 0 commits and pushes as it does today.
- **Expected outcome**: exit 0, plus a statement of which elements were checked
  and which properties were not, so the pass is not read as broader than it is.

### J3 — a directive missing a required element

- **Actor**: execution session.
- **Trigger**: `bin/check-directive` exits non-zero at the first act.
- **Steps**: the session stops and surfaces, naming the missing elements and
  the governed text each derives from. It does not repair the directive, does
  not infer intent, and does not begin the work.
- **Expected outcome**: the cycle costs one invocation instead of one
  execution. The missing element goes back to the decision session, the only
  place it can be supplied. The motivating incident takes this journey: no
  labelled disposition statement, so M3 fails.

## 4. Goals and non-goals

### Relationship to `bin/cycle-open`

**G0 — one generator.** `bin/cycle-open` becomes a mode of `bin/directive`. One
generator, one home for invariant text. Not a second generator beside
`cycle-open`, and not a replacement that discards the cycle format.

**Migration scope.** What moves is `cycle-open`'s skeleton emission —
`render_directive` and the identity and document-set resolution feeding it.
Where its bundle emission, `--bundle` expansion, `--out` contract, and
`--allow-dirty` behaviour end up is a TRD question; that they keep working is
not, because the contract governing them is preserved whole.

**Mode scoping.** `bin/directive` has two modes with different obligations, so
every claim about the generator names its mode:

- **Cycle mode** replaces `bin/cycle-open` and preserves AC-CO-1 through
  AC-CO-12 (`docs/packages/package-a-spec.md` §3.6 and §8.2) intact, including
  their refusals (AC-CO-1, -2, -5, -6, -12) and their writes (AC-CO-1 and
  AC-CO-7, bounded by AC-CO-11). The cycle-mode skeleton carries AC-CO-3's
  structure *plus* the disposition slot and the source manifest, as an extension
  none of the twelve forbids. Nothing AC-CO-3 enumerates may be dropped,
  reordered, or altered.
- **General mode** is every other directive class.
- A claim naming no mode binds both.
- **Conflict rule.** A goal in this document that cannot be satisfied without
  breaking a preserved AC-CO criterion, or a decision that makes one binary's
  output fail the other's check, is a defect in this document — surfaced, not
  resolved by the implementer. It is raised as a blocking finding at the next
  gate review and resolved by a dictated disposition that states, in this
  document's text, which of the two moved and why.

### Scope split with the TRD

This document carries goals, journeys, risk posture, and the criteria decidable
at PRD level. Generator/lint interaction mechanics are routed to the TRD, each
with a named route and a PRD-level property the resolution must satisfy:

- the disposition label's lexical form — §8 Q9, which fixes the single-source
  property;
- the mechanism by which a generated skeleton holds G3's invariant — §8 Q10;
- any markdown sensitivity of M3's match beyond the fence exclusion — M3's row.

G11 routes the skeleton's marker syntax at its own site; G5 routes the
failing-path invocation point to Q2.

### Functional goals

#### `bin/directive` — the generator

- **G1 — Invariant text is read, never hardcoded.** Every invariant section the
  skeleton carries — sandbox constraints, stop conditions, the disposition
  prompt, verification steps, report format, claim labels — is read from
  committed governed text at generation time. A string constant in the tool
  holding text that also lives in a governed file is the defect this goal
  prevents.
- **G2 — The author writes only the middle.** The task-specific region and the
  disposition author region are the only regions the decision session composes
  freehand. AC-DT-18 fixes the count at two.
- **G3 — The working-tree disposition is a slot, not prose, and the slot is two
  regions.** Omitting it is visible rather than silent.
  - The **disposition prompt** is invariant (G1). It states that a disposition
    is required, names the two admitted forms, and states that the disposition
    is written as its own labelled statement. A prompt is not a labelled
    disposition statement; its naming of the forms is incidental mention and is
    outside M3's match.
  - The **disposition author region** is the author's. The generator emits the
    TRD-fixed label as the region's marker over an empty content slot; the
    author writes the content — the actual assignment or sole-tree declaration
    — and label plus content is the labelled statement the governed rule
    requires. The label is not governed text and G1 does not reach it: the
    governed rule delegates its form to tooling.

  **Generated-skeleton invariant.** The skeleton as emitted, in either mode,
  contains exactly one unfenced labelled disposition statement — the one over
  the empty content slot — whatever committed text its invariant regions carry
  or quote. This is what makes a faithfully filled skeleton pass M3 by
  construction. How the generator holds to it is §8 Q10; AC-DT-03 checks it.
- **G4 — The generator gates no directive content.** In general mode it refuses
  nothing. In cycle mode it carries the five precondition refusals it inherits.
  In neither mode does it refuse the content an author writes; refusal of a
  directive lives in `bin/check-directive`. Keeping the general mode ungated
  lets the generator be adopted before the lint is trusted.
- **G11 — The skeleton records its own sources and their extents, in the
  file.** The generator emits a source manifest: one entry per emitted region,
  in emission order, each naming the marker that begins the region and either
  the committed path it was read from or an explicit author-region marking —
  exactly one classification per entry. Every region, author regions included,
  begins with a marker, so the markers partition the whole file and each
  region's extent runs from its marker to the next. The generator-supplied
  share of a landed directive is computable from the file alone. Marker syntax
  is a TRD question. The manifest is an output of the generator and an input to
  nothing the lint does.

#### `bin/check-directive` — the lint

- **G5 — It runs inside the existing first act.** Write the directive file,
  lint it, commit, push. AC-DT-19 states the tool-side precondition. Where the
  invocation sits on the failing path is §8 Q2.
- **G6 — The required-element set derives from committed governed text.**
  Sources: Core's Vocabulary, Decision Layer rule 14,
  `skills/directive-authoring.md`, and `decisions/log.md`. A requirement the
  tool enforces and no governed file states is a defect in the tool. The
  label's lexical form is the one thing M3 does not read off governed text, and
  need not: the governed rule delegates it, so a TRD fixing one is discharging
  a delegation, not inventing a requirement.
- **G7 — Mechanically checkable elements only.** The lint checks properties
  decidable by inspecting the directive text and the repository. It makes no
  claim about properties requiring judgment.
- **G8 — Non-zero exit names what is missing**, and the governed text each
  requirement derives from.
- **G9 — The pass states its own bounds.** Exit 0 is accompanied by a statement
  of what was not checked. A silent pass is the failure mode that turns a narrow
  lint into a broad-sounding assurance (§7).
- **G10 — Two provenance labels.** The tools' own claims are labelled
  *observed* or *unknown*, and no other class — a subset of Core rule 6, on the
  precedent `specs/bin-land.md` §4 G6 sets. Text they quote or emit from
  committed sources is outside this.

#### The two element sets

**Mechanically checkable** — the lint's elements, each traced to its source:

| # | Element | Derived from |
| --- | --- | --- |
| M1 | A reviewed-ref pin is present and resolves to a commit | `skills/directive-authoring.md`, "Pin STOP conditions to the reviewed ref" |
| M2 | Each companion citation `<path> @ <sha>` names a path present at the reviewed ref and a SHA that resolves to a commit touching that path. Neither fullness nor lastness is checked (AC-DT-17) | Core Vocabulary, "Companion document" and "Directive file" |
| M3 | Exactly one labelled disposition statement is present outside fenced code blocks, and it carries exactly one of the two admitted forms: an exclusive assignment (a named directory plus the command creating it) or a literal sole-tree declaration. Unconditional; no parallelism test; no region extent. Zero such statements fails whatever else the file mentions. The label's lexical form is a TRD decision (§8 Q9); any markdown sensitivity beyond the fence exclusion is a TRD decision | `skills/directive-authoring.md`, first rule under "Writing the directive file" |
| M4 | The stop conditions are present: cannot-execute-as-written, and concurrent tree mutation | Core rules 11 and 15 |
| M5 | The first instruction is write-the-directive-file, commit, push, report the SHA. DEC-000160 fixes this for every directive class; no exemption | Core Vocabulary, "Execution block" |
| M6 | A report section is present and enumerates its required fields | Decision Layer rule 14 |
| M7 | The claim-label instruction is present | Core rule 6 |
| M8 | The filename, resolved to a repository-relative path from the root (AC-DT-19), matches exactly one of three patterns: `docs/cycles/<descriptor>-<timestamp>.md`, timestamp `YYYYMMDDThhmmss` with date and time both present, optionally `Z`-suffixed; `docs/cycles/cycle-<N>-directive.md`; or `docs/cycles/<SLUG>-directive.md`, `<SLUG>` any single-component basename with no character class. Membership is the whole claim: M8 does not check whether the pattern matched is the one this directive's mode should have produced | `skills/directive-authoring.md`, "Naming"; `docs/packages/package-a-spec.md` §3.6 AC-CO-1; Core rule 14 |

**Judgment-only** — governed rules that bind the author and stay out of the
lint's claims:

- "No blanket constraint may contradict an explicit instruction in the same
  file." Semantic contradiction is not mechanical.
- "Scope Do-not lists to the blast radius." Requires knowing the blast radius.
- "Carry dictated wording as a pointer unless the directive is itself the
  wording's origin." Requires knowing whether the directive is the origin.
- "A directive is self-contained." The lint cannot see the conversation.
- Whether the dictated content is correct or executable in the executor's
  environment. M3 checks that a disposition was *made*; it cannot check that it
  can be *carried out*. This effort demonstrated it: the cycle-1 directive's
  well-formed assignment to a sibling directory was denied by the sandbox's
  write allowlist, and M3 would have passed it.

### Non-functional goals

- **Performance**: no latency target. The lint adds no network round-trip
  beyond resolving M1 and M2 against the local object store.
- **Reliability**: a non-zero exit is a claim the lint found a missing element;
  exit 0 is a claim only about the checked set. Neither is a claim about
  directive quality. An element the lint cannot decide is reported unknown and
  exits non-zero. M3 is total by construction and never undecidable.
- **Scalability**: N/A. One directive per invocation.
- **Security**: neither tool invokes `gh`, touches a credential, writes to the
  remote, stages, or commits. The lint writes nothing. The generator in general
  mode writes its skeleton and manifest to stdout or a named output path and
  nothing else; in cycle mode it writes what AC-CO-1 and AC-CO-7 require,
  bounded by AC-CO-11. Threat model: the tools must not become a remote-write
  path, must never modify a document they did not create, and a lint on the
  first act must not be able to damage the tree it inspects (AC-DT-12).
- **Maintainability**: G0, G1, and G6. A governed rule that changes changes the
  tools' behaviour without a code edit.
- **Usability**: the generator's success condition is that the author writes
  less; the lint's is that its failure output is actionable without reading the
  tool's source.
- **Observability**: the lint prints its checked set, per-element result, and
  unchecked set on both exit paths. The manifest is the generator's
  observability surface and persists in the landed file.
- **Portability / Compatibility**: depends on `git` and a checkout of this
  repository. The cycle mode's output must remain acceptable to the
  reviewer-gated cycle format under DEC-000180's route/model/no-track rule.
- **Compliance**: N/A.

### Non-goals

- **Reviewing directives.** The lint checks presence, not quality. Whether a
  gated directive class eventually wants a reviewer role is a separate
  question.
- **Repairing a directive.** The lint reports; it never edits. Neither does the
  executor.
- **Judging executability.** Per the judgment-only set.
- **Retrofitting the existing corpus.** The lint governs directives written
  after adoption; historical directive files are not retrofitted, because
  renaming the existing corpus would break every citation by path that points
  into it.
- **Claiming `cycle-open`'s non-skeleton behaviour.** Per the migration scope.
- **Naming vocabulary.** Binary names are not methodology vocabulary; neither
  tool enters `LEXICON.md`.
- **Invoking `gh`.** Never.

## 5. User outcomes and measurement

- **The freehand surface shrinks.** Signal: the share of a landed directive's
  bytes in generator-supplied regions versus author-composed. Baseline: 100%
  author-composed for every class except the spec-review cycle, whose baseline
  is the small skeleton `bin/cycle-open` already supplies. Mechanism: G11's
  manifest, read from the landed file. Bound: the manifest records the skeleton
  as emitted; an author writing inside a generator-supplied region afterwards is
  not recorded.
- **Malformed directives are caught at the first act rather than mid-cycle.**
  Signal: lint failures at the first act versus executor stops on a missing
  element after work began. Baseline: at least one — the motivating incident.
  Mechanism: execution reports and retros.
- **Invariant text stops contradicting itself.** Signal: new contradictions
  between the invariant sections of directives landed after adoption — the set
  §4's no-retrofit non-goal scopes the lint to. Baseline: the one contradiction
  across nine files the research document recorded. Mechanism: manual review of
  the corpus. Bound: the first recount reads zero against zero by construction,
  the post-adoption set being empty at adoption, so an early zero is arithmetic
  and not evidence; the outcome is meaningful only once enough post-adoption
  directives exist for a contradiction to have had the opportunity to appear.

Lint pass rate is not a quality measure and is not tracked (§7).

## 6. Acceptance criteria

These criteria derive from §4, each concrete enough to derive a test case from.
The test substrate is fixture directives — well-formed, and each missing one
element — checked against a fixture repository, which makes the set testable
offline: no criterion here requires this repository's commit history to run.
AC-DT-15 and AC-DT-16 are the two exceptions, discharged against this
repository rather than a fixture one, and both offline.

- **AC-DT-01** — Changing the committed text of a source a skeleton section is
  read from changes that section in the next generated skeleton, with no edit to
  the generator.
- **AC-DT-02** — For every entry in the source manifest, no string literal in
  the generator's source reproduces a line of that entry's committed content,
  where reproduction means exactly equal after whitespace normalization (strip
  ends, collapse internal runs to one space). Excluded from the check: any line
  of the committed source consisting solely of whitespace and characters from
  the set `-` `=` `~` `` ` `` `#` `*` `_` `|` `>` `+`, read raw. The exclusion
  is a test-selection rule for this criterion, not a constraint on any governed
  file. Verifiable statically over the generator's source against its own
  manifest; independent of Q1.
- **AC-DT-03** — A generated skeleton, in either mode, contains: a prompt
  region whose text matches the committed source its manifest entry names, and
  which states that a disposition is required, names both admitted forms, and
  states the labelled-statement requirement; an author region beginning with
  the label its manifest entry names as marker, over a blank content slot; and,
  over the whole emitted file, exactly one unfenced labelled disposition
  statement (G3's invariant). The count assertion becomes executable when Q9
  fixes the label.
- **AC-DT-04** — In general mode the generator exits 0 for every invocation
  that produces a skeleton and has no refusal path. In both modes no text an
  author places in the task-specific region causes a non-zero exit, including
  text the lint would fail.
- **AC-DT-05** — The generator emits a source manifest naming, per emitted
  region, the marker that begins it and either the committed file it was read
  from or an author-region marking — exactly one per entry — as part of the
  skeleton written to the file. Every marker appears in the file exactly once,
  every region carries one, and taking each entry's extent from its marker to
  the next partitions the whole file with no overlap and no gap, yielding one
  generator-supplied share per skeleton.
- **AC-DT-06** — For each element M1–M8, a fixture directive missing exactly
  that element exits non-zero, naming the element and citing the governed text
  it derives from. The M3 fixtures are stated as shapes and become instantiable
  when Q9 fixes the label:
  - (i) one labelled statement, one admitted form — exit 0; one fixture per
    form, the sole-tree form included;
  - (ii) unlabelled prohibition only (the motivating incident) — non-zero;
  - (iii) one well-formed labelled statement plus, elsewhere, an unlabelled line
    instantiating an admitted form (e.g. a stop condition naming a directory
    and its `git worktree add`) — exit 0;
  - (iv) generated skeleton, content slot correctly filled — exit 0;
  - (v) generated skeleton, content slot blank — non-zero, on form-membership;
  - (vi) one unfenced labelled statement plus one or more fenced labelled
    statements (carried wording under the origin exception) — exit 0;
  - (vii) the only labelled statement is fenced — non-zero;
  - two unfenced labelled statements — non-zero; a single statement carrying
    neither form, or both — non-zero.
  For M8, eight fixtures — four passing, four failing. Passing: one
  `<descriptor>-<timestamp>.md`, one `cycle-<N>-directive.md`, one
  `<SLUG>-directive.md`, and one named from a subdirectory by relative path,
  which matches on the resolved path. Failing: `<descriptor>-YYYYMMDD.md`, a
  date with no time, because M8 requires the full `<date>T<time>` form; a name
  that is neither timestamped nor `-directive.md`-suffixed; and
  `docs/cycles/sub/nested-directive.md` and `docs/escaped-directive.md`, the two
  names `bin/cycle-open` was observed to emit that AC-CO-1 does not license. A
  fixture named by absolute path also matches on the resolved path. No fixture
  exercises a `<SLUG>` character boundary and none may: M8 carries no character
  class, so such a fixture would assert a requirement G6 forbids, and the
  passing slug fixture may therefore use any characters.
- **AC-DT-07** — A well-formed fixture directive carrying every element M1–M8
  exits 0.
- **AC-DT-08** — Exit 0 output includes the unchecked set — at minimum:
  executability of the working-tree disposition; route and model tier; every
  judgment-only rule in §4; and mode-appropriateness of the filename.
- **AC-DT-09** — A directive citing a companion by a SHA that resolves to a
  blob, a tag, or a commit not touching the cited path exits non-zero and names
  the citation. Fixtures are synthetic, in the fixture repository: blob hash
  (fail), tag (fail), commit touching a different path (fail), commit touching
  the path (pass).
- **AC-DT-10** — An element the lint cannot decide is reported unknown and
  exits non-zero; no undecidable element yields exit 0.
- **AC-DT-11** — Every claim either tool makes about its own findings carries
  *observed* or *unknown* and no other class. The claim-label instruction the
  skeleton carries, which names all four classes, is emitted text, not a claim
  by the generator.
- **AC-DT-12** — (a) Both tools, every mode: no code path invokes `gh`, writes
  to a remote, reads a credential, stages, commits, or modifies any file the
  invocation did not create. (b) The lint: no code path writes to the
  filesystem. (c) The generator's general mode: writes only the skeleton and
  manifest, to stdout or the named output path, and mutates nothing else. The
  cycle mode is bounded by AC-CO-11 instead, verified under AC-DT-15. All three
  verifiable statically; (c) also by running against a fixture repository and
  diffing the tree.
- **AC-DT-13** — The lint enforces no requirement absent from its cited
  governed sources. Every element M1–M8 satisfies this as written; the label's
  lexical form is a delegation the governed rule makes, not an unsourced
  requirement. M3's fence exclusion is this document's own and no governed file
  states it, but it is not an exception either: it narrows what the lint
  matches rather than adding a requirement the lint enforces, and this
  criterion is about enforcement.
- **AC-DT-14** — After migration, `bin/` contains exactly one directive-skeleton
  generator. The cycle skeleton is produced by `bin/directive` in cycle mode,
  carries Route and Model and no Track (DEC-000180), and `bin/cycle-open` no
  longer emits a skeleton of its own.
- **AC-DT-15** — `bin/tests/test_cycle_open.py` passes after the migration,
  with AC-CO-1 through AC-CO-12 satisfied and none retired, whichever binary
  each is invoked through. A red in that suite is a failed migration.
- **AC-DT-16** — Binds the decision session, not the implementer. The
  migration does not land until (a) `decisions/log.md` carries a new entry
  superseding DEC-000180 whose tooling consequence names `bin/directive`'s
  cycle mode, and (b) `OPEN-ITEMS.md`'s "`bin/cycle-open` and the retirement of
  Track" section names the cycle mode as the bearer of that obligation. A
  release gate reads this entry as waiting on a decision session, not as red.
- **AC-DT-17** — M2 is a resolvability-and-touch check and nothing more. Two
  synthetic fixtures, both exit 0 on M2: (a) a file cited by an abbreviated SHA
  of a touching commit; (b) a file cited by the full SHA of a content commit
  that is not the last commit touching the path. A lint failing either has been
  built to the metadata policy or AC-CO-4 rather than to M2.
- **AC-DT-18** — In a freshly generated skeleton, the manifest marks exactly
  one region as the task-specific author slot, exactly one as the disposition
  author region, and every other entry names a committed path. A property of
  the emitted skeleton, not the landed file.
- **AC-DT-19** — The lint takes the path of the directive file as it stands on
  disk as its only required argument; no check requires the file to be staged,
  committed, or pushed. The argument is resolved to a repository-relative path
  from the root before any element's check applies; it may be given relative to
  any working directory or as an absolute path inside the repository. A path
  resolving outside the repository is a refused invocation, exits non-zero, and
  names no element; which status, and whether refusals are distinguished from
  element findings, is Q6. Verifiable in a fixture repository in four
  invocations: uncommitted file, relative path from a subdirectory, absolute
  path, path outside the repository.

## 7. Risk tolerance

Both tools sit at the head of the directive path. The posture is conservative
about claims and permissive about work: neither tool gates an author's judgment
about content, and the lint fails loudly rather than passing quietly.

**The primary risk is the halo, not a false negative.** A lint that checks
eight mechanical elements at the head of every execution session will be read
as saying the directive is good. It says nothing of the kind, and the elements
it cannot check — self-containment, non-contradiction, correctness of the
dictated content, executability of the disposition — are the ones that produced
the failures on record. G9 and AC-DT-08 keep the claim narrow at the point of
use; §5 declines to measure quality by pass rate for the same reason.

**Accepted.**

- A directive that passes the lint and is still wrong. A bounded true claim is
  worth having; the alternative leaves the motivating incident unaddressed.
- A hand-written general-mode directive named `<slug>-directive.md` passes M8
  without a timestamp. Mode-appropriateness is not decidable from a filename.
  Mitigation: the generator makes the name correct by construction, and
  AC-DT-08 discloses the bound on every pass.
- A lint that stops an executor on a well-formed directive it mis-parses. A
  false stop costs one invocation and returns the question to a decision
  session. That is the cheap direction, and every other false positive here
  leans on it.
- Adoption of the generator ahead of the lint, or the reverse.
- **With a named cost:** folding `cycle-open` into `bin/directive` (G0) puts a
  working tool through a migration for a benefit that only pays off once a
  second class of directive uses it. The alternative accepted risk was two
  generators drifting; that one has no ceiling, and this one is bounded by the
  migration.
- A labelled disposition statement that is true in form and false in fact —
  the tree it names is not the tree the session will use.
- Two residuals of M3's fence handling:
  - A fenced labelled statement that is not carried wording but the author's
    own disposition, wrongly fenced. It is a statement formatted badly rather
    than a mention, but M3's fence exclusion does not match it, so the file
    carries zero unfenced labelled statements and fails though the author did
    state a disposition. False positive, surfaced loudly, corrected by the
    author.
  - A labelled statement carried outside a fence: a directive quoting another
    directive's labelled disposition in running text carries two unfenced
    labelled statements and exits non-zero, though it states exactly one
    disposition of its own. The governed rule does not draw that line either —
    it distinguishes the labelled statement from incidental mention of trees or
    commands, not from a labelled statement under carriage — so a lint drawing
    it would enforce a requirement no governed file states (G6).

**Not accepted.**

- A lint claim about a judgment-only property (G7).
- Invariant text or a required element hardcoded in a tool rather than read
  from committed text (G1, AC-DT-02). That failure recreates the drift the
  tools exist to remove, in a place with less visibility than prose.
- A refusal by either mode that turns on the *content* of a directive rather
  than on a precondition (G4), which would put refusal in two places and make
  the generator a second gate.
- Any write from the lint, of any kind, and any write from the generator beyond
  the skeleton and manifest — in cycle mode, beyond what AC-CO-1 and AC-CO-7
  require within AC-CO-11 (AC-DT-12). Either tool on the write path to the
  remote is not accepted alongside this, not in place of it.
- A requirement enforced that no governed file states (G6, AC-DT-13).
- A silent pass — an exit 0 that does not state its bounds (G9).

**Escalation.** A lint failure returns the directive to the decision session;
the executor never repairs it. Anything the lint cannot decide is reported
unknown and handed to the session, which stops and surfaces. Whether an
undecidable element is acceptable is Dave's judgment, never the tool's.

## 8. Open product questions

Closed questions are recorded in the cycle directives under `docs/cycles/`,
each with the ruling that closed it; only the open ones are carried here.

- **Q1 — Where the invariant text lives and how the generator resolves it.**
  Candidates: a section of an existing governed file addressed by heading, a
  new governed standing document, or a machine-readable block. No acceptance
  criterion depends on the answer. Resolved by: Dave, at the TRD stage.
- **Q2 — Lint sequencing relative to commit and push.** Whether a directive
  that fails the lint still lands for the audit trail. Landing preserves the
  record of what was handed over; not landing keeps a malformed directive from
  being citable by SHA. Resolved by: Dave.
- **Q4 — Whether the rest of these tools' requirements move into
  `skills/directive-authoring.md` or sit beneath it.** The mandatory
  working-tree rule already lives there. Resolved by: Dave.
- **Q5 — Whether route and model tier belong in the unchecked set only, or
  whether the generator should emit them into the file so they become
  checkable.** DEC-000180 requires them of the dispatch, not the file, so a
  file-scoped lint is coherent either way. Resolved by: Dave, at the TRD/AC
  stage.
- **Q6 — One exit status, or a blocking/advisory split.** AC-DT-10 currently
  fails every undecidable element, the strict reading of G7; a malformed
  companion citation and a missing stop condition are not obviously the same
  severity. Includes whether AC-DT-19's refusal is distinguished by status from
  an element finding. Resolved by: Dave, or a stated severity model at the
  TRD/AC stage.
- **Q9 — The disposition label's lexical form.** The fixed text M3 matches and
  `bin/directive` emits. Property the resolution must satisfy: the generator
  and the lint source the label from one committed definition. Three criteria
  wait on it — AC-DT-06's M3 fixtures as files, the single-source property, and
  AC-DT-03's count — all specified now, and all three read on AC-DT-16's model,
  as waiting on a decision rather than as red, until this question resolves.
  Resolved by: the TRD stage.
- **Q10 — The mechanism by which a generated skeleton holds G3's invariant.**
  Candidates: the prompt's committed source shows the label only inside a
  fenced block; that source is bounded not to show it; or the generator fences
  sourced text at emission. The third would put fence markers in the emitted
  region that the committed source does not carry, so it obliges a matching
  change to AC-DT-03's prompt-matches-source assertion. Each choice constrains
  Q1. Resolved by: the TRD stage, with Q1.
