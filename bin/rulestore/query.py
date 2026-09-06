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
    """A row's tie-break value: its first `topic`, or a process row's stem."""
    if row.kind == "process":
        stem = (row.path or row.id).rsplit("/", 1)[-1]
        if stem.endswith(".md"):
            stem = stem[: -len(".md")]
        return stem
    return (row.keys.get("topic") or [""])[0]


def sort_key(row):
    """Ascending `order` (`None` last), then first `topic`, then `id`."""
    order = row.order if row.order is not None else _NO_ORDER
    return (order, _topic_sort_value(row), row.id)


def select(rows, where):
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
    return sorted(hits, key=sort_key)
