# bin/ package — enforce the converging status: Test Designer (red)

ROUTE AND MODEL

Route: fresh execution session
Model: solid general-purpose

FIRST ACT

Write this directive verbatim to docs/cycles/converging-enforce-tests-20260902T230000Z.md, commit it alone with a
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-converging-enforce", created by: git worktree add --no-track "$TMPDIR/fiducial-converging-enforce" -b converging-enforce origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch converging-enforce, if a branch of that name already exists locally or on origin (git ls-remote origin converging-enforce returns a ref), or if "$TMPDIR/fiducial-converging-enforce" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal. Push with git push origin converging-enforce (never -u: the sandbox refuses .git/config writes).

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
cfddcde3dfa0ffc151320d022e5258093b12ce53. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- roles/test-designer-agent.md @ d66f36f25c30eb8b12808921ec518e47ba2a4cbc — you fill this role; its "During convergence" section governs.
- policies/document-metadata-policy.md @ fef34aae7e8b0edc419eb71c79554dbc18429878 — the governed behaviour under test: `status:` values, "`status: converging` requires no `last-reviewed`", the revision-lifecycle bullets naming `converging`, and the enforcement sentence this package exists to discharge.
- OPEN-ITEMS.md @ 457aca1afdadaba99a1446434841ad3995a2407e — the "Queued next" paragraph's entry "bin/ package — enforce the converging status"; the acceptance criteria below are restated from it.
- bin/tests/helpers.py @ 7b15a7f734bbec410b620ae6e678adbc327f7df3 — the harness (make_repo, make_home, run_cli, frontmatter_block, stage, commit).
- bin/tests/test_frontmatter.py @ 6211312bad20d3272b70f25b2fd94a3b6e07e0ce
- bin/tests/test_check_frontmatter.py @ b65cc7bf1bef6e10e64c0f5be0582d97c9a8b172
- bin/tests/test_flip_agreed.py @ e1741ca87096ba1970172a95ca91484a6ed02418
- bin/tests/test_migrate_frontmatter.py @ e1741ca87096ba1970172a95ca91484a6ed02418

TASK

You are the Test Designer for the bin/ package that enforces the `converging` status (DEC-000360; decisions/log.md at the reviewed ref). You write tests only. You do not edit bin/aimeta/frontmatter.py, bin/check-frontmatter, bin/flip-agreed, bin/migrate-frontmatter, bin/install-hooks, or policies/document-metadata-policy.md. A separate Coder session turns these tests green on this branch after you; the policy sentence removal is the Coder's, in that change.

Read the four tools under test from the working tree before writing anything, so each test asserts the tool's real interface and exit codes (helpers.run_cli, cli.EXIT_* in bin/aimeta). Do not stub or monkeypatch the tools: the red must come from the tools' current behaviour, not from an absent import.

Acceptance criteria, one or more tests each, in the existing test module for the tool named:

AC-CV-1 (bin/tests/test_frontmatter.py) — frontmatter.validate over a document with `status: converging` reports no status finding; a status outside the six admitted values still does.

AC-CV-2 (bin/tests/test_frontmatter.py) — `status: converging` with `last-reviewed` absent, and with `last-reviewed: null`, both validate clean; `status: agreed` with `last-reviewed: null` still fails as it does today.

AC-CV-3 (bin/tests/test_check_frontmatter.py) — in `--staged` (hook) mode, a content edit to an in-scope document at `status: converging` is committed unflipped: status stays `converging`, `last-reviewed` is unchanged, no FLIPPED diagnostic, exit 0. The existing agreed -> in-review flip on a content edit is asserted alongside in the same test, in the same repository, so the two cases are shown to differ on status alone.

AC-CV-4 (bin/tests/test_check_frontmatter.py) — `--all` over a repository containing a `status: converging` document exits 0 with no finding on it.

AC-CV-5 (bin/tests/test_flip_agreed.py) — `flip-agreed <doc> --status converging` on a document at `status: in-review` lands a frontmatter-only commit whose status is `converging` and whose `last-reviewed` is unchanged; no `--review` is required. The commit touches exactly that file and only its frontmatter.

AC-CV-6 (bin/tests/test_flip_agreed.py) — `flip-agreed <doc> --status agreed --review <pointer>` on a document at `status: converging` lands the agreement flip exactly as it does from `in-review` today; assert the resulting status and `last-reviewed`.

AC-CV-7 (bin/tests/test_migrate_frontmatter.py) — the migrator's status mapping admits `converging` on the same footing as `draft` and `in-review`; read the tool to express this against its real input form, and if the mapping's legacy form cannot carry the value, express the test against whatever surface the tool exposes and record why in your report.

Red-gate. Run bin/tests/run with output captured to "$TMPDIR/fiducial-converging-enforce-red.log". Expected: every AC-CV test fails, and it fails on the tool's present behaviour (the status finding, the argparse rejection of `--status converging`, the missing mapping), not on an import or a harness error; every pre-existing test still passes (baseline at the reviewed ref: 604 ran, OK, 9 skipped — told). A new test that passes before the Coder has run is a broken test; fix it or report it, do not leave it.

Commit the tests alone, one commit, message "Tests: enforce the converging status (red)". Push with git push origin converging-enforce and verify with git ls-remote origin converging-enforce. No pull request: the decision session opens it after green.

Findings. A criterion you cannot express as a test, or a place where the policy text and the tools' interfaces do not admit a single reading, is a finding in your report with the reason, not a silent omission and not a test that guesses. The stop conditions below govern anything you cannot execute as written.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-converging-enforce" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

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

Pinned to the reviewed ref cfddcde3dfa0ffc151320d022e5258093b12ce53. Cannot execute as written: stop
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

    bin/ package — enforce the converging status: Test Designer (red) — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
