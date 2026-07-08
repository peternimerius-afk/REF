# REF Schemas

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define the structured objects used by REF.

Schemas in this file are conceptual. Future versions may provide formal JSON Schema or YAML Schema definitions.

---

## Requirement Object

The Requirement Object is the central unit of REF.

```yaml
id: NFR-001
source:
  document: draft-requirements.docx
  location: section 5.2
  original_text: >
    The solution shall provide robust authentication and authorization.
classification:
  type: requirement
  confidence: 0.94
capability:
  primary: authentication
  secondary:
    - authorization
engineering:
  status: needs_split
  quality_score: 42
  lint:
    - RFP001
    - RFP002
evaluation:
  method: binary
  rationale: Mandatory baseline compliance.
requirement:
  text: The solution shall support federated authentication.
  actor: solution
  obligation: support
  object: federated authentication
evidence:
  - Technical documentation
verification:
  method: documentation_review
traceability:
  generated_from:
    - source.original_text
  references:
    - core/engineering.md#e001-atomicity
```

---

## Capability Object

Capabilities describe what a project may need to procure.

```yaml
id: api-integration
name: API Integration
category: interoperability
description: Ability to expose and consume machine-readable interfaces.
normally_required: true
default_evaluation: binary
scoreable_variant: api-maturity
dependencies:
  - authentication
  - authorization
  - logging
typical_evidence:
  - API documentation
  - OpenAPI specification
  - Integration guide
knowledge_packs:
  - generic/api
```

---

## Knowledge Pack Object

Knowledge packs describe domain, technology, regulatory, or industry-specific engineering knowledge.

```yaml
id: technology-ai
name: AI Technology
type: technology
extends:
  - generic/security
  - generic/privacy
capabilities:
  required:
    - ai-governance
    - data-isolation
    - model-monitoring
  recommended:
    - explainability
    - model-lifecycle-management
  scoreable:
    - ai-governance-maturity
```

---

## Policy Object

Policies configure REF behaviour.

```yaml
id: default
evaluation:
  default_method: binary
  maximum_scoreable_ratio: 0.25
style:
  language: en
  mandatory_keyword: shall
  maximum_binary_words: 20
  maximum_scoreable_words: 35
requirements:
  split_multiple_obligations: true
  separate_evidence: true
  allow_subjective_language: false
```

---

## Project Configuration Object

A project configuration describes the current procurement context.

```yaml
project:
  name: example-airport-aodb
  language: en
procurement:
  profile: sweden-luf
deployment:
  model: saas
industry:
  - aviation
solution:
  - aodb
technology:
  - ai
security:
  classification: lis-2-3-3
data:
  personal_data: true
evaluation:
  maximum_scoreable_ratio: 0.20
```

---

## Lint Finding Object

```yaml
code: RFP001
severity: Error
message: Multiple obligations detected.
recommendation: Split into atomic requirements.
reference: core/lint.md#rfp001-multiple-obligations
```

---

## Gap Finding Object

```yaml
capability: disaster-recovery
status: missing
source:
  expected_from:
    - deployment/saas
    - generic/resilience
recommendation:
  action: generate_requirement
  priority: high
```
