"""Exercise 16.2 - An in-memory repository

The storage layer behind a REST API, without any web code.

Run:  python ex_02_todo_repo.py
"""

from __future__ import annotations


class NotFoundError(KeyError):
    """Raised when a todo id does not exist."""


class TodoRepo:
    """Stores todos as ``{"id", "title", "done"}`` dicts."""

    def __init__(self) -> None:
        self._items: dict[int, dict[str, object]] = {}
        self._next_id = 1

    def add(self, title: str) -> dict[str, object]:
        """Create a todo (done=False) with the next id and return it."""
        # TODO: build the dict, store it under self._next_id, then increment.
        # --- solution ---
        item: dict[str, object] = {"id": self._next_id, "title": title, "done": False}
        self._items[self._next_id] = item
        self._next_id += 1
        return item
        # --- end ---

    def list(self, done: bool | None = None) -> list[dict[str, object]]:
        """All todos in id order; filter by ``done`` when it is not None."""
        # TODO: sort by id and filter.
        # --- solution ---
        items = [self._items[key] for key in sorted(self._items)]
        return items if done is None else [i for i in items if i["done"] is done]
        # --- end ---

    def complete(self, todo_id: int) -> dict[str, object]:
        """Mark done and return it; raise NotFoundError for unknown ids."""
        # TODO: look the id up (raise NotFoundError) and set done=True.
        # --- solution ---
        if todo_id not in self._items:
            raise NotFoundError(todo_id)
        self._items[todo_id]["done"] = True
        return self._items[todo_id]
        # --- end ---

    def delete(self, todo_id: int) -> None:
        """Remove the todo; raise NotFoundError for unknown ids."""
        # TODO: delete or raise.
        # --- solution ---
        if todo_id not in self._items:
            raise NotFoundError(todo_id)
        del self._items[todo_id]
        # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    repo = TodoRepo()
    first, second = repo.add("a"), repo.add("b")
    assert (first["id"], second["id"]) == (1, 2) and first["done"] is False
    repo.complete(1)
    assert [t["id"] for t in repo.list(done=True)] == [1]
    assert [t["id"] for t in repo.list(done=False)] == [2]
    assert len(repo.list()) == 2
    repo.delete(2)
    assert [t["id"] for t in repo.list()] == [1]
    assert repo.add("c")["id"] == 3, "ids must never be reused"
    for action in (lambda: repo.complete(99), lambda: repo.delete(99)):
        try:
            action()
        except NotFoundError:
            pass
        else:
            raise AssertionError("unknown id must raise NotFoundError")


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_02_todo_repo: {exc!r}")
    print("PASS ex_02_todo_repo")
