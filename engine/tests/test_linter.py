from ref_engine.linter import lint_requirement

def test_subjective_wording_detected():
    codes={f.code for f in lint_requirement('The solution shall provide robust monitoring.')}
    assert 'RFP002' in codes

def test_embedded_evidence_detected():
    codes={f.code for f in lint_requirement('The supplier shall provide documentation showing audit logging is supported.')}
    assert 'RFP004' in codes
