"""Similarity search over row bodies (AC-RS-5).

Contract: `docs/cycles/bundle-tool-tests-20260906T110000Z.md` § "INTERFACE
CONTRACT", landed at `d5b643b48cf0285194d29b09f6755db1b8a16b34`.
"""

from __future__ import annotations

import re

_WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)


def _words(text):
    """Lower-cased word set: punctuation stripped, words of <= 2 letters dropped."""
    return {word for word in _WORD_RE.findall((text or "").lower()) if len(word) > 2}


def _jaccard(left, right):
    union = left | right
    if not union:
        return 0.0
    return len(left & right) / len(union)


def near(text, rows, threshold=0.3):
    """Rows scoring at or above `threshold` against `text`, highest first."""
    query_words = _words(text)
    hits = []
    for row in rows:
        score = _jaccard(query_words, _words(row.body))
        if score >= threshold:
            hits.append((row, score))
    return sorted(hits, key=lambda pair: pair[1], reverse=True)
