"""Exercise 03.3 - Format a receipt

Use f-string format specs for width, alignment and precision.

Run:  python ex_03_receipt.py
"""

from __future__ import annotations


def format_row(name: str, qty: int, price: float) -> str:
    """Return name left (10 cols), qty right (4), price right (9, 2 decimals)."""
    # TODO: one f-string with {name:<10}{qty:>4}{price:>9.2f}.
    raise NotImplementedError("TODO: your turn")


def format_total(amount: float) -> str:
    """Return ``TOTAL`` plus the amount with thousands separators and 2 decimals."""
    # TODO: use the "," and ".2f" format spec; keep total width 23 with the label left.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert format_row("apple", 3, 0.5) == "apple        3     0.50"
    assert format_row("watermelon", 12, 1234.5) == "watermelon  12  1234.50"
    assert format_total(1234567.891) == "TOTAL      1,234,567.89"
    assert len(format_total(5)) == 23


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_receipt: {exc!r}")
    print("PASS ex_03_receipt")
