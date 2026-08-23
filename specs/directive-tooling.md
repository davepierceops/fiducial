---
status: draft
last-reviewed: null
audience: [all-roles, human]
---

# PRD: directive tooling — `bin/directive` and `bin/check-directive`

This is the PRD in the spec spine for two tools that together gate the directive
artifact class. The TRD and the acceptance criteria derived from this document
follow at the TRD/AC stage; §6 states the criteria at the level a PRD carries
them.

Its content is dictated by Dave in the decision sessions that directed this
authorship. The directive file
`docs/cycles/directive-tooling-spec-20260823T194242Z.md` @ `c5398a42` is the
origin of the cycle-1 wording, and
`docs/cycles/directive-tooling-spec-2-20260823T195803Z.md` @ `d5a82172` is the
origin of the cycle-2 dispositions this revision carries. This document does not
restate either as if it were derived from somewhere else. Assertions about this
repository carry a provenance class: *observed*, *inferred*, *told*, *unknown*.

## 1. Problem and intent

**Dictated problem statement** (*told* — the cycle-1 directive is its origin):
directives are the only ungated load-bearing artifact class in this methodology.
Specs get the Spec Reviewer, governed documents get the Context Quality Reviewer,
code gets the red-gate; directives ship freehand from a decision session to an
executor. Freehand composition has an irreducible error rate that worsens with
accumulated context; a decision session late in a long conversation is a degraded
author. The countermeasure is structural, not exhortative: shrink the freehand
surface, gate the remainder.

The gate asymmetry is *observed* in committed text, and each half checks out:

- Specs. `roles/spec-reviewer-agent.md` @ `ed88dcde` states its gate review "is a
  **hard gate**" and that Dave does not agree a PRD, a TRD, or their acceptance
  criteria without a sign-off.
- Governed documents. `roles/context-quality-reviewer.md` scopes itself to "every
  file frontmatter enforcement reaches — the in-scope set enumerated in the
  document metadata policy's Scope section," with nothing excluded from it.
- Code. `operating-model.md` line 137: "The red-gate at step 4 is mandatory."
- Directives. `policies/document-metadata-policy.md` @ `a06460a9` enumerates the
  frontmatter in-scope set, and `docs/cycles/**` does not appear in it. No role
  document names directives as its review scope. So the absence is structural,
  not an oversight of enforcement: nothing is configured to reach them.

The absence of a *gate* is not the absence of *tooling*. `bin/cycle-open` already
generates a directive skeleton for one directive class (*observed* — its module
docstring reads "Open a spec-review cycle: directive skeleton + reviewed-revision
bundle," and its `render_directive` function at `bin/cycle-open:115` emits a
heading, a date, a `Documents in scope` list of `path @ sha` pairs, and three
placeholder sections). §4 states what `bin/directive` is relative to it.

The cost of freehand authorship is already measured, though for a neighbouring
purpose. `docs/research/gh-write-friction-20260823T184149Z.md` @ `49bd6ff4`
records that across the 90 directive files in `docs/cycles/`, sentences carrying
write-path vocabulary are 16.5% of sentences and 21.8% of characters; that in the
six most recent `pass2` directives write mechanics run 13.9% to 43.3% of each
file; and that eight committed directives instruct one merge mechanism while the
most recent instructs its opposite, with neither superseding the other in any
governed document (*observed*, per that document). Those figures describe the
invariant text this effort proposes to stop hand-writing.

**Dictated motivating incident, which this spec must state and must prevent
recurring** (*told*): a parallel directive stated a working-tree prohibition
instead of an assignment; `skills/directive-authoring.md` requires an assignment —
a named directory plus the command creating it (e.g.
`git worktree add ../fiducial-pass2 origin/main`). The executor stopped correctly;
the omission class is the target.

One qualification, *observed*, that the tool design must respect, and its
resolution. The committed sentence in `skills/directive-authoring.md` @ `27ca4560`
reads: "Two sessions sharing a tree mutate each other's preconditions. Prefer not
splitting; where unavoidable, state the tree assignment in each directive." It
requires the assignment to be *stated*, it does not in that sentence require the
command that creates the tree, and it conditions the requirement on splitting. The
dictated characterization is therefore stronger than the committed text it cites,
in both dimensions.

