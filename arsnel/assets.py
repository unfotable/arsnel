"""Write the generated SVG assets (hero banner and XP bar)."""

from __future__ import annotations

from pathlib import Path

from arsnel.paths import ASSETS
from arsnel.pixelart import banner_svg, xp_bar_svg
from arsnel.progress_core import Snapshot


def write_assets(snapshot: Snapshot, out_dir: Path = ASSETS) -> list[Path]:
    """Write ``banner.svg`` and ``xp_bar.svg`` into ``out_dir``."""
    out_dir.mkdir(parents=True, exist_ok=True)
    level, rank = snapshot.level
    files = {
        "banner.svg": banner_svg(),
        "xp_bar.svg": xp_bar_svg(
            snapshot.percent, snapshot.xp, snapshot.max_xp, level, rank
        ),
    }
    written = []
    for name, text in files.items():
        path = out_dir / name
        path.write_text(text, encoding="utf-8")
        written.append(path)
    return written
