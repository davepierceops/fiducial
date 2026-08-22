# Directive — Pass 1, Cycle 23: specs templates, vendors, engagements

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Documents in scope, all @ 1bbd5b7:
- specs/prd-template.md
- specs/trd-template.md
- vendors/README.md
- vendors/claude-code/environment-config.md
- engagements/assistant.md
- engagements/cartographer.md
- engagements/skeptic.md
- engagements/quiet-notes.md

Rubric: docs/global-context/review-rubric.md @ 1bbd5b7, eleven criteria.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md — all @ 1bbd5b7, all through Pass 1. Read roles/context-quality-reviewer.md first: it is this session's role.
Prior context: docs/batons/baton-20260822T153848.md, "What this session settled" — in particular: engagement files carry role audiences, no client-shaped selector; harnesses are adapters downstream of bundles, no harness reads the repo; the SLO / Top K requirement has one home, operating-model's change package item 7.

## Context

Fiducial is a bundle compiler. Three file classes here, each with its own criterion-10 question:

Spec templates: a PRD or TRD template is instantiated per project, and the instantiated document is out of the frontmatter scope. Ask whether the template is agent context (selected into a bundle) or a human-facing form, and what audience: follows. Every rule a template restates from the foundation is a finding; a template that carries a rule carries it into every instantiated spec, where it drifts. Both templates are known to carry the SLO / Top K requirement.

Vendor files: the baton says no harness reads the repo. Ask whether each vendor file describes an adapter's environment (retained, audience human) or states methodology policy (a finding — policy lives in governed documents). vendors/README.md states the vendor swap test; judge whether that test has a better home in a foundation file.

Engagements: the four single files (assistant, cartographer, skeptic, quiet-notes) predate the engagement-files-carry-role-audiences rule. For each, answer: is this a role, a skill, a standing instruction to a session, or history; what audience: follows; does a role document already carry it. quiet-notes.md is 205 bytes; state what it is.

Retired terms: dispatch, sync block, track, prompt — every use is a finding under criterion 4. Vendor and model names are findings under criterion 8, except inside vendors/, where the vendor's own name is the subject; there, flag any second vendor or any model name.

## Instructions

1. Fetch origin; verify the tree contains 1bbd5b7 with no later edits to the eight files.
2. Read the role, the rubric, the baton section, and the five foundation files in full. Then the eight documents in full.
3. For each, answer criterion 10 first and explicitly: retain, retain-with-changes, retire, or merge-into (name the target), with the audience: that follows. Then all eleven criteria. The finding list is the edit list an executor can apply.
4. Count and flag: rules restated from the foundation; output-shape lists with a home elsewhere; path-shaped references; vendor and model names; retired terms; SLO / Top K copies.
5. Check the four engagement files against each other, against engagements/working-with-dave.md, and against the roles whose names they share (cartographer has no role; skeptic has roles/skeptic-risk-agent.md).
6. Known and out of scope: all-decision-roles is not yet a reserved audience value; docs/global-context/ is outside the frontmatter scope; the README unmatched-glob warning; references to deleted files in files outside this scope; everything under engagements/comfy/ (its own cycle); bin/ behaviour; CLAUDE.md and AGENTS.md (Pass 2). Do not report any of these.
7. Write one artifact per file per skills/review-artifact.md, filename reviews/<stem>-cycle-<n>.md where n is one more than the highest existing cycle for that stem in reviews/ (1 if none). Verdict first. Not inspected required.
8. Commit on branch p1-cycle-23-review, push to origin, open a pull request against main titled "Pass 1 cycle 23: eight review artifacts (specs, vendors, engagements)" via the REST API with curl if gh cannot authenticate; if neither works, report the compare URL. Do not merge. No edits to any document. No status flip. Report the SHA read back from git.

## Report shape

One line per file: path, criterion-10 disposition, proposed audience:, verdict, finding counts. Then branch, SHA, PR number or compare URL. Then one line each: what quiet-notes.md is; where the vendor swap test should live.
