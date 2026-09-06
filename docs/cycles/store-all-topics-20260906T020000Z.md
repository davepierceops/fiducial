# Store: write rules/ for every remaining topic under the pilot rulings

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to docs/cycles/store-all-topics-20260906T020000Z.md in
that worktree, commit it alone with a message naming the package it opens
(`store: all topics — directive`), push the branch store-all to origin with a
plain `git push origin store-all`, never with `-u`, and report the SHA. Do
this before reading anything else and before touching any other file. Base
verification below runs before this act.

FENCE NOTE: the author-written regions (TASK, VERIFICATION) fence with tildes
so they survive transport inside a paste block; the generator's regions keep
their backtick fences and the paste block carrying this directive is opened
with four backticks for that reason. Treat a tilde fence exactly as a backtick
fence.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-store-all", created by:
git worktree add --no-track "$TMPDIR/fiducial-store-all" -b store-all origin/main

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a184967413681950a2e8ffa2ab3e16be552f7158. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- Every in-scope source file, read from the base ref fd54448
  (`git show fd54448:<path>`), as each topic is reached; each row's `source`
  points at that text. Never main's copy.
- docs/rule-register/rule-register-20260904T210000Z.md @ 45b02c7b88a0e08f4872713aa39f840a59117423
  — per topic, the rows whose source column is that file; read the whole
  file once if you must, but write one topic at a time
- docs/rule-register/rule-clusters-20260904T223000Z.md @ acdfef73fc04bed73d6f854b3f66fe8df5411519
  — whole: method notes, all 15 divergent clusters, agreeing clusters,
  intra-file clusters, per-file view, singletons
- docs/rule-register/topic-digest-20260905T181500Z.md @ 0bd149ce85f8519e2e9d681d3827b74bef237f43
  — whole: 54 cards and the closing questions
- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — whole; cite
  DEC ids in `## Human` where a ruling settled a row
- process/change-flow.md @ 81310de105b0f0b4133117fa4c209baea9d84b09 — the
  agreed change-flow document; its closing section "What this document
  changes or retires" governs the spec-review-cycle, spec-reviewer,
  test-designer, and operating-model topics
- docs/cycles/store-pilot-core-20260906T003000Z.md and
  docs/cycles/store-decision-layer-20260906T010000Z.md, on branches
  store-pilot-core and store-decision-layer respectively (fetch the branches
  read-only; do not check them out into your worktree) — the two prior
  directives, superseded by this one where they differ; and those branches'
  rules/ trees, which you are rewriting, not reusing

TASK

Write the whole store: every topic that survives Dave's rulings, as rows under
rules/, on one branch, one commit per topic, in the order below. This
directive is the rulebook; it supersedes the pilot's and decision-layer's
where they differ. You may run one sub-agent per topic; the parent session
owns the branch, commits in order, keeps the counts, and writes the report.
Where a rule is under-specified, decide, and record the decision under
"Decisions taken" in the report, grouped by topic.

CORE AND DECISION-LAYER ARE REWRITTEN FIRST, from scratch, on this branch —
not copied from their branches. Dave reviewed both row by row; his rulings are
listed under RULINGS BY ROW below and are applied exactly.

WHAT A ROW IS. One file per rule under rules/, filename `<id>.md`. YAML
frontmatter between `---` lines, then the instruction as the body, then an
optional `## Human` section. Keys in this order:

~~~text
id: R0196
topic: [core]
order: 140
role: [all]
session: [decision, execution]
corpus: [software, writing, methodology]
verb: require
condition: null
source: docs/global-context/core.md:33 @ fd54448
term: null
~~~

- `id`: the register id of the row (the lowest where rows merge). A split
  takes the register id with a letter suffix (`R0248a`, `R0248b`). Never a
  new number, never reused.
- `topic`: one value per row, the topic name from the TOPIC MAP below.
- `order`: by 10 in source order within the topic; a merged topic continues
  numbering across its source files in the order the map lists them.
- `role`: the audience the source file's frontmatter at fd54448 declares,
  resolved: `all-roles` → `[all]`; `all-decision-roles` → every role
  document under roles/ at fd54448 whose frontmatter says `session:
  decision`, by basename slug; a named list → that list. A role document's
  own rows carry its own slug. Narrow a row where it plainly binds fewer
  roles; say so.
- `session`: `[decision]`, `[execution]`, or both, from the file's own
  statement of which session kind it governs, narrowed per row where a row
  plainly binds one side (the reader of a report, not its writer).
- `corpus`: `[software, writing, methodology]` unless the file is one corpus's
  (public-prose-criteria, voice, the writer/copy-editor/critic/outline files
  are `[writing]`; spec templates, testing, production-grade, boundary and
  release policies are `[software]`; the rest carry all three).
