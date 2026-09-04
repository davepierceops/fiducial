# document-metadata-policy cycle 21 — Editor revision Directive

Date: 2026-09-04
Documents in scope:
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/document-metadata-policy-cycle-21-directive.md, commit it alone with a
message naming the cycle it opens, push with git push origin document-metadata-policy-cycle-21 (no -u), verify by git ls-remote origin document-metadata-policy-cycle-21, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-document-metadata-policy-cycle-21", created by: git worktree add --no-track "$TMPDIR/fiducial-document-metadata-policy-cycle-21" -b document-metadata-policy-cycle-21 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch document-metadata-policy-cycle-21, if a branch of that name already exists locally or on origin (git ls-remote origin document-metadata-policy-cycle-21 returns a ref), or if "$TMPDIR/fiducial-document-metadata-policy-cycle-21" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening cycle 21 of policies/document-metadata-policy.md,
not a findings disposition. The document is in-review at main: pull request #294
removed its enforcement-precedes-use sentence and the hook flipped it. It is a gate
document (its own condition 3 list names it), so it returns to agreed only through a
full cycle; a Context Quality Reviewer gate follows in a later directive. Four items
are listed below, and four is the count. Every item is a fold-in recorded in
OPEN-ITEMS.md (told — the tracker at the revision the COMPANIONS region names);
wording is dictated where the resolution says so. Line numbers are at
dda60a262c6eb775632ae5fefcf18fbe02d9add5 (observed).

### DMP21-1 — accept (converging: the absent-key reading)
Finding: line 82 reads "`status: converging` requires no `last-reviewed`." The
sentence admits two readings — the key is not required, or the key must be absent.
Enforcement takes the first: validate() in bin/aimeta/frontmatter.py (observed at
the revision COMPANIONS names) raises missing-last-reviewed for every status except
converging when the key is absent, and accepts null on any status. The tracker
records this as the one reading to confirm at this cycle.
Resolution: replace the sentence at line 82 with the dictated wording. Nothing else
on that bullet changes.
Dictated wording: `status: converging` does not require `last-reviewed`; the key may be absent or carry `null`.

### DMP21-2 — accept (doc-only Sequence: multi-commit revision, cycle-12 N1)
Finding: the doc-only `### Sequence` (lines 268-279) imports two of the expedited
path's condition-1 clauses — exactly one in-scope document, no other tracked path —
and is silent on the third, single-commit. The path carries a document of any size,
so a multi-commit content revision is expected, and the text does not say which
commit `last-reviewed` and the log entry name.
Resolution: replace the sentence at lines 271-273 beginning "One difference:" with
the dictated wording. The paragraph at lines 275-279 is handled under DMP21-3.
Dictated wording: Two differences: a new document's content commit lands it at `draft`, where an edit to an already-agreed document flips it to `in-review`; and the content revision may span several commits, because this path carries a document of any size — the log entry and `last-reviewed` then name the final content commit, and every content commit touches only that document.

