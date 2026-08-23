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

Its content is dictated by Dave in the decision session that directed this
authorship; the directive file `docs/cycles/directive-tooling-spec-20260823T194242Z.md`
@ `c5398a42` is the origin of that wording, and this document does not restate it
as if it were derived from somewhere else. Assertions about this repository carry
a provenance class: *observed*, *inferred*, *told*, *unknown*.

## 1. Problem and intent

**Dictated problem statement** (*told* — this directive is its origin): directives
are the only ungated load-bearing artifact class in this methodology. Specs get
the Spec Reviewer, governed documents get the Context Quality Reviewer, code gets
the red-gate; directives ship freehand from a decision session to an executor.
Freehand composition has an irreducible error rate that worsens with accumulated
context; a decision session late in a long conversation is a degraded author. The
countermeasure is structural, not exhortative: shrink the freehand surface, gate
the remainder.

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

One qualification, *observed*, that the tool design must respect. The committed
sentence in `skills/directive-authoring.md` @ `27ca4560` reads: "Two sessions
sharing a tree mutate each other's preconditions. Prefer not splitting; where
unavoidable, state the tree assignment in each directive." It requires the
assignment to be *stated*; it does not, in that sentence, require the command that
creates the tree. The dictated characterization is therefore stronger than the
committed text it cites. This matters because §4 G6 forbids the lint from
inventing its required-element set: a lint that demands a creating command is
enforcing a rule no governed file states. Either the governed text is amended to
say what the dictated characterization says, or the lint checks only for a named
directory. §8 Q7 carries the choice.

**Purpose** (*told* — dictated). Two tools, together: `bin/directive` shrinks the
freehand surface by emitting the invariant text from committed sources, and
`bin/check-directive` gates what remains by failing an executor's first act on a
directive missing a required element.

## 2. Users and use cases

**Primary actor — the decision session**, authoring a directive. It runs
`bin/directive`, receives a skeleton whose invariant sections are already filled
from committed repo text, and writes only the task-specific middle. It is the
actor whose error rate the problem statement names, and it is *inferred* that it
is least able to self-check, because the degradation the problem statement
describes is degradation of exactly the faculty a self-check would use.

