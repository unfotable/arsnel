"""Variables and the core built-in types."""

# A variable is a name that points at a value. No declaration needed.
name = "Ada"
age = 36
height_m = 1.65
is_hacker = True
nothing = None

for value in (name, age, height_m, is_hacker, nothing):
    print(f"{value!r:>8}  ->  {type(value).__name__}")

# Names can be re-bound to values of a different type (dynamic typing).
x: int | str = 10  # annotated so type checkers allow the re-binding below
print("x is", x, type(x).__name__)
x = "ten"
print("x is", x, type(x).__name__)

# Convert between types explicitly.
print(int("42") + 1)  # 43
print(float("3.5") * 2)  # 7.0
print(str(99) + " red balloons")
print(bool(0), bool(""), bool("0"), bool([]), bool([0]))  # truthiness

# Several assignments at once.
a, b = 1, 2
a, b = b, a  # swap without a temp variable
print(a, b)

# Constants are a naming convention, not a language feature.
MAX_LIVES = 3
print("lives:", MAX_LIVES)
