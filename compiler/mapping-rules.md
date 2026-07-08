# Mapping Rules

**Version:** 0.1.0  
**Status:** Draft

Mapping rules connect Requirement Objects to capabilities.

## MAP-001 Map by procurement intent

Map to the capability the requirement intends to secure.

Do not map only by keyword occurrence.

---

## MAP-002 Evidence does not provide coverage

Evidence text alone does not mean a capability is covered.

---

## MAP-003 Split before final mapping

Requirements with multiple obligations shall be split before final mapping.

---

## MAP-004 Dependency expansion

When a capability has dependencies, add dependent capabilities to the expected capability set.

Example:

API Integration may imply:

- Authentication
- Authorization
- Audit Logging
- Monitoring

---

## MAP-005 Maturity as separate capability

Scoreable maturity variants shall be separate capabilities from mandatory baseline capabilities.

Example:

- `api-integration`
- `api-maturity`
