# Store: write rules/ for topic decision-layer from the Pass 3 clusters

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to
docs/cycles/store-decision-layer-20260906T010000Z.md in that worktree, commit
it alone with a message naming the package it opens
(`store: decision-layer — directive`), push the branch store-decision-layer to
origin with a plain `git push origin store-decision-layer`, never with `-u`,
and report the SHA. Do this before reading anything else and before touching
any other file. Base verification below runs before this act.

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
worktree at "$TMPDIR/fiducial-store-decision-layer", created by:
git worktree add --no-track "$TMPDIR/fiducial-store-decision-layer" -b store-decision-layer origin/main

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a184967413681950a2e8ffa2ab3e16be552f7158. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/global-context/decision-layer.md @ 0129260877703b3b0b13045de1726c20040c8ec9,
  read from the base ref fd54448
  (`git show fd54448:docs/global-context/decision-layer.md`); this is the
  text every row's `source` points at, 38 lines. Not main's copy.
- docs/rule-register/rule-register-20260904T210000Z.md @ 45b02c7b88a0e08f4872713aa39f840a59117423
  — the 40 rows whose source column is docs/global-context/decision-layer.md;
  do not read it whole
- docs/rule-register/rule-clusters-20260904T223000Z.md @ acdfef73fc04bed73d6f854b3f66fe8df5411519
  — the method notes; the clusters containing a decision-layer row (the
  digest names C063, C109, C110 and there may be intra-file ones); the
  decision-layer line of the per-file view
- docs/rule-register/topic-digest-20260905T181500Z.md @ 0bd149ce85f8519e2e9d681d3827b74bef237f43
  — card 16 (decision-layer) and the header
- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — DEC-000380,
  DEC-000400 whole

TASK

Write topic `decision-layer` as rows under rules/. This is the second topic of
the Store package; the first (core, branch store-pilot-core) taught the rules
below, which supersede the pilot's where they differ. Where you find a rule
under-specified, decide, and put the decision in the report under "Decisions
taken" so it can be ruled on once.

WHAT A ROW IS. One file per rule under rules/, filename `<id>.md`. YAML
frontmatter between `---` lines, then the instruction as the body, then an
optional `## Human` section. Frontmatter keys, in this order:

~~~text
id: R0234
topic: [decision-layer]
order: 40
role: [chief-of-staff, writer, copy-editor, critic]
session: [decision]
corpus: [software, writing, methodology]
verb: require
condition: null
source: docs/global-context/decision-layer.md:14 @ fd54448
term: null
~~~

- `id` is the register id of the row (the lowest id where rows merge); never
  a new number, never reused.
- `topic` is `[decision-layer]` for every row in this run.
- `order` counts by 10 in the order the rules appear in decision-layer.md at
  fd54448, so adjacency survives.
- `role` lists every role that runs as a decision session; the audience of
  decision-layer.md at fd54448 is `all-decision-roles`, and the roles it
  resolves to are the role documents under roles/ at fd54448 whose
  frontmatter says `session: decision` — read them from the ref with
  `git show fd54448:roles/<file>` and list their basename slugs. Where a
  single row plainly binds a narrower set (a row about the artifact pane
  binds the roles that use one), narrow it and say so under "Decisions
  taken".
- `session` is `[decision]` for every row; this file never reaches an
  execution session.
- `corpus` is `[software, writing, methodology]` unless a row plainly binds
  one corpus.
- `verb` is the register's: require, forbid, define, stop.
- `condition` copies the trigger in plain words for querying, or `null`. It
  is never the only place the trigger lives: **the body states its own
  trigger**, and reads as a complete instruction with the frontmatter
  covered.
- `source` is written exactly as the example above: the path, a colon, the
  line number at fd54448 where the rule is stated, then the ref. Verify each
  line number by reading the ref, not the register.
- `term` is the word or phrase defined, for `verb: define` rows only, listing
  every surface form used (`[baton, batons]`); `null` otherwise, and `null`
  where a define row defines a proposition rather than a term.

The body is the instruction, one obligation, in the second person or as a
bare imperative, stated so an agent holding nothing else can act on it — not
a quotation of the file, the rule the file states, in the file's own scope
and no more. A `define` row's body is the definition.

