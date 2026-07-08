from __future__ import annotations
import re
from .models import CapabilityMatch

def _terms_for_capability(cap: dict) -> list[str]:
    terms=set()
    for key in ['id','name','category']:
        val=cap.get(key)
        if isinstance(val,str):
            terms.add(val.lower()); terms.update(val.lower().replace('-',' ').split())
    for key in ['purpose','baseline_requirement']:
        val=cap.get(key)
        if isinstance(val,str):
            for word in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", val.lower()): terms.add(word)
    for field in ['typical_evidence','common_mistakes','related_capabilities']:
        val=cap.get(field,[])
        if isinstance(val,list):
            for item in val:
                if isinstance(item,str):
                    for word in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", item.lower()): terms.add(word)
    stop={'shall','support','provide','documented','documentation','technical','service','solution'}
    return sorted(t for t in terms if t not in stop and len(t)>=4)

def map_capabilities(text: str, capabilities: list[dict], limit: int=3) -> list[CapabilityMatch]:
    lower=text.lower(); matches=[]
    for cap in capabilities:
        terms=_terms_for_capability(cap); matched=[t for t in terms if t in lower]
        if not matched: continue
        conf=min(0.99,0.35+0.12*len(matched))
        matches.append(CapabilityMatch(str(cap.get('id','unknown')), str(cap.get('name',cap.get('id','unknown'))), round(conf,2), matched[:8]))
    matches.sort(key=lambda m:m.confidence, reverse=True)
    return matches[:limit]
