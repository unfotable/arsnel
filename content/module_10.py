"""Module 10 content: decorators, context managers and typing."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=10,
    intro="Decorators wrap behaviour, context managers guarantee cleanup, and type hints document intent so tools can check it. Together they are the heart of idiomatic, professional Python.",
    lessons=(
        Lesson(
            "Decorators",
            """
A decorator is a function that takes a function and returns a function:

```python
import functools

def shout(func):
    @functools.wraps(func)           # keep name and docstring
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name): return f"hi {name}"
```

`@shout` is sugar for `greet = shout(greet)`. Stacked decorators apply bottom-up.
""",
        ),
        Lesson(
            "Decorators with arguments and classes",
            """
A decorator **factory** is a function returning a decorator:

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **k):
            for _ in range(times):
                result = func(*a, **k)
            return result
        return wrapper
    return decorator

@repeat(3)
def ping(): ...
```

Classes can be decorators too (implement `__call__`), and decorators can wrap classes.
""",
        ),
        Lesson(
            "Context managers",
            """
```python
with open("f.txt") as fh:          # __enter__ ... __exit__
    ...

from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        print(time.perf_counter() - start)
```

Use `contextlib.suppress(Error)` to ignore expected errors and `ExitStack` for a dynamic number of resources.
""",
        ),
        Lesson(
            "Type hints",
            """
```python
def first(items: list[int], default: int | None = None) -> int | None: ...
```

Hints are **not enforced at runtime**; tools like `mypy` check them. Useful pieces:
`list[int]`, `dict[str, int]`, `X | None`, `Callable[[int], str]`, `TypeVar` for generics,
`TypedDict`, `Literal["a", "b"]`, `Protocol` for structural typing, `ParamSpec` for decorators.
Run `mypy .` in CI so the hints stay true.
""",
        ),
    ),
    examples=(
        Example(
            "decorators_basics.py",
            "Decorators from scratch",
            "Closures, functools.wraps and stacking.",
        ),
        Example(
            "decorator_factories.py",
            "Decorators with arguments",
            "Factories, class-based decorators and class decorators.",
        ),
        Example(
            "context_managers.py",
            "Context managers",
            "__enter__/__exit__, contextlib and ExitStack.",
        ),
        Example(
            "typing_basics.py",
            "Type hints",
            "Unions, generics, Callable, TypedDict, Literal, Protocol.",
        ),
        Example(
            "typed_decorators.py",
            "Typed decorators",
            "ParamSpec and a taste of the mypy workflow.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_count_calls.py",
            "Count calls",
            "a decorator that counts and keeps metadata.",
            2,
        ),
        Exercise("ex_02_retry.py", "Retry", "a decorator factory with an argument.", 3),
        Exercise(
            "ex_03_temp_chdir.py",
            "Context manager and generics",
            "restore state with try/finally; a typed helper.",
            2,
        ),
    ),
    quiz=(
        Question(
            "`@deco` above `def f` is equivalent to...",
            ("f = deco", "f = deco(f)", "deco = f(deco)", "f()"),
            1,
            "The decorator is called with the function and its result replaces the name.",
        ),
        Question(
            "What does functools.wraps do?",
            (
                "Speeds up calls",
                "Copies the wrapped function's name and docstring onto the wrapper",
                "Adds type hints",
                "Makes it async",
            ),
            1,
            "It preserves metadata for introspection and debugging.",
        ),
        Question(
            "A decorator that takes arguments needs how many nested functions (typically)?",
            ("1", "2", "3", "0"),
            2,
            "factory -> decorator -> wrapper.",
        ),
        Question(
            "What runs when a `with` block exits due to an exception?",
            ("Nothing", "__exit__", "__enter__", "__del__ only"),
            1,
            "__exit__ always runs, receiving the exception details.",
        ),
        Question(
            "Are type hints enforced at runtime by Python?",
            (
                "Yes always",
                "No, tools like mypy check them",
                "Only for ints",
                "Only in functions",
            ),
            1,
            "CPython ignores annotations when running.",
        ),
        Question(
            "Which writes a union of int and None?",
            ("int & None", "int | None", "int + None", "Union[int]"),
            1,
            "X | None (PEP 604) is the modern spelling of Optional[X].",
        ),
        Question(
            "What does `yield` do inside a @contextmanager function?",
            (
                "Ends the function",
                "Marks where the with-body runs",
                "Raises an error",
                "Returns a list",
            ),
            1,
            "Code before yield is __enter__, after is __exit__.",
        ),
    ),
    cheatsheet=(
        "`@functools.wraps(func)` in every wrapper",
        "`@decorator(arg)` = factory returning a decorator",
        "`with ctx as x:`; `@contextmanager` + `yield`",
        "`contextlib.suppress`, `ExitStack`",
        "`X | None`, `list[int]`, `Callable[[A], B]`, `TypeVar`",
        "run `mypy` to check hints",
    ),
    next_steps="Next: do many things at once with async, threads and processes in module 11.",
)
