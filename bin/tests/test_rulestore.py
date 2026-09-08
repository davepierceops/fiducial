"""AC-RS-*: the rule-store processing modules, over rows built in memory.

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT" and § "ACCEPTANCE CRITERIA" — this suite's directive file, landed at
`d5b643b48cf0285194d29b09f6755db1b8a16b34`. The `AC-RS-` prefix is the PRD's,
carried into the directive because the PRD itself is not on `main`; the same
pattern `test_bundle_audience.py` establishes for `AC-BA-`.

Backing decisions: DEC-000400 (the row), DEC-000410 (the storage boundary),
DEC-000420 (definitions by term), DEC-000490 (process documents selected by
key), all in `decisions/log.md @ a00deba150c0736f77562ec80d858c3986cd7f11`.

**Nothing in this module touches the filesystem.** AC-RS-4 makes that a
property of the processing layer, not a convenience: every row here is built by
hand and handed to `MemoryRowSource`, so a `query`/`terms`/`keys`/`near`/
`render` that could only work against real files fails here. The one storage
name this module reaches for is `store.normalize_fields`, a pure function over
raw frontmatter values; see NORMALIZATION below.

NORMALIZATION. The contract states the rules ("a value is a list; a bare word is
a list of one; `[a, b]` splits on commas; every element is stripped and
lower-cased; `null` and an empty list are an absent key; `order` parses to int;
any other typed value ... is a defect the source raises `RowShapeError` for,
naming the id and the key") without naming the function that applies them. This
suite fixes it as

    store.normalize_fields(row_id, fields) -> (keys, order)

taking the **raw** value text as it stands after `key: `, quotes included —
because "a quoted number on another key is text" is only decidable before the
quotes come off. `id` and `order` are excluded from `keys`; `order`'s integer
spelling is `bin/aimeta/frontmatter.py`'s `^[+-]?[0-9]+$`. That choice is
reported to the decision session with this branch.
"""

from __future__ import annotations

import dataclasses
import unittest

from rulestore import keys as keys_mod
from rulestore import named_queries
from rulestore import near as near_mod
from rulestore import query, render, store, terms
from rulestore.store import FileRowSource, MemoryRowSource, Row, RowShapeError
from tests.helpers import REPO_ROOT


# --------------------------------------------------------------- fixture rows


def row(row_id, body="Prose.", *, human=None, order=None, kind="rule",
        path=None, blob="0" * 40, **keys):
    """One in-memory `Row`. Keyword keys become the row's normalized key map."""
    normalized = {
        key.replace("_", "-"): ([value] if isinstance(value, str) else list(value))
        for key, value in keys.items()
    }
    return Row(
        id=row_id,
        body=body,
        human=human,
        keys=normalized,
        order=order,
        kind=kind,
        path=path,
        blob=blob,
    )


def definition(row_id, term, body, *, order=None, topic="lexicon"):
    """A definition row: a `term` key and no `role` key (DEC-000420)."""
    return row(row_id, body, order=order, topic=topic,
               term=[term] if isinstance(term, str) else list(term))


def ids(rows):
    return [r.id for r in rows]


# ------------------------------------------------------------------- AC-RS-1


