# ADR 0005: Capability package structure

**Status:** Accepted  
**Date:** 2026-07-08

## Context

Knowledge packs need to scale beyond a few Markdown files. Capabilities require metadata, engineering guidance, evidence guidance, examples, and scoring guidance.

## Decision

Each reusable capability shall be represented as a package.

Recommended structure:

```text
knowledge/<group>/<capability>/
  capability.yaml
  engineering.md
  requirements.md
  evidence.md
  scoring.md
  examples.md
```

## Consequences

- Capabilities become independently maintainable.
- Future engines can load `capability.yaml`.
- Humans can read Markdown guidance.
- Domain packs can extend generic capabilities.

## Rationale

REF should separate machine-readable capability metadata from human-readable engineering guidance.
