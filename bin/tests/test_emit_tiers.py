"""The tier map, `bin/rulestore/emit/tiers.json` (R0259, DEC-001270): one
file the emitters read, never a row. The claude-code column names Claude
Code's aliases; the codex column names the verified installed model ids;
every role with an agent file has a tier.
"""

from __future__ import annotations

import json
import unittest

from rulestore.emit import TIERS_PATH, EmitError, load_tiers
from rulestore.emit import TIER_NAMES
from tests.helpers import temp_dir


class TestTierMap(unittest.TestCase):
    def test_the_committed_map_loads_and_names_claude_codes_aliases(self):
        tiers = load_tiers()
        self.assertEqual(tiers["harnesses"]["claude-code"],
                         {"frontier": "opus", "solid": "sonnet", "cheap": "haiku"})

    def test_the_codex_column_names_the_verified_installed_models(self):
        column = load_tiers()["harnesses"]["codex"]
        self.assertEqual(sorted(column), sorted(TIER_NAMES))
        self.assertEqual(column, {"frontier": "gpt-6-astra",
                                  "solid": "gpt-6.1-sol", "cheap": "gpt-6-luna"})

    def test_every_role_maps_to_a_tier(self):
        roles = load_tiers()["roles"]
        self.assertEqual(sorted(roles), [
            "architect-agent", "coder-agent", "context-quality-reviewer",
            "release-manager-agent", "reviewer-agent", "skeptic-risk-agent",
            "spec-reviewer-agent", "test-designer-agent"])
        for role, tier in roles.items():
            self.assertIn(tier, TIER_NAMES, role)

    def test_no_row_names_a_model_only_the_map_does(self):
        """The map is the one place a model name lives; the store speaks in
        tiers (R0264's criterion, carried by store-lint)."""
        text = TIERS_PATH.read_text(encoding="utf-8")
        for alias in ("opus", "sonnet", "haiku"):
            self.assertIn(alias, text)

    def test_a_column_missing_a_tier_is_refused(self):
        path = temp_dir(self, "tiers-") / "tiers.json"
        path.write_text(json.dumps({"harnesses": {"x": {"frontier": "a"}}, "roles": {}}))
        with self.assertRaises(EmitError) as caught:
            load_tiers(path)
        self.assertIn("solid", str(caught.exception))

    def test_a_role_with_an_unknown_tier_is_refused(self):
        path = temp_dir(self, "tiers-") / "tiers.json"
        path.write_text(json.dumps({"harnesses": {}, "roles": {"coder-agent": "huge"}}))
        with self.assertRaises(EmitError):
            load_tiers(path)


if __name__ == "__main__":
    unittest.main()
