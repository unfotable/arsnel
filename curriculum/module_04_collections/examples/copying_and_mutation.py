"""Aliases, shallow copies and deep copies - the root of many surprises."""

import copy

# Assignment never copies: both names point at the SAME list.
a = [1, 2, 3]
b = a
b.append(4)
print("alias:  ", a, "| same object?", a is b)

# A shallow copy creates a new outer list; inner objects are shared.
grid = [[0, 0], [0, 0]]
shallow = grid.copy()  # same as list(grid) or grid[:]
shallow[0][0] = 99
print("shallow share inner lists:", grid)

# A deep copy duplicates the whole structure recursively.
grid = [[0, 0], [0, 0]]
deep = copy.deepcopy(grid)
deep[0][0] = 99
print("deep copy untouched:      ", grid, "| copy:", deep)

# Classic trap: multiplying a list of lists repeats the SAME inner list.
trap = [[0] * 2] * 2
trap[0][0] = 1
print("trap:   ", trap)
safe = [[0] * 2 for _ in range(2)]
safe[0][0] = 1
print("comprehension:", safe)

# Immutable values are safe to share: "changing" them rebinds the name.
s = "abc"
t = s
t += "d"
print("strings:", s, t)

# Tuples are immutable, but a tuple CONTAINING a list can still change.
record = ("ids", [1, 2])
record[1].append(3)
print("tuple holding a list:", record)

# Mutating while iterating is a bug; iterate over a copy or build a new list.
items = [1, 2, 3, 4, 5, 6]
kept = [n for n in items if n % 2]
print("kept odds:", kept)
