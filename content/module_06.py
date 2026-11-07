"""Module 06 content: modules, packages, venv, pip and project layout."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=6,
    intro="Real programs span many files and use other people's code. You will learn how imports work, how to build a package, how virtual environments and pip fit together and how to lay out a project.",
    lessons=(
        Lesson(
            "Modules and imports",
            """
Any `.py` file is a **module**. Import it by name:

```python
import math                     # math.sqrt(2)
from math import sqrt, pi       # sqrt(2)
import numpy as np              # alias
```

Python searches `sys.path` (script folder, standard library, site-packages). Importing runs the module
once and caches it in `sys.modules`. Avoid `from x import *`.
""",
        ),
        Lesson(
            "The main guard",
            """
```python
def main() -> None: ...

if __name__ == "__main__":
    main()
```

`__name__` is `"__main__"` when you run the file and the module's name when it is imported,
so the guard lets a file be both a script and a library.
""",
        ),
        Lesson(
            "Packages",
            """
A **package** is a folder of modules, usually with an `__init__.py`:

```text
greeter/
  __init__.py      # often re-exports the public API
  core.py
```

Use absolute imports (`from greeter.core import greet`) or explicit relative ones (`from .core import greet`).
`__all__` lists what `from pkg import *` exposes.
""",
        ),
        Lesson(
            "venv, pip and project layout",
            """
```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install requests
python -m pip freeze > requirements.txt
```

Recommended layout: `src/yourpkg/`, `tests/`, `pyproject.toml`, `README.md`, `.gitignore`.
Pin application dependencies; give libraries version *ranges*.
""",
        ),
    ),
    examples=(
        Example(
            "imports_demo.py",
            "Import styles",
            "import, from-import, aliases and the main guard.",
        ),
        Example(
            "build_package.py",
            "Build and import a package",
            "Create a package in a temp dir and import it dynamically.",
        ),
        Example(
            "project_layout.py",
            "A src-layout tree",
            "Generate a recommended project and print its tree.",
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_safe_import.py",
            "Safe import",
            "import by name and handle ModuleNotFoundError.",
            1,
        ),
        Exercise(
            "ex_02_make_package.py",
            "Make a package",
            "write a package on disk and import it.",
            2,
        ),
        Exercise(
            "ex_03_layout_tree.py", "Layout tree", "indent path strings into a tree.", 3
        ),
    ),
    quiz=(
        Question(
            "What is `__name__` when a file is run directly?",
            ("'main'", "'__main__'", "the file name", "None"),
            1,
            "The interpreter sets it to '__main__'.",
        ),
        Question(
            "Where does Python look for modules?",
            ("Only the current folder", "sys.path", "The internet", "PATH"),
            1,
            "sys.path lists the search locations.",
        ),
        Question(
            "What marks a folder as a regular package?",
            ("__init__.py", "package.json", "setup.cfg", "main.py"),
            0,
            "__init__.py makes it a regular package.",
        ),
        Question(
            "Why use a virtual environment?",
            (
                "Faster code",
                "Isolate each project's dependencies",
                "Encrypt code",
                "Compile Python",
            ),
            1,
            "Projects get their own package versions.",
        ),
        Question(
            "What does `from math import sqrt` add to your namespace?",
            ("math", "sqrt", "everything", "nothing"),
            1,
            "Only the name sqrt is bound.",
        ),
        Question(
            "Which command freezes installed packages?",
            ("pip freeze", "pip list --lock", "pip save", "pip dump"),
            0,
            "pip freeze prints name==version lines.",
        ),
        Question(
            "Why is `from module import *` discouraged?",
            (
                "It is slow",
                "It hides where names come from and can overwrite yours",
                "It is removed",
                "It needs admin",
            ),
            1,
            "Explicit imports keep code readable.",
        ),
    ),
    cheatsheet=(
        "`import x`, `from x import y`, `import x as z`",
        '`if __name__ == "__main__":` guard',
        "package = folder + `__init__.py`",
        "`python -m venv .venv`; `python -m pip install ...`",
        "src layout: `src/pkg`, `tests`, `pyproject.toml`",
        "`sys.path`, `importlib.import_module`",
    ),
    next_steps="Next: persist data and handle errors in module 07.",
)
