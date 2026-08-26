---
status: in-review
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
origin of the cycle-4 dispositions, and
`docs/cycles/directive-tooling-spec-5-20260823T214112Z.md` @ `ff0f56f0` is the
origin of the cycle-5 dispositions, and
`docs/cycles/directive-tooling-spec-6-20260823T222826Z.md` @ `fe4ee58c` is the
origin of the cycle-6 dispositions, and
`docs/cycles/directive-tooling-spec-7-20260823T230004Z.md` @ `34a57ac7` is the
origin of the cycle-7 dispositions, and
`docs/cycles/directive-tooling-spec-9-20260823T233309Z.md` @ `b0f84690` is the
origin of the cycle-9 dispositions, and
`docs/cycles/directive-tooling-spec-10-20260823T235811Z.md` @ `eeaa06cb` is the
origin of the cycle-10 dispositions, and
`docs/cycles/directive-tooling-spec-11-20260824T002031Z.md` @ `c93eaba3` is the
origin of the cycle-11 dispositions, and
`docs/cycles/directive-tooling-spec-12-20260824T003835Z.md` @ `a580deb7` is the
origin of the cycle-12 dispositions, and
`docs/cycles/directive-tooling-spec-14-20260824T013026Z.md` @ `ef5755f4` is the
origin of the cycle-14 dispositions, and
`docs/cycles/directive-tooling-spec-15-20260824T021751Z.md` @ `438fa4f5` is the
origin of the cycle-15 dispositions, and
`docs/cycles/directive-tooling-spec-17-20260824T033019Z.md` @ `7010e8ff` is the
origin of the cycle-17 dispositions, and
`docs/cycles/directive-tooling-spec-18-20260824T042409Z.md` @ `5ffe9ed6` is the
origin of the cycle-18 dispositions — including the
**descope** that still governs, which fixes what this document decides and what it
routes to the TRD stage (§4, "Scope split with the TRD") — and
`docs/cycles/directive-tooling-spec-19-20260824T061718Z.md` @ `c05efadd` is the
origin of the cycle-19 dispositions this revision carries, including **Dave's
ruling** on the cycle mode's disposition statement (§4, "The cycle mode emits the
disposition statement too") and the **reading** that reconciles the governed
exactly-one count with M3's unfenced count (§4, "The count is exactly one"). And
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6` is
the origin of the two dispositions **this** revision carries, both ruled against
`reviews/directive-tooling-cycle-19.md`: the **scoping** of that reading to
**carried** wording, which returns the fenced-only shape to §7's residual set as
an accepted false positive (§4, "The count is exactly one"; §7), and the
**restoration** of the fourth sentence of the governed bullet M3's Derived-from
cell quotes, which that gate found dropped from a cell claiming the rule was
quoted whole (§4, M3's row). Cycle 8 contributes no
dispositions and has no directive in this series: it was the **independent
gate** on the cycle-7 revision — the first cycle whose review was not written by
the session that authored the revision — run under
`docs/cycles/directive-tooling-gate-20260823T231530Z.md` @ `b642d4fc`, and its
findings are what the cycle-9 directive dispositions (*observed*). **Cycle 13 is
the second independent gate and likewise contributes no directive in this
series**: it was run under
`docs/cycles/directive-tooling-gate-2-20260824T005952Z.md` — named here so a
reader tracing the second independent gate has the same path for it that the
first has (*told* — the cycle-17 directive's O6, disposing the cycle-16 gate's
O6) — it reviewed the cycle-12 revision at `0eafc306`, and its findings are
what the cycle-14 directive dispositions — B1 (M3's search predicate), N1
(AC-DT-02's single exclusion rule), N2 (the lint's manifest contract), and N3
(the lint's path resolution), with O1–O5 taking no action (*observed*, by
reading `reviews/directive-tooling-cycle-13.md` and the cycle-14 directive).
**Cycle 14 is a self-gate and contributes no directive in this series either**:
it reviewed the cycle-13 revision at `c764da19`, and its findings are what the
cycle-15 directive dispositions — B1 (a false negative reachable in M3's
whole-file branch), N1 (the check stated once and referenced everywhere else),
N2 (§7's residual enumeration, stated in extension), and N3 (the third
enumerated shape of M3's retired predicate), with O1–O4 taking no action
(*observed*, by reading `reviews/directive-tooling-cycle-14.md` and the cycle-15
directive). **Cycle 16 is the third independent gate and contributes no
directive in this series either**: it was run under
`docs/cycles/directive-tooling-gate-3-20260824T030834Z.md`, it reviewed the
cycle-15 revision at `0b1c90c6`, and its findings are what the cycle-17
directive dispositions — B1
(the skeleton could not convey the label form M3 matches, and AC-DT-03 and
AC-DT-06's fixture (v) contradicted each other about it), N1 (M3's count clause,
and the extension over which §7 stated its residual), N2 (the label form
untracked in §8), N3 (§1's motivating incident stated narrower than the current
governed rule), and N4 (the conflict rule's scope), with O6 accepted and O1–O5
taking no action (*observed*, by reading
`reviews/directive-tooling-cycle-16.md` and the cycle-17 directive). **Cycle 17's
review is a self-gate**, produced under the cycle-17 directive by the session
that authored the cycle-17 revision: `reviews/directive-tooling-cycle-17.md`
reviewed that revision at `6d29a4ab`, and its findings are what the cycle-18
directive dispositions — B1 (nothing bounded the disposition **prompt** from
carrying the label's lexical form, so a generator conforming to AC-DT-03 could
emit a skeleton carrying two labelled disposition statements), N1 (M3's
exactly-one count still stated by no governed file, disclosed rather than
closed), N2 (no criterion requiring the generator and the lint to take the label
from one source), and N3 (the fenced-only shape pinned by an inference rather
than by a fixture), with O1–O5 taking no action (*observed*, by reading
`reviews/directive-tooling-cycle-17.md` and the cycle-18 directive). **Cycle 18
is a self-gate on the same pattern**, its review artifact
`reviews/directive-tooling-cycle-18.md` produced under the cycle-18 directive by
the session that authored the cycle-18 revision, and its findings are what the
cycle-19 directive dispositions — B1 (G3's generated-skeleton invariant binding
"in either mode" against a cycle-mode skeleton that preserves AC-CO-3's structure
and carries no disposition region at all), N1 (the governed count reading
"exactly one per directive" flat while M3 counts only unfenced statements), and
N2 (three PRD-level properties gated on §8 Q9 at once), with O1–O6 taking no
action (*observed*, by reading `reviews/directive-tooling-cycle-18.md` and the
cycle-19 directive). **Cycle 19's review is a self-gate on the same pattern**,
its review artifact `reviews/directive-tooling-cycle-19.md` produced under this
cycle's directive by the session that authored this revision, with a
confirmation-scoped independent gate to follow it (*told* — the cycle-19
directive). This document
does not restate any of them as if it were derived from somewhere else. Assertions
about this repository carry a provenance class: *observed*, *inferred*, *told*,
*unknown*.

**One cycle-10 disposition was settled in the decision exchange rather than in
the directive file, and is recorded here because Core rule 4 makes the artifact
the record** (*told*). The cycle-10 directive's **N2** ends "keep both fixtures"
and its **O2** reads "Drop the subsumed fixture", and the fixture the cycle-9
gate's O2 identifies as subsumed — `docs/escaped-directive.md` — is one of the
two N2 keeps. The execution session stopped and surfaced the conflict rather
than reinterpreting either disposition, and Dave dictated that **N2 governs**:
both fixtures are kept, O2's second clause is executed as a stated relation
between the fixtures, and O2's first clause is overridden. AC-DT-06 carries the
disposition and the reason it went that way; §7's accepted-risk list is
unaffected. Nothing else in this cycle turned on the answer.

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
- Code. `operating-model.md` line 137: "The red-gate at step 4 is mandatory and
  behavioral: the tests demonstrably fail".
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
records, in its §3.1, that across **the 90 markdown files** it measured in
`docs/cycles/` — the directory held **91** at that revision, 90 excluding that
cycle's own file, and the count is of markdown files in a directory, not of
directives as a class — sentences carrying write-path vocabulary are 16.5% of
sentences and 21.8% of characters; that in the six most recent `pass2`
directives write mechanics run 13.9% to 43.3% of each file; and, in its §3.2,
that eight committed directives instruct one merge mechanism while the most
recent instructs its opposite — **one** contradiction, spread across nine files,
with neither side superseding the other in any governed document (*observed*,
per that document). Those figures describe the invariant text this effort
proposes to stop hand-writing.

**Every corpus figure in this document is stated with its scope where it
appears** (*told* — the cycle-9 directive's N2 dispositions this; *observed* for
both counts). Two different counts of the same directory appear in this
document, and they were previously written as though they were one. They are
not, and neither is approximate. The figure above is the **research document's**:
markdown files in `docs/cycles/` as the directory stood at `49bd6ff4` — 91
present, 90 in the measured corpus — and it says nothing about how many of them
are directives. §4's recount is **this document's own**, taken at this revision
against M8's three patterns: **112** markdown files, of which 3 match no
licensed pattern and 2 of those 3 are not directives at all. The two figures
differ because the directory has grown by twenty-one files since the research was
written and because one counts files while the other classifies them. Neither
supersedes the other, and **neither is a count of directives as a class**. One
figure in this document is class-scoped — §4's "exactly one" non-conforming
**directive file**, which §5 carries — and it is derived rather than counted:
three names match no licensed pattern, two of those three are not directives, so
one non-conforming directive file remains. It is stated with that derivation
where it appears, and it is the only place a class figure is asserted.

**Dictated motivating incident, which this spec must state and must prevent
recurring** (*told* for the incident; *observed* for the rule as it now stands):
a parallel directive **stated** a working-tree prohibition and no disposition of
either admitted form. The executor stopped correctly; the omission class is the
target.

**That paragraph is the incident's record, and the requirement it is measured
against is the governed rule at its current form** (*told* — the cycle-17
directive's N3, disposing the cycle-16 gate's N3). It is stated in the past
tense because it records something that happened, and the rule it was originally
narrated against — "requires an assignment — a named directory plus the command
creating it" — was accurate when the cycle-1 directive dictated it and is
narrower than the rule in force now, in three dimensions: the current rule at
`skills/directive-authoring.md` @ `7853525a` admits an **explicit sole-tree
declaration** as an equal branch beside the exclusive assignment, it
additionally requires the disposition to be stated as **its own labelled
statement**, and it fixes the count of such statements at **exactly one per
directive** — the third dimension added by the fifth expedited amendment, below
(*observed*; *told* — the cycle-18 directive's N1 for the re-anchoring). The
incident fails the current rule as it failed its predecessor,
and for the rule's own reason twice over: a prohibition is neither admitted form,
and it is not a labelled disposition statement. Nothing in the rule's currency
softens what this spec must prevent, and `git worktree add ../fiducial-pass2
origin/main` remains what it always was here — an **example** of the assignment
branch, not a statement of the requirement. This is the changed-fact-changes-
everywhere class of Core rule 13, closed at the site where a reader takes the
requirement's shape before reaching §4.

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
is not a disposition." That is the unconditional two-form rule in both the
dimensions earlier cycles found missing: it names the command, and it conditions
the requirement on nothing. It also names the motivating incident's exact failure
in its own words — a prohibition is not a disposition. The file carries
`status: agreed`, and the expedited log's entry for the amendment reads
"2026-08-23 — skills/directive-authoring.md @ 48ad7fd1… — working-tree
disposition made mandatory for every directive"; it reached `origin/main` in
merge commit `820d071e`.

**A fourth expedited amendment then changed that rule, and M3's
labelled-statement anchor is on the amended text** (*observed* for the text and the log entry; the disposition to
anchor there is *told* — the cycle-15 directive's B1). At
`skills/directive-authoring.md` @ `b4a0fa58` the same rule continues: "The
disposition is stated as its own labelled statement, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form is a tooling concern, not this document's." The
expedited log's entry reads "2026-08-23 — skills/directive-authoring.md @
b4a0fa58… — disposition must be its own labelled statement, mechanically
distinguishable from incidental mention of trees or commands", and it reached
`origin/main` in merge commit `7bbb3a71`. The file's body at `b4a0fa58` and at
`origin/main` differ in nothing but the frontmatter lifecycle fields (*observed*,
by diff), so `b4a0fa58` is the content commit for this rule as `48ad7fd1` was
for its predecessor. **This is the amendment that moved M3's anchor**,
and the **fifth** moved M3's count (below). The second and
third amendments left the working-tree rule's text unchanged and neither
disturbed M3 (*observed*, by diff across all three); this one adds the property
M3's check is now anchored on, and M3's row and its supporting section in §4 are
restated over it — the extent apparatus three cycles built is retired with the
problem it solved (§4, "M3's check is over the labelled statement"). The file's
`last-reviewed` pointer has since advanced
four times, and at `origin/main` it reads `reviews/expedited-log.md @
7853525a`, which selects the **fifth** amendment (below). It selected this
**fourth**, `b4a0fa58`, before that, and the **third**,
`6179221a` — the Naming change that requires a time component, and that M8's
timestamp rule turns on (§4) — before that, and the **second**, `83b60511`, the
numbered cycle form, before that (*observed*, all five).

**A fifth expedited amendment has since fixed the count, and M3's exactly-one
clause is anchored on it** (*observed* for the text, the log entry, and the
merge; the disposition to re-anchor is *told* — the cycle-18 directive's N1,
disposing the cycle-17 gate's N1). At `skills/directive-authoring.md` @
`7853525a` the same rule reads: "The disposition is stated as its own labelled
statement, **exactly one per directive**, mechanically distinguishable from
incidental mention of trees or commands elsewhere in the file; the label's fixed
form is a tooling concern, not this document's" — the emphasis this document's,
the sentence quoted whole in M3's row. The amendment inserts exactly the phrase
"exactly one per directive," into the labelled-statement clause and changes
nothing else in the file's body (*observed*, by diff against `b4a0fa58`). The
expedited log's entry reads "2026-08-23 — skills/directive-authoring.md @
7853525aedf831bcc07da3264c3af7a91825b048 — exactly one labelled disposition
statement per directive", and it reached `origin/main` in merge commit
`b5fc675c`. The file's body at `7853525a` and at `origin/main` differ in nothing
but the frontmatter lifecycle fields (*observed*, by diff), so `7853525a` is the
content commit for this rule as `b4a0fa58` was for its predecessor. **What this
closes.** M3's exactly-one count was dictated by the cycle-17 directive @
`7010e8ff` and stood for exactly one cycle as a requirement no governed file
stated — an exposure this document **disclosed** at §7 and AC-DT-13 rather than
absorbing, and the exposure the cycle-16 and cycle-17 gates each filed. The
count now reads off the governed sentence; the disclosure is **removed** at both
sites rather than softened, and the every-element-governed claims at §7's "Not
accepted" and at AC-DT-13 are true as written again (§4, "The count is exactly
one"). The **fence exclusion** is untouched by the amendment and remains this
document's, which §4 states where the check is grounded rather than leaving it
to be inferred from the amendment's arrival. **The gap the cycle-18 gate then
read between the governed count and M3's is closed by reading rather than by a
sixth amendment** (*told* — the cycle-19 directive's N1, scoped to **carried**
wording by `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @
`5ea201e6`, N2): a fenced instance of carried wording is a **mention** rather
than a statement, so for the shape that gate described the two counts return the
same number (§4, "The count is exactly one").

Two citation notes, stated because M2 below is about exactly this discipline.
First, `48ad7fd1` is the **content commit** — the commit that introduced the rule
text — and is the SHA the expedited log uses to select the agreement. It is not
the last commit touching the file: that is now `d4a3158b`, a frontmatter-only
status transition following the **fifth** amendment, having been `7f321a07`
after the fourth, `54a721c2`
after the third, `14bc7c97` after the second, and `511b4dca` after the first
(*observed*, all six). This document cites content commits, as the log does —
`48ad7fd1` for the working-tree rule's two-form requirement, `b4a0fa58` for the
same rule's labelled-statement requirement, `7853525a` for the same rule's
**exactly-one count**,
`83b60511` for the Naming rule's numbered cycle form, and `6179221a` for the
Naming rule's time component — and M2's derivation is narrowed accordingly (§4,
"M2's Derived-from is narrowed"), because a check enforcing lastness would fail
all five of these citations and the log's own convention with them. Second, the
earlier cycles' reading was accurate when made: at `27ca4560` the sentence read
"Two sessions sharing a tree mutate each other's preconditions. Prefer not
splitting; where unavoidable, state the tree assignment in each
directive," which required the assignment to be stated, did not require the
command, and conditioned the requirement on splitting (*observed*). The amendment
closed both gaps, and the fourth amendment at `b4a0fa58` tightened the rule
again rather than reopening either, as the fifth at `7853525a` did after it. G6
is therefore satisfied for M3 as of
`48ad7fd1` for the two-form requirement, `b4a0fa58` for the
labelled-statement requirement, and `7853525a` for the exactly-one count, and M3
carries no standing qualification
anywhere in this document.

**Purpose** (*told* — dictated). Two tools, together: `bin/directive` shrinks the
freehand surface by emitting the invariant text from committed sources, and
`bin/check-directive` gates what remains by failing an executor's first act on a
directive missing a required element.

## 2. Users and use cases

