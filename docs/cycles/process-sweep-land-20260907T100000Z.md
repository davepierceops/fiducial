Process sweep, land: the read's edits and the ten agreements in the decision log

ROUTE AND MODEL

Route: fresh
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first — that command
creates the branch process-sweep-land from origin/process-sweep-fix — then,
in that worktree, write this directive verbatim to
docs/cycles/process-sweep-land-20260907T100000Z.md, commit it alone with a
message naming the package it opens, push the branch with a plain
`git push origin process-sweep-land`, never with `-u`, and report the SHA.
Do this before reading anything else and before touching any other file.
Base verification below runs before this act.

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
worktree at "$TMPDIR/fiducial-process-sweep-land", created by:
git worktree add --no-track "$TMPDIR/fiducial-process-sweep-land" -b process-sweep-land origin/process-sweep-fix

BASE VERIFICATION

Before anything else, fetch origin/process-sweep-fix and origin/main and confirm the base — the
branch process-sweep-fix, not main — is at the reviewed ref
7e865022edefa1afd1211e0cab363850ed485223, and that the branch's merge base with origin/main is
7549f7efed0ed961536bf61620d621ebe6fbb81b. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- every file under process/ except voice.md, read from the base ref
  7e865022edefa1afd1211e0cab363850ed485223 — the ten documents; nine of them you edit
- decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11 — the log;
  last entry DEC-000510; read `git show
  origin/main:decisions/log.md` for the current tail, since main is ahead
  of this branch on that file
- process/decision-log.md, read from the base ref 7e865022edefa1afd1211e0cab363850ed485223 — the
  entry form and id arithmetic

TASK

Two parts, in order. Part A: nine edits the human ruled while reading the
swept documents; one commit per document, verbatim where text is given.
Part B: eleven decision-log entries, one commit each, recording the
agreements. Nothing else changes.

PART A — the edits.

1. process/change-flow.md, line 43: "the second trigger for two" becomes
   "the other trigger for two".
2. process/retro.md: (a) frontmatter `role:` becomes `[chief-of-staff,
   writer]`; (b) move the paragraph beginning "`date:` is the session's
   last interaction" (lines 12–16) to immediately after the schema block
   that defines those fields, keeping its text unchanged.
3. process/trd-template.md: (a) line 38, remove "[R1573]" from the
   non-goals clause and place it on the sentence about design preference
   if one exists; if none does, drop the citation; (b) after the first
   paragraph add one sentence: "The Architect drafts it; the Spec Reviewer
   gates it before the human agrees it."
4. process/prd-template.md: after the first paragraph add one sentence:
   "The Chief of Staff drafts it with the human; the Spec Reviewer gates
   it before the human agrees it."
5. process/decomposition.md, item 2: replace the whole item body with
   "Decompose a spec only after its branch has closed, pinning the
   default-branch SHA. While the branch is open, the only directive against
   the spec is the test suite's, to the Test Designer. Asked to decompose
   an open spec, propose closing it first." Keep any citation the item
   carried, on the first sentence.
6. process/outline.md: frontmatter `role:` becomes `[writer, copy-editor,
   critic]`.
7. process/decision-log.md, line 11: move "[R0583, R0592, R1603]" from
   the "where the log lives" sentence onto the next sentence that states
   the log's rules (append-only, one decision per entry, reverse by
   superseding entry); if those rules are stated as three sentences, cite
   each id on the sentence it supports.
8. process/project-setup.md: (a) remove the `role:` line from the
   frontmatter entirely — no bundle selects this document; (b) line 14,
   "Confirm they hold and say so" becomes "The Chief of Staff confirms they
   hold, once per session, and says so".
9. process/spec-test-suite.md, the paragraph beginning "The one act that
   runs against a spec before it closes": replace it with "Before a spec
   closes, the only work run against it is writing its tests. Write them
   against the spec as it stands; the suite is the evidence the close
   reads [R1468, R1158]. Decomposition waits for the close."

