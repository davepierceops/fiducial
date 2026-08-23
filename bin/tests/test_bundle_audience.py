"""AC-BA-*: `bin/bundle --audience <value>` — audience-scoped document bundle.

Contract: `docs/cycles/bundle-audience-tests-20260823T043025Z.md` (this
suite's directive file, landed at `5feddbf596815db843c5c262f4c88a2ee6c146ba`)
and `OPEN-ITEMS.md`, "`bin/bundle`'s path-following closure mode is retired,
replaced in Pass 2 by audience selection". Those are the spec; the `AC-BA-`
prefix is local to this suite because the work is dispatched from a directive
rather than from `docs/packages/package-a-spec.md`, on the same pattern
`test_expedited_log.py` establishes for `AC-EL-` (its own docstring: "the
`AC-EL-` prefix is local to this suite because the work is dispatched from the
tracker entry rather than from `docs/packages/package-a-spec.md`").

- **AC-BA-1** The governed file set is exactly: every file matched by
  `bin/check-frontmatter`'s configured in-scope globs (read at runtime from
  `policies/document-metadata-policy.md` §Scope, via `aimeta.scope`), union
  `docs/global-context/**`, `engagements/**`, and `prose-criteria.md`.
  Nothing under `docs/history/`, `docs/batons/`, `docs/cycles/`, `reviews/`,
  `retros/`, `decisions/`, or an adapter file (e.g. `CLAUDE.md`) is ever a
  candidate, even when it carries an `audience:` field.
- **AC-BA-2** A governed file is a member of bundle `<value>` when its
  `audience:` field contains `<value>` literally, or contains `all-roles`, or
  contains `all-decision-roles` and `<value>` is the basename slug of a role
  document whose frontmatter has `session: decision`. A role document is one
  whose first top-level heading is `# Role:`, under `roles/` or
  `engagements/` (including `engagements/sre/`) — the discrimination
  `aimeta.repo.role_slugs`/`_is_role_document` already applies.
- **AC-BA-3** Members are ordered ascending by `order:` where present; members
  without `order:` sort after every member that has one; ties (equal `order:`,
  or both absent) break by path, ascending.
- **AC-BA-4** Output is one self-contained document. Its header stamps the
  repo (`davepierceops/fiducial`), the `HEAD` commit SHA, a generation
  timestamp, and the ordered file list with each file's own blob SHA. Each
  embedded file is preceded by a separator naming its path and blob SHA, in
  the same shape `bin/bundle-methodology` emits today (its `BAR` /
  `<!-- FILE i/N: path @ sha -->` / `BAR` triple). `--out <dir>` writes
  `<dir>/bundle-<value>-<timestamp>.md`; without `--out`, the document goes to
  stdout instead.
- **AC-BA-5** `bin/bundle --list` emits every valid audience value: the
  basename slug of every role document under `roles/` or `engagements/` (as
  `aimeta.repo.role_slugs`/`_is_role_document` discriminates), plus the three
  reserved values (`all-roles`, `all-decision-roles`, `human` — the set named
  in `policies/document-metadata-policy.md` §Required fields), plus every
  literal `audience:` value present in any governed file — deduplicated, one
  per line, sorted, exit 0. Amendment 1 to
  `docs/cycles/bundle-audience-coder-20260823T045135Z.md` adds the
  role-document-slug member to what was, pre-amendment, literal values plus
  the three reserved values only.
- **AC-BA-6** `bin/bundle --audience <value>` for a `<value>` outside the set
  AC-BA-5 would list exits non-zero, naming `<value>` in its message.
- **AC-BA-7** The positional path-following closure mode (`bin/bundle ENTRY
  [ENTRY ...]`, today's `--depends-on`/body-reference walk) is removed;
  invoking `bin/bundle` with a positional entry and no `--audience`/`--list`
  exits non-zero with a message pointing at `--audience`.
- **AC-BA-8** Python stdlib only, and the same interpreter version check as
  the existing `bin/` scripts. *No dedicated test below*: `bin/tests/
  test_cross_cutting.py`'s `test_x2_every_import_is_stdlib_or_local`
  (`AC-X-2`) already statically scans every file directly under `bin/`,
  `bin/bundle` included, for non-stdlib imports, so a second copy of that scan
  here would test nothing new. On the "same interpreter version check": no
  existing `bin/` script performs a *runtime* `sys.version_info` check —
  confirmed by grep across `bin/bundle`, `bin/bundle-methodology`,
  `bin/check-frontmatter`, `bin/flip-agreed`, `bin/cycle-open`,
  `bin/migrate-frontmatter`, `bin/install-hooks`, and `bin/aimeta/*.py`; the
  only stated version constraint is `docs/packages/package-a-spec.md`'s "Python
  3 (>= 3.9)" prose and each script's `#!/usr/bin/env python3` shebang. "Same
  check as the existing scripts" is therefore satisfied by adding none, which
  a test cannot meaningfully assert as red — *inferred*, not *told*; flagged
  for Dave in this branch's report rather than encoded as a test that would
  pass vacuously against the stub below.

Fixture trees only, never the live repo (`AC-BA-2`'s `session: decision` case
does not exist on any real role document today, so it is tested only against
a fixture role document built for it — *observed* via `grep -rn '^session:'
roles/*.md engagements/*.md engagements/sre/*.md`, zero matches).
"""

