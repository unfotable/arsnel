"""Command-line arguments: ``sys.argv`` by hand, then ``argparse`` properly.

``argparse.parse_args()`` normally reads ``sys.argv``; passing an explicit list
lets us demonstrate it (and test it) without a real terminal.
"""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="greet", description="Greet someone.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("-n", "--times", type=int, default=1, help="repeat")
    parser.add_argument("-v", "--verbose", action="store_true", help="show details")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the tool; ``argv=None`` means "use sys.argv[1:]"."""
    args = build_parser().parse_args(argv)
    for _ in range(args.times):
        print(f"Hello, {args.name}!")
    if args.verbose:
        print(f"(parsed: {vars(args)})")
    return 0


if __name__ == "__main__":
    # sys.argv[0] is the script name; the rest are the arguments you typed.
    print("sys.argv[1:] when run bare:", sys.argv[1:])

    main(["Ada"])
    main(["Ada", "--times", "2", "-v"])

    try:
        main(["Ada", "--times", "lots"])  # not a number: argparse exits
    except SystemExit as exc:
        print(f"argparse rejected bad input with exit code {exc.code}")

    build_parser().print_usage()
