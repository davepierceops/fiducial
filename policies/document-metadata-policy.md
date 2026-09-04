---
status: in-review
last-reviewed: null
audience: [all-roles, human]
---

# Policy: Document Versioning & Metadata

This file governs both session kinds; the conditions marked **Dave's** are
decision-session acts.

## Scope

Frontmatter applies to documents that agents consume as governing
context; it does not apply to state trackers, adapters, or instantiated
project artifacts.

**In scope (frontmatter required):**

- `policies/**`
- `roles/**`
- `context-sets/**`
- `boundaries/**`
- `skills/**`
- `specs/**`
- `vendors/**`
- `docs/global-context/**`
- `engagements/**`
- `operating-model.md`
- `LEXICON.md`
- `public-prose-criteria.md`
- `voice.md`
- `voice-template.md`

**Out of scope:**

- History: `docs/history/**`. Retired material, kept for the record and
  explicitly excluded. The in-scope globs anchor at the repository root, so
  the retired copies under `docs/history/engagements/` are out of scope for
  the same reason.
- State and tracker artifacts: `MANIFEST.md`, `OPEN-ITEMS.md`,
  `COLLAB-STATE.md`, `BACKLOG-v2.md`, review artifacts
  (`reviews/**`, `REVIEW-*.md`), retros (`retros/`), merge history
  (`MERGE-NOTES-v0.4.md`), the voice inbox (`voice-inbox.md`).
- Adapters — the per-tool entry files that point a vendor's harness at
  this methodology, and their configuration directories.
- Instantiated project PRDs/TRDs. These live in project repos, not
  here, so this repo's enforcement does not reach them mechanically —
  but adoption is not optional.

Enforcement (hooks) checks exactly the in-scope set.

## Versioning

- The version of a document at reference time is the SHA of the last
  commit touching the file.
- Supersession is conditional on agreement: upon this policy reaching
  `agreed`, it supersedes the prior "single version declared once in
  `MANIFEST.md`" decision. The removal of the `Tree version` line from
  `MANIFEST.md` and the revision of the spec-template footers land in
  the same change package as the agreement.

## Metadata format

All in-scope documents begin with YAML frontmatter, fenced by `---`
lines, before any content.

## Required fields

- `status:` one of `draft | in-review | converging | agreed | superseded | deprecated`
  - `converging` = of a document under `specs/` only: its first
    reviewer gate has run and, on Dave's say, the spec is edited
    freely while tests are written against it; nothing in it is
    agreed. No other document holds this status.
  - `agreed` = Dave has agreed this document. This is the repo's
    standing verb; "approved" is not used.
  - `superseded` = replaced; a successor exists.
  - `deprecated` = do not use; no replacement.
- `last-reviewed:` the path to the review artifact in `reviews/` plus
  the reviewed commit SHA — or `null` if never reviewed.
  - Format: `<reviews/path.md> @ <sha>`
  - `status: agreed` requires a non-null `last-reviewed`.
  - `status: converging` does not require `last-reviewed`; the key may
    be absent or carry `null`.
  - The cited artifact must state, in its own scope, that it reviewed
    this document at the cited SHA.
  - `status: agreed` requires that artifact's verdict to be `ready` or
    `ready-with-findings`. Non-blocking findings do not bar agreement;
    Dave weighs them when he agrees. `changes-required` never satisfies.
  - **Grandfather clause:** documents agreed before this policy's
    adoption may carry `last-reviewed: null` until their next revision,
    at which point normal rules apply. Applicability is not judged
    case-by-case: at adoption, the adopting repo records a one-time
    per-document disposition list naming which documents enter
    migration as `agreed` under this clause, and its adoption record
    declares where that list lives; recording "none" is a valid and
    complete answer. A document absent from the list
    does not qualify. If no disposition list exists, the clause does
    not apply and normal rules govern.
- `audience:` list of roles that consume this document. Values are the
  basename slug of any role document under `roles/` or `engagements/`
  (including `engagements/sre/`), plus three reserved values:
  `all-roles`, `all-decision-roles`, and `human`. A role document is one
  whose first heading is `# Role:`; `engagements/working-with-dave.md` and
  `engagements/sre/README.md` are not role documents. `all-decision-roles`
  selects every role that runs as a decision session. Any other value
  fails enforcement.
- `session:` one of `decision | execution`, stating the session kind the
  role runs as. Required on every role document — one whose first heading
  is `# Role:` — and permitted on no other document. This is the field
  `all-decision-roles` reads.

