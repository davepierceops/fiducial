#!/usr/bin/env python3
"""Reconcile `rules/` against the ruled sort table (subtraction plan, package 1a).

Reads the per-topic tables of `docs/research/sort-table-20261103.md` (the
ruled sort; the "Classes for ruling" section is the superseded proposal and is
not read) and the working tree, and reports per row: the ruled sort, where the
file is, its `enforce:` / `retired:` state, and match or mismatch. Where a
decision-log entry overrides the table (DEC-001150 through DEC-001460), the
entry governs; every override is listed in `DEC_OVERRIDES` with its entry.

Checks, each fatal on failure (exit 1):

- every row sorted `retired` is under `rules/retired/` with a `retired:` line
  naming the successor `RETIRED_SUCCESSOR` records — one id, a surviving row
  id where the table or the entry names one, else the governing DEC id
  (AC-RS-10) — placed directly after `id:`, the only line added over base;
- every row sorted `harness:<x>` is under `rules/` with `enforce: <x>`
  (R1408: `hook`, DEC-001230 and plan §1a) and differs from the base only by
  that line;
- every row sorted `stays` is under `rules/` with neither key, byte-identical
  to the base unless its topic retired, in which case it carries the topic
  `RETOPIC` maps it to and differs from the base only by `topic:`/`order:`;
- every row sorted `out-of-scope` is byte-identical to the base;
- no row deleted: every id in the table, and every row file at the base, is
  present under `rules/` or `rules/retired/`, and no id is in both;
- the store loads (`FileRowSource`), so the schema admits what landed;
- the merges DEC-001310 rules without naming a survivor (`DEFERRED_MERGES`)
  are listed, not applied: their rows are checked as `stays`.

Also prints the row count for `role=chief-of-staff session=decision`, read
through `bin/rulestore`'s own query code (package 3 needs it).

Usage: `bin/tests/reconcile_sort.py [--base 28366d4] [--root <repo>]`.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rulestore import named_queries  # noqa: E402
from rulestore import query  # noqa: E402
from rulestore.store import ENFORCE_VALUES, FileRowSource, RowShapeError  # noqa: E402

TABLE = "docs/research/sort-table-20261103.md"
DEFAULT_BASE = "28366d4"
ROW_RE = re.compile(r"^\|\s*(R\d{4}[ab]?)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|")
ID_RE = re.compile(r"^R\d{4}[ab]?$")
#: AC-RS-10: a `retired:` value is a successor row id or a decision id.
RETIRED_VALUE_RE = re.compile(r"^(R\d{4}[ab]?|DEC-\d{6})$")

#: Topics whose process document retires; survivors move (plan §1a).
RETOPIC = {
    "directive-invariants": "chief-of-staff",
    "convergence": "change-flow",
    "trd": "spec",
    "prd-template": "spec",
}

#: Where a decision-log entry and the table differ, the entry governs
#: (plan §1a). `sort` is the ruled sort; `enforce` the value for a harness row.
DEC_OVERRIDES = {
    # DEC-001310: one survivor per duplicate pair; the other retires.
    "R0489": {"sort": "retired", "dec": "DEC-001310"},
    "R0022": {"sort": "retired", "dec": "DEC-001310"},
    "R0023": {"sort": "retired", "dec": "DEC-001310"},
    "R0024": {"sort": "retired", "dec": "DEC-001310"},
    "R0025": {"sort": "retired", "dec": "DEC-001310"},
    "R0026": {"sort": "retired", "dec": "DEC-001310"},
    "R0113": {"sort": "retired", "dec": "DEC-001310"},
    "R1602": {"sort": "retired", "dec": "DEC-001310"},
    "R1153": {"sort": "retired", "dec": "DEC-001310"},
    "R1543": {"sort": "retired", "dec": "DEC-001310"},
    # DEC-001230 and plan §1a: a path deny cannot tell an existing reviews/
    # file from a new one, so R1408 is a hook.
    "R1408": {"sort": "harness:hook", "dec": "DEC-001230"},
}

#: DEC-001310's merges name no surviving id, so no file moves here: each row
#: is checked as its ruled sort (`stays`, re-topiced where its topic retired)
#: and the merge — body and the loser's move — is package 1b's and the
#: decision session's. Printed in the summary so the deferral is visible.
DEFERRED_MERGES = (
    "R1533 + R0472 + R0759 -> one row about the spec (DEC-001310)",
    "R1513 + R1542 -> one row about an approved SPEC.md (DEC-001310)",
)

#: Every retired row's `retired:` value and where it comes from. A row sorted
#: `retired` (after overrides) must be here, and nothing else may be. One id
#: per row: the surviving row the table's note or the entry names, else the
#: DEC id that retired it (review F-1; AC-RS-10).
RETIRED_SUCCESSOR = {
    'R0561': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0757': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0758': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0871': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R1541': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0872': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0046': ('DEC-001210', 'DEC-001210 (into process/spec-template.md)'),
    'R0470': ('DEC-001190', 'DEC-001190 (table: SPEC.md definition of done)'),
    'R0474': ('R0007', 'table: R0007 + subagents; class 3 DEC-001180'),
    'R0483': ('R0862b', 'table: plan mode + R0862b; class 4 DEC-001190'),
    'R0489': ('R1031', 'DEC-001310: R0489 retires (R1031 is now an agent description)'),
    'R0896': ('R0229', 'table: subagents; R0229 covers pasted output; class 3 DEC-001180'),
    'R1613': ('DEC-001260', 'DEC-001260 (no successor)'),
    'R1468': ('R0017', 'table: R0017 + R0083; class 4 DEC-001190'),
    'R1476': ('DEC-001180', 'DEC-001180 (subagents)'),
    'R1490': ('R0009', 'DEC-001200; table'),
    'R1491': ('DEC-001200', 'DEC-001200 (no successor; table said R0570/R1206)'),
    'R1602': ('R0006', 'DEC-001310'),
    'R0202': ('DEC-001330', 'DEC-001330 (no successor)'),
    'R0212': ('R0208', 'table: R0208 execution block + SPEC.md; class 1 DEC-001160'),
    'R0256': ('DEC-001160', 'DEC-001160 (class 1; restated under command-blocks)'),
    'R0060': ('DEC-001160', 'DEC-001160 (class 1; restated under command-blocks)'),
    'R1302': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1304': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1305': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1306': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1307': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1308': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1310': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1311': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1312': ('R0259', 'table; class 1 DEC-001160'),
    'R1313': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1314': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1340': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1341': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1344': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1347': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1350': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1286': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1287': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1288': ('DEC-001160', 'DEC-001160 (class 1; table: PreToolUse path guard)'),
    'R1289': ('DEC-001160', 'DEC-001160 (class 1; table: PreToolUse path guard allow-list)'),
    'R1290': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1291': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1292': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1293': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R1295': ('DEC-001170', 'DEC-001170 (harness-managed subagent worktrees)'),
    'R1296': ('DEC-001170', 'DEC-001170 (harness-managed subagent worktrees; table said none)'),
    'R1298': ('R1202', 'table; class 1 DEC-001160'),
    'R1608': ('DEC-001160', 'DEC-001160 (class 1; table: subagents and --resume)'),
    'R1610': ('R1048', 'table; class 1 DEC-001160'),
    'R1615': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R0003': ('DEC-001200', 'DEC-001200 (no successor)'),
    'R0008': ('DEC-001200', 'DEC-001200 (no successor)'),
    'R0012': ('DEC-001200', 'DEC-001200 (no successor)'),
    'R0013': ('DEC-001200', 'DEC-001200 (no successor)'),
    'R0054': ('DEC-001370', 'DEC-001370 (no successor)'),
    'R0058': ('DEC-001160', 'DEC-001160 (class 1; table: none)'),
    'R0022': ('R0131', 'DEC-001310'),
    'R0023': ('R0133', 'DEC-001310'),
    'R0024': ('R0135', 'DEC-001310'),
    'R0025': ('R0137', 'DEC-001310'),
    'R0026': ('R0139', 'DEC-001310'),
    'R0113': ('R0485', 'DEC-001310'),
    'R1153': ('R0017', 'DEC-001310'),
    'R1543': ('R0876', 'DEC-001310'),
    'R1246': ('DEC-001260', 'DEC-001260 (no successor; table said the retro skill)'),
    'R1395a': ('R1396', 'table: subagents; R1396; class 3 DEC-001180'),
    'R1395b': ('R1614', 'table: subagents; R1614; class 3 DEC-001180'),
    'R1101': ('R1107', 'table; class 4 DEC-001190'),
    'R1106': ('R1107', 'table: subagents; R1107; class 3 DEC-001180'),
    'R1126': ('R0083', 'table: SPEC.md definition of done + R0083 + R1396; class 4 DEC-001190'),
    'R1158': ('R0083', 'table; class 4 DEC-001190'),
    'R0085': ('DEC-001190', 'DEC-001190 (table: SPEC.md design section)'),
    'R0086': ('R0862b', 'table; class 4 DEC-001190'),
}


# ------------------------------------------------------------------ reading


def read_table(root):
    """`{id: (sort, note)}` from the per-topic tables, in table order."""
    text = (root / TABLE).read_text(encoding="utf-8")
    rows = {}
    in_tables = False
    for line in text.splitlines():
        if line.startswith("## Per-topic tables"):
            in_tables = True
            continue
        if line.startswith("## Classes for ruling"):
            break
        if not in_tables:
            continue
        match = ROW_RE.match(line)
        if not match:
            continue
        row_id = match.group(1)
        if row_id in rows:
            raise SystemExit("table lists %s twice" % row_id)
        rows[row_id] = (match.group(3).strip(), match.group(4).strip())
    return rows


def git_show(root, ref, relpath):
    proc = subprocess.run(
        ["git", "show", "%s:%s" % (ref, relpath)],
        cwd=str(root), capture_output=True,
    )
    return proc.stdout if proc.returncode == 0 else None


def base_row_paths(root, ref):
    """Every `rules/**/R*.md` path at `ref`."""
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "rules/"],
        cwd=str(root), capture_output=True, text=True, check=True,
    )
    return sorted(p for p in proc.stdout.splitlines() if p.endswith(".md"))


def frontmatter(data):
    """`{key: raw value}` of a row file's frontmatter, keys in file order."""
    lines = data.decode("utf-8").splitlines()
    fields = {}
    if not lines or lines[0].strip() != "---":
        return fields
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, raw = line.partition(":")
            fields[key.strip()] = raw.strip()
    return fields


