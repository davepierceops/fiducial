# Converging model — cycle 2 re-gate (confirmation-scoped, two full-depth) Directive

Date: 2026-09-02
Documents in scope:
- policies/document-metadata-policy.md @ d96ef65a802fba5735aae432222cab44c976fdc6
- operating-model.md @ bf0fa24d250325f1b63ee138752803288ce34f67
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
- context-sets/spec-and-change-discipline.md @ 468798e83dd076b2f5772faa03e1749b3ead9176
- roles/chief-of-staff.md @ 0685f4d7fb34910e36ca94a51cc1fdf94fa13308
- roles/spec-reviewer-agent.md @ eb15a8bbdd03fdff075bf75539802d2eca3455f5

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/converging-model-regate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-converging-model-regate", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-model-regate" -b converging-model-regate origin/main

## Decisions

A re-gate disposes the findings of the cycle it closes and takes no new
decisions; a new decision, if one is needed, is filed as a finding for the
decision session and opens its own cycle. Nothing is ruled here.

ROLE AND TASK. This session fills one role: Context Quality Reviewer per
roles/context-quality-reviewer.md, independent — this session authored
nothing under review. The review is one artifact with two scopes:

Baseline: 3a511a1e6353428948a923a751423ac47c7f8a8b (main at cycle 1's reviewed ref)
Reviewed: a57ae41204a8d89a81169088c2671ca865c6fb75 (main at the merge of fix 2)

Scope A — confirmation-scoped, over the seven documents cycle 1 reviewed:
read the named resolutions in docs/cycles/converging-model-fix-directive.md
(N-1, N-2, N-3, N-5) and docs/cycles/converging-model-fix-2-directive.md
(F2-1, F2-2), plus the range diff Baseline..Reviewed over these seven
against the governed text each change cites, and confirm three things:
(1) each named resolution landed as ruled; (2) the two executors' disclosed
judgment calls hold against the rubric; (3) the diff introduces no new
contradiction with the governed text it cites. Read nothing else in these
seven; a finding outside this scope is filed only if it is a new blocking
contradiction the diff introduced.

Scope B — full-depth, over the two documents that joined the branch at the
fix: roles/chief-of-staff.md and roles/spec-reviewer-agent.md, whole, at
their reviewed revisions, against docs/global-context/review-rubric.md and
LEXICON.md conformance, and for consistency with the seven — one model, no
two documents disagreeing.

LOOP START (told — the decision session's statement, Dave's to override;
unchanged from cycle 1): the agreement bar is ready or ready-with-findings
with zero blocking findings across the branch; this re-gate is the last
gate of the cadence; the nine flips follow on Dave's go.

ARTIFACT. Produce reviews/converging-model-cycle-2.md per
skills/review-artifact.md at its reviewed revision: stem names the branch;
header carries Baseline: and Reviewed: as above, lists all nine documents
with their SHAs, and states the two scopes and which documents fall under
each; verdict first. Before writing it, confirm the path is absent at the
base ref (git cat-file -e a57ae41204a8d89a81169088c2671ca865c6fb75:reviews/converging-model-cycle-2.md
must fail); if it exists, stop and report. This session creates exactly two
files — this directive file and the review artifact — and modifies nothing.
Review only: no edits to any governed file.

## Deferred / out of scope

- The nine flips by bin/flip-agreed, one invocation per document, citing
  reviews/converging-model-cycle-2.md at the reviewed SHA of each document
  — the decision session's, on Dave's go, after this report.
- The bin/ package enforcing `converging`; the flush carrying N-4, O-3,
  O-4, and the cycle-11 riders.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin converging-model-regate — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed (git ls-remote
  origin converging-model-regate shows the artifact commit), remove your own
  worktree from the main tree: git worktree remove "$TMPDIR/fiducial-converging-model-regate"
  (no --force). Report the result as the final line.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a57ae41204a8d89a81169088c2671ca865c6fb75. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- policies/document-metadata-policy.md @ d96ef65a802fba5735aae432222cab44c976fdc6
- operating-model.md @ bf0fa24d250325f1b63ee138752803288ce34f67
- roles/test-designer-agent.md @ 7dfa91d7b6f9637953169a90845a6d541523d746
- skills/spec-review-cycle.md @ 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e
- skills/review-artifact.md @ 96a18367a5d316ecc29032e5692bda60b314eede
- LEXICON.md @ 2ae1d055380a780b351e04c364dfd47d22cd5d48
- context-sets/spec-and-change-discipline.md @ 468798e83dd076b2f5772faa03e1749b3ead9176
- roles/chief-of-staff.md @ 0685f4d7fb34910e36ca94a51cc1fdf94fa13308
- roles/spec-reviewer-agent.md @ eb15a8bbdd03fdff075bf75539802d2eca3455f5
- reviews/converging-model-cycle-1.md @ f16df8b55e77e470d6592d3b07327e5e044f4047
- docs/cycles/converging-model-fix-directive.md @ 578a5eb0db80d5d3840708089fd4e568f43ced8f
- docs/cycles/converging-model-fix-2-directive.md @ 5e6cb5198e201a53edc67572a1a25cf6ec74e2ff
- decisions/log.md @ 15b1a874c6fdb1cbbebe89ce149ab81409a3acd5
- roles/context-quality-reviewer.md @ d202b83412d8da512b025eb7f39de4dd8a3f2e40
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
   "$TMPDIR/fiducial-converging-model-regate-frontmatter.log", exit status
   reported.
2. The artifact's header carries Baseline and Reviewed, all nine documents at
   their SHAs, and the two scopes; its verdict line is first. State these,
   labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref a57ae41204a8d89a81169088c2671ca865c6fb75. Cannot execute as written: stop
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

    Converging model — cycle 2 re-gate (confirmation-scoped, two full-depth) Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
