# Architecture

REF is designed as a layered framework.

```text
Project Configuration
        |
        v
Policies + Knowledge Packs
        |
        v
Capability Catalog
        |
        v
Requirement Objects
        |
        v
Engineering / Evaluation / Gap Analysis
        |
        v
Exported Requirement Set
```

## Core components

### Import Engine

Transforms Word, Excel, PDF, Markdown or text into a normalized document model.

### Requirement Detector

Classifies document content as requirement, evidence, explanation, background, comment, assumption or question.

### Requirement Object

Internal structured representation of a requirement candidate.

### Engineering Engine

Applies universal requirement engineering rules.

### Evaluation Engine

Determines whether a requirement should be binary, scoreable or rejected.

### Capability Mapping

Maps requirements to capabilities in the capability catalog.

### Gap Analysis Engine

Compares expected capabilities with detected capabilities and identifies missing coverage.

### Requirement Generator

Produces normalized requirements, evidence statements and scoring criteria.

## Knowledge hierarchy

```text
Regulations
  -> Generic NFR
  -> Industry
  -> Solution
  -> Technology
```

Examples:

- Regulations: LUF, LOU, GDPR, NIS2.
- Generic NFR: availability, backup, logging, API, monitoring.
- Industry: aviation.
- Solution: AODB, BRS, RMS, FIDS.
- Technology: SaaS, AI, on-prem, mobile.

## AI role

AI may be used for classification, normalization and capability mapping. REF itself remains model-independent.
