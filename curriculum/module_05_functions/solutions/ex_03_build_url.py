"""Exercise 05.3 - Flexible function signatures

Combine *args, **kwargs and keyword-only parameters.

Run:  python ex_03_build_url.py
"""

from __future__ import annotations


def build_url(base: str, *parts: str, secure: bool = True, **params: object) -> str:
    """Build ``scheme://base/part1/part2?k=v`` with query keys sorted.

    ``secure`` picks ``https`` over ``http``. Extra keyword arguments become the
    query string (sorted by key); no ``?`` when there are none.
    """
    # TODO: join the parts with "/", add the scheme and the sorted query string.
    # --- solution ---
    scheme = "https" if secure else "http"
    path = "/".join([base.strip("/"), *(p.strip("/") for p in parts)])
    url = f"{scheme}://{path}"
    if params:
        query = "&".join(f"{key}={params[key]}" for key in sorted(params))
        url += f"?{query}"
    return url
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert build_url("example.com") == "https://example.com"
    assert build_url("example.com", "a", "b") == "https://example.com/a/b"
    assert build_url("example.com/", "/x/", secure=False) == "http://example.com/x"
    assert build_url("h.io", "s", q="py", page=2) == "https://h.io/s?page=2&q=py"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_build_url: {exc!r}")
    print("PASS ex_03_build_url")
