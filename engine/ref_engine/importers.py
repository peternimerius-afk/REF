from __future__ import annotations
from pathlib import Path
from .models import ContentUnit, SourceLocation
SUPPORTED_SUFFIXES = {".xlsx", ".docx", ".md", ".txt"}

def import_file(path: str | Path) -> list[ContentUnit]:
    p = Path(path)
    suffix = p.suffix.lower()
    if suffix == ".xlsx":
        return import_xlsx(p)
    if suffix == ".docx":
        return import_docx(p)
    if suffix in {".md", ".txt"}:
        return import_text(p)
    raise ValueError(f"Unsupported file type: {suffix}. Supported: {sorted(SUPPORTED_SUFFIXES)}")

def import_text(path: Path) -> list[ContentUnit]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    units=[]
    for idx,line in enumerate(text.splitlines(), start=1):
        cleaned=line.strip()
        if cleaned:
            units.append(ContentUnit(f"TXT-{idx}", cleaned, SourceLocation(str(path), path.suffix.lower().lstrip('.'), {"line": idx}), "line"))
    return units

def import_docx(path: Path) -> list[ContentUnit]:
    try:
        from docx import Document
    except ImportError as exc:
        raise RuntimeError("python-docx is required for DOCX import.") from exc
    doc=Document(str(path)); units=[]; counter=1
    for idx,para in enumerate(doc.paragraphs, start=1):
        text=para.text.strip()
        if text:
            units.append(ContentUnit(f"DOCX-P-{counter}", text, SourceLocation(str(path), "docx", {"paragraph": idx}), "paragraph")); counter+=1
    for t_idx,table in enumerate(doc.tables, start=1):
        for r_idx,row in enumerate(table.rows, start=1):
            for c_idx,cell in enumerate(row.cells, start=1):
                text=cell.text.strip()
                if text:
                    units.append(ContentUnit(f"DOCX-T-{t_idx}-{r_idx}-{c_idx}", text, SourceLocation(str(path), "docx", {"table": t_idx,"row": r_idx,"column": c_idx}), "table_cell"))
    return units

def import_xlsx(path: Path) -> list[ContentUnit]:
    try:
        import openpyxl
    except ImportError as exc:
        raise RuntimeError("openpyxl is required for XLSX import.") from exc
    wb=openpyxl.load_workbook(str(path), data_only=True)
    units=[]
    for ws in wb.worksheets:
        headers={}
        for row_idx,row in enumerate(ws.iter_rows(values_only=True), start=1):
            values=["" if v is None else str(v).strip() for v in row]
            if row_idx==1:
                headers={i+1: val for i,val in enumerate(values) if val}
            for col_idx,value in enumerate(values, start=1):
                if not value or row_idx==1:
                    continue
                header=headers.get(col_idx, f"Column {col_idx}")
                units.append(ContentUnit(f"XLSX-{ws.title}-{row_idx}-{col_idx}", value, SourceLocation(str(path), "xlsx", {"worksheet": ws.title,"row": row_idx,"column": col_idx,"header": header}), "cell"))
    return units
