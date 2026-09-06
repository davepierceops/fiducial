# Store pilot: write rules/ for topic core from the Pass 3 clusters

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to docs/cycles/store-pilot-core-20260906T003000Z.md in
that worktree, commit it alone with a message naming the package it opens
(`store: pilot core — directive`), push the branch store-pilot-core to origin
with a plain `git push origin store-pilot-core`, never with `-u`, and report
the SHA. Do this before reading anything else and before touching any other
file. Base verification below runs before this act.

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
worktree at "$TMPDIR/fiducial-store-pilot-core", created by:
git worktree add --no-track "$TMPDIR/fiducial-store-pilot-core" -b store-pilot-core origin/main

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a184967413681950a2e8ffa2ab3e16be552f7158. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16, read from the
  base ref fd54448 (`git show fd54448:docs/global-context/core.md`); this is
  the text every row's `source` points at, 55 lines. Not main's copy.
- docs/rule-register/rule-register-20260904T210000Z.md @ 45b02c7b88a0e08f4872713aa39f840a59117423
  — the 61 rows whose source column is docs/global-context/core.md, plus
  every row that shares a cluster with one of them (the clusters artifact
  names them); do not read it whole
- docs/rule-register/rule-clusters-20260904T223000Z.md @ acdfef73fc04bed73d6f854b3f66fe8df5411519
  — the method notes; every cluster in any section that contains a core row
  (23 clusters, 27 core rows); the core line of the per-file view
- docs/rule-register/topic-digest-20260905T181500Z.md @ 0bd149ce85f8519e2e9d681d3827b74bef237f43
  — card 5 (core) and the header
- decisions/log.md @ d81c41a6ab60288764d8a3898cd66b354b3c664b — DEC-000290,
  DEC-000380, DEC-000400 whole

TASK

This is the pilot of the Store package: one topic, `core`, written as rows so
Dave can judge the row model on real rules before the other 53 topics follow.
Everything below is the rule for every later topic unless the pilot changes
it; where you find the rule under-specified, decide, and put the decision in
the report under its own heading so it can be ruled on once.

WHAT A ROW IS. One file per rule under rules/, filename `<id>.md`. YAML
frontmatter between `---` lines, then the instruction as the body, then an
optional `## Human` section. Frontmatter keys, in this order:

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
also: null
term: null
~~~

- `id` is the register id of the row's representative (below); never a new
  number, never reused.
- `topic` is `[core]` for every row in this run.
- `order` counts by 10 in the order the rules appear in core.md at fd54448,
  so adjacency in the file survives; a rule the file states once but the
  register split into several rows gets consecutive orders.
- `role` is `[all]` — core's audience is every role. `session` is
  `[decision, execution]` for every row; core governs both.
- `corpus` is `[software, writing, methodology]` — every corpus in use.
- `verb` is the register's: require, forbid, define, stop.
- `condition` is the trigger in plain words, taken from the register's
  condition column, or `null`.
- `source` is written exactly as the example above: the path, a colon, the
  line number in core.md at fd54448 where the rule is stated, then the ref.
  Verify each line number by reading the ref, not the register.
- `also` lists the register ids of every other row in the same cluster
  (from any file), so nothing is lost and later topics know these are
  written; `null` for singletons.
- `term` is the word or phrase defined, for `verb: define` rows only —
  `[decision session]`, `[paste block]`, `[baton]`; `null` otherwise. Where a
  definition is used in more than one surface form (`tranche`, `tranches`),
  list the forms.

The body is the instruction, one obligation, in the second person or as a
bare imperative, stated so an agent holding nothing else can act on it. It
is not a quotation of core.md; it is the rule core.md states, at the
register's granularity. A `define` row's body is the definition.

The `## Human` section is written only where core.md gives a reason for the
rule in its own prose — the "why", never a restatement. Where the prose gives none, omit
the section; do not invent a rationale.

WHAT TO WRITE. One row per distinct rule the digest counts for core: 57 —
61 register rows less the intra-core duplicates the clusters artifact names.
The rules:

1. A core row in no cluster is one store row, `also: null`.
2. A cluster containing one or more core rows is one store row under topic
   core, whichever files its other members come from: core is loaded first
   by every session and is the canonical home of what it states. The
   representative is the lowest core register id in the cluster; the body is
   written from the fullest statement in the cluster, wherever it lives; the
   `source` points at core's line; `also` lists every other member.
3. C019 — the timestamp-precision divergence — is ruled: DEC-000290, the
   strictest form (`<YYYYMMDD>T<HHMMSS>Z`, UTC, `Z` required). Write the
   row in that form and cite DEC-000290 in `## Human`.
4. C001 and any other divergent cluster containing a core row: apply Dave's
   ruling as the digest's card 5 and the clusters artifact record it; if a
   divergent cluster with a core row has no recorded ruling, write the row
   in core's own form and name the cluster under "Decisions taken" in the
   report.
5. Nothing in core retires (card 5: Retiring none). If you find a row whose
   only obligation is the document-lifecycle machinery DEC-000380 retires,
   do not write it; name it in the report. Expect zero.
6. A compound register row — one row stating two obligations — is two
   store rows, consecutive orders, both citing the same source line. Name
   each split in the report.

THE MAP. Write docs/rule-register/store-map-20260906T003000Z.md: a table,
one line per register id this run consumed — the 61 core rows and every
cluster-mate listed under `also` — with columns register id, source file,
disposition (written / merged into <store id> / split into <ids> /
retired), store id. Later topic runs read this file first and skip every id
in it. State the counts under the table: rows consumed, store rows written,
definitions among them.

Commit the rows and the map in one commit with the
message `store: pilot core — 57 rows from the Pass 3 clusters` (the real count
if it differs, and say why in the report). Push. Do not open a pull request. Then
remove the worktree (`git worktree remove "$TMPDIR/fiducial-store-pilot-core"`)
and report that it is gone.

rules/ and docs/rule-register/ are outside the frontmatter hook's in-scope
set; the hook should not fire. If it does, stop and report; do not bypass it.

The report also carries two sections beyond the standard items: "Decisions taken" —
every place this directive left something to your judgment and what you
chose, one line each, so Dave can rule on the batch; and a section "Rows
worth reading first" — the five rows you are least sure of, by id, with one
line each on why.

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
  grep -l '^verb: define' rules/*.md | wc -l
  grep -h '^source: ' rules/*.md | sed 's/.*core.md:\([0-9]*\) @.*/\1/' | sort -n | uniq | awk '$1<1 || $1>55' | wc -l
  grep -c '^| R' docs/rule-register/store-map-20260906T003000Z.md
  git -C "$TMPDIR/fiducial-store-pilot-core" diff --stat origin/main..HEAD | tail -1
  git -C "$TMPDIR/fiducial-store-pilot-core" log --oneline origin/main..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/store-pilot-core-verify.log"
~~~

Expected, in order: the row-file count (57 unless the report says why not);
0 files without an id line; the definition count (20 unless a definition was
merged or split — say which); 0 source lines outside 1–55; the map's line
count, equal to rows consumed; the diff-stat's last line naming that many
files plus the directive plus the map, all additions; 2 commits.

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

    Store pilot: write rules/ for topic core from the Pass 3 clusters — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
