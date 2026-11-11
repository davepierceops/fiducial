# Decision Log — davepierceops/ai

Append-only record of methodology decisions, per
`policies/decision-log-policy.md`. Newest last. Entries are never edited or
deleted; a reversal is a new entry whose `Supersedes:` names the old ID.

## DEC-000010 — Doc-only cycle is a sanctioned route to `agreed`
Date: 2026-08-06
Decision: A co-authored methodology/governance document may reach `status:
agreed` through the doc-only cycle — authored or edited together in the artifact
pane, at least one consistency sweep, and Dave's verbal sign-off — recorded as an
entry in `reviews/expedited-log.md`, with `last-reviewed` citing the log and the
reviewed SHA.
Context: Entry conditions — the document is methodology/governance prose (any
format, not a program meant to run); it is co-authored in the artifact pane;
Dave asks for the cycle and agrees. The metadata policy previously sanctioned
only the full reviewer cycle and the expedited path, neither of which fits a
co-authored, multi-section, or new prose document.

## DEC-000020 — Doc-only cycle overrides metadata-policy route-to-`agreed` limits
Date: 2026-08-06
Decision: The doc-only cycle overrides the expedited-path eligibility conditions
in `policies/document-metadata-policy.md` (the ≤10-line body cap, the single
in-scope-file rule, and the gate/enforcement-doc exclusion) wherever they would
block a co-authored, signed-off document from reaching `agreed`. Dave is the
final arbiter of policy; this ruling governs over the metadata-policy text until
that text is amended to describe the doc-only route.
Context: `policies/decision-log-policy.md` is a new multi-section policy, so it
fails the expedited eligibility conditions, yet it was co-authored and signed
off under the doc-only cycle. `bin/flip-agreed` enforces only a frontmatter-only
transition and that the cited SHA resolves to a log entry — not the eligibility
conditions — so this agreement lands cleanly. Amending the metadata-policy prose
is queued as follow-up.

## DEC-000030 — Doc-only cycle excludes review-regime documents; they keep independent review
Date: 2026-08-06
Decision: Narrows DEC-000020. The doc-only cycle still overrides the expedited
path's ≤10-line body cap and single-in-scope-file rule for co-authored
documents, but it does not override the gate/enforcement-doc exclusion.
Documents that state a gate, a hard stop, or an enforcement rule governing how
work is reviewed, agreed, or released — the class defined in
`policies/document-metadata-policy.md`, "Expedited return to `agreed`",
condition 3 — reach `agreed` only through the full reviewer-gated cycle
(`skills/spec-review-cycle.md`), even when co-authored. The doc-only cycle's
verbal sign-off is not sufficient for that class.
Context: DEC-000020 overrode the gate-doc exclusion alongside the size and
single-file limits, which was too broad. The doc-only cycle trades away
independent review, and the one class where independence is load-bearing is the
set of documents that define the routes to `agreed`: a self-serving change there
would propagate to every future agreement with only its author having read it.
Prompted by the pending `document-metadata-policy.md` amendment, which under
this entry routes through the full cycle. This does not unwind the agreement of
`policies/decision-log-policy.md` under DEC-000020 — that document states a
working-practice obligation (consult the log), not a route to `agreed`, so it
falls outside the class this entry protects. Size and multi-file freedom are
retained for all other co-authored prose.
Supersedes: DEC-000020

## DEC-000040 — Doc-only cycle is single-document; multi-file override withdrawn
Date: 2026-08-06
Decision: Supersedes DEC-000030. The doc-only cycle overrides the expedited
path's ≤10-line body cap for co-authored documents — a co-authored document may
be any size — but does not override the single-in-scope-file rule: a doc-only
agreement covers exactly one in-scope document, as the expedited path does.
Several documents co-authored in one session are agreed as separate, sequential
agreements. The gate/enforcement-doc exclusion carried by DEC-000030 stands
unchanged: documents that state a gate, a hard stop, or an enforcement rule
governing how work is reviewed, agreed, or released reach `agreed` only through
the full reviewer-gated cycle, even when co-authored.
Context: DEC-000030 also overrode the single-file rule, letting one content
commit agree multiple documents under one shared content SHA. The cycle-11
re-gate of `document-metadata-policy.md` (finding B1) found the shared SHA
defeats the single-entry pointer resolution `### The record` relies on —
`bin/flip-agreed` / `bin/aimeta/expedited.py` match a `last-reviewed` pointer on
SHA alone, so document B's pointer is satisfied by document A's entry: a false
claim of review in the one case the SHA is deliberately shared. Rather than make
the checker path-aware (a `bin/` change), the single-file rule is restored; size
freedom is retained.
Supersedes: DEC-000030

## DEC-000050 — decision-log-policy.md sits outside the gate-document class
Date: 2026-08-06
Decision: `policies/decision-log-policy.md` is not a gate/enforcement document in
the sense of the doc-only cycle's condition 3 — it states a working-practice
obligation (consult the log), not a route to `agreed` or a gate over how work is
reviewed, agreed, or released. Its revisions are eligible for the doc-only cycle
when co-authored, and its agreement under DEC-000020 stands.
Context: DEC-000030 recorded this carve-out; DEC-000040 superseded DEC-000030 and
carried the gate-doc exclusion forward but not this classification, so under the
decision log's whole-entry supersession rule the carve-out went dead. This entry
restates it as a live decision. Not a supersession — DEC-000040 remains fully in
force; this adds back only the dropped classification.

## DEC-000060 — LEXICON.md brought into metadata in-scope set by owner override
Date: 2026-08-07
Decision: The single-line additive edit naming `LEXICON.md` in the in-scope set
of `policies/document-metadata-policy.md` is agreed without a review cycle, on
owner authority. That document is agreed and its in-scope set is an enforcement
rule, so the doc-only cycle's condition 3 would otherwise force a full review
cycle; the owner overrides condition 3 for this revision only. This does not
create a general owner-flip route for enforcement-rule documents.
Context: The edit is additive — it brings a governed definitional document under
enforcement it already claims via its frontmatter — so it cannot blind
enforcement of itself. `bin/check-frontmatter --all` was verified green with
LEXICON in scope. A full multi-agent gate is disproportionate to a one-line
additive scope change.

## DEC-000070 — ACs are an execution-time input, not pinned by the decomposition doc
Date: 2026-08-07
Decision: The tranche decomposition doc pins the PRD/TRD SHAs it derives from; acceptance criteria are consumed at package execution time and are not part of what the decomp pins. Staleness-check strictness (block vs. flag on spec movement past the pin) is left unsettled, to be learned by doing.
Context: Raised while adding a spec-drift guard to roles/chief-of-staff.md. The decomp is a derived artifact and can drift from canonical specs; pinning the PRD/TRD SHA gives a staleness signal. ACs sit between agreed spec and execution and are better re-read live than pinned into a derived doc that later work references in place of the spec.

## DEC-000080 — Flakiness-workaround directives retained; Track B auto-propose trigger kept as contention detector
Date: 2026-08-07
Decision: An audit of the "special MCP-handling" directives — remote-write
verification, the spec-review-cycle small-writes rule, remote/sync hygiene, and
the Track B auto-propose-after-two-failures trigger — removes none of them. The
trigger is retained specifically as a contention detector: its two-failure fire
is how contention between concurrent Claude Desktop chats gets noticed, and that
diagnostic value holds independent of whether the underlying cause is random
flakiness or contention.
Context: GitHub MCP is not fixed; the real failure mode is concurrent-Desktop
contention, which Track B sidesteps. An audit (per the global-retro-inbox
2026-08-04 entry) tested whether any directive existed only to work around
now-nonexistent flakiness and found none: remote-write verification is
transport-general evidence discipline, and the spec-review-cycle small-writes
rule rests on the decision/execution layer boundary. The trigger was nearly cut
as cruft this session before Dave noted it had already surfaced an accidental
contention event once; skills/directive-dispatch.md frames it only as a Track B
on-ramp, so its keep-reason is recorded here.

## DEC-000090 — Track B carries the sync step in the echoed line; the sync block is Track A only
Date: 2026-08-08
Decision: `LEXICON.md`'s `Sync block` is narrowed to precede every **Track A**
execution block, not every execution block. Track B has no sync block: it carries
the sync step in the echoed dispatch line, and what that line asks for is a
working-tree-current check in the same clone — HEAD at the echoed SHA, no
uncommitted edits to the files in scope — not a remote fetch. The alternative
direction, restoring a sync command block to the Track B sequence, is rejected.
Context: Trivium cycle-1 gate, `reviews/LEXICON-cycle-1.md` B1 ≡
`reviews/directive-dispatch-cycle-1.md` B1 — two canonical documents disagreed
with no tiebreak, `81bd2de` having dropped the standalone Track B sync block. The
tracks differ for a reason worth stating: Track B is same-machine and
commit-not-push, so the executor runs in the clone that already holds the
unpushed commit. A Track A remote fetch has no remote to fetch the directive from
and could check out a tree lacking it. This closes `OPEN-ITEMS.md`'s "Sync as a
skill rather than a step inside every directive", whose proposed phrasing the
tree had already adopted ahead of its own analysis. It does **not** decide that
item's broader proposal — sync as a role-held skill so directives carry no
version-control mechanics — which is untouched and reopens on its own if wanted.

## DEC-000100 — The shell-termination rule is stated by effect, not by enumeration
Date: 2026-08-08
Decision: `skills/command-blocks.md`'s interactive-shell rule and its conformance
criterion are stated by effect — no construct that can terminate the shell the
block is pasted into — with `exit`, `exec`, `logout`, `|| { …; exit; }`, and
`set -e` named as known instances and adopting projects directed to add their
own. `skills/directive-dispatch.md`'s restatement of the same enumeration is
replaced by a pointer to that criterion, so the rule lives in one document and
cannot drift.
Context: `reviews/command-blocks-cycle-1.md` B1 ≡
`reviews/directive-dispatch-cycle-1.md` B2. `set -e` ends an interactive shell on
the next failing command exactly as `exit` does (verified by running under both
`bash -i` and `zsh -i`), and is the idiomatic opening line of a careful block —
so the enumeration that `ed7d904` added passed the construct the rule exists to
stop. Choosing effect over enumeration also settles the document against itself:
the copy-control rule at the same file already used the "known instance, not the
rule" pattern, so the document held two patterns for the same kind of rule. No
prior decision governs the enumeration — it entered in `ed7d904` with no entry —
so this reverses nothing.

## DEC-000110 — Reviewer-gated cycle directives fix route and model by class; track is required
Date: 2026-08-08
Decision: A reviewer-gated cycle directive states its **track** and its execution
block per directive, and takes **route** (fresh) and **model** (Opus 5) as fixed
by its class, stated once in `skills/spec-review-cycle.md` rather than restated
per cycle. This is a bounded exception to `skills/directive-dispatch.md`'s
all-four-every-time rule, mirrored there and in `LEXICON.md`'s `Directive`
definition so the general statement admits it rather than contradicting it.
Context: `reviews/spec-review-cycle-cycle-1.md` B1 ≡ `reviews/LEXICON-cycle-1.md`
N1. The cycle-directive format required none of route/model/track and licensed
the omission ("Everything else as needed"), while two other canonical documents
called each unstated part a defect. Route and model genuinely do not vary for
this class — one conversation per cycle with execution in a fresh session, and
directive execution over canonical documents is the row the model table already
decides — so restating them per directive adds no information. Track does vary,
so it is carried. The matching change to `bin/cycle-open`'s generated skeleton
(`:116`) is deliberately **not** in this doc cycle: it is a code change needing
acceptance criteria, tests, and a red gate, filed as its own package. Until it
ships, the author hand-adds Track, as this cycle's own directive did.

## DEC-000120 — The command-block remote rule is rewritten; `origin` was never the hazard
Date: 2026-08-08
Decision: `skills/command-blocks.md`'s "Name remotes explicitly; do not rely on
the `origin` alias" rule is replaced rather than enforced. The rule now targets
the real hazard: a sync or remote command in a pasted block names its remote and
ref explicitly, does not lean on branch-upstream configuration, and has its exit
status checked before anything downstream acts on the tree it produced. `origin`
is a valid explicit remote name and using it is fine. The false rationale — that
an auth failure surfaces as missing work rather than as an auth error — is
removed. A seventh conformance criterion is added for the rewritten rule.
Context: `reviews/command-blocks-cycle-1.md` B2 reported the rule as the one body
rule with no conformance criterion. On inspection the rule itself was unsound:
`origin` is a remote *name*, not a protocol, and a `git fetch`/`push` that cannot
authenticate exits non-zero rather than returning empty results silently. It
entered in a bulk drafting commit (`c4baefe`) with no decision or incident behind
it. Adding a criterion would have hardened an incorrect rule. The criterion
question was left to ride with the rewrite; the criterion is added because the
finding's underlying gap — a body rule invisible to the checklist a reviewer
actually runs down — survives the rewrite, and the rewritten rule is per-block
and mechanically checkable, which is the shape the other criteria have.

## DEC-000130 — Remote-write Rule 3 is about provenance; SHA abbreviation is out of its scope
Date: 2026-08-08
Decision: `policies/remote-write-verification-policy.md` Rule 3 drops "Never
abbreviate a SHA that will be used as a pointer" and keeps the provenance rule
(state SHAs read from git; never invent one), with a pointer to
`skills/directive-dispatch.md`, which carries the narrow, correctly-scoped
abbreviation rule for dispatch blocks. Complementary: the policy's Scope now
reaches the case where the agent cannot read its own write back — Track B —
where verification is the operator's and the agent reports only what the operator
reported.
Context: `reviews/remote-write-verification-policy-cycle-1.md` B1 and N1. The
abbreviation clause contradicted `policies/document-metadata-policy.md`, which is
`agreed` and contemplates abbreviated `last-reviewed` pointers, and
`bin/aimeta/expedited.py`, which is shipped specifically to normalize them
through `git rev-parse`. A draft policy contradicting an agreed one is the
serious direction: an agent holding both cannot tell which to satisfy. Rule 3's
surrounding sentences are about provenance, so the clause read as a scoping slip
rather than a disagreement, and it is dropped rather than promoted — widening it
would have been an edit to an agreed policy and to shipped tooling, and belongs
in a cycle over those.

## DEC-000140 — methodology-context-bundle: filename format, file-set rule, interim generation procedure, script deferred to tooling tranche
Date: 2026-08-08
Decision: The uploaded chat-context bundle is named
`methodology-context-bundle-<YYYY-MM-DD-HHMM>.md` — timestamped deliberately,
overriding the no-derived-metadata-in-filenames default, for project-view
version visibility (Dave). File set: the fixed decision-layer spine
(`context-sets/base.md`, `context-sets/spec-and-change-discipline.md`,
`context-sets/collab-workflow.md`, `operating-model.md`,
`roles/chief-of-staff.md`, `policies/commit-and-change-control-policy.md`) plus
every `skills/*.md` whose `audience` frontmatter contains `all-roles` or
`chief-of-staff`. The bundle pins `Source: @ <repo HEAD>` and a per-file blob
short-SHA (each file's own blob, `git rev-parse --short HEAD:<path>` — not the
repo HEAD), with `<!-- FILE n/N: path @ sha -->` separators. Building
`bin/bundle-methodology` is folded into the tooling tranche alongside the
drift-audit `bin/` check (`docs/global-retro-inbox.md`) — not built as its own
package. Until it exists, regenerate with the procedure below, which computes
the file set from the audience rule (not a hardcoded list) so a skill's
audience change or a new skill is picked up automatically.

Context: this filename format and a working generator were reached 2026-08-08
(chat "AI retro: Methodology bugs") but recorded only as an aspiration in
`docs/global-retro-inbox.md` — "should be a script." The decision and the
artifact went nowhere durable, and were re-derived from scratch the same day,
the second regen opening with "there is no generator." That re-derivation is
the drift the log exists to stop; hence this entry carries the runnable
procedure, not just a pointer.

Interim generation procedure — run from the `ai` clone root on a synced `main`;
writes the timestamped bundle to `~/code/`:

