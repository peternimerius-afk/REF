from ref_engine.detector import detect_requirements
from ref_engine.models import ContentUnit, SourceLocation


def test_detects_shall_requirement():
    unit = ContentUnit(
        id="T1",
        text="The solution shall support SAML 2.0.",
        source=SourceLocation("test.txt", "txt", {"line": 1}),
        kind="line",
    )

    result = detect_requirements([unit])

    assert len(result) == 1
    assert result[0].confidence >= 0.9


def test_ignores_numeric_id_cell():
    unit = ContentUnit(
        id="T1",
        text="1",
        source=SourceLocation(
            "test.xlsx",
            "xlsx",
            {"row": 4, "column": 1, "header": "RFP - AI Requirements"},
        ),
        kind="cell",
    )

    result = detect_requirements([unit])

    assert len(result) == 0


def test_ignores_section_heading_cell():
    unit = ContentUnit(
        id="T1",
        text="A. DATA PROTECTION, PRIVACY & SECURITY",
        source=SourceLocation(
            "test.xlsx",
            "xlsx",
            {"row": 3, "column": 1, "header": "RFP - AI Requirements"},
        ),
        kind="cell",
    )

    result = detect_requirements([unit])

    assert len(result) == 0