After part A, record each of the ten documents' SHA: `git log -1
--format=%H -- process/<file>` in the worktree, after your last commit to
it. These are the SHAs part B names.

PART B — the decision log. Append to decisions/log.md, whose current tail
is on origin/main (DEC-000510); take the file from origin/main first
(`git checkout origin/main -- decisions/log.md`, committed as the first
part-B commit, `decisions: take the log from main`), then append. Ids
DEC-000520 through DEC-000620. Date 2026-09-07. The form is the log's.
Decision lines verbatim.

- DEC-000520 — process/change-flow.md agreed after the sweep
  Decision: process/change-flow.md is agreed at <sha>, under the process
  gate; one frontier read (reviews/change-flow-read-20260907T060000Z.md),
  blocking findings applied, then the human's sign-off.
  Context: the process sweep of 2026-09-07 reduced it from 252 to 81
  lines.
- DEC-000530 through DEC-000610 — the same form for review-artifact,
  retro, trd-template, prd-template, decomposition, outline, decision-log,
  project-setup, spec-test-suite, in that order, each naming its own read
  artifact and its own line counts (from the sweep: 139→82, 151→67,
  155→59, 119→56, 85→39, 78→41, 77→29, 56→22, 50→26; use the counts after
  part A where they differ). retro's Context adds: "keyed to
  chief-of-staff and writer; the human has never asked a copy editor or
  critic for one." project-setup's adds: "no bundle selects it; the human
  works it once per repository." trd-template's adds: "agreed for this
  version; the human intends to revisit it."
- DEC-000620 — The two-tranche cap is dropped
  Decision: No limit is placed on how many tranches run at once; the rule
  that concurrent deltas cover disjoint spec territory stands unchanged.
  Supersedes: DEC-000170
  Context: the human's ruling of 2026-09-07 on the read of
  process/change-flow.md and process/decomposition.md: R0013 already
  prevents the collision the cap guarded, and no third tranche has ever
  been opened.

Commits: part A `process: land <stem> — <one clause>`; part B `decisions:
DEC-0005NN — <short title>`. Push after every commit. Do not open a pull
request. Remove the worktree at the end (`git worktree remove
"$TMPDIR/fiducial-process-sweep-land"`) and report that it is gone.
Neither process/ nor decisions/ is in the frontmatter hook's in-scope set;
if the hook fires, stop and report.

Report also carries: the ten SHAs part B names, one per line with the
file.

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
  grep -c '^## DEC-' decisions/log.md
  grep '^## DEC-' decisions/log.md | tail -12
  grep -c '^Supersedes: DEC-000170' decisions/log.md
  grep -L '^role:' process/*.md
  grep '^role:' process/retro.md process/outline.md
  grep -c 'the other trigger' process/change-flow.md
  grep -c 'Decomposition waits for the close' process/spec-test-suite.md
  for f in change-flow review-artifact retro trd-template prd-template decomposition outline decision-log project-setup spec-test-suite; do printf '%s ' "$f"; git log -1 --format=%H -- "process/$f.md"; done
  bin/bundle --keys >/dev/null && echo parses
  git -C "$TMPDIR/fiducial-process-sweep-land" diff --stat origin/process-sweep-fix..HEAD | tail -1
  git -C "$TMPDIR/fiducial-process-sweep-land" log --oneline origin/process-sweep-fix..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/process-sweep-land-verify.log"
~~~

Expected: 62 entries; the last twelve headings from DEC-000510 through
DEC-000620; 1; project-setup.md alone under "no role line"; the two role
lists; 1; 1; ten SHAs, each equal to the one its DEC entry names; parses;
a diff-stat touching process/, decisions/log.md and the directive only; 22
commits (1 directive + 9 edits + 1 take-from-main + 11 entries).

STOP CONDITIONS

Pinned to the reviewed ref 7e865022edefa1afd1211e0cab363850ed485223. Cannot execute as written: stop
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

    Process sweep, land: the read's edits and the ten agreements in the decision log — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — author region
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
