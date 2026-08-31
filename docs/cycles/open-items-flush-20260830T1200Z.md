You are the Executor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Update OPEN-ITEMS.md with the deltas below — exact text, nothing else in the file changes. OPEN-ITEMS.md is outside the frontmatter in-scope set; it has no frontmatter and needs none. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/open-items-flush-20260830T1200Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: OPEN-ITEMS flush 2026-08-30 (directive-invariants arc)", push with git push origin open-items-flush-20260830b (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-oi-flush-b", created by: git worktree add --no-track "$TMPDIR/fiducial-oi-flush-b" -b open-items-flush-20260830b origin/main
Before creating it, run git fetch origin, then git worktree list; if any existing worktree holds branch open-items-flush-20260830b, or if "$TMPDIR/fiducial-oi-flush-b" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: origin/main must contain 3e64efed9116b053c187eddefb10d99fa50a291d. If origin/main is beyond it, proceed only if no commit past it touches OPEN-ITEMS.md; otherwise stop and report. Confirm OPEN-ITEMS.md at HEAD has blob SHA df211fa559ce457328458dc91230c958ffb5ccac (git rev-parse HEAD:OPEN-ITEMS.md); if not, stop and report.

EDITS, in file order. Each names its anchor by the exact heading line; if an anchor is not found exactly once, stop and report. Preserve the file's ~80-column wrap style in new prose.

E1. Under the heading "## `bin/cycle-open` and the retirement of Track", no change. (Anchor check only.)

E2. Replace the entire section headed "## `skills/directive-invariants.md` is `draft` and load-bearing" — from that heading line through the line before the next "---" — with:

## ~~`skills/directive-invariants.md` is `draft` and load-bearing~~

**RESOLVED** 2026-08-30: agreed at `3f0a96e4f97015ed3091e3d666b64fbc22895eec`
(`reviews/directive-invariants-cycle-4.md`), flip `a8a9913`, on `main` at
`3e64efe`. Four Context Quality Reviewer cycles and three revisions, PRs
#250–#258, all merge commits. Directives: `docs/cycles/directive-invariants-{gate,rev-1b,rev-1c,rev-1d,gate-2,rev-2,rev-2b,gate-3,rev-3,gate-4,agree}-*.md`.
Rejected and recorded at cycle 1: F-4/F-5 (Stop-conditions and Claim-labels
regions restate Core 11/15 and 6 — by-value quotation into emitted skeletons,
same class as the disposition prompt). Suite at every content commit: 604 OK /
7 skipped, zero reds — the three writing-workstream reds (test_scope sc1/sc3,
test_check_frontmatter cf13) are gone; expected-state lists in directives now
name no known red.

Riders on the document, for its next cycle: cycle-4 F-1 — state the
match-rule property as an editor constraint inside the format-rules paragraph;
cycle-4 O-2 — the Preamble markers positional prose (`<document heading>`
first, literal second) is a second unstated positional dependency; code
classifies by shape, so swapping the entries leaves the check green and the
prose false; cycle-4 O-3 — "eligible line" and "unfenced line" alternate in
the fence-only paragraph; the second is stronger; cycle-4 O-1 — `<name>` in
the worked example is still undefined as a placeholder.

**Original entry, kept for the record:**