- `verb`: the register's.
- `condition`: the trigger in plain words, for querying; never the only place
  the trigger lives.
- `source`: exactly as the example — path, colon, line number at fd54448, the
  ref. Verify each line by reading the ref.
- `term`: for `verb: define` rows, the word or phrase defined, every surface
  form; `null` where a define row states a proposition rather than a term.

The body: one obligation, imperative, complete with the frontmatter covered —
the rule at its shortest, not the source sentence and not a concatenation of
merged rows. A define row's body is the definition. `## Human` only where
the source prose gives a reason; cite the DEC id where a ruling settled the
row.

GENERAL RULINGS, in force for every topic:

1. Two register rows are one store row only when they state the same
   obligation and would carry the same keys. A key difference — topic,
   role, session, corpus, condition, term — splits a cluster. Cross-file
   cluster-mates are never merged across topics; no `also` key.
2. A rule stated then restated is one row: rule plus negation, rule plus
   named instance, rule plus per-audience elaboration, rule plus
   cross-reference to another rule. Write the positive form at its shortest.
   Where an elaboration is a distinct obligation with a distinct trigger or
   audience, it is its own row.
3. Different triggers are different rows, even on one source line.
4. Container rules retire: any row about loading, ordering, or the
   precedence of documents, or a disclaimer about what the file does or does
   not authorize. Restate the latter as an instruction where an obligation
   is underneath (core's production-system line becomes a `require`).
5. A `forbid` whose only content is the negation of an adjacent `require`
   is not written. A ban that names the banned word is rewritten positive
   without the word where the positive form says the same thing.
6. The body states its own trigger. A row whose body cannot be read without
   its `condition` key is a defect.
7. A row that binds one side of a flow is re-keyed, not retired.
8. Merges produce the rule, not the sum of the rows. If the merged body is
   longer than the longest source row, it is wrong.
9. Retire under DEC-000380: every row whose only obligation is the
   document-lifecycle machinery — status, last-reviewed, the agreement flip,
   per-document review cycles and their artifacts, the expedited and doc-only
   paths, the in-scope set, the pre-commit hook, and the tools
   check-frontmatter, flip-agreed, install-hooks, migrate-frontmatter,
   reviews/expedited-log.md. The digest's header lists 124 rows; retire by
   substance, not by word, and name each in the topic's map. A row stating
   an obligation that survives the machinery is restated in open/closed
   vocabulary per process/change-flow.md's closing section.
10. Compound rows R0018, R1486, R1483 (named by the clusters artifact) are
    split, letter-suffixed, consecutive orders. Any other row stating two
    obligations likewise.
11. Definitions are rows, `term` set (DEC pending, ruled 2026-09-05).
12. Engagement material is not written (ruled 2026-09-05): every file under
    engagements/ — cards 29, 31, 32, 33, 41, 42, 43, 44, 46, 49, 53 — is
    skipped whole. Rows from other files that cluster with engagement rows
    are written by their own topics as usual. The four verification-vocabulary
    rows in working-with-dave.md survive through their cluster-mates in
    testing-and-verification.

DIVERGENT CLUSTERS, Dave's rulings (write the row as ruled, cite the source
of the ruling in `## Human`):

- C002, C004 — retire by DEC-000380; scope statements become the `session`
  key, not rows.
- C017, C024 — one row stating DEC-000360's three values in open/closed
  vocabulary per process/change-flow.md; R0694 yields.
- C025 — one row: every known, unresolved boundary gap carries one of the
  four labels; `not-material` is a valid label, not an exemption.
- C019 — DEC-000290, strictest form.
- C097 — two rows, positive: "A Test Designer edits tests and nothing else; a
  spec change it needs is a finding to the decision session" (role
  test-designer); "A spec writer edits specs and nothing else; a test change
  it needs is a finding to the decision session" (role architect and any
  session under a spec-editing directive).
- C153 — cut: neither the Copy Editor's "report the readability conflict" row
  nor the Criteria's "readability wins over discoverability" row is written.
