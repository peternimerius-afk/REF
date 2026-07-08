from __future__ import annotations

import re

from .models import LintFinding


SUBJECTIVE_WORDS = [
    "robust",
    "modern",
    "flexible",
    "user-friendly",
    "intuitive",
    "seamless",
    "future-proof",
    "comprehensive",
    "adequate",
    "sufficient",
    "efficient",
    "state-of-the-art",
    "best practice",
    "excellent",
]

EVIDENCE_PATTERNS = [
    "describe how",
    "provide documentation",
    "submit evidence",
    "demonstrate",
    "explain",
    "include in the tender response",
    "attach",
    "provide the",
]

OBLIGATION_TERMS = [
    " shall ",
    " must ",
    " shall not ",
    " must not ",
    " is required to ",
]


def lint_requirement(text: str, max_words: int = 45) -> list[LintFinding]:
    lower = f" {text.lower()} "
    findings: list[LintFinding] = []

    obligation_count = sum(lower.count(term) for term in OBLIGATION_TERMS)
    if obligation_count > 1:
        findings.append(
            LintFinding(
                code="RFP001",
                severity="Error",
                message="Multiple obligations detected.",
                recommendation="Split into atomic requirements.",
            )
        )

    subjective = [word for word in SUBJECTIVE_WORDS if word in lower]
    if subjective:
        findings.append(
            LintFinding(
                code="RFP002",
                severity="Error",
                message="Subjective wording detected: " + ", ".join(subjective),
                recommendation="Replace subjective wording with measurable criteria.",
            )
        )

    if any(pattern in lower for pattern in EVIDENCE_PATTERNS):
        findings.append(
            LintFinding(
                code="RFP004",
                severity="Warning",
                message="Evidence request appears embedded in requirement.",
                recommendation="Move evidence to the evidence field.",
            )
        )

    word_count = len(re.findall(r"\b\w+\b", text))
    if word_count > max_words:
        findings.append(
            LintFinding(
                code="RFP008",
                severity="Warning",
                message=f"Requirement has {word_count} words, exceeding limit {max_words}.",
                recommendation="Compress requirement while preserving obligation.",
            )
        )

    return findings
