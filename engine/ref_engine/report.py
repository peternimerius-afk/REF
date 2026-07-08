from __future__ import annotations
import json
from pathlib import Path
from .models import AnalysisReport

def print_console_report(report: AnalysisReport, max_examples: int=10) -> None:
    print('='*60); print('REF ENGINE REPORT'); print('='*60)
    print(f"Input file:            {report.input_file}")
    print(f"Content units:         {report.content_units}")
    print(f"Requirements detected: {len(report.requirements)}")
    if report.average_quality_score is not None: print(f"Average quality score: {report.average_quality_score}/100")
    print('
Classification')
    for k,v in sorted(report.classification_counts.items()): print(f"  {k:<15} {v}")
    print('
Lint findings')
    if report.lint_counts:
        for k,v in sorted(report.lint_counts.items()): print(f"  {k:<8} {v}")
    else: print('  None')
    print('
Capability mappings')
    if report.capability_counts:
        for k,v in sorted(report.capability_counts.items(), key=lambda x:x[1], reverse=True): print(f"  {k:<30} {v}")
    else: print('  None')
    print('
Examples')
    for req in report.requirements[:max_examples]:
        caps=', '.join(c.id for c in req.capabilities) or 'unmapped'; lint=', '.join(f.code for f in req.lint) or 'none'
        print('-'*60); print(f"{req.id} | quality={req.quality_score} | lint={lint} | caps={caps}"); print(req.original_text[:500])

def write_json_report(report: AnalysisReport, path: str | Path) -> None:
    Path(path).write_text(json.dumps(report.to_dict(), indent=2, ensure_ascii=False), encoding='utf-8')
