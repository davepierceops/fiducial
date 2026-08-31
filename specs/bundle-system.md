---
status: draft
last-reviewed: null
audience: [human]
---

# PRD: Context Bundle System

## 1. Problem and intent

Every agent session — decision or execution, any model, any vendor — starts
from a bundle: the governed text it needs and nothing else. The bundle is the
product; the repository is where it is made. Today the product is wrong in
five ways, each observed at `main` 6e77040 unless stated otherwise.

**The unit of authoring is the file, and a file is a bag of rules.** A bundle
that needs one rule from a file gets the whole file. The rule register from
the dedup passes counted 878 rules across the corpus; a bundle is assembled at
file granularity, so review-rubric criterion 10 — every member earns its
place — is applied per file, never per rule.

**Selection by `audience:` alone over-selects.** `bin/bundle --audience
writer` emits 22 files and about 15,000 words. The set Dave ruled for the
Writer is 6 files and about 3,800 words: Core, the Decision Layer, the role,
the Public Prose Criteria, the Voice document, the Outline skill. The other 16
are software-delivery material carried in by the `all-roles` floor — 17
files that every audience receives, including the release-readiness policy,
the project-setup policy, and three engineering context sets — which a
writer never uses. The Chief of Staff bundle is 33 files. Size degrades the
bundle: a rule nobody follows because it is one of a thousand is not a rule;
it is noise degrading the others.

**The bundle carries no provenance a consumer can act on.** The header names
the repository, the HEAD, and a generation time. It does not say how far
behind the default branch the bundle is, and nothing says when a bundle must
be regenerated. A gate directive in August cited a path from a bundle three
weeks stale, and the stale path was the reviewer's first finding. Two of the
retrospectives in this repository's corpus ask for the stamp; six ask for
regeneration on rename, flip, or audience change.

**Two conventions describe one output.** The decision that fixed the file-set
rule carried forward a filename and header from the prior hand procedure —
`methodology-context-bundle-<stamp>.md`, a `Source: @ <HEAD>` line — while
`bin/bundle` writes `bundle-<audience>-<stamp>.md` with `# bundle-<audience>`.
The writing bundles hand-built on 2026-08-30 were built to the tool's header
so that hand-built and generated bundles interchange. One output cannot
satisfy both; the conflict is a decision this document must record.

**The corpus is portable; its edges are not.** The governed text is
vendor-neutral. What is not neutral is how a session reaches it: sandbox
mechanics and connector behaviour are carried per directive because they have
no home, a writer who is not a repository user has no way to obtain a bundle
except by asking Dave, and an adopting project has no stated way to reach
the corpus at all — the one adapter that existed restated ten rules and was
deleted for it.

The intent: one command on Dave's Mac emits the right bundle for any role in
any audience, small enough to be followed, carrying what a consumer needs to
judge its freshness; a writer or an adopting project obtains the same file
from a release without touching the repository; and nothing built now
forecloses a rule-granular end state.

## 2. Users and use cases

- **Dave, operator.** Regenerates bundles after methodology changes; uploads
  one per project; cuts a release for writers. Wants one command and one
  directory.
- **Agent sessions — decision and execution, any model.** Load a bundle as
  their first act. Need the governed text for their role, in load order, and
  a header that says what it was made from and how old it is.
- **Writers who are not repository users.** Have a document and a chat and
  nothing else. Download one file from one URL and paste it; never see git.
- **Adopting projects.** A project repository applying this methodology
  needs a stated way to reach the corpus that restates no rule.
- **Methodology authors.** Add a governed file, or a rule, and expect it to
  join the right bundles by tagging — one change in one place.

## 3. User journeys

### J1 — Dave regenerates a bundle after a methodology change

- **Actor:** Dave, at a synced clone on his Mac.
- **Trigger:** a governed file was agreed, renamed, or re-tagged; a project's
  uploaded bundle is stale.
- **Steps:** one command names the audience; the tool syncs or refuses on an
  unsynced tree, assembles the set, and writes one file to `~/Downloads`
  named to sort to the top. Dave uploads it to the project, deleting the
  prior one.
