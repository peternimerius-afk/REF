from __future__ import annotations

from .models import ContentUnit, RequirementCandidate


OBLIGATION_TERMS = [
    " shall ",
    " must ",
    " shall not ",
    " must not ",
    " is required to ",
    " are required to ",
]

HEADER_TERMS = [
    "requirement",
    "krav",
    "shall",
    "must",
    "rfp requirement",
]


def detect_requirements(units: list[ContentUnit]) -> list[RequirementCandidate]:
    candidates: list[RequirementCandidate] = []

    for unit in units:
        result = detect_requirement(unit)
        if result is not None:
            candidates.append(result)

    return candidates


def detect_requirement(unit: ContentUnit) -> RequirementCandidate | None:
    text = unit.text.strip()
    lower = f" {text.lower()} "
    header = str(unit.source.location.get("header", "")).lower()

    if any(term in header for term in HEADER_TERMS):
        return RequirementCandidate(
            id=f"REQ-{unit.id}",
            text=text,
            source=unit.source,
            confidence=0.95,
            reason="Requirement-like column header",
        )

    for term in OBLIGATION_TERMS:
        if term in lower:
            return RequirementCandidate(
                id=f"REQ-{unit.id}",
                text=text,
                source=unit.source,
                confidence=0.90,
                reason=f"Detected obligation term: {term.strip()}",
            )

    return None
