"""#398: every `retired:` value names something that exists.

`bin/tests/reconcile_sort.py` holds the shape check (`RETIRED_VALUE_RE`) but
is a one-off script, not part of this suite, and exits non-zero by design.
This module is the suite's check. A `retired:` value is either a row id or a
decision id:

- a row id must name a row under `rules/` or `rules/retired/`;
- a decision id must have a `## DEC-NNNNNN` heading in `decisions/log.md`;
- a chain of retired rows (a retired row whose successor is itself retired)
  must end at a live row or at an existing decision, and must not loop.

The checker is `retired_target_problems(root)`. The class over the real
store is the regression guard (B3); the class over synthetic stores proves
the checker refuses a missing target and a cycle (B1, B2) without touching
the real store.
"""

from __future__ import annotations

import pathlib
import re
import unittest

from tests.helpers import REPO_ROOT, temp_dir, write

#: AC-RS-10: a `retired:` value is a successor row id or a decision id.
RETIRED_VALUE_RE = re.compile(r"^(R\d{4}[ab]?|DEC-\d{6})$")
DECISION_HEADING_RE = re.compile(r"^## (DEC-\d{6})\b", re.M)


def _frontmatter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, raw = line.partition(":")
            fields[key.strip()] = raw.strip()
    return fields


def retired_target_problems(root):
    """Every problem with a retired row's `retired:` target under `root`."""
    root = pathlib.Path(root)
    live = {p.stem for p in (root / "rules").glob("*.md")}
    retired = {}
    for path in sorted((root / "rules" / "retired").glob("*.md")):
        retired[path.stem] = _frontmatter(path.read_text(encoding="utf-8")).get("retired")
    log = root / "decisions" / "log.md"
    decisions = set(DECISION_HEADING_RE.findall(log.read_text(encoding="utf-8"))) if log.is_file() else set()

    problems = []
    for row_id, value in sorted(retired.items()):
        if not value:
            problems.append("%s: retired row carries no retired: value" % row_id)
            continue
        if not RETIRED_VALUE_RE.match(value):
            problems.append("%s: retired: %s is neither a row id nor a decision id" % (row_id, value))
            continue
        seen = [row_id]
        target = value
        while True:
            if target.startswith("DEC-"):
                if target not in decisions:
                    problems.append("%s: retired: %s names a decision that is not in decisions/log.md"
                                    % (row_id, target))
                break
            if target in live:
                break
            if target not in retired:
                problems.append("%s: retired: %s names a row present under neither rules/ nor rules/retired/"
                                % (row_id, target))
                break
            if target in seen:
                problems.append("%s: retired: chain loops %s" % (row_id, " -> ".join(seen + [target])))
                break
            seen.append(target)
            nxt = retired[target]
            if not nxt or not RETIRED_VALUE_RE.match(nxt):
                problems.append("%s: retired: chain through %s has no valid retired: value" % (row_id, target))
                break
            target = nxt
    return problems


def _row(row_id, retired=None):
    lines = ["---", "id: %s" % row_id]
    if retired:
        lines.append("retired: %s" % retired)
    lines += ["topic: [core]", "order: 10", "verb: require", "---", "", "Body of %s." % row_id, ""]
    return "\n".join(lines)


def _log(*decision_ids):
    return "# Decision log\n\n" + "".join("## %s — a decision\n\nText.\n\n" % d for d in decision_ids)


class SyntheticStoreCase(unittest.TestCase):
    def store(self, live=(), retired=(), decisions=("DEC-000010",)):
        root = temp_dir(self, "retired-targets-")
        for row_id in live:
            write(root, "rules/%s.md" % row_id, _row(row_id))
        for row_id, target in retired:
            write(root, "rules/retired/%s.md" % row_id, _row(row_id, target))
        write(root, "decisions/log.md", _log(*decisions))
        return root


class TestRetiredTargetsOnSyntheticStores(SyntheticStoreCase):
    def test_b1_a_row_id_target_present_under_rules_passes(self):
        root = self.store(live=["R0001"], retired=[("R0002", "R0001")])
        self.assertEqual(retired_target_problems(root), [])

    def test_b1_a_decision_target_present_in_the_log_passes(self):
        root = self.store(retired=[("R0002", "DEC-000010")])
        self.assertEqual(retired_target_problems(root), [])

    def test_b1_a_missing_row_target_fails_naming_the_row_and_the_target(self):
        root = self.store(live=["R0001"], retired=[("R0002", "R0777")])
        problems = retired_target_problems(root)
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("R0002", problems[0])
        self.assertIn("R0777", problems[0])

    def test_b1_a_missing_decision_target_fails_naming_the_row_and_the_target(self):
        root = self.store(retired=[("R0002", "DEC-009999")])
        problems = retired_target_problems(root)
        self.assertEqual(len(problems), 1, problems)
        self.assertIn("R0002", problems[0])
        self.assertIn("DEC-009999", problems[0])

    def test_b1_a_decision_is_found_by_its_heading_not_by_a_mention(self):
        root = self.store(retired=[("R0002", "DEC-000555")])
        write(root, "decisions/log.md", _log("DEC-000010") + "See DEC-000555 for why.\n")
        self.assertEqual(len(retired_target_problems(root)), 1)

    def test_b2_a_chain_ending_at_a_live_row_passes(self):
        root = self.store(live=["R0001"], retired=[("R0002", "R0003"), ("R0003", "R0001")])
        self.assertEqual(retired_target_problems(root), [])

    def test_b2_a_chain_ending_at_an_existing_decision_passes(self):
        root = self.store(retired=[("R0002", "R0003"), ("R0003", "DEC-000010")])
        self.assertEqual(retired_target_problems(root), [])

    def test_b2_a_chain_ending_at_a_missing_decision_fails(self):
        root = self.store(retired=[("R0002", "R0003"), ("R0003", "DEC-009999")])
        problems = retired_target_problems(root)
        self.assertTrue(any("R0003" in p and "DEC-009999" in p for p in problems), problems)

    def test_b2_a_cycle_fails(self):
        root = self.store(retired=[("R0002", "R0003"), ("R0003", "R0002")])
        problems = retired_target_problems(root)
        self.assertTrue(problems)
        self.assertTrue(any("R0002" in p and "R0003" in p for p in problems), problems)

    def test_b2_a_self_loop_fails(self):
        root = self.store(retired=[("R0002", "R0002")])
        self.assertTrue(retired_target_problems(root))


class TestRetiredTargetsOnTheRealStore(unittest.TestCase):
    def test_b3_every_retired_target_in_the_real_store_exists(self):
        self.assertEqual(retired_target_problems(REPO_ROOT), [])

    def test_b3_the_r1283_chain_ends_at_a_decision(self):
        """R1283 -> R1608 -> decision is the one retired-to-retired chain the
        issue names; the checker must walk it, not skip it."""
        retired = REPO_ROOT / "rules" / "retired"
        first = _frontmatter((retired / "R1283.md").read_text(encoding="utf-8"))["retired"]
        self.assertEqual(first, "R1608")
        second = _frontmatter((retired / "R1608.md").read_text(encoding="utf-8"))["retired"]
        self.assertRegex(second, r"^DEC-\d{6}$")
        self.assertIn(second, DECISION_HEADING_RE.findall(
            (REPO_ROOT / "decisions" / "log.md").read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
