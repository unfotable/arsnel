"""Module 02 content: operators, conditionals and loops."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=2,
    intro="Programs get interesting when they decide and repeat. This module covers every operator you will meet, if/elif/else, the modern match statement, and Python's for and while loops with their useful extras.",
    lessons=(
        Lesson(
            "Operators and truthiness",
            """
| Group | Operators |
| --- | --- |
| comparison | `== != < <= > >=` (chainable: `1 < x <= 10`) |
| logical | `and or not` (short-circuit, return an operand) |
| membership | `in`, `not in` |
| identity | `is`, `is not` (same object; use for `None`) |

**Falsy** values: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is truthy,
so write `if items:` instead of `if len(items) > 0:`.
""",
        ),
        Lesson(
            "Conditionals",
            """
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

label = "adult" if age >= 18 else "minor"     # conditional expression
```

Indentation (4 spaces) defines the block. Branches are checked top to bottom; the first match wins.
""",
        ),
        Lesson(
            "match statements",
            """
`match` (Python 3.10+) compares a value against **patterns**:

```python
match command.split():
    case ["go", direction]:
        ...
    case ["take", *items] if items:
        ...
    case _:
        ...
```

Patterns destructure sequences, mappings and classes; `_` is the wildcard; `if` adds a guard.
""",
        ),
        Lesson(
            "Loops",
            """
```python
for i in range(5): ...                    # 0..4
for i, x in enumerate(items, start=1): ...
for a, b in zip(xs, ys): ...
while condition: ...
```

`break` leaves the loop, `continue` skips to the next pass, and a loop's `else` block runs only
when the loop finished **without** `break`. Beware infinite `while True` loops without a `break`.
""",
        ),
    ),
    examples=(
        Example(
            "operators.py",
            "Operators",
            "Comparison, logic, membership, identity and truthiness.",
        ),
        Example(
            "conditionals.py",
            "Conditionals and match",
            "if/elif/else, the ternary and pattern matching.",
        ),
        Example(
            "loops.py",
            "Loops",
            "for, while, range, break/continue/else, enumerate and zip.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_fizzbuzz.py", "FizzBuzz", "the classic loop-and-modulo puzzle.", 1
        ),
        Exercise(
            "ex_02_leap_year_and_grade.py",
            "Leap years and grades",
            "boolean logic and if/elif chains.",
            2,
        ),
        Exercise(
            "ex_03_primes_and_collatz.py",
            "Primes and Collatz",
            "nested loops, while and for/else.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What does `0 or 'default'` evaluate to?",
            ("0", "'default'", "True", "None"),
            1,
            "`or` returns the first truthy operand.",
        ),
        Question(
            "Which is the right way to test for None?",
            ("x == None", "x is None", "x = None", "not x"),
            1,
            "None is a singleton; use identity.",
        ),
        Question(
            "What does `range(2, 10, 3)` produce?",
            ("2, 5, 8", "2, 5, 8, 10", "3, 6, 9", "2, 3, 4"),
            0,
            "Start 2, stop before 10, step 3.",
        ),
        Question(
            "When does a loop's `else` block run?",
            (
                "Always",
                "When the loop ends without break",
                "When break happens",
                "Never",
            ),
            1,
            "for/else's else means no break occurred.",
        ),
        Question(
            "What does `continue` do?",
            (
                "Ends the loop",
                "Skips to the next iteration",
                "Restarts the program",
                "Raises an error",
            ),
            1,
            "It jumps to the next pass of the loop.",
        ),
        Question(
            "What is `bool([])`?",
            ("True", "False", "None", "Error"),
            1,
            "Empty containers are falsy.",
        ),
        Question(
            "In `match`, what does the pattern `_` do?",
            (
                "Matches nothing",
                "Matches anything (wildcard)",
                "Raises",
                "Matches None only",
            ),
            1,
            "It is the catch-all case.",
        ),
    ),
    cheatsheet=(
        "`== != < > <= >=`, chained `a < b < c`",
        "`and or not`, `in`, `is`",
        "`if / elif / else`, `x if c else y`",
        "`match value: case pattern:`",
        "`for x in range/enumerate/zip`; `while`",
        "`break`, `continue`, loop `else`",
    ),
    next_steps="Next: work with text in module 03.",
)
