# Flush 2026-09-02c — converging model landed, queue updates, riders Directive

Date: 2026-09-02
Documents in scope:
- OPEN-ITEMS.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0

ROUTE AND MODEL

Route: fresh
Model: solid

FIRST ACT

Write this directive verbatim to docs/cycles/open-items-flush-20260902c-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-open-items-flush-20260902c", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush-20260902c" -b open-items-flush-20260902c origin/main

## Decisions

All content below is ruled by Dave in the decision session (2026-09-02:
spec-review-cycle cycle 11 triage; the converging-model branch, cycles 1–2;
agreement and nine flips at pull request #292). This directive lands the
record in OPEN-ITEMS.md; it decides nothing. DEC-000360 already sits in
decisions/log.md (pull request #287); no log entry is owed here.

### FL-1 — accept: closures
Resolution, in OPEN-ITEMS.md, wording the executor's where not quoted:
1. "Convergence process — canonization owed": strike the heading and
   prepend "**RESOLVED** 2026-09-02 by DEC-000360 and the converging-model
   branch (pull requests #287–#292): convergence is the standard change
   flow with a named status, converging; written into operating-model.md,
   skills/spec-review-cycle.md, policies/document-metadata-policy.md,
   roles/test-designer-agent.md, roles/chief-of-staff.md,
   roles/spec-reviewer-agent.md, LEXICON.md,
   context-sets/spec-and-change-discipline.md, skills/review-artifact.md;
   all nine agreed at reviews/converging-model-cycle-2.md."
2. Topic walk ruling 3 (spec-review-cycle skill cycle) and follow-up 6:
   append "LANDED 2026-09-02 — cycle 11 (reviews/spec-review-cycle-cycle-11.md)
   closed into the converging-model branch; agreed at
   reviews/converging-model-cycle-2.md, reviewed document SHA
   0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e."
3. "Queued next" line: mark the spec-review cycle DONE with the pointer in
   item 2.
4. "Review artifact schema — third-use feedback" item 4 (Baseline:):
   append "LANDED 2026-09-02 in skills/review-artifact.md (converging-model
   CM-5)."

### FL-2 — accept: new queued entries
Resolution: add, beside the other queued cycles:
1. "bin/ package — enforce the converging status (DEC-000360 precondition:
   lands before any document enters converging). ACs: bin/aimeta/frontmatter.py
   STATUSES admits converging; bin/migrate-frontmatter STATUS_MAP likewise;
   the pre-commit hook does not flip a converging document on a content
   edit; bin/flip-agreed accepts converging as a source status for
   --status agreed and as a --status target for the entry transition from
   in-review; status: converging requires no last-reviewed; tests red then
   green; the package removes the policy sentence 'enforcement lands as a
   bin/ change before any document enters it' (reviews/converging-model-cycle-1.md
   O-3) in the same change. Test Designer and Coder separate."
2. "Converging follow-up cycle — context-sets/spec-and-change-discipline.md
   and roles/chief-of-staff.md (reviews/converging-model-cycle-2.md N-6,
   N-7): N-6, the convergence suite's interface-contract source — the
   discipline still says 'from the architecture summary', which is now
   stage 6; Dave rules the source (candidate: the TRD's interface list).
   N-7, the Chief of Staff pending-gates read lists in-review and omits
   converging, which owes an exit gate."

### FL-3 — accept: riders
Resolution: append each to the named existing entry or queue:
1. specs/bin-land-trd.md untriaged-findings entry (Corpus defects carried
   from prior batons): "Rider: line ~1536 cites the retired per-task
   confirmation as the metadata policy's build-gating rule; restate under
   the three-valued rule (reviews/converging-model-cycle-1.md N-4)."
2. "Review artifact schema" entry: "O-4 (reviews/converging-model-cycle-1.md):
   the multi-document branch gate is a third range form; the Reviewed
   line carries a commit plus several documents and the schema does not
   describe it; name the form at the schema's next cycle."
3. skills/conversation-retro.md conforming revision (Queued next line):
   "Rider from pull request #273: the skill's 'routes' reuses the
   Lexicon's directive-sense term in another sense; conform."
4. policies/document-metadata-policy.md — add a rider line to the
   "document-metadata-policy.md doc-only cycle — advisory clarity items"
   entry: "Rider from pull request #273: the doc-only path sentence (near
   'A doc-only agreement covers exactly one in-scope document') lacks the
   F-10 clause the expedited path's sentence carries; fold in with F-10
   at the policy's next cycle."
5. specs/directive-tooling-trd.md rider queue: "M5 false positive
   (slashless root-level path in Documents in scope read as a companion
   marker) fired on five of this session's directives, 2026-09-02;
   M2's flip-pointer false positive (artifact @ reviewed-document SHA)
   fired on the nine-flip directive. Both classified, not worked around."
6. skills/directive-authoring.md next cycle (topic-walk item 5):
   "The invariants skeleton emits no Cleanup region; worktree removal is
   an author-region obligation and one 2026-09-02 directive omitted it,
   leaving $TMPDIR/fiducial-converging-model-fix-2 on disk. Candidate:
   a committed Cleanup region in skills/directive-invariants.md."
7. Executor self-recovery entry: "2026-09-02: a Sonnet 5 executor reported
   the clone's main tree, behind origin/main, as 'ahead'; harmless,
   recorded as a claim-labelling miss."

## Deferred / out of scope

- Every queued cycle and package named above — later directives.
- The six unlogged decisions from the 15-hour session — reconstruction
  still owed; their entry stands untouched.

## Execution notes

- Touch only OPEN-ITEMS.md; one commit after the directive's own commit.
  Update its "Last updated" line to 2026-09-02.
- Where an instruction names an anchor that does not exist in the file,
  stop and report rather than guess a placement.
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin open-items-flush-20260902c — no -u; the sandbox refuses the
  .git/config write.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed, remove your
  own worktree from the main tree: git worktree remove "$TMPDIR/fiducial-open-items-flush-20260902c"
  (no --force). Report the result as the final line.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
f90a6d4ac2d5485ad934a9baec0b3dc39b7de8e9. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- OPEN-ITEMS.md @ f56ec0a85ad8e797c682f5655af637edd96d95c0
- decisions/log.md @ 15b1a874c6fdb1cbbebe89ce149ab81409a3acd5
- reviews/converging-model-cycle-1.md @ f16df8b55e77e470d6592d3b07327e5e044f4047
- reviews/converging-model-cycle-2.md @ 01c29474ee4d6be7c8c387c348de28321c7ec9bb
- reviews/spec-review-cycle-cycle-11.md @ d66a89333f85682f69f7424e60fd91d51cbc30f7

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

Named verification, before the push:

1. bin/check-frontmatter --all, output captured to
   "$TMPDIR/fiducial-open-items-flush-20260902c-frontmatter.log", exit status reported.
2. git diff --stat against the base ref, captured to
   "$TMPDIR/fiducial-open-items-flush-20260902c-diffstat.log"; expected: OPEN-ITEMS.md and this
   directive file only.
3. grep -c "2026-09-02" OPEN-ITEMS.md before and after; state both counts,
   labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref f90a6d4ac2d5485ad934a9baec0b3dc39b7de8e9. Cannot execute as written: stop
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

    Flush 2026-09-02c — converging model landed, queue updates, riders Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