class TestRowShape(unittest.TestCase):
    """AC-RS-1: the row's shape and its frontmatter normalization."""

    def test_ac_rs_1_row_carries_exactly_the_contracted_fields(self):
        """AC-RS-1: `Row` is a dataclass of id/body/human/keys/order/kind/path/blob."""
        self.assertTrue(dataclasses.is_dataclass(Row))
        self.assertEqual(
            [f.name for f in dataclasses.fields(Row)],
            ["id", "body", "human", "keys", "order", "kind", "path", "blob"],
        )

    def test_ac_rs_1_a_bare_word_normalizes_to_a_list_of_one(self):
        """AC-RS-1: every value is a list of words; a bare word is a list of one."""
        keys, _ = store.normalize_fields("R0001", {"verb": "require"})
        self.assertEqual(keys, {"verb": ["require"]})

    def test_ac_rs_1_a_bracket_list_splits_on_commas_and_lower_cases(self):
        """AC-RS-1: `[a, b]` splits on commas; every element is stripped and lowered."""
        keys, _ = store.normalize_fields(
            "R0002", {"role": "[ Writer,  COPY-editor ]", "corpus": "[software]"}
        )
        self.assertEqual(keys, {"role": ["writer", "copy-editor"], "corpus": ["software"]})

    def test_ac_rs_1_a_typed_value_inside_a_bracket_list_is_also_a_defect(self):
        """AC-RS-1/Q7: bracketing a typed value must not hide the defect."""
        with self.assertRaises(RowShapeError) as caught:
            store.normalize_fields("R0009", {"weight": "[12, true]"})
        self.assertIn("R0009", str(caught.exception))
        self.assertIn("weight", str(caught.exception))

    def test_ac_rs_1_a_quoted_comma_inside_a_list_element_is_not_split(self):
        """AC-RS-1/S4: `["a, b", c]` keeps the quoted comma inside its item,
        instead of the scalar branch's correct handling and the list
        branch's naive `str.split(",")` disagreeing."""
        keys, _ = store.normalize_fields("R0010", {"topic": '["a, b", c]'})
        self.assertEqual(keys, {"topic": ["a, b", "c"]})

    def test_ac_rs_1_null_and_the_empty_list_are_an_absent_key(self):
        """AC-RS-1: `null` and an empty list carry no key at all."""
        keys, _ = store.normalize_fields(
            "R0003", {"term": "null", "session": "[]", "topic": "core"}
        )
        self.assertEqual(keys, {"topic": ["core"]})

    def test_ac_rs_1_order_parses_to_an_int_and_is_not_a_key(self):
        """AC-RS-1: `order` is the one numeric key, and it is not part of `keys`."""
        keys, order = store.normalize_fields("R0004", {"order": "360", "topic": "core"})
        self.assertEqual(order, 360)
        self.assertIsInstance(order, int)
        self.assertEqual(keys, {"topic": ["core"]})

    def test_ac_rs_1_id_is_never_a_key_and_an_absent_order_is_none(self):
        """AC-RS-1: `id` is excluded from `keys`; a row with no `order` carries None."""
        keys, order = store.normalize_fields("R0005", {"id": "R0005", "topic": "core"})
        self.assertIsNone(order)
        self.assertEqual(keys, {"topic": ["core"]})

    def test_ac_rs_1_a_non_integer_order_is_a_defect_naming_id_and_key(self):
        """AC-RS-1: a value the dialect cannot type is a defect, not a silent None."""
        with self.assertRaises(RowShapeError) as caught:
            store.normalize_fields("R0006", {"order": "twenty"})
        message = str(caught.exception)
        self.assertIn("R0006", message)
        self.assertIn("order", message)

    def test_ac_rs_1_a_bare_number_on_another_key_is_a_defect(self):
        """AC-RS-1: `order` is the only typed key; a bare number elsewhere is a defect."""
        with self.assertRaises(RowShapeError) as caught:
            store.normalize_fields("R0007", {"weight": "12"})
        self.assertIn("R0007", str(caught.exception))
        self.assertIn("weight", str(caught.exception))

    def test_ac_rs_1_a_quoted_number_on_another_key_is_text(self):
        """AC-RS-1: "a quoted number on another key is text", so it normalizes."""
        keys, _ = store.normalize_fields("R0008", {"source": '"12"'})
        self.assertEqual(keys, {"source": ["12"]})

    def test_ac_rs_1_memory_row_source_returns_exactly_what_it_was_given(self):
        """AC-RS-1/AC-RS-4: `MemoryRowSource` is the identity over its rows."""
        given = [row("R0001", topic="core"), row("R0002", topic="intake")]
        self.assertEqual(MemoryRowSource(given).rows(), given)


# ------------------------------------------------------------------- AC-RS-2