- **Expected outcome:** the file is the audience's set and nothing else, and
  its header names the repository, the HEAD, the generation time, and every
  member with its blob.

### J2 — an agent session judges the freshness of its bundle

- **Actor:** any agent session, loading a bundle as its first act.
- **Trigger:** the session is about to cite a path, a rule, or a count from
  the bundle.
- **Steps:** the session reads the bundle header; where it can reach the
  repository it computes commits behind the default branch from the HEAD
  stamped there; where it cannot, it states the generation time as the
  bound on what it knows.
- **Expected outcome:** a stale bundle is named as stale before anything is
  cited from it, and a directive derived from it pins the bundle's HEAD as
  the revision it read.

### J3 — a writer obtains a writing bundle

- **Actor:** a writer with a document and a chat.
- **Trigger:** starting a Writer, Copy Editor, or Critic session.
- **Steps:** opens the repository's latest release, downloads the one file
  named for the role, pastes it into a fresh chat with the role's word.
- **Expected outcome:** the session behaves as the role document specifies,
  with the Criteria and the Voice document present; a new author also finds
  the Voice template in the release.

### J4 — an author adds a governed file

- **Actor:** a methodology author, in a review cycle.
- **Trigger:** a new role, skill, or criteria document is agreed — a fourth
  writing role, say.
- **Steps:** the file carries a complete, deliberate `audience:` and, where
  load position matters, `order:`; nothing else is edited.
- **Expected outcome:** the next generation of every bundle whose audience
  the file names includes it, in the right position, and no bundle that
  should not carry it does.

### J5 — an adopting project reaches the corpus

- **Actor:** an agent session in a project repository that applies this
  methodology.
- **Trigger:** the session's first act.
- **Steps:** the project states, in one place, which bundle its sessions load
  and at which release; the session obtains it by the same route a writer
  does.
- **Expected outcome:** the project carries no restated rule and no
  vendor-shaped adapter; changing methodology changes the release the
  project points at, not the project.

## 4. Goals and non-goals

### The end state, as a design constraint

A **row** is one rule, with at minimum: a stable `id` cited by other rows and
by decisions; an `agent` form — the instruction, nothing extra; an optional
`human` form — the rationale; an `audience`; an `order`; a `status`; and a
`source`. A bundle for audience *A* is the set of rows whose audience
includes *A*, in order, rendered in agent form, with provenance in the
header. Files are one store for rows; a database is another; the model is
the same either way. Nothing this document requires may foreclose that model,
and the store is decided after the audit below says how many rows there are.

### Delivery shape

Delivery is incremental and file-based, in this order; each step is a
package under this document and lands on evidence.

1. **Audit.** Inventory every file that can enter any bundle; per file, keep,
   merge, split, or retire, applying criterion 10 per file now and per rule
   where a file is plainly a bag; dedup against Core and the Decision Layer.
2. **Tag.** Every governed file carries a complete, deliberate `audience:`;
   nothing is left to inference; the `all-roles` floor is what every session
   needs and nothing else.
3. **Select.** The selection mechanism this document names produces exactly
   the ruled writing sets and a Chief of Staff set the audit confirms.
4. **Stamp and deliver.** Provenance and staleness in the header; the
   filename and header decided; one command on the Mac; releases.
5. **Reach.** The adopting-project route and the lore home.

Invariants held from step 1: no rule is restated in two files — a file that
needs another file's rule cites it by identity; no `audience:` is left to
inference; human-form text cut from an agent-facing file moves to a named
companion with a `human` audience, never to nowhere.

### Functional goals

- **G1 — One command.** From a synced clone on Dave's Mac, one command emits
  the bundle for any audience value and writes it to `~/Downloads`, named to
  sort to the top. An unsynced tree is refused, not silently bundled.
- **G2 — Each rule once.** Every governed rule lives in exactly one file; a
  bundle never carries a rule twice; a rule that must be referenced from a
  second file is referenced by identity.
- **G3 — Only what the audience needs.** Every member of a bundle earns its
  place for that audience. The floor every bundle carries is deliberate and
  small. The Writer, Copy Editor, and Critic bundles are exactly the sets in
  AC-BS-4; the Chief of Staff bundle is the set the audit confirms.
