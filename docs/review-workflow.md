# REF Review Workflow

**Version:** 0.1.0  
**Status:** Draft

The REF review workbook is the working copy for requirement review.

## Principle

The source document is never modified.

REF creates a separate review workbook that records:

- Original requirement
- REF findings
- Recommended action
- REF proposal
- Reviewer revision
- Reviewer decision
- Final output preview
- Version history
- Change log

## Decision values

| Decision | Meaning |
|---|---|
| New | Not yet reviewed |
| Accept REF Recommendation | Use REF proposal |
| Accept with Changes | Use reviewer revision |
| Keep Original | Use original requirement |
| Deferred | Do not export yet |

## Artifact model

```text
Source Document
      ↓
REF Review Workbook
      ↓
Final RFP Output
```

## Versioning

The review workbook contains:

- Review version
- Final RFP version
- Version history
- Change log

Final RFP artifacts shall not overwrite previous versions.

Recommended naming:

```text
AODB_RFP_Final_v0.1.xlsx
AODB_RFP_Final_v0.2.xlsx
AODB_RFP_Final_v1.0.xlsx
```
