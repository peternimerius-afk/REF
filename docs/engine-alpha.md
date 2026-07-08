# REF Engine Alpha

**Version:** 0.1.0-alpha

Commit 0006 introduces the first executable REF engine.

## Capabilities

The alpha engine can:

- Import `.xlsx`, `.docx`, `.md`, and `.txt`
- Classify content units
- Detect candidate requirements
- Apply initial lint rules
- Map requirements to loaded capabilities
- Produce console and JSON reports

## Non-goals

The alpha engine does not yet:

- Rewrite requirements
- Generate missing requirements
- Perform full gap analysis
- Export revised Word or Excel files
- Use AI
- Parse PDF files

## Run

```powershell
cd engine
python -m pip install -e .
python -m ref_engine.cli analyze --input "..\your-file.xlsx" --project "..\projects\example-aodb-saas.yaml"
```
