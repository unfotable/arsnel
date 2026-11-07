"""Module 05 content: functions, *args/**kwargs, lambdas and closures."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=5,
    intro="Functions are Python's unit of reuse - and values you can pass around. Here you learn every kind of parameter, how scope works, and how closures and lambdas let functions build other functions.",
    lessons=(
        Lesson(
            "Defining functions and parameters",
            """
```python
def power(base: float, exp: int = 2, *, verbose: bool = False) -> float:
    \"\"\"Return base ** exp.\"\"\"
    return base ** exp
```

- **Positional** `base`, **default** `exp`, **keyword-only** after `*` (`verbose`).
- Call by position or keyword: `power(3)`, `power(3, exp=3)`.
- **Never use a mutable default** (`def f(x=[])`): it is created once and shared. Use `None` and create inside.
- A function without `return` returns `None`.
""",
        ),
        Lesson(
            "*args and **kwargs",
            """
`*args` collects extra positional arguments into a **tuple**, `**kwargs` collects extra keyword arguments into a **dict**.

```python
def log(level, *messages, **context): ...
log("INFO", "a", "b", user="ada")
nums = [1, 2, 3]; opts = {"sep": "-"}
print(*nums, **opts)        # unpack when calling
```
""",
        ),
        Lesson(
            "Scope, closures and lambdas",
            """
Python looks names up **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in (LEGB).
Assignment inside a function creates a local; use `nonlocal` to rebind an enclosing variable.

A **closure** is a function that remembers variables of the scope that created it:

```python
def make_adder(n):
    return lambda x: x + n
add5 = make_adder(5); add5(1)   # 6
```

`lambda` makes small anonymous functions - handy as `key=`, not for multi-line logic.
Gotcha: closures capture *variables*, not values (late binding in loops).
""",
        ),
        Lesson(
            "Functions as values, recursion and docstrings",
            """
Functions are objects: store them in lists/dicts, pass them as arguments, return them.

**Recursion** = a function calling itself; it needs a **base case**. CPython limits depth
(`sys.getrecursionlimit()`, default 1000), so prefer loops for deep iteration.

Document with a docstring: one summary line, then details. Type hints describe the contract.
""",
        ),
    ),
    examples=(
        Example(
            "parameters.py",
            "Parameter kinds",
            "Positional, keyword, defaults, keyword-only and the mutable-default trap.",
        ),
        Example(
            "args_and_kwargs.py",
            "*args and **kwargs",
            "Collecting and unpacking arguments.",
        ),
        Example(
            "scope_and_closures.py",
            "Scope and closures",
            "LEGB, nonlocal, closures and late binding.",
        ),
        Example(
            "first_class_functions.py",
            "Functions as values",
            "Passing, storing and returning functions; lambdas.",
        ),
        Example(
            "recursion_and_docstrings.py",
            "Recursion and docstrings",
            "Base cases, the recursion limit and good docs.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_clamp_and_stats.py",
            "Clamp and stats",
            "defaults, keyword-only and *args.",
            1,
        ),
        Exercise(
            "ex_02_make_counter.py", "Closures", "a counter factory and compose().", 2
        ),
        Exercise(
            "ex_03_build_url.py",
            "Flexible signatures",
            "*parts and **params together.",
            2,
        ),
    ),
    quiz=(
        Question(
            "What does a function return if it has no return statement?",
            ("0", "None", "An empty string", "It raises an error"),
            1,
            "Falling off the end returns None.",
        ),
        Question(
            "Why is `def f(items=[])` dangerous?",
            (
                "It is a syntax error",
                "The list is created once and shared between calls",
                "It is slower",
                "It cannot be called",
            ),
            1,
            "Defaults are evaluated once at definition time.",
        ),
        Question(
            "In `def f(*args, **kwargs)`, what are the types of args and kwargs?",
            ("list and dict", "tuple and dict", "tuple and tuple", "set and dict"),
            1,
            "*args is a tuple; **kwargs is a dict.",
        ),
        Question(
            "Which keyword rebinds a variable of the enclosing function?",
            ("global", "nonlocal", "outer", "static"),
            1,
            "nonlocal binds to the nearest enclosing function scope.",
        ),
        Question(
            "What is `(lambda x: x * 2)(4)`?",
            ("4", "8", "A function", "Error"),
            1,
            "The lambda is called immediately with 4.",
        ),
        Question(
            "What does LEGB stand for?",
            (
                "Local, Enclosing, Global, Built-in",
                "Loop, Exception, Generator, Block",
                "Lambda, Eval, Global, Base",
                "Local, Extern, General, Builtin",
            ),
            0,
            "It is the order Python searches for a name.",
        ),
        Question(
            "What does `def f(a, *, b)` mean?",
            (
                "b is optional",
                "b must be passed by keyword",
                "a must be a keyword",
                "b collects extras",
            ),
            1,
            "Parameters after a bare * are keyword-only.",
        ),
    ),
    cheatsheet=(
        "`def f(a, b=1, *args, key=None, **kw)`",
        "`f(*list, **dict)` unpacks when calling",
        "LEGB lookup; `nonlocal` / `global`",
        "`lambda x: expr` for tiny callables",
        "closures remember enclosing variables",
        "recursion needs a base case",
    ),
    next_steps="Next: split code across files with modules and packages in module 06.",
)