**Primary actor — the decision session**, authoring a directive. It runs
`bin/directive`, receives a skeleton whose invariant sections are already filled
from committed repo text, and writes only the task-specific middle **and the
working-tree disposition's author region** — into which the generator has
already emitted the label, so what the author supplies there is the statement's
**content** (§4 G3; *told* — the cycle-17 directive's B1). **Two freehand regions, not
one** (*told* — the cycle-11 directive's N2 dispositions this; the cycle-10
gate's N2 is the finding). The one-region phrasing this replaces predates the
cycle-10 slot split, and after that split this sentence was the last site in the
document still stating one region where J1, G2, G3, G11, and AC-DT-18 state two.
It understated the author's freehand surface by exactly the element the motivating
incident is about, so a reader taking §2 as the actor description concluded the
disposition was generator-supplied end to end — the G1-side half of the dual
classification cycle 9 filed as blocking, still standing in the one section that
was not on that finding's location list. Where the
directive is a reviewer-gated spec-review cycle, it runs the same tool in the mode
that replaces today's `bin/cycle-open` — which emits the **same disposition
slot**, so the actor's two freehand regions are the same in both modes (*told* —
the cycle-19 directive's B1; §4, "The cycle mode emits the disposition statement
too"). It is the actor whose error rate the
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
  constraints, stop conditions, the working-tree disposition **prompt**, the
  verification steps, the report format, and the claim-label instruction, each
  read from committed repo text at generation time, together with a
  **disposition author region** beneath that prompt carrying the **label over an
  empty content slot** (§4 G3); fills the task-specific middle and the
  disposition content slot, and no other region; hands the directive to an
  execution session.
- **Expected outcome**: a directive whose invariant text matches the repository's
  current committed text, with the author's freehand contribution confined to the
  **task-specific middle and the disposition author region** — the two regions §2,
  G2, G11, and AC-DT-18 name, and no others. This line carried the same one-region
  phrasing §2 did, and is corrected with it under Core rule 13 (*told* — the
  cycle-11 directive's N2 directs the correction "everywhere it appears").
  **A skeleton whose disposition content slot is filled faithfully passes the
  lint** (*told* — the cycle-17 directive's B1, disposing the cycle-16 gate's
  B1). The generator emits the label M3 matches, in the form M3 matches it, so
  the author supplies content and nothing else and is never asked to reconstruct
  a form the skeleton did not show them. **The property rests on G3's
  generated-skeleton invariant** — that the skeleton as emitted carries exactly
  one unfenced labelled disposition statement whatever committed text it also
  sources (*told* — the cycle-18 directive's B1, disposing the cycle-17 gate's
  B1, which found this property asserted here and at J2 with nothing in the
  document requiring it of the generator). That property is stated here as an
  expected outcome of this journey because it is the one the two tools have to
  share: J1 produces what J2 checks.

### J2 — the executor's first act clears the lint

- **Actor**: execution session.
- **Trigger**: the session's first act under a directive.
- **Steps**: writes the directive file, runs `bin/check-directive` against it,
  and — on exit 0 — commits and pushes as it does today.
- **Expected outcome**: exit 0, plus a statement of which elements were checked
  and which properties were not, so the pass is not read as broader than it is.
  For a directive generated by `bin/directive` and filled as J1 describes, the
  **M3 half of that exit is guaranteed by construction** rather than by the
  author's care (*told* — the cycle-17 directive's B1; §4, "The two generated
  cases") — the guarantee resting on **G3's generated-skeleton invariant**, which
  fixes the emitted file's count of unfenced labelled disposition statements at
  one whatever committed text the skeleton sources (*told* — the cycle-18
  directive's B1). The generator and the lint cannot disagree about the label,
  because one of them fixes it and the other matches what it emitted — **which
  holds only if the form is fixed once, in one committed definition both tools
  read**, a property **§8 Q9** states that the TRD's resolution must satisfy
  rather than one this document can establish on its own (*told* — the cycle-18
  directive's N2, disposing the cycle-17 gate's N2). A generator/lint
  pair that lost that property would be a defect in this document, surfaced
  under the conflict rule in §4's "Mode scoping", which reaches conflicts
  between this document's own goals and not only conflicts with a preserved
  AC-CO criterion (*told* — the cycle-17 directive's N4).

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
  presence-and-form test over **labelled disposition statements** (§4, M3's row;
  §4, "M3's check is over the labelled statement") — fails. It carries **no
  labelled disposition statement**, so it fails whatever else in the file
  mentions a tree or a command, and the check needs no reading of **which region**
  of the file anything sits in. A skeleton generated for that directive and left
  **unfilled** fails too, though on the other half of the check: the prompt region
  names both admitted forms but is not a labelled statement, and the author region
  carries the emitted label over a **blank content slot**, so the file carries
  exactly one labelled disposition statement carrying **neither** admitted form
  and fails on form-membership (*told* — the cycle-17 directive's B1; §4, "The two
  generated cases"). Both routes to this journey are mechanical and neither turns
  on reading the author's intent.

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

**The governing contract for what moves, and where each half of it lives**
(*observed* for the sources; the disposition to name them is *told* — cycle-3
directive B2, re-anchored by the cycle-9 directive's B1). `bin/cycle-open` is not
ungoverned code. `docs/packages/package-a-spec.md` governs it in **two**
sections, and this document cites each at a revision where the cited text
exists: **§3.6 specifies the CLI and carries AC-CO-1 through AC-CO-11**, and
**§8.2 carries AC-CO-12**, both at `docs/packages/package-a-spec.md` @
`768bbe3b` — the last commit touching that path, and a revision at which all
twelve exist together. `bin/tests/test_cycle_open.py` implements
them, referring to `AC-CO-` identifiers 34 times. AC-CO-3 fixes the skeleton's
structure — the `# Cycle <n> Directive — <title>` heading, the `Date:` line, the
`Documents in scope:` list of `- <path> @ <full sha>` entries, a `## Decisions`
section with a commented placeholder carrying `Finding: / Resolution: /
Dictated wording:`, `## Deferred / out of scope`, and `## Execution notes` — and
AC-CO-4 fixes the SHA rule. Those are precisely the behaviours the migration moves,
and until this cycle this document named the tool without naming what governs it.

**The anchor was wrong until this cycle, in both coordinates, and the stale one
is not carried forward** (*told* — the cycle-9 directive's B1 dispositions this;
*observed* for the verification). From cycle 2 until this revision, this
document stated that §3.6 "carries AC-CO-1 through AC-CO-12" and pinned
`434e5921` as the only SHA it ever gave that file. Neither half held. §3.6 ends at **AC-CO-11**; and
`434e5921` contains exactly eleven `AC-CO-` entries and **no AC-CO-12 at all**,
so a reader following the one citation this document offered found nothing where
it pointed. The substance asserted *about* AC-CO-12 — that it is a precondition
refusal, and that an absolute `--out` exits 2 — was right throughout; only its
address was wrong. The wording entered in this effort's own cycle-2 review
artifact and was carried through five further gates written by the same session
that authored the revisions, and cycle 8 — the first gate written independently —
is where it was found (*told*, per that artifact's B1 and O1). Every place this
document relies on AC-CO-12, and every place it relies on AC-CO-1, now names
`768bbe3b`; `434e5921` is retained nowhere as an anchor for text it does not
contain.

**AC-CO-12, quoted whole**, as this document requires of every AC-CO criterion it
relies on (`docs/packages/package-a-spec.md` §8.2 @ `768bbe3b`, *observed*):
"**AC-CO-12** *(F4; wording corrected at the second re-gate)* `--out` is
interpreted **relative to the repo root**, not to the current working directory,
and **any absolute path is refused with exit 2** — including one that happens to
fall inside the repo — as is any path escaping the root via `..`." The two
parenthetical notes that follow it in §8.2 record the defect history that
produced the criterion and state no further requirement.

**§8.2 amends none of AC-CO-1 through AC-CO-11** (*told* — the cycle-9
directive's B1 requires this be stated; the provenance is the cycle-8 gate,
`reviews/directive-tooling-cycle-8.md` @ `e8bf561c`, finding B1, which verified
it; corroborated *observed* at this revision, two independent ways). §8's own
preamble enumerates the pre-existing ids appearing in that section as
**cross-references, not additions** — `AC-CF-5`, `AC-CO-9`, `AC-FA-11`,
`AC-MG-13`, `AC-SC-2`, `AC-X-5` — and `AC-CO-9` is the only `AC-CO` id among
them. And §3.6 is **byte-identical** at `434e5921` and at `768bbe3b`, the
red-gate revision and the last-touching one, so nothing in §8 edited it in place
either. This is recorded rather than left to inference: a reader who finds one
preserved criterion inside a section headed "Gate findings and **revised**
acceptance criteria" has no way to know the other eleven are untouched, and
"preserved intact" is a claim about all twelve.

**The disposition of that contract: preserved intact, under the cycle mode**
(*told* — dictated). AC-CO-1 through AC-CO-12 — §3.6's eleven and §8.2's
twelfth, at `768bbe3b` — are neither superseded nor split. Those two sections
together remain the authoritative acceptance-criteria
artifact for the behaviour they specify, and the cycle mode of `bin/directive`
satisfies it unchanged: the same filename contract (AC-CO-1, both of its
branches — which is why M8 admits three patterns), the same skeleton structure
(AC-CO-3) — which the cycle mode emits **and extends**, by the disposition slot
and the source manifest, without amending or narrowing the criterion (below,
"The cycle mode emits the disposition statement too") — the same SHA rule
(AC-CO-4), the same refusals, and the same `--out` and bundle behaviour wherever
the TRD lands those. `bin/tests/test_cycle_open.py` is the **named test surface
that must stay green through the migration**: it is the executable statement of the
contract, and a migration that reds it has changed the contract rather than moved
it (AC-DT-15). What the TRD may decide is where those criteria are *invoked* from —
which binary, which mode — not what they require.

**The cycle mode emits the disposition statement too, and the preserved criteria
are untouched by it** (*told* — the cycle-19 directive
`docs/cycles/directive-tooling-spec-19-20260824T061718Z.md` @ `c05efadd`, B1,
disposing the cycle-18 gate's B1; **Dave's ruling**, taken in that directive
because §4's conflict rule reserves the resolution to a dictated disposition
rather than to a reviewer). The **cycle mode** emits the working-tree
disposition slot — the prompt region, and the author region carrying the
**label over an empty content slot** — exactly as the general mode does (G3;
AC-DT-03). The cycle-mode skeleton is therefore AC-CO-3's structure **plus**
that slot, and every criterion AC-CO-1 through AC-CO-12 states is satisfied
unchanged.

**The conflict this resolves, recorded where it was filed.** The cycle-18 gate
found three commitments of which at most two could hold: that the cycle mode
preserves AC-CO-3's structure whole; that a generated skeleton carries exactly
one unfenced labelled disposition statement, **in either mode** (G3's
generated-skeleton invariant); and that M3 is unconditional over every directive
while DEC-000160 puts `bin/check-directive` inside the first act for every
directive class, **reviewer-gated cycle directives included** (§2). Read with
AC-CO-3's enumeration as exhaustive, a conforming cycle-mode skeleton carries
**zero** labelled disposition statements and fails M3 at the executor's first
act — the same generator/lint defect class the cycle-16 and cycle-17 gates each
filed as blocking, in the other mode. The invariant did not create that
conflict; it made a latent one unignorable.

**The ground of the ruling.** The governed requirement reaches this class in
fact, not only in form: reviewer-gated cycle directives **demonstrably use
working trees**. This effort's own cycle directives are the standing instance —
the cycle-15, cycle-17, cycle-18, and cycle-19 directives each carry an
exclusive working-tree assignment naming a directory and the `git worktree add`
that creates it (*observed*, by reading them at this revision). Those files are
hand-authored and carry pattern-1 names; they are reviewer-gated cycle
directives by **class** — the class `skills/spec-review-cycle.md` governs — not
by filename, and the class is what the governed rule and DEC-000160 both range
over. The seven `cycle-<N>-directive.md` files in `docs/cycles/` that
`bin/cycle-open` actually produced carry **no** working-tree disposition at all,
only incidental mentions of a tree in two of them (*observed*, by running over
the corpus at this revision) — which is not a counter-instance but the reason
the mode has to move: those are exactly the files a conforming M3 would fail,
and §4's no-retrofit disposition is why the existing ones are not reopened. A
class that uses working trees is a class `skills/directive-authoring.md`'s first
rule binds
— it says "**every** directive states its working-tree disposition" and states no
class exemption — and DEC-000160 says the same of the lint that checks it. So
the requirement reaches the cycle mode, and the mode that cannot express it is
the one that has to move.

**Which of the two moved: neither preserved criterion did.** The resolution is
that this is an **extension of the emitted structure**, not an amendment of a
preserved criterion. AC-CO-1 through AC-CO-12 constrain what the skeleton
**must contain**; none of them constrains what it **may additionally** contain.
That reading was **verified against all twelve before it was written**, as the
cycle-19 directive requires, and the verification is recorded here rather than
asserted (*observed*, at `docs/packages/package-a-spec.md` @ `768bbe3b` for
§3.6's eleven and §8.2's twelfth): AC-CO-1, -2, -5, -6 govern the filename and
the refusals and say nothing about the skeleton; AC-CO-7, -8, -9, and -12 govern
the bundle and `--out`; AC-CO-11 bounds which **files** the tool writes — "only
the directive and the bundle directory" — not what the directive contains. Two
reach the skeleton's **content** without reaching its **membership**: AC-CO-4
fixes the value of each SHA in the `Documents in scope:` list and AC-CO-10 fixes
the value of the `Date:` line, each constraining an element AC-CO-3 already
enumerates rather than bounding the set of elements. **AC-CO-3 is the only one
that reaches the skeleton's structure — which elements it carries** — and it
states that the skeleton "matches the format in `skills/spec-review-cycle.md`"
followed by an enumeration of what that format carries. It contains **no exhaustiveness clause** — no "and nothing else"
— and the skill it defers to carries **no skeleton format at all**, so AC-CO-3's
own enumeration is the whole of the stated format and there is no second text
that could supply the missing clause (*observed*, at both paths; that the
deferral resolves to nothing is a defect in
`docs/packages/package-a-spec.md` §3.6 rather than in this document, and no
reading here repairs it). Had any criterion forbidden additions, the cycle-19 directive's stop
condition would have fired and this ruling would not have been written; it did
not fire, and that is stated so a later reader can audit the check rather than
trust it.

**The floor reading is corroborated by an addition this document has required
since cycle 2, which no cycle has ever filed as a conflict** (*observed*, at
`decisions/log.md` and `bin/cycle-open`). DEC-000180 states as its consequence
for tooling that the cycle skeleton "emits Route and Model and no Track", and
**AC-DT-14** carries that obligation onto `bin/directive`'s cycle mode. Neither
`Route` nor `Model` appears in AC-CO-3's enumeration, and `render_directive`
(`bin/cycle-open:115`) emits neither today. So a cycle-mode skeleton that is
AC-CO-3's structure **plus** two lines the criterion does not name has been this
document's standing requirement since the **cycle-2** revision, where AC-DT-14
first entered (*observed*, `git log -S 'AC-DT-14'` resolving to `dcfd966`), and
every gate from cycle 3 to cycle 18 — the three independent ones among them —
has read AC-CO-3 beside it without anyone reading the two as in conflict. That is not proof of the floor reading, but it is the
same reading already applied, in the same criterion, at a site nobody contested:
the disposition slot is a second instance, not a first.

**The executable statement of AC-CO-3 agrees, which is what makes this
auditable rather than interpretive** (*observed*, by reading
`bin/tests/test_cycle_open.py` at this revision). The three cases implementing
AC-CO-3 — `test_co3_heading_date_and_scope_list`,
`test_co3_required_sections_are_present`, and
`test_co3_decisions_section_carries_a_commented_placeholder` — are
**presence** assertions: `assertIn` and `assertRegex` over the emitted text,
with no equality assertion over the whole skeleton and no absence assertion
anywhere in the file that reaches skeleton structure. A skeleton carrying the
enumerated elements **and** a disposition slot passes all three. So the
extension does not red the suite AC-DT-15 names, and AC-DT-15 is satisfied by
the same reading rather than by an exception to it.

**What follows for the invariant.** G3's generated-skeleton invariant holds
**uniformly in both modes**, which is what it already said and what it may now
say with a ground: the cycle-mode skeleton carries the emitted label, so it
carries exactly one unfenced labelled disposition statement, and a cycle
directive whose content slot is filled faithfully passes M3 by construction —
the same property J1 and J2 state for the general mode. The **mechanism** by
which either mode holds to the invariant is unchanged and still routed to the
TRD by §8 Q10. **This is not a widening of the migration's scope**: what moves
is still `cycle-open`'s skeleton emission (above), and what the cycle mode emits
beyond it is this document's own goal G3, which the migration carries into the
mode rather than inheriting from `cycle-open`.

**The ruling's reach is stated, because the disposition slot is not the only
region this document's goals add to a generated skeleton.** G11's **source
manifest** is emitted per region, names no mode, and is therefore likewise an
addition AC-CO-3's enumeration does not name — and it stands on the same reading
for the same reason: the enumeration constrains what the skeleton must contain.
So a cycle-mode skeleton is AC-CO-3's structure plus the disposition slot plus
the manifest that names every region of it, and AC-DT-05, AC-DT-18, and AC-DT-03
each bind it in both modes as they already read. What the reading does **not**
license is subtraction: no region AC-CO-3 enumerates may be dropped, reordered
out of the format `skills/spec-review-cycle.md` states, or emitted in a form
`bin/tests/test_cycle_open.py` fails, and a proposal to do any of those is a
change to `docs/packages/package-a-spec.md` §3.6 made there, exactly as §4's
conflict rule already requires.

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
cycle 3 found between this document's goals and the contract it absorbs; the
cycle-5 directive's N3 replaced its precedence clause, below).
`bin/directive` has two modes and they do not carry the same obligations, so a
claim about "the generator" is ambiguous unless it names the mode it binds. The
convention this document adopts, and applies from here on:

- **Cycle mode** — the mode that replaces `bin/cycle-open`. It preserves the
  inherited contract whole: AC-CO-1 through AC-CO-12 — §3.6's AC-CO-1 through
  AC-CO-11 and §8.2's AC-CO-12, at `docs/packages/package-a-spec.md` @
  `768bbe3b` — including their refusals
  (AC-CO-1, -2, -5, -6, -12) and their writes (AC-CO-1 and AC-CO-7, bounded by
  AC-CO-11). **Preserving the contract whole is a claim about the criteria, not
  a claim that the cycle-mode skeleton carries nothing beyond what AC-CO-3
  enumerates**: it also carries the disposition slot and the source manifest, as
  an extension none of the twelve forbids (above, "The cycle mode emits the
  disposition statement too"; *told* — the cycle-19 directive's B1).
- **General mode** — every other invocation. This is the mode G4 and AC-DT-04
  describe, and the mode AC-DT-12(c)'s mutation bound binds.

**A conflict between this document and the preserved contract is a defect in
this document, surfaced at review — not something this scoping resolves** (*told*
— the cycle-5 directive's N3 replaces the cycle-4 precedence clause, which read
"Where a goal or criterion of this document would say otherwise, the preserved
contract governs the cycle mode"). That clause disposed of every such conflict
silently and in one direction, which is the mechanism by which the contradiction
cycle 5 found — AC-CO-1's second filename branch against a two-pattern M8 — would
have been absorbed without anyone seeing it. The rule that replaces it:

- Where a goal or criterion of this document and a preserved AC-CO criterion
  cannot both be satisfied, **neither silently wins**. The conflict is a defect in
  this document and is raised as a blocking finding at the next gate review, and
  it is resolved by a dictated disposition that states, in this document's text,
  which of the two moved and why. Cycle 5's B1 is the demonstrating instance:
  M8 gained a third pattern by disposition, on the record, rather than AC-CO-1
  quietly overriding M8 in the cycle mode or M8 quietly narrowing "preserved
  intact".
- **The rule is not confined to conflicts with a preserved AC-CO criterion**
  (*told* — the cycle-17 directive's N4, disposing the cycle-16 gate's N4). Where
  **any** two of this document's own goals or criteria cannot both be satisfied,
  the conflict is a defect in this document and surfaces the same way: raised as
  a blocking finding at the next gate review, resolved by a dictated disposition
  stated at the goals or criteria it reaches, never absorbed by one side
  silently winning. The class this widening exists for is the
  **generator/lint** conflict — a skeleton `bin/directive` emits that
  `bin/check-directive` fails — which has no AC-CO criterion on either side and
  which the rule as first written did not reach, though three sites cited it for
  exactly that. A silently-absorbed internal conflict is the same failure as a
  silently-absorbed inherited one, which is the reasoning the bullet above
  already rests on. The demonstrating instance is the cycle-16 gate's B1: a
  prompt that named the labelling requirement without the label's form, guiding
  a faithful author into a directive the same binary's lint fails.
- The obligation runs the other way too. A conflict is **not** resolved in this
  document's favour either: no goal or criterion here narrows a preserved AC-CO
  criterion by implication, and a proposal to retire or split one is a change to
  `docs/packages/package-a-spec.md` §3.6 or §8.2, made there, not a reading taken
  here.
- Where a conflict has been dispositioned, the resolution is stated at the goal or
  criterion it reaches, so precedence is a decision on the record rather than a
  default. The **six** found so far **between this document and a preserved
  AC-CO criterion** are stated where they land — the enumeration is scoped to
  that class, the widened rule's internal conflicts being recorded at the goals
  they reach rather than counted here (*told* — the cycle-19 directive's B1,
  which adds the sixth and requires the count be readable): refusals at G4,
  writes at AC-DT-12, and filenames at M8 **three times** — the pattern set in
  cycle 5, where M8 moved to admit AC-CO-1's second branch; the `<SLUG>` character
  class in cycle 7, where M8 moved again to stop rejecting a legal invocation of
  it; and `<SLUG>`'s path structure in cycle 9, where cycle 8's B2 found the
  phrase "what the preserved contract can emit" undecided and the disposition
  fixed it against what AC-CO-1 **licenses**, bounding pattern 3 to one path
  component (§4, "Pattern 3 is bounded by AC-CO-1's destination clause"). The
  third is the first of the three in which M8 moved **inward**, and it is stated
  here so the rule is not read as one that only ever widens this document.
  **The sixth is the first resolved with neither side moving**, and it is stated
  above under "The cycle mode emits the disposition statement too" (*told* — the
  cycle-19 directive's B1, disposing the cycle-18 gate's B1). G3's
  generated-skeleton invariant and AC-CO-3 appeared to conflict only under a
  reading of AC-CO-3's enumeration as **exhaustive**; the ruling is that the
  enumeration states what the skeleton must contain and not what it may
  additionally contain, so the invariant reaches the cycle mode and no preserved
  criterion is amended, narrowed, or excepted. That the rule admits this outcome
  is not a loophole in it: the rule requires the disposition to state **which of
  the two moved and why**, and "neither, because the conflict rested on a reading
  the criterion does not state" is such a statement — provided the reading is
  verified against every preserved criterion rather than assumed, which is why
  the verification is recorded there in extension rather than asserted.

**Reading either mode's claims.** Two claims here were previously written as
though they were global, and both now name their mode: **G4 / AC-DT-04** (no
refusal path) and **AC-DT-12** (no working-tree mutation). Reading either
globally is what made them contradict
AC-DT-15, and the scoping is what removes the contradiction rather than
weakening either claim where it applies. **AC-DT-15 is not scoped by this
convention and is not narrowed by it**: `bin/tests/test_cycle_open.py` must stay
green through the migration, whole, and it is the cycle mode that suite
exercises.

### Scope split with the TRD

**What this document decides, and what the TRD decides** (*told* — the cycle-18
directive `docs/cycles/directive-tooling-spec-18-20260824T042409Z.md` @
`5ffe9ed6`, whose **descope** governs this revision as it did the last — the
cycle-19 directive dispositions no change to it, and its N2 records that the
questions the split leaves open are the split's design rather than a gap in it
(§8 Q9)). This PRD carries goals,
journeys, risk posture, and the criteria decidable at PRD level. Three classes of
generator/lint interaction mechanic are **not** decided here, and each carries a
**named route** to the TRD stage: the label's **lexical form**, routed by **§8
Q9**, which also fixes the single-source property that resolution must satisfy;
the **mechanism** by which a generated skeleton holds to G3's
generated-skeleton invariant — fencing of sourced text, bounds on the
disposition prompt's content, or another means — routed by **§8 Q10**; and any
**markdown sensitivity** of M3's match beyond the fence exclusion, routed **at
M3's row**, which names the TRD stage and states the one sensitivity this
document does fix. A route is either a §8 question or a routing stated at the
site, and both forms are used here; what makes it a route is that it names what
resolves the decision, not where it is written.

**Where a mechanism is routed, the property it must secure is stated here.** The
split is not silence: this document fixes the invariant or the property, and
leaves the means open, so a reader looking for the means finds a question naming
what resolves it, and a TRD taking the decision has something to satisfy rather
than a blank. **The test this split applies at review** is that pair — a routed
mechanism carries a **named route** and a **PRD-level property** stating what its
resolution must achieve. A mechanism with neither is a defect in
this document; a mechanism with both is a deferral this document intends, and not
a gap in it. Stated here because the previous two cycles each moved a mechanism
into and back out of the PRD, and a reviewer needs the boundary written down
rather than reconstructed.

**This section does not claim to enumerate every TRD-stage decision in the
document, and the test above is not applied to every one.** G11 routes the
skeleton's **marker syntax** at its own site, G5 routes the failing-path
invocation point to Q2, and §8 carries further questions whose resolver is Dave
rather than a stage. What this section governs is the one class the cycle-18
descope names — **generator/lint interaction mechanics**, where a decision taken
one way makes one binary's output fail the other's check — and the test above is
the test for that class.

### Functional goals

#### `bin/directive` — the generator

- **G1 — Invariant text is read, never hardcoded.** Every invariant section the
  skeleton carries — sandbox constraints, stop conditions, the working-tree
  disposition **prompt**, verification steps, report format, claim labels — is
  read from committed repo text at generation time (*told* — dictated). The
  entry in that enumeration is the **prompt region** of the split slot G3 states
  — the half that carries the requirement that a disposition be stated and the
  two legal forms `skills/directive-authoring.md` names — and it is invariant
  for the same reason every other entry is: its text is governed, and a tool
  holding it as a constant drifts from the file that governs it. The
  **disposition author region** beneath it is not an invariant section and this
  enumeration does not reach it (*told* — the cycle-10 directive's B1). A string constant
  in the tool holding text that also lives in a governed file is the defect this
  goal exists to prevent; it recreates, one layer down, the drift the problem
  statement describes.
- **G2 — The author writes only the middle.** The skeleton's task-specific region
  is the only region the decision session composes freehand, alongside the
  **author region** of the disposition slot G3 requires (*told* — dictated).
  **This goal was narrowed in cycle 9, and the narrowing is recorded here rather
  than left to a diff** (*told* — the cycle-9 directive's O5 licensed the
  narrowing; the cycle-10 directive's O5 requires this line). Through cycle 8 the
  goal read "is the only region the decision session composes freehand", full
  stop, which contradicted J1 — where the author has always filled the
  disposition as well — and the clause naming the disposition was added to
  correct it. The narrowing widens the goal by exactly one region and says so,
  which is this document's convention at every other scope change (M8, §5's
  third outcome, AC-DT-13); recording it is also what made the dual
  classification the cycle-9 gate raised as B1 visible, since the added clause
  put a **goal** on the author-composed side of a slot G1 called invariant.
  Until cycle 9 this goal
  carried no acceptance criterion of its own and was testable only through G1,
  G3, and G11; **AC-DT-18** now states it directly, by fixing how many freehand
  regions a generated skeleton has and which they are — which none of those
  three states (*told* — the cycle-9 directive's O5).
- **G3 — The working-tree disposition is a slot, not prose, and the slot is two
  regions.** It is emitted as a
  named, structurally-present field admitting exactly the two forms §1
  names, so that omitting it is visible rather than silent. This is the goal that
  addresses the motivating incident directly: an omission the author cannot see is
  the failure mode, and a slot makes the omission a blank rather than an absence.

  **The slot divides into two regions, and each carries exactly one
  classification in G11's manifest** (*told* — the cycle-10 directive's B1 is the
  origin of the split; the defect it disposes is the cycle-9 gate's B1):

  - **The disposition prompt** — **invariant**, read from committed text at
    generation time exactly as every other invariant section is (G1). It carries
    the requirement that a disposition be stated, the two legal forms
    `skills/directive-authoring.md` @ `b4a0fa58` names — "either an exclusive
    assignment (a named directory plus the command creating it) or an explicit
    sole-tree declaration. A prohibition is not a disposition." — **and the
    requirement that the disposition be written as its own labelled statement**,
    which is the property M3 checks (*told* — the cycle-15 directive's B1). That
    last part is not optional decoration: a prompt that named the forms and not
    the label would guide an author into a directive the same binary's lint
    fails, which is the generator/lint conflict §4's "Mode scoping" rule exists
    to surface rather than absorb — a class that rule reaches explicitly as of
    this revision, having been scoped to conflicts with a preserved AC-CO
    criterion before it (*told* — the cycle-17 directive's N4, disposing the
    cycle-16 gate's N4, which found this citation outside the rule's stated
    scope). The prompt is **necessary** for the property but not sufficient for
    it: the generator also emits the **label**, which is what makes a faithfully
    filled skeleton pass (AC-DT-03; *told* — the cycle-17 directive's B1). The author
    neither writes it nor edits it, and the manifest entry for it names a
    committed path. **A prompt is not a labelled disposition statement** (*told* —
    the cycle-15 directive's B1, which retires the region scoping this bullet
    carried): the forms it quotes are incidental mention in the governed rule's
    own sense, so a prompt's **naming of the two admitted forms** is outside
    M3's match wherever the region sits and whatever else the file carries (§4,
    M3's row). No manifest is needed to buy that exclusion and none is consulted
    for it.

    **That reading does not by itself fix the skeleton's count** (*told* — the
    cycle-18 directive's B1, disposing the cycle-17 gate's B1). It is a claim
    about what a prompt **is**, and M3 matches **text**: a committed source that
    explains the labelling requirement by **showing** the label would leave the
    reading untouched and still put a second matchable instance in the emitted
    file. The count over a generated skeleton is fixed by the invariant below,
    not by this bullet, and the means by which the generator holds to it is a
    TRD decision §8 Q10 carries.
  - **The disposition author region** — the **author's**, and emitted carrying
    the **label over an empty content slot** (*told* — the cycle-17 directive's
    B1, disposing the cycle-16 gate's B1; this bullet previously read "empty as
    emitted"). The generator emits the TRD-fixed **label** as the **marker that
    begins this region** — which is what G11's manifest already names per
    emitted region (AC-DT-05) — and leaves the **content slot** beneath it
    blank. The author writes the content, the actual exclusive assignment or
    sole-tree declaration for this directive, and label plus content is the
    **labelled statement** the governed rule requires
    (`skills/directive-authoring.md` @ `b4a0fa58`; M3's row).

    **The label is not governed text, and G1 does not reach it.** The governed
    rule delegates the label's fixed form to tooling in its own words — "the
    label's fixed form is a tooling concern, not this document's" — so no
    committed governed file holds it, and a generator emitting it recreates no
    drift, which is the single test G1 applies. G1's prohibition is on a tool
    holding text that **also lives in a governed file**; a TRD-fixed label lives
    in no such file by the governed rule's own disposition.

    **The region's classification does not move, and the two-region split
    stands.** The label is the region's **marker**, not its content, so this
    region remains one of the two freehand regions G2 names, the only part of the
    slot J1 hands to the author, author-marked in the manifest, and the region
    AC-DT-18 counts as author-marked; AC-DT-05's partition attributes the
    marker's bytes as it attributes every other region's marker. What changed is
    only what AC-DT-03 asserts of the region **as emitted** — a present label
    over a blank content slot, rather than a blank region — and the dual
    classification the split exists to prevent is not reintroduced, because no
    region is claimed by both classifications.

    **It is not an extent M3's search is scoped to**, because M3
    has no **region** extent: what M3 matches is the labelled statement itself,
    wherever in the file the author put it (*told* — the cycle-15 directive's B1,
    which retires the scoping the cycle-11 and cycle-14 dispositions stated
    here). M3's one structural sensitivity is the **fence exclusion** (M3's row;
    §4, "The count is exactly one"), and that is a property of a passage's
    markdown context rather than of a region of the skeleton.

  **G3's generated-skeleton invariant: exactly one unfenced labelled disposition
  statement** (*told* — the cycle-18 directive's B1, disposing the cycle-17
  gate's B1). Whatever committed text a generated skeleton carries — the
  disposition prompt, the sandbox constraints, the stop conditions, the report
  format, and anything any of them quotes — the skeleton **as emitted** contains
  **exactly one unfenced labelled disposition statement**: the one the generator
  emits over the empty content slot. The count is over the **whole emitted
  file**, not over the author region, and it holds of every skeleton the
  generator produces, in either mode. This is a requirement on the
  **generator**, stated at goal level because it is a property of what the tool
  emits rather than of any one region of it, and **AC-DT-03** is where it is
  checked.

  **"In either mode" now has a ground, and the cycle mode is where it was
  missing** (*told* — the cycle-19 directive's B1, disposing the cycle-18 gate's
  B1; **Dave's ruling**). The invariant is a count of labelled statements in the
  emitted file, so it presupposes that the emitted file has one — and the cycle
  mode preserves AC-CO-3's structure, which enumerates no disposition region.
  Read with that enumeration as exhaustive, the cycle-mode skeleton carried
  **zero** and the invariant could not hold of it. The ruling is that the
  **cycle mode emits the slot too**, as an extension of the emitted structure
  with every preserved AC-CO criterion untouched, and §4's "The cycle mode emits
  the disposition statement too" states it, its ground, and the verification
  against AC-CO-1 through AC-CO-12 that the ruling was checked against before
  being written. This goal states the invariant uniformly for both modes because
  it now holds uniformly in both.

  **The passes-by-construction property rests on this invariant.** J1 and J2
  state that a skeleton whose content slot is filled faithfully passes the lint,
  and that follows from the invariant directly: the emitted file carries one
  unfenced labelled statement, the author supplies its content, and content
  faithfully supplied is one admitted form — count one, form-member, exit 0 (§4,
  "The two generated cases"). It does **not** rest on the prompt bullet's
  categorical reading above. That reading stands as the governed rule's own
  incidental-mention distinction, but it is a claim about what a prompt **is**
  where M3 matches **text**, and the cycle-17 gate's B1 is the finding that a
  prompt whose committed source shows the label satisfies every criterion this
  document states and still emits a skeleton the same binary's lint fails. The
  invariant closes that by fixing the count over the emitted file rather than by
  arguing about any one region's status.

  **How the generator holds to the invariant is a TRD decision** (*told* — the
  cycle-18 directive's B1, via the descope; §4, "Scope split with the TRD"). The
  candidates differ materially — the committed source the prompt is read from
  shows the label only inside a **fenced** block, which M3 does not match; or
  that source is **bounded** so it does not show the label at all; or the
  generator **fences sourced text** as it emits it, which reaches every invariant
  region rather than the prompt alone — and each constrains Q1's answer
  differently. Choosing among them is a mechanism at the granularity this
  document routes rather than fixes. **§8 Q10** carries the question and names
  what resolves it; this goal states the invariant and states nothing about the
  means.

  **The split is what makes the slot classifiable, and the dual classification it
  replaces was a real defect rather than a wording infelicity.** Before it, G1
  listed the slot among the invariant sections read from committed text while
  G3, J1, and AC-DT-03 had the author fill it, and G11's manifest admits each
  region as one or the other and not both. Two consequences followed and both
  are closed by the split: §5's first measurement summed the author's own
  disposition text into the generator-supplied share — biasing the signal
  upward by exactly the bytes of the element this spec exists to make visible —
  and AC-DT-05's partition yielded two different numbers for the same landed
  file depending on which classification an implementer took (*told* — the
  cycle-9 gate's B1, which raised this as blocking and declined to pick a
  disposition because picking one is not a reviewer's call). The prompt is
  invariant because its text is governed and drifts if hardcoded; the author
  region is the author's because the disposition itself is a judgment no
  committed file can supply. **Every site in this document that names the slot
  names which region it means**, and no site retains the dual classification:
  G1 and this goal, J1, G11, §5's first outcome, AC-DT-03, AC-DT-05, and
  AC-DT-18. **The split survives the retirement of M3's search extent, because
  it was never M3's** (*told* — the cycle-15 directive's B1): what it makes
  well-defined is G11's partition, AC-DT-05's one-share-per-skeleton property,
  AC-DT-18's count of author-marked regions, and §5's first measurement, none of
  which M3 ever consumed. M3's retired scoping borrowed the split; it did not
  motivate it.
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
  skeleton — each invariant section, the working-tree disposition **prompt**, the
  **disposition author region**, and the task-specific author region alike —
  under a named, stable section marker of its own choosing, and the manifest names
  every region in emission order, each entry carrying either the committed path
  that region was read from or an explicit marking that the region is an **author
  region**. **Exactly one classification per entry, never both and never
  neither** — which is well-defined at the working-tree disposition because G3
  splits it: the disposition **prompt** is an entry naming a committed path, the
  disposition **author region** is an author-marked entry, and no entry is both
  (*told* — the cycle-10 directive's B1). The manifest therefore admits
  **exactly two** author-marked regions, the task-specific region and the
  disposition author region, which AC-DT-18 distinguishes by name so that the
  count is checkable rather than implied. Because every region is marked and the manifest enumerates them all, the
  markers partition the whole file: a region's extent runs from its own marker to
  the next marker or to end of file, with nothing falling between two regions. The
  generator-supplied share is the sum of the extents whose entries name a committed
  path. Marking the author regions is the part that makes this work, and it is
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
  question; that every region carries one, and that the manifest names it, is
  not. **The manifest is an output of `bin/directive` and an input to nothing
  the lint does** (*told* — the cycle-15 directive's B1, which retires M3's
  search predicate and with it the input-contract clause the cycle-14
  directive's N2 stated here). `bin/check-directive` reads no manifest at all:
  M3 matches labelled disposition statements and consults no region, no marker,
  and no manifest entry (§4, M3's row), and no other element consumed one. The
  manifest's dependents are therefore **three, and all three are properties of
  the generator** — AC-DT-02's static check over the generator's own source,
  §5's first measurement by way of AC-DT-05's partition, and AC-DT-18's count of
  author-marked entries in a freshly generated skeleton. None of them is a check
  the lint performs. The PRD-level obligation that both binaries read one
  manifest form is **withdrawn with the element that needed it**, and that is
  stated here rather than left to a diff, because a prior cycle's dictated
  disposition is being vacated by this one.

#### `bin/check-directive` — the lint

- **G5 — It runs inside the existing first act.** Write the directive file, lint
  it, commit, push (*told* — dictated; the act itself is DEC-000160's). The lint
  adds no new step to the executor's sequence; it adds a condition to a step that
  already exists. **AC-DT-19** states the half of this goal a PRD can carry — the
  tool-side precondition that makes the placement possible, namely that the lint
  runs against an uncommitted file on disk and needs nothing the first act has
  not yet produced. The other half is not testable here and is marked for the
  TRD stage: where the invocation sits on the **failing** path is Q2, and the
  ordering of the executor's four steps is a property of the execution session's
  procedure rather than of either tool (*told* — the cycle-9 directive's O5).
- **G6 — The required-element set derives from committed governed text.** Its
  sources are `docs/global-context/core.md`'s Vocabulary,
  `docs/global-context/decision-layer.md` rule 14, `skills/directive-authoring.md`,
  and `decisions/log.md` (*told* — dictated for the first three; the decision log
  was added in cycle 2 per that cycle's B3). No requirement is invented in the
  tool. A requirement the tool enforces and no governed file states is a defect in
  the tool, not a stricter tool. The one place this bit is closed: M3's
  unconditional two-form rule is governed text as of
  `skills/directive-authoring.md` @ `48ad7fd1`, its **labelled-statement**
  requirement as of the same file @ `b4a0fa58`, and its **exactly-one count** as
  of the same file @ `7853525a` (§1) — the third of those landing this cycle and
  closing the one exposure this goal carried (*told* — the cycle-18 directive's
  N1) — so every element M1–M8
  traces to committed text and none is held back. The label's fixed **lexical
  form** is the one part M3 does not read off that text, and it does not have
  to: the governed sentence assigns it — "the label's fixed form is a tooling
  concern, not this document's" — so a TRD that fixes one is discharging a
  delegation a governed file makes, not inventing a requirement (M3's row;
  AC-DT-13). The goal itself is unchanged and still binds every element added
  later.
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
| M3 | A working-tree disposition is present as **its own labelled statement**, and that statement carries **exactly one** of two forms: an exclusive assignment (a named directory plus the command creating it), or a literal sole-tree declaration. Unconditional — every directive, no parallelism test. **The check is over labelled disposition statements, and this row is where it is fixed: exactly one labelled disposition statement is present in the file outside fenced code blocks, and it carries exactly one of the two admitted forms. Zero such statements fails, whatever else the file mentions. Two or more fails. Text inside a fenced code block is outside M3's match entirely, labelled or not. A labelled statement carrying neither admitted form — a prohibition, for instance — fails on form-membership, and so does one carrying both.** The **exactly-one count is governed text** and is anchored on it: `skills/directive-authoring.md` @ `7853525a`, whose fifth expedited amendment inserts "exactly one per directive" into the labelled-statement clause (*observed* for the text; *told* — the cycle-18 directive `docs/cycles/directive-tooling-spec-18-20260824T042409Z.md` @ `5ffe9ed6`, N1, disposing the cycle-17 gate's N1, which found the count ungoverned while it was dictated by the cycle-17 directive @ `7010e8ff`; §1). The **fence exclusion** is **not** governed text: it remains this document's, dictated by the cycle-17 directive @ `7010e8ff` (N1, its origin), and it **narrows** what the lint matches rather than adding a requirement the lint enforces, so it creates no exposure against G6 and none is carried (§4, "The count is exactly one"; §7, "Not accepted"; AC-DT-13). It is nonetheless the **mechanical form of a line the governed rule draws** where the fenced text is **carried** wording, such an instance being a **mention** rather than a statement, which is why this row's unfenced count and the governed "exactly one per directive" return the same number over the shapes carriage produces; where an author fences their **own** sole statement the two counts differ, this row counting zero against the governed one, and that difference runs in the **false-positive** direction and is §7's accepted residual rather than an exposure (*told* — the cycle-19 directive's N1 for the reading and `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`, N2, for its scoping — a **consequential update under Core rule 13** at a site that directive did not name, this row governing every other mention of M3; §4, "The count is exactly one"; §7). **The fence exclusion is M3's only markdown sensitivity at this level**; any finer markdown-awareness — indentation, list nesting, block quotes, HTML blocks — is a **TRD** concern and is not fixed here. Text instantiating an admitted form **without** the label is not a disposition for M3's purposes and is outside M3's match; that exclusion is the governed rule's own rather than this document's normalization of it, the rule requiring the disposition to be stated "as its own labelled statement, mechanically distinguishable from incidental mention of trees or commands elsewhere in the file". **M3's contract at this level is label-presence and form-membership, and nothing else**; the label's fixed **lexical form** is a **TRD decision**, and the delegation is the governed rule's, which states that "the label's fixed form is a tooling concern, not this document's" — so a TRD fixing one discharges a delegation a governed file makes rather than inventing a requirement (G6, AC-DT-13). Because the match is over labelled statements, **no part of M3 turns on which region of the file the statement sits in**: M3 has no region extent, no manifest scoping, and no whole-file fallback, and the locatability predicate, the region-scoped branch, and the whole-file branch the three prior dispositions built are **retired** (*told* — the cycle-15 directive `docs/cycles/directive-tooling-spec-15-20260824T021751Z.md` @ `438fa4f5`, B1, which is the origin of this check; the retired region scoping originates in the cycle-11 directive's B1, the whole-file fallback in the cycle-12 directive's B1, and the predicate joining them in the cycle-14 directive's B1, and the defect the labelled-statement anchor closes is the cycle-14 gate's B1). **M3 remains total by construction**: every file either carries exactly one unfenced labelled disposition statement carrying an admitted form or does not, with no third outcome, so M3 is never an element the lint cannot decide (AC-DT-10). Every other mention of M3 in this document is a **reference to this row** and states no test of its own; where any of them appears to say something different, this row governs, and the difference is a defect in that site rather than a second rule. See "M3's check is over the labelled statement" below the table | `skills/directive-authoring.md` @ `7853525a`, "Writing the directive file", first rule, quoted whole at its current form: "Every directive states its working-tree disposition — either an exclusive assignment (a named directory plus the command creating it) or an explicit sole-tree declaration. A prohibition is not a disposition. The disposition is stated as its own labelled statement, exactly one per directive, mechanically distinguishable from incidental mention of trees or commands elsewhere in the file; the label's fixed form is a tooling concern, not this document's. Two sessions sharing a tree mutate each other's preconditions; prefer not splitting work across trees." Three content commits build that sentence and this document cites each where it states its requirement: `48ad7fd1` the two-form rule, `b4a0fa58` the labelled-statement rule, `7853525a` the exactly-one count (§1). **The quotation reaches the end of the governed bullet as of this revision**, the previous form having stopped three sentences in while claiming wholeness (*told* — `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`, N1, disposing the cycle-19 gate's N1; *observed*, matched by running against `skills/directive-authoring.md` at `origin/main`, whose body differs from `7853525a`'s in nothing but the frontmatter lifecycle fields). The restored sentence states a rationale and a preference, not a requirement, so nothing M3 enforces, nothing G6 tests, and nothing AC-DT-13 asserts moves with it | **none.** Label-presence, form-membership, the exclusivity of the two forms, and the **exactly-one count** all read off the cited governed sentence, the count as of `skills/directive-authoring.md` @ `7853525a` (*told* — the cycle-18 directive's N1; the qualification this cell carried at the previous revision is removed with the exposure it disclosed). The **fence exclusion** is this document's and is dictated by the cycle-17 directive @ `7010e8ff` (N1), but it narrows M3's match rather than adding a requirement the lint enforces, so it is not a qualification of this kind — see "The count is exactly one" below the table. **The two counts agree over carriage** and this cell's "none" holds without a reading gap: a fenced instance of **carried** wording is a **mention** in the governed rule's own sense rather than a statement, so for the shape the cycle-18 gate described the governed "exactly one per directive" and this row's unfenced count return the same number and no false negative hides behind the exclusion (*told* — the cycle-19 directive `docs/cycles/directive-tooling-spec-19-20260824T061718Z.md` @ `c05efadd`, N1, disposing the cycle-18 gate's N1, **by reading and with no amendment**, scoped to carried wording by `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`, N2 — a **consequential update under Core rule 13** at a site that directive did not name; §4, "The count is exactly one"). Where an author fences their **own** sole statement the counts differ in the **false-positive** direction, which narrows what the lint matches rather than adding a requirement it enforces, so this cell's "none" is unqualified in that direction too (§7) |
| M4 | The stop conditions are present: cannot-execute-as-written, and concurrent tree mutation | Core rules 11 and 15 | none |
| M5 | The first instruction is write-the-directive-file, commit, push, report the SHA | Core Vocabulary, "Execution block" | DEC-000160 fixes this for **every** directive class, so no class exemption exists for the lint to carry |
| M6 | A report section is present and enumerates its required fields | Decision Layer rule 14, "Write it so the returned report is triageable by the next decision session" | none |
| M7 | The claim-label instruction is present | Core rule 6 | none |
| M8 | The directive filename is a member of the **licensed form set**. The name the patterns are matched against is the lint's path argument **resolved to a repository-relative path from the repository root** (AC-DT-19), never the argument as typed. So resolved, it matches **exactly one of three patterns** — `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format with date and time components **both present**, `YYYYMMDDThhmmss`, optionally `Z`-suffixed; or `docs/cycles/cycle-<N>-directive.md`; or `docs/cycles/<SLUG>-directive.md`, `<SLUG>` being **any** slug the preserved contract **licenses** — that is, any **single-component basename**: the pattern states **no character class**, and it admits **no path separator**, because AC-CO-1's destination clause states that the output is written at `docs/cycles/<name>-directive.md` and a separator-bearing name produces a path that is not that destination. A trailing date with no time component is **not** a timestamp for this check. Membership is the **whole** claim: no fourth pattern passes, and M8 asserts nothing about whether the pattern a filename matches is the one that directive's mode should have produced — see "What M8 claims" below the table | pattern 1 from `skills/directive-authoring.md` @ `6179221a`, "Naming": "A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format with date and time components both present (as `20260820T161541`) — except a reviewer-gated cycle directive, which is `docs/cycles/cycle-<n>-directive.md` per its stated convention." Patterns 2 and 3 anchor **directly** on the stated convention that sentence defers to: `docs/packages/package-a-spec.md` §3.6 AC-CO-1 @ `768bbe3b`, quoted whole — "Writes `docs/cycles/cycle-<N>-directive.md` for `--cycle N`, or `docs/cycles/<SLUG>-directive.md` for `--name SLUG`; exactly one of the two is required (exit 2)." Corroborated for pattern 1 by Core rule 14, whose yield clause is what licenses 2 and 3 | none — pattern 3 states **no character class** and **one path component**, and both halves are read off the same cited text: AC-CO-1 states no class, so under G6 a class here would be a requirement the lint enforces and no governed file states (*told* — the cycle-7 directive's B1); and AC-CO-1's destination clause states where the output lands, which is what bounds the name to a single component (*told* — the cycle-9 directive's B2). See "Pattern 3 is bounded by AC-CO-1's destination clause, and by nothing else" below the table |

**M3's check is over the labelled statement, and this section states no test of
its own** (*told* — the cycle-15 directive
`docs/cycles/directive-tooling-spec-15-20260824T021751Z.md` @ `438fa4f5`, B1;
the governed sentence it anchors on is `skills/directive-authoring.md` @
`b4a0fa58`, and the defect the anchor closes is the cycle-14 gate's B1). **The
check is fixed in M3's own row**, which governs on any apparent difference;
everything below is *why* it has the shape it has and *what follows* from it.

**What the anchor is.** The governed rule no longer asks only that a directive
state a disposition. It asks that the disposition be **its own labelled
statement, mechanically distinguishable from incidental mention of trees or
commands elsewhere in the file** (*observed*,
`skills/directive-authoring.md` @ `b4a0fa58`). That sentence does two things a
lint can use. It makes the disposition a **named object in the file** rather
than a shape some sentence may or may not have, so a check can ask whether the
object is present and what form it carries. And it draws the line between the
disposition and incidental mention **in the governed text itself**, so a lint
matching only labelled statements is applying the rule rather than normalizing
it — which is what G6 requires of every element, and which is why the exclusion
of incidental text is cited to the rule and not argued for here.

**What is retired, and why none of it is needed.** Three cycles of dispositions
built an apparatus for deciding *where in the file* M3 should look: a
region-scoped branch (the cycle-11 directive's B1), a whole-file fallback (the
cycle-12 directive's B1), and a locatability predicate over G11's manifest
joining the two (the cycle-14 directive's B1). **All three are retired** (*told*
— the cycle-15 directive's B1). The apparatus existed to solve exactly one
problem: the generator's disposition **prompt** carries the governed sentence
naming both admitted forms, so a check reading the file's text at large counted
the prompt's forms as instances, and could neither pass a correctly-filled
directive nor fail an unfilled one. The label dissolves that problem at its
source. A prompt is not a labelled disposition statement, so it is outside M3's
match whatever it quotes — it is precisely the incidental mention the governed
rule distinguishes. **That reading disposes of the prompt's naming of the two
forms; it does not by itself fix a generated skeleton's count**, which G3's
generated-skeleton invariant does (*told* — the cycle-18 directive's B1). With
no text-at-large match there is nothing for an extent
to bound, and a document keeping the extent apparatus beside the
labelled-statement check would carry two tests where the governed rule states
one.

**The motivating incident's catch is restored, mechanically and
unconditionally.** The cycle-14 gate's B1 found a **false negative** reachable
in the retired whole-file branch: a hand-written directive stating only a
working-tree **prohibition** exited **0** on M3 whenever any other line in the
file — a stop condition, a provenance note — happened to instantiate one
admitted form. Under the labelled-statement check that file carries **zero**
labelled disposition statements and fails, whatever else it mentions. **The
defect is closed by construction, not accepted**: it is not carried into §7, and
§7's residual set is restated without it. The disposition is **none of the three
that finding proposed** — it does not accept the false negative (a), does not
narrow a search extent (b), and does not route an unlocatable disposition to
AC-DT-10 as undecidable (c). An unlabelled disposition is a **failure**, not an
unknown, and the anchor it turns on is carried by the governed rule rather than
by a manifest, so hand-written directives stay inside M3's range at the cost of
a label.

**The two generated cases are decided without any scoping, and the ordinary
generated path passes by construction** (*told* — the cycle-17 directive's B1,
disposing the cycle-16 gate's B1; the invariant it rests on is *told* — the
cycle-18 directive's B1, disposing the cycle-17 gate's B1). The generator emits
the label over an empty content slot (G3, AC-DT-03), and the skeleton it emits
carries **exactly one unfenced labelled disposition statement** whatever
committed text it also sources (G3's generated-skeleton invariant; AC-DT-03).
So a **correctly-filled** skeleton carries exactly one unfenced labelled
statement whose content is one admitted form: count one, form-member, exit
**0**. That is not a coincidence of the
author's care, and — this is what the invariant adds — it is not a coincidence
of which committed text the prompt happened to be read from either. The previous
revision rested the same conclusion on the prompt's categorical exclusion alone,
which is a claim about what a prompt **is** where M3 matches **text** (G3, "The
passes-by-construction property rests on this invariant"). The only thing a faithful author supplies is the **content**, the
label being already present in the exact form M3 matches, so **filling the slot
faithfully is sufficient for M3 to pass** — the property J1 and J2 now state,
and the property the cycle-16 gate's B1 found this document nowhere carried. An
**unfilled** skeleton carries the prompt and the label over a blank content
slot: count one, carrying **neither** admitted form, exit **non-zero**.
**Both cases are cases of either mode** (*told* — the cycle-19 directive's B1;
§4, "The cycle mode emits the disposition statement too"): the cycle mode emits
the slot as the general mode does, so a reviewer-gated cycle directive whose
content slot is filled faithfully passes M3 by construction on the same
reasoning, and an unfilled cycle-mode skeleton fails on form-membership on the
same reasoning. This is stated because until cycle 19 the cycle-mode skeleton
carried no disposition region at all under the reading then in force, and these
two cases silently had only one mode in range.

**The unfilled case is decided on form-membership, not on the count, and that
is what reconciles AC-DT-03 with AC-DT-06's fixture (v).** The previous revision
left two readings of the unfilled skeleton — a file carrying no labelled
statement at all, or one carrying a label with neither form — and stated one at
each criterion, so two implementations conforming to §6 produced different
files. There is now one reading: the generator emits the label, so the file
always carries exactly one labelled statement, and an unfilled slot fails
because its content is neither form. The exit is the same whatever lexical form
the TRD fixes, which is why both criteria can state the case without waiting on
that decision (§8 Q9).

**The count is exactly one, it is scoped outside fenced code blocks, and the two
halves now stand differently** (*told* — the cycle-18 directive
`docs/cycles/directive-tooling-spec-18-20260824T042409Z.md` @ `5ffe9ed6`, N1,
disposing the cycle-17 gate's N1; the fence exclusion and the count both
originate in the cycle-17 directive
`docs/cycles/directive-tooling-spec-17-20260824T033019Z.md` @ `7010e8ff`, N1,
disposing the cycle-16 gate's N1; M3's row is where the check itself is fixed).
The **ground** the disposition states is the authoring corpus the check has to
live in. The same governed skill's fifth authoring rule reads: "**Carry dictated
wording as a pointer** — the source's path and SHA plus its field or section,
never restated — **unless the directive is itself the wording's origin**, in
which case it carries it inline and downstream artifacts point at it"
(*observed*, `skills/directive-authoring.md` at `origin/main`, `:29-32`, quoted
**whole**; the judgment-only table below cites the same rule). That exception is not rare in this effort. A directive that
originates other directives' dispositions — a fixture set, a dictated example,
this document's own directives — carries their labelled statements **inline**,
and carries several at once. Fenced carriage is how such wording travels, so
**fenced text is outside M3's match**: a directive quoting or originating other
labelled statements inside fences states exactly one disposition of its own,
unfenced, and passes. The motivating incident is untouched by the exclusion —
it carries no labelled statement anywhere, fenced or not, and fails on count
zero.

**The count is governed text as of the fifth expedited amendment, and the
reading this document carried for one cycle retires with it** (*told* — the
cycle-18 directive's N1, disposing the cycle-17 gate's N1; *observed* for the
text, the log entry, and the merge). `skills/directive-authoring.md` @
`7853525a` states the rule as: "The disposition is stated as its own labelled
statement, **exactly one per directive**, mechanically distinguishable from
incidental mention of trees or commands elsewhere in the file" — the emphasis
this document's, the sentence quoted whole in M3's row, the file's `status:
agreed`, the expedited log's entry naming the amendment, and merge commit
`b5fc675c` carrying it to `origin/main` (§1). **Label-presence**,
**form-membership**, the exclusivity of the two forms, **at-least-one**, and now
**at-most-one** all read straight off it.

**The governed count and M3's count agree over carried wording, and they agree
because a fenced instance of it is a mention rather than a statement** (*told* —
the cycle-19 directive's N1,
disposing the cycle-18 gate's N1; the disposition is **resolved by reading, no
amendment**). That gate read the two counts as differing: the governed sentence
qualifies "exactly one per directive" by nothing, while M3 counts labelled
statements **outside fenced code blocks**, so a directive carrying one unfenced
labelled disposition statement **and a fenced copy of one** appeared to violate
the governed rule while exiting **0** on M3 — a false negative §7's residual set
did not disclose. **The reading that resolves it**: a labelled disposition
statement **reproduced** inside a fence — a copy rather than an original — is a
**mention**, not a statement. Fenced text of that kind is **exhibited** wording —
a copy of a statement belonging to another directive, or a duplicate of one this
file states unfenced — and exhibiting a statement is not making it.

**The reading scopes to carried wording, and the scoping is stated here because
this is where the reading is stated** (*told* —
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
N2, disposing the cycle-19 gate's N2; the alternative on the record there was to
confirm the reading's reach unscoped, and it was not taken). A fenced **copy of
another directive's statement**, and a fenced **duplicate** of one this file
states unfenced, are **mentions**: both are wording under carriage, and carriage
is what the ground below is about. An author's **own** fenced statement — the
only labelled instance in the file, carried from nowhere — is **a statement they
formatted badly**, not a mention. Nothing is being exhibited there, so the
carriage frame does not reach it, and the reading says nothing about it. The two
shapes therefore part company at §7 rather than sharing one verdict here, and
what the scoping costs is stated at both sites rather than left to be inferred
from the reading's wording.

The distinction is not imported: the
governed rule **draws it itself**, requiring the disposition to be stated "as its
own labelled statement, **mechanically distinguishable from incidental mention**
of trees or commands elsewhere in the file", and the same skill's
carry-as-pointer rule frames quoted wording as **carriage** — an origin
directive "carries it inline and downstream artifacts point at it" — which is
carriage of a statement, not a second making of it. So "exactly one per
directive" counts what a directive **states**, M3 counts unfenced labelled
instances, and the two are the same number **wherever the fenced text is
carriage** — which is the shape the gate described. That shape carries
exactly **one** statement, is not a violation of the governed rule, and M3's
exit **0** on it applies the rule rather than falling short of it — which is
what AC-DT-06 fixture (vi) pins. **No false negative arises and none is
recorded**; §7's residual set gains no member on this account, and its claim
that residual one is the only false-negative member is true as written. What the
reading does **not** move at §7 is stated two paragraphs below: under the
scoping the fenced-only shape stays in §7's set as an accepted **false
positive**, so the set gains no member and loses none.

**What the reading changes about the fence exclusion, and what it does not.**
It does not move the exclusion's **provenance**: the exclusion is still this
document's, dictated by the cycle-17 directive @ `7010e8ff`, and no governed
sentence states it. What the reading supplies is its **ground** — the exclusion
is the mechanical form of a line the governed rule draws in judgment terms, so
it is neither an arbitrary narrowing nor a requirement smuggled in beside the
governed one. **That ground reaches the exclusion where the fenced text is
carriage, and no further** (*told* —
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
N2): where an author fences their own sole statement, no governed line stands
behind the exclusion and it is a plain narrowing, whose product is §7's accepted
false positive rather than an exposure (§7). It still narrows what the lint
**matches** rather than adding a
requirement the lint **enforces**, so no G6 exposure appears and none is
recorded at §7 or AC-DT-13 (below; AC-DT-13).

**The consequence the previous revision drew at §7 does not follow from the
scoped reading, and it is withdrawn rather than left standing** (*told* —
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
N2; the previous revision's reclassification was a **consequential update under
Core rule 13** taken from the reading unscoped, and its reversal is one too,
labelled here and at its site). That revision reasoned: if a fenced instance is
a mention, then a directive whose **only** labelled instance is fenced states
**no** disposition, so M3's non-zero exit on it is the governed rule applied
rather than a false stop on a well-formed directive — and it reclassified §7's
residual two, second shape, from an accepted false positive to correct
behaviour. **Under the scoping the antecedent does not hold**: that author's
fenced statement is not carried wording, so it is a statement badly formatted
rather than a mention, the directive **has** stated its disposition, and M3's
non-zero exit on it is a false stop on a well-formed directive after all. The
shape **returns to §7's residual set as an accepted false positive**, which is
where the cycle-17 and cycle-18 revisions carried it (§7). AC-DT-06 fixture
**(vii)** is untouched by either movement: its verdict is **non-zero under both
scopings**, so no test, no criterion, and no fixture moved in either direction,
and what moved twice is the characterization alone. The reading's reach is
bounded and stated so it can be audited: it says a fenced instance of
**carried** wording is a mention, it says an author's own fenced statement is a
badly formatted statement, and it says nothing about indentation, block quotes,
or any other markdown context, all of which remain TRD concerns (M3's row).

**What that closes, stated rather than left to a diff.** Until the amendment,
at-most-one did **not** read off the sentence: it stated no count, and its only
carrier was the definite singular of "the disposition" read together with the
first rule's "**every** directive states **its** working-tree disposition" — a
reading, not a read-off. This document disclosed that as an exposure against G6
at §7's "Not accepted" and at AC-DT-13, for exactly one cycle, rather than
absorbing it. It is now closed the **first** of the two admissible routes §7's
item names — an expedited amendment to the governed skill, not deletion of the
clause — and the disclosure is **removed** at both sites rather than softened,
because the thing it disclosed no longer exists. M3's count is not narrowed and
nothing else about the check moves.

**The fence exclusion is still this document's, and it is not the same kind of
thing.** It narrows what the lint **matches** rather than adding a requirement
the lint **enforces**, so it cannot put the lint outside G6: a narrower match
enforces strictly less than the governed sentence licenses, never more. It rests
on the authoring corpus described above rather than on a governed sentence, and
that is stated here so it can be audited instead of assumed. It carries no
exposure at §7 or AC-DT-13 and none is recorded there; what it does carry is
§7's residual two, which is a false-positive class rather than an unsourced
requirement.

**M3 is still total, and AC-DT-10's non-reach is still derived rather than
declared.** Every file either carries exactly one **unfenced** labelled
disposition statement carrying an admitted form or does not; fencing is a
property of the text a parser decides before the count is taken, so it adds no
third outcome and no input on
which M3 has nothing to decide. So M3 is never an element the lint cannot
decide, AC-DT-10 stands unamended and has no M3 instance to govern, and the
**Reliability** goal is not excepted for M3. Totality is also what keeps the
older AC-DT-06 / AC-DT-10 contradiction the cycle-11 gate filed removed, and it
keeps it removed for the same reason it did under the retired predicate: every
input has a decidable verdict, so no fixture is required to exit **0** by one
criterion and **non-zero** by the other.

**The cycle-14 gate's N3 is dissolved with the predicate that raised it**
(*told* — the cycle-15 directive's N3). That finding asked whether the third
shape M3's predicate enumerated — "a conforming manifest that locates no
disposition author region" — is **vacuous** under G11, and observed that if it
is, the predicate was extensionally the conforming-manifest-present binary. The
predicate is retired and M3 enumerates no shapes of manifest at all, so the
question has **no referent**: it is dissolved, not answered. It is recorded here
because this is where the enumeration it questioned stood. The TRD-stage
consequence that finding flagged — that a non-vacuous third shape would oblige
the TRD to say what a conforming manifest missing that entry looks like —
lapses with it, and §8 Q6 carries no residue of it.

**M3 no longer consumes G11's manifest** (*told* — the cycle-15 directive's B1).
The cycle-14 directive's N2 made the manifest a machine-readable **input** to
`bin/check-directive` by way of M3's input-contract clause, and required both
binaries to read the same form. That clause was a clause of the retired
predicate and is retired with it: the lint reads no manifest, because the only
element that consumed one no longer does. What the manifest is still for is the
**measurement and generator-side apparatus**: §5's first outcome, which needs
the generator-supplied region of a landed directive identifiable as a byte
range, by way of AC-DT-05's partition; AC-DT-02's static check over the
generator's own source, which ranges over the manifest the generator declares;
and AC-DT-18's count of author-marked entries in a freshly generated skeleton.
All three are properties of the **generator**, and none is a check the lint
performs. G11 states the same list, so a reader arriving from either side finds
it.

**M8 admits three patterns because AC-CO-1 names two filename branches, and G0
puts both inside one tool** (*told* — the cycle-5 directive's B1 is the origin of
the third pattern; the cycle-3 directive is the origin of the second; *observed*
for the sources). The reasoning is one step, applied twice. `skills/directive-authoring.md`
@ `83b60511`, "Naming", states the timestamp form and excepts "a reviewer-gated
cycle directive ... per its stated convention." The stated convention it defers to
is `docs/packages/package-a-spec.md` §3.6 AC-CO-1 @ `768bbe3b`, and AC-CO-1 reads,
**whole**: "Writes `docs/cycles/cycle-<N>-directive.md` for `--cycle N`, or
`docs/cycles/<SLUG>-directive.md` for `--name SLUG`; exactly one of the two is
required (exit 2)." Both branches are implemented (`bin/cycle-open:61-67`) and both
are asserted green by the suite AC-DT-15 forbids reddening
(`bin/tests/test_cycle_open.py`, `test_co1_cycle_number_names_the_directive` and
`test_co1_slug_names_the_directive`) (*observed*). G0 folds that generator into
`bin/directive`, so an M8 admitting fewer than both branches would fail — at the
executor's first act, under J3 — a well-formed directive this spec's own generator
was told to produce. Cycle 3 saw the `--cycle` branch and licensed it; cycle 5's
B1 licenses the `--name` branch on identical grounds, and the only reason it took
two cycles is that until now this document quoted AC-CO-1 by halves.

Core rule 14 states the timestamp form "when no stated convention names the file"
and adds "Where a convention names it, follow the convention," so both AC-CO-1
branches are licensed by the rule they appear to contradict.

**Pattern 3 is bounded by AC-CO-1's destination clause, and by nothing else**
(*told* — the cycle-7 directive's B1 removed the character class; the cycle-9
directive's B2 states the path boundary and the reading that produces it;
*observed* for the sources). Two questions have been asked of pattern 3's
`<SLUG>` and they have different answers, from the same sentence of governed
text. **Character class: none.** Cycle 6 gave pattern 3 a `<SLUG>` class — lowercase alphanumerics and
hyphens, no leading and no trailing hyphen — as the lint's own normalization of a
boundary AC-CO-1 leaves unstated. No governed file states such a class. AC-CO-1
reads, whole, "Writes `docs/cycles/cycle-<N>-directive.md` for `--cycle N`, or
`docs/cycles/<SLUG>-directive.md` for `--name SLUG`; exactly one of the two is
required (exit 2)", and `bin/cycle-open` takes `--name SLUG` as a free-form string
(`bin/cycle-open:39`) and interpolates it into the path unvalidated (`:67`), with
`bin/tests/test_cycle_open.py` asserting the branch and nothing about the class
(*observed*). G6 is the ground and it is unambiguous: "A requirement the tool
enforces and no governed file states is a defect in the tool, not a stricter tool."
A class in M8 would have made `bin/directive --name Pass3_Fix` — a legal AC-CO-1
invocation, whose output AC-DT-15 forbids reddening — emit a filename the same
binary's lint rejects, which is exactly the case the conflict rule under "Mode
scoping" exists to surface rather than absorb. So pattern 3 accepts a slug of
**any characters**.

**Path structure: one component, no separators — and "what the preserved contract
can emit" means what AC-CO-1 licenses, read through its destination clause**
(*told* — the cycle-9 directive's B2 dictates the boundary and the reading; the
cycle-10 directive's N2 dictates that the metavariable step below be stated as a
step; *observed* for the sources). Cycle 7 left the phrase "any slug the preserved
contract can emit" undecided in exactly one dimension, and cycle 8's B2 is where
the cost of leaving it undecided was demonstrated. The phrase is now read one
way and the reading is stated: **"what the contract can emit" means what AC-CO-1
licenses**, not what any implementation of it happens to produce. And AC-CO-1
does not stop at naming a template — it states a destination. Quoted whole
again, at `768bbe3b`: "Writes `docs/cycles/cycle-<N>-directive.md` for
`--cycle N`, or `docs/cycles/<SLUG>-directive.md` for `--name SLUG`; exactly one
of the two is required (exit 2)."

The boundary follows in three steps, and the **second is a reading being taken**,
stated as one rather than presented as a conclusion — because a metavariable read
one way without saying so is the move this document's own record says "hid
pattern 3 for two cycles" (*told* — the cycle-10 directive's N2):

1. **The destination clause locates the output.** AC-CO-1 does not merely supply
   a template to interpolate into; it states where the file is written:
   `docs/cycles/<SLUG>-directive.md`. That is **a single directory level** —
   `docs/cycles/`, and then a filename in it.
2. **Therefore `<SLUG>` denotes one path component.** This is the reading, and it
   is the step the rest rests on: the metavariable stands for a **filename
   component**, not for an arbitrary string that may itself contain separators.
   Read the other way — `<SLUG>` as a free string, which is exactly how
   `bin/cycle-open:39` takes it — the clause still fixes the prefix but no
   longer fixes the depth, and the "destination" it states would name a family
   of paths at every level below `docs/cycles/` rather than one file in it. The
   step is taken because a destination clause that does not fix the
   destination's depth states nothing the word *destination* means; it is
   **stated** because taking it silently is the failure this effort has already
   paid for twice.
3. **Both excluded cases follow from those two steps, in different
   proportions.** `sub/nested` yields `docs/cycles/sub/nested-directive.md`,
   which carries the licensed prefix but sits **one level too deep**, so its
   parent is not `docs/cycles/` — excluded by step 2, and by step 2 alone, since
   step 1 admits the prefix. `../escaped` yields `docs/escaped-directive.md`,
   which resolves **outside** `docs/cycles/` altogether — excluded by step 1 on
   its own, with no need for step 2 at all.

So a separator-bearing name is **outside the set AC-CO-1 licenses**, and
pattern 3 matches a **single-component basename**. The asymmetry in step 3 is
load-bearing rather than incidental: the two cases are excluded by different
clauses, which is why AC-DT-06 fixtures both, and why the `../escaped` case —
the one resting on the shorter ground — is not the one to drop.

This boundary is **derived from cited governed text, not invented**, which is
what G6 requires of it and what distinguishes it from the character class cycle
7 deleted. The class had no source; the destination does — it is in AC-CO-1's own
sentence, and G6 and that clause are the ground stated together. The two
dispositions are therefore consistent rather than opposed: G6 forbids a
requirement no governed file states, and it equally forbids **widening** a
pattern past what the governed text licenses, because a lint that admits names
the contract does not license is no longer checking the contract.

**Implementation behaviour beyond the licensed set is not pattern 3's referent**
(*told* — the cycle-9 directive's B2 requires this stated explicitly).
`bin/cycle-open` takes `--name SLUG` as a free-form string (`:39`) and
interpolates it into the path unvalidated (`:67`), so it will emit paths AC-CO-1
does not license — the cycle-8 gate verified by running that
`--name 'sub/nested'` exits 0 writing `docs/cycles/sub/nested-directive.md`, and
`--name '../escaped'` exits 0 writing `docs/escaped-directive.md`
(`reviews/directive-tooling-cycle-8.md` @ `e8bf561c`, B2, *told* to this document
and not re-run here). **Both are stated as outside the licensed set**, and both
appear as **failing** fixtures in AC-DT-06. That an implementation emits them is
a fact about the implementation, and — if it matters — a defect in it against
AC-CO-1; it is not evidence about what pattern 3 admits, because pattern 3's
referent is the licensed set and not the emitted one. This is the same
permissive-check / strict-emission direction M2 and M8 already take, applied to
the one place where reading the phrase the other way would have made a lint
ratify its own tool's escape.

The looseness pattern 3 still admits — any characters, one component — is not a
new residual: it falls inside the mode-appropriateness residual §7 already
accepts, and it is bounded the same way — the generator names the file, so no
directive the generator produced can carry a name its mode did not choose. With
the class gone and the path boundary sourced, AC-DT-13's "as written" claim and
§7's final "Not accepted" item are true of M8, and neither needed a carve-out to
become so. **Neither disposition moves a figure in the corpus recount** (below,
*observed*): `docs/cycles/` contains no subdirectory at this revision, so no
committed name exercises the separator boundary in either direction, and the
classification run with the character class and without it agrees on every
file.

**What M8 claims, and what it does not** (*told* — the cycle-6 directive's B1 is
the origin of this scoping; it replaces a cycle-5 sentence that read "the pattern
is determined by the generator's mode and, in the cycle mode, by the selector",
which described a determination M8 does not make). M8 asserts **form-set
membership and nothing else**: the filename matches one of the three licensed
patterns. It asserts nothing about **mode-appropriateness** — whether the pattern
a given filename matches is the pattern that directive's mode should have
produced — because no check over a filename can decide it. The lint is handed the
directive file the executor writes (§2, §5) and nothing else: it has no mode
argument, no selector, and no class signal, and the file carries no marker it
could read one from. Inventing such a marker is Q5's territory — what the
directive file itself declares — and is not decided here.

**Being handed the whole file is not the same as every element matching over the
whole file** (*told* — the cycle-11 directive's B1; restated over the labelled
statement under the cycle-15 directive's B1). The paragraph above is about the
**inputs** the lint has — one file, no mode, no selector — and says nothing
about what any single element matches inside that file. M3 matches **labelled
disposition statements** and nothing else, wherever in the file they sit and
whatever else the file carries (above, M3's row and "M3's check is over the
labelled statement"); this section restates no part of that test. No statement
in this document about the lint's inputs may be read as fixing what any element
matches.

**Mode-appropriateness is guaranteed by the generator, by construction.** The
cycle mode emits the AC-CO-1 form its selector names — pattern 2 for `--cycle N`,
pattern 3 for `--name SLUG` — and the general mode emits the timestamp form; the
author does not choose the name in either. So a directive the generator produced
carries the mode-appropriate pattern because the generator had the mode and the
filename was never freehand. That is a property of **the generator**, stated here
as one, and it is not a property M8 verifies or may be read as verifying. This is
the same permissive-check / strict-emission split M2 takes, and it is stated in
the same direction G6 requires when the two differ.

**The residual is an accepted minor defect class** (*told* — the cycle-6
directive's B1 dispositions it as accepted). A **hand-written** general-mode
directive named `<slug>-directive.md` passes M8 without carrying a timestamp, and
no filename check can catch it: the name is a member of the licensed form set, and
the fact that makes it wrong — that it was not produced by the cycle mode — is not
in the filename. The class is bounded on both sides: it reaches only hand-written
directives, and only those whose author chose a `-directive.md` name; every
generated directive is correct by construction, and every hand-written directive
that also omits a *required element* is still caught by M1–M7. The **mitigation is
the generator's adoption**, which is what removes hand-written naming from the path
altogether, and which G4 keeps ungated in the general mode so it can be adopted
first. §7 carries this as an accepted risk rather than leaving it implicit here.

**A fourth filename branch, if one is found, is a defect to surface — not a
pattern to absorb** (*told* — the cycle-5 directive's B1 states this explicitly).
Three consecutive cycles found the absorbed contract doing something this document
said it did not, and each time the fix was to widen this document to match. That
sequence stops here — and cycle 8 is the first evidence that it did. The
independent gate found pattern 3's path boundary undecided and raised it as a
**blocking** finding rather than reading a width into it, and the cycle-9
disposition bounded pattern 3 **inward**, to what AC-CO-1 licenses, instead of
widening M8 a third time (*told* — the cycle-9 directive's B2). The rule fired as
written. Under the conflict rule stated above under "Mode scoping",
any further filename branch discovered in AC-CO-1 through AC-CO-12 (§3.6 and
§8.2 @ `768bbe3b`) — or any other
contract behaviour M8 would reject — is raised as a **blocking finding** and
disposed by Dave on the record. It is not absorbed into M8 by a reviewer or an
implementer reading the contract, and M8's "no fourth pattern passes" is written
to make that absorption visible rather than convenient. The corollary is that
**AC-CO-1 through AC-CO-12 must be quoted whole wherever this document relies on
them**; the half-quotation of AC-CO-1 is what hid pattern 3 for two cycles, and
the quotation above is the first place this document states it entire. The
obligation has a second limb, added this cycle because a criterion cannot be
quoted whole from an address it is not at: **each quotation names a revision at
which the quoted text exists**. AC-CO-12 was relied on across this document's
cycle-mode claims from cycle 2 onward — the refusal lists at "Mode scoping", G4,
and AC-DT-04, and the preserved range at AC-DT-15 — and quoted in none of them,
against a SHA that does not contain it. It is quoted whole above, at `768bbe3b`,
and that is what closes the gap (*told* — the cycle-9 directive's B1).

**The skill that specialises rule 14 to directives licenses the timestamp form
directly and the two cycle forms by deferral, and M8 is anchored accordingly**
(*observed* for the text; the anchoring is *told* — the cycle-4 directive's N2 for
the skill sentence, the cycle-5 directive's B1 for the direct AC-CO-1 anchor, the
cycle-6 directive's B2 for the time component).
Cycle 3 recorded a residual: `skills/directive-authoring.md`'s "Naming" section
restated Core rule 14 without its yield clause, so read alone it admitted only the
timestamp form. That residual is **closed**. The Naming section at `origin/main`
now reads, whole: "A directive file is
`docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in ISO 8601 basic format
with date and time components both present (as `20260820T161541`) — except a
reviewer-gated cycle directive, which is
`docs/cycles/cycle-<n>-directive.md` per its stated convention." Its content
commit is `6179221a`, agreed by expedited amendment and recorded in
`reviews/expedited-log.md` — "2026-08-23 — skills/directive-authoring.md @
6179221a… — timestamp form requires date and time components both present"
— reaching `origin/main` in merge commit `e01d9e00`. It is the **third** expedited
amendment to that file, following `48ad7fd1` (the working-tree rule, §1) and
`83b60511` (the numbered cycle form, whose sentence this one extends rather than
replaces), and preceding a **fourth**, `b4a0fa58`, and a **fifth**, `7853525a`,
each of which amends the working-tree
rule rather than the Naming section — the fourth adding the labelled-statement
property M3's check anchors on and the fifth the **exactly-one count** it now
also anchors on (§1; §4, M3's row). Nothing in this document
schedules an amendment to either section, because all **five** have landed: no open
question and no criterion waits on one.

**M8's time-component rule is governed text, and is anchored on that sentence**
(*told* — the cycle-6 directive's B2 dispositions this; *observed* for the text and
the log entry). Cycle 5 recorded that the rule as then written was **stricter than
its source**: the skill said "ISO 8601 basic format", which admits a bare calendar
date, while M8 required a date and a time. G6 names that as a defect in the tool
rather than a stricter tool, and AC-DT-13 and §7's "Not accepted" both assert that
no element stands in that position. The gap is **closed at the source**: the
governed sentence now says "with date and time components both present (as
`20260820T161541`)", so `20260823` alone is not the form the skill licenses, and
M8's rule states what its cited text states rather than narrowing it. No carve-out
is taken and none is needed: AC-DT-13's "as written" claim and §7's final "Not
accepted" item are true of M8 as they are of M3, and both name the amendment that
makes them true. The mechanism is the same one M3's gap took — an expedited
amendment to the governed file, recorded in `reviews/expedited-log.md` — which is
the third instance of it in this effort and the pattern this document has now used
consistently rather than reaching for an exception.

What that sentence does **not** do is enumerate the cycle forms exhaustively. It
names `cycle-<n>-directive.md` and then yields — "per its stated convention" — to a
convention it does not quote, and the convention it yields to names two branches,
not one. So M8's patterns 2 and 3 are anchored on **AC-CO-1 itself**, cited by path
and SHA (`docs/packages/package-a-spec.md` §3.6 @ `768bbe3b`), rather than on the
skill's partial restatement of it. The skill remains the corroborating source and
the document an author is instructed to follow; it is not the authority for the
set of cycle-mode filenames, because it does not state that set. The metavariable
differs cosmetically between the two — `<n>` in the skill, `<N>` in AC-CO-1 and in
M8 — and nothing turns on it (*observed*).

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
  **five** times, for cause: `skills/directive-authoring.md` is cited at its five
  **content commits** — `48ad7fd1` for the working-tree rule's two-form
  requirement, `b4a0fa58` for that rule's labelled-statement requirement,
  `7853525a` for that rule's exactly-one count,
  `83b60511` for the Naming rule's numbered cycle form, and `6179221a` for its
  date-and-time requirement — while the last commit touching that path is
  `d4a3158b`, a frontmatter-only status transition that introduced none of them.
  `reviews/expedited-log.md`
  selects all five agreements the same way (*observed*). A lint enforcing lastness
  would fail all five citations and the expedited log's own convention with them.
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
longer cites it as though it were. **The narrowing is pinned by AC-DT-17** (*told*
— the cycle-5 directive's N2), so it binds an implementer as a criterion rather
than resting on an argument in §4 that §6 does not carry.

Historical directive files are **not retrofitted** (*told* — dictated); the lint
governs directives written after adoption, and renaming the existing corpus would
break every citation by path that points into it. `metadata-scope-fix-20260823.md`
is specifically not retrofitted, notwithstanding that M8's time-component rule now
decides it (*told* — the cycle-5 directive's N1, governed at `6179221a` per B2).

**The corpus recount against the three-pattern check** (*observed*, recounted at
this revision; the disposition to recount is *told* — the cycle-5 directive's B1
and N1). **Scope of this count**, stated with it because §1 carries a different
count of the same directory: this is every `*.md` entry in `docs/cycles/` **as
the directory stands at this revision**, classified against M8's three patterns —
not the research document's 91/90 measured at `49bd6ff4` (§1), and not a count
of directives as a class. `docs/cycles/` holds **112** markdown files, of which
**76** match pattern 1, **7** match pattern 2 `cycle-<N>-directive.md`, **26**
match pattern 3 `<SLUG>-directive.md`, and **3 match none**. The total and the
pattern-1 count each rise by **one** against the cycle-19 revision's 111/75,
which rose by one from cycle 18's 110/74: cycle 18's
110/74 rose by one from cycle 17's 109/73, that by two from cycle 15's 107/71,
that by one from cycle 14's 106/70,
that by two from cycle 12's 104/68,
that by one from cycle 11's 103/67, that from cycle 10's 102/66 and that from
cycle 9's 101/65, and cycle 6's 98/62 rose by one from
cycle 5's 97/61 and that from cycle 4's 96/60, because each cycle's own
directive file is in the directory by the time its revision recounts. The rise
is **two** only when an independent gate's directive lands in the same interval,
which has now happened three times — cycle 9 (against cycle 7's 99/63), cycle 14
(cycle 13 having been the second independent gate), and cycle 17 (against cycle
15's 107/71, the third independent gate's directive landing with it) — and **it
has not happened in any of the three intervals since**: cycle 17's review, cycle
18's, and cycle 19's are all **self-gates** and none landed a directive of its
own (§1), so the one file this interval added is
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md`, the directive
this revision executes, which matches pattern 1 (*observed*, by running). This paragraph's figures are a **consequential update
under Core rule 13**, not a dictated disposition: neither the cycle-19 directive
nor `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @
`5ea201e6` dispositions a figure, and the recount is restated because it is
stated "at this revision" and the file this interval added — that directive
itself — is in the directory. **Cycle 9's pattern-3 disposition moves none of these figures,
and nor did cycle 7's** (*told* — the cycle-7 directive's B1 and the cycle-9
directive's B2 each direct this be stated; *observed* for the verification; the
cycle-12 directive's N2 is the origin of naming cycle 9 explicitly here, the
deictics it replaces having named cycle 9 implicitly since cycle 9). The classification run with cycle 6's character class and run
without it agrees on every file in the corpus — which cycle 6's gate verified at
98 files (`reviews/directive-tooling-cycle-6.md` @ `d8f8d7a6`, O4) and which
reproduces at 112 at this revision — and the single-component boundary added in
cycle 9 is likewise inert over the corpus, because `docs/cycles/` **contains no
subdirectory**: `git ls-tree` at this revision returns blobs only, so no
committed name carries a path separator to be admitted or rejected (*observed*).
The only figures that moved are the total and the pattern-1 count, by the +1 the
paragraph above accounts for — **that figure was stale at the cycle-18 revision
and was corrected at the cycle-19 one rather than left to a diff**: it read
"+2", which was right at cycle 17 where the rise was two and wrong at cycle 18
where the paragraph above it already said "rise by **one**", a Core rule 13 miss
inside a paragraph that labels itself a Core rule 13 update (*observed*, by diff
against `6d29a4ab` and `de0cc683`) — and neither movement is an effect of a
disposition. The three that match none are
`metadata-scope-fix-20260823.md`
(N1's date-only case) and two files that are not directives at all —
`doc-review-2026-08-02-questions.md` and `friction-refactor-2026-08-09-decisions.md`
— which the lint would never be pointed at, since it takes the directive file the
executor writes, not the directory. So the directive-file corpus written before
adoption has **exactly one** name the three-pattern check rejects.

**Provenance of the recount**, stated because Core rule 13 requires a changed
number to be reproducible where it appears: the classification was computed at
this revision over every `*.md` entry in `docs/cycles/`, applying, in order,
pattern 1 = `.+-\d{8}T\d{6}Z?\.md`, pattern 2 = `cycle-\d+-directive\.md`,
pattern 3 = `[^/]+-directive\.md`, first match wins. Those three
are transcriptions of **M8's own patterns**, not classification rules of the
recount's: pattern 3 carries no character class because M8's row states none
(*told* — the cycle-7 directive's B1), and its `[^/]` is the single-component
boundary M8's row states, transcribed rather than invented here (*told* — the
cycle-9 directive's B2) — which is why the recount is reproducible
from the criterion rather than only from this block. Over this corpus the
`[^/]` makes no difference, the directory holding no subdirectory, and it is
transcribed anyway so that the block reproduces the criterion and not a
simplification of it. Pattern 2 is
a subset of pattern 3 and is tested first so the two counts do not double-count.
The one non-`.md` entry in the directory
(`comfy-archive-and-generalize-20260822T195900-check.txt`) is out of scope and is
excluded (*observed*).

**Why the number moved so far, and what that costs.** Cycle 4 recorded 29
non-conforming against the two-pattern M8; the three-pattern check takes that to 1,
because 26 of the 29 were `<SLUG>-directive.md` names that pattern 3 now admits and
2 were never directive files. The dictated cycle-2 figure of 37, counted against
the **single-pattern** M8, stays on the record with its provenance, as does cycle
4's 29 (*told* — the cycle-4 directive's O1). The cost of the widening is stated
rather than buried: pattern 3 constrains a filename to the `-directive.md` suffix
and to a single path component, and to nothing else, so M8 is a weak check on any
name of that shape — and cycle 7 made it weaker still, by dropping the character
class cycle 6 had given it. That is
what licensing AC-CO-1's second branch buys, at the price G6 sets: the class was a
requirement no governed file states, so keeping it would have cost more than the
looseness does. Cycle 9's single-component boundary moves the width back the
other way by exactly one dimension, and it is the dimension a governed sentence
decides — AC-CO-1's destination clause — which is why it is a boundary rather
than a second normalization. §6's AC-DT-06 fixture set is where the residual strength of the
check is pinned, and "What M8 claims" above is where the weakness is scoped rather
than talked around — the residual it leaves, at either width, is an accepted defect
class (§7), not an unstated one.

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
  environment. **This is where the first of M3's two accepted residuals sits**
  (*told* — the cycle-15 directive's N2; §7): M3 checks that a labelled
  disposition statement is present and carries an admitted form, and it cannot
  check that what the statement says is **true** — that the tree it names is the
  tree the session will use. The second, a labelled statement under quotation,
  is a false positive rather than a judgment-only property and is stated at §7
  alone.

That last one is not a limitation to be engineered away, and this effort
demonstrates why twice. The cycle-1 directive as first issued assigned the working
tree `../fiducial-directive-tooling` — a present, well-formed, correctly-shaped
assignment: written as the labelled statement the governed rule now requires, it
is one M3 passes on both label-presence and form-membership (M3's row). It was
**not executable**: the
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
  exits non-zero, rather than passing it. The rule admits no exception, and M3 is
  not one: M3's check is total by construction — every file either carries
  exactly one **unfenced** labelled disposition statement carrying an admitted
  form or does not, with no third outcome (§4, M3's row; §4, "M3's check is over
  the labelled statement"; §4, "The count is exactly one") — so M3 is never an element the lint cannot decide and the rule
  simply has no M3 instance to govern. That is a derived consequence of the
  check, not a carve-out from this goal.
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
  section by its committed source, the working-tree disposition **prompt** by its
  committed source alongside them, and **two** regions as the author's: the
  task-specific region and the disposition **author region** (§4 G3, G11) —
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
  **This measurement is well-defined only because the disposition slot is split**
  (*told* — the cycle-10 directive's B1). Until the split, the slot's bytes were
  the generator's under G1 and the author's under J1, so this first signal
  counted an author-written disposition into the generator-supplied share, in
  exactly the bytes of the element the motivating incident is about. The
  cycle-9 gate's worked example sizes it: a 60-line directive carrying a
  four-line exclusive assignment overstates the generator's share by four lines
  in sixty, about seven points (*inferred*, arithmetic on that example's
  figures; it is an illustration of the direction and magnitude, not a measured
  corpus figure). With the prompt sourced and the author region marked, the
  disposition contributes to whichever side actually wrote it, and the signal
  measures what §5 says it measures.
  Sizing context: write mechanics run 13.9% to 43.3% of each recent `pass2`
  directive (*observed*, per the research findings). That those write-mechanic
  sentences are the same region a generator would fill is this spec's own reading
  of that measurement (*inferred*), not a finding of the research document.
- **Malformed directives are caught at the first act rather than mid-cycle.**
  Signal: lint failures at the first act, and — the number that matters —
  execution sessions that stop and surface on a directive defect *after* work has
  begun. Baseline for the second: at least one, the motivating incident (*told*).
  Mechanism: execution reports and retros.
- **Invariant text stops contradicting itself.** Signal: **new contradiction
  instances** among the directives authored after adoption — a count of
  contradictions, where a contradiction is one directive instructing a mechanism
  another instructs the opposite of, with neither superseding the other. The
  unit is the **instance**, and every figure in this bullet is in it.
  Baseline: **one** contradiction — the merge-mechanism disagreement recorded at
  `docs/research/gh-write-friction-20260823T184149Z.md` @ `49bd6ff4` §3.2, where
  eight committed directives instruct a `curl`-against-the-REST-API merge and
  the ninth instructs its opposite (*observed*, per that document, which calls it
  "the eight-versus-one contradiction" and describes one disagreement, not nine).
  The nine is the **spread** of that single contradiction across the corpus and
  is not a baseline in this unit; it is stated here as context and is not the
  figure the mechanism reads against (*told* — the cycle-9 directive's B3
  dispositions this; the file-unit baseline this bullet previously carried is
  removed).
  Mechanism: a recount of contradiction instances over directives authored after
  adoption, reading **zero new instances** as the target. **The first recount is
  expected to read 0 against 0** — the post-adoption set is empty at adoption, so
  an early zero is arithmetic and not evidence — and this outcome is **meaningful
  only over time**, once enough post-adoption directives exist for a
  contradiction to have had the opportunity to appear. That bound is stated
  rather than left to the reader, because a count that starts at zero by
  construction is the kind of signal §7's halo risk describes: it looks like
  success on the day it is first taken.
  **This outcome is narrowed, not re-baselined** (*told* — the cycle-6 directive's
  O4, which offered the two branches and asked which was taken; this is the second).
  Cycle 5's O4 read this signal as measuring **filename conformance**, and observed
  that a check rejecting 1 name in 97 — the corpus size at that revision — would
  produce a near-flat one. The narrowing
  is that this outcome never measured filename conformance and does not now: the
  contradiction it tracks is between *instructions*, which is what G1 addresses by
  emitting invariant text from one committed source, and no part of it is computed
  from the filename recount. So the filename recount does not re-baseline this
  outcome, because it is not evidence for it in either direction. Where the
  filename number does belong is stated where it is measured: M8's yield against
  the pre-adoption corpus is **1 non-conforming directive file of 112 markdown
  files in `docs/cycles/` at this revision** — the scope §4 states with the
  recount — with the
  classification and its provenance in §4, and it is a property of the lint's
  reach, not a measured user outcome. Recording it here as this outcome's baseline
  would have been the re-baselining branch, and it was declined because it would
  put a number under a signal that does not produce it.
  **The term "concurrently-live" is dropped, and the outcome is narrowed to what
  the recount reproduces without it** (*told* — the cycle-7 directive's N2). The
  signal previously read "across **concurrently-live** directives", and nothing in
  this document, or in any document it cites, decides when a committed directive
  stops being live: no mechanism here retires one, and supersession is defined for
  decision-log entries by `policies/decision-log-policy.md`, not for directive
  files (*observed*). A counter would therefore have had to invent a liveness rule
  per pair of directives, which makes the outcome unfalsifiable — the property Core
  rule 13's discipline exists to prevent. What the recount reproduces without the
  term is narrower, and is what the signal now states: contradiction instances
  **among the post-adoption directives**, which is the set these tools govern (§4,
  "Historical directive files are **not** retrofitted"), counted in instances
  against the one-instance merge-mechanism baseline stated above (*told* — the
  cycle-9 directive's B3; the phrase "the nine-directive merge-mechanism
  baseline" that stood here mixed the units and is removed). The narrowing is
  real and is stated rather than absorbed: a
  contradiction between a post-adoption directive and a pre-adoption one is
  **outside** the count, so this outcome measures whether the tools stop *new*
  invariant text from contradicting itself, not whether the standing corpus
  becomes consistent. Nothing in this document claims the latter, and §4's
  no-retrofit disposition is why.

Not measured, and stated so the list is not read as exhaustive: whether directive
*quality* improves in the judgment dimensions of §4's second table. The lint makes
no claim there, so no signal it produces would be evidence for it, and treating
lint pass rate as a quality metric is the specific misreading §7 names.

## 6. Acceptance criteria

Derived from §4. Each is concrete enough to derive a test case from. The test
substrate is expected to be fixture directives — well-formed and each missing one
element — checked against a fixture repository, which makes the whole set testable
offline (*inferred*).

That preamble is true **as written**, and cycle 6 is where it was made so
(*told* — the cycle-6 directive's N2). Two criteria previously took
their fixtures from this repository's real commit history: AC-DT-09, whose blob-hash
case was a citation in this effort's own cycle-1 directive, and AC-DT-17, whose
abbreviated-SHA and non-last-commit cases were this document's own citations of
`skills/directive-authoring.md`. Both are now stated as **synthetic cases embedded
in the offline fixture repository**, each constructed to the same shape as the
historical instance it replaces — a blob hash cited where a commit was meant, an
abbreviated SHA, a commit that touches a path but is not the last to touch it. The
historical instances are cited in prose as **provenance** — they are why each case
is in the set, and evidence that the shape occurs in practice — and are not test
inputs. No criterion in this section requires this repository's commit history to
run. Two are verified against this repository rather than against a fixture
repository, and neither is a fixture-directive test: AC-DT-15 runs the committed
suite `bin/tests/test_cycle_open.py`, and AC-DT-16 is discharged by reading
`decisions/log.md` and `OPEN-ITEMS.md`. Both are offline, so the preamble's claim
holds for them as well; they are named here so "fixture directives against a
fixture repository" is not read as covering every entry.

- **AC-DT-01** — Changing the committed text of a source a skeleton section is
  read from changes that section in the next generated skeleton, with no edit to
  the generator. Verifiable by mutating a fixture source and regenerating.
- **AC-DT-02** — For every entry in the source manifest the generator emits
  (G11, AC-DT-05), no string literal in the generator's source reproduces **a
  line of that entry's committed content that the exclusion rule below does not
  exclude**, where
  reproduction means the two are **exactly equal after whitespace
  normalization**.
  **The exclusion is one rule, stated once, and the criterion states no second
  formulation and claims no equivalence between formulations** (*told* — the
  cycle-14 directive's N1; the defect it disposes is the cycle-13 gate's N1,
  which showed the two formulations the previous revision called equivalent
  disagreeing on every line mixing whitespace with set characters, including the
  table rule the criterion's own prose names as covered). The rule:

  > A line is **excluded** when it consists solely of whitespace and characters
  > from the set `-` `=` `~` `` ` `` `#` `*` `_` `|` `>` `+`.

  The rule is a property of the **line as it stands in the committed source**,
  read raw. It is not applied to the normalized line, and normalization is not
  part of it — normalization belongs only to the comparison clause below, which
  is a different test over different operands. The criterion's older two names
  for the excluded lines survive only as names for sub-cases of this one rule
  and add no test: a **blank** line is the sub-case carrying no character from
  the set, and a **structural** line is the sub-case carrying at least one.
  Both are excluded by the single rule, so the criterion never has to decide
  which name a line takes.
  **The class is delimited by enumeration, not named as a category** (*told* —
  the cycle-11 directive's N1 dispositions this; the cycle-10 gate's N1 is the
  finding). The wording this replaces read "a markdown structural delimiter or a
  punctuation mark", which names two categories and enumerates neither: "markdown
  structural delimiter" has no standard extension at all, and "punctuation mark"
  has one — Unicode general category P — that does not contain `|`, `>`, `=`, `+`,
  or `~`, every one of which is category Sm and every one of which is a markdown
  structural character. The union was therefore stated nowhere, and two
  implementations could disagree at the margins about lines such as `1.`, `**`, or
  `<!-- -->`. The rule above decides all three and every other line by inspection, and each
  example below is **re-derived from the rule as stated** rather than carried
  from the previous revision (*told* — the cycle-14 directive's N1, which
  requires the re-derivation): `**` is excluded, both characters being in the
  set; `1.` is not, `1` and `.` being outside it; `<!-- -->` is not, `<` and `!`
  being outside it.
  **The set is this criterion's test-selection rule, and it is not a rule imposed
  on any governed file** (*told* — the same disposition). It says which lines of a
  named source the static check compares literals against; it says nothing about
  what a governed file may contain, forbids no character anywhere, and no governed
  document is in or out of conformance by reference to it. A line the set excludes
  is a line this check does not range over, and nothing more.
  **The exclusion rule and the comparison are the criterion's own contract**,
  not an implementer's normalization of it (*told* — the cycle-9 directive's N1
  for the exclusion of blank lines and for the comparison, the cycle-10
  directive's N1 for the exclusion of structural lines, the cycle-11 directive's
  N1 for delimiting the set by enumeration, and the cycle-14 directive's N1 for
  collapsing the exclusion to one rule). Taken in turn — the rule's two
  sub-cases, then the comparison:
  *the blank sub-case* excludes the blank lines every governed file contains and
  every generator's source reproduces trivially — under a literal reading of "a
  line" the criterion failed for every correct implementation, since a generator
  that emits `""` or `"\n"` reproduces a blank line of every source it names.
  *The structural sub-case* excludes the line a governed file carries as a
  **marker** rather than as content, and the criterion names its demonstrating
  exclusion: **`---`**. Every governed file the manifest will name carries the
  frontmatter fence — `grep -c '^---$'` returns **2** for each of
  `docs/global-context/core.md`, `docs/global-context/decision-layer.md`, and
  `skills/directive-authoring.md` (*observed*, at this revision) — so without
  the exclusion rule a generator holding the literal `"---"` for any purpose,
  whether emitting frontmatter into the skeleton, a horizontal rule, or a fence,
  reproduces a line of every one of those entries exactly, and the static check
  reds a correct generator. The same shape reaches every short
  marker a generator legitimately holds, and each is re-derived from the rule:
  a lone `#`, `|`, `-`, or `>` is one set character and nothing else; a fence is
  three backticks; and **a table rule of hyphens and pipes** — `| --- | --- |` —
  consists solely of pipes, hyphens, and the spaces between them, every
  character of which is either whitespace or in the set, so the rule excludes it.
  That last example is the one the two formulations of the previous revision
  disagreed on, and it holds under the rule this criterion now states.
  What the rule does **not** exclude is a
  short line carrying a **word** — a heading such as `## Naming` carries `N`,
  which is neither whitespace nor in the set, so it remains within the
  criterion's range and a literal matching it is still reported, which is
  correct, because that is invariant prose the generator is required to read
  rather than hold. The bound is a property of the **line in the committed
  source**, not of the literal's purpose in the generator, so it is decidable by
  the same static pass and needs no knowledge of why the literal is there.
  Without the exclusion rule the criterion was decidable but not satisfiable, which is the residual the cycle-9 gate's N1
  named: the guard on G1 — this document's central prohibition — was the check
  that reddened spuriously for most correct implementations.
  *Exactly equal after whitespace normalization* fixes the comparison rather than
  leaving it to be chosen: strip leading and trailing whitespace from each side
  and collapse internal runs of whitespace to one space, then compare for
  equality. So a literal differing from a source line only in indentation **is** a
  reproduction and is caught, and a literal that merely contains, extends, or
  resembles a source line is **not** one and is not reported. This clause fixes
  the **comparison**, and nothing else: it does not restate the exclusion rule
  above, in normalized terms or otherwise, and the two tests have different
  operands — the exclusion rule reads a line of the committed source raw, the
  comparison reads a literal and a line and normalizes both. Stating the
  comparison here is what keeps two implementations of AC-DT-02 from disagreeing
  about what "a line" means, which is the property the criterion needs to be the
  mechanical enforcement of G1. Verifiable statically over the source against
  the manifest the generator itself declares, which makes the criterion decidable
  without knowing where the invariant text lives — so it does not depend on Q1.
  Q1's resolution changes which paths the manifest names; it does not change what
  this criterion asserts or how it is checked.
- **AC-DT-03** — A generated skeleton contains a working-tree disposition slot
  in the **two regions** G3 states, and the criterion binds each separately
  (*told* — the cycle-10 directive's B1; this criterion previously treated the
  slot as one region the author fills, which is the half of the dual
  classification that sat opposite G1). **The prompt region** is present and
  **non-empty**: it is read from committed text (G1), it states that a
  working-tree disposition is required, it names both admitted forms, and it
  states that the disposition is written as its own **labelled statement**
  (*told* — the cycle-15 directive's B1; §4 G3). The last clause is what keeps
  the generator and the lint in agreement: M3 checks label-presence, so a prompt
  omitting the labelling requirement would produce skeletons whose faithful
  completion fails M3.
  **The author region** is present and carries the **labelled statement with an
  empty content slot**: the TRD-fixed **label** is emitted by the generator as
  the region's marker, the **content slot** beneath it is blank, and a blank
  content slot is structurally distinguishable from one an author has filled
  (*told* — the cycle-17 directive's B1, disposing the cycle-16 gate's B1). This
  criterion previously required the region to be "present and **empty**", which
  put the label's form nowhere in the skeleton and left a faithful author unable
  to learn the form M3 matches — the defect that gate filed as blocking. The
  author writes the **content** and nothing else; label plus content is the
  **labelled disposition statement** M3 requires (§4, M3's row).
  This is the state AC-DT-06's unfilled-skeleton fixture (v) requires M3 to fail
  on, and it fails on **form-membership**, not on the count: the file carries
  exactly one labelled disposition statement, whose empty content carries neither
  admitted form, and the prompt above it is not a labelled statement at all. The
  two criteria now state the **same file**, which the previous revision did not
  (§4, "The unfilled case is decided on form-membership").
  **This criterion names no mode, and as of cycle 19 that reading is grounded
  rather than merely conventional** (*told* — the cycle-19 directive's B1,
  disposing the cycle-18 gate's B1; **Dave's ruling**). Under §4's Mode scoping
  convention a claim naming no mode binds both, so this criterion has always
  bound the **cycle mode** as well — which was unsatisfiable while AC-CO-3's
  enumeration was read as exhaustive, since a cycle-mode skeleton then carried no
  disposition region at all. The ruling is that the cycle mode **emits the slot
  too**, as an extension of the emitted structure with every preserved AC-CO
  criterion untouched (§4, "The cycle mode emits the disposition statement
  too"). A skeleton generated in either mode is therefore in this criterion's
  range, and the fixtures below are generated in either.
  **The criterion additionally binds the skeleton as a whole** (*told* — the
  cycle-18 directive's B1, disposing the cycle-17 gate's B1). A generated
  skeleton contains **exactly one unfenced labelled disposition statement** — the
  emitted one — whatever committed text its prompt region or any other invariant
  region carries. This is G3's generated-skeleton invariant, and this criterion
  is where it is checked. **The two region clauses above do not imply it**: the
  prompt clause enumerates what the prompt **states** and bounds nothing about
  what its committed source may additionally **contain**, and the cycle-17 gate's
  B1 is the finding that a source explaining the labelling requirement by
  **showing** the label satisfies both clauses and still puts a second matchable
  instance in the emitted file. The invariant is therefore stated over the
  emitted file rather than over any region of it. **By what mechanism the
  generator holds to it is not fixed here** and is routed to the TRD by §8 Q10
  (§4, "Scope split with the TRD"): this criterion asserts the count, not the
  means.
  **Together the three clauses secure the property the generated path rests on** —
  that a skeleton whose content slot is filled faithfully passes M3 (J1, J2; §4,
  "The two generated cases"). The prompt states the requirement; the emitted
  label supplies the form; the invariant fixes the count. No two of the three are
  sufficient, which is why this criterion binds all three.
  Verifiable by generating a skeleton
  and asserting, from the file and its manifest alone, that the prompt region's
  text matches the committed source its manifest entry names, that the author
  region is present and begins with the label its manifest entry names as the
  region's marker, and that the content slot beneath that label is blank — and,
  over the **whole emitted file**, that the number of unfenced labelled
  disposition statements is **one**. The last assertion is a count over the file
  and needs no manifest; like AC-DT-06's M3 fixtures it is **specified now** and
  becomes **executable** once the TRD fixes the label's lexical form (§8 Q9),
  and it should be read on AC-DT-16's model until then rather than as red.
  **That it waits on Q9 is the descope's design and not a defect in this
  criterion** (*told* — the cycle-19 directive's N2, disposing the cycle-18
  gate's N2, **no action, recorded**): §8 Q9 names the three PRD-level
  properties gated on it, in one place, and names what resolves them.
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
  region was read from or an explicit marking that the region is an **author
  region**;
  and the manifest is part of the skeleton written to the directive file rather
  than terminal-only output. **Each entry carries exactly one of those two
  classifications**, never both and never neither, which is well-defined at the
  working-tree disposition because G3 splits it: the disposition **prompt** is
  an entry naming a committed file, and the disposition **author region** is an
  author-marked entry (*told* — the cycle-10 directive's B1). **The label the
  generator emits into the disposition author region is that region's marker,
  and the partition treats it as it treats every other marker** (*told* — the
  cycle-17 directive's B1): every region the generator emits begins with a
  generator-emitted marker, the task-specific author slot included, and each
  marker's bytes fall inside the extent of the region it begins. So emitting the
  label introduces no asymmetry into the partition and no new bias into §5's
  first measurement — the convention is uniform across regions and was already
  uniform before the label existed. What the measurement is bounded by is
  unchanged and stated at §5's first outcome. Every marker the manifest names appears in the emitted
  file exactly once, every region the generator emits carries one, and the manifest
  enumerates every region in emission order — so taking each entry's extent from
  its marker to the next marker or to end of file partitions the **whole file**
  with no overlap and no gap, and the generator-supplied share is the sum of the
  extents whose entries name a committed source. Verifiable by generating a
  skeleton and computing that partition from the file alone — which now yields
  **one** share for a given skeleton rather than one per classification an
  implementer might take of the disposition slot. That is the property this
  criterion was written to pin and could not pin before the split: two
  implementations, one reading the slot per G1 and one per J1, computed
  different numbers for the same landed file.
- **AC-DT-06** — For each element in the mechanically-checkable table M1–M8, a
  fixture directive missing exactly that element causes a non-zero exit, and the
  output names that element and cites the governed text it derives from. For M3
  the check is an **unconditional presence-and-form test over labelled
  disposition statements**, with no parallelism precondition, no sequencing
  precondition, and **no region extent of any kind** — its one structural
  sensitivity being the **fence exclusion** (§4, M3's row) (*told* — the cycle-15
  directive's B1, which retires the region scoping of the cycle-11 disposition,
  the whole-file fallback of the cycle-12 disposition, and the locatability
  predicate of the cycle-14 disposition; §4, M3's row) — the governed rule is
  committed (`skills/directive-authoring.md` @ `b4a0fa58` for the
  labelled-statement requirement and @ `7853525a` for the exactly-one count, the
  latter landing this cycle), so this criterion is
  **live now and its fixtures are specified now**. They become **instantiable as
  files** once the TRD fixes the label's lexical form (*told* — the cycle-17
  directive's N2, disposing the cycle-16 gate's N2). Every M3 fixture below
  states the **shape** a file must have — one labelled statement, two, none,
  this admitted form or that, fenced or unfenced — and none states literal label
  text, because M3's contract at this level is label-presence and
  form-membership and the label's form is delegated to the TRD by the governed
  rule itself (M3's row). A release gate reading §6 as an implementer checklist
  should read the M3 fixtures the way AC-DT-16 asks its own entry to be read:
  waiting on a decision session rather than red. **§8 Q9 tracks that decision**
  and names what resolves it, so the dependency is scheduled rather than
  dangling.
  **The M3 fixtures are stated over the labelled statement, and the verdicts
  below are applications of M3's row rather than a second statement of its
  check** (*told* — the cycle-15 directive's N1, which requires every M3 site to
  reference the check rather than restate it). A fixture carrying
  **one labelled disposition statement carrying one admitted form** exits 0 on
  that element, and there is one such fixture for each of the two forms — the
  sole-tree one included, which under this criterion must pass M3 rather than be
  exempt from it. A fixture carrying **no unfenced labelled disposition
  statement** exits non-zero — which reaches both the file that carries none at
  all and the file whose only labelled statement is fenced. A fixture carrying **two unfenced** labelled disposition statements
  exits non-zero. A fixture whose single labelled statement carries **neither** admitted
  form exits non-zero, and so does one whose single labelled statement carries
  **both** — the both-forms fixture the previous revision stated over a searched
  extent, restated here over the statement.
  **Three of them are named individually, because each pins a direction the
  retired apparatus decided differently** (*told* — the cycle-15 directive's B1).
  **(i) Labelled and well-formed** — a directive whose disposition is a labelled
  statement carrying exactly one admitted form: exits **0**.
  **(ii) Unlabelled prohibition-only** — a hand-written directive whose only
  working-tree statement is a **prohibition**, carrying no label: exits
  **non-zero**. That is the motivating incident, and it now fails on the count of
  labelled statements rather than on a reading of the prohibition's words, though
  the governed rule decides it in its own words as well ("A prohibition is not a
  disposition").
  **(iii) Labelled statement plus incidental mention elsewhere** — a directive
  carrying one well-formed labelled disposition statement **and**, elsewhere in
  the file, a line instantiating an admitted form without the label, such as a
  stop condition naming a directory and the `git worktree add` that creates it:
  exits **0**.
  Fixture (iii) is the discriminating one, and the pair (ii)/(iii) is where this
  cycle's reversal is pinned by a test rather than by prose. Under the retired
  whole-file fallback a directive of shape (ii) carrying such a line exited
  **0** — the false negative the cycle-14 gate filed as blocking — while a
  directive of shape (iii) exited **non-zero**. Under the labelled-statement
  check (ii) fails and (iii) passes, which is the direction the motivating
  incident requires in both cases.
  **Every fixture in this set has a decidable M3 verdict, and that follows from
  the check rather than being asserted of the set**: every file either carries
  exactly one **unfenced** labelled disposition statement carrying an admitted
  form or does not. No M3 fixture is therefore an undecidable element, none falls to
  AC-DT-10, and the two criteria agree on every one of them — a derived
  consequence, not a property this criterion claims for its own fixtures alone.
  **Two generated-skeleton fixtures remain, and what they assert is the prompt's
  exclusion rather than a scoping** (*told* — the cycle-15 directive's B1; the
  pair originates in the cycle-11 directive's B1). Both are **generated
  skeletons**, so both carry the prompt region and its naming of the two admitted
  forms, and they differ only in the author region.
  **(iv) Correctly filled** — the author region's **content slot** filled, so
  the region carries one labelled disposition statement with one admitted form:
  exits **0**, the prompt not being a labelled statement and so not counting.
  This is the ordinary generated path, and it passes **by construction** rather
  than by the author's care (J1, J2; §4, "The two generated cases").
  **(v) Unfilled** — the author region as emitted, carrying the label over a
  **blank content slot**: exits **non-zero**, the file carrying exactly one
  labelled disposition statement whose content carries **neither** admitted form,
  so it fails on **form-membership** (*told* — the cycle-17 directive's B1, which
  reconciles this fixture with AC-DT-03). The previous wording offered two
  readings — no labelled statement at all, or a label with neither form — and
  AC-DT-03 asserted the first while this fixture contemplated the second, so two
  implementations conforming to §6 produced different files. There is now one
  reading, it is AC-DT-03's, and both criteria state the same file.
  An implementation that matched the prompt's quoted forms would pass (v) and
  fail (iv), so the pair still pins the behaviour in both directions. What it no
  longer asserts is any claim about which region of the file M3 looks in.
  **(vi) One unfenced labelled statement plus fenced labelled statements** — a
  directive carrying its own labelled disposition statement in running text and,
  elsewhere in the file, one or more **fenced** labelled disposition statements,
  as a directive originating another directive's wording carries it inline under
  the carry-as-pointer rule's origin exception: exits **0** (*told* — the
  cycle-17 directive's N1; §4, "The count is exactly one"). This fixture pins the
  fence exclusion in the direction the count would otherwise break: without it,
  the ordinary directive of this effort — one dictating AC-DT-06's own fixtures
  (i)–(v) — states exactly one disposition and exits non-zero. **This fixture's
  exit is the governed rule applied rather than a narrowing of it** (*told* —
  the cycle-19 directive's N1): the fenced statements here are **carried**
  wording — another directive's, under the origin exception — so they are
  **mentions**, the file states exactly one disposition, and the governed
  "exactly one per directive" and M3's unfenced count return the same number
  (§4, "The count is exactly one"). The scoping of that reading to carried
  wording leaves this fixture exactly where it was, carriage being what it
  exhibits (*told* —
  `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
  N2). **Its complement
  is fixtured beside it rather than left as an application of another fixture's
  verdict** (*told* — the cycle-18 directive's N3, disposing the cycle-17 gate's
  N3).
  **(vii) Fenced-only disposition** — a directive whose **only** labelled
  disposition statement sits inside a fenced code block: exits **non-zero**, the
  file carrying **zero** unfenced labelled disposition statements (*told* — the
  cycle-18 directive's N3; §4, M3's row). Like every other M3 fixture here it
  states a **shape** and no literal label text, Q9's deferral applying to it as
  to the rest. Together (vi) and (vii) pin the fence exclusion in **both**
  directions, which is the convention (i)–(v) already set for every other
  direction of M3's behaviour: each of them exists because a prior cycle's
  reversal needed a test rather than prose, and the fence exclusion is this
  cycle's predecessor's reversal. **What this fixture's non-zero exit is called
  moved twice inside cycle 19 and its verdict moved neither time** (*told* — the
  cycle-19 directive's N1 for the reading and
  `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
  N2, for its scoping; both characterizations are **consequential updates under
  Core rule 13** and neither is a change to this fixture). The previous revision
  read a fenced instance as a **mention** without qualification, so a directive
  whose only labelled instance is fenced stated no disposition and this exit was
  the governed rule applied. The reading is scoped to **carried** wording, and
  such an author's fenced statement is their own rather than carried, so this
  exit is again the **false positive** §7 accepts (§7; §4, "The count is exactly
  one"). **The fixture is untouched by either movement** — the shape and the
  non-zero verdict are what cycle 18 pinned, and the verdict is non-zero under
  both scopings — which is the point of having pinned it: pinning it here is
  what would make a later narrowing of the fence exclusion **fail a test** rather
  than pass silently, and it is what lets the characterization move without the
  behaviour moving with it.
  For M8 the check is a **form-set membership
  test over three patterns**, with eight fixtures, matched against the lint's
  path argument **as resolved** to a repository-relative path and not as given
  (AC-DT-19). What the fixtures establish is
  membership and only membership; **none of them asserts mode-appropriateness**,
  and none can, because the fixture is a filename and the property is a fact about
  the invocation that produced it (§4, "What M8 claims"). Passing: a
  `<descriptor>-<timestamp>.md` fixture, a
  `cycle-<N>-directive.md` fixture, and a `<SLUG>-directive.md` fixture — the third
  added in cycle 5 per B1, because AC-CO-1's `--name SLUG` branch requires the
  cycle mode to emit exactly that name and AC-DT-15 forbids reddening the test that
  asserts it. **No fixture exercises a `<SLUG>` character boundary, and none may**
  (*told* — the cycle-7 directive's N1, resolved by its B1): pattern 3 states no
  character class at all (§4, "Pattern 3
  is bounded by AC-CO-1's destination clause"), so a character-boundary fixture
  would assert a requirement M8 does not carry and G6 forbids. The passing slug
  fixture may therefore use any characters. **Path structure is a different
  question and is fixtured**, because M8 does carry a boundary there (*told* —
  the cycle-9 directive's B2): two failing fixtures, a directive named
  `docs/cycles/sub/nested-directive.md` and one named
  `docs/escaped-directive.md`, each of which exits non-zero. Neither is a member
  of the licensed set — the first is not a single-component basename under
  `docs/cycles/`, the second is not under `docs/cycles/` at all — and both are
  names `bin/cycle-open` is **observed to emit** from `--name 'sub/nested'` and
  `--name '../escaped'` respectively (`reviews/directive-tooling-cycle-8.md` @
  `e8bf561c`, B2, verified by running there and *told* to this document). That
  the implementation emits them does not put them in the licensed set, and these
  two fixtures are where that reading is pinned by a test rather than by prose:
  a lint that passes either has been built to what `bin/cycle-open` produces
  rather than to what AC-CO-1 licenses.
  **Both are kept, and the relation between `docs/escaped-directive.md` and the
  pre-existing no-pattern fixture is stated rather than settled by dropping one**
  (*told* — the cycle-10 directive's N2 and O2 give opposite instructions for
  this fixture; the execution session stopped and surfaced rather than
  reinterpreting either, and Dave dictated in the same decision exchange that
  **N2 governs**, which the preamble records because the exchange is not in the
  directive file). The cycle-9 gate's O2 held that `docs/escaped-directive.md`
  is subsumed by the pre-existing failing fixture "a name that is neither
  timestamped nor `-directive.md`-suffixed". **That subsumption does not hold as
  stated** (*observed*, by reading the failing fixtures against M8's row): all
  three patterns carry the literal prefix `docs/cycles/`, and **four** of this
  criterion's eight fixtures fail, on four **different** clauses (*told* — the
  cycle-12 directive's N1, which corrects an enumeration reading "the three
  failing fixtures" where four fail): the pre-existing no-pattern one on the
  **suffix**, not being `-directive.md`-suffixed; `docs/escaped-directive.md` on
  the **directory anchor**, since it *is* `-directive.md`-suffixed and fails only
  for carrying `docs/` where every pattern requires `docs/cycles/`;
  `docs/cycles/sub/nested-directive.md` on the **single-component boundary**,
  carrying the right prefix and a separator inside the slug; and the
  **date-with-no-time** fixture on the **time component**, matching pattern 1 in
  every respect but the `T<time>` field M8 requires. They are
  complements, not duplicates. Dropping the escape fixture would leave M8's
  directory anchor with no fixture exercising it in the escape direction, and it
  would drop the case §4's step 3 shows has the shorter ground.
  **The eighth fixture is a resolution fixture, and it passes** (*told* — the
  cycle-14 directive's N3; the defect it disposes is the cycle-13 gate's N3): a
  well-formed directive at `docs/cycles/<descriptor>-<timestamp>.md`, invoked
  **from a subdirectory of the repository by a path that is not its
  repository-relative form** — `../../docs/cycles/<descriptor>-<timestamp>.md`
  — exits **0** on M8, because M8 matches the resolved repository-relative path
  and not the argument as typed. It is what makes the four failing fixtures
  discriminate as **resolution** questions rather than as string questions:
  without it, an implementation matching M8's patterns against the argument as
  typed passes every fixture stated as a bare name while failing a well-formed
  directive invoked from anywhere but the repository root, and nothing in this
  set would catch it. The out-of-repository refusal is the other half of the
  same rule and is verified at AC-DT-19 rather than here, because it is a
  refused invocation that reaches no element and so has no exit this criterion
  can assert of an element. The fixture count therefore stands at **eight** —
  four passing (the three pattern fixtures and this one) and four failing. Failing: a fixture whose trailing field
  is a **date with no time** (`<descriptor>-YYYYMMDD.md`) exits non-zero, because M8 requires the full
  `<date>T<time>` form that `skills/directive-authoring.md` @ `6179221a` states and
  a calendar date alone is not a timestamp for this check
  (cycle 5, N1; governed at the source in cycle 6, B2); and a fixture matching no
  pattern at all — a name that is neither
  timestamped nor `-directive.md`-suffixed — exits non-zero. The cycle-4 fixture
  asserting that a bare `<slug>-directive.md` exits non-zero is **removed**: it
  asserted the defect cycle 5's B1 names, and a fixture asserting it would now
  assert mode-appropriateness, which this criterion does not claim.
- **AC-DT-07** — A well-formed fixture directive carrying every element M1–M8
  exits 0.
- **AC-DT-08** — Exit 0 output includes the unchecked set — at minimum, that the
  following were **not** checked: executability of the working-tree disposition;
  route and model tier (which do not reach the directive file, per §4); every
  judgment-only rule in §4; and **mode-appropriateness of the filename** — M8
  checked form-set membership only, and did not check whether the pattern the
  filename matches is the pattern this directive's mode should have produced
  (*told* — the cycle-7 directive's B2). That last entry is the disclosure §7's
  accepted defect class requires at the point of use: without it, a lint built to
  this criterion could exit 0 on a hand-written `<slug>-directive.md` while naming
  an unchecked set that omits the one bound making the pass narrow, which is the
  halo failure §7 names as the primary risk.
- **AC-DT-09** — A directive citing a companion by a SHA that resolves to a blob,
  a tag, or a commit that does not touch the cited path exits non-zero and names
  the citation. The fixtures are **synthetic and live in the fixture repository**:
  a fixture directive citing a fixture companion by the **blob** hash of that
  companion's content (failing), one citing it by a tag (failing), one citing a
  commit that touches a different path (failing), and one citing a commit that
  touches the cited path (passing). Provenance for the blob case, in prose and not
  as a test input: this effort's own cycle-1 directive,
  `docs/cycles/directive-tooling-spec-20260823T194242Z.md` @ `c5398a42`, cited
  `docs/cycles/pass2-held-fix-20260823T180753Z.md` by its blob hash `9f5f4c9d`, and
  the cycle-2 directive @ `d5a82172` corrected it to `@ commit b9444973` — which is
  the shape the synthetic pair reproduces, and the reason the branch is in the
  criterion at all (*observed*, §4).
- **AC-DT-10** — An element the lint cannot decide is reported unknown and exits
  non-zero; no undecidable element yields exit 0. **Its coverage of M1–M8 is a
  derived fact, and no element is exempted from it.** M3's check is total by
  construction — a presence-and-form test over labelled disposition statements,
  on which every file either carries exactly one carrying an admitted form or
  does not, with no third outcome (§4, M3's row; §4, "M3's check is over the
  labelled statement") — so M3 is never an element the lint cannot decide, and
  this criterion has no M3 instance to govern. That is a consequence of the
  check; nothing about M3 amends, narrows, or retires this criterion (*told* —
  the cycle-15 directive's B1, which restates this coverage statement over the
  labelled-statement check; the cycle-14 directive's B1 is where the previous
  revision's rule-form statement of the non-reach was disposed).
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
  demands. **Every element M1–M8 satisfies this as written**, with no exception
  at this revision (*told* — the cycle-18 directive's N1, disposing the cycle-17
  gate's N1) — M3 included for **all three** of its requirements
  (`skills/directive-authoring.md` @ `48ad7fd1` for the two-form requirement,
  the same file @ `b4a0fa58` for the labelled-statement requirement, whose
  delegation of the label's fixed lexical form to tooling is what licenses a TRD
  to fix one without the lint enforcing an unsourced requirement, and the same
  file @ `7853525a` for the **exactly-one count**) and M8's
  timestamp rule included
  (the same file @ `6179221a`, which states the date-and-time requirement M8
  enforces). **The one exception this criterion carried at the previous revision
  is closed, and closed at the source** (*told* — the cycle-18 directive's N1).
  M3's exactly-one count was dictated by the cycle-17 directive @ `7010e8ff` and
  rested on a reading of "the disposition" as a definite singular; the fifth
  expedited amendment states the count in the governed sentence's own words —
  "exactly one per directive" — so the clause is read **off** the sentence
  rather than **into** it (§1; §4, "The count is exactly one"). The disclosure
  this criterion carried is **removed** rather than softened, and §7's "Not
  accepted" is restored in the same terms; a criterion asserting universal
  satisfaction is now true as written rather than true with a named exception.
  The **fence
  exclusion** is not an exception either: it narrows what the lint matches rather
  than adding a requirement the lint enforces, and this criterion is about
  enforcement. **Nor does it leave the count short of the governed sentence in
  the direction that would matter here** (*told* — the cycle-19 directive's N1
  for the reading and
  `docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
  N2, for its scoping): a fenced instance of **carried** wording is a
  **mention**, not a statement, so over the shapes carriage produces M3's
  unfenced count and the governed "exactly one per directive" return the same
  number and no **false negative** hides behind the exclusion. Where an author
  fences their **own** sole statement the two counts do differ, M3 counting zero
  against the governed one, and that difference runs in the **false-positive**
  direction — a narrower match, not a requirement the lint enforces — which is
  why it is §7's accepted residual and not a qualification of this criterion
  (§7; §4, "The count is exactly one").
  No element is held back, none carries a sequencing qualification, and
  **no element carries a silent carve-out from this criterion**, and at this
  revision none carries a stated one either: an element has outrun its
  source in this effort **four** times, and the resolution was an expedited amendment
  to the governed file **three** times (M3's two-form rule at `48ad7fd1`, M8's
  timestamp rule at `6179221a`, and M3's exactly-one count at `7853525a`)
  and **deletion of the requirement** once (M8's `<SLUG>` character class, cycle 7's
  B1) — never an exception recorded here. The fourth stood as a **disclosed**
  exposure at this criterion and at §7 for exactly one cycle before the amendment
  closed it, which is the pattern this document uses in place of a carve-out. The
  criterion binds every element added
  later, which is the case it now exists to catch.
- **AC-DT-14** — After migration, `bin/` contains exactly one directive-skeleton
  generator. The reviewer-gated cycle skeleton is produced by `bin/directive` in
  its cycle mode, it carries Route and Model and no Track (DEC-000180), and
  `bin/cycle-open` no longer emits a skeleton of its own. Verifiable by generating
  a cycle skeleton through the new path and by static inspection of `bin/`.
- **AC-DT-15** — The migration preserves the contract it absorbs:
  `bin/tests/test_cycle_open.py` passes after the migration, with AC-CO-1 through
  AC-CO-12 — `docs/packages/package-a-spec.md` §3.6 and §8.2 @ `768bbe3b` —
  satisfied and none of them retired — whichever binary each criterion is
  invoked through, which is the TRD's question and not this criterion's. A red in
  that suite is a failed migration, not a superseded criterion. Verifiable by
  running the pre-existing suite.
  **The cycle-mode disposition slot does not red it, and that is checked rather
  than assumed** (*told* — the cycle-19 directive's B1; *observed* for the
  suite): the three cases implementing AC-CO-3 are **presence** assertions over
  the emitted text, so a skeleton carrying AC-CO-3's enumerated elements **and**
  the disposition slot passes them (§4, "The cycle mode emits the disposition
  statement too"). This criterion is satisfied by that reading rather than
  excepted from it.
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

- **AC-DT-17** — **M2 is a resolvability-and-touch check and nothing more, and
  §6 states its two upper bounds so that §6 read alone cannot support the strict
  check** (*told* — the cycle-5 directive's N2; the narrowing itself is cycle 4's
  N1, argued in §4 under "M2's Derived-from is narrowed"). What M2 enforces: for
  each `<path> @ <sha>` companion citation, the path is present at the reviewed
  ref, and the SHA resolves to a commit that touches that path. What M2 does
  **not** enforce, and what this criterion makes testable: **(a) fullness** — a
  citation by an **abbreviated** SHA that resolves to a touching commit exits 0 on
  M2; and **(b) lastness** — a citation by a commit that touches the path but is
  **not** the last commit to touch it exits 0 on M2. Both fixtures are **synthetic
  and live in the fixture repository** (*told* — the cycle-6 directive's N2), each
  constructed to the shape it must exercise. The fixture repository carries a
  governed file with a **content commit** followed by a later frontmatter-only
  commit touching the same path, and the two fixture citations are: **(a)** that
  file cited by the **abbreviated** content commit, which exercises fullness; and
  **(b)** that file cited by the **full** content commit, which is not the last
  commit touching the path and so exercises lastness. Each isolates one property,
  and both exit 0 on M2.
  The shape is not invented: this document's own citations have it, which is why the
  criterion exists. Provenance, in prose and not as a test input —
  `skills/directive-authoring.md` is cited here at `48ad7fd1`, `b4a0fa58`,
  `7853525a`, `83b60511`, and
  `6179221a`, each eight characters and each a content commit, while the last commit
  touching that path is `d4a3158b`, a frontmatter-only status transition; this
  document cites it that way deliberately, five times, following
  `reviews/expedited-log.md`'s own convention (*observed*, §1). A lint that fails
  either fixture has been built to `policies/document-metadata-policy.md` and
  AC-CO-4 rather than to M2, and it would reject the document that specified it.
  Verifiable by running the lint over the two fixture citations and asserting exit
  0 on M2 for each, in a fixture repository and with no dependence on this
  repository's history.

- **AC-DT-18** — **G2's criterion** (*told* — the cycle-9 directive's O5, which
  requires G2 to carry one). In a freshly generated skeleton, the source manifest
  (G11, AC-DT-05) marks **exactly one** region as the **task-specific author
  slot**, marks **exactly one** region as the **disposition author region** G3
  requires, and every other region it enumerates names a **committed path** it
  was read from. So a
  skeleton carries exactly one region for the directive's substance that the
  decision session composes freehand, exactly one author region for the
  disposition, and
  no third region that is the author's to write. Verifiable by generating a
  skeleton and reading its manifest alone: count the entries marked as the
  task-specific slot — which must be one — count the entries marked as the
  disposition author region — which must also be one — and assert that every
  remaining entry names a committed path. That is what makes G2
  decidable rather than a restatement of G1, G3, and G11: it fixes **how many**
  freehand regions a skeleton has and **which**, and none of those three states
  either.
  Two bounds, both stated rather than assumed. **First**, this is a property of
  the **emitted skeleton**, not of the landed file — an author may write inside a
  generator-supplied region afterwards, and neither the manifest nor this
  criterion records that; §5's first outcome carries the same bound.
  **Second, the disposition slot's representation in the manifest is settled,
  and this criterion states it rather than holding under either reading**
  (*told* — the cycle-10 directive's B1; the bound this replaces recorded the
  question as open, which is what the cycle-9 gate raised as blocking). G3 splits
  the slot: the **prompt** is an entry naming a committed path, the **author
  region** is an author-marked entry, and each carries exactly one
  classification. So the manifest of a freshly generated skeleton carries
  **exactly two** author-marked entries — the task-specific region and the
  disposition author region — and this criterion is a count of two named things
  rather than a count that varies with how an implementer classified the slot.
  The question reached G11's partition and §5's first measurement and not only
  this criterion, and both are now stated over the split at their own sites
  (§4 G3, G11; §5, first outcome).

- **AC-DT-19** — **G5's criterion, at the level a PRD carries it** (*told* — the
  cycle-9 directive's O5). The lint is invocable at the point in the executor's
  first act where G5 places it: it takes the **path of the directive file as it
  stands on disk** as its only required argument, and no check it performs
  requires that file to have been staged, committed, or pushed. Running it
  between "write the directive file" and "commit and push" therefore adds no step
  to the executor's sequence — the mechanically decidable half of G5.
  **The argument is resolved before any element's check applies to it** (*told* —
  the cycle-14 directive's N3; the defect it disposes is the cycle-13 gate's N3).
  The lint resolves the argument to a **repository-relative path from the
  repository root**, and what M8's patterns are matched against is that resolved
  path and never the argument as typed. The argument may therefore be given
  relative to any working directory or as an absolute path. **An argument that
  resolves outside the repository is a refused invocation and exits non-zero**,
  reporting the refusal rather than an element finding, so a path escaping the
  root is neither silently matched against M8 nor reported as a missing element.
  Which non-zero status a refusal carries, and whether refusals and element
  findings are distinguished by status, is **Q6** and is answered at the TRD
  stage; that a refusal is non-zero is fixed here.
  **The motivating precedent is recorded, not hypothetical.**
  `docs/packages/package-a-spec.md` §8.2 AC-CO-12 @ `768bbe3b` records that the
  sibling tool this document absorbs shipped resolving `--out` against the
  current working directory and accepting absolute paths inside the repo — spec
  and code disagreeing, a correctness defect that required a re-gate to correct —
  and states the rule this criterion applies to the lint's own argument: "`--out`
  is interpreted **relative to the repo root**, not to the current working
  directory, and **any absolute path is refused with exit 2** … as is any path
  escaping the root via `..`". The two halves of the binary pair therefore
  resolve paths the same way, which is what AC-CO-12's own note asks for ("One
  rule, stated once, is worth more than a convenience here"). One difference is
  deliberate and stated: AC-CO-12 refuses **every** absolute path, including one
  inside the repo, because `--out` names a location the tool **writes**; the lint
  writes nothing and is handed a file that already exists, so an absolute path
  inside the repository resolves and is checked, and only a path resolving
  outside the repository is refused.
  Verifiable in a fixture repository, in four invocations. On an **uncommitted
  and unstaged** directive file, the lint reaches a verdict on every element
  M1–M8 — in particular M1 and M2, whose checks resolve SHAs against the object
  store, do not require the directive file itself to be an object in it. On the
  same file named **from a subdirectory by a relative path**, and on the same
  file named by an **absolute path**, the verdict is the same as the first, which
  is what pins the resolution and what AC-DT-06's resolution fixture asserts for
  M8 specifically. On a path resolving **outside the repository**, the invocation
  is refused with a non-zero exit that names no element.
  **The remainder of G5 is not testable at PRD level and is marked for the TRD
  stage.** Where the invocation sits relative to commit and push on the
  **failing** path — whether a directive that fails the lint still lands for the
  audit trail — is **Q2**, open and Dave's to answer; and the ordering of the four
  steps in the executor's act is a property of the execution session's procedure,
  which no criterion over either tool can assert. §2, J2, and G5 describe the
  passing path only, which is what keeps them consistent with Q2. This criterion
  fixes the tool-side precondition that makes either placement possible; the
  placement itself is stated at the TRD/AC stage once Q2 is answered.

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

**Accepted, as a minor defect class with a named mitigation** (*told* — the
cycle-6 directive's B1). A **hand-written** general-mode directive named
`<slug>-directive.md` passes M8 without a timestamp. M8 claims form-set membership
only, and mode-appropriateness is not decidable from a filename by any check (§4,
"What M8 claims"), so this residual is not closable inside the lint. It is accepted
rather than engineered around: the mitigation is the generator, which makes the
pattern correct by construction because the mode chooses the name and the author
does not, and G4 keeps the general mode ungated so it can be adopted before the
lint is trusted. The class does not reach generated directives at all, and a
hand-written directive that also omits a required element is still failed by
M1–M7. **The defect class is disclosed at the point of use**: AC-DT-08's unchecked
set names mode-appropriateness explicitly, so a lint built to §6 cannot exit 0
without stating this bound (*told* — the cycle-7 directive's B2). Cycle 7
**widened the defect class**, by dropping pattern 3's character class: the residual
reaches any hand-written `<slug>-directive.md`, not only a
lowercase-and-hyphens one. It is accepted at that width, for the same reason and with the same
mitigation — the class the drop removed was a requirement no governed file states,
which G6 forbids the lint from enforcing (§4, "Pattern 3 is bounded by AC-CO-1's
destination clause"). **Cycle 9 narrowed the defect class again, in the one
dimension a governed sentence decides**, and the narrowing is not the deleted
character class returning under another name (*told* — the cycle-9 directive's
B2): pattern 3 now admits a
**single-component basename only**, because AC-CO-1's destination clause states
where the output lands and a separator-bearing name does not land there. That
boundary is read off cited governed text, which is precisely what the deleted
class was not, so G6 is satisfied in both directions — the lint enforces nothing
no governed file states, and it admits nothing the governed text does not
license. The residual that remains after both moves is the mode-appropriateness
one and only that: a hand-written `<slug>-directive.md` in one path component
still passes M8. What would close it is a mode or class marker in the directive
file for the lint to read, which is Q5's open question and not a change this
document makes.

**Accepted, and the residual set is stated in extension** (*told* — the
cycle-15 directive's N2 for this restatement, its B1 for the check the residuals
are stated over). M3 leaves **two** residuals under the labelled-statement
check. They run in opposite directions, and both are named here rather than left
to be found.

**Residual one — a labelled statement whose content is false.** M3 reads
**label-presence and form-membership**. It cannot read whether what the
statement says is **true**: a directive carrying the label and one admitted form,
and naming a tree the session does not use or a command it will not run, passes.
Truth of the content is in neither half of the check, and no check over the
directive text can supply it, the fact that would decide it being in the
executor's environment rather than in the file. This is an instance of the class
§4's judgment-only table already carries as "whether the dictated content is
correct, or executable in the executor's environment", and it is disclosed at
the point of use by AC-DT-08, whose unchecked set names every judgment-only rule
in §4 together with executability of the working-tree disposition. Its direction
is the **false negative** — the lint passes a directive that is wrong. There is
no mitigation inside the lint and none is claimed: the generator's adoption does
not reach it either, because the generator emits the **prompt** and the author
writes the **statement**.

**Residual two — a labelled statement carried outside a fence.** A directive
that carries **another directive's labelled disposition statement in running
text, outside a fenced code block**, carries **two** unfenced labelled statements
and exits non-zero, though it states exactly one disposition of its own. A label
carried is a label present, and distinguishing an asserted statement from a
carried one is not a property this document fixes. The governed rule does not
draw that line either: it distinguishes the labelled statement from **incidental
mention of trees or commands**, not from a labelled statement under carriage, so
a lint that tried to draw it would be enforcing a requirement no governed file
states (G6).

**This residual is stated over the shapes the governed authoring rules actually
produce, and the previous revision stated it over shapes they forbid** (*told* —
the cycle-17 directive's N1, disposing the cycle-16 gate's N1). That revision
named a provenance note, a carried constraint, and a citation of a prior cycle.
All three are **carried-forward** wording, and
`skills/directive-authoring.md`'s fifth authoring rule directs an author to
carry such wording **as a pointer** — path, SHA, and section, never restated — so
a conforming author does not produce any of the three, and the residual as
stated was over shapes that do not occur. The shape that **does** occur is that
rule's own exception: a directive that is itself the wording's origin carries it
**inline**, and this effort's own directives are the standing instance, one
dictating AC-DT-06's fixtures (i)–(v) originating several labelled statements at
once. The **fence exclusion** is what keeps that instance passing (§4, "The
count is exactly one"; AC-DT-06 fixture (vi)), so what is left of the residual is
the author who carries such wording inline and **unfenced** — a false positive of
authoring style, not of the check's reach. This is the governing rule §4's
judgment-only table already carries as its carry-as-pointer entry, and the
cross-reference is made here so the two are read together.

**A second shape runs the same direction**: an author whose only disposition is
written **inside** a fence carries zero unfenced labelled statements and fails.
It is pinned by a fixture of its own — AC-DT-06's **(vii)** — rather than by an
inference from another fixture's verdict, so a later cycle narrowing or dropping
the fence exclusion moves a test rather than only this paragraph (*told* — the
cycle-18 directive's N3, disposing the cycle-17 gate's N3). **The previous
revision removed this shape from the set, and it is restored here** (*told* —
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
N2, disposing the cycle-19 gate's N2; the removal was a **consequential update
under Core rule 13** drawn from the cycle-19 reading of the count taken
unscoped, and its reversal is one too). That reading is scoped to **carried**
wording: a fenced copy or duplicate is a mention, but an author's **own** fenced
sole statement is a statement they formatted badly, so such a directive **has**
stated its disposition and M3's non-zero exit on it is a false stop on a
well-formed directive (§4, "The count is exactly one"). Fixture (vii)'s
**verdict is unchanged by either reading** — it exits non-zero under both
scopings — so nothing executable moved in either direction, and what moved twice
is this section's characterization of why. The movement is stated at both ends
rather than left to a diff, because this section states its set in extension and
a member leaving it and returning is a change a reader of either revision has to
be able to see.
Neither shape is produced by the generated path, which emits the label
unfenced (G3, AC-DT-03) into a skeleton carrying exactly one unfenced labelled
disposition statement (G3's generated-skeleton invariant, which holds in **both**
modes as of this cycle). Both are **false positives** — a false stop on a
well-formed directive, at a cost of one invocation, which is the direction this
section's next item accepts in general. The mitigation available to the other
residuals is not available here, the generator emitting the prompt and the label
rather than policing what an author carries. What would close them is a TRD-stage
label form a carried statement cannot reproduce, or a governed rule about
carrying directives; neither is decided here, and the residual is accepted at
this width.

**Whether M3's match is sensitive to any further markdown context is not left
open**: the fence exclusion is its only such sensitivity at this level, and
indentation, list nesting, block quotes, and HTML blocks are TRD concerns (M3's
row). Cycle 15's N1 asked the question and the previous revision carried no
answer; this revision answers it at PRD level rather than parking it.

**The accepted set changed in extension again this cycle, and the change is
stated rather than characterized** (*told* — the cycle-15 directive's N2; the
framing this replaces is the "restated, not widened as a defect class" label the
cycle-14 gate's N2 filed against, which is dropped rather than repaired). M3's
accepted residual has now been stated three ways across cycles 12, 14, and 15,
and the set changed in **extension** each time, not only in wording. Cycle 12
accepted a **false positive** over one shape: a hand-written directive that
pasted the generated prompt into itself. Cycle 14 restated it over every file
reaching the retired whole-file branch, which added the damaged-manifest shape
the cycle-12 statement had excluded by name. This cycle the set changes in both
directions at once. **Removed**: both cycle-12 and cycle-14 shapes, because M3
no longer reads the file's text at large, so generator-sourced text naming both
forms cannot be counted — neither the pasted-prompt shape nor the
damaged-manifest shape reaches anything. **Removed**: the **false negative** the
cycle-14 gate filed as blocking, and by construction rather than by acceptance —
a prohibition-only directive carries no labelled disposition statement and fails
whatever else the file mentions (§4, "M3's check is over the labelled
statement"). **Added**: the two residuals above. So the set neither grew nor
shrank as a whole; it was **replaced**, and the false-negative member is new in
kind — the residual this section carried at cycles 12 and 14 was false-positive
only, and this one is not. That is stated plainly because a false stop costs one
invocation and a false pass costs whatever the wrong tree costs, and the two are
not interchangeable in an accepted-risk list.

**The set changed again in cycle 17, in extension and in one direction only**
(*told* — the cycle-17 directive's N1). Residual one is unchanged. Residual two
**shrank**: under the fence exclusion it no longer reaches the carried wording a
conforming author writes as a pointer, nor the originating wording a conforming
author fences, and what remains is unfenced inline carriage plus the
fenced-only-disposition shape. **One shape is new in kind and it is named
rather than folded in**: the fenced-only disposition did not exist as a residual
before this cycle, the fence exclusion being what creates it, and it is a
**false positive** like the carriage shape beside it. The **false-negative**
member of the set is still residual one and still the only one, so the direction
mix is unchanged, and the set's extension is narrower on balance — the point of
the restatement being that it is now stated in shapes an author can recognize
rather than in shapes the authoring rules forbid.

**The set did not change in cycle 18, and that is stated rather than left to a
diff** (*told* — the cycle-18 directive's N1 and N3; this document restates the
extension whenever it moves, so a revision where it does not move says so).
Residual one and residual two stand exactly as the previous revision states them,
in both members and both directions. The **exactly-one count** becoming governed
text does not touch them: the count was never a residual of the check, it was an
exposure of the count's **source**, recorded in "Not accepted" above and now
closed there. The **fence exclusion** — which is what produces both of residual
two's shapes — is untouched by that amendment and remains this document's, so
what an author can trip on is what it was. The only change at these two residuals
is that the fenced-only shape is now pinned by AC-DT-06 fixture (vii).

**The set does not change in cycle 19 — neither in extension nor in direction —
and the movement the previous revision stated is reversed here** (*told* — the
cycle-19 directive's N1 for the reading and
`docs/cycles/directive-tooling-spec-19-fix-20260824T081022Z.md` @ `5ea201e6`,
N2, for its scoping; the movement stated at the previous revision and its
reversal here are both **consequential updates under Core rule 13**, neither a
dictated disposition of its own). Two things happen here and they should not be
confused. **First, nothing is added.** The cycle-18 gate read the
newly-governed "exactly one per directive" as flat and M3's count as
fence-scoped, and reported that the difference was an undisclosed **false
negative** of this set. The cycle-19 disposition resolves that **by reading, not
by amendment**: a fenced instance of **carried** wording is a mention, so for
the shape the gate described the two counts are the same number and it violates
nothing (§4, "The count is exactly one"). Residual one is therefore still the
**only** false-negative member of this set, and the claims above are true as
written. **Second, nothing leaves either.** The previous revision reclassified
residual two's fenced-only shape as correct behaviour and left residual two with
**one** shape where it had two. The reading is scoped to carried wording, and an
author's own fenced sole statement is not carried, so that shape is a **false
positive** and it stands: residual two carries **two** shapes — unfenced inline
carriage and the fenced-only disposition — as it did at cycles 17 and 18. The
**count of residuals is two**, the extension is what the cycle-17 revision left
it, and the direction mix is unchanged, residual one remaining the only false
negative and residual two remaining a false positive. **Nothing else about the
check moves**: the fence exclusion is still this document's, its provenance
untouched by the reading (§4), and AC-DT-06's fixtures (vi) and (vii) keep their
verdicts, which they do under both scopings.

Two bounds on the acceptance, so it is auditable. It is **not** an acceptance of
the motivating incident going uncaught: that case fails mechanically now, and
nothing in this item softens it. And it is **not** the residual the cycle-11
gate's B1 proposed closing by requiring a conforming manifest on every directive
— that reading is still declined, and it is now moot, since the anchor M3 uses
is carried by the governed rule rather than by a manifest, and no hand-written
directive is put outside M3's range by it.

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
enforcement of a requirement no governed file states (G6, AC-DT-13). **Four**
elements have stood in that position in this effort, and **all four are closed at
this revision** (*told* — the cycle-18 directive's N1, disposing the cycle-17
gate's N1; the previous revision recorded the fourth as standing and disclosed).
A reader of this section should be able to audit the claim it makes about itself,
since this is the section Dave signs: at this revision the claim is "**none
stands**", where at the previous revision it was "one stands".
**Two were closed by amending the governed source**, not by taking an exception
here: M3's unconditional two-form rule is governed text at
`skills/directive-authoring.md` @ `48ad7fd1`, and M8's date-and-time requirement
is governed text in the same file @ `6179221a`. **A third stood for exactly one
cycle and was closed the other admissible way — by deletion rather than
amendment**: cycle 6's `<SLUG>`
character class stated a requirement no governed file states, and cycle 7's B1
removed it from M8 instead of seeking an amendment or recording a carve-out (*told*
— the cycle-7 directive's B1). Deletion is the cheaper route where the requirement
was never needed, and that it was available is what keeps this item true without a
further expedited amendment taken **for that purpose**. **The fourth also stood
for exactly one cycle, and it was closed by amendment because the requirement is
one M3 needs**: M3's **exactly-one count** was dictated by the cycle-17 directive
@ `7010e8ff`, was disclosed here and at AC-DT-13 rather than absorbed, and is
governed text as of the fifth expedited amendment to the same skill @ `7853525a`,
which states "exactly one per directive" in the rule's own words (§1; §4, "The
count is exactly one"; AC-DT-13). The disclosure is **removed** rather than
softened. Which of the two routes fits is decided by whether the requirement is
needed: deletion where it was not, amendment where it was, and this effort has now
taken each where it fits. The **fence exclusion**
does not stand in this position and never did: it narrows what the lint matches
rather than adding a requirement the lint enforces. Neither the fourth amendment
to that file, `b4a0fa58`, nor the fifth's **labelled-statement** half is an
instance of an element outrunning its source: each tightened the governed rule
and M3 followed it, rather than M3 having enforced the property before the rule
stated it (§1; AC-DT-13). The prohibition
stands undiminished for every element
added after any of them. **Cycle 9's single-component boundary on pattern 3 is not
a fourth instance and does not stand in that position** (*told* — the cycle-9
directive's B2; *observed* for the source): it is stated by AC-CO-1's own
destination clause at `docs/packages/package-a-spec.md` §3.6 @ `768bbe3b`, so it
is a requirement a governed file states, cited where it states it. The test this
item applies is whether a governed sentence can be pointed at, and here one can.

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
  prerequisite is discharged: M3's unconditional two-form rule is stated in that
  skill as of `48ad7fd1`, and its labelled-statement requirement as of the same
  skill @ `b4a0fa58`, and its exactly-one count as of the same skill @
  `7853525a`, each agreed via `reviews/expedited-log.md` and merged to
  `origin/main` in `820d071e`, `7bbb3a71`, and `b5fc675c` respectively, so
  nothing in this
  document waits on an amendment
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
  **One further status question is carried here rather than left dangling**
  (*told* — the cycle-14 directive's N3 fixes the refusal but not its status):
  AC-DT-19 refuses an invocation whose path argument resolves outside the
  repository with a **non-zero** exit, and whether that refusal is distinguished
  by status from an element finding is the same severity-model question and is
  answered with it. That the refusal is non-zero is fixed at AC-DT-19 and is not
  open.
  Resolved by: Dave, or a stated severity model at the TRD/AC stage.
- **Q7 — closed** (cycle 2, by the B2 disposition). Whether the working-tree
  requirement is "a named directory" or "a named directory plus the command
  creating it." It is the latter, for the assignment branch, with a literal
  sole-tree declaration as the only alternative. M3 is now writable as a test
  (AC-DT-06). The residual obligation this created — amending
  `skills/directive-authoring.md` so G6 is satisfied — is **discharged**: the
  amendment landed at `48ad7fd1` and is recorded in §1 and Q4, not here.

- **Q8 — closed** (cycle 3, by dictated disposition; **widened in cycle 5, by a
  second dictated disposition**). Which filename convention M8 enforces, given
  that G0 puts a generator required to emit AC-CO-1's filenames inside a lint that
  a single-pattern M8 would require to reject them. Recorded as a question because
  the choice lay between governed conventions and was not the author's to make.
  Chosen, cycle 3: two forms, the cycle mode emitting the AC-CO-1 form and every
  other mode the timestamp form. Chosen by: Dave, in
  `docs/cycles/directive-tooling-spec-3-20260823T203821Z.md` @ `d258434e`.
  **Chosen, cycle 5: three patterns**, because AC-CO-1 names two filename branches
  and cycle 3 licensed only the first — the cycle mode emits
  `cycle-<N>-directive.md` for `--cycle N` and `<SLUG>-directive.md` for
  `--name SLUG`, the general mode emits the timestamp form, M8 accepts exactly
  these three, and no governed source is amended. Chosen by: Dave, in
  `docs/cycles/directive-tooling-spec-5-20260823T214112Z.md` @ `ff0f56f0`. Two
  residuals are closed with it: `skills/directive-authoring.md`'s "Naming"
  sentence was amended at `83b60511` and no longer omits Core rule 14's yield
  clause (cycle 4), and M8's cycle-mode patterns now anchor on AC-CO-1 directly
  rather than on the skill's partial restatement of it (cycle 5, §4).
  **Scoped, cycle 6**: what the three-pattern answer asserts is **form-set
  membership only**. Mode-appropriateness was never decidable from a filename, the
  cycle-5 wording implied M8 decided it, and §4's "What M8 claims" now states that
  the generator guarantees it by construction and M8 does not check it, with the
  hand-written residual accepted in §7. Scoped by: Dave, in
  `docs/cycles/directive-tooling-spec-6-20260823T222826Z.md` @ `fe4ee58c`.
  **Loosened, cycle 7**: pattern 3 states **no character class**. The class cycle 6
  gave it was a requirement no governed file states, which G6 forbids the lint from
  enforcing, and which would have made a legal AC-CO-1 invocation emit a name the
  same binary's lint rejects; dropping it leaves the three-pattern answer intact and
  changes no figure in the corpus recount (§4). Loosened by: Dave, in
  `docs/cycles/directive-tooling-spec-7-20260823T230004Z.md` @ `34a57ac7`.
  **Bounded, cycle 9**: pattern 3 matches a **single-component basename**, no
  path separators. Cycle 8's independent gate found that "any slug the preserved
  contract can emit" was implementable two ways and that the phrase did not say
  whether it meant what AC-CO-1 licenses or what `bin/cycle-open` produces. The
  disposition answers both halves: it means what AC-CO-1 **licenses**, and
  AC-CO-1's destination clause — output at `docs/cycles/<name>-directive.md` — is
  what bounds the name to one component. Implementation behaviour beyond the
  licensed set is not pattern 3's referent, and the two names cycle 8 observed
  `bin/cycle-open` emit are failing fixtures in AC-DT-06. No governed source is
  amended and no figure in the recount moves. Bounded by: Dave, in
  `docs/cycles/directive-tooling-spec-9-20260823T233309Z.md` @ `b0f84690`. What Q8
  does
  **not** answer, and what §4 now routes elsewhere: whether a fourth branch exists
  anywhere in AC-CO-1 through AC-CO-12 (§3.6 and §8.2 @ `768bbe3b`). Under the
  conflict rule in §4's "Mode
  scoping", finding one is a blocking finding, not a fourth widening of M8.
- **Q9 (raised by the cycle-16 gate; open).** The label's **lexical form** — the
  fixed text that marks a working-tree disposition statement, which M3 matches
  on and which `bin/directive` emits into the disposition author region. The
  governed rule delegates it in its own words ("the label's fixed form is a
  tooling concern, not this document's"), and this document states M3's contract
  at label-presence and form-membership and goes no further (§4, M3's row).
  **What waits on the answer, and what does not.** M3's contract does not wait
  on it, nor does AC-DT-03's structure, nor AC-DT-06's fixture **shapes**; what
  waits is instantiating those fixtures as **files**, since none can be written
  without the literal text (AC-DT-06). Until it is fixed, an implementer reading
  §6 as a checklist should read the M3 fixtures as waiting on a decision session
  rather than as red, on AC-DT-16's model. **B1's reconciliation is the other
  half of the same decision** (*told* — the cycle-17 directive's B1 and N2): the
  generator emits the label, so whatever the TRD fixes is what the lint matches
  and what a faithful author sees, and the two cannot drift apart. Recorded as a
  question because leaving it untracked is what let the generator and the lint
  disagree about it for two cycles.
  **One property the resolution must satisfy is fixed here, and it is not a
  choice of form** (*told* — the cycle-18 directive's N2, disposing the cycle-17
  gate's N2): the generator and the lint **source the label from one committed
  definition**. Whatever lexical form the TRD fixes, it is fixed **once** and
  both tools read it; a TRD giving `bin/directive` and `bin/check-directive`
  separate label constants would not have resolved this question. The reason it
  is stated as a constraint rather than left implicit is that nothing else in
  this document requires it. J2's "the generator and the lint cannot disagree
  about the label" and §4's passing-by-construction property both rest on there
  being one form rather than two; AC-DT-02's static check ranges over the
  generator's **invariant** regions and the label is explicitly not invariant
  text (G3), so it does not reach the label; and AC-DT-06's fixture (iv) would
  catch a divergence only once the fixtures are instantiable, which is what this
  question gates. Stating the single-source property here keeps the divergence
  **scheduled** rather than accepted, and it is a property of the resolution
  rather than a mechanism, which is why it sits at PRD level (§4, "Scope split
  with the TRD").
  **Three PRD-level properties are gated on this question, and that is the
  descope's design rather than a defect** (*told* — the cycle-19 directive's N2,
  disposing the cycle-18 gate's N2, whose disposition is **no action,
  recorded**). They are named here, in one place, so a release gate reading §6
  as a checklist can see the set rather than reconstruct it: **(a)** AC-DT-06's
  M3 fixture set, which is specified as shapes and instantiable as files only
  once the label's literal text exists; **(b)** the **single-source** property
  stated immediately above, which AC-DT-06's fixture (iv) catches a violation of
  only once the fixtures are instantiable; and **(c)** AC-DT-03's assertion that
  a generated skeleton carries exactly **one** unfenced labelled disposition
  statement, which is a count of labelled statements and so uncomputable without
  the label (G3's generated-skeleton invariant). All three are **specified now**
  and read on AC-DT-16's model until this question resolves. **That they queue
  behind one question is a property of the split, not a shortfall in executing
  it**: the descope routes mechanisms and fixes the properties they must secure
  (§4, "Scope split with the TRD"), and a question naming its resolver is a
  deferral this document intends. A TRD stage resolving Q9 discharges all three
  at once; one deferring it again leaves the set where it is, which is a
  **scheduling** item for the release gate rather than a defect in the text. No
  criterion is amended for it and none is proposed.
  Resolved by: the **TRD stage**, which fixes
  the form and the single source together; nothing in this document is held back
  by it.
- **Q10 (raised by the cycle-17 gate, routed here by the cycle-18 descope;
  open).** By what **mechanism** a generated skeleton holds to G3's
  generated-skeleton invariant — that the emitted file contains exactly one
  unfenced labelled disposition statement, whatever committed text its invariant
  regions carry. **The invariant is not open**: it is fixed at G3 and checked at
  AC-DT-03, and J1 and J2's passes-by-construction property rests on it. The
  **means** is open, and the candidates differ materially: the committed source
  the disposition **prompt** is read from shows the label only inside a
  **fenced** block, which M3 does not match; or that source is **bounded** so it
  does not show the label at all; or the generator **fences sourced text** as it
  emits it, which reaches every invariant region rather than the prompt alone.
  Each choice constrains **Q1**'s answer, since Q1 fixes where the invariant text
  lives and therefore who may edit it into violating the invariant, and the two
  are best resolved together. Recorded as a question because the previous
  revision rested the property on a categorical reading — a prompt is not a
  labelled disposition statement — which is true of what a prompt **is** and
  silent about what its text **contains**, and that gap is what the cycle-17 gate
  filed as blocking.
  **One constraint on the answer is visible now and is stated rather than left to
  be discovered at the TRD.** AC-DT-03 asserts, of a generated skeleton, that the
  **prompt region's text matches the committed source its manifest entry names**.
  A mechanism that transforms sourced text **at emission** — the third candidate,
  fencing as the generator emits — would put fence markers in the emitted region
  that the committed source does not carry, so taking it obliges a matching change
  to AC-DT-03's assertion rather than leaving that criterion standing as written.
  The first two candidates leave it untouched, because both act on the committed
  source rather than on the emission. The cost is stated here so the choice is
  made with it visible, and so a TRD taking the third does not silently red a
  criterion this document states.
  Resolved by: the **TRD stage**, together with Q1; nothing in
  this document is held back by it.
