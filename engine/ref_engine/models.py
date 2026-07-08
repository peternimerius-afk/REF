from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class SourceLocation:
    document: str
    document_type: str
    location: dict[str, Any]


@dataclass
class ContentUnit:
    id: str
    text: str
    source: SourceLocation
    kind: str


@dataclass
class RequirementCandidate:
    id: str
    text: str
    source: SourceLocation
    confidence: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AnalysisReport:
    input_file: str
    content_units: int
    requirements_detected: int
    requirements: list[RequirementCandidate]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
