from __future__ import annotations
from collections import Counter
from pathlib import Path
from .models import AnalysisReport, RequirementObject
from .importers import import_file
from .classifier import classify
from .linter import lint_requirement, quality_score
from .loader import find_repo_root, load_capabilities
from .mapper import map_capabilities

def analyze_file(input_path: str, project_path: str | None=None, repo_root: str | None=None) -> AnalysisReport:
    root=Path(repo_root) if repo_root else find_repo_root(Path.cwd())
    capabilities=load_capabilities(root)
    units=import_file(input_path)
    classification_counts=Counter(); lint_counts=Counter(); capability_counts=Counter(); requirements=[]; req_counter=1
    for unit in units:
        classification, confidence=classify(unit); classification_counts[classification]+=1
        if classification!='requirement' or confidence<0.70: continue
        findings=lint_requirement(unit.text)
        for f in findings: lint_counts[f.code]+=1
        matches=map_capabilities(unit.text, capabilities)
        for m in matches: capability_counts[m.id]+=1
        requirements.append(RequirementObject(f"REQ-{req_counter:04d}", unit.source, unit.text, classification, confidence, findings, matches, quality_score(findings)))
        req_counter+=1
    avg=None
    if requirements: avg=round(sum(r.quality_score or 0 for r in requirements)/len(requirements),1)
    return AnalysisReport(str(input_path), len(units), requirements, dict(classification_counts), dict(lint_counts), dict(capability_counts), avg)
