---
order: 70
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Decomposition

One decomposition doc per tranche, with its change packages as entries, produced
in a decision session. The doc carries no directives; a directive is written at
handover as its own file.

1. Read the agreed PRD and TRD in full.
2. Decompose a spec only after its branch has closed, pinning the
   default-branch SHA. While the branch is open, the only directive against
   the spec is the test suite's, to the Test Designer. Asked to decompose
   an open spec, propose closing it first.
3. Propose a breakdown into tranches, with rationale; the human approves, renames,
   or redraws, and his approved name slugs each tranche.
4. Before proposing a second concurrent tranche, check the claim on the documents it
   would touch [R0012, R0013]; never two deltas over one
   tranche. Where no disjoint territory is left, propose serial execution or send
   the second tranche cross-project.
5. For an approved tranche, decompose into change packages before any agentic work
   begins: the smallest independently executable units, in dependency order.
6. Flag any spec ambiguity that would force an agent to decide rather than escalate,
   and resolve it with the human first.
7. Write `docs/packages/<tranche>-decomposition.md`: the PRD and TRD SHAs derived
   from, the ordered package list, the sequencing rationale, the dependency map,
   and the flagged ambiguities with their resolutions.
8. Stop; the human's one approval of the ordered list ends this procedure.

Hand a package to an execution session as a directive derived from the decomposition
doc rather than from the spec, stating the acceptance criteria the package must
satisfy and the boundaries the session must not cross. A full spec is loaded in a
dedicated session; later tranche work references the doc. Before a tranche executes,
check whether the spec has moved past the SHAs its doc pins, and re-check the
affected packages against the current spec.