- **G4 — Two forms, one rule.** A rule may carry an agent form and a human
  form; agent bundles render the agent form; the human form is never lost.
- **G5 — Computed assembly.** Membership is computed from properties on the
  members, never from a maintained list. A new file joins by tagging.
  Where a role's set is not derivable from `audience:` alone, the mechanism
  that makes it derivable is a property on the file or the role, not a list
  kept elsewhere.
- **G6 — Provenance and staleness.** Every bundle states the repository, the
  HEAD it was generated from, the generation time, and every member with its
  blob; a consumer that can reach the repository can compute commits behind
  the default branch from the header alone.
- **G7 — Stated regeneration triggers.** A rename touching a bundle's file
  set, an agreement flip of a member, or an audience change on any file
  obliges regeneration of every affected bundle, and the obligation is stated
  where the change is made.
- **G8 — Releases.** Bundles for consumers who are not repository users are
  distributed through GitHub Releases: one file per audience, pinned to the
  generating SHA; a consumer downloads one file from one URL. No generated
  bundle is ever committed to the tree. New audience values need no code
  change.
- **G9 — Writing bundles are complete for a writer.** Every writing bundle
  carries the Public Prose Criteria and the author's Voice document; the
  Voice template reaches a new author through the release without being in
  any role's bundle.
- **G10 — Reach.** An adopting project reaches the corpus through a stated
  route that restates no rule and works for a consumer with a document and a
  chat and nothing else.
- **G11 — A home for lore.** Sandbox, connector, and environment facts that
  directives carry today have one governed home with a stated audience, so a
  directive cites it rather than restating it.

### Non-functional goals

- **Performance:** generation completes in seconds on the Mac; N/A otherwise.
- **Reliability:** the tool refuses — with a stated reason — rather than
  emitting a bundle from an unsynced tree, an unknown audience, or a file
  set that violates an invariant; a bundle is either complete or absent.
- **Scalability:** the model holds at a thousand rules and at a second
  corpus; the file store is retired for a database only when assembly or
  dedup becomes tedious, per the evidence in §5.
- **Security:** no secret value enters a bundle; a release carries only what
  the tree holds at the pinned SHA.
- **Maintainability:** every rule about membership is a property on a
  governed file, read at generation; changing membership never edits the
  tool.
- **Usability:** the operator runs one command; a writer downloads one file;
  an agent reads one header.
- **Observability:** the header is the telemetry — what, from where, when,
  how stale; nothing else is emitted.
- **Portability / Compatibility:** vendor-neutral: a bundle is a Markdown
  file any model reads; the tool runs where the repository runs; no
  vendor-shaped adapter is required to consume one.
- **Compliance:** N/A.

### Non-goals

- A per-project or per-vendor fork of the corpus.
- Replacing git as the store; whatever holds rows, git holds it.
- Deciding the row store now; that is decided on the evidence §5 names.
- Committing generated bundles; the tree holds sources and the tool, never
  outputs.
- Merging the writing corpus's roles into a single writing bundle; each role
  has its own, and the roles never share a session.

## 5. User outcomes and measurement

- **Bundle size per audience.** Baselines at 6e77040: Chief of Staff 33
  files; Writer 22 files, about 15,000 words; the `all-roles` floor 17
  files. Targets: the Writer, Copy Editor, and Critic bundles at the sets in
  AC-BS-4 (6, 5, and 5 files); the Chief of Staff bundle at the set the audit
  confirms; the floor at what every session needs. Observed by `bin/bundle
  --audience <value> --list` at each package's landing.
- **Rules restated.** Baseline: the rule register counted 878 rules with
  clusters of restatement; the collapse netted about 70 lines. Target: zero
  rules carried twice in any one bundle. Observed by the audit's register.
- **Stale citations.** Baseline: one gate finding from a stale bundle path
  in August. Target: none, and every directive derived from a bundle pins
  the bundle's HEAD. Observed by review artifacts and directives.
- **Regeneration cost.** Baseline: a hand procedure with a heredoc-free
  block, run from a clone root. Target: one command, one directory. Observed
  by the command's existence and the retros that stop mentioning it.
