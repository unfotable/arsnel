"""Custom exceptions, ``raise ... from`` and EAFP vs LBYL."""

import json
import tempfile
from pathlib import Path


class AppError(Exception):
    """Base class for every error this application raises on purpose."""


class ConfigError(AppError):
    """The configuration file is missing or invalid."""

    def __init__(self, message: str, *, key: str | None = None) -> None:
        super().__init__(message)
        self.key = key  # extra context that handlers can use


def load_port(raw: str) -> int:
    """Parse the ``port`` field, translating low-level errors into ours."""
    try:
        data = json.loads(raw)
        return int(data["port"])
    except json.JSONDecodeError as exc:
        raise ConfigError("not valid JSON") from exc  # explicit cause
    except KeyError as exc:
        raise ConfigError("missing key", key="port") from exc
    except (TypeError, ValueError) as exc:
        raise ConfigError("port must be a number", key="port") from exc


for raw in ['{"port": "8080"}', "{oops", '{"host": "x"}', '{"port": "abc"}']:
    try:
        print("port =", load_port(raw))
    except AppError as exc:  # one handler for the whole family
        cause = type(exc.__cause__).__name__
        print(f"ConfigError: {exc} (key={getattr(exc, 'key', None)}, cause={cause})")

# --- EAFP vs LBYL ------------------------------------------------------------
# LBYL = Look Before You Leap: check first. Racy for files (it can change
# between the check and the use) and often longer.
# EAFP = Easier to Ask Forgiveness than Permission: try it, handle failure.
settings = {"colour": "blue"}

if "size" in settings:  # LBYL  # noqa: SIM108, SIM401
    size = settings["size"]
else:
    size = "medium"

try:  # EAFP
    size = settings["size"]
except KeyError:
    size = "medium"
print("size:", size, "| dict.get does it in one line:", settings.get("size", "medium"))

with tempfile.TemporaryDirectory() as tmp:
    missing = Path(tmp) / "nope.txt"
    try:
        missing.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("EAFP: no such file, using defaults")
