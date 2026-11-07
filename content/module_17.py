"""Module 17 content: best practices: clean code, logging, ruff/black/mypy and CI."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=17,
    intro="Working code is the start. These habits - readable style, structured logs, automatic formatting and linting, type checking and CI - are what keep projects healthy for years and make collaboration painless.",
    lessons=(
        Lesson(
            "Clean code",
            """
- **Names** reveal intent: `elapsed_seconds`, `is_valid`. **Functions** do one thing and fit on a screen.
- Prefer **guard clauses** over deep nesting; prefer data (a dict of rates) over long `if` chains.
- No magic numbers: name constants. Delete dead code; comment the *why*, not the *what*.
- Follow PEP 8 (style) and PEP 20 (`import this`): *explicit is better than implicit*, *readability counts*.
""",
        ),
        Lesson(
            "Logging, not printing",
            """
```python
log = logging.getLogger(__name__)      # one logger per module
log.info("loaded %d rows", n)          # lazy %-formatting
log.exception("failed")                # inside except: adds traceback
```

Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL. **Libraries** create loggers and never configure handlers;
the **application** configures them once (`logging.basicConfig` or `dictConfig`). Never log secrets.
""",
        ),
        Lesson(
            "Automate quality: ruff, black, mypy",
            """
```toml
[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP"]
[tool.mypy]
strict = true
```

`black` formats (no more style debates), `ruff` lints and sorts imports in milliseconds, `mypy` checks your type hints.
Run them locally, in `pre-commit`, and in CI so main is always green.
""",
        ),
        Lesson(
            "Continuous integration",
            """
A CI service (GitHub Actions) runs your quality gate on every push and pull request:

```yaml
- run: ruff check .
- run: black --check .
- run: mypy .
- run: pytest
```

Test on every supported Python version with a matrix. Keep the pipeline fast and the main branch protected.
Review checklist: tests added? errors handled? names clear? docs updated? secrets absent?
""",
        ),
    ),
    examples=(
        Example(
            "logging_demo.py",
            "The logging module",
            "Loggers, levels, handlers and dictConfig.",
        ),
        Example(
            "refactoring.py",
            "Refactoring before/after",
            "The same behaviour, clearer code.",
        ),
        Example(
            "tooling_config.py",
            "ruff, black and mypy config",
            "A pyproject snippet validated with tomllib.",
        ),
        Example("ci_workflow.py", "A CI workflow", "A GitHub Actions file explained."),
    ),
    exercises=(
        Exercise(
            "ex_01_make_logger.py",
            "Configure a logger",
            "handler, format and no duplicates.",
            2,
        ),
        Exercise(
            "ex_02_refactor_shipping.py",
            "Refactor with data",
            "guard clauses and a lookup table.",
            2,
        ),
        Exercise(
            "ex_03_validate_input.py",
            "Validate input",
            "specific errors and safe lookups.",
            2,
        ),
    ),
    quiz=(
        Question(
            "Which should a library do with logging handlers?",
            (
                "Add a StreamHandler",
                "Create loggers but leave handler configuration to the application",
                "Call basicConfig",
                "Print instead",
            ),
            1,
            "Applications own logging configuration.",
        ),
        Question(
            "Why `log.info('x=%s', x)` rather than an f-string?",
            (
                "It is shorter",
                "Formatting is skipped if the level is disabled",
                "f-strings are invalid",
                "It is required",
            ),
            1,
            "The message is only built when it will be emitted.",
        ),
        Question(
            "What does `black --check .` do?",
            (
                "Reformats files",
                "Fails if any file would be reformatted",
                "Lints",
                "Runs tests",
            ),
            1,
            "--check reports without modifying files.",
        ),
        Question(
            "Which tool checks type hints?",
            ("ruff", "black", "mypy", "pytest"),
            2,
            "mypy performs static type checking.",
        ),
        Question(
            "What is a guard clause?",
            (
                "A try block",
                "An early return/raise for invalid cases",
                "A decorator",
                "A loop",
            ),
            1,
            "It keeps the main path unindented.",
        ),
        Question(
            "What does CI stand for here?",
            (
                "Code Inspection",
                "Continuous Integration",
                "Compiled Image",
                "Central Index",
            ),
            1,
            "Automatically build and test every change.",
        ),
        Question(
            "What should never be written to logs?",
            (
                "Request ids",
                "Secrets such as passwords and tokens",
                "Timings",
                "Counts",
            ),
            1,
            "Logs are widely readable and long lived.",
        ),
    ),
    cheatsheet=(
        "PEP 8 style, PEP 20 philosophy",
        "`logging.getLogger(__name__)`; `log.exception`",
        "`ruff check`, `black --check`, `mypy`, `pytest`",
        "guard clauses; constants; small functions",
        "CI matrix on supported Pythons",
        "protect main; review checklist",
    ),
    next_steps="Next: build three real projects in module 18 (after data and web in modules 15-16).",
)
