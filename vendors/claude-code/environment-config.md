---
status: agreed
last-reviewed: reviews/corpus-regate-cycle-1.md @ 8402c23
audience: [human]
---

# Claude Code — Environment Configuration

This file governs no session; it is for Dave, configuring a clone in which
Claude Code acts as the agent-runner. It records the intended `settings.json`
posture, which is not the posture the committed file currently carries — see
"Divergence" below.

## Posture

### Sandbox

```json
"sandbox": { "enabled": true, "autoAllowBashIfSandboxed": true }
```

```json
"allowUnsandboxedCommands": false
```

These two must be read together and neither changed alone: a configuration that
auto-allows sandboxed commands *and* permits unsandboxed ones has auto-allowed
everything.

### Credential denies

Read access denied to, at minimum:

- `~/.ssh/**`
- `.env`
- the credential file of whatever cloud provider this clone reaches

That last entry is a working set, not a fixed list: the deny must name the
actual path for the rule to execute, so it is extended as a clone reaches new
providers.

### Network allowlist

Outbound network access is allowlisted rather than open. The working set is the
hosts the job actually needs — package registries, the API endpoint, the git
forge, and whatever hosts the current task legitimately reaches.

### Push

```json
"ask": []
```

```json
"deny": ["Bash(git push --force*)"]
```

Nothing is asked; force-push is denied locally.

### Notification hook

A `Notification` hook fires when the session needs attention.

## Divergence from the committed file

`.claude/settings.json` on the default branch carries a single
`permissions.deny` array and nothing else:

```json
{
  "permissions": {
    "deny": [
      "Bash(git push --force*)",
      "Bash(git push -f*)",
      "Bash(git push * --force*)",
      "Bash(git push * -f *)",
      "Bash(git push * -f)",
      "Bash(rm -rf *)",
      "Read(.env)",
      "Read(~/.ssh/**)"
    ]
  }
}
```

It carries no `defaultMode`, no `allow` list, no `ask` list, no `sandbox` block,
no `allowUnsandboxedCommands`, no network allowlist, and no hooks. Against the
posture above it therefore diverges on the sandbox pair, the network allowlist,
the cloud-credential deny, and the notification hook. Its force-push deny is
broader than the single pattern above, covering five spellings. `git push` is
neither asked nor denied.

(`.claude/settings.local.json` is untracked and local-only, so an individual
clone may already be closer to this posture than the committed file is.)

## Scope boundary

The settings strings live here.
