"""List, set and dict comprehensions - and generator expressions."""

nums = range(1, 11)

# [expression for item in iterable if condition]
squares_of_evens = [n * n for n in nums if n % 2 == 0]
print("squares of evens:", squares_of_evens)

# The same loop written out; comprehensions say WHAT, loops say HOW.
result = []
for n in nums:
    if n % 2 == 0:
        result.append(n * n)
assert result == squares_of_evens

# Conditional EXPRESSION goes before the `for`; a filter goes after.
labels = ["even" if n % 2 == 0 else "odd" for n in range(4)]
print("labels:", labels)

# Nested loops read left to right, like the equivalent for-loops.
pairs = [(x, y) for x in range(3) for y in range(x)]
print("pairs:", pairs)
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in matrix for value in row]
transposed = [list(col) for col in zip(*matrix, strict=True)]
print("flat:", flat, "| transposed:", transposed)

# Set and dict comprehensions use braces.
lengths = {len(word) for word in ["a", "bb", "cc", "ddd"]}
print("distinct lengths:", sorted(lengths))
index = {word: len(word) for word in ["tea", "coffee"]}
print("index:", index)

# A generator expression uses () and produces items lazily, one at a time.
total = sum(n * n for n in range(1_000_000))
print("sum of squares:", total)
lazy = (n * n for n in range(3))
print("type:", type(lazy).__name__, "->", list(lazy), "-> now:", list(lazy))

# Keep comprehensions short: if it needs two conditions AND a nested loop,
# a plain for-loop is easier to read.
