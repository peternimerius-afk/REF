# REF Engine Alpha

**Version:** 0.1.0-alpha  
**Status:** Experimental

The REF Engine is the executable implementation of the Requirements Engineering Framework.

This first alpha provides:

- CLI entry point
- Input parsing for `.xlsx`, `.docx`, `.md`, and `.txt`
- Candidate requirement detection
- Basic content classification
- Basic linting
- Basic capability mapping from capability YAML
- Console report output
- JSON report output

PDF support, advanced normalization, full gap analysis, and document export are intentionally deferred.

## Install for local development

From the repository root:

```powershell
cd engine
python -m pip install -e .
```

## Analyze a file

```powershell
python -m ref_engine.cli analyze --input "..\path\to\requirements.xlsx" --project "..\projects\example-aodb-saas.yaml"
```

Optional JSON output:

```powershell
python -m ref_engine.cli analyze --input "..\path\to\requirements.xlsx" --json-out report.json
```

## Notes

The engine currently uses deterministic rules. It does not call an AI model.
