You are an execution session for davepierceops/fiducial. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin main && git worktree add --no-track "$TMPDIR/rule-extraction-pass1" origin/main && cd "$TMPDIR/rule-extraction-pass1" && git checkout -b rule-extraction-pass1
~~~
Write this entire block, verbatim, to docs/cycles/rule-extraction-pass1-20260825T1435.md. Commit it with message "docs/cycles: land rule-extraction-pass1 directive". Push with `git push origin rule-extraction-pass1`. Verify with `git ls-remote origin rule-extraction-pass1`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: f9a7a5e8b4c695e8aa52549e180dae277da94a28.
STOP CONDITIONS — stop and report, do not recover:
- Any in-scope file below differs from its content at f9a7a5e (check with `git diff --stat f9a7a5e -- <paths>`; must be empty).
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — Pass 1 of a corpus deduplication: extract every rule in the governed corpus into one table. Extraction only. No merging, no judgment about duplicates, no edits to any governed file.

IN SCOPE (read from the tree, not from memory):
- docs/global-context/*.md
- LEXICON.md
- operating-model.md
- context-sets/*.md
- boundaries/*.md
- policies/*.md
- roles/*.md (top level only; not roles/*/ subdirectories)
- skills/*.md
OUT OF SCOPE: specs/, engagements/, reviews/, retros/, docs/cycles/, docs/packages/, bin/, everything else.

WHAT A RULE IS: one sentence or clause that binds an agent or a human to do, not do, or do-under-condition something. Definitions in LEXICON.md count as rules (binds: all; verb: define). Rationale, examples, and context do not count. When a sentence carries two obligations, emit two rows. When unsure whether something is a rule, emit it and set `binds` to `unsure`.

OUTPUT — write docs/rule-register/rule-register-20260825T1435.md with this exact shape:

~~~
# Rule register — Pass 1 extraction

Derived artifact. Source: davepierceops/fiducial @ f9a7a5e8b4c695e8aa52549e180dae277da94a28. Extraction only; no deduplication performed.

Files read: <N>. Rows: <M>.

| id | file | line | binds | verb | rule | condition | source |
|---|---|---|---|---|---|---|---|
| R0001 | docs/global-context/core.md | 12 | all | forbid | secret values entering context | — | "Secret values never enter context." |
~~~

Column rules:
- id: R + four digits, sequential in file order then line order.
- file: repo-relative path.
- line: line number of the source sentence in that file at f9a7a5e.
- binds: one of `all`, `decision`, `execution`, `dave`, a role slug from the file's own frontmatter or heading (e.g. `chief-of-staff`, `coder-agent`), or `unsure`.
- verb: one of `require`, `forbid`, `define`, `escalate`, `stop`.
- rule: the obligation restated in ≤12 plain words, present tense, no file names, no rationale.
- condition: the triggering condition in ≤12 words, or `—`.
- source: the verbatim sentence, in double quotes, pipes escaped as `\|`.

Work file by file in the order listed under IN SCOPE (alphabetical within each group). Do not skip a file because it looks like it has no rules; a file with no rules gets no rows and is still counted in "Files read".

VERIFY before committing: pick 10 rows at random; confirm each `source` string is present verbatim at the stated file and line. Report the 10 ids and pass/fail for each.

COMMIT AND PUSH: commit the register with message "docs/rule-register: Pass 1 extraction at f9a7a5e". Push with `git push origin rule-extraction-pass1`. Verify with `git ls-remote origin rule-extraction-pass1`.

DO NOT: edit any file other than the two named above; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Register path and commit SHA.
3. Files read: N. Rows: M. Rows with binds=unsure: count.
4. Per-file row counts, one line each.
5. Verification: the 10 sampled ids with pass/fail.
6. Anything you could not extract, with file and line, and why.
Label every claim in the report observed, inferred, told, or unknown.