from __future__ import annotations

import re
import unittest

from tests.helpers import (
    base_env,
    commit,
    frontmatter_block,
    make_home,
    make_repo,
    no_traceback,
    run_cli,
    temp_dir,
    write,
)


# --------------------------------------------------------------- fixture docs


def doc(audience, order=None, body="\nProse.\n", **extra_fields):
    """A minimal governed document: valid lifecycle frontmatter plus `audience:`."""
    fields = dict(
        status="agreed",
        last_reviewed="reviews/sample-review.md @ abc1234",
        audience=list(audience),
    )
    if order is not None:
        fields["order"] = order
    fields.update(extra_fields)
    return frontmatter_block(**fields) + body


def role_doc(slug, session=None, heading="# Role: %s"):
    """A role-shaped document: first heading `# Role: <slug>`, optional `session:`."""
    fields = dict(
        status="agreed",
        last_reviewed="reviews/sample-review.md @ abc1234",
        audience=["all-roles"],
    )
    if session is not None:
        fields["session"] = session
    body = "\n%s\n\nRole prose.\n" % (heading % slug)
    return frontmatter_block(**fields) + body


#: A separator matcher for one embedded file, in `bundle-methodology`'s shape:
#: a `BAR` line, a `<!-- FILE i/N: path @ sha -->` line, another `BAR` line.
def separator_re(path, index=None, total=None):
    idx = r"\d+" if index is None else str(index)
    tot = r"\d+" if total is None else str(total)
    return re.compile(
        r"<!-- =+ -->\n<!-- FILE %s/%s: %s @ [0-9a-f]{7,40} -->\n<!-- =+ -->"
        % (idx, tot, re.escape(path))
    )


