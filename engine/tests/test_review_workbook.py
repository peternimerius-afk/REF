from pathlib import Path

from ref_engine.models import AnalysisReport, RequirementCandidate, SourceLocation
from ref_engine.review_workbook import write_review_workbook


def test_write_review_workbook(tmp_path: Path):
    report = AnalysisReport(
        input_file="test.xlsx",
        content_units=1,
        requirements_detected=1,
        requirements=[
            RequirementCandidate(
                id="REQ-001",
                text="The solution shall support REST APIs.",
                source=SourceLocation("test.xlsx", "xlsx", {"worksheet": "Sheet1", "row": 2, "column": 4}),
                confidence=0.9,
                reason="Detected obligation term: shall",
                lint=[],
            )
        ],
        lint_counts={},
    )

    output = tmp_path / "review.xlsx"
    write_review_workbook(report, output)

    assert output.exists()
    assert output.stat().st_size > 0
