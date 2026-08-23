"""AC-BN-10: `bin/bundle` — regression guard retained across the AC-BA-*
audience-bundle rewrite.

Contract: `docs/cycles/bundle-audience-coder-20260823T045135Z.md`. The
positional path-following closure mode (`depends-on`/body-reference walk,
`--format`/`--max-depth`/`--why`/`--strict`/`--write`) is retired by
AC-BA-7; every test that exercised it is deleted. `TestAgainstThisRepository`
is kept, unmodified, as a named exception: the two pre-existing failures it
produces (now against the removed positional-entry mode rather than their
prior cause) are the "two pre-existing test_bn10 failures" the retiring
directive names explicitly.
"""

from __future__ import annotations

import unittest

from tests.helpers import REPO_ROOT, base_env, run_cli


class TestAgainstThisRepository(unittest.TestCase):
    """AC-BN-10 runs against the real methodology repo. Read-only."""

    def setUp(self):
        self.env = base_env(methodology_home=REPO_ROOT)

    def bundle(self, *args):
        return run_cli("bundle", *args, cwd=REPO_ROOT, env=self.env)

    def test_bn10_bundle_base_yields_exactly_itself(self):
        """AC-BN-10(a): `bundle base` yields exactly `context-sets/base.md`.

        Tightened from `assertIn` to `assertEqual` when §3.7 was revised:
        `base.md` declares `depends-on: []` and cites no documents, so a
        closure returning anything more is over-collecting.
        """
        rc, out, err = self.bundle("base")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        self.assertEqual(
            [l for l in out.splitlines() if l.strip()], ["context-sets/base.md"]
        )

    def test_bn10_transitive_body_references_are_followed_in_this_repo(self):
        """AC-BN-10: `policies/source-of-truth-policy.md` is reachable from `operating-model.md`.

        The spec's regression anchor. Note that it is asserted from
        `operating-model.md`, which is where that reference actually lives;
        `context-sets/base.md` declares `depends-on: []` and cites no
        documents, so nothing is reachable from `base` alone.
        """
        rc, out, err = self.bundle("operating-model.md")
        self.assertEqual(rc, 0, "stdout=%r stderr=%r" % (out, err))
        paths = out.splitlines()
        self.assertIn("operating-model.md", paths)
        self.assertIn("policies/source-of-truth-policy.md", paths)


if __name__ == "__main__":
    unittest.main()