**Dictated disposition** (*told* — the cycle-2 directive is its origin, and it
closes what §8 Q3 and Q7 previously carried): every directive states its
working-tree disposition explicitly — either an **exclusive assignment** (a named
directory plus the command creating it) or a literal **sole-tree declaration**.
The requirement is unconditional; there is no parallel/sole-tree distinction for
the lint to draw, because both branches are stated dispositions and one of them is
always required.

That disposition creates one prerequisite, stated here rather than deferred
(*inferred* from §4 G6). G6 forbids the lint from enforcing a requirement no
governed file states. `skills/directive-authoring.md` as committed states the
weaker, conditional rule. So M3 is enforceable only once that skill is amended to
state the unconditional two-branch rule. The amendment is a prerequisite of the
lint, not of this PRD, and it is out of this document's change scope; §8 Q4 is
where the sequencing sits.

**Purpose** (*told* — dictated). Two tools, together: `bin/directive` shrinks the
freehand surface by emitting the invariant text from committed sources, and
`bin/check-directive` gates what remains by failing an executor's first act on a
directive missing a required element.

## 2. Users and use cases

**Primary actor — the decision session**, authoring a directive. It runs
`bin/directive`, receives a skeleton whose invariant sections are already filled
from committed repo text, and writes only the task-specific middle. Where the
directive is a reviewer-gated spec-review cycle, it runs the same tool in the mode
that replaces today's `bin/cycle-open` (§4). It is the actor whose error rate the
problem statement names, and it is *inferred* that it is least able to self-check,
because the degradation the problem statement describes is degradation of exactly
the faculty a self-check would use.

**Primary actor — the execution session**, receiving a directive. It already
writes the directive file, commits, and pushes as its first act (*observed* —
`docs/global-context/core.md` @ `17f75612`, Vocabulary, "Execution block": "Its
first instruction is to write the directive to a file, commit, push, and report
the SHA."; governed by `decisions/log.md` DEC-000160, which fixes that first act
"to every directive class, reviewer-gated cycle directives included"). It runs
`bin/check-directive` inside that act and stops before any work if the lint exits
non-zero.

**Secondary actor — Dave.** Consumes a lint failure as a signal that a directive
he authored is malformed, before an executor has spent a cycle discovering it. He
does not run either tool on the write path.

**Use cases.**

- Generate a directive skeleton whose invariant text is current with the
  repository rather than with the author's memory of it.
- Fail a malformed directive at the executor's first act, at a cost of one
  invocation rather than one cycle.
- Establish, mechanically, which required elements a directive carries — and
  state, equally mechanically, which properties were not checked.

## 3. User journeys

Top K = 3.

### J1 — author a directive from the skeleton

- **Actor**: decision session.
- **Trigger**: Dave directs work that needs an execution session.
- **Steps**: invokes `bin/directive`; receives a skeleton carrying the sandbox
  constraints, stop conditions, a working-tree disposition slot, the verification
  steps, the report format, and the claim-label instruction, each read from
  committed repo text at generation time; fills the task-specific middle and the
  disposition slot; hands the directive to an execution session.
- **Expected outcome**: a directive whose invariant text matches the repository's
  current committed text, with the author's freehand contribution confined to the
  middle.

### J2 — the executor's first act clears the lint

- **Actor**: execution session.
- **Trigger**: the session's first act under a directive.
- **Steps**: writes the directive file, runs `bin/check-directive` against it,
  and — on exit 0 — commits and pushes as it does today.
- **Expected outcome**: exit 0, plus a statement of which elements were checked
  and which properties were not, so the pass is not read as broader than it is.

### J3 — a directive missing a required element

- **Actor**: execution session.
- **Trigger**: `bin/check-directive` exits non-zero at the first act.
- **Steps**: the session stops and surfaces, naming the missing elements and the
  governed text each requirement derives from. It does not repair the directive,
  does not infer the author's intent, and does not begin the work.
- **Expected outcome**: the cycle costs one invocation instead of one execution.
  The missing element goes back to the decision session, which is the only place
  it can be supplied. This is the journey the motivating incident would have
  taken: the directive in that incident stated a prohibition and no disposition of
  either admitted form, which M3 — unconditional, and mechanically checkable as a
  presence test over two named forms — fails.

## 4. Goals and non-goals

### Relationship to `bin/cycle-open`

