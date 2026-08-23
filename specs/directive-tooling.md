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
origin of the cycle-1 wording,
`docs/cycles/directive-tooling-spec-2-20260823T195803Z.md` @ `d5a82172` is the
origin of the cycle-2 dispositions, and
`docs/cycles/directive-tooling-spec-3-20260823T203821Z.md` @ `d258434e` is the
origin of the cycle-3 dispositions, and
`docs/cycles/directive-tooling-spec-4-20260823T212151Z.md` @ `6650617e` is the
origin of the cycle-4 dispositions this revision carries. This document does not
restate any of the four as if it were derived from somewhere else. Assertions
about this repository carry a provenance class: *observed*, *inferred*, *told*,
*unknown*.

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

**Dictated disposition** (*told* — the cycle-2 directive is its origin, and it
closes what §8 Q3 and Q7 previously carried): every directive states its
working-tree disposition explicitly — either an **exclusive assignment** (a named
directory plus the command creating it) or a literal **sole-tree declaration**.
The requirement is unconditional; there is no parallel/sole-tree distinction for
the lint to draw, because both branches are stated dispositions and one of them is
always required.

**That disposition is governed text, and the lint's prerequisite is discharged**
(*observed*). `skills/directive-authoring.md` @ `48ad7fd1` states, as the first
rule under "Writing the directive file": "**Every directive states its
working-tree disposition** — either an exclusive assignment (a named directory
plus the command creating it) or an explicit sole-tree declaration. A prohibition
is not a disposition." That is the unconditional two-branch rule in both the
dimensions earlier cycles found missing: it names the command, and it conditions
the requirement on nothing. It also names the motivating incident's exact failure
in its own words — a prohibition is not a disposition. The file carries
`status: agreed`, and the expedited log's entry for the amendment reads
"2026-08-23 — skills/directive-authoring.md @ 48ad7fd1… — working-tree
disposition made mandatory for every directive"; it reached `origin/main` in
merge commit `820d071e`. The file's `last-reviewed` pointer has since advanced to
`reviews/expedited-log.md @ 83b60511`, which selects the **second** expedited
amendment to the same file — the Naming change M8 turns on (§4) — and does not
disturb the working-tree rule, whose text is unchanged between the two
(*observed*, by diff).

Two citation notes, stated because M2 below is about exactly this discipline.
First, `48ad7fd1` is the **content commit** — the commit that introduced the rule
text — and is the SHA the expedited log uses to select the agreement. It is not
the last commit touching the file: that is now `14bc7c97`, a frontmatter-only
status transition following the second amendment, having been `511b4dca`, the
equivalent transition following the first (*observed*, all three). This document
cites content commits, as the log does — `48ad7fd1` for the working-tree rule and
`83b60511` for the Naming rule — and M2's derivation is narrowed accordingly (§4,
"M2's Derived-from is narrowed"), because a check enforcing lastness would fail
both of these citations and the log's own convention with them. Second, the
earlier cycles' reading was accurate when made: at `27ca4560` the sentence read
"Two sessions sharing a tree mutate each other's preconditions. Prefer not
splitting; where unavoidable, state the tree assignment in each
directive," which required the assignment to be stated, did not require the
command, and conditioned the requirement on splitting (*observed*). The amendment
closed both gaps. G6 is therefore satisfied for M3 as of `48ad7fd1`, and M3
carries no standing qualification anywhere in this document.

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
document-set resolution feeding it. Nothing else is claimed to move. In
particular this document makes no claim about **where** `cycle-open`'s bundle
emission (`write_bundle`), its `--bundle` context-set expansion, its `--out`
directory contract, or its `--allow-dirty` behaviour end up; whether those travel
with the mode, stay where they are, or split is a TRD question. What this document
does claim about them is stated immediately below and is orthogonal to placement:
they keep working, because the contract that governs them is preserved whole.