def diff_lines(base, now):
    """`(removed, added)` line lists between two byte strings."""
    import difflib

    a = base.decode("utf-8").splitlines()
    b = now.decode("utf-8").splitlines()
    removed, added = [], []
    for line in difflib.unified_diff(a, b, lineterm="", n=0):
        if line.startswith(("---", "+++", "@@")):
            continue
        if line.startswith("-"):
            removed.append(line[1:])
        elif line.startswith("+"):
            added.append(line[1:])
    return removed, added


def frontmatter_span(data):
    """Line indexes `(open, close)` of the frontmatter fences, or None."""
    lines = data.decode("utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return 0, index
    return None


def only_added_key(base, now, key):
    """True when `now` is `base` plus exactly one `<key>:` line, and that line
    sits directly after `id:` — line 2 of the file, inside the frontmatter."""
    removed, added = diff_lines(base, now)
    if removed or len(added) != 1 or not added[0].startswith(key + ":"):
        return False
    lines = now.decode("utf-8").splitlines()
    return (
        len(lines) > 2
        and lines[0].strip() == "---"
        and lines[1].startswith("id:")
        and lines[2] == added[0]
        and base.decode("utf-8").splitlines()[2:] == lines[3:]
    )


def only_changed_keys(base, now, keys):
    """True when every changed line is a frontmatter line on one of `keys`,
    and the frontmatter is the only region that changed."""
    removed, added = diff_lines(base, now)
    allowed = tuple(k + ":" for k in keys)
    span = frontmatter_span(now)
    if span is None:
        return False
    lines = now.decode("utf-8").splitlines()
    base_lines = base.decode("utf-8").splitlines()
    base_span = frontmatter_span(base)
    if base_span is None or base_lines[base_span[1]:] != lines[span[1]:]:
        return False
    return (
        all(line.startswith(allowed) for line in removed)
        and all(line.startswith(allowed) for line in added)
        and len(removed) == len(added)
    )


# ------------------------------------------------------------------- checks


def reconcile(root, base):
    table = read_table(root)
    problems = []
    lines = []
    counts = {"retired": 0, "retopiced": 0, "untouched": 0, "out-of-scope": 0}
    enforce_counts = {value: 0 for value in ENFORCE_VALUES}
    base_paths = base_row_paths(root, base)
    base_ids = {pathlib.Path(p).stem: p for p in base_paths}
    orders_by_topic = {}

    def note(row_id, ruled, location, state, verdict, why=""):
        lines.append("%-7s %-14s %-22s %-40s %s%s" % (
            row_id, ruled, location, state, verdict, (" — " + why) if why else ""))
        if verdict != "match":
            problems.append("%s: %s" % (row_id, why or verdict))

    for row_id, (table_sort, table_note) in table.items():
        ruled = table_sort
        override = DEC_OVERRIDES.get(row_id)
        if override:
            ruled = override["sort"]
        live = root / "rules" / ("%s.md" % row_id)
        retired = root / "rules" / "retired" / ("%s.md" % row_id)
        if live.is_file() and retired.is_file():
            note(row_id, ruled, "both", "", "mismatch", "present under rules/ and rules/retired/")
            continue
        if not live.is_file() and not retired.is_file():
            note(row_id, ruled, "missing", "", "mismatch", "row deleted")
            continue
        path = live if live.is_file() else retired
        location = "rules/retired/" if path == retired else "rules/"
        now = path.read_bytes()
        fields = frontmatter(now)
        state = []
        if "enforce" in fields:
            state.append("enforce: %s" % fields["enforce"])
        if "retired" in fields:
            state.append("retired: %s" % fields["retired"])
        state_text = "; ".join(state) or "-"
        base_path = base_ids.get(row_id)
        base_bytes = git_show(root, base, base_path) if base_path else None
        if base_bytes is None:
            note(row_id, ruled, location, state_text, "mismatch", "no row file at %s" % base)
            continue
        if base_path.startswith("rules/retired/"):
            # Retired before this package; not the table's concern beyond presence.
            if location != "rules/retired/" or now != base_bytes:
                note(row_id, ruled, location, state_text, "mismatch", "pre-retired row changed")
            else:
                note(row_id, ruled, location, state_text, "match", "retired before base")
            continue

        if ruled == "retired":
            expected = RETIRED_SUCCESSOR.get(row_id)
            if expected is None:
                note(row_id, ruled, location, state_text, "mismatch", "no successor recorded in RETIRED_SUCCESSOR")
            elif location != "rules/retired/":
                note(row_id, ruled, location, state_text, "mismatch", "not under rules/retired/")
            elif fields.get("retired") != expected[0]:
                note(row_id, ruled, location, state_text, "mismatch",
                     "retired: should be %r (%s)" % (expected[0], expected[1]))
            elif not RETIRED_VALUE_RE.match(fields["retired"]):
                note(row_id, ruled, location, state_text, "mismatch",
                     "retired: is neither a row id nor a DEC id (AC-RS-10)")
            elif not only_added_key(base_bytes, now, "retired"):
                note(row_id, ruled, location, state_text, "mismatch", "differs from base beyond the retired: line")
            else:
                counts["retired"] += 1
                note(row_id, ruled, location, state_text, "match", expected[1])
            continue

        if row_id in RETIRED_SUCCESSOR:
            note(row_id, ruled, location, state_text, "mismatch", "RETIRED_SUCCESSOR names a row not sorted retired")
            continue
        if location != "rules/":
            note(row_id, ruled, location, state_text, "mismatch", "retired but sorted %s" % ruled)
            continue

        if ruled.startswith("harness:"):
            value = ruled.split(":", 1)[1]
            if value not in ENFORCE_VALUES:
                note(row_id, ruled, location, state_text, "mismatch", "sort names no enforce value")
            elif fields.get("enforce") != value:
                note(row_id, ruled, location, state_text, "mismatch", "enforce: should be %s" % value)
            elif not only_added_key(base_bytes, now, "enforce"):
                note(row_id, ruled, location, state_text, "mismatch", "differs from base beyond the enforce: line")
            else:
                enforce_counts[value] += 1
                note(row_id, ruled, location, state_text, "match",
                     override["dec"] if override else "")
            continue

        if ruled == "out-of-scope":
            if now != base_bytes:
                note(row_id, ruled, location, state_text, "mismatch", "not byte-identical to %s" % base)
            else:
                counts["out-of-scope"] += 1
                note(row_id, ruled, location, state_text, "match", "byte-identical to %s" % base)
            continue

        if ruled == "stays":
            if "enforce" in fields or "retired" in fields:
                note(row_id, ruled, location, state_text, "mismatch", "a stays row carries enforce:/retired:")
                continue
            base_topic = frontmatter(base_bytes).get("topic", "").strip("[]").strip()
            target = RETOPIC.get(base_topic)
            if target is None:
                if now != base_bytes:
                    note(row_id, ruled, location, state_text, "mismatch", "stays row changed")
                else:
                    counts["untouched"] += 1
                    note(row_id, ruled, location, state_text, "match", "untouched")
                continue
            topic_now = fields.get("topic", "").strip("[]").strip()
            if topic_now != target:
                note(row_id, ruled, location, state_text, "mismatch",
                     "topic should be %s (was %s)" % (target, base_topic))
            elif not only_changed_keys(base_bytes, now, ("topic", "order")):
                note(row_id, ruled, location, state_text, "mismatch", "differs from base beyond topic:/order:")
            else:
                counts["retopiced"] += 1
                order = fields.get("order")
                orders_by_topic.setdefault(target, {}).setdefault(order, []).append(row_id)
                note(row_id, ruled, location, "topic: %s; order: %s" % (target, order), "match",
                     "re-topiced from %s" % base_topic)
            continue

        note(row_id, ruled, location, state_text, "mismatch", "unknown sort %r" % ruled)

    # Order collisions inside the receiving topics, against every live row there.
    for target in sorted(set(RETOPIC.values())):
        seen = {}
        for path in sorted((root / "rules").glob("R*.md")):
            f = frontmatter(path.read_bytes())
            if f.get("topic", "").strip("[]").strip() == target:
                seen.setdefault(f.get("order"), []).append(path.stem)
        for order, ids in sorted(seen.items(), key=lambda kv: str(kv[0])):
            if len(ids) > 1:
                problems.append("%s: order %s shared by %s" % (target, order, ", ".join(ids)))

    # No deletion against the base, and no id in both places.
    present = {p.stem for p in (root / "rules").glob("R*.md")}
    present_retired = {p.stem for p in (root / "rules" / "retired").glob("R*.md")}
    for row_id in sorted(base_ids):
        if row_id not in present and row_id not in present_retired:
            problems.append("%s: at %s but deleted from the tree" % (row_id, base))
    for row_id in sorted(present & present_retired):
        problems.append("%s: under rules/ and rules/retired/" % row_id)
    for row_id in sorted(present | present_retired):
        if row_id not in table and row_id not in base_ids:
            problems.append("%s: in the tree but in neither the table nor %s" % (row_id, base))
    for row_id in sorted(RETIRED_SUCCESSOR):
        if row_id not in table:
            problems.append("%s: RETIRED_SUCCESSOR names an id the table lacks" % row_id)
    for path in sorted((root / "rules").glob("R*.md")):
        if "retired" in frontmatter(path.read_bytes()):
            problems.append("%s: retired: under rules/" % path.stem)
    for path in sorted((root / "rules" / "retired").glob("R*.md")):
        value = frontmatter(path.read_bytes()).get("retired")
        if value is None or not RETIRED_VALUE_RE.match(value):
            problems.append("%s: retired: %r is neither a row id nor a DEC id (AC-RS-10)" % (path.stem, value))
    for expected, _source in RETIRED_SUCCESSOR.values():
        if not RETIRED_VALUE_RE.match(expected):
            problems.append("RETIRED_SUCCESSOR carries a non-id value %r" % expected)

    # The store loads, and the count package 3 needs.
    cos_count = None
    try:
        source = FileRowSource(root)
        rows = source.rows()
        sequences = named_queries.sequences(source.named_queries_text())
        selected = query.select(rows, {"role": "chief-of-staff", "session": "decision"}, sequences)
        cos_count = len(selected)
    except RowShapeError as error:
        problems.append("store does not load: %s" % error)

    return table, lines, problems, counts, enforce_counts, cos_count, base_ids


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--base", default=DEFAULT_BASE, help="the commit out-of-scope rows must match")
    parser.add_argument("--root", default=None, help="repository root (default: this script's)")
    parser.add_argument("--quiet", action="store_true", help="summary and mismatches only")
    args = parser.parse_args(argv)
    root = pathlib.Path(args.root) if args.root else pathlib.Path(__file__).resolve().parents[2]

    table, lines, problems, counts, enforce_counts, cos_count, base_ids = reconcile(root, args.base)

    print("reconcile_sort: %s against %s at base %s" % (TABLE, root, args.base))
    print("%-7s %-14s %-22s %-40s %s" % ("id", "ruled sort", "location", "state", "verdict"))
    for line in lines:
        if not args.quiet or "mismatch" in line:
            print(line)
    print()
    print("summary")
    print("  table rows:            %d" % len(table))
    print("  row files at base:     %d (%d live, %d retired)" % (
        len(base_ids),
        sum(1 for p in base_ids.values() if not p.startswith("rules/retired/")),
        sum(1 for p in base_ids.values() if p.startswith("rules/retired/"))))
    print("  retired (this package): %d" % counts["retired"])
    for value in ENFORCE_VALUES:
        print("  enforce: %-6s         %d" % (value, enforce_counts[value]))
    print("  enforce total:          %d" % sum(enforce_counts.values()))
    print("  re-topiced:             %d" % counts["retopiced"])
    print("  stays, untouched:       %d" % counts["untouched"])
    print("  out-of-scope, identical:%d" % counts["out-of-scope"])
    for merge in DEFERRED_MERGES:
        print("  deferred merge (1b):    %s" % merge)
    live_now = len(list((root / "rules").glob("R*.md")))
    retired_now = len(list((root / "rules" / "retired").glob("R*.md")))
    print("  rows now:               %d live, %d retired" % (live_now, retired_now))
    print("  role=chief-of-staff session=decision: %s rows" % (
        cos_count if cos_count is not None else "store did not load"))
    print("  mismatches:             %d" % len(problems))
    for problem in problems:
        print("  MISMATCH " + problem)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
