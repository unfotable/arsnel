"""Exercise 17.2 - Refactor a messy function

Replace nested ifs with data and guard clauses.

Run:  python ex_02_refactor_shipping.py
"""

from __future__ import annotations

RATES = {"standard": 5.0, "express": 12.0, "overnight": 25.0}
FREE_SHIPPING_OVER = 100.0


def shipping_cost(method: str, order_total: float) -> float:
    """Return the shipping price.

    Unknown methods raise ValueError, negative totals raise ValueError and orders over
    100 ship free with the standard method only.
    """
    # TODO: guard clauses first, then look the price up in RATES.
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert shipping_cost("standard", 50) == 5.0
    assert shipping_cost("standard", 100.01) == 0.0
    assert shipping_cost("express", 500) == 12.0
    for method, total in (("teleport", 10), ("standard", -1)):
        try:
            shipping_cost(method, total)
        except ValueError:
            continue
        raise AssertionError(f"({method!r}, {total}) must raise ValueError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_refactor_shipping: {exc!r}")
    print("PASS ex_02_refactor_shipping")
