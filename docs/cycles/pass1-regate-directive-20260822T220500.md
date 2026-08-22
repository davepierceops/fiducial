# Directive — Pass 1 reconciliation re-gate

Date: 2026-08-22
Route: fresh
Model: frontier
Role: Context Quality Reviewer

## Working-tree rule

This session runs in a clone no other session is using. If any file this session did not change moves, or HEAD moves, or an index lock appears, stop and report; do not recover.

Starting state: main @ 8402c23. Every document in scope is read at this SHA.

Rubric: docs/global-context/review-rubric.md @ 8402c23, eleven criteria.
Foundation (criterion 4 is judged against their current text): docs/global-context/core.md, docs/global-context/decision-layer.md, LEXICON.md, operating-model.md, engagements/working-with-dave.md. Read roles/context-quality-reviewer.md first: it is this session's role.
Prior context: docs/batons/baton-20260822T212629.md in full; docs/cycles/pass1-cycle-26-writing-retire-20260822T220000.md, "Decision".

## Context

Pass 1 reviewed the corpus file by file across 26 cycles, each against the foundation as it stood that day. The foundation moved during the pass, files were retired, merged, renamed, and generalized, and three documents were produced by directive without ever being reviewed. This cycle is the whole-corpus read that no single cycle could do: every file at one SHA, against one foundation, against each other.

Two questions per file, in this order: does it still pass all eleven criteria at 8402c23; does anything it states collide with, duplicate, or contradict another file in the corpus. The second is what earlier cycles could not ask.

## Scope

The corpus is every non-code governed file: everything `bin/check-frontmatter --all` matches, plus docs/global-context/*.md, engagements/**/*.md, and prose-criteria.md (the latter three are outside the frontmatter scope by a known policy gap, not by intent). Enumerate the set first and record it in the reconciliation artifact; the set is evidence. Exclude docs/history/**, docs/batons/**, docs/cycles/**, reviews/**, retros/**, OPEN-ITEMS.md, BACKLOG*.md, decisions/log.md, README.md, CLAUDE.md, AGENTS.md.

Three files have never been rubric-reviewed and get a full first-cycle review, not a confirmation pass: engagements/sre/ (seven files, treated as one set with one artifact per file), roles/writer.md, prose-criteria.md.

## Instructions

1. Fetch origin; verify the tree is at 8402c23 with no later edits.
2. Read the role, the rubric, and the five foundation files in full. Then every file in scope in full. Do not skim; do not sample.
3. Confirmation pass, every file: all eleven criteria at the current foundation. A file that passed its own cycle and fails now is a finding, with the criterion and the foundation change that caused it.
4. Reconciliation sweep, corpus-wide, one table per check in the reconciliation artifact:
   a. Duplicate rules: any rule stated in two or more files. Name both locations; propose the one home.
   b. Contradictions: any two files that state incompatible rules or definitions. Name both; do not resolve.
   c. Term collisions: any term used with a meaning LEXICON does not give it, or a term LEXICON defines that a file uses differently. Include any term two files use for different things.
   d. Audience values: every distinct audience: value in use, with a file count; flag any used by exactly one file and any that names a retired role.
   e. Path-shaped references, corpus-wide, with the target's existence at 8402c23 (exists / deleted / renamed-to).
   f. Retired vocabulary, corpus-wide: dispatch, sync block, track, prompt, and every retired role name (editor, section-writer, instruction-reviewer, orchestrator, cartographer-as-role). Vendor and model names outside vendors/.
   g. Boundaries two roles could both claim (criterion 11), across the full role set including engagements/sre/ roles and roles/writer.md.
5. First-cycle reviews for the nine never-reviewed files, full artifact each, criterion 10 answered first.
6. Known and out of scope; do not report: all-decision-roles not yet reserved; docs/global-context/, engagements/**, and root prose-criteria.md outside the frontmatter scope; the README unmatched-glob warning; bin/ behaviour, including the unbuilt audience bundler; the two pre-existing bin/tests failures; references in docs/history/, docs/batons/, reviews/, retros/; CLAUDE.md and AGENTS.md; baton delivery having no home in Core.
7. Artifacts, per skills/review-artifact.md, verdict first, Not inspected required:
   - reviews/corpus-regate-cycle-1.md: the reconciliation artifact. Header, then the enumerated scope, then the seven sweep tables, then one line per confirmation-pass file: path, verdict. A clean file is one line; do not write a per-file artifact for a clean confirmation.
   - reviews/<stem>-cycle-<n>.md for every confirmation-pass file with at least one finding, n one more than the highest existing for that stem.
   - reviews/<stem>-cycle-1.md for each of the nine first-cycle files; engagements/sre/ stems are sre-<basename>.
8. Commit on branch p1-regate-review, push to origin, open a pull request against main titled "Pass 1 re-gate: reconciliation and first-cycle artifacts" via the REST API with curl. Do not merge. No edits to any document. No status flip. Report the SHA read back from git.

## Report shape

File count in scope. Confirmation pass: clean count, files with findings (path, finding count), one line each. Sweep: one line per check with the row count. First-cycle: one line per file, criterion-10 disposition, verdict, finding counts. Then branch, SHA, PR number. Then the single largest reconciliation problem, one line. Then anything that could not be executed as written.