class BundleAudienceTestCase(unittest.TestCase):
    """Shared governed-set fixture used by most AC-BA-1/2/3/4 tests.

    One file per governed root (policy-glob, `docs/global-context/`,
    `engagements/`, `prose-criteria.md`), plus one file under each excluded
    root (AC-BA-1's negative list) and an adapter-shaped file at the repo
    root. Every excluded/adapter file carries a value unique to itself
    (`excluded-<slug>`) so its absence from `--list`/a bundle is a positive
    assertion, not just "nothing broke".
    """

    TARGET = "widget-role"

    EXCLUDED_FIXTURES = {
        "docs/history/old.md": "excluded-history",
        "docs/batons/baton-1.md": "excluded-batons",
        "docs/cycles/cycle-9-directive.md": "excluded-cycles",
        "reviews/some-review.md": "excluded-reviews",
        "retros/retro-1.md": "excluded-retros",
        "decisions/log.md": "excluded-decisions",
    }

    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

        # Governed roots: one file each, all carrying TARGET so a single
        # `--audience widget-role` run proves the whole governed set.
        write(self.repo, "policies/glob-member.md", doc([self.TARGET]))
        write(self.repo, "docs/global-context/extra.md", doc([self.TARGET]))
        write(self.repo, "engagements/some-engagement.md", doc([self.TARGET]))
        write(self.repo, "prose-criteria.md", doc([self.TARGET]))

        # Excluded roots: same audience value would make them members if the
        # governed-set boundary leaked.
        for relpath, value in self.EXCLUDED_FIXTURES.items():
            write(self.repo, relpath, doc([self.TARGET, value]))

        # An adapter-shaped file at the repo root — out of scope per the
        # metadata policy's "Adapters" carve-out, and not one of the three
        # extra roots either.
        write(self.repo, "CLAUDE.md", doc([self.TARGET, "excluded-adapter"]))

        self.head = commit(self.repo, "seed governed-set fixture", env=self.env)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)


# --------------------------------------------------------------- AC-BA-1


