"""Module 00 content: setup and the terminal."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=0,
    intro=(
        "Before any code: get Python installed, learn the five shell commands you "
        "will use every day, create an isolated virtual environment and run a script "
        "four different ways. This module is mostly about *workflow* - the habits "
        "that make everything later smoother."
    ),
    lessons=(
        Lesson(
            "Installing Python",
            """
Install Python 3.11 or newer from [python.org](https://www.python.org/downloads/),
your OS package manager (`brew install python`, `apt install python3`) or a
tool such as `pyenv`/`uv`. Check it worked:

```bash
python --version      # or: python3 --version
python -c "print('it works')"
```

On Windows the launcher `py` picks a version: `py -3.12 --version`.
Always know *which* interpreter you are using - `python -c "import sys; print(sys.executable)"`.
""",
        ),
        Lesson(
            "The terminal in five commands",
            """
| Command | Meaning |
| --- | --- |
| `pwd` | print the current directory |
| `ls` (`dir` on Windows) | list files |
| `cd folder` / `cd ..` | enter / leave a folder |
| `mkdir name` | create a folder |
| `cat file` (`type` on Windows) | print a file |

Paths can be **absolute** (`/home/ada/project`) or **relative** (`../data`).
Tab completes names; the up arrow recalls history. `Ctrl+C` stops a running program.
""",
        ),
        Lesson(
            "Virtual environments and pip",
            """
A **virtual environment** is a private folder of packages for one project, so
projects never fight over versions.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
python -m pip install --upgrade pip
python -m pip install requests
python -m pip freeze > requirements.txt
deactivate
```

Use `python -m pip` so pip always matches the interpreter. Never commit `.venv/`.
""",
        ),
        Lesson(
            "Running scripts and reading arguments",
            """
There are several ways to run code:

```bash
python script.py            # a file
python -c "print(1 + 1)"    # a one-liner
python -m module_name       # a module (e.g. python -m venv)
python                      # the interactive REPL (exit with Ctrl+D / exit())
```

Scripts receive command-line arguments in `sys.argv` (a list of strings;
index 0 is the script name). For anything non-trivial use `argparse`, which
adds `--help`, types and validation for free.
""",
        ),
    ),
    examples=(
        Example(
            "python_environment.py",
            "Ask Python about itself",
            "Version, executable, platform and the module search path.",
            False,
        ),
        Example(
            "shell_basics.py",
            "Shell ideas with pathlib",
            "pwd, ls, cd, mkdir and cat re-created in Python.",
            False,
        ),
        Example(
            "make_venv.py",
            "Create a virtual environment",
            "Build a venv in a temp folder and peek inside.",
            False,
        ),
        Example(
            "running_code.py",
            "Four ways to run Python",
            "Run a file, -c, -m and stdin, driven from Python.",
            False,
        ),
        Example(
            "script_arguments.py",
            "Command-line arguments",
            "sys.argv by hand, then argparse.",
            False,
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_parse_command.py",
            "Parse a command line",
            "split a shell-like command into parts.",
            1,
        ),
        Exercise(
            "ex_02_activation_command.py",
            "Venv activation command",
            "return the right activate command per OS.",
            1,
        ),
        Exercise(
            "ex_03_version_check.py",
            "Compare Python versions",
            "parse and compare version strings.",
            2,
        ),
        Exercise(
            "ex_04_simulate_cd.py",
            "Simulate cd",
            "resolve relative paths like the shell does.",
            2,
        ),
    ),
    quiz=(
        Question(
            "Which command creates a virtual environment in `.venv`?",
            (
                "pip venv .venv",
                "python -m venv .venv",
                "python venv create .venv",
                "virtualenv install .venv",
            ),
            1,
            "The standard library module `venv` is run with `python -m venv`.",
        ),
        Question(
            "Why prefer `python -m pip install x` over `pip install x`?",
            (
                "It is faster",
                "It always uses the pip of that exact interpreter",
                "It skips dependency checks",
                "It works offline",
            ),
            1,
            "`python -m pip` guarantees the pip matches the interpreter you called.",
        ),
        Question(
            "In `python script.py a b`, what is `sys.argv`?",
            (
                "['a', 'b']",
                "['script.py', 'a', 'b']",
                "('script.py', 'a', 'b')",
                "'script.py a b'",
            ),
            1,
            "`sys.argv` is a list of strings whose first item is the script name.",
        ),
        Question(
            "What does `cd ..` do?",
            (
                "Lists parent files",
                "Moves to the parent directory",
                "Deletes the folder",
                "Moves to the home directory",
            ),
            1,
            "`..` means the parent directory.",
        ),
        Question(
            "What should you NOT commit to Git?",
            ("pyproject.toml", "The `.venv/` folder", "README.md", "Your source code"),
            1,
            "Virtual environments are large, machine specific and reproducible from requirements files.",
        ),
        Question(
            "Which runs a standard-library module as a script?",
            (
                "python -m http.server",
                "python -c http.server",
                "python http.server.py",
                "python --run http.server",
            ),
            0,
            "`-m` runs a module by name, searching `sys.path`.",
        ),
    ),
    cheatsheet=(
        '`python --version`, `python -c "..."`, `python -m module`',
        "`python -m venv .venv` then activate it",
        "`python -m pip install|freeze|list`",
        "`pwd`, `ls`, `cd`, `mkdir`, `cat`",
        "`sys.argv` for raw args, `argparse` for real CLIs",
    ),
    next_steps="Next: write real programs - variables, types and I/O - in module 01.",
)
