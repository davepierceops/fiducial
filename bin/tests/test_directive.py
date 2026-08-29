"""AC-DT-01..AC-DT-05, AC-DT-11, AC-DT-12, AC-DT-14, AC-DT-15, AC-DT-18.

`bin/directive`, the generator. Contract: `specs/directive-tooling.md` §6 and
`specs/directive-tooling-trd.md` §3.2, §3.3, §3.9, §6, §7.

Written before the binary exists, and proven red on **wrong behaviour** rather
than on an absent module by running against `bin/tests/stubs/directive` — a
stub that emits a skeleton with no manifest and two unfenced labelled
disposition statements, ignores `--write`, and exits 0. See
`bin/tests/red-run-with-stubs.log`.

The general-mode timestamp is fixed with `--timestamp` (TRD §3.9), so every
expected destination path here is deterministic.
"""

from __future__ import annotations

import ast
import pathlib
import re
import unittest

from tests.helpers import (
    BIN_DIR,
    DISPOSITION_LABEL,
    INVARIANTS_RELPATH,
    base_env,
    bracket_codes,
    citation_fixtures,
    commit,
    dt_bin_dir,
    git,
    head_sha,
    invariants_doc,
    invariants_sections,
    invariants_text,
    make_home_repo,
    make_repo,
    no_traceback,
    porcelain,
    read,
    run_dt,
    snapshot_tree,
    write,
)

TIMESTAMP = "20260828T170000"
GENERAL_RELPATH = "docs/cycles/fixture-%sZ.md" % TIMESTAMP

MANIFEST_ENTRY_RE = re.compile(r"^(?P<marker>.+?) — (?P<source>.+)$")
COMMITTED_SOURCE_RE = re.compile(r"^(?P<path>\S+) @ (?P<sha>[0-9a-f]{40})$")
AUTHOR_SOURCE = "author region"

#: §3.3's marker syntax, reimplemented test-side so the assertions do not
#: depend on the implementation's own idea of what a marker is.
ATX_MARKER_RE = re.compile(r"^#{1,6} (?P<token>.+)$")
CAPS_MARKER_RE = re.compile(r"^(?P<token>[A-Z0-9-]+(?: [A-Z0-9-]+)*)")

#: AC-DT-02's exclusion: lines of committed source made only of separators.
SEPARATOR_CHARS = set("-=~`#*_|>+ \t")


def is_marker(line):
    """`(True, token)` when `line` is a marker per §3.3, else `(False, None)`."""
    atx = ATX_MARKER_RE.match(line)
    if atx:
        return True, atx.group("token").strip()
    caps = CAPS_MARKER_RE.match(line)
    if caps:
        token = caps.group("token")
        if len(token) >= 3:
            return True, token
    return False, None


def normalize(line):
    """AC-DT-02's normalization: strip ends, collapse internal runs to one space."""
    return " ".join(line.split())


def is_separator_only(line):
    """AC-DT-02's exclusion, read raw."""
    return line != "" and set(line) <= SEPARATOR_CHARS


def parse_manifest(text):
    """The `SOURCE MANIFEST` region's entries, in emission order.

    Returns `[(marker_token, source)]`, where `source` is either
    `("committed", path, sha)` or `("author",)`.
    """
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        found, token = is_marker(line)
        if found and token == "SOURCE MANIFEST":
            start = index
            break
    if start is None:
        return []
    entries = []
    for line in lines[start + 1:]:
        match = MANIFEST_ENTRY_RE.match(line.strip())
        if not match:
            continue
        marker = match.group("marker").strip()
        source = match.group("source").strip()
        if source == AUTHOR_SOURCE:
            entries.append((marker, ("author",)))
            continue
        committed = COMMITTED_SOURCE_RE.match(source)
        if committed:
            entries.append(
                (marker, ("committed", committed.group("path"), committed.group("sha")))
            )
    return entries


