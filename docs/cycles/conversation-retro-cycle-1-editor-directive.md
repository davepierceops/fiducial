# Retro-skill cycle 1 — Editor revision Directive

Date: 2026-08-31
Documents in scope:
- skills/conversation-retro.md @ 62f2fa6c1e278f0b75894e23b4e44fa374e2efbc

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/conversation-retro-cycle-1-editor-directive.md, commit it alone with a
message naming the package it opens, push the branch to origin, and report the
SHA. Do this before reading anything else and before touching any other file.

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
worktree at "$TMPDIR/fiducial-retro-skill-cycle-1", created by: git worktree add --no-track "$TMPDIR/fiducial-retro-skill-cycle-1" -b retro-skill-cycle-1 origin/main

## Decisions

This is an Editor revision opening the cycle, not a findings disposition: no
review artifact precedes it. Each entry below is a ruled change (told — Dave's
rulings, recorded in OPEN-ITEMS.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b,
"Retrospective session 2026-08-31 — follow-ups" item 1 and the "Queued next"
line, and in retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203,
topics T17 and T18). Intent is binding; wording is the Editor's — no wording is
dictated. The document is on the expedited path's ineligible list; a full
Context Quality Reviewer gate follows this revision in a later directive.

### RS-1 — accept
Finding: the retro procedure must read nothing from and write nothing to any
remote, GitHub included.
Resolution: revise the skill so the retro is produced and handed in chat only;
placement into the repo is a separate command-block step from a decision
session. Remove or rewrite any text implying the retro session touches a
remote. This also retires the unverified connector landing path T18 records —
no landing path remains to verify.
Dictated wording: none.

### RS-2 — accept
Finding: `date:` currently reads as generation time; the ruling is that
`date:` is the session's last interaction.
Resolution: define `date:` as the session's last interaction, derived from the
last dated artifact the session touched; add a `generated:` field for
generation time; the filename timestamp stays the opaque, collision-free
handle it already is. Generated timestamps conform to DEC-000290: UTC,
`Z` required.
Dictated wording: none.

### RS-3 — accept
Finding: a synthesis does not name what it covered, so unsynthesized retros
cannot be computed.
Resolution: require a synthesis document to list the retro filenames it
covers, so the unsynthesized set is computable by comparing that list against
the `retros/` directory.
Dictated wording: none.

### RS-4 — accept
Finding: a prompt for standing preferences repeated across sessions exists
nowhere governed (the 08-05 board's AI-15, disposed superseded — see PR #269's
dispositions file, retros/board-dispositions-20260831T213000Z.md).
Resolution: add to the retro procedure a prompt that surfaces standing
preferences Dave has repeated across sessions, held separate from in-session
corrections, as candidate standing rules.
Dictated wording: none.

### RS-5 — accept
Finding: three retro triggers exist in practice — Dave says retro; the Chief
of Staff proposes rotation; end of chat — and the skill states only part of
this.
Resolution: state the three triggers as this one skill's "Use when" set, so
all three routes run the same procedure.
Dictated wording: none.

## Deferred / out of scope

- The Context Quality Reviewer gate over this revision — a later directive
  from the decision session; tracked by the cycle itself.
- Every other cycle the 2026-08-31 rulings opened — tracked in OPEN-ITEMS.md,
  "Topic walk 2026-08-31 — rulings".

## Execution notes

- Edit skills/conversation-retro.md only. The content edit flips
  status: in-review and last-reviewed: null in the same commit, per the
  document metadata policy's revision lifecycle.
- Leave the document conformant to docs/global-context/review-rubric.md and to
  LEXICON.md (the touch rule); the Context Quality Reviewer gates the result
  in a later directive.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
580d171c24348825d9c478365e7037684e47c13c. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- skills/conversation-retro.md @ 62f2fa6c1e278f0b75894e23b4e44fa374e2efbc
- OPEN-ITEMS.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b
- retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- policies/document-metadata-policy.md @ 1d6213baf82bd2a9eeb4c10e9dc9b8fb78025390

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
   "$TMPDIR/fiducial-retro-skill-cycle-1-frontmatter.log", exit status
   reported.
2. Read the revised document once against each of the five Decisions entries
   and state, per entry, where its change landed (section or line), labelled
   observed.

STOP CONDITIONS

Pinned to the reviewed ref 580d171c24348825d9c478365e7037684e47c13c. Cannot execute as written: stop
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

    Retro-skill cycle 1 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
