---
order: 46
topic: [command-blocks]
role: [chief-of-staff]
session: [decision, execution]
corpus: [software, writing]
---

# Process: Command Blocks

Use before composing human-run shell commands or instructions for another agent session; ordinary internal tool calls do not trigger this skill.

Applies to chief-of-staff in decision and execution sessions, for software and writing.

## Compose and hand over the block

A block runs verbatim as pasted, with no manual step inside the fence: a manual step goes in prose outside it.

A command producing evidence captures its output to a named file with `tee` or equivalent, and the block or its surrounding instruction names the path; where a block's output is consumed in the moment and never cited, say so where the block is defined.

Name the remote and the ref in every sync or remote command a block runs, rather than leaning on branch-upstream configuration or an implied default. `origin` counts: it is a remote name.

Nothing downstream acts on the tree a sync produced until that sync's exit status has been checked; a bad sync fails loudly, with a non-zero exit.

A block pushes a branch, never the default branch; the decision session merges that branch through a pull request.

A block renders copyable whole in the surface that delivers it, with that surface's copy control intact; avoid constructs known to break the surface in use — a heredoc (`<<'EOF'`) suppresses the desktop copy control, so a multi-paragraph commit message is written as repeated `-m` flags.

Fence a block nested inside a paste block with `~~~`, preceded by a one-line fence note stating that the inner fence is `~~~` and why.

Where a human must relay output between blocks, send one block per turn: wait for the output, then compose the next.

A block carries no construct that can end the shell it is pasted into — `exit`, `exec`, `logout`, `|| { …; exit; }`, and `set -e` are known instances, not the extent of the rule; guard a precondition by branching (`if…elif…else…fi`) instead, so a failed check prints and the block ends without ending the session.

One purpose per block, and no placeholders in it: ask an unknown value as a question above the block rather than leaving a token for the reader to substitute.

Before handing over a block: every command in it is valid and non-harmful, and re-running it compounds no damage; it has been run end-to-end against a local stand-in for the remote, guard and re-run paths included, with any substituted value bound; its expected output is stated in one line below it — what was observed in the environment the block will run in, or qualitatively, what to look for, with no number — and its blast radius above it where it is destructive.

Write an execution block so the executor needs only the block and the repository, with no dependency on the conversation that produced it.

When handing off an execution block, put the block first, with no preceding prose.
