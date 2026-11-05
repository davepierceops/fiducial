---
order: 43
topic: [intake]
role: [chief-of-staff, context-quality-reviewer]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Intake

Carry a proposed change to governed context from proposal through review and
landing.
The judgment governing the proposal and its ruling is [R0166, R0462]; the
intake rubric is [R0264, R0266, R0284, R0950].

A durable rule lives in the store, never only in vendor tooling. An adapter is derived from it: update the store first, keep the adapter short, note every deliberate deviation.

1. **Proposal.** Collect the proposed wording or diff, its reason and evidence,
   and the affected rows or process documents.
2. **Candidate.** Create an `intake/<proposal-slug>` branch and apply the
   candidate change there. This is the branch observable used by R0934's
   governed-path hook. Tree-derived fields use [R1606, R1607].
3. **Review.** Give the candidate diff and proposal to a Context Quality
   Reviewer subagent, using the rubric cited above and the separation in
   [R0462]. For a process delta, use the process read and sign-off path
   [R1270]. The reviewer writes the artifact in
   `process/review-artifact.md`'s form.
4. **Disposition.** Bring the proposal and artifact to the human for any
   outstanding ruling [R0166, R1614]. Record each intake in its review
   artifact: the changes it lands, or the candidates refused and
   the rows against which they were refused.
5. **Landing.** Commit the approved change and its intake artifact on the
   intake branch, push plainly, and open the pull request. At merge, the
   decision session appends the ruling by `process/decision-log.md`; report
   the landed changes or refusal with the read-back evidence [R0172].

Provenance: DEC-001300, DEC-001320; R0944, R0934; retained judgment cited above.