def eligible_lines(text):
    """§3.5's mask, test-side: line indices a line-anchored match may consider."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    eligible = []
    fence = None
    in_comment = False
    for index, line in enumerate(lines):
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)
        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if fence is None and "<!--" in line:
            if "-->" not in line.split("<!--", 1)[1]:
                in_comment = True
            continue
        if fence is not None:
            if indent <= 3 and re.match(r"^(%s{%d,})\s*$" % (fence[0], fence[1]), stripped):
                fence = None
            continue
        opening = re.match(r"^(`{3,}|~{3,})", stripped)
        if opening and indent <= 3:
            fence = (opening.group(1)[0], len(opening.group(1)))
            continue
        if stripped.startswith(">"):
            continue
        eligible.append(index)
    return lines, eligible


def leading_content(line):
    """§3.5's stripping, applied once each, in order."""
    text = re.sub(r"^ {0,3}", "", line)
    text = re.sub(r"^(?:[-*+]|\d+[.)]) ", "", text)
    text = re.sub(r"^#{1,6} ", "", text)
    text = re.sub(r"^(\*\*|__)", "", text)
    return text


def unfenced_labelled_statements(text, label=DISPOSITION_LABEL):
    """Indices of lines carrying an unfenced labelled disposition statement (§3.4)."""
    lines, eligible = eligible_lines(text)
    hits = []
    for index in eligible:
        content = leading_content(lines[index])
        if not content.startswith(label):
            continue
        rest = content[len(label):]
        if ":" in rest:
            hits.append(index)
    return hits


def production_dt_files():
    """The generator's own source: the binary plus the modules only it reaches."""
    files = []
    binary = dt_bin_dir() / "directive"
    if binary.is_file():
        files.append(binary)
    for name in ("directive.py", "invariants.py"):
        candidate = BIN_DIR / "aimeta" / name
        if candidate.is_file():
            files.append(candidate)
    return files


def string_constants(path):
    """Every string constant in a Python source file, or [] when it will not parse."""
    try:
        tree = ast.parse(path.read_text(errors="replace"), filename=str(path))
    except SyntaxError:
        return []
    return [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]


