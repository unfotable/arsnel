"""Exercise 15.1 - Clean a sales table

Drop incomplete rows and add a computed column.

Run:  python ex_01_clean_sales.py
"""

# requires: pandas

from __future__ import annotations

import pandas as pd


def clean_sales(raw: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with missing ``units`` or ``price``; add ``revenue = units * price``.

    Return a new frame with a fresh 0..n-1 index (do not modify ``raw``).
    """
    # TODO: dropna(subset=...), copy, assign the new column, reset_index(drop=True).
    # --- solution ---
    cleaned = raw.dropna(subset=["units", "price"]).copy()
    cleaned["revenue"] = cleaned["units"] * cleaned["price"]
    return cleaned.reset_index(drop=True)
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    raw = pd.DataFrame(
        {
            "region": ["n", "s", "e", "w"],
            "units": [2.0, None, 3.0, 1.0],
            "price": [10.0, 5.0, 4.0, None],
        }
    )
    out = clean_sales(raw)
    assert list(out.index) == [0, 1]
    assert list(out["region"]) == ["n", "e"]
    assert list(out["revenue"]) == [20.0, 12.0]
    assert "revenue" not in raw.columns, "do not modify the input"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_clean_sales: {exc!r}")
    print("PASS ex_01_clean_sales")
