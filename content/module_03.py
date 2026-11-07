"""Module 03 content: strings and formatting."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=3,
    intro="Text is everywhere: names, files, logs, messages. You will slice and search strings, learn the methods worth memorising, and format output precisely with f-strings.",
    lessons=(
        Lesson(
            "Strings are immutable sequences",
            """
```python
s = "pythonista"
s[0], s[-1]        # 'p' 'a'
s[2:6]             # 'thon'  (stop is excluded)
s[::-1]            # reversed
len(s), "thon" in s
```

You cannot assign to `s[0]`; build a new string instead. Strings are Unicode: `len("café") == 4`
but its UTF-8 encoding has 5 bytes. `.encode()` gives `bytes`, `.decode()` goes back.
""",
        ),
        Lesson(
            "Methods worth knowing",
            """
| Method | Does |
| --- | --- |
| `strip() / lstrip() / rstrip()` | trim whitespace |
| `lower() / upper() / title()` | change case |
| `split(sep)` / `"-".join(parts)` | text <-> list |
| `replace(a, b)`, `find(x)`, `count(x)` | edit and search |
| `startswith / endswith` | prefix and suffix tests |
| `isdigit / isalpha / isalnum` | classification |

Methods return **new** strings; the original never changes.
""",
        ),
        Lesson(
            "f-strings and format specs",
            """
```python
f"{name:<10}|{qty:>4}|{price:>8.2f}"     # align, width, precision
f"{1234567.891:,.2f}"                     # 1,234,567.89
f"{0.256:.1%}"                            # 25.6%
f"{255:#x} {255:08b} {42:+d}"
f"{value=}  {name!r}"                     # debugging helpers
```

Spec grammar: `[[fill]align][sign][width][,][.precision][type]` with align `<` `>` `^`.
`str.format()` and `%` still exist but f-strings are the modern default.
""",
        ),
        Lesson(
            "Raw strings and multi-line text",
            """
`r"C:\\new\\table"` keeps backslashes (regular expressions, Windows paths).
Triple quotes (`\"\"\"...\"\"\"`) span lines. `"\\n"` is a newline, `"\\t"` a tab.
`print(text, end="")` controls the line ending.

**Common mistake:** building big strings with `+=` in a loop - collect parts in a list and `"".join(parts)`.
""",
        ),
    ),
    examples=(
        Example(
            "indexing_and_slicing.py",
            "Indexing and slicing",
            "Immutability, slicing, ord/chr and encodings.",
        ),
        Example("string_methods.py", "String methods", "The everyday toolkit."),
        Example(
            "fstrings.py",
            "f-strings and format specs",
            "Alignment, precision, separators and debugging forms.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_palindrome.py",
            "Palindromes",
            "normalise text, compare with its reverse.",
            1,
        ),
        Exercise(
            "ex_02_caesar.py", "Caesar cipher", "shift letters with ord() and chr().", 2
        ),
        Exercise(
            "ex_03_receipt.py",
            "Format a receipt",
            "width, alignment and precision specs.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What is `'python'[1:4]`?",
            ("pyt", "yth", "ytho", "tho"),
            1,
            "Index 1 up to but not including 4.",
        ),
        Question(
            "What does `'abc'[::-1]` return?",
            ("'abc'", "'cba'", "'bca'", "Error"),
            1,
            "A step of -1 walks backwards.",
        ),
        Question(
            "Which line raises TypeError?",
            ("s = 'a' + 'b'", "s[0] = 'z'", "s.upper()", "len(s)"),
            1,
            "Strings are immutable.",
        ),
        Question(
            'What does f"{3.14159:.2f}" give?',
            ("3.14159", "3.14", "3.1", "3.142"),
            1,
            ".2f means 2 digits after the point.",
        ),
        Question(
            "What does `'a,b,,c'.split(',')` return?",
            ("['a','b','c']", "['a','b','','c']", "['a,b,,c']", "('a','b','c')"),
            1,
            "Empty fields are kept.",
        ),
        Question(
            "What does `r'\\n'` contain?",
            ("A newline", "Two characters: backslash and n", "Nothing", "An error"),
            1,
            "Raw strings do not process escapes.",
        ),
        Question(
            "How do you join a list of strings efficiently?",
            ("+= in a loop", "''.join(parts)", "str(parts)", "parts.join('')"),
            1,
            "join builds the result once.",
        ),
    ),
    cheatsheet=(
        "`s[i]`, `s[a:b:step]`, `s[::-1]`",
        "`strip split join replace find count`",
        '`f"{x:>8.2f}"`, `f"{n:,}"`, `f"{x=}"`',
        '`r"raw"`, triple quotes',
        "`s.encode()` -> bytes, `b.decode()` -> str",
        "`''.join(parts)` instead of repeated `+`",
    ),
    next_steps="Next: containers - lists, tuples, sets and dicts - in module 04.",
)
