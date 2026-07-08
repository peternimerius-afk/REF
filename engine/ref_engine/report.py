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
    print("Examples")
    print("-" * 60)

    for requirement in report.requirements[:max_examples]:
        location = requirement.source.location
        print(f"{requirement.id}")
        print(f"Confidence: {requirement.confidence}")
        print(f"Reason:     {requirement.reason}")
        print(f"Location:   {location}")
        print(requirement.text[:500])
        print("-" * 60)
