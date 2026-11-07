"""Module 18 content: capstone projects."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=18,
    intro="Time to build. Three self-contained projects tie the whole course together: a command-line habit tracker, a data-visualisation report and a small REST API. Read each example, run it, then extend it with the exercises.",
    lessons=(
        Lesson(
            "How to approach a capstone",
            """
1. **Slice it**: write the smallest version that runs end to end.
2. **Separate concerns**: pure logic (streaks, aggregation, services) away from I/O (files, HTTP, plots).
3. **Test the logic** with `check()`-style asserts or pytest; keep I/O thin.
4. **Make it a tool**: `main(argv)`, exit codes, helpful `--help`.
5. **Polish**: type hints, ruff/black/mypy, logging, README.
""",
        ),
        Lesson(
            "Capstone 1: CLI habit tracker",
            """
`examples/capstone_1_cli_tool.py` combines argparse subcommands, JSON persistence and date logic.
The interesting part is `current_streak()`: a pure function that is trivial to test, while `main()` only wires
arguments to logic and storage. Extend it: longest streak (exercise 1), `--remove`, weekly goals, CSV export.
""",
        ),
        Lesson(
            "Capstone 2: data-viz report",
            """
`examples/capstone_2_dataviz_report.py` generates reproducible synthetic sales (seeded numpy), summarises them
with a pandas pivot table, draws a matplotlib chart and writes a Markdown report. Needs the `data` extra.
Extend it: more charts, a `markdown_table` helper (exercise 2), HTML output, CLI arguments for the seed and size.
""",
        ),
        Lesson(
            "Capstone 3: a small API",
            """
`examples/capstone_3_small_api.py` (needs the `web` extra) keeps a clean service layer and a thin FastAPI shell.
`capstone_3b_stdlib_api.py` shows the same idea with only the standard library, so you can see what frameworks
automate. Extend it: write a tiny router (exercise 3), persistence, authentication, pagination, tests with `TestClient`.
""",
        ),
    ),
    examples=(
        Example(
            "capstone_1_cli_tool.py",
            "Capstone 1: habit tracker CLI",
            "argparse, JSON and a pure streak function.",
            False,
        ),
        Example(
            "capstone_2_dataviz_report.py",
            "Capstone 2: data-viz report",
            "pandas aggregation, matplotlib chart, Markdown report.",
            False,
        ),
        Example(
            "capstone_3_small_api.py",
            "Capstone 3: small FastAPI service",
            "service layer plus a thin web shell.",
            False,
        ),
        Example(
            "capstone_3b_stdlib_api.py",
            "Capstone 3b: stdlib API",
            "the same service with http.server.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_streaks.py", "Longest streak", "extend the habit tracker's logic.", 2
        ),
        Exercise(
            "ex_02_markdown_table.py",
            "Markdown table",
            "render report rows as a table.",
            2,
        ),
        Exercise(
            "ex_03_router.py",
            "A tiny router",
            "dispatch method + path with parameters.",
            3,
        ),
    ),
    quiz=(
        Question(
            "What is the best first step for a capstone?",
            (
                "Polish the UI",
                "Build the smallest end-to-end version",
                "Write all tests",
                "Choose a framework",
            ),
            1,
            "Get something working, then improve it.",
        ),
        Question(
            "Why keep pure logic separate from I/O?",
            ("It is shorter", "It is easy to test and reuse", "I/O is banned", "Speed"),
            1,
            "Pure functions need no files or network in tests.",
        ),
        Question(
            "Why seed a random generator in a report?",
            ("Faster", "Reproducible output", "Security", "Smaller files"),
            1,
            "The same seed gives the same data.",
        ),
        Question(
            "What does a thin web layer do?",
            (
                "Business rules",
                "Translate HTTP to service calls and errors to status codes",
                "Store data",
                "Format dates",
            ),
            1,
            "Services decide; routes translate.",
        ),
        Question(
            "Why return an exit code from `main()`?",
            (
                "Style",
                "Scripts and tests can detect failure",
                "It is required",
                "Speed",
            ),
            1,
            "Non-zero means error; SystemExit(main()) forwards it.",
        ),
        Question(
            "Which part of capstone 3b mirrors what FastAPI automates?",
            (
                "Printing",
                "Routing and JSON parsing/serialising by hand",
                "Imports",
                "Type hints",
            ),
            1,
            "Frameworks handle routing, parsing and validation.",
        ),
        Question(
            "What should you do after the project works?",
            (
                "Stop",
                "Add types, lint, tests, docs and logging",
                "Delete tests",
                "Rewrite in another language",
            ),
            1,
            "Quality work is part of the job.",
        ),
    ),
    cheatsheet=(
        "slice -> build -> separate logic from I/O -> test -> polish",
        "`main(argv) -> int`; `raise SystemExit(main())`",
        "seed randomness for reproducible reports",
        "services + thin routes",
        "document, type, lint, test, log",
    ),
    next_steps="Congratulations - you reached the end of ARSNEL. Keep building, keep reading other people's code, ship something real.",
)
