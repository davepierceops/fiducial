"""The computed key census (AC-RS-3).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""

from __future__ import annotations


def keys_in_use(rows):
    """`{key: {value: count}}`, computed from `rows` alone. `id`/`order` excluded."""
    census = {}
    for row in rows:
        for key, values in (row.keys or {}).items():
            bucket = census.setdefault(key, {})
            for value in values:
                bucket[value] = bucket.get(value, 0) + 1
    return census
