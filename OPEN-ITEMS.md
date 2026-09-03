# Open Items

This file tracks open questions, deferred decisions, and outstanding fixes
for the AI operating model. Updated at defined checkpoints per
`context-sets/spec-and-change-discipline.md`.

Last updated: 2026-09-02

---

## ~~Chat-originated package prompts have no compliant write path — `.prompts/` assumes a filesystem the chat layer lacks~~

**RESOLVED** by
`docs/cycles/friction-refactor-corrections-2026-08-10-directive.md` (C3),
2026-08-10, by removing the mechanism rather than fixing it. The `.prompts/`
rule is gone from `roles/chief-of-staff.md`, the `.gitignore` entry with it, and
`prompt` is retired as a term (C4). A package is dispatched as a directive, and
a directive is landed in git by the executor as its first act
(`skills/directive-dispatch.md`) — which is the recommendation this entry
reached, arrived at from the other direction: the record of what actually
executed is committed by the party that executed it, and no chat-side write is
involved at all. No unsatisfiable rule survives to satisfy.

**Source:** wne-crm cos session, 2026-08-03. The first package prompt drafted
under the migrated methodology was delivered as a chat blob, old-orchestrator
style — a straight process violation of `roles/chief-of-staff.md`'s prompt
rule (standalone file at `.prompts/<tranche>-<package>.md`, path stated in
chat), flagged by Dave, not self-caught.

**The gap the violation exposed:** the rule is unsatisfiable from chat as
written. `.prompts/` is gitignored in the local clone; chat's only write
surface is GitHub MCP, which writes committed files — exactly what the role's
"never committed" forbids for prompts. The mechanism implicitly assumes
filesystem access (Claude Code) or Dave saving the file by hand. Chat-origin
prompts therefore have no compliant path at all.

**The "never committed" rationale is weaker than stated.** It rests on
"regenerable artifacts are noise," but the repo's actual doctrine targets
*derivable state* — "a second copy of a derivable fact drifts and then lies."
An executed prompt is not state; it is an append-only record of what an agent
was told, the same artifact class as cycle directives, review artifacts, and
red-run logs, all of which are committed without controversy. The one real
drift risk is narrower: prompts are drafts and Dave owns the final used in a
session, so a committed *draft* can lie about what actually executed. That
indicts committing drafts, not committing prompts.

**Recommendation (chat, not decided):** the executor commits the prompt it
actually ran, alongside its work — same pattern as red-run logs — rather
than chat committing the draft. Accurate by construction; the record lands
only if execution starts, which is the acceptable failure mode (an
unexecuted draft is the one case where "regenerable, discard" is true).

**What's needed:** a methodology decision, then amend
`roles/chief-of-staff.md` (prompt-generation section) and the gitignore
convention via normal review cycle. Interacts with the directive-execution
skill item below — if `skills/directive-execution.md` gets drafted, the
"record what you executed" rule is plausibly one line in it rather than a
role-doc change.

---

## wne-crm migration to current methodology — ad hoc first, extract adoption skill after

**DECIDED 2026-08-02 (chat), execution pending.** Bring wne-crm from the
old-iteration methodology to current, running the migration ad hoc, then
extract `skills/project-adoption.md` from the experience; catchable runs
under the drafted skill as its first validation before the skill gates to
`agreed`. Working plan (from the chat session; not yet a governed artifact):
install the shim/hook via the sibling-directory convention; frontmatter
migration of wne-crm governed docs with the grandfather-clause disposition
list + adoption record; move the kickoff bundle to the current 7-file
target; template reconciliation decision (existing PRD/TRD predate current
templates); stand up `retros/`. Precondition satisfied 2026-08-02: the cos
supersession package is fully landed.

**EXECUTED 2026-08-03,** wne-crm PR #31 (branch
`methodology-migration-2026-08-03`, tip `a115431`, from ai @ `64a7ca8`),
merged at `d705a8a`. All five plan items landed; the one-line kickoff held.
Follow-ups completed same day: hook installed per clone, local `../ai`
updated to main, and branch protection's unenforced state accepted and
recorded (wne-crm `ACCEPTED-RISKS.md` #9 — free-plan private repo; revisit
on org upgrade). Template reconciliation deferred by executor disposition
(no agreed template target — both templates are `draft`), Dave's to
override. The session retro at `wne-crm:retros/` is the extraction input
for `skills/project-adoption.md` — that drafting, via normal review cycle,
is what remains of this entry. catchable runs under the drafted skill as
first validation before it gates.

---

## ~~MCP write verification must cover content, not just landing — a success-shaped response can commit malformed content~~

