# Bundle tool, follow-up: diff-scoped re-read of the fix

ROUTE AND MODEL

Route: fresh
Model: frontier

FIRST ACT

Write this directive verbatim to docs/cycles/bundle-tool-followup-reread-20260907T210000Z.md, commit it alone with a
message naming the package it opens, push the branch bundle-tool-followup-reread to origin with a plain push
(git push origin bundle-tool-followup-reread — never with -u), and report the SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

```text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
```

Both admitted forms, worked:

```text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
```

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "$TMPDIR/fiducial-bundle-tool-followup-reread", created by:
git worktree add --no-track "$TMPDIR/fiducial-bundle-tool-followup-reread" -b bundle-tool-followup-reread origin/bundle-tool-followup-fix

BASE VERIFICATION

Before anything else, fetch origin/bundle-tool-followup-fix, origin/bundle-tool-followup and
origin/bundle-tool-followup-read, and confirm the base — the branch
bundle-tool-followup-fix — is at the reviewed ref
02722aa76be18b6da00fa163d0b1a3df05ec7eeb, that its parent branch is at
252928b84e19b530b9acc25159a80ab478223848, and that the read branch is at
7a6f3ce5751168946eaa08d4d81c48f447f2479a. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- reviews/bundle-tool-followup-quality-20260907T190000Z.md and
  reviews/bundle-tool-followup-skeptic-20260907T190000Z.md, read from
  origin/bundle-tool-followup-read at 7a6f3ce5751168946eaa08d4d81c48f447f2479a —
  the findings the fix claims to close
- docs/cycles/bundle-tool-followup-fix-20260907T200000Z.md, read from the
  base ref 02722aa76be18b6da00fa163d0b1a3df05ec7eeb — what the Coder was told,
  and the human's ruling on F2 (grouped) it carries
- process/review-artifact.md, read from the base ref
  02722aa76be18b6da00fa163d0b1a3df05ec7eeb
- the diff origin/bundle-tool-followup..origin/bundle-tool-followup-fix
  (252928b84e19b530b9acc25159a80ab478223848..02722aa76be18b6da00fa163d0b1a3df05ec7eeb) — the
  change under review, 11 files in 13 commits, and nothing outside it

TASK

A diff-scoped re-read of the fix, in the same two passes as the read it
answers, both from this session, each its own artifact with its own
verdict. Review the diff from origin/bundle-tool-followup to the base ref;
the rest of the follow-up delta was read at 7a6f3ce5751168946eaa08d4d81c48f447f2479a and
is not re-read here, though you read whatever you need to judge the fix.
Edit nothing under bin/, process/ or decisions/.

For each of F1–F6, S13–S16 and the tenth refusal: closed as the fix
directive states, not closed, or closed with a new defect — and whether
the fix reaches outside its finding. F7 was held and is not a finding here.
Continuity: DEC-000640 as amended against `sort_key` and `_topic_sort_value`
and against process/named-queries.md's prose; the `~~~` fences against the
widened `_FENCE_RE`; the docstring of bin/tests/test_rulestore.py, which still
claims nothing in the module touches the filesystem while the F1 guard test
reads the real process/named-queries.md through `FileRowSource` — say
whether that is a finding or the directive's own doing to be recorded.

PASS 1 — QUALITY (Reviewer): the code review of the diff and the adequacy
of the tests the fix added, then the suite's summary line. Artifact:
reviews/bundle-tool-followup-quality-reread-20260907T210000Z.md.

PASS 2 — SKEPTICISM (Skeptic/Risk): construct, do not read — run
bin/release end-to-end against a purpose-built store repository once clean
and once with README.md edited; give a list entry a name carrying `[` and
a second entry a repeated name; delete process/named-queries.md and run
again; and render the real chief-of-staff bundle in the worktree through
FileRowSource, select and render and confirm the rule band now orders as
DEC-000640 amended states and the process band follows the process
sequence. Artifact:
reviews/bundle-tool-followup-skeptic-reread-20260907T210000Z.md.

Both artifacts follow process/review-artifact.md, scoped to this diff, with
a Verdict per pass; the overall verdict is the more severe. Commits, in
order, pushed after each: the directive (FIRST ACT); the quality artifact;
the skeptic artifact. Nothing else. Do not open a pull request. Remove the
worktree at the end
(`git worktree remove "$TMPDIR/fiducial-bundle-tool-followup-reread"`) and
report that it is gone. If the frontmatter hook fires, stop and report.

Report also carries: both verdicts and the overall; one line per finding
saying closed / not closed / new defect; and one line per blocking finding
if any.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

From the worktree, after the last commit and before removing the worktree:

~~~sh
{
  ls reviews/bundle-tool-followup-*reread*
  grep -h '^Verdict' reviews/bundle-tool-followup-quality-reread-20260907T210000Z.md reviews/bundle-tool-followup-skeptic-reread-20260907T210000Z.md
  bin/tests/run 2>&1 | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup-reread" diff --stat origin/bundle-tool-followup-fix..HEAD | tail -1
  git -C "$TMPDIR/fiducial-bundle-tool-followup-reread" log --oneline origin/bundle-tool-followup-fix..HEAD | wc -l
} 2>&1 | tee "$TMPDIR/bundle-tool-followup-reread-verify.log"
~~~

Expected: two files; four verdict lines; OK from the suite; a diff-stat
touching reviews/ and the directive file only; 3 commits.

STOP CONDITIONS

Pinned to the reviewed ref 02722aa76be18b6da00fa163d0b1a3df05ec7eeb. Cannot execute as written: stop
and report. Concurrent tree mutation: stop and report. On any failed command,
any precondition not met, or any tree mutation you did not intend, including
your own — stop and report; do not retry with different flags, and do not
delete or create any ref to recover. A remote operation that exits successfully
is not a failed command, whatever a credential helper writes to stderr.

REPORT

- the directive file's commit SHA
- every commit SHA this session landed, in order, and the branch they are on
- what was verified, how, and where the run log is
- every count reported, with the tree it was observed in — the clone's main
  tree, or the worktree the directive assigns; a sandboxed run says so
- anything observed this directive did not anticipate
- the worktree-removal status — or, under the sole-tree form, that no worktree
  existed

CLAIM LABELS

Label every claim observed, inferred, told, or unknown.

SOURCE MANIFEST

One entry per emitted region, in emission order: the marker that begins the
region, and either the committed path it was read from at the revision named
or an author-region marking.

    Bundle tool, follow-up: diff-scoped re-read of the fix — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    ROUTE AND MODEL — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    FIRST ACT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    DISPOSITION PROMPT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    WORKING-TREE DISPOSITION — author region
    BASE VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    COMPANIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    TASK — author region
    SANDBOX — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    VERIFICATION — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    STOP CONDITIONS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    REPORT — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    CLAIM LABELS — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
    SOURCE MANIFEST — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
