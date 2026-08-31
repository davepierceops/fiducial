You are the Editor, an execution session on davepierceops/fiducial, clone at ~/code/fiducial. Revise skills/directive-authoring.md (the consolidation cycle) and skills/directive-invariants.md (its riders, and the one fence that moves with the skill) per the decisions below. You do not flip status, do not run bin/flip-agreed, do not edit any review artifact, and do not edit bin/, specs/, docs/global-context/, policies/, or roles/. No other session holds the branch or worktree named below.

FIRST ACT — directive file. Write this entire directive verbatim to docs/cycles/directive-authoring-consolidation-20260831T150000Z.md in the worktree named below (create the worktree first, then write), commit it alone with message "Directive: directive-authoring consolidation revision", push with git push origin directive-authoring-consolidation (no -u), and report the SHA. Never bypass the pre-commit hook.

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-da-consol", created by: git worktree add --no-track "$TMPDIR/fiducial-da-consol" -b directive-authoring-consolidation 37c681888cf5bf26f59843424bc0195de6220711
Before creating it, run git fetch origin, then git worktree list; if any existing worktree holds branch directive-authoring-consolidation, or if "$TMPDIR/fiducial-da-consol" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION before anything else: git fetch origin. Judge the fetch by the refs it reports, not by credential-helper noise on stderr. The reviewed ref 37c681888cf5bf26f59843424bc0195de6220711 must be an ancestor of origin/main (git merge-base --is-ancestor 37c681888cf5bf26f59843424bc0195de6220711 origin/main, exit 0); if it is not, stop and report. The worktree is created from the reviewed ref itself, so origin/main having moved past it is expected and is not a stop. In the worktree, git rev-parse HEAD:skills/directive-authoring.md must be 91b2ccff30130dbd6b97e69274ab449ece2400d3 and HEAD:skills/directive-invariants.md must be 726df3cc9abcab37cd1bd16767692f512ee29e8e; if either differs, stop and report.

READ before writing, whole, from the worktree: skills/directive-authoring.md and skills/directive-invariants.md (the two documents under revision); reviews/directive-invariants-cycle-4.md (F-1, O-1, O-2, O-3 — the riders); reviews/directive-invariants-cycle-2.md O-3 (the pronoun that inverts); reviews/directive-authoring-cycle-3.md F-1 and F-3; reviews/expedited-log.md, the five 2026-08-23 entries for skills/directive-authoring.md; docs/global-context/review-rubric.md (the twelve criteria both documents will be gated against); bin/aimeta/invariants.py and bin/aimeta/mdmask.py (to confirm which fences the parser reads and what unfenced_labelled_statements tests — you add, remove, or reorder no fence).

STATUS: the pre-commit hook flips each edited agreed document to in-review with last-reviewed null. Both flips are expected; do not flip any status by hand.

EDITING CONSTRAINTS, binding over every decision below; each decision has been read against them and none contradicts. In skills/directive-invariants.md: no ## section is added, removed, renamed, or reordered; no region section's first body line changes; no fenced block is added, removed, or reordered anywhere; region bodies are unchanged except the first fence of ## Working-tree disposition prompt (D-1); preamble prose changes only where D-2 and D-3 name it; lint-section prose changes only where D-4 names it. In both files, after the edits, no eligible line satisfies the disposition label's match rule — the shipped unfenced_labelled_statements check returns no hit over either file. In skills/directive-authoring.md, the disposition label is not spelled anywhere, fenced or not. Both files state rules, cite no file by path other than the filename patterns the Naming section prescribes, and cite no document by section number. Frontmatter: untouched by you; the hook's flips are the only frontmatter change.

