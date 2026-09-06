---
order: 100
role: [chief-of-staff]
session: [decision]
corpus: [software]
---

# Process: Project Setup

**Status of this draft:** proposal for Dave's correction, 2026-09-06. Written
under the gate DEC-000380 sets for a process document: one frontier read against
the rows it cites, then Dave's sign-off, recorded as a decision-log entry naming
the SHA. It is drawn from `policies/project-setup-requirements.md` and
`policies/commit-and-change-control-policy.md` @ fd54448 and from the store rows
R0566, R0568, R0703 and R0705, which retire into it.

## The principle

**An adoption precondition is something that must be true about a repository
before the methodology governs work in it — not a day-to-day rule.**

These preconditions live outside git, in the forge's configuration and in the
agent runner's. Git cannot record them and no hook can enforce them, so they are
written down and a human confirms them. Confirming them is the human's, once per
repository, before either session kind begins work in it.

## The checklist

1. **Branch protection on the default branch.** In the forge's configuration,
   `main` — or whatever the repo's default branch is — is protected:
   - no force-push
   - no branch deletion
   - changes land only through a pull request
   - no bypass, including for administrators

   The last one carries the others. This is the structural gate: it is what
   makes "agents may push and merge" safe to say, because history on the default
   branch cannot be rewritten or destroyed, whoever holds the credential.
   Branch protection lives in the forge, not in the repository; nothing in the
   repository can verify it, so a human confirms it at adoption.

2. **A force-push deny in the agent runner.** The runner's configuration denies
   force-push, and the deny holds in every permission mode, including the modes
   that otherwise skip prompting. A deny a permissive mode waives is not a deny.

The two layers are deliberate: the forge binds every credential that reaches the
repository, including ones no local configuration has ever seen, and the runner
binds the session before the credential is used. Neither alone is enough.

## What this does not decide

- **Whether the repository is ready for work.** The Chief of Staff confirms the
  preconditions hold and says so; a precondition that does not hold is reported,
  not worked around.
- **Anything a session does after adoption.** The day-to-day rules are rows in
  the store; this document is the one-time gate in front of them.
