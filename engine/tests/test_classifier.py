from ref_engine.classifier import classify
from ref_engine.models import ContentUnit, SourceLocation

def unit(text): return ContentUnit('T1', text, SourceLocation('test.txt','txt',{}))

def test_requirement_classification():
    cls, confidence=classify(unit('The solution shall support SAML 2.0.'))
    assert cls=='requirement'; assert confidence>=0.7

def test_evidence_classification():
    cls, confidence=classify(unit('The supplier shall describe how backup is performed.'))
    assert cls=='evidence'; assert confidence>=0.7