**Primary actor — the execution session**, receiving a directive. It already
writes the directive file, commits, and pushes as its first act (*observed* —
`docs/global-context/core.md` @ `17f75612`, Vocabulary, "Execution block": "Its
first instruction is to write the directive to a file, commit, push, and report
the SHA."). It runs `bin/check-directive` inside that act and stops before any
work if the lint exits non-zero.

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
  constraints, stop conditions, a working-tree assignment slot, the verification
  steps, the report format, and the claim-label instruction, each read from
  committed repo text at generation time; fills the task-specific middle and the
  assignment slot; hands the directive to an execution session.
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
  taken.

## 4. Goals and non-goals

### Functional goals

#### `bin/directive` — the generator

- **G1 — Invariant text is read, never hardcoded.** Every invariant section the
  skeleton carries — sandbox constraints, stop conditions, working-tree
  assignment slot, verification steps, report format, claim labels — is read from
  committed repo text at generation time (*told* — dictated). A string constant
  in the tool holding text that also lives in a governed file is the defect this
  goal exists to prevent; it recreates, one layer down, the drift the problem
  statement describes.
- **G2 — The author writes only the middle.** The skeleton's task-specific region
  is the only region the decision session composes freehand (*told* — dictated).
- **G3 — The working-tree assignment is a slot, not prose.** It is emitted as a
  named, empty, structurally-present field, so that omitting it is visible rather
  than silent. This is the goal that addresses the motivating incident directly:
  an omission the author cannot see is the failure mode, and a slot makes the
  omission a blank rather than an absence.
- **G4 — The generator gates nothing.** It refuses no directive and blocks no
  author. Its whole contribution is to make the invariant text correct by
  construction; `bin/check-directive` is where refusal lives. Keeping generation
  ungated is what allows the generator to be adopted before the lint is trusted.

#### `bin/check-directive` — the lint

- **G5 — It runs inside the existing first act.** Write the directive file, lint
  it, commit, push (*told* — dictated). The lint adds no new step to the
  executor's sequence; it adds a condition to a step that already exists.
- **G6 — The required-element set derives from committed governed text.** Its
  sources are `docs/global-context/core.md`'s Vocabulary,
  `docs/global-context/decision-layer.md` rule 14, and
  `skills/directive-authoring.md` (*told* — dictated). No requirement is invented
  in the tool. A requirement the tool enforces and no governed file states is a
  defect in the tool, not a stricter tool.
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
- **G10 — Two provenance labels.** The lint's output labels each claim *observed*
  or *unknown*, and no other class. A tool observes a fact or fails to; it is
  never in a position to infer or to be told. This is a subset of Core rule 6's
  four classes, not a redefinition of them, and follows the precedent
  `specs/bin-land.md` @ `87ae153a` §4 G6 sets.

#### The two element sets

**Mechanically checkable** — candidates for the lint, each traced to its source:

| # | Element | Derived from |
| --- | --- | --- |
| M1 | A reviewed-ref pin is present and resolves to a commit | `skills/directive-authoring.md`, "Pin STOP conditions to the reviewed ref" |
| M2 | Each companion citation `<path> @ <sha>` names a path present at the reviewed ref, and a SHA that resolves to a **commit touching that path** | Core Vocabulary, "Companion document ... Cited with its own path and SHA"; `policies/document-metadata-policy.md`, "The version of a document at reference time is the SHA of the last commit touching the file" |
| M3 | A working-tree assignment is present and non-empty where the directive is parallel | `skills/directive-authoring.md`, "state the tree assignment in each directive" — see §1's qualification and §8 Q7 |
| M4 | The stop conditions are present: cannot-execute-as-written, and concurrent tree mutation | Core rules 11 and 15 |
| M5 | The first instruction is write-the-directive-file, commit, push, report the SHA | Core Vocabulary, "Execution block" |
| M6 | A report section is present and enumerates its required fields | Decision Layer rule 14, "Write it so the returned report is triageable by the next decision session" |
| M7 | The claim-label instruction is present | Core rule 6 |
| M8 | The directive filename conforms to `docs/cycles/<descriptor>-<timestamp>.md`, timestamp in ISO 8601 basic | `skills/directive-authoring.md`, "Naming"; Core rule 14 |

M2 is *observed* to catch a real defect, in this cycle: the directive that
originated this document cites its sandbox-constraint provenance as
`docs/cycles/pass2-held-fix-20260823T180753Z.md` @ `9f5f4c9d8ce06d1c5489bf3b5a3248b5386fe650`,
and that SHA is the **blob** hash of the file's content at `origin/main`, not a
commit. `git cat-file -t` returns `blob`; the only commit touching that path is
`b9444973`. The citation resolves to the right bytes and to no commit, so a
reader following the repository's own versioning rule finds nothing. This was
caught by a human-run check in this session and would have been caught by M2.

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

That last one is not a limitation to be engineered away, and this cycle
demonstrates why. The directive as first issued assigned the working tree
`../fiducial-directive-tooling` — a present, well-formed, correctly-shaped
assignment that M3 would pass. It was **not executable**: this session's sandbox
restricts writes to an allowlist carrying the clone root and `$TMPDIR` and not the
clone's parent, so `git worktree add` exited 128 with "could not create leading
directories," and a bare `mkdir` of the same path was denied while
`/Users/dave/code` stood `drwxr-xr-x dave:staff` (*observed*, this session; the
probes were removed and the failed add left no entry in `.git/worktrees`).
Executability is a property of the executor's sandbox, discoverable only at
execution. The lint checks that an assignment was *made*; it cannot check that it
can be *carried out*, and G9 requires it to say so.

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
  remote, or mutates the working tree. The generator writes to stdout; the lint
  reads. Threat model: the tools must not become a write path, and a lint on the
  first act must not be able to damage the tree it is inspecting.
- **Maintainability**: G1 and G6 are the maintainability requirements. Invariant
  text and required elements both live in committed governed files; the tools
  resolve them. A governed rule that changes changes the tools' behaviour without
  a code edit, and a tool that hardcodes either is the drift this spec targets.
- **Usability**: the generator's reader is Dave in a decision session; the lint's
  reader is an execution session. The generator's success condition is that the
  author writes less; the lint's is that its failure output is actionable without
  reading the tool's source.
- **Observability**: the lint prints its checked set, its result per element, and
  its unchecked set, on both exit paths. The generator prints which committed
  files each invariant section was read from, so a skeleton can be audited
  against its sources.
- **Portability / Compatibility**: depends on `git` and a checkout of this
  repository. Neither tool asserts what the sandbox permits.
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
- **Naming vocabulary.** Neither `directive` nor `check-directive` enters
  `LEXICON.md`. Per the dictated naming disposition (*told*; Dave, in the
  decision session that directed this authorship, with this directive file as the
  committed origin until the bin-land cycle 3 directive lands the durable
  record): binary names are not methodology vocabulary, and no LEXICON entry is
  created for a binary name. This document creates none, and edits `LEXICON.md`
  not at all.
- **Invoking `gh`.** Never, for anything.

## 5. User outcomes and measurement

- **The freehand surface shrinks.** Signal: the share of a directive's bytes that
  the generator supplied versus the author composed. Baseline: 100% author-composed
  today (*observed* — no generator exists; `bin/` holds `aimeta`, `bundle`,
  `bundle-methodology`, `check-frontmatter`, `cycle-open`, `flip-agreed`,
  `install-hooks`, `migrate-frontmatter`, `tests`). The research findings give the
  size of the region a generator would fill: write mechanics alone run 13.9% to
  43.3% of each recent `pass2` directive (*observed*, per that document).
  Mechanism: measure generator-supplied versus hand-authored bytes over directives
  authored after adoption.
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
- **AC-DT-02** — No invariant text the skeleton emits appears as a literal in the
  generator's source. Verifiable statically over the source, against the set of
  sections G1 enumerates.
- **AC-DT-03** — A generated skeleton contains a working-tree assignment slot that
  is present and empty, and is distinguishable from an assignment that has been
  filled.
- **AC-DT-04** — The generator exits 0 for every invocation that produces a
  skeleton, and rejects no content. It has no refusal path.
- **AC-DT-05** — The generator names, in its output, the committed file each
  invariant section was read from.
- **AC-DT-06** — For each element in the mechanically-checkable table M1–M8, a
  fixture directive missing exactly that element causes a non-zero exit, and the
  output names that element and cites the governed text it derives from.
- **AC-DT-07** — A well-formed fixture directive carrying every element M1–M8
  exits 0.
- **AC-DT-08** — Exit 0 output includes the unchecked set — at minimum, that
  executability of the working-tree assignment and every judgment-only rule in §4
  were not checked.
- **AC-DT-09** — A directive citing a companion by a SHA that resolves to a blob,
  a tag, or a commit that does not touch the cited path exits non-zero and names
  the citation. The historical citation in
  `docs/cycles/pass2-held-fix-20260823T180753Z.md` @ `9f5f4c9d` is a fixture case
  for the blob branch.
- **AC-DT-10** — An element the lint cannot decide is reported unknown and exits
  non-zero; no undecidable element yields exit 0.
- **AC-DT-11** — Every claim in either tool's output carries the label *observed*
  or *unknown*, and no output carries *inferred* or *told*.
- **AC-DT-12** — No code path in either tool invokes `gh`, writes to a remote,
  mutates the working tree or the index, or reads a credential. Verifiable
  statically over the source.
- **AC-DT-13** — The lint enforces no requirement absent from its cited governed
  sources. Verifiable by review of the requirement table against those files, and
  mechanically to the extent each requirement carries the citation AC-DT-06
  demands.

## 7. Risk tolerance

Both tools sit at the head of the directive path, so the posture is conservative
about claims and permissive about work: neither tool blocks an author, and the
lint fails loudly rather than passing quietly.

**The primary risk is the halo, not a false negative.** A lint that checks eight
mechanical elements, run at the head of every execution session, will be read as
saying the directive is good. It says nothing of the kind, and the elements it
cannot check — self-containment, non-contradiction, correctness of the dictated
content, executability of the assignment — are precisely the ones that produced
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

**Not accepted.** Any lint claim about a judgment-only property. Any exit 0 that
does not state its bounds. Any invariant text or required element hardcoded in a
tool rather than read from committed text — that failure recreates the drift the
tools exist to remove, in a place with less visibility than prose. Any write, of
any kind, from either tool.

**Escalation.** A lint failure returns the directive to the decision session; the
executor never repairs it. Anything the lint cannot decide is reported unknown and
handed to the session, which stops and surfaces. Whether an undecidable element is
acceptable is Dave's judgment, never the tool's.

## 8. Open product questions

- **Q1 (dictated; must remain open at this stage).** Where the invariant text
  lives, and how the generator resolves it. The candidates differ materially: a
  section of an existing governed file addressed by heading, a new governed
  standing document, or a machine-readable block. Note that the research findings
  rank a standing write-path document first among its options and call it a
  precondition for the other options being citable (*observed*, per that
  document), so this question overlaps a decision already in flight. Resolved by:
  Dave.
- **Q2 (dictated).** Lint sequencing relative to commit and push — specifically,
  whether a failing directive still lands for the audit trail. The tension is
  real in both directions: landing it preserves the record of what was actually
  handed over, and not landing it keeps a known-malformed directive from being
  citable by SHA. Resolved by: Dave.
- **Q3 (dictated).** How the lint distinguishes a parallel directive, where a
  worktree assignment is required, from a sole-tree one. Nothing in a directive's
  text marks it as parallel today (*observed* — no such marker appears in the
  governed sources G6 names), so this is a question about what the generator emits
  as much as about what the lint reads. Resolved by: Dave, at the TRD/AC stage.
- **Q4 (dictated).** Whether these tools change the text of
  `skills/directive-authoring.md` or sit beneath it. Resolved by: Dave.
- **Q5 (raised by the author).** Whether the directive **file** is the right unit
  for the lint at all. Core's Vocabulary defines a directive as "one line stating
  route (fresh or existing session) and model tier, then the execution block,"
  with "All three stated every time"; the directive file holds the execution
  block. This cycle's own directive file carries neither route nor model tier
  (*observed*), and it is genuinely unclear whether that is a defect or the
  expected shape of the file as distinct from the package. A lint that checks the
  file cannot see the two parts that never reach it. Resolved by: Dave, before the
  requirement table is fixed — Q3 does not settle it, since a marker for
  parallelism would be a fourth thing the file must carry.
- **Q6 (raised by the author).** Whether the lint has one exit status or a
  blocking/advisory split. AC-DT-10 currently makes every undecidable element
  fail, which is the strict reading of G7; a directive with a malformed companion
  citation and one with no stop conditions are not obviously the same severity.
  Resolved by: Dave, or a stated severity model at the TRD/AC stage.
- **Q7 (raised by the author).** Whether the working-tree requirement is "a named
  directory" or "a named directory plus the command creating it." §1 records that
  the dictated characterization is stronger than the sentence in
  `skills/directive-authoring.md` it cites, and G6 forbids the lint from enforcing
  the stronger reading while the governed text carries the weaker one. Resolved
  by: Dave — either by amending the skill or by scoping M3 to the directory alone.
  This is the one open question that blocks writing M3 as a test.