Landed 2026-08-29 (PR #231, `ab3f2ef`; heading line amended PR #244, `c4a0353`). Every skeleton `bin/directive` emits, in both modes, reads its regions from this document at its last commit in the methodology home, so the document governs every directive from adoption forward while sitting at `status: draft`.

---

## `skills/directive-authoring.md` consolidation cycle owed — adoption of `bin/directive` waits on it

Five expedited amendments outstanding, plus: the OQ-Q4(c) path pointer to
`skills/directive-invariants.md`; the own-worktree-cleanup-and-report-final-line
rule; the holder-check rule; "expected-output lines are claims" (verify it is
already there in spirit); OQ-10's Naming-section branch gap; `git push origin
<branch>` with no `-u` in the sandbox (`.git/config` is not writable); never
bypassing the pre-commit hook. Added 2026-08-30 from the invariants arc:
cycle-2 O-3 — the governed rule's "this document" inverts its referent when the
bullet is emitted into a directive by value; fixable only in this skill, and the
two copies move together under the byte-equality rule; and **the route line
names one session** — "the holding session" is ambiguous when two execution
sessions hold the same worktree, which happened on rev-1c/rev-1d (below).
Evidence for adoption: three of this arc's stops were authoring defects
`bin/check-directive` exists to catch — a blanket constraint contradicting an
instruction (rev-1b, F-11), a dictated literal violating the same directive's
own self-check (rev-2, F-2), and a base-verification guard broader than the
blast radius (rev-1). Adoption — authors reaching for `bin/directive` rather
than freehand — waits on the pointer.

E3. In the section headed "## `specs/directive-tooling-trd.md` — rider queue and open questions", append to the end of its first paragraph (the one ending "…and drift would be silent."):

Confirmed absent 2026-08-30 by the cycle-2 gate sweep
(`reviews/directive-invariants-cycle-2.md` O-2): `AUTHORING_RELPATH` is defined
in `bin/tests/helpers.py` and referenced by nothing. Two more riders from the
invariants arc: §3.3's cycle-mode table has no Placeholders column, so
`{{heading}}`, `{{date}}`, `{{scope_list}}` are fixed only in
`skills/directive-invariants.md` and `bin/aimeta/directive.py`; and §3.4's
decision sentence calls the label the bare token while its match-rule bullet
says "exactly the literal" whose definition carries the colon — the document
and `matches_label` both take the bare-token reading.

E4. In the section headed "## Executor self-recovery — tracked behaviour defect", append a new paragraph after the last one:

2026-08-30, directive-invariants arc: one more disclosed deviation and its
cause. Two execution sessions held the same worktree — rev-1c and rev-1d were
routed to "the holding session" while two existed — and the session that did
the work continued past a directive commit the other had landed under it,
citing benign content; the other stopped correctly three times on the same
class of mutation. The deviation is accepted; the cause is the route line, now
a consolidation-cycle item above. Six correct stops in the same arc, three of
them on the Chief of Staff's own authoring defects.

E5. Replace the entire section headed "## Worktree and branch pile" — from that heading line through the line before the next "---" — with:

## ~~Worktree and branch pile~~

**RESOLVED** 2026-08-30. One command block from the CoS, computed rather than
listed: every branch on origin fully merged into `origin/main` — 178 of them,
the 27 listed here among them — deleted; 39 local branches deleted (31 by
plain delete, 8 by force after an ancestor-of-`origin/main` check, because the
local `main` was behind); both stale worktree entries pruned; `git worktree
list` shows only the main tree. Record: `~/Downloads/branch-cleanup-20260830T1100Z.txt`.
The `retros/` untracked files in the main clone were not touched.

E6. In the section headed "## Writing methodology landed — follow-ups", replace the first bullet (beginning "- **Full cycle owed on `policies/document-metadata-policy.md`.**" through "…cycle later.") with:

- ~~**Full cycle owed on `policies/document-metadata-policy.md`.**~~ Agreed
  2026-08-30 at cycle 20 (PR #249, `d577819`).

SCOPE, one commit: OPEN-ITEMS.md only. Commit message: "OPEN-ITEMS flush 2026-08-30: directive-invariants agreed, branch pile cleared". Push with git push origin open-items-flush-20260830b.

VERIFICATION after the commit, output to "$TMPDIR/fiducial-oi-flush-b-run.log": git show --stat HEAD (expected: OPEN-ITEMS.md only); bin/check-frontmatter --all (expected: exit 0, 61 files / 14 globs — this file is out of scope). Any other file in the diff, or any different count, is a stop.

GH: never invoke gh. The decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin open-items-flush-20260830b shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-oi-flush-b" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to 3e64efed9116b053c187eddefb10d99fa50a291d: on any failed command, any anchor not found exactly once, any precondition not met, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; content commit SHA; branch name; run-log path; per edit E1–E6, done with the resulting line range; diff stat; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
