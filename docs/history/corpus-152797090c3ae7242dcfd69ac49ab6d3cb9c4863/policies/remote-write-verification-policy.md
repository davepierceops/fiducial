---
status: agreed
last-reviewed: reviews/remote-write-verification-policy-cycle-8.md @ 21e0c1e729a689bf7e4687f7e5910f86f972ac48
audience: [all-roles, human]
---

# Policy: Remote Write Verification

This policy governs both session kinds: decision sessions and execution
sessions. Its rules govern any tool-mediated remote mutation, because the
failure is that a response is a claim about a write rather than evidence of one.

## The rules

### 1. The repository's own log is the source of record

Where a local clone exists, `git log` against the fetched remote is the
authority on what landed — not the tool's response, and not the agent's
recollection of what it sent. Where a project uses another version control
system, the rule is the same: the repository's own log is authoritative over the
tool's response.

State SHAs read from the log. Never invent one.

### 2. Two consecutive qualifying failures is a fact about the environment

A single transport failure is noise. **Two in a row is a signal** — the tooling
is degraded, or two concurrent sessions are contending for the same transport.
Stop, say so, and establish state before continuing. Do not absorb the second
failure as another retry.

- **Qualifying:** write timeouts; writes returning success but unconfirmable on
  read-back; transport errors (5xx, connection reset, connector absent
  mid-session).
- **Not qualifying:** auth/permission errors; not-found errors (almost always a
  wrong path or ref); any failure from the agent's own malformed call —
  including a write that lands but commits wrong content (rule 3).

**Counting.** Timed-out-but-confirmed-landed is not a failure; it resets the
count. Timed-out-and-confirmed-not-landed is one. A read-back that itself times
out is the second, and means state is unknown — that case fires immediately, at
the first failure, and nothing here may delay it.

The detector is kept for what it **detects**: a two-failure fire is how
contention between concurrent sessions gets noticed at all, and that diagnostic
value holds whatever the underlying cause turns out to be.

### 3. Landing and content are verified separately

Rules 1 and 2 verify that a write **landed**. Before reporting any
tool-mediated write, also verify that what landed is what was intended:

- compare the response's `size` field against the expected size of the content
  sent;
- read the landed commit's stats — files changed, insertions, deletions —
  against the expected blast radius of the change.

A mismatch on either is reported as a failed write, whatever the response said.
The case this catches: a call carrying a placeholder string as its content
parameter replaced a ~64KB file on the default branch with 19 bytes. The
response was success-shaped, the commit was real, and only the `size` field
disagreed with expectation.

### 4. A connector write is a create or a small verified diff

A **connector write** is a write made from a decision session through a tool
that commits directly to the remote, with no working tree. A connector write
creates a file or applies a small diff verified under rule 3. An existing
governed document is never regenerated whole over the connector. A change too
large for a small verified diff goes to an execution session against a working
tree.

### 5. A connector write of an in-scope file sets its frontmatter explicitly

The pre-commit hook does not run on a connector write. Any connector write of a
file in the document metadata policy's in-scope set — the set that policy's
Scope section names as frontmatter-required — sets every frontmatter field
explicitly, to the values that policy requires after the edit. Before the pull
request merges, an execution session runs `bin/check-frontmatter --all` on the
branch.

### 6. After a timeout, read state before re-creating

After a timeout or an unconfirmable response on any write, read the pull
request or commit state before re-creating anything. The re-create is
conditional on what the read shows: landed — continue from the landed state;
not landed — re-create once; the read itself fails — state is unknown, the
case rule 2's counting names. This is the per-write procedure rule 2's count is
built on.

### 7. A reported tool failure is classified before any remedy

Treat a reported tool failure as a claim by the session reporting it, not as
telemetry. Classify it before choosing any remedy, and let the remedy follow
the class:

- **Lost response** — the call may have reached the remote, and the write may
  have landed. Remedy: rule 6.
- **Never sent** — the call did not reach the remote; nothing landed. Remedy:
  send it again, counted under rule 2.
- **Caller error** — a malformed call, a wrong path, a wrong ref. Remedy:
  correct the call. A corrected call is a new write, not a retry.
- **Tool defect** — a well-formed call, and the tool did something other than
  what it reported. Remedy: stop and report; the session does not choose a
  workaround.

Lost response and never sent are what rule 2 counts. Caller error is what it
does not. A tool defect is a fact about the environment on its first instance
and needs no second.
