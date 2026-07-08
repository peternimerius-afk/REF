# Requirement Object

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define the canonical internal representation of a requirement.

The Requirement Object is the central processing unit in REF. Importers, classifiers, linters, evaluators, generators, and exporters shall operate on Requirement Objects rather than raw document text.

## Design goals

A Requirement Object shall:

- Preserve original source text.
- Support traceability to document, table, row, page, section, or paragraph.
- Separate requirement, evidence, evaluation, and verification.
- Support linting and quality scoring.
- Support capability mapping.
- Support gap analysis.
- Support export to Word, Excel, Markdown, YAML, or JSON.
- Avoid storing confidential project content in reusable REF framework files.

## Canonical structure

```yaml
id: NFR-001
title: Availability
status: draft

source:
  document_id: draft-nfr
  document_name: draft-nfr.xlsx
  document_type: excel
  location:
    worksheet: NFR
    row: 12
    column: Re-written requirement
  original_text: >
    The solution shall provide high availability and the supplier shall
    describe historical uptime and planned maintenance procedures.

classification:
  primary: requirement
  confidence: 0.92
  secondary:
    - evidence
    - explanation

capability_mapping:
  primary:
    id: availability
    confidence: 0.95
  secondary:
    - id: maintenance-window
      confidence: 0.72

engineering:
  quality_score: 44
  status: needs_split
  lint:
    - code: RFP001
      severity: Error
      message: Multiple obligations detected.
    - code: RFP004
      severity: Warning
      message: Evidence embedded in requirement.

evaluation:
  method: binary
  rationale: Minimum availability target is a mandatory baseline.
  scoreable_candidate: false

normalized:
  requirements:
    - id: NFR-001.1
      text: Monthly production availability shall be at least 99.9%.
      evaluation:
        method: binary
      evidence:
        - SLA
    - id: NFR-001.2
      text: Availability calculation method shall be documented.
      evaluation:
        method: binary
      evidence:
        - SLA

evidence:
  requested:
    - Historical availability reports.
    - SLA.

verification:
  method: documentation_review
  verifier_notes:
    - Verify availability target and calculation method.

traceability:
  generated_from:
    - source.original_text
  references:
    - core/engineering.md#e001-atomicity
    - core/evaluation.md
    - core/lint.md#rfp001-multiple-obligations
```

## Required fields

| Field | Required | Description |
|---|---:|---|
| `id` | Yes | Stable identifier |
| `source.original_text` | Yes | Original imported text |
| `classification.primary` | Yes | Content classification |
| `capability_mapping.primary` | Recommended | Primary capability |
| `evaluation.method` | Yes after evaluation | Binary, scoreable, reject, etc. |
| `engineering.quality_score` | Yes after analysis | 0-100 score |
| `engineering.lint` | Yes after linting | Diagnostic list |
| `traceability.generated_from` | Yes after normalization | Source linkage |

## Status values

| Status | Meaning |
|---|---|
| `imported` | Imported but not analyzed |
| `classified` | Content classification complete |
| `mapped` | Capability mapping complete |
| `needs_split` | Multiple obligations detected |
| `needs_rewrite` | Engineering defects detected |
| `rejected` | Cannot be objectively evaluated |
| `normalized` | Procurement-ready |
| `generated` | Created from missing capability |
| `approved` | Human reviewed |
| `exported` | Included in output |

## Evaluation methods

| Method | Meaning |
|---|---|
| `binary` | Yes/No compliance |
| `score_1_4` | Objective score scale |
| `baseline_plus_score` | Mandatory baseline plus scored maturity |
| `reject` | Not suitable as written |
| `defer` | Requires human decision |

## Confidentiality rule

Requirement Objects may contain project content. They belong in project repositories or regression fixtures, not in the public REF framework unless anonymized.

REF framework files shall contain methodology, schemas, examples, and generic knowledge only.