**RESOLVED** 2026-09-02 by remote-write verification policy cycle 8 (pull requests #295–#297; agreed at reviews/remote-write-verification-policy-cycle-8.md, reviewed document SHA 21e0c1e729a689bf7e4687f7e5910f86f972ac48): rule 3 makes the content check — response size against expectation, landed-commit stats against the expected blast radius — a rule, with this entry's incident as its example.

**Source:** wne-crm OPEN-ITEMS update, 2026-08-03 (chat cos session).
A `create_or_update_file` call intended to append one item to
`wne-crm:OPEN-ITEMS.md` was constructed with a placeholder string as the
`content` parameter; the API faithfully committed it, replacing the ~64KB
tracker with 19 bytes on `main` (`2606385`). The tool response was
success-shaped in every respect except the `size` field, which is what
triggered the catch; the file was restored with the intended addition four
minutes later (`e04780d`), verified by fetching the content back and
comparing against the pre-damage blob.

**Why this is a distinct learning:** the existing verification rule (verify
that MCP writes *landed* — fetch back before reporting) was written against
phantom-success failures, where the response lies about the write. This
failure is the mirror: the response is truthful, the *request* was wrong,
and landing-verification alone would have "confirmed" a destroyed file as a
successful commit. The check that works is content-shaped: response `size`
(and stats on the follow-up `get_commit`) against expectation — the same
stats-expectation guard the model-selection item records as invented
mid-session for full-file MCP writes, now with a second incident
demonstrating why it must be routine rather than improvised.

**What's needed:** fold into canonical text where the write-verification
rule lives (`policies/verification-boundary-policy.md` and/or the
directive-execution skill when drafted): after any full-file MCP write,
check the response's reported size/stats against expectation before
reporting success — landing and content are separate verifications, and a
diff-stats check (`get_commit`, expect append-only additions on an append)
is the cheap strong form. Also a candidate input for the tracker-append
pattern generally: full-file replacement as the only append mechanism is
what makes this failure class possible.

---

## gh CLI TLS verification failure in the Claude Code sandbox — workaround used, cause unknown

**OPEN.** During cos-supersession execution (PR #13), `gh` could not verify
api.github.com's TLS certificate in the sandbox; the session created the PR
via `curl` using gh's stored token. Unresolved: whether curl verified the
cert (benign CA-bundle gap in gh) or ran unverified (token sent over an
unauthenticated connection). Next session: `curl -v https://api.github.com`
and inspect how the workaround was invoked. Until understood, treat
extract-token-and-curl as a deliberate exception, not a habit.

---

## Directive-execution mechanics are oral tradition — the kickoff restates governed rules

**SUPERSEDED IN PART** by
`docs/cycles/friction-refactor-corrections-2026-08-10-directive.md` (C3, C4),
2026-08-10. The "rule, effective now" below — that a kickoff is one line citing
a directive path — no longer describes anything: a directive travels as a paste
block and the executor lands it, so there is no separate kickoff to keep to one
line (`skills/directive-dispatch.md`; `DEC-000160`, proposed). The word *prompt*
is also retired as a term (C4); this heading is conformed, the body below is
left as the record of what was found.

**Still open:** the gap the entry names. `skills/directive-dispatch.md`
Executor obligations now holds land-the-directive-first, stop-and-surface on an
unexecutable instruction, on concurrent tree mutation, and on an unreachable
remote, plus the report shape. It does **not** hold branch naming, the
run-the-tests-and-`check-frontmatter`-before-the-PR gate, or STOP semantics.
Those still have no canonical home, and a `skills/directive-execution.md` is
still the proposed fix.

**Source:** chat triage session, 2026-08-02, at the dispatch of
`docs/cycles/triage-2026-08-02b-directive.md`. The kickoff prompt drafted for
the executor session ran ~30 lines. On inspection, every line was one of two
defects: a restatement of rules the directive or the canonical text behind it
already states (red-gate, no-flip, executor recusal, branch-plus-PR,
stop-and-surface), or a session mechanic with no canonical home at all,
re-invented at every dispatch — pull first and record the SHA executed, branch
naming, verify every push in `git log` before reporting it, run `bin/tests/run`
and `check-frontmatter --all` before opening the PR, report shape, STOP
semantics. Dave rejected the prompt and named the defect: a per-dispatch
restatement is an unversioned derived copy of governed text, and derived
copies written fresh drift — the same defect class as the pending-gate rule's
"derived body" clause and the write-access-boundary rationale. Worse, if the
executor *needs* the restatement to comply, that is the load-bearing-context
failure relocated from bundles to prompts.

**The rule, effective now:** a kickoff prompt is one line — "Execute
<directive path> from origin/main HEAD." Anything more is a signal of a gap in
canonical text; fix the gap there, once. (The b-directive execution ran on the
one-line kickoff and delivered clean, which is one data point that the
restatement was ceremony.)

**What's needed:** `skills/directive-execution.md` via normal
drafting-and-review process, giving the session-level mechanics above one
canonical home. When drafted, assess it against the expedited path's
ineligibility criterion — it states verification steps that function as
enforcement rules, so under the criterion-primary reading it is likely
ineligible whether or not it is ever named in the list.

---

## AC-CF-23 is silent on the likely failure — a single typo'd in-scope glob

**Source:** Package A release decision, 2026-08-01. Accepted as a known gap at
the human gate; recorded here so it is tracked rather than absorbed.

`bin/check-frontmatter --staged` warns (`WARN [empty-scope]`) when the in-scope
glob set matches **no** tracked path — the total-no-op case. Verified at the
gate: when one glob is typo'd (`policies/**` → `polices/**`) while the others
still match, the hook is **silent**, and a content edit to an `agreed` document
in the affected directory commits with `status: agreed` intact and no
diagnostic. That is the more likely failure of the two, and it is the one not
covered.

**Why it was scoped that way:** per-glob `WARN [unmatched-glob]` lines exist in
`--all` and were deliberately kept out of `--staged`, because a project repo
legitimately matches only `specs/**` and would emit warnings on every commit.
The AC was written against the rarer case; that was an authoring error at the
spec level, not an implementation defect.

**Current mitigation:** run `check-frontmatter --all` after any edit to the
metadata policy's Scope section. This is a habit, which is exactly the class of
control this initiative exists to replace.

**What's needed:** a diagnostic that distinguishes "this glob legitimately
matches nothing in this repo" from "this glob used to match and no longer
does." Candidate: compare the matched set against the previous commit's, and
warn only on a glob that lost all its matches. Unverified — the design is not
settled, which is why this is an open item rather than a fix.

---

## Write-access boundary for ai/ — read-only except OPEN-ITEMS.md (DECIDED, pending policy incorporation)

**Decided by Dave, 2026-07-31, effective immediately:** project sessions
(any agent working a project repo, in any role) treat everything in this
repo as read-only, with one exception: `OPEN-ITEMS.md`. Sessions may
append or amend open items here to capture methodology observations,
decisions, and gaps as they surface — that is the designed intake path.
All other files (roles, policies, context sets, skills, boundaries,
`operating-model.md`, README, MANIFEST) are canonical and change only
through this repo's own drafting-and-review process, in sessions whose
purpose is methodology work.

**Rationale:** canonical methodology docs changing as a side effect of
project sessions is the same defect class as spec drift — untracked,
unreviewed mutation of a source of truth. The single writable surface
gives project sessions somewhere to put what they learn without opening
that door. (This very entry is the worked example: the rule was decided
in a project session and recorded here rather than written into
`operating-model.md` directly.)

**What's needed:** fold the rule into canonical text — likely
`operating-model.md` "Relationship to tools" and/or a `boundaries/` doc,
plus a line in `roles/chief-of-staff.md` — via normal process. Until
then this entry is the binding statement.

---

## Model selection by role — make cost/capability a per-role, per-step decision

**Source:** wne-crm Orchestrator session, 2026-07-31 (cycle-10 closure). A
frontier-tier model ran the Orchestrator role for a session that was
majority-mechanical (SHA bookkeeping, write-verify loops, ref discipline,
handoff maintenance). The methodology names roles and session boundaries
but is silent on which model tier each role warrants — every session
implicitly inherits whatever model the operator happens to open.

**The observation:** the evidence model already externalizes much of the
safety. Where errors are detectable by construction — stats-guarded
writes, red-gates, verify-before-assert, re-gates — a cheaper model is
safe, because the guards catch drift regardless of who drifts. Capability
was load-bearing in that session at exactly three points: treating a
one-line stats anomaly (+3/−3 vs. expected +2/−2) as a stop condition
rather than noise; inventing a new guard mid-session (the stats-expectation
check on full-file MCP writes); and byte-exact long-context reproduction
of a ~107KB document. Judgment-dense work — spec-cycle triage, reviewer
disagreements, directive drafting with STOP conditions, handoff synthesis —
propagates mistakes into canonical documents and stays frontier.

**What's needed:** a methodology update — probably a section in
`operating-model.md` plus a line per role doc — covering:

1. **A model-tier recommendation per role,** chosen at session open the
   same way the role is chosen. Working hypothesis from the source
   session: efficient tier for Orchestrator-as-executor, Coder on routine
   packages, and mechanical directive execution; frontier tier for
   Spec Reviewer, Skeptic/Risk, Architect, spec-cycle Orchestration, and
   anything drafting canonical text.
2. **Assignment criteria,** not just a static table: (a) are this role's
   errors detectable by construction — i.e. do externalized guards catch
   them? (b) is long-context fidelity load-bearing? (c) do this role's
   judgments propagate into canonical documents or gates? Two or three
   "yes" answers → frontier.
3. **An evidence step before demotion:** trial the cheaper tier on a
   routine package with all guards active; the guard-fire rate is the
   signal. Tier decisions are recorded with that evidence, per the core
   rule — not assigned by intuition, including the intuition of the
   frontier model that proposed this item.
4. **Vendor neutrality per the tooling rule:** durable policy speaks in
   tiers (frontier / efficient), never model names. Concrete model
   choices live in per-project configuration, same as the flag-backend
   pattern.

**Note:** interacts with the session-boundary habit (fresh chat per
phase) — the phase boundary is the natural tier-switch point, so this
costs nothing operationally once the recommendation exists.

---

## Per-project frontmatter enforcement as a project-setup step

**Source:** Document metadata policy cycle-2 revision session, 2026-07-21.
The revised `policies/document-metadata-policy.md` mandates that every
project applying this methodology adopts the metadata schema for its spec
documents — adoption is not optional. But the methodology repo's hooks
cannot reach project repos, so each project must stand up its own
enforcement.

**What's needed:** "Stand up frontmatter enforcement" becomes a defined
project-setup step. This belongs in the per-project TRD/setup guidance
covering CI/CD mechanics — currently deferred territory per the v0.4
decision to map deploy/release mechanics in per-project TRDs. When that
guidance is written, include the frontmatter hook as a required setup item.
Blocked on the policy reaching `agreed`; sequenced with the CI/CD mechanics
mapping.

---

## ~~Build this repo's frontmatter-enforcement hook~~

**RESOLVED** by Package A (F1), 2026-08-01. `bin/check-frontmatter` plus the
managed pre-commit hook installed by `bin/install-hooks` enforce the in-scope
set, read from the policy at runtime.

Struck by Package D, 2026-08-02, on the handoff in
`docs/packages/package-c-change-package.md` §9. The entry had gone on asserting
"Blocked on the policy reaching `agreed`" after the policy was agreed, the hook
was live, and the work had shipped — a live tracker asserting a blocker that no
longer exists.

---

## ~~Migrate existing docs to YAML frontmatter per document-metadata-policy~~

**RESOLVED** by Package B (F2), 2026-08-01. 34 documents migrated to YAML
frontmatter with a repo-wide disposition list under the grandfather clause; one
batch gate review.

Struck by Package D, 2026-08-02, on the same handoff as the item above, for the
same reason: it still read "Blocked on the policy itself reaching `agreed`".

---

## ~~`bin/bundle` supersedes MANIFEST's bundle definitions~~ — WITHDRAWN

**Withdrawn 2026-08-01 by the Package C gate review**, which found the premise
false. The streamlining directive deferred this as "after F4 lands and closure
output is trusted"; F4 landed, and the deferral does not survive contact with
the tool.

`bin/bundle` computes a reference closure — what a document cites. A bundle is
a curated judgment — what a conversation needs. Measured against "Spec chat"
(`base` + `spec-and-change-discipline` + `ai-native-engineering`): unbounded
closure returns every context-set plus trackers and historical artifacts;
`--max-depth 1` returns two and misses `ai-native-engineering`. No depth returns
three — the count goes 2, 4, 6 — because `bin/bundle` walks two graphs that fail
in opposite directions: `depends-on` is too sparse (every context-set points
only at `base`), and in-body citations are too dense and not curatorial
(`ai-native-engineering` arrives at depth 2 as a citation inside a policy). The
distinguishing information is in each set's prose `include-when:` field, which
is editorial judgment, not a reference.

**Consequence:** `MANIFEST.md` is not pending automation by `bin/bundle`, and
both files now say so.

**The door left open, deliberately.** What was disproved is that *closure*
derives a bundle. What was not disproved is that bundles could be derived at
all: declaring membership as data — a `bundles:` frontmatter key, or a small
`bundles.yaml` — relocates the judgment into machine-readable form without
removing it. Not proposed, not costed, and a different change from closure
computation. **Enriching `depends-on` to fake it is rejected**: co-selection is
not dependency, and encoding it there corrupts the field for every other
consumer. If membership-as-data is ever built, MANIFEST's lists become a second
copy of a derivable fact and should move.

---

## ~~`TREE.txt` mention survives in the agreed metadata policy~~

**RESOLVED** by Package D, 2026-08-02, exactly as this entry planned: the rider
rode the F6 cycle that opened the document for a substantive reason, and the
mention left the out-of-scope list in the same diff the reviewer read.

Confirmed inert on the way out, by the cycle-5 gate review rather than on the
executor's say-so: `bin/aimeta/scope.py` stops parsing at the `Out of scope`
marker, so enforcement never read the prose; `check-frontmatter --all` and the
321-test `bin/` suite are unchanged by the removal.

---

## ~~The expedited path's log entry is unenforced — `flip-agreed` checks existence, not content~~ — PRECONDITION SATISFIED

**RESOLVED** by `docs/cycles/triage-2026-08-02b-directive.md` (W-2), 2026-08-02.
Tests `2556226` (red: 15 tests, 6 failing); implementation `4e90b03` (green:
336 tests, 0 failing). New `bin/aimeta/expedited.py` decides
the rule; `bin/flip-agreed`'s `check_review` and `bin/check-frontmatter`'s
`check_worktree` both consult it.

All four ACs below are implemented and covered. Two notes on what was decided
inside them, so the reading is not left to the next reader:

- **What counts as an entry.** A Markdown list item carrying `@ <sha>`, per the
  format the log documents. A SHA appearing only in the log's header prose does
  not satisfy a pointer, and there is a test for that.
- **`--staged` is deliberately not covered,** and this is the one place the
  implementation is narrower than a maximal reading of "over the whole in-scope
  set". The AC names `check-frontmatter`, and `check_worktree` serves both
  `--all` and path mode; hook mode was left alone because the log rule is a fact
  about the repository's review record rather than about the staged change, and
  a blocking hook that consults a file outside the commit can refuse a commit
  for a condition that commit did not cause. **Consequence, stated rather than
  absorbed:** a hand-edited frontmatter pointer at a log SHA that does not exist
  still commits, and is caught by the next `--all` run rather than at the hook.

**The precondition on the next agreement flip is satisfied.** The flip itself
remains gated: it needs the reviewer re-gate and Dave's approval, and this
directive does not authorize it.

**Original entry, kept for the record:**

**Source:** Package D cycle-5 gate review (B4), 2026-08-02. Verified by
running, in a scratch clone: with step 3 of the expedited sequence **skipped
entirely**, `bin/flip-agreed --review 'reviews/expedited-log.md @ <sha>'` exited
0 against a log holding no entries, and `check-frontmatter --all` then reported
the repo clean.

**Why it matters now and did not before.** A per-cycle review artifact had to be
*created* to satisfy the existence check, so existence was weak evidence that a
review happened. `reviews/expedited-log.md` exists permanently, so the same
check is satisfied vacuously and forever, for every document in the repo. The
policy now states the rule that carries the weight — the SHA cited in
`last-reviewed` must appear in an entry in the log — but nothing checks it.

**What's needed:** `bin/flip-agreed` (and probably `bin/check-frontmatter`)
verify that the cited SHA appears in the target artifact when that artifact is
the expedited log. Small and checkable. It is a `bin/` change with its own ACs
and tests, which is why it is not inside Package D — F6 is a routing change, and
the directive scopes Package D to F6 alone.

**Disposition at the Package D gate, 2026-08-02.** Named as a release risk, not
absorbed, and Dave decided: it does **not** block the Package D flip, because
the expedited path has zero addressable documents and therefore zero exposure.
It **is a hard precondition on the next agreement flip**, when a second document
reaches `agreed` and the exposure stops being zero. The check ships in `bin/`
with its own acceptance criteria and tests before that flip runs.

The ACs it needs, so the work starts from a spec rather than a description:
`flip-agreed --review` resolves the cited SHA against the target artifact's
contents when that artifact is the expedited log, and fails closed when the SHA
is absent; abbreviation is normalized through `git rev-parse` before comparison,
per the policy's stated rule; a non-log artifact keeps today's
existence-only behaviour; and `check-frontmatter` reports the same condition
over the whole in-scope set.

Recorded at the trip point as well as here: `skills/spec-review-cycle.md` step
11 states the precondition where the next cycle will actually run the flip.

---

## A policy edit can blind enforcement of itself — the self-referential scope hazard

**Source:** Package D cycle-5 gate review (B2), 2026-08-02. Pre-dates F6;
surfaced by testing F6's blast radius.

**Verified by running,** in a scratch clone: a single commit deleting the
`policies/**` line from the metadata policy's in-scope list dropped enforcement
from 38 files / 8 globs to 31 / 7, and the committed file still read
`status: agreed` with its prior `last-reviewed` intact — because
`bin/aimeta/scope.py` reads the globs from the policy on disk, so by the time
the hook evaluated the commit the file had already removed itself from scope and
the flip never fired. The mirror case is worse: when the flip does land first,
`flip-agreed` then refuses the document as "outside the frontmatter in-scope
set" and it cannot return to `agreed` by tool at all.

**Mitigated, not fixed.** F6 eligibility condition 3 keeps this policy off the
expedited path entirely, so the hazard is not *authorized*. It remains reachable
by any ordinary commit.

**What's needed:** the same diagnostic class as the typo'd-glob item at the top
of this file — compare the matched set against the previous commit's and warn on
a glob that lost all its matches. Both items are one fix.

---

## ~~Settle condition 3's enumerated class before a second document reaches `agreed`~~

**RESOLVED** by `docs/cycles/triage-2026-08-02b-directive.md` (W-1), 2026-08-02,
on Dave's decision at E2. Both open questions are answered in the same
restatement:

- **The borderline trio is in.** `policies/testing-policy.md`,
  `policies/verification-boundary-policy.md`, and `roles/skeptic-risk-agent.md`
  are named in condition 3's list. Each states a hard stop removable inside the
  ten-line ceiling, and a gate over work carries the same
  small-diff-removes-a-gate hazard as a gate over documents.
- **Neither narrowed nor widened — the criterion is primary.** The class is no
  longer "enumerated, not judged." A document stating a gate, a hard stop, or an
  enforcement rule is ineligible whether or not it is named, the list is an
  explicit floor ("at minimum"), and an added fail-safe clause makes an unclear
  case ineligible — mirroring the commit policy's "when in doubt,
  consequential."

The forcing point the entry named is honoured, not bypassed: the settlement
rides the same reviewer-gated cycle that returns
`policies/document-metadata-policy.md` to `agreed`, and no flip has run.

**Original entry, kept for the record:**

**Source:** Package D cycle-7 gate review (B1/B2/N2), 2026-08-02. The expedited
path's condition 3 excludes a named list of documents that state a gate, hard
stop, or enforcement rule. The list is normative, is not derivable by any tool,
and therefore has to be maintained by hand.

**It was incomplete on the day it was written.** Cycle 7 measured five in-scope
documents matching the class, unnamed, each with a gate removable inside the
ten-line ceiling: `operating-model.md` (4 body lines removes both hard gates),
`roles/reviewer-agent.md` (2), `skills/conversation-retro.md` (4),
`boundaries/human-review-boundary.md` (1), `README.md` (2). All five are now
named, along with the release trio the class definition implied.

**Unsettled, and Dave's call:** `policies/testing-policy.md` (the red-gate),
`policies/verification-boundary-policy.md` (boundary-declaration rules), and
`roles/skeptic-risk-agent.md` (a change-flow review step). Each states a gate or
enforcement rule over *work* rather than over documents, which is where the
class definition's edge falls. Also open: whether the class definition should be
narrowed to match the list, or the list widened to match the definition.

**The forcing point, named explicitly so this does not become the `TREE.txt`
mention again:** none of it is reachable until a second document reaches
`agreed`, because until then the expedited path has no addressable document at
all. That day arrives through a reviewer-gated cycle, so the gate is already
attached — **settle this list at that cycle, before the flip.**

---

## ~~Does the Spec Reviewer gate non-spec canonical documents? Two canonical documents disagree~~

**RESOLVED by Dave at the Package D gate, 2026-08-02, in favour of practice:**
the Spec Reviewer hard gate covers **any canonical document**, not `specs/`
only. `skills/spec-review-cycle.md` and the entire review record already said
so; the four contradicting documents were `draft`, and were corrected by plain
commit to match rather than being carried as a standing contradiction. Corrected:
`roles/spec-reviewer-agent.md` (the Activation clause, which was the origin of
the narrow reading), `README.md` principle 9, `operating-model.md` change-flow
step 1, and `boundaries/human-review-boundary.md`. Deliberately not part of
Package D's diff.

The one bounded exception is now named in the role doc: the expedited path
substitutes Dave's read for this gate under five stated conditions.
(Update 2026-08-06: a second bounded exception, the doc-only cycle, landed with
the cycle-10 revision of `document-metadata-policy.md`; the role doc names both.)

**Original entry, kept for the record:**

**Source:** Package D cycle-5 gate review (N2), 2026-08-02. Pre-dates F6.
Surfaced because F6 eligibility condition 4 has to rest on the answer.

`roles/spec-reviewer-agent.md` triggers the hard gate on "initial PRD or TRD
authorship" and "any revision to a **spec** document"; `README.md`,
`operating-model.md`, and `boundaries/human-review-boundary.md` all scope the
hard gate to spec documents, in three different formulations.
`skills/spec-review-cycle.md` scopes the cycle to "spec documents (PRD, TRD,
**or any canonical document**)".

**Practice follows the skill, not the role doc.** Every gate review in
`reviews/` is over a non-`specs/` document — four cycles over the metadata
policy, two over Package C, this one — including the four that produced the text
F6 amends. So the class of document that has received every gate review in this
repo's history is the class the role doc says is not gated.

**What's needed:** Dave's call on which reading is canonical, then reconcile the
two documents. F6 does not block on it: condition 4 defers to the gate wherever
it applies rather than defining its reach, and conditions 1–3 bound the override
to a ten-line single-file diff outside this policy either way.

---

## Review artifact schema — third-use feedback from the cycle-5 gate review

**Source:** Package D cycle-5 gate review, schema feedback section, 2026-08-02.
Cycle 2 of Package C asked for a third data point on two specific frictions;
this is it, plus two new ones. Not acted on in Package D — the F3 schema is
Package C's document and F6 does not authorize revising it beyond the
expedited-log carve-out.

1. **A `Severity:` qualifier inside `blocking` — friction confirmed, and it
   scales badly.** Six blocking entries here span two orders of magnitude of
   weight. The header line `Findings: 6 blocking` reads as six equal hard stops.
   The reviewer reports considering demoting two findings purely to keep the
   count honest — the schema shaping the finding. Proposed cheaper fix that
   avoids the "everyone ships past `Severity: low`" failure: let the count read
   `6 blocking (B1–B2 material)`.
2. **Omit-if-none header fields — no friction, but the reasoning is
   asymmetric.** `Not inspected` is required because omitting it is how an
   unbounded claim gets made by accident; `Dave should inspect` carries the same
   risk and is omit-if-none. `Cross-checked` and `Prior cycle` are fine as-is.
3. **New: the schema has no shape for a check that passed.** Dave named the
   compounding check as this review's priority and it passed, with no field for
   that. `observation` was the only bucket and its required `Consequence:` field
   ("what goes wrong, concretely") can never be filled by one — the artifact
   carries `Consequence: None` four times. Without those entries a reader cannot
   distinguish "the check passed" from "the check was never run", which is the
   distinction `Not inspected` exists to protect.
4. **New: the header names one revision where a revision review has two.**
   `Reviewed: <path> @ <sha>` fits a first-cycle review of a draft. Cycles 2+
   review a range; the baseline SHA is what makes the diff reproducible. A
   `Baseline:` field would carry it. LANDED 2026-09-02 in
   skills/review-artifact.md (converging-model CM-5).
5. **O-4** (reviews/converging-model-cycle-1.md): the multi-document branch
   gate is a third range form; the Reviewed line carries a commit plus
   several documents and the schema does not describe it; name the form at
   the schema's next cycle.

**What worked, recorded because it is load-bearing:** the
`verified by running` / `inferred by reading` split. B2 and B4 exist because the
field pushed the reviewer to execute the sequence instead of reasoning about it,
and both are things a reading-only review would have gotten wrong in the
confident direction.

---

## ~~Remove repo version number from MANIFEST.md~~

**Source:** Document metadata policy session, 2026-07-21.
`policies/document-metadata-policy.md` supersedes the "single version
declared once in `MANIFEST.md`" decision — git SHA is the version.

**RESOLVED** by Package C (F7), 2026-08-01. `MANIFEST.md` dropped its version
declaration in `0230e11`; `README.md`'s echo of it — `Tree version: v0.4 — see
MANIFEST.md for the changelog` — survived that commit and was removed here.

Worth recording why that mattered: the agreed metadata policy's supersession
clause requires that the removal land in the same change package as the
agreement, so that **the repo never holds both conventions as canonical**. From
`0230e11` until Package C, it did — MANIFEST said the SHA was the version while
README said the tree version was "the single source for what's current." Two
review cycles passed over that package without catching it. Found by the
Package C gate review, not by the executor.

---

## Adopt reviews/ directory for review history; migrate root REVIEW-*.md

**Source:** Document metadata policy review session, 2026-07-21. The cycle-1
gate review of `policies/document-metadata-policy.md` is being written to
`reviews/document-metadata-policy-cycle-1.md`, establishing `reviews/` as the
home for review-history artifacts.

**What's needed:** Make `reviews/` the standing convention for review history
and migrate the three existing root-level files (`REVIEW-v0.4.md`,
`REVIEW-NOTES-v0.3.md`, `REVIEW-NOTES-v0.2.md`) into it. Rationale: root is
crowding, and one home for review artifacts keeps them from scattering. Keep
reviewer findings (`reviews/`) distinct from triage decisions (cycle
directives) — the canonical-vs-derived split from
`policies/source-of-truth-policy.md`. Low priority; cheap now, cheaper than
running two conventions indefinitely.

---

## Project context configuration for WNRealtor-CRM (token optimization, workstream 1 of 2)

**Source:** Token optimization session, 2026-07-20. Workstream 2 (methodology
change) shipped as v0.5 (`skills/spec-review-cycle.md`, commit `a3ffe08`).
This item is the remaining workstream.

**What's needed:** Decide the Context panel file list and Instructions text
for the WNRealtor-CRM Claude project. Candidates already proposed:
`roles/spec-reviewer-agent.md`, writer style guide,
`boundaries/mocked-boundaries.md`, `skills/spec-review-cycle.md`. Exclusions
already decided: PRD/TRD (change every cycle),
`context-sets/collab-workflow.md` (artifact-pane default is the wrong mode
for that project's gate-cycle chats). Short behavioral directives (terse
tone, follow spec-review-cycle for gate reviews) go in Instructions, not
Context.

---

## Spec evolution policy — how does the spec stay canonical when reality diverges?

**Source:** Catchable Phase 1, 2026-07-15. The 511 SF Bay stops API returned a
response shape (`Contents.dataObjects.ScheduledStopPoint[]`) that differed from
what the TRD assumed. The bug was fixed in code and captured in a retro, but the
TRD was not updated. This is spec drift.

**The gap:** The operating model states that specs are canonical and that
conflicts are hard stops. But it is silent on what happens when live integration
discoveries, bug fixes, or real-world misalignments invalidate a spec assumption
mid-implementation. There is no policy for:

- When the spec must be updated (before the fix ships? after? never for bugs?)
- Who triggers the update (the agent that found the divergence? DAVE?)
- What constitutes a spec-worthy divergence vs. an implementation detail
- How to keep the spec trustworthy as a regeneration artifact over time

**Why this matters:** If the spec is the leverage point for LLM-driven
regeneration (e.g. rewrites, new platforms), spec drift silently erodes that
leverage. A spec that doesn't reflect reality can't reliably regenerate the
correct implementation.

**What's needed:** A lightweight policy — probably a section in
`context-sets/spec-and-change-discipline.md` — covering:
1. The trigger: what kinds of divergence require a spec update?
2. The timing: before fix, after fix, or at session end?
3. The owner: which role is responsible?
4. The mechanism: in-place edit to PRD/TRD, or a versioned amendment?

**Note:** This is distinct from the retro process open item. Retros capture what
went wrong; this policy governs ongoing spec maintenance as the codebase evolves.

---

## Add retrospective process to the operating model

**Source:** Catchable Phase 1, 2026-07-01. Missing `index.html` + `src/main.tsx`
reached `origin/main` with 225 passing tests. The architect role did not produce
a per-change architecture summary that listed browser entry files as explicit
deliverables.

**What's needed:** A lightweight retro step or trigger in the operating model —
when to run one, what it should capture (what happened, why it wasn't caught,
which role/gate failed, recommended process change), and where the output lives.
Retros are distinct from the skeptic/risk review: they happen after a failure is
discovered, not before release.

**Note:** The architect role instruction for Vite/React projects should be
updated immediately as a direct fix, independent of the broader retro process
definition.

---

## ~~A2 — Consequential-change class: confirm membership is complete~~

**RESOLVED.** The list is exhaustive. Updated
`policies/commit-and-change-control-policy.md` to state this explicitly.
Iterate via normal change process if additions are needed later.

---

## ~~A8 — Define "meaningful change"~~

**RESOLVED.** A meaningful change is any change that warrants a change package
— any change affecting behavior, interfaces, tests, dependencies, boundaries,
or documentation of substance. Trivial changes (typo fixes, comment edits,
purely mechanical formatting) do not require a change package and are not
meaningful in this sense. All affected documents should use this definition.

---

## ~~Reviewer gate vs. advisory~~

**RESOLVED.** The Reviewer Agent is a hard gate. A meaningful change does not
proceed to Skeptic/Risk review or release without Reviewer sign-off. Updated
`roles/reviewer-agent.md` and `policies/agent-review-policy.md`.

---

## ~~Per-file vs. single-file role granularity~~

**RESOLVED.** Roles operate per change unit. The Reviewer Agent reviews the
entire change as a single pass — all files, test plan, diff, and boundary
updates together. If only a subset was reviewed, the reviewer must state what
was and was not inspected. Updated `roles/reviewer-agent.md`.

---

## ~~Error budget exhaustion as a consequential-change trigger~~

**RESOLVED.** Any change to a code path for a Top K user journey whose SLO
error budget is at or below 20% remaining is automatically consequential,
regardless of other characteristics. Updated
`policies/commit-and-change-control-policy.md`.

---

## ~~SRE production readiness checklist~~

**RESOLVED (deferred).** Moved to `BACKLOG-v2.md`. Not blocking current
work. When tackled, likely a new context set or policy doc that extends the
definition of done in `context-sets/spec-and-change-discipline.md`.

---

## `LEXICON.md` frontmatter is unenforced — docroot is not in the in-scope glob list

**Source:** Trivium, 2026-08-06. `bin/check-frontmatter` reports 45 files after
the Trivium merge; `LEXICON.md` is not among them.

The in-scope list in `policies/document-metadata-policy.md` globs `policies/**`,
`roles/**`, `context-sets/**`, `boundaries/**`, `skills/**`, `specs/**`, and
`vendors/**`, and names `operating-model.md` and `README.md` individually.
Docroot is otherwise out of scope, and the out-of-scope list is explicitly for
state and tracker artifacts — `MANIFEST.md`, `OPEN-ITEMS.md`, `BACKLOG-v2.md`.
`LEXICON.md` is a governed definitional document sitting in tracker company.

It carries `status`, `last-reviewed`, and `audience` today and nothing validates
them. It also cannot reach `agreed` by tool: `bin/flip-agreed` refuses documents
outside the in-scope set.

**What's needed:** add `LEXICON.md` to the in-scope list. One line, but the
metadata policy is `agreed`, so it is a review cycle. **Decided by Dave
2026-08-06:** take the cycle and keep the file at docroot; `policies/lexicon.md`
would misfile a lexicon as a policy.

Note the interaction with the self-referential scope hazard recorded above: this
edit *adds* a glob rather than removing one, so it cannot blind enforcement of
itself in the same way. It does mean the document is unenforced for every commit
before the edit lands.

---

## ~~`handoff` at `skills/spec-review-cycle.md:57` contradicts the lexicon~~

**RESOLVED** by `docs/cycles/trivium-gate-cycle-1-directive.md` (D6), 2026-08-08.
The heading now reads `### 2. Directive`; `LEXICON.md`'s "Known misuse to
correct" paragraph is struck in the same commit, since the misuse it named is
gone. Three records — the skill, the lexicon, and this entry — reconciled
together, which is what the finding asked for.

**Source:** Trivium, 2026-08-06. Recorded as known misuse in `LEXICON.md`.

Line 57 reads `### 2. Directive (handoff artifact)`. The lexicon defines a
handoff as the *transfer* of unfinished responsibility, and a directive as one
mechanism by which a handoff is carried out — so naming the mechanism "the
handoff artifact" collapses the distinction the term exists to preserve.

Not fixed in Trivium: scope was cut to files already being edited, and
`spec-review-cycle.md`'s only Trivium change was the one-line dictated-wording
fix. Deliberately excluded from the touch rule on the grounds that a surgical
one-line edit should not trigger a whole-file conformance pass.

**What's needed:** rename the section. Trivial edit, but it is a canonical
document and needs a cycle.

---

## ~~A handoff into another decision session has no name~~

**RESOLVED** by
`docs/cycles/friction-refactor-corrections-2026-08-10-directive.md` (C2),
2026-08-10. The name is **baton**, defined in `LEXICON.md` under Handoff: the
artifact a decision session hands its successor decision session, carrying the
composed package of unfinished responsibility. The boundary sentence is the
load-bearing half — a baton passes between decision sessions, a directive
dispatches work to an execution session, and the two never blur. `LEXICON.md`'s
"has no term yet" paragraph is struck in the same commit, and
`context-sets/collab-workflow.md`'s Session handoff section names the artifact
alongside the open-items flush. `kickoff` is neither retired nor narrowed here —
it was never a lexicon term, and the execution-session sense the
directive-execution-mechanics entry above describes is superseded separately by
the paste transport.

**Source:** Trivium, 2026-08-06. Flagged as open work in `LEXICON.md`.

The lexicon names the execution-session column completely — dispatch, directive,
directive file, dispatch block. The decision-session column is empty: there is no
term for the artifact that carries a handoff into a fresh chat, nor for the
paste block that delivers it.

`kickoff` is unavailable and actively ambiguous. `OPEN-ITEMS.md` uses it for the
one-line prompt that starts an *execution* session — the thing the lexicon calls
a dispatch block — while the working brief that opened the Trivium session is
titled "Kickoff — AI-9" and is the other thing entirely. Same word, both senses,
both live.

**Candidates raised, none chosen:** `handover` (appears nowhere in the repo, so
it cannot collide), `briefing`. Naming it also means deciding whether `kickoff`
is retired or narrowed.

---

## ~~Write-verification covers landing, not content~~

**RESOLVED** 2026-09-02 by remote-write verification policy cycle 8, as the entry above: the policy's Known gap section is gone and rule 3 states the content check.

**Source:** Trivium, 2026-08-06, on moving the policy out of `vendors/`.
Duplicates the substance of the success-shaped-response item above; recorded
here as the gap in the *policy document* specifically.

`policies/remote-write-verification-policy.md` states three rules, all of which
verify that a write **landed**. None verifies that what landed is what was
intended. The policy now says so explicitly in a Known gap section rather than
reading as complete.

**What's needed:** a content-expectation check alongside the landing check —
response `size` against expectation, and stats on the follow-up commit read.
Specifying it is open work; the policy deliberately does not.

---

## Promote the write-verification principle into `context-sets/base.md`

**Source:** flagged in the original 2026-08-02 draft; carried forward unchanged
when the document moved to `policies/remote-write-verification-policy.md`,
2026-08-06.

The principle — *a write through an unreliable transport is not evidence that
the write landed; verify before reporting, and read state before retrying* — is
the same claim as `base.md`'s "agent claims require evidence," applied to the
transport. `base.md` is always loaded; the policy is not.

The move out of `vendors/` did **not** settle this. A rule in `base.md` plus a
detailed procedure in the policy is the normal shape, and the two are not
exclusive.

**What's needed:** a cycle on `context-sets/base.md`.

---

## `name` and `description` frontmatter on the remaining six skills

**Source:** Trivium, 2026-08-06.

**Decided:** every skill carries `name` and `description` per Anthropic's skill
authoring guidance
(https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
`description` is what an agent matches a request against when choosing among
skills, so a skill without one only fires for someone who already knew it
existed — the population least in need of it. The motivating case: a
skeptic/risk role needing to send a remediation to an execution session cannot
discover `skills/directive-dispatch.md` by reading the directory.

Done in Trivium: `skills/directive-dispatch.md`, `skills/command-blocks.md`.

Remaining: `boundary-audit`, `change-package-creation`, `conversation-retro`,
`evidence-review`, `release-readiness-review`, `spec-review-cycle`,
`test-plan-review`.

**Verified 2026-08-06:** `bin/check-frontmatter` passes with `name` and
`description` present — the validator checks for required keys and carries a
denylist for git-derivable fields, not an allowlist, so unknown keys pass.
`bin/flip-agreed` shares the parser but was **not** exercised; its path only
runs on an actual agreement flip.

---

## Skills conformance pass — rubric first, scope undecided

**Source:** Trivium, 2026-08-06. The sequencing question was raised and never
answered.

A pass over all skills conforming them to: Anthropic's skill-authoring guidance,
`LEXICON.md`, and this repo's frontmatter policy.

**The unresolved call:** whether the standard lands as a committed rubric first
and the pass runs against it, or whether the criteria live in the directive that
executes the pass. A rubric is a governed document and a gate; a checklist in a
directive is not. Reviewing eight skills against a web page that can change, and
that is not in the repo, is the thing `context-sets/base.md`'s tooling rule
forbids.

**Substance worth keeping from the guidance:** brevity is not the rule. Cut what
the model already knows; keep rationale that encodes a failure mode it cannot
infer. Bare imperatives — all-caps MUST/NEVER — are flagged as an anti-pattern,
because the model follows the letter and misses edge cases the author did not
anticipate.

---

## ~~Sync as a skill rather than a step inside every directive~~

**RESOLVED** by `docs/cycles/trivium-gate-cycle-1-directive.md` (D1), 2026-08-08,
on direction (a): narrow the rule rather than restore a block. `LEXICON.md`
scopes the sync block to Track A; `skills/directive-dispatch.md` states that
Track B carries the sync step in the echoed dispatch line, and says what that
line asks for — a working-tree-current check in the same clone, not a remote
fetch — and why the tracks differ (same-machine, commit-not-push).

Closed rather than left "Not analysed": the tree had already adopted this item's
proposed phrasing ahead of the analysis, and the cycle-1 gate settled the
question. What this entry does **not** decide is the broader proposal it also
carried — making sync a role-held skill so directives carry no version-control
mechanics. That argument (the mechanics are git-specific; a non-git project
would need every directive rewritten) is untouched and unrefuted here. If it is
wanted, it opens as its own item.

**Source:** Dave, Trivium, 2026-08-06. Parked mid-session, not developed.

Today `skills/directive-dispatch.md` requires every dispatch to open with a sync
step, and `skills/command-blocks.md` governs how that block is built. The
proposal: make sync a skill that agent roles hold, so a directive reads "sync,
then read and execute `<path>` @ `<sha>`" and carries no mechanics.

**The argument for it:** the mechanics are version-control-specific. A project on
something other than git would need every directive rewritten; a skill would
need replacing once.

Not analysed. Interacts with the dispatch block's two-step form and with what
"self-contained" means for a directive.

---

## ~~A paste block must be copyable in the surface that delivers it~~

**Source:** Trivium, 2026-08-06, found in use. A command block containing a
heredoc rendered in the Claude desktop client **without a copy button** — the
block could not be copied in its entirety. A second version of the same commit,
using `-m` flags instead of a heredoc, rendered normally.

**Why this is a distinct rule and not covered by existing ones.** `LEXICON.md`
defines a paste block as one "intended to be copied in its entirety and pasted
in its entirety somewhere else." A block the surface will not let the reader
copy fails that definition before any conformance criterion applies.
`skills/command-blocks.md` requires that a block "runs verbatim as pasted,"
which presupposes the paste already happened. Neither document states the
precondition: **the block must be copyable in the surface it is delivered to.**

The failure is silent from the author's side. The block is well-formed, every
command is valid, and nothing in the text signals the problem — it appears only
in rendering, which the author does not see.

**RESOLVED** 2026-08-06, same session. `skills/command-blocks.md` states the
principle as a rule and names heredocs in the Claude desktop client as a *known
instance* rather than as the rule itself, with adopting projects directed to
substitute their own cases. Also added as a fifth conformance criterion.

The alternative — principle only, no instance — was rejected as unenforceable:
an author cannot check "does this render correctly" while writing, which is how
this defect reached delivery in the first place. Naming a vendor instance inside
a portable skill is a real cost; `context-sets/base.md`'s tooling rule forbids
durable policy living *only* in a vendor surface, which this does not, and
`skills/directive-dispatch.md` already names Claude Code by product.

## ~~`bundle base` red — stale AC after the decision-log citation~~

**RESOLVED** by PR #221 (`448e93e7`), 2026-08-27: `bin/tests/test_bundle.py` was deleted along with `bin/bundle-methodology` under DEC-000210, because its tests exercised the positional closure mode removed under AC-BA-7. Directive `docs/cycles/retire-bundle-methodology-20260827T0120.md` @ `c695d881`; gate `reviews/retire-bundle-methodology-cycle-1.md` @ `32371f14` (RBM-1). Suite 441/2-failing → 424/0.

**Original entry, kept for the record:**

`bin/tests/test_bundle.py::test_bn10_bundle_base_yields_exactly_itself` fails:
`bundle base` returns 67 paths, not just `context-sets/base.md`. Cause, pinned in
the cycle-11 re-gate (O3): `context-sets/base.md` gained the decision-log consult
obligation under the AI-6 landing (`consult … decisions/log.md … cite the
governing entry by ID`), so reference closure from `base` now pulls in the cited
documents, and AC-BN-10(a)'s "declares `depends-on: []` and cites no documents"
premise is stale. Not a flake, not a reason to hold any flip. Fix is a `bin/`
change (Reviewer Agent territory): correct the AC, or confirm the citation-closure
behavior is intended and rewrite the assertion.

## document-metadata-policy.md doc-only cycle — advisory clarity items (cycle-12)

Accepted as advisory at the cycle-12 agreement, deferred rather than spun into a
cycle 13. Each is a clarity edit to the now-agreed gate document, so each would
take the full reviewer cycle:
- **N1** — the doc-only `### Sequence` imports two of the expedited path's
  condition-1 clauses ("exactly one in-scope document", "no other tracked path")
  and is silent on the third, single-commit. On an unbounded-size route a
  multi-commit content revision is expected; the intended reading is that
  `last-reviewed` cites the final content commit. State it.
- **N3** — the single-document rule is stated under `### Sequence`, not among the
  five eligibility conditions, though it is eligibility-shaped. Consider
  promoting it to a numbered condition.
- Rider from pull request #273: the doc-only path sentence (near "A doc-only
  agreement covers exactly one in-scope document") lacks the F-10 clause the
  expedited path's sentence carries; fold in with F-10 at the policy's next
  cycle.
- CR5-3 (reviews/conversation-retro-cycle-5.md, observation): the sentence
  "a document may exclude its own revisions from this path, and the retro
  skill does" is false at skills/conversation-retro.md @ 649809aa — the skill
  excludes retro-surfaced methodology revisions from lighter paths, not its
  own revisions; what binds the skill's revisions to the full cycle is this
  policy's condition 3 list. Correct the sentence at the policy's next cycle.

## bin/aimeta/expedited.py is path-blind (benign under the single-document rule)

`check_pointer` matches a `last-reviewed` pointer on SHA alone, not on document
path. Harmless now that every route admits one in-scope document per content
commit (one SHA selects one entry), but untracked. If a future decision ever
re-admits multi-document shared-SHA agreements, this must become path-aware
first. Surfaced at cycle-11 B1.

## MANIFEST.md carries an embedded changelog contrary to git-SHA versioning

Header says it holds only the context-set bundle definitions ("everything else removed"), yet it still carries a changelog (`### v0.5 changes`, `### Post-v0.5 changes`). Repo rule is git-SHA-is-the-version / git-log-is-the-changelog (`policies/document-metadata-policy.md`; the version number dropped in Package C). The embedded changelog is a second copy of git history. Symptom: `MANIFEST.md:129` carries the "handoff artifact" misuse corrected in cycle-1 D6, left as historical. Fix is removal of the changelog, not correction of the line. Source: Trivium gate cycle-1 triage, 2026-08-08.

## The open spec delta has never been run

**Source:** `docs/cycles/friction-refactor-2026-08-09-directive.md` (Change 2),
2026-08-09. The design is written into
`context-sets/spec-and-change-discipline.md`, `skills/spec-review-cycle.md`,
`roles/chief-of-staff.md`, and `LEXICON.md` with **zero** executions behind it.
Every prior mechanism in this repo that was written before being run — Track B
most recently — needed rewriting after its first real use.

Unknowns worth watching on the first delta: how much drift accumulates before a
reconciliation cycle stops being reviewable in one pass; whether "brought to full
agreement with what was actually built" is judgeable by a reviewer who did not
watch the tranche execute; and whether the encouraged norm of frequent small
reconciliations survives contact with the cost of opening one.

**What's needed:** run one, then a retro against the written design before it is
treated as settled.

## The disjoint-territory claim rule is unenforced

**Source:** as above (D2.5). "A spec document is claimed by appearing in an open
delta's diff; a document claimed by one open delta may not be claimed by another"
is stated in `context-sets/spec-and-change-discipline.md` and checked by nobody.
The state is computable — `git diff <default>...spec/<slug> --name-only` per open
spec branch, intersected — which makes it a `bin/` candidate rather than a
register to maintain (`roles/chief-of-staff.md`, the computed-state constraint).

The violation is silent and expensive: the collision is only discovered at the
second reconciliation, when the second delta's diff no longer applies cleanly and
the refused case — merging convergent spec edits — is what is left on the table.

**What's needed:** a check in the Chief of Staff read-sequence at minimum; a
`bin/` script if the manual step proves tedious, per the same constraint.

## `bin/cycle-open` and the retirement of Track

**Track is retired — do not resurrect the field.** `DEC-000180` removed `track` from the methodology entirely; the requirements are **route, model, execution block**, three not four, and `LEXICON.md` carries a tombstone. The obligation that the cycle skeleton emit **Route and Model and nothing else** of the three is borne by **`bin/directive`'s cycle mode** (`DEC-000270`, 2026-08-30): route and model come from the committed `Route and model` section of `skills/directive-invariants.md` into a committed region of every skeleton, in both modes, and no region emits a `Track:` line. `bin/cycle-open` is a forwarder (TRD §3.9 step 4) and holds no skeleton text of its own, so there is no shelved spec left to guard; the guard is the invariants document, which is governed text and changes only through its review cycle.

**Landing precondition recorded 2026-08-24 — discharged 2026-08-30.** `specs/directive-tooling.md` AC-DT-16 made two acts preconditions on the landing that migrates the cycle mode: the entry superseding `DEC-000180` (now `DEC-000270`) and this rewrite. Both landed in the decision session that merged PR #244.

## `bin/bundle`'s path-following closure mode is retired, replaced in Pass 2 by audience selection

Recorded 2026-08-21, Pass 1 cycle 12 revision: rubric criterion 3 proceeds as written, so removing in-body backticked `*.md` paths from the corpus silently shrinks `bin/bundle`'s closure to `depends-on` edges only; no edit to `bin/` was made in that cycle, and audience selection replaces the path-following mode in Pass 2.

## `bin/land` is not agent-facing until a governed write-path usage document is agreed

Dave's sequencing decision, recorded in `specs/bin-land.md` §8 and originating
in `docs/cycles/bin-land-spec-7-20260823T203500Z.md` @
`8a77c2a017977976d88552d86bf523109bbdd0b5`: a governed standing write-path
usage document — stating when an agent invokes `bin/land` and what its output
means — must be agreed before the tool becomes agent-facing, where
agent-facing means the first directive instructing an executor to invoke it.
Implementation is not blocked by this gate; the build-gating rule in
`policies/document-metadata-policy.md` governs implementation independently.

**Source:** `specs/bin-land.md` §8; `docs/cycles/bin-land-spec-7-20260823T203500Z.md` @ `8a77c2a017977976d88552d86bf523109bbdd0b5`.

---

## `bin/bundle` output format does not match DEC-000210

**Source:** CoS session 2026-08-26, on regenerating the CoS bundle. `bin/bundle --audience <value> --out DIR` writes `bundle-<value>-<stamp>.md` with a `# bundle-<value>` header. DEC-000210 carries forward from DEC-000190 the filename `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md`, the `Source: @ <repo HEAD>` line, the per-file blob short-SHA, and the `<!-- FILE n/N: path @ sha -->` separators. The separators and blob SHAs match; the filename and header do not.

**What's needed:** a change to `bin/bundle`'s ACs (AC-BA-*), as a package under the bundle-system PRD. Until then, the bundle uploaded per project is the `bundle-chief-of-staff-*` file `bin/bundle` emits.

**Folded 2026-08-31 into `specs/bundle-system.md` OQ-5**, which records the
filename/header conflict as Dave's open ruling; this entry closes when OQ-5
resolves and adds nothing to it.

---

## Bundle-system PRD draft is uncommitted

`~/Downloads/bundle-system-prd-draft-20260825T023000.md`, status draft, on Dave's disk only. DEC-000210 cites it as the decision's context and names the `bundle-methodology` removal (now landed, PR #221) as a package under it.

**What's needed:** commit it under `specs/`, then the spec-review cycle.

**Recorded requirement for the PRD's cycle 1 (Dave, via the writing workstream decision session, 2026-08-28):** bundles are distributed through GitHub Releases. `bin/bundle` generates one bundle file per audience; a release attaches those files pinned to the repository SHA they were generated from; a consumer downloads one file and never touches the repository. No generated bundle is ever committed to the tree. Consequences the PRD must state: new audience values (`writer`, `copy`, `critic` are coming) must be accepted without a code change; whether a release carries every audience's bundle or a stated subset is the PRD's decision; every writing bundle carries the Public Prose Criteria document, the per-author Voice document, and a Voice template for new authors, mechanism the PRD's call; release cadence and ownership are open, unconstrained by the writing workstream. Nothing here changes DEC-000210 — this adds a delivery surface downstream of `bin/bundle`.

**Seven further requirements for cycle 1 (retrospective session, 2026-08-31):** provenance and staleness stamps on every bundle; filename and header per DEC-000210; stated regeneration triggers; per-rule selection or a stated reason for file granularity; Releases distribution as recorded above; how an adopting project reaches the corpus with a document and a chat and nothing else; a home for sandbox and connector lore with a stated audience. Each is stated in full under "Follow-ups — bundle-system PRD inputs" in retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203, with the retros that raised it.

---

## ~~`CLAUDE.md` carries a derived copy of governed rules~~

**RESOLVED** 2026-08-28 by PR #224: `CLAUDE.md` and `AGENTS.md` are deleted. fiducial is a portable corpus; the project-adapter question belongs to the bundle-system PRD.

**Source:** pass-2b gate, `reviews/pass-2b-rulings-cycle-1.md` @ `32371f14` (F1), 2026-08-26. The adapter's "Required behavior" list restates ten rules from `operating-model.md` and is now stale on the C018 wording. It also says guidance lives under `/ai/` (the repo was renamed) and points at `context-sets/base.md` and `context-sets/collab-workflow.md`, whose presence in the current corpus is unverified. Deliberately not edited by the pass-2b directive: adapters are outside the governed set.

**What's needed:** cut the file to what an adapter is — a pointer at the bundle or the reading list, no restated rules. Outside the frontmatter set, so a plain commit; fix the stale paths in the same commit.

---

## ~~`specs/directive-tooling.md` names a retired binary~~

**RESOLVED** 2026-08-28 by the PRD rewrite (PR #225, agreed at cycle 23 @ `d3ab472`): the rewrite carries none of the references this entry names — verified by two full reads. The document's next opening cycle is queued under "`specs/directive-tooling.md` — rider queue" below.

**Source:** `reviews/retire-bundle-methodology-cycle-1.md` @ `32371f14` (RBM-4), 2026-08-26. Line ~2051 lists `bundle-methodology` in a `bin/` inventory marked observed; the binary is gone as of PR #221. The spec is `agreed`, so the fix is a cycle. Bundle with the stale AC-CO-3 pointer and the three findings `skills/directive-authoring.md` defers to the TRD stage, so the document opens once.

---

## ~~`skills/directive-invariants.md` is `draft` and load-bearing~~

**RESOLVED** 2026-08-30: agreed at `3f0a96e4f97015ed3091e3d666b64fbc22895eec`
(`reviews/directive-invariants-cycle-4.md`), flip `a8a9913`, on `main` at
`3e64efe`. Four Context Quality Reviewer cycles and three revisions, PRs
#250–#258, all merge commits. Directives: `docs/cycles/directive-invariants-{gate,rev-1b,rev-1c,rev-1d,gate-2,rev-2,rev-2b,gate-3,rev-3,gate-4,agree}-*.md`.
Rejected and recorded at cycle 1: F-4/F-5 (Stop-conditions and Claim-labels
regions restate Core 11/15 and 6 — by-value quotation into emitted skeletons,
same class as the disposition prompt). Suite at every content commit: 604 OK /
7 skipped, zero reds — the three writing-workstream reds (test_scope sc1/sc3,
test_check_frontmatter cf13) are gone; expected-state lists in directives now
name no known red.

Riders on the document, for its next cycle: cycle-4 F-1 — state the
match-rule property as an editor constraint inside the format-rules paragraph;
cycle-4 O-2 — the Preamble markers positional prose (`<document heading>`
first, literal second) is a second unstated positional dependency; code
classifies by shape, so swapping the entries leaves the check green and the
prose false; cycle-4 O-3 — "eligible line" and "unfenced line" alternate in
the fence-only paragraph; the second is stronger; cycle-4 O-1 — `<name>` in
the worked example is still undefined as a placeholder.

**Original entry, kept for the record:**

Landed 2026-08-29 (PR #231, `ab3f2ef`; heading line amended PR #244, `c4a0353`). Every skeleton `bin/directive` emits, in both modes, reads its regions from this document at its last commit in the methodology home, so the document governs every directive from adoption forward while sitting at `status: draft`.

---

## ~~`skills/directive-authoring.md` consolidation cycle owed — adoption of `bin/directive` waits on it~~

**RESOLVED 2026-08-31.** Consolidation revision D-0 plus amendments b, c, d;
gates at cycles 4/5 (ready-with-findings, 0 blocking), 5/6
(ready-with-findings, 1 non-blocking each), and 6/7 (ready, zero findings).
Both documents `agreed` at `reviews/directive-authoring-cycle-6.md` and
`reviews/directive-invariants-cycle-7.md`, both @
afbe7df9924f0449a2f48a408c26c67399595eb8; flips landed by `bin/flip-agreed`
(one self-commit per invocation), PRs #263–#267, all merge commits, main at
24dab436. Adoption is unblocked: directives are generated with
`bin/directive` and linted with `bin/check-directive` from here on. Persisting
items and riders moved to the topic-walk section below.

Five expedited amendments outstanding, plus: the OQ-Q4(c) path pointer to
`skills/directive-invariants.md`; the own-worktree-cleanup-and-report-final-line
rule; the holder-check rule; "expected-output lines are claims" (verify it is
already there in spirit); OQ-10's Naming-section branch gap; `git push origin
<branch>` with no `-u` in the sandbox (`.git/config` is not writable); never
bypassing the pre-commit hook. Added 2026-08-30 from the invariants arc:
cycle-2 O-3 — the governed rule's "this document" inverts its referent when the
bullet is emitted into a directive by value; fixable only in this skill, and the
two copies move together under the byte-equality rule; and **the route line
names one session** — "the holding session" is ambiguous when two execution
sessions hold the same worktree, which happened on rev-1c/rev-1d (below).
Evidence for adoption: three of this arc's stops were authoring defects
`bin/check-directive` exists to catch — a blanket constraint contradicting an
instruction (rev-1b, F-11), a dictated literal violating the same directive's
own self-check (rev-2, F-2), and a base-verification guard broader than the
blast radius (rev-1). Adoption — authors reaching for `bin/directive` rather
than freehand — waits on the pointer.

---

## `specs/directive-tooling.md` — rider queue

For the PRD's next opening cycle; do not open a cycle for these alone. (a) §4 "plus the disposition slot and the source manifest" is illustrative, not exhaustive — dictated clause per TRD §9 OQ-5 (Dave, 2026-08-28). (b) AC-DT-09 "tag" → "annotated tag"; a lightweight tag is indistinguishable, verified by running. (c) AC-DT-04's author-text clause clarification; the TRD states satisfied-by-construction meanwhile.

---

## `specs/directive-tooling-trd.md` — rider queue and open questions

Riders for the TRD's next opening cycle, each from an implementation-package ruling on main (directives `docs/cycles/directive-tooling-impl-{1,2,3,4,4b}-*.md`, `directive-tooling-tests-{fix-1,fix-2,fix-2b,3}-*.md`, 2026-08-29/30): §3.3 Heading (cycle)'s first line is `# {{heading}}`, filled whole from `directive_identity`, and the placeholder table drops `{{cycle}}`/`{{title}}` for that section (ruling (b)); §3.3 "appears exactly once in the file" reads *once among eligible lines*, the mask applying to the generator's self-check and the tests alike (ruling (a)); `{{reviewed_ref}}` and `{{companion_list}}` have no flag in the §3.9 flag set and are emitted as author slots inside committed regions, which the manifest then classifies as committed; M2 skips the source-manifest region, because manifest entries cite the methodology home, which in the test substrate is not the linted repository; §3.7's git dependency notes that `status` reads run with `--no-optional-locks`, which is what holds §3.9's "reading is not writing" (test_x5 caught the index rewrite); the stale counts cycle-1 deferred as O-1..O-4 (`bin/` executable count; corpus 170/114/68 today vs 144/109/63 in the text). Test-suite gap for the Test Designer: §3.3's byte-equality test of the disposition prompt against `skills/directive-authoring.md`'s bullet does not exist, so §4.2's B3 is pinned by nothing and drift would be silent.

Confirmed absent 2026-08-30 by the cycle-2 gate sweep
(`reviews/directive-invariants-cycle-2.md` O-2): `AUTHORING_RELPATH` is defined
in `bin/tests/helpers.py` and referenced by nothing. Two more riders from the
invariants arc: §3.3's cycle-mode table has no Placeholders column, so
`{{heading}}`, `{{date}}`, `{{scope_list}}` are fixed only in
`skills/directive-invariants.md` and `bin/aimeta/directive.py`; and §3.4's
decision sentence calls the label the bare token while its match-rule bullet
says "exactly the literal" whose definition carries the colon — the document
and `matches_label` both take the bare-token reading.

Open questions carrying recommendations, Dave's to rule whenever: Q2 rec (b), directive lands and work stops; Q4 rec (c), the skill gains a path pointer to the invariants document; Q6 rec (b), the five-code contract — §7 is already written to (b). Plus the TRD's own OQ-1..10; OQ-7 (sole-tree literal) and OQ-9 (M3-extent reading) want a gate or Dave.

Candidate M-rule: a dictated artifact path must not exist at the base ref —
mechanical, would have caught both 2026-09-01 instances. M5 false positive: a
slashless root-level path in Documents in scope (OPEN-ITEMS.md) is misread as
a companion marker preceding FIRST ACT and fails first-act-missing; observed
2026-09-01 on this flush directive, in both scope-line orders. Classified,
not worked around, per the M2 precedent.

M5 false positive (slashless root-level path in Documents in scope read as a
companion marker) fired on five of this session's directives, 2026-09-02;
M2's flip-pointer false positive (artifact @ reviewed-document SHA) fired on
the nine-flip directive. Both classified, not worked around.

directive-tooling TRD lines ~808-810 quote old Decision Layer rule 14
verbatim — the TRD's own B3/G6 defect class; recorded as DL-4 in
reviews/decision-layer-cycle-14.md.

Riders from the 2026-09-02 session-2 directives, for bin/directive and the skeleton (skills/directive-invariants.md): (a) the FIRST ACT region says "before touching any other file" and precedes the disposition, so an executor wrote the directive commit on local main and hit branch protection — the region must say "create the worktree named in the disposition below first, then write"; (b) cycle mode appends " Directive" to --title, producing "Directive Directive" when the title already ends in the word; (c) --cycle N alone collides with the generic docs/cycles/cycle-N-directive.md already present — the --name selector avoids it, and the collision is the same class as the candidate M-rule above; (d) the skeleton has no Cleanup region, so the worktree-removal line is hand-written into every directive. Authoring rule, for the same skill: a directive must not state a stop condition on a fact it has only been told — a told count of untracked files stopped an executor when a retro appeared in the clone mid-run. Sandbox lore for the same queue: heredoc-fed while-read loops lose PATH; zsh does not word-split unquoted variables; a bare echo of equals signs is refused by zsh; an ~/.ssh deny rule false-matches a cd-relative path containing roles/chief-of-staff.md.

---

## ~~Convergence process — canonization owed~~

**RESOLVED** 2026-09-02 by DEC-000360 and the converging-model branch (pull requests #287–#292): convergence is the standard change flow with a named status, converging; written into operating-model.md, skills/spec-review-cycle.md, policies/document-metadata-policy.md, roles/test-designer-agent.md, roles/chief-of-staff.md, roles/spec-reviewer-agent.md, LEXICON.md, context-sets/spec-and-change-discipline.md, skills/review-artifact.md; all nine agreed at reviews/converging-model-cycle-2.md.

Ruled ad hoc for the directive-tooling TRD, canonization after from the retro (Dave, 2026-08-28). The shape as run: one blocker-scoped review cycle, the TRD stays open, the Test Designer writes tests against it, findings mediated through the decision session both ways, joint flip when they cohere. It ran clean; evidence is the `docs/cycles/directive-tooling-trd-*.md` chain and `reviews/directive-tooling-trd-cycle-{1,2,3}.md`. One detail the description added and the run used: the decision session as the mediating agent — executors state intent in dispositions and verify against the counterparty's artifacts, and correct a wrong disposition with disclosure. A full cycle on `skills/spec-review-cycle.md` (or a sibling skill) writes it in.

---

## PRD and TRD templates carry the wrong audience — directed fix

Dave, 2026-08-28: PRDs and TRDs are audience `[human]` (the narrowing of `specs/directive-tooling.md` from `[all-roles, human]` was deliberate and kept, cycle 21 O1). Both templates (`prd-template`, `trd-template`) still say otherwise and are wrong. A directed change awaiting its review cycle, not a candidate.

---

## Corpus dedup, Passes 1–2b — closed

Record only. Pass 1 extracted 878 rules (`docs/rule-register/rule-register-20260825T1435.md`); Pass 2 clustered 220 of them into 77 clusters (`docs/rule-register/rule-clusters-20260825T1600.md`). Rulings: C001–C008 (`rule-divergence-rulings`, PR #211); the 69 agreeing clusters (`docs/cycles/agreeing-clusters-collapse-20260826T2120.md`, `agreeing-clusters-collapse-2-20260826T2200.md`, PRs #215–#217); Pass 2b, the eleven agreeing clusters found divergent on reading (`docs/cycles/pass-2b-rulings-20260827T0025.md` @ `94c01bf7`, PRs #218–#220 — three edits, eight accepted as consistent). Net corpus change was about −70 lines; Pass 2's "a quarter of the corpus restates itself" did not hold — the clustering over-matched.

---

## Candidate methodology changes from the dedup sessions

Each is a full cycle on a gate document; none is decided.

- **Rubric criteria 3, 4, 6, 11, 12 are absence tests.** Restate affirmatively (e.g. 4 → "every rule is stated in exactly one governed file, and this file is that one"). Dave's concern: negated framing primes the forbidden thing and yields uncitable "I didn't see one" findings. Run the same audit over `docs/global-context/core.md` and `decision-layer.md`. criterion 12 exemption for a template's examples (DEC-000240; reviews/document-metadata-policy-cycle-19.md DMP19-3, rejected there) — encode in the rubric or the reviewer's role, or refuse.
- **Multi-document review artifacts.** A gate over a branch is now practice (PRs #211, #215, #218, #221) but `skills/spec-review-cycle.md` and `skills/review-artifact.md` are written for one document, one stem. Write the case in: artifact stem names the branch; `Reviewed:` lists the documents; `Baseline:` carries the pre-change ref.
- **Bundle invariant.** A rule may be deleted from file A only if the home B's audience covers A's; otherwise the duplicate is legitimate. Lives only in a collapse directive today; belongs in the rubric.
- **Decision-layer 3, "landmine".** Sharpened 2026-08-29 (Dave): the word is reserved for a consequence of doing what was asked that is severe or hard to reverse — a wrong merge, a lost record, a broken gate. Expected tool behaviour, state information, and items already on the tracker or baton are triage, unlabelled. Observed 2026-08-26 and again 2026-08-29: the label spent on nothing trains the reader to skip it.
- **Executor STOP wording.** State the tree-mutation stop on intent, not cause: "any tree mutation you did not intend, including your own." Used in the pass-2b directives; the gate executor stopped correctly under it.
- **Governed documents carry substance only.** Findings dispositions, cycle changelog prose, per-sentence provenance tags and SHA citations belong in review artifacts and cycle directives, not in the document they concern. The directive-tooling PRD rewrite (PR #225) went from a bloated draft to 511 lines on this rule alone; write it into the rubric or the authoring skills.
- **Executor decision lists are committed, not chatted.** Every implementation package this session reported a numbered list of decisions the spec left open; those lists live only in chat, and the package-3 executor could not read package 1's. The report's decision list is appended to the directive file (or a sibling report file) as the executor's last commit, so the next executor reads it from the tree.

---

## Executor self-recovery — tracked behaviour defect

Two instances: the agreeing-clusters gate executor ran `git checkout <sha> -- .`, staged branch content by mistake, reset itself, and continued (2026-08-26); the pass-2b executor's `git worktree add -b … origin/<ref>` failed on a sandbox `.git/config` write-deny, and it deleted the stray ref and retried with `--no-track` (2026-08-26). Neither damaged anything; both flagged honestly; both should have stopped. Under the intent-based STOP wording above the pass-2b gate executor did stop on the same failure. Operating note: in the sandbox, create worktrees with `--no-track`, or check out an existing local branch.

2026-08-29/30, directive-tooling packages: two more, disclosed and accepted — the package-1 executor committed its directive file with the pre-commit hook bypassed (verified clean afterwards; directives now say "never bypass the pre-commit hook"), and the AC-DT-16 executor committed its edits before its directive file and pushed both together (record accepted as-is, PR #245). Against that, four correct stops in the same run: tests-fix-2 on an unruled finding, tests-3 on the parameterization scope, impl-4 on test_x5, and impl-1's own self-check refusing its first skeleton. The stop wording holds; the two deviations are a different class — a step taken on the executor's own judgment rather than a recovery — and the invariants document's First act and Sandbox regions are where they get closed.

2026-08-30, directive-invariants arc: one more disclosed deviation and its
cause. Two execution sessions held the same worktree — rev-1c and rev-1d were
routed to "the holding session" while two existed — and the session that did
the work continued past a directive commit the other had landed under it,
citing benign content; the other stopped correctly three times on the same
class of mutation. The deviation is accepted; the cause is the route line, now
a consolidation-cycle item above. Six correct stops in the same arc, three of
them on the Chief of Staff's own authoring defects.

2026-09-02: a Sonnet 5 executor reported the clone's main tree, behind
origin/main, as "ahead"; harmless, recorded as a claim-labelling miss.

---

## ~~Worktree and branch pile~~

**RESOLVED** 2026-08-30. One command block from the CoS, computed rather than
listed: every branch on origin fully merged into `origin/main` — 178 of them,
the 27 listed here among them — deleted; 39 local branches deleted (31 by
plain delete, 8 by force after an ancestor-of-`origin/main` check, because the
local `main` was behind); both stale worktree entries pruned; `git worktree
list` shows only the main tree. Record: `~/Downloads/branch-cleanup-20260830T1100Z.txt`.
The `retros/` untracked files in the main clone were not touched.

---

## Corpus defects carried from prior batons

- Four untriaged finding classes against agreed `specs/bin-land-trd.md`: completeness gap, coverage gaps, unverified boundary conditions, open questions. Rider: line ~1536 cites the retired per-task confirmation as the metadata policy's build-gating rule; restate under the three-valued rule (reviews/converging-model-cycle-1.md N-4).
- DEC-000140 sweep still owed.
- `roles/architect-agent.md` session-kind self-contradiction; C053 touched the file — re-check before opening a cycle.
- Six methodology decisions from the 15-hour session not yet in `decisions/log.md`.
- ~~Writing corpus: the GitHub connector cannot see `davepierceops/writing` (404); `prose-criteria.md` audience tag defect.~~ RESOLVED 2026-08-29 by PR #230 (`53f7f40`): the writing repository's content was migrated from a snapshot at `387bde6`, so the connector no longer needs to see it; `prose-criteria.md` is retired to `docs/history/` and replaced by `public-prose-criteria.md` and `voice.md` (DEC-000240).

---

## Writing methodology landed — follow-ups

**Source:** writing workstream decision session, 2026-08-28/29; PR #230 (`53f7f40`); DEC-000220 through DEC-000260.

- ~~**Full cycle owed on `policies/document-metadata-policy.md`.**~~ Agreed
  2026-08-30 at cycle 20 (PR #249, `d577819`).
- ~~**Doc-only agreements owed**, one each, sequential: `roles/copy-editor.md`, `roles/critic.md`, `roles/writer.md` (in-review), `skills/outline.md`, `public-prose-criteria.md`, `voice.md`, `voice-template.md`. All co-authored in the pane; none is a gate document.~~ all seven agreed 2026-08-29, PRs #235, #236, #238, #239, #240, #242, #243.
- **Voice inbox triage owed**: the 2026-08-22 §4 and §5 entries in `voice-inbox.md`, against `voice.md`, as a doc-only cycle.
- **Retire `davepierceops/writing`** after the agreements above land and Dave confirms nothing is missing. Its `pieces/converging-on-intent/` directory (arc, outline, six pass reports at `387bde6`) is piece record, not methodology, and is Dave's to keep outside fiducial per DEC-000250.
- **Candidate Core line** (later cycle): a role that names a document absent from its context asks for it before acting on what it governs, and never proceeds from memory of it.
- **`voice-template.md` audience is `[human]`**; how it reaches a writing bundle is the bundle-system PRD's decision (DEC-000260).
- **`review-artifact.md` lists `critic` in its audience**; that slug now resolves to `roles/critic.md`. Whether the review-artifact skill should reach the Critic at all is open — the Critic emits comments in a document, not a review artifact.

---

## Retrospective session 2026-08-31 — follow-ups

**Source:** retros/retro-synthesis-20260831T163000.md @ b615d0d04da9421941c47fd789d3690ad7849203, the first synthesis over this repository's `retros/` (29 files, 33 deduplicated topics, each with count, most recent session, and state against `main` at 37c6818). Topic numbers below are that document's. Each item is a candidate for a review cycle on the named document; none is decided. The prior retrospective session, 2026-08-05, ran over wne-crm's corpus; its board is `retros/retro-triage-board.md` and its action items have no recorded disposition (item 14).

1. **`skills/conversation-retro.md` — one cycle, five changes (T17, T18).** The retro reads nothing from and writes nothing to any remote — the file is handed in chat, placement is a separate command-block step from a decision session; `date:` is the session's last interaction, derived from the last dated artifact the session touched, with `generated:` added and the filename timestamp kept as the opaque handle; a synthesis lists the retro filenames it covers, so unsynthesized retros are computed; a prompt for standing preferences repeated across sessions, held separate from in-session corrections (the 08-05 board's AI-15, never landed). The document is on the expedited path's ineligible list; full gate. LANDED 2026-09-01 — agreed at cycle 4, reviews/conversation-retro-cycle-4.md.
2. **`roles/chief-of-staff.md` read-sequence — "what else is running" (T05).** A check for other chats holding the connector and other worktrees before any connector write; and the constraint itself — one chat holds GitHub at a time — stated where decision sessions read it. LANDED 2026-09-02 in Chief of Staff cycle 7 (CS-1, CS-2, CS-3).
3. **Decision Layer 13 vs the 2026-08-24 recovery retro (T08).** Rule 13 says a baton carries "pointers and state"; the retro says a baton carries never computed state, which is re-read from the repo. Two governed-adjacent sources disagree; Dave's ruling, then the losing text moves.
4. **Decision Layer 5 or the Chief of Staff role (T08).** The baton's ordered next-step list is Dave's ruling; the successor session's first response dispatches item one and does not ask whether to.
5. **Decision Layer register (T16, T17).** "Say what the item is before the choice" and "y/n where possible" — repeated across sessions, in no governed text.
6. **`skills/spec-review-cycle.md` (T09).** A re-gate disposes findings and takes no new decisions; the agreement bar and gate cadence are stated at loop start; findings below the reviewed document's stage are routed to the next stage's question list, not filed as blockers. LANDED 2026-09-02 — cycle 11 (reviews/spec-review-cycle-cycle-11.md) closed into the converging-model branch; agreed at reviews/converging-model-cycle-2.md, reviewed document SHA 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e.
7. **`skills/command-blocks.md` (T19).** No ``` fence inside a paste block — inner fences are `~~~` with a fence note; an expected-output line is observed in the environment the block runs in, or is qualitative; a block never pushes the default branch. LANDED 2026-09-03 — cycle 7 (CB-1, CB-2, CB-3; criteria nine → eleven), pull requests #302–#304; agreed at reviews/command-blocks-cycle-7.md, reviewed document SHA 1c86595f0bcd89c6ddb6ae38ed637f1e5b180d8c, verdict ready. Riders to the skill's next cycle, recorded in the artifact: CB7-1, the never-push rule says "the decision session merges" — narrower than the commit and change control policy, which grants routine open-and-merge to agents without naming a session kind; Dave to inspect, not yet ruled. CB7-2, the one-block-per-turn rule has no conformance criterion, and criteria 1 and 3 have no body rule — predates cycle 7.
8. **`skills/directive-authoring.md`, after the consolidation cycle (T20, T21, T22).** Reviewer Fix text carried verbatim unless the record states the departure; every fix names its seam and the sweep that checks it; position-bearing derived artifacts get a mechanical re-check; dispositions are intent — the executor verifies against the counterparty artifact and discloses deviation.
9. **Trivial-additive fast lane (T25).** An owner-approved, additive, tool-verifiable-green change that neither the doc-only nor the expedited path covers: scope it or refuse it.
10. **Session rotation and the autonomous run (T23).** A stated trigger for the Chief of Staff to propose handoff and take an ack; a named skill for the autonomous overnight run if it is to recur — two instances exist as its evidence. First half LANDED 2026-09-02 in Chief of Staff cycle 7 (CS-5, the rotation trigger); the autonomous-run skill remains open.
11. **Files handed to Dave (T26).** `~/Downloads`, named to sort to the top; long documents presented rendered and navigable. One line in the Decision Layer; today it lives in memory only.
12. **Tooling-facts artifact (T30, T04).** A dated, falsifiable record of connector and sandbox behaviour — or the decision that the bundle-system PRD's lore-home requirement is that artifact. `git push -u` in the executor sandbox lands the ref, then fails only the upstream-config write (`.git/config`: Operation not permitted); push without `-u`. Connector whole-file writes drift when content is retyped: precompute the target blob locally and compare after the write; one caught instance 2026-09-01 (a one-word regression, corrected before merge). Process substitution (<(...)) is refused by the executor sandbox; use temp files. Observed by two executors 2026-09-02.
13. **SLO gate hole (T29, open since 2026-08-05).** The consequential class and the change package reference Top K journeys and SLO budgets that nothing defines or maintains, so a gate criterion cannot fire: define them or remove the criterion and the field.
14. **The 2026-08-05 board pass (T33).** One disposition — landed, superseded, or still open — per action item AI-1 through AI-15 of `retros/retro-triage-board.md`, recorded so the board can be called synthesized.
15. **Test counts carry their environment (T06).** A count reported by an executor states the environment it was observed in (clone, worktree, sandbox); a count measured elsewhere is not an expectation. **LANDED 2026-08-31** — the invariants Report region bullet (amendment b, refined by amendment d's arc to the tree axis with a sandbox clause), agreed at cycle 7.
16. **`bin/check-directive` M2 rejects a backticked citation (TRD rider).** Observed 2026-08-31 linting this directive: a `path @ sha` citation written with the path in backticks fails M2 as path-absent, because the citation pattern takes the backtick as part of the path. Either the pattern strips inline-code delimiters or the authoring skill states that citations are written bare. Add to the `specs/directive-tooling-trd.md` rider queue above.

Confirmed by the corpus and already tracked above, no new entry: convergence-process canonization; multi-document gates; substance-only governed documents; rubric negation, bundle invariant, agent-instruction test; landmine test; executor self-recovery; six unlogged decisions; skills conformance and name/description; Illuminait retro; `bin/land` usage document; PRD/TRD template audience; Critic vs review-artifact audience.

---

## Topic walk 2026-08-31 — rulings

**Source:** the full 33-topic walk over
retros/retro-synthesis-20260831T163000.md, ruled by Dave one topic per turn in
the retrospective decision session, same day. Every topic now has a home; this
section is the record. The follow-up numbers below are the section above's.

**Cycles opened or re-scoped by the walk:**

1. **Decision Layer cycle (one open, several changes).** Rule 13 becomes
   pointers-only — a baton carries decisions, open questions, and pointers;
   every fact about the tree is re-read; one carve-out: a baton may name a
   state the successor would not know to check (a session left running, a
   branch mid-merge), labelled told (T08). Rule 5 gains: dispatch of ruled
   work is emitted, not offered (T08). Rule 3 gains the test: a landmine is a
   consequence Dave would act on differently if it went unnamed (T15).
   Register lines: say what the item is before the choice; y/n where
   possible; after a turn carrying a report or a block, restate the open
   question (T16). A spoken standing rule enters governed text the same turn
   (T17); a decision is logged in the session that makes it (T24); a document
   handed for reading is delivered rendered — the pane is for documents being
   edited (T26). Follow-ups 3, 4, 5, and 11 close into this cycle. LANDED
   2026-09-01 — human review with Dave; agreed at cycle 15
   (reviews/decision-layer-cycle-15.md; reviewed document SHA
   999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec). Rider for the next Decision
   Layer cycle: cycle 14's DL-2, the pane named inconsistently across
   documents; and the command-blocks pointer — the rule binding decision
   sessions to skills/command-blocks.md was deleted at 3e89a21, and nothing
   in the Decision Layer now points a decision session at that skill
   (observed by the Reviewer, reviews/command-blocks-cycle-7.md cross-check
   text). Follow-ups 3, 4, 5, and 11 closed.
2. **Remote-write verification policy cycle** (`policies/remote-write-verification-policy.md`).
   Four rules: the content-expectation check (size and stats, closing the
   policy's own Known gap); connector writes are creates or small verified
   diffs — an existing governed document is never regenerated whole over the
   connector; any connector write of an in-scope file sets all frontmatter
   explicitly and an executor runs `bin/check-frontmatter --all` on a branch
   before merge; after a timeout on a write, read the PR or commit state
   before re-creating (T07, T11). Plus classify-before-remedy: a reported
   tool failure is classified — lost response, never dispatched, caller
   error, tool defect — before any remedy (T30). The 2026-08-03
   success-shaped-response entry and the 2026-08-06 landing-not-content entry
   fold into this cycle and close when it lands. LANDED 2026-09-02 — cycle 8,
   five rules added (rules 3–7); agreed at
   reviews/remote-write-verification-policy-cycle-8.md, reviewed document SHA
   21e0c1e729a689bf7e4687f7e5910f86f972ac48, verdict ready-with-findings.
   Riders to the policy's next cycle: RW8-1, rule 7's tool-defect class
   overlaps the nothing-landed case that "never sent" counts — narrow tool
   defect to exclude it; RW8-2, "small verified diff" carries no bound (a
   candidate ruling, not a defect).
3. **Spec-review-cycle skill cycle** (follow-up 6 + convergence, T09, T20).
   A re-gate disposes findings and takes no new decisions — a new decision
   opens its own cycle; the agreement bar and gate cadence are stated at loop
   start, and a gate may be scoped to confirmation of named resolutions;
   findings below the reviewed document's stage route to the next stage's
   question list; a named defect class is triaged before its instances; plus
   the convergence shape — spec and tests revised together, joint flip, the
   decision session mediating, dispositions are intent (the executor verifies
   against the counterparty artifact and discloses deviation). The
   "Convergence process — canonization owed" entry closes into this cycle.
   LANDED 2026-09-02 — cycle 11 (reviews/spec-review-cycle-cycle-11.md)
   closed into the converging-model branch; agreed at
   reviews/converging-model-cycle-2.md, reviewed document SHA
   0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e.
4. **Chief of Staff role cycle** (T05, T23). The one-chat-holds-the-connector
   constraint stated where decision sessions read it; a decision session
   assumes sole hold unless the baton or Dave says otherwise, and treats a
   timeout as contention first, restart second; the baton names any session
   left running, labelled told; and the rotation trigger — the Chief of Staff
   proposes handoff before the next major work item, one line, taking an ack.
   Follow-ups 2 and 10's first half close into this cycle. LANDED 2026-09-02 —
   cycle 7, two documents on one branch (pull requests #298–#300; agreed at
   reviews/chief-of-staff-cycle-7.md; role reviewed at
   00bdd4648f8e0efdc687886b341c1ef71b259393, context set at
   0c1a51dcede20c823c4cea85796fb362cfb9f2a8). N-7 closed in the role; N-6
   closed in context-sets/spec-and-change-discipline.md under DEC-000370.
   Ruling owed, Dave's: CS7-1 — the role says a connector timeout is
   contention first, the remote-write policy's rule 2 says a single failure
   is noise and contention is what the second failure detects; one sentence
   in one document yields, which one is the ruling. Rider to the role's next
   cycle: CS7-2, "the states rule 13's carve-out admits" closes a class
   rule 13 leaves open — "among". Observation on the context set: O-8,
   stage-7 "take theirs from the architecture summary" against the operating
   model's "selected"; a reconciling reading is stated in the artifact.

**Riders recorded on existing entries and queues:**

5. **`skills/directive-authoring.md` next cycle** (follow-up 8 pile; T02,
   T03, T20, T21, walk evidence): a verification step in a directive binds
   the directive's own dictated text — read every dictated string against
   every self-check before sending; the holder check names a third case, the
   branch existing with no worktree; the reuse form — cite the prior
   directive path @ SHA as companion, `git worktree add "<path>" <branch>`
   with no -b and no --no-track, re-pin, deltas only; carry the remedy with
   the ban; a directive that dictates wording cites its source or marks it
   new; a flip directive states `bin/flip-agreed`'s self-commit behaviour —
   one commit per invocation, never a caller-authored combined commit; the
   Naming example gains the UTC `Z` per the filename decision below;
   per-file test runs use `python3 -m unittest discover -s bin/tests -t bin
   -p <file>`; a long test suite states its expected duration so an
   executor's tool timeout is raised before the run. Cycle-number
   derivation: the artifact cycle number comes from a full, version-sorted
   listing of reviews/ (never sort|tail on lexical names), and the directive
   instructs the executor to confirm the artifact path absent at the base
   before writing. Two instances 2026-09-01: conversation-retro cycle 3,
   decision-layer cycle 14 — both stopped by the executor, neither reached a
   record. The invariants skeleton emits no Cleanup region; worktree removal
   is an author-region obligation and one 2026-09-02 directive omitted it,
   leaving $TMPDIR/fiducial-converging-model-fix-2 on disk. Candidate: a
   committed Cleanup region in skills/directive-invariants.md.
6. **`specs/directive-tooling-trd.md` rider queue:** M2's citation pattern
   captures an enclosing backtick or quote as part of the path (observed
   twice, 2026-08-31: backticked citation; the flip directive's quoted
   `--review` argument) — strip delimiters or the skill states citations are
   written bare; and M2 requires the cited SHA to touch the path, which a
   multi-document artifact's tip citation and a flip's artifact citation both
   trip — state the rule's intended reach.
7. **Rubric candidate entry** (T13, T28): add the collapse check — before
   collapsing two duplicate rules, confirm they state the same rule, not
   merely similar text (pass-2b evidence: the clustering over-matched); the
   criterion-with-no-reviewer-is-a-wish test and
   prohibition-becomes-per-instance-test rules cross-reference here from the
   conformance pass.
8. **Skills-conformance-pass entry** (T28): scope candidates recorded — the
   role-register audit (roles written before rubric criterion 5 carry a
   human register; writer.md's rewrite is the precedent), and the two
   test-form rules above; scope decided when the pass's rubric is drafted.
9. **`operating-model.md` next opening cycle** (T10): two riders — a spike
   step (time-boxed, throwaway, permitted before agreement, findings only,
   never shipping code), and mutation-as-coverage-finding (a mutation
   surviving a green suite is a finding; the code's author does not write
   the closing test). The orchestrator question is closed by the
   spec-review-cycle cycle; the expedited-stretch question becomes a
   one-line check at `policies/document-metadata-policy.md`'s next cycle.
10. **`policies/commit-and-change-control-policy.md` next cycle** (T29,
    follow-up 13): remove the Top K / SLO-budget criterion and the change
    package's SLO field — a criterion nothing defines cannot fire and reads
    as coverage — and relocate: a project with user-facing journeys defines
    its Top K and budgets at adoption, stated in the Project Setup
    Requirements policy. The 08-05 board's AI-1 disposes into this.
11. **`context-sets/collab-workflow.md` next opening** (T12): one rider —
    before "ship," the pane content is verified against the diff that
    actually lands; the commit derives from the pane, never from memory of
    the discussion.
12. **`docs/global-context/core.md` next opening** (filename decision): rule
    14's example gains the `Z`.
13. **Bundle-system PRD cycle 1 riders** (T26, T30): replace the three
    hard-coded `~/Downloads` paths and both "sort to the top" phrases with a
    citation of the delivery-directory decision, `--out` remaining the
    override per AC-BN-12; and the lore home (G11/AC-BS-12) is the
    tooling-facts artifact — entries are dated, falsifiable, and classified
    (lost response / never dispatched / caller error / tool defect).
    Follow-up 12 closes into this.
14. **`bin/land` usage-document entry** (T32): two added requirements — a
    flip runs from a tree that contains the review artifact it cites, and
    the document states `bin/flip-agreed`'s self-commit behaviour.
15. **By-title pointer dependency** (gate cycle-4 O-2, record only): the
    criterion-3 by-title reference between the two directive skills holds
    because both carry audience [chief-of-staff, human]; the dependency is
    recorded here and nowhere in either file — an audience change on either
    breaks criteria 1 and 3 silently. Dave weighs whether it ever needs more
    than this record.

**Refusals and deferrals, recorded:**

16. **Trivial-additive fast lane (T25, follow-up 9): refused 2026-08-31.**
    Two instances, both predating the cycle-20 metadata policy. Hitting the
    gap again is itself the trigger for a revisit — the next concrete case
    with no fitting route reopens this entry with itself as the evidence,
    and is not absorbed or worked around.
17. **Autonomous overnight-run skill (T23): deferred until the next run is
    wanted.** Two clean runs exist as evidence; when Dave next says "keep
    going, I'm off to bed," the skill is drafted first — bounds (ruled work
    only, nothing consequential, no flips), stop conditions (any question
    that would go to Dave), wake-up report shape — and that run validates it.
18. **Illuminait / discovery methodology (T27): stays parked**, one note
    added — the spike definition is landing via the operating-model rider
    above; the parked gap analysis does not re-derive it.

**Owned elsewhere, confirmed by the walk:** T01 adoption (landed above); T04
sandbox lore and T31 adapters/reach (bundle-system PRD); T14 staleness and
format (PRD; format entry folded into OQ-5); T33 closed — the class is swept
by this walk, with the same-turn encoding line and the retro skill's
standing-preferences prompt as the two structural fixes that keep it empty.

**Queued next:** the 08-05 board pass (follow-up 14) as a read-only directive
appending a per-item disposition table (AI-1 → T29; AI-8 → T30's ruling;
AI-15 → superseded, pull request #269's body the ruling, the
standing-preferences half landed 2026-09-01 via the retro-skill cycle; the
rest read against main); then the retro-skill cycle (follow-up 1, five
changes; DONE 2026-09-01, agreed at cycle 4,
reviews/conversation-retro-cycle-4.md), the bundle PRD cycle 1 (PRD
human-reviewed 2026-09-01, pull request #275; OQ-5, OQ-6, OQ-10 resolved
in-document; Spec Reviewer gate still owed; AGREED 2026-09-02 at cycle 2
(reviews/bundle-system-cycle-2.md; reviewed document SHA
7c50f0fd1c8f648d3e95a527edaf7125b7b07ab4; flip pull request #283). Build
packages remain queued.), the spec-review cycle (DONE 2026-09-02 —
cycle 11, reviews/spec-review-cycle-cycle-11.md, closed into the
converging-model branch; agreed at reviews/converging-model-cycle-2.md,
reviewed document SHA 0cc7b8dd189be9eff24af083b1fc8c1540e6ff2e), the
remote-write policy cycle (DONE 2026-09-02 — cycle 8, ruling 2 above), the Decision Layer cycle (DONE 2026-09-01, human
review with Dave, agreed at cycle 15, reviews/decision-layer-cycle-15.md;
reviewed document SHA 999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec), the
command-blocks cycle (DONE 2026-09-03 — cycle 7, follow-up 7 above), the Chief of Staff role
cycle (DONE 2026-09-02 — cycle 7, ruling 4 above), and skills/conversation-retro.md's conforming revision — drop the
chat-close auto-run and the rule-12 standing-obligation deference, per
DEC-000310; full cycle, ineligible list. Rider from pull request #273: the
skill's 'routes' reuses the Lexicon's directive-sense term in another
sense; conform. (DONE 2026-09-03 — cycle 5, CR5-1 and CR5-2, both landed; pull
requests #305–#307; agreed at reviews/conversation-retro-cycle-5.md, reviewed
document SHA 649809aa28b24f40af38441b93f945dde103cd7e, verdict ready, zero
findings. Observation CR5-3 for the metadata policy's cycle, recorded on that
entry.) Tagging package (bundle-system
PRD): the sre-critic rename and engagement retags per DEC-000350;
skills/outline.md human-value removal per DEC-000340; order: on the
copy-editor and critic role files (cycle-1 O-4). After the rename lands,
one PRD conform touch folds the two wording residues from pull request
#282 (the six-further-files count includes the role file itself; §1's
five measured ways against §5's seven baseline paragraphs); and
prd-template cycle: the skeleton's [all-roles, human] audience default
would violate the agreed PRD's AC-BS-5 (cycle-1 O-5); bin/ package —
enforce the converging status (DEC-000360 precondition: lands before any
document enters converging). ACs: bin/aimeta/frontmatter.py STATUSES
admits converging; bin/migrate-frontmatter STATUS_MAP likewise; the
pre-commit hook does not flip a converging document on a content edit;
bin/flip-agreed accepts converging as a source status for --status agreed
and as a --status target for the entry transition from in-review; status:
converging requires no last-reviewed; tests red then green; the package
removes the policy sentence 'enforcement lands as a bin/ change before any
document enters it' (reviews/converging-model-cycle-1.md O-3) in the same
change. Test Designer and Coder separate; and converging follow-up cycle —
context-sets/spec-and-change-discipline.md and roles/chief-of-staff.md
(reviews/converging-model-cycle-2.md N-6, N-7): N-6, the convergence
suite's interface-contract source — the discipline still says 'from the
architecture summary', which is now stage 6; Dave rules the source
(candidate: the TRD's interface list). N-7, the Chief of Staff
pending-gates read lists in-review and omits converging, which owes an
exit gate. Both DONE 2026-09-02: the bin/ package landed as pull request #294
(Test Designer at c2fc39fedb4e3b865fd171fd255053c475375480 red, Coder at
2e23b84 green; STATUSES, TRANSITION_STATUSES and STATUS_MAP admit converging;
the policy's enforcement-precedes-use sentence removed, flipping
policies/document-metadata-policy.md to in-review — it owes a full cycle, a
gate document; one reading to confirm at that cycle: validate() now lets a
converging document omit the last-reviewed key entirely, not only carry
null, the Test Designer's reading of "requires no last-reviewed"). The
converging follow-up cycle landed as Chief of Staff cycle 7 (ruling 4 above;
N-6 under DEC-000370).
