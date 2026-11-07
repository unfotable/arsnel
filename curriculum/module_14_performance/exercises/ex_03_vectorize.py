"""Exercise 14.3 - Vectorise with numpy

Replace Python loops by array operations.

Run:  python ex_03_vectorize.py
"""

# requires: numpy

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def normalize(values: NDArray[np.float64]) -> NDArray[np.float64]:
    """Scale to mean 0 and standard deviation 1 (no loops)."""
    # TODO: (values - values.mean()) / values.std()
    raise NotImplementedError("TODO: your turn")


def count_above_mean(values: NDArray[np.float64]) -> int:
    """How many values are strictly above the mean? Use a boolean mask."""
    # TODO: sum a boolean mask.
    raise NotImplementedError("TODO: your turn")


def moving_average(values: NDArray[np.float64], window: int) -> NDArray[np.float64]:
    """Simple moving average with 'valid' windows."""
    # TODO: np.convolve(values, np.ones(window) / window, mode="valid")
    raise NotImplementedError("TODO: your turn")


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    data = np.array([1.0, 2.0, 3.0, 4.0, 10.0])
    z = normalize(data)
    assert abs(z.mean()) < 1e-9 and abs(z.std() - 1) < 1e-9
    assert count_above_mean(data) == 1
    assert np.allclose(moving_average(data, 2), [1.5, 2.5, 3.5, 7.0])


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_vectorize: {exc!r}")
    print("PASS ex_03_vectorize")
