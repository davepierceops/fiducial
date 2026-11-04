---
name: project-status
description: Assess a project's current work, recent changes, pending decisions, and next step when the user asks for project status or orientation. Starting a Chief of Staff session alone does not trigger this skill.
---

# Project Status

Use the project's available evidence to give the user a current picture and a
proposed next step. Keep the assessment within the project and scope requested.

## Gather the state

Identify the project from the request and available context. Ask only if the
target is unclear. Use the project's established tracker and repository tools;
the skill does not require a particular host, connector, or tracker.

For a full status assessment, inspect:

- The project's issue tracker, including open work, blockers, and pending human
  decisions or review gates. On GitHub, these are Issues and Milestones; pending
  gates may carry a `human-gate` label.
- Recent commits on the default branch and branches on the remote that are ahead
  of it. Establish the default branch from repository metadata.
- Work known to be running in other sessions and local worktrees. Include
  connector ownership or contention only when a shared connector is in use.
- Every untracked file under `retros/` in the relevant local clone, so unfinished
  retrospective intake remains visible.

Use read-only inspection. Refresh remote evidence when access is available;
distinguish fresh remote observations from cached refs, local state, and reports
from the user. An unavailable tracker or session inventory is unknown, not empty.
If access is missing, give the useful partial assessment and name the gap.

## Report the status

Summarize active work, recent changes, pending decisions, and relevant loose ends,
including untracked retros by path. Identify evidence sources and material gaps,
then propose the next useful step. For a focused status question, report the
requested slice rather than a full project inventory.

The assessment does not itself change issues, acquire connector ownership,
commit retros, merge branches, or start the proposed work. Those actions follow
the user's instructions and the project's existing workflow.
