# REF Compiler Specification

**Version:** 0.1.0  
**Status:** Draft

The REF Compiler defines executable behaviour for requirement engineering.

The compiler does not replace the REF core principles. It operationalizes them.

## Compiler stages

```text
Requirement Object
        ↓
Lint
        ↓
Transform
        ↓
Map
        ↓
Evaluate
        ↓
Validate
        ↓
Generate / Export
```

## Rule families

| Prefix | Family | Purpose |
|---|---|---|
| LINT | Lint Rules | Detect defects |
| TR | Transformation Rules | Rewrite or restructure requirement objects |
| MAP | Mapping Rules | Map requirements to capabilities |
| EVAL | Evaluation Rules | Select binary/scored/reject evaluation |
| GEN | Generation Rules | Generate requirements for missing capabilities |
| GAP | Gap Rules | Detect missing capabilities |
| VAL | Validation Rules | Validate output consistency |

## Deterministic principle

AI may assist with classification, mapping, wording and suggestions.

REF rules decide the engineering action.

A decision should be explainable as:

```text
Applied <RULE-ID> because <CONDITION> was detected.
```
