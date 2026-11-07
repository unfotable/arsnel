"""Tuples (immutable records, unpacking) and sets (uniqueness, algebra)."""

# A tuple is an immutable, ordered record. The comma makes the tuple.
point = (3, 4)
single = (42,)  # one-element tuple needs the trailing comma
print("point:", point, "| single:", single, "| not a tuple:", (42))

# Unpacking assigns several names at once.
x, y = point
first, *middle, last = [10, 20, 30, 40, 50]
print("x, y =", x, y)
print("first:", first, "middle:", middle, "last:", last)

# Swap without a temporary variable.
a, b = 1, 2
a, b = b, a
print("swapped:", a, b)

# Tuples cannot change; trying to is a TypeError.
try:
    point[0] = 99  # type: ignore[index]
except TypeError as exc:
    print("TypeError:", exc)

# Because they are hashable, tuples work as dict keys and set members.
grid = {(0, 0): "start", (2, 3): "goal"}
print("grid[(2, 3)]:", grid[(2, 3)])

# Sets: unordered, unique, fast membership. {} alone is an empty DICT.
python_fans = {"ada", "grace", "linus", "guido"}
rust_fans = {"linus", "ferris", "grace"}
print("union:       ", sorted(python_fans | rust_fans))
print("intersection:", sorted(python_fans & rust_fans))
print("difference:  ", sorted(python_fans - rust_fans))
print("symmetric:   ", sorted(python_fans ^ rust_fans))
print("subset?      ", {"ada"} <= python_fans)

# Deduplicate (order is lost, so sort for stable output).
with_dupes = [3, 1, 3, 2, 1]
print("unique:", sorted(set(with_dupes)))

# Elements must be hashable: lists are not, tuples (of hashables) are.
try:
    bad = {[1, 2]}
except TypeError as exc:
    print("TypeError:", exc)