## Conditional fields

- `superseded-by:` required if and only if `status: superseded`. A path
  or URL to the successor.
- `order:` optional on any document. An integer fixing the document's
  position within a bundle, lower first. Absent means the document sorts
  after every ordered file.
- Null semantics: null ≡ absent. A key present with value `null` (e.g.,
  `superseded-by: null` on a draft) is permitted and treated as the
  field being absent.

## Revision lifecycle

- When an `agreed` document is edited, the same commit flips
  `status: in-review` and resets `last-reviewed: null`, whatever the
  edit's size.
- Transitions to `superseded` / `deprecated`, the transition to
  `converging`, and the agreement flip itself, are **status
  transitions**, not revisions, and are exempt from the
  edit-flips-in-review rule; content edits alone trigger it.
  A status-transition commit contains nothing but the frontmatter
  transition.
- **Dave's.** A spec enters `converging` after its first reviewer gate
  has run, whatever the verdict, on Dave's say. A content edit to a
  `converging` spec changes neither its status nor its `last-reviewed`.
  The spec leaves `converging` only by the agreement flip, on Dave's
  ruling at the exit gate.
- **Dave's.** A revision of an `agreed` spec — flipped to `in-review` by
  its edit — may enter `converging` under the same entry rule: a reviewer
  gate has run on the revision, whatever its verdict; Dave says so; and
  the transition is a frontmatter-only status transition from `in-review`
  to `converging`. It leaves `converging` the same way the first interval
  does. A revision whose tests do not change takes the ordinary route
  from `in-review` to `agreed`.
- The document returns to `agreed` when Dave agrees the revision, and
  `last-reviewed` points at the new review artifact.

## Expedited return to `agreed`

The expedited path drops the reviewer-gated cycle — the findings
round-trip, the cycle directive, and the per-cycle review artifact.

### Eligibility

1. The revision is a **single commit** touching **exactly one** in-scope
   document and no other tracked path. A second file — including a
   tracker or an adapter edited alongside — escalates, and so does a
   revision spread across two commits.
2. The diff is **no more than ten changed lines of document body**,
   added plus deleted — the `+`/`-` lines below the frontmatter's
   closing `---`. Exceeding it costs a full cycle.
3. The document does not state a gate, a hard stop, or an enforcement
   rule governing how work or documents are reviewed, agreed, or
   released. **When it is unclear, it is ineligible.**

   The class includes, at minimum:
   - `policies/document-metadata-policy.md` — this document.
   - `policies/commit-and-change-control-policy.md`
   - `policies/source-of-truth-policy.md`
   - `policies/release-readiness-policy.md`
   - `policies/verification-boundary-policy.md`
   - `policies/project-setup-requirements.md` — effective when that
     document reaches `agreed`.
   - `roles/spec-reviewer-agent.md`
   - `roles/reviewer-agent.md`
   - `roles/release-manager-agent.md`
   - `roles/skeptic-risk-agent.md`
   - `roles/context-quality-reviewer.md`
   - `skills/spec-review-cycle.md`
   - `skills/conversation-retro.md`
   - `skills/review-artifact.md`
   - `boundaries/human-review-boundary.md`
   - `docs/global-context/core.md`
   - `docs/global-context/decision-layer.md`
   - `docs/global-context/review-rubric.md`
   - `operating-model.md`

   These return to `agreed` only through a full cycle. The list is
   normative where it names a document, and cannot bound the class; a
   repo that adds a governing document names it here, or substitutes
   its own paths for these.
4. The document is not under `specs/`. Spec agreement is gated by the
   Spec Reviewer Agent; this path does not reach that gate and does not
   override it.
5. **Dave's.** Dave reads the whole diff and agrees it **as-is**: zero
   findings, no dictated wording, no requested change.

*Any* finding escalates, however small; an edit that acquires one does
not get a second attempt at this path and becomes a full cycle.

The five conditions are necessary, not sufficient. Condition 3's class
is this policy's own exclusion; a document may exclude a further class
of revisions from this path, and skills/conversation-retro.md does —
any methodology revision a retro or a synthesis surfaces takes the
full cycle, whatever lighter path it would otherwise be eligible for.

### The record

Each expedited or doc-only agreement appends one line to
`reviews/expedited-log.md` naming the document, the reviewed SHA, the
date, and what changed — or, where the document is new and nothing
changed, what the document is; `last-reviewed` then reads
`reviews/expedited-log.md @ <sha>`.

