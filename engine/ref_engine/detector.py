from __future__ import annotations

import re

from .models import ContentUnit, RequirementCandidate


OBLIGATION_TERMS = [
    " shall ",
    " must ",
    " shall not ",
    " must not ",
    " is required to ",
    " are required to ",
]

REQUIREMENT_HEADERS = [
    "requirement",
    "requirements",
    "rfp requirement",
    "krav",
]

SECTION_HEADING_PATTERN = re.compile(r"^[A-ZÅÄÖ]\.?\s+")
NUMERIC_ID_PATTERN = re.compile(r"^\d+[A-Za-z]?$")


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
    header = str(unit.source.location.get("header", "")).lower().strip()

    if _is_noise_cell(text):
        return None

    for term in OBLIGATION_TERMS:
        if term in lower:
            return RequirementCandidate(
                id=f"REQ-{unit.id}",
                text=text,
                source=unit.source,
                confidence=0.90,
                reason=f"Detected obligation term: {term.strip()}",
            )

    # Header-based detection is deliberately conservative.
    # It shall not treat a workbook title such as
    # "RFP - AI Requirements..." as proof that every cell in the column is a requirement.
    if _looks_like_requirement_column(header) and _looks_like_requirement_text(text):
        return RequirementCandidate(
            id=f"REQ-{unit.id}",
            text=text,
            source=unit.source,
            confidence=0.82,
            reason="Requirement-like column header and requirement-like text",
        )

    return None


def _looks_like_requirement_column(header: str) -> bool:
    if not header:
        return False

    # Avoid treating long workbook titles as column headers.
    if len(header.split()) > 6:
        return False

    return any(term == header or term in header for term in REQUIREMENT_HEADERS)


def _looks_like_requirement_text(text: str) -> bool:
    lower = text.lower()
    if len(text.split()) < 5:
        return False

    weak_terms = [
        "support",
        "provide",
        "retain",
        "encrypt",
        "log",
        "authenticate",
        "authorize",
        "integrate",
        "comply",
    ]
    return any(term in lower for term in weak_terms)


def _is_noise_cell(text: str) -> bool:
    stripped = text.strip()

    if not stripped:
        return True

    if NUMERIC_ID_PATTERN.match(stripped):
        return True

    if stripped.lower() in {"id", "no", "nr", "requirement", "requirements"}:
        return True

    # Section headings such as "A. DATA PROTECTION, PRIVACY & SECURITY"
    if len(stripped.split()) <= 8 and stripped.upper() == stripped and any(c.isalpha() for c in stripped):
        return True

    if SECTION_HEADING_PATTERN.match(stripped) and stripped.upper() == stripped:
        return True

    return False
