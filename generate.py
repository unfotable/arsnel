"""Generate module READMEs, exercise stubs and quiz runners.

Usage:
    python generate.py              # (re)write generated files
    python generate.py --check      # exit 1 if anything is out of date (CI)
    python generate.py --module 7   # only module 07
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from arsnel.paths import ROOT
from arsnel.scaffold import ScaffoldError, generate


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0] if __doc__ else ""
    )
    parser.add_argument("--check", action="store_true", help="only report drift")
    parser.add_argument("--module", type=int, help="limit to one module number")
    parser.add_argument(
        "--no-output", action="store_true", help="skip running examples"
    )
    args = parser.parse_args(argv)
    try:
        changed = generate(
            only=args.module, check=args.check, with_output=not args.no_output
        )
    except ScaffoldError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2
    verb = "out of date" if args.check else "written"
    for path in changed:
        print(f"{verb}: {path.relative_to(ROOT)}")
    print(
        f"[OK] {len(changed)} file(s) {verb}."
        if changed
        else "[OK] everything up to date."
    )
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