class TestSelect(unittest.TestCase):
    """AC-RS-2: `--where k=v [k=v ...]` over rows, and the result's order."""

    def test_ac_rs_2_parse_where_reads_k_equals_v_tokens(self):
        """AC-RS-2: `parse_where` turns `k=v` tokens into a key-value mapping."""
        self.assertEqual(
            query.parse_where(["role=writer", "corpus=writing"]),
            {"role": "writer", "corpus": "writing"},
        )

    def test_ac_rs_2_a_token_with_no_equals_raises_query_error(self):
        """AC-RS-2: a token with no `=` is a `QueryError`."""
        with self.assertRaises(query.QueryError):
            query.parse_where(["role"])

    def test_ac_rs_2_an_empty_key_raises_query_error(self):
        """AC-RS-2: a token with an empty key is a `QueryError`."""
        with self.assertRaises(query.QueryError):
            query.parse_where(["=writer"])

    def test_ac_rs_2_an_empty_value_raises_query_error(self):
        """AC-RS-2: a token with an empty value is a `QueryError`."""
        with self.assertRaises(query.QueryError):
            query.parse_where(["role="])

    def test_ac_rs_2_an_empty_token_raises_query_error(self):
        """AC-RS-2: an empty token has neither key nor value; a `QueryError`."""
        with self.assertRaises(query.QueryError):
            query.parse_where([""])

    def test_ac_rs_2_a_bare_equals_raises_query_error(self):
        """AC-RS-2: `=` alone has an empty key and an empty value; a `QueryError`."""
        with self.assertRaises(query.QueryError):
            query.parse_where(["="])

    def test_ac_rs_2_a_single_key_selects_the_rows_holding_the_value(self):
        """AC-RS-2: a row matches when the named key's list contains the value."""
        rows = [
            row("R0001", order=10, topic="core", role=["writer", "critic"]),
            row("R0002", order=20, topic="core", role=["coder-agent"]),
            row("R0003", order=30, topic="lexicon"),  # carries no `role` at all
        ]
        self.assertEqual(ids(query.select(rows, {"role": "writer"})), ["R0001"])

    def test_ac_rs_2_multiple_keys_are_conjunctive(self):
        """AC-RS-2: every named key must contain its value."""
        rows = [
            row("R0001", order=10, topic="core", role=["writer"], corpus=["writing"]),
            row("R0002", order=20, topic="core", role=["writer"], corpus=["software"]),
            row("R0003", order=30, topic="core", role=["writer"]),  # no `corpus`
        ]
        selected = query.select(rows, {"role": "writer", "corpus": "writing"})
        self.assertEqual(ids(selected), ["R0001"])

    def test_ac_rs_2_a_missing_key_is_a_non_match(self):
        """AC-RS-2: a row that does not carry the key never matches on it."""
        rows = [
            row("R0001", order=10, topic="core", role=["writer"]),
            row("R0002", order=20, topic="lexicon"),  # no `role` at all
        ]
        self.assertEqual(ids(query.select(rows, {"role": "writer"})), ["R0001"])

    def test_ac_rs_2_with_no_sequence_every_topic_ties_and_sorts_by_name_then_order_then_id(self):
        """AC-RS-2/DEC-000640: no sequence given, every topic is "unnamed" and
        ties at position 0 — the result falls back to name, then order, then id."""
        rows = [
            row("R0009", order=20, topic="zeta", role=["writer"]),
            row("R0003", order=10, topic="beta", role=["writer"]),
            row("R0002", order=10, topic="alpha", role=["writer"]),
            row("R0001", order=10, topic="beta", role=["writer"]),
        ]
        selected = query.select(rows, {"role": "writer"})
        self.assertEqual(ids(selected), ["R0002", "R0001", "R0003", "R0009"])

    def test_ac_rs_2_a_row_without_order_sorts_after_every_integer(self):
        """AC-RS-2: `None` order sorts after every integer, however large.

        Every row shares one topic, so the topic-position/name key ties and
        the order/id tiebreak is isolated.
        """
        rows = [
            row("R0001", order=None, topic="alpha", role=["writer"]),
            row("R0002", order=999, topic="alpha", role=["writer"]),
            row("R0003", order=None, topic="alpha", role=["writer"]),
        ]
        selected = query.select(rows, {"role": "writer"})
        self.assertEqual(ids(selected), ["R0002", "R0001", "R0003"])

    def test_ac_rs_2_a_two_line_sequence_orders_topic_position_ahead_of_order(self):
        """AC-RS-2/DEC-000640: a later-named topic sorts after an earlier one,
        whatever its `order` — the two-line sequence's position dominates."""
        rows = [
            row("R0001", order=1, topic="beta", role=["writer"]),
            row("R0002", order=999, topic="alpha", role=["writer"]),
        ]
        sequences = ([["alpha"], ["beta"]], [])
        selected = query.select(rows, {"role": "writer"}, sequences)
        self.assertEqual(ids(selected), ["R0002", "R0001"])

    def test_ac_rs_2_a_topic_the_sequence_does_not_name_sorts_after_every_named_one(self):
        """AC-RS-2/DEC-000640: an unnamed topic sorts last, ties breaking
        alphabetically by name among the unnamed rows."""
        rows = [
            row("R0001", order=1, topic="zeta", role=["writer"]),
            row("R0002", order=2, topic="yankee", role=["writer"]),
            row("R0003", order=100, topic="alpha", role=["writer"]),
        ]
        sequences = ([["alpha"]], [])
        selected = query.select(rows, {"role": "writer"}, sequences)
        self.assertEqual(ids(selected), ["R0003", "R0002", "R0001"])

    def test_ac_rs_2_a_query_nothing_holds_selects_nothing(self):
        """AC-RS-2: "exactly the rows" — including when that is none of them."""
        rows = [
            row("R0001", order=10, topic="core", role=["writer"]),
            row("R0002", order=20, topic="lexicon"),  # no `role` at all
        ]
        self.assertEqual(query.select(rows, {"role": "nobody"}), [])


