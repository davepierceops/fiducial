"""Selection and ordering over rows (AC-RS-2).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""

from __future__ import annotations

#: `None` order sorts after every integer, however large.
_NO_ORDER = float("inf")


class QueryError(Exception):
    """A `--where` token that is not a `k=v` pair with both halves non-empty."""


def parse_where(args):
    """`{key: value}` from `k=v` tokens. Any other shape is a `QueryError`."""
    where = {}
    for token in args:
        if "=" not in token:
            raise QueryError("not a k=v token: %r" % (token,))
        key, _, value = token.partition("=")
        key = key.strip()
        value = value.strip()
        if not key or not value:
            raise QueryError("empty key or value: %r" % (token,))
        where[key] = value
    return where


def _topic_sort_value(row):
    """A row's position name: its first `topic`, or a process row's stem."""
    if row.kind == "process":
        name = (row.keys.get("topic") or [None])[0]
        if name is not None:
            return name
        stem = (row.path or row.id).rsplit("/", 1)[-1]
        if stem.endswith(".md"):
            stem = stem[: -len(".md")]
        return stem
    return (row.keys.get("topic") or [""])[0]


def _position(name, band_list, is_process):
    """`name`'s index in the band's sequence list, or the list's length."""
    if is_process:
        try:
            return band_list.index(name)
        except ValueError:
            return len(band_list)
    for index, names in enumerate(band_list):
        if name in names:
            return index
    return len(band_list)


def sort_key(row, sequences=([], [])):
    """(band, position, name, order, id) — DEC-000640's three-band ordering.

    Band 0 is a rule, band 1 a process row. `position` is the index of the
    row's topic (or a process row's path stem, when it carries no `topic`)
    in that band's sequence list; a name the sequence does not carry sorts
    after every named one, and ties among unnamed rows break on the name
    itself, alphabetically, ahead of `order` (`None` last) and `id`.
    """
    topic_positions, process_positions = sequences
    is_process = row.kind == "process"
    band = 1 if is_process else 0
    name = _topic_sort_value(row)
    band_list = process_positions if is_process else topic_positions
    position = _position(name, band_list, is_process)
    order = row.order if row.order is not None else _NO_ORDER
    return (band, position, name, order, row.id)


def select(rows, where, sequences=([], [])):
    """Exactly the rows where every named key's list contains the value."""
    hits = []
    for row in rows:
        matched = True
        for key, value in where.items():
            values = row.keys.get(key)
            if not values or value not in values:
                matched = False
                break
        if matched:
            hits.append(row)
    return sorted(hits, key=lambda row: sort_key(row, sequences))
