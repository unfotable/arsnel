"""ASCII / block-character art: banner, mascot, XP bar and boxes."""

from __future__ import annotations

from arsnel.pixelfont import bitmap_to_blocks, text_bitmap

# Original pixel-snake mascot. Legend: # body, o eye, ~ tongue, . empty.
MASCOT: tuple[str, ...] = (
    ".....######.....",
    "...##########...",
    "..############..",
    "..##oo####oo##..",
    "..##oo####oo##..",
    "..############..",
    "...##########...",
    ".....##~~##.....",
    "......#~~#......",
    "..######.#####..",
    ".####..###..###.",
    "####..#####..###",
    "####.......#####",
    ".###############",
    "..#############.",
)

_MASCOT_BLOCKS = {"#": "██", "o": "  ", "~": "▒▒", ".": "  "}


def banner(text: str = "ARSNEL") -> str:
    """Return the large block-letter banner for ``text``."""
    return "\n".join(bitmap_to_blocks(text_bitmap(text)))


def mascot() -> str:
    """Return the snake mascot as block characters."""
    return "\n".join("".join(_MASCOT_BLOCKS[c] for c in row).rstrip() for row in MASCOT)


def box(lines: list[str], title: str = "") -> str:
    """Draw a single-line box around ``lines`` with an optional ``title``."""
    width = max([len(line) for line in lines] + [len(title) + 4])
    label = f"[ {title} ]" if title else ""
    top = "┌─" + label + "─" * (width + 1 - len(label)) + "┐"
    body = [f"│ {line.ljust(width)} │" for line in lines]
    return "\n".join([top, *body, "└" + "─" * (width + 2) + "┘"])


def xp_bar(percent: float, width: int = 32) -> str:
    """Return a block-character progress bar, e.g. ``[████░░░░] 50%``."""
    percent = max(0.0, min(100.0, percent))
    filled = round(width * percent / 100)
    return f"[{'█' * filled}{'░' * (width - filled)}] {percent:5.1f}%"


def hero() -> str:
    """Banner, tagline and prompt, ready to drop inside a ``text`` code fence."""
    return "\n".join(
        [
            banner(),
            "",
            "  > Learn Python. From `print()` to production. One pixel at a time.",
            "  $ python bootstrap.py █",
        ]
    )
