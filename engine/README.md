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

Supported inputs in this commit:

- `.xlsx`
- `.docx`
- `.md`
- `.txt`

This commit deliberately implements only:

- import
- simple requirement detection
- console reporting

Linting, capability mapping, JSON reports and normalization come in later commits.
