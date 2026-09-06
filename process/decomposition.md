---
order: 70
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Decomposition

**Status of this draft:** proposal for Dave's correction, 2026-09-06. Written
under the gate DEC-000380 sets for a process document: one frontier read against
the rows it cites, then Dave's sign-off, recorded as a decision-log entry naming
the SHA. It is drawn from `roles/chief-of-staff.md` @ fd54448 and from the store
rows R0901–R0916 and R0925–R0930, which retire into it.

## The principle

**A decomposition is derived from a closed spec, and it derives nothing but an
ordered list Dave approves once.**

The decomposition doc is a tranche's durable artifact. It carries no directives:
a directive is written at handover and lands in git as its own file. Because the
doc is derived, it drifts — so it records the spec SHAs it derived from, and
movement past them is a staleness signal.

## The sequence

One decomposition doc per tranche, with the change packages as entries within
it. The whole procedure runs in a decision session; execution belongs to an
execution session.

1. **Read the agreed PRD and TRD in full.** A proposal derives from whole-spec
   comprehension, not a fragment.
2. **Decompose only from a closed spec.** While a spec branch is open, the one
   act admitted against it is the test-suite directive to a Test Designer
   (`process/spec-test-suite.md`), and nothing else in this procedure. Where a
   delta is open over the spec a proposed decomposition would derive from, say
   so and propose reconciliation as the next step instead. A decomposition
   derived from ungated text propagates an ungated decision into every package
   beneath it; this is why the SHAs a decomposition doc pins are always
   default-branch SHAs.
3. **Propose a breakdown into tranches, with rationale.** Dave approves,
   renames, or redraws; his approved name slugs each tranche.
4. **Before proposing a second concurrent tranche, check the claim** on the
   documents it would touch. At most two tranches run at once, and only over
   disjoint spec territory. Where the territory overlaps, propose serial
   execution or a different project.
5. **For an approved tranche, decompose into change packages** before any
   agentic work on the tranche begins: the smallest independently executable
   units, in dependency order.
6. **Flag any spec ambiguity that would force an agent to decide rather than
   escalate**, and resolve it with Dave first.
7. **Write `docs/packages/<tranche>-decomposition.md`**: the PRD and TRD SHAs it
   derived from, the ordered package list, the sequencing rationale, the
   dependency map, and the flagged ambiguities with their resolutions.
8. **Stop.** Dave approves the ordered list in one approval — his to reorder,
   merge, split, or drop — and that approval ends this procedure.

## Handover

A package is handed to an execution session as a directive derived from the
decomposition doc, not from the spec. The directive states the acceptance
criteria the package must satisfy and the boundaries the execution session must
not cross. A full spec is loaded in a dedicated session; later tranche work
references the decomposition doc, not the spec.

Before a tranche executes, check whether the spec has moved past the SHAs its
decomposition doc pins, and re-check the affected packages against the current
spec. How strict that re-check is — block or flag — is deliberately unsettled,
to be learned by doing. Acceptance criteria are a separate execution-time input,
not part of what a decomposition doc pins.

## What this does not decide

- **Whether the breakdown is right.** The Chief of Staff proposes; Dave
  approves, reorders, merges, splits, or drops. The proposal is not the
  decision.
- **Anything a spec ambiguity turns on.** An ambiguity that would force an agent
  to decide goes to Dave before the decomposition is written, not into a package
  as an instruction.
- **How strict the staleness re-check is.** Left open on purpose.
- **What a package's implementation looks like.** That is the execution
  session's, under the directive.
