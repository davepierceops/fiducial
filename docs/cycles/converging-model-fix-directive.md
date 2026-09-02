# Converging model — fix revision (cycle-1 findings) Directive

Date: 2026-09-02
Documents in scope:
- operating-model.md @ 03ece2f57758cfee74b76cc760adda2f19627631
- roles/chief-of-staff.md @ 2d13aea33acb47ab6d89fdf5cfae03fe86eacb2f
- roles/spec-reviewer-agent.md @ a092f4938256503a5d894eeb9c05c5a777b72cde
- skills/spec-review-cycle.md @ 58790b3e14aab0c47ea48c4a577e2d7517d07dc6
- policies/document-metadata-policy.md @ 4129a453b59dd32dedcb5afc6b9512602fd49128
- LEXICON.md @ f93dcf7ad29034b76dfa43d40615071f67d75411

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-fix-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-converging-model-fix", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model-fix" -b converging-model-fix origin/main

## Decisions

Disposes reviews/converging-model-cycle-1.md (N-1 through N-5, O-1 through
O-4) as ruled by Dave in the decision session, 2026-09-02 (told). Two role
documents join the branch here because N-1 and N-3 name them as the losing or
silent text; the re-gate that follows reads those two full-depth and the rest
confirmation-scoped. Intent is binding; wording is the Editor's — no wording
is dictated.

### N-1 — accept: split the per-spec lifecycle from the per-change stages
Finding: the change flow's per-change stages 2–3 now sit inside the
converging interval, and the Chief of Staff role decomposes only from an
agreed spec, so the convergence tests have no admitted source.
Resolution, three documents:
- operating-model.md: restate the change flow as two parts. First, the spec
  lifecycle, once per spec (and again for a revision that re-enters
  converging, per N-2): first gate → converging → the spec's test suite
  written and confirmed red against it → exit gate → agreed. Then the
  per-change stages, each after the spec is agreed: acceptance criteria for
  the unit; architecture summary; the unit's tests selected from the spec's
  suite and confirmed red; implement to green; quality review; skeptic/risk;
  release package; release gate. State plainly that the convergence suite is
  the spec's, not any unit's, and that the per-change stages never run
  against a converging spec. Conform Definition of done and the change
  package where they refer to the old numbering.
- roles/chief-of-staff.md: state that decomposition still requires an agreed
  spec, and add the one act permitted before it — directing a convergence
  directive from a spec that is converging and has cleared its first gate,
  pinning the entry-transition SHA; the Test Designer's convergence work is
  that directive's, not a package's. Conform "Decomposition requires a closed
  delta" so it does not read as forbidding this.
- skills/spec-review-cycle.md: the Convergence section says the suite is the
  spec's and names the convergence directive as the vehicle.
Dictated wording: none.

### N-2 — accept: once per spec; a revision may re-enter converging
Finding: the flow does not say its spec clauses run once; nothing says
whether a revision of an agreed spec may re-enter converging.
Resolution: the once-per-spec statement falls out of N-1's split; state it
in one sentence there. In policies/document-metadata-policy.md, state that a
revision of an agreed spec — flipped to in-review by its edit — may enter
converging under the same entry rule (a gate has run on the revision; Dave's
say; frontmatter-only transition from in-review to converging) and exits the
same way, and that a revision whose tests do not change takes the ordinary
in-review → agreed route. In LEXICON.md, drop "before first agreement" from
the Converging definition and say the interval may recur per revision.
Dictated wording: none.

### N-3 — accept: the exit gate's check over the tests is stated
Finding: the exit gate reviews "the tests" with no stated check; the Spec
Reviewer role is silent on the exit gate.
Resolution: in skills/spec-review-cycle.md, the exit-gate step states that
the gate checks the coherence condition (every testable claim has a test;
every test asserts a stated claim) and that the red-gate result is present
and behavioral, and that test adequacy is not its question — that stays
with quality review. In roles/spec-reviewer-agent.md, add the exit gate as
a third activation, naming what it inspects (the range diff from the entry
transition to the reviewed SHA, plus the tests, against the two checks
above) and what it does not (test adequacy).
Dictated wording: none.

