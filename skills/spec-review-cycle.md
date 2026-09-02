---
status: in-review
last-reviewed: null
audience: [spec-reviewer-agent, context-quality-reviewer, architect-agent, test-designer-agent, chief-of-staff, human]
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
- **An exit gate's directive states its range.** Two labelled lines:
  `Baseline:` the status-transition commit that set `converging`, and
  `Reviewed:` the reviewed SHA. The gate reviews the diff between them; its
  artifact carries both lines.

## Inputs

- reviewer findings (self-contained report from the reviewer agent)
- the reviewed documents, at the commit the reviewer reviewed
- prior cycle directive, for continuity

## Loop start

The loop is the run of cycles over one document, from its first gate to its
agreement flip. At loop start, Dave states two things, and the opening
directive records both; they stand for every cycle in the loop unless Dave
restates them, and the cycle directive records the restatement as the opening
directive recorded the originals:

- **The agreement bar** — which verdict satisfies the flip: `ready`, or
  `ready-with-findings`. The document metadata policy admits either; the bar
  says which this document takes.
- **The gate cadence** — which revisions take a full-depth gate and which take
  a confirmation-scoped re-gate, as step 9 defines them.

## Procedure

### 1. Triage

1. Start a fresh conversation. Open with the reviewer findings and the reviewed
   commit SHA per document.
2. Triage each finding with Dave: **accept / reject / modify**. One finding
   at a time where judgment is required; batch the mechanical ones.
   - **A named defect class is triaged before its instances.** When the
     reviewer names a class and lists its instances, the class takes one
     ruling, and the instances dispose under it. No instance is triaged on
     its own ahead of the class ruling.
   - **A finding below the reviewed document's stage routes forward.** A
     PRD gate raising a TRD question, or a spec gate raising an
     implementation question, routes the finding to the loose-end tracker,
     where the next stage — the TRD, the change package — takes it up. It is
     not filed as a blocking finding against the reviewed document, and it
     does not bar the flip.
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
   cycle number; pushes; and discloses in its report any deviation from a
   disposition.

### 4. Verify and re-gate

8. Dave reviews the git diff — the human control surface.
9. Hand the revised documents back for the gate re-check, which is run by the
   role that gated. Findings from that re-check open the next cycle at step 1.
   - **A re-gate disposes the findings of the cycle it closes and takes no
     new decision.** A ruling that appears only in a review artifact is a
     decision lost; a new decision — a ruling, a change of bar, a change of
     scope — opens its own cycle at step 1, where the directive records it.
   - **A re-gate takes one of two forms**, and its directive and its artifact
     each state which. *Full-depth*: the whole document is read again.
     *Confirmation-scoped*: the gate reads the named resolutions of the cycle
     it closes and the revision's diff against the governed text it cites,
     and nothing else; it confirms that the resolutions landed as ruled, and
     files a finding outside them only when it is a new blocking
     contradiction the revision introduced.
10. On Dave's go, the agreement flip lands as a frontmatter-only
    status-transition commit, `last-reviewed` naming the review artifact and
    the reviewed SHA.

## Convergence — spec and tests before agreement

When tests are written against the document under review — a TRD and its
test suite — the document and the tests converge before the document is
agreed. This is the standard flow for such a document, not an exception.
`converging` is a status between `in-review` and `agreed`, and the interval
the document holds it; the loop runs in this shape:

1. **Entry.** After the document's first reviewer gate has run, whatever its
   verdict, Dave says the document enters `converging`. The transition lands
   as a frontmatter-only status-transition commit, and that commit is the
   entry point; nothing else records it.
2. **While `converging`.** The spec is edited freely, and the Test Designer
   writes tests against it; nothing is implemented against it. A content
   edit to a `converging` document changes neither its status nor its
   `last-reviewed`. Neither the spec nor the tests is final until they
   cohere: every testable claim the spec makes has a test asserting it, and
   every test asserts something the spec states. A test that had to invent a
   contract the spec does not state is a spec finding; a spec claim no test
   can be derived from is a test-side gap.
3. **Findings flow both ways.** A gate over the spec files findings against
   the tests where the tests encode something the spec does not say; the
   Test Designer's report files findings against the spec where the spec
   leaves a test underivable. Both go to triage at step 1 of the Procedure.
   The decision session is the mediating agent between the two execution
   sessions — the one revising the spec and the one writing the tests.
   Findings pass between them only through the decision session's triage and
   directives; neither execution session edits the other's artifact on its
   own judgment.
4. **Dispositions are intent.** The executor of a disposition verifies its
   edit against the counterparty's artifact — the tests when revising the
   spec, the spec when revising the tests — and discloses any deviation from
   the disposition in its report. A disposition found wrong on verification
   is corrected with disclosure, not absorbed.
5. **Exit gate.** When they cohere, one gate, run by the role that gated the
   document, reviews the diff from the entry point to the exit point together
   with the tests. Its directive states the range — `Baseline:` the
   transition commit that set `converging`, `Reviewed:` the reviewed SHA —
   and its artifact carries both lines. The Test Designer's red-gate result
   is the gate's evidence for the tests. Dave reads that diff before the
   flip.
6. **Exit is one ruling by Dave.** The spec flips `agreed` as step 10 has
   it — a frontmatter-only status-transition commit, `last-reviewed` naming
   the exit gate's artifact and the reviewed SHA. The tests' acceptance as
   red-gate evidence is recorded in that artifact, not in the flip commit.
   Neither lands without the other, and implementation begins only after
   both.

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