### DMP21-3 — accept (doc-only: promote the single-document rule, cycle-12 N3)
Finding: the single-document rule is stated under `### Sequence` (lines 275-279),
not among the eligibility conditions, though it is eligibility-shaped: it decides
whether an agreement may use the path at all.
Resolution: add a sixth numbered condition after condition 5 (line 260), with the
dictated wording; change the heading at line 240 to "### Eligible when all six
hold"; change "The five conditions" at line 265 to "The six conditions" (the
sentence itself is rewritten under DMP21-4 — apply both there); and cut the first
sentence of the paragraph at lines 275-279 ("A doc-only agreement covers ...
sequential agreements."), leaving the companion-path sentence that follows it as
the paragraph. "The five conditions" at line 201 is the expedited path's own count
and stays five. Then sweep the whole document for any other statement of the
doc-only condition count (Core 13) and report what you find, labelled observed.
Dictated wording: 6. **One document.** The agreement covers exactly one in-scope document, as the expedited path's condition 1 does; several documents co-authored in one session are agreed as separate, sequential agreements.

### DMP21-4 — accept (the retro-skill cross-reference, CR5-3 and the #273 rider)
Finding: lines 201-202 read "A document may exclude its own revisions from this
path, and the retro skill does." That is false at skills/conversation-retro.md
(observed at the revision COMPANIONS names): its lines 18-20 exclude any
methodology revision a retro or a synthesis surfaces from every lighter path, not
this skill's own revisions; what binds that skill's own revisions to the full cycle
is this policy's condition 3 list, at line 180. The doc-only counterpart at lines
265-266 carries the same "may exclude its own revisions" clause without the
example, and the #273 rider asks that the two sentences be brought into line.
Resolution: replace the two sentences at lines 201-202 with the first dictated
wording; replace the sentence at lines 265-266 (from "The five conditions" to "from
this path.") with the second. Neither edit touches skills/conversation-retro.md.
Dictated wording (expedited, lines 201-202): The five conditions are necessary, not sufficient. Condition 3's class is this policy's own exclusion; a document may exclude a further class of revisions from this path, and skills/conversation-retro.md does — any methodology revision a retro or a synthesis surfaces takes the full cycle, whatever lighter path it would otherwise be eligible for.
Dictated wording (doc-only, lines 265-266): The six conditions are necessary, not sufficient, here as on the expedited path, and the same further exclusions reach this path: skills/conversation-retro.md's, and any other a document states.

## Deferred / out of scope

- The Context Quality Reviewer gate over the revised document — a later directive
  from the decision session; artifact reviews/document-metadata-policy-cycle-21.md.
  Two one-line checks travel to that gate, not to this revision: the
  expedited-stretch check (OPEN-ITEMS.md, "Topic walk 2026-08-31 — rulings", item 9:
  confirm conditions 2 and 4 as written now foreclose the 1,400-line TRD agreement
  the 2026-08-24 retro records), and whether enforcement admitting a well-formed
  `last-reviewed` pointer on a converging document (validate() does) needs a
  policy sentence.
- DMP20-1 (reviews/document-metadata-policy-cycle-20.md) — a bin/tests change;
  landed (observed at main: no `prose-criteria.md` that is not
  `public-prose-criteria.md` remains in bin/tests/test_bundle_audience.py). Nothing
  to do here.
- The cycle-20 "Dave should inspect" note on the suite's accepted-red baseline —
  not this document's; stays in OPEN-ITEMS.md.
- bin/aimeta/expedited.py path-blindness (OPEN-ITEMS.md entry) — unchanged by this
  revision; the single-document rule it relies on is promoted, not altered.
- skills/conversation-retro.md — read for lines 18-20 only; do not edit it.

## Execution notes

- One content commit after the directive's own commit, touching
  policies/document-metadata-policy.md only. The document is already in-review with
  last-reviewed null; the pre-commit hook leaves both as they are — never bypass it.
- Apply the four items in the order given; DMP21-3 and DMP21-4 both touch line 265
  — the final text of that sentence is DMP21-4's second dictated wording.
- Dictated wording is used verbatim. Wrap prose at the column the surrounding text
  uses; a numbered condition follows the indentation of conditions 1-5.
- Nothing else in the file changes. The Lexicon touch rule applies; if it would
  require a further edit, stop and report rather than make it.
- Inner fences in this directive are ~~~ so it travels inside one paste block;
  write them to the file as they are.
- Write citations bare — no backticks or quotes around a path in a path @ sha
  citation.
- Push with git push origin document-metadata-policy-cycle-21 — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by the
  sandbox; use temp files.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-document-metadata-policy-cycle-21"
  (no --force). If it fails, report the failure; do not retry. Your report's
  final line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
06d3ba53f94665a721615ec1f5254fe4d46ad95a. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5
- reviews/document-metadata-policy-cycle-20.md @ 3aa12a53e5cd5c134b54c4f77325f306c4d12ece — the prior cycle's record; read for context, nothing in it is re-opened here.
- OPEN-ITEMS.md @ 56060d52a644c137d944e474d5a93e19e4d810ed — two entries only: "document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)", and the bin/ package paragraph in "Queued next" that ends "the Test Designer's reading of "requires no last-reviewed"".
- skills/conversation-retro.md @ abd7c9cde0b71b3639edda22b8e5e2c062514cee — lines 18-20 only.
- bin/aimeta/frontmatter.py @ 2e23b8445f10fb0ee680192e856af63da954ea65 — validate(), the last-reviewed branch only.
- LEXICON.md @ e4e62cc6375934c34e13f8ff15545f6f42185b41 — the touch rule.

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
   "$TMPDIR/fiducial-document-metadata-policy-cycle-21-frontmatter.log", exit
   status reported (expected 0).
2. grep -n "five\|six" policies/document-metadata-policy.md in the worktree, output
   captured to "$TMPDIR/fiducial-document-metadata-policy-cycle-21-grep.log";
   expected: "five" appears only in the expedited path's sentence, "six" in the
   doc-only heading and the doc-only sentence — state every hit, labelled observed.
3. grep -n "retro skill" policies/document-metadata-policy.md in the worktree;
   expected zero matches; state the count, labelled observed.
4. git diff --stat of the content commit: exactly one file; state it, labelled
   observed. Then git show of that commit, read whole: confirm each dictated
   wording appears verbatim and that no hunk falls outside the seven locations the
   four items name (lines 82, 201-202, 240, the insertion after 260, 265-266,
   271-273, 275-279 at the reviewed ref) — state the hunk count, labelled observed.
5. head -5 of the document in the worktree: status in-review, last-reviewed null,
   audience unchanged; state each, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref 06d3ba53f94665a721615ec1f5254fe4d46ad95a. Cannot execute as written: stop
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

    document-metadata-policy cycle 21 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
