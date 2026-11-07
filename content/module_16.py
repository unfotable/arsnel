"""Module 16 content: web: HTTP, FastAPI and a tiny CLI tool."""

from __future__ import annotations

from arsnel.models import Example, Exercise, Lesson, ModuleContent, Question

CONTENT = ModuleContent(
    number=16,
    intro="Programs become useful to others through interfaces. You will see what HTTP really is, build a command-line tool with argparse, and expose logic as a typed REST API with FastAPI. FastAPI comes from the optional web extra.",
    lessons=(
        Lesson(
            "HTTP in 60 seconds",
            """
A **request** has a method (`GET` read, `POST` create, `PUT/PATCH` update, `DELETE` remove), a path, optional query
string and body. A **response** has a status code and body (often JSON):

| Code | Meaning |
| --- | --- |
| 200 / 201 | OK / created |
| 400 / 422 | bad request / validation error |
| 404 | not found |
| 500 | server error |

The standard library can serve and call HTTP (`http.server`, `urllib.request`), which is great for learning.
""",
        ),
        Lesson(
            "Command-line tools with argparse",
            """
```python
parser = argparse.ArgumentParser(prog="todo")
sub = parser.add_subparsers(dest="command", required=True)
add = sub.add_parser("add"); add.add_argument("title")
args = parser.parse_args(argv)

def main(argv=None) -> int: ...          # return an exit code
if __name__ == "__main__":
    raise SystemExit(main())
```

Take `argv` as a parameter so tests can call `main([...])`. Return codes: 0 success, non-zero failure.
Expose the tool with `[project.scripts]` in `pyproject.toml` (module 13).
""",
        ),
        Lesson(
            "FastAPI",
            """
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)

@app.post("/items", status_code=201, response_model=Item)
def create(item: Item) -> Item: ...

@app.get("/items/{item_id}")
def read(item_id: int, verbose: bool = False): ...
```

Type hints drive parsing, validation and the interactive docs at `/docs`. Run with
`uvicorn module:app --reload`. Test in-process with `fastapi.testclient.TestClient` (needs `httpx`).
""",
        ),
        Lesson(
            "Structure: keep logic out of routes",
            """
Put business rules in plain classes/functions (a **service** or **repository**), and keep route functions thin:
parse input -> call service -> translate errors to `HTTPException`. Use `Depends(...)` to inject the service so
tests can swap it. This is also why the exercises here need no web framework to run.
""",
        ),
    ),
    examples=(
        Example(
            "stdlib_http.py",
            "HTTP with the standard library",
            "A server thread and a urllib client.",
        ),
        Example(
            "cli_tool.py",
            "A command-line tool",
            "argparse subcommands, JSON storage, testable main().",
        ),
        Example(
            "fastapi_basics.py",
            "FastAPI basics",
            "Path/query params, bodies, errors and TestClient.",
            False,
        ),
        Example(
            "fastapi_dependencies.py",
            "FastAPI dependencies",
            "Routers and dependency injection.",
            False,
        ),
    ),
    exercises=(
        Exercise(
            "ex_01_validate_user.py",
            "Validate a request body",
            "return every problem with a payload.",
            2,
        ),
        Exercise(
            "ex_02_todo_repo.py",
            "In-memory repository",
            "the storage behind a REST API.",
            2,
        ),
        Exercise(
            "ex_03_build_parser.py",
            "Build a CLI parser",
            "argparse subcommands and types.",
            2,
        ),
    ),
    quiz=(
        Question(
            "Which HTTP method is meant for creating a resource?",
            ("GET", "POST", "HEAD", "TRACE"),
            1,
            "POST creates; GET must not change state.",
        ),
        Question(
            "What does status 404 mean?",
            ("Server crashed", "Resource not found", "Created", "Unauthorised"),
            1,
            "The path does not map to a resource.",
        ),
        Question(
            "Why should `main(argv)` take argv as a parameter?",
            (
                "Speed",
                "So tests can call it with arguments",
                "It is required by Python",
                "Security",
            ),
            1,
            "Parameters make code testable.",
        ),
        Question(
            "In FastAPI, what validates the JSON body?",
            ("The route name", "Pydantic models via type hints", "uvicorn", "argparse"),
            1,
            "Annotated parameters become validated models.",
        ),
        Question(
            "What does `Depends(get_repo)` do?",
            (
                "Imports a module",
                "Injects a dependency into the route",
                "Starts a server",
                "Creates a thread",
            ),
            1,
            "FastAPI calls the dependency and passes its result.",
        ),
        Question(
            "How do you run a FastAPI app in development?",
            (
                "python app.py always",
                "uvicorn module:app --reload",
                "pip run app",
                "fastapi.exe",
            ),
            1,
            "uvicorn is the ASGI server.",
        ),
        Question(
            "Why keep business logic out of route functions?",
            (
                "Style only",
                "Easier to test and reuse without HTTP",
                "Faster",
                "Required by pydantic",
            ),
            1,
            "Thin routes translate; services decide.",
        ),
    ),
    cheatsheet=(
        "HTTP: method + path + body -> status + body",
        '`argparse`: `add_subparsers`, `type=int`, `action="count"`',
        "`def main(argv=None) -> int`",
        "FastAPI: `@app.get/post`, pydantic models, `HTTPException`",
        "`TestClient(app)` for in-process tests",
        "thin routes, fat services; `Depends`",
    ),
    next_steps="Next: ship your projects with best practices in module 17, then build the capstones in module 18.",
)
