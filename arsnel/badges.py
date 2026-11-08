"""Ranks and achievement badges, defined in Python and rendered as ASCII."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from arsnel.pixelfont import glyph

# (minimum percent complete, rank title)
RANKS: tuple[tuple[float, str], ...] = (
    (0.0, "NOOB"),
    (10.0, "SCRIPT KIDDIE"),
    (25.0, "CODER"),
    (45.0, "HACKER"),
    (65.0, "ENGINEER"),
    (85.0, "ARCHITECT"),
    (100.0, "ARSNEL MASTER"),
)


def rank_for(percent: float) -> tuple[int, str]:
    """Return ``(level_number, title)`` for a completion percentage."""
    level, title = 1, RANKS[0][1]
    for index, (threshold, name) in enumerate(RANKS, start=1):
        if percent >= threshold:
            level, title = index, name
    return level, title


@dataclass(frozen=True)
class Stats:
    """Facts about a learner that badge rules look at."""

    percent: float = 0.0
    exercises_done: int = 0
    quizzes_passed: int = 0
    modules_done: frozenset[int] = frozenset()
    total_quizzes: int = 19
    all_done: bool = False


@dataclass(frozen=True)
class Badge:
    """An achievement: id, name, description, glyph, tier and unlock rule."""

    key: str
    name: str
    description: str
    symbol: str
    tier: str  # bronze | silver | gold
    rule: Callable[[Stats], bool]

    def unlocked(self, stats: Stats) -> bool:
        """Return ``True`` when ``stats`` satisfies this badge's rule."""
        return self.rule(stats)


def _module(number: int) -> Callable[[Stats], bool]:
    return lambda s: number in s.modules_done


BADGES: tuple[Badge, ...] = (
    Badge(
        "first_blood",
        "FIRST BLOOD",
        "Pass your first exercise",
        "1",
        "bronze",
        lambda s: s.exercises_done >= 1,
    ),
    Badge(
        "quiz_rookie",
        "QUIZ ROOKIE",
        "Pass your first quiz",
        "Q",
        "bronze",
        lambda s: s.quizzes_passed >= 1,
    ),
    Badge("hello_world", "HELLO WORLD", "Finish module 01", "H", "bronze", _module(1)),
    Badge("loop_lord", "LOOP LORD", "Finish module 02", "L", "bronze", _module(2)),
    Badge(
        "ten_down",
        "TEN DOWN",
        "Pass 10 exercises",
        "X",
        "silver",
        lambda s: s.exercises_done >= 10,
    ),
    Badge(
        "halfway", "HALFWAY", "Reach 50% XP", "%", "silver", lambda s: s.percent >= 50
    ),
    Badge(
        "snake_charmer", "SNAKE CHARMER", "Finish module 08", "S", "silver", _module(8)
    ),
    Badge("async_ace", "ASYNC ACE", "Finish module 11", "A", "silver", _module(11)),
    Badge("test_pilot", "TEST PILOT", "Finish module 12", "T", "silver", _module(12)),
    Badge("shipper", "SHIPPER", "Finish module 13", "P", "silver", _module(13)),
    Badge("speed_demon", "SPEED DEMON", "Finish module 14", "Z", "silver", _module(14)),
    Badge("data_wizard", "DATA WIZARD", "Finish module 15", "D", "gold", _module(15)),
    Badge("web_weaver", "WEB WEAVER", "Finish module 16", "W", "gold", _module(16)),
    Badge("capstone", "CAPSTONE", "Finish module 18", "C", "gold", _module(18)),
    Badge(
        "quiz_master",
        "QUIZ MASTER",
        "Pass every quiz",
        "!",
        "gold",
        lambda s: s.total_quizzes > 0 and s.quizzes_passed >= s.total_quizzes,
    ),
    Badge(
        "arsnel_master",
        "ARSNEL MASTER",
        "Complete 100% of ARSNEL",
        "*",
        "gold",
        lambda s: s.all_done,
    ),
)

_BORDER = {"bronze": "▒▒", "silver": "▓▓", "gold": "██"}


def badge_art(badge: Badge, unlocked: bool) -> list[str]:
    """Return the 9-line pixel-art badge (locked badges are shaded ``░``)."""
    border = _BORDER[badge.tier] if unlocked else "░░"
    fill = "██" if unlocked else "░░"
    rows = glyph(badge.symbol if unlocked else "?")
    lines = [border * 7]
    for y in range(-1, 8):
        inner = (
            "  " * 5  # blank padding row, as wide as a 5-column glyph
            if y in (-1, 7)
            else "".join(fill if c == "#" else "  " for c in rows[y])
        )
        lines.append(border + inner + border)
    lines.append(border * 7)
    return lines


def badge_grid(stats: Stats, per_row: int = 4) -> str:
    """Render every badge in a grid, with names underneath."""
    blocks: list[list[str]] = []
    for badge in BADGES:
        ok = badge.unlocked(stats)
        art = badge_art(badge, ok)
        label = badge.name if ok else "LOCKED"
        art.append(label.center(14)[:14])
        blocks.append(art)
    out: list[str] = []
    for start in range(0, len(blocks), per_row):
        row = blocks[start : start + per_row]
        for line in zip(*row, strict=True):
            out.append("  ".join(line).rstrip())
        out.append("")
    return "\n".join(out).rstrip()