```
python3 - <<'PY'
import subprocess, glob, re, os, datetime
sh=lambda *a: subprocess.check_output(a).decode()
repo=sh("git","rev-parse","HEAD").strip()
blob=lambda p: sh("git","rev-parse","--short","HEAD:%s"%p).strip()
stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
spine=["context-sets/base.md","context-sets/spec-and-change-discipline.md",
 "context-sets/collab-workflow.md","operating-model.md",
 "roles/chief-of-staff.md","policies/commit-and-change-control-policy.md"]
def aud(p):
    m=re.search(r'^audience:\s*\[([^\]]*)\]',open(p,encoding="utf-8").read(),re.M)
    return {x.strip() for x in m.group(1).split(",")} if m else set()
skills=sorted(p for p in glob.glob("skills/*.md") if aud(p)&{"all-roles","chief-of-staff"})
files=spine+skills; N=len(files); bar="<!-- "+"="*60+" -->"
o=["# methodology-context-bundle\n",
 "**Derived artifact — do not edit.** Regenerate from davepierceops/ai; the repo is canonical.\n",
 "- Source: davepierceops/ai @ %s"%repo, "- Generated: %s"%stamp,
 "- File set: fixed decision-layer spine + every skills/*.md whose audience includes all-roles or chief-of-staff (rule; Dave 2026-08-07).\n"]
o+=["  %d. %s (blob %s)"%(i,p,blob(p)) for i,p in enumerate(files,1)]; o.append("")
for i,p in enumerate(files,1):
    o+=["",bar,"<!-- FILE %d/%d: %s @ %s -->"%(i,N,p,blob(p)),bar,"",open(p,encoding="utf-8").read().rstrip("\n"),""]
dest=os.path.expanduser("~/code/methodology-context-bundle-%s.md"%stamp)
open(dest,"w",encoding="utf-8").write("\n".join(o)+"\n")
print("WROTE",dest,"| source",repo[:7],"| files",N)
PY
```

Then upload the written file to each project's Context and delete the prior
bundle (uploads are per-project; same-name re-upload does not propagate across
projects).

## DEC-000150 — Reviewer-gated cycle directives state all four; fresh and Opus 5 are defaults, not fixed by class
Date: 2026-08-08
Decision: A reviewer-gated cycle directive states **all four** dispatch
requirements — route, model, track, and the execution block — like every other
dispatch. Route *fresh* and model *Opus 5* are the class **defaults**: stated per
directive and overridable. This reverses the route/model half of `DEC-000110`.
Its other half is carried forward unchanged and restated here so it stays live
under whole-entry supersession: **track is required per directive**, because it
genuinely varies. The carve-out is removed from `skills/spec-review-cycle.md`
(Cycle directive format), `skills/directive-dispatch.md` (Use when, The four
requirements), and `LEXICON.md` (`Directive`).
Context: owner override (Dave), per
`docs/cycles/trivium-gate-cycle-2-directive.md` R1, after `DEC-000110` had landed
agreed. The finding `DEC-000110` answered
(`reviews/spec-review-cycle-cycle-1.md` B1 ≡ `reviews/LEXICON-cycle-1.md` N1) is
still answered, by the other route that review named: with all four stated,
nothing is omitted, so `skills/directive-dispatch.md`'s "an unstated part is a
defect" is satisfied by statement rather than by exemption. That review called it
the smaller change and the one not requiring a new exception class. Restating the
track half is deliberate — `policies/decision-log-policy.md` supersedes whole
entries, which is how `DEC-000030`'s carve-out went dead under `DEC-000040`, and
a half-reversal expressed as a pointer to a superseded entry would repeat it.
Consequence for tooling: `bin/cycle-open` (TP-1) must emit Route, Model, and
Track, not Track alone; the Track-only PR is superseded and held.
Supersedes: DEC-000110

## DEC-000160 — Directives travel as paste blocks; the executor lands them and reports the SHA post-hoc
Date: 2026-08-09
Decision: A directive is dispatched as a paste block. The executor's first act is
to write it to `docs/cycles/`, commit it, read the SHA back from git, and report
"executed <path>, landed as <sha>". The SHA is established post-hoc and is
sufficient for the decision record. This applies to every directive class,
reviewer-gated cycle directives included. Chat-side tool-mediated writes leave the
dispatch path entirely; `policies/remote-write-verification-policy.md` accordingly
governs the mediated writes that remain rather than a dispatch step. The
`~/Downloads` delivery path — pre-flight glob, relocate/commit/echo blocks,
artifact-and-blocks-in-one-turn — is retired, and with it the deferred
`bin/dispatch`, whose premise was a chat-side commit to gate. This entry is
silent on **track**, which the 2026-08-10 corrections retire outright; the
proposed `DEC-000180` carries that, and supersedes `DEC-000150`.
The two-consecutive-failure trigger is retained as a pure detector and relocated
to `policies/remote-write-verification-policy.md` Rule 4, preserving DEC-000080's
keep-reason without the delivery path it used to open.
Context: a directive does two jobs — transport, whose value expires at execution,
and record, whose value accrues later. Only the record needs git, and the executor
is the party for whom git is cheap. The integrity question shifts from provenance
to paste-arrival-intactness, already governed by the parse-atomic paste rules. Dave
confirmed post-hoc SHAs are sufficient for the decision record. Executed as
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D1.1–D1.4).
Supersedes: —

## DEC-000170 — Open spec delta: spec branches are ungated; agreement attaches at reconciliation
Date: 2026-08-09
Decision: During a tranche's execution, spec documents may be edited freely on
`spec/<tranche-slug>` with no reviewer gate and no per-edit ceremony — an **open
spec delta**; the branch is the state, with no new status value and no register.
**Reconciliation** closes it: the spec is brought to full agreement with what was
built, and the whole accumulated diff goes through the reviewer gate once, as a
single cycle, arriving on the default branch as a pull request. A delta is bounded
by its tranche and never spans two; reconciliation blocks the next tranche's
decomposition, and decomposing from unreviewed spec is prohibited. Reconciliation
may be invoked early at will, and frequent small reconciliations are the norm.
Mid-delta dispatches derive from the spec branch and pin its SHA. At most two
tranches execute concurrently, over disjoint spec territory; a
document is claimed by appearing in an open delta's diff and may not be claimed by
a second, and the convergent-edit case is refused rather than tooled.
Context: agreement attaches to the version of record at reconciliation, not to a
version pre-approved before building. The amnesiac-executor constraint requires
truth-at-handoff, not agreement-in-advance, and the recreate-from-spec goal needs
the spec true at rest between deltas rather than at every instant during one. The
design test applied: operator attention is the system's scarcest,
non-parallelizable resource, and evidence integrity may not be purchased by
spending it as if it were free. Executed as
`docs/cycles/friction-refactor-2026-08-09-directive.md` (D2.1–D2.7).
Supersedes: —

## DEC-000180 — Track is retired; the dispatch requirements are three, not four
Date: 2026-08-10
Decision: `track` is removed from the methodology entirely. A dispatch states
**three** requirements, all three every time: route, model, and the execution
block. `DEC-000150`'s route/model half is carried forward unchanged and restated
here so it stays live under whole-entry supersession: a reviewer-gated cycle
directive states every requirement like any other dispatch, with route *fresh*
and model *Opus 5* as class defaults — stated per directive and overridable, not
fixed by class. What is reversed is `DEC-000150`'s other half, "track is required
per directive, because it genuinely varies": it does not vary in any way a
directive can usefully state. The one condition the term still covered after
`DEC-000160` retired its delivery sense — the executor's remote is unreachable —
is not a property of the work being dispatched and is not knowable by the party
writing the directive. It is an executor obligation instead: an executor that
cannot push stops and surfaces it, and never commits locally and reports a
same-machine SHA as if it were pushed (`skills/directive-dispatch.md`, Executor
obligations). `LEXICON.md` carries a tombstone rather than a definition. The
sync block precedes every execution block with no exception. Consequence for
tooling: `bin/cycle-open` (TP-1, shelved) emits Route and Model and no Track;
`DEC-000150`'s "must emit Route, Model, and Track" is superseded, and
`OPEN-ITEMS.md` carries the guard against resurrecting the field on unshelving.
Context: owner override (Dave), per
`docs/cycles/friction-refactor-corrections-2026-08-10-directive.md` (C1), after
reviewing the overnight run that had kept track and redefined it
(`docs/cycles/friction-refactor-2026-08-09-decisions.md` D1). The reason the
redefinition failed: forge downtime is a transient property of the executor's
machine, and a standing instruction line stating it is a line that is wrong
whenever it matters. A field nobody can fill correctly in advance is worse than
no field, because a stated value is what a report gets measured against.
Supersedes: DEC-000150

## DEC-000190 — methodology-context-bundle: docs/global-context/*.md lead the file set; retired spine files removed
Date: 2026-08-24
Decision: Supersedes DEC-000140 whole. The bundle's file set is, in order: every `docs/global-context/*.md`, sorted by its `order:` frontmatter ascending with files lacking `order:` last; then the fixed decision-layer spine — `context-sets/spec-and-change-discipline.md`, `operating-model.md`, `roles/chief-of-staff.md`, `policies/commit-and-change-control-policy.md`; then every `skills/*.md` whose `audience:` contains `all-roles` or `chief-of-staff`. `context-sets/base.md` and `context-sets/collab-workflow.md` are no longer in the spine. The filename `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md`, the `Source: @ <repo HEAD>` line, the per-file blob short-SHA, the `<!-- FILE n/N: path @ sha -->` separators, the upload-per-project instruction, and the deferral of `bin/bundle-methodology` to the tooling tranche are carried forward unchanged. The repository named is `davepierceops/fiducial`. The interim generation procedure is restated below with the amended spine; it is run from the fiducial clone root on a synced `main`, uses no heredoc, and writes to `~/code/`.
Context: The bundle in the fiducial project context was generated 2026-08-09 and predated the 2026-08-22 rename of `skills/directive-dispatch.md` to `skills/directive-authoring.md`; a 2026-08-24 gate directive cited the stale path from it (`reviews/directive-authoring-cycle-3.md`, S-1). The first regeneration under DEC-000140's procedure, at `b31b75a`, reported both retired spine files missing and omitted `docs/global-context/core.md` and `docs/global-context/decision-layer.md`, the two files every session loads first. Dave amended the spine 2026-08-24; the bundle at `48aa1b5` (12 files) was generated under the amended rule with its header naming this entry as pending.

Interim generation procedure:

```
cd /Users/dave/code/fiducial && git fetch origin main && git checkout -q main && git merge -q --ff-only origin/main
if [ $? -ne 0 ]; then
  echo "STOP: could not sync main from origin — bundle not generated"
else
python3 -c '
import subprocess, glob, re, os, datetime
sh=lambda *a: subprocess.check_output(a).decode()
repo=sh("git","rev-parse","HEAD").strip()
blob=lambda p: sh("git","rev-parse","--short","HEAD:%s"%p).strip()
stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H%M")
def fm(p,key):
    m=re.search(r"^%s:\s*(.*)$"%key,open(p,encoding="utf-8").read(),re.M)
    return m.group(1).strip() if m else None
gc=glob.glob("docs/global-context/*.md")
gc=sorted(gc,key=lambda p:(int(fm(p,"order")) if (fm(p,"order") or "").isdigit() else 10**6,p))
fixed=["context-sets/spec-and-change-discipline.md","operating-model.md",
 "roles/chief-of-staff.md","policies/commit-and-change-control-policy.md"]
missing=[p for p in fixed if not os.path.exists(p)]
for p in missing: print("MISSING spine file:",p)
fixed=[p for p in fixed if os.path.exists(p)]
def aud(p):
    v=fm(p,"audience") or ""
    return {x.strip() for x in v.strip("[]").split(",")}
skills=sorted(p for p in glob.glob("skills/*.md") if aud(p)&{"all-roles","chief-of-staff"})
files=gc+fixed+skills; N=len(files); bar="<!-- "+"="*60+" -->"
o=["# methodology-context-bundle\n",
 "**Derived artifact — do not edit.** Regenerate from davepierceops/fiducial; the repo is canonical.\n",
 "- Source: davepierceops/fiducial @ %s"%repo, "- Generated: %s"%stamp,
 "- File set: docs/global-context/*.md by order, then the fixed decision-layer spine, then every skills/*.md whose audience includes all-roles or chief-of-staff (rule; DEC-000190).\n"]
o+=["  %d. %s (blob %s)"%(i,p,blob(p)) for i,p in enumerate(files,1)]; o.append("")
for i,p in enumerate(files,1):
    o+=["",bar,"<!-- FILE %d/%d: %s @ %s -->"%(i,N,p,blob(p)),bar,"",open(p,encoding="utf-8").read().rstrip("\n"),""]
dest=os.path.expanduser("~/code/methodology-context-bundle-%s.md"%stamp)
open(dest,"w",encoding="utf-8").write("\n".join(o)+"\n")
print("WROTE",dest,"| source",repo[:7],"| files",N)
'
fi
```

Then upload the written file to each project's Context and delete the prior bundle.
Supersedes: DEC-000140

## DEC-000200 — Everything an agent hands Dave, or asks him to produce, lands in ~/Downloads
Date: 2026-08-25
Decision: Any file an agent delivers to Dave, and any file an agent asks Dave to produce or place for it, lives in `~/Downloads`. No other delivery directory (`~/code/`, a clone root, `/tmp`) is used for the hand-off. The file is named so it sorts to the top of that directory — timestamped per Core rule 14, with a leading descriptor that makes it findable by name. This is a delivery-path rule only: it does not change where committed artifacts live in a repository, and it does not revive the retired `~/Downloads` dispatch path that DEC-000160 removed — directives still travel as paste blocks and are landed by the executor.
Context: Owner decision (Dave), 2026-08-25. Delivery locations had drifted per entry: DEC-000140 and DEC-000190 wrote bundles to `~/code/`; the bundle-system PRD draft and four writing-corpus bundles were hand-built to `~/Downloads` the same night. One directory Dave already watches, sorted by name, removes the per-artifact question of where a thing went.

## DEC-000210 — methodology-context-bundle: the audience-driven rule is the file set; bin/bundle-methodology and the hand procedure are retired
Date: 2026-08-25
Decision: Supersedes DEC-000190 whole. The file set of any bundle is what `bin/bundle --audience <audience>` emits for that audience, computed from each file's `audience:` frontmatter and `order:`; the Chief of Staff bundle is `bin/bundle --audience chief-of-staff`. There is no hand-maintained spine and no hand-run generation procedure. `bin/bundle-methodology` and its tests are retired, not repaired, and its deferral to a tooling tranche is withdrawn; the removal is a package under the bundle-system PRD. Carried forward unchanged from DEC-000190: the filename `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md`; the `Source: @ <repo HEAD>` line; the per-file blob short-SHA; the `<!-- FILE n/N: path @ sha -->` separators; upload per project, deleting the prior bundle. Not carried forward: the `~/code/` destination (DEC-000200 governs — bundles land in `~/Downloads`). Direction the bundle system builds toward, as a design constraint not yet a spec: any model may run as a decision or an execution session; bundles are generated on demand from Dave's Mac; delivery is incremental in files, with a row-granular end state as the mental model that nothing built now may foreclose.
Context: Owner decision (Dave), 2026-08-25, recorded in the bundle-system PRD draft (`~/Downloads/bundle-system-prd-draft-20260825T023000.md`, status draft, not yet committed). Two file-set rules disagreed on the default branch at `2f5323d`: DEC-000190's hand procedure yields a 12-file Chief of Staff bundle; `bin/bundle --audience chief-of-staff` yields 35 (told: reported by an execution session from a sandbox clone at `2f5323d`, not observed in a decision session). The audience-driven rule is chosen because it is the one the corpus's own `audience:` frontmatter already encodes and the one a new file joins by tagging rather than by editing a list. The 12-vs-35 gap is a corpus-tagging question, not a rule question: the 35 includes the `all-roles` floor of 20 files, which carries `specs/bin-land-trd.md`, `specs/bin-land.md`, and `specs/directive-tooling.md` (inferred: a tagging mistake). Fixing tags changes the bundle without changing this rule. `bin/bundle-methodology` is retired because it is stale at three points — it encodes the DEC-000140 spine, names `davepierceops/ai`, and omits `docs/global-context/` — and its two failing tests (the AC-BN-10 pair) test that stale spine; repairing it would reproduce a hand list the audience rule makes unnecessary. This entry rests on a draft PRD; the PRD's agreement may refine the rule's mechanics (ordering, floor contents) but its choice of the audience-driven rule over a hand list is decided here.
Supersedes: DEC-000190

