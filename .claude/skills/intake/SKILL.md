---
name: intake
description: Carry a proposed change to governed context from proposal through review and landing.
---
<!-- fiducial:begin -->
# Process: Intake

Carry a proposed change to governed context from proposal through review and
landing.
The judgment governing the proposal and its ruling is [R0166, R0462]; the
intake rubric is [R0264, R0266, R1621].

For chief-of-staff and coder-agent in software and writing decision and execution sessions, when creating or changing a vendor-specific artifact:

A durable rule lives in the store, never only in vendor tooling. An adapter is derived from it: update the store first, keep the adapter short, note every deliberate deviation.

The intake steps below apply to chief-of-staff and context-quality-reviewer in software and writing decision and execution sessions.

1. **Proposal.** Collect the proposed wording or diff, its reason and evidence,
   and the affected rows or process documents.
2. **Candidate.** Create an `intake/<proposal-slug>` branch and apply the
   candidate change there. This is the branch observable used by R0934's
   governed-path hook.
3. **Review.** Give the candidate diff and proposal to a Context Quality
   Reviewer subagent, using the rubric cited above and the separation in
   [R0462]. For a process delta, use the process read and sign-off path
   [R1270]. The reviewer writes the artifact in
   `process/review-artifact.md`'s form.
4. **Disposition.** Bring the proposal and artifact to the human for any
   outstanding ruling [R0166]. Apply the review dispositions in
   `process/change-flow.md`. Record each intake in its review
   artifact: the changes it lands, or the candidates refused and
   the rows against which they were refused.
5. **Landing.** Commit the approved change and its intake artifact on the
   intake branch, push plainly, and open the pull request. At merge, the
   decision session appends the ruling by `process/decision-log.md`; report
   the landed changes or refusal with the read-back evidence [R0172].

Provenance: DEC-001300, DEC-001320; R0944, R0934; retained judgment cited above.

## Rules

Cite a row by its ID in square brackets only if it covers every role, session, and corpus of the citing row.

### Definitions

**decision session** — A decision session triages, decides, and produces the artifacts that direct and record work — plans, subagent prompts, session records, tracker updates. It reads freely and writes those artifacts; the changes a plan specifies happen elsewhere, in the session that runs it. The boundary is role in the flow, not capability: a decision session may hold a clone and may commit.
<!-- fiducial:end -->
