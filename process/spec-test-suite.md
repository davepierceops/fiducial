---
order: 80
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Spec Test Suite

Before a spec closes, the only work run against it is writing its tests. Write
them against the spec as it stands; the suite is the evidence the close reads
[R1468, R1158]. Decomposition waits for the close.

1. Once the entry read has run over the open spec, whatever its verdict, and the
   human has said to proceed, direct a test-suite directive to a Test Designer
   execution session [R1101].
2. Derive the directive from the spec itself, never from a decomposition doc, and
   pin the spec's revision at handoff [R0474].
3. State that the tests it produces are the spec's suite, written under that
   directive and not under any change package [R0474].
4. Keep the directive to tests: it decomposes nothing and admits no
   implementation [R1153].
5. Triage in the decision session every finding the Test Designer files against
   the spec [R1155, R1476]; the close is a read over the whole diff and one
   ruling from the human [R0481], not a consequence of the suite existing.
