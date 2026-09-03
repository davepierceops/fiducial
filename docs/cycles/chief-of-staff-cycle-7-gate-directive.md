# Chief of Staff role cycle 7 — Context Quality Reviewer gate Directive

Date: 2026-09-02
Documents in scope:
- roles/chief-of-staff.md @ 00bdd4648f8e0efdc687886b341c1ef71b259393
- context-sets/spec-and-change-discipline.md @ 0c1a51dcede20c823c4cea85796fb362cfb9f2a8

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/chief-of-staff-cycle-7-gate-directive.md, commit it alone with a
message naming the gate it opens, push with git push origin chief-of-staff-cycle-7-gate (no -u), verify by git ls-remote origin chief-of-staff-cycle-7-gate, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-chief-of-staff-cycle-7-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-chief-of-staff-cycle-7-gate" -b chief-of-staff-cycle-7-gate origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch chief-of-staff-cycle-7-gate, if a branch of that name already exists locally or on origin (git ls-remote origin chief-of-staff-cycle-7-gate returns a ref), or if "$TMPDIR/fiducial-chief-of-staff-cycle-7-gate" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens the review, not a re-gate.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored nothing
under review (the Editor revision was a different session; this directive's
author drafted neither document nor revision). One gate over two documents,
one artifact: full-depth review of
roles/chief-of-staff.md @ 00bdd4648f8e0efdc687886b341c1ef71b259393 and of
context-sets/spec-and-change-discipline.md @ 0c1a51dcede20c823c4cea85796fb362cfb9f2a8
against docs/global-context/review-rubric.md and LEXICON.md conformance,
including whether the ruled changes recorded in
docs/cycles/chief-of-staff-cycle-7-editor-directive.md (CS-1 through CS-6 for
the role; SD-1 for the context set) are faithfully realized. Intent was
binding, wording was the Editor's; a wording choice is not a finding unless it
breaks a rubric criterion, the lexicon, or a ruled intent. One Editor-flagged
item (told — the Editor's report): CS-3 and CS-4 cite the remote-write policy
and the Decision Layer by document name and rule number, not by path, under
rubric criterion 3; rule on it as a finding or a non-finding. Cross-checks in
scope: the role's new connector, baton and rotation text against
docs/global-context/decision-layer.md rules 12 and 13 and against
policies/remote-write-verification-policy.md rules 2, 6 and 7, for
contradiction or restatement; the role's pending-gates enumeration against
policies/document-metadata-policy.md's revision lifecycle for the converging
exit gate; and the context set's red-gate paragraph against operating-model.md
stages 3, 6 and 7 and roles/test-designer-agent.md, for whether the two
contract sources and their stages agree with the flow as written. Finding ids
continue reviews/converging-model-cycle-2.md's sequence where they touch N-6
or N-7, so a later citation stays unambiguous; new findings take this cycle's
own prefix.

LOOP START (told — the decision session's statement, Dave's to override): the
agreement bar for this cycle is a verdict of ready or ready-with-findings with
zero blocking findings, per document; cadence is one full-depth gate (this
directive), then a fix directive if findings warrant one, then one
confirmation-scoped re-gate over the fix, then the flips — two, one per
document, each citing this artifact at its own reviewed SHA.

ARTIFACT. Produce reviews/chief-of-staff-cycle-7.md per
skills/review-artifact.md, verdict first, its Reviewed: line listing both
documents each at its SHA above, and stating in its own scope that it reviewed
each at that SHA. Before writing it, confirm the path is absent at the base
ref (git cat-file -e ff1a9decba21d3b07d5c3427eff4d198fe41f102:reviews/chief-of-staff-cycle-7.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to either reviewed document or any governed file.

## Deferred / out of scope

- Findings triage, any resulting fix directive, the re-gate, and the two
  agreement flips — the decision session's next steps after this report;
  tracked by the cycle.
- The decision-log entry for the N-6 ruling — the flush.
- The autonomous-run skill (T23's second half) and bin/state — not this cycle.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin chief-of-staff-cycle-7-gate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files. Heredoc-fed while-read loops have lost PATH in
  this sandbox (told — the Editor's report); use flat commands.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-chief-of-staff-cycle-7-gate"
  (no --force). If it fails, report the failure; do not retry. Your report's
  final line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
ff1a9decba21d3b07d5c3427eff4d198fe41f102. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- roles/chief-of-staff.md @ 00bdd4648f8e0efdc687886b341c1ef71b259393
- context-sets/spec-and-change-discipline.md @ 0c1a51dcede20c823c4cea85796fb362cfb9f2a8
- docs/cycles/chief-of-staff-cycle-7-editor-directive.md @ 94ed5d0f9e3c394fe613e9fea760cd7dee3fd092
- reviews/converging-model-cycle-2.md @ 01c29474ee4d6be7c8c387c348de28321c7ec9bb
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
- skills/review-artifact.md @ 7b52f6ba0e50f6987993fc29e465dbab6e8d25b8
- skills/spec-review-cycle.md @ 0911b06042f62aabb5de9d5fa49547e93b1eeed8
- docs/global-context/review-rubric.md @ fda7970ece0f0cc4d8f0fdadf2185194444f677d
- docs/global-context/decision-layer.md @ 0129260877703b3b0b13045de1726c20040c8ec9
- policies/remote-write-verification-policy.md @ 2a14bcc1b7f5092d2c991abc9e044a3b07298912
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5
- operating-model.md @ 2fbb092b2544475021c2a4e7a9c68c4ddcb9d727
- roles/test-designer-agent.md @ d66f36f25c30eb8b12808921ec518e47ba2a4cbc
- roles/spec-reviewer-agent.md @ e4110f0cc3e47a245a51289b9aa00639ccf05fdb
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
   "$TMPDIR/fiducial-chief-of-staff-cycle-7-gate-frontmatter.log", exit status
   reported.
2. The artifact's header states both reviewed documents at the SHAs above,
   and its verdict line is first; state all three, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref ff1a9decba21d3b07d5c3427eff4d198fe41f102. Cannot execute as written: stop
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

    Chief of Staff role cycle 7 — Context Quality Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
