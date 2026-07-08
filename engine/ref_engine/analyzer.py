from __future__ import annotations

from .detector import detect_requirements
from .importers import import_file
from .models import AnalysisReport


def analyze_file(input_path: str) -> AnalysisReport:
    units = import_file(input_path)
    requirements = detect_requirements(units)

    return AnalysisReport(
        input_file=input_path,
        content_units=len(units),
        requirements_detected=len(requirements),
        requirements=requirements,
    )
