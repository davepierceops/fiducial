---
status: draft
last-reviewed: null
audience: [human]
---

# TRD: directive tooling — `bin/directive` and `bin/check-directive`

This is the standing technical specification for the two tools
`specs/directive-tooling.md` specifies. That document owns *what* they do and
*why*; this one owns *how*.

It proposes. Where a choice is product judgment, or where making it would amend
an agreed goal or acceptance criterion, this document records it in §9 as an
open technical question naming what would resolve it, rather than settling it
here. Three questions the PRD routes to Dave — Q2, Q4, Q6 — are carried in
§9 in exactly that form, with options, tradeoffs, and a recommendation. Every
other section is written to stand whichever way each of the three is ruled;
where a section cannot, §9's entry names it.

## 1. System overview

Two **single-invocation command-line tools**, not services. Each runs once in a
working tree and exits. Neither holds a process, listens on anything, or
persists state of its own.

- **`bin/directive`** — the generator. Assembles a directive skeleton from
  regions, each read from committed governed text or left as an author slot,
  and emits it together with a manifest of where each region came from. Two
  modes: **cycle mode**, which is `bin/cycle-open`'s surface after the G0
  migration (§3.9), and **general mode**, every other directive class.
- **`bin/check-directive`** — the lint. Takes the path of a directive file as
  it stands on disk, decides the eight elements M1–M8, and exits non-zero when
  any is missing or undecidable. It writes nothing, anywhere.

