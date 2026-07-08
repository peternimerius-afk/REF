from __future__ import annotations
from pathlib import Path
from typing import Any
import yaml

def load_yaml(path: str | Path) -> Any:
    with Path(path).open('r', encoding='utf-8') as f: return yaml.safe_load(f)

def find_repo_root(start: str | Path | None=None) -> Path:
    current=Path(start or '.').resolve()
    if current.is_file(): current=current.parent
    for cand in [current,*current.parents]:
        if (cand/'knowledge').exists() and (cand/'policies').exists(): return cand
    return current

def load_capabilities(repo_root: str | Path) -> list[dict[str, Any]]:
    root=Path(repo_root); caps=[]
    for cap_file in root.glob('knowledge/**/capability.yaml'):
        data=load_yaml(cap_file)
        if isinstance(data,dict):
            data['_source']=str(cap_file.relative_to(root)); caps.append(data)
    flat=root/'catalog'/'capabilities.yaml'
    if flat.exists():
        data=load_yaml(flat)
        if isinstance(data,dict):
            for item in data.get('capabilities',[]):
                item['_source']=str(flat.relative_to(root)); caps.append(item)
    return caps
