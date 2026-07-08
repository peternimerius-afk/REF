from pathlib import Path

from ref_engine.models import AnalysisReport, RequirementCandidate, SourceLocation, LintFinding
from ref_engine.report import write_excel_report


def test_write_excel_report(tmp_path: Path):
    report = AnalysisReport(
        input_file="test.xlsx",
        content_units=1,
        requirements_detected=1,
        lint_counts={"RFP001": 1},
        requirements=[
            RequirementCandidate(
                id="REQ-001",
                text="The solution shall support REST APIs. The solution shall provide documentation.",
                source=SourceLocation("test.xlsx", "xlsx", {"worksheet": "Sheet1", "row": 2, "column": 4}),
                confidence=0.9,
                reason="Detected obligation term: shall",
                lint=[
                    LintFinding(
                        code="RFP001",
                        severity="Error",
                        message="Multiple obligations detected.",
                        recommendation="Split into atomic requirements.",
                    )
                ],
            )
        ],
    )

    output = tmp_path / "report.xlsx"
    write_excel_report(report, output)

    assert output.exists()
    assert output.stat().st_size > 0
