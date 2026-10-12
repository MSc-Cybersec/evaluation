# G04-BACKUP

## Question
What backup evidence is mandatory before go-live of a critical service?

## Sage response
## Bottom line

Before a critical service goes live, the mandatory backup evidence under **BACKUP-M-001** is proof that backups are **encrypted, access-controlled, and governed by documented retention and secure-deletion policies**. The catalogue also specifies automated configuration checks and restore-test execution as enforcement activities; therefore, the release record should contain a successful backup configuration assessment and restore-test report. No separate Mandard defining a critical-service-specific go-live evidence pack was found.

## Risk and impact

**High risk.** Without this evidence, backup data may be exfiltrated, retained unlawfully, deleted prematurely, or prove unusable during recovery. Go-live should be blocked where encryption, access control, retention, secure deletion, or the required enforcement checks cannot be demonstrated.

## Governing mandates

| Mandard | Title | Risk level |
|---|---|---:|
| **BACKUP-M-0001** | Encrypted Backups & Retention | High |

Per **BACKUP-M-001**: backups containing sensitive data must be encrypted, access-controlled, and subject to documented retention and secure-deletion policies. Its enforcement guidance calls for periodic configuration checks, backup-integrity verification, retention auditing, and restore-test execution in the testing pipeline.

## Framework mapping

The following directly relevant mappings were returned for **BACKUP-M-001**:

- **NIST SP 800-53 Rev. 5:** CP-9 System Backup; CP-10 System Recovery and Reconstitution; SC-12 Cryptographic Key Establishment and Management; SC-13 Cryptographic Protection; SC-28 Protection of Information at Rest; SI-12 Information Management and Retention; MP-4 Media Storage.
- **ISO/IEC 27001:2022**: A.8.13 Information Backup; A.8.14 Redundancy of Information Processing Facilities; A.5.29 Information Security During Disruption; A.5.30 ICT Readiness for Business Continuity; A.8.24 Use of Cryptography; A.5.33 Protection of Records.
- **PCI DSS v4.0:** Requirement 3 Protect Stored Account Data; Requirement 4 Protect Cardholder Data in Transit.
- **SOC 2 Type!I:** A1.2 Availability; C1.1 Confidentiality.

## Required actions

1. **Service owner:** Attach evidence that production backup targets and snapshots are encrypted.
2. **Cloud/platform owner:** Provide the effective RBAC or access-control configuration for backup vaults, stores, service accounts, and administrative roles.
3. **Data owner:** Approve and attach the applicable retention schedule and secure-deletion procedure.
4. **Engineering/release manager:** Attach a passing CSPM or backup-configuration check confirming encryption and retention settings.
5. **Service continuity owner:** Attach a successful restore-test report identifying the backup restored, target environment, execution date, outcome, and unresolved exceptions.
6. **Release authority:** Block go-live for failed checks or record a formally approved exception through the organisation’s risk-acceptance process.

## Evidence for audit

The minimum release evidence pack should include:

- Backup policy or configuration export showing scope, schedule, encryption, retention, and soft-delete/erasure settings.
- Backup-vault RBAC export or equivalent access-control report.
- Approved retention schedule and secure-deletion procedure.
- Passing CSPM, backup-integrity, or configuration-compliance report.
- Successful restore-test execution report and linked pipeline result.
- Exception and risk-acceptance record for any unmet requirement.

## Assumptions and limits

The only matching backup-domain control found was **BACKUP-M-001**. No Mandard explicitly defining a separate critical-service go-live checklist, recovery-time target, recovery-point target, or required sign-off role was found.

The only mapped knowledge document was **VeriFy-DECOM-002**, “14. Decommissioning & Destruction,” mapped to **BACKUP-M-001** and available at https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/720666741. It requires final backups before decommissioning but does not define pre-go-live backup evidence, so it was set aside for this decision.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**BACKUP-M-001**](https://verify.example-org.internal/?id=BACKUP-M-001) | High | Backup & Recovery | CCPA_CPRA (Storage Limitation); CIS_CONTROLS (CIS 11, CIS 3); COBIT_2019 (DSS04); CSA_CCM (BCR); CWE (CWE-327); ENISA_SMLA (SMLA-29); +13 more |

Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.

## Scoring notes
- actionability: pass (provisional auto-score)
- citation_correctness: pass (provisional auto-score)
- evidence_audit: pass (provisional auto-score)
- framework_mapping: pass (provisional auto-score)
- risk_impact: pass (provisional auto-score)
- bottom_line: pass (provisional auto-score)
- governing_mandards: fail (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass