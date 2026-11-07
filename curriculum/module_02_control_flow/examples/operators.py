"""Comparison, logical, membership and identity operators; truthiness."""

x, y = 7, 3
print(x > y, x == y, x != y, 1 < x <= 10)  # chained comparison

# `and`/`or` short-circuit and return one of their operands.
print(0 or "default", "" or None, 5 and 6, [] and "never")  # noqa: SIM222, SIM223
print(not 0, not "text")

# Membership and identity.
print("a" in "banana", 4 in [1, 2, 3], "k" not in {"k": 1})
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # equal values vs the very same object
print(None is None, 5 != None)

# Falsy values: 0, 0.0, "", [], {}, set(), None, False. Everything else is truthy.
samples: tuple[object, ...] = (0, 0.0, "", [], {}, None, "0", [0])
for value in samples:
    print(f"{value!r:>5} -> {bool(value)}")
