"""Before and after: the same behaviour, much easier to read and change."""

from dataclasses import dataclass


def process_before(d, t):  # type: ignore[no-untyped-def]
    if t == "a":
        if d > 100:
            return d * 0.8
        else:
            return d * 0.9
    elif t == "b":
        return d * 0.95
    else:
        return d


RATES = {"gold": 0.8, "silver": 0.9, "bronze": 0.95}
BIG_ORDER = 100


@dataclass(frozen=True)
class Order:
    total: float
    tier: str = "none"


def discounted_total(order: Order) -> float:
    """Apply the tier discount; gold only applies to big orders."""
    if order.tier == "gold" and order.total <= BIG_ORDER:
        return order.total * RATES["silver"]
    return order.total * RATES.get(order.tier, 1.0)


for old_args, new in (
    (("a", 150), Order(150, "gold")),
    (("a", 50), Order(50, "gold")),
    (("b", 200), Order(200, "silver")),
):
    print(
        round(process_before(old_args[1], old_args[0]), 2), "->", discounted_total(new)
    )
