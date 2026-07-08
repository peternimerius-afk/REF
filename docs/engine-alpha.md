# REF Engine Alpha

**Version:** 0.1.0-alpha

Commit 0006B improves the first real Excel test result.

## Implemented

- CLI
- Excel import
- Word import
- Markdown/Text import
- Conservative requirement detection
- Noise filtering for Excel ID cells and section headings
- Basic lint summary
- Console report

## Not implemented yet

- Capability mapping
- JSON reports
- Gap analysis
- Normalization
- Export

## Run

```powershell
cd engine
python -m ref_engine.cli analyze --input "..\AI.xlsx"
```