# ------------------------------------------------------------------- AC-RS-3


class TestKeysInUse(unittest.TestCase):
    """AC-RS-3: the key census is computed from the rows, never maintained."""

    def test_ac_rs_3_every_key_and_value_is_counted(self):
        """AC-RS-3: every key in use, with every value and the count of rows."""
        rows = [
            row("R0001", order=10, topic="core", role=["writer", "critic"]),
            row("R0002", order=20, topic="core", role=["writer"]),
            row("R0003", order=30, topic="intake", role=["critic"]),
        ]
        self.assertEqual(
            keys_mod.keys_in_use(rows),
            {
                "topic": {"core": 2, "intake": 1},
                "role": {"writer": 2, "critic": 2},
            },
        )

    def test_ac_rs_3_id_and_order_are_excluded(self):
        """AC-RS-3: the two typed keys are not part of the census."""
        census = keys_mod.keys_in_use([row("R0001", order=10, topic="core")])
        self.assertNotIn("id", census)
        self.assertNotIn("order", census)

    def test_ac_rs_3_a_row_carrying_no_keys_contributes_nothing(self):
        """AC-RS-3: computed from the rows given, and from nothing else."""
        self.assertEqual(keys_mod.keys_in_use([row("R0001")]), {})


# ------------------------------------------------------------------ AC-RS-13


