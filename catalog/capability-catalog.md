# Capability Catalog

The capability catalog defines reusable capabilities that may require non-functional requirements.

Capabilities are not requirements. Capabilities are used to derive, validate and gap-check requirements.

## Generic NFR capabilities

| Capability | Usually mandatory | Usually scoreable | Typical evidence |
|---|---:|---:|---|
| Availability | Yes | Sometimes | SLA, availability reports |
| Backup | Yes | Rarely | Backup policy, restore test report |
| Disaster Recovery | Yes | Sometimes | DR plan, test report |
| RTO | Yes | Sometimes | SLA, DR documentation |
| RPO | Yes | Sometimes | SLA, backup architecture |
| Authentication | Yes | Rarely | Technical documentation |
| Authorization | Yes | Rarely | Access control documentation |
| Identity Federation | Yes | Rarely | Integration documentation |
| Audit Logging | Yes | Rarely | Logging documentation |
| Monitoring | Yes | Sometimes | Monitoring documentation |
| Incident Management | Yes | Sometimes | Process documentation |
| Encryption in Transit | Yes | Rarely | Security documentation |
| Encryption at Rest | Yes | Rarely | Security documentation |
| Key Management | Yes | Sometimes | Key management policy |
| API Support | Often | Sometimes | API documentation |
| API Maturity | No | Yes | Developer portal, OpenAPI, sandbox |
| Performance | Yes | Sometimes | Performance test reports |
| Capacity | Yes | Sometimes | Capacity documentation |
| Scalability | Often | Sometimes | Architecture documentation |
| Maintainability | Often | Sometimes | Maintenance documentation |
| Support | Yes | Sometimes | Support model, SLA |
| Patch Management | Yes | Rarely | Patch policy |
| Vulnerability Management | Yes | Sometimes | Vulnerability process |
| Configuration Management | Often | Rarely | Configuration documentation |
| Data Retention | Often | Rarely | Retention policy |
| Data Portability | Often | Sometimes | Export documentation |
| Interoperability | Often | Sometimes | Interface documentation |
| Time Synchronization | Sometimes | Rarely | Architecture documentation |
| Business Continuity | Yes | Sometimes | BCP, test report |
| Operational Resilience | Often | Yes | Resilience design, test reports |

## Use in gap analysis

Expected capabilities are selected from project configuration and loaded knowledge packs.

Gap analysis compares expected capabilities with mapped capabilities in the requirement set.