**The governing contract for what moves** (*observed* for the sources; the
disposition to name them is *told* — cycle-3 directive B2). `bin/cycle-open` is not
ungoverned code. `docs/packages/package-a-spec.md` §3.6 specifies its CLI and
carries **AC-CO-1 through AC-CO-12**, and `bin/tests/test_cycle_open.py` implements
them, referring to `AC-CO-` identifiers 34 times. AC-CO-3 fixes the skeleton's
structure — the `# Cycle <n> Directive — <title>` heading, the `Date:` line, the
`Documents in scope:` list of `- <path> @ <full sha>` entries, a `## Decisions`
section with a commented placeholder carrying `Finding: / Resolution: /
Dictated wording:`, `## Deferred / out of scope`, and `## Execution notes` — and
AC-CO-4 fixes the SHA rule. Those are precisely the behaviours the migration moves,
and until this cycle this document named the tool without naming what governs it.

**The disposition of that contract: preserved intact, under the cycle mode**
(*told* — dictated). AC-CO-1 through AC-CO-12 are neither superseded nor split.
`docs/packages/package-a-spec.md` §3.6 remains the authoritative acceptance-criteria
artifact for the behaviour it specifies, and the cycle mode of `bin/directive`
satisfies it unchanged: the same filename contract (AC-CO-1 — which is why M8
admits two forms), the same skeleton structure (AC-CO-3), the same SHA rule
(AC-CO-4), the same refusals, and the same `--out` and bundle behaviour wherever
the TRD lands those. `bin/tests/test_cycle_open.py` is the **named test surface
that must stay green through the migration**: it is the executable statement of the
contract, and a migration that reds it has changed the contract rather than moved
it (AC-DT-15). What the TRD may decide is where those criteria are *invoked* from —
which binary, which mode — not what they require.

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

