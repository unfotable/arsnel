"""Learner-facing curriculum content, kept as plain Python data."""

from __future__ import annotations

import importlib

from arsnel.manifest import MODULES
from arsnel.models import ModuleContent


def load(number: int) -> ModuleContent | None:
    """Return the :class:`ModuleContent` for module ``number`` (``None`` if absent)."""
    try:
        module = importlib.import_module(f"content.module_{number:02d}")
    except ModuleNotFoundError as exc:
        if exc.name == f"content.module_{number:02d}":
            return None
        raise
    content: ModuleContent = module.CONTENT
    return content


def all_content() -> dict[int, ModuleContent]:
    """Load every module that has content."""
    found: dict[int, ModuleContent] = {}
    for meta in MODULES:
        content = load(meta.number)
        if content is not None:
            found[meta.number] = content
    return found
