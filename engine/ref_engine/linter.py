from __future__ import annotations
import re
from .models import LintFinding
SUBJECTIVE_WORDS=["robust","modern","flexible","user-friendly","intuitive","seamless","future-proof","comprehensive","adequate","sufficient","efficient","state-of-the-art","best practice","excellent"]
EVIDENCE_PATTERNS=["describe how","provide documentation","submit evidence","demonstrate","explain","include in the tender response","attach"]
OBLIGATION_TERMS=[" shall "," must "," shall not "," must not "," is required to "]
def lint_requirement(text: str, max_words: int=20) -> list[LintFinding]:
    lower=f" {text.lower()} "; findings=[]
    obligation_count=sum(lower.count(term) for term in OBLIGATION_TERMS)
    conjunction_signal=len(re.findall(r"(and|or|including)", lower))>=2
    if obligation_count>1 or conjunction_signal:
        findings.append(LintFinding("RFP001","Error","Multiple obligations detected.","Split into atomic requirements."))
    found=[w for w in SUBJECTIVE_WORDS if w in lower]
    if found:
        findings.append(LintFinding("RFP002","Error",f"Subjective wording detected: {', '.join(found)}.","Replace subjective wording with measurable criteria."))
    if any(p in lower for p in EVIDENCE_PATTERNS):
        findings.append(LintFinding("RFP004","Warning","Evidence request appears embedded in requirement.","Move evidence to the evidence field."))
    wc=len(re.findall(r"\w+", text))
    if wc>max_words:
        findings.append(LintFinding("RFP008","Warning",f"Requirement has {wc} words, exceeding limit {max_words}.","Compress requirement while preserving obligation."))
    if not any(t in lower for t in ["shall","must","support","provide","retain","encrypt","log"]):
        findings.append(LintFinding("RFP003","Error","Requirement may not be objectively evaluable.","Rewrite with objective compliance criteria."))
    return findings

def quality_score(findings: list[LintFinding]) -> int:
    score=100
    penalties={"Error":25,"Warning":10,"Notice":5,"Info":0}
    for f in findings: score-=penalties.get(f.severity,10)
    return max(0,score)
