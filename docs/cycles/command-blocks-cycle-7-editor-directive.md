# Command blocks cycle 7 — Editor revision Directive

Date: 2026-09-02
Documents in scope:
- skills/command-blocks.md @ f9e517b5331b62a3c0f6fe04af619f8ad56d0583

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/command-blocks-cycle-7-editor-directive.md, commit it alone with a
message naming the cycle it opens, push with git push origin command-blocks-cycle-7 (no -u), verify by git ls-remote origin command-blocks-cycle-7, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

~~~text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
~~~

Both admitted forms, worked:

~~~text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
~~~

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-command-blocks-cycle-7", created by: git worktree add --no-track "$TMPDIR/fiducial-command-blocks-cycle-7" -b command-blocks-cycle-7 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch command-blocks-cycle-7, if a branch of that name already exists locally or on origin (git ls-remote origin command-blocks-cycle-7 returns a ref), or if "$TMPDIR/fiducial-command-blocks-cycle-7" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening the cycle, not a findings disposition. One
document is in scope; a Context Quality Reviewer gate follows in a later
directive. Entries CB-1 through CB-3 are the three changes queued for this
document (told — OPEN-ITEMS.md @ 320f6ca2d13be8ab8c8832f02a347242db5eb230,
"Retrospective session 2026-08-31 — follow-ups" item 7 and the "Queued next"
paragraph; retros/retro-synthesis-20260831T163000.md @
b615d0d04da9421941c47fd789d3690ad7849203, topic T19). Each carries the retro
that evidenced it. Intent is binding; wording is the Editor's — no wording is
dictated. Each change adds a rule paragraph in the body and its criterion to
the conformance list, and the list's stated count changes to match (Core 13).

### CB-1 — accept (T19, fence rule)
Finding: a paste block that contains a ``` fence splits in the delivery
surface into two blocks with loose text between them; observed 2026-08-24
(retros/retro-20260824T163000Z.md, evidence 6). The skill's copyability rule
names heredocs as a known instance and says nothing about inner fences.
Resolution: state the rule — a paste block never contains a ``` fence; any
block nested inside it is fenced with ~~~ and preceded by a one-line fence
note saying the inner fence is ~~~ and why. Place it beside the copyability
rule, as a second known instance or as its own rule, the Editor's call. Add
the matching criterion to the conformance list.
Dictated wording: none.

### CB-2 — accept (T19, environment rule)
Finding: the expected-output rule lets an author state a count measured in a
different environment from the one the block will run in; a sandbox count
was stated as an expectation and did not hold (retros/retro-20260827T155000.md,
"Expected-output lines are claims" and its candidate change).
Resolution: the expected-output line states only what was observed in the
environment the block will run in, or is qualitative — what to look for,
without a number. A count measured elsewhere is not an expectation. Amend
the existing expected-output rule and its criterion; do not add a second
criterion for this.
Dictated wording: none.

### CB-3 — accept (T19, never push the default branch)
Finding: a flip block pushed directly to main and was rejected by branch
protection; a second block moved the commits to a branch
(retros/retro-20260826T2130.md, evidence 10). The skill's sync-and-remote
rule names remote and ref and says nothing about which ref a block may push.
Resolution: state that a command block never pushes the default branch; it
pushes a branch, and the decision session merges through a pull request.
Ground it in policies/commit-and-change-control-policy.md ("changes land via
pull request"; branch protection) by citation, not by restating the policy.
Add the matching criterion to the conformance list.
Dictated wording: none.

## Deferred / out of scope

- The Context Quality Reviewer gate over the revised document — a later
  directive from the decision session; tracked by the cycle.
- T19's parse-atomic-on-paste note (heredocs and multi-line strings stalling
  an interactive shell) — landed in cycle 6 as the copyability rule's known
  instance; not reopened here.
- Any edit to skills/directive-authoring.md or skills/directive-invariants.md
  for the execution-block fence form — a separate item (retro 2026-08-24's
  candidate change); OPEN-ITEMS follow-up 8 territory, not this cycle.

## Execution notes

- Edit skills/command-blocks.md only, in one content commit. The edit flips
  status: in-review and last-reviewed: null in the same commit, per the
  document metadata policy's revision lifecycle; the pre-commit hook does
  this — never bypass it.
- The conformance list's count word ("all nine") is a stated count; Core 13
  applies — change it wherever it appears in the document.
- Leave the document conformant to docs/global-context/review-rubric.md and
  to LEXICON.md (the touch rule); the Context Quality Reviewer gates the
  result in a later directive.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin command-blocks-cycle-7 — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-command-blocks-cycle-7" (no
  --force). If it fails, report the failure; do not retry. Your report's final
  line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
fdee0809441109d9389a4f8dd4c12dd5b4bb5b36. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/command-blocks.md @ f9e517b5331b62a3c0f6fe04af619f8ad56d0583
- reviews/command-blocks-cycle-6.md @ 8e3b95ad622e256e6abc80f5bbeb370ed14616f1
- OPEN-ITEMS.md @ 320f6ca2d13be8ab8c8832f02a347242db5eb230
- retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203
- retros/retro-20260824T163000Z.md @ 361a14d4122df05b53c7c2ebd8ff284309464d0b
- retros/retro-20260826T2130.md @ 361a14d4122df05b53c7c2ebd8ff284309464d0b
- retros/retro-20260827T155000.md @ 361a14d4122df05b53c7c2ebd8ff284309464d0b
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- docs/global-context/decision-layer.md @ 0129260877703b3b0b13045de1726c20040c8ec9
- policies/commit-and-change-control-policy.md @ 6bb7189ab8351ae6d6526a28eac9b72de0c705d6
- policies/remote-write-verification-policy.md @ 2a14bcc1b7f5092d2c991abc9e044a3b07298912
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, before the final push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-command-blocks-cycle-7-frontmatter.log", exit status
   reported.
2. Read the revised document once against CB-1, CB-2 and CB-3 and state, per
   entry, where its change landed (section or line) and which conformance
   criterion carries it, labelled observed.
3. Count the conformance criteria in the revised list and state the count
   beside the count word the document now uses; state whether they agree,
   labelled observed.
4. git diff --stat of the content commit: exactly one file; state it, labelled
   observed.

STOP CONDITIONS

Pinned to the reviewed ref fdee0809441109d9389a4f8dd4c12dd5b4bb5b36. Cannot execute as written: stop
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

    Command blocks cycle 7 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    Decisions — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Deferred / out of scope — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    Execution notes — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
