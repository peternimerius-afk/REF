from __future__ import annotations
from .models import ContentUnit
REQUIREMENT_TERMS=["shall","must","is required to","are required to","shall not","must not","supports","support","provide","provides","retain","retains","encrypt","encrypts","log","logs","authenticate","authenticates","authorize","authorizes","integrate","integrates"]
EVIDENCE_TERMS=["provide documentation","describe how","submit evidence","demonstrate","explain","include in the tender response","attach","documentation shall include"]
BACKGROUND_TERMS=["because","in order to","for example","the purpose of","currently","today","historically"]
QUESTION_STARTS=("what ","how ","describe ","can ","does ","please ")
def classify(unit: ContentUnit) -> tuple[str,float]:
    text=unit.text.strip(); lower=text.lower(); header=str(unit.source.location.get('header','')).lower()
    if any(h in header for h in ["requirement","krav","shall"]):
        return ("requirement",0.82 if any(t in lower for t in EVIDENCE_TERMS) else 0.95)
    if any(t in lower for t in EVIDENCE_TERMS): return "evidence",0.86
    if lower.startswith(QUESTION_STARTS): return "question",0.82
    if any(t in lower for t in REQUIREMENT_TERMS): return "requirement",0.88
    if any(t in lower for t in BACKGROUND_TERMS): return "background",0.70
    return "unknown",0.45
