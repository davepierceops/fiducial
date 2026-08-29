"""The TRD's own testable decisions, and the four questions it does not decide.

Contract: `specs/directive-tooling-trd.md` §3.1 (the `invariants.py` split),
§3.3 (marker syntax), §3.4 (Q9), §7 (exit statuses and diagnostic codes), §8
(required integration points), §9 (OQ-Q2, OQ-Q4, OQ-Q5, OQ-Q6).

Tests blocked on the four questions the PRD routes to Dave are written to the
TRD's recommendation and **skipped with a reason naming the question**, so the
suite is honest about what a ruling would change rather than silently encoding
one. AC-DT-16 binds the decision session and not code, so it is represented the
way §3.9 step 5 and §7 direct — as waiting on a decision, not as a red test.
"""

from __future__ import annotations

import pathlib
import unittest

from tests.helpers import (
    BIN_DIR,
    CLI_MINIMAL_ARGS,
    CLI_NAMES,
    DISPOSITION_LABEL,
    INVARIANTS_RELPATH,
    REPO_ROOT,
    base_env,
    bracket_codes,
    citation_fixtures,
    directive_fixture,
    invariants_doc,
    invariants_sections,
    make_home_repo,
    make_repo,
    no_traceback,
    read,
    run_dt,
    temp_dir,
    write,
)
from tests.test_directive import (
    TIMESTAMP,
    unfenced_labelled_statements,
)

SKIP_Q2 = (
    "PRD §8 Q2 (lint sequencing on the failing path) is open; TRD OQ-Q2 "
    "recommends (b), the directive lands and the work does not. Nothing in the "
    "tool depends on the answer, so this test asserts a session procedure, not "
    "a tool property."
)
SKIP_Q4 = (
    "PRD §8 Q4 (where these tools' requirements live) is open; TRD OQ-Q4 "
    "recommends (c), the invariants document is the home and "
    "`skills/directive-authoring.md` gains a path pointer to it. Under (a) or "
    "(b) this assertion is wrong rather than merely unmet."
)
SKIP_Q5 = (
    "PRD §8 Q5 (route and model: unchecked set only, or emitted) is open; TRD "
    "OQ-Q5 recommends (c), emit into a committed region and do not check. "
    "Under (a) the ROUTE AND MODEL region does not exist; under (b) a ninth "
    "element does, and the TRD does not stand."
)
SKIP_Q6 = (
    "PRD §8 Q6 (one exit status, or a blocking/advisory split) is open; TRD "
    "OQ-Q6 recommends (b), the existing five-code contract with refusals at 2 "
    "and findings at 1. Under (a) every non-zero collapses to 1; under (c) "
    "AC-DT-10 needs amending."
)
SKIP_AC_DT_16 = (
    "AC-DT-16 binds the decision session, not the implementer: the migration "
    "does not land until `decisions/log.md` carries an entry superseding "
    "DEC-000180 whose tooling consequence names `bin/directive`'s cycle mode, "
    "and `OPEN-ITEMS.md`'s `bin/cycle-open` section names the cycle mode as "
    "the bearer of that obligation. TRD §3.9 step 5 and §7 direct a release "
    "gate to read this as waiting on a decision, not as red."
)


class TrdTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home_repo(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        self.citations = citation_fixtures(self.repo, env=self.env)
        self.reviewed_ref = self.citations["last"]

    def generate(self, *args):
        return run_dt("directive", *args, cwd=self.repo, env=self.env)

    def lint(self, *args, cwd=None):
        return run_dt("check-directive", *args, cwd=cwd or self.repo, env=self.env)

    def fixture(self, **kwargs):
        kwargs.setdefault("reviewed_ref", self.reviewed_ref)
        kwargs.setdefault("companion_sha", self.citations["touching"])
        return directive_fixture(self.repo, **kwargs)

    def assert_lint_passes(self, rc, out, err, *elements):
        """Exit 0 **and** a report naming a result for each element (G9).

        Never exit 0 alone: a silent pass is what G9 puts under "Not accepted",
        and asserting only the status lets a silent stub clear the test.
        """
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(rc, 0, "expected exit 0; stdout=%r stderr=%r" % (out, err))
        for element in elements or ("M1", "M3", "M5", "M6"):
            self.assertIn(
                element, out, "exit 0 stated no result for %s; stdout=%r" % (element, out)
            )


class TestSingleSourceLabel(TrdTestCase):
    """Q9's property: the generator and the lint source the label from one place.

    §3.1 makes this structural rather than conventional by putting the label in
    one committed file read by one module. The test that proves it is
    behavioural: change the definition, and *both* binaries follow.
    """

    ALT_LABEL = "TREE ASSIGNMENT"

    def _redefine_label(self):
        sections = invariants_sections()
        overrides = {
            name: body.replace(DISPOSITION_LABEL, self.ALT_LABEL)
            for name, body in sections.items()
            if DISPOSITION_LABEL in body
        }
        self.assertTrue(overrides, "the fixture document does not define the label")
        invariants_doc(
            self.home, overrides=overrides, env=self.env, message="redefine the label"
        )

    def test_q9_the_generator_emits_the_label_the_committed_definition_fixes(self):
        self._redefine_label()
        rc, out, err = self.generate(
            "--descriptor", "q9", "--title", "T", "--timestamp", TIMESTAMP
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "%s:" % self.ALT_LABEL, out, "the generator held its own copy of the label"
        )
        self.assertNotIn("%s:" % DISPOSITION_LABEL, out)

    def test_q9_the_lint_matches_the_label_the_committed_definition_fixes(self):
        self._redefine_label()
        relpath = self.fixture(
            replace={
                "disposition": (
                    '%s (exclusive assignment): work only in a worktree at "wt/q9",\n'
                    'created by: git worktree add "wt/q9" main\n' % self.ALT_LABEL
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(
            rc, 0, "the lint held its own copy of the label; stdout=%r stderr=%r" % (out, err)
        )
        self.assertIn("M3", out, "exit 0 stated no result for M3 (G9)")

    def test_q9_the_old_label_stops_matching_once_the_definition_changes(self):
        self._redefine_label()
        relpath = self.fixture()
        rc, out, err = self.lint(relpath)
        self.assertNotEqual(
            rc, 0, "the lint still matched the superseded label; stdout=%r" % out
        )
        self.assertIn("disposition-absent", bracket_codes(out + err))

    def test_q9_the_generators_output_satisfies_the_lint_by_construction(self):
        """§3.1: the sharing is the mechanism, not an economy.

        Whatever the label is, a generated skeleton carries exactly one unfenced
        labelled statement under it — J2's construction (§2).
        """
        self._redefine_label()
        rc, out, err = self.generate(
            "--descriptor", "q9", "--title", "T", "--timestamp", TIMESTAMP
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        hits = unfenced_labelled_statements(out, label=self.ALT_LABEL)
        self.assertEqual(len(hits), 1, "emitted %d labelled statements" % len(hits))


class TestMarkerSyntax(TrdTestCase):
    """§3.3's marker syntax, as the lint applies it (M5's ordering, M6's token)."""

    def test_a_lowercase_run_is_not_a_marker(self):
        """Only ATX headings and all-caps runs are markers, so a lowercase line
        before the first-act statement does not trip M5's ordering rule."""
        relpath = self.fixture(
            replace={
                "route": (
                    "ROUTE AND MODEL\n\nRoute: fresh\nModel: Opus 5\n\n"
                    "some lowercase context the author put first\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err, "M5")

    def test_a_two_character_caps_run_is_not_a_marker(self):
        """§3.3: three or more characters."""
        relpath = self.fixture(
            replace={
                "route": "ROUTE AND MODEL\n\nRoute: fresh\nModel: Opus 5\n\nNB: a note.\n"
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err, "M5")

    def test_an_indented_caps_run_is_not_a_marker(self):
        """§3.3: a marker is a line **at column 0**."""
        relpath = self.fixture(
            replace={
                "report": (
                    "REPORT\n\n- the directive file's commit SHA\n"
                    "- anything observed this directive did not anticipate\n"
                    "\n  NESTED HEADING\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err, "M6")

    def test_an_atx_heading_is_a_marker(self):
        """The heading arm exists so cycle mode's AC-CO-3 headings are markers."""
        relpath = self.fixture(
            replace={
                "report": (
                    "### Report\n\n- the directive file's commit SHA\n"
                    "- anything observed this directive did not anticipate\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err, "M6")


class TestMarkerManifestPartition(TrdTestCase):
    """§3.3's uniqueness/partition invariant is the generator's, not the lint's.

    G11: "the manifest is an output of the generator and an input to nothing the
    lint does." A directive carrying no manifest at all must still pass the lint.
    """

    def test_the_lint_does_not_require_a_source_manifest(self):
        relpath = self.fixture()
        self.assertNotIn(
            "SOURCE MANIFEST", read(self.repo, relpath), "the fixture must carry no manifest"
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err)

    def test_the_lint_reads_no_manifest_to_decide_m5s_ordering(self):
        """§3.6 M5: "the lint reads no manifest to check the ordering"."""
        relpath = self.fixture(
            extra="SOURCE MANIFEST\n\nFIRST ACT — a fabricated entry, author region\n"
        )
        rc, out, err = self.lint(relpath)
        self.assert_lint_passes(rc, out, err, "M5")


class TestInvariantsDocumentIsGovernedText(TrdTestCase):
    """§4.2's B1 — represented as a fixture copy plus one live-verified read."""

    def test_b1_the_real_invariants_document_shows_the_label_only_inside_fences(self):
        """Live-verified against the committed document (§4.2, B1).

        Red until migration step 1 lands `skills/directive-invariants.md`; the
        TRD names that landing as the migration's first, with no code changes.
        """
        path = REPO_ROOT / INVARIANTS_RELPATH
        self.assertTrue(
            path.is_file(),
            "%s is not committed; TRD §3.9 step 1 lands it before any code"
            % INVARIANTS_RELPATH,
        )
        hits = unfenced_labelled_statements(path.read_text())
        self.assertEqual(
            hits, [], "the committed invariants document carries the label unfenced"
        )

    def test_b1_the_real_invariants_document_carries_every_named_section(self):
        """§3.3's tables name each region's source section by heading."""
        path = REPO_ROOT / INVARIANTS_RELPATH
        self.assertTrue(path.is_file(), "%s is not committed" % INVARIANTS_RELPATH)
        body = path.read_text()
        missing = [
            name for name in invariants_sections() if ("## %s" % name) not in body
        ]
        self.assertEqual(missing, [], "sections absent from the committed document")


class TestRequiredIntegrationPoints(TrdTestCase):
    """§8's integration points, and §4.1's substrate change.

    These are deliberately red rather than made green here: adding the two
    binaries to `CLI_NAMES` before they exist would redden AC-X-1 through
    AC-X-7, which are existing green tests. The implementer lands the helpers
    change with the binary (TRD §3.9 steps 1-2).
    """

    def test_both_tools_are_covered_by_the_cross_cutting_criteria(self):
        for name in ("directive", "check-directive"):
            with self.subTest(cli=name):
                self.assertIn(
                    name,
                    CLI_NAMES,
                    "%s is not in CLI_NAMES, so AC-X-1..X-7 do not cover it" % name,
                )
                self.assertIn(name, CLI_MINIMAL_ARGS)

    def test_both_binaries_exist_and_support_help(self):
        """AC-X-3's shape, for the two new tools."""
        for name in ("directive", "check-directive"):
            with self.subTest(cli=name):
                self.assertTrue(
                    (BIN_DIR / name).is_file(), "bin/%s does not exist" % name
                )
                rc, out, err = run_dt(name, "--help", cwd=self.repo, env=self.env)
                self.assertEqual(rc, 0, "%s --help: stderr=%r" % (name, err))
                self.assertIn("usage", (out + err).lower())


class TestExitStatusContract(TrdTestCase):
    """§7's exit table. Blocked on Q6 — written to OQ-Q6's recommendation (b)."""

    @unittest.skip(SKIP_Q6)
    def test_q6_the_lint_uses_one_for_findings_and_two_for_refusals(self):
        relpath = self.fixture(omit="M3")
        rc, out, err = self.lint(relpath)
        self.assertEqual(rc, 1, "a finding is exit 1; stdout=%r stderr=%r" % (out, err))

        outside = temp_dir(self, "aimeta-outside-")
        target = outside / "elsewhere-20260828T170000.md"
        target.write_text("# Elsewhere\n")
        rc, out, err = self.lint(str(target))
        self.assertEqual(rc, 2, "a refused invocation is exit 2")

    @unittest.skip(SKIP_Q6)
    def test_q6_an_undecidable_element_exits_one_not_zero(self):
        """AC-DT-10 under (b): unknown is a finding, never an advisory pass."""
        relpath = self.fixture(
            replace={
                "base-verification": (
                    "BASE VERIFICATION\n\nPinned to the reviewed ref %s.\n"
                    % self.citations["unresolvable"]
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assertEqual(rc, 1, "stdout=%r stderr=%r" % (out, err))

    @unittest.skip(SKIP_Q6)
    def test_q6_the_generator_uses_two_for_usage_and_three_for_preconditions(self):
        rc, out, err = self.generate("--title", "T")
        self.assertEqual(rc, 2, "the selector rule is a usage error")
        invariants_doc(
            self.home, drop=("Sandbox constraints",), env=self.env, message="drop"
        )
        rc, out, err = self.generate(
            "--descriptor", "x", "--title", "T", "--timestamp", TIMESTAMP
        )
        self.assertEqual(rc, 3, "a precondition refusal is exit 3")


class TestOpenQuestions(TrdTestCase):
    """Q2, Q4, Q5 — written to the TRD's recommendation, skipped with the reason."""

    @unittest.skip(SKIP_Q2)
    def test_q2_a_failing_lint_still_leaves_the_directive_landable(self):
        """OQ-Q2 (b): the directive lands, the work does not.

        The tool cannot tell whether a commit has happened (AC-DT-19), so the
        only tool-side property is that the verdict is the same either way —
        which `test_check_directive.py` asserts unconditionally. This test
        stands for the session procedure a ruling would fix.
        """
        relpath = self.fixture(omit="M3")
        before = self.lint(relpath)
        from tests.helpers import commit

        commit(self.repo, "land the malformed directive", env=self.env)
        after = self.lint(relpath)
        self.assertEqual(before[0], after[0])

    @unittest.skip(SKIP_Q4)
    def test_q4_the_authoring_skill_points_at_the_invariants_document(self):
        """OQ-Q4 (c): the skill's delegation sentence gains a path pointer."""
        body = (REPO_ROOT / "skills" / "directive-authoring.md").read_text()
        self.assertIn(
            INVARIANTS_RELPATH,
            body,
            "the skill delegates the label's form to tooling without naming where "
            "(F-3's residue, OQ-8)",
        )

    @unittest.skip(SKIP_Q5)
    def test_q5_route_and_model_are_substituted_into_a_committed_region(self):
        """OQ-Q5 (c): values inside a committed region, not a third author slot."""
        from tests.test_directive import parse_manifest

        rc, out, err = self.generate(
            "--descriptor", "q5", "--title", "T", "--timestamp", TIMESTAMP,
            "--route", "fresh", "--model", "Opus 5",
        )
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("Route: fresh", out)
        self.assertIn("Model: Opus 5", out)
        entries = dict(parse_manifest(out))
        self.assertIn("ROUTE AND MODEL", entries)
        self.assertEqual(
            entries["ROUTE AND MODEL"][0],
            "committed",
            "route and model became a third author region, breaking AC-DT-18's two",
        )

    @unittest.skip(SKIP_Q5)
    def test_q5_the_element_set_stays_at_eight(self):
        """OQ-Q5 (c): no ninth element checks route and model."""
        rc, out, err = self.lint(self.fixture())
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertNotIn("M9", out)


class TestDecisionSessionGate(unittest.TestCase):
    """AC-DT-16 — represented as the TRD directs, not as a red test."""

    @unittest.skip(SKIP_AC_DT_16)
    def test_ac_dt_16_the_superseding_decision_and_the_open_item_are_recorded(self):
        log = (REPO_ROOT / "decisions" / "log.md").read_text()
        self.assertIn("DEC-000180", log)
        self.assertIn("bin/directive", log)
        open_items = (REPO_ROOT / "OPEN-ITEMS.md").read_text()
        self.assertIn("cycle-open", open_items)
        self.assertIn("cycle mode", open_items)


if __name__ == "__main__":
    unittest.main()
