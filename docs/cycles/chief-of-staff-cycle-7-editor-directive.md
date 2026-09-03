# Chief of Staff role cycle 7 — Editor revision Directive

Date: 2026-09-02
Documents in scope:
- roles/chief-of-staff.md @ 3f1cd98f0110910300798e46a4cdf030ab99b3af
- context-sets/spec-and-change-discipline.md @ 234ca7292dac3572212fba0d713f4c9a8cfd9105

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/chief-of-staff-cycle-7-editor-directive.md, commit it alone with a
message naming the cycle it opens, push with git push origin chief-of-staff-cycle-7 (no -u), verify by git ls-remote origin chief-of-staff-cycle-7, and report the
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

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-chief-of-staff-cycle-7", created by: git worktree add --no-track "$TMPDIR/fiducial-chief-of-staff-cycle-7" -b chief-of-staff-cycle-7 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch chief-of-staff-cycle-7, if a branch of that name already exists locally or on origin (git ls-remote origin chief-of-staff-cycle-7 returns a ref), or if "$TMPDIR/fiducial-chief-of-staff-cycle-7" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

## Decisions

This is an Editor revision opening the cycle, not a findings disposition. Two
documents are in scope, on one branch, gated together by one Context Quality
Reviewer artifact in a later directive; each is edited in its own commit.
Entries CS-1 through CS-5 are ruled changes to roles/chief-of-staff.md (told —
Dave's rulings, recorded in OPEN-ITEMS.md @ 457aca1afdadaba99a1446434841ad3995a2407e,
"Topic walk 2026-08-31 — rulings" item 4 and "Retrospective session 2026-08-31
— follow-ups" items 2 and 10; and in
retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203,
topics T05 and T23). CS-6 disposes N-7 and SD-1 disposes N-6, both from
reviews/converging-model-cycle-2.md @ 01c29474ee4d6be7c8c387c348de28321c7ec9bb;
Dave ruled N-6 on 2026-09-02 (told — the decision session's record; the log
entry is the flush's). Intent is binding; wording is the Editor's — no wording
is dictated.

### CS-1 — accept
Finding: one chat holds the GitHub connector at a time, and the constraint is
stated nowhere a decision session reads it.
Resolution: state the constraint in roles/chief-of-staff.md where the
read-sequence's connector use is governed: one decision session holds the
connector at a time; a second active session means no connector writes from
either until the hold is settled.
Dictated wording: none.

### CS-2 — accept
Finding: a decision session has no rule for whether it holds the connector
when it starts.
Resolution: a decision session assumes sole hold of the connector unless the
baton or Dave says otherwise; and before any connector write it checks what
else is running — the baton's told state, and the tree for worktrees or
branches another session may hold — as a read-sequence step.
Dictated wording: none.

### CS-3 — accept
Finding: a connector timeout has been treated as a transport fault and
retried, when the more frequent cause is a second session holding the
connector.
Resolution: state that a connector timeout is treated as contention first —
establish whether another session holds the connector — and as a reconnect or
restart second. Relate this to policies/remote-write-verification-policy.md
rules 2, 6 and 7 by citation, not by restating them.
Dictated wording: none.

### CS-4 — accept
Finding: a baton has handed over with an execution session still running or a
worktree still held, and the successor did not know to check.
Resolution: state the Chief of Staff's obligation, at baton time, to name any
session left running, any worktree held, and whether the connector is
released, each labelled told. This is the role's side of the Decision Layer
rule 13 carve-out (docs/global-context/decision-layer.md); cite it, do not
restate it.
Dictated wording: none.

### CS-5 — accept
Finding: sessions have run past the point where context quality degrades,
with no stated trigger for rotation.
Resolution: state the rotation trigger — before the next major work item
(a new cycle, a new package, a new engagement thread), the Chief of Staff
proposes handoff to a successor decision session in one line and takes Dave's
ack or wave-off; a wave-off ends it for that item. State it once, in the role;
the mechanics of the baton stay in the Decision Layer.
Dictated wording: none.

### CS-6 — accept (N-7)
Finding: the read-sequence's pending-gates step lists documents at
status: in-review and omits documents at status: converging, each of which owes
an exit gate.
Resolution: the pending-gates enumeration names documents at status: converging
alongside in-review, the former owing an exit gate.
Dictated wording: none.

### SD-1 — accept (N-6), context-sets/spec-and-change-discipline.md
Finding: the red-gate paragraph names the architecture summary as the Test
Designer's source for the interface contract, but under DEC-000360 the spec's
suite is written at stage 3, before any architecture summary exists (stage 6).
Resolution: Dave's ruling — the spec's suite takes its interface contract from
the TRD's stated interface list (the one the Spec Reviewer's TRD check
confirms); the unit's tests, at the per-change stage, take theirs from the
architecture summary. Edit the red-gate paragraph to name both sources, each
with its stage; touch nothing else in the document.
Dictated wording: none.

