"""The ARSNEL curriculum manifest: modules, skills, concepts and algorithms.

Everything the charts, README and site need to know about the curriculum's
*shape* lives here. The learner-facing prose lives in ``content/module_NN.py``.
"""

from __future__ import annotations

from dataclasses import dataclass

from arsnel.models import ModuleMeta

# Radar-chart axes, in display order.
SKILLS: tuple[str, ...] = (
    "Foundations",
    "Data Structures",
    "Functions & Modules",
    "I/O & Errors",
    "OOP",
    "Idioms",
    "Concurrency",
    "Quality",
    "Shipping & Perf",
    "Data & Web",
    "Capstone",
)


def _m(
    number: int,
    slug: str,
    title: str,
    tagline: str,
    level: str,
    skill: str,
    hours: float,
    prereq: tuple[int, ...] = (),
) -> ModuleMeta:
    return ModuleMeta(number, slug, title, tagline, level, skill, hours, prereq)


MODULES: tuple[ModuleMeta, ...] = (
    _m(
        0,
        "setup",
        "Setup & the terminal",
        "Install Python, master the shell, make a venv, run your first script.",
        "BEGINNER",
        "Foundations",
        1.5,
    ),
    _m(
        1,
        "syntax",
        "Syntax, variables, types & I/O",
        "Names, numbers, text, booleans, and talking to the user.",
        "BEGINNER",
        "Foundations",
        3,
        (0,),
    ),
    _m(
        2,
        "control_flow",
        "Operators, conditionals & loops",
        "Make decisions and repeat work with if, for and while.",
        "BEGINNER",
        "Foundations",
        3,
        (1,),
    ),
    _m(
        3,
        "strings",
        "Strings & formatting",
        "Slice, search, transform and format text with f-strings.",
        "BEGINNER",
        "Foundations",
        2.5,
        (1,),
    ),
    _m(
        4,
        "collections",
        "Lists, tuples, sets, dicts & comprehensions",
        "Python's built-in containers and the comprehension one-liners.",
        "BEGINNER",
        "Data Structures",
        4,
        (2, 3),
    ),
    _m(
        5,
        "functions",
        "Functions, *args/**kwargs, lambdas & closures",
        "Package behaviour into reusable, flexible callables.",
        "INTERMEDIATE",
        "Functions & Modules",
        3.5,
        (4,),
    ),
    _m(
        6,
        "modules",
        "Modules, packages, venv, pip & project layout",
        "Split code into files, install libraries, structure a project.",
        "INTERMEDIATE",
        "Functions & Modules",
        3,
        (5,),
    ),
    _m(
        7,
        "files_errors",
        "Files, JSON, CSV, pathlib & exceptions",
        "Read and write data on disk and handle failure gracefully.",
        "INTERMEDIATE",
        "I/O & Errors",
        4,
        (5,),
    ),
    _m(
        8,
        "oop",
        "OOP: classes, dunders, inheritance, dataclasses & protocols",
        "Model the world with objects and make them feel native.",
        "INTERMEDIATE",
        "OOP",
        5,
        (5, 7),
    ),
    _m(
        9,
        "iterators",
        "Iterators, generators, itertools & functools",
        "Lazy sequences, pipelines and functional toolkits.",
        "INTERMEDIATE",
        "Idioms",
        4,
        (8,),
    ),
    _m(
        10,
        "decorators",
        "Decorators, context managers & typing",
        "Wrap behaviour, manage resources and annotate your intent.",
        "INTERMEDIATE",
        "Idioms",
        4.5,
        (5, 8),
    ),
    _m(
        11,
        "concurrency",
        "Async/await, threads & multiprocessing",
        "Do many things at once: I/O-bound and CPU-bound.",
        "ADVANCED",
        "Concurrency",
        5,
        (9, 10),
    ),
    _m(
        12,
        "testing",
        "Testing: pytest, fixtures, mocking & TDD",
        "Prove your code works, then keep proving it.",
        "ADVANCED",
        "Quality",
        4,
        (8, 10),
    ),
    _m(
        13,
        "packaging",
        "Packaging, pyproject.toml & publishing to PyPI",
        "Turn a folder of scripts into an installable distribution.",
        "ADVANCED",
        "Shipping & Perf",
        3.5,
        (6, 12),
    ),
    _m(
        14,
        "performance",
        "Performance: profiling, caching, Big-O & numpy basics",
        "Measure first, then make it fast.",
        "ADVANCED",
        "Shipping & Perf",
        4.5,
        (9, 10),
    ),
    _m(
        15,
        "data_viz",
        "Data & viz: pandas, matplotlib & Plotly",
        "Wrangle tables and turn numbers into pictures.",
        "ADVANCED",
        "Data & Web",
        5,
        (14,),
    ),
    _m(
        16,
        "web",
        "Web: FastAPI & a tiny CLI tool",
        "Ship an HTTP API and a command-line tool.",
        "ADVANCED",
        "Data & Web",
        5,
        (10, 11, 12),
    ),
    _m(
        17,
        "best_practices",
        "Best practices: clean code, logging, ruff/black/mypy & CI",
        "The habits that keep real projects healthy.",
        "ADVANCED",
        "Quality",
        4,
        (12, 13),
    ),
    _m(
        18,
        "capstones",
        "Capstone projects",
        "Build three real projects: a CLI tool, a data-viz report and a small API.",
        "ADVANCED",
        "Capstone",
        12,
        (15, 16, 17),
    ),
)

