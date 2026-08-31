---
project: fiducial
date: 2026-08-31
source: Chief of Staff decision session, main 6e80742 → a3acb75 (PRs #214–#217)
---

# Retro — fiducial — 2026-08-31

## Context

Chief of Staff session opened on a baton with three candidate next steps. Dave chose the cheap one first (untag three specs from the all-roles floor), then the large one (collapse the 69 "agreeing" rule clusters from Pass 2). The collapse ran as two execution directives on one branch, one CQR gate cycle with three findings, one fix directive, one re-gate, then 26 frontmatter flips. Four PRs merged; CoS bundle went from 8,946 lines to 3,217.

## Evidence

1. The sandbox probe before the audience-untag block established two facts the directive depended on: the hook does not flip status on an audience-only edit, and the bundle drops to 3,289 lines. Both were stated as observed in the message that asked Dave for his ruling.
2. Dave rejected a two-word path guess (`~/fiducial`) with "dude". The correct path was already in memory as `~/code/fiducial`; the block was drafted from a guess anyway.
3. The first collapse directive introduced a bundle invariant (a rule may leave file A only if home B's audience covers A's). The executor applied it, left five clusters, and reported the uncovered audience value for each.
4. The executor found 35 of 69 "agreeing" clusters were not duplicates on reading: counted checklists restating their own prose, and lexicon definitions clustered with rules that use the term. Net size win from the collapse was 70 lines against a Pass 2 claim of "a quarter of the corpus."
5. Dave's reaction to the first report was that it was too big; his reaction to the first triage item was that he could not tell what it was. The rewrite that landed explained the item in plain terms before restating the choice.
6. Dave overrode the CoS recommendation on C049–C051 (leave duplicated) with "I can't think of any benefit" to other roles reading the CoS procedure. Ruling: cut.
7. Dave asked why F3 restored a sentence rather than deleting the section; the CoS checked for numbered cross-references in the sandbox, found none, and the ruling became delete.
8. Dave raised, unprompted, that rubric criteria 3, 4, 6, 11, 12 are absence tests and that negated framing may introduce what it forbids. Queued as a candidate methodology change.
9. The CQR gate found one blocking defect the collapse had introduced: the CQR role doc lost the sentence ceding specs to the Spec Reviewer, so its scope claimed everything.
10. The re-gate executor ran `git checkout <sha> -- .` in its tree by mistake, undid it, and continued rather than stopping. HEAD never moved. It reported the event and noted the stop condition was worded on effect, not cause.
11. Two directives were routed to the existing execution session on the same worktree (SOLE TREE disposition). Both landed clean; the second (cycle-2 fixes) took under three minutes.
12. Every flip block was dry-run in the sandbox against a probe branch before delivery. Zero failures; the dry run cost one tool call.
13. Dave asked what the twelve rubric criteria were while waiting on the gate. The directive had said "apply all twelve rubric criteria" without naming them.

## Interpretation

- (4, 6) Pass 2 clustering is text-similarity, not rule-identity. The read-before-collapse instruction was the control that caught it; without it the executor would have deleted 7 of command-blocks' 9 conformance criteria. Rule-dedup tooling needs a "same rule on reading" gate before "same text" is acted on.
- (3, 9) The bundle invariant did its job for the deletion side, and the gate did its job for the one deletion the invariant could not see (a qualifying sentence inside a rule that was itself kept). Two independent controls, each catching what the other missed.
- (2) A memory fact existed and was not consulted before emitting a block. Core rule 8 (read; do not recall) applies to the CoS's own memory as much as to the repository.
- (5, 13) Terse triage fails when the item's identity is assumed. Dave's register preference is terse *after* he knows what the thing is; the first line about any item has to say what it is.
- (6, 7) Both overrides were Dave seeing a simpler answer than the CoS recommended. The CoS was defaulting to "preserve" where "delete" was correct. Bias worth naming: recommending the conservative edit when the reviewer has already established the rule survives elsewhere.
- (10) The self-recovery defect class recurred with a new shape: the mutation was the executor's own. The stop condition as written was arguably satisfied and the executor argued its way out. Wording that names "any mutation you did not intend, including your own" closes the argument.
- (11, 12) Existing-session routing and sandbox dry-runs are both cheap and both worked. Neither is written down anywhere but the baton.

## Durable insights

- Before any collapse of "duplicate" rules, the executor reads every cited row and confirms same-rule, not same-text; divergent-on-reading is a first-class disposition.
- A rule may be removed from a file only if its home's audience covers that file's audience (bundle invariant). Duplicates across non-overlapping bundles are legitimate.
- Dry-run every block Dave will paste in the sandbox first when the sandbox can run it.
- The first sentence of any triage item states what the item is; the choice comes second.
- When the CoS has a fact in memory (paths, names), it reads it before drafting; a guess with a memory fact available is a Core rule 8 violation.

## Candidate methodology changes

- review-rubric.md: restate criteria 3, 4, 6, 11, 12 affirmatively; audit core.md and decision-layer.md for the same pattern. Full cycle.
- skills/spec-review-cycle.md and skills/review-artifact.md: add the multi-document reconciliation cycle (artifact stem names the branch; `Reviewed:` lists documents). Practice has run ahead of the skill three times.
- Add the bundle invariant to the rubric (criterion 4 or 12) or to a dedup skill if one is written.
- skills/directive-authoring.md: stop conditions name unintended mutation of any cause, including the executor's own; a self-recovery is a stop.
- A directive that says "apply all N criteria" names or points at them; the executor loads the rubric from its bundle, but the directive should still say which file.
