# Tagging package — sre-critic rename, outline audience, role order

ROUTE AND MODEL

Route: fresh execution session
Model: cheap

FIRST ACT

Create the worktree named in the disposition below first. Then, in that worktree, write this directive verbatim to docs/cycles/tagging-package-20260903T203000Z.md, commit it alone with a
message naming the package it opens, push with git push origin tagging-package-20260903 (no -u), verify by git ls-remote origin tagging-package-20260903, and report the
SHA. Do this before reading anything else and before touching any other file.

DISPOSITION PROMPT

A working-tree disposition is required, and it is stated below as its own
labelled statement. The governed rule it answers to:

~~~text
**Every directive states its working-tree disposition** — either an exclusive
assignment (a named directory plus the command creating it) or an explicit
sole-tree declaration. A prohibition is not a disposition. The disposition is
stated as its own labelled statement, exactly one per directive, mechanically
distinguishable from incidental mention of trees or commands elsewhere in the
file; the label's fixed form, the canonical sole-tree sentence, and a worked
example of each form are stated in the Directive Invariants document, which is
their one definition. Two sessions sharing a tree mutate each other's
preconditions; prefer not splitting work across trees.
~~~

Both admitted forms, worked:

~~~text
WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a
worktree at "wt/<name>", created by: git worktree add --no-track "wt/<name>" -b
<name> origin/main

WORKING-TREE DISPOSITION: This session works in the sole tree at the clone root.
~~~

WORKING-TREE DISPOSITION (exclusive assignment): this session works only in a worktree at "$TMPDIR/fiducial-tagging-package-20260903", created by: git worktree add --no-track "$TMPDIR/fiducial-tagging-package-20260903" -b tagging-package-20260903 origin/main

Before creating it, run git fetch origin, then git worktree list; if any worktree holds branch tagging-package-20260903, if a branch of that name already exists locally or on origin (git ls-remote origin tagging-package-20260903 returns a ref), or if "$TMPDIR/fiducial-tagging-package-20260903" already exists, stop and report. Entries git marks prunable are not yours; ignore them. Do not touch the main tree except for the final worktree removal.

BASE VERIFICATION

Before anything else, fetch and confirm the base is at the reviewed ref
83ca3bc201de730dfd876aae30a642cb4cb2b8f2. Judge every remote operation — fetch, push, ls-remote — by
the refs it reports, not by a credential helper's noise on stderr. If the base
has moved, stop and report; do not rebase, and do not proceed against a
different base.

COMPANIONS

Read these whole, from the working tree, at the revision each names, before
writing anything:

- specs/bundle-system.md @ 4d6373a6d73e44023fdc86961e1d49a36eb0b342 — §5 (the tagging package, "Tag" step; the critic-collision paragraph near "engagements/critic.md, an execution role") and AC-BS-4.
- decisions/log.md @ 9cca04849c14d3f49a8ff0e171932e7590073158 — DEC-000340 and DEC-000350, the two rulings this package lands.
- reviews/bundle-system-cycle-1.md @ 42636f35f4407ffacc37626ab8f0240fb0c70740 — O-4, the order: observation.
- policies/document-metadata-policy.md @ dda60a262c6eb775632ae5fefcf18fbe02d9add5 — audience and order fields; the revision-lifecycle rule (content edits flip status; frontmatter edits do not).
- engagements/critic.md @ 13e8c64d07f648528dfd5e3cede6220c3fb78cd8
- engagements/working-with-dave.md @ 209de669a3424e77bc7fe7cfb17939192e9960df
- engagements/sre/README.md @ b1baf1702668523b98f4c519e423c60a8e38a74f
- engagements/sre/speed-audit.md @ cf8b1610d10588fdb0dbab197f3d4a4c958a2f9a
- engagements/sre/override-log-policy.md @ e2dffaa9562c6661341980c0d866de9317c55c35
- engagements/sre/engagement-change-package.md @ 6fcbfb9ad041628c3db24dcca115254e7fa74654
- skills/review-artifact.md @ 7b52f6ba0e50f6987993fc29e465dbab6e8d25b8
- roles/critic.md @ ba86076ae8e022e0b48287321c15afa4ed83a931
- roles/copy-editor.md @ ddab9072aa9ac4b4ae365f04f50faa76088a4126
- skills/outline.md @ 68662ce55e16df3f75433d8705d543855a29802f

TASK