- **Writer reach.** Baseline: three writing bundles hand-built and handed by
  Dave. Target: a writer obtains one from a release without Dave. Observed
  when the first writer who is not Dave does.
- **Dual-form need.** Evidence to gather before the store decision: whether
  the agent/human split is common or rare across the audited rows; if rare,
  a companion-file convention beats a schema field.
- **Row count.** Evidence to gather: the count after the audit. Under about
  two hundred rows, files with frontmatter suffice; a database earns its
  place only past the tedium threshold the Decision Layer names for
  proposing a script.

## 6. Acceptance criteria

Each is testable against the tool, the tree, or a release. `AC-BS-n` are this
document's; the TRD derives its tests from them.

- **AC-BS-1 — One command, one directory.** One invocation naming an audience
  value writes exactly one file to `~/Downloads`, named to sort to the top,
  and exits non-zero with a stated reason on an unsynced tree, an unknown
  audience value, or an invariant violation, writing nothing.
- **AC-BS-2 — Header.** Every bundle opens with the repository, the HEAD
  SHA, the generation time, and a numbered list of every member with its
  path and blob SHA, in load order; every member is delimited by a marker
  carrying its path and blob. Whether the filename and header take the
  tool's present form or the form carried forward in DEC-000210 is OQ-5;
  whichever is chosen, hand-built and generated bundles are interchangeable
  under it, and the other form is retired in the same package.
- **AC-BS-3 — Computed membership.** Adding a governed file with a complete
  `audience:` (and `order:` where needed) places it in every bundle whose
  audience it names and in no other, with no edit to the tool and no edit
  to any list.
- **AC-BS-4 — Writing sets.** The tool emits these sets, in this order, and
  no other file:
  - `writer`: `docs/global-context/core.md`,
    `docs/global-context/decision-layer.md`, `roles/writer.md`,
    `public-prose-criteria.md`, `voice.md`, `skills/outline.md`.
  - `copy-editor`: `docs/global-context/core.md`,
    `docs/global-context/decision-layer.md`, `roles/copy-editor.md`,
    `public-prose-criteria.md`, `voice.md`.
  - `critic`: `docs/global-context/core.md`,
    `docs/global-context/decision-layer.md`, `roles/critic.md`,
    `public-prose-criteria.md`, `voice.md`.
  No writing bundle carries another writing role, any `all-roles` policy,
  context set, or boundary, the operating model, the Lexicon, the
  command-blocks skill, or the retro skill. The present 22-file
  `--audience writer` output is retired by this criterion; two bundles with
  one name and different contents is a defect.
- **AC-BS-5 — Floor.** The set every audience receives is stated in one
  governed place, is what every session needs, and carries no spec, no
  release or project-setup policy, and no engineering context set unless
  that place says why.
- **AC-BS-6 — Each rule once.** No bundle carries the same rule twice; a
  check over the bundle's members reports a restatement as a defect, and
  the audit's register is the evidence for the check's baseline.
- **AC-BS-7 — Staleness is computable.** From the header alone, a consumer
  with repository access computes commits behind the default branch;
  without it, the generation time bounds the claim. The header states
  nothing a consumer would have to recompute to trust.
- **AC-BS-8 — Regeneration triggers.** The governed text that authorizes a
  rename touching a bundle's file set, an agreement flip, or an audience
  change states the regeneration obligation at the point of change, and the
  tool can report which bundles a given commit range affects.
- **AC-BS-9 — Releases.** A release attaches one bundle per audience the
  release carries, each pinned to the release's SHA and generated from it;
  no bundle is committed to the tree; a new audience value appears in the
  next release with no code change. Which audiences a release carries —
  all, or a stated subset — is OQ-6.
- **AC-BS-10 — Voice template delivery.** `voice-template.md`, audience
  `[human]`, is attached to every release that carries a writing bundle and
  is in none of the role bundles.
- **AC-BS-11 — Adopting-project route.** A project reaches the corpus by a
  documented route that names a release and an audience and restates no
  rule; a project file that restates a governed rule is a defect the route's
  documentation says how to detect.
