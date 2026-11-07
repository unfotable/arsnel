"""Exercise 07.3 - CSV summary

Read a CSV with DictReader and aggregate it.

Run:  python ex_03_csv_summary.py
"""

from __future__ import annotations

import csv
import tempfile
from pathlib import Path


def total_by_category(path: Path) -> dict[str, float]:
    """Sum the ``amount`` column per ``category`` of a CSV file."""
    # TODO: open with newline="", iterate csv.DictReader, add up float(amount).
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "spend.csv"
        path.write_text(
            "category,amount\nfood,10.5\nfun,4\nfood,2.5\n", encoding="utf-8"
        )
        assert total_by_category(path) == {"food": 13.0, "fun": 4.0}
        empty = Path(tmp) / "empty.csv"
        empty.write_text("category,amount\n", encoding="utf-8")
        assert total_by_category(empty) == {}


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_csv_summary: {exc!r}")
    print("PASS ex_03_csv_summary")