This package lands three rulings already logged; it decides nothing. Every edit is frontmatter-only or a rename: no document body changes. The pre-commit hook flips agreed → in-review on body edits only (bin/check-frontmatter compares the body at HEAD to the staged body; a frontmatter-only edit passes with no flip — observed by the decision session in a sandbox clone at the base ref). So every touched document stays agreed and no re-agreement cycle is owed. If the hook flips any file in this package, stop and report: that means a body changed, which this package forbids.

One content commit after the directive's own commit, touching exactly the files named below and nothing else. Edit frontmatter values in place; do not reorder, add, or remove any other key.

Edit A — DEC-000350, the sre-critic rename and retags.
1. git mv engagements/critic.md engagements/sre-critic.md. Basename only; the file stays under engagements/ (not engagements/sre/). Its body, including its H1 "# Role: Critic", is untouched — the heading is not the role slug; whether it should read SRE Critic is a rider for that document's next cycle, not this package.
2. In engagements/sre-critic.md, audience: [critic, human] becomes audience: [sre-critic, human].
3. In each of these five files, replace the value critic with sre-critic in place, keeping list position and every other value:
   - engagements/working-with-dave.md
   - engagements/sre/README.md
   - engagements/sre/speed-audit.md
   - engagements/sre/override-log-policy.md
   - engagements/sre/engagement-change-package.md
4. skills/review-artifact.md: replace critic with sre-critic in place. The engagement's critic is the role that writes review artifacts (engagements/sre-critic.md's body names the review-artifact schema); AC-BS-4 rules the writing Critic's bundle carries no skill. Inferred by the decision session from those two facts; Dave was told before this directive was handed over.
Untouched by design: roles/critic.md, public-prose-criteria.md, and voice.md keep critic — that value is now the writing Critic's alone.

Edit B — DEC-000340. skills/outline.md: audience: [writer, human] becomes audience: [writer].

Edit C — cycle-1 O-4. roles/critic.md and roles/copy-editor.md each gain the line order: 10, inserted immediately after the audience: line, matching roles/writer.md's value and key position. The two roles never share a bundle, so the equal value never ties.

Verification, in the worktree, each captured to a named file under "$TMPDIR/" with the tagging-package-20260903 prefix, each stated with its exit status and labelled observed:
1. bin/check-frontmatter --all — exit 0; and confirm no FLIPPED line appeared in the hook output of the content commit.
2. bin/tests/run — the full suite passes (611 tests, 9 skipped at the base ref, observed by the decision session; report your counts).
3. bin/bundle --list — contains sre-critic; contains critic exactly once.
4. bin/bundle --audience critic — the Files: header lists no path under engagements/ and not skills/review-artifact.md; lists roles/critic.md before public-prose-criteria.md. State the file count.
5. bin/bundle --audience sre-critic — the Files: header lists engagements/sre-critic.md, the five retagged engagement files, and skills/review-artifact.md. State the file count.
6. bin/bundle --audience copy-editor — roles/copy-editor.md appears before public-prose-criteria.md.
7. bin/bundle --audience human — skills/outline.md absent.
8. git diff --stat 83ca3bc201de730dfd876aae30a642cb4cb2b8f2..HEAD — exactly eleven paths: this directive, the rename (shown as a rename, similarity 100%), and the nine edited files; no other path.
A bundle count differing from AC-BS-4's five-file sets is expected — the selection build that retires the all-roles floor from writing bundles has not landed; this package fixes tags and order only. Report counts, do not judge them against AC-BS-4.

Push with git push origin tagging-package-20260903 (no -u) and verify by git ls-remote origin tagging-package-20260903: the tip must be the content commit. No pull request: the decision session opens it.

CLEANUP — after the report is composed and the push is verified landed: from the main tree, run git worktree remove "$TMPDIR/fiducial-tagging-package-20260903" (no --force). If it fails, report the failure; do not retry. Your report's final line states whether the worktree was removed.

SANDBOX

Commands run inside the sandbox. `gh` cannot reach the GitHub API from here,
so a directive that wants a pull request gets a pushed branch and a report line
saying so, and the decision session opens it. No credential ever enters a file
or stdout.

VERIFICATION

Run the verification this directive names, from the working tree it assigns
you, with the output captured to a file. State each result and the log's path.
A step you did not run is reported as not run, never as passed.

STOP CONDITIONS

Pinned to the reviewed ref 83ca3bc201de730dfd876aae30a642cb4cb2b8f2. Cannot execute as written: stop
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

    Tagging package — sre-critic rename, outline audience, role order — skills/directive-invariants.md @ 4c9cd22b01d3387bbc4d62e20a7d26bc5e0ab035
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
