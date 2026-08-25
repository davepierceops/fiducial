You are an execution session. Read nothing from any prior conversation; everything you need is here and in the repository.

FIRST ACT — land this directive. Write this entire message, verbatim, to docs/cycles/decision-log-bundle-spine-20260824T152500Z.md on a new branch `decision-log-bundle-spine` cut from origin/main, commit it with message "Add decision-log-bundle-spine directive", push the branch (no -u), and read the landed SHA back with `git ls-remote origin refs/heads/decision-log-bundle-spine`. Report "landed docs/cycles/decision-log-bundle-spine-20260824T152500Z.md as <sha>" before doing anything else. If stderr shows "fatal: failed to store: 100001", that is keychain noise; the ls-remote result is what counts.

ROLES: no reviewer role is engaged. You act as the scribe for two dictated edits to records outside the frontmatter in-scope set (decisions/log.md, OPEN-ITEMS.md). The decision wording originates in this directive; this directive is what downstream artifacts point at. You do not merge.

WORKING TREE — exclusive assignment: `git fetch origin && git worktree add "${TMPDIR:-/tmp/claude-501}/fiducial-decision-log-bundle-spine" -b decision-log-bundle-spine origin/main` — run every subsequent command inside that directory. Do not touch /Users/dave/code/fiducial or any other worktree.

REVIEWED REF: origin/main @ 48aa1b577b46d924201c6f3fa097b11a52a7c66b. Every STOP condition below is evaluated against this commit, not against the branch head.

COMPANIONS — read whole before editing: policies/decision-log-policy.md, decisions/log.md, OPEN-ITEMS.md, all @ 48aa1b577b46d924201c6f3fa097b11a52a7c66b.

FENCE NOTE: this directive is itself a fenced paste block, so the shell procedure inside INSTRUCTION 1 is shown between `~~~` lines. When you write it into decisions/log.md, write those two fence lines as triple backticks, matching DEC-000140's own fence.

STOP AND SURFACE (do not proceed past the first that holds; report which):
- decisions/log.md @ the reviewed ref has an entry whose Supersedes line names DEC-000140.
- decisions/log.md @ the reviewed ref has an entry whose ID is not of the form DEC-<six digits> ending in 0, or the last entry's ID cannot be read.
- OPEN-ITEMS.md @ the reviewed ref has no section headed "`bin/cycle-open` and the retirement of Track".
- Any instruction here cannot be carried out as written.

INSTRUCTION 1 — append one entry to decisions/log.md. Its ID is the last entry's ID plus 10. Match the existing entries' format exactly (heading line, Date, Decision, Context, Supersedes; blank line between entries). Content, verbatim except where <ID> is substituted:

## DEC-<ID> — methodology-context-bundle: docs/global-context/*.md lead the file set; retired spine files removed
Date: 2026-08-24
Decision: Supersedes DEC-000140 whole. The bundle's file set is, in order: every `docs/global-context/*.md`, sorted by its `order:` frontmatter ascending with files lacking `order:` last; then the fixed decision-layer spine — `context-sets/spec-and-change-discipline.md`, `operating-model.md`, `roles/chief-of-staff.md`, `policies/commit-and-change-control-policy.md`; then every `skills/*.md` whose `audience:` contains `all-roles` or `chief-of-staff`. `context-sets/base.md` and `context-sets/collab-workflow.md` are no longer in the spine. The filename `methodology-context-bundle-<YYYY-MM-DD-HHMM>.md`, the `Source: @ <repo HEAD>` line, the per-file blob short-SHA, the `<!-- FILE n/N: path @ sha -->` separators, the upload-per-project instruction, and the deferral of `bin/bundle-methodology` to the tooling tranche are carried forward unchanged. The repository named is `davepierceops/fiducial`. The interim generation procedure is restated below with the amended spine; it is run from the fiducial clone root on a synced `main`, uses no heredoc, and writes to `~/code/`.
Context: The bundle in the fiducial project context was generated 2026-08-09 and predated the 2026-08-22 rename of `skills/directive-dispatch.md` to `skills/directive-authoring.md`; a 2026-08-24 gate directive cited the stale path from it (`reviews/directive-authoring-cycle-3.md`, S-1). The first regeneration under DEC-000140's procedure, at `b31b75a`, reported both retired spine files missing and omitted `docs/global-context/core.md` and `docs/global-context/decision-layer.md`, the two files every session loads first. Dave amended the spine 2026-08-24; the bundle at `48aa1b5` (12 files) was generated under the amended rule with its header naming this entry as pending.

