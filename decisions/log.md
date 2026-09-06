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