- C125 — one row from operating-model's seven-item control-surfaces list;
  the line-18 thesis row ("primary control is evidence, not line-by-line
  review") is not written.
- C206 — one row with the TRD template §4's four fields; §3's row becomes a
  pointer to it.
- C046 — three rows under command-blocks: expected output one line below;
  that line observed in the target environment or qualitative; blast radius
  above where destructive.
- C020 — two rows: Depth 1 continuity scan at a spec delta's close
  (process/change-flow.md amended R1104/R1135); wider depths by the delta's
  reach; Depth 3's scope conformed to "the rules store".
- C121, C119, C175 — moot or resolved by the rulings above; write the
  operating-model rows as they stand.

TOPIC MAP (ruled 2026-09-05; 17 of the digest's 18 proposals accepted;
engagement merges moot). Topics not listed keep the digest's proposed name.
- document-metadata-policy → topic `spec-gating` (its 34 surviving rows).
- spec-review-cycle → split into `convergence` and `reconciliation`, per the
  change-flow document's open/closed vocabulary.
- commit-and-change-control → split into `commit-control` and
  `change-control`; project-setup-requirements → into `commit-control`;
  release-readiness → into `change-control`.
- review-artifact → `review-artifact-schema` (and its verdict rule amended
  per change-flow: one overall `Verdict:`, one per pass, most severe wins).
- review-rubric → `context-quality-criteria`.
- directive-authoring → into `directive-invariants`.
- test-plan-review → into `test-designer`.
- evidence-review → into `skeptic`.
- boundary-audit → into `verification-boundaries`.
- production-grade-software → into `verification` (with
  testing-and-verification).
- architect-agent → into `trd` (with trd-template).
- reviewer-agent → keep as `reviewer`, rows in force until an adopted
  code-review standard replaces them (change-flow).
- Every other file: topic = its basename without extension.

RULINGS BY ROW — core (all keys: topic core, role all, both sessions, all
corpora):
- R0162, R0163 retired (container rules).
- R0164 stays. R0203 rewritten positive as a `require` at order 20:
  "Treat every deployed or production system as off limits. Act against one
  only where a policy in your bundle authorizes the action and names the
  gate it passes through." `## Human` keeps core's reason.
- R0166+R0167 → one row: "Propose; do not decide. Agreement, release,
  prioritization, and publication are Dave's." Cluster-mates (operating
  model's ownership list, decision-log's no-who-field) go to their topics.
- R0168+R0169 → one row, core's sentence.
- R0170+R0171 → one row: "Anything that must survive the session exists as
  an artifact — a committed file, a log entry, a tracker entry — before the
  session ends; chat is never the sole record of a decision."
- R0173+R0189: two define rows (different terms). R0175 re-keyed
  `session: [decision]`. R0176 stays.
- R0183+R0184+R0185 → one row: "When two sources disagree, surface it — name
  both and the contradiction — and leave the resolution to Dave; do not pick
  the newer one, the easier one, or reconcile silently. If one source is
  canonical and the other derived from it, stop work on that item until it is
  resolved."
- R0188 stands alone, trigger in body, `session: [execution]`. R0199 core's
  own sentence, `session: [execution]`.
- R0193 (+R0194, R0195) → one row: "A changed fact changes everywhere it
  appears. When you change a value, name, count, or reference, find every
  other place that states it; update the ones you are permitted to edit and
  name the ones you are not."
- R0198 not written (negation of R0196).
- R0200+R0201+R0204 → one define row, `term: [decision session]`. R0202
  stays (execution session).
- R0205+R0206 → one define row, `term: [decision layer, execution layer,
  shell layer]`. R0207 → "Call an artifact by its defined name — directive,
  baton, command block, review artifact — never by a generic word."
- R0208–R0222 → three define rows: (1) paste block / command block /
  execution block; (2) directive / directive file / instruction / companion
  document, including the executor's first act; (3) handoff / baton. Text as
  ruled 2026-09-05, reproduced here in full:
  (1) "A paste block is copied whole and pasted whole. There are two kinds.
  A command block is shell commands run as given — never instructions to an
  LLM, and never described as executing. An execution block is instructions
  an LLM agent session carries out — never shell commands." (2) "A directive
  is the package handed to an execution session: one line stating route
  (fresh or existing session) and model tier, stated in full every time, then
  the execution block. The executor's first act is to write it to a file,
  commit it alone, push, and report the SHA; from then on it is cited by path
  and SHA. An instruction is one direction in it, individually refusable. A
  companion document is a committed file the directive requires the executor
  to read first, cited by its own path and SHA." (3) "A handoff transfers
  unfinished responsibility between sessions, with whatever the receiver
  needs to continue. A baton is the handoff between decision sessions —
  state, open questions, decisions in flight, every decision already in a
  committed artifact. A directive is the handoff to an execution session. The
  two are never the same object."
- Every other core row: as the pilot wrote it, re-checked against rulings
  1–8, cluster-mates removed from bodies.

RULINGS BY ROW — decision-layer (role: the four decision roles; session
decision):
- R0223, R0224 retired. R0248 split stands. R0232's "never repeat" lives in
  R0230.
- R0230–R0233 → one row: "If doing what Dave asked has a consequence he would
  act on differently if it went unnamed, say so in one line in the same
  response that hands him the work — once — and then do the work. Anything
  less than that stays unsaid."
- R0234–R0240 → one row: "When what's needed is obvious, produce it — never
  describe it, offer it, or ask whether to. If the call is Dave's, give
  options and ask."
