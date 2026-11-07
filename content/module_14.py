"""Module 14 content: performance: profiling, caching, Big-O and numpy."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=14,
    intro="Fast code starts with measurement. You will profile to find real hot spots, reason about algorithmic growth with Big-O, cache expensive results, choose better data structures and vectorise numeric work with numpy.",
    lessons=(
        Lesson(
            "Measure first",
            """
> Premature optimisation is the root of all evil. - Knuth

```python
timeit.timeit(lambda: f(), number=1000)      # micro-benchmarks
cProfile.run("main()", sort="cumtime")       # where does time go?
tracemalloc.start(); ...; tracemalloc.get_traced_memory()   # memory
```

Profile with realistic data, change one thing, measure again. Compare *relative* numbers; absolute times vary by machine.
""",
        ),
        Lesson(
            "Big-O",
            """
| Complexity | Example | n = 1,000,000 |
| --- | --- | --- |
| O(1) | dict/set lookup, list index | 1 |
| O(log n) | binary search (`bisect`) | ~20 |
| O(n) | scan a list, `x in list` | 10^6 |
| O(n log n) | `sorted()` | ~2x10^7 |
| O(n^2) | nested loops | 10^12 |
| O(2^n) | naive recursive fibonacci | hopeless |

Big-O describes **growth**, ignoring constants - great for choosing algorithms, silent about small inputs.
""",
        ),
        Lesson(
            "Caching and data structures",
            """
```python
@functools.lru_cache(maxsize=None)
def fib(n): ...                      # O(2^n) -> O(n)
```

Pick the container for the operation you repeat: membership -> `set`/`dict`; both ends -> `collections.deque`;
sorted insert/search -> `bisect`; counting -> `Counter`. Generators keep memory flat for big streams.
Cache only **pure** functions (same input, same output).
""",
        ),
        Lesson(
            "numpy basics",
            """
```python
import numpy as np
a = np.arange(6).reshape(2, 3)
a * 10 + 1               # vectorised, runs in C
a + np.array([1, 2, 3])  # broadcasting
a[a % 2 == 0]            # boolean mask
a.sum(axis=0)            # per column
```

Replace Python loops over numbers with array expressions: 10-100x faster. Arrays hold one `dtype`, so they are
compact. numpy is an optional dependency here: `pip install -e ".[data]"`.
""",
        ),
    ),
    examples=(
        Example(
            "profiling.py",
            "timeit, cProfile, tracemalloc",
            "Measure time and memory.",
            False,
        ),
        Example(
            "big_o_counts.py", "Big-O by counting", "Deterministic operation counts."
        ),
        Example(
            "data_structures.py",
            "Choosing data structures",
            "list vs set vs deque vs bisect.",
        ),
        Example(
            "numpy_basics.py",
            "numpy basics",
            "Arrays, broadcasting, masks and axis.",
            False,
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_binary_search.py",
            "Binary search",
            "find items in O(log n) steps.",
            2,
        ),
        Exercise("ex_02_memoize.py", "Memoize", "cache results by hand.", 2),
        Exercise(
            "ex_03_vectorize.py",
            "Vectorise with numpy",
            "no loops: arrays and masks.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What should you do before optimising?",
            (
                "Rewrite in C",
                "Measure with a profiler",
                "Add threads",
                "Cache everything",
            ),
            1,
            "Find the real bottleneck first.",
        ),
        Question(
            "What is the complexity of `x in some_list`?",
            ("O(1)", "O(log n)", "O(n)", "O(n^2)"),
            2,
            "A list is scanned linearly; a set is O(1).",
        ),
        Question(
            "Binary search on 1,000,000 sorted items needs about how many steps?",
            ("20", "1,000", "500,000", "1,000,000"),
            0,
            "log2(10^6) is about 20.",
        ),
        Question(
            "Which functions are safe to cache with lru_cache?",
            (
                "Any function",
                "Pure functions",
                "Functions that read files",
                "Functions with side effects",
            ),
            1,
            "Same inputs must always give the same output.",
        ),
        Question(
            "Which container gives O(1) appends AND pops at both ends?",
            ("list", "deque", "tuple", "set"),
            1,
            "collections.deque is built for that.",
        ),
        Question(
            "Why is numpy fast?",
            (
                "It uses threads only",
                "Vectorised operations run in compiled code on contiguous typed memory",
                "It skips checks",
                "It caches",
            ),
            1,
            "Loops happen in C, not in the interpreter.",
        ),
        Question(
            "What does broadcasting do?",
            (
                "Sends over a network",
                "Stretches smaller arrays to match shapes in operations",
                "Sorts",
                "Copies files",
            ),
            1,
            "It lets arrays of different shapes combine without loops.",
        ),
    ),
    cheatsheet=(
        "`timeit`, `cProfile`, `tracemalloc`",
        "O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n)",
        "`functools.lru_cache` for pure functions",
        "set/dict for lookup, deque for queues, bisect for sorted data",
        "numpy: vectorise, broadcast, mask, axis",
        "measure -> change one thing -> measure",
    ),
    next_steps="Next: tables and charts with pandas and matplotlib in module 15.",
)