class DirectiveTestCase(unittest.TestCase):
    def setUp(self):
        self.home = make_home_repo(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        self.citations = citation_fixtures(self.repo, env=self.env)
        self.reviewed_ref = self.citations["last"]

    def generate(self, *args, cwd=None):
        return run_dt("directive", *args, cwd=cwd or self.repo, env=self.env)

    def general(self, *args, descriptor="fixture", title="Fixture"):
        return self.generate(
            "--descriptor", descriptor,
            "--title", title,
            "--timestamp", TIMESTAMP,
            *args,
        )

    def cycle_directive(self, *args, relpath="docs/cycles/cycle-7-directive.md"):
        """Run cycle mode and return the directive it landed, asserting it landed."""
        rc, out, err = self.generate(*args)
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(
            (self.repo / relpath).is_file(),
            "cycle mode wrote no directive at %s; worktree: %r"
            % (relpath, porcelain(self.repo, env=self.env)),
        )
        return read(self.repo, relpath)

    def skeleton(self, *args, **kwargs):
        """A general-mode skeleton on stdout, with the run asserted successful."""
        rc, out, err = self.general(*args, **kwargs)
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(out.strip(), "the generator emitted nothing on stdout")
        return out


class TestInvariantTextIsRead(DirectiveTestCase):
    """AC-DT-01 and Q1's mechanism — the text is read, never hardcoded."""

    def test_ac_dt_01_changing_a_committed_section_changes_the_next_skeleton(self):
        """AC-DT-01: no edit to the generator; the commit is what changes.

        Asserted in the methodology home, because §3.2 resolves the invariants
        document's revision there — which is why `make_home_repo` gives the home
        a history to change in (F-2's resolution).
        """
        before = self.skeleton()
        self.assertIn("Commands run in a sandbox", before)
        invariants_doc(
            self.home,
            overrides={
                "Sandbox constraints": "SANDBOX\n\nA WHOLLY DIFFERENT SANDBOX RULE.\n"
            },
            env=self.env,
            message="amend the sandbox section",
        )
        after = self.skeleton()
        self.assertIn(
            "A WHOLLY DIFFERENT SANDBOX RULE.",
            after,
            "the skeleton did not follow the committed text",
        )
        self.assertNotIn("Commands run in a sandbox", after)

    def test_ac_dt_01_an_uncommitted_edit_does_not_reach_the_skeleton(self):
        """§3.2: resolution is against committed content, not the working tree."""
        write(
            self.home,
            INVARIANTS_RELPATH,
            invariants_text({"Sandbox constraints": "SANDBOX\n\nUNCOMMITTED.\n"}),
        )
        rc, out, err = self.general("--allow-dirty")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(
            "Commands run in a sandbox",
            out,
            "the committed section body did not reach the skeleton at all",
        )
        self.assertNotIn(
            "UNCOMMITTED.", out, "the generator read the working tree, not the commit"
        )

    def test_fm_g3_an_uncommitted_invariants_document_is_refused(self):
        """FM-G3: refusal, at exit 3, with [invariants-dirty]."""
        write(
            self.home,
            INVARIANTS_RELPATH,
            invariants_text({"Sandbox constraints": "SANDBOX\n\nUNCOMMITTED.\n"}),
        )
        rc, out, err = self.general()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invariants-dirty", bracket_codes(out + err))

    def test_fm_g3_allow_dirty_downgrades_the_refusal_to_a_warning(self):
        """FM-G3: AC-CO-5's shape, applied to a second class of input."""
        write(
            self.home,
            INVARIANTS_RELPATH,
            invariants_text({"Sandbox constraints": "SANDBOX\n\nUNCOMMITTED.\n"}),
        )
        rc, out, err = self.general("--allow-dirty")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("WARN", out + err)

    def test_fm_g1_a_home_that_is_not_a_repository_is_refused(self):
        """FM-G1: no working-tree fallback; a section with no committed body is absent."""
        home = make_home_repo(self, git_init=False)
        write(home, INVARIANTS_RELPATH, invariants_text())
        env = base_env(methodology_home=home)
        rc, out, err = run_dt(
            "directive", "--descriptor", "fixture", "--title", "T",
            "--timestamp", TIMESTAMP, cwd=self.repo, env=env,
        )
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invariants-missing", bracket_codes(out + err))

    def test_fm_g2_a_missing_named_section_is_refused(self):
        """FM-G2: refusal before anything is written."""
        invariants_doc(
            self.home, drop=("Sandbox constraints",), env=self.env,
            message="drop the sandbox section",
        )
        rc, out, err = self.general()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invariants-section-missing", bracket_codes(out + err))

    def test_fm_g4_an_unrecognised_placeholder_is_refused_not_passed_through(self):
        """FM-G4: the placeholder set is closed; never a silent pass-through."""
        invariants_doc(
            self.home,
            overrides={"Sandbox constraints": "SANDBOX\n\nSee {{nonexistent_thing}}.\n"},
            env=self.env,
            message="add an unknown placeholder",
        )
        rc, out, err = self.general()
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("invariants-placeholder-unknown", bracket_codes(out + err))

    def test_fm_g5_an_existing_destination_is_refused(self):
        """FM-G5: the computed destination is never clobbered (OQ-4's reading of G4)."""
        write(self.repo, GENERAL_RELPATH, "# existing\n")
        rc, out, err = self.general("--write")
        self.assertEqual(rc, 3, "stdout=%r stderr=%r" % (out, err))
        self.assertIn("directive-exists", bracket_codes(out + err))
        self.assertIn("# existing", read(self.repo, GENERAL_RELPATH))


class TestNoHardcodedInvariantText(DirectiveTestCase):
    """AC-DT-02 — a static scan over the generator's source, against its manifest."""

    def test_ac_dt_02_no_generator_literal_reproduces_committed_region_content(self):
        text = self.skeleton()
        entries = parse_manifest(text)
        committed = [e for e in entries if e[1][0] == "committed"]
        self.assertTrue(
            committed,
            "the skeleton carried no committed manifest entry to scan against; "
            "AC-DT-02 is a scan over the manifest's own entries",
        )
        sources = production_dt_files()
        self.assertTrue(sources, "no generator source found to scan")
        literals = set()
        for path in sources:
            if path.suffix == ".py" or path.name == "directive":
                literals |= {normalize(v) for v in string_constants(path)}
            literals |= {normalize(line) for line in path.read_text(errors="replace").splitlines()}
        offenders = []
        for marker, source in committed:
            body = read(self.home, source[1])
            for line in body.splitlines():
                if is_separator_only(line) or not line.strip():
                    continue
                if normalize(line) in literals:
                    offenders.append("%s: %r" % (marker, line))
        self.assertEqual(
            offenders,
            [],
            "the generator's source reproduces committed region content:\n%s"
            % "\n".join(offenders),
        )

    def test_ac_dt_02_scans_the_generator_only(self):
        """§8 and the agreed criterion scope the scan to the generator's source.

        §3.6 says elsewhere that it runs over the lint's source too; F-8. This
        test pins the agreed scope, and is the test that changes if the wider
        reading is adopted as a PRD amendment.
        """
        scanned = {p.name for p in production_dt_files()}
        self.assertNotIn("check-directive", scanned)
        self.assertNotIn("elements.py", scanned)
        self.assertNotIn("mdmask.py", scanned)


class TestDispositionSlot(DirectiveTestCase):
    """AC-DT-03 and Q10 — the slot is two regions, and the invariant holds."""

    def test_ac_dt_03_the_prompt_region_matches_the_committed_source_it_names(self):
        text = self.skeleton()
        entries = dict(parse_manifest(text))
        self.assertIn(
            "DISPOSITION PROMPT",
            entries,
            "no prompt region in the manifest; §3.3's tables must carry one (F-3)",
        )
        source = entries["DISPOSITION PROMPT"]
        self.assertEqual(source[0], "committed", "the prompt is not an author region")
        committed_body = read(self.home, source[1])
        section = committed_body.split("## Working-tree disposition prompt\n", 1)[1]
        section = section.split("\n## ", 1)[0].strip()
        self.assertIn(
            section,
            text,
            "the emitted prompt region does not match its named committed source",
        )

    def test_ac_dt_03_the_prompt_states_the_requirement_and_both_forms(self):
        text = self.skeleton()
        prompt = text.split("DISPOSITION PROMPT", 1)[1].split(DISPOSITION_LABEL, 1)[0]
        lowered = prompt.lower()
        self.assertIn("required", lowered, "the prompt does not state that it is required")
        self.assertIn("exclusive assignment", lowered)
        self.assertIn("sole-tree", lowered)
        self.assertIn(
            "labelled statement", lowered, "the prompt does not state the labelled-statement requirement"
        )

    def test_ac_dt_03_the_author_region_is_the_label_over_a_blank_slot(self):
        text = self.skeleton()
        lines = text.split("\n")
        hits = [i for i, l in enumerate(lines) if l.startswith("%s:" % DISPOSITION_LABEL)]
        self.assertEqual(
            len(hits), 1, "expected exactly one label line at column 0; got %d" % len(hits)
        )
        index = hits[0]
        self.assertEqual(
            lines[index].strip(),
            "%s:" % DISPOSITION_LABEL,
            "the emitted slot is not empty",
        )
        self.assertEqual(
            lines[index + 1].strip(), "", "the content slot is not a blank slot"
        )

    def test_ac_dt_03_exactly_one_unfenced_labelled_statement_general_mode(self):
        """G3's generated-skeleton invariant, general mode."""
        text = self.skeleton()
        hits = unfenced_labelled_statements(text)
        self.assertEqual(
            len(hits),
            1,
            "the skeleton carries %d unfenced labelled disposition statements, not "
            "one; G3 is the invariant the whole design rests on" % len(hits),
        )

    def test_ac_dt_03_exactly_one_unfenced_labelled_statement_cycle_mode(self):
        """G3's invariant holds "in either mode"."""
        text = self.cycle_directive(
            "--cycle", "7", "--title", "T", "--date", "2026-08-28", "docs/companion-a.md"
        )
        hits = unfenced_labelled_statements(text)
        self.assertEqual(len(hits), 1, "cycle mode emitted %d statements" % len(hits))

    def test_q10_the_invariants_document_shows_the_label_only_inside_fences(self):
        """§3.2's condition 2, the one property of one file that makes G3 hold."""
        body = read(self.home, INVARIANTS_RELPATH)
        hits = unfenced_labelled_statements(body)
        self.assertEqual(
            len(hits),
            0,
            "the invariants document carries the label unfenced at lines %r; "
            "condition 2 is what makes the emitted count exactly one" % hits,
        )

    def test_q10_the_generator_fences_nothing_at_emission(self):
        """Q10's rejected third candidate: no fence appears that the source lacks."""
        text = self.skeleton()
        emitted = text.count("```") + text.count("~~~")
        committed = read(self.home, INVARIANTS_RELPATH)
        sections = invariants_sections()
        expected = sum(
            sections[name].count("```") + sections[name].count("~~~")
            for name in (
                "Heading (general)", "Route and model", "First act",
                "Working-tree disposition prompt", "Base verification", "Companions",
                "Task", "Sandbox constraints", "Verification steps", "Stop conditions",
                "Report format", "Claim labels", "Source manifest",
            )
        )
        self.assertEqual(
            emitted,
            expected,
            "the generator added or dropped fence markers relative to its sources; "
            "committed document length %d" % len(committed),
        )


class TestGeneratorExitAndRefusals(DirectiveTestCase):
    """AC-DT-04 and §3.9's mode selection."""

    def test_ac_dt_04_general_mode_exits_zero_and_produces_a_skeleton(self):
        rc, out, err = self.general()
        self.assertTrue(no_traceback(out, err), "traceback: %r" % err)
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertIn(DISPOSITION_LABEL, out, "no skeleton was produced")
        self.assertIn(
            "SOURCE MANIFEST",
            out,
            "the manifest is part of the skeleton (AC-DT-05), so a skeleton "
            "without one is not a skeleton",
        )

    def test_ac_dt_04_general_mode_write_lands_the_skeleton_at_exit_zero(self):
        """"Every invocation that produces a skeleton" includes the `--write` path."""
        rc, out, err = self.general("--write")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(
            (self.repo / GENERAL_RELPATH).is_file(),
            "--write produced no file at %s; worktree: %r"
            % (GENERAL_RELPATH, porcelain(self.repo, env=self.env)),
        )

    def test_ac_dt_04_general_mode_has_no_content_refusal_path(self):
        """G4: in general mode the generator refuses nothing about content."""
        rc, out, err = self.general(descriptor="anything-at-all", title="A title with — an em dash")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

    def test_selector_rule_neither_selector_is_a_usage_error(self):
        """§3.9: exactly one of `--cycle N`, `--name SLUG`, `--descriptor SLUG`."""
        rc, out, err = self.generate("--title", "T")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_selector_rule_two_selectors_is_a_usage_error(self):
        rc, out, err = self.generate("--cycle", "7", "--descriptor", "x", "--title", "T")
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_flag_collision_timestamp_in_cycle_mode_is_a_usage_error(self):
        """§3.9: `--timestamp` is general-mode-only, `--date` cycle-mode-only."""
        rc, out, err = self.generate(
            "--cycle", "7", "--title", "T", "--timestamp", TIMESTAMP, "docs/companion-a.md"
        )
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_flag_collision_date_in_general_mode_is_a_usage_error(self):
        rc, out, err = self.generate(
            "--descriptor", "x", "--title", "T", "--date", "2026-08-28"
        )
        self.assertEqual(rc, 2, "stdout=%r stderr=%r" % (out, err))

    def test_write_is_a_switch_and_names_no_path(self):
        """§3.9/F-5: `--write` takes no value; the destination is computed."""
        rc, out, err = self.general("--write", "somewhere/else.md")
        self.assertNotEqual(
            rc, 0, "`--write` accepted a path argument; stdout=%r stderr=%r" % (out, err)
        )

    def test_the_general_mode_filename_is_utc_and_z_suffixed(self):
        """§3.9: `docs/cycles/<descriptor>-<YYYYMMDDThhmmss>Z.md`."""
        rc, out, err = self.general("--write")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(
            (self.repo / GENERAL_RELPATH).is_file(),
            "expected %s; worktree: %r" % (GENERAL_RELPATH, porcelain(self.repo, env=self.env)),
        )


class TestSourceManifest(DirectiveTestCase):
    """AC-DT-05 and AC-DT-18 — the manifest, the markers, and the partition."""

    def test_ac_dt_05_the_manifest_is_part_of_the_emitted_skeleton(self):
        text = self.skeleton()
        entries = parse_manifest(text)
        self.assertTrue(entries, "the skeleton carried no source manifest at all")

    def test_ac_dt_05_every_entry_carries_exactly_one_classification(self):
        text = self.skeleton()
        entries = parse_manifest(text)
        self.assertTrue(entries, "the skeleton carried no manifest entries to classify")
        for marker, source in entries:
            with self.subTest(marker=marker):
                self.assertIn(source[0], ("committed", "author"))
                if source[0] == "committed":
                    self.assertRegex(source[2], r"^[0-9a-f]{40}$")

    def test_ac_dt_05_every_marker_appears_in_the_file_exactly_once(self):
        text = self.skeleton()
        entries = parse_manifest(text)
        self.assertTrue(entries, "the skeleton carried no manifest entries to locate")
        lines = text.split("\n")
        for marker, _ in entries:
            with self.subTest(marker=marker):
                hits = [l for l in lines if is_marker(l) == (True, marker)]
                self.assertEqual(
                    len(hits), 1, "marker %r appears %d times" % (marker, len(hits))
                )

    def test_ac_dt_05_the_markers_partition_the_whole_file(self):
        """Each region runs marker to next marker: no head gap, no gap, no overlap."""
        text = self.skeleton()
        entries = parse_manifest(text)
        self.assertTrue(entries, "no manifest to partition against")
        lines = text.split("\n")
        positions = []
        for marker, _ in entries:
            found = [i for i, l in enumerate(lines) if is_marker(l) == (True, marker)]
            self.assertEqual(len(found), 1, "marker %r is not unique" % marker)
            positions.append(found[0])
        self.assertEqual(
            positions[0], 0, "the first region's marker is not the file's first line"
        )
        self.assertEqual(
            positions,
            sorted(positions),
            "the manifest's emission order does not match the file's order",
        )
        self.assertEqual(
            len(set(positions)), len(positions), "two entries share one marker line"
        )

    def test_ac_dt_18_exactly_two_author_regions_general_mode(self):
        """AC-DT-18: one task-specific slot, one disposition region, all else committed."""
        entries = parse_manifest(self.skeleton())
        self.assertTrue(entries, "no manifest emitted")
        authors = [m for m, s in entries if s[0] == "author"]
        self.assertEqual(
            sorted(authors),
            sorted([DISPOSITION_LABEL, "TASK"]),
            "the two author regions are not the task slot and the disposition slot",
        )
        committed = [m for m, s in entries if s[0] == "committed"]
        self.assertEqual(
            len(committed), len(entries) - 2, "every other entry must name a committed path"
        )

    def test_ac_dt_18_exactly_two_author_regions_cycle_mode(self):
        entries = parse_manifest(self.cycle_directive(
            "--cycle", "7", "--title", "T", "--date", "2026-08-28", "docs/companion-a.md"
        ))
        self.assertTrue(entries, "cycle mode emitted no manifest")
        authors = [m for m, s in entries if s[0] == "author"]
        self.assertEqual(
            sorted(authors),
            sorted([DISPOSITION_LABEL, "Execution notes"]),
            "cycle mode's author regions are not the disposition slot and "
            "`## Execution notes`",
        )

    def test_ac_dt_05_the_manifest_preamble_names_a_committed_path(self):
        """§3.3: the manifest's own entry names a committed path, without exception."""
        entries = dict(parse_manifest(self.skeleton()))
        self.assertIn("SOURCE MANIFEST", entries)
        self.assertEqual(entries["SOURCE MANIFEST"][0], "committed")


class TestGeneratorClaims(DirectiveTestCase):
    """AC-DT-11's generator half — two provenance labels and no other class."""

    def test_ac_dt_11_generator_diagnostics_use_no_class_beyond_observed_and_unknown(self):
        invariants_doc(
            self.home, drop=("Sandbox constraints",), env=self.env, message="drop a section"
        )
        rc, out, err = self.general()
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        lowered = err.lower()
        for forbidden in ("inferred", "told"):
            self.assertNotIn(
                forbidden,
                lowered,
                "the generator used the %r class for its own claim; stderr=%r"
                % (forbidden, err),
            )

    def test_ac_dt_11_the_emitted_claim_label_region_is_not_a_claim(self):
        """The skeleton's claim-label instruction names all four classes; that is
        emitted text, not a claim by the generator."""
        text = self.skeleton()
        for word in ("observed", "inferred", "told", "unknown"):
            self.assertIn(word, text.lower(), "the CLAIM LABELS region is incomplete")


class TestGeneratorWriteBoundary(DirectiveTestCase):
    """AC-DT-12(a) and (c)."""

    FORBIDDEN_ARGV = {
        "gh", "push", "fetch", "ls-remote", "remote", "clone",
        "commit", "add", "stage", "update-index", "credential",
    }

    def test_ac_dt_12a_no_code_path_names_a_remote_or_a_write_subcommand(self):
        """Static scan over both tools, extended to fetch/push/ls-remote (§8)."""
        files = []
        for name in ("directive", "check-directive"):
            candidate = dt_bin_dir() / name
            if candidate.is_file():
                files.append(candidate)
        for name in ("directive.py", "invariants.py", "elements.py", "mdmask.py"):
            candidate = BIN_DIR / "aimeta" / name
            if candidate.is_file():
                files.append(candidate)
        self.assertTrue(files, "no production source found to scan")
        offenders = []
        for path in files:
            for value in string_constants(path):
                if value.strip() in self.FORBIDDEN_ARGV:
                    offenders.append("%s: %r" % (path.name, value))
            if "gh " in path.read_text(errors="replace"):
                offenders.append("%s invokes gh" % path.name)
        self.assertEqual(offenders, [], "\n".join(offenders))

    def test_ac_dt_12c_general_mode_writes_only_the_skeleton(self):
        """Verified by running against a fixture repository and diffing the tree."""
        before = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        rc, out, err = self.general("--write")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        after = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        added = sorted(set(after) - set(before))
        changed = sorted(k for k in set(after) & set(before) if after[k] != before[k])
        self.assertEqual(
            added, [GENERAL_RELPATH.replace("/", "/")], "unexpected writes: %r" % added
        )
        self.assertEqual(changed, [], "the generator modified files it did not create")

    def test_ac_dt_12c_stdout_mode_writes_nothing_at_all(self):
        before = snapshot_tree(self.repo, skip=[self.repo / ".git"])
        self.skeleton()
        self.assertEqual(
            snapshot_tree(self.repo, skip=[self.repo / ".git"]),
            before,
            "the generator wrote to the tree without --write",
        )

    def test_ac_dt_12a_the_generator_never_stages_or_commits(self):
        before_head = head_sha(self.repo, env=self.env)
        rc, out, err = self.general("--write")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(
            (self.repo / GENERAL_RELPATH).is_file(), "--write produced no file"
        )
        self.assertEqual(head_sha(self.repo, env=self.env), before_head)
        staged = git(
            self.repo, "diff", "--cached", "--name-only", env=self.env, check=True
        )[1]
        self.assertEqual(staged.strip(), "")


class TestCycleMode(DirectiveTestCase):
    """AC-DT-14 and AC-DT-15 — the G0 migration."""

    def open_cycle(self, binary, *args):
        return run_dt(binary, *args, cwd=self.repo, env=self.env) if binary == "directive" \
            else run_dt(binary, *args, cwd=self.repo, env=self.env)

    def test_ac_dt_14_the_cycle_skeleton_carries_route_and_model_and_no_track(self):
        """AC-DT-14 as agreed. Expected red against the TRD's current design:
        §3.3's cycle-mode region table has no route-and-model region, and states
        so — "general mode's region 2, `ROUTE AND MODEL`, has no counterpart
        either". Written to the criterion, per DEC of 2026-08-28."""
        text = self.cycle_directive(
            "--cycle", "7", "--title", "T", "--date", "2026-08-28",
            "--route", "fresh", "--model", "Opus 5", "docs/companion-a.md",
        )
        self.assertIn("Route:", text, "the cycle skeleton carries no Route (DEC-000180)")
        self.assertIn("Model:", text, "the cycle skeleton carries no Model (DEC-000180)")
        self.assertNotIn("Track:", text, "DEC-000180 retired Track")

    def test_ac_dt_14_bin_holds_exactly_one_directive_skeleton_generator(self):
        """`bin/cycle-open` no longer emits a skeleton of its own (a forwarder)."""
        source = (BIN_DIR / "cycle-open").read_text(errors="replace")
        self.assertNotIn(
            "def render_directive",
            source,
            "bin/cycle-open still emits a skeleton of its own; after the migration "
            "it forwards argv and nothing else",
        )

    def test_ac_dt_15_cycle_mode_preserves_ac_co_1_and_ac_co_3(self):
        """Representative AC-CO criteria through `bin/directive`.

        The full discharge is `bin/tests/test_cycle_open.py` parameterized over
        the binary name at migration step 3 (TRD §3.9); that suite is the
        migration's evidence and is not restated here.
        """
        text = self.cycle_directive(
            "--cycle", "7", "--title", "Streamlining", "--date", "2026-08-01",
            "docs/companion-a.md",
        )
        self.assertIn("# Cycle 7 Directive — Streamlining", text)
        self.assertIn("Date: 2026-08-01", text)
        self.assertIn("Documents in scope:", text)
        self.assertIn("## Decisions", text)
        self.assertIn("## Deferred / out of scope", text)
        self.assertIn("## Execution notes", text)
        self.assertRegex(text, r"- docs/companion-a\.md @ [0-9a-f]{40}")

    def test_ac_dt_15_cycle_mode_stages_nothing_ac_co_11(self):
        before_head = head_sha(self.repo, env=self.env)
        self.cycle_directive(
            "--cycle", "7", "--title", "T", "--date", "2026-08-01", "docs/companion-a.md"
        )
        self.assertEqual(head_sha(self.repo, env=self.env), before_head)
        status = porcelain(self.repo, env=self.env)
        modified = [l for l in status.splitlines() if not l.startswith("??")]
        self.assertEqual(modified, [], "documents were modified: %r" % status)


if __name__ == "__main__":
    unittest.main()
