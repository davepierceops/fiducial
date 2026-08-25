You are an execution session for davepierceops/fiducial. Read this whole block before acting.

FIRST ACT — land this directive.
Working-tree disposition: EXCLUSIVE ASSIGNMENT. Create and use only this tree:
~~~
cd /Users/dave/code/fiducial && git fetch origin rule-extraction-pass1 && git worktree add --no-track "$TMPDIR/rule-dedup-pass2" origin/rule-extraction-pass1 && cd "$TMPDIR/rule-dedup-pass2" && git checkout -b rule-dedup-pass2
~~~
Write this entire block, verbatim, to docs/cycles/rule-dedup-pass2-20260825T1600.md. Commit with message "docs/cycles: land rule-dedup-pass2 directive". Push with `git push origin rule-dedup-pass2`. Verify with `git ls-remote origin rule-dedup-pass2`. Report "landed <path> as <sha>" using the SHA read back from git. Keychain noise ("failed to store: 100001") is not an error; the git exit code is.

REVIEWED REF: 6d2744bef0cb4344d85081eeb41d84b77fb75652 (branch rule-extraction-pass1). The input is docs/rule-register/rule-register-20260825T1435.md at that SHA.
STOP CONDITIONS — stop and report, do not recover:
- `git diff --stat 6d2744b -- docs/rule-register/` is non-empty.
- A file this session did not change moves, HEAD moves, or an index lock appears.
- Any push fails.

TASK — Pass 2 of a corpus deduplication: cluster the 878 rows of the register into groups that state the same rule, and report agreement or divergence within each group. Analysis only. Do not edit any governed file. Do not edit the register.

READ the register in full before clustering. Work from the `rule`, `binds`, `verb`, and `condition` columns first; consult `source` to confirm a match or a divergence, never to find matches by wording — restatements share no words.

CLUSTERING RULES:
- Two rows are the SAME RULE when they bind the same party to the same obligation under the same condition, however worded. Different `binds` values are not the same rule unless one is `all`.
- A cluster has two or more rows. Rows that match nothing are singletons and are not reported.
- Within a cluster, rows AGREE when carrying either one out satisfies the other. They DIVERGE when the obligation, party, or condition differs in a way an agent could act on — stricter/looser, different trigger, different party, different exception. Divergence is the finding that matters; do not resolve it, surface it.
- A cluster where every row is in one file is INTRA-FILE. Report it, but rank it below cross-file clusters.
- A row that is a definition (`verb` = define) clusters only with other definitions of the same term.

OUTPUT — write docs/rule-register/rule-clusters-20260825T1600.md:

~~~
# Rule clusters — Pass 2

Derived artifact. Input: docs/rule-register/rule-register-20260825T1435.md @ 6d2744b. Analysis only; no edits proposed to governed files.

Rows read: 878. Clustered rows: <n>. Clusters: <c> (<d> divergent, <a> agreeing). Cross-file: <x>. Intra-file: <i>.

## Divergent clusters, cross-file, largest first
### C001 — <the rule, ≤12 words>
Rows: R0012 (core.md:12), R0455 (document-metadata-policy.md:88), …
Divergence: <one sentence — what differs and how an agent's behaviour would differ>
Proposed home: <one file, or "unsure">

## Agreeing clusters, cross-file, largest first
### C0nn — <the rule>
Rows: …
Proposed home: <file>

## Intra-file clusters
(same shape, both kinds)
~~~

Proposed home is the file whose audience is widest among the cluster's rows, unless a row already sits in docs/global-context/core.md or decision-layer.md, in which case that file. Where two files have equal claim, write "unsure" — the choice is Dave's.

VERIFY before committing: for the 10 largest clusters, re-read each member row's `source` and confirm the cluster claim holds. For every divergent cluster, confirm the divergence is visible in `source`, not only in the `rule` paraphrase. Report the count of clusters you dissolved or split during verification.

COMMIT AND PUSH: commit with message "docs/rule-register: Pass 2 clusters over 6d2744b". Push with `git push origin rule-dedup-pass2`. Verify with `git ls-remote origin rule-dedup-pass2`.

DO NOT: edit any file other than the two named above; edit the register; open a pull request; merge; delete branches or worktrees.

REPORT, in this order:
1. Directive path and landed SHA.
2. Clusters file path and commit SHA.
3. The summary line from the file header.
4. The five divergent clusters you judge most consequential: id, rule, one-line divergence.
5. Clusters dissolved or split during verification: count and ids.
6. Rows you could not place because the register row was itself wrong (paraphrase not matching source): ids and why.
Label every claim in the report observed, inferred, told, or unknown.
