# Requirement Review Report Template

Use this template when reviewing existing requirements.

```yaml
source:
  id:
  document:
  location:
original:
quality:
  score:
  status:
lint:
  - code:
    severity:
    finding:
    recommendation:
capability_mapping:
  primary:
  secondary:
recommendation:
  action: keep | split | rewrite | reject | generate_missing
output:
  requirements:
    - id:
      text:
      evaluation:
      evidence:
notes:
```

## Markdown output

## `<Requirement ID>` — `<Title>`

### Original

> `<original requirement text>`

### Quality

`<score>/100`

### Lint findings

| Code | Severity | Finding | Recommendation |
|---|---|---|---|

### Capability mapping

`<capability>`

### Recommendation

`<keep | split | rewrite | reject | generate missing>`

### Normalized output

`<final requirement(s)>`
