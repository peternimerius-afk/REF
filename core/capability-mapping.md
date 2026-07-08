# Capability Mapping

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define how requirements are mapped to capabilities.

Capability mapping connects existing requirements to the Capability Catalog. It enables normalization, duplicate detection, coverage analysis, and gap analysis.

## Principle

A requirement shall be mapped to the capability it is intended to ensure, not merely to keywords contained in the text.

Example:

> The supplier shall provide OpenAPI documentation.

This may map to:

- API Integration
- API Documentation

It is not primarily a documentation capability.

## Mapping levels

| Level | Meaning |
|---|---|
| Primary | Main capability addressed by the requirement |
| Secondary | Related capabilities |
| Dependency | Capability required because of the primary capability |
| Evidence-only | Capability mentioned only as evidence |

## Mapping confidence

| Confidence | Meaning |
|---:|---|
| 0.90-1.00 | Strong semantic match |
| 0.70-0.89 | Likely match |
| 0.40-0.69 | Possible match, review recommended |
| 0.00-0.39 | Weak match |

## Mapping object

```yaml
capability_mapping:
  primary:
    id: api-integration
    confidence: 0.94
  secondary:
    - id: authentication
      confidence: 0.71
    - id: audit-logging
      confidence: 0.68
  dependencies:
    - id: authorization
      reason: API access requires authorization.
```

## Mapping rules

### M001: Map by intent

Map to the intended capability, not to incidental words.

### M002: Split before final mapping

If a requirement contains multiple obligations, split before assigning final capability mappings.

### M003: Evidence is not capability coverage

Evidence text may mention a capability without covering it.

### M004: Capability coverage requires obligation

A capability is covered only where there is an actual obligation.

### M005: Scoreable maturity is a separate capability

A scoreable maturity area should be mapped separately from mandatory baseline compliance.

Example:

- `api-integration` = binary baseline
- `api-maturity` = scoreable differentiator

## Coverage states

| State | Meaning |
|---|---|
| `covered` | Capability has at least one valid requirement |
| `partial` | Capability is mentioned but not fully covered |
| `evidence_only` | Only evidence exists |
| `missing` | Capability expected but absent |
| `not_applicable` | Capability excluded by project configuration |

## Example

Requirement:

> The solution shall support REST APIs, OpenAPI documentation and webhook callbacks.

Initial mapping:

```yaml
primary: api-integration
secondary:
  - api-documentation
  - webhook-callbacks
status: needs_split
```