## Deferred / out of scope

- The Context Quality Reviewer gate over both documents — a later directive
  from the decision session; tracked by the cycle.
- The decision-log entry recording the N-6 ruling — the flush after the
  cycle lands, not the Editor.
- A named skill for the autonomous overnight run (T23's second half) — not
  this cycle; remains an OPEN-ITEMS follow-up.
- bin/state — a BACKLOG-v2.md entry; the read-sequence stays manual.

## Execution notes

- Edit roles/chief-of-staff.md and context-sets/spec-and-change-discipline.md
  only, each in its own commit, the role first. Each content edit flips its
  document's status: in-review and last-reviewed: null in the same commit, per
  the document metadata policy's revision lifecycle.
- Leave both documents conformant to docs/global-context/review-rubric.md and
  to LEXICON.md (the touch rule); the Context Quality Reviewer gates the
  result in a later directive. The role document is in-scope for the rubric's
  role criteria (session: decision, audience unchanged).
- Write citations bare — no backticks or quotes around a path in a
  path @ sha citation.
- Push with git push origin chief-of-staff-cycle-7 — no -u; the sandbox
  refuses the .git/config write. Process substitution (<(...)) is refused by
  the sandbox; use temp files.
- Never bypass the pre-commit hook.
- Do not open a pull request; push the branch and report. The decision session
  opens the pull request.
- After the report is composed and the push is verified landed: from the main
  tree, run git worktree remove "$TMPDIR/fiducial-chief-of-staff-cycle-7" (no
  --force). If it fails, report the failure; do not retry. Your report's final
  line states whether the worktree was removed.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
a246098c7b1fdf5e5e38f05b4b6ecfe1813f1d98. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- roles/chief-of-staff.md @ 3f1cd98f0110910300798e46a4cdf030ab99b3af
- context-sets/spec-and-change-discipline.md @ 234ca7292dac3572212fba0d713f4c9a8cfd9105
- OPEN-ITEMS.md @ 457aca1afdadaba99a1446434841ad3995a2407e
- retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203
- reviews/converging-model-cycle-2.md @ 01c29474ee4d6be7c8c387c348de28321c7ec9bb
- reviews/chief-of-staff-cycle-6.md @ 8e3b95ad622e256e6abc80f5bbeb370ed14616f1
- docs/global-context/decision-layer.md @ 0129260877703b3b0b13045de1726c20040c8ec9
- policies/remote-write-verification-policy.md @ 2a14bcc1b7f5092d2c991abc9e044a3b07298912
- operating-model.md @ 2fbb092b2544475021c2a4e7a9c68c4ddcb9d727
- roles/spec-reviewer-agent.md @ e4110f0cc3e47a245a51289b9aa00639ccf05fdb
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
   "$TMPDIR/fiducial-chief-of-staff-cycle-7-frontmatter.log", exit status
   reported.
2. Read each revised document once against its Decisions entries (CS-1
   through CS-6 for the role; SD-1 for the context set) and state, per entry,
   where its change landed (section or line), labelled observed.
3. git diff --stat of the context-set commit: exactly one file, and the body
   change confined to the red-gate paragraph; state it, labelled observed.

STOP CONDITIONS

Pinned to the reviewed ref a246098c7b1fdf5e5e38f05b4b6ecfe1813f1d98. Cannot execute as written: stop
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

    Chief of Staff role cycle 7 — Editor revision Directive — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
