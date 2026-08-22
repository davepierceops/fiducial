---
status: draft
last-reviewed: null
audience: [cartographer, assistant, human]
---

# Skill: System Discovery

This skill runs in an execution session.

Procedure for building the System Map of a client pipeline. Executed by the
Cartographer.

## Procedure

1. **Inventory the sources.** Repositories, workflow files, Terraform or
   equivalent, container image definitions, delivery pipelines, dashboards,
   runbooks, and any statements client humans have made (as relayed by Dave).
   List what exists before reading deeply.
2. **Reconstruct the pipeline under study.** From trigger to ready: what event
   starts it, what stages execute, in what order, on what infrastructure, with
   what dependencies between them. Cite the file and line that establishes each
   link.
3. **Tag every claim** with its provenance. The unknowns become the question
   list for Dave.
4. **Identify the measurement points.** For each stage: where would a timestamp
   come from — existing logs, CI APIs, workflow annotations? Prefer measurement
   that requires no changes at all; then measurement requiring only PR-able
   changes; flag anything that would need write access.
5. **Render the map.** One document: pipeline narrative, stage table, claim
   provenance, unknowns, proposed measurement plan. Small enough to read in one
   sitting; everything else links out.

## Output

The System Map, in the engagement working area — a client-hosted repository
designated at kickoff — plus the unknowns list ready for the Assistant's
triage. The map is a living document: corrections from later evidence amend it,
and amendments note what earlier belief they replaced.

## Failure modes to avoid

- letting the map editorialize; recommendations belong to proposals, not maps
