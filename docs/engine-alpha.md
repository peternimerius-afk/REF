# REF Engine Alpha

**Version:** 0.1.0-alpha

Commit 0007 improves readability and reporting.

## Implemented

- CLI
- Excel import
- Word import
- Markdown/Text import
- Conservative requirement detection
- Basic linting with descriptive titles
- Console lint summary with descriptions
- Excel report output

## Excel report sheets

The generated workbook contains:

- `Summary`
- `Lint Findings`
- `Requirements`
- `Lint Legend`

## Run

```powershell
cd engine
python -m ref_engine.cli analyze --input "..\AI.xlsx" --excel-out "..\AI_REF_Report.xlsx"
```
