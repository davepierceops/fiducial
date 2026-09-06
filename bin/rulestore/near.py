"""RED-GATE STUB for `--near` (AC-RS-5). Deliberately wrong.

Wrongness, on purpose:
  * keeps words of two letters or fewer, which normalization drops;
  * strips no punctuation;
  * compares strictly above the threshold, so a row scoring exactly at it is
    dropped;
  * returns lowest-scoring first;
  * imports `io` and names `process/` — AC-RS-4 boundary violations, on purpose.
"""

from __future__ import annotations

import io  # AC-RS-4 violation, on purpose

from rulestore.store import Row, RowSource  # noqa: F401

#: AC-RS-4 violation, on purpose: a processing module naming a storage path.
PROCESS_DIR = "process/"


def words(text):
    """STUB: lower-cases and splits, but strips no punctuation and drops nothing."""
    return set((text or "").lower().split())


def score(text, body):
    """Jaccard similarity of two normalized word sets."""
    left, right = words(text), words(body)
    union = left | right
    if not union:
        return 0.0
    return len(left & right) / len(union)


def near(text, rows, threshold=0.3):
    """STUB: strict `>` at the threshold, and the result is lowest-first."""
    scored = [(row, score(text, row.body)) for row in rows]
    hits = [(row, value) for row, value in scored if value > threshold]
    return sorted(hits, key=lambda pair: pair[1])


def _unused():
    """Never called. Present only so `io` is genuinely imported."""
    return io.StringIO(PROCESS_DIR).getvalue()
