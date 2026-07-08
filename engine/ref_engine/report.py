from __future__ import annotations

from .models import AnalysisReport


def print_console_report(report: AnalysisReport, max_examples: int = 20) -> None:
    print("=" * 60)
    print("REF ENGINE REPORT")
    print("=" * 60)
    print(f"Input file:            {report.input_file}")
    print(f"Content units:         {report.content_units}")
    print(f"Requirements detected: {report.requirements_detected}")

    print()
    print("Lint findings")
    print("-" * 60)

    if report.lint_counts:
        for code, count in sorted(report.lint_counts.items()):
            print(f"{code:<8} {count}")
    else:
        print("None")

    print()
    print("Examples")
    print("-" * 60)

    for requirement in report.requirements[:max_examples]:
        location = requirement.source.location
        lint_codes = ", ".join(finding.code for finding in requirement.lint) or "none"

        print(f"{requirement.id}")
        print(f"Confidence: {requirement.confidence}")
        print(f"Reason:     {requirement.reason}")
        print(f"Lint:       {lint_codes}")
        print(f"Location:   {location}")
        print(requirement.text[:700])
        print("-" * 60)
