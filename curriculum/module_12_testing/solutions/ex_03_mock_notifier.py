"""Exercise 12.3 - Dependency injection and mocks

Inject collaborators so they can be replaced by Mock objects.

Run:  python ex_03_mock_notifier.py
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
from unittest.mock import Mock


def greeting(clock: Callable[[], datetime]) -> str:
    """Morning before 12:00, afternoon before 18:00, otherwise evening."""
    # TODO: call clock() to get the time instead of datetime.now().
    # --- solution ---
    hour = clock().hour
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"
    # --- end ---


def alert_if_hot(sensor: Mock, notifier: Mock, limit: float = 30.0) -> bool:
    """Read ``sensor.read()``; if above ``limit`` call ``notifier.send(msg)``.

    Return True when an alert was sent.
    """
    # TODO: read once, compare, and send f"too hot: {temp}" when above the limit.
    # --- solution ---
    temp = sensor.read()
    if temp > limit:
        notifier.send(f"too hot: {temp}")
        return True
    return False
    # --- end ---


def check() -> None:
    """Self-test: raises AssertionError when something is wrong."""
    assert greeting(lambda: datetime(2025, 1, 1, 9)) == "Good morning"
    assert greeting(lambda: datetime(2025, 1, 1, 12)) == "Good afternoon"
    assert greeting(lambda: datetime(2025, 1, 1, 23)) == "Good evening"
    sensor, notifier = Mock(), Mock()
    sensor.read.return_value = 35.5
    assert alert_if_hot(sensor, notifier) is True
    notifier.send.assert_called_once_with("too hot: 35.5")
    sensor.read.return_value = 20
    notifier.reset_mock()
    assert alert_if_hot(sensor, notifier) is False
    notifier.send.assert_not_called()


if __name__ == "__main__":
    import sys

    try:
        check()
    except (AssertionError, NotImplementedError) as exc:
        sys.exit(f"FAIL ex_03_mock_notifier: {exc!r}")
    print("PASS ex_03_mock_notifier")