**One landing requirement follows from G0, and it is not a code change** (*told* —
the cycle-3 directive is its origin; *observed* for the records it names). Three
committed records name `bin/cycle-open` by name as the bearer of a decided
obligation: `decisions/log.md` DEC-000150 ("`bin/cycle-open` (TP-1) must emit
Route, Model, and Track"), DEC-000180 ("`bin/cycle-open` (TP-1, shelved) emits
Route and Model and no Track"), and `OPEN-ITEMS.md`'s section headed
"`bin/cycle-open` and the retirement of Track". `policies/decision-log-policy.md`
makes the log append-only — "A decision is never edited in place. To change or
reverse one, append a new entry whose `Supersedes:` names the old ID" — so those
references cannot be rewritten where they stand, and Core rule 13's
changed-fact-changes-everywhere is satisfied by supersession, not by edit. The
requirement: **the migration does not land until a new decision-log entry
supersedes DEC-000180**, restating its still-live content and re-anchoring the
tooling consequence on `bin/directive` in its cycle mode. That is whole-entry
supersession, exactly the mechanism DEC-000180 itself used against DEC-000150 and
DEC-000150 against DEC-000110. DEC-000150's own `cycle-open` reference is already
inert, DEC-000180 having superseded it (*observed*), so no action reaches it.

**The third record is not append-only, and the requirement extends to it** (*told*
— the cycle-4 directive's N3). `OPEN-ITEMS.md`'s section headed "`bin/cycle-open`
and the retirement of Track" is a **tracker**, editable in place, and its guard —
"If TP-1 is unshelved, its skeleton emits **Route and Model and nothing else**" —
anchors the obligation on `bin/cycle-open` by name (*observed*). The same landing
that appends the superseding log entry also updates that section to name
`bin/directive`'s cycle mode. Those are two acts on two mechanisms — an append
where the log forbids editing, an edit where the tracker permits it — and both are
preconditions on the same landing. Extending the requirement is what takes the
count of records still pointing at a binary that no longer emits a skeleton from
one to none.

**No edit is made to either record in this cycle** (*told* — dictated): this
document states both requirements as AC-DT-16, and both acts fall to **the
decision session that lands the migration**. Appending to `decisions/log.md` is
decision-session work under `policies/decision-log-policy.md`; the tracker edit
accompanies it. Neither is an obligation on the implementer of either tool, and
AC-DT-16 says so in its own text so that it cannot be read as one.

`cycle-open`'s existing docstring principle — "Every SHA is the full id of the
last commit touching the path, read from git — never invented, never abbreviated"
— is *observed* to be the same principle G1 states for invariant text and M2
states for citations. The generalization inherits it rather than introducing it.

**Mode scoping — how every claim about the generator is to be read** (*told* —
the cycle-4 directive is the origin of this scoping, which disposes the conflict
cycle 3 found between this document's goals and the contract it absorbs).
`bin/directive` has two modes and they do not carry the same obligations, so a
claim about "the generator" is ambiguous unless it names the mode it binds. The
convention this document adopts, and applies from here on:

- **Cycle mode** — the mode that replaces `bin/cycle-open`. It preserves the
  inherited contract whole: AC-CO-1 through AC-CO-12, including their refusals
  (AC-CO-1, -2, -5, -6, -12) and their writes (AC-CO-1 and AC-CO-7, bounded by
  AC-CO-11). Where a goal or criterion of this document would say otherwise, the
  preserved contract governs the cycle mode — "preserved intact" is the dictated
  disposition, and this document is not free to narrow it by implication.
- **General mode** — every other invocation. This is the mode G4 and AC-DT-04
  describe, and the mode AC-DT-12(c)'s mutation bound binds.

Two claims here were previously written as though they were global, and both now
name their mode: **G4 / AC-DT-04** (no refusal path) and **AC-DT-12** (no
working-tree mutation). Reading either globally is what made them contradict
AC-DT-15, and the scoping is what removes the contradiction rather than
weakening either claim where it applies. **AC-DT-15 is not scoped by this
convention and is not narrowed by it**: `bin/tests/test_cycle_open.py` must stay
green through the migration, whole, and it is the cycle mode that suite
exercises.

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
- **G4 — The generator gates no directive content; in its general mode it
  refuses nothing at all.** This goal is **scoped to the general mode** ("Mode
  scoping", above). In the general mode the generator refuses no directive and
  blocks no author. In the cycle mode it carries the five precondition refusals
  AC-CO-1, -2, -5, -6, and -12 state, intact, because that contract is preserved
  whole. In **neither** mode does it refuse, reject, or gate the *content* an
  author writes: every refusal it has is a precondition refusal — no mode
  selected or both selected, an existing directive it would overwrite, a dirty or
  untracked in-scope document, an absolute `--out` — and none of them is a
  judgment about a directive. Its whole contribution is to make the invariant
  text correct by construction; `bin/check-directive` is where refusal *of a
  directive* lives. Keeping the general mode ungated is what allows the generator
  to be adopted before the lint is trusted.
- **G11 — The skeleton records its own sources *and their extents*, in the file.**
  The generator emits, as part of the skeleton it writes, a **source manifest**:
  one entry per emitted region, carrying that region's source **and its location in
  the emitted file**. Location is mechanical, not descriptive. The generator emits **every** region of the
  skeleton — each invariant section and the task-specific author slot alike —
  under a named, stable section marker of its own choosing, and the manifest names
  every region in emission order, each entry carrying either the committed path
  that region was read from or an explicit marking that the region is the author's
  slot. Because every region is marked and the manifest enumerates them all, the
  markers partition the whole file: a region's extent runs from its own marker to
  the next marker or to end of file, with nothing falling between two regions. The
  generator-supplied share is the sum of the extents whose entries name a committed
  path. Marking the author slot is the part that makes this work, and it is
  required, not incidental: without it an invariant section's extent would run
  through whatever the author wrote after it, and the share would compute to
  everything. Extent is therefore computable by reading the landed file together
  with the manifest it carries, without knowing what the generator emitted, without
  the generator being present, and without any tooling. The manifest is part of the
  directive the executor lands, not a side channel to the author's terminal. Two
  things depend on it that nothing else supplies: AC-DT-02's static check needs a declared set of
  sources to range over, and §5's first measurement needs the generator-supplied
  region of a landed directive to be identifiable **as a byte range, not merely as
  a count**, from the committed file alone. Which marker syntax is used is a TRD
  question; that every region carries one, and that the manifest names it, is not.

#### `bin/check-directive` — the lint

- **G5 — It runs inside the existing first act.** Write the directive file, lint
  it, commit, push (*told* — dictated; the act itself is DEC-000160's). The lint
  adds no new step to the executor's sequence; it adds a condition to a step that
  already exists.
- **G6 — The required-element set derives from committed governed text.** Its
  sources are `docs/global-context/core.md`'s Vocabulary,
  `docs/global-context/decision-layer.md` rule 14, `skills/directive-authoring.md`,
  and `decisions/log.md` (*told* — dictated for the first three; the decision log
  was added in cycle 2 per that cycle's B3). No requirement is invented in the
  tool. A requirement the tool enforces and no governed file states is a defect in
  the tool, not a stricter tool. The one place this bit is closed: M3's
  unconditional two-branch rule is governed text as of
  `skills/directive-authoring.md` @ `48ad7fd1` (§1), so every element M1–M8 traces
  to committed text and none is held back. The goal itself is unchanged and still
  binds every element added later.
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
| M2 | Each companion citation `<path> @ <sha>` names a path present at the reviewed ref, and a SHA that resolves to a **commit touching that path**. Neither fullness nor lastness is checked — see the narrowing note below the table | Core Vocabulary, "Companion document ... Cited with its own path and SHA" and "Directive file ... thereafter cited by path and the SHA of the commit that landed it"; `bin/cycle-open`'s docstring principle, "never invented" | none |
| M3 | A working-tree disposition is present, in **exactly one** of two forms: an exclusive assignment (a named directory plus the command creating it), or a literal sole-tree declaration. Unconditional — every directive, no parallelism test | `skills/directive-authoring.md` @ `48ad7fd1`, "Writing the directive file", first rule: "Every directive states its working-tree disposition — either an exclusive assignment (a named directory plus the command creating it) or an explicit sole-tree declaration. A prohibition is not a disposition." | none |
| M4 | The stop conditions are present: cannot-execute-as-written, and concurrent tree mutation | Core rules 11 and 15 | none |
| M5 | The first instruction is write-the-directive-file, commit, push, report the SHA | Core Vocabulary, "Execution block" | DEC-000160 fixes this for **every** directive class, so no class exemption exists for the lint to carry |
| M6 | A report section is present and enumerates its required fields | Decision Layer rule 14, "Write it so the returned report is triageable by the next decision session" | none |
| M7 | The claim-label instruction is present | Core rule 6 | none |
| M8 | The directive filename conforms to **exactly one of two forms**: `docs/cycles/<descriptor>-<timestamp>.md` with the timestamp in ISO 8601 basic, or `docs/cycles/cycle-<N>-directive.md` for a reviewer-gated cycle directive. No third form passes | both forms, from one sentence: `skills/directive-authoring.md` @ `83b60511`, "Naming": "A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format — except a reviewer-gated cycle directive, which is `docs/cycles/cycle-<n>-directive.md` per its stated convention." Corroborated for the first form by Core rule 14, and for the second by `docs/packages/package-a-spec.md` §3.6 AC-CO-1, which Core rule 14 defers to as a stated convention | none |

**M8 admits two forms because two governed sources name two conventions, and G0
puts both inside one tool** (*told* — the cycle-3 directive is the origin of the
disposition; *observed* for the sources). `skills/directive-authoring.md` @
`48ad7fd1`, "Naming", states the timestamp form. `docs/packages/package-a-spec.md`
§3.6 AC-CO-1 requires `bin/cycle-open` to write `docs/cycles/cycle-<N>-directive.md`
for `--cycle N`, which carries no timestamp. G0 folds that generator into
`bin/directive`, so a single-pattern M8 would fail — at the executor's first act,
under J3 — a well-formed directive this spec's own generator was told to produce.
The disposition: the form is **determined by the generator's mode**, not chosen by
the author. The cycle mode emits the AC-CO-1 form; every other mode emits the
timestamp form; M8 is a two-pattern check accepting exactly these two and nothing
else. Core rule 14 states the timestamp form "when no stated convention names the
file" and adds "Where a convention names it, follow the convention," so AC-CO-1 is
licensed by the rule it appears to contradict.

**Both forms are now licensed in the skill that specialises rule 14 to
directives, and M8's second form is anchored there** (*observed* for the text;
the re-anchoring is *told* — the cycle-4 directive's N2). Cycle 3 recorded a
residual: `skills/directive-authoring.md`'s "Naming" section restated Core rule
14 without its yield clause, so read alone it admitted only the timestamp form,
and M8's second form rested on Core rule 14 and AC-CO-1 rather than on the skill
an author is instructed to follow. That residual is **closed**. The Naming
section at `origin/main` now reads, whole: "A directive file is
`docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format
— except a reviewer-gated cycle directive, which is
`docs/cycles/cycle-<n>-directive.md` per its stated convention." Its content
commit is `83b60511`, agreed by expedited amendment and recorded in
`reviews/expedited-log.md` — "2026-08-23 — skills/directive-authoring.md @
83b60511… — numbered cycle-directive form licensed alongside the timestamp form"
— reaching `origin/main` in merge commit `073ca747`. M8's Derived-from column
cites that sentence for both forms. Nothing in this document schedules an
amendment to that section, because the amendment has landed: no open question and
no criterion waits on it, and the permissive-lint argument the residual rested on
is no longer needed, the skill and the lint now admitting the same two forms.

**M2's Derived-from is narrowed to what M2's check enforces** (*told* — the
cycle-4 directive's N1 disposes this; the choice it offered was to strengthen the
check or to narrow the derivation, and narrowing is the branch that keeps this
document's own citations passing the rule it writes). Cycle 3 recorded that M2's
sources were stricter than M2: `policies/document-metadata-policy.md` says "The
version of a document at reference time is the SHA of the last commit touching
the file," and AC-CO-4 requires the *full* SHA of the *last* commit. M2 checks
neither property, and the narrowing is deliberate rather than an omission:

- **Lastness is wrong for this check.** A citation may deliberately select a
  commit that is not the last one touching the path, and this document does it
  twice, for cause: `skills/directive-authoring.md` is cited at its two **content
  commits**, `48ad7fd1` for the working-tree rule and `83b60511` for the Naming
  rule, while the last commit touching that path is `14bc7c97`, a
  frontmatter-only status transition that introduced neither. `reviews/expedited-log.md`
  selects both agreements the same way (*observed*). A lint enforcing lastness
  would fail both citations and the expedited log's own convention with them.
- **Fullness is not enforced, because no governed source states it for a
  citation.** AC-CO-4 states it for SHAs the generator **emits**, which is a
  different act from the SHAs the lint **reads**, and G6 forbids the lint from
  enforcing what no governed file requires of the thing it is checking. Every
  companion SHA in this document is abbreviated to eight characters, as is the
  prevailing convention in the committed directive corpus (*observed*).

So the two standards inside one binary are asymmetric on purpose, and the
asymmetry is now stated rather than denied: the cycle mode **emits** full
last-commit SHAs (AC-CO-4, preserved intact), and the lint **accepts** any
resolvable commit touching the cited path, abbreviated or not. Permissive check,
strict emission — the same direction the M8 disposition takes, and the direction
G6 requires when the two differ. `policies/document-metadata-policy.md`'s rule is
not repudiated; it is simply not what M2 checks, and M2's Derived-from column no
longer cites it as though it were.

Historical directive files are **not retrofitted** (*told* — dictated); the lint
governs directives written after adoption, and renaming the existing corpus would
break every citation by path that points into it. The dictated figure for the
non-conforming set is 37, which was the count against the **single-pattern** M8 at
cycle 2 (*told*). Against the two-pattern M8, and at this document's own revision,
`docs/cycles/` holds 96 markdown files, of which 60 match the timestamp form, 7
match `cycle-<N>-directive.md`, and **29 match neither** — mostly the
`<slug>-directive.md` and `<slug>-<YYYY-MM-DD>-directive.md` forms (*observed*,
recounted at this revision; the total and the timestamp-form count each rise by
one against cycle 3's because this cycle's own directive file is in the
directory). The classification counts a name as the timestamp form when its
trailing field is `YYYYMMDDTHHMMSS` with an optional `Z`; one committed file
carries a date and no time — `metadata-scope-fix-20260823.md` — and is counted in
the 29, which is the classification cycle 3 used and is preserved here so the two
counts are comparable. Both figures stay on the record with their provenance
(*told* — the cycle-4 directive's O1). The disposition is unchanged by either
count; the counts are restated because Core rule 13 requires a changed number to
change where it appears.

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
and its assignment executed (*observed*, cycle 2); the cycle-3 assignment, also
under `$TMPDIR`, executed the same way (*observed*, cycle 3). Executability is a
property of the executor's sandbox, discoverable only at execution and only after
the
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
  remote, stages, or commits. What each may write to the tree is bounded, and the
  bound is mode-scoped. The lint reads and writes nothing at all. The generator in
  its **general mode** writes its skeleton and its source manifest to stdout or to
  a named output path and touches nothing else. The generator in its **cycle
  mode** additionally writes what the preserved contract requires of it — the
  directive file (AC-CO-1) and the reviewed-revision bundle under `--out`
  (AC-CO-7) — inside the boundary that contract already draws: AC-CO-11, "The tool
  writes only the directive and the bundle directory. It does not stage, commit,
  or modify any document." Threat model: the tools must not become a remote-write
  path, must never modify a document they did not create, and a lint on the first
  act must not be able to damage the tree it is inspecting. §6 AC-DT-12 states
  this criterion in the three parts this bound divides into, and is aligned to
  this paragraph rather than the reverse.
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
  The manifest names every region of the file in emission order — each invariant
  section by its committed source, the task-specific region as the author's slot —
  and names the marker that begins each, so the markers partition the file and each
  region's extent runs from its marker to the next marker or to end of file. The
  byte share is therefore computable from the committed artifact alone — sum the
  extents whose entries name a committed source, divide by file size — by reading
  the file and its manifest and nothing else. That is the
  mechanism the signal needs and that naming a source path alone did not supply:
  a source locates where text *came from*, and a share requires knowing where it
  *sits*. Its bound, stated
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
- **AC-DT-04** — Scoped to the **general mode** (§4, "Mode scoping"). In the
  general mode the generator exits 0 for every invocation that produces a
  skeleton, rejects no content, and has no refusal path. In **both** modes it
  rejects no directive *content*: no text an author places in the skeleton's
  task-specific region causes a non-zero exit in either mode, including text the
  lint would fail. Verifiable by invoking the general mode across a fixture set
  that includes such text and asserting exit 0 throughout. The cycle mode's five
  precondition refusals (AC-CO-1, -2, -5, -6, -12) are outside this criterion and
  are required by AC-DT-15; running this criterion's fixtures through the general
  mode is what keeps the two testable without contradiction.
- **AC-DT-05** — The generator emits a source manifest naming, per emitted
  region, **the marker that begins that region** and either the committed file the
  region was read from or an explicit marking that the region is the author's slot;
  and the manifest is part of the skeleton written to the directive file rather
  than terminal-only output. Every marker the manifest names appears in the emitted
  file exactly once, every region the generator emits carries one, and the manifest
  enumerates every region in emission order — so taking each entry's extent from
  its marker to the next marker or to end of file partitions the **whole file**
  with no overlap and no gap, and the generator-supplied share is the sum of the
  extents whose entries name a committed source. Verifiable by generating a
  skeleton and computing that partition from the file alone.
- **AC-DT-06** — For each element in the mechanically-checkable table M1–M8, a
  fixture directive missing exactly that element causes a non-zero exit, and the
  output names that element and cites the governed text it derives from. For M3
  the check is an **unconditional presence test** over two named forms, with no
  parallelism precondition and no sequencing precondition — the governed rule is
  committed (`skills/directive-authoring.md` @ `48ad7fd1`), so this criterion is
  live now and its fixtures are written now: a fixture with neither an exclusive
  assignment nor a sole-tree declaration exits non-zero, a fixture carrying both
  exits non-zero, and each of the two single-form fixtures exits 0 on that element.
  The fixture set includes a sole-tree directive, which under this criterion must
  pass M3 rather than be exempt from it, and a fixture whose only working-tree
  statement is a **prohibition**, which must exit non-zero — that is the motivating
  incident, and the governed rule decides it in its own words ("A prohibition is
  not a disposition"). For M8 the check is a **two-pattern test**: a
  `<descriptor>-<timestamp>.md` fixture and a `cycle-<N>-directive.md` fixture each
  exit 0 on that element, and a fixture matching neither — a bare
  `<slug>-directive.md`, the historical form — exits non-zero.
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
- **AC-DT-12** — Stated in three parts, because the boundary is mode-scoped;
  §4's Security NFR is the statement these parts align to. **(a) Both tools,
  every mode**: no code path invokes `gh`, writes to a remote, reads a
  credential, stages, commits, or modifies any file the invocation did not
  create. **(b) The lint**: no code path writes to the filesystem at all. **(c)
  The generator's general mode**: it writes only the skeleton and its source
  manifest, to stdout or to the named output path, and mutates nothing else in
  the working tree or the index. The generator's **cycle mode** is outside (c),
  bounded instead by the contract preserved intact — it writes the directive file
  (AC-CO-1) and the bundle (AC-CO-7) and nothing further, which is AC-CO-11's own
  boundary, and AC-DT-15 is where that is verified. All three parts are
  verifiable statically over the source; (c) is additionally verifiable by
  running the general mode against a fixture repository and diffing the tree.
- **AC-DT-13** — The lint enforces no requirement absent from its cited governed
  sources. Verifiable by review of the requirement table against those files, and
  mechanically to the extent each requirement carries the citation AC-DT-06
  demands. Every element M1–M8 satisfies this as written, M3 included
  (`skills/directive-authoring.md` @ `48ad7fd1`); no element is held back and none
  carries a sequencing qualification. The criterion binds every element added
  later, which is the case it now exists to catch.
- **AC-DT-14** — After migration, `bin/` contains exactly one directive-skeleton
  generator. The reviewer-gated cycle skeleton is produced by `bin/directive` in
  its cycle mode, it carries Route and Model and no Track (DEC-000180), and
  `bin/cycle-open` no longer emits a skeleton of its own. Verifiable by generating
  a cycle skeleton through the new path and by static inspection of `bin/`.
- **AC-DT-15** — The migration preserves the contract it absorbs:
  `bin/tests/test_cycle_open.py` passes after the migration, with AC-CO-1 through
  AC-CO-12 satisfied and none of them retired — whichever binary each criterion is
  invoked through, which is the TRD's question and not this criterion's. A red in
  that suite is a failed migration, not a superseded criterion. Verifiable by
  running the pre-existing suite.
- **AC-DT-16** — **Binds the decision session that lands the migration, not the
  implementer of either tool** (*told* — the cycle-4 directive's O3 fixes the
  wording; the substance is unchanged). The migration does not land until both
  records that still bind the obligation to `bin/cycle-open` have been
  re-anchored: **(a)** `decisions/log.md` carries a new entry whose `Supersedes:`
  names DEC-000180 and whose tooling consequence names `bin/directive`'s cycle
  mode rather than `bin/cycle-open`; and **(b)** `OPEN-ITEMS.md`'s section headed
  "`bin/cycle-open` and the retirement of Track" names `bin/directive`'s cycle
  mode as the bearer of the Route-and-Model-and-no-Track obligation. Verifiable by
  reading the two files. (a) is an append, `policies/decision-log-policy.md`
  scoping appends to decision sessions; (b) is an in-place edit, the tracker not
  being append-only. Neither is a property of either tool's behaviour and no
  implementation session can discharge either, so a release gate reading §6 as an
  implementer checklist should read this entry as waiting on a decision session
  rather than as red. It is stated as a criterion because supersession by a new
  entry is the only mechanism the append-only log offers for a committed record to
  stop naming a binary that no longer bears the obligation, and because the
  tracker would otherwise be the one record nothing reaches.

## 7. Risk tolerance

Both tools sit at the head of the directive path, so the posture is conservative
about claims and permissive about work: neither tool gates an author's judgment
about directive content, and the lint fails loudly rather than passing quietly.
The generator's cycle mode does refuse on the five preconditions it inherits (§4,
"Mode scoping"); that is a refusal to *run*, not a refusal of a directive, and the
posture is unchanged by it.

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
are independently useful, and G4 keeps the general mode ungated so it can go
first. The cycle mode is not ungated and never was — it inherits `cycle-open`'s
preconditions — but it is not new surface either, so adopting it early imposes no
refusal an author does not already meet today.

**Accepted, with a named cost.** Folding `cycle-open` into `bin/directive` (G0)
puts a working tool through a migration for a benefit — one home for invariant
text — that only pays off once the second class of directive uses it. The
alternative accepted risk was two generators drifting; that one has no ceiling,
and this one is bounded by the migration.

**Not accepted.** Any lint claim about a judgment-only property. Any exit 0 that
does not state its bounds. Any invariant text or required element hardcoded in a
tool rather than read from committed text — that failure recreates the drift the
tools exist to remove, in a place with less visibility than prose. Any write from
the lint, of any kind; and any write from the generator beyond the skeleton it
was invoked to
produce and, in the cycle mode, the directive file and bundle the preserved
contract requires (AC-DT-12, AC-CO-11). The boundary moved this cycle from "no
writes" to "only these writes," and what is not accepted is a write outside it —
the narrowing is of the claim, not of the protection. Any refusal by either mode
that turns on the *content* of a directive rather than on a precondition, which
would put refusal in two places and make the generator a second gate. Any lint
enforcement of a requirement no governed file states (G6, AC-DT-13) — the one
element that stood in that position, M3, is now governed text, and the
prohibition stands undiminished for every element added after it.

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
  restated in cycle 2 so that no acceptance criterion depends on the answer.
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
- **Q4 — the sequencing item is closed** (cycle 3); the original question stays
  open, narrower. Whether these tools change the text of
  `skills/directive-authoring.md` or sit beneath it. The half that had become a
  prerequisite is discharged: M3's unconditional two-branch rule is stated in that
  skill as of `48ad7fd1`, agreed via `reviews/expedited-log.md` and merged to
  `origin/main` in `820d071e`, so nothing in this document waits on an amendment
  and no element is held back (§1, §4 G6, AC-DT-13). **The governed home is settled
  with it** (*told* — cycle-3 directive, disposing cycle-1 finding O1): the
  mandatory working-tree rule lives in `skills/directive-authoring.md`, not in the
  `skills/directive-execution.md` that `OPEN-ITEMS.md` proposes for
  directive-execution mechanics. The amendment settles it by landing there, which
  is a stronger answer than an argument for either home would have been. What
  remains open is the narrower original question: whether the *rest* of these
  tools' requirements eventually move into that skill's text or sit beneath it
  unchanged. Resolved by: Dave.
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
  (AC-DT-06). The residual obligation this created — amending
  `skills/directive-authoring.md` so G6 is satisfied — is **discharged**: the
  amendment landed at `48ad7fd1` and is recorded in §1 and Q4, not here.

- **Q8 — closed** (cycle 3, by dictated disposition). Which filename convention M8
  enforces, given that G0 puts a generator required to emit
  `cycle-<N>-directive.md` inside a lint that a single-pattern M8 would require to
  reject it. Recorded as a question because the choice lay between two governed
  conventions and was not the author's to make. Chosen: **two forms, determined by
  the generator's mode** — the cycle mode emits the AC-CO-1 form, every other mode
  emits the timestamp form, M8 accepts exactly these two, and neither governed
  source is amended. Chosen by: Dave, in
  `docs/cycles/directive-tooling-spec-3-20260823T203821Z.md` @ `d258434e`. The
  residual cycle 3 recorded — that `skills/directive-authoring.md`'s "Naming"
  sentence restated Core rule 14 without its yield clause, so the skill admitted
  only one of the two forms — is **closed, not carried**: that section was amended
  at `83b60511`, now names both forms, and M8's Derived-from is re-anchored on it
  (§4). Nothing in this question waits on an amendment.
