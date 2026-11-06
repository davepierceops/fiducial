---
order: 41
topic: [gate]
role: [chief-of-staff, release-manager-agent]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Gate

Prepare the human's gate request from an assembled change package.
Classification and authority are [R0534, R0535, R0562]; the release
boundary is [R0490].

1. Open one tracker issue for the pending change and label it `human-gate`.
   Derive its body from the change package using the template below; re-derive
   any field that has drifted from its source.
2. Link the issue from the change package. Before presenting the change,
   confirm that the issue is open and linked.
3. Announce the pending gate in chat with the notification template below.
4. If the issue could not be opened, keep its derived body in the change
   package and present that body in place of the issue pointer in chat. Hold
   the change short of release until the issue can be opened and linked.

For the Chief of Staff in decision sessions:

Take the `human-gate` issue as canonical for the existence and state of a pending gate, and the change package as canonical for its evidence.

## Issue body

~~~markdown
Intent: <from the change package>
Evidence summary: <from the change package>
Verification boundary: <from the change package>
Known gaps: <from the change package>
Blocked until a go: <the release or other gated action>
~~~

## Chat notification

`<change> is in the consequential class; gate: <issue pointer>. Go/no-go?`

Keep evidence in the issue body. When opening the issue failed, substitute
the full derived body for `<issue pointer>`.

Provenance: DEC-001280; R0551, R0552, R0553, R0558, R0560, R1039, R0505; retained judgment cited above.