## DEC-000220 — Writing methodology lives in fiducial; davepierceops/writing migrates in and retires
Date: 2026-08-29
Decision: All LLM methodology, prose writing included, lives in this repository; there is no separate writing-methodology repository. `davepierceops/writing` migrates into fiducial completely and is retired when the migration is confirmed complete; nothing is deleted until then. Migrated at PR #230 (`53f7f40`): the roles, the criteria, `voice-inbox.md`, and `retros/retro-20260812-201500.md`. Retired without migration: the Editor (orchestrator), Section Writer, Instruction Reviewer, and machinery-criteria documents, and `bin/session-tar`; the one-section-per-session workflow is retired as an experiment Dave did not want to keep.
Context: Owner decision (Dave), 2026-08-28. The bundle compiler selects by `audience:`, so a writing bundle costs no new machinery; a second repository would duplicate Core, the review machinery, and `bin/`. Writing rules are expected to grow into a large body with little overlap; that is a tagging cost the audience mechanism exists to carry, not a structural one. The writing repository's methodology content was audited from a snapshot at `387bde6` before this decision.

## DEC-000230 — Writing roles: Writer, Copy Editor, Critic; passes split by workload; one-word activation on an uploaded document
Date: 2026-08-29
Decision: Three writing roles. The Writer drafts whatever the author asks for, including outlines per `skills/outline.md`; it computes no piece state. The Copy Editor (`copy`) runs the checklist passes — proofread and copyedit as tracked changes, and claims-tier audit, discoverability and cold reader, justification ledger, and many-languages read as anchored comments — at solid tier, with the Google developer documentation style guide as base authority where the Voice document is silent. The Critic runs the judgment passes — Skeptic, AI-smell, voice — as anchored comments only, at frontier tier, advisory and never a gate. Each reviewing role runs every pass it knows by default and a subset on request; a `.docx` uploaded to a fresh session plus the role's word is the whole instruction. The two reviewing roles never share a session with each other or with the Writer. Output is the author's own `.docx`, returned with tracked changes and comments that Google Docs imports as suggestions and comments. Every rule is written vendor-neutral and repository-neutral: it states the outcome and the verification, never a tool, and assumes the author has a document and a chat and nothing else.
Context: Owner decisions (Dave), 2026-08-28/29, worked in the artifact pane. The tracked-changes and comments round trip through Google Docs was proven end to end on 2026-08-28 before the roles were written. The split by workload rather than by tier keeps the roles stable if tiers shift. The writing repository's Reviewer and Skeptic roles were absorbed into this catalogue; the coverage map from every criterion to the pass that checks it was recorded in the workstream's working document and every criterion is checked by a named pass, is the Writer's by design, or is a stance with nothing to check.

## DEC-000240 — prose-criteria.md splits into Public Prose Criteria and Voice; a Voice template ships with labeled examples
Date: 2026-08-29
Decision: `prose-criteria.md` is retired to `docs/history/` as superseded and replaced by two documents. `public-prose-criteria.md` holds what is true of any author's prose under this method. `voice.md` holds the author: purpose and audience, register, profanity, vocabulary, mechanics (the house-style sheet the Copy Editor applies over its base authority), repo citation, venue, disclosure wording. Roles bind to both by name, never to a person; the voice pass is reads-as-the-Voice-document. `voice-template.md` is a human-facing template a new author fills in, carrying Dave's Voice sections as labeled examples; the template states that examples are a snapshot, may lag the live Voice document, and are never a review finding — criterion 12 of the review rubric applies to rules, not examples. Voice-inbox lines default to Voice on triage; generic ones route to the Criteria. The TL;DR summary-label convention is retired; a summary section's label is per piece.
Context: Owner decisions (Dave), 2026-08-29. The split is what lets a second author use the method by replacing one file. The examples are embedded rather than pointed at so that a new author writes their own Voice rather than adopting Dave's. `policies/document-metadata-policy.md`'s in-scope set was amended in the same PR to name the three new docroot files; that policy is a gate document and its full cycle is owed.

## DEC-000250 — Piece artifacts live with the piece; the voice inbox lives in fiducial; the roles assume no repository
Date: 2026-08-29
Decision: The record of a piece — outline, findings, drafts — travels in or beside the author's document, in the author's own storage, never in fiducial. "The repository never holds prose" stands with no exception. `voice-inbox.md` lives in fiducial because it feeds methodology; the Writer harvests into it at session close and states in one line when there is nothing to harvest, and triage is a doc-only cycle on `voice.md` or `public-prose-criteria.md` on Dave's cadence. Every writing role is written so a writer with a document and a chat and no repository can run it. A role that names a document absent from its context asks the author for it before acting on anything it governs and never proceeds from memory of it; this is written into the three writing roles and is a candidate Core line for a later cycle.
Context: Owner decisions (Dave), 2026-08-29. The constraint came from distribution: writers who are not fiducial users cannot satisfy a rule that reads a repository path. Solving for them solves the artifact question for Dave the same way.

## DEC-000260 — Writing bundles are distributed through GitHub Releases
Date: 2026-08-29
Decision: Bundles for writers who are not repository users are distributed through GitHub Releases: `bin/bundle` generates one bundle per audience, a release attaches them pinned to the repository SHA they were generated from, and a consumer downloads one file from one URL. No generated bundle is committed to the tree. Every writing bundle ships the Public Prose Criteria and the Voice document; the Outline skill is ask-on-demand; how the Voice template reaches a bundle is the bundle-system PRD's decision. New audience values `writer`, `copy-editor`, and `critic` are in use.
Context: Owner decision (Dave), 2026-08-28/29. Handed to the bundle-system PRD workstream as a requirement on 2026-08-28 and recorded in `OPEN-ITEMS.md` under the PRD entry (`docs/cycles/open-items-bundle-release-req-20260828T1900.md`). Adds a delivery surface downstream of `bin/bundle`; changes nothing in DEC-000210.

## DEC-000270 — bin/directive's cycle mode bears DEC-000180's tooling consequence; bin/cycle-open becomes a forwarder
Date: 2026-08-30
Decision: The tooling consequence DEC-000180 attached to `bin/cycle-open` — the cycle skeleton emits Route and Model and no Track — is borne by `bin/directive`'s cycle mode. Both of `bin/directive`'s modes emit route and model from the committed `Route and model` section of `skills/directive-invariants.md` into a committed region of the skeleton, and nothing checks either value (`specs/directive-tooling-trd.md` §3.3, Q5 ruled (c)); no region of either mode emits a `Track:` line, and the invariants document is the only place a region's text lives. `bin/cycle-open` survives as a forwarding executable, passing argv to the same entry point and emitting no skeleton of its own (TRD §3.9 step 4); its acceptance suite runs unchanged against both names, which is the migration's evidence (AC-DT-15). `OPEN-ITEMS.md`'s guard against resurrecting the field is re-anchored on the cycle mode. Everything else DEC-000180 decided is carried forward unchanged and restated here so it stays live under whole-entry supersession: `track` is removed from the methodology entirely; a dispatch states three requirements every time — route, model, and the execution block; a reviewer-gated cycle directive states them like any other dispatch, with route *fresh* and model *frontier tier* as class defaults, stated per directive and overridable (the tier wording is Core's and the Decision Layer's; DEC-000180 named the model, and the default is unchanged); an executor that cannot push stops and surfaces it, and never reports a same-machine SHA as if pushed; `LEXICON.md` carries a tombstone for track; the sync block precedes every execution block.
Context: `specs/directive-tooling.md` AC-DT-16 (agreed at `d3ab472`, cycle 23) and TRD §3.9 step 5 bind the decision session, not the implementer, to land this entry and the `OPEN-ITEMS.md` rewrite before the cycle-mode migration lands. The landing is PR #244 (`docs/cycles/directive-tooling-impl-3-20260829T2300Z.md`, commit `3d1f921`), which put cycle mode in `bin/directive` with `bin/cycle-open` untouched; the forwarder is the next package. Owner decision (Dave), 2026-08-30, in the decision session that merged the tooling.
Supersedes: DEC-000180

