#!/usr/bin/env python3
"""Pass 4 mechanical shortlist over the rule store.

Reads every row under rules/, normalizes each row's body text together with its
`condition` key, and emits every same-verb pair whose token-set Jaccard >= 0.35
or whose difflib SequenceMatcher ratio >= 0.55 to
docs/rule-register/store-near-candidates-20260906T070000Z.md.

The Pass 3b shortlist (docs/rule-register/shortlist.py) read the register's
table; this reads the store's own rows, and reports only pairs whose two rows
sit in different topics — the cross-topic sweep of store fix pass 4 item 9.
Each pair carries the two rows' role lists and whether they intersect, because
the item's test is whether any role's query loads both.

Python 3 standard library only. No network. Deterministic.
"""

import difflib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RULES = os.path.join(ROOT, "rules")
CANDIDATES = os.path.join(HERE, "store-near-candidates-20260906T070000Z.md")

J_THRESHOLD = 0.35
R_THRESHOLD = 0.55

# Stated stopword list, unchanged from docs/rule-register/shortlist.py.
STOPWORDS = frozenset("""
a an the this that these those there here
is are was were be been being am
do does did done doing
have has had having
of in on at to for from by with without within into onto upon over under
and or but nor so yet if then else than as
it its it's they them their theirs he she his her him hers
we us our ours you your yours i my mine
not no never any all each every some such other others another
which who whom whose what when where while whether why how
must shall should may might can could will would
one two both same only just also more most less least very
per via across about after before during until unless once
any-of no-op
""".split())

WORD_RE = re.compile(r"[^a-z0-9]+")
LIST_RE = re.compile(r"^\[(.*)\]$")


def normalize(rule, condition):
    """Lowercase, strip punctuation, collapse whitespace, drop stopwords."""
    raw = (rule or "") + " " + (condition or "")
    raw = raw.lower()
    raw = WORD_RE.sub(" ", raw)
    tokens = [t for t in raw.split() if t and t not in STOPWORDS]
    return tokens


def parse_row(path):
    """Split a row file into its frontmatter mapping and its body."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---\n"):
        sys.exit("no frontmatter: %s" % path)
    _, front, rest = text.split("---\n", 2)
    keys = {}
    for line in front.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        k, _, v = line.partition(": ")
        keys[k.strip()] = v.strip()
    body = rest.split("\n## Human", 1)[0].strip()
    return keys, body


def listval(raw):
    if raw is None or raw == "null":
        return []
    m = LIST_RE.match(raw)
    if not m:
        return [raw]
    return [x.strip() for x in m.group(1).split(",") if x.strip()]


def load_rows():
    rows = []
    for name in sorted(os.listdir(RULES)):
        if not name.endswith(".md"):
            continue
        keys, body = parse_row(os.path.join(RULES, name))
        cond = keys.get("condition", "null")
        rows.append(
            {
                "id": keys.get("id", name[:-3]),
                "topic": (listval(keys.get("topic")) or ["?"])[0],
                "verb": keys.get("verb", "?"),
                "roles": frozenset(listval(keys.get("role"))),
                "condition": "" if cond in (None, "null") else cond,
                "rule": " ".join(body.split()),
            }
        )
    return rows


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def main():
    rows = load_rows()
    for r in rows:
        toks = normalize(r["rule"], r["condition"])
        r["tokens"] = frozenset(toks)
        r["norm"] = " ".join(toks)

    by_verb = {}
    for r in rows:
        by_verb.setdefault(r["verb"], []).append(r)

    pairs = []
    for verb in sorted(by_verb):
        group = by_verb[verb]
        sm = difflib.SequenceMatcher(autojunk=False)
        for i in range(len(group)):
            a = group[i]
            sm.set_seq2(a["norm"])
            ta = a["tokens"]
            for j in range(i + 1, len(group)):
                b = group[j]
                if a["topic"] == b["topic"]:
                    continue
                tb = b["tokens"]
                union = len(ta | tb)
                jac = (len(ta & tb) / union) if union else 0.0
                if jac >= J_THRESHOLD:
                    sm.set_seq1(b["norm"])
                    ratio = sm.ratio()
                else:
                    sm.set_seq1(b["norm"])
                    if sm.real_quick_ratio() < R_THRESHOLD:
                        continue
                    if sm.quick_ratio() < R_THRESHOLD:
                        continue
                    ratio = sm.ratio()
                    if ratio < R_THRESHOLD:
                        continue
                pairs.append((a, b, jac, ratio))

    pairs.sort(key=lambda p: (-max(p[2], p[3]), p[0]["id"], p[1]["id"]))

    with open(CANDIDATES, "w", encoding="utf-8") as out:
        out.write("# Store near-pairs — store fix pass 4 item 9\n\n")
        out.write(
            "Derived artifact. Input: every row under `rules/` on branch "
            "`store-fix-4`, read before item 9 applied its retirements. "
            "Generated by "
            "`docs/rule-register/store-near-20260906T070000Z.py`; Python 3 "
            "standard library only, no network, deterministic. Analysis only.\n\n"
        )
        out.write(
            "Thresholds: token-set Jaccard >= %.2f OR difflib SequenceMatcher "
            "ratio >= %.2f, over the normalized text (body + condition, "
            "lowercased, punctuation stripped, whitespace collapsed, stopwords "
            "removed, `## Human` excluded). Stopword list length: %d. Pairs are "
            "same-verb and cross-topic only. Rows read: %d. Pairs emitted: "
            "%d.\n\n" % (J_THRESHOLD, R_THRESHOLD, len(STOPWORDS), len(rows), len(pairs))
        )
        out.write(
            "`roles meet` is whether the two rows' `role` lists intersect — "
            "whether any role's query loads both. A `define` row carries no "
            "`role` key: it is pulled by term, so a define pair always meets.\n\n"
        )
        out.write(
            "| pair | id A | id B | topic A | topic B | verb | jaccard | ratio "
            "| roles meet | rule A | rule B |\n"
        )
        out.write("|---|---|---|---|---|---|---|---|---|---|---|\n")
        for n, (a, b, jac, ratio) in enumerate(pairs, 1):
            if a["verb"] == "define":
                meet = "define"
            else:
                meet = "yes" if (a["roles"] & b["roles"]) else "no"
            out.write(
                "| %d | %s | %s | %s | %s | %s | %.3f | %.3f | %s | %s | %s |\n"
                % (
                    n,
                    a["id"],
                    b["id"],
                    a["topic"],
                    b["topic"],
                    a["verb"],
                    jac,
                    ratio,
                    meet,
                    cell(a["rule"]),
                    cell(b["rule"]),
                )
            )

    print("rows: %d" % len(rows))
    print("pairs: %d" % len(pairs))


if __name__ == "__main__":
    main()