They are the ninth and tenth executables in `bin/`. The shape is the one the
existing eight use: a `#!/usr/bin/env python3` shebang, `argparse`, a
`sys.path.insert` onto the script's own directory, then `from aimeta import
...`, with `sys.exit(cli.run(main))` as the last line.

The two tools share one committed file and one module. The file is
`skills/directive-invariants.md` (§3.2): the generator reads its region text,
and the lint reads the disposition label and match rule defined in it. The
module is `bin/aimeta/invariants.py`, the only code that parses that file. That
sharing is not an economy — it is the mechanism by which the generator's output
satisfies the lint by construction (G3), and by which the label has one
definition rather than two agreeing copies (Q9's property).

Everything is Python 3 standard library. No third-party import is added;
`bin/tests/test_cross_cutting.py` AC-X-2 enforces that over every production
file under `bin/`.

## 2. User journeys and SLOs

The PRD declares Top K = 3: J1 author a directive from the skeleton, J2 the
executor's first act clears the lint, J3 a directive missing a required
element.

**None of the three has an SLO.** This is stated explicitly, as the template
requires, and recorded in §9 as OQ-1.

The reason is structural rather than an omission, and it is the same reason
`specs/bin-land-trd.md` §2 gives for its tool: an SLO is an objective observed
in production against a running surface, and neither tool has one. Each is a
script executed inside a session's sandbox; neither emits telemetry, nothing
aggregates invocations, and no error budget can be consumed because no shared
service degrades when either fails. The PRD says the same from the product
side — no latency target, scalability N/A.

### J1 — author a directive from the skeleton

- **SLO**: none. Unverified in production.
- **Measurement mechanism**: none in production. Pre-release, PRD §6's
  acceptance criteria against the substrate in §4.1. Post-adoption, the
  generator-supplied share of a landed directive, computed from the manifest
  in the landed file — PRD §5's first outcome signal, which is a corpus count
  rather than a rate observed from the tool.
- **Alerting threshold**: N/A. There is no aggregate to threshold.

### J2 — the executor's first act clears the lint

- **SLO**: none. Unverified in production. The property that would otherwise be
  this journey's objective — that a faithfully filled skeleton passes — is not
  a rate but a construction, proven before release by AC-DT-03 and AC-DT-06's
  fixture (iv), and made true by §3.2's three conditions rather than observed
  afterwards.
- **Measurement mechanism**: the test suite, pre-release. In production, the
  session's own report.
- **Alerting threshold**: N/A.

### J3 — a directive missing a required element

- **SLO**: none. What matters here is not a rate but where the cost lands, and
  PRD §5's second outcome signal measures that by reading execution reports and
  retros: lint failures at the first act versus executor stops after work
  began.
- **Measurement mechanism**: execution reports and retros, read by hand.
- **Alerting threshold**: N/A.

## 3. Architecture and boundaries

### 3.1 Components and responsibilities

| Component | Responsibility |
| --- | --- |
| `bin/directive` | Parse argv, select the mode, call the assembler, write or print the result, exit with the mapped code. No git logic, no region text, no rendering decisions. |
| `bin/check-directive` | Parse argv, resolve the path, call the element set, serialize the finding report, exit with the mapped code. No element logic. |
| `aimeta/invariants.py` | New. Parses `skills/directive-invariants.md` into named sections; exposes each section's raw body, the substitution pass, the disposition label literal, M3's match rule, the marker syntax, the preamble-marker list, and §3.6's match phrases. The single reader of that file. |
| `aimeta/directive.py` | New. The region set per mode, emission order, substitution, the manifest, and the generated-skeleton invariant. Cycle mode's identity and document-set resolution, migrated from `bin/cycle-open`. |
| `aimeta/mdmask.py` | New. One pure function over directive text: which lines are eligible for a line-anchored match, and which are masked (§3.5). Touches no git and no filesystem. |
| `aimeta/elements.py` | New. M1–M8, one function each, over `(root, relpath, text, eligible_lines, invariants)`. Returns per-element results. Knows nothing of exit codes or output format. |
| `aimeta/cli.py` | Existing, reused unchanged. Exit constants, `ToolError`, `diagnostic`, `relpath_of`, `repo_relative_path`, `load_root`, `load_context`. |
| `aimeta/repo.py` | Existing, reused unchanged. `git`, `run`, `last_commit_sha`, `file_at_rev`, `methodology_home`. |
| `aimeta/closure.py` | Existing, reused unchanged. Cycle mode's `--bundle` expansion. |

Dependency direction runs one way and carries no cycle:

    bin/directive       → directive.py → invariants.py, repo.py, closure.py, cli.py
    bin/check-directive → elements.py  → invariants.py, mdmask.py, repo.py, cli.py

`invariants.py` and `mdmask.py` import neither `directive.py` nor
`elements.py`. `mdmask.py` imports nothing of this repository's at all.

Two splits are load-bearing rather than tidy:

- **`invariants.py` apart from both tools.** The label and the match rule exist
  in one committed file, read by one function, called by both binaries. A
  second definition anywhere — a regex in the lint, a string constant in the
  generator — is the defect AC-DT-02 scans for and the failure Q9's property
  names. Making it one module rather than one convention is what turns
  agreement between the two tools into a structural fact.
- **`mdmask.py` apart from `elements.py`.** M3's markdown sensitivity (§3.5) is
  the part of this design most likely to need revision after the first corpus
  of post-adoption directives exists. Isolating it as a pure text function
  means that revision is exercised by a test file that builds no repository at
  all, and that no element's logic has to move when it changes.

### 3.2 Where the invariant text lives — Q1 and Q10, decided jointly

The PRD routes both questions to this stage and notes that each choice
constrains the other. They are decided here as one decision because the second
is a property of the first.

**Q1 — decision: a new governed standing document,
`skills/directive-invariants.md`, holding one section per region, each
addressed by its heading; the generator copies a named section's body
verbatim, substituting a closed set of placeholders.**

The PRD's other two candidates were considered and are rejected on facts about
the repository as it stands:

- **A section of an existing governed file addressed by heading.** Two of G1's
  six named regions have no governed home to address. No file under
  `policies/`, `docs/global-context/`, `skills/`, `context-sets/`, or `roles/`
  contains the word *sandbox* at all; and the nearest thing to a governed
  report format is one sentence of Decision Layer rule 14, which states that a
  directive must be written so its report is triageable and states no format.
  The four regions that do have homes have them in the wrong register: Core
  rule 11 is *"Cannot execute as written → stop and surface"*, a standing rule
  addressed to every agent, not a stop-conditions block pinned to one reviewed
  ref for one session. Emitting it verbatim would put rules-register prose
  where directive prose belongs, and the author would rewrite it — which is the
  freehand surface the effort exists to shrink.
- **A machine-readable block inside existing governed files.** Solves neither
  problem above, and puts tool-shaped markup into documents whose audience is
  human and whose review gate has nothing to do with tooling.

The chosen document is therefore a **new home for text that has no home**, not
a copy of text that has one. That distinction matters, because a governed file
restating rules stated elsewhere is the drift this repository has already paid
to remove. §3.3's table states, per region, whether its text is net-new or
renders an existing governed rule; exactly one region does the latter, and
§3.3 states the check that keeps it honest.

Placement is `skills/`, beside `skills/directive-authoring.md`, whose audience
it shares — `[chief-of-staff, human]`. It is not placed under
`docs/global-context/`, whose files are loaded as governing context by every
session; this one is read by a tool and by the author reviewing what the tool
produced.

**Resolution is against committed content, not the working tree — and the
tree it resolves in is the methodology home, not the repository the tool was
invoked in.** The generator reads each section's body from the last commit
touching the invariants document *in the repository that holds that document*:
`repo.last_commit_sha` and `repo.file_at_rev` are called with
`repo.methodology_home(root)` as their root, not with `root`. This is the
discipline AC-CO-4 already imposes on cycle mode's scope list, applied in the
tree the input actually lives in. An uncommitted edit to the invariants
document is refused (§6, FM-G3), downgraded to a `WARN` by `--allow-dirty`,
which is AC-CO-5's behaviour applied to a second class of input; FM-G3's
`git status --porcelain` runs in the same tree. This is what makes AC-DT-01
literal: the section changes in the next skeleton when its **commit** changes,
with no edit to the generator.

**The home-vs-root relationship this assumes.** `repo.methodology_home` returns
`$AI_METHODOLOGY_HOME`, else `root`, else `root.parent/"ai"`. Only the second
candidate makes the home and the invocation root the same tree. This design
assumes nothing about which candidate is taken; it assumes exactly one thing —
**the methodology home is a git repository, and the invariants document is
committed in it**. Where home and root coincide, that assumption is free: it is
the repository the tool was invoked in. Where they do not — a sibling checkout,
or `$AI_METHODOLOGY_HOME` pointing elsewhere, which is the configuration the
home mechanism exists for — the two trees carry independent histories, and the
SHA a manifest entry records for an invariants-document section is a SHA in the
home's history. A reader resolving that entry in the directive's own repository
will not find it. That is stated rather than designed around: the manifest's
job is to name the revision the text was read at, and the revision is the
home's.

**There is no fallback when the home is not a repository.** The generator
refuses (§6, FM-G1): `last_commit_sha` returns `None` for a path in a tree with
no history, and a section whose committed body cannot be read is, for this
design's purposes, a section that is not there. Refusing is what keeps AC-DT-01
literal rather than partially true — a generator that fell back to the working
tree would emit a skeleton whose manifest names a revision it did not read.

**What the test fixture must therefore provide.** §4.1's `make_home` must
`git init` and commit the invariants document inside the home, not merely write
files into a directory. That is one helper change, and §3.9 names it as the
migration's most likely red.

**The substitution syntax.** Region bodies are templates. A placeholder is
`{{name}}` from a closed set fixed per region in §3.3; `{{{{` is a literal
`{{`. A placeholder the generator does not recognise is a refusal, not a
silent pass-through (§6, FM-G4). The set is closed and small deliberately: it
is a second syntax a human author of that document must respect, and its whole
cost is bounded by being enumerable in one table.

**Q10 — decision: the invariants document carries the disposition label only
inside fenced code blocks, and the generator fences nothing at emission.**

The PRD's third candidate — the generator fences sourced text at emission — is
rejected on the PRD's own ground: it would put fence markers in the emitted
region that the committed source does not carry, obliging an amendment to
AC-DT-03's prompt-matches-source assertion. This document does not amend agreed
criteria.

Between the remaining two, the choice is the fenced-example form rather than
the bounded-silence form, and the bound is then widened from the prompt section
to the whole document. The reason is F-3 (§9, OQ-8): the sole-tree form of the
disposition has zero instances in the 144-file `docs/cycles/` corpus, so an
author needing it has nothing to imitate. A prompt that may not show the label
can only describe it. A prompt that shows both admitted forms, worked, inside a
fence, hands the author the sentence F-3 says does not exist — in the one place
both tools read, at the moment of use. AC-DT-06's fixture (vi) already fixes a
file carrying one unfenced labelled statement plus fenced ones as a **passing**
shape, so the emitted skeleton is a shape the criteria already contemplate.

**The generated-skeleton invariant, and why it holds.** G3 requires that the
skeleton as emitted, in either mode, contains exactly one unfenced labelled
disposition statement. Three conditions make that true, and each is mechanical:

1. Every invariant region is copied verbatim from a section of
   `skills/directive-invariants.md`; the generator composes no prose of its own
   (AC-DT-02).
2. That document contains the label only inside fenced blocks. This is a
   property of one file, asserted by one test that reads it and applies §3.5's
   mask.
3. The generator emits the label unfenced in exactly one place: as the
   disposition author region's marker.

Condition 2 is where Q1 and Q10 meet, and it is why they are one decision.
Under Q1's rejected first candidate the bound would have to be imposed on
`skills/directive-authoring.md`, `docs/global-context/core.md`, and whatever
else a region was addressed into — a tooling constraint on documents whose
review has nothing to do with tooling, and one that a future amendment to any
of them could break silently. Under the chosen candidate it lands on exactly
one file, authored for this purpose, whose test is one file read.

Together the three conditions are AC-DT-03's count assertion made executable.

### 3.3 The regions, the markers, and the manifest — G11 decided

**Marker syntax — decision.** A marker is a line, at column 0, that is either:

- an ATX heading: one to six `#` characters, a space, then text; the marker
  token is the text after the `#` run; or
- an **all-caps run**: three or more characters drawn from `A`–`Z`, `0`–`9`,
  `-`, and single interior spaces, terminated by any character outside that
  set or by end of line; the marker token is the run.

Nothing else is a marker. The syntax is stated in the invariants document and
compiled by `invariants.py`, so the generator and the lint read one definition
(§3.5 needs it for M5).

The syntax is chosen to satisfy one hard constraint the PRD sets: G3 requires
the disposition author region's marker to *be* the TRD-fixed label. So markers
cannot be HTML comments or any other invisible form — the label is
human-readable text an author writes beneath. The all-caps arm makes
`WORKING-TREE DISPOSITION` an instance. The heading arm exists because
AC-CO-3's cycle skeleton is built from ATX headings that may not be dropped,
reordered, or altered; with headings as markers, cycle mode's regions align
exactly with the structure AC-CO-3 already fixes, and no marker line has to be
added above or beside one.

**Uniqueness and partition.** Every marker the generator emits appears exactly
once in the file, and each region's extent runs from its marker to the next, so
the entries partition the file with no gap and no overlap (AC-DT-05). The
first region's marker is the file's first line, so the partition has no head
gap. Uniqueness is a generator-side invariant asserted by AC-DT-05, not a lint
check: the manifest is an output of the generator and an input to nothing the
lint does (G11).

**The manifest.** Emitted as the final region. Its preamble — the prose saying
what the manifest is — is itself read from a committed section, so its own
entry names a committed path and AC-DT-18's "every other entry names a
committed path" holds without exception. The entries are the region's payload,
in emission order, one line each:

    <marker token> — <path> @ <full sha>
    <marker token> — author region

Exactly one classification per entry (G11). The path alone satisfies AC-DT-05;
the SHA is the discipline AC-CO-4 already imposes on cycle mode's scope list,
and it is what makes the generator-supplied share of a landed directive
computable against a known revision rather than against whatever the invariants
document says later.

**General-mode regions, in emission order.**

| # | Marker | Region source | Placeholders |
| --- | --- | --- | --- |
| 1 | `<title>` (heading) | `§Heading (general)` | `{{title}}` |
| 2 | `ROUTE AND MODEL` | `§Route and model` | `{{route}}`, `{{model}}` |
| 3 | `FIRST ACT` | `§First act` | `{{directive_path}}` |
| 4 | `DISPOSITION PROMPT` | `§Working-tree disposition prompt` | — |
| 5 | `WORKING-TREE DISPOSITION` | **author region** | — |
| 6 | `BASE VERIFICATION` | `§Base verification` | `{{reviewed_ref}}` |
| 7 | `COMPANIONS` | `§Companions` | `{{companion_list}}` |
| 8 | `TASK` | **author region** | — |
| 9 | `SANDBOX` | `§Sandbox constraints` | — |
| 10 | `VERIFICATION` | `§Verification steps` | — |
| 11 | `STOP CONDITIONS` | `§Stop conditions` | `{{reviewed_ref}}` |
| 12 | `REPORT` | `§Report format` | — |
| 13 | `CLAIM LABELS` | `§Claim labels` | — |
| 14 | `SOURCE MANIFEST` | `§Source manifest` | `{{manifest}}` |

Fourteen regions: two author, twelve committed — AC-DT-18 exactly.

**Route and model are emitted, and not checked.** `--route` and `--model`
supply region 2's two placeholders. Both flags are accepted in both modes, and
the cycle-mode table below carries the same region read from the same section,
so a directive of either class states the dispatch that produced it. The values
go into a **committed** region rather than an author slot: the author-region
count stays at two, which is what G2 and AC-DT-18 fix, and the manifest
classifies region 2 as committed like every other sourced region. The lint
checks neither value. Route and model stay in AC-DT-08's unchecked set, the
element set stays at eight, and no element derives a requirement from
DEC-000180 — which fixes route and model of the *dispatch*, not of the file,
and would have to be amended before any lint could enforce them.

**The prompt is region 4, and its marker is `DISPOSITION PROMPT`.** G3 makes
the disposition slot two regions — an invariant prompt and an author region —
and AC-DT-03 asserts directly on the first: its text must match the committed
source *its manifest entry names*, and it must state that a disposition is
required, name both admitted forms, and state the labelled-statement
requirement. So the prompt is an emitted region with a marker, a source
section, and a manifest entry, like any other. Its marker token is
`DISPOSITION PROMPT` rather than `WORKING-TREE DISPOSITION PROMPT` because the
label literal may not begin a second marker line: §3.2's condition 3 says the
generator emits the label unfenced in exactly one place, and a marker beginning
with the literal would make that sentence false even though §3.4's colon
requirement would keep the line out of M3's match. AC-DT-03 fixes no marker
token, so the choice is free and is made where it keeps condition 3 literally
true.

**Cycle-mode regions, in emission order.** AC-CO-3's six items appear in
AC-CO-3's relative order; added regions are interleaved without disturbing it.

| # | Marker | Region source | Note |
| --- | --- | --- | --- |
| 1 | `Cycle <n> Directive — <title>` or `<Title> Directive` (heading) | `§Heading (cycle)` | Carries the heading, the `Date:` line, and the `Documents in scope:` list — AC-CO-3's first three items, one region because AC-CO-3 fixes them as one block. Two marker forms, one per selector; see below |
| 2 | `ROUTE AND MODEL` | `§Route and model` | Added; the same section general mode's region 2 reads, with the same two placeholders |
| 3 | `FIRST ACT` | `§First act` | Added |
| 4 | `DISPOSITION PROMPT` | `§Working-tree disposition prompt` | Added; G3's first region |
| 5 | `WORKING-TREE DISPOSITION` | **author region** | Added; the slot the PRD names |
| 6 | `Decisions` (heading) | `§Decisions` | AC-CO-3, carrying the commented placeholder verbatim |
| 7 | `Deferred / out of scope` (heading) | `§Deferred` | AC-CO-3 |
| 8 | `Execution notes` (heading) | **author region** | AC-CO-3's third section; cycle mode's task-specific slot |
| 9 | `BASE VERIFICATION` | `§Base verification` | Added |
| 10 | `COMPANIONS` | `§Companions` | Added |
| 11 | `SANDBOX` | `§Sandbox constraints` | Added |
| 12 | `VERIFICATION` | `§Verification steps` | Added |
| 13 | `STOP CONDITIONS` | `§Stop conditions` | Added |
| 14 | `REPORT` | `§Report format` | Added |
| 15 | `CLAIM LABELS` | `§Claim labels` | Added |
| 16 | `SOURCE MANIFEST` | `§Source manifest` | Added |

Sixteen regions: two author, fourteen committed. Every row is enumerated rather
than given as a range, because AC-DT-05's partition and AC-DT-18's counts are
per-mode assertions over the entries themselves, and a range names no marker to
assert on. The correspondence with general mode, stated once so it need not be
inferred from the table: general mode's region 2 is row 2 here, and general
mode's regions 6, 7 and 9–13 are rows 9–15, all carrying the same source
sections and the same placeholders; general mode's `TASK` region has no
counterpart, cycle mode's task-specific slot being row 8.

**AC-DT-14's route-and-model clause is satisfied by row 2.** The criterion
requires the cycle skeleton to carry Route and Model and no Track; row 2 emits
both, from the section general mode reads, and no region of either mode emits a
`Track:` line — DEC-000180 retired it, and nothing in the invariants document
restores it. Both modes therefore carry the region, and the clause is discharged
by the cycle emission rather than by a check.

**Row 1 has two marker forms, one per cycle-mode selector.** `--cycle N` emits
`# Cycle <n> Directive — <title>`, whose marker token is
`Cycle <n> Directive — <title>`. `--name SLUG` emits `# <Title> Directive`,
whose token is `<Title> Directive`, `<Title>` defaulting to the slug with its
hyphens read as spaces. Both are AC-CO-1's forms, preserved unchanged by the
migration. The two are **one region and one manifest entry either way**, so
AC-DT-18's counts read identically under each — sixteen entries, two author,
fourteen committed — and AC-DT-05's partition reads identically too: the token
is whatever text follows the `#` run on the emitted line, that line is the
file's first, so the partition has no head gap, and the token appears once. What
differs between the selectors is the entry's marker *text*, and AC-DT-05 fixes
the entry as naming "the marker that begins the region" rather than any
particular literal. Nothing in either assertion depends on which form was
emitted, which is why the row is one row and not two.

**Cycle mode's region 5 is a committed region an author writes into.** The
`## Decisions` placeholder is committed text (AC-CO-3 requires those exact
fields), so the manifest classifies it as committed, which is accurate for *the
skeleton as emitted* — the only thing the manifest claims. PRD §5 already bounds the
measure this way: an author writing inside a generator-supplied region
afterwards is not recorded. The consequence is worth stating rather than
discovering: in cycle mode the region the author fills most is a committed one,
so the generator-supplied share reads higher for cycle directives than the
author's real contribution warrants. The measure is sound for the comparison
PRD §5 draws — before and after, within a class — and over-reads across classes.

**Which regions render an existing governed rule.** Of the twelve committed
sections the general-mode table reads, eleven are text that exists nowhere else
today. One does not: `§Working-tree disposition prompt`, which renders
`skills/directive-authoring.md`'s first bullet under "Writing the directive
file". That section carries the bullet verbatim, flowed, inside its fence, and
a test asserts byte-equality against the bullet as committed. Drift between the
two is then a red test rather than a reader's discovery — which is the cost
`reviews/directive-authoring-cycle-3.md`'s downstream-exposure table prices for
by-value quotation, paid here in a place that fails loudly.

#### The invariants document's own format

§3.2 decides *that* the document holds one section per region, "each addressed
by its heading", and the two tables above address them. It fixes no schema for
the document itself, and the tools parse it, so the schema is fixed here.

**Heading level.** One `#` title opens the document. Every section is a `##` ATX
heading at column 0, and there is no third level. A section's body is everything
between its heading and the next section heading, under one rule that is
load-bearing rather than incidental: **the first non-blank line of a body is
always body, never a heading.** Three region sections — `Decisions`, `Deferred`,
`Execution notes` — carry an ATX marker as the first line of their body (rows 6,
7 and 8 of the cycle table), so a parse that ended a section at the first `##`
line inside it would read all three as empty and invent three sections that are
not there. The rule is what makes cycle mode's AC-CO-3 headings expressible as
committed region text at all.

**Section-name form.** A section's name is its heading text, in sentence case,
and it names the **region rather than the marker**: `Deferred` is the name,
`Deferred / out of scope` is the marker its body carries. The names are the keys
the tables above address, written there as `§<name>`. There are twenty-one:

- **seventeen region sections** — `Heading (general)`, `Heading (cycle)`,
  `Route and model`, `First act`, `Working-tree disposition prompt`,
  `Base verification`, `Companions`, `Task`, `Sandbox constraints`,
  `Verification steps`, `Stop conditions`, `Report format`, `Claim labels`,
  `Decisions`, `Deferred`, `Execution notes`, `Source manifest`;
- **four lint sections** — `Disposition label`, `Marker syntax`,
  `Preamble markers`, `Match phrases`.

**A committed region's marker line is the first line of its committed section
body.** The marker is copied text, not prose the generator composes, which is
§3.2's condition 1 applied to the one line an author would otherwise expect the
tool to supply from a literal of its own. It is also what keeps AC-DT-02
satisfiable in the direction that matters: the criterion forbids the generator's
source from reproducing a line of a manifest entry's committed content, and a
marker line is such a line.

**An author region has no committed content, so AC-DT-02 does not reach its
marker.** Its manifest entry names no path, and the criterion scans per entry
against *that entry's* committed content; where there is none, a marker literal
in the generator's source offends nothing the criterion states. This design
holds no such literal anyway, and the reason is Q9 rather than AC-DT-02: the
disposition author region's marker is the label, read from `§Disposition label`,
which the single-source property (§3.1) requires, and `TASK` and
`## Execution notes` are read from `§Task` and `§Execution notes`, whose bodies
are their marker lines and nothing else. What makes those entries *author*
entries is that the region's content below the marker is the author's — which is
the whole of what AC-DT-18's classification claims.

**Where §3.4's three parts live.** All three — the literal the generator emits,
the match rule the lint compiles, and the statement's extent — are in the one
`## Disposition label` section, together with the exclusive-assignment form's
rule. **The canonical sole-tree sentence is in that same section**, inside a
fence, and `§Working-tree disposition prompt`'s own fence carries it worked, per
§3.2's Q10 decision. One section, so a change to the label's definition moves
the generator's emission and the lint's match together rather than one of them.

**Where §3.6's compiled phrases live.** `## Match phrases`, one fenced block per
element, each labelled by its element: M1's `reviewed ref`; M4's two
stop-condition phrases; M5's four first-act phrases; M6's `report`; M7's four
class words. M2, M3 and M8 have no block, and their absence is not an omission —
M2 and M8 match no phrase at all, and M3's strings are `## Disposition label`'s.

**Fencing.** The label literal appears in this document only inside fenced
blocks, which is §3.2's condition 2 and the one property of the one file that
makes G3 hold. `## Preamble markers` and `## Match phrases` fence their strings
for the same reason the label section does: they are text a tool compiles, and a
fence is what separates a string to be matched from prose about matching.
`## Marker syntax` fences nothing, because it states a grammar rather than a set
of strings.

### 3.4 The disposition label — Q9 decided

**Decision: the label is the literal `WORKING-TREE DISPOSITION`, and a labelled
disposition statement is a line whose leading content, after §3.5's stripping,
is that literal, followed by a colon anywhere later on the same line.**

Stated as three parts, all three in the invariants document's one
`## Disposition label` section (§3.3):

- **The literal the generator emits:** `WORKING-TREE DISPOSITION:` at column 0.
- **The match rule the lint compiles:** an eligible line (§3.5) whose leading
  content is exactly the literal, with any text permitted between the literal
  and the first `:` on that line. Case-sensitive. No hyphen variants, no case
  folding, no other spelling.
- **The statement's extent:** the label line plus every following line up to
  the first blank line — one paragraph. Form-membership is decided over that
  extent.

The parenthetical tolerance is not decoration. The form a decision session
writes today is `WORKING-TREE DISPOSITION (exclusive assignment):`, and a rule
admitting only the bare literal would fail the current practice on its first
use. What it admits is bounded: the leading literal is exact, and the colon is
required.

The extent rule is what makes AC-DT-06's fixture (v) — generated skeleton,
content slot blank — decidable. A blank slot is a label line followed
immediately by a blank line; the extent is the label line alone; it carries
neither admitted form; M3 fails on form-membership, which is what the fixture
asserts. Fixture (i) is the same shape with a filled paragraph.

M3's "no region extent" clause is read as *the statement need not sit inside
any particular generator region* — M3 is total over the file — and not as *the
statement has no textual extent*, which would leave form-membership undecidable
and fixture (v) uninstantiable. The reading is recorded in §9 as OQ-9 because
it is a reading of agreed text rather than a mechanism the PRD routed here.

**Form-membership.** Over the statement's extent, exactly one of:

- **Exclusive assignment** — a path-shaped token and a command creating a tree.
  Decided as: the extent contains a `git worktree add` invocation, and a
  quoted or backticked path-shaped token. Both, or neither.

  **That match rule is this document's own narrowing, and is disclosed as
  one.** The governed rule — `skills/directive-authoring.md`'s first bullet
  under "Writing the directive file", carried into PRD M3 verbatim — admits
  "a named directory plus the command creating it". It names no subcommand and
  no quoting. This document fixes both halves narrower: `git worktree add` for
  the command, and a quoted or backticked token for the path. The narrowing
  bounds what the lint **matches**; it adds nothing the lint **enforces**. No
  directive is required to write its disposition this way, and the requirement
  M3 states remains the governed one. AC-DT-13 is satisfied on exactly the
  reading it states for the fence exclusion — "it narrows what the lint matches
  rather than adding a requirement the lint enforces, and this criterion is
  about enforcement" — and §3.5's mask is disclosed on the same ground.

  What the narrowing costs is a **false stop**: a well-formed disposition
  phrased outside the match — a bare unquoted path, another tree-creating
  command, or a command introduced in a block below the statement's extent —
  fails M3 though the author did state a disposition. That cost is accepted,
  and it is not a new risk: it instantiates PRD §7's accepted item "a lint that
  stops an executor on a well-formed directive it mis-parses", whose accepted
  reason is that "a false stop costs one invocation and returns the question to
  a decision session. That is the cheap direction, and every other false
  positive here leans on it." This is one of those false positives, named. The
  direction is ruled rather than open; OQ-7 records the parallel narrowing on
  the sole-tree branch, which is not.
- **Sole-tree declaration** — the extent contains the literal sentence
  `## Disposition label` fixes as the canonical sole-tree form (§3.3), which is
  also the worked example the prompt's fence carries. A literal, because F-3 records
  that no instance of this form exists to generalise from, and inventing a
  pattern from zero examples would enforce a shape no author has ever written.

Zero forms fails; both forms fails; exactly one passes — AC-DT-06's last two
shapes.

**The three criteria this unblocks**, which PRD §8 Q9 names: AC-DT-06's M3
fixtures become instantiable as files; the single-source property is satisfied
by §3.1's `invariants.py` split; and AC-DT-03's count assertion becomes
executable.

### 3.5 M3's markdown sensitivity — decided

`mdmask.py` takes directive text and returns the set of **eligible** line
indices — lines a line-anchored match may consider — plus, per eligible line,
its **leading content** after stripping. Everything M3 does about markdown is
here, and nothing else in the lint knows markdown at all.

**Masked (not eligible):**

- **Fenced code blocks.** Backtick or tilde, an opening run of three or more of
  the same character at column 0 or indented up to three spaces, closed by a
  run of at least the opening length. An unclosed fence masks to end of file.
  The fence lines themselves are masked. This is the exclusion the PRD states.
- **Blockquotes.** A line whose leading non-whitespace is `>`. Same rationale
  as the fence: carriage of another document's wording is the common case for
  both. Masking narrows what the lint matches rather than adding a requirement
  it enforces, so AC-DT-13's reasoning about the fence exclusion covers this
  one unchanged.
- **HTML comments.** From a line containing `<!--` through the line containing
  the matching `-->`. `bin/cycle-open`'s own skeleton puts its placeholder
  decision entry inside an HTML comment, so commented-out text is already
  established in this corpus as non-content, and cycle mode emits that
  placeholder unchanged.

**Not masked:**

- **Indented code blocks.** Four-space indentation is how this corpus writes
  continuation lines inside list items, and masking it would silently drop real
  dispositions. The cost is that a genuinely indented code block containing the
  label produces a false stop — the cheap direction, per PRD §7.

**Leading-content stripping**, applied to every eligible line before the
literal is tested: up to three leading spaces; then one list marker (`-`, `*`,
`+`, or digits followed by `.` or `)`) and the space after it; then an ATX
heading run and its space; then leading `**` or `__`. Applied once each, in
that order. The corpus writes labels bare, bulleted, and bolded, and refusing
the bulleted form would fail authors on a distinction no governed file draws.

**Not handled, deliberately:** inline code spans. A label inside backticks in
running prose — *the `WORKING-TREE DISPOSITION` label* — is not line-leading
after stripping, so the line-anchored match already excludes it. No inline
parser is added for a case the anchor decides.

**Line endings.** `\r\n` and `\r` are normalized to `\n` before masking. The
literal match is byte-exact thereafter.

### 3.6 The lint's sequence

One invocation, in order, stopping at the first refusal:

1. **Parse.** One required argument: the directive file's path. `--help` exits
   0 (AC-X-3).
2. **Resolve the path.** Via `cli.load_root` and `cli.relpath_of`, to a
   repository-relative path from the root, whatever the working directory and
   whether the argument was relative or absolute (AC-DT-19). A path resolving
   outside the repository is a refused invocation naming no element; a path
   that does not exist likewise. Neither requires the file to be staged,
   committed, or pushed.
3. **Read the file** and build the mask (§3.5). One read, decoded UTF-8
   explicitly (AC-X-7).
4. **Load the invariants** — the label, the match rule, the marker syntax, the
   preamble-marker list, and the match phrases — from the methodology home
   (§3.7), **at their last commit there, exactly as the generator reads them**
   (§3.2). The read is scoped to committed content, and an uncommitted
   modification to the invariants document is a refused invocation (§6, FM-L7),
   the lint-side analogue of FM-G3. The reason is Q9's single-source property:
   the generator's output satisfies the lint by construction only if both tools
   read the same bytes, and a working-tree edit that reached one tool and not
   the other would break that construction with no diagnostic anywhere. The lint
   has no `--allow-dirty` to downgrade the refusal with — it takes one required
   argument and no flag (step 1) — and the refusal is applied after step 4's
   absence check, so a document that is not there is still `invariants-missing`
   rather than `invariants-dirty`.
5. **Decide M1–M8**, each independently, each returning pass, fail with a
   named cause, or unknown. No element reads another's result. M3 is total by
   construction and never returns unknown.

   **What returns unknown, named as one class.** An element is unknown when **a
   git read fails for a reason the lint cannot attribute to the directive** — an
   unreadable object store, a damaged repository, `git` exiting with no answer
   about the object. These are environment faults rather than findings: nothing
   about the directive's text has been decided, so no coded finding would be an
   honest report of them. Every condition in that class maps to `element-unknown`
   and exit 1 (§7), which is AC-DT-10's requirement that no undecidable element
   yields exit 0, and it is the only class that does. The boundary against a
   finding is drawn by the citation cases: a SHA that resolves to no object is
   `citation-unresolvable`, a claim *about the citation the directive wrote*; a
   read that cannot say whether the object exists at all is unknown.
6. **Report and exit.** The checked set, the per-element result, and the
   unchecked set, on both exit paths (G9, AC-DT-08). Exit per §7.

**Per element:**

Each element below states its **match** (the phrase or phrases tested), its
**extent** (the span the match is decided over), its **anchoring** (whether the
match is line-leading or free within the extent), whether §3.5's **mask**
applies, and its **derivation** (the governed wording the phrase is read from,
or, where there is none, a disclosure saying so). *Extent* where it is a
statement means §3.4's: the matched line plus every following line up to the
first blank line. All phrase matches are case-insensitive and collapse interior
whitespace runs to one space, unless an element says otherwise.

- **M1** — a reviewed-ref pin is present, and its SHA resolves to a commit
  (`git cat-file -e <sha>^{commit}`).
  - **Match:** an eligible line containing the phrase `reviewed ref` (the two
    words separated by whitespace or a hyphen) and, later on that same line, a
    run of 7 to 40 hexadecimal characters bounded by non-hexadecimal characters
    or by a line end. That run is the SHA the element resolves.
  - **Extent:** one line. **Anchoring:** free within the line — the corpus
    writes the pin bolded, bulleted, and mid-sentence. **Mask:** applies.
  - **Derivation:** `skills/directive-authoring.md`, "Pin STOP conditions to
    the reviewed ref", supplies the phrase; the hexadecimal run is the ref that
    bullet says to pin, not wording added here.
- **M2** — for each companion citation of the form `<path> @ <sha>`: the SHA
  resolves to a commit; **the object the SHA itself names is a commit** —
  `git cat-file -t <sha>` returns exactly `commit`; the path is present in that
  commit's tree; and **that commit itself touches the path**, decided as
  `git diff-tree --root --no-commit-id --name-only -r <sha> -- <path>`
  returning a non-empty result. Nothing more. Neither fullness nor lastness is
  checked, which is AC-DT-17's whole content: an abbreviated SHA of a touching
  commit passes, and a content commit that is not the last touching the path
  passes.
  - **The object-type step, and why it is separate from resolution.**
    `cat-file -e <sha>^{commit}` peels, and so does `diff-tree`: an annotated
    tag's SHA satisfies both, because git resolves the tag object to the commit
    it points at before answering. AC-DT-09 requires a citation by tag to fail,
    so the type is read **unpeeled** and compared for equality with `commit`; a
    `tag` or a `blob` fails with `citation-unresolvable`, before the touch test
    runs. What the step reaches is bounded, and the bound is stated rather than
    left to be discovered: **a lightweight tag is indistinguishable from its
    commit.** A lightweight tag's ref carries no object of its own, so the SHA
    an author copies out of it *is* the commit's SHA and `cat-file -t` returns
    `commit` — it passes, correctly, since it names the commit M2 is about.
    **Only an annotated tag is rejectable**, and AC-DT-09's "tag" is satisfied
    on that form, which is the form its fixture builds.
  - **`--root` is not optional.** Without it, `diff-tree` compares a root
    commit against nothing and reports it as touching no path — so a citation
    naming a fixture repository's first commit, which is the natural way to
    build AC-DT-09's fixtures, would fail though that commit introduced the
    file.
  - **`git log -1 --format=%H <sha> -- <path>` is not the mechanism**, and a
    non-empty result from it is not the property M2 states. Given a pathspec,
    `log` walks history, so it is non-empty whenever *any* ancestor of `<sha>`
    touches the path, and returns that ancestor rather than `<sha>`. Compared
    for *equality* with the resolved `<sha>` it decides the same property as
    `diff-tree --root`; the `diff-tree` form is chosen because it states the
    property directly rather than by comparison, and because it needs no
    separate resolution of `<sha>` to compare against. AC-DT-09's third fixture
    — a commit touching a different path — is a fail under either form and a
    pass under the non-emptiness reading, which is why the form is fixed here
    rather than left to the implementer.
  - **A merge commit touches nothing, for M2's purposes.** `diff-tree` emits no
    diff for a merge without `-m` or `-c`, and `log`'s pathspec walk simplifies
    merges away, so both forms agree. A citation naming a merge fails M2 with
    `citation-not-touching`. That is the cheap direction (PRD §7): a companion
    is cited for its content, and the content commit is the one to cite.
- **M3** — §3.4 and §3.5.
- **M4** — both stop conditions present: cannot-execute-as-written, and
  concurrent tree mutation.
  - **Match:** two independent tests over the whole file, each satisfied by an
    eligible line containing the phrase — `cannot execute as written` for the
    first, `concurrent tree mutation` for the second. Both must be satisfied.
  - **Extent:** one line each. **Anchoring:** free within the line.
    **Mask:** applies.
  - **Derivation:** the two phrases are the governed rules' own trigger
    clauses, read verbatim — Core rule 11, "Cannot execute as written → stop
    and surface", and Core rule 15, "Concurrent tree mutation → stop and
    surface". The invariants document's `§Stop conditions` section is written
    to contain both, which is how the generator's own output satisfies M4.
- **M5** — a first-act statement is present, and no other marker line (§3.3)
  precedes it except those the invariants document lists as **preamble
  markers**.
  - **Match:** the first extent containing all four of a form of the verb
    *write*, the word *commit*, the word *push*, and the phrase
    `report the SHA`. That extent is the first-act statement.
  - **Extent:** as above. **Anchoring:** free within the extent.
    **Mask:** applies.
  - **Derivation:** Core's Vocabulary entry for *Execution block* — "Its first
    instruction is to write the directive to a file, commit, push, and report
    the SHA" — supplies all four phrases, and supplies the ordering requirement
    in the word *first*.
  - **The marker beginning the statement's own region does not precede it.**
    The ordering rule is about what stands *before* the first-act statement, and
    the statement sits inside a region whose marker line opens it — `FIRST ACT`
    in both modes. Counting that marker as preceding would make the rule
    unsatisfiable by any skeleton this generator emits, and would oblige the
    preamble list to name one marker per mode, a list that then has to be
    maintained against §3.3's two tables. The exclusion is therefore in the rule
    rather than in the list: the marker whose region contains the statement is
    not a preceding marker, so `FIRST ACT` is not a preamble marker and does not
    need to be. The statement is the more general one on purpose — it holds for
    whatever marker a mode gives the first-act region, and for a hand-written
    directive that gives it none.
  - **The preamble-marker list is a tolerance, not a requirement.** It is one
    line of committed text in the invariants document — the document heading and
    `ROUTE AND MODEL` — and it only *widens* what counts as first, admitting two
    markers a bare reading of the Vocabulary would exclude. **One list serves
    both modes.** Now that §3.3's cycle table carries the route-and-model region
    too, the same two markers precede the first-act statement in a cycle
    directive and in a general one, so the route-and-model entry needs no
    per-mode duplicate; and the heading entry is written as *the document
    heading* rather than as any mode's heading text, so §3.3's three heading
    forms — general mode's, and cycle mode's two — need no entry of their own
    either. The list admits directives the bare reading would fail and refuses
    none the bare reading would admit, so it adds no requirement the lint
    enforces, and AC-DT-13's reasoning about the fence exclusion covers it
    unchanged. The lint reads no manifest to check the ordering.
- **M6** — a report section is present and enumerates its required fields.
  - **Match:** a marker line (§3.3) whose token, case-folded, is `report`; and,
    over that region's extent — its marker line to the next marker line — at
    least two lines from which §3.5's stripping removed a list marker.
  - **Extent:** the region the marker begins. **Anchoring:** the marker is
    line-anchored by §3.3's syntax; the enumerated lines are not.
    **Mask:** applies.
  - **Derivation, and a disclosed gap.** Decision Layer rule 14 is one
    sentence — "One self-contained directive per session. The executor needs
    the block and the repository, nothing from this conversation. Write it so
    the returned report is triageable by the next decision session" — and it
    names no section, no fields, and no count. *Presence of a report section*
    is the weakest mechanical reading of *triageable* the rule supports. **The
    enumeration half is not read off governed text at all.** This document
    fixes it, at two list items, because "enumerates its required fields" is
    PRD M6 as agreed and an unenumerated section would satisfy it vacuously.
    It is disclosed here, per element, in the shape G6 licenses for M3's label
    — with the difference stated rather than elided: M3's label is a form the
    governed rule *delegates*, and rule 14 delegates nothing. §4.2's B3 records
    the exposure; OQ-2 records what would close it.
- **M7** — the claim-label instruction is present.
  - **Match:** an extent containing all four class words — `observed`,
    `inferred`, `told`, `unknown`.
  - **Extent:** a statement extent. **Anchoring:** free within the extent.
    **Mask:** applies.
  - **Derivation:** Core rule 6 names exactly those four classes and no others;
    requiring all four and nothing else adds no wording. G10 and AC-DT-11 bind
    the *tools'* own claims to two of the four — a different rule about
    different text, which does not narrow M7.
- **M8** — the resolved repository-relative path matches exactly one of the
  three patterns. Membership is the whole claim; mode-appropriateness is not
  checked and is named in the unchecked set.

M1, M4, M5, M6, and M7 are presence checks whose phrases are compiled by
`invariants.py` from the invariants document rather than held as literals in
the lint's source — the same single-source discipline as the label, applied to
five more strings. That the lint holds no literal is a property of §3.1's
split: one module reads that file, both binaries call it, and the lint's
imports show it.

**AC-DT-02's scan walks the generator's source and nothing else**, as the
criterion states and as §8 restates it. This document does not widen an agreed
criterion, and the single-source discipline over M1 and M4–M7 is not a reason
to: AC-DT-02 is about a manifest's entries and the generator that emits them,
and the lint emits no manifest.

A section that contains a governed rule's trigger phrase is not thereby a
*rendering* of that rule. §3.3's one-rendering claim and its byte-equality test
are at whole-section grain; `§Stop conditions`, `§First act`, `§Report format`
and `§Claim labels` instantiate their rules for one session rather than restate
them, which is the distinction §3.2 draws in rejecting Q1's first candidate.

### 3.7 External dependencies

- **`git`**, as an executable on `PATH`. Used for object resolution only: M1's
  `cat-file`, M2's `cat-file` and `diff-tree`, and the generator's
  `last_commit_sha` and `file_at_rev`. Neither tool performs a network
  operation of any kind.
- **The methodology home**, resolved by `repo.methodology_home`, which is where
  `skills/directive-invariants.md` is read from **and the repository its
  revision is resolved in** (§3.2). The home must therefore be a git repository
  with that document committed in it; where it is not, both tools refuse. This
  is a change in cycle mode's environmental preconditions: `bin/cycle-open`
  today calls `cli.load_root` and never touches the home. §3.9 states what that
  costs the migration.
- **`skills/directive-invariants.md`** itself. Absent, unreadable, or missing a
  named section, the generator refuses (§6). The lint refuses on the same
  condition, because without the label it cannot decide M3 and an undecidable
  element may not yield exit 0 (AC-DT-10).

No `gh`, no remote, no credential, no network, in either tool, in any mode.

### 3.8 Boundaries

- **B1 — `skills/directive-invariants.md` as governed text.** The tools read a
  file whose content is a decision session's and the Context Quality Reviewer's
  to change. An amendment that breaks §3.2's condition 2 breaks G3 for every
  subsequent skeleton.
- **B2 — `git` itself.** The plumbing relied on: `cat-file -e <rev>^{commit}`,
  `diff-tree --root --no-commit-id --name-only -r <rev> -- <path>`,
  `rev-parse`, and, in cycle mode, everything `bin/cycle-open` already uses.
- **B3 — the governed rules M1–M8 derive from.** Core rules 6, 11, 14, 15 and
  its Vocabulary; Decision Layer rule 14; `skills/directive-authoring.md`;
  `decisions/log.md`. A rule that moves or is reworded makes an element check
  match text no governed file states any more, which is a G6 defect that no
  test in this design detects.
- **B4 — the directive corpus the lint governs.** Post-adoption directives are
  written by decision sessions whose composition this design does not control.

Each is declared in §4.2 with its representation and evidence class.

### 3.9 The G0 migration

**What moves.** `render_directive` is deleted. Its literal strings —
`## Decisions`, the commented placeholder with its `Finding: / Resolution: /
Dictated wording:` fields, `## Deferred / out of scope`, `## Execution notes`,
and the heading template — become committed sections of
`skills/directive-invariants.md`. This is forced rather than chosen: AC-DT-02
forbids the generator's source from reproducing any line of an entry's
committed content after whitespace normalization, and none of those strings
falls inside that criterion's separator-character exclusion. **AC-CO-3 is
thereafter satisfied by the invariants document rather than by the generator's
source**, and AC-CO-3's own test is unchanged, because it asserts on the output.

`directive_identity`, `collect_documents`, and `resolve_revisions` move into
`aimeta/directive.py` unchanged in behaviour.

**What stays.** Bundle emission, `--bundle` expansion, the `--out` contract,
`--allow-dirty`, and the not-ignored warning stay exactly as they are, reached
from cycle mode. They are cycle-mode-only; general mode writes no bundle.

**`bin/cycle-open` survives as a forwarding executable** — argv passed through
to the same entry point, no parsing and no skeleton emission of its own.
AC-DT-14 is satisfied on the reading that a forwarder is not a generator: it
emits no skeleton. The alternative — deleting it and rewriting every
`run_cli("cycle-open", ...)` call in `bin/tests/test_cycle_open.py` — was
rejected because AC-DT-15 makes that suite the migration's evidence, and a mass
edit to the evidence is the one edit most likely to weaken it silently.

**Flag collision, resolved.** `--out` means the bundle directory under
AC-CO-12, which fixes it as repo-relative and refuses absolute paths with exit
2. General mode's skeleton destination is therefore **`--write`**, not `--out`.
Reusing `--out` for a second meaning would silently redefine a flag whose
contract an agreed criterion fixes.

**`--write` is a switch, not a path.** It takes no value. Given, the skeleton
and its manifest are written to the one destination the generator computes
below; omitted, both go to stdout and nothing is written anywhere. General mode
has exactly one destination and the author does not name it. That is not a
convenience. PRD §7 accepts, as a named risk, that "a hand-written general-mode
directive named `<slug>-directive.md` passes M8 without a timestamp", and
accepts it on the mitigation that "the generator makes the name correct by
construction" — a mitigation a `--write` taking an arbitrary path would make
false, since the generator could then be driven to emit a skeleton its own lint
fails M8 on, which is the state PRD §4's Conflict rule reserves for surfacing.
AC-DT-12(c)'s "the named output path" is this computed path: the name is the
generator's, which is exactly what the mitigation asserts.

**Mode selection.** Exactly one of `--cycle N`, `--name SLUG` (cycle mode) or
`--descriptor SLUG` (general mode) is required; none or more than one is a
usage error, exit 2 — AC-CO-1's rule extended to a third selector, with
AC-CO-1's own behaviour unchanged whenever one of its two is given.

**The general-mode filename — the timestamp form decided.** General mode writes
to `docs/cycles/<descriptor>-<YYYYMMDDThhmmss>Z.md`: UTC, `Z`-suffixed, from
`datetime.datetime.now(datetime.timezone.utc)`. M8 admits both the suffixed
and unsuffixed forms and stays exactly as agreed; the generator emits one of
the two. The asymmetry is deliberate and costs nothing
under G4, because emitting one admitted form gates no author and refuses
nothing.

The choice is UTC-and-suffixed because
`reviews/directive-authoring-cycle-3.md` F-2 records what the alternative costs:
`skills/directive-authoring.md` fixes neither the zone nor the suffix, 63 of the
109 timestamped files in `docs/cycles/` carry a `Z` and 46 do not, and any future
rule reading a time out of a filename reads the unsuffixed 46 as local time of an
unknown zone. The generator cannot fix the governed sentence — that edit is a
governed skill's and is priced by that review's exposure table — but it can stop
adding to the split, and every name it emits from adoption forward is
unambiguous. What it does not do is retrofit: the no-retrofit non-goal governs
the existing names, and M8's optional group stays because M8 is what the PRD
agreed.

**Fixing that timestamp for tests — a second flag, not `--date`.** `--date`
cannot do this job, and saying it could would leave the general-mode path
undeterminable. AC-CO-10 fixes `--date` as the cycle directive's `Date:` line;
its value is a `YYYY-MM-DD` date with no time component, and its default is
today's **local** date. The general-mode filename carries `hhmmss` and is
**UTC**. Nothing about `--date` determines the time component or the zone, so
the determinism claim does not belong to it. General mode therefore takes
**`--timestamp YYYYMMDDThhmmss`**, which supplies the whole timestamp verbatim,
read as UTC, and is the only thing that determines it when given; the clock is
read only in its absence. It is general-mode-only, and `--date` is
cycle-mode-only: AC-CO-10's contract is untouched — no widening of its grain,
no change to its zone, no new meaning in the mode that already uses it. Giving
`--timestamp` in cycle mode, or `--date` in general mode, is a usage error,
exit 2, on the selector rule above. This is what makes the expected path
writable for AC-DT-12(c)'s tree diff, for FM-G5's existing-destination refusal,
and for any AC-DT-05 or AC-DT-18 assertion that names the emitted file.

**Steps, ordered so a red is attributable to one landing.**

1. Land `skills/directive-invariants.md`: the twelve general-mode sections,
   the cycle-mode sections carrying AC-CO-3's strings, the label section, the
   marker syntax, and the preamble-marker list. No code changes. Nothing
   consumes it. `test_cycle_open.py` untouched and green.
2. Land `aimeta/invariants.py`, `aimeta/directive.py`, `bin/directive` —
   **general mode only** — plus `bin/tests/test_directive.py`. `bin/cycle-open`
   untouched; its suite untouched and green.
3. Add cycle mode to `bin/directive`, wired to the migrated identity,
   document-set, and bundle code, with `bin/cycle-open` still the executable
   the suite drives. Parameterize `test_cycle_open.py`'s `open_cycle` helper
   over the binary name and run all twelve criteria against **both** binaries.
   This step is where AC-DT-15's "whichever binary each is invoked through"
   becomes a fact rather than an intention.
4. Replace `bin/cycle-open`'s body with the forwarder. The suite stays green,
   now driving two names into one implementation.
5. AC-DT-16's gate, which binds the decision session and not the implementer:
   `decisions/log.md` carries an entry superseding DEC-000180 whose tooling
   consequence names `bin/directive`'s cycle mode, and `OPEN-ITEMS.md`'s
   `bin/cycle-open` section names the cycle mode as the bearer of that
   obligation. A release gate reads this as waiting on a decision, not as red.

**The migration's most likely red, named in advance.** Cycle mode gains a
dependency on the methodology home, because that is where the invariants
document is read from **and where its revision is resolved** (§3.2, §3.7).
`bin/tests/helpers.py`'s `make_home` installs a metadata policy, role
documents, and a `bin/` symlink into a plain directory, and nothing else; it
runs no `git init`. Every `test_cycle_open.py` case already passes
`base_env(methodology_home=self.home)`, so the home exists — but the invariants
document does not, and neither does a repository around it to resolve its
revision in. Both gaps are one helper change: `make_home` gains the document
*and* becomes a git repository with that document committed. It lands in step 1
or 2, and if either half is missed every cycle-mode case fails at once — with
an unresolvable-section refusal for the first, and with FM-G1's
no-committed-body refusal for the second. Both are loud failures rather than
subtle ones, which is why it is acceptable to state them here rather than
design around them.

**AC-CO-11 stands unchanged.** Cycle mode now *reads* one more file. Reading is
not writing; the tool still writes only the directive and the bundle directory,
and `snapshot_tree` proves it as it does today.

## 4. Verification boundaries (standing)

### 4.1 Test substrate — decided

**Decision: the existing `bin/tests/helpers.py` substrate — a real repository
from `git init` in a throwaway temp directory (`make_repo`) plus a throwaway
methodology home (`make_home`) — extended with fixture-directive helpers, and
with `make_home` becoming a repository of its own.**

`make_home` today writes files into a plain directory and runs no `git init`,
so the home has no history. §3.2 resolves the invariants document's revision in
the home, so the substrate must give it one: `make_home` runs `git init` and
commits what it installs. This is the substrate's only structural change. The
home and the repository under test stay separately rooted, as every existing
consumer of the two helpers already has them — which is the production
configuration the home mechanism exists for, and therefore the one worth
testing against.

PRD §6 mandates fixture directives, well-formed and each missing one element,
checked against a fixture repository, with no criterion requiring this
repository's commit history. That substrate already exists and already carries
the constraint that makes it worth having: *no mocked git* — every git
interaction in the suite runs against a real repository. Nothing here needs a
remote, so no bare repository and no `file://` transport is added.

**New helpers:**

- `directive_fixture(repo, *, omit=None, name=None, **regions)` — writes a
  directive built from one well-formed base and returns its relpath. `omit`
  names one element and removes exactly that element's text. Building the
  failing fixtures by subtraction from one base, rather than writing eight files
  by hand, is what makes "missing exactly that element" a property of the helper
  instead of a claim about eight files nobody re-reads.

  **Two of the eight substitute rather than subtract, and `omit=` cannot build
  them.** M2's failing fixture cites **a non-touching SHA** in place of the
  touching one, because M2 quantifies over the citations a directive carries:
  removing the companion region leaves zero citations, zero citations satisfy
  the quantifier vacuously, and subtraction would therefore yield a fixture that
  exits 0 on the very element it was built to fail. M8's failing fixture is
  written under **a non-matching name**, because M8 is a property of the
  resolved path and not of the text — there is no line for `omit=` to remove.
  Both substitutions leave the rest of the base intact, so a non-zero exit is
  still attributable to one element; what differs is that the fixture is a
  corrupted base rather than a reduced one, and the helper states which of the
  two each fixture is at its definition.
- `disposition_fixture(repo, shape)` — the seven M3 shapes AC-DT-06 enumerates,
  now instantiable because §3.4 fixes the label.
- `citation_fixtures(repo)` — the four synthetic M2 citations AC-DT-09 needs
  (blob hash, tag, commit touching another path, commit touching the path) and
  AC-DT-17's two passing forms, all made by real commits in the fixture repo.
- `invariants_doc(home, **overrides)` — installs `skills/directive-invariants.md`
  into the methodology home **and commits it there**, with per-section
  overrides so AC-DT-01 can change one section's committed text, commit the
  change in the home, and assert the next skeleton changed. AC-DT-01 is
  asserted in the home because §3.2 resolves the document's revision there; the
  criterion needs a commit to change, so the home must have a history for it to
  change in.

**New test files:**

- `bin/tests/test_directive.py` — AC-DT-01 through AC-DT-05, AC-DT-11's
  generator half, AC-DT-12(a) and (c), AC-DT-18.
- `bin/tests/test_check_directive.py` — AC-DT-06 through AC-DT-11, AC-DT-12(b),
  AC-DT-13, AC-DT-17, AC-DT-19.

**§3.5's mask has no test file of its own.** There is no
`bin/tests/test_mdmask.py`: a unit test that imports `aimeta.mdmask` before the
module exists reds on the import, and an import red says nothing about the
behaviour under test — the same red the red-gate discipline does not buy
anything with. So the mask is asserted **through the lint binary**, in
`TestMarkdownSensitivity` in `bin/tests/test_check_directive.py`, one case per
masking rule §3.5 states, each phrased as a directive the lint must pass
because the labelled statement inside it is masked. Those reds are
behavioural. Whether the implementer later adds a pure-text unit test beside
`mdmask.py`, once the module exists to import, is left open; nothing in this
document depends on one.

**Existing files that change:** `bin/tests/helpers.py` gains `directive` and
`check-directive` in `CLI_NAMES` and `CLI_MINIMAL_ARGS`, so AC-X-1 through
AC-X-7 cover both tools from their first landing; and `make_home` gains both
the invariants document and a git repository around it, committed (§3.9).
`bin/tests/test_cycle_open.py` gains the binary-name parameterization of step 3
and nothing else.

**Both helper changes land with the implementation, not with the tests.**
Adding the two names to `CLI_NAMES` before the binaries exist reddens AC-X-1
through AC-X-7, and turning `make_home` into a repository before a tool reads
the home reddens `test_cycle_open.py` — in both cases a red in the *pre-existing*
suite that says nothing about the new work, which is the one red the red-gate
discipline does not buy anything with. So the test-side form is **additive**:
`make_home_repo` supplies the repository-backed home with the invariants
document committed in it, while `make_home` keeps its present behaviour byte for
byte, and the integration point is asserted instead by one test that stays red
until the implementer folds `make_home_repo` into `make_home` and adds the two
names at migration step 1 or 2 (§3.9). `make_home_repo` is a step in the
migration, not a second substrate: after that landing there is one helper again.

**Criteria that are not tests.** AC-DT-02 and AC-DT-12(a)/(b) are static scans
over source text, in the idiom `test_cross_cutting.py` already uses for AC-X-1
and AC-X-2. AC-DT-15 is the existing suite, run. AC-DT-16 is a release-gate read
of two documents and is discharged by no test at all.

### 4.2 Standing boundaries

**B1 — `skills/directive-invariants.md` as governed text.**
- Production surface: the committed document in this repository, amended by
  decision sessions under the Context Quality Reviewer's gate.
- Currently represented as: a fixture copy written by `invariants_doc`, plus
  one test that reads the real document and asserts §3.2's condition 2.
- Evidence class: **contract-verified** for the parse, **live-verified** for
  condition 2, which is asserted against the real file.
- Does not prove: that a future amendment keeps every section's prose fit for
  the register a directive needs, which is a judgment no test makes.
- Deferred-verification path: none needed for condition 2. For fitness, the
  document's own review gate.

**B2 — `git`.**
- Production surface: whatever `git` the session has.
- Currently represented as: live, incidentally — every test runs against the
  one `git` present.
- Evidence class: **live-verified, incidentally.**
- Does not prove: behaviour on another version. No minimum version is asserted;
  the plumbing used is long-stable and is a subset of what the existing eight
  tools already depend on.

**B3 — the governed rules M1–M8 derive from.**
- Production surface: Core, the Decision Layer, `skills/directive-authoring.md`,
  `decisions/log.md`, as committed.
- Currently represented as: **not represented**, except for the one bullet
  §3.3's byte-equality test pins.
- Evidence class: **assumed.** This is the weakest point in the design, and it
  is the one AC-DT-13 asserts by reading rather than by running: nothing detects
  a governed rule being reworded out from under an element check.
- Does not prove: that M4's, M5's, M6's, or M7's matched phrases still
  correspond to what Core and the Decision Layer say.
- Deferred-verification path: extend §3.3's byte-equality pattern to the other
  sources, one governed quotation per element. Recorded as OQ-2, because doing
  so for five more rules is a cost the PRD did not price.

**B4 — the post-adoption directive corpus.**
- Production surface: directives written by decision sessions after adoption.
- Currently represented as: fixture directives this design authors, which are
  written by the same hand that writes the matcher.
- Evidence class: **assumed.** A fixture suite proves the lint decides the
  shapes its author imagined.
- Does not prove: that real directives take those shapes. §3.5's mask is the
  part most exposed, which is why §3.1 isolates it.
- Deferred-verification path: run the lint over the existing 144-file
  `docs/cycles/` corpus as a **read-only survey**, not as a gate — the
  no-retrofit non-goal means its failures are not defects — and read the failure
  distribution as evidence about the matcher. Recorded as OQ-3.

## 5. Data and state

Neither tool has persistent state. No configuration file, no cache, no log
file, no lock.

**Inputs.**

- The generator: argv; `skills/directive-invariants.md` at its last commit in
  the methodology home (§3.2); for cycle mode, the document set and each
  document's last-touching commit in the invocation root; the clock, for the
  general-mode timestamp, unless `--timestamp` fixes it, and for cycle mode's
  `Date:` line, unless `--date` fixes it.
- The lint: argv; the directive file's bytes as they stand on disk;
  `skills/directive-invariants.md`; the local object store for M1 and M2.

**Outputs.**

- The generator, general mode: the skeleton with its manifest, to stdout, or —
  when `--write` is given — to the single `docs/cycles/` destination the
  generator computes (§3.9). Nothing else is written, and `--write` names no
  path.
- The generator, cycle mode: the directive file and the bundle directory,
  exactly as AC-CO-1, AC-CO-7, and AC-CO-11 fix them.
- The lint: a report on stdout on both exit paths; diagnostics on stderr;
  nothing on the filesystem, ever.

**The report's shape.** The lint's stdout carries, in order: the checked set —
one line per element M1–M8 with its result; the per-failure cause and the
governed text that requirement derives from (G8); and the unchecked set,
carrying at minimum executability of the working-tree disposition, route and
model tier, every judgment-only rule PRD §4 lists, and mode-appropriateness of
the filename (AC-DT-08). Every claim in it is labelled *observed* or *unknown*
and no other class (G10, AC-DT-11).

**The manifest is the generator's only persistent artifact of itself**, and it
persists inside the landed directive. It is what makes PRD §5's first outcome
signal computable from the file alone, and it is an input to nothing.

**Authority.** The invariants document is authoritative for every region's
text, for the label, for the marker syntax, for the preamble-marker list, and
for §3.6's match phrases. No copy of any of them exists in code.

## 6. Failure modes and recovery

**There is no recovery inside either tool.** Neither retries, repairs, edits,
or infers. The lint never edits the directive it inspects and neither does the
executor (PRD non-goals). Every failure is handed to the invoking session,
which stops and surfaces; a lint failure returns the directive to the decision
session, the only place a missing element can be supplied.

Diagnostic codes are §7's to assign; no cell below names one.

**AC-DT-04's author-text clause is satisfied by construction, and no cell below
can name it.** The criterion requires that in both modes no text an author
places in the task-specific region causes a non-zero exit, including text the
lint would fail. The generator never sees such text. §5 enumerates its inputs —
argv, the invariants document at its last commit in the methodology home, cycle
mode's document set and each document's last-touching commit, and the clock —
and none of them is directive prose: the task-specific region is emitted as an
empty author slot, and it is filled after the generator has exited. There is
consequently no exit path for author text to reach, and the clause is discharged
by the input set rather than by a check, which is why it appears in no row of
either table below. What is enforceable in the clause lives on the other tool:
the lint is the one that reads author text, and its posture under G4 is that it
decides M1–M8 and refuses nothing else about content — no element is added for
what an author wrote in a region, and the unchecked set says so on every pass
(AC-DT-08).

**The generator.**

| # | Failure mode | Detected by | Effect |
| --- | --- | --- | --- |
| FM-G1 | The invariants document is absent or unreadable, or the methodology home carries no committed revision of it — the home is not a git repository, or the document is untracked there | Read of the methodology home; `last_commit_sha` against the home (§3.2) | Refusal before anything is written. There is no working-tree fallback: a section whose committed body cannot be read is a section that is not there |
| FM-G2 | A named section is missing from it | Section parse | Refusal before anything is written |
| FM-G3 | The invariants document has uncommitted modifications | `git status --porcelain` on it | Refusal, or a `WARN` under `--allow-dirty` — AC-CO-5's shape, applied to a second input |
| FM-G4 | A region body carries a placeholder the generator does not recognise | Substitution pass | Refusal; never a silent pass-through |
| FM-G5 | The destination file already exists | Existence check, before any write | Refusal. AC-CO-2 in cycle mode; in general mode this is a precondition refusal, and §9's OQ-4 records that G4's "in general mode it refuses nothing" admits a stricter reading |
| FM-G6 | Cycle mode's existing five refusals | Unchanged | AC-CO-1, -2, -5, -6, -12, unchanged in cause and exit status |
| FM-G7 | Two markers collide, or the emitted skeleton carries more or fewer than one unfenced labelled statement | Self-check before emission | Refusal. §3.2's three conditions make this unreachable in principle; the check exists because G3 is the invariant the whole design rests on, and a silent violation of it would defeat J2 |

FM-G7 is the one refusal that is not a precondition and not content: it is the
tool refusing to emit output it can see is malformed. It refuses rather than
warns because a skeleton that fails the lint is worse than no skeleton — the
author would fill it, hand it over, and the executor would stop.

**The lint.**

| # | Failure mode | Detected by | Effect |
| --- | --- | --- | --- |
| FM-L1 | The path resolves outside the repository, or does not exist | Path resolution (AC-DT-19) | Refused invocation; names no element |
| FM-L2 | Not inside a git repository | `cli.load_root` (AC-X-4) | Refused invocation |
| FM-L3 | The invariants document is absent, unreadable, or missing the label section | Section parse | Refused invocation. The lint cannot decide M3 without the label, and AC-DT-10 forbids exit 0 for an element it cannot decide |
| FM-L4 | One or more of M1–M8 fails | The element set | Non-zero, naming each element and the governed text it derives from |
| FM-L5 | An element cannot be decided: a git read fails for a reason the lint cannot attribute to the directive — an unreadable object store, a damaged repository, `git` returning no answer about the object (§3.6 step 5) | The element set | Reported **unknown** against that element, exit 1 (AC-DT-10). Distinct from a citation finding, which is a claim about text the directive carries |
| FM-L6 | The file is not valid UTF-8 | Decode | Refused invocation. Not an element finding: the lint cannot read the text every element is about |
| FM-L7 | The invariants document has uncommitted modifications | `git status --porcelain` on that document, in the methodology home | Refused invocation — FM-G3's analogue on the lint's side (§3.6 step 4). There is no `--allow-dirty` to downgrade it. Applied after FM-L3, so an absent document is still FM-L3 |

**What no failure mode of either tool includes:** a write to a remote, a
staged change, a commit, a modification to a file the invocation did not
create, or any filesystem write at all from the lint (AC-DT-12).

## 7. Operational concerns

**Release model.** Deploy and release are the same event: a landing on `main`
makes a tool available to the next session that runs it. There is no flag
backend and no separate release decision, because there is no deployed surface
to gate. The one gate that exists is AC-DT-16's, and it gates the *migration*,
not a release: the cycle mode does not land until the decision session has
recorded the superseding decision and the OPEN-ITEMS obligation. Adoption of
the generator ahead of the lint, or the reverse, is an accepted risk the PRD
already names, and needs no mechanism.

**Observability.** stdout carries the report (the lint) or the skeleton and
manifest (the generator, general mode) and nothing else. stderr carries
human-readable diagnostics, each with a stable bracketed code — the convention
`bin/tests/helpers.py` already relies on, where tests assert on codes and never
on English wording. Exit status is the third channel. There is no log file and
no telemetry sink.

**Exit statuses.** Within Q6's bounds and under §9's OQ-6 recommendation, the
existing five-code contract is reused with no new code and no advisory tier:

| Code | The lint | The generator |
| --- | --- | --- |
| 0 | Every checked element passed; the report states the unchecked set | A skeleton was produced |
| 1 | At least one element failed or is unknown | Cycle mode's AC-CO-6 refusal, unchanged |
| 2 | Refused invocation: no argument, a path outside the repository, a path that does not exist, not in a repository, undecodable file, an invariants document that is absent, missing a named section, or uncommitted (FM-L7) | Usage: the selector rule, a flag given in the mode it does not belong to (`--timestamp` in cycle mode, `--date` in general mode), AC-CO-12's absolute `--out` |
| 3 | Unused | Precondition: FM-G1 through FM-G5, FM-G7; AC-CO-2 and AC-CO-5 unchanged |
| 4 | Unused | Unused |

Refusals are distinguished from element findings by status — 2 against 1 —
which is the sub-question AC-DT-19 leaves to Q6, answered here in the
recommended direction and restated in OQ-6.

**Diagnostic codes.** Each matches the form `bin/tests/helpers.py` already
pins: a lowercase letter, then lowercase alphanumerics and hyphens, in square
brackets. One code per situation a session must answer differently.

| Code | Situation | Tool |
| --- | --- | --- |
| `reviewed-ref-missing` | No reviewed-ref pin (M1) | lint |
| `reviewed-ref-unresolvable` | The pin does not resolve to a commit (M1) | lint |
| `citation-unresolvable` | A companion SHA resolves to no commit (M2) | lint |
| `citation-path-absent` | The cited path is not in that commit's tree (M2) | lint |
| `citation-not-touching` | The commit does not touch the cited path (M2) | lint |
| `disposition-absent` | Zero labelled statements (M3) | lint |
| `disposition-multiple` | More than one (M3) | lint |
| `disposition-form-absent` | One statement, neither admitted form (M3) | lint |
| `disposition-form-ambiguous` | One statement, both forms (M3) | lint |
| `stop-condition-missing` | A stop condition is absent (M4) | lint |
| `first-act-missing` | Absent, or preceded by a non-preamble marker (M5) | lint |
| `report-section-missing` | No report section, or no field list (M6) | lint |
| `claim-labels-missing` | No claim-label instruction (M7) | lint |
| `filename-unmatched` | The resolved path matches no pattern (M8) | lint |
| `element-unknown` | An element could not be decided | lint |
| `path-outside-repo` | AC-DT-19's refusal | lint |
| `path-absent` | The named file does not exist | lint |
| `invariants-missing` | The invariants document is absent or unreadable | both |
| `invariants-section-missing` | A named section is absent | both |
| `invariants-dirty` | Uncommitted modifications to the invariants document (FM-G3, FM-L7) | both |
| `invariants-placeholder-unknown` | An unrecognised placeholder (FM-G4) | generator |
| `directive-exists` | The destination already exists (FM-G5) | generator |
| `skeleton-self-check-failed` | FM-G7 | generator |
| `out-not-relative` | AC-CO-12, unchanged | generator |
| `dirty-document` | AC-CO-5's `WARN`, unchanged | generator |
| `bundle-not-ignored` | AC-CO-8's `WARN`, unchanged | generator |

**Configuration and secrets.** None. Neither tool reads an environment
variable of its own beyond `AI_METHODOLOGY_HOME`, which the existing tools
already read, and neither reads, writes, logs, or passes a credential.

**Quotas and billing.** None. No network operation of any kind.

## 8. Constraints, NFRs, and non-goals

The technical instantiation of PRD §4's non-functional goals.

**Performance.** No latency target. The concrete constraint is negative and
enforceable: **zero network operations** in either tool, in either mode. Git is
invoked only against the local object store. Enforced by the same static scan
AC-DT-12(a) uses for `gh` and the remote, extended to `fetch`, `push`, and
`ls-remote`.

**Reliability.** A non-zero exit is a claim that a checked element is missing or
undecidable; exit 0 is a claim about the checked set and nothing wider, and it
says so in its own output (G9). Neither is a claim about directive quality. No
retry, no fallback, no backoff — deliberately.

**Scalability.** N/A. One directive per invocation. The only dimension that
grows is the number of companion citations, costing two git reads each.

**Security.** No authentication, no credential path, no remote. The threat
surface is the argv each tool constructs: a path or a SHA read out of a
directive is caller-supplied text, so every git invocation passes arguments as
an argv list through `repo.run`'s `subprocess.run` with no shell, and pathspecs
are always separated by `--`. A SHA read from a directive is passed to
`cat-file` and `diff-tree` as a single argv element and never interpolated into
a revision expression built by string concatenation. The lint writes nothing, so
it cannot damage the tree it inspects (AC-DT-12(b)) — verifiable statically.

**Maintainability.** G1, G6, and G0. A governed rule that changes changes the
tools' behaviour with no code edit, because the text lives in a committed file
and the code holds none of it. The strongest expression of this is AC-DT-02,
which fails if any line of committed region content appears as a string literal
in the generator's source. §4.2's B3 states where this property does *not*
reach.

**Usability.** The reader of both outputs is an agent. The lint's failure output
is actionable without reading the tool's source, because each finding names the
element, the cause, and the governed text the requirement derives from. The
generator's success condition is that the author writes two regions and no
more.

**Observability.** As §7. Instrumented: nothing. What surfaces: stdout, the
bracketed diagnostics, the exit code, and the manifest inside the landed file.

**Portability / Compatibility.** Python 3 standard library and `git`. Cycle
mode's output must remain acceptable to the reviewer-gated cycle format under
DEC-000180's route/model/no-track rule; AC-DT-14 asserts it carries Route and
Model and no Track.

**Compliance.** N/A.

### Technical non-goals

- **No network operation**, of any kind, in either tool.
- **No `gh` invocation**, for anything.
- **No write from the lint**, of any kind.
- **No repair.** Neither tool edits a directive.
- **No judgment claim.** No element decides a property from PRD §4's
  judgment-only set, and the unchecked set names each one on every pass.
- **No second definition of the label**, the marker syntax, or any invariant
  region's text, anywhere in code.
- **No retrofitting.** The lint is never run as a gate over the pre-adoption
  corpus; OQ-3's survey is read-only.
- **No shell.** Every subprocess is an argv list.
- **No markdown parser.** §3.5's mask is a line scanner, not a parser, and
  nothing in either tool builds a document tree.

### Required integration points

- `bin/tests/helpers.py`: `directive` and `check-directive` in `CLI_NAMES` and
  `CLI_MINIMAL_ARGS`; the invariants document in `make_home`; the fixture
  helpers of §4.1.
- `bin/tests/test_cycle_open.py`: the binary-name parameterization of §3.9
  step 3.
- `skills/directive-invariants.md`: new, and the migration's first landing.
- `bin/tests/test_directive.py`, `bin/tests/test_check_directive.py`: new.
  §3.5's mask is covered inside the second of these, in
  `TestMarkdownSensitivity`, driven through the lint binary; there is no
  `test_mdmask.py`, because a unit test over a module that does not yet exist
  reds on its import rather than on the behaviour (§4.1).

## 9. Open technical questions

Three of these are the PRD's Q2, Q4, and Q6, carried here with options,
tradeoffs, and a recommendation, and **not decided**. Each names what it would
cost to rule either way, and which section of this document, if any, cannot
stand under a given ruling.

- **OQ-Q2 — Lint sequencing on the failing path.** G5 and J2 already fix the
  passing path: write the directive file, lint it, commit, push. What is open
  is only what happens on a failure.
  - **(a) Nothing lands.** The executor writes the file, the lint fails, the
    session stops with nothing committed. A malformed directive is never
    citable by SHA and never enters the history.
  - **(b) The directive lands, the work does not.** The executor writes,
    lints, commits, and pushes as it would have, then stops before any other
    work, its report carrying the lint output.
  - Tradeoff: (a) keeps a malformed directive out of the history, at the cost
    that the only record of what was handed over is the decision session's
    chat — which Core rule 4 rules out as a sole record. (b) preserves the
    record, at the cost that a malformed directive is citable by SHA and may be
    cited later as if valid.
  - Surfaced by the design: **nothing in this document depends on the answer.**
    The lint takes a path on disk, writes nothing, and cannot tell whether a
    commit has happened; AC-DT-19 states as much. Q2 is a directive-authoring
    question, not a tool-design one, and every section here stands either way.
  - **Recommendation: (b)**, because M1 and M2 cite by SHA, and a directive
    that never lands cannot be cited by the retro that dispositions it.
- **OQ-Q4 — Whether these tools' requirements move into
  `skills/directive-authoring.md` or sit beneath it.**
  - **(a) Move them in.** One document the author reads.
  - **(b) Leave them in the PRD and this document**, with the skill unchanged.
  - **(c) The invariants document is the home**, and the skill's delegation
    sentence gains a path pointer to it.
  - Tradeoff: (a) puts mechanism into a document whose audience is an author,
    and grows a governed skill with matter that changes when tooling changes.
    (b) leaves the skill's delegation of the label's form pointing at nothing,
    which is exactly F-3's finding. (c) costs one edit to the skill's first
    bullet.
  - Surfaced by the design: (c) already exists as a side effect of Q1's
    decision — the invariants document is where the label and the region text
    live regardless. So (c) is the cheapest of the three, and it is the fix
    `reviews/directive-authoring-cycle-3.md` F-3 proposes in its second form:
    state the delegation's holder by path. Its cost is priced by that review's
    downstream-exposure table: the edit touches the bullet
    `specs/directive-tooling.md`'s M3 cell quotes whole, so it costs a
    directive-tooling cycle.
  - **Recommendation: (c).**
  - Sections that cannot stand under a ruling: under (a), §3.3's source table
    changes which path each region names. The mechanism — read a named section
    from a governed file — is unchanged, so only that column moves.
- **OQ-Q6 — One exit status, or a blocking/advisory split.**
  - **(a) One non-zero status.** Every finding, every unknown, and AC-DT-19's
    refusal exit 1. The session's rule is "non-zero, stop".
  - **(b) Reuse the existing five-code contract.** Findings and unknowns exit 1;
    refused invocations exit 2. No advisory tier. This is what §7 is written to.
  - **(c) A blocking/advisory split.** Some elements — a malformed companion
    citation, say — warn at exit 0 while others fail.
  - Tradeoff: (a) is simplest and loses the distinction between "this directive
    is missing something" and "you invoked me wrongly", which are different
    messages to different readers. (b) costs nothing, reuses the meanings the
    other eight tools already carry, and answers AC-DT-19's sub-question. (c)
    is the only one that addresses Q6's actual observation — that a malformed
    citation and a missing stop condition are not obviously the same severity —
    but an advisory exit 0 is a pass that does not state its own bounds, which
    PRD §7 puts under "Not accepted", and it moves a judgment PRD §7 reserves
    to Dave into the tool.
  - **Recommendation: (b).**
  - Sections that cannot stand under a ruling: under (a), §7's exit table
    collapses to two rows and nothing else moves. **Under (c), §7's exit table
    and code table both need an advisory column, and AC-DT-10 needs amending**,
    since it currently forbids exit 0 for any undecidable element.

The remaining questions are this document's own.

- **OQ-1 — No SLO exists for J1, J2, or J3.** §2 states this and gives the
  structural reason. *Resolved by*: Dave deciding whether any post-adoption
  signal about either tool is wanted beyond PRD §5's two corpus counts, and
  where it would be recorded.
- **OQ-2 — Whether the governed sources behind M4–M7 should be pinned by
  quotation.** §3.3 pins one bullet by byte-equality; §4.2's B3 records that
  the other five rules are pinned by nothing, so a rewording makes an element
  match text no governed file states any more, undetected. *Resolved by*: a
  decision on whether five more by-value quotations are worth the cost the
  downstream-exposure table prices, or whether B3 stays an assumed boundary.
- **OQ-3 — Whether to survey the pre-adoption corpus.** Running the lint over
  the 144 existing `docs/cycles/` files as a read-only survey would say a great
  deal about §3.5's mask against text nobody wrote for it. It is not a gate —
  the no-retrofit non-goal makes its failures non-defects. *Resolved by*: a
  decision that the survey is worth running and that its output is read as
  evidence about the matcher rather than about the corpus.
- **OQ-4 — Whether general mode may refuse an existing destination.** G4 says
  the general mode "refuses nothing", and also that what it does not refuse is
  "the content an author writes". §3.9 reads the first clause as bounded by the
  second and has general mode refuse an existing computed destination (FM-G5),
  the same precondition AC-CO-2 states for cycle mode. The alternative is
  silent overwrite, which no reading of the PRD asks for. *Resolved by*: a
  reading of G4 at the next gate.
- **OQ-5 — Whether cycle mode's added regions exceed what the PRD licenses.**
  PRD §4 says the cycle-mode skeleton carries AC-CO-3's structure "plus the
  disposition slot and the source manifest". §3.3 has cycle mode carry the
  first-act, base-verification, sandbox, verification, stop-conditions, report,
  and claim-label regions as well. It must: without them a generated cycle
  directive fails M4, M5, M6, and M7 — the lint failing the generator's own
  output, which is precisely the state PRD §4's Conflict rule names as a defect
  in the PRD, to be surfaced rather than resolved by the implementer. This
  document designs to the reading that the PRD's two-item list is illustrative
  of the license rather than a cap on the region set. The route-and-model region
  is added on a different ground and is not part of this question: AC-DT-14
  requires the cycle skeleton to carry Route and Model, so an agreed criterion
  licenses it directly. *Resolved by*: a dictated disposition in the PRD's text
  stating which of the two moved and why, per the Conflict rule.
- **OQ-6 — Q6's answer determines §7.** Recorded above as OQ-Q6; noted here so
  §7's tables have a single pointer.
- **OQ-7 — Whether the sole-tree form's canonical sentence is this document's
  to fix.** §3.4 makes M3's sole-tree branch a literal match against a sentence
  the invariants document fixes, because zero instances exist to generalise
  from. That sentence is text an author must write verbatim, which is a
  stronger constraint than the governed rule states. *Resolved by*: Dave, or
  the next gate, ruling whether a literal is acceptable or whether the branch
  should match a pattern — and if a pattern, against what evidence, given that
  the corpus supplies none.
- **OQ-8 — F-3's residue in `skills/directive-authoring.md`.** This document
  discharges the delegation: the label has a form, and the sole-tree form has a
  worked example. The skill's own sentence still delegates to tooling without
  naming where. That edit is OQ-Q4(c). *Resolved by*: OQ-Q4's ruling.
- **OQ-9 — The reading of M3's "no region extent".** §3.4 reads it as *the
  statement need not sit in any particular region*, not as *the statement has
  no textual extent*. Under the second reading, form-membership is undecidable
  and AC-DT-06's fixture (v) cannot be instantiated. *Resolved by*: a reading at
  the next gate, or a clarifying amendment to M3.
- **OQ-10 — F-1's residue.** `skills/directive-authoring.md`'s Naming section
  admits one of the two cycle-mode filenames AC-CO-1 licenses, so an author
  running the tested `--name SLUG` path gets a filename the governing document
  does not admit. M8 is unaffected — its patterns 2 and 3 anchor on AC-CO-1
  directly — and so is the generator, which preserves both branches. The defect
  is in a governed skill and its fix is an edit this document cannot make.
  *Resolved by*: Dave's disposition of that finding, at the cost its review's
  exposure table prices.