class TestPullDefinitions(unittest.TestCase):
    """AC-RS-13 / DEC-000420: definitions are rows pulled in by term."""

    def test_ac_rs_13_a_used_term_pulls_its_definition(self):
        """AC-RS-13: a selected row whose body uses a term pulls that definition."""
        tranche = definition("R0003", "tranche", "A tranche is one workstream.", order=20)
        # `ranch` sits inside `tranche`; whole-word matching must not pull it.
        ranch = definition("R0500", "ranch", "A ranch is not a store term.", order=30)
        selected = [row("R0100", "Open one tranche per delta.", order=10, role=["writer"])]
        pulled = terms.pull_definitions(selected, selected + [tranche, ranch])
        self.assertEqual(ids(pulled), ["R0003"])

    def test_ac_rs_13_a_pulled_definition_pulls_further_definitions(self):
        """AC-RS-13: the scan repeats over pulled bodies until nothing new is added."""
        delta = definition("R0020", "delta", "A delta is a claimed spec change.", order=30)
        claimed = definition("R0012", "claimed", "A document is claimed in an open delta.",
                             order=40)
        selected = [row("R0100", "Open one delta per tranche.", order=10, role=["writer"])]
        pulled = terms.pull_definitions(selected, selected + [delta, claimed])
        self.assertEqual(ids(pulled), ["R0020", "R0012"])

    def test_ac_rs_13_a_term_matches_whole_words_only(self):
        """AC-RS-13: whole-word matching — `row` inside `rowdy` pulls nothing."""
        rowdef = definition("R0030", "row", "A row is one obligation.", order=20)
        selected = [row("R0100", "A rowdy meeting settles nothing.", order=10,
                        role=["writer"])]
        self.assertEqual(terms.pull_definitions(selected, selected + [rowdef]), [])

    def test_ac_rs_13_a_term_is_a_phrase_and_matches_case_insensitively(self):
        """AC-RS-13: each term is a phrase; the match ignores case."""
        phrase = definition("R0040", "spec delta", "A spec delta is an open change.",
                            order=20)
        # `pen` sits inside `open`; a phrase match is still a whole-word match.
        pen = definition("R0501", "pen", "A pen is not a store term.", order=30)
        selected = [row("R0100", "While a Spec Delta is open, edit freely.", order=10,
                        role=["writer"])]
        pulled = terms.pull_definitions(selected, selected + [phrase, pen])
        self.assertEqual(ids(pulled), ["R0040"])

    def test_ac_rs_13_a_definition_is_never_added_twice(self):
        """AC-RS-13: two selected rows using one term add that definition once."""
        tranche = definition("R0003", "tranche", "A tranche is one workstream.", order=20)
        selected = [
            row("R0100", "Open one tranche per delta.", order=10, role=["writer"]),
            row("R0101", "Close the tranche at the end.", order=11, role=["writer"]),
        ]
        self.assertEqual(ids(terms.pull_definitions(selected, selected + [tranche])),
                         ["R0003"])

    def test_ac_rs_13_a_definition_already_selected_is_not_added_again(self):
        """AC-RS-13: definitions already in the selection are not added twice."""
        tranche = definition("R0003", "tranche", "A tranche is one workstream.", order=20)
        delta = definition("R0020", "delta", "A delta is a claimed spec change.", order=30)
        ranch = definition("R0500", "ranch", "A ranch is not a store term.", order=40)
        selected = [row("R0100", "Open one tranche per delta.", order=10, role=["writer"]),
                    tranche]
        pulled = terms.pull_definitions(selected, selected + [delta, ranch])
        self.assertEqual(ids(pulled), ["R0020"])

    def test_ac_rs_13_a_role_less_definition_is_not_selected_by_role(self):
        """AC-RS-13: a definition's role-less shape excludes it from role selection."""
        tranche = definition("R0003", "tranche", "A tranche is one workstream.", order=20)
        ordinary = row("R0100", "Open one tranche.", order=10, role=["writer"])
        self.assertEqual(ids(query.select([tranche, ordinary], {"role": "writer"})),
                         ["R0100"])

    def test_ac_rs_13_a_row_carrying_term_and_a_role_is_not_a_definition(self):
        """AC-RS-13: "a `term` key and no `role` key" — a role disqualifies the row."""
        hybrid = row("R0241", "A critic reads for the reader.", order=20,
                     term=["critic"], role=["critic"])
        # `read` sits inside `reads`; whole-word matching must not pull it either.
        read = definition("R0502", "read", "A read is not a store term.", order=30)
        selected = [row("R0100", "The critic reads last.", order=10, role=["writer"])]
        self.assertEqual(terms.pull_definitions(selected, selected + [hybrid, read]), [])

    def test_ac_rs_13_a_row_carrying_term_and_session_is_not_a_definition(self):
        """AC-RS-13/DEC-000420 (Q4): a `session` key disqualifies a row from
        being a definition, just as `role` and `corpus` do."""
        hybrid = row("R0503", "A note about method.", order=20,
                     term=["method"], session=["execution"])
        selected = [row("R0100", "The method matters.", order=10, role=["writer"])]
        self.assertEqual(terms.pull_definitions(selected, selected + [hybrid]), [])

    def test_ac_rs_13_pulled_definitions_sort_by_order_then_id_none_last(self):
        """AC-RS-13/F3: the definitions band is pinned to `(order, id)`, `None`
        order last — its own key, independent of `select`'s sequence-based one."""
        late = definition("R0050", "beta", "A beta is a beta.", order=30)
        early = definition("R0060", "alpha", "An alpha is an alpha.", order=10)
        unordered = definition("R0070", "gamma", "A gamma is a gamma.", order=None)
        selected = [row("R0100", "An alpha precedes a beta precedes a gamma.",
                        order=5, role=["writer"])]
        pulled = terms.pull_definitions(selected, selected + [late, early, unordered])
        self.assertEqual(ids(pulled), ["R0060", "R0050", "R0070"])


# ------------------------------------------------------------------- AC-RS-5


