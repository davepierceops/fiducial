# Bundle tool, follow-up: the one read over the delta, two passes

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-followup-read-20260907T190000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-followup-read to origin with a plain push
(git push origin bundle-tool-followup-read — never with -u), and report the SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-bundle-tool-followup-read", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-followup-read" -b bundle-tool-followup-read origin/bundle-tool-followup

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-followup and origin/main and confirm the base — the
branch bundle-tool-followup, not main — is at the reviewed ref
252928b84e19b530b9acc25159a80ab478223848, and that origin/main is at
cd5d8fd29477df29a712609e5b50a1a30e2d8d7f, the branch's merge base. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/bundle-tool-followup-20260907T170000Z.md, read from the base
  ref 252928b84e19b530b9acc25159a80ab478223848 — what the Coder was told: the rulings,
  the dispositions of the earlier findings, and the ruled test edits
- reviews/bundle-tool-quality-20260906T150000Z.md,
  reviews/bundle-tool-skeptic-20260906T150000Z.md,
  reviews/bundle-tool-quality-reread-20260906T170000Z.md and
  reviews/bundle-tool-skeptic-reread-20260906T170000Z.md, read from the base
  ref 252928b84e19b530b9acc25159a80ab478223848 — the findings the delta claims to close
- process/review-artifact.md and process/named-queries.md, read from the base
  ref 252928b84e19b530b9acc25159a80ab478223848
- the diff origin/main..origin/bundle-tool-followup
  (cd5d8fd29477df29a712609e5b50a1a30e2d8d7f..252928b84e19b530b9acc25159a80ab478223848) — the
  change under review, 30 files in 25 commits, and nothing outside it

TASK

The one read over the delta: the whole diff from origin/main to the base
ref, in two passes, each its own artifact with its own verdict, both from
this session. The delta is routine — no consequential-class surface — so
one session runs both. Review the diff; do not edit anything under bin/,
process/ or decisions/; nothing outside the diff is under review, though
you read whatever you need to judge it.

CONTINUITY, carried in each pass where it applies: does the delta
contradict anything it did not change? Read the four DEC entries it appends
against the code that implements them and against process/named-queries.md's
prose; read process/named-queries.md's list against the twelve role values
that `bin/bundle --keys` reports; read the eleven `topic:` keys against each
file's stem; read the interface-contract citations the Coder amended.

PASS 1 — QUALITY (Reviewer). A code review of every file in the diff. For
each of items 3–6 of the directive: does the code do what the item says,
and is it minimum change. For each accepted finding in item 7: closed as
its Fix stated, or not. For item 8: are the ruled test edits the ones
ruled and no others — the Coder reports folding four fixture and assertion
changes into items 3, 4, 5 and 8, landing Q5's `LOCAL_MODULES` line early
under item 6, and rewriting probe (f) beyond S10's scope; judge each as
within the directive's grant or as a finding, and say which. Then test
adequacy for what is new: the named-queries parser (a missing file, a
missing heading, a block with blank lines, a name on two lines), the sort
key (unnamed topics, a process row with no `topic` key), and bin/release
(every refusal it lists, the gh line's shape, cleanup on a failed entry).
Run the suite and cite its summary line. Artifact:
reviews/bundle-tool-followup-quality-20260907T190000Z.md.

PASS 2 — SKEPTICISM (Skeptic/Risk). Where is this lying to us? Construct,
do not read: run bin/release end-to-end against a purpose-built store
repository (bare origin, level clone, README.md, a named-queries.md listing
three roles) and check the assets' names, that every asset's first line is
the one-line header at that HEAD, and that the printed gh line names the
tag, the target SHA, README.md and every asset by full path; then make one
listed query select nothing and confirm exit 2 and an empty `--out`. Render
all twelve real bundles in the worktree directly through FileRowSource,
select and render (the CLI's sync refusal fires on a branch) and report, per
role, row count, process-document count and definition count — and whether
any bundle renders empty or any role in the list selects nothing. Check the
sort for a topic the sequence does not name (architect-agent rows carry
no `topic: architect-agent`; say where they land and why). Re-run the probe
script whole and say which sub-probes now report the tree as it stands and
which still print static text. Artifact:
reviews/bundle-tool-followup-skeptic-20260907T190000Z.md.

One thing is already known and is not a finding: the Coder's check script
counted `## Releasing` in process/named-queries.md as an `## R` heading;
the regex was the directive's, and no row heading exists.

Both artifacts follow process/review-artifact.md, scoped to the diff, with
a Verdict per pass; the overall verdict is the more severe. Every finding
carries its Location, Consequence and Fix, labelled blocking or
non-blocking; a defect class with several instances is one finding listing
them. Commits, in order, pushed after each: the directive (FIRST ACT); the
quality artifact; the skeptic artifact. Nothing else. Do not open a pull
request. Remove the worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-followup-read"`) and
report that it is gone. If the frontmatter hook fires, stop and report.

Report also carries: both verdicts and the overall; the per-role table from
PASS 2; and one line per blocking finding.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the last commit and before removing the worktree:

~~~sh
{
  ls reviews/bundle-tool-followup-*
  grep -h '^Verdict' reviews/bundle-tool-followup-quality-20260907T190000Z.md reviews/bundle-tool-followup-skeptic-20260907T190000Z.md
  bin/tests/run 2>&1 | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup-read" diff --stat origin/bundle-tool-followup..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup-read" log --oneline origin/bundle-tool-followup..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-followup-read-verify.log"
~~~

Expected: two files; four verdict lines; OK from the suite; a diff-stat
touching reviews/ and the directive file only; 3 commits.

STOP CONDITIONS

Pinned to the reviewed ref 252928b84e19b530b9acc25159a80ab478223848. Cannot execute as written: stop
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

    Bundle tool, follow-up: the one read over the delta, two passes — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
