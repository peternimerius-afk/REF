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
