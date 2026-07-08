# Simple Review Example

## Original

> The solution shall provide robust authentication and flexible authorization and the supplier shall describe how this is implemented.

## Lint

```yaml
lint:
  - code: RFP001
    severity: Error
    finding: Multiple obligations detected.
    recommendation: Split authentication and authorization.
  - code: RFP002
    severity: Error
    finding: Subjective wording detected.
    recommendation: Replace "robust" and "flexible" with objective criteria.
  - code: RFP004
    severity: Warning
    finding: Evidence request embedded.
    recommendation: Move description request to evidence.
```

## Normalized requirements

### Requirement 1

> The solution shall support federated authentication.

Evaluation:

> Yes / No

Evidence:

> Technical documentation.

### Requirement 2

> The solution shall support role-based access control.

Evaluation:

> Yes / No

Evidence:

> Technical documentation.
