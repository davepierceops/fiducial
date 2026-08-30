You are an execution session on davepierceops/fiducial, clone at ~/code/fiducial, applying the decision session's OPEN-ITEMS flush. Every edit below is dictated; carry the text verbatim. You edit OPEN-ITEMS.md and nothing else.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/open-items-flush-20260830T0500Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: OPEN-ITEMS flush 2026-08-30", push with git push origin open-items-flush-20260830 (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-open-items-flush", created by: git worktree add --no-track "$TMPDIR/fiducial-open-items-flush" -b open-items-flush-20260830 origin/main
Before creating it, run git worktree list; if any existing worktree holds branch open-items-flush-20260830, or if "$TMPDIR/fiducial-open-items-flush" already exists, stop and report. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. origin/main must contain 59caa405b021d9dd38110530d7de6c08a5a6f5f9. If origin/main is beyond it, proceed only if no commit past it touches OPEN-ITEMS.md; otherwise stop and report.

READ before writing: OPEN-ITEMS.md in full. Confirm each section heading named below exists exactly once and is shaped as the edit assumes; if one is not, stop and report which.

EDITS, in file order. A "strike" wraps the section's heading text in ~~ ~~ (keeping the leading ## ) and inserts the given resolution paragraph as the first paragraph of the body; the rest of the body stays. A "new section" is inserted where stated, as ## heading, blank line, body, blank line, ---, blank line, matching the file's existing separator convention.

1. Header line "Last updated: 2026-08-29" becomes "Last updated: 2026-08-30".

2. Strike "## `CLAUDE.md` carries a derived copy of governed rules". Resolution paragraph:
**RESOLVED** 2026-08-28 by PR #224: `CLAUDE.md` and `AGENTS.md` are deleted. fiducial is a portable corpus; the project-adapter question belongs to the bundle-system PRD.

