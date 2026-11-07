"""Exercise 11.1 - Thread pool and a safe counter

Use ThreadPoolExecutor and a Lock.

Run:  python ex_01_thread_pool.py
"""

from __future__ import annotations

import threading
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


def parallel_map(
    func: Callable[[int], int], items: list[int], workers: int = 4
) -> list[int]:
    """Apply ``func`` to every item with a thread pool; keep the input order."""
    # TODO: open a ThreadPoolExecutor and use pool.map.
    # --- solution ---
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(func, items))
    # --- end ---


class SafeCounter:
    """A counter that stays correct when many threads call ``increment``."""

    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        """Add one, atomically."""
        # TODO: do the += inside `with self._lock:`.
        # --- solution ---
        with self._lock:
            self.value += 1
        # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert parallel_map(lambda n: n * n, [1, 2, 3, 4]) == [1, 4, 9, 16]
    assert parallel_map(lambda n: n + 1, []) == []
    counter = SafeCounter()

    def hammer() -> None:
        for _ in range(2000):
            counter.increment()

    threads = [threading.Thread(target=hammer) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert counter.value == 16000, f"lost updates: {counter.value}"


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_01_thread_pool: {exc!r}")
    print("PASS ex_01_thread_pool")