The `## Human` section is written only where decision-layer.md gives a reason
for the rule in its own prose — the why, never a restatement. Where the prose
gives none, omit the section.

WHAT MERGES AND WHAT DOES NOT — Dave's rulings from the pilot, in force for
every topic:

1. **Two register rows are one store row only when they state the same
   obligation AND would carry the same keys.** Where members of a cluster
   would differ on any key — topic, role, session, corpus, condition, term —
   that key splits the cluster, one row per distinct value. Cross-file
   cluster-mates therefore always differ on `topic` and are never merged into
   this topic's rows: they are written by their own topic runs. This run
   writes decision-layer's rows only; there is no `also` key.
2. **One rule stated then restated is one row.** Where the file states a rule
   and then its negation ("do X" / "never not-X"), or a rule and then its
   named instance, or a rule and then its per-audience elaboration, write one
   row from the positive form; the extractor's split does not survive. Where
   the elaboration is a distinct obligation that binds a narrower audience,
   it is its own row with the narrower key.
3. **Container rules retire.** A row whose instruction is about loading,
   ordering, or the precedence of documents — "load this after Core", "this
   layer adds to Core" — is not written; name it in the report. Expect
   decision-layer's opening lines to yield one or two.
4. **Bodies are the file's own text.** Where a cluster-mate from another file
   has fuller wording, it stays in that file's topic; this topic's body is
   what decision-layer.md says, sharpened for an agent holding nothing else,
   not widened.
5. Nothing in decision-layer retires under DEC-000380 (card 16: Retiring
   none). If a row's only obligation is the lifecycle machinery DEC-000380
   names, do not write it and name it in the report. Expect zero.
6. A compound register row — one row stating two obligations — is two store
   rows, consecutive orders, same source line. Name each split in the report.
7. A row that turns out to bind one side of a flow (the reader of a report,
   not its writer) is not retired; it is re-keyed. Name each re-keying.

THE MAP. Write docs/rule-register/store-map-decision-layer-20260906T010000Z.md:
a table, one line per decision-layer register id (40), with columns register
id, disposition (written / merged into <store id> / split into <ids> /
retired), store id. Under the table: rows consumed, store rows written,
definitions among them, rows retired.

Commit the rows and the map in one commit with the
message `store: decision-layer — <n> rows from the Pass 3 clusters`, n the
real count. Push. Do not open a pull request. Then remove the worktree
(`git worktree remove "$TMPDIR/fiducial-store-decision-layer"`) and report
that it is gone.

rules/ and docs/rule-register/ are outside the frontmatter hook's in-scope
set; the hook should not fire. If it does, stop and report; do not bypass it.
rules/ does not exist on main at the base; create it. The pilot's rows are on
another branch and are not in your tree; do not fetch them.

The report also carries two sections beyond the standard items: "Decisions
taken" — every place this directive left something to your judgment and what
you chose, one line each; and "Rows worth reading first" — the five rows you
are least sure of, by id, one line each on why.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the commit and before removing the worktree:

~~~sh
{
  ls rules/*.md | wc -l
  grep -L '^id: ' rules/*.md | wc -l
  grep -L '^topic: \[decision-layer\]' rules/*.md | wc -l
  grep -l '^verb: define' rules/*.md | wc -l
  grep -h '^source: ' rules/*.md | sed 's/.*decision-layer.md:\([0-9]*\) @.*/\1/' | sort -n | uniq | awk '$1<1 || $1>38' | wc -l
  grep -c '^| R' docs/rule-register/store-map-decision-layer-20260906T010000Z.md
  git -C "$TMPDIR/fiducial-store-decision-layer" diff --stat origin/main..HEAD | tail -1
  git -C "$TMPDIR/fiducial-store-decision-layer" log --oneline origin/main..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/store-decision-layer-verify.log"
~~~

Expected, in order: the row-file count (the report says what it is and why
it differs from the digest's 38); 0 files without an id; 0 files outside the
topic; the definition count; 0 source lines outside 1–38; 40 map lines; the
diff-stat's last line naming that many row files plus the directive plus the
map, all additions; 2 commits.

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

    Store: write rules/ for topic decision-layer from the Pass 3 clusters — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