**G0 — one generator.** `bin/cycle-open` becomes a **mode** of `bin/directive`
(*told* — dictated, cycle-2 directive). One generator, one home for invariant
text. This spec licenses that implementation and no other: not a second generator
built beside `cycle-open`, and not a replacement that discards the cycle format.

**Migration scope**, stated so a TRD does not have to guess and does not claim
more than this PRD does: what moves is `cycle-open`'s **skeleton emission** — the
behaviour of `render_directive` at `bin/cycle-open:115` and the identity and
document-set resolution feeding it. Nothing else is claimed at PRD level. In
particular this document makes no claim about `cycle-open`'s bundle emission
(`write_bundle`), its `--bundle` context-set expansion, its `--out` directory
contract, or its `--allow-dirty` behaviour; whether those travel with the mode,
stay where they are, or split is a TRD question.

Two committed decisions bind the cycle mode and are carried, not re-decided
(*observed*, `decisions/log.md`):

- **DEC-000180** — a dispatch states three requirements, all three every time:
  route, model, and the execution block; track is retired. Its stated consequence
  for tooling is that `bin/cycle-open` "emits Route and Model and no Track." That
  obligation transfers to the cycle mode of `bin/directive`.
- **DEC-000110** — fixed route and model by class for reviewer-gated cycle
  directives. It **does not govern**: DEC-000150 superseded it, and DEC-000180
  superseded DEC-000150. It is cited here only to record that the class exemption
  a reader may remember is dead, and that the live rule is DEC-000180's
  all-three-every-time with *fresh* and *Opus 5* as stated-and-overridable class
  defaults.

`cycle-open`'s existing docstring principle — "Every SHA is the full id of the
last commit touching the path, read from git — never invented, never abbreviated"
— is *observed* to be the same principle G1 states for invariant text and M2
states for citations. The generalization inherits it rather than introducing it.

### Functional goals

#### `bin/directive` — the generator

- **G1 — Invariant text is read, never hardcoded.** Every invariant section the
  skeleton carries — sandbox constraints, stop conditions, working-tree
  disposition slot, verification steps, report format, claim labels — is read from
  committed repo text at generation time (*told* — dictated). A string constant
  in the tool holding text that also lives in a governed file is the defect this
  goal exists to prevent; it recreates, one layer down, the drift the problem
  statement describes.
- **G2 — The author writes only the middle.** The skeleton's task-specific region
  is the only region the decision session composes freehand (*told* — dictated).
- **G3 — The working-tree disposition is a slot, not prose.** It is emitted as a
  named, empty, structurally-present field admitting exactly the two forms §1
  names, so that omitting it is visible rather than silent. This is the goal that
  addresses the motivating incident directly: an omission the author cannot see is
  the failure mode, and a slot makes the omission a blank rather than an absence.
- **G4 — The generator gates nothing.** It refuses no directive and blocks no
  author. Its whole contribution is to make the invariant text correct by
  construction; `bin/check-directive` is where refusal lives. Keeping generation
  ungated is what allows the generator to be adopted before the lint is trusted.
- **G11 — The skeleton records its own sources, in the file.** The generator emits,
  as part of the skeleton it writes, a **source manifest**: for each invariant
  section, the committed path it was read from. The manifest is part of the
  directive the executor lands, not a side channel to the author's terminal. Two
  things depend on it that nothing else supplies: AC-DT-02's static check needs a
  declared set of sources to range over, and §5's first measurement needs the
  generator-supplied region of a landed directive to be identifiable from the
  committed file alone.

#### `bin/check-directive` — the lint

