# Flush 2026-09-01 — rulings to the log and OPEN-ITEMS Directive

Date: 2026-09-02
Documents in scope:
- OPEN-ITEMS.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b
- decisions/log.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b

ROUTE AND MODEL

Route: fresh
Model: solid

FIRST ACT

Write this directive verbatim to docs/cycles/open-items-flush-20260902T035739Z-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-flush-20260902", created by: git worktree add --no-track "$TMPDIR/fiducial-flush-20260902" -b open-items-flush-20260902 origin/main

## Decisions

All content below is ruled by Dave, 2026-09-01, in the decision session
(retro-skill cycle close, bundle-system PRD human review, Decision Layer
human review). This directive lands the record; it decides nothing.

### FL-1 — accept: four decision-log entries, dictated verbatim
Resolution: append to decisions/log.md, after the last entry, exactly:

    ## DEC-000310 — A retro runs when Dave asks, not by default
    Date: 2026-09-01
    Decision: A retrospective runs only when Dave asks for one. There is no
    standing end-of-session obligation, no skip condition (nothing is owed
    by default), and no baton-before-retro ordering rule.
    Context: Owner decision (Dave), 2026-09-01, Decision Layer human
    review; Decision Layer rule 12 rewritten accordingly, agreed at
    cycle 15 (reviews/decision-layer-cycle-15.md; reviewed document SHA
    999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec).
    skills/conversation-retro.md still encodes the prior obligation; its
    conforming revision is queued as a full cycle.

    ## DEC-000320 — Bundle filename and header: ruled form; DEC-000210's carried form retired
    Date: 2026-09-01
    Decision: A generated bundle is named
    fiducial-bundle-<audience>-<timestamp>, timestamp per DEC-000290,
    delivered per DEC-000200. The header keeps the tool's present fields —
    repository, HEAD SHA, generation time, numbered member list with
    per-file blob SHAs, per-member markers. Hand-built and generated
    bundles are interchangeable under this form. DEC-000210's
    carried-forward filename and Source-line form is retired; the losing
    form's removal lands in the bundle-system PRD's header package.
    Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
    review, resolving the PRD's OQ-5. Recorded in specs/bundle-system.md
    at the review's landing (pull request #275).
    Supersedes: DEC-000210 (carried-forward filename and header clause only)

    ## DEC-000330 — Releases: every audience, whole, at one HEAD; event-driven; go is Dave's
    Date: 2026-09-01
    Decision: A release re-produces every audience's bundle, regenerated
    whole at the release's SHA — untouched audiences included, so every
    asset states the same SHA; release notes name the audiences whose
    member set or content changed. Cadence is event-driven, no calendar:
    when a default-branch commit changes any bundle member, the decision
    session tells Dave a release is owed, and it is cut on his explicit
    go. The go is Dave's; the decision session owns mechanics and
    verification (generate, cut, attach, notes, read-back confirming every
    asset's SHA); a release found wrong returns to Dave as a triage item,
    never a silent fix.
    Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
    review, resolving the PRD's OQ-6 whole.

    ## DEC-000340 — skills/outline.md audience: writer alone
    Date: 2026-09-01
    Decision: skills/outline.md is audience [writer]; the human value comes
    off in the bundle-system tagging package. A human does not need the
    outline skill.
    Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
    review, resolving the PRD's OQ-10.

Dictated wording: the four entries above, verbatim, indentation removed
(they are indented here only to survive this directive's formatting).

### FL-2 — accept: OPEN-ITEMS corrections and closures
Resolution: in OPEN-ITEMS.md, with wording the executor's where not quoted:
1. Follow-up 1: change "four changes" to "five changes"; append to the
   entry: "LANDED 2026-09-01 — agreed at cycle 4,
   reviews/conversation-retro-cycle-4.md."
2. The "Owned elsewhere" line reading "AI-15 -> landed via T17": correct to
   superseded, citing pull request #269's body as the ruling and noting the
   standing-preferences half landed 2026-09-01 via the retro-skill cycle.
3. Topic-walk ruling 1 (Decision Layer cycle): append "LANDED 2026-09-01 —
   human review with Dave; agreed at cycle 15
   (reviews/decision-layer-cycle-15.md; reviewed document SHA
   999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec).
   Rider for the next Decision Layer cycle: cycle 14's DL-2, the pane named
   inconsistently across documents. Follow-ups 3, 4, 5, and 11 closed."
4. The "Queued next" queue: mark items 1 (retro-skill cycle) and 5
   (Decision Layer cycle) done with the dates and artifacts above; annotate
   item 2 (bundle PRD): "PRD human-reviewed 2026-09-01 (pull request #275);
   OQ-5, OQ-6, OQ-10 resolved in-document; Spec Reviewer gate still owed."

### FL-3 — accept: new riders and queue entries
Resolution: add, each where its pile already lives in OPEN-ITEMS.md:
1. Directive-authoring pile: "Cycle-number derivation: the artifact cycle
   number comes from a full, version-sorted listing of reviews/ (never
   sort|tail on lexical names), and the directive instructs the executor to
   confirm the artifact path absent at the base before writing. Two
   instances 2026-09-01: conversation-retro cycle 3, decision-layer cycle
   14 — both stopped by the executor, neither reached a record."
2. specs/directive-tooling-trd.md rider queue: "Candidate M-rule: a
   dictated artifact path must not exist at the base ref — mechanical,
   would have caught both 2026-09-01 instances." And: "M5 false positive:
   a slashless root-level path in Documents in scope (OPEN-ITEMS.md) is
   misread as a companion marker preceding FIRST ACT and fails
   first-act-missing; observed 2026-09-01 on this flush directive, in
   both scope-line orders. Classified, not worked around, per the M2
   precedent."
3. Tooling-facts pile (follow-up 12): "git push -u in the executor sandbox
   lands the ref, then fails only the upstream-config write
   (.git/config: Operation not permitted); push without -u." And:
   "Connector whole-file writes drift when content is retyped: precompute
   the target blob locally and compare after the write; one caught
   instance 2026-09-01 (a one-word regression, corrected before merge)."
4. Spec Reviewer queue: "directive-tooling TRD lines ~808-810 quote old
   Decision Layer rule 14 verbatim — the TRD's own B3/G6 defect class
   (cycle 14's DL-4)."
5. Queued cycles: "skills/conversation-retro.md conforming revision —
   drop the chat-close auto-run and the rule-12 standing-obligation
   deference, per DEC-000310; full cycle, ineligible list."

## Deferred / out of scope

- The six unlogged decisions from the 15-hour session — reconstruction
  still owed; their OPEN-ITEMS entry stands untouched.
- Every queued cycle named above — later directives.

## Execution notes

- Touch only OPEN-ITEMS.md and decisions/log.md; one commit carrying both,
  after the directive's own commit.
- decisions/log.md is append-only: add the four entries at the end; edit
  nothing above them. Before appending, read the last entry's ID and
  confirm it is DEC-000300; if it is not, stop and report.
- The trailing prose note in the log about the six unwritten decisions
  stays where it is; append after it.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin open-items-flush-20260902, without -u.
- Do not open a pull request; the decision session opens it.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
c49d37696827b884f19a482ecee58fd0e8f82066. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b
- decisions/log.md @ 0556912f6d4e9b48be0dfd4a81c408243c1e038b
- reviews/decision-layer-cycle-15.md @ 1fae380a41931d0efa5d5516c4f1c0788bbf514e
- reviews/conversation-retro-cycle-4.md @ 30a9a938835e4f3a7d0d24e3eca3b9bf862de03b

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

1. grep -c "^## DEC-" decisions/log.md before and after the append; after
   equals before plus four. The four new IDs are DEC-000310, DEC-000320,
   DEC-000330, DEC-000340, confirmed present by grep. Output captured to
   "$TMPDIR/fiducial-flush-20260902-verify.log".
2. bin/check-frontmatter --all, exit status reported, captured beside it.
3. git diff origin/main --stat: exactly OPEN-ITEMS.md, decisions/log.md,
   and this directive file.

STOP CONDITIONS

Pinned to the reviewed ref c49d37696827b884f19a482ecee58fd0e8f82066. Cannot execute as written: stop
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

    Flush 2026-09-01 — rulings to the log and OPEN-ITEMS Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
