"""Module 09 content: iterators, generators, itertools and functools."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=9,
    intro="Iteration is Python's backbone. You will see exactly how for loops work, write lazy generators that handle infinite or huge data, and use itertools and functools as a functional toolbox.",
    lessons=(
        Lesson(
            "The iterator protocol",
            """
An **iterable** has `__iter__` returning an **iterator**; an iterator has `__next__` and raises `StopIteration`
when finished. A `for` loop is just `iter()` followed by repeated `next()`.

```python
it = iter([10, 20])
next(it); next(it); next(it, "default")
```

Iterators are **single-use**; an iterable like a list can create new ones whenever you loop again.
""",
        ),
        Lesson(
            "Generators",
            """
A function with `yield` returns a **generator**: values are produced lazily and the function pauses between them.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

squares = (n * n for n in range(10**9))     # generator expression: no memory cost
```

`yield from other` delegates to another iterable. Lazy pipelines process one item at a time, so memory stays flat.
""",
        ),
        Lesson(
            "itertools",
            """
| Function | Does |
| --- | --- |
| `chain(a, b)` / `chain.from_iterable` | concatenate iterables |
| `islice(it, n)` | slice any iterator |
| `count`, `cycle`, `repeat` | infinite sources |
| `product`, `permutations`, `combinations` | combinatorics |
| `accumulate`, `pairwise`, `zip_longest` | running results, neighbours, padding |
| `groupby(sorted_items, key)` | group **consecutive** equal keys |
""",
        ),
        Lesson(
            "functools",
            """
```python
from functools import partial, reduce, lru_cache, singledispatch

reduce(operator.mul, [1, 2, 3, 4])      # 24
hex_to_int = partial(int, base=16)
@lru_cache(maxsize=None)                # memoise pure functions
def fib(n): ...
```

`singledispatch` picks an implementation by argument type; `total_ordering` completes comparison methods.
""",
        ),
    ),
    examples=(
        Example(
            "iterators.py",
            "The iterator protocol",
            "iter(), next(), StopIteration and custom iterators.",
        ),
        Example(
            "generators.py",
            "Generators",
            "yield, yield from, lazy pipelines and expressions.",
        ),
        Example("itertools_tour.py", "itertools tour", "The building blocks."),
        Example(
            "functools_tour.py",
            "functools tour",
            "partial, reduce, lru_cache and singledispatch.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_countdown.py",
            "Countdown iterator",
            "implement __iter__ and __next__.",
            2,
        ),
        Exercise(
            "ex_02_generators.py",
            "Generator functions",
            "fibonacci, chunked and running_total.",
            2,
        ),
        Exercise(
            "ex_03_toolkit.py",
            "itertools + functools toolkit",
            "reduce, partial, chain and combinations.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What does an iterator raise when it has no more items?",
            ("IndexError", "StopIteration", "EOFError", "KeyError"),
            1,
            "StopIteration signals exhaustion to the for loop.",
        ),
        Question(
            "What does a function containing `yield` return when called?",
            ("A list", "A generator object", "None", "The first value"),
            1,
            "Calling it creates a generator; code runs on next().",
        ),
        Question(
            "Which is lazy?",
            (
                "[n for n in range(5)]",
                "(n for n in range(5))",
                "list(range(5))",
                "sorted(range(5))",
            ),
            1,
            "Parentheses create a generator expression.",
        ),
        Question(
            "What does itertools.groupby require for useful groups?",
            ("Unique keys", "Input sorted by the key", "A list", "Strings only"),
            1,
            "It groups consecutive items only.",
        ),
        Question(
            "What does @lru_cache do?",
            (
                "Limits recursion",
                "Caches results by arguments",
                "Locks threads",
                "Logs calls",
            ),
            1,
            "It memoises return values for repeated calls.",
        ),
        Question(
            "What is `list(itertools.islice(itertools.count(5), 3))`?",
            ("[5, 6, 7]", "[0, 1, 2]", "[5, 6]", "Infinite loop"),
            0,
            "count(5) yields 5, 6, 7... and islice takes 3.",
        ),
        Question(
            "An iterable that can be looped over twice has...",
            (
                "only __next__",
                "an __iter__ that returns a fresh iterator",
                "no methods",
                "a yield",
            ),
            1,
            "Each iter() call should start a new pass.",
        ),
    ),
    cheatsheet=(
        "`iter(x)`, `next(it, default)`",
        "`def gen(): yield x`; `yield from other`",
        "`(expr for x in it)` is lazy",
        "`itertools`: chain islice count product permutations combinations accumulate groupby",
        "`functools`: partial reduce lru_cache singledispatch total_ordering",
        "iterators are single-use",
    ),
    next_steps="Next: decorators, context managers and typing in module 10.",
)
