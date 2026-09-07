---
order: 120
topic: [named-queries]
role: [chief-of-staff, release-manager-agent]
session: [decision]
corpus: [software, writing]
---

# Process: Named Queries

The list of bundles fiducial distributes and the order every bundle renders
in. Each list entry is one query over the store; a release attaches one
bundle per entry, generated at the release's SHA. This document is the one
place a bundle's definition and the render order live; the tool reads both
from the fenced blocks below and nothing else names them.

## The list

One bundle per role, named by the role's slug. The query is `role=<slug>`
and nothing more: a role's rows are whatever carries its value, and the
definitions those rows use follow by term. One line per bundle: the name,
then the query.

```text
chief-of-staff            role=chief-of-staff
architect-agent           role=architect-agent
spec-reviewer-agent       role=spec-reviewer-agent
test-designer-agent       role=test-designer-agent
coder-agent               role=coder-agent
reviewer-agent            role=reviewer-agent
skeptic-risk-agent        role=skeptic-risk-agent
release-manager-agent     role=release-manager-agent
context-quality-reviewer  role=context-quality-reviewer
writer                    role=writer
copy-editor               role=copy-editor
critic                    role=critic
```

A new role is a new line here and a new value on `role`; the tool does not
change.

## Sequence

A bundle is three bands: the rows, then the process documents, then the
definitions. Within the first band a row's `order` is its position within
its topic; the first block below is the position of topics, one position
per line, the topics on a line sharing it. Within the second band the
second block is the position of process documents, by stem. A topic or a
stem neither block names sorts after the last named one, alphabetically.
Definitions render last, always.

```text
core
chief-of-staff architect-agent spec-reviewer-agent test-designer coder-agent reviewer skeptic release-manager-agent context-quality-reviewer writer copy-editor critic
decision-layer
intake
change-flow convergence change-control commit-control
directive-invariants command-blocks remote-write-verification-policy
verification verification-boundaries human-review-boundary
review-artifact-schema retro decision-log-policy
public-prose-criteria voice trd prd-template
```

The second line holds the twelve role topics at one position: one per
bundle, and they never co-occur.

```text
change-flow
prd-template
trd-template
review-artifact
voice
outline
decomposition
spec-test-suite
retro
project-setup
decision-log
```

## Generating

Running `bin/bundle --where role=<slug> --name <slug>` on a synced clone
writes `fiducial-bundle-<slug>-<timestamp>Z.md` to `~/Downloads`. The file opens
with one line, an HTML comment naming the repository, HEAD and the
generation time; a session judges the bundle's age from HEAD.

## Releasing

A release is cut on the human's go at one SHA of `main` and tagged
as `v<YYYY>.<MM>.<DD>`. It attaches README.md and every bundle in the list,
each generated at that SHA and named `fiducial-bundle-<slug>.md`, and
nothing else. `bin/release` generates them and prints the `gh release
create` command; the human runs it. A bundle attached to a release is the
version of record for that role until the next release.

## Consuming

- A chat session loads its bundle as a project file, replaced at each
  release.
- A project repository's adapter vendors the bundle file at a pinned
  release tag and points the harness at it; the session reads, never
  fetches. Bumping the tag is the adoption of a release.
- Anyone else reaches a bundle by its release URL:
  `releases/latest/download/fiducial-bundle-<slug>.md`.

The store itself is not distributed. An agent needs its bundle, not the
rows.