DECISIONS (Dave, 2026-08-31, ruling the consolidation entry in OPEN-ITEMS.md as of 37c6818 and the cycle-4 riders on skills/directive-invariants.md; wording the Chief of Staff's, read against the sources named above):

### D-0 — accept: consolidate skills/directive-authoring.md; the whole body below the frontmatter is dictated
Finding: five same-day expedited amendments were agreed without a reviewer cycle; the OPEN-ITEMS consolidation entry lists what the cycle carries.
Resolution: Replace everything below the frontmatter's closing --- in skills/directive-authoring.md with the dictated body in the fenced block that follows, byte for byte, including the leading blank line and the final newline. The first bullet is the one the Directive Invariants document's disposition-prompt fence quotes; D-1 moves the fence with it. The cycle-2 O-3 pronoun is resolved by naming the holder — "the Directive Invariants document" — in every copy, so the sentence reads the same in the skill, in the fence, and in an emitted directive. The holder is named by title, not by path, because the review rubric's criterion 3 treats a path-shaped reference as a defect and both documents load in the same bundle. The Naming section now admits both cycle-mode filenames (cycle-3 F-1, TRD OQ-10). New bullets carry: the route line names one session; the disposition label leads no other unfenced line; base guards scoped to the blast radius; expected-state lines read from the tree; the holder check; own-worktree removal with the report's final line; push with no upstream; the hook is never bypassed.
Dictated wording:

```text

# Skill: Directive Authoring

This procedure runs in a decision session.

## Writing the directive file

- **Every directive states its working-tree disposition** — either an
  exclusive assignment (a named directory plus the command creating it) or an
  explicit sole-tree declaration. A prohibition is not a disposition. The
  disposition is stated as its own labelled statement, exactly one per
  directive, mechanically distinguishable from incidental mention of trees or
  commands elsewhere in the file; the label's fixed form, the canonical
  sole-tree sentence, and a worked example of each form are stated in the
  Directive Invariants document and nowhere else. Two sessions sharing a tree
  mutate each other's preconditions; prefer not splitting work across trees.
- **The disposition label leads the disposition statement and no other
  unfenced line.**
- **The route line names one session** — a fresh session, or an existing
  session named by the directive it landed, never by the tree or branch it
  holds.
- **Pin STOP conditions to the reviewed ref**, not the head of the branch the
  directive lands on — the directive's own commit moves that head.
- **No blanket constraint may contradict an explicit instruction in the same
  file.** Read the constraint block against the instruction list before sending.
- **Scope Do-not lists and base guards to the blast radius.** Where a required
  consistency fix reaches outside it, name that file as explicitly permitted.
  A guard on the base names the files the work touches, never a directory.
- **Carry dictated wording as a pointer** — the source's path and SHA plus its
  field or section, never restated — unless the directive is itself the
  wording's origin, in which case it carries it inline and downstream artifacts
  point at it.
- **An expected-state line is read from the tree at the reviewed ref** —
  counts, exit codes, blob SHAs — never carried from a session report or from
  memory.
- **A directive that assigns a worktree instructs the holder check**: before
  creating it, fetch the base and list worktrees; if any worktree holds the
  branch, or the path exists, stop and report. Entries marked prunable are not
  the session's.
- **A directive that assigns a worktree instructs its removal** from the main
  tree, after the report is composed and every push is verified landed,
  without force and without retry; the report's final line states the outcome.
- **A push instruction names the remote and the branch and sets no upstream.**
- **Every directive states that the pre-commit hook is never bypassed.**

## Naming

A directive file is `docs/cycles/<descriptor>-<timestamp>.md`, the timestamp in
ISO 8601 basic format with date and time components both present (as
`20260820T161541`) — except a directive generated in cycle mode, which is
`docs/cycles/cycle-<n>-directive.md` for a numbered cycle or
`docs/cycles/<slug>-directive.md` for a named one, the slug a single path
component.
```

### D-1 — accept (cycle-2 O-3, and the byte-equality rule): the disposition-prompt fence moves with the bullet
Finding: the fence at skills/directive-invariants.md:85–94 quotes the skill's first bullet, and the two are required to be byte-equal after flowing; the bullet changes under D-0.
Resolution: Replace the body of that fence — the lines between the ```text line at 85 and the closing ``` at 94, nothing else — with the dictated text below. The fence lines, the framing sentence above the fence, the "Both admitted forms, worked:" line, and the second fence are unchanged. Confirm by the cycle-2 method: flow the fence body and the skill's first bullet (whitespace runs collapsed to one space, lines joined, the bullet's leading "- " stripped) and compare; they are equal at 655 bytes each.
Dictated wording:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document and
nowhere else. Two sessions sharing a tree mutate each other's preconditions;
prefer not splitting work across trees.
```

### D-2 — accept (cycle-4 F-1 with O-3): the match-rule property becomes an editor constraint in the format-rules paragraph
Finding: the property the whole design rests on is stated as a description at :44–49, outside the paragraph that binds the editor, and its second clause says "unfenced" where the check tests "eligible".
Resolution: Two edits. (a) Append to the format-rules paragraph at :18–25, directly after "no fence is added, removed, or reordered there.", this text, reflowed to the paragraph's width: No eligible line of this document — eligibility as the Disposition label section defines it — leads, after stripping, with the bare label token and carries a colon later on the same line; the bare token may appear where it does not lead the line, and the colon-terminated literal appears only inside fenced blocks. (b) Delete the paragraph at :44–49 ("Outside fenced blocks, no eligible line …" through "… where it does not lead the line.") and the blank line that follows it, so one blank line separates the placeholders paragraph from the first ## heading.

### D-3 — accept (cycle-4 O-1 rider): an angle-bracketed slot in a worked example is not a placeholder
Finding: `<name>` in the worked exclusive-assignment example is undefined against the placeholder rules, which define `{{name}}` syntax only.
Resolution: Append to the sentence at :42, after "never a pass-through.", in the same paragraph: An angle-bracketed token inside a worked example, such as `<name>`, is a slot the author fills; it is not a placeholder and the generator never substitutes it. Reflow to the paragraph's width.

### D-4 — accept (cycle-4 O-2): the Preamble markers prose classifies by shape, as the code does
Finding: :272–273 states the two fenced entries positionally ("the first entry … the second"); the shipped classifier decides by whether an entry is written in angle brackets, so swapping the entries leaves the check green and the prose false.
Resolution: Replace the two lines at :272–273 with: The entry written in angle brackets stands for whatever heading line the mode emits and is not matched as a literal; the other entry is matched as a literal. Reflow to the paragraph's width; the fence above it is untouched.

### Everything else in reviews/directive-invariants-cycle-4.md and reviews/directive-authoring-cycle-3.md — no action.

SCOPE, one commit after the directive-file commit: skills/directive-authoring.md and skills/directive-invariants.md only, plus the hook's frontmatter flips on the same two files. Commit message: "directive-authoring: consolidation revision (D-0); directive-invariants: fence moves with the bullet, cycle-4 riders (D-1..D-4)". Push with git push origin directive-authoring-consolidation.

VERIFICATION after the commit, from the worktree, output to "$TMPDIR/fiducial-da-consol-run.log": bin/tests/run for the whole suite; bin/check-frontmatter --all (state exit code and count); the shipped unfenced_labelled_statements check over each of the two files (state the call and the result, expected: no hits in either); the byte-equality flow check named in D-1 (state both byte counts and the comparison result, expected: 655 and 655, equal); a grep of skills/directive-authoring.md for the bare label token (expected: zero hits); git diff --stat of the content commit (expected: exactly two files); and the frontmatter of both files as landed (expected: status in-review, last-reviewed null, audience unchanged).
Expected state, and a stop if it differs: whole suite OK with zero failures and zero errors, 7 skipped; test_cross_cutting.py 17/17; test_cycle_open.py 62/62; test_directive.py 43/43; test_directive_trd.py 16 passed + 6 skipped; test_check_directive.py 84/84; check-frontmatter exit 0, 61 files / 14 globs. Any red is a stop: report it with the assertion text; do not adjust a test and do not adjust either document to satisfy it.

GH: never invoke gh. Push the branch; the decision session opens the pull request.

CLEANUP — after the report is composed and both pushes are verified landed (git ls-remote origin directive-authoring-consolidation shows your content commit SHA): from the main tree, run git worktree remove "$TMPDIR/fiducial-da-consol" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

STOP CONDITIONS, pinned to reviewed ref 37c681888cf5bf26f59843424bc0195de6220711. Cannot execute as written: stop and report. Concurrent tree mutation: stop and report. On any failed command, any precondition not met, any decision above you cannot carry out inside the editing constraints, or any tree mutation you did not intend, including your own — stop and report; do not retry with different flags, do not delete or create any ref to recover.

REPORT

- the directive-file commit SHA
- the content commit SHA, and the branch it is on
- the run-log path
- per decision D-0 to D-4, one line stating what changed and the line numbers as landed
- the four changed passages of skills/directive-invariants.md verbatim as landed
- suite counts, whole and per the five files named above
- check-frontmatter exit code and count
- the unfenced-label results for both files, and the byte-equality result
- anything observed this directive did not anticipate
- the worktree-removal status, as the final line

Label every claim observed, inferred, told, or unknown.
