# Conversation retro cycle 5 — Editor revision Directive

Date: 2026-09-03
Documents in scope:
- skills/conversation-retro.md @ dc72fcd3c42ea76f09074f70934ea6bb3bfe2507

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that
worktree, write this directive verbatim to
docs/cycles/conversation-retro-cycle-5-editor-directive.md, commit it alone
with a message naming the cycle it opens, push with git push origin conversation-retro-cycle-5
(no -u), verify by git ls-remote origin conversation-retro-cycle-5, and report the SHA. Do this
before reading anything else and before touching any other file.

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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-conversation-retro-cycle-5", created by: git worktree add --no-track "$TMPDIR/fiducial-conversation-retro-cycle-5" -b conversation-retro-cycle-5 origin/main

Before creating it, run git fetch origin, then git worktree list; if any
worktree holds branch conversation-retro-cycle-5, if a branch of that name already exists locally or
on origin (git ls-remote origin conversation-retro-cycle-5 returns a ref), or if "$TMPDIR/fiducial-conversation-retro-cycle-5" already exists,
stop and report. Entries git marks prunable are not yours; ignore them. Do not
touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening cycle 5, not a findings disposition. One
document is in scope; a Context Quality Reviewer gate follows in a later
directive. Two changes are queued for this document (told —
decisions/log.md @ 9cca04849c14d3f49a8ff0e171932e7590073158, DEC-000310;
OPEN-ITEMS.md @ 320f6ca2d13be8ab8c8832f02a347242db5eb230, "Queued next"
paragraph, the skills/conversation-retro.md conforming-revision sentence and
its pull-request-#273 rider). Intent is binding; wording is the Editor's — no
wording is dictated.

### CR5-1 — accept (DEC-000310, conform to the ruling)
Finding: the document still encodes the obligation DEC-000310 retired. Its
"Use when" section defers to Decision Layer rule 12 as stating when a retro
is owed, a skip condition, and a baton-before-retro ordering; rule 12 at main
now reads "A retro runs when Dave asks, not by default" and states none of
those. The section's third trigger runs a retro on chat close, and its second
runs one on a Chief of Staff end-of-session recommendation that Dave acks —
both are the default-run DEC-000310 removes.
Resolution: conform the document to DEC-000310. A retro is produced when Dave
asks for one; there is no standing obligation, no skip condition, and no
ordering against a baton. Remove the deference paragraph and the two
default-run triggers; keep "Dave directs a retro explicitly" (or its
equivalent) as the single condition. Read the rest of the document for any
sentence that presupposes one retro per session or a retro owed at close —
the Purpose paragraph's "one retrospective per LLM conversation" is the
candidate — and rephrase where it does (Core 13: a changed fact changes
everywhere it appears). "How to produce one" is unchanged.
Dictated wording: none.

### CR5-2 — accept (pull request #273 rider, "routes")
Finding: the "Use when" section calls its triggers "routes". Route is a
directive term: Core's vocabulary entry for Directive names route as the
first of its three stated parts (fresh or existing session), and the Lexicon's
retired-terms entry for Track repeats it. The skill reuses the word in a
second sense.
Resolution: the document does not call a trigger a route. Whatever
triggering text survives CR5-1 uses another word — condition, trigger, or
plain prose — and the word "route" does not appear in the revised document
in the trigger sense. The Lexicon's touch rule applies to the whole edit.
Dictated wording: none.


## Deferred / out of scope

- The Context Quality Reviewer gate over the revised document — a later
  directive from the decision session; tracked by the cycle.
- policies/document-metadata-policy.md's sentence "a document may exclude its
  own revisions from this path, and the retro skill does" — whether the skill
  still states such an exclusion is a question for that policy's own queued
  cycle (OPEN-ITEMS "Queued next"), not this one. Do not edit the policy.
- docs/global-context/decision-layer.md rule 12 — already conformed at cycle
  15 (reviews/decision-layer-cycle-15.md); read it, do not edit it.

## Execution notes

- Edit skills/conversation-retro.md only, in one content commit. The edit
  flips status: in-review and last-reviewed: null in the same commit, per the
  document metadata policy's revision lifecycle; the pre-commit hook does
  this — never bypass it.
- Leave the document conformant to docs/global-context/review-rubric.md and
  to LEXICON.md (the touch rule); the Context Quality Reviewer gates the
  result in a later directive.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin conversation-retro-cycle-5 — no -u; the sandbox refuses the .git/config
  write. Process substitution (<(...)) is refused by the sandbox; use temp
  files.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-conversation-retro-cycle-5" (no --force). If it fails, report the
  failure; do not retry. Your report's final line states whether the worktree
  was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
1f1404b2a13a57883897e7203ecf92464a4693f1. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/conversation-retro.md @ dc72fcd3c42ea76f09074f70934ea6bb3bfe2507
- decisions/log.md @ 9cca04849c14d3f49a8ff0e171932e7590073158
- OPEN-ITEMS.md @ 320f6ca2d13be8ab8c8832f02a347242db5eb230
- reviews/conversation-retro-cycle-4.md @ 30a9a938835e4f3a7d0d24e3eca3b9bf862de03b
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- docs/global-context/decision-layer.md @ 0129260877703b3b0b13045de1726c20040c8ec9
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d

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
   "$TMPDIR/fiducial-conversation-retro-cycle-5-frontmatter.log", exit status
   reported.
2. Read the revised document once against CR5-1 and CR5-2 and state, per
   entry, where its change landed (section or line), labelled observed.
3. grep -n -i "rule 12\|route" skills/conversation-retro.md in the worktree,
   output captured to "$TMPDIR/fiducial-conversation-retro-cycle-5-grep.log";
   state the match count and, for any match, the sense in which the word is
   used, labelled observed. The expected outcome is qualitative: no match in
   the trigger sense and no reference to Decision Layer rule 12.
4. git diff --stat of the content commit: exactly one file; state it, labelled
   observed.

STOP CONDITIONS

Pinned to the reviewed ref 1f1404b2a13a57883897e7203ecf92464a4693f1. Cannot execute as written: stop
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

    Conversation retro cycle 5 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