- **G5 — It runs inside the existing first act.** Write the directive file, lint
  it, commit, push (*told* — dictated; the act itself is DEC-000160's). The lint
  adds no new step to the executor's sequence; it adds a condition to a step that
  already exists.
- **G6 — The required-element set derives from committed governed text.** Its
  sources are `docs/global-context/core.md`'s Vocabulary,
  `docs/global-context/decision-layer.md` rule 14, `skills/directive-authoring.md`,
  and `decisions/log.md` (*told* — dictated for the first three; the decision log
  is added this cycle per the cycle-2 directive's B3). No requirement is invented
  in the tool. A requirement the tool enforces and no governed file states is a
  defect in the tool, not a stricter tool. §1 records the one place this bites
  today: M3's unconditional two-branch rule is not yet in
  `skills/directive-authoring.md`, and enforcing it before the amendment lands
  would violate this goal.
- **G7 — Mechanically checkable elements only.** The lint checks properties
  decidable by inspecting the directive text and the repository. It makes no
  claim about properties requiring judgment, and its output does not imply one.
  The two sets are enumerated below; keeping the judgment set out of the lint's
  claims is a goal, not a limitation to be worked around later.
- **G8 — Non-zero exit names what is missing.** A directive missing a required
  element exits non-zero, and the output names each missing element and the
  governed text the requirement derives from (*told* — dictated for the exit
  status; the citation requirement is *inferred* from G6, since a requirement
  that cannot name its source cannot be audited against G6).
- **G9 — The pass states its own bounds.** Exit 0 is accompanied by a statement
  of what was not checked. A silent pass is the failure mode that turns a narrow
  lint into a broad-sounding assurance; §7 names this as the primary risk.
- **G10 — Two provenance labels.** The lint's own claims are labelled *observed*
  or *unknown*, and no other class. A tool observes a fact or fails to; it is
  never in a position to infer or to be told. This is a subset of Core rule 6's
  four classes, not a redefinition of them, and follows the precedent
  `specs/bin-land.md` @ `87ae153a` §4 G6 sets. It constrains what the tools assert;
  it does not constrain text they quote or emit from committed sources.

#### The two element sets

**Mechanically checkable** — candidates for the lint, each traced to its source:

| # | Element | Derived from | Decision qualification |
| --- | --- | --- | --- |
| M1 | A reviewed-ref pin is present and resolves to a commit | `skills/directive-authoring.md`, "Pin STOP conditions to the reviewed ref" | none |
| M2 | Each companion citation `<path> @ <sha>` names a path present at the reviewed ref, and a SHA that resolves to a **commit touching that path** | Core Vocabulary, "Companion document ... Cited with its own path and SHA" and "Directive file ... thereafter cited by path and the SHA of the commit that landed it"; `policies/document-metadata-policy.md`, "The version of a document at reference time is the SHA of the last commit touching the file" | none |
| M3 | A working-tree disposition is present, in **exactly one** of two forms: an exclusive assignment (a named directory plus the command creating it), or a literal sole-tree declaration. Unconditional — every directive, no parallelism test | The cycle-2 directive's B2 disposition, which strengthens `skills/directive-authoring.md`'s "state the tree assignment in each directive" — see §1's prerequisite | not enforceable until `skills/directive-authoring.md` states the unconditional rule (G6) |
| M4 | The stop conditions are present: cannot-execute-as-written, and concurrent tree mutation | Core rules 11 and 15 | none |
| M5 | The first instruction is write-the-directive-file, commit, push, report the SHA | Core Vocabulary, "Execution block" | DEC-000160 fixes this for **every** directive class, so no class exemption exists for the lint to carry |
| M6 | A report section is present and enumerates its required fields | Decision Layer rule 14, "Write it so the returned report is triageable by the next decision session" | none |
| M7 | The claim-label instruction is present | Core rule 6 | none |
| M8 | The directive filename conforms to `docs/cycles/<descriptor>-<timestamp>.md`, timestamp in ISO 8601 basic | `skills/directive-authoring.md`, "Naming"; Core rule 14 | none |

No element in this table covers route or model tier. That is deliberate and is
the answer §8 Q5 now carries: Core's Vocabulary distinguishes the **directive**
(the package — "one line stating route ... and model tier, then the execution
block as a paste block. All three stated every time") from the **directive file**
(the markdown file the executor writes and commits). DEC-000180 requires all three
of the package every time; two of the three never reach the file. A file-scoped
lint therefore cannot see them, and their absence from a directive file is not a
defect the lint may report (*observed*, both sources).

M2 is *observed* to catch a real defect, in this effort's own directives. The
cycle-1 directive cited its sandbox-constraint provenance as
`docs/cycles/pass2-held-fix-20260823T180753Z.md` @ `9f5f4c9d8ce06d1c5489bf3b5a3248b5386fe650`,
which is the **blob** hash of the file's content at `origin/main`, not a commit:
`git cat-file -t` returns `blob`, and the only commit touching that path is
`b9444973`. The citation resolved to the right bytes and to no commit, so a reader
following the repository's own versioning rule found nothing. The cycle-2 directive
cites the same provenance as `@ commit b9444973` (*observed*), which M2 passes —
the defect and its correction are both in the record, one cycle apart, and M2 is
what would have caught the first without the second cycle.

**Judgment-only** — governed rules that bind the author and must stay out of the
lint's claims, each *observed* in the cited text:

- "No blanket constraint may contradict an explicit instruction in the same file"
  (`skills/directive-authoring.md`). Detecting semantic contradiction is not
  mechanical.
- "Scope Do-not lists to the blast radius" (same). Requires knowing the blast
  radius.
- "Carry dictated wording as a pointer ... unless the directive is itself the
  wording's origin" (same). Requires knowing whether the directive is the origin.
- "A directive is self-contained. The executor needs the block and the
  repository, nothing from this conversation" (Decision Layer rule 14). The lint
  cannot see the conversation, so it cannot check the property that references it.
- Whether the dictated content is correct, or executable in the executor's
  environment.

That last one is not a limitation to be engineered away, and this effort
demonstrates why twice. The cycle-1 directive as first issued assigned the working
tree `../fiducial-directive-tooling` — a present, well-formed, correctly-shaped
assignment that M3 passes in both dimensions. It was **not executable**: the
sandbox restricts writes to an allowlist carrying the clone root and `$TMPDIR` and
not the clone's parent, so `git worktree add` exited 128 with "could not create
leading directories," and a bare `mkdir` of the same path was denied while
`/Users/dave/code` stood `drwxr-xr-x dave:staff` (*observed*, cycle 1; the probes
were removed and the failed add left no entry in `.git/worktrees`). The cycle-2
directive carries the corrected constraint — worktrees under `$TMPDIR` — as told,
and its assignment executed (*observed*, this cycle). Executability is a property
of the executor's sandbox, discoverable only at execution and only after the
constraint has been learned once. The lint checks that a disposition was *made*;
it cannot check that it can be *carried out*, and G9 requires it to say so.

### Non-functional goals

- **Performance**: no latency target. The negative constraint is what binds: the
  lint runs inside an act the executor already performs, and adds no network
  round-trip beyond what resolving M1 and M2 against the local object store
  requires (*inferred* from G5).
- **Reliability**: a non-zero exit is a claim the lint found a missing element,
  and exit 0 is a claim only about the checked set. Neither is a claim about
  directive quality. A lint that cannot decide an element reports it unknown and
  exits non-zero, rather than passing it.
- **Scalability**: N/A. One directive per invocation; no growth dimension.
- **Security**: neither tool invokes `gh`, touches a credential, writes to the
  remote, or mutates the working tree. The generator writes its skeleton and its
  source manifest to stdout or to a named output path and touches nothing else;
  the lint reads. Threat model: the tools must not become a write path, and a lint
  on the first act must not be able to damage the tree it is inspecting.
- **Maintainability**: G1 and G6 are the maintainability requirements. Invariant
  text and required elements both live in committed governed files; the tools
  resolve them. A governed rule that changes changes the tools' behaviour without
  a code edit, and a tool that hardcodes either is the drift this spec targets. G0
  is the third: two generators would drift from each other, which is the same
  defect between files rather than within one.
- **Usability**: the generator's reader is Dave in a decision session; the lint's
  reader is an execution session. The generator's success condition is that the
  author writes less; the lint's is that its failure output is actionable without
  reading the tool's source.
- **Observability**: the lint prints its checked set, its result per element, and
  its unchecked set, on both exit paths. The generator's source manifest (G11) is
  the generator's observability surface, and it persists into the landed file
  rather than expiring with the terminal session.
- **Portability / Compatibility**: depends on `git` and a checkout of this
  repository. Neither tool asserts what the sandbox permits. Compatibility has one
  named obligation from G0: the cycle mode's output must remain acceptable to the
  reviewer-gated cycle format, under DEC-000180's route/model/no-track rule.
- **Compliance**: N/A. No regulatory, legal, or data-residency dimension.

### Non-goals

- **Reviewing directives.** Neither tool is a reviewer role, and the lint is not
  the directive-class equivalent of the Spec Reviewer. It checks presence, not
  quality. Whether a gated directive class eventually wants a reviewer role is a
  separate question this spec does not open.
- **Repairing a directive.** The lint reports; it never edits. The executor does
  not repair either — a missing element goes back to the decision session, which
  is the only place the intent exists.
- **Judging executability.** Per §4, above.
- **Claiming `cycle-open`'s non-skeleton behaviour.** Per the migration scope
  above.
- **Naming vocabulary.** Neither `directive` nor `check-directive` enters
  `LEXICON.md`. Per the dictated naming disposition (*told*; Dave, in the
  decision session that directed the cycle-1 authorship): binary names are not
  methodology vocabulary, and no LEXICON entry is created for a binary name. This
  document creates none, and edits `LEXICON.md` not at all.

  *Sequencing note* (*told* — cycle-2 directive, O2): the durable record of that
  disposition lands with the **bin-land cycle 3** directive, not here. Until it
  does, this spec and the cycle-1 directive file are the only committed statements
  of it, and `specs/bin-land.md` @ `87ae153a` §8 Q2 — "The binary name `land` is
  provisional, pending Dave's `LEXICON.md` check" — remains live and unconformed.
  `specs/bin-land.md` is outside this cycle's change scope and was not edited.
- **Invoking `gh`.** Never, for anything.

## 5. User outcomes and measurement

- **The freehand surface shrinks.** Signal: the share of a landed directive's
  bytes falling in sections the generator supplied, versus the share the author
  composed. Baseline: for every directive class except the reviewer-gated
  spec-review cycle, 100% author-composed today (*observed* — `bin/` holds
  `aimeta`, `bundle`, `bundle-methodology`, `check-frontmatter`, `cycle-open`,
  `flip-agreed`, `install-hooks`, `migrate-frontmatter`, `tests`, and only
  `cycle-open` emits a directive skeleton). For the cycle class the baseline is
  what `render_directive` already supplies: a heading, a date, a
  `Documents in scope` list, and three section headers with placeholders
  (*observed*, `bin/cycle-open:115`) — small, but not zero, and the measurement
  starts from it rather than from nothing.
  **Attribution mechanism**: G11's source manifest, carried in the landed file.
  The manifest names each generator-supplied section, so the split is recoverable
  from the committed artifact with no tooling beyond reading it. Its bound, stated
  because the signal would otherwise be read as tighter than it is: the author may
  edit inside a generator-supplied section, and the manifest does not record that.
  The signal therefore measures the *region the generator supplied*, not the bytes
  that survived untouched.
  Sizing context: write mechanics run 13.9% to 43.3% of each recent `pass2`
  directive (*observed*, per the research findings). That those write-mechanic
  sentences are the same region a generator would fill is this spec's own reading
  of that measurement (*inferred*), not a finding of the research document.
- **Malformed directives are caught at the first act rather than mid-cycle.**
  Signal: lint failures at the first act, and — the number that matters —
  execution sessions that stop and surface on a directive defect *after* work has
  begun. Baseline for the second: at least one, the motivating incident (*told*).
  Mechanism: execution reports and retros.
- **Invariant text stops contradicting itself.** Signal: contradictory
  instructions across concurrently-live directives. Baseline: the merge-mechanism
  contradiction across eight directives and their successor (*observed*, per the
  research findings). Mechanism: recount over directives authored after adoption.

Not measured, and stated so the list is not read as exhaustive: whether directive
*quality* improves in the judgment dimensions of §4's second table. The lint makes
no claim there, so no signal it produces would be evidence for it, and treating
lint pass rate as a quality metric is the specific misreading §7 names.

## 6. Acceptance criteria

Derived from §4. Each is concrete enough to derive a test case from. The test
substrate is expected to be fixture directives — well-formed and each missing one
element — checked against a fixture repository, which makes the whole set testable
offline (*inferred*).

- **AC-DT-01** — Changing the committed text of a source a skeleton section is
  read from changes that section in the next generated skeleton, with no edit to
  the generator. Verifiable by mutating a fixture source and regenerating.
- **AC-DT-02** — For every entry in the source manifest the generator emits
  (G11, AC-DT-05), no string literal in the generator's source reproduces a line
  of that entry's committed content. Verifiable statically over the source against
  the manifest the generator itself declares, which makes the criterion decidable
  without knowing where the invariant text lives — so it does not depend on Q1.
  Q1's resolution changes which paths the manifest names; it does not change what
  this criterion asserts or how it is checked.
- **AC-DT-03** — A generated skeleton contains a working-tree disposition slot
  that is present and empty, names both admitted forms, and is distinguishable
  from a slot that has been filled.
- **AC-DT-04** — The generator exits 0 for every invocation that produces a
  skeleton, and rejects no content. It has no refusal path.
- **AC-DT-05** — The generator emits a source manifest naming, per invariant
  section, the committed file it was read from, and the manifest is part of the
  skeleton written to the directive file rather than terminal-only output.
- **AC-DT-06** — For each element in the mechanically-checkable table M1–M8, a
  fixture directive missing exactly that element causes a non-zero exit, and the
  output names that element and cites the governed text it derives from. For M3
  the check is an **unconditional presence test** over two named forms, with no
  parallelism precondition: a fixture with neither an exclusive assignment nor a
  sole-tree declaration exits non-zero, a fixture carrying both exits non-zero,
  and each of the two single-form fixtures exits 0 on that element. The fixture
  set includes a sole-tree directive, which under this criterion must pass M3
  rather than be exempt from it.
- **AC-DT-07** — A well-formed fixture directive carrying every element M1–M8
  exits 0.
- **AC-DT-08** — Exit 0 output includes the unchecked set — at minimum, that
  executability of the working-tree disposition, route and model tier (which do
  not reach the directive file, per §4), and every judgment-only rule in §4 were
  not checked.
- **AC-DT-09** — A directive citing a companion by a SHA that resolves to a blob,
  a tag, or a commit that does not touch the cited path exits non-zero and names
  the citation. The historical citation in
  `docs/cycles/directive-tooling-spec-20260823T194242Z.md` @ `c5398a42` — which
  cites `docs/cycles/pass2-held-fix-20260823T180753Z.md` by its blob hash
  `9f5f4c9d` — is a fixture case for the blob branch, and the corrected citation
  in `docs/cycles/directive-tooling-spec-2-20260823T195803Z.md` @ `d5a82172` is
  the matching passing fixture.
- **AC-DT-10** — An element the lint cannot decide is reported unknown and exits
  non-zero; no undecidable element yields exit 0.
- **AC-DT-11** — Every claim either tool makes about its own findings — the
  lint's per-element results and its unchecked-set statement, the generator's
  source manifest — carries the label *observed* or *unknown*, and no other class.
  Text the tools quote or emit from committed sources is outside this criterion.
  In particular, the claim-label instruction the skeleton carries is an
  **instruction to the executor** to label its own claims, and a faithful
  rendering of Core rule 6 necessarily names all four classes; that rendering is
  not a claim by the generator and does not violate this criterion.
- **AC-DT-12** — No code path in either tool invokes `gh`, writes to a remote,
  mutates the working tree or the index, or reads a credential. Verifiable
  statically over the source.
- **AC-DT-13** — The lint enforces no requirement absent from its cited governed
  sources. Verifiable by review of the requirement table against those files, and
  mechanically to the extent each requirement carries the citation AC-DT-06
  demands. M3 is the standing case: until `skills/directive-authoring.md` states
  the unconditional two-branch rule, a lint enforcing M3 fails this criterion.
- **AC-DT-14** — After migration, `bin/` contains exactly one directive-skeleton
  generator. The reviewer-gated cycle skeleton is produced by `bin/directive` in
  its cycle mode, it carries Route and Model and no Track (DEC-000180), and
  `bin/cycle-open` no longer emits a skeleton of its own. Verifiable by generating
  a cycle skeleton through the new path and by static inspection of `bin/`.

## 7. Risk tolerance

Both tools sit at the head of the directive path, so the posture is conservative
about claims and permissive about work: neither tool blocks an author, and the
lint fails loudly rather than passing quietly.

**The primary risk is the halo, not a false negative.** A lint that checks eight
mechanical elements, run at the head of every execution session, will be read as
saying the directive is good. It says nothing of the kind, and the elements it
cannot check — self-containment, non-contradiction, correctness of the dictated
content, executability of the disposition — are precisely the ones that produced
the failures on record. G9 and AC-DT-08 exist to keep the claim narrow at the
point of use, and §5 declines to measure quality by lint pass rate for the same
reason.

**Accepted.** A directive that passes the lint and is still wrong. The lint's
claim is bounded and stated; a bounded true claim is worth having, and the
alternative — declining to check the mechanical elements because the judgment
ones are unreachable — leaves the motivating incident unaddressed.

**Accepted.** A lint that stops an executor on a well-formed directive it
mis-parses. A false stop costs one invocation and returns the question to a
decision session. That is the cheap direction.

**Accepted.** Adoption of the generator ahead of the lint, or the reverse. They
are independently useful, and G4 keeps the generator ungated so it can go first.

**Accepted, with a named cost.** Folding `cycle-open` into `bin/directive` (G0)
puts a working tool through a migration for a benefit — one home for invariant
text — that only pays off once the second class of directive uses it. The
alternative accepted risk was two generators drifting; that one has no ceiling,
and this one is bounded by the migration.

**Not accepted.** Any lint claim about a judgment-only property. Any exit 0 that
does not state its bounds. Any invariant text or required element hardcoded in a
tool rather than read from committed text — that failure recreates the drift the
tools exist to remove, in a place with less visibility than prose. Any write, of
any kind, from either tool. Any lint enforcement of M3 before the governed text
states it (G6, AC-DT-13).

**Escalation.** A lint failure returns the directive to the decision session; the
executor never repairs it. Anything the lint cannot decide is reported unknown and
handed to the session, which stops and surfaces. Whether an undecidable element is
acceptable is Dave's judgment, never the tool's.

## 8. Open product questions

- **Q1 (dictated; open, and this stage is the right place for it).** Where the
  invariant text lives, and how the generator resolves it. The candidates differ
  materially: a section of an existing governed file addressed by heading, a new
  governed standing document, or a machine-readable block. The research findings
  rank a standing write-path document first among its options and call it a
  precondition for the other options being citable (*observed*, per that
  document), so this question overlaps a decision already in flight. AC-DT-02 was
  restated this cycle so that no acceptance criterion depends on the answer.
  Resolved by: Dave, at the TRD stage.
- **Q2 (dictated).** Lint sequencing relative to commit and push — specifically,
  whether a failing directive still lands for the audit trail. The tension is
  real in both directions: landing it preserves the record of what was actually
  handed over, and not landing it keeps a known-malformed directive from being
  citable by SHA. Resolved by: Dave.
- **Q3 — closed** (cycle 2, by the B2 disposition). How the lint distinguishes a
  parallel directive from a sole-tree one. It does not: M3 is unconditional, and
  both cases are stated dispositions. No parallelism marker is needed in the
  directive text or the skeleton.
- **Q4 (dictated; widened this cycle).** Whether these tools change the text of
  `skills/directive-authoring.md` or sit beneath it. §1 makes one half of this
  concrete and no longer optional: M3's unconditional two-branch rule must be
  stated in that skill before the lint may enforce it (G6), so at least one
  amendment is a prerequisite rather than a preference. What remains open is the
  scope of the rest, and the sequencing against it. Resolved by: Dave.
- **Q5 — narrowed to near-closure** (cycle 2, against `decisions/log.md` and Core
  Vocabulary). Whether the directive **file** is the right unit for the lint,
  given that a directive package is route + model + execution block. Core's
  Vocabulary defines the directive file as a distinct artifact — the markdown file
  the executor writes, commits, and cites — and DEC-000180 requires route and model
  of the *dispatch*, not of the file. So a file-scoped lint is coherent, and a
  directive file carrying neither route nor model tier is not thereby defective.
  What remains: whether route and model belong in AC-DT-08's unchecked set only
  (the current answer), or whether the generator should additionally emit them into
  the file so they become checkable. Resolved by: Dave, at the TRD/AC stage.
- **Q6 (raised by the author).** Whether the lint has one exit status or a
  blocking/advisory split. AC-DT-10 currently makes every undecidable element
  fail, which is the strict reading of G7; a directive with a malformed companion
  citation and one with no stop conditions are not obviously the same severity.
  Resolved by: Dave, or a stated severity model at the TRD/AC stage.
- **Q7 — closed** (cycle 2, by the B2 disposition). Whether the working-tree
  requirement is "a named directory" or "a named directory plus the command
  creating it." It is the latter, for the assignment branch, with a literal
  sole-tree declaration as the only alternative. M3 is now writable as a test
  (AC-DT-06). The residual obligation this creates — amending
  `skills/directive-authoring.md` so G6 is satisfied — is carried in §1 and Q4,
  not here.