- R0241–R0243 → one row: "State is computed, never maintained. Don't keep a
  status file or register whose contents follow from existing artifacts; if
  gathering it is tedious, propose a script. A record of things that can't be
  derived — a loose-end tracker — is not state, and this doesn't reach it."
  `term: [loose-end tracker]`.
- R0244, R0245, R0246 stay three rows: "Before governing something, check
  decisions/log.md for an entry that already governs it and cite it by ID."
  / "A decision Dave makes is appended to decisions/log.md before the
  session that made it ends." / "A standing rule Dave states aloud is
  proposed as a row in the same turn."
- R0250, R0251 retired; the conversation-retro topic's "use when" row reads
  "when Dave asks", and nothing else invites a retro.
- R0252+R0254+R0255 → one row: "A session that hands responsibility to a
  successor decision session ends by emitting a baton: one paste block —
  decisions, open questions, pointers — and no state the successor can
  recompute from the tree, except a state it would not know to check,
  labelled told." The chief-of-staff topic's baton rows survive only where
  they add to this.
- R0256, R0257, R0258 retired (directive-invariants owns them). R0259–R0261
  → one row: "Choose the model tier by the workload: frontier for canonical
  text, review gates, and anything where a wrong answer is expensive and
  hard to detect; solid general-purpose for implementation against a spec
  and routine review; cheap for mechanical, verifiable work."
- R0262 → "When a file is written to Dave's filesystem — by you or by an
  executor you directed — give its full path as its own paste block: one
  line, nothing else on it, home written as `~`."
- Every other decision-layer row: as its branch wrote it, re-checked against
  rulings 1–8.

ORDER OF WORK, one commit per topic, message `store: <topic> — <n> rows`:
core; decision-layer; then the remaining topics in the digest's card order
(largest first), skipping engagement files, merged topics committed once
under the merged name when their last source file is done.

PER-TOPIC MAP: docs/rule-register/store-map-<topic>-20260906T020000Z.md —
one line per register id consumed: register id, source file, disposition
(written / merged into <id> / split into <ids> / retired-DEC-000380 /
retired-ruling / not-written-engagement), store id; counts beneath.

AFTER THE LAST TOPIC: docs/rule-register/store-summary-20260906T020000Z.md —
one line per topic: source files, rows consumed, rows written, definitions,
retired, with totals; and the list of every register id not consumed by any
topic (expect: the engagement files' rows and nothing else). Commit it alone.

Push after every commit, so partial progress is on origin if the session
ends early. Do not open a pull request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-store-all"`) and report that it is
gone.

rules/ and docs/rule-register/ are outside the frontmatter hook's in-scope
set; the hook should not fire. If it does, stop and report; do not bypass it.

The report also carries: "Decisions taken", grouped by topic, one line each;
"Rows worth reading first", ten across the whole store; and the summary's
totals.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the summary commit and before removing the worktree:

~~~sh
{
  ls rules/*.md | wc -l
  grep -L '^id: ' rules/*.md | wc -l
  grep -h '^topic: ' rules/*.md | sort | uniq -c | sort -rn
  grep -l '^verb: define' rules/*.md | wc -l
  grep -L '^term: ' rules/*.md | wc -l
  ls docs/rule-register/store-map-*-20260906T020000Z.md | wc -l
  git -C "$TMPDIR/fiducial-store-all" log --oneline origin/main..HEAD | wc -l
  git -C "$TMPDIR/fiducial-store-all" diff --stat origin/main..HEAD | tail -1
} 2>&1 | tee "$TMPDIR/store-all-verify.log"
~~~

Expected: a row count the summary explains against the digest's 1043
surviving distinct rules less the engagement rows (about 900) and the
merges Dave's rulings force; 0 without id; one line per topic in the topic
table, none named `engagements`; the definition count; 0 files without a
term key; one map per topic; commits = topics + 2; all additions.

STOP CONDITIONS

Pinned to the reviewed ref a184967413681950a2e8ffa2ab3e16be552f7158. Cannot execute as written: stop
and report. Concurrent tree mutation: stop and report. On any failed command,
any precondition not met, or any tree mutation you did not intend, including
your own — stop and report; do not retry with different flags, and do not
delete or create any ref to recover. A remote operation that exits successfully
is not a failed command, whatever a credential helper writes to stderr.

REPORT

- the directive file's commit SHA
- every commit SHA this session landed, in order, and the branch they are on
- what was verified, how, and where the run log is
- every count reported, with the tree it was observed in — the clone's main
  tree, or the worktree the directive assigns; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status — or, under the sole-tree form, that no worktree
  existed

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Store: write rules/ for every remaining topic under the pilot rulings — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
