---
order: 80
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Spec Test Suite

**Status of this draft:** proposal for Dave's correction, 2026-09-06. Written
under the gate DEC-000380 sets for a process document: one frontier read against
the rows it cites, then Dave's sign-off, recorded as a decision-log entry naming
the SHA. It is drawn from `roles/chief-of-staff.md` @ fd54448 and from the store
rows R0917–R0923, which retire into it.

## The principle

**One act runs against a spec before it closes: the tests are written against
the spec as it stands.**

Everything else in the decomposition procedure waits on the spec closing agreed.
This one does not, because the suite is the evidence the close reads — the
red-gate the Spec Reviewer takes with the diff.

## The sequence

1. **Wait for the entry read.** Once the entry read has run over the open spec —
   whatever its verdict — and Dave has said to proceed, direct a test-suite
   directive to a Test Designer execution session.
2. **Derive the directive from the spec itself**, never from a decomposition
   doc. There is no decomposition yet; there cannot be one, because the spec is
   open.
3. **Pin the spec's revision at handoff** in the directive.
4. **State that the tests it produces are the spec's suite**, written under that
   directive and not under any change package. The Test Designer's work here
   belongs to the directive, not to a package.
5. **Keep the directive to tests.** It decomposes nothing and admits no
   implementation.
6. **Triage in the decision session every finding the Test Designer files
   against the spec.** Findings return here, not to the execution session that
   raised them.

## What this does not decide

- **Whether the spec is right.** A finding against the spec is triaged in the
  decision session and settled by Dave; the Test Designer does not edit the
  spec, and this directive does not authorize an edit to it.
- **When the spec closes.** The close is a read over the whole diff and one
  ruling from Dave, not a consequence of the suite existing.
- **Anything about implementation.** No package, no code, no schedule.