- **AC-BS-12 — Lore home.** Sandbox, connector, and environment facts have
  one governed file with a stated audience; a directive that carries such a
  fact inline rather than citing that file is a lint finding once the
  directive lint learns the file.
- **AC-BS-13 — Two forms.** Where a rule carries a human form, the agent
  bundle omits it and a human-audience artifact carries it; a rule's human
  form is never deleted by a cut that shortens the agent form.
- **AC-BS-14 — Dual-corpus invariant.** A rule both the software corpus and
  the writing corpus hold has one canonical home; the other cites it.

## 7. Risk tolerance

A bundle is the whole of what a session knows. A wrong bundle degrades every
session silently, which is worse than no bundle: the session proceeds
confidently on a stale or over-full text. So:

- **Refusal over emission.** The tool never emits a bundle it cannot vouch
  for; the operator prefers a stated refusal to a silently wrong file.
- **Selection rules are consequential.** A change to the selection
  mechanism, the floor, or the header format is a change to a public
  interface every session depends on, and takes the explicit go the commit
  and change control policy reserves for that class. Membership changes that
  follow from tagging a file are routine.
- **Releases are exposure.** The first release carrying writing bundles is a
  first exposure of a new surface to users, and is gated as such.
- **Corpus edits under the audit are routine** where they remove restatement
  without changing a rule, and take a review cycle where a rule's text moves
  or changes, as every governed edit does.
- **Accepted risk:** the file-based path may prove to be throwaway if the
  audit's row count forces the database early. The path is chosen anyway:
  the audit is needed under either store, and the tagging it produces
  survives the store change.

## 8. Open product questions

- **OQ-1 — Audience as roles or as conditions.** Is a row's `audience` a set
  of roles, or a set of conditions — role × session kind × corpus? Session
  kind is already a role property; corpus may fold into repository. Resolved
  by the audit's first pass over roles that need different text per session
  kind.
- **OQ-2 — One agent form per row.** Does a row ever need two agent forms —
  decision-session and execution-session phrasing? If so, that is two rows
  with two audiences. Resolved by the same audit pass.
- **OQ-3 — Project-specific rows.** Do project rows live in the project
  repository, selected by the same tool? The tool already reads
  `engagements/`. Resolved by the first adopting project under AC-BS-11.
- **OQ-4 — Canonical corpus for shared rules.** Which corpus is canonical for
  a rule both hold — claim classes in Core and in the writing claims
  taxonomy? Resolved by AC-BS-14's first instance, Dave ruling.
- **OQ-5 — Filename and header.** The tool's present form (`# bundle-<name>`,
  Repo, HEAD, Generated, numbered list with blobs) or DEC-000210's carried
  form (`methodology-context-bundle-<stamp>.md`, `Source: @ <HEAD>`). The
  writing bundles were built to the former so hand-built and generated
  interchange; DEC-000210 carried the latter from the hand procedure it
  retired. Dave's ruling; the losing form is retired in the header package.
- **OQ-6 — Release contents.** Every audience's bundle, or a stated subset?
  And cadence and ownership of releases, unconstrained so far. Dave's.
- **OQ-7 — Selection mechanism.** What makes the writing sets derivable:
  an explicit per-bundle file list, a profile property on the role, or rows.
  A list is the thing G5 forbids unless it is itself a property read at
  generation; a profile on the role document is one change in one place; rows
  are the end state. Resolved at the TRD, within G5.
- **OQ-8 — Decision Layer in writing bundles.** In today, by ruling; the one
  file a writer session could plausibly drop, about 570 of 3,800 words.
  Resolved by the first writer session that misbehaves without it, or does
  not.
- **OQ-9 — Writing bundle as a kind.** Is a writing bundle a first-class
  kind alongside role bundles, or one instance of a general per-role
  profile? Resolved with OQ-7.
- **OQ-10 — Outline skill audience.** `skills/outline.md` is tagged
  `[writer, human]`; whether `writer` alone suffices now that the skill is
  in the writer bundle. Resolved by the tagging package.
- **OQ-11 — The store.** Files with frontmatter or a database, decided on
  the row count and the dual-form evidence §5 names, after the audit.
