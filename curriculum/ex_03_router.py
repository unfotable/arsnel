"""Exercise 18.3 - A tiny API router

The core of a web framework: map method + path to handlers.

Run:  python ex_03_router.py
"""

from __future__ import annotations

from collections.abc import Callable

Handler = Callable[..., tuple[int, object]]


class Router:
    """Dispatch (method, path) to handlers; ``{name}`` segments capture parameters."""

    def __init__(self) -> None:
        self._routes: list[tuple[str, list[str], Handler]] = []

    def register(self, method: str, pattern: str, handler: Handler) -> None:
        """Remember a route such as ("GET", "/books/{book_id}")."""
        # TODO: split the pattern on "/" and store it with the upper-cased method.
        raise NotImplementedError("TODO: your turn")

    def dispatch(self, method: str, path: str) -> tuple[int, object]:
        """Call the matching handler with captured params as keyword arguments.

        Return (404, {"detail": "not found"}) when nothing matches and
        (405, {"detail": "method not allowed"}) when the path exists for other methods.
        """
        # TODO: compare segment by segment; "{x}" segments capture the text.
        raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    router = Router()
    router.register("GET", "/books", lambda: (200, ["a", "b"]))
    router.register("get", "/books/{book_id}", lambda book_id: (200, {"id": book_id}))
    router.register("POST", "/books", lambda: (201, {"created": True}))
    assert router.dispatch("GET", "/books") == (200, ["a", "b"])
    assert router.dispatch("GET", "/books/42/") == (200, {"id": "42"})
    assert router.dispatch("POST", "/books") == (201, {"created": True})
    assert router.dispatch("DELETE", "/books") == (
        405,
        {"detail": "method not allowed"},
    )
    assert router.dispatch("GET", "/nope") == (404, {"detail": "not found"})
    assert router.dispatch("GET", "/books/1/extra") == (404, {"detail": "not found"})


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_router: {exc!r}")
    print("PASS ex_03_router")
