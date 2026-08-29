"""AC-DT-06..AC-DT-13, AC-DT-17, AC-DT-19: `bin/check-directive`, the lint.

Contract: `specs/directive-tooling.md` §6 (the agreed acceptance criteria) and
`specs/directive-tooling-trd.md` §3.4, §3.5, §3.6, §7 (the mechanisms).

Written before either binary exists. The suite is proven red on **wrong
behaviour** rather than on an absent module by running it against
`bin/tests/stubs/check-directive`, a stub that always exits 0 silently; see
`bin/tests/red-run-with-stubs.log`.

Two conventions carry through every test here:

- an **exit 0 is never asserted on its status alone**. G9 forbids a silent
  pass, so every passing assertion also reads the per-element report. That is
  what makes the always-exit-0 stub fail these tests rather than clear them.
- **codes, not wording.** Findings are asserted through `bracket_codes`, per
  `helpers.py`'s existing convention and TRD §7's code table.
"""

from __future__ import annotations

import os
import pathlib
import stat
import unittest

from tests.helpers import (
    DISPOSITION_LABEL,
    DT_COMPANION_A,
    DT_COMPANION_B,
    DT_M3_PASSING,
    DT_M3_SHAPES,
    DT_M8_FAILING_NAMES,
    DT_M8_PASSING_NAMES,
    DT_DISPOSITION_STATEMENT,
    SOLE_TREE_SENTENCE,
    base_env,
    bracket_codes,
    citation_fixtures,
    commit,
    directive_fixture,
    disposition_fixture,
    invariants_doc,
    make_home_repo,
    make_repo,
    no_traceback,
    run_dt,
    snapshot_tree,
    temp_dir,
    write,
)

ELEMENTS = ("M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8")

#: PRD §4's judgment-only set plus the two AC-DT-08 names outright. Asserted by
#: keyword rather than by sentence, so rewording the report does not break it.
UNCHECKED_KEYWORDS = (
    "executab",       # executability of the working-tree disposition
    "route",          # route and model tier
    "model",
    "contradict",     # "no blanket constraint may contradict…"
    "blast radius",   # "scope Do-not lists to the blast radius"
    "dictated",       # "carry dictated wording as a pointer…"
    "self-contained",
    "mode",           # mode-appropriateness of the filename
)


class CheckDirectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home_repo(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        self.citations = citation_fixtures(self.repo, env=self.env)
        self.reviewed_ref = self.citations["last"]
        self.companion_sha = self.citations["touching"]

    # ------------------------------------------------------------- invocation

    def lint(self, *args, cwd=None):
        return run_dt("check-directive", *args, cwd=cwd or self.repo, env=self.env)

    def fixture(self, **kwargs):
        kwargs.setdefault("reviewed_ref", self.reviewed_ref)
        kwargs.setdefault("companion_sha", self.companion_sha)
        return directive_fixture(self.repo, **kwargs)

    def shape(self, name, **kwargs):
        kwargs.setdefault("reviewed_ref", self.reviewed_ref)
        kwargs.setdefault("companion_sha", self.companion_sha)
        return disposition_fixture(self.repo, name, **kwargs)

    # ------------------------------------------------------------- assertions

    def assert_pass(self, rc, out, err, elements=ELEMENTS):
        """Exit 0 **and** a report that states a result for each element (G9)."""
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(rc, 0, "expected exit 0; stdout=%r stderr=%r" % (out, err))
        for element in elements:
            self.assertIn(
                element,
                out,
                "exit 0 stated no result for %s; a silent pass is G9's failure "
                "mode. stdout=%r" % (element, out),
            )

    def assert_fails(self, rc, out, err, element, code=None):
        """Non-zero, naming the element, and — where §7 fixes one — its code."""
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertNotEqual(
            rc, 0, "expected a non-zero exit; stdout=%r stderr=%r" % (out, err)
        )
        self.assertIn(
            element, out + err, "the failure named no element; stdout=%r stderr=%r"
            % (out, err),
        )
        if code is not None:
            self.assertIn(
                code,
                bracket_codes(out + err),
                "expected diagnostic [%s] (TRD §7); saw %r"
                % (code, bracket_codes(out + err)),
            )


class TestWellFormedDirective(CheckDirectiveTestCase):
    """AC-DT-07, AC-DT-08, AC-DT-11 — the passing path and the bounds it states."""

    def test_ac_dt_07_a_well_formed_directive_exits_zero(self):
        """AC-DT-07: a fixture carrying every element M1-M8 exits 0."""
        relpath = self.fixture()
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_ac_dt_08_exit_zero_states_the_unchecked_set(self):
        """AC-DT-08: the pass names what it did not check."""
        relpath = self.fixture()
        rc, out, err = self.lint(relpath)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        lowered = out.lower()
        missing = [word for word in UNCHECKED_KEYWORDS if word not in lowered]
        self.assertEqual(
            missing,
            [],
            "exit 0 did not name these unchecked properties: %r; stdout=%r"
            % (missing, out),
        )

    def test_ac_dt_08_the_unchecked_set_is_stated_on_the_failing_path_too(self):
        """G9/AC-DT-08: the report's bounds are stated on both exit paths."""
        relpath = self.fixture(omit="M7")
        rc, out, err = self.lint(relpath)
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        lowered = (out + err).lower()
        missing = [word for word in UNCHECKED_KEYWORDS if word not in lowered]
        self.assertEqual(
            missing, [], "the failing path did not state its bounds: %r" % missing
        )

    def test_ac_dt_11_the_lint_labels_its_claims_observed_or_unknown_only(self):
        """AC-DT-11: two provenance labels, and no other class."""
        relpath = self.fixture()
        rc, out, err = self.lint(relpath)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        lowered = out.lower()
        self.assertIn(
            "observed", lowered, "the lint made no labelled claim at all; stdout=%r" % out
        )
        for forbidden in ("inferred", "told"):
            self.assertNotIn(
                forbidden,
                lowered,
                "the lint used the %r class, which G10 does not admit for its own "
                "claims; stdout=%r" % (forbidden, out),
            )


class TestMissingElements(CheckDirectiveTestCase):
    """AC-DT-06: one fixture per element, missing exactly that element."""

    def test_ac_dt_06_m1_missing_reviewed_ref_pin(self):
        """AC-DT-06/M1: no reviewed-ref pin exits non-zero, naming M1."""
        rc, out, err = self.lint(self.fixture(omit="M1"))
        self.assert_fails(rc, out, err, "M1", "reviewed-ref-missing")

    def test_ac_dt_06_m1_names_the_governed_text_it_derives_from(self):
        """AC-DT-06: the failure cites the governed text (G8)."""
        rc, out, err = self.lint(self.fixture(omit="M1"))
        self.assertIn(
            "directive-authoring",
            (out + err),
            "M1's failure did not cite skills/directive-authoring.md; stdout=%r "
            "stderr=%r" % (out, err),
        )

    def test_ac_dt_06_m2_citation_that_does_not_touch_its_path(self):
        """AC-DT-06/M2: built by corruption, not subtraction — no citation passes M2."""
        relpath = self.fixture(companion_sha=self.citations["non_touching"])
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M2", "citation-not-touching")

    def test_ac_dt_06_m3_no_labelled_disposition_statement(self):
        """AC-DT-06/M3: the motivating incident — a prohibition, no labelled statement."""
        rc, out, err = self.lint(self.fixture(omit="M3"))
        self.assert_fails(rc, out, err, "M3", "disposition-absent")

    def test_ac_dt_06_m4_missing_stop_conditions(self):
        """AC-DT-06/M4: both stop conditions absent exits non-zero."""
        rc, out, err = self.lint(self.fixture(omit="M4"))
        self.assert_fails(rc, out, err, "M4", "stop-condition-missing")

    def test_ac_dt_06_m5_missing_first_act_statement(self):
        """AC-DT-06/M5: no write-commit-push-report-the-SHA statement."""
        rc, out, err = self.lint(self.fixture(omit="M5"))
        self.assert_fails(rc, out, err, "M5", "first-act-missing")

    def test_ac_dt_06_m6_missing_report_section(self):
        """AC-DT-06/M6: no report section exits non-zero."""
        rc, out, err = self.lint(self.fixture(omit="M6"))
        self.assert_fails(rc, out, err, "M6", "report-section-missing")

    def test_ac_dt_06_m6_report_section_present_but_not_enumerated(self):
        """M6 (TRD §3.6): a report section with fewer than two list items fails."""
        relpath = self.fixture(
            replace={"report": "REPORT\n\nReport whatever seems relevant.\n"}
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M6", "report-section-missing")

    def test_ac_dt_06_m7_missing_claim_label_instruction(self):
        """AC-DT-06/M7: no claim-label instruction exits non-zero."""
        rc, out, err = self.lint(self.fixture(omit="M7"))
        self.assert_fails(rc, out, err, "M7", "claim-labels-missing")

    def test_ac_dt_06_m8_filename_matching_no_pattern(self):
        """AC-DT-06/M8: a name matching none of the three patterns exits non-zero."""
        rc, out, err = self.lint(self.fixture(omit="M8"))
        self.assert_fails(rc, out, err, "M8", "filename-unmatched")


class TestM3Shapes(CheckDirectiveTestCase):
    """AC-DT-06's M3 shape set (i)-(vii), plus two-statement and neither/both."""

    def _run(self, shape):
        return self.lint(self.shape(shape))

    def test_ac_dt_06_m3_shape_i_exclusive_assignment_passes(self):
        """(i): one labelled statement, the exclusive-assignment form."""
        rc, out, err = self._run("i-exclusive")
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m3_shape_i_sole_tree_declaration_passes(self):
        """(i): the sole-tree form, which the corpus has zero instances of."""
        rc, out, err = self._run("i-sole-tree")
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m3_shape_ii_unlabelled_prohibition_fails(self):
        """(ii): the motivating incident. A prohibition is not a disposition."""
        rc, out, err = self._run("ii-unlabelled-prohibition")
        self.assert_fails(rc, out, err, "M3", "disposition-absent")

    def test_ac_dt_06_m3_shape_iii_unlabelled_instance_elsewhere_passes(self):
        """(iii): an unlabelled line instantiating a form is incidental mention."""
        rc, out, err = self._run("iii-plus-unlabelled-instance")
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m3_shape_iv_filled_slot_passes(self):
        """(iv): the skeleton's content slot, filled faithfully."""
        rc, out, err = self._run("iv-slot-filled")
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m3_shape_v_blank_slot_fails_on_form_membership(self):
        """(v): a blank slot is a one-line extent carrying neither form (§3.4)."""
        rc, out, err = self._run("v-slot-blank")
        self.assert_fails(rc, out, err, "M3", "disposition-form-absent")

    def test_ac_dt_06_m3_shape_vi_one_unfenced_plus_fenced_passes(self):
        """(vi): carried wording under the origin exception is fenced, so masked."""
        rc, out, err = self._run("vi-unfenced-plus-fenced")
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m3_shape_vii_only_fenced_statement_fails(self):
        """(vii): a fenced-only statement leaves zero unfenced ones."""
        rc, out, err = self._run("vii-only-fenced")
        self.assert_fails(rc, out, err, "M3", "disposition-absent")

    def test_ac_dt_06_m3_two_unfenced_statements_fail(self):
        """Exactly one is the requirement; two is a failure."""
        rc, out, err = self._run("two-unfenced")
        self.assert_fails(rc, out, err, "M3", "disposition-multiple")

    def test_ac_dt_06_m3_one_statement_carrying_neither_form_fails(self):
        """Zero admitted forms fails."""
        rc, out, err = self._run("neither-form")
        self.assert_fails(rc, out, err, "M3", "disposition-form-absent")

    def test_ac_dt_06_m3_one_statement_carrying_both_forms_fails(self):
        """Both admitted forms in one extent fails."""
        rc, out, err = self._run("both-forms")
        self.assert_fails(rc, out, err, "M3", "disposition-form-ambiguous")

    def test_ac_dt_06_m3_shape_set_is_complete(self):
        """Every shape AC-DT-06 enumerates is instantiable and has a fixture."""
        for shape in DT_M3_SHAPES:
            with self.subTest(shape=shape):
                relpath = self.shape(shape)
                self.assertTrue(
                    (self.repo / relpath).is_file(), "no fixture for shape %r" % shape
                )


class TestM8FilenamePatterns(CheckDirectiveTestCase):
    """AC-DT-06's nine M8 fixtures: five passing, four failing."""

    def test_ac_dt_06_m8_timestamped_descriptor_passes(self):
        rc, out, err = self.lint(self.fixture(name=DT_M8_PASSING_NAMES["timestamped"]))
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m8_cycle_directive_name_passes(self):
        rc, out, err = self.lint(self.fixture(name=DT_M8_PASSING_NAMES["cycle"]))
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m8_slug_directive_name_passes_with_any_characters(self):
        """M8 carries no character class, so the slug fixture uses odd characters."""
        rc, out, err = self.lint(self.fixture(name=DT_M8_PASSING_NAMES["slug"]))
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m8_relative_path_from_a_subdirectory_passes(self):
        """The fourth passing fixture: matched on the resolved path (AC-DT-19)."""
        relpath = self.fixture(name=DT_M8_PASSING_NAMES["timestamped"])
        nested = self.repo / "sub" / "deep"
        nested.mkdir(parents=True, exist_ok=True)
        rc, out, err = self.lint("../../" + relpath, cwd=nested)
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m8_absolute_path_passes(self):
        """The fifth passing fixture: also matched on the resolved path."""
        relpath = self.fixture(name=DT_M8_PASSING_NAMES["timestamped"])
        rc, out, err = self.lint(str(self.repo / relpath))
        self.assert_pass(rc, out, err)

    def test_ac_dt_06_m8_date_without_a_time_fails(self):
        """`<descriptor>-YYYYMMDD.md`: M8 requires the full `<date>T<time>` form."""
        rc, out, err = self.lint(self.fixture(name=DT_M8_FAILING_NAMES["date-only"]))
        self.assert_fails(rc, out, err, "M8", "filename-unmatched")

    def test_ac_dt_06_m8_neither_timestamped_nor_directive_suffixed_fails(self):
        rc, out, err = self.lint(self.fixture(name=DT_M8_FAILING_NAMES["neither"]))
        self.assert_fails(rc, out, err, "M8", "filename-unmatched")

    def test_ac_dt_06_m8_nested_subdirectory_name_fails(self):
        """`docs/cycles/sub/nested-directive.md` — a name AC-CO-1 does not license."""
        rc, out, err = self.lint(self.fixture(name=DT_M8_FAILING_NAMES["nested"]))
        self.assert_fails(rc, out, err, "M8", "filename-unmatched")

    def test_ac_dt_06_m8_outside_docs_cycles_fails(self):
        """`docs/escaped-directive.md` — the second unlicensed name."""
        rc, out, err = self.lint(self.fixture(name=DT_M8_FAILING_NAMES["escaped"]))
        self.assert_fails(rc, out, err, "M8", "filename-unmatched")


class TestCompanionCitations(CheckDirectiveTestCase):
    """AC-DT-09 and AC-DT-17 — M2 is a resolvability-and-touch check, exactly."""

    def test_ac_dt_09_citation_by_blob_hash_fails(self):
        relpath = self.fixture(companion_sha=self.citations["blob"])
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M2", "citation-unresolvable")
        self.assertIn(DT_COMPANION_A, out + err, "the failure named no citation")

    def test_ac_dt_09_citation_by_annotated_tag_fails(self):
        """A tag object is not a commit.

        Written to AC-DT-09 as agreed, not to TRD §3.6's mechanism: an annotated
        tag SHA satisfies both `cat-file -e <sha>^{commit}` and
        `diff-tree --root ... <sha>`, because git peels it. Filed as a finding.
        """
        relpath = self.fixture(companion_sha=self.citations["tag"])
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M2", "citation-unresolvable")

    def test_ac_dt_09_commit_touching_a_different_path_fails(self):
        relpath = self.fixture(companion_sha=self.citations["non_touching"])
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M2", "citation-not-touching")

    def test_ac_dt_09_root_commit_touching_the_cited_path_passes(self):
        """F-1's `--root` semantics: the touching commit is the repository's first.

        Without `--root`, `diff-tree` compares a root commit against nothing and
        reports it as touching no path, so this fixture is exactly the one that
        distinguishes the two forms.
        """
        relpath = self.fixture(companion_sha=self.citations["touching"])
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_ac_dt_09_citation_path_absent_from_the_commit_tree_fails(self):
        """M2's second clause: the path must be present in that commit's tree."""
        relpath = self.fixture(
            companion_path=DT_COMPANION_B, companion_sha=self.citations["touching"]
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M2", "citation-path-absent")

    def test_ac_dt_17_abbreviated_sha_of_a_touching_commit_passes(self):
        """AC-DT-17 (a): fullness is not checked."""
        relpath = self.fixture(companion_sha=self.citations["abbreviated"])
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_ac_dt_17_content_commit_that_is_not_the_last_passes(self):
        """AC-DT-17 (b): lastness is not checked.

        A lint failing this has been built to the metadata policy or AC-CO-4
        rather than to M2.
        """
        self.assertNotEqual(
            self.citations["not_last"],
            self.citations["last"],
            "the fixture must cite a commit that is not the last touching the path",
        )
        relpath = self.fixture(companion_sha=self.citations["not_last"])
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)


class TestUndecidableElements(CheckDirectiveTestCase):
    """AC-DT-10 — an element the lint cannot decide is unknown, and never exit 0."""

    def test_ac_dt_10_an_unresolvable_reviewed_ref_never_yields_exit_zero(self):
        """AC-DT-10: no element that is not a pass yields exit 0."""
        relpath = self.fixture(
            replace={
                "base-verification": (
                    "BASE VERIFICATION\n\nConfirm the base is at the reviewed ref %s.\n"
                    % self.citations["unresolvable"]
                ),
                "stop-conditions": (
                    "STOP CONDITIONS\n\nPinned to the reviewed ref %s. Cannot execute\n"
                    "as written: stop and surface. Concurrent tree mutation: stop and\n"
                    "surface.\n" % self.citations["unresolvable"]
                ),
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M1", "reviewed-ref-unresolvable")

    @unittest.skipIf(os.geteuid() == 0, "root can read a mode-000 directory")
    def test_ac_dt_10_a_failed_git_read_is_reported_unknown_and_exits_non_zero(self):
        """AC-DT-10/FM-L5: an element that cannot be decided is `unknown`.

        The only induceable form of FM-L5's "a git read fails" is to make the
        object store unreadable; the TRD names no other. Recorded as a finding.
        """
        relpath = self.fixture()
        objects = self.repo / ".git" / "objects"
        original = objects.stat().st_mode
        self.addCleanup(objects.chmod, stat.S_IMODE(original))
        objects.chmod(0o000)
        rc, out, err = self.lint(relpath)
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "unknown",
            (out + err).lower(),
            "an undecidable element was not reported unknown; stdout=%r" % out,
        )


class TestLintWritesNothing(CheckDirectiveTestCase):
    """AC-DT-12(b) — the lint writes nothing to the filesystem, ever."""

    def test_ac_dt_12b_a_passing_run_mutates_no_file(self):
        relpath = self.fixture()
        before = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)
        self.assertEqual(
            snapshot_tree(self.repo, skip=[self.repo / ".git"]),
            before,
            "the lint wrote to the tree it inspects",
        )

    def test_ac_dt_12b_a_failing_run_mutates_no_file(self):
        relpath = self.fixture(omit="M3")
        before = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-absent")
        self.assertEqual(
            snapshot_tree(self.repo, skip=[self.repo / ".git"]),
            before,
            "the lint wrote to the tree it inspects on the failing path",
        )

    def test_ac_dt_12b_the_lint_never_stages_or_commits(self):
        from tests.helpers import git, head_sha

        relpath = self.fixture()
        before_head = head_sha(self.repo, env=self.env)
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)
        self.assertEqual(head_sha(self.repo, env=self.env), before_head)
        staged = git(
            self.repo, "diff", "--cached", "--name-only", env=self.env, check=True
        )[1]
        self.assertEqual(staged.strip(), "")


class TestSourcedRequirements(CheckDirectiveTestCase):
    """AC-DT-13 — the lint enforces no requirement absent from its cited sources."""

    def test_ac_dt_13_every_failure_cites_a_governed_source(self):
        """Each element's failure names the governed text it derives from (G8)."""
        expected = {
            "M1": "directive-authoring",
            "M3": "directive-authoring",
            "M4": "core",
            "M5": "core",
            "M6": "decision",
            "M7": "core",
            "M8": "directive-authoring",
        }
        for element, needle in expected.items():
            with self.subTest(element=element):
                rc, out, err = self.lint(self.fixture(omit=element))
                self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
                self.assertIn(
                    needle,
                    (out + err).lower(),
                    "%s's failure cited no governed source containing %r; "
                    "stdout=%r stderr=%r" % (element, needle, out, err),
                )

    def test_ac_dt_13_no_ninth_element_is_enforced(self):
        """The checked set is exactly M1-M8: route and model stay unchecked (OQ-Q5)."""
        rc, out, err = self.lint(self.fixture())
        self.assert_pass(rc, out, err)
        for absent in ("M9", "M10"):
            self.assertNotIn(absent, out, "the lint reported an element beyond M8")

    def test_ac_dt_13_a_bare_unquoted_path_disposition_is_the_disclosed_false_stop(self):
        """§3.4's narrowing, tested as the TRD decides it and disclosed as a cost.

        The governed rule admits "a named directory plus the command creating
        it" with no quoting requirement; §3.4 requires a quoted or backticked
        token. This test pins the TRD's decision, and is the test that changes
        if F-7's narrowing is ruled the other way.
        """
        relpath = self.fixture(
            replace={
                "disposition": (
                    "%s (exclusive assignment): work only in wt/bare, created by\n"
                    "git worktree add wt/bare main\n" % DISPOSITION_LABEL
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-form-absent")


class TestPathResolution(CheckDirectiveTestCase):
    """AC-DT-19 — the path as it stands on disk, resolved from the root."""

    def test_ac_dt_19_an_uncommitted_file_is_linted(self):
        """No check requires the file to be staged, committed, or pushed."""
        relpath = self.fixture()
        from tests.helpers import porcelain

        self.assertIn(
            "??", porcelain(self.repo, env=self.env), "the fixture must be uncommitted"
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_ac_dt_19_a_committed_file_is_linted_identically(self):
        """Q2's sequencing changes nothing the lint can see (OQ-Q2)."""
        relpath = self.fixture()
        before = self.lint(relpath)
        commit(self.repo, "land the directive", env=self.env)
        after = self.lint(relpath)
        self.assertEqual(before[0], after[0], "committing changed the lint's verdict")
        self.assert_pass(*after)

    def test_ac_dt_19_a_relative_path_from_a_subdirectory_resolves(self):
        relpath = self.fixture()
        nested = self.repo / "sub" / "deep"
        nested.mkdir(parents=True, exist_ok=True)
        rc, out, err = self.lint("../../" + relpath, cwd=nested)
        self.assert_pass(rc, out, err)

    def test_ac_dt_19_an_absolute_path_inside_the_repository_resolves(self):
        relpath = self.fixture()
        rc, out, err = self.lint(str(self.repo / relpath))
        self.assert_pass(rc, out, err)

    def test_ac_dt_19_a_path_outside_the_repository_is_refused_naming_no_element(self):
        """A refused invocation, not an element finding. Its status is Q6."""
        outside = temp_dir(self, "aimeta-outside-")
        target = outside / "docs" / "cycles" / "elsewhere-20260828T170000.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Elsewhere\n")
        rc, out, err = self.lint(str(target))
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "path-outside-repo",
            bracket_codes(out + err),
            "expected [path-outside-repo]; saw %r" % bracket_codes(out + err),
        )
        for element in ELEMENTS:
            self.assertNotIn(
                element, out, "a refused invocation named element %s" % element
            )

    def test_ac_dt_19_a_path_that_does_not_exist_is_refused(self):
        rc, out, err = self.lint("docs/cycles/never-written-20260828T170000.md")
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "path-absent",
            bracket_codes(out + err),
            "expected [path-absent]; saw %r" % bracket_codes(out + err),
        )


class TestElementMatchRules(CheckDirectiveTestCase):
    """TRD §3.6's per-element match, extent, anchoring, and mask decisions."""

    def test_m1_the_pin_is_matched_free_within_the_line(self):
        """§3.6 M1: anchoring is free — the corpus writes the pin mid-sentence."""
        relpath = self.fixture(
            replace={
                "base-verification": (
                    "BASE VERIFICATION\n\n- **Reviewed ref**: everything below is\n"
                    "  pinned to %s, mid-sentence and bolded.\n" % self.reviewed_ref
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_m1_a_hyphenated_reviewed_ref_spelling_matches(self):
        """§3.6 M1: "the two words separated by whitespace or a hyphen"."""
        relpath = self.fixture(
            replace={
                "base-verification": (
                    "BASE VERIFICATION\n\nPinned to the reviewed-ref %s.\n"
                    % self.reviewed_ref
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_m1_a_short_hex_run_below_seven_characters_is_not_a_sha(self):
        """§3.6 M1: the run is 7 to 40 hexadecimal characters."""
        relpath = self.fixture(
            replace={
                "base-verification": "BASE VERIFICATION\n\nPinned to the reviewed ref abc12.\n",
                "stop-conditions": (
                    "STOP CONDITIONS\n\nCannot execute as written: stop and surface.\n"
                    "Concurrent tree mutation: stop and surface.\n"
                ),
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M1")

    def test_m4_each_stop_condition_is_an_independent_test(self):
        """§3.6 M4: both must be satisfied; one alone fails."""
        relpath = self.fixture(
            replace={
                "stop-conditions": (
                    "STOP CONDITIONS\n\nPinned to the reviewed ref %s. Cannot execute\n"
                    "as written: stop and surface.\n" % self.reviewed_ref
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M4", "stop-condition-missing")

    def test_m4_the_phrases_are_matched_case_insensitively(self):
        """§3.6: all phrase matches are case-insensitive and collapse whitespace."""
        relpath = self.fixture(
            replace={
                "stop-conditions": (
                    "STOP CONDITIONS\n\nPinned to the reviewed ref %s. CANNOT   EXECUTE\n"
                    "AS WRITTEN: stop. Concurrent   Tree   Mutation: stop.\n"
                    % self.reviewed_ref
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_m5_all_four_phrases_must_share_one_extent(self):
        """§3.6 M5: the first extent containing all four is the first-act statement."""
        relpath = self.fixture(
            replace={
                "first-act": (
                    "FIRST ACT\n\nWrite the directive file.\n\nCommit it.\n\nPush it.\n\n"
                    "Then report the SHA.\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M5", "first-act-missing")

    def test_m5_a_non_preamble_marker_before_the_statement_fails(self):
        """§3.6 M5: only the heading and `ROUTE AND MODEL` may precede it."""
        relpath = self.fixture(
            replace={
                "route": (
                    "ROUTE AND MODEL\n\nRoute: fresh\nModel: Opus 5\n\n"
                    "BACKGROUND\n\nSome context the author put first.\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M5", "first-act-missing")

    def test_m5_the_route_and_model_preamble_marker_is_tolerated(self):
        """The preamble list widens what counts as first; it refuses nothing."""
        rc, out, err = self.lint(self.fixture())
        self.assert_pass(rc, out, err)

    def test_m6_the_report_marker_is_matched_case_folded(self):
        """§3.6 M6: a marker line whose token, case-folded, is `report`."""
        relpath = self.fixture(
            replace={
                "report": (
                    "## Report\n\n- the directive file's commit SHA\n"
                    "- anything observed this directive did not anticipate\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_m7_all_four_class_words_are_required(self):
        """§3.6 M7: Core rule 6 names exactly four classes; three is not enough."""
        relpath = self.fixture(
            replace={"claim-labels": "CLAIM LABELS\n\nLabel every claim observed,\ninferred, or told.\n"}
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M7", "claim-labels-missing")

    def test_m7_the_four_class_words_must_share_one_extent(self):
        """§3.6 M7: extent is a statement extent, not the whole file."""
        relpath = self.fixture(
            replace={
                "claim-labels": (
                    "CLAIM LABELS\n\nLabel claims observed.\n\nOr inferred.\n\n"
                    "Or told.\n\nOr unknown.\n"
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M7", "claim-labels-missing")


class TestMarkdownSensitivity(CheckDirectiveTestCase):
    """TRD §3.5 — everything M3 does about markdown, driven through the binary.

    Driven through the binary rather than by importing `aimeta.mdmask`: a unit
    test over an absent module reds on the import, which proves nothing about
    the suite. These reds are behavioural.
    """

    def test_mask_a_fenced_labelled_statement_is_masked(self):
        """The exclusion the PRD states: backtick fences."""
        rc, out, err = self.lint(self.shape("vi-unfenced-plus-fenced"))
        self.assert_pass(rc, out, err)

    def test_mask_a_tilde_fenced_labelled_statement_is_masked(self):
        """§3.5: backtick **or tilde**, three or more of the same character."""
        relpath = self.fixture(
            extra="~~~\n%s: %s\n~~~\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_mask_an_unclosed_fence_masks_to_end_of_file(self):
        """§3.5: an unclosed fence masks to end of file."""
        relpath = self.fixture(
            extra="```\n%s: %s\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_mask_a_blockquoted_labelled_statement_is_masked(self):
        """§3.5: a line whose leading non-whitespace is `>`."""
        relpath = self.fixture(
            extra="> %s: %s\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_mask_an_html_commented_labelled_statement_is_masked(self):
        """§3.5: `<!--` through the matching `-->`."""
        relpath = self.fixture(
            extra="<!--\n%s: %s\n-->\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_mask_an_indented_block_is_not_masked(self):
        """§3.5, deliberately: four-space indentation is continuation, not code.

        The cost is the disclosed false stop — a genuinely indented code block
        carrying the label produces a second statement and a non-zero exit.
        """
        relpath = self.fixture(
            extra="    %s: %s\n" % (DISPOSITION_LABEL, SOLE_TREE_SENTENCE)
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-multiple")

    def test_stripping_a_bulleted_label_is_recognised(self):
        """§3.5's stripping: one list marker and the space after it."""
        relpath = self.fixture(
            replace={"disposition": "- " + DT_DISPOSITION_STATEMENT}
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_stripping_a_bolded_label_is_recognised(self):
        """§3.5's stripping: leading `**` or `__`."""
        relpath = self.fixture(
            replace={
                "disposition": (
                    "**%s (exclusive assignment):** work only in a worktree at\n"
                    '"wt/bold", created by: git worktree add "wt/bold" main\n'
                    % DISPOSITION_LABEL
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_stripping_an_inline_code_span_in_prose_is_not_a_statement(self):
        """§3.5, not handled deliberately: the line anchor already excludes it."""
        relpath = self.fixture(
            extra="The `%s` label is fixed by the invariants document.\n"
            % DISPOSITION_LABEL
        )
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)

    def test_the_label_match_is_case_sensitive(self):
        """§3.4: case-sensitive, no hyphen variants, no other spelling."""
        relpath = self.fixture(
            replace={
                "disposition": (
                    'Working-tree disposition (exclusive assignment): "wt/x",\n'
                    'created by: git worktree add "wt/x" main\n'
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-absent")

    def test_the_space_spelled_label_variant_does_not_match(self):
        """§3.4: `WORKING TREE` (space, no hyphen) is not the label.

        29 of the corpus's 33 labelled dispositions use that spelling
        (review observation O-3), so this test pins a decision with a corpus
        cost, not a free one.
        """
        relpath = self.fixture(
            replace={
                "disposition": (
                    'WORKING TREE — exclusive assignment: "wt/x", created by:\n'
                    'git worktree add "wt/x" main\n'
                )
            }
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-absent")

    def test_crlf_line_endings_are_normalized_before_masking(self):
        """§3.5: `\\r\\n` and `\\r` normalize to `\\n`; the match is byte-exact after."""
        relpath = self.fixture()
        path = pathlib.Path(self.repo) / relpath
        path.write_bytes(path.read_text().replace("\n", "\r\n").encode("utf-8"))
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err)


class TestInvariantsDocumentDependency(CheckDirectiveTestCase):
    """FM-L3, and the asymmetry §3.6 step 4 leaves against §3.2.

    §3.2 scopes the **generator's** read of the invariants document to committed
    content in the methodology home. §3.6 step 4 says only "load the invariants
    … from the methodology home" and scopes the **lint's** read to nothing. This
    class tests the lint to the TRD as written — an uncommitted edit takes
    effect immediately — and is the test that changes if the asymmetry resolves.
    """

    def test_fm_l3_a_missing_invariants_document_refuses_the_invocation(self):
        """Without the label the lint cannot decide M3, and AC-DT-10 forbids exit 0."""
        (pathlib.Path(self.home) / "skills" / "directive-invariants.md").unlink()
        rc, out, err = self.lint(self.fixture())
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "invariants-missing",
            bracket_codes(out + err),
            "expected [invariants-missing]; saw %r" % bracket_codes(out + err),
        )

    def test_fm_l3_a_missing_label_section_refuses_the_invocation(self):
        invariants_doc(self.home, drop=("Disposition label",), env=self.env,
                       message="drop the label section")
        rc, out, err = self.lint(self.fixture())
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "invariants-section-missing",
            bracket_codes(out + err),
            "expected [invariants-section-missing]; saw %r" % bracket_codes(out + err),
        )

    def test_the_lints_read_is_not_scoped_to_committed_content(self):
        """§3.6 step 4 as written: an **uncommitted** label change takes effect.

        The generator refuses the same edit under FM-G3. The asymmetry is filed
        as a finding; if it resolves toward §3.2, this test inverts.
        """
        write(
            self.home,
            "skills/directive-invariants.md",
            open(pathlib.Path(self.home) / "skills" / "directive-invariants.md").read()
            .replace(DISPOSITION_LABEL, "TREE ASSIGNMENT"),
        )
        relpath = self.fixture()
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-absent")


class TestGeneratedSkeletonPassesTheLint(CheckDirectiveTestCase):
    """J2's construction: a faithfully filled skeleton passes M3 by construction.

    AC-DT-06's fixtures (iv) and (v) as the TRD frames them — against a real
    generated skeleton rather than a hand-built imitation of one.
    """

    def generate(self, *args):
        return run_dt(
            "directive",
            "--descriptor", "roundtrip",
            "--title", "Round trip",
            "--timestamp", "20260828T170000",
            *args,
            cwd=self.repo,
            env=self.env,
        )

    def test_ac_dt_06_iv_a_generated_skeleton_with_the_slot_filled_passes(self):
        rc, out, err = self.generate("--write")
        self.assertEqual(rc, 0, "generator: stdout=%r stderr=%r" % (out, err))
        relpath = "docs/cycles/roundtrip-20260828T170000Z.md"
        path = pathlib.Path(self.repo) / relpath
        self.assertTrue(path.is_file(), "the generator wrote no skeleton at %s" % relpath)
        filled = path.read_text().replace(
            "%s:" % DISPOSITION_LABEL,
            '%s: this session works only in a worktree at "wt/rt", created by:\n'
            'git worktree add "wt/rt" main' % DISPOSITION_LABEL,
            1,
        )
        path.write_text(filled)
        rc, out, err = self.lint(relpath)
        self.assert_pass(rc, out, err, elements=("M3",))

    def test_ac_dt_06_v_a_generated_skeleton_with_a_blank_slot_fails(self):
        rc, out, err = self.generate("--write")
        self.assertEqual(rc, 0, "generator: stdout=%r stderr=%r" % (out, err))
        relpath = "docs/cycles/roundtrip-20260828T170000Z.md"
        self.assertTrue(
            (pathlib.Path(self.repo) / relpath).is_file(),
            "the generator wrote no skeleton at %s" % relpath,
        )
        rc, out, err = self.lint(relpath)
        self.assert_fails(rc, out, err, "M3", "disposition-form-absent")


if __name__ == "__main__":
    unittest.main()
