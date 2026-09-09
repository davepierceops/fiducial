---
status: agreed
last-reviewed: reviews/rule-divergence-rulings-cycle-2.md @ 3e064f6
audience: [context-quality-reviewer, chief-of-staff, human]
---

# Review Rubric — Fiducial Assembly, Pass 1 (prose)

Applied by the Context Quality Reviewer, an execution session.

Criteria every file in the Context Quality Reviewer's scope, as that role's
Scope rule states it, is examined against. A file passes when it satisfies all
twelve or is proposed for retirement. Findings cite the criterion number.

A criterion is a test for a stated rule and may name it; criterion 4 does not
apply to this file.

1. **Bundles are the product.** The file is written to be read inside a
   generated bundle, by an agent that has never seen the repository. Nothing
   in it assumes the reader can open another file.

2. **`audience:` is the selector.** The file carries `audience:` with at least
   one value from the known set, and `order:` if it must load before another
   file in the same bundle.

3. **No references to other files by path.** If the file needs something
   another file states, it states it. A path-shaped reference is a defect.
   A file whose subject is paths — a scope definition, a glob configuration —
   states them without defect.

4. **Core states it → remove it here.** The file does not restate a rule that
   Core or the Decision Layer already states.

5. **Agent instruction, not authoring principle.** Every rule is an instruction
   to the agent reading it.

6. **Instructions, not rationale.** Rules are stated; arguments for them are
   cut. "Never X" restatements of a stated rule and trailing justifications
   are cut.

7. **Session kind is explicit.** The file is for decision sessions, execution
   sessions, or both, and says nothing only the other kind needs.

8. **Tiers, not model names; route, model, and execution block, not track.**
   Model selection speaks in tiers. A directive states route, model, and the
   execution block. Track does not appear.

9. **Filenames are `<descriptor>-<timestamp>`.** Any filename the file
   prescribes or generates follows the convention, unless a stated convention
   names the file. No random strings, hashes, or UUIDs.

10. **The file earns its place or is retired.** It lands in at least one
    bundle and contributes something no other file in that bundle states.
    A file that fails this is proposed for retirement; retirement is Dave's.

11. **Escalation is not left to inference.** No wording lets the agent decide
    what is Dave's. Underspecified conditions, missing escalation triggers,
    language implying authority the methodology does not grant, and boundaries
    two roles could both claim are defects.

12. **The file contradicts no other governed file.** Where it states a fact, a
    definition, or a rule another governed file also states, it states it the
    same way. The reviewer names what was cross-checked. A disagreement is a
    defect, surfaced rather than resolved.