class TestGovernedFileSet(BundleAudienceTestCase):
    def test_ba1_policy_glob_member_is_governed(self):
        """AC-BA-1: a file matched by check-frontmatter's configured globs is a candidate."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/glob-member.md", out)

    def test_ba1_docs_global_context_is_governed(self):
        """AC-BA-1: `docs/global-context/**` is a governed root even though it
        is not one of check-frontmatter's configured globs."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("docs/global-context/extra.md", out)

    def test_ba1_engagements_is_governed(self):
        """AC-BA-1: `engagements/**` is a governed root."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("engagements/some-engagement.md", out)

    def test_ba1_prose_criteria_is_governed(self):
        """AC-BA-1: `prose-criteria.md` is a governed file."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("prose-criteria.md", out)

    def test_ba1_excluded_roots_never_appear(self):
        """AC-BA-1: docs/history, docs/batons, docs/cycles, reviews, retros,
        decisions are never candidates, whatever their `audience:` says."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        for relpath in self.EXCLUDED_FIXTURES:
            self.assertNotIn(relpath, out, "%s leaked into the governed set" % relpath)

    def test_ba1_adapter_file_never_appears(self):
        """AC-BA-1: an adapter-shaped file at the repo root is never a candidate."""
        rc, out, err = self.bundle("--audience", self.TARGET)
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertNotIn("CLAUDE.md", out)

    def test_ba1_excluded_values_absent_from_list(self):
        """AC-BA-1, cross-checked via AC-BA-5: --list never surfaces a value
        that appears only on an excluded/adapter document."""
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        values = out.splitlines()
        for excluded_value in list(self.EXCLUDED_FIXTURES.values()) + ["excluded-adapter"]:
            self.assertNotIn(excluded_value, values)


# --------------------------------------------------------------- AC-BA-2


class TestMembership(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def seed(self, extra_docs, commit_msg="seed membership fixture"):
        for relpath, text in extra_docs.items():
            write(self.repo, relpath, text)
        commit(self.repo, commit_msg, env=self.env)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def test_ba2_direct_value_is_a_member(self):
        """AC-BA-2: `audience:` containing the requested value literally is a member."""
        self.seed({"policies/direct.md": doc(["target-role"])})
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/direct.md", out)

    def test_ba2_non_matching_value_is_excluded(self):
        """AC-BA-2: a document whose `audience:` names neither the value nor
        `all-roles` is not a member.

        `policies/keeps-value-known.md` keeps `target-role` in AC-BA-5's known
        set (Amendment 1) — otherwise AC-BA-6 (unknown value) would fire
        before the membership rule this test is about ever runs, as
        `test_ba2_all_decision_roles_selects_a_decision_session_role_slug`'s
        docstring already notes for its own fixture.
        """
        self.seed(
            {
                "policies/other.md": doc(["some-other-role"]),
                "policies/keeps-value-known.md": doc(["target-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertNotIn("policies/other.md", out)

    def test_ba2_all_roles_is_always_a_member(self):
        """AC-BA-2: `audience: [all-roles]` is a member of any requested bundle.

        `policies/keeps-value-known.md` keeps `target-role` in AC-BA-5's known
        set (Amendment 1), for the same reason as
        `test_ba2_non_matching_value_is_excluded`.
        """
        self.seed(
            {
                "policies/broad.md": doc(["all-roles"]),
                "policies/keeps-value-known.md": doc(["target-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/broad.md", out)

    def test_ba2_all_decision_roles_selects_a_decision_session_role_slug(self):
        """AC-BA-2: `all-decision-roles` is a member when <value> is the slug of
        a role document whose frontmatter has `session: decision`.

        `policies/keeps-value-known.md` keeps `widget-role` in AC-BA-5's known
        set — otherwise AC-BA-6 (unknown value) would fire before the
        membership rule this test is about ever runs.
        """
        self.seed(
            {
                "roles/widget-role.md": role_doc("widget-role", session="decision"),
                "policies/for-decision-roles.md": doc(["all-decision-roles"]),
                "policies/keeps-value-known.md": doc(["widget-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "widget-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/for-decision-roles.md", out)

    def test_ba2_all_decision_roles_excludes_a_non_decision_session_role(self):
        """AC-BA-2: a role document without `session: decision` does not grant
        `all-decision-roles` membership for its slug."""
        self.seed(
            {
                "roles/exec-role.md": role_doc("exec-role", session="execution"),
                "policies/for-decision-roles.md": doc(["all-decision-roles"]),
                "policies/keeps-value-known.md": doc(["exec-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "exec-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertNotIn("policies/for-decision-roles.md", out)

    def test_ba2_all_decision_roles_requires_a_role_document_not_any_slug(self):
        """AC-BA-2: `all-decision-roles` grants nothing for a value that is not
        the slug of any role document, decision-session or not."""
        self.seed(
            {
                "policies/for-decision-roles.md": doc(["all-decision-roles"]),
                "policies/keeps-value-known.md": doc(["no-such-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "no-such-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertNotIn("policies/for-decision-roles.md", out)

    def test_ba2_all_decision_roles_via_an_engagements_role_document(self):
        """AC-BA-2: a role document under `engagements/` counts too, per
        `aimeta.repo.role_slugs`."""
        self.seed(
            {
                "engagements/widget-role.md": role_doc("widget-role", session="decision"),
                "policies/for-decision-roles.md": doc(["all-decision-roles"]),
                "policies/keeps-value-known.md": doc(["widget-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "widget-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/for-decision-roles.md", out)

    def test_ba2_a_document_without_the_role_heading_is_not_a_role_document(self):
        """AC-BA-2: `session: decision` on a `roles/*.md` file with no
        `# Role:` heading does not make it a role document (the discrimination
        `aimeta.repo._is_role_document` already applies)."""
        self.seed(
            {
                "roles/widget-role.md": role_doc(
                    "widget-role", session="decision", heading="# Not A Role Heading %s"
                ),
                "policies/for-decision-roles.md": doc(["all-decision-roles"]),
                "policies/keeps-value-known.md": doc(["widget-role"]),
            }
        )
        rc, out, err = self.bundle("--audience", "widget-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertNotIn("policies/for-decision-roles.md", out)

    def test_ba2_block_list_audience_form_is_read_the_same_as_inline(self):
        """AC-BA-2: YAML block-list `audience:` (one `- value` per line, as
        `test_bundle_methodology.py`'s SKILL_GAMMA fixture uses) is read
        identically to the inline `[value, ...]` form."""
        write(
            self.repo,
            "policies/block-list.md",
            "---\n"
            "status: agreed\n"
            "last-reviewed: reviews/sample-review.md @ abc1234\n"
            "audience:\n"
            "- target-role\n"
            "---\n"
            "\nProse.\n",
        )
        commit(self.repo, "seed block-list fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/block-list.md", out)


# --------------------------------------------------------------- AC-BA-3


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def member_order(self, out, paths):
        """The order `paths` appear in `out`, as a list of (path, index)."""
        return sorted(paths, key=lambda p: out.index(p))

    def test_ba3_ascending_order_field_is_honored(self):
        """AC-BA-3: members with `order:` sort ascending by that value.

        Paths deliberately contradict path order (`aaa-high` < `zzz-low`
        alphabetically) so a path-only sort cannot satisfy this by accident.
        """
        write(self.repo, "policies/aaa-high.md", doc(["target-role"], order=5))
        write(self.repo, "policies/zzz-low.md", doc(["target-role"], order=1))
        commit(self.repo, "seed order fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertLess(out.index("policies/zzz-low.md"), out.index("policies/aaa-high.md"))

    def test_ba3_members_without_order_sort_after_ordered_members(self):
        """AC-BA-3: a member with no `order:` comes after every member that has one."""
        write(self.repo, "policies/z-ordered.md", doc(["target-role"], order=99))
        write(self.repo, "policies/a-unordered.md", doc(["target-role"]))
        commit(self.repo, "seed order fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertLess(
            out.index("policies/z-ordered.md"), out.index("policies/a-unordered.md")
        )

    def test_ba3_ties_in_order_break_by_path(self):
        """AC-BA-3: equal `order:` values break the tie by path, ascending."""
        write(self.repo, "policies/b.md", doc(["target-role"], order=1))
        write(self.repo, "policies/a.md", doc(["target-role"], order=1))
        commit(self.repo, "seed order-tie fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertLess(out.index("policies/a.md"), out.index("policies/b.md"))

    def test_ba3_ties_with_no_order_break_by_path(self):
        """AC-BA-3: two members with no `order:` at all break the tie by path."""
        write(self.repo, "policies/z-unordered.md", doc(["target-role"]))
        write(self.repo, "policies/a-unordered.md", doc(["target-role"]))
        commit(self.repo, "seed order-tie fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertLess(
            out.index("policies/a-unordered.md"), out.index("policies/z-unordered.md")
        )

    def test_ba3_full_ordering_across_all_four_cases(self):
        """AC-BA-3: ordered-ascending, then unordered-by-path, end to end.

        Paths deliberately contradict path order within and across the
        ordered/unordered groups (`aaa-high-order` sorts first alphabetically
        but must land after the `order: 1` pair) so a path-only sort cannot
        satisfy this by accident.
        """
        write(self.repo, "policies/aaa-high-order.md", doc(["target-role"], order=5))
        write(self.repo, "policies/zzz-tie-b.md", doc(["target-role"], order=1))
        write(self.repo, "policies/aaa-tie-a.md", doc(["target-role"], order=1))
        write(self.repo, "policies/zzz-unordered.md", doc(["target-role"]))
        write(self.repo, "policies/aaa-unordered.md", doc(["target-role"]))
        commit(self.repo, "seed full-order fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        expected = [
            "policies/aaa-tie-a.md",
            "policies/zzz-tie-b.md",
            "policies/aaa-high-order.md",
            "policies/aaa-unordered.md",
            "policies/zzz-unordered.md",
        ]
        positions = [out.index(p) for p in expected]
        self.assertEqual(positions, sorted(positions), "order was: %r" % positions)


# --------------------------------------------------------------- AC-BA-4


class TestOutputFormat(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        write(self.repo, "policies/one.md", doc(["target-role"], order=1))
        write(self.repo, "policies/two.md", doc(["target-role"], order=2))
        self.head = commit(self.repo, "seed output-format fixture", env=self.env)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def test_ba4_header_names_the_repo(self):
        """AC-BA-4: the header stamp names `davepierceops/fiducial`."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("davepierceops/fiducial", out)

    def test_ba4_header_names_the_head_sha(self):
        """AC-BA-4: the header stamp names the `HEAD` commit SHA."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn(self.head, out)

    def test_ba4_header_carries_a_generation_timestamp(self):
        """AC-BA-4: the header stamp carries a generation timestamp."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        header = out.split("<!-- FILE", 1)[0]
        self.assertRegex(header, r"\d{4}-\d{2}-\d{2}")

    def test_ba4_header_lists_files_with_blob_shas(self):
        """AC-BA-4: the header's file list carries each file's own blob SHA."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        header = out.split("<!-- FILE", 1)[0]
        self.assertRegex(header, r"policies/one\.md.*[0-9a-f]{7,40}")

    def test_ba4_each_file_is_preceded_by_a_bundle_methodology_shaped_separator(self):
        """AC-BA-4: each embedded file's separator matches `bundle-methodology`'s
        `BAR` / `<!-- FILE i/N: path @ sha -->` / `BAR` shape."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertRegex(out, separator_re("policies/one.md", 1, 2))
        self.assertRegex(out, separator_re("policies/two.md", 2, 2))

    def test_ba4_without_out_the_document_goes_to_stdout(self):
        """AC-BA-4: absent `--out`, the rendered bundle is stdout, not a file."""
        rc, out, err = self.bundle("--audience", "target-role")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("policies/one.md", out)
        self.assertTrue((self.repo).is_dir())
        self.assertFalse(
            any(p.name.startswith("bundle-target-role-") for p in self.repo.glob("*.md"))
        )

    def test_ba4_out_dir_writes_the_conventional_filename(self):
        """AC-BA-4: `--out <dir>` writes `<dir>/bundle-<value>-<timestamp>.md`."""
        out_dir = temp_dir(self, "bundle-audience-out-")
        rc, out, err = self.bundle("--audience", "target-role", "--out", str(out_dir))
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        files = list(out_dir.glob("bundle-target-role-*.md"))
        self.assertEqual(len(files), 1, "found %r in %s" % (files, out_dir))
        self.assertRegex(files[0].name, r"^bundle-target-role-\d{8}T\d{6}\.md$")

    def test_ba4_out_dir_file_contains_the_same_document_as_stdout(self):
        """AC-BA-4: the `--out` file and the stdout form carry the same bundle."""
        out_dir = temp_dir(self, "bundle-audience-out-")
        rc, _, err = self.bundle("--audience", "target-role", "--out", str(out_dir))
        self.assertEqual(rc, 0, "stderr=%r" % err)
        files = list(out_dir.glob("bundle-target-role-*.md"))
        self.assertEqual(len(files), 1)
        written = files[0].read_text(encoding="utf-8")

        rc2, stdout_out, err2 = self.bundle("--audience", "target-role")
        self.assertEqual(rc2, 0, "stderr=%r" % err2)
        self.assertEqual(written, stdout_out)


# --------------------------------------------------------------- AC-BA-5


class TestList(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def test_ba5_list_surfaces_a_literal_governed_value(self):
        """AC-BA-5: --list surfaces a literal `audience:` value from a governed file."""
        write(self.repo, "policies/one.md", doc(["widget-role"]))
        commit(self.repo, "seed list fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("widget-role", out.splitlines())

    def test_ba5_list_is_sorted(self):
        """AC-BA-5: --list output is sorted."""
        write(self.repo, "policies/one.md", doc(["zeta-role", "alpha-role"]))
        commit(self.repo, "seed list fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        lines = out.splitlines()
        self.assertEqual(lines, sorted(lines))

    def test_ba5_list_deduplicates_across_files(self):
        """AC-BA-5: a value repeated across files appears once in --list."""
        write(self.repo, "policies/one.md", doc(["widget-role"]))
        write(self.repo, "policies/two.md", doc(["widget-role"]))
        commit(self.repo, "seed list-dedup fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        lines = out.splitlines()
        self.assertEqual(lines.count("widget-role"), 1)

    def test_ba5_list_always_includes_the_three_reserved_values(self):
        """AC-BA-5: `all-roles`, `all-decision-roles`, `human` are always listed,
        even with no governed file naming them."""
        write(self.repo, "policies/one.md", doc(["widget-role"]))
        commit(self.repo, "seed list fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        lines = set(out.splitlines())
        self.assertEqual(
            {"all-roles", "all-decision-roles", "human"} - lines,
            set(),
            "missing reserved value(s); got %r" % lines,
        )

    def test_ba5_list_exits_zero(self):
        """AC-BA-5: --list exits 0."""
        write(self.repo, "policies/one.md", doc(["widget-role"]))
        commit(self.repo, "seed list fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertTrue(no_traceback(out, err))

    def test_ba5_list_includes_a_role_document_slug_with_no_literal_reference(self):
        """AC-BA-5, Amendment 1: a role document's basename slug is listed even
        when no governed file's `audience:` names it literally."""
        write(self.repo, "roles/widget-role.md", role_doc("widget-role"))
        write(self.repo, "policies/unrelated.md", doc(["some-other-value"]))
        commit(self.repo, "seed role-slug list fixture", env=self.env)
        rc, out, err = self.bundle("--list")
        self.assertEqual(rc, 0, "stderr=%r" % err)
        self.assertIn("widget-role", out.splitlines())


# --------------------------------------------------------------- AC-BA-6


class TestInvalidAudienceValue(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        write(self.repo, "policies/one.md", doc(["widget-role"]))
        commit(self.repo, "seed fixture", env=self.env)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def test_ba6_unknown_value_exits_non_zero(self):
        """AC-BA-6: a value outside AC-BA-5's set exits non-zero."""
        rc, out, err = self.bundle("--audience", "no-such-audience-value")
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

    def test_ba6_unknown_value_is_named_in_the_message(self):
        """AC-BA-6: the failure message names the offending value, as a clean
        diagnostic rather than an unhandled exception."""
        rc, out, err = self.bundle("--audience", "no-such-audience-value")
        self.assertIn("no-such-audience-value", out + err)
        self.assertTrue(no_traceback(out, err))

    def test_ba6_a_role_document_slug_is_valid_with_no_literal_reference(self):
        """AC-BA-6, Amendment 1: a role document's basename slug is a valid
        `--audience` value even when no governed file's `audience:` names it
        literally — it is a member of AC-BA-5's set by role-document slug
        alone, so AC-BA-6 does not reject it."""
        write(self.repo, "roles/widget-role.md", role_doc("widget-role"))
        commit(self.repo, "seed role-slug validity fixture", env=self.env)
        rc, out, err = self.bundle("--audience", "widget-role")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))


# --------------------------------------------------------------- AC-BA-7


class TestPositionalModeRemoved(unittest.TestCase):
    def setUp(self):
        self.home = make_home(self)
        self.repo = make_repo(self)
        self.env = base_env(methodology_home=self.home)
        write(self.repo, "context-sets/entry.md", doc(["all-roles"]))
        commit(self.repo, "seed fixture", env=self.env)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=self.repo, env=self.env)

    def test_ba7_positional_entry_exits_non_zero(self):
        """AC-BA-7: `bundle ENTRY` (the old closure mode) exits non-zero."""
        rc, out, err = self.bundle("entry")
        self.assertNotEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))

    def test_ba7_positional_entry_message_points_at_audience(self):
        """AC-BA-7: the rejection message points the caller at `--audience`, as
        a clean diagnostic rather than an unhandled exception."""
        rc, out, err = self.bundle("entry")
        self.assertIn("--audience", out + err)
        self.assertTrue(no_traceback(out, err))


if __name__ == "__main__":
    unittest.main()