_BY_NUMBER: dict[int, ModuleMeta] = {m.number: m for m in MODULES}


def get_module(number: int) -> ModuleMeta:
    """Return the :class:`ModuleMeta` for ``number`` (raises ``KeyError``)."""
    return _BY_NUMBER[number]


# --------------------------------------------------------------------------- #
# Concept dependency graph: concept -> (module that teaches it, prerequisites)
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Concept:
    """A teachable concept and the concepts it builds on."""

    name: str
    module: int
    requires: tuple[str, ...] = ()


CONCEPTS: tuple[Concept, ...] = (
    Concept("terminal", 0),
    Concept("venv", 0, ("terminal",)),
    Concept("variables", 1, ("terminal",)),
    Concept("types", 1, ("variables",)),
    Concept("input/output", 1, ("variables",)),
    Concept("operators", 2, ("types",)),
    Concept("conditionals", 2, ("operators",)),
    Concept("loops", 2, ("conditionals",)),
    Concept("strings", 3, ("types",)),
    Concept("f-strings", 3, ("strings",)),
    Concept("lists", 4, ("loops",)),
    Concept("dicts", 4, ("lists", "types")),
    Concept("sets", 4, ("lists",)),
    Concept("comprehensions", 4, ("lists", "loops")),
    Concept("functions", 5, ("conditionals", "variables")),
    Concept("args/kwargs", 5, ("functions",)),
    Concept("closures", 5, ("functions",)),
    Concept("modules", 6, ("functions",)),
    Concept("packages", 6, ("modules", "venv")),
    Concept("files", 7, ("strings", "functions")),
    Concept("exceptions", 7, ("functions",)),
    Concept("json/csv", 7, ("files", "dicts")),
    Concept("classes", 8, ("functions", "dicts")),
    Concept("inheritance", 8, ("classes",)),
    Concept("dunders", 8, ("classes",)),
    Concept("dataclasses", 8, ("classes",)),
    Concept("iterators", 9, ("dunders", "loops")),
    Concept("generators", 9, ("iterators", "functions")),
    Concept("decorators", 10, ("closures",)),
    Concept("context mgrs", 10, ("dunders", "exceptions")),
    Concept("typing", 10, ("classes", "functions")),
    Concept("async", 11, ("generators",)),
    Concept("threads", 11, ("functions",)),
    Concept("multiprocessing", 11, ("threads",)),
    Concept("pytest", 12, ("functions", "exceptions")),
    Concept("mocking", 12, ("pytest", "classes")),
    Concept("packaging", 13, ("packages",)),
    Concept("profiling", 14, ("functions",)),
    Concept("big-O", 14, ("loops", "lists", "dicts")),
    Concept("numpy", 14, ("lists",)),
    Concept("pandas", 15, ("numpy", "dicts")),
    Concept("matplotlib", 15, ("numpy",)),
    Concept("fastapi", 16, ("decorators", "typing", "async")),
    Concept("cli", 16, ("modules", "functions")),
    Concept("logging", 17, ("exceptions",)),
    Concept("lint + CI", 17, ("pytest", "packaging")),
    Concept("capstone", 18, ("pandas", "fastapi", "lint + CI")),
)


# --------------------------------------------------------------------------- #
# Algorithms taught, for the Big-O chart: (label, complexity, module)
# --------------------------------------------------------------------------- #
COMPLEXITY_ORDER: tuple[str, ...] = (
    "O(1)",
    "O(log n)",
    "O(n)",
    "O(n log n)",
    "O(n^2)",
    "O(2^n)",
)

ALGORITHMS: tuple[tuple[str, str, int], ...] = (
    ("dict / set lookup", "O(1)", 4),
    ("list index", "O(1)", 4),
    ("binary search (bisect)", "O(log n)", 14),
    ("linear scan / `in` on a list", "O(n)", 4),
    ("memoised fibonacci", "O(n)", 14),
    ("sorted() / list.sort()", "O(n log n)", 14),
    ("nested loops / bubble sort", "O(n^2)", 2),
    ("naive recursive fibonacci", "O(2^n)", 5),
)
