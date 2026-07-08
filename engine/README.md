# REF Engine Alpha

Minimal executable REF engine.

## Install

```powershell
cd engine
python -m pip install -e .
```

## Run

```powershell
python -m ref_engine.cli analyze --input "..\path\to\requirements.xlsx"
```

## Run with Excel report output

```powershell
python -m ref_engine.cli analyze --input "..\AI.xlsx" --excel-out "..\AI_REF_Report.xlsx"
```

Supported inputs:

- `.xlsx`
- `.docx`
- `.md`
- `.txt`

Current functionality:

- import
- simple requirement detection
- basic linting
- console reporting
- Excel report output