## DEC-000280 — Writing bundles: the three role file sets are ruled
Date: 2026-08-31
Decision: The Writer, Copy Editor, and Critic bundles are exactly the sets AC-BS-4 of `specs/bundle-system.md` states: writer — core, decision-layer, the role, public-prose-criteria, voice, the outline skill, in that order; copy-editor and critic — the same minus the outline skill, with their own role files. No writing bundle carries another writing role or any software-delivery file. The 22-file `--audience writer` output is retired by that criterion when the selection mechanism lands.
Context: Owner decision (Dave), 2026-08-30, writing-workstream decision session; recorded in the PRD at its landing (PR #262) and logged here at the 2026-08-31 catch-up. The log entry was owed from the 08-30 session, which ruled the sets over the hand-built bundles at 40a8914.

## DEC-000290 — Delivery naming: sort-to-top is dropped; timestamps are UTC with a required Z
Date: 2026-08-31
Decision: Supersedes DEC-000200's naming clause only; the single delivery location `~/Downloads` stands, as does everything else in that entry. Files an agent hands Dave take the standing filename convention — `<descriptor>-<timestamp>` — with no sort-to-top prefix. Repo-wide, a generated timestamp is ISO 8601 basic format, UTC, with the `Z` designator required and date and time components both present: `<YYYYMMDD>T<HHMMSS>Z`. Core rule 14's example and the directive-authoring Naming example gain the `Z` at their documents' next cycles; existing filenames are not renamed.
Context: Owner decision (Dave), 2026-08-31, topic-walk session, on seeing the `0-` prefixes the sort-to-top clause produced. UTC over local because that's what professionals do. Closes the timezone gap `reviews/directive-authoring-cycle-3.md` F-2 and `reviews/directive-authoring-cycle-4.md` O-3 recorded.
Supersedes: DEC-000200 (naming clause only)

## DEC-000300 — Trivial-additive fast lane: refused, with a hit-again revisit trigger
Date: 2026-08-31
Decision: No third sanctioned route to `agreed` is created for owner-approved, additive, tool-verifiable-green changes. The next concrete case that fits no existing route is itself the trigger for a revisit: it reopens the OPEN-ITEMS entry with itself as evidence rather than being absorbed or worked around.
Context: Owner decision (Dave), 2026-08-31, topic-walk session, T25. The two motivating instances (2026-08-24) predate the cycle-20 revision of the document-metadata policy; a route defined from stale evidence is how gate complexity accretes.

The six decisions owed from the 15-hour session are not written here: their content is not recoverable from this session and must be reconstructed from that session's records before entries can be drafted. The OPEN-ITEMS entry for them stands.

## DEC-000310 — A retro runs when Dave asks, not by default
Date: 2026-09-01
Decision: A retrospective runs only when Dave asks for one. There is no
standing end-of-session obligation, no skip condition (nothing is owed
by default), and no baton-before-retro ordering rule.
Context: Owner decision (Dave), 2026-09-01, Decision Layer human
review; Decision Layer rule 12 rewritten accordingly, agreed at
cycle 15 (reviews/decision-layer-cycle-15.md; reviewed document SHA
999dc9a1cfa8aa695e4a324f4cbd4c5320f200ec).
skills/conversation-retro.md still encodes the prior obligation; its
conforming revision is queued as a full cycle.

## DEC-000320 — Bundle filename and header: ruled form; DEC-000210's carried form retired
Date: 2026-09-01
Decision: A generated bundle is named
fiducial-bundle-<audience>-<timestamp>, timestamp per DEC-000290,
delivered per DEC-000200. The header keeps the tool's present fields —
repository, HEAD SHA, generation time, numbered member list with
per-file blob SHAs, per-member markers. Hand-built and generated
bundles are interchangeable under this form. DEC-000210's
carried-forward filename and Source-line form is retired; the losing
form's removal lands in the bundle-system PRD's header package.
Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
review, resolving the PRD's OQ-5. Recorded in specs/bundle-system.md
at the review's landing (pull request #275).
Supersedes: DEC-000210 (carried-forward filename and header clause only)

## DEC-000330 — Releases: every audience, whole, at one HEAD; event-driven; go is Dave's
Date: 2026-09-01
Decision: A release re-produces every audience's bundle, regenerated
whole at the release's SHA — untouched audiences included, so every
asset states the same SHA; release notes name the audiences whose
member set or content changed. Cadence is event-driven, no calendar:
when a default-branch commit changes any bundle member, the decision
session tells Dave a release is owed, and it is cut on his explicit
go. The go is Dave's; the decision session owns mechanics and
verification (generate, cut, attach, notes, read-back confirming every
asset's SHA); a release found wrong returns to Dave as a triage item,
never a silent fix.
Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
review, resolving the PRD's OQ-6 whole.

## DEC-000340 — skills/outline.md audience: writer alone
Date: 2026-09-01
Decision: skills/outline.md is audience [writer]; the human value comes
off in the bundle-system tagging package. A human does not need the
outline skill.
Context: Owner decision (Dave), 2026-09-01, bundle-system PRD human
review, resolving the PRD's OQ-10.

## DEC-000350 — Audience value critic is the writing Critic's alone; the SRE engagement role becomes sre-critic
Date: 2026-09-02
Decision: The SRE engagement's critic role document is renamed
sre-critic (basename, and therefore audience value), and the
engagement files tagged critic are retagged sre-critic; the rename
lands in the bundle-system tagging package. Role-document basenames
are unique across roles/ and engagements/; a future collision is a
detectable defect.
Context: Owner decision (Dave), 2026-09-02, disposing
reviews/bundle-system-cycle-1.md finding B-1: the value critic named
two role documents, emitting a 28-file critic bundle against a
five-file target. The uniqueness rule is stated in
specs/bundle-system.md, agreed at cycle 2.

## DEC-000360 — Convergence is the standard change flow; `converging` is a status
Date: 2026-09-02
Decision: Spec and tests converge before agreement, as the standard change
flow, not an exception. A fourth agreed-route status, `converging`, sits
between `in-review` and `agreed`: entered after the first reviewer gate on
Dave's say by a frontmatter-only transition; while converging the spec is
edited freely and the Test Designer writes tests against it, and content
edits change neither status nor `last-reviewed`; exited by one exit gate
over the diff from the entry transition commit to the reviewed SHA plus the
tests, Dave's read of that diff, and one ruling that flips the spec agreed
and records the tests' acceptance in the exit artifact. Building against a
document is three-valued: draft/in-review nothing; converging tests only;
agreed implementation. Enforcement of the value lands as a bin/ package
before the first document enters it.
Context: Owner decision (Dave), 2026-09-02, triaging
reviews/spec-review-cycle-cycle-11.md N-1, which found the cycle-11
Convergence section contradicting the metadata policy, the operating model,
and the Test Designer role. Dave refused an exception-shaped fix: the rules
say convergence is how it is done, and the three texts yield. Landed by
docs/cycles/converging-model-editor-directive.md as one branch-scoped cycle.

## DEC-000370 — The interface contract has a source per stage
Date: 2026-09-02
Decision: The spec's convergence suite takes its interface contract from the TRD's stated interface list — the list the Spec Reviewer's TRD check confirms complete. A unit's tests, at the per-change stage, take theirs from the architecture summary. The discipline context set names both sources, each with its stage.
Context: reviews/converging-model-cycle-2.md N-6: under DEC-000360 the spec's suite is written at stage 3, before any architecture summary exists at stage 6, and context-sets/spec-and-change-discipline.md named only the architecture summary. Ruled 2026-09-02; landed by docs/cycles/chief-of-staff-cycle-7-editor-directive.md SD-1, agreed at reviews/chief-of-staff-cycle-7.md.

## DEC-000380 — Rebuild: gates move from documents to content; the document-lifecycle machinery retires
Date: 2026-09-04
Decision: Rules become rows in rules/ (one rule, one record); a row in rules/ is in force and nothing else certifies it. The one gate on a rule is intake: a Context Quality Reviewer session shapes the proposal into one instruction, checks it against the store, sets and normalizes its keys, and lands it in one commit. Retired with this ruling: the status and last-reviewed fields, the agreement flip, review cycles per document, the expedited and doc-only paths, the in-scope set, the pre-commit hook, and the tools check-frontmatter, flip-agreed, install-hooks, migrate-frontmatter, and reviews/expedited-log.md. Documents that describe a sequence stay prose under process/, gated by one frontier read against the rows they cite plus Dave's sign-off, recorded as a decision-log entry naming the SHA. Content carries — rules, this log, retros; machinery does not.
Context: 62 governed files, each a bag of rules carrying a lifecycle that certified the container while agents act only on the content; one policy took 22 cycles to agree; Pass 3 at main 4a118f5 counted 1600 rows, 1131 distinct rules, 206 clusters of restatement across files. The machinery was an artifact of how the project grew from June, not a requirement of the methodology. Dave rejected "one file per row with the old gates" as the same complexity under a new name. Ruled in the session that produced rule-store-prd-20260904T233500Z.md, the PRD superseding specs/bundle-system.md.
Supersedes: DEC-000010, DEC-000020, DEC-000030, DEC-000040, DEC-000050, DEC-000060

## DEC-000390 — The name and the history stay: fiducial, no rewrite, old corpus moved to docs/history
Date: 2026-09-04
Decision: The methodology and the repository keep the name fiducial. History is preserved: no force-push, no rewrite of any ref; the retired corpus moves whole to docs/history/corpus-<sha>/, never deleted, so every row's source resolves at the named SHA. Git mechanics of the move are the Chief of Staff's to carry out; Dave does not rule on them.
Context: The rebuild (DEC-000380) replaces the governed files with rows. Renaming or restarting the repository would cost the history that the rows' source pointers, the decision log, and the retros rest on, for no gain the ruling needs.

## DEC-000400 — The row: id, instruction, zero-to-N free key-value pairs; selection is a query over keys
Date: 2026-09-04
Decision: A row is an id, an instruction body, and zero or more key-value pairs with no fixed schema. Selection is a query over keys (bin/bundle --where role=writer corpus=writing): a row matches when every named key holds the value. No reserved values; no special tags key; the keys in use are computed on demand (bin/bundle --keys) and never maintained as a list; intake normalizes every incoming key against the keys already in use. Conventions: every value is a list of words (a bare word is a list of one); exactly two keys are typed — id is text, order is a number. topic carries the grouping the file used to do, seeded from the source path and corrected from the clustering output; no topic list is designed in advance. A row is one obligation and stands alone; adjacency that still matters is carried by order within a topic. An optional ## Human section carries the rationale and is never rendered to an agent.
Context: The bundle-system TRD's audience-and-corpus model resolved membership through a file's frontmatter and a fixed vocabulary; the rebuild needs membership to be the row's own keys so that a new role, corpus, or topic is a new value, not a tool edit. "Tag" framing was retired with this ruling: a tag is just a key with one value. Stated in full in fiducial-rebuild-shape-20260905T000500Z.md § "The row".

## DEC-000410 — Storage boundary: the filesystem is the initial persistence mechanism, not an architectural dependency
Date: 2026-09-04
Decision: Treat the filesystem representation as the initial persistence mechanism, not as an architectural dependency of the rule-processing logic. Define a narrow abstraction for obtaining rule rows. Code that selects, validates, orders, bundles, retires, or otherwise reasons about rules operates on row objects and does not know whether those rows came from individual files, a database, or another backing store. The initial implementation may read one rule per file from rules/, but filesystem traversal, filename conventions, frontmatter parsing, and file I/O stay inside the storage layer. The boundary makes it possible to replace the filesystem-backed implementation later with a database-backed implementation without changing the rule-processing logic. Do not introduce a database now merely to satisfy this abstraction. The goal is substitution, not premature infrastructure.
Context: Files are an unusual store for something that is plainly rows — a fine choice for now, but one the project should be free to change, and changing it should touch one layer of the code and nothing else. Dave's wording, verbatim from fiducial-rebuild-shape-20260905T000500Z.md § "Storage boundary"; the PRD carries it as G7 and AC-RS-4.

## DEC-000420 — Definitions are rows selected by term
Date: 2026-09-05
Decision: A definition is a row carrying a `term` key and no role, session, or corpus key. The bundle tool includes a definition when a selected row's body uses one of its terms, and scans the pulled definitions' bodies the same way, transitively.
Context: The PRD's G12; a definition keyed to roles either duplicates across bundles or goes missing from one.

## DEC-000430 — Engagement material waits for the next engagement
Date: 2026-09-05
Decision: No engagement material is written as rows now. `engagements/` stays as it is until the next engagement needs it, and is written then through intake.
Context: Resolves the rule-store PRD's OQ-2; the 153 register rows from the engagement files were left untouched by the store migration.

## DEC-000440 — A Test Designer edits tests only; a spec writer edits specs only
Date: 2026-09-05
Decision: A Test Designer edits tests and nothing else; a spec change it needs is a finding to the decision session. A spec writer edits specs and nothing else; a test change it needs is a finding to the decision session.
Context: Register cluster C097; the positive wording Dave chose over the two prohibitions the source files carried.

## DEC-000450 — Two register rows merge only on the same obligation and the same keys
Date: 2026-09-05
Decision: Two register rows become one store row only when they state the same obligation and would carry the same keys. Any difference in keys splits them, however close the wording.
Context: The rule the store migration and every fix pass merged under; a merged row states the rule at its shortest, not the sum of its sources.

## DEC-000460 — process/change-flow.md agreed at 81310de
Date: 2026-09-05
Decision: process/change-flow.md is agreed at 81310de105b0f0b4133117fa4c209baea9d84b09, the first document under the process gate DEC-000380 names. It supersedes DEC-000360's mechanism — the converging status and its transitions — and not its substance; DEC-000370 stands. Every pull request gets an agentic code review with no trivial-change exemption; quality and skepticism are always two passes, in one session or two by class or by a size call; the Reviewer rows stay in force until an adopted published code-review standard replaces them in the same commit.
Context: Five frontier reads (reviews/change-flow-read-*.md), then Dave's agreement on 2026-09-05.
Supersedes: DEC-000360

## DEC-000470 — `all` is not a role value
Date: 2026-09-05
Decision: No row carries `role: [all]`. Every row's role list is decided for that row; the roles in use are the twelve role-document slugs at fd54448.
Context: A blanket role list defeats selection by query, which is the store's whole mechanism.

## DEC-000480 — Corpus values are software and writing
Date: 2026-09-05
Decision: The `corpus` key takes the values `software` and `writing`. `methodology` is not a value until a row needs it.
Context: The register's methodology rows all keyed to a role and a session already; a third corpus value had nothing to select.

## DEC-000490 — Templates and schemas are process documents
Date: 2026-09-05
Decision: A template or a schema is a `process/` document selected by key, not a set of rows. Rows are written only where an agent performs an act: the TRD, PRD, voice, outline, review-artifact, retro, decision-log entry form, and project setup are process documents.
Context: A document's form is prose; rows that restated a template's sections were the restatement problem in another shape.

## DEC-000500 — One decision per decision-log entry
Date: 2026-09-05
Decision: A decision-log entry records exactly one decision. Two decisions made together are two entries.
Context: Dave's ruling of 2026-09-06 when the rebuild's entries were listed for the flush; an entry carrying several rulings cannot be superseded one at a time.

## DEC-000510 — The intake checklist is the store's construction rule
Date: 2026-09-05
Decision: R0264, the intake checklist, is the rule every row is judged by on entry and the rule the store was built under. Its criteria are rows in topic intake, not decisions; a change to a criterion goes through intake like any row.
Context: The criteria were ruled one at a time across the fix-pass reads of 2026-09-05 and 2026-09-06 and are recorded here once, as one rule.

## DEC-000520 — process/change-flow.md agreed after the sweep
Date: 2026-09-07
Decision: process/change-flow.md is agreed at b814e4561c25db77d248c76c2b0f992e01965f2c, under the process gate; one frontier read (reviews/change-flow-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 252 to 81 lines.

## DEC-000530 — process/review-artifact.md agreed after the sweep
Date: 2026-09-07
Decision: process/review-artifact.md is agreed at 1be6fb02371d947aa21eca772d67212e0783e11a, under the process gate; one frontier read (reviews/review-artifact-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 139 to 82 lines.

## DEC-000540 — process/retro.md agreed after the sweep
Date: 2026-09-07
Decision: process/retro.md is agreed at 757a6c4cc4e256ca85f178e9d9cc1e448bb3eae0, under the process gate; one frontier read (reviews/retro-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 151 to 67 lines; keyed to chief-of-staff and writer; the human has never asked a copy editor or critic for one.

## DEC-000550 — process/trd-template.md agreed after the sweep
Date: 2026-09-07
Decision: process/trd-template.md is agreed at 40784df9d818f82c5a571607a10818a5b375e01f, under the process gate; one frontier read (reviews/trd-template-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 155 to 60 lines; agreed for this version; the human intends to revisit it.

## DEC-000560 — process/prd-template.md agreed after the sweep
Date: 2026-09-07
Decision: process/prd-template.md is agreed at a78145bd16d9a761dd6b51b070bbc85890b5836b, under the process gate; one frontier read (reviews/prd-template-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 119 to 58 lines.

## DEC-000570 — process/decomposition.md agreed after the sweep
Date: 2026-09-07
Decision: process/decomposition.md is agreed at fa0022f05a165f32efe16bb62f1565840e50a01a, under the process gate; one frontier read (reviews/decomposition-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 85 to 39 lines.

## DEC-000580 — process/outline.md agreed after the sweep
Date: 2026-09-07
Decision: process/outline.md is agreed at 4283d79bad9fe213cdabd65a19172b3d4ec0502e, under the process gate; one frontier read (reviews/outline-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 78 to 41 lines.

## DEC-000590 — process/decision-log.md agreed after the sweep
Date: 2026-09-07
Decision: process/decision-log.md is agreed at 1f6d7e3ba361c360bc5879e586fe569d47b202ae, under the process gate; one frontier read (reviews/decision-log-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 77 to 29 lines.

## DEC-000600 — process/project-setup.md agreed after the sweep
Date: 2026-09-07
Decision: process/project-setup.md is agreed at 85f6e437b5ce8796523d4266eeacb5fb1bada2e9, under the process gate; one frontier read (reviews/project-setup-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 56 to 21 lines; no bundle selects it; the human works it once per repository.

## DEC-000610 — process/spec-test-suite.md agreed after the sweep
Date: 2026-09-07
Decision: process/spec-test-suite.md is agreed at 74f7eef61128f5443642cc8bfb0cd7fe270f96ce, under the process gate; one frontier read (reviews/spec-test-suite-read-20260907T060000Z.md), blocking findings applied, then the human's sign-off.
Context: the process sweep of 2026-09-07 reduced it from 50 to 25 lines.

## DEC-000620 — The two-tranche cap is dropped
Date: 2026-09-07
Decision: No limit is placed on how many tranches run at once; the rule that concurrent deltas cover disjoint spec territory stands unchanged.
Context: the human's ruling of 2026-09-07 on the read of process/change-flow.md and process/decomposition.md: R0013 already prevents the collision the cap guarded, and no third tranche has ever been opened.
Supersedes: DEC-000170

## DEC-000630 — A bundle's header is one comment line
Date: 2026-09-06
Decision: A generated bundle opens with exactly one line, an HTML comment: `<!-- fiducial <owner/repo> @ <full HEAD SHA> <generation timestamp> -->`, the timestamp in the `<YYYYMMDD>T<HHMMSS>Z` form. No member list, no blob list, no title line.
Context: the human's ruling of 2026-09-06 on the first generated bundles: the 240-line member list served no session that loaded a bundle, and the SHA is the one fact a session judges the bundle's age by.
Supersedes: DEC-000320 (header clause only; the filename clause stands)

## DEC-000640 — A bundle is three bands of body text
Date: 2026-09-07
Decision: A bundle renders its rows as body text, one row after another with a blank line between, under no per-row heading; then every selected process document, body only; then the definitions the rows use, under one `## Definitions` heading. Rows sort by their topic's position in the topic sequence, then by topic name, then `order`, then id — so topics sharing a position render as contiguous alphabetical runs; process documents sort by their `topic` value's position in the process sequence, the path stem standing in where the key is absent. A topic or stem the sequence does not name sorts after the last named one, alphabetically. Definitions sort by `order`, then id.
Context: the human's rulings of 2026-09-06 (no `## R` headings) and 2026-09-07 (rows first, then the process documents as their own band, then the definitions). `order` keeps its meaning as position within a topic.

## DEC-000650 — process/named-queries.md is where a bundle and the sequence are defined
Date: 2026-09-07
Decision: The list of distributed bundles — one per role, the query `role=<slug>` — and the two sequences DEC-000640 orders by live in `process/named-queries.md`, in fenced blocks the tool reads. A process document carries `topic: [<its stem>]`. Nothing else names a bundle or an ordering.
Context: resolves the rule-store PRD's OQ-1. A durable rule lives in the store and the tool derives from it (R0763); a new role or a reordered topic is an edit to the document, never to the tool.

## DEC-000660 — Release assets carry no timestamp; a release is tagged by date
Date: 2026-09-06
Decision: A release attaches README.md and one `fiducial-bundle-<slug>.md` per entry in the list, each generated at the release's SHA, and is tagged `v<YYYY>.<MM>.<DD>`. The file bin/bundle writes for a session keeps its timestamped name. bin/release generates the assets from a synced clone, refuses whole on any failure, and prints the `gh release create` command; the human runs it.
Context: the human's ruling of 2026-09-06 on distribution: a stable asset name gives `releases/latest/download/` a stable URL; the date is the version, since a methodology's semantic version cannot be computed.

## DEC-000670 — The rule-store PRD is agreed
Date: 2026-09-07
Decision: specs/rule-store.md is agreed at db94962d2c9c596f2ee1dc07fbf58d8bd48ea92b as the standing product specification for the rule store, the bundle tool and the release, superseding specs/bundle-system.md; process/named-queries.md is agreed at 0eb0085f9f564e5bac1e32d3b31090073b0ecb74 as the one place a bundle and the render order are defined.
Context: the human read the PRD redrafted against main at 8d21cd3 to state what was built, and called it version one.

## DEC-000680 — Rule-store PRD revised: AC-RS-9 exempts the invariants document
Date: 2026-09-08
Decision: specs/rule-store.md is agreed at 70971887e92c80790f962b6cb68aae2aba17cc1d. AC-RS-9 now reads the old corpus as the 62 in-scope files less skills/directive-invariants.md, a tool input that moves to process/directive-invariants.md rather than to docs/history/.
Context: bin/directive and bin/check-directive read their regions from the invariants document, and rows R1302 and R1304 name its path; moving it to history with the corpus would leave the generator, the lint and two rows in force pointing at nothing. Supersedes nothing: DEC-000670 agreed the PRD at db94962 and stands as history; this entry names the current agreed SHA.

## DEC-000690 — Rule-store PRD revised: AC-RS-9 moves the agent-facing corpus only
Date: 2026-09-09
Decision: specs/rule-store.md is agreed at 8ee33c8daeae0d5511c44758969a1b59f3a272a3. AC-RS-9 names no count: the old corpus moved to docs/history/ is the agent-facing in-scope files at the baseline SHA less skills/directive-invariants.md; the [human] files OQ-3 names stay as files.
Context: the 62 in-scope files at 4a118f5 include 8 [human] documents — specs, vendor notes, the voice template, README.md — that OQ-3 keeps as files and G10 reads from the root at release; moving them with the corpus contradicted both. DEC-000680 stands as history; this entry names the current agreed SHA.

## DEC-000700 — A non-blocking finding never reopens a delta
Date: 2026-09-09
Decision: A non-blocking finding never reopens a delta or delays its landing; it goes to the loose-end tracker and is fixed in a later package of its own. Only a blocking finding reopens a delta.
Context: the AC-RS-8/9 and prose-criteria-rows reads of 2026-09-09, whose non-blocking findings this package files.

## DEC-000710 — A row citation must co-render with what it cites
Date: 2026-09-09
Decision: A row may cite another row by ID in square brackets only where every value the citing row carries on role, session and corpus the cited row carries too, so the two always co-render; a citation that cannot co-render is a defect. Landed as R1605 in topic intake.
Context: intake finding F-3 on prose-criteria-rows; chosen over forbidding citations because a paraphrase drifts silently while a dangling pointer is lintable — F-7 on the loose-end tracker records that R1605's test passes a keyless citing row vacuously.

## DEC-000720 — prose-criteria-rows delta agreed
Date: 2026-09-09
Decision: The prose-criteria-rows delta is agreed, at 09cb08cd9bf3f9db0a6fef825c5d4a1e1af6e703, the SHA its merge to main (pull request #343) landed at: R1604 replaces R1161, R0953 and R1001; R1013 cites four structure rows by ID; R0038 drops its citation; R1605 is added.
Context: the independent read prose-criteria-rows-read-3 returned ready-with-findings with no blocking finding.

## DEC-000730 — process-criteria-refs delta signed off
Date: 2026-09-10
Decision: The process delta process-criteria-refs — process/outline.md and process/voice.md stop naming the Public Prose Criteria as a document — is signed off at b3a8f008884bc47ca9447f784afe29be16ec367f.
Context: one frontier read, reviews/process-criteria-refs-read-20260910T193000Z.md @ 79c9263, returned ready-with-findings with no blocking finding; its findings go to the loose-end tracker under DEC-000700.

## DEC-000740 — R1606: dictate intent and agreed prose, never tree facts
Date: 2026-09-11
Decision: R1606 (directive-invariants) is agreed: Dictate intent, acceptance criteria, and prose the human agreed; dictate no tree fact — an id, a key value, a position, which rows carry a term, a tool's existence, a count, a SHA. The executor derives each fact it needs from the tree and reports the derivation with its evidence.
Context: 09-09 E4–E10 and 09-10 E5–E10.

## DEC-000750 — R1607: a tree-resolvable precondition is resolved, not stopped on
Date: 2026-09-11
Decision: R1607 (directive-invariants) is agreed: A precondition the tree resolves with no judgment call and no change of intent is resolved and reported, not stopped on. Stop on what the tree does not resolve.
Context: 09-09 E4–E10 and 09-10 E5–E10.

## DEC-000760 — R1608: every new directive routes to a fresh session
Date: 2026-09-11
Decision: R1608 (directive-invariants) is agreed: Route every new directive to a fresh session. An amendment goes to the session whose stopped report it answers, supersedes named instructions in that directive, and is the only use of the existing-session route.
Context: the 09-09 self-review.

## DEC-000770 — R1609: a block is tested end-to-end, substitution bound
Date: 2026-09-11
Decision: R1609 (command-blocks) is agreed: Before handing over a block, run it end-to-end against a local stand-in for the remote, guard and re-run paths included; a block carrying a substituted value is run with the value bound, since the substitution is the untested part.
Context: 09-07 E10 and 09-08 E11.

## DEC-000780 — R1610: dictated text is verified by byte-for-byte diff
Date: 2026-09-11
Decision: R1610 (directive-invariants) is agreed: Verify dictated text by diffing the landed file against the directive's own fenced block, byte for byte; a heading, a count, or the executor's report is not the check.
Context: 09-04 #314 and 09-08 F1.

## DEC-000790 — R1611: read the spec spine whole before directing against it
Date: 2026-09-11
Decision: R1611 (chief-of-staff) is agreed: Before directing against a spec, read the PRD, the TRD, and the decision-log entries that agree them, whole. A question put to the human that the spec answers is a defect in the read, not a question.
Context: 09-09 E4/E5/E7.

## DEC-000800 — R1283 retires into R1608
Date: 2026-09-11
Decision: rules/R1283.md is deleted; R1608 carries the route obligation, and the amendment route is the only existing-session route.
Context: the 2026-09-09 read that became a self-review; the three citations of R1283 under docs/rule-register/ are derived records and stand as written.

## DEC-000810 — R1606 distinguishes a pinned ref from a dictated tree fact
Date: 2026-09-11
Decision: R1606 (directive-invariants) is amended to: Dictate intent, acceptance criteria, and prose the human agreed; dictate no tree fact for the executor to land — an id, a key value, a position, which rows carry a term, a tool's existence, a count. A ref pinned for the executor to verify is a claim, read from the tree and cited, not a dictated fact.
Context: NB-1 and NB-2 of reviews/tree-fact-rows-read-20260911T180000Z.md.

## DEC-000820 — R1607 carries the executor's derivation and the stop boundary
Date: 2026-09-11
Decision: R1607 (directive-invariants) is amended to: A precondition the tree resolves with no judgment call and no change of intent is resolved and reported, not stopped on; a fact derived from the tree — an id, a position, a key value — is reported with the evidence it was derived from. Stop on what the tree does not resolve.
Context: NB-2 and NB-4 of reviews/tree-fact-rows-read-20260911T180000Z.md.

## DEC-000830 — R1609 is the one pre-handover check for a block — R1220 and R1228 retire into it
Date: 2026-09-11
Decision: R1609 (command-blocks) is amended to: Before handing over a block: every command in it is valid and non-harmful, and re-running it compounds no damage; it has been run end-to-end against a local stand-in for the remote, guard and re-run paths included, with any substituted value bound; its expected output is stated in one line below it, and its blast radius above it where it is destructive. rules/R1220.md and rules/R1228.md are deleted; R1609 carries their obligation.
Context: NB-3 of reviews/tree-fact-rows-read-20260911T180000Z.md.

## DEC-000840 — R0188 retires into R1607
Date: 2026-09-11
Decision: rules/R0188.md is deleted; R1607 carries its obligation.
Context: NB-4 of reviews/tree-fact-rows-read-20260911T180000Z.md.

## DEC-000850 — R1610 covers text carried by pointer
Date: 2026-09-11
Decision: R1610 (directive-invariants) is amended to: Verify dictated text by diffing the landed file against the directive's own fenced block, byte for byte; a heading, a count, or the executor's report is not the check. Text carried by pointer is diffed against its source.
Context: NB-5 of reviews/tree-fact-rows-read-20260911T180000Z.md.

## DEC-000860 — A pull request handed for merging is its URL alone
Date: 2026-09-11
Decision: R1612 (decision-layer) is agreed: Hand a pull request to the human for merging as its URL, alone in a paste block with nothing else in it.
Context: the human's stated preference, 2026-09-11.

## DEC-000870 — Retired rows live under rules/retired/, per AC-RS-10
Date: 2026-09-11
Decision: R1283, R1220, R1228 and R0188 are restored under rules/retired/, each with a retired: line naming its successor; DEC-000800 and DEC-000840 stand as written, and "deleted" there reads as "retired" from this entry on.
Context: the decision session directed deletion twice against the agreed PRD (specs/rule-store.md, AC-RS-10), which moves a retired row and never deletes it; the executor of the tree-fact-rows-nb package flagged the conflict.

## DEC-000880 — The loose-end tracker is GitHub Issues
Date: 2026-09-16
Decision: The loose-end tracker for fiducial is the repository's GitHub Issues and Milestones on davepierceops/fiducial; an open item is an issue, and a pending gate keeps its human-gate label there. OPEN-ITEMS.md is retired: its open residue is filed as issues under #370 and the file moves to docs/history/ once every open entry has a destination.
Context: the human's ruling, 2026-09-16, confirming the direction recorded in docs/research/evaluation-work-plan-2026-09-14.md and #370; two trackers had claimed the same items since #355–#375 were filed.

## DEC-000890 — The 2026-09-14 evaluation and its work plan are agreed; #355–#375 are the derived work
Date: 2026-09-16
Decision: docs/research/repository-evaluation-2026-09-14.md and docs/research/evaluation-work-plan-2026-09-14.md are the record of the 2026-09-14 evaluation session, baseline 8ea66f527cf0114441b34976b09a8326fccbf3c2; issues #355 through #375 and their milestones are the work agreed from them. A plan item the work plan marks proposed or not yet agreed is issue text, not a decision, until an entry here says otherwise.
Context: the session ran outside the change flow and left no directive, review artifact or entry; the human handed the two files over on 2026-09-16 and they landed at 1a41ea75d37b10280d3601abb0e16c8f60e001a2.

## DEC-000900 — README agreed at 10471df
Date: 2026-09-16
Decision: README.md is agreed at 10471df5096fc5d5e236423a424b8eaddb998361, the version pull requests #376 and #377 landed; it links GitHub Issues and Milestones as the live roadmap and carries no duplicated task list.
Context: the rewrite closed #369 on 2026-09-15 with the human's own read as its gate; README.md is outside the four delta kinds process/change-flow.md gates, so no read was owed, and this entry is its record.

## DEC-000910 — Harness adapters are thin pointers to a pinned local bundle
Date: 2026-09-16
Decision: CLAUDE.md, AGENTS.md and any other harness entry file are kept as thin pointers that tell the agent where the substantive instructions are — a pinned local bundle — and carry no restated rules. This reverses the removals at 8e26700 and 23c1a57, which deleted the adapters rather than thinning them; the package that lands them is #360.
Context: docs/research/evaluation-work-plan-2026-09-14.md section D, agreed adapter design; it settles the executor-context question open since 2026-09-11, when the decision session found Claude Code executors had carried no repository standing context since 8e26700.

## DEC-000920 — Routine releases run on standing authorization; consequential ones wait for explicit approval
Date: 2026-09-16
Decision: A routine release has the human's standing authorization once the required checks and reviews pass and needs no fresh approval prompt; a consequential release waits for the human's explicit go. Passing checks does not make a consequential change routine, and a merge that exposes nothing is not the release event. The row edits that state this consistently — R0490 and the consequential-class definition among them — land under #364 as an intake delta; the classification itself is unchanged by this entry. DEC-000330's other rulings stand and are restated here under whole-entry supersession: a release re-produces every audience's bundle, regenerated whole at the release's SHA, untouched audiences included, so every asset states the same SHA; release notes name the audiences whose member set or content changed; cadence is event-driven, no calendar — when a default-branch commit changes any bundle member, the decision session tells the human a release is owed; the decision session owns mechanics and verification (generate, cut, attach, notes, read-back confirming every asset's SHA); a release found wrong returns to the human as a triage item, never a silent fix.
Context: docs/research/evaluation-work-plan-2026-09-14.md section E item 3, agreed; the evaluation found R0490 and the consequential-class definition read as contradicting each other.
Supersedes: DEC-000330

## DEC-000930 — Bundles label a rule's ID only where another bundle member cites it
Date: 2026-09-16
Decision: A rendered bundle carries a rule's ID only when a retained reference elsewhere in the same bundle cites it; unreferenced rules render unlabelled as today. Authors decide which citations are necessary instruction and which are provenance only, and the bundler labels the targets of the former and refuses to render when a retained target is absent. The specification and tooling change lands under #358 as a spec delta on the rule-store PRD.
Context: docs/research/evaluation-work-plan-2026-09-14.md section B, agreed; the evaluation found process text citing rule IDs the renderer omits and 15 cited rules absent from the chief-of-staff bundle.

## DEC-000940 — Ordinary bundle generation renders the local tree; only release generation checks its inputs against origin
Date: 2026-09-16
Decision: bin/bundle renders local files as they stand — uncommitted edits included, offline, on any branch — with input validation kept; the fetch and the HEAD-equals-origin/main refusal move to the release path, where cleanliness is checked over the files that generate the release assets and nothing else. The specification and tooling change lands under #366 as a spec delta on the bundle-system PRD.
Context: docs/research/evaluation-work-plan-2026-09-14.md section F2, agreed; the sync refusal blocked every pre-merge bundle check on a delta branch, recorded on the loose-end tracker on 2026-09-10.

## DEC-000950 — bin/land is agent-facing
Date: 2026-09-16
Decision: bin/land is agent-facing from this entry: a directive may instruct an executor to invoke it, and the executor lands the directive file and the session's work with it rather than by hand. The precondition set on 2026-08-23 — a governed usage document agreed first — is withdrawn; specs/bin-land.md's user journeys J1 and J2 are the tool's usage statement, and the directive that invokes it says what its report and exit status mean. The four untriaged finding classes against specs/bin-land-trd.md are filed on the tracker as deferred and do not hold the tool.
Context: the human's ruling of 2026-09-16 on learning the tool had been built, tested and unused since August; the sequencing decision it withdraws lives in docs/cycles/bin-land-spec-7-20260823T203500Z.md @ 8a77c2a and specs/bin-land.md §8 Q3, not in this log, so there is no entry to supersede. The first directive to invoke bin/land is the one that lands this entry.

## DEC-000960 — R0225 carries the ruling-question form
Date: 2026-09-16
Decision: R0225 (decision-layer) is amended to: Ask one question at a time, the one that matters most; name the item before the choice and shape it yes/no where it can be; after handing over a report or a block, restate the question still open. A ruling question defines the corpus term it turns on in one sentence, restates the situation from the ground floor where it arrives without its context, and names which option matches the human's prior rulings, offering the reversible one.
Context: items 10 and 11 of retros/retro-synthesis-20260910T225935Z.md, ruled 2026-09-16; item 11 folds into item 10.

## DEC-000970 — R0148 names per-clone state as boundary-sensitive
Date: 2026-09-16
Decision: R0148 (verification) is amended to add per-clone state — hooks, local config, credential helpers — to the boundary-sensitive list, and one sentence: a package that retires or changes a tool which installs per-clone state names the operator step that removes it and where that step is published.
Context: item 13 of retros/retro-synthesis-20260910T225935Z.md, ruled 2026-09-16; bin/install-hooks left a pre-commit hook in the human's clone after its retirement.

## DEC-000980 — R0829 carries the plain-phrase alternative for readers outside software
Date: 2026-09-16
Decision: R0829 (public-prose-criteria) is amended to: Define each governed or specialist term where it first appears, for a public reader; where the audience includes readers outside software, use the plain phrase for a software term or define it in the sentence that first uses it. R0983 stays as the copy-editor's check.
Context: item 14 of retros/retro-synthesis-20260910T225935Z.md, first ruled a new row on 2026-09-16, then ruled an amendment the same day because a new row would carry the obligation R0829 already states.

## DEC-000990 — An untracked file under retros/ lands with the next flush package
Date: 2026-09-16
Decision: A file under retros/ that is untracked in the clone lands with the next flush package; a row in topic chief-of-staff carries this, and R0880's invocation state check names every such file. R1244 stands: a retro never reads from or writes to a remote.
Context: a standing-preference candidate of retros/retro-synthesis-20260910T225935Z.md, confirmed as a row on 2026-09-16 after the 09-10 synthesis was found never landed.

## DEC-001000 — A non-blocking finding lands by default; the human may raise it to blocking at triage
Date: 2026-09-16
Decision: A non-blocking finding's disposition at triage is file-and-land by default: it goes to the loose-end tracker and the delta lands. The human may raise a finding to blocking at triage, before the pull request merges; one raise buys one read over the diff since the reviewed revision. Nothing else reopens a delta. A row in topic review-artifact-schema carries this for every reviewing role and the chief of staff.
Context: the human's ruling of 2026-09-16 on DEC-000700's "never": too constraining, and one reviewer must not be the sole gate — while a return to trivial findings reopening deltas is refused. DEC-000700's tracker routing survives in this entry.
Supersedes: DEC-000700

## DEC-001010 — R1609 regains R1220's expected-output constraint and its Human notes
Date: 2026-09-16
Decision: R1609 (command-blocks) is amended so the expected output stated below a block is what was observed in the environment the block will run in, or qualitative — what to look for, with no number; its Human section carries the Human notes of retired R1220 and R1228 verbatim.
Context: the three tracker findings of reviews/tree-fact-rows-nb-read-20260911T230000Z.md against R1609, ruled 2026-09-16; DEC-000830's merged body had dropped the constraint.

## DEC-001020 — DEC-000830 also reads "deleted" as "retired"
Date: 2026-09-16
Decision: R1283, R1220, R1228 and R0188 live under rules/retired/, each with a retired: line naming its successor; DEC-000800, DEC-000830 and DEC-000840 stand as written, and "deleted" in each reads as "retired" from this entry on.
Context: DEC-000870 named DEC-000800 and DEC-000840 but not DEC-000830, which also says "deleted" (a finding of reviews/tree-fact-rows-nb-read-20260911T230000Z.md); the whole entry is restated here under whole-entry supersession.
Supersedes: DEC-000870

## DEC-001030 — A directive states the count it lists or none
Date: 2026-09-16
Decision: Where a directive states how many items it lists, the count matches the list; otherwise it states no count. A row in topic directive-invariants carries this.
Context: carried from the 2026-09-04 session, where a directive's stated count and its list disagreed; ruled into this delta 2026-09-16.

## DEC-001040 — R1171 names the public-prose-criteria rows by topic
Date: 2026-09-16
Decision: R1171 (writer) is amended so the voice harvest names "the Voice document or the public-prose-criteria rows", replacing "the prose-criteria rows in this bundle".
Context: F1 of reviews/criteria-rows-read-20260917T033521Z.md, the class F6 of reviews/process-criteria-refs-read-20260910T193000Z.md named: a bundle-relative phrase reads wrong outside the bundle; ruled 2026-09-16.

## DEC-001050 — R0241 states where the loose-end tracker lives
Date: 2026-09-16
Decision: R0241 (decision-layer), the row defining the loose-end tracker, is amended to add: The loose-end tracker is the project's issue tracker — on GitHub, the repository's Issues and Milestones: an open item is an issue, and a pending gate carries its human-gate label there.
Context: the definition row DEC-000880 called for, ruled 2026-09-16; R0551 and R0560 already assume a tracker issue and its label.

## DEC-001060 — Project Status is a separate skill, not Chief of Staff startup
Date: 2026-09-29
Decision: The Chief of Staff begins with the human's requested work; R0880 no longer requires a project-status sweep on invocation, and that assessment moves to the separately invoked Project Status skill. A file under retros/ that is untracked in the clone still lands with the next flush package under R1613, and R1244 still requires that a retro never reads from or writes to a remote.
Context: the human chose this single change as the starting point for production engineering work with Fiducial; further role changes will be informed by use and session retros rather than prescribed in advance. This replaces DEC-000990's startup-check requirement while retaining its retrospective handling obligations.
Supersedes: DEC-000990

## DEC-001070 — The decision session runs its executors; the human is a gate
Date: 2026-11-03
Decision: Fiducial's standing model is that the decision session runs execution and review as subagents in the harness it is in; the human receives triage lines, pull requests, and gate requests, and carries nothing between sessions. A command block, execution block, or baton is handed only where a subagent cannot reach.
Context: The 2026-11-02 Illuminait session ran this way under a one-night amendment (its DEC-000010) and the retro's evidence supported making it standing. The courier model — the human as message bus — was fiducial's assumption from June.

## DEC-001080 — Orchestration leaves fiducial; the sort test
Date: 2026-11-03
Decision: Fiducial stops carrying orchestration. Every row is sorted by one test: if a harness (Claude Code, Claude, Codex) can enforce it deterministically it leaves the store — as a hook, a deny rule, an agent file, a skill, or nothing; if it requires judgment it stays. The sort is recorded per row; retired rows go to `rules/retired/` naming their successor.
Context: Fiducial was built to understand the harness problem space. The lesson it taught is that orchestration belongs in deterministic code around the model, and the harnesses now carry that code.

## DEC-001090 — One SPEC.md; Anthropic's vocabulary where it names the same thing
Date: 2026-11-03
Decision: The PRD and TRD collapse into one `SPEC.md` per project. Fiducial adopts Anthropic's terms where the two name the same thing — spec, definition of done, approve, reviewer, a check to run, subagent, hook, deny rule, skill, agent — and keeps its own where Anthropic has none: evidence class, verification boundary, consequential class, decision log, retro.
Context: Anthropic's best-practices document (read 2026-11-03) names exactly one document, `SPEC.md`, and no architecture document; OpenAI's Codex documentation names none.

## DEC-001100 — The store stays the source; the adopter reconciles into repos
Date: 2026-11-03
Decision: The row store remains the source of truth (provisionally — revisited if the generator rework proves costly). The generator emits per-harness shapes, and an adopter skill reconciles them into a repo that already has harness files: inventory what exists, read for contradictions, create what is missing, append what is wanted; re-runnable.
Context: A repo being adopted may already carry `CLAUDE.md`, `.claude/settings.json`, `AGENTS.md`, `.codex/` and the rest; fiducial must merge into it, not overwrite it. This replaces the thin-pointer adapter model.
Supersedes: DEC-000910

## DEC-001110 — The writing corpus is out of scope; writing roles stay standalone bundles
Date: 2026-11-03
Decision: The writer, copy-editor and critic rows and their topics, `voice.md`, `outline.md` and the public-prose criteria are unchanged by this revision, and those roles keep a standalone bundle form invoked by name.
Context: The writing roles are used differently — loaded by name as a context, not reconciled into a repo.

## DEC-001120 — This revision runs under the new model
Date: 2026-11-03
Decision: The revision is specified in one `SPEC.md` the human approves; the decision session then runs execution and review as subagents and hands the human pull requests and gates. Every ruling still lands here as a DEC entry.
Context: The first use of the model on fiducial itself, rather than intake deltas carried as directives.

## DEC-001130 — Command block, execution block and baton stay, pruned
Date: 2026-11-03
Decision: Three human-facing forms survive the sort because a harness cannot compute them: the command block (shell the human runs as given), the execution block (the secondary path for an executor the decision session cannot spawn), and the baton (only what a successor cannot recompute from the tree). The directive package — route-and-model line, FIRST ACT, worktree choreography, the M1–M8 lint — retires.
Context: The human still applies Terraform and pushes from the machine holding the credential, and still ends long chat sessions by choice; those crossings need a form.

## DEC-001140 — SPEC.md for the subtraction is approved
Date: 2026-11-03
Decision: The human approves `SPEC.md` at 2c0d491ae5024073a2510834b6794146a62007c2 as the spec for the revision DEC-001080 names. Its definition of done governs the work; its open questions are resolved by the means each names.
Context: Drafted in the 2026-11-03 session from that day's rulings, corrected in review (Codex artifacts named in the adopter journey; command block, execution block and baton kept), and shipped by the human's word.

## DEC-001150 — The sort table is the evidence record for the subtraction
Date: 2026-11-03
Decision: The sort of every row under the DEC-001080 test is recorded in `docs/research/sort-table-20261103.md` as ruled; the execution pass derives the retirements, hooks, agent fields, skill steps and rewordings from it, and ids, orders and successors are derived from the tree, not dictated.
Context: One subagent read all 461 rows at `4134897` and proposed fifteen classes, five undecided rows and six notes; the human ruled on each on 2026-11-03. 358 rows are in scope; 103 writing-corpus rows are untouched under DEC-001110.

## DEC-001160 — Class 1: the directive-package rows retire
Date: 2026-11-03
Decision: Every row that shapes, lints, routes or verifies a directive retires with the package (32 rows, class 1 of the sort table); the two execution-block invariants — self-contained, nothing before the block — restate once under `command-blocks`, and the route-and-model line becomes the agent `model:` field.
Context: DEC-001130 kept the execution block as a secondary path and retired the directive package around it.

## DEC-001170 — Class 2: worktree choreography retires; R0199 stays
Date: 2026-11-03
Decision: R1295 and R1296 retire, successor harness-managed subagent worktrees. R0199 (if a file you did not change moves, HEAD moves or an index lock appears, stop and report rather than recover) stays, reworded from execution session to subagent and working tree.
Context: The harness denied worktree isolation on 2026-11-02 and worktrees were made by hand, so the condition R0199 guards still arises.

## DEC-001180 — Class 3: the courier rows retire; three judgment rows stay
Date: 2026-11-03
Decision: R0896, R0474, R1476, R1395a, R1395b and R1106 retire, successor subagents: the decision session spawns both sides and reads the report in-session. R1478, R1479 and R1480 stay, reworded from session to subagent.
Context: The six exist only because the human carried reports and findings between sessions; the three are rules about lanes and dispositions that happen to mention sessions.

## DEC-001190 — Class 4: spec-test-suite and convergence sequencing retires; the coherence standard stays
Date: 2026-11-03
Decision: R1468, R1101, R1126, R1158, R0470, R0085, R0086 and R0483 retire, successor `SPEC.md`'s definition of done, the red gate and plan mode. R1473 (spec and tests cohere) and R1474 (spec finding versus test-side gap) stay.
Context: Sequencing is the harness's; the standard the review applies is judgment.

## DEC-001200 — Class 5: the tranche vocabulary retires
Date: 2026-11-03
Decision: R0003, R0008, R0012, R0013 and R1491 retire with no successor; R1490 retires into R0009. The open-delta rows (R0004, R0006, R0007, R0009, R0011, R0017) stay, pruned of the word tranche. Issue #383 closes: there is no claimed territory left to enforce.
Context: One `SPEC.md` per project (DEC-001090) leaves no concurrent spec territory.

## DEC-001210 — Class 6: the PRD/TRD two-document rows retire; R0863 stays
Date: 2026-11-03
Decision: R0757, R0758, R0871, R1541, R0872, R0046 and R0561 retire into `process/spec-template.md`. R0863, the Architect's design obligations, stays reworded to the spec's design section.
Context: R0863 is content the spec's design section must contain, not a statement that there are two documents.

## DEC-001220 — Class 7: secrets and production become deny rules
Date: 2026-11-03
Decision: R0164 and R0203 carry `enforce: deny`; the generator emits a `Read` deny on credential paths and a block on apply, destroy, deploy and production commands (a `PreToolUse` hook on Codex, which has no deny rules), and emits the one-line principle into `CLAUDE.md`. The Human note states that a deny matches tool calls, not intent.
Context: The 2026-11-02 session proved the hook form in two minutes and it held all night.

## DEC-001230 — Class 8: git and record immutability become deny rules and hooks
Date: 2026-11-03
Decision: R0564 (no force-push; no per-push approval for a plain push), R0583 (append-only decision log) and R1408 (existing review artifacts are not rewritten) carry `enforce: deny` or `enforce: hook`. R0564's Human note gains: on a GitHub Free repo the forge layer is absent and the hook is the only layer.
Context: Each is a byte-level check on the tool call.

## DEC-001240 — Class 9: the path-scoped write guards become hooks; the finding sentence moves to the agent definitions
Date: 2026-11-03
Decision: R0091 and R1156 carry `enforce: hook` — a `PreToolUse` on Edit and Write keyed on the agent and the path. The sentence "a change you need outside your lane is a finding, not an edit" is emitted into the architect and test-designer agent definitions by the generator.
Context: The guard is deterministic; the reason for it is not.

## DEC-001250 — Class 10: the store and artifact lint rows become one hook
Date: 2026-11-03
Decision: R1605 (citations co-render), R0196 (generated-file timestamp name) and R1414 (the `Verdict:` lines and their enum) carry `enforce: hook` and are emitted as one `PostToolUse` lint over `rules/` and `reviews/`.
Context: Each has bitten at least once and none needs judgment.

## DEC-001260 — Retros land themselves
Date: 2026-11-03
Decision: The retro skill's last step commits `retros/retro-<timestamp>.md` on a branch, pushes, opens the pull request, merges it as a routine change under R0570 and DEC-000920, and reads main back. R1244 keeps its input half (the retro's inputs are the conversation and the local tree) and drops "write nothing to any remote"; R1246 and R1613 retire with no successor; the synthesis procedure lands the same way. The human's `retro-land` shell function retires.
Context: The no-remote rule existed to keep two sessions off one shared connector; each sandbox session now has its own clone and credential. DEC-001060's other ruling survives unchanged and is restated here: the Chief of Staff begins with the human's requested work, and the project-status assessment is the separately invoked Project Status skill.
Supersedes: DEC-001060

## DEC-001270 — Class 11: the agent-definition rows become agent-file fields
Date: 2026-11-03
Decision: R0259 becomes the `model:` field, the generator mapping the three tiers to each harness's current model names. R0939, R1031, R1056 and R1141 become the `description:` of the coder, release-manager, reviewer and test-designer agents. A role's judgment rules stay rows and are emitted into the agent file's body.
Context: R1056's Human note (in force until a published code-review standard replaces it) rides with the description.

## DEC-001280 — Class 12: the gate-request procedure becomes the gate skill
Date: 2026-11-03
Decision: R0551, R0552, R0553, R0558, R0560, R1039 and R0505 become the steps and template of `gate`, a skill the decision session invokes for a consequential change, with `disable-model-invocation: true`. Whether a change is consequential (R0535, R0536) and that absence of a response is not a go (R0562) stay rows.
Context: A procedure with a fixed order and a template is a skill.

## DEC-001290 — Class 13: the release-package and report templates become skill templates
Date: 2026-11-03
Decision: R0502, R0503, R1032, R1041, R1042, R1044 and R1045 become the `release` skill's templates and their two sentences of instruction; R0506 becomes a shared report template the review skill also reads. R0509 and the verification rows stay.
Context: A field list is a form, and a form belongs in the skill that fills it.

## DEC-001300 — Class 14: two procedure steps become skill steps; R1611 stays
Date: 2026-11-03
Decision: R0486 (a different agent implements than wrote the tests) becomes a step of the build skill and R0944 (record each intake as a review artifact) a step of the intake skill. R1611 stays, reworded for one `SPEC.md`: read the spec and its approving entries whole before directing; a question the spec answers is a defect in the read.
Context: R1244 and R1246 are disposed by DEC-001260.

## DEC-001310 — Class 15: one survivor per duplicate pair
Date: 2026-11-03
Decision: Where two rows define or require the same thing, the copy with content survives: R0131–R0139 over R0022–R0026; R0485 over R0113; R0489 retires (R1031 is now an agent description); R0006 over R1602; R0017 over R1153; R1533, R0472 and R0759 merge into one row about the spec; R0876 over R1543; R1513 and R1542 merge into one row about an approved `SPEC.md`; R0009 over R1490.
Context: One source of truth per topic (SPEC.md §4).

## DEC-001320 — R0934 becomes a hook
Date: 2026-11-03
Decision: R0934 carries `enforce: hook`: governed paths (`rules/`, `process/`) are editable only inside the intake skill. No prose row is kept; R0462 and R0166 carry the judgment halves.
Context: Traced to the old Chief of Staff role file's constraints with no incident recorded; the mistake it prevents — editing a row and pushing it — is one the harness can prevent outright.

## DEC-001330 — R0202 retires; R0205 is cut to the block distinction
Date: 2026-11-03
Decision: R0202 (the execution-session definition) retires with no successor; surviving rows say subagent or the session that runs it, and `session: [execution]` is a schema key, not a term. R0205 stays as one sentence: a command block is shell the human runs; an execution block is instructions a session carries out.
Context: Thirteen rows used the term; all but seven retire, and those seven read correctly with subagent.

## DEC-001340 — R1606 stays, reworded for plans and subagent prompts
Date: 2026-11-03
Decision: R1606 stays: a plan or subagent prompt dictates intent, acceptance criteria and agreed wording; a fact the tree resolves — an id, a position, a key value, a tool name — is derived and reported by the one who runs it. R1607 stays with it.
Context: The mistake it prevents still happens under subagents and nothing in the harness checks it.

## DEC-001350 — R0720 becomes a hook, successor R0172
Date: 2026-11-03
Decision: R0720 carries `enforce: hook`: after any `git push`, fetch the remote and print the ref's SHA, failing loudly if it differs from what was sent. The claim obligation is R0172's. No prose row is kept.
Context: The incident behind R0720 was a session with no evidence in front of it; the hook supplies the evidence and R0172 obliges the citation. Where no hook fires, the first retro catching a "landed" without a read-back is the signal to revisit.

## DEC-001360 — The verb is approved
Date: 2026-11-03
Decision: R0611 stays reworded: something is approved when the human has approved it, and no other word carries the act. The execution pass replaces agree and agreed across surviving rows, process documents and the spec template. Existing decision-log entries keep their wording.
Context: DEC-001090 adopted Anthropic's vocabulary.

## DEC-001370 — R0054 retires; skill takes the harness meaning
Date: 2026-11-03
Decision: R0054 (the skill-document category) retires with no successor. In the lexicon, a skill is a procedure saved as `SKILL.md` that the session reads only when it is invoked.
Context: The category is empty once the directive-era documents retire, and the word collides with the harness meaning this revision adopts.

## DEC-001380 — R0264 loses its four lintable criteria to the store lint hook
Date: 2026-11-03
Decision: The criteria "refers to no file by path", "every key value taken from values the key already holds", "names the session kind", and "speaks in tiers, never model names" leave R0264 and join the `PostToolUse` lint of DEC-001250. The twelve judgment criteria stay in R0264.
Context: R0264's own criterion: a rule a tool enforces is the tool's.

## DEC-001390 — The author/reviewer separation rows stay; R0065 widens to review
Date: 2026-11-03
Decision: R0462, R0065, R0487 and R0488 stay. R0065 widens from code review to review, so a reviewer that did not write a plan reads the plan before dispatch.
Context: The harness provides the means of separation, not the obligation to use it; the 2026-11-02 retro's evidence 11 is the case. R0038 and R0493 stay as the sort proposed; the one-classification question is #393.

## DEC-001400 — enforce: takes four values
Date: 2026-11-04
Decision: A row's `enforce:` field takes `hook`, `deny`, `agent` or `skill`; `SPEC.md` §7 is amended from its three values, since an agent-field row and a skill-step row also leave the store with the generator still reading them.
Context: The plan's review (2026-11-04, F-2) found the spec and the sort disagreeing on the value set.

## DEC-001410 — The two live specs reconcile into one specs/rule-store.md
Date: 2026-11-04
Decision: `specs/rule-store.md` and `specs/bundle-system.md` are reconciled in package 6 of the subtraction plan into one `specs/rule-store.md` in the spec-template form, the generator as its design section.
Context: The store and the generator are one system once the emitters land, and a superseded PRD left live is drift.

## DEC-001420 — The Codex emitter is built by a Codex session
Date: 2026-11-04
Decision: `SPEC.md` open question 4 resolves: the Codex emitter is in this revision as package 3b, handed to a Codex session on the human's machine as an execution block written from package 3a's landed interface, and live-verified there — the session emits into a stand-in repo, starts itself in it, and reports what loaded.
Context: A Codex session is the one executor that can verify a Codex emitter by loading its own output; this is DEC-001130's secondary path in use.

## DEC-001430 — Search current documentation before diagnosing an external failure
Date: 2026-11-04
Decision: A new row in `core`, every software role, decision and execution: on a failure from an external system, search current documentation before offering a mechanism from memory, and prefer a probe that distinguishes hypotheses over a diagnosis. Package 1b lands it.
Context: The 2026-11-02 retro's evidence 16 and 17 — two wrong mechanisms asserted from training in one night, each settled by one search or one probe.

## DEC-001440 — A review pass that did not run is recorded, never read as clean
Date: 2026-11-04
Decision: A new row in `review-artifact-schema`, the reviewer roles and the Chief of Staff: a review artifact names every pass that was planned, and a pass that did not run — a subagent killed by a usage cap, say — is recorded with why, so a missing verdict is never read as a clean one. Package 1b lands it.
Context: The 2026-11-02 retro's evidence 12 — the env-roots skeptic pass never ran and only the retro noticed.

## DEC-001450 — A review artifact over a delta is named by the delta's branch slug
Date: 2026-11-04
Decision: A review artifact over a delta takes its name from the delta's branch slug. Package 2 applies it to `process/review-artifact.md`.
Context: Ruled 2026-09-16 when the filename rule had no form for a two-document delta; carried in the 09-17 baton and never recorded until the plan's review found the plan citing it.

## DEC-001460 — The subtraction plan is approved
Date: 2026-11-04
Decision: The human approves `docs/plans/subtraction-plan-20261104.md` at 28366d488f20f01093df1339a109600e066e87c6 (merge of PR #395) as the plan for the revision SPEC.md governs. Packages dispatch in its order from 1a; each package's DEC entries are appended at merge.
Context: Written in the 2026-11-04 session, reviewed once by a subagent that did not write it, revised, and approved by the human's merge.

## DEC-001470 — Package 1a landed: the sort's moves
Date: 2026-11-04
Decision: Package 1a of the subtraction plan is merged at 699a0fa (PR #397, branch tip a270653): 75 rows retired to `rules/retired/` with `retired:` lines naming a row id or a DEC id, `enforce:` on 34 rows (hook 9, deny 3, agent 5, skill 17), 20 rows re-topiced (`directive-invariants` survivors to `chief-of-staff`, `convergence` to `change-flow`, `trd` and `prd-template` to the new topic `spec`), the store admitting `enforce:` with four values, and `bin/tests/reconcile_sort.py` as the proof. Review artifact: `reviews/pkg-1a-store-moves-read-20261104T185942Z.md` — ready on re-read.
Context: The two DEC-001310 merges with no named survivor (R1533+R0472+R0759; R1513+R1542) were escalated by the coder and pass to package 1b, whose blast radius widens to move the losers.

## DEC-001480 — Package 1b landed: the sort's bodies
Date: 2026-11-04
Decision: Package 1b of the subtraction plan is merged at 19f6760 (PR #401, branch tip 0da3040): 40 rows reworded or pruned per DEC-001170 to DEC-001390, the two DEC-001310 merges (R0472 and R1513 survive), the approve sweep, fenced blocks on all 34 `enforce:` rows under the `bin/hooks/<name>` convention, and new rows R1616 (DEC-001430) and R1617 (DEC-001440). Store: 384 live, 83 retired. Review artifact: `reviews/pkg-1b-store-bodies-read-20261104T203811Z.md` — ready-with-findings on re-read; hand-offs #399, #400.
Context: Two amendments restored six obligations the first rewording had dropped; the reviewer's independent render confirmed no retired mechanism names a definition.

## DEC-001490 — R0205 retires into R0208
Date: 2026-11-04
Decision: R0205 retires into R0208, which already carries the command-block / execution-block distinction in full; DEC-001330's ruling that R0205 stays as one sentence is superseded for that half only — its ruling that R0202 retires stands.
Context: Found during package 1b's amendment: R0205's one surviving sentence duplicated R0208, and with its layer terms gone it rendered nowhere. Ruled by the human 2026-11-04 under DEC-001310's one-survivor principle.
Supersedes: DEC-001330
## DEC-001500 — Package 2 landed: the process documents
Date: 2026-11-04
Decision: Package 2 of the subtraction plan is merged at b4f1909 (PR #402, branch tip 26f4df7): three documents retired to `docs/history/`, `process/spec-template.md` written from the two templates, `change-flow.md` rewritten around the subagent model at 42 lines, retros landing themselves, the decision-log and review-artifact rules as DEC-001260 and DEC-001450 state, project-setup's Free-tier fallback (closes #389), `spec` and `spec-template` sequenced before `change-flow`. Review artifact: `reviews/pkg-2-process-docs-read-20261104T224509Z.md`.
Context: One read found the gate placed at the merge; three amendments; re-read ready-with-findings.

## DEC-001510 — A planned review pass that did not run is recorded as not-run
Date: 2026-11-04
Decision: R1414 gains a fourth pass verdict, `not-run`, more severe than `ready-with-findings` and less than `changes-required`; a pass that was planned and did not run carries `Verdict (<pass>): not-run` and one line saying why (R1617), and the overall verdict is still the most severe pass verdict on that order. Landed in package 2.
Context: R1617 (DEC-001440) and R1414 conflicted as written; the store-lint hook of DEC-001250 would have refused the first artifact recording an unrun pass.

## DEC-001520 — process/project-setup.md renders to the Chief of Staff
Date: 2026-11-04
Decision: `process/project-setup.md` carries `role: [chief-of-staff]` and renders into that bundle. The 2026-09-06 choice to drop its role key (commit 85f6e43, recorded in no entry) is reversed: under the subagent model the Chief of Staff runs the adopter, whose first act is the document's preconditions.
Context: Issue #389's first item — the document said the Chief of Staff confirms the preconditions but never rendered to him.

## DEC-001530 — Packages 3b and 4 go to a Codex session; package 6 splits
Date: 2026-11-04
Decision: Packages 3b and 4 of the subtraction plan are handed together, as one execution block, to a Codex session on the human's machine, which orchestrates both with its own subagents — a coder and a reviewer that did not write the work per package — and opens one pull request per package. Package 6 splits: 6a (remove the four tools and `bin/aimeta/`, archive the root residue and the old specs, reconcile `specs/rule-store.md` to the template per DEC-001410) depends on 1 and 3a and runs now in this session at the solid tier; 6b (self-adoption, README) depends on 5. Packages 5 and 6b are routed when 4 lands. The package 7 close read stays in this session at the frontier tier, gated by the human. DEC-001460's routing is superseded to that extent and stands otherwise.
Context: The subtraction's first day consumed half the human's weekly Anthropic usage, every subagent having run at the frontier tier by an unset default; he is cash-constrained. The execution block is DEC-001130's secondary path.
Supersedes: DEC-001460

## DEC-001540 — Subagent dispatch names its model tier; the frontier tier is gated
Date: 2026-11-04
Decision: Every subagent the decision session dispatches names its model tier explicitly — solid for coding and mechanical review, frontier only where the plan names it — and a frontier dispatch the plan does not name is asked of the human first, yes/no, each time. Briefs point at files in the tree rather than restating rulings; a re-read over an amendment reads only the diff; a package whose findings are all non-blocking lands without a re-read (DEC-001000).
Context: R0259 already says it; it was not followed because the dispatch tool inherits the session's model when no tier is set. Ruled by the human 2026-11-04.

## DEC-001550 — Packages 3b and 4 landed, by a Codex session
Date: 2026-11-04
Decision: Package 3b (the `codex` emission target; PR #408, tip 23c2850, verdict ready, live-verified in a Codex session) and package 4 (the procedure documents `gate.md`, `release.md`, `intake.md`, `build.md`, `project-status.md` under `process/`, `skills/` retired, rows R1618–R1622 — four role descriptions and the reviewer lane guard; PR #407, tip eb64fe6, ready after one amendment) are merged at 9c0dcbd and 17861e1. Both were orchestrated by a Codex session on the human's machine from one execution block (DEC-001530).
Context: The first packages run on the secondary path; Codex settled the per-agent scope question from inside Codex and recorded it in 3b's artifact.

## DEC-001560 — bin/bundle --where renders the local tree
Date: 2026-11-04
Decision: `bin/bundle --where` no longer refuses on a dirty `rules/` or `process/` tree or on HEAD differing from `origin/main`; it renders the local tree as `--emit` does. `bin/release` keeps its own sync check. Landed in package 6a.
Context: DEC-000940 ruled this for ordinary generation; package 3a applied it to `--emit` only, and the 6a review found the reconciled spec ratifying the old refusal. Ruled by the human 2026-11-04.


## DEC-001570 — Package 5 landed: adopter and first real adoption
Date: 2026-11-04
Decision: Package 5 is merged by PR #413 at f21939831ac72dacfb24ae450e83ff47198f3d51, branch tip e8dc0252d87f2460ae2c6a33ffcd3270f6ae101f; its procedure review is ready-with-findings, with non-blocking follow-ups #411 and #412. The first real adoption is https://github.com/davepierceops/illuminait/pull/26: the package execution artifact records installation and push but no merge, and the later committed live-check artifact records that PR still open at its read-back; these are dated evidence, not a claim about its present merge state.
Context: reviews/pkg-5-adopter-execution-20261105T012406Z.md and reviews/fiducial-adoption-20261105T011135Z.md record the pinned-source run, independent contradiction read, human C1–C4 rulings and no-op repeat apply. The human subsequently ran the supplied fresh-session check and supplied a screenshot and /context all output, recorded in reviews/fiducial-adoption-live-check-20261105T020041Z.md: CLAUDE.md (8.6k tokens), eight project agents and twelve model-invocable project skills were discovered (live-verified for loading/discovery only); actual native hook firing, manual gate invocation and Codex trust in that target remain unverified.

## DEC-001580 — Package 6a landed: cleanup and reconciled tooling spec
Date: 2026-11-04
Decision: Package 6a is merged by PR #409 at 95e77f71c771de5a216a2c3f4900c0ff21435eed, branch tip 3f6a815122befe8fae6731e5b645f3739f04717c: obsolete directive tools and bin/aimeta are removed, root residue and obsolete specs archived, and specs/rule-store.md reconciled to the single-spec form and all three emitters. DEC-001560 records the accompanying local-tree --where behavior.
Context: reviews/pkg-6a-cleanup-read-20261105T005654Z.md preserves the changes-required first read and records the decision session's amendment verification without a second independent read; its reported suite passed 290 tests (contract-verified), with remaining non-blocking findings carried for the close read.

## DEC-001590 — Package 6b landed: self-adoption and README
Date: 2026-11-04
Decision: Package 6b is merged by PR #414 at e3850f6587a242920bd04c90cb48e8f2e3ba2b62, branch tip f07277464924c3fc11a321b79c1603d258ffee1c: Fiducial installs both emitted harness trees, preserves existing denies, removes the four stale adapters/placeholders and rewrites README.md. Its independent review is ready in quality, skepticism and continuity.
Context: reviews/pkg-6b-self-adopt-read-20261105T013508Z.md and reviews/pkg-6b-self-adopt-execution-20261105T013113Z.md record 303 passing tests, unchanged repeat apply, and installed intake-hook subprocess refusals (contract-verified); actual harness-driven enforcement and fresh-session loading in this separate target remain unverified. The Illuminait loading evidence in DEC-001570 does not establish Fiducial target loading.

## DEC-001600 — Package 7 routes to this Codex decision session
Date: 2026-11-04
Decision: The human's package 7 execution block assigns the close to this Codex decision session on pkg-7-close from e3850f6, with one pull request, plain pushes, append-only decisions and no agent merge or release. One fresh frontier reviewer that authored none of the packages reads the whole revision; independence from the authors but not from the executor family is an accepted-risk gap for the human to ratify at release.
Context: This replaces DEC-001530's package 7 routing only; its other rulings survive: packages 3b/4 were routed together to Codex with separate coder/reviewer work and one PR each; package 6 splits into 6a cleanup depending on 1/3a and 6b self-adoption/README depending on 5; packages 5/6b route after 4; DEC-001460's approved plan and remaining routing stand. The human answers OQ1–3 before the close read; OQ4 remains resolved by DEC-001420; the human retains merge and release.
Supersedes: DEC-001530


## DEC-001610 — OQ1: tagged source for software adoption; existing downloads retained
Date: 2026-11-04
Decision: The human resolves SPEC.md §9 OQ1: software adoption consumes the repository source pinned to a release tag and generates the harness trees from it; this release retains all twelve role bundles plus README.md as compatibility and chat downloads. No generated harness archives are required as release assets, and the writing-role bundles remain available unchanged in form.
Context: Package 5 consumed source checkout bb2ebcb4ea140deb40d7148d7dbffcae56806fe2 rather than downloaded bundle files. bin/release currently generates the twelve process/named-queries.md bundles plus README.md and prints the human-run publication command; that asset set already matches this ruling. The human answered yes to tagged-source adoption with existing downloads retained; OQ2 separately settles the Claude-chat Chief of Staff loading form.


## DEC-001620 — OQ2: Claude chat keeps the Chief of Staff bundle
Date: 2026-11-04
Decision: The human resolves SPEC.md §9 OQ2: the Chief of Staff in ordinary Claude chat continues to load the generated chief-of-staff bundle uploaded as a Claude project file. No separate chat-specific file format or loading workflow is introduced in this revision.
Context: README.md already describes this path and bin/release includes the bundle. The human answered yes after the question was clarified in ordinary workflow terms. No comparison trial against a separate chat format is recorded; that comparison remains unverified, and this ruling makes no claim that it ran or that Claude Code's separate /context evidence establishes Claude-chat behavior.


## DEC-001630 — OQ3: the store remains the source of truth
Date: 2026-11-04
Decision: The human confirms SPEC.md §9 OQ3: rules/ and process/ remain the master sources, with the generator deriving Claude Code, Codex and standalone bundle forms. The adopter still inventories existing harness context, obtains independent contradiction review and human rulings, then creates or reconciles owned output without overwriting unrelated project context; DEC-000910's thin-pointer adapter model remains superseded.
Context: The generator rework produced shared emitter code and three output targets, required review amendments, and the package 7 baseline passes 303 tests (contract-verified); no aggregate time or monetary cost is recorded. The human judged this sufficient to retain one source rather than maintain harness files independently, confirming DEC-001100's provisional choice; no claim of measured cost savings is made.
Supersedes: DEC-001100


## DEC-001640 — Package 3a landed; its reviewed policy amendments are ratified
Date: 2026-11-04
Decision: Package 3a landed by PR #404 at 3f6fc8c276d5f095aba51b6a77e76e2e4c992ead, branch tip 57467011afe144c2e32d46d14dfe4a104dfd4ae9; the human now ratifies its implemented policy amendments: 200 CLAUDE.md lines are guidance with warning-and-emission, matching standing topics spill into skills, agents retain the shared tool list with scoped guards, and bundles render enforcement rows as prose only, omitting enforcement YAML and Human notes. Review immutability protects files on origin/main or main, permits unlanded branch drafts, and falls back to tracked-at-HEAD protection only when neither default-branch ref exists; R1408 and the governing spec/plan are reconciled to that behavior.
Context: reviews/pkg-3a-generator-read-20261104T231554Z.md records the frontier first read, amendment and ready-with-findings re-read; the original landing had omitted its DEC entry. The human explicitly approved this complete close amendment on 2026-11-04 after reviews/pkg-7-close-read-20261105T024910Z.md exposed the gap. This amends SPEC.md §4's strict line limit and the plan §3a refusal requirement; it does not authorize a broader context-pruning project (#403), change the tier map, or claim native enforcement.

## DEC-001650 — The close restores retained obligations and reconciles current guidance
Date: 2026-11-04
Decision: The human approves the complete package 7 continuity amendment: restore the two retained execution-block obligations once under command-blocks, add the promised skill definition, and reconcile live spec, plan, README and procedure text to DEC-001260 and DEC-001610–001640. The two new implementation findings in the close read, push-readback payload/ref handling and source-only paths in emitted skills, remain non-blocking file-and-land follow-ups; the same independent reader reviews only the amendment.
Context: The restored obligations implement DEC-001160 and DEC-001370 without reviving the directive package. R1623 and R1624 are judgment rows sorted stays; R1625 is the live skill definition, sorted stays. The candidate follows intake on intake/pkg-7-close-reconciliation before incorporation into the single pkg-7-close PR; derived context is regenerated and independently checked. No prior decision or review artifact is rewritten, and the human retains merge and release.


## DEC-001660 — The close read finds twelve definition-of-done items met; human merge remains
Date: 2026-11-04
Decision: Record SPEC.md §6 as read at 15da4ad0b8780b60600cbb522825f5f4bded8683, with staged plan d6600cc35af4efc93a0d85e365b33c5767853be420aa85044dca0a7f55426667: items 1–11 and 13 are met, and item 12 remains unchecked solely for the required human merge. This records the independent assessment and evidence pointers, not human merge, release approval, or a waiver of that remaining condition.
Context: reviews/pkg-7-close-read-20261105T024910Z.md reads 3c686e0..8dddcd2; the same independent reader's reviews/pkg-7-close-amendment-read-20261105T033515Z.md resolves F1–F3 and is ready-with-findings in quality, skepticism and continuity. The parent installed and verified the five reviewed writes exactly; reviews/pkg-7-regeneration-evidence-20261105T033230Z.md records that read-back and an empty repeat plan. Process amendments in process/adopt.md and process/named-queries.md were read at the named SHA under the human's DEC-001650 authorization; the human's PR merge remains their final reconciliation approval. F4/#415 and F5/#416 remain non-blocking, with executor-family risk reserved for release ratification.


## DEC-001670 — Adopt the published release into Fiducial itself
Date: 2026-11-05
Decision: Dave authorizes Fiducial self-adoption from v2026.11.04 at 0ca563ee53c309840be4ab94dda74f9b075149ba and explicitly approves merging PR #421. The installed context already matches that release; the adoption updates only the source-provenance comments in AGENTS.md and CLAUDE.md and their ownership hashes.
Context: Dave instructed "adopt fiducial" and, after the completed installation and reviewed PR were presented, answered "Yes, merge it." reviews/fiducial-adoption-read-20261105T184649Z.md is ready in quality, skepticism and continuity with no contradictions. docs/fiducial-adoption-20261105T184428Z.md and its retained execution-report copy record exact installed byte/mode verification, an empty repeat plan and unchanged stand-in repeat apply (contract-verified). Native loading and hook enforcement remain unverified/deferred; this routine provenance update makes no new runtime claim.


## DEC-001680 — Approve the skill extraction and Fiducial self-adoption
Date: 2026-11-05
Decision: Dave signs off the reviewed process delta and authorizes merging PR #423 at reviewed candidate 99945ed1e49aafa897effa3bb09df55537445b4d: move the 27 command/execution-block and verification-checklist instruction bodies into two skills, retain explicit standing invocation rules, retire the approved R0456 duplicate in favor of unchanged R0021, and adopt the derived context into Fiducial itself. This approves the scoped extraction only; further #403 pruning remains a one-by-one human review, with no release tag or publication authorized.
Context: After the completed candidate and independent frontier read were presented, Dave answered "Yes, merge it. Then let's go through the remaining CLAUDE.md rules one by one." reviews/skill-context-extraction-read-20261105T215920Z.md is ready in quality, skepticism and continuity with no findings or adoption contradictions. docs/skill-context-extraction-evidence-20261105T220112Z.md records 310 passing tests, exact adoption byte/mode readback and an empty repeat plan (contract-verified); installed CLAUDE.md and AGENTS.md each shrink from 295 to 243 lines. Native skill invocation/loading/adherence and hook enforcement remain unverified/deferred. This entry records the final process sign-off that the earlier candidate evidence correctly marked pending.


## DEC-001690 — Approve standing-context pruning and final self-adoption
Date: 2026-11-05
Decision: Dave signs off the complete rule-by-rule pruning recorded in docs/plans/claude-rule-pruning-rulings-20261105T221134Z.md, the process and emitter changes reviewed at 722dc0482fd689c48ce16136926e0f272204a8a0, and the equivalent projected context presented in PR #424; he authorizes finalizing its retirement records, self-adopting the generated context into Fiducial, and merging that PR. The manifest’s 43 remaining rows retire under this decision (33 without replacement and 10 into skills), the 23 successor retirements and approved wording stand, and the two enforcement-only rows retain their existing mechanisms; these final rulings replace their earlier wording and scope rulings where the recorded sequence explicitly supersedes them, with unrelated specialized rules and definitions retained.
Context: After the completed candidate, measurements, passing tests, independent frontier review and explicit merge-time finalization boundary were presented, Dave answered “Yes, finalize it and merge.” reviews/claude-rule-pruning-read-20261106T070137Z.md is ready in quality, skepticism and continuity with no remaining findings; docs/claude-rule-pruning-evidence-20261106T070025Z.md records 318 passing tests and seven passing amendment checks. The human-approved projection has 18 standing instructions and 18 pulled definitions, with each generated root reduced from 241 to 75 lines and 3,252 to 1,069 words; some standalone bundles grow as documented. This approval includes the scoped shared-rule effects on writing roles despite the older subtraction SPEC’s exclusion, and requires final archive validity, output equivalence, independent adoption review and exact readback before merge. Native loading, invocation/adherence and live enforcement remain unverified; no tag, publication or other-repository adoption is authorized.


## DEC-001700 — Finalize definition pruning and retain tracker context pending adoption work
Date: 2026-11-06
Decision: Dave approves the definition-by-definition rulings in docs/plans/claude-definition-pruning-rulings-20261106T181925Z.md: retire the fourteen rows in the finalization manifest, retaining the approved R0208 paragraph in command-blocks; shorten R0535, R0780 and R0045; revise R0166; and leave R0064 unchanged pending #425. He authorizes finalization and landing of this batch with regenerated repository context, subject to required independent review and verification.
Context: After completing the review, Dave asked to finalize the batch, asked for a recommendation on R0064, and answered “go” to leaving it unchanged and retiring it later with the separate adoption work. These rulings replace the corresponding earlier wording and retention requirements, including R0611 in DEC-001360, R1625 in DEC-001370/DEC-001650, R0208 placement in DEC-001490, and R0166 wording in DEC-001690; all unrelated rulings survive. Formal retirement references are allocated during this merge finalization after checking origin/main at cb0194aee512f48f3046e5ba9be445d85f97fbd3. No generator-selection change, tracker migration, release tag, or other-repository adoption is included.


## DEC-001710 — Finalize role, review and release consolidation
Date: 2026-11-06
Decision: Dave approves the 43 rulings in docs/plans/review-verification-pruning-map-20261106T200257Z.md and authorizes unattended finalization, required independent review and verification, repository self-adoption, and merge of this batch. Apply the finalization manifest: retire twelve rows without replacement and five into named successors, retain R1414 as a hook with its explanation in review-artifact, shorten the approved role rules, give build ownership of the execution sequence, and consolidate release reporting into one change package with a readiness section.
Context: Dave instructed “Yes, finalize it and merge. Please do it as unattended as the rules allow, I'm stepping away for a long time”. This replaces only the specific wording, retention and template decisions identified by the 43 rulings, including the affected portions of DEC-000460, DEC-001280, DEC-001290 and DEC-001390; unrelated obligations survive. Review/quality policy and R0152/R0558 remain deferred to #427; SLO/Top K machinery and R0129/R0130/R1183 remain deferred to #428; tracker portability remains with #425. After checking origin/main at 1df9a4ec813e5cec756665123d8a5298c7597cef, the decision session allocates this retirement reference during merge finalization. Required review and verification must complete before landing; this authorization neither asserts they have passed nor authorizes a release tag, other-repository adoption, or deferred policy redesign.


## DEC-001720 — Finalize remaining role consolidation; defer further writing review
Date: 2026-11-08
Decision: Dave approves finalization and merge of PR #432, carrying the 81 rulings in docs/plans/remaining-role-pruning-inventory-20261107T001928Z.md and the reviewed checkpoint at 4157ddd3e1b50ff3b28c31f387e5e9e96793a3a9. Archive R0940, R0499, R0284, R1091, R1485, R1249, R0159 and R0800 under this decision, retain the seven completed successor consolidations and approved wording/scope changes, and refresh Fiducial's derived repository context after independent review and verification; approved writing edits through R1167 stand, while R1168 and further Writer, Copy Editor, Critic and shared prose/voice review remain deferred.
Context: Dave instructed “Yes, finalize it and merge. Leave the remaining writing-role work for another time.” The checkpoint's 337 passing tests and independent ready review establish the candidate; final archive/output-equivalence and adoption checks remain required before merge. The decision session allocated this reference after fetching origin/main at 2be5327e9704b0066eed7e8ef44302aa55179b18. These rulings replace only the prior wording, scope and retention choices expressly changed in the ruling log, including the applicable R0166 approval consolidation, editing/finding guidance and retro candidate-rule duties; unrelated decisions survive. R1249's archive preserves the already-approved narrower audience. The older subtraction spec's writing exclusion does not undo the writing changes individually approved in this later pass. Remaining definition cleanup and #425/#427/#428/#430/#431 are separate; no release tag, other-repository adoption or further policy redesign is authorized.


## DEC-001730 — Adopter preserves existing modes on Markdown and JSON files, manifest included
Date: 2026-11-10
Decision: Dave approves fixing #411 before any v2026.11.10 publication, and approves fixing the ownership manifest's hard-coded 0644 in the same change: an existing Markdown or JSON file, including `.claude/fiducial-ownership.json`, keeps its mode through adoption, and a new file takes the generated mode. Landed by PR #434, main at f48552aa1d52a754610f7663f57d1ea44478c0b4, with a routine self-adoption refresh applied on his go after an independent contradiction read found none.
Context: Dave pointed the decision session at `docs/releases/v2026.11.10/session-handoff.md` @ 7288c7a, which holds publication until #411 is fixed. The fix was reproduced at 5b2a62f, tested first by a separate test designer, and read independently; the reads are in `reviews/adopter-preserve-modes-*`. The remaining-role-pruning finalization tests were pinned to the #432 merge commit because they compared the working tree to a frozen preview and failed on any later process change. Publication remains unapproved (#433).


## DEC-001740 — Triage of the #411 reads' non-blocking findings
Date: 2026-11-10
Decision: Of the six non-blocking findings from the reads over `intake/adopter-preserve-modes`, the manifest mode is fixed in DEC-001730's change, the read-only-file partial write is recorded as one comment on #412, and the other four are not filed: the store cannot tighten an existing file's mode, a prose imprecision about the TOML and hook rule, missing 0400/0666 test cases, and a named-queries read in the finalization test's shared setup.
Context: Five independent reads over a two-line change produced these; Dave asked why one fix had grown to six findings and a blocker, and answered "y" to this disposition. The four unfiled findings remain readable in the review artifacts.


## DEC-001750 — Publish v2026.11.10 at a8d87bc
Date: 2026-11-10
Decision: Dave approves publication of the context-consolidation revision as release `v2026.11.10` at a8d87bc95afed9f5ac8b54fe2c8863013ce10265, with README.md and the twelve named role bundles as its assets and the deferred gaps listed on gate #433 carried as stated there. Published 2026-11-11T04:25:42Z by Dave from his clone.
Context: Asked "Publish this candidate, yes or no?" after the candidate and evidence were regenerated with the #411 fix (DEC-001730), Dave answered "yes". The tag keeps the gate's proposed name; it was still 2026-11-10 in his timezone. Read back from GitHub after publication: the tag resolves to the candidate, the release is neither draft nor prerelease, and all 13 asset names, sizes and SHA256 digests equal `docs/releases/v2026.11.10/SHA256SUMS` on branch `release-candidate-20261111` at f0d5be8af4135bacffb1576dfa54cb5bbaf82bdf. Native skill loading, adherence and hook enforcement remain unverified, and #412 remains open.


## DEC-001760 — Adopt v2026.11.10 into fiducial
Date: 2026-11-10
Decision: Dave approves adopting the released `v2026.11.10` (a8d87bc95afed9f5ac8b54fe2c8863013ce10265) into fiducial's own repository as a routine adoption. The installed context's pinned store commit becomes the released commit; nothing else in the installed context changes.
Context: After publishing the release (DEC-001750), Dave instructed "I'd like you to adopt it into Fiducial." The plan wrote `CLAUDE.md`, `AGENTS.md` and `.claude/fiducial-ownership.json`; an independent contradiction read found none; the report is `docs/fiducial-adoption-20261111T042936Z.md`. Live Claude Code loading and Codex hook trust were not checked.

## DEC-001770 — Fix adopter preflight, push read-back and skill references before the live probe
Date: 2026-11-10
Decision: Dave approves fixing #412, #415 and #416 as one change before the repeatable live probe (#439) is built: adoption refuses a destination that became a directory or that it lacks permission to write, delete or create, before its first write; push read-back keeps slash-containing branch names and reads Codex `cmd` payloads for shell tools; emitted skills refer to other skills in each harness's own form, and emission fails on a reference with no skill. Reviewed on `intake/adopter-hook-portability` at b3be5cc56c2beb046159275abd93b09fa66b2dbb.
Context: Shown the open backlog grouped by readiness and asked "Is that first group the work you want before the probe: yes or no?", Dave answered "yes". The plan, its independent read, the tests and both review artifacts are on the branch (`docs/plans/adopter-hook-portability-plan-20261111T053544Z.md`, `reviews/adopter-hook-portability-*`); both reads returned ready-with-findings with no blocking finding, and the non-blocking findings are filed as #440. #399 was left out pending #427. Fiducial's own installed context is not refreshed by this change: DEC-001760 pins it to the released commit, and it takes this change when the next release is adopted. Contract-verified only; live harness loading and hook delivery remain unverified. No release is authorized by this entry.

## DEC-001780 — Fix rule-body, release-check and read follow-up defects as the batch's second change
Date: 2026-11-11
Decision: Dave approves fixing #365, #398, #440 and the open parts of #381 and #366 as one change in the current batch: the store refuses a rule with no instruction; a suite test checks that every retirement target exists; `bin/release` prints a command that names the repository, checks each generated bundle for its selected rows and for retired text, and checks cleanliness over the generation inputs only; and the adopter, push read-back, Codex adapter and reference rewrite follow-ups from #440 are fixed. No release, adoption or live probe follows this change; those run once at the end of the batch (#439).
Context: Asked "Is that the next package: yes or no?" on 2026-11-11, Dave answered "yes". #358 was proposed in that package and left out: refusing a bundle on a missing reference target would fail today's bundles, and the editorial work that resolves it is tied by the issue to #362 and #363. The release cleanliness check is scoped to the input folders rather than to each bundle's exact selection, a conservative reading of #366's proposal. Plan, tests and review artifacts are on `intake/generator-hook-defects` (`docs/plans/generator-hook-defects-plan-20261111T161818Z.md`, `reviews/generator-hook-defects-*`). Contract-verified only.

## DEC-001790 — A bundle rendered from uncommitted inputs marks its revision
Date: 2026-11-11
Decision: A generated bundle opens with exactly one line, an HTML comment: `<!-- fiducial <owner/repo> @ <revision> <generation timestamp> -->`, the timestamp in the `<YYYYMMDD>T<HHMMSS>Z` form. The revision is the full HEAD SHA; where a bundle is rendered from a tree whose rules, process documents or generator differ from HEAD, the SHA is followed by `+local.` and twelve hex characters identifying the uncommitted input state. Release assets never carry the marker. No member list, no blob list, no title line.
Context: Asked "Should bundles generated from uncommitted edits carry the `+local` marker in the header: yes or no?" on 2026-11-11, Dave answered "yes". #366 and DEC-000940 agreed that local output must not misrepresent its source revision; the independent read of the change found that the header's form was fixed by this entry's predecessor and that `specs/rule-store.md` §8 makes a header change consequential, so it goes on the gate of the release that first carries it. The matching spec sentences are proposed on the same branch and await Dave's ruling.
Supersedes: DEC-000630

## DEC-001800 — The rule-store spec states the local marker and the release tool's refusals
Date: 2026-11-11
Decision: Dave agrees six changes to `specs/rule-store.md` as reviewed on `intake/generator-hook-defects` at 541f3201ba1350d5cae1bd3fa965f30ec7066f83: journeys J1 and J4, G6 and AC-RS-14 state the `+local` header marker of DEC-001790; AC-RS-12 has the printed release command name the repository; and the refusals paragraph lists `bin/release`'s refusals as an unsynced tree, an uncommitted change to a generation input, an origin that is unreachable or not a GitHub repository, and a generated bundle that lacks a selected row or carries a retired one.
Context: Shown the six changes and asked "Do you agree these six spec changes: yes or no?" on 2026-11-11, Dave answered "y". The independent read of the whole change at c2b06c8 (`reviews/generator-hook-defects-reread2-20261111T180211Z.md`) returned ready with nothing blocking, found each changed sentence true of the code and covered by a test, and the spec file is unchanged between c2b06c8 and the agreed revision. The agreement attaches to the version of record on the default branch once the change lands.
