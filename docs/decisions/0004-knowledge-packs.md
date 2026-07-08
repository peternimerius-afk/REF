# ADR 0004: Knowledge packs

**Status:** Accepted  
**Date:** 2026-07-08

## Context

REF needs to support generic NFRs, aviation, AODB, BRS, RMS, FIDS, SaaS, AI, and future domains without hardcoding them in the core.

## Decision

Domain, technology, regulatory, and solution-specific knowledge shall be implemented as knowledge packs.

## Consequences

- REF core remains domain-agnostic.
- Aviation knowledge is separate from core engineering rules.
- AI is treated as a technology knowledge pack.
- Public framework files shall not contain confidential customer, vendor, or project content.

## Rationale

The core defines how requirements are engineered. Knowledge packs define what capabilities may be relevant.