class TestNear(unittest.TestCase):
    """AC-RS-5: Jaccard similarity of normalized word sets, highest first."""

    #: 4 text words, 9 body words, 3 shared -> 3 / 10, exactly the default
    #: threshold, which the contract says is inclusive ("at or above").
    AT_TEXT = "alpha beta gamma delta"
    AT_BODY = "alpha beta gamma epsilon zeta eta theta iota kappa"
    #: 2 shared of a 11-word union -> 0.18, below the threshold.
    BELOW_BODY = "alpha beta epsilon zeta eta theta iota kappa lambda"

    def test_ac_rs_5_a_row_scoring_exactly_at_the_threshold_is_returned(self):
        """AC-RS-5: "at or above threshold" — the boundary is inclusive."""
        at = row("R0001", self.AT_BODY, order=10)
        hits = near_mod.near(self.AT_TEXT, [at])
        self.assertEqual(ids([r for r, _ in hits]), ["R0001"])
        self.assertAlmostEqual(hits[0][1], 0.3, places=9)

    def test_ac_rs_5_a_row_below_the_threshold_is_dropped(self):
        """AC-RS-5: only the rows at or above the threshold come back."""
        rows = [row("R0001", self.AT_BODY, order=10),
                row("R0002", self.BELOW_BODY, order=20)]
        hits = near_mod.near(self.AT_TEXT, rows)
        self.assertEqual(ids([r for r, _ in hits]), ["R0001"])

    def test_ac_rs_5_results_come_back_highest_first(self):
        """AC-RS-5: the rows are ordered by score, highest first."""
        weak = row("R0002", self.AT_BODY, order=10)
        strong = row("R0001", "alpha beta gamma delta", order=20)
        hits = near_mod.near(self.AT_TEXT, [weak, strong])
        self.assertEqual(ids([r for r, _ in hits]), ["R0001", "R0002"])

    def test_ac_rs_5_normalization_drops_short_words_and_punctuation(self):
        """AC-RS-5: lower-cased, punctuation stripped, words of <= 2 letters dropped."""
        target = row("R0001", "Tranche, delta; workstream!", order=10)
        hits = near_mod.near("a tranche, an  DELTA -- of workstream.", [target])
        self.assertEqual(ids([r for r, _ in hits]), ["R0001"])
        self.assertAlmostEqual(hits[0][1], 1.0, places=9)

    def test_ac_rs_5_the_threshold_is_a_parameter_and_is_inclusive(self):
        """AC-RS-5: `threshold` defaults to 0.3 and admits a score equal to it."""
        exact = row("R0001", self.AT_TEXT, order=10)
        at = row("R0002", self.AT_BODY, order=20)
        hits = near_mod.near(self.AT_TEXT, [exact, at], threshold=1.0)
        self.assertEqual(ids([r for r, _ in hits]), ["R0001"])


# ------------------------------------------------- AC-RS-6 / AC-RS-14 / AC-RS-15