`agreed` still requires a non-null `last-reviewed` naming an artifact
that exists, and **the SHA cited in `last-reviewed` must appear in an
entry in the log** — same commit, same form, so a checker matches pointer
to entry character-for-character or normalizes both through `git
rev-parse`. The log is append-only; entries are never edited or removed.

### Sequence

1. The content edit commits; the hook flips `status: in-review` and
   `last-reviewed: null`.
2. Dave reads the diff and agrees it as-is.
3. The log entry commits, naming the SHA from step 1.
4. A frontmatter-only status-transition commit flips the document back
   to `agreed`, with `last-reviewed` citing the log and the same step-1
   SHA the entry names.

Steps 3 and 4 stay separate commits, so the transition contains nothing
but the transition; step 3 lands before step 4.

## Doc-only cycle

A document co-authored with Dave in the artifact pane reaches `agreed` on his
sign-off, with no separate reviewer. It records as the expedited path does, per
"The record", but carries a co-authored document of **any size, new or
revised**, where the expedited path is capped at a ten-line revision.

The path reaches only documents in the frontmatter in-scope set above.

### Eligible when all six hold

1. **Prose, not a program.** Methodology or governance text in any format; a
   script or executable is out.
2. **Co-authored with Dave in the artifact pane — Dave's.** Drafted together,
   not finished elsewhere and presented for sign-off.
3. **Not a gate document.** Nothing stating a gate, hard stop, or enforcement
   rule over how work is reviewed, agreed, or released — the gate-document class
   defined by the expedited path's condition 3. That class takes the full
   reviewer cycle even when co-authored.
4. **Asked for, and agreed as-is — Dave's.** Dave asks for this path; at least
   one consistency sweep is run; Dave signs off with no open findings.

   A **consistency sweep** checks the document — and the documents it
   cross-references and that reference it — for any value or cross-reference the
   change has made stale. The co-authoring agent runs it before sign-off; "at
   least one" means the most recent sweep post-dates the final edit. Completion
   is attested by Dave's sign-off, not a separate artifact.
5. **Not under `specs/`**, per the expedited path's condition 4.
6. **One document.** The agreement covers exactly one in-scope document, as the
   expedited path's condition 1 does; several documents co-authored in one
   session are agreed as separate, sequential agreements.

Enforcement checks none of this: it verifies the pointer's format, that
the cited SHA resolves to an entry in the log, and that the transition commit is
frontmatter-only — it cannot see whether a document was co-authored, swept, or
asked for. The six conditions are necessary, not sufficient, here as on the
expedited path, and the same further exclusions reach this path:
skills/conversation-retro.md's, and any other a document states.

### Sequence

As the expedited path — content commit, then the log entry naming that SHA, then
a frontmatter-only flip to `agreed`, log entry before flip. Two differences: a
new document's content commit lands it at `draft`, where an edit to an
already-agreed document flips it to `in-review`; and the content revision may
span several commits, because this path carries a document of any size — the
log entry and `last-reviewed` then name the final content commit, and every
content commit touches only that document.

A companion tracked path (a `decisions/log.md` entry, an `OPEN-ITEMS.md`
update) lands in its own commit, per the expedited path's "no other tracked
path" rule.

## Excluded fields (do not add)

- Version number — git SHA is the version.
- Last-modified date — git log.
- Author — git blame.
- Changelog — git history.

## Agent behavior

- The build-gating rule covers `specs/` documents (PRDs/TRDs) only.
  "Build against" means: implement, modify, or test code whose
  requirements derive from that spec. Citing or discussing a draft
  spec is not building against it.
- The build-gating rule is three-valued by status:
  - `draft` or `in-review` — nothing is implemented or tested against
    the spec.
  - `converging` — tests are written and run against the spec; nothing
    is implemented against it.
  - `agreed` — implementation proceeds.
  An agent handed a task against a spec states the spec's current
  status in its report and does no more than that status admits.
- Methodology documents (policies, roles, context-sets, boundaries,
  skills) are governed by context loading, not the build-gating rule:
  agents follow the currently agreed methodology; a `draft` methodology
  document is not loaded as governing context unless the human
  explicitly directs it for a specific task.
- Never consume `superseded` or `deprecated` docs except to follow a
  `superseded-by` pointer.
- Bundle membership is declared by the document's `audience` value; no
  reader selects it.
