# Bundle-system PRD cycle 1 — Spec Reviewer gate Directive

Date: 2026-09-02
Documents in scope:
- specs/bundle-system.md @ cf3b87e08cf6257ee09c7066a3a53ed2adafcd15

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-system-cycle-1-gate-directive.md, commit it alone with a
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
worktree at "$TMPDIR/fiducial-bundle-cycle-1-gate", created by: git worktree add --no-track "$TMPDIR/fiducial-bundle-cycle-1-gate" -b bundle-system-cycle-1-gate origin/main

## Decisions

No findings precede this gate; nothing is disposed here. This directive
opens cycle 1 of the PRD's review. The document was human-reviewed with
Dave 2026-09-01 (pull request #275); rulings from that review are fenced:

### R-1 — ruled and applied: delivery form (topic-walk ruling 13 T26; DEC-000320)
Finding: the PRD formerly hard-coded ~/Downloads and sort-to-top.
Resolution: applied in the human review — the delivery directory and
filename now cite DEC-000200/DEC-000290 at three sites. Verify all three
state the ruled form and none was missed; a missed site is a finding.
Do not re-derive the ruling.
Dictated wording: none.

### R-2 — pre-ruled, not yet applied: lore home (topic-walk ruling 13 T30)
Finding: the lore home for G11 / AC-BS-12 is ruled — the tooling-facts
artifact; entries dated, falsifiable, classified (lost response / never
dispatched / caller error / tool defect) — but the PRD does not yet state
it.
Resolution: record under a "Pre-ruled" heading where G11 and AC-BS-12 will
absorb this; file nothing on it; do not re-derive the ruling.
Dictated wording: none.

### OQ dispositions — resolved ones are closed, not re-opened
Finding: OQ-5, OQ-6, and OQ-10 carry in-document resolutions dated
2026-09-01, Dave's, with log entries DEC-000320, DEC-000330, DEC-000340.
Resolution: verify each resolution is internally consistent with the ACs
that cite it (AC-BS-2, AC-BS-9); inconsistency is a finding, the ruling
itself is not. The remaining OQs have named resolvers; note where the PRD
depends on them, resolve none.
Dictated wording: none.

ROLE AND TASK. This session fills one role: Spec Reviewer per
roles/spec-reviewer-agent.md, independent — this session authored nothing
under review. Full-depth gate review of specs/bundle-system.md @
cf3b87e08cf6257ee09c7066a3a53ed2adafcd15, a PRD at status draft, against
specs/prd-template.md and the role's obligations, including the continuity
scan: claims the PRD makes about the present tool and corpus (file counts,
audience values, baselines at 6e77040, the header form) are checked by
running bin/bundle and bin/bundle --list in the assigned worktree and by
reading the decisions/log.md entries the PRD cites, each checked claim
labelled observed; a claim that cannot be checked is labelled so. A
finding is a claim: cite the location, demonstrate it, classify it.

ARTIFACT. Produce reviews/bundle-system-cycle-1.md per
skills/review-artifact.md, verdict first, with the "Pre-ruled" heading
carrying R-1's verification result and R-2, and an "OQ dependencies"
heading for the open OQs. Before writing it, confirm by listing that
reviews/bundle-system-cycle-1.md does not exist at the base; if it exists,
stop and report. This session creates exactly two files — this directive
file and the review artifact — and modifies nothing. Review only.

## Deferred / out of scope

- The revision disposing this cycle's findings, R-2's application, and the
  re-gate — later directives; tracked by the cycle.
- The remaining OQs — each has a named resolver in §8.
- Spec agreement — the Spec Reviewer gate is necessary, not sufficient;
  Dave agrees after the cycle closes.

## Execution notes

- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin bundle-system-cycle-1-gate, without -u.
- Do not open a pull request; push the branch and report. The decision
  session opens the pull request.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
6790702bae7c06fffbb1edbfd678ebcddc5dc881. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/bundle-system.md @ cf3b87e08cf6257ee09c7066a3a53ed2adafcd15
- specs/prd-template.md @ 39b04d90e87267d260ee925ed3d5e3b3ccfd1f67
- roles/spec-reviewer-agent.md @ a092f4938256503a5d894eeb9c05c5a777b72cde
- skills/spec-review-cycle.md @ 9d5456cb8010ed8efddf9500af8dd2771c38f5e3
- skills/review-artifact.md @ 6b210cb0a749bcf40227a3f7bc7da8f6d0306a3d
- decisions/log.md @ 1ffe27a75428416a4bb3388cc144ad2fcc8c0276

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
   "$TMPDIR/fiducial-bundle-cycle-1-gate-frontmatter.log", exit status
   reported.
2. bin/bundle --list, and bin/bundle --audience writer and --audience
   chief-of-staff, output captured to
   "$TMPDIR/fiducial-bundle-cycle-1-gate-bundle.log"; observed counts and
   audience values stated against the PRD's claims and §5 baselines.
3. The review artifact's verdict line stated verbatim in the report, with
   findings by severity, the Pre-ruled results, and the OQ dependencies
   list.

STOP CONDITIONS

Pinned to the reviewed ref cf3b87e08cf6257ee09c7066a3a53ed2adafcd15 (the document commit) on main at 6790702bae7c06fffbb1edbfd678ebcddc5dc881. Cannot execute as written: stop
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

    Bundle-system PRD cycle 1 — Spec Reviewer gate Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
