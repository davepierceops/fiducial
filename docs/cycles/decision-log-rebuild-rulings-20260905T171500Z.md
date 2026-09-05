# Decision-log entries: rebuild rulings of 2026-09-04

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first, then write. Write
this directive verbatim to
docs/cycles/decision-log-rebuild-rulings-20260905T171500Z.md in that worktree,
commit it alone with a message naming the package it opens
(`decision-log: rebuild rulings of 2026-09-04 — directive`), push the branch
`decision-log-rebuild-rulings` to origin, and report the SHA. Do this before
reading anything else and before touching any other file.

FENCE NOTE: fences in the author-written regions (TASK, VERIFICATION) use
`~~~` so they survive transport inside a paste block; the generator's own
regions keep their ``` fences and the paste block that carries this directive
is opened with four backticks for that reason. Treat `~~~` fences exactly as
````fences.

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
worktree at "$TMPDIR/fiducial-decision-log-rebuild-rulings", created by:
git worktree add --no-track "$TMPDIR/fiducial-decision-log-rebuild-rulings" -b decision-log-rebuild-rulings origin/main

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
4a118f5b57f5192a7bb668346f718a5cc188b745. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/decision-log-policy.md @ 8a6efb0c49255a28b42f7ed2ba7c0cbe83cec2cb
  (the entry format and ID assignment rule)
- decisions/log.md @ 9cca04849c14d3f49a8ff0e171932e7590073158, read from the
  base ref 4a118f5b57f5192a7bb668346f718a5cc188b745 — the last entry only
  (DEC-000370); confirm it is the last entry before appending

TASK

Append four entries to decisions/log.md, in this order, verbatim. Each is one
decision; none is edited or merged. The log is append-only: touch nothing above
the new entries. Confirm first that DEC-000370 is the last entry; if any entry
above DEC-000370 exists, stop and report — the ids below are wrong.

Separate each entry from the one before it with one blank line, matching the
existing entries. Every entry is Dave's ruling of 2026-09-04; the wording is
fixed and the executor does not improve it.

~~~markdown
## DEC-000380 — Rebuild: gates move from documents to content; the document-lifecycle machinery retires
Date: 2026-09-04
Decision: Rules become rows in rules/ (one rule, one record); a row in rules/ is in force and nothing else certifies it. The one gate on a rule is intake: a Context Quality Reviewer session shapes the proposal into one instruction, checks it against the store, sets and normalizes its keys, and lands it in one commit. Retired with this ruling: the status and last-reviewed fields, the agreement flip, review cycles per document, the expedited and doc-only paths, the in-scope set, the pre-commit hook, and the tools check-frontmatter, flip-agreed, install-hooks, migrate-frontmatter, and reviews/expedited-log.md. Documents that describe a sequence stay prose under process/, gated by one frontier read against the rows they cite plus Dave's sign-off, recorded as a decision-log entry naming the SHA. Content carries — rules, this log, retros; machinery does not.
Context: 62 governed files, each a bag of rules carrying a lifecycle that certified the container while agents act only on the content; one policy took 22 cycles to agree; Pass 3 at main 4a118f5 counted 1600 rows, 1131 distinct rules, 206 clusters of restatement across files. The machinery was an artifact of how the project grew from June, not a requirement of the methodology. Dave rejected "one file per row with the old gates" as the same complexity under a new name. Ruled in the session that produced rule-store-prd-20260904T233500Z.md, the PRD superseding specs/bundle-system.md.
Supersedes: DEC-000010, DEC-000020, DEC-000030, DEC-000040, DEC-000050, DEC-000060

## DEC-000390 — The name and the history stay: fiducial, no rewrite, old corpus moved to docs/history
Date: 2026-09-04
Decision: The methodology and the repository keep the name fiducial. History is preserved: no force-push, no rewrite of any ref; the retired corpus moves whole to docs/history/corpus-<sha>/, never deleted, so every row's source resolves at the named SHA. Git mechanics of the move are the Chief of Staff's to carry out; Dave does not rule on them.
Context: The rebuild (DEC-000380) replaces the governed files with rows. Renaming or restarting the repository would cost the history that the rows' source pointers, the decision log, and the retros rest on, for no gain the ruling needs.

## DEC-000400 — The row: id, instruction, zero-to-N free key-value pairs; selection is a query over keys
Date: 2026-09-04
Decision: A row is an id, an instruction body, and zero or more key-value pairs with no fixed schema. Selection is a query over keys (bin/bundle --where role=writer corpus=writing): a row matches when every named key holds the value. No reserved values; no special tags key; the keys in use are computed on demand (bin/bundle --keys) and never maintained as a list; intake normalizes every incoming key against the keys already in use. Conventions: every value is a list of words (a bare word is a list of one); exactly two keys are typed — id is text, order is a number. topic carries the grouping the file used to do, seeded from the source path and corrected from the clustering output; no topic list is designed in advance. A row is one obligation and stands alone; adjacency that still matters is carried by order within a topic. An optional ## Human section carries the rationale and is never rendered to an agent.
Context: The bundle-system TRD's audience-and-corpus model resolved membership through a file's frontmatter and a fixed vocabulary; the rebuild needs membership to be the row's own keys so that a new role, corpus, or topic is a new value, not a tool edit. "Tag" framing was retired with this ruling: a tag is just a key with one value. Stated in full in fiducial-rebuild-shape-20260905T000500Z.md § "The row".

## DEC-000410 — Storage boundary: the filesystem is the initial persistence mechanism, not an architectural dependency
Date: 2026-09-04
Decision: Treat the filesystem representation as the initial persistence mechanism, not as an architectural dependency of the rule-processing logic. Define a narrow abstraction for obtaining rule rows. Code that selects, validates, orders, bundles, retires, or otherwise reasons about rules operates on row objects and does not know whether those rows came from individual files, a database, or another backing store. The initial implementation may read one rule per file from rules/, but filesystem traversal, filename conventions, frontmatter parsing, and file I/O stay inside the storage layer. The boundary makes it possible to replace the filesystem-backed implementation later with a database-backed implementation without changing the rule-processing logic. Do not introduce a database now merely to satisfy this abstraction. The goal is substitution, not premature infrastructure.
Context: Files are an unusual store for something that is plainly rows — a fine choice for now, but one the project should be free to change, and changing it should touch one layer of the code and nothing else. Dave's wording, verbatim from fiducial-rebuild-shape-20260905T000500Z.md § "Storage boundary"; the PRD carries it as G7 and AC-RS-4.
~~~

Commit the log edit alone, on the same branch, with the message
`decision-log: DEC-000380 to DEC-000410 — rebuild rulings of 2026-09-04`.
Push the branch to origin. Do not open a pull request; report the branch and
both SHAs.

decisions/log.md is outside the frontmatter hook's in-scope set; the hook
should not fire. If it does, stop and report; do not bypass it.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the log commit:

~~~sh
{
  grep -n '^## DEC-' decisions/log.md | tail -5
  git -C "$TMPDIR/fiducial-decision-log-rebuild-rulings" diff --stat origin/main..HEAD
  git -C "$TMPDIR/fiducial-decision-log-rebuild-rulings" log --oneline origin/main..HEAD
} 2>&1 | tee "$TMPDIR/decision-log-rebuild-rulings-verify.log"
~~~

Expected: the last five headings are DEC-000370 through DEC-000410 in order;
the diff-stat names exactly two files — this directive and decisions/log.md —
with decisions/log.md showing insertions only, zero deletions; the log shows
exactly two commits. Any deletion in decisions/log.md is a stop: the log is
append-only.

STOP CONDITIONS

Pinned to the reviewed ref 4a118f5b57f5192a7bb668346f718a5cc188b745. Cannot execute as written: stop
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

    Decision-log entries: rebuild rulings of 2026-09-04 — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
