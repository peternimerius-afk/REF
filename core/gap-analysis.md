# Gap Analysis

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define how REF detects missing capabilities and missing requirements.

Gap analysis compares expected capabilities from project configuration and knowledge packs against capabilities covered by existing requirements.

## Purpose

REF shall not only improve existing requirements. It shall also identify important capabilities that are missing.

Missing requirements are often more damaging than verbose requirements because they may be difficult to add after publication.

## Inputs

Gap analysis requires:

1. Project configuration
2. Capability catalog
3. Selected knowledge packs
4. Existing Requirement Objects
5. Capability mappings
6. Policies

## Process

```text
Project configuration
        ↓
Load required knowledge packs
        ↓
Resolve expected capabilities
        ↓
Map existing requirements to capabilities
        ↓
Calculate coverage
        ↓
Identify missing or partial capabilities
        ↓
Recommend generate / ignore / review
```

## Expected capability sources

Expected capabilities may come from:

- Generic NFR baseline
- Procurement profile
- Security profile
- Industry pack
- Solution pack
- Deployment model
- Technology pack
- Organization policy
- Project configuration

## Coverage calculation

```text
Expected capabilities - covered capabilities = missing capabilities
```

Coverage states:

| State | Meaning |
|---|---|
| `covered` | At least one valid requirement exists |
| `partial` | Some but not all required aspects covered |
| `evidence_only` | Evidence exists but no obligation |
| `missing` | No valid requirement exists |
| `not_applicable` | Excluded by configuration |
| `deferred` | Human decision required |

## Gap finding object

```yaml
gap:
  capability: disaster-recovery
  status: missing
  priority: high
  expected_from:
    - deployment/saas
    - generic/resilience
  rationale: SaaS services require defined recovery capability.
  recommendation:
    action: generate_requirement
    evaluation: binary
    evidence:
      - Disaster recovery plan
      - DR test report
```
