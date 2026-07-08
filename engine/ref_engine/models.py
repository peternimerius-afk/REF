from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class SourceLocation:
    document: str
    document_type: str
    location: dict[str, Any] = field(default_factory=dict)

@dataclass
class ContentUnit:
    id: str
    text: str
    source: SourceLocation
    kind: str = "unknown"

@dataclass
class LintFinding:
    code: str
    severity: str
    message: str
    recommendation: str | None = None

@dataclass
class CapabilityMatch:
    id: str
    name: str
    confidence: float
    matched_terms: list[str] = field(default_factory=list)

@dataclass
class RequirementObject:
    id: str
    source: SourceLocation
    original_text: str
    classification: str
    confidence: float
    lint: list[LintFinding] = field(default_factory=list)
    capabilities: list[CapabilityMatch] = field(default_factory=list)
    quality_score: int | None = None
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class AnalysisReport:
    input_file: str
    content_units: int
    requirements: list[RequirementObject]
    classification_counts: dict[str, int]
    lint_counts: dict[str, int]
    capability_counts: dict[str, int]
    average_quality_score: float | None = None
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
