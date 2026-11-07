"""A tiny command-line tool with subcommands, JSON storage and testable main()."""

import argparse
import json
import tempfile
from collections.abc import Sequence
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="A tiny todo list")
    parser.add_argument("--file", type=Path, required=True, help="JSON storage file")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add", help="add a task")
    add.add_argument("title")
    done = sub.add_parser("done", help="complete a task")
    done.add_argument("number", type=int)
    sub.add_parser("list", help="show tasks")
    return parser


def load(path: Path) -> list[dict[str, object]]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def main(argv: Sequence[str] | None = None) -> int:
    """Return an exit code instead of calling sys.exit: easy to test."""
    args = build_parser().parse_args(argv)
    tasks = load(args.file)
    if args.command == "add":
        tasks.append({"title": args.title, "done": False})
        print(f"added #{len(tasks)}: {args.title}")
    elif args.command == "done":
        if not 1 <= args.number <= len(tasks):
            print(f"error: no task #{args.number}")
            return 1
        tasks[args.number - 1]["done"] = True
        print(f"completed #{args.number}")
    else:
        for number, task in enumerate(tasks, start=1):
            mark = "x" if task["done"] else " "
            print(f"[{mark}] {number}. {task['title']}")
    args.file.write_text(json.dumps(tasks), encoding="utf-8")
    return 0


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        store = str(Path(tmp) / "todo.json")
        for line in (
            ["add", "write code"],
            ["add", "ship it"],
            ["done", "1"],
            ["done", "9"],
            ["list"],
        ):
            print("$ todo", *line)
            main(["--file", store, *line])
