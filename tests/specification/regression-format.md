# Regression Test Format

**Version:** 0.1.0  
**Status:** Draft

Regression tests verify compiler behaviour.

## Test case structure

```yaml
id: REG-001
name: Split API requirement
input:
  text: The solution shall support REST APIs, OpenAPI documentation and webhook callbacks.
  project_config: projects/example-aodb-saas.yaml
expected:
  lint:
    - RFP001
  transformations:
    - TR-001
  requirements:
    - text: The solution shall support REST APIs.
      evaluation: binary
      capability: api-integration
    - text: OpenAPI documentation shall be provided.
      evaluation: binary
      capability: api-documentation
    - text: The solution shall support webhook callbacks.
      evaluation: binary
      capability: webhook-callbacks
```

## Regression principles

Regression tests shall verify:

- Lint findings
- Transformation rules
- Capability mapping
- Evaluation method
- Evidence separation
- Final requirement wording
- Gap findings where applicable