class TestRender(unittest.TestCase):
    """DEC-000630 the header, DEC-000640 the three bands, AC-RS-14 the two forms.

    Contract: `docs/cycles/bundle-tool-followup-20260907T170000Z.md`, item 5 —
    overrides the tests directive's header/manifest/heading form.
    """

    HEAD = "a5d60506d1d1266d8685f498662f514d49e12136"
    GENERATED = "20260906T110000Z"
    REPO = "davepierceops/fiducial"
    HEADER = "<!-- fiducial %s @ %s %s -->" % (REPO, HEAD, GENERATED)

    def rendered(self, rows, definitions=()):
        return render.render(
            list(rows),
            list(definitions),
            repo=self.REPO,
            head=self.HEAD,
            generated=self.GENERATED,
        )

    def test_dec_000630_the_header_is_one_comment_line_then_a_blank_line(self):
        """DEC-000630: `<!-- fiducial <repo> @ <head> <generated> -->`, then blank."""
        lines = self.rendered([row("R0001", "Prose.", order=10, blob="b" * 40)]).splitlines()
        self.assertEqual(lines[0], self.HEADER)
        self.assertEqual(lines[1], "")

    def test_dec_000630_no_title_or_manifest_lines_appear(self):
        """DEC-000630: no member list, no blob list, no title line."""
        text = self.rendered([row("R0001", "Prose.", order=10, blob="b" * 40)])
        self.assertNotIn("# fiducial-bundle", text)
        self.assertNotIn("- Repo:", text)
        self.assertNotIn("- Rows:", text)
        self.assertNotIn("- Definitions:", text)
        self.assertNotIn("b" * 40, text)

    def test_dec_000640_each_row_renders_as_body_text_with_no_heading(self):
        """DEC-000640: rows render one after another, blank line between, no heading."""
        text = self.rendered(
            [row("R0001", "First prose.", order=10), row("R0002", "Second prose.", order=20)]
        )
        self.assertNotIn("## R0001", text)
        self.assertNotIn("## R0002", text)
        body = text.split("\n\n", 1)[1]
        self.assertEqual(body, "First prose.\n\nSecond prose.\n")

    def test_ac_rs_14_the_human_form_is_carried_on_the_row_and_never_rendered(self):
        """AC-RS-14 (G4): two forms, one row — `## Human` reaches no output."""
        carried = row("R0007", "Dave edits freely.",
                      human="DEC-000170: the branch is the state.", order=10)
        self.assertEqual(carried.human, "DEC-000170: the branch is the state.")
        self.assertNotIn("DEC-000170", carried.body)
        text = self.rendered([carried])
        self.assertNotIn("## Human", text)
        self.assertNotIn("DEC-000170", text)

    def test_ac_rs_15_a_process_document_renders_as_body_text_under_no_heading(self):
        """AC-RS-15/DEC-000640: a process row is body-only, not headed by its path."""
        text = self.rendered([
            row("change-flow", "The flow.", order=10, kind="process",
                path="process/change-flow.md", blob="c" * 40)
        ])
        self.assertNotIn("## process/change-flow.md", text)
        self.assertIn("The flow.", text)

    def test_ac_rs_15_process_rows_sort_after_every_rule_whatever_their_order(self):
        """AC-RS-15/DEC-000640: a process document is its own band, after every
        rule regardless of `order` — no interleaving."""
        rows = query.select(
            [
                row("R0002", "Late rule.", order=30, topic="core", role=["writer"]),
                row("change-flow", "The flow.", order=1, kind="process",
                    path="process/change-flow.md", role=["writer"]),
                row("R0001", "Early rule.", order=10, topic="core", role=["writer"]),
            ],
            {"role": "writer"},
        )
        text = self.rendered(rows)
        self.assertEqual(
            [line for line in text.splitlines() if line.strip()],
            [self.HEADER, "Early rule.", "Late rule.", "The flow."],
        )

    def test_dec_000640_definitions_render_last_under_one_heading(self):
        """DEC-000640: definitions render last, under one `## Definitions` heading."""
        selected = [row("R0001", "Open one tranche.", order=10)]
        defs = [definition("R0003", "tranche", "A tranche is one workstream.", order=20)]
        text = self.rendered(selected, defs)
        headings = [line for line in text.splitlines() if line.startswith("## ")]
        self.assertEqual(headings, ["## Definitions"])
        self.assertLess(text.index("Open one tranche."), text.index("## Definitions"))

    def test_ac_rs_6_a_definition_renders_under_its_first_term(self):
        """Each definition as `**<first term>** — <body>`."""
        text = self.rendered(
            [row("R0001", "Open one tranche.", order=10)],
            [definition("R0003", ["tranche", "tranches"],
                        "A tranche is one workstream.", order=20)],
        )
        self.assertIn("**tranche** — A tranche is one workstream.", text)

    def test_dec_000630_the_render_carries_nothing_else(self):
        """"Nothing else": no separator furniture, no extra list lines."""
        text = self.rendered([row("R0001", "Prose.", order=10, blob="b" * 40)])
        self.assertEqual(text.count("<!--"), 1)
        lines = text.splitlines()
        self.assertEqual([line for line in lines if line.startswith("#")], [])
        self.assertEqual(lines, [self.HEADER, "", "Prose."])


class TestNamedQueriesRealDocument(unittest.TestCase):
    """F1: the real process/named-queries.md parses to its full counts — the
    guard against a fence spelling `_FENCE_RE` does not recognize emptying
    both sequences and the bundle list in silence."""

    def test_the_real_document_parses_to_its_full_counts(self):
        text = FileRowSource(REPO_ROOT).named_queries_text()
        topic_positions, process_positions = named_queries.sequences(text)
        self.assertEqual(len(topic_positions), 9)
        self.assertEqual(len(process_positions), 11)
        self.assertEqual(len(named_queries.bundles(text)), 12)


if __name__ == "__main__":
    unittest.main()
