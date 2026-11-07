"""Exercise 15.2 - Totals per group

Aggregate with groupby and return plain Python.

Run:  python ex_02_group_totals.py
"""

# requires: pandas

from __future__ import annotations

import pandas as pd


def revenue_by_region(frame: pd.DataFrame) -> dict[str, float]:
    """Sum ``revenue`` per ``region``; the dict is ordered by revenue, highest first."""
    # TODO: groupby("region")["revenue"].sum().sort_values(ascending=False) -> dict.
    # --- solution ---
    totals = frame.groupby("region")["revenue"].sum().sort_values(ascending=False)
    return {str(region): float(value) for region, value in totals.items()}
    # --- end ---


def top_product(frame: pd.DataFrame) -> str:
    """Name of the product with the highest total ``units``."""
    # TODO: groupby product, sum units, idxmax().
    # --- solution ---
    return str(frame.groupby("product")["units"].sum().idxmax())
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    frame = pd.DataFrame(
        {
            "region": ["n", "s", "n", "e"],
            "product": ["pen", "pen", "book", "lamp"],
            "units": [10, 5, 2, 1],
            "revenue": [15.0, 7.5, 24.0, 25.0],
        }
    )
    result = revenue_by_region(frame)
    assert list(result.items()) == [("n", 39.0), ("e", 25.0), ("s", 7.5)], result
    assert top_product(frame) == "pen"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_group_totals: {exc!r}")
    print("PASS ex_02_group_totals")
