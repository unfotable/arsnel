"""SVG pixel art built from rectangles: hero banner and XP bar.

No fonts are used: all lettering is drawn with the 5x7 bitmap font, so the
images look identical on GitHub, in the generated site and offline.
"""

from __future__ import annotations

from arsnel.ascii_art import MASCOT
from arsnel.pixelfont import GLYPH_H, text_bitmap, text_width

WHITE = "#ffffff"
BLACK = "#000000"
CARBON = "#232323"
TERMINAL = "#0b0b0b"
GREEN = "#39ff6a"
DIM = "#8a8a8a"
EMPTY = "#e6e6e6"
EDGE = "#bdbdbd"

_HEAD = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
    'width="{w}" height="{h}" shape-rendering="crispEdges" role="img" '
    'aria-label="{label}">'
)


def _rects(
    rows: list[str] | tuple[str, ...], x: int, y: int, scale: int, fill: str
) -> str:
    """Merge horizontal runs of ``#`` into ``<rect>`` elements."""
    out: list[str] = []
    for ry, row in enumerate(rows):
        cx = 0
        while cx < len(row):
            if row[cx] == "#":
                start = cx
                while cx < len(row) and row[cx] == "#":
                    cx += 1
                out.append(
                    f'<rect x="{x + start * scale}" y="{y + ry * scale}" '
                    f'width="{(cx - start) * scale}" height="{scale}" fill="{fill}"/>'
                )
            else:
                cx += 1
    return "".join(out)


def text_svg(text: str, x: int, y: int, scale: int, fill: str) -> str:
    """Draw ``text`` with the pixel font; ``(x, y)`` is the top-left corner."""
    return _rects(text_bitmap(text), x, y, scale, fill)


def mascot_svg(x: int, y: int, scale: int, body: str = GREEN) -> str:
    """Draw the snake mascot (eyes are cut-outs, tongue is white)."""
    body_rows = [row.replace("o", ".").replace("~", ".") for row in MASCOT]
    tongue_rows = ["".join("#" if c == "~" else "." for c in row) for row in MASCOT]
    return _rects(body_rows, x, y, scale, body) + _rects(
        tongue_rows, x, y, scale, WHITE
    )


def _grid_defs() -> str:
    return (
        '<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">'
        f'<path d="M24 0H0V24" fill="none" stroke="{CARBON}" stroke-opacity="0.12" '
        'stroke-width="1"/></pattern></defs>'
        f'<rect width="100%" height="100%" fill="{WHITE}"/>'
        '<rect width="100%" height="100%" fill="url(#grid)"/>'
    )


def banner_svg() -> str:
    """The README hero: a terminal window with the ARSNEL wordmark."""
    w, h = 960, 340
    parts = [
        _HEAD.format(w=w, h=h, label="ARSNEL - Learn Python, one pixel at a time"),
        _grid_defs(),
        # hard shadow
        f'<rect x="36" y="36" width="912" height="276" fill="{CARBON}"/>',
        f'<rect x="24" y="24" width="912" height="276" fill="{TERMINAL}" '
        f'stroke="{BLACK}" stroke-width="2"/>',
        f'<rect x="24" y="24" width="912" height="32" fill="{CARBON}"/>',
    ]
    for i in range(3):
        parts.append(
            f'<rect x="{40 + i * 22}" y="34" width="12" height="12" fill="{WHITE}"/>'
        )
    parts.append(text_svg("ARSNEL@PIXEL:~$ PYTHON", 128, 34, 2, DIM))
    parts.append(text_svg(">", 56, 84, 12, GREEN))
    parts.append(text_svg("ARSNEL", 136, 84, 12, GREEN))
    parts.append(
        text_svg("LEARN PYTHON. FROM PRINT() TO PRODUCTION.", 56, 208, 3, WHITE)
    )
    parts.append(text_svg("ONE PIXEL AT A TIME.", 56, 244, 3, GREEN))
    cursor_x = 56 + text_width("ONE PIXEL AT A TIME.") * 3 + 18
    parts.append(
        f'<rect x="{cursor_x}" y="244" width="15" height="{GLYPH_H * 3}" '
        f'fill="{GREEN}">'
        '<animate attributeName="opacity" values="1;1;0;0" dur="1s" '
        'repeatCount="indefinite"/></rect>'
    )
    parts.append(mascot_svg(768, 76, 8))
    parts.append("</svg>")
    return "".join(parts)


def xp_bar_svg(percent: float, xp: int, max_xp: int, level: int, rank: str) -> str:
    """A pixel-art XP bar with level, rank, percentage and totals."""
    w, h = 960, 140
    cells, cell_w = 48, 17
    pct = max(0.0, min(100.0, percent))
    filled = round(cells * pct / 100)
    total = f"{xp}/{max_xp} XP"
    parts = [
        _HEAD.format(w=w, h=h, label=f"XP {pct:.0f} percent, level {level} {rank}"),
        _grid_defs(),
        f'<rect x="30" y="30" width="900" height="96" fill="{CARBON}"/>',
        f'<rect x="24" y="24" width="900" height="96" fill="{WHITE}" '
        f'stroke="{BLACK}" stroke-width="2"/>',
        text_svg(f"LVL {level} {rank}", 40, 38, 3, BLACK),
        text_svg(total, 908 - text_width(total) * 3, 38, 3, BLACK),
    ]
    for i in range(cells):
        x = 40 + i * (cell_w + 1)
        on = i < filled
        parts.append(
            f'<rect x="{x}" y="74" width="{cell_w}" height="30" '
            f'fill="{GREEN if on else EMPTY}" '
            f'stroke="{BLACK if on else EDGE}" stroke-width="1"/>'
        )
    parts.append("</svg>")
    return "".join(parts)
