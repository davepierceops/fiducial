# Remote-write verification policy cycle 8 — Editor revision Directive

Date: 2026-09-02
Documents in scope:
- policies/remote-write-verification-policy.md @ 5f747c63a79788496cb513688dc8a95c7b38b277

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/remote-write-verification-policy-cycle-8-editor-directive.md, commit it alone with a
message naming the cycle it opens, push with git push origin remote-write-cycle-8 (no -u), verify by git ls-remote origin remote-write-cycle-8, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-remote-write-cycle-8", created by: git worktree add --no-track "$TMPDIR/fiducial-remote-write-cycle-8" -b remote-write-cycle-8 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch remote-write-cycle-8, if a branch of that name already exists locally or on origin (git ls-remote origin remote-write-cycle-8 returns a ref), or if "$TMPDIR/fiducial-remote-write-cycle-8" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening the cycle, not a findings disposition: no
review artifact precedes it. Each entry below is a ruled change (told — Dave's
rulings, recorded in OPEN-ITEMS.md @ 457aca1afdadaba99a1446434841ad3995a2407e,
"Topic walk 2026-08-31 — rulings" item 2, and the two entries "MCP write
verification must cover content, not just landing" and "Write-verification
covers landing, not content"; and in
retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203,
topics T07, T11, T30). Intent is binding; wording is the Editor's — no wording
is dictated. A full Context Quality Reviewer gate follows this revision in a
later directive. The policy keeps its present shape — numbered rules under "The
rules" — and the new rules take the next numbers.

### RW-1 — accept
Finding: the policy's three rules verify that a write landed and none verifies
that what landed is what was intended; the policy says so in its Known gap.
Resolution: add the content-expectation check as a rule: after any tool-mediated
write, compare the response's size field against the expected size of what was
sent, and read the landed commit's stats (files changed, insertions, deletions)
against the expected blast radius before reporting the write; a mismatch on
either is reported as a failed write whatever the response said. Remove the
Known gap section, since this rule closes it; carry its incident (the ~64KB file
replaced by 19 bytes) into the rule as the example.
Dictated wording: none.

### RW-2 — accept
Finding: an existing governed document has been regenerated whole over the
connector, which is where the placeholder-content incident came from and where
the largest silent-corruption risk lives.
Resolution: state as a rule that connector writes are creates or small verified
diffs — an existing governed document is never regenerated whole over the
connector; a change too large for a small verified diff goes to an execution
session against a working tree.
Dictated wording: none.

### RW-3 — accept
Finding: connector writes bypass the pre-commit hook, so an in-scope file
written over the connector can land with wrong or missing frontmatter and no
flip.
Resolution: state as a rule that any connector write of a file in the document
metadata policy's in-scope set sets every frontmatter field explicitly, and that
an execution session runs bin/check-frontmatter --all on the branch before the
pull request merges. Cite the document metadata policy for the in-scope set
rather than restating it.
Dictated wording: none.

### RW-4 — accept
Finding: after a timeout on a write, a blind re-create has produced duplicate
pull requests and duplicate commits.
Resolution: state as a rule that after a timeout or an unconfirmable response
on any write, the writer reads the pull request or commit state before
re-creating anything; the re-create is conditional on what the read shows. This
is the per-write procedure that rule 2's two-failure detector counts.
Dictated wording: none.

### RW-5 — accept
Finding: a reported tool failure is a claim by the session that reports it, not
telemetry, and remedies have been chosen before the failure was classified.
Resolution: state as a rule that a reported tool failure is classified before
any remedy — lost response (the write may have landed), never dispatched (it
did not), caller error (malformed call, wrong path or ref), or tool defect —
and that the remedy follows the class. Relate it to rule 2's qualifying and
non-qualifying lists rather than duplicating them: the classes name what rule 2
counts and what it does not.
Dictated wording: none.

## Deferred / out of scope

- The Context Quality Reviewer gate over this revision — a later directive
  from the decision session; tracked by the cycle itself.
- Closing the two OPEN-ITEMS entries this cycle folds in — the decision
  session's flush after the cycle lands; the Editor does not edit OPEN-ITEMS.md.
- Promotion of the write-verification principle into the always-loaded layer
  — the OPEN-ITEMS entry "Promote the write-verification principle into
  context-sets/base.md"; docs/global-context/core.md rule 12 already carries
  the short form, and whether more is owed is not this cycle's question.
- A tooling-facts artifact (T30's AI-8) — open, tracked in the retro synthesis;
  not this document.

## Execution notes

- Edit policies/remote-write-verification-policy.md only. The content edit
  flips status: in-review and last-reviewed: null in the same commit, per the
  document metadata policy's revision lifecycle.
- Leave the document conformant to docs/global-context/review-rubric.md and to
  LEXICON.md (the touch rule); the Context Quality Reviewer gates the result
  in a later directive.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin remote-write-cycle-8 — no -u; the sandbox refuses
  the .git/config write. Process substitution (<(...)) is refused by the
  sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-remote-write-cycle-8" (no
  --force). If it fails, report the failure; do not retry. Your report's final
  line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
49350e0c15a2c05b5705647b6f5d8e7f8568dfa2. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/remote-write-verification-policy.md @ 5f747c63a79788496cb513688dc8a95c7b38b277
- OPEN-ITEMS.md @ 457aca1afdadaba99a1446434841ad3995a2407e
- retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203
- reviews/remote-write-verification-policy-cycle-7.md @ 8e3b95ad622e256e6abc80f5bbeb370ed14616f1
- docs/global-context/core.md @ 941d7f2482fa260f42147ab52647d813bac17e16
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5
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
   "$TMPDIR/fiducial-remote-write-cycle-8-frontmatter.log", exit status
   reported.
2. Read the revised document once against each of the five Decisions entries
   and state, per entry, where its change landed (section or rule number),
   labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref 49350e0c15a2c05b5705647b6f5d8e7f8568dfa2. Cannot execute as written: stop
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

    Remote-write verification policy cycle 8 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
