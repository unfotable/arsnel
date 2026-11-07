"""Arithmetic, integer division, remainders, powers and float surprises."""

import math

print(7 + 3, 7 - 3, 7 * 3)  # 10 4 21
print(7 / 2)  # 3.5   true division always gives a float
print(7 // 2)  # 3     floor division
print(7 % 2)  # 1     remainder (modulo)
print(2**10)  # 1024  power
print(divmod(17, 5))  # (3, 2)

# Order of operations is like maths: parentheses, **, * / // %, + -
print(2 + 3 * 4, (2 + 3) * 4)

# Underscores make big numbers readable.
big = 1_000_000
print(big, type(big).__name__)

# Floats are binary approximations.
print(0.1 + 0.2)  # 0.30000000000000004
print(math.isclose(0.1 + 0.2, 0.3))  # True: compare floats with isclose
print(round(3.14159, 2), round(2.5), round(3.5))  # banker's rounding

# The math module has the usual functions.
print(math.sqrt(144), math.floor(2.7), math.ceil(2.1), math.pi)

# Augmented assignment.
score = 10
score += 5
score *= 2
print(score)  # 30