3. Strike "## `specs/directive-tooling.md` names a retired binary". Resolution paragraph:
**RESOLVED** 2026-08-28 by the PRD rewrite (PR #225, agreed at cycle 23 @ `d3ab472`): the rewrite carries none of the references this entry names — verified by two full reads. The document's next opening cycle is queued under "`specs/directive-tooling.md` — rider queue" below.

4. New section, inserted immediately before "## Corpus dedup, Passes 1–2b — closed":

## `skills/directive-invariants.md` is `draft` and load-bearing

Landed 2026-08-29 (PR #231, `ab3f2ef`; heading line amended PR #244, `c4a0353`). Every skeleton `bin/directive` emits, in both modes, reads its regions from this document at its last commit in the methodology home, so the document governs every directive from adoption forward while sitting at `status: draft`. **What's needed:** its Context Quality Reviewer cycle, first in the directive-tooling queue. Then the `skills/directive-authoring.md` consolidation cycle (five expedited amendments outstanding), which also carries: the OQ-Q4(c) path pointer to this document; the own-worktree-cleanup-and-report-final-line rule; the holder-check rule; "expected-output lines are claims" (verify it is already there in spirit); OQ-10's Naming-section branch gap; `git push origin <branch>` with no `-u` in the sandbox (`.git/config` is not writable); never bypassing the pre-commit hook. Adoption — authors reaching for `bin/directive` rather than freehand — waits on that pointer.

---

## `specs/directive-tooling.md` — rider queue

For the PRD's next opening cycle; do not open a cycle for these alone. (a) §4 "plus the disposition slot and the source manifest" is illustrative, not exhaustive — dictated clause per TRD §9 OQ-5 (Dave, 2026-08-28). (b) AC-DT-09 "tag" → "annotated tag"; a lightweight tag is indistinguishable, verified by running. (c) AC-DT-04's author-text clause clarification; the TRD states satisfied-by-construction meanwhile.

---

## `specs/directive-tooling-trd.md` — rider queue and open questions

Riders for the TRD's next opening cycle, each from an implementation-package ruling on main (directives `docs/cycles/directive-tooling-impl-{1,2,3,4,4b}-*.md`, `directive-tooling-tests-{fix-1,fix-2,fix-2b,3}-*.md`, 2026-08-29/30): §3.3 Heading (cycle)'s first line is `# {{heading}}`, filled whole from `directive_identity`, and the placeholder table drops `{{cycle}}`/`{{title}}` for that section (ruling (b)); §3.3 "appears exactly once in the file" reads *once among eligible lines*, the mask applying to the generator's self-check and the tests alike (ruling (a)); `{{reviewed_ref}}` and `{{companion_list}}` have no flag in the §3.9 flag set and are emitted as author slots inside committed regions, which the manifest then classifies as committed; M2 skips the source-manifest region, because manifest entries cite the methodology home, which in the test substrate is not the linted repository; §3.7's git dependency notes that `status` reads run with `--no-optional-locks`, which is what holds §3.9's "reading is not writing" (test_x5 caught the index rewrite); the stale counts cycle-1 deferred as O-1..O-4 (`bin/` executable count; corpus 170/114/68 today vs 144/109/63 in the text). Test-suite gap for the Test Designer: §3.3's byte-equality test of the disposition prompt against `skills/directive-authoring.md`'s bullet does not exist, so §4.2's B3 is pinned by nothing and drift would be silent.

Open questions carrying recommendations, Dave's to rule whenever: Q2 rec (b), directive lands and work stops; Q4 rec (c), the skill gains a path pointer to the invariants document; Q6 rec (b), the five-code contract — §7 is already written to (b). Plus the TRD's own OQ-1..10; OQ-7 (sole-tree literal) and OQ-9 (M3-extent reading) want a gate or Dave.

---

## Convergence process — canonization owed

Ruled ad hoc for the directive-tooling TRD, canonization after from the retro (Dave, 2026-08-28). The shape as run: one blocker-scoped review cycle, the TRD stays open, the Test Designer writes tests against it, findings mediated through the decision session both ways, joint flip when they cohere. It ran clean; evidence is the `docs/cycles/directive-tooling-trd-*.md` chain and `reviews/directive-tooling-trd-cycle-{1,2,3}.md`. One detail the description added and the run used: the decision session as the mediating agent — executors state intent in dispositions and verify against the counterparty's artifacts, and correct a wrong disposition with disclosure. A full cycle on `skills/spec-review-cycle.md` (or a sibling skill) writes it in.

---

## PRD and TRD templates carry the wrong audience — directed fix

Dave, 2026-08-28: PRDs and TRDs are audience `[human]` (the narrowing of `specs/directive-tooling.md` from `[all-roles, human]` was deliberate and kept, cycle 21 O1). Both templates (`prd-template`, `trd-template`) still say otherwise and are wrong. A directed change awaiting its review cycle, not a candidate.

---

5. In "## Candidate methodology changes from the dedup sessions", replace the bullet beginning "**Decision-layer 3, \"landmine\".**" with:
- **Decision-layer 3, "landmine".** Sharpened 2026-08-29 (Dave): the word is reserved for a consequence of doing what was asked that is severe or hard to reverse — a wrong merge, a lost record, a broken gate. Expected tool behaviour, state information, and items already on the tracker or baton are triage, unlabelled. Observed 2026-08-26 and again 2026-08-29: the label spent on nothing trains the reader to skip it.
and append these bullets at the end of the same list:
- **Governed documents carry substance only.** Findings dispositions, cycle changelog prose, per-sentence provenance tags and SHA citations belong in review artifacts and cycle directives, not in the document they concern. The directive-tooling PRD rewrite (PR #225) went from a bloated draft to 511 lines on this rule alone; write it into the rubric or the authoring skills.
- **Executor decision lists are committed, not chatted.** Every implementation package this session reported a numbered list of decisions the spec left open; those lists live only in chat, and the package-3 executor could not read package 1's. The report's decision list is appended to the directive file (or a sibling report file) as the executor's last commit, so the next executor reads it from the tree.

6. In "## Executor self-recovery — tracked behaviour defect", append this paragraph to the end of the body:
2026-08-29/30, directive-tooling packages: two more, disclosed and accepted — the package-1 executor committed its directive file with the pre-commit hook bypassed (verified clean afterwards; directives now say "never bypass the pre-commit hook"), and the AC-DT-16 executor committed its edits before its directive file and pushed both together (record accepted as-is, PR #245). Against that, four correct stops in the same run: tests-fix-2 on an unruled finding, tests-3 on the parameterization scope, impl-4 on test_x5, and impl-1's own self-check refusing its first skeleton. The stop wording holds; the two deviations are a different class — a step taken on the executor's own judgment rather than a recovery — and the invariants document's First act and Sandbox regions are where they get closed.

7. Replace the whole body of "## Worktree and branch pile" with:
Worktrees: cleared. `git worktree prune` from Dave's terminal on 2026-08-29 left one registered worktree, `fiducial-dmp-cycle-20`, which belongs to a live cycle. Standing pattern that held for every directive this session: each session removes its own worktree as its final act and reports the status as the report's last line; a worktree another session created cannot be removed from the sandbox (EPERM on `.git/worktrees/<name>`), and `git worktree prune` from Dave's terminal clears the metadata once the directory is gone.

Branches to delete, all merged to main: `log-dec-200-210`, `rule-extraction-pass1`, `rule-dedup-pass2`, `rule-divergence-rulings`, `rule-divergence-rulings-gate`, `rule-divergence-rulings-cycle-2`, `rule-divergence-rulings-gate-2`, `flip-rule-divergence-rulings`, `flip-directive-tooling`, `untag-specs-audience`, `agreeing-clusters`, `agreeing-clusters-gate`, `flip-agreeing-clusters`, `pass-2b-rulings`, `pass-2b-rulings-gate`, `flip-pass-2b-rulings`, `retire-bundle-methodology`, `retire-bundle-methodology-gate`, `open-items-flush-20260827`, `directive-tooling-impl-1`, `directive-tooling-tests-fix-1`, `directive-tooling-impl-2`, `directive-tooling-tests-fix-2`, `directive-tooling-tests-3`, `directive-tooling-impl-3`, `directive-tooling-ac-dt-16`, `directive-tooling-impl-4`. One command block from the CoS; the `retros/` untracked files in the main clone are Dave's and are not touched.

Commit with message "OPEN-ITEMS flush 2026-08-30: directive-tooling landed; rider queues; invariants doc CQR owed; landmine sharpened". Push with git push origin open-items-flush-20260830.

VERIFICATION, from the worktree: bin/check-frontmatter --all (state exit code and count; OPEN-ITEMS.md is outside its globs, so the count should be unchanged); git diff origin/main --stat must show exactly OPEN-ITEMS.md and the directive file; grep -c "^## " OPEN-ITEMS.md before and after (expect the after count to be the before count plus 5).

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin open-items-flush-20260830 shows your edit commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-open-items-flush" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 59caa405b021d9dd38110530d7de6c08a5a6f5f9: on any failed command, any precondition not met, any named section absent or duplicated, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT: directive-file commit SHA; edit commit SHA; branch name; the heading counts before and after; the list of headings struck and added; check-frontmatter exit code and count; anything observed this directive did not anticipate; worktree-removal status as the final line. Label every claim observed, inferred, told, or unknown.
