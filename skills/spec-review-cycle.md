---
status: agreed
last-reviewed: reviews/agreeing-clusters-cycle-2.md @ ade5dad
audience: [spec-reviewer-agent, context-quality-reviewer, architect-agent, chief-of-staff, human]
---

# Skill: Spec Review Cycle

Triage and the directive run in a decision session; execution and verification
run in an execution session.

## Purpose

Execute one external-gate review cycle over a governed document.

## Use when

- an external reviewer agent has produced gate findings against one or more
  canonical documents
- the findings require triage and document revision

This skill governs the reviewer-gated cycle only. It does not govern
interactive co-authoring or artifact-pane review.

## Hard constraints

- **One conversation per cycle.** Each cycle starts a fresh conversation. Carry
  forward only reviewer findings and prior cycle directives — the directives
  are the decision record (rejections, dictated wording, deferred items).
- **Documents are read by the execution session from the repository.** Full
  documents are never carried through the decision session.
- **Reviewed commit SHAs are recorded in the directive.** This is the audit
  link from directive to reviewed state. A directive without SHAs is invalid.
  Which revisions those SHAs name mid-delta is stated per the Spec and Change
  Discipline context set.

## Inputs

- reviewer findings (self-contained report from the reviewer agent)
- the reviewed documents, at the commit the reviewer reviewed
- prior cycle directive, for continuity

## Procedure

### 1. Triage

1. Start a fresh conversation. Open with the reviewer findings and the reviewed
   commit SHA per document.
2. Triage each finding with Dave: **accept / reject / modify**. One finding
   at a time where judgment is required; batch the mechanical ones.
3. Record any wording or constraints Dave dictates verbatim.

### 2. Directive

4. Produce the cycle directive. It records one decision entry per finding,
   **including rejections** — a rejection recorded nowhere is a decision lost.
5. The cycle conversation is done. Do not continue into execution in it.

### 3. Execution

6. The SHA the executor reads back and reports for the landed directive is what
   the decision record cites.
7. The executor verifies the working tree matches the reviewed SHAs (or
   contains them in history with no intervening edits to the documents in
   scope); makes targeted edits per the directive; commits referencing the
   cycle number; pushes.

### 4. Verify and re-gate

8. Dave reviews the git diff — the human control surface.
9. Hand the revised documents back for the gate re-check, which is run by the
   role that gated. Findings from that re-check open the next cycle at step 1.
10. On Dave's go, the agreement flip lands as a frontmatter-only
    status-transition commit, `last-reviewed` naming the review artifact and
    the reviewed SHA. The SHA it cites must resolve to a recorded agreement
    entry.

## Reconciliation — the cycle that closes an open spec delta

1. Bring the spec to full agreement with what was actually built. Reconciliation
   is not a review of intentions — a spec that still describes something the
   tranche did not build is not reconciled.
2. Open a pull request from the tranche's spec branch to the default branch.
   What the gate fires over there is stated per the Commit and Change Control
   policy.
3. Run the cycle from step 1 of the Procedure, with the spec-branch SHAs as the
   reviewed revisions. Findings are triaged and executed against the spec
   branch; the pull request updates in place.
4. On a clean gate, the pull request merges, and **then** Dave's agreement lands
   on the default branch as it always does: a frontmatter-only status transition,
   `last-reviewed` citing the review artifact and the reviewed spec-branch SHA.
   The order is load-bearing. Flipping on the spec branch first would set
   `agreed` on a branch that has not merged and might not, which is precisely the
   claim this design exists to make impossible; and the cited SHA still resolves
   after the merge, being an ancestor of the default branch.
