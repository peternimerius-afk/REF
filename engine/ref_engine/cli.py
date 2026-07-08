from __future__ import annotations

import argparse

from .analyzer import analyze_file
from .report import print_console_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="ref",
        description="REF Engine Alpha",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze a requirements document",
    )

    analyze_parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input file (.xlsx, .docx, .md, .txt)",
    )

    analyze_parser.add_argument(
        "--max-examples",
        type=int,
        default=20,
        help="Maximum detected requirement examples to print",
    )

    args = parser.parse_args(argv)

    if args.command == "analyze":
        report = analyze_file(args.input)
        print_console_report(report, max_examples=args.max_examples)
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
