from ref_engine.linter import lint_requirement


def test_detects_multiple_obligations():
    findings = lint_requirement(
        "The solution shall support REST APIs. The solution shall provide OpenAPI documentation."
    )
    assert "RFP001" in {finding.code for finding in findings}


def test_detects_embedded_evidence():
    findings = lint_requirement(
        "The solution shall support audit logging. Describe how this is implemented."
    )
    assert "RFP004" in {finding.code for finding in findings}