Interim generation procedure:

~~~
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
 "- File set: docs/global-context/*.md by order, then the fixed decision-layer spine, then every skills/*.md whose audience includes all-roles or chief-of-staff (rule; DEC-<ID>).\n"]
o+=["  %d. %s (blob %s)"%(i,p,blob(p)) for i,p in enumerate(files,1)]; o.append("")
for i,p in enumerate(files,1):
    o+=["",bar,"<!-- FILE %d/%d: %s @ %s -->"%(i,N,p,blob(p)),bar,"",open(p,encoding="utf-8").read().rstrip("\n"),""]
dest=os.path.expanduser("~/code/methodology-context-bundle-%s.md"%stamp)
open(dest,"w",encoding="utf-8").write("\n".join(o)+"\n")
print("WROTE",dest,"| source",repo[:7],"| files",N)
'
fi
~~~

Then upload the written file to each project's Context and delete the prior bundle.
Supersedes: DEC-000140

INSTRUCTION 2 — in OPEN-ITEMS.md, in the section headed "`bin/cycle-open` and the retirement of Track", append this paragraph as the section's last paragraph, verbatim:

**Landing precondition, recorded 2026-08-24:** `specs/directive-tooling.md` AC-DT-16 (agreed at `06e5d110`) makes two acts preconditions on the landing that migrates the cycle mode from `bin/cycle-open` to `bin/directive`: a new `decisions/log.md` entry superseding DEC-000180 and re-anchoring its tooling consequence on `bin/directive`'s cycle mode, and the rewrite of this section's guard to name that binary. Both fall to the decision session that lands the migration, not to the implementer, and neither is done before it.

Also update the "Last updated:" line near the top of OPEN-ITEMS.md to 2026-08-24.

INSTRUCTION 3 — Core rule 13 sweep, run as a report. `git grep -n "DEC-000140"` and `git grep -n "context-sets/base.md\|context-sets/collab-workflow.md"` over the worktree. Any hit outside decisions/log.md and OPEN-ITEMS.md is reported with path:line, labelled *observed*, and NOT edited; the Do-not below wins and the decision session disposes of the hits.

INSTRUCTION 4 — gates. Before your edits, on the untouched worktree: `bin/tests/run 2>&1 | tee "$TMPDIR/tests-baseline-decision-log-bundle-spine.txt"` and record the final count line. After your edits: `bin/check-frontmatter --all 2>&1 | tee "$TMPDIR/frontmatter-decision-log-bundle-spine.txt"` (expected exit 0) and `bin/tests/run 2>&1 | tee "$TMPDIR/tests-after-decision-log-bundle-spine.txt"`. The accepted failure set is whatever the baseline run produced on the reviewed ref; report both count lines and STOP if they differ.

INSTRUCTION 5 — commit and push. Two commits on `decision-log-bundle-spine`: one for decisions/log.md ("decisions: DEC-<ID> supersedes DEC-000140 — bundle spine amended"), one for OPEN-ITEMS.md ("OPEN-ITEMS: record AC-DT-16 landing precondition on the Track guard"). Push the branch (no -u). Read the head back with ls-remote. Do not open a pull request, do not merge, never use gh, never force-push.

DO NOT: edit any file other than decisions/log.md, OPEN-ITEMS.md, and the directive file this session landed; edit or reorder any existing decision-log entry; touch any other branch or worktree; run `git worktree remove` or `prune`.

REPORT, in this order, each claim labelled observed/inferred/told/unknown: directive path and landed SHA; the entry ID assigned and the last-entry ID it followed; the three commit SHAs and the branch head by ls-remote; sweep hits (path:line) or "none"; frontmatter exit status; both test count lines; anything you could not do as written.
