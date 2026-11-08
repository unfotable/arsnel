"""Bitmap font, ASCII art and SVG pixel art."""

from __future__ import annotations

import xml.etree.ElementTree as ET

from arsnel import ascii_art
from arsnel.badges import BADGES, badge_grid
from arsnel.pixelart import banner_svg, xp_bar_svg
from arsnel.pixelfont import GLYPH_H, glyph, text_bitmap, text_width
from arsnel.progress_core import Snapshot


def test_glyph_dimensions() -> None:
    for char in "ARSNEL0123456789 >_":
        rows = glyph(char)
        assert len(rows) == GLYPH_H == 7
        assert {len(r) for r in rows} == {5}


def test_text_bitmap_width_matches() -> None:
    rows = text_bitmap("ARSNEL")
    assert len(rows) == 7
    assert {len(r) for r in rows} == {text_width("ARSNEL")}


def test_banner_contains_blocks() -> None:
    art = ascii_art.banner()
    assert "██" in art
    assert len(art.splitlines()) == 7


def test_xp_bar_fill() -> None:
    assert ascii_art.xp_bar(0, 10).count("█") == 0
    assert ascii_art.xp_bar(100, 10).count("█") == 10
    assert "50" in ascii_art.xp_bar(50, 10)


def test_box_is_rectangular() -> None:
    lines = ascii_art.box(["hello", "ARSNEL"], title="> t").splitlines()
    assert len({len(line) for line in lines}) == 1


def test_svgs_are_valid_xml() -> None:
    banner = ET.fromstring(banner_svg())
    assert banner.tag.endswith("svg")
    bar = ET.fromstring(xp_bar_svg(42.0, 100, 238, 3, "HACKER"))
    assert bar.attrib["aria-label"].startswith("XP 42")
    # no rounded corners anywhere in the pixel art
    assert "rx=" not in banner_svg() + xp_bar_svg(10, 1, 10, 1, "NOOB")


def test_badge_grid_locked_state() -> None:
    grid = badge_grid(Snapshot(timestamp="t").stats())
    assert grid.count("LOCKED") == len(BADGES)


def test_every_badge_is_a_clean_rectangle() -> None:
    """Locked and unlocked badges must have equal-width rows (README alignment)."""
    from arsnel.badges import badge_art

    for badge in BADGES:
        for unlocked in (False, True):
            lines = badge_art(badge, unlocked)
            assert len({len(line) for line in lines}) == 1, (badge.name, unlocked)
            assert len(lines) == 11


def test_badge_grid_rows_align() -> None:
    from arsnel.progress_core import ModuleProgress

    snap = Snapshot(timestamp="t")
    snap.modules = [ModuleProgress(n, 3, 3, 100.0, True) for n in range(19)]
    for stats in (Snapshot(timestamp="t").stats(), snap.stats()):
        for block in badge_grid(stats).split("\n\n"):
            art_rows = block.splitlines()[:-1]  # the last line holds the labels
            assert {len(row) for row in art_rows} == {62}
