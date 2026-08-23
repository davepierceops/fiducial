---
status: agreed
last-reviewed: reviews/command-blocks-cycle-6.md @ cd7db71
audience: [all-roles, human]
---

# Skill: Command Blocks

This file governs both decision sessions and execution sessions.

A command block is a paste block whose content is shell commands intended to run
as given. It is not an execution block: an execution block is a paste block of
instructions an LLM agent session carries out, and it is never described as
executing or being executed. Command blocks are emitted in many contexts that
involve no directive at all.

**A block runs verbatim as pasted.** No manual steps inside a fence. A fence is
a paste contract, and a manual step inside one breaks it silently: it is either
skipped as a comment or it halts the block partway with no signal about which
half ran. Manual steps go in prose outside the fence, or into the directive file
if there is one.

**Blocks producing evidence capture output to a named file** (`tee` or
equivalent), and the block or its surrounding instruction names the path.
Output that only reaches the terminal scrolls and is gone. If the output is not
worth capturing, it was not evidence.

*Evidence* here is scoped: output that is cited later or that leaves the session
— a test run, a verification, anything a report will rest on. Output consumed
in-the-moment by the person running the block, and never referred to again, is
not evidence in this sense and needs no capture. A listing someone reads to
decide what to do next is the standard case — an `ls` before choosing which file
to act on, a `git status` before choosing whether to proceed. Where a document
emits such a block, it says so where the block is defined, so that a reviewer
running down these criteria is not left to guess whether the exemption was
claimed or forgotten.

**A sync or remote command names its remote and ref, and fails loudly.** State
both rather than leaning on branch-upstream configuration or an implied default:
a block runs in a clone whose config the author cannot see, and a `git pull`
resolved through the wrong upstream is silent about it. `origin` is a remote
*name*, not a protocol — it is a valid explicit remote and using it is fine.
What the rule is guarding is the other half: a bad sync fails loudly (non-zero
exit), so nothing downstream may act on the tree the sync produced without that
exit status having been checked. An unverified sync followed by unconditional
work is how a stale tree gets reported as current.

**The block must be copyable in the surface that delivers it.** A block the
reader cannot copy whole is not a paste block at all — a paste block is copied
whole and pasted whole, and a block that cannot be copied whole fails that
definition before any rule below applies. This failure is invisible from the
author's side: the text is well-formed, every command is valid, and the problem
appears only in rendering, which the author does not see. So avoid constructs
known to break the surface in use.

*Known instance, not the rule:* heredocs (`<<'EOF'`) suppress the desktop copy
control. Prefer repeated `-m` flags for multi-paragraph commit messages.

**Send one block per turn when a human must relay output between blocks.** Wait
for the output, then compose the next. A second block written before the first
has run is written against a guess at its output — batching does not merely
inconvenience the relay, it commits to an untested assumption and hides that it
did so. This binds blocks handed to a human intermediary; it does not bind a
sequence an agent runs itself with no one in the loop.

**A block pasted into an interactive shell must not terminate it.** The rule is
stated by effect: no construct that can end the shell the block runs in — on
most terminals closing its window. Guard preconditions by branching
(`if…elif…else…fi`) so a failed check prints and the block ends without ending
the session.

*Known instances, not the rule:* `exit`, `exec`, `logout`, `|| { …; exit; }`,
and `set -e` — which ends an interactive shell on the next failing command
exactly as `exit` does, while being the idiomatic opening line of a careful
multi-command block.

**One purpose per block, and no placeholders.** An unknown value is a question
asked above the block, not a token the reader is expected to substitute.

**State the expected output in one line below the block**, and where the block
is destructive, state its blast radius above it.

## Conformance criteria

Every command block satisfies all nine. An untested block is still a command
block, and still non-conformant.

- Every command is valid and non-harmful.
- Every command runs safely as given, with no manual step inside the fence.
- The whole is safe to re-run: re-running does not compound damage, and an
  append is guarded by the entry's own marker. (*Safe to re-run*, not
  *idempotent* — a block containing a commit, an issue creation, or an append
  to a log cannot be idempotent, and demanding it would make the rule
  unfollowable.)
- Any command producing evidence captures its output to a named path, where
  *evidence* is output cited later or leaving the session.
- The block renders with its delivery surface's copy control intact.
- The block cannot terminate the shell it is pasted into — no construct with
  that effect. Known instances: `exit`, `exec`, `logout`, `|| { …; exit; }`,
  `set -e`. Preconditions fall through via `if…elif…else…fi`.
- Every sync or remote command names its remote and ref, and its exit status is
  checked before anything downstream acts on the result.
- The block has one purpose and carries no placeholders.
- The expected output is stated in one line below the block, and the blast
  radius above it where the block is destructive.
