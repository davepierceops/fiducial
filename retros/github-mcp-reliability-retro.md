# Retro: GitHub MCP Reliability Investigation (Aug 4–5, 2026)

## Summary

The investigation began with the belief that the GitHub MCP was "completely and utterly non-reliable" — constant intermittent timeouts blocking the chat→directive→Claude Code workflow. Two days of instrumentation and log forensics produced a different conclusion: the transport layer failed exactly once in three days of logs spanning two unrelated server implementations. "Unreliable MCP" decomposed into three distinct failure classes with different causes, different owners, and different fixes. None of them is the MCP server.

## What changed mechanically

The local `github-mcp-server` binary (Homebrew, v1.4→v1.8) was replaced with an `mcp-remote` shim pointing at GitHub's hosted remote server (`api.githubcopilot.com`), authenticated with a fine-grained PAT (Contents/Issues/PRs read-write, scoped repos) read from `~/.claudemcp.pat` at launch, toolsets trimmed via the `X-MCP-Toolsets` header. The swap did not fix the symptoms — which was itself the pivotal diagnostic: identical failures across two implementations sharing zero code ruled the server out and pointed the investigation at everything above and around it.

## The failure taxonomy

### Class 1 — Dispatched, executed, response lost

One specimen. A write dispatched at 02:19Z sat unanswered for exactly 240 seconds (Claude Desktop's tool-call timeout), was cancelled, and was reported to the chat as "timed out" — yet the write had landed on GitHub, verified by read-back. Rare (1 in ~three days of calls), and self-healing if the retry discipline is verify-before-retry rather than blind resend.

### Class 2 — Never dispatched

One specimen, caught live under the failure-report protocol. A read-only call waited four minutes and received a harness error ("No result received from the Claude Desktop app"), while the shim log for the bracketing window shows healthy sub-3-second calls on both sides of a traffic-free quiet period — no dispatch, and no cancellation notification either (Class 1 produced both). The call died inside Claude Desktop / the harness: Anthropic-side software, not network, GitHub, or shim. This class is invisible to every log below Desktop by construction, which is why it resisted diagnosis. Owed a bug report to Anthropic with the evidence package.

### Class 3 — Caller error

One specimen, and likely the volume leader historically. A write failed with a SHA mismatch because the session transcribed the hash incorrectly — the argument literally contained an ellipsis. The server rejected it quickly with the correct SHA in the error text; the session, operating under the protocol, self-diagnosed "my error, not the connection." Before the protocol, this event would have been narrated as "GitHub MCP failing again" and been indistinguishable from Classes 1–2.

## Theories killed, with the evidence that killed them

Server implementation (two implementations, same symptoms). Network path and NAT idle-teardown (probe showed healthy fresh connections during a failure; gap analysis showed calls completing normally after 1.3h and 2.4h idle periods). "The browser would work better" (no GitHub connector exists for claude.ai web; the local-process capability is Desktop's differentiator). Also killed: the assumption that instrumentation was installed because it was pasted — the stdio tap was believed live for a day before a file check showed it never was. Verify installs; `ls` is cheap.

## What worked and stays

**The session failure-report protocol.** On any apparent MCP failure: tool and args verbatim in a code block, exact error text quoted (or "no error text returned"), attempt number, no silent retries, read-back "landed/absent" before retrying writes, missing-tool reported as configuration rather than failure, facts without reliability commentary. It converted unreliable narration into evidence, and produced correct self-attribution on its first Class 3 encounter.

**Verify-before-retry on writes.** Timed-out writes usually landed. Blind retry risks double-commits; read-back costs one call.

**SHA discipline.** Hashes are copied verbatim from the immediately preceding read result, never reconstructed from context — a language model paraphrases hashes the way it paraphrases prose. The `write2gh` skill (fetch SHA before update, read error responses, recover from mismatches, mandated by role directive for all GitHub writes) is the enforcement layer; expected to cut write error rates dramatically.

**Least-privilege with cheap expansion.** Fine-grained PATs and toolset headers are editable in place; scoping tight and widening on demand cost ninety seconds when the PR toolset day came.

## Core lessons

The epistemics mattered more than the plumbing. "Failures" were, precisely stated, *Claude instances reporting failures* — a claim, not telemetry — and the investigation only progressed once that distinction was enforced. Perceived constant failure decomposed into rare real events of two kinds, one configuration gap presenting as flakiness, and caller errors presenting as infrastructure. Classification had to precede remedy; every fix proposed before the taxonomy existed (server swap, transport swap, version pin) targeted the wrong layer.

## Open items

Anthropic bug report for Class 2. Remove the stdio tee-taps from the Desktop config when the investigation closes. PAT rotation due ~early November (overwrite `~/.claudemcp.pat`, restart). Watch class frequencies under the protocol to confirm Class 3 dominates and Classes 1–2 stay rare.