### N-4 — accept as routed; no edit here
Finding: specs/bin-land-trd.md cites the retired per-task confirmation.
Resolution: loose-end tracker entry at the next flush, for the TRD's next
revision; specs/ is outside this branch.
Dictated wording: none.

### N-5 — accept
Finding: trailing justification, policies/document-metadata-policy.md ~82.
Resolution: end the sentence at "last-reviewed".
Dictated wording: none.

### O-1 through O-4 — record only
No edit. O-3 (the enforcement-precedes-use sentence expires) is queued
with the bin/ package; O-4 (multi-document Reviewed line) with the
review-artifact schema queue at the next flush.

## Deferred / out of scope

- The re-gate: confirmation-scoped over operating-model.md,
  skills/spec-review-cycle.md, policies/document-metadata-policy.md, and
  LEXICON.md; full-depth over roles/chief-of-staff.md and
  roles/spec-reviewer-agent.md — a later directive; then nine flips.
- skills/review-artifact.md, roles/test-designer-agent.md, and
  context-sets/spec-and-change-discipline.md are on the branch, carry no
  cycle-1 finding, and are not edited here.
- The bin/ package enforcing converging; the N-4 tracker entry — next flush.

## Execution notes

- Edit only the six documents in scope. One content commit per document, in
  the order operating-model.md, roles/chief-of-staff.md,
  roles/spec-reviewer-agent.md, skills/spec-review-cycle.md,
  policies/document-metadata-policy.md, LEXICON.md. The two role documents
  are agreed at the base: their content commit flips status to in-review and
  last-reviewed to null. The other four are already in-review / null; leave
  their frontmatter as it is.
- A changed fact changes everywhere it appears within these files; name any
  place outside them in the report.
- Leave every edited document conformant to docs/global-context/review-rubric.md
  and to LEXICON.md (the touch rule).
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin converging-model-fix — no -u; the sandbox refuses
  the .git/config write. Process substitution (<(...)) is refused by the
  sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
ccc14f6bdbfbd4bacbdb6b8d243f466b18bbb96d. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- operating-model.md @ 03ece2f57758cfee74b76cc760adda2f19627631
- roles/chief-of-staff.md @ 2d13aea33acb47ab6d89fdf5cfae03fe86eacb2f
- roles/spec-reviewer-agent.md @ a092f4938256503a5d894eeb9c05c5a777b72cde
- skills/spec-review-cycle.md @ 58790b3e14aab0c47ea48c4a577e2d7517d07dc6
- policies/document-metadata-policy.md @ 4129a453b59dd32dedcb5afc6b9512602fd49128
- LEXICON.md @ f93dcf7ad29034b76dfa43d40615071f67d75411
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- context-sets/spec-and-change-discipline.md @ dd86a8a99349324a02bb87c8ab373f937de8f7c3
- reviews/converging-model-cycle-1.md @ f16df8b55e77e470d6592d3b07327e5e044f4047
- docs/cycles/converging-model-editor-directive.md @ 0c84d626d35686d04a039cf2c6fd122ccc6e460f
- decisions/log.md @ 15b1a874c6fdb1cbbebe89ce149ab81409a3acd5
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
   "$TMPDIR/fiducial-converging-model-fix-frontmatter.log", exit status
   reported.
2. Read each revised document once against the findings it disposes and
   state where each change landed (section or line), labelled observed.
3. git diff --stat against the base ref, captured to
   "$TMPDIR/fiducial-converging-model-fix-diffstat.log"; expected: exactly
   the six documents in scope plus this directive file.

STOP CONDITIONS

Pinned to the reviewed ref ccc14f6bdbfbd4bacbdb6b8d243f466b18bbb96d. Cannot execute as written: stop
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

    Converging model — fix revision (cycle-1 findings) Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
