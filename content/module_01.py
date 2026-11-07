"""Module 01 content: syntax, variables, types and I/O (the authoring template)."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=1,
    intro=(
        "Python reads like English, but every character matters. In this module you "
        "write real programs: print text, store values in variables, meet the core "
        "types and ask the user questions. By the end you will think in "
        "*values* and *names* - the foundation of everything after."
    ),
    lessons=(
        Lesson(
            "Your first program",
            """
A Python program is a text file of **statements** that run top to bottom.
The simplest statement calls the built-in function `print()`:

```python
print("Hello, ARSNEL!")
```

- Text lives inside quotes (`"..."` or `'...'`) - that is a **string**.
- `#` starts a **comment**; Python ignores the rest of the line.
- Indentation is *syntax*, not decoration (you will see why in module 02).
- Run a file with `python file.py`; experiment live with `python` (the REPL).
""",
        ),
        Lesson(
            "Variables and names",
            """
A variable is a **name bound to a value**. Assign with `=`:

```python
score = 10
score = score + 5     # rebinding; score is now 15
```

Rules and conventions:

| Rule | Example |
| --- | --- |
| letters, digits, `_`; cannot start with a digit | `player_1` OK, `1player` error |
| case-sensitive | `Score` and `score` differ |
| `snake_case` for variables | `max_lives` |
| `UPPER_CASE` for constants (convention) | `MAX_LIVES = 3` |
| cannot reuse keywords | `class`, `for`, `if`, ... |

Pick names that explain intent: `elapsed_seconds` beats `x`.
""",
        ),
        Lesson(
            "The core types",
            """
Every value has a **type**. Check it with `type(value)`.

| Type | Example | Notes |
| --- | --- | --- |
| `int` | `42`, `-7`, `1_000_000` | arbitrary size |
| `float` | `3.14`, `2e3` | binary approximation |
| `str` | `"hi"` | immutable text |
| `bool` | `True`, `False` | subclass of `int` |
| `NoneType` | `None` | "no value" |

Python is **dynamically typed**: a *name* has no type, the *value* it points to does.
Convert explicitly with `int()`, `float()`, `str()` and `bool()`.
""",
        ),
        Lesson(
            "Numbers and arithmetic",
            """
| Operator | Meaning | `7 ? 2` |
| --- | --- | --- |
| `+ - *` | add, subtract, multiply | `9 5 14` |
| `/` | true division (float) | `3.5` |
| `//` | floor division | `3` |
| `%` | remainder | `1` |
| `**` | power | `49` |

Floats are binary approximations: `0.1 + 0.2 != 0.3`. Compare floats with
`math.isclose()` and use `round()` only for *display*.
""",
        ),
        Lesson(
            "Input and output",
            """
`input(prompt)` pauses, reads a line and returns it **as a string**:

```python
age = int(input("age? "))     # convert before doing maths
print(f"Next year: {age + 1}")
```

`print()` takes `sep=` and `end=`, and `file=sys.stderr` writes to the error
stream. f-strings (`f"...{value}..."`) embed expressions - module 03 digs deeper.

**Common mistakes**

- `"5" + 5` raises `TypeError` - convert first.
- `input()` never returns a number.
- `=` assigns, `==` compares.
""",
        ),
    ),
    examples=(
        Example(
            "hello_world.py",
            "Hello, world",
            "print(), comments, sep/end and multi-line strings.",
        ),
        Example(
            "variables_and_types.py",
            "Variables and types",
            "Names, the five core types, conversions and truthiness.",
        ),
        Example(
            "numbers_and_math.py",
            "Numbers and math",
            "Operators, divmod, float surprises and the math module.",
        ),
        Example(
            "input_output.py",
            "Input and output",
            "input() with a safe fallback when no terminal is attached.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_greeting.py", "Greeting", "build a greeting with an f-string.", 1
        ),
        Exercise(
            "ex_02_temperature.py",
            "Temperature converter",
            "Celsius <-> Fahrenheit.",
            1,
        ),
        Exercise(
            "ex_03_bill_splitter.py",
            "Bill splitter",
            "tips, rounding and type detection.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What does `print(7 // 2)` display?",
            ("3.5", "3", "4", "1"),
            1,
            "`//` is floor division: it divides and rounds down, giving 3.",
        ),
        Question(
            "What type does `input()` always return?",
            ("int", "float", "str", "It depends on what the user typed"),
            2,
            "input() returns text. Convert with int() or float() when you need numbers.",
        ),
        Question(
            "Which is a valid variable name?",
            ("2fast", "my-var", "player_1", "class"),
            2,
            "Names may contain letters, digits and underscores but cannot start with a digit, contain '-' or be a keyword.",
        ),
        Question(
            "What is `0.1 + 0.2 == 0.3` in Python?",
            ("True", "False", "An error", "None"),
            1,
            "Floats are binary approximations; the sum is 0.30000000000000004. Use math.isclose().",
        ),
        Question(
            "What does `bool('0')` evaluate to?",
            ("False", "True", "0", "An error"),
            1,
            "Any non-empty string is truthy, including the text '0'.",
        ),
        Question(
            "After `a, b = 1, 2` then `a, b = b, a`, what is `a`?",
            ("1", "2", "(1, 2)", "An error"),
            1,
            "Tuple unpacking swaps the values without a temporary variable.",
        ),
        Question(
            "Which statement writes `a-b-c`?",
            (
                "print('a','b','c', sep='-')",
                "print('a','b','c', end='-')",
                "print('a-b-c', sep='-', end='')",
                "print('a' + 'b' + 'c')",
            ),
            0,
            "`sep` controls the separator between arguments; `end` controls what follows the last one.",
        ),
    ),
    cheatsheet=(
        '`print(a, b, sep="-", end="")` - output control',
        "`type(x)` / `isinstance(x, int)` - inspect types",
        "`int()`, `float()`, `str()`, `bool()` - conversions",
        "`/` true div, `//` floor div, `%` remainder, `**` power",
        "`x += 1` augmented assignment",
        '`input("prompt")` always returns `str`',
    ),
    next_steps="Next: decisions and loops - `if`, `for`, `while` - in module 02.",
)
