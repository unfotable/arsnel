"""Module 07 content: files, JSON, CSV, pathlib and exceptions."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=7,
    intro="Programs become useful when they remember things. You will read and write files safely, speak JSON and CSV, handle paths with pathlib - and handle failure with exceptions instead of crashing.",
    lessons=(
        Lesson(
            "Files and pathlib",
            """
```python
from pathlib import Path
p = Path("notes") / "todo.txt"
p.parent.mkdir(exist_ok=True)
p.write_text("buy milk\\n", encoding="utf-8")
for line in p.read_text(encoding="utf-8").splitlines(): ...
with p.open("a", encoding="utf-8") as fh:   # 'with' closes the file for you
    fh.write("walk dog\\n")
```

Modes: `r` read, `w` write (truncates!), `a` append, `b` binary. Always pass `encoding="utf-8"` for text.
`pathlib.Path` replaces string juggling: `/` joins, `.suffix`, `.stem`, `.exists()`, `.glob("*.py")`.
""",
        ),
        Lesson(
            "JSON and CSV",
            """
```python
import json, csv
data = json.loads('{"a": [1, 2]}')       # str -> Python
text = json.dumps(data, indent=2)        # Python -> str
with open("rows.csv", newline="") as fh:
    for row in csv.DictReader(fh): print(row["name"])
```

JSON maps to dict/list/str/int/float/bool/None. Open CSV files with `newline=""`.
Everything read from CSV is a **string** - convert it.
""",
        ),
        Lesson(
            "Exceptions",
            """
```python
try:
    value = int(text)
except ValueError as exc:
    print("bad number:", exc)
else:
    print("parsed", value)       # only if no exception
finally:
    print("always runs")
```

Catch the *specific* exception you can handle; never a bare `except:`.
`raise` re-raises; `raise NewError(...) from exc` keeps the cause.
""",
        ),
        Lesson(
            "Custom exceptions and style",
            """
```python
class ConfigError(Exception):
    \"\"\"Problem in a config file.\"\"\"
```

**EAFP** (easier to ask forgiveness) - just try and catch - is usually more Pythonic than
**LBYL** (look before you leap) checks, and avoids race conditions with files.
Raise exceptions for exceptional situations, not for normal control flow.
""",
        ),
    ),
    examples=(
        Example(
            "file_basics.py",
            "File basics",
            "open(), with, modes, text vs binary.",
            False,
        ),
        Example(
            "pathlib_tour.py",
            "pathlib tour",
            "Building, inspecting and searching paths.",
            False,
        ),
        Example(
            "json_and_csv.py",
            "JSON and CSV",
            "Round-trips through temporary files.",
            False,
        ),
        Example(
            "exceptions_flow.py",
            "try/except/else/finally",
            "The full control flow of exception handling.",
        ),
        Example(
            "custom_errors.py",
            "Custom errors",
            "Custom exceptions, raise from, EAFP vs LBYL.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_read_config.py",
            "Read a config file",
            "parse key=value lines and raise ConfigError.",
            2,
        ),
        Exercise(
            "ex_02_safe_parsing.py",
            "Safe parsing",
            "turn failures into values with try/except.",
            1,
        ),
        Exercise(
            "ex_03_csv_summary.py", "CSV summary", "aggregate a CSV with DictReader.", 2
        ),
    ),
    quiz=(
        Question(
            "Which mode truncates an existing file?",
            ("r", "a", "w", "x"),
            2,
            "'w' opens for writing and empties the file first.",
        ),
        Question(
            "Why use `with open(...) as f`?",
            (
                "It is faster",
                "It closes the file automatically, even on errors",
                "It encrypts data",
                "It locks the file forever",
            ),
            1,
            "The context manager guarantees cleanup.",
        ),
        Question(
            "What does `json.loads` take?",
            ("A file object", "A path", "A string", "A dict"),
            2,
            "loads = load from string; load reads a file object.",
        ),
        Question(
            "When does the `else` block of try/except run?",
            (
                "Always",
                "Only when an exception was raised",
                "Only when no exception was raised",
                "Never",
            ),
            2,
            "else runs after a successful try.",
        ),
        Question(
            "What does `raise X from exc` do?",
            ("Hides exc", "Chains X to its cause exc", "Retries", "Exits the program"),
            1,
            "It preserves the original exception as __cause__.",
        ),
        Question(
            "Values read by csv.DictReader are...",
            ("ints", "floats", "strings", "auto-typed"),
            2,
            "CSV has no types; convert yourself.",
        ),
        Question(
            "Which is the better way to build a path?",
            ("'a' + '/' + 'b'", "Path('a') / 'b'", "'a'.join('b')", "os.system('a/b')"),
            1,
            "pathlib's / operator is portable and readable.",
        ),
    ),
    cheatsheet=(
        "`Path.read_text/write_text/exists/glob/mkdir`",
        "`with open(p, encoding='utf-8') as fh`",
        "`json.loads/dumps/load/dump`",
        "`csv.DictReader/DictWriter` (newline='')",
        "`try/except X as e/else/finally`",
        "`class MyError(Exception)`; `raise A from B`",
    ),
    next_steps="Next: model the world with classes in module 08.",
)
