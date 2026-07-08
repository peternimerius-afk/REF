# ADR 0006: Compiler rule families

**Status:** Accepted  
**Date:** 2026-07-08

## Context

REF needs behaviour that can be implemented consistently by AI, scripts, applications, or future services.

## Decision

REF shall define compiler-style rule families:

- LINT
- TR
- MAP
- EVAL
- GEN
- GAP
- VAL

## Consequences

- Engineering decisions become explainable.
- AI suggestions can be checked against deterministic rules.
- Regression tests can verify expected behaviour.
- Future implementations can share one specification.

## Rationale

REF should behave like an engineering compiler, not a prose rewriting assistant.
