from __future__ import annotations

import re

from .models import LintFinding


LINT_RULES: dict[str, dict[str, str]] = {
    "RFP001": {
        "title": "Multiple obligations",
        "severity": "Error",
        "description": "The text appears to contain more than one independent obligation.",
        "recommendation": "Split into separate atomic requirements.",
    },
    "RFP002": {
        "title": "Subjective wording",
        "severity": "Error",
        "description": "The text contains subjective or marketing-oriented wording.",
        "recommendation": "Replace subjective wording with measurable criteria.",
    },
    "RFP004": {
        "title": "Evidence embedded",
        "severity": "Warning",
        "description": "The requirement appears to include evidence or response instructions.",
        "recommendation": "Move evidence requests to a separate evidence field.",
    },
    "RFP008": {
        "title": "Excessive verbosity",
        "severity": "Warning",
        "description": "The requirement exceeds the configured word limit.",
        "recommendation": "Compress the wording while preserving the obligation.",
    },
}


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
    "describe the",
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
        findings.append(make_finding("RFP001"))

    subjective = [word for word in SUBJECTIVE_WORDS if word in lower]
    if subjective:
        findings.append(
            make_finding(
                "RFP002",
                detail="Detected terms: " + ", ".join(subjective),
            )
        )

    if any(pattern in lower for pattern in EVIDENCE_PATTERNS):
        findings.append(make_finding("RFP004"))

    word_count = len(re.findall(r"\b\w+\b", text))
    if word_count > max_words:
        findings.append(
            make_finding(
                "RFP008",
                detail=f"Detected {word_count} words. Configured limit is {max_words}.",
            )
        )

    return findings


def make_finding(code: str, detail: str | None = None) -> LintFinding:
    rule = LINT_RULES[code]
    message = f"{rule['title']}: {rule['description']}"
    if detail:
        message = f"{message} {detail}"

    return LintFinding(
        code=code,
        severity=rule["severity"],
        message=message,
        recommendation=rule["recommendation"],
    )


def lint_catalog() -> dict[str, dict[str, str]]:
    return LINT_RULES
