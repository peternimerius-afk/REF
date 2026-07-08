from __future__ import annotations

from collections import Counter

from .detector import detect_requirements
from .importers import import_file
from .linter import lint_requirement
from .models import AnalysisReport


def analyze_file(input_path: str) -> AnalysisReport:
    units = import_file(input_path)
    requirements = detect_requirements(units)

    lint_counter: Counter[str] = Counter()

    for requirement in requirements:
        requirement.lint = lint_requirement(requirement.text)
        for finding in requirement.lint:
            lint_counter[finding.code] += 1

    return AnalysisReport(
        input_file=input_path,
        content_units=len(units),
        requirements_detected=len(requirements),
        requirements=requirements,
        lint_counts=dict(lint_counter),
    )
