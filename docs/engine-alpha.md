# REF Engine Alpha

**Version:** 0.1.0-alpha

Commit 0006A introduces a clean minimal Python engine.

## Implemented

- CLI
- Excel import
- Word import
- Markdown/Text import
- Simple requirement detection
- Console report

## Not implemented yet

- Linting
- Capability mapping
- JSON reports
- Gap analysis
- Normalization
- Export

## Run

```powershell
cd engine
python -m pip install -e .
python -m ref_engine.cli --help
python -m ref_engine.cli analyze --input "..\path\to\requirements.xlsx"
```
