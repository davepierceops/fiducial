# bin/ package — enforce the converging status: Coder (green)

ROUTE AND MODEL

Route: fresh execution session
Model: solid general-purpose

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/converging-enforce-impl-20260903T034500Z.md, commit it alone with a
message naming the package it continues, push with git push origin converging-enforce (no -u), verify by git ls-remote origin converging-enforce, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-converging-enforce", created by: git worktree add "$TMPDIR/fiducial-converging-enforce" converging-enforce

Reuse form: the branch converging-enforce already exists, on origin and (after the fetch below) locally, with no worktree holding it; the prior directive on it is a companion below. Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch converging-enforce, or if "$TMPDIR/fiducial-converging-enforce" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal. If local converging-enforce is behind origin/converging-enforce, fast-forward it to origin/converging-enforce before the worktree add; if it is ahead or diverged, stop and report. Push with git push origin converging-enforce (never -u: the sandbox refuses .git/config writes).

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
c2fc39fedb4e3b865fd171fd255053c475375480 — that is origin/converging-enforce, the red commit; origin/main is expected at cfddcde3dfa0ffc151320d022e5258093b12ce53 (told) and if it has moved, report it and continue, since this branch's base is the red commit, not main. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- docs/cycles/converging-enforce-tests-20260902T230000Z.md @ e5bc06ed26857960ea49a737fabe2a964cd24ba9 — the Test Designer's directive; its acceptance criteria AC-CV-1 to AC-CV-7 are yours to satisfy.
- roles/coder-agent.md @ 1819451f2b39ef017e33ba76b52d2a369cb8fc5c — you fill this role.
- policies/document-metadata-policy.md @ fef34aae7e8b0edc419eb71c79554dbc18429878 — the governed behaviour; the sentence you remove is the "Enforcement of `converging`" bullet in "Revision lifecycle".
- bin/aimeta/frontmatter.py @ 6211312bad20d3272b70f25b2fd94a3b6e07e0ce
- bin/check-frontmatter @ 4e90b03ac27b3b8590bf06f087d02218e997da06
- bin/flip-agreed @ 4e90b03ac27b3b8590bf06f087d02218e997da06
- bin/migrate-frontmatter @ e1741ca87096ba1970172a95ca91484a6ed02418
- bin/tests/helpers.py @ c2fc39fedb4e3b865fd171fd255053c475375480 — and the four test modules the red commit touched, at the same revision.

TASK

You are the Coder for the bin/ package that enforces the `converging` status (DEC-000360). The Test Designer has landed seven red tests at c2fc39fe; six fail today, and AC-CV-6 already passes because bin/flip-agreed never inspected the source status (told, from the Test Designer's report). Your job is the minimum change that turns the suite green, plus the policy sentence removal. You do not edit any file under bin/tests/. If a test cannot be made green without a change you judge wrong, stop and report with the reason; do not edit the test.

Expected change surface, minimum:
- bin/aimeta/frontmatter.py — STATUSES admits `converging`; validation requires no `last-reviewed` for it (AC-CV-1, AC-CV-2, AC-CV-4).
- bin/check-frontmatter — the hook flips only `agreed` documents on a content edit; confirm from the tests whether any code change is needed for AC-CV-3 and say so in the report.
- bin/flip-agreed — TRANSITION_STATUSES admits `converging` as a target; `--review` is required for `agreed` only (AC-CV-5, AC-CV-6).
- bin/migrate-frontmatter — STATUS_MAP maps `converging` to `converging` (AC-CV-7).
Anything beyond this list is reported with the reason before it is committed.

Green-gate. Run bin/tests/run with output captured to "$TMPDIR/fiducial-converging-enforce-green.log". Expected: 611 ran, 0 failures, 0 errors (skip count as the sandbox produces it; the red run showed 7 — told). Also run bin/check-frontmatter --all with output captured to "$TMPDIR/fiducial-converging-enforce-fm.log" and state its exit status.

Commits, in this order, each pushed and verified by git ls-remote origin converging-enforce:
1. The code change alone, message "Implement: enforce the converging status (green)". Green-gate runs against this commit.
2. The policy edit alone, message "Policy: remove the enforcement-precedes-use sentence (DEC-000360 precondition met)": delete the whole "Enforcement of `converging` — ... before any document enters the status." bullet from policies/document-metadata-policy.md and nothing else. Never bypass the pre-commit hook: it will flip the policy's frontmatter to status: in-review and last-reviewed: null in this commit, and that is intended — state the resulting frontmatter in the report. Run bin/check-frontmatter --all again after this commit and state its exit status.

No pull request: the decision session opens it.

CLEANUP — after the report is composed and the last push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-converging-enforce" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

STOP CONDITIONS

Pinned to the reviewed ref c2fc39fedb4e3b865fd171fd255053c475375480. Cannot execute as written: stop
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

    bin/ package — enforce the converging status: Coder (green) — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
