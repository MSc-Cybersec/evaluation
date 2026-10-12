# G20-DECOM

## Question
What evidence is required when decommissioning an application handling sensitive data?

## Sage response

## Bottom line

An application handling sensitive data must not be marked decommissioned until the change record contains evidence of compliant retention, secure erasure or irreversible de-identification, removal of every access and exposure path, and updates to authoritative asset inventories. Per **DECOM-M-001**, closure must be blocked until this evidence is attached; for SaaS or externally managed platforms, a provider certificate of assurance is required.

## Risk and impact

The applicable mandards are rated **High**. Missing evidence creates the risk that sensitive data remains recoverable from databases, backups, cloud resources, or physical media, while orphaned accounts, certificates, DNS entries, firewall rules, and APIs leave an unmonitored attack surface.

The consequences include data breach, privacy or retention violations, unauthorized access, continued supplier exposure, unnecessary infrastructure cost, and inability to prove compliant disposal during audit or regulatory review.

## Governing mandards

| Mandard | Title | Risk | Relevance |
|---|---|---:|---|
| **DECOM-M-001** | Secure Decommissioning and Data Destruction | High | Primary decommissioning, destruction, exposure removal, and evidence requirement |
| **BACKUP-M-001** | Encrypted Backups & Retention | High | Protection, retention, and secure deletion of sensitive backups |
| **DATA-M-002** | Data Classification & Handling | High | Data inventory, classification, retention, storage, and handling requirements |
| **IAM-M-004** | Maintain Identity Lifecycle Management for CI/CD Accounts | High | Removal and inventory of affected CI/CD identities and service accounts |
| **CRYPT-M-005** | Certificate Management & Pinning | High | Retirement of certificates and related renewal arrangements |
| **NSEG-M-002** | DMZ & Network Segmentation | High | Removal or validation of network and firewall access paths |
| **WAF-M-001** | WAF Rule Configuration & Management | High | Removal of WAF associations and rules for retired external services |
| **GOV-G-006** | Security Deviation and Exception Management | High | Formal approval of any incomplete or exceptional decommissioning action |

Per **DECOM-M-001**: data must first be archived or retained according to the approved schedule, then securely erased using a media-appropriate method. Data that cannot be deleted must be de-identified so individuals cannot be re-identified, and the reason for retention must be recorded. All credentials, access paths, certificates, APIs, DNS records, and network exposure must then be removed.

Implementation guidance is provided by **VeriFy-DECOM-002**, mapped to **DECOM-M-001**, **BACKUP-M-001**, **DATA-M-002**, **IAM-M-004**, **CRYPT-M-005**, **NSEG-M-002**, **WAF-M-001**, and **GOV-G-006**: [Decommissioning & Destruction standard](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/720666741).

## Framework mapping

The primary decommissioning mandard, **DECOM-M-001**, maps to:

| Framework | Controls returned by the catalogue |
|---|---|
| NIST SP 800-53 Rev. 5 | MP-6, CM-8, SA-22, AC-2 |
| ISO/IEC 27001:2022 | A.8.10 Information deletion |
| SOC 2 | P4 Privacy — Use, Retention and Disposal |
| GDPR | Article 17 Right to erasure |
| CCPA/CPRA | Consumer Right to Delete; Storage Limitation |
| CIS Controls v8 | CIS 1 Inventory and Control of Enterprise Assets; CIS 3 Data Protection |
| NIST CSF 2.0 | ID.AM; PR.DS |

## Required actions

1. **Approve the data-disposition decision.**  
   The application owner and data owner must identify all sensitive-data locations, classifications, applicable retention periods, legal holds, and the approved outcome for each dataset: migrate, archive, delete, or de-identify. Per **DATA-M-002**, handling and retention must correspond to the declared data classification.

2. **Complete and protect any required final backup.**  
   Per **BACKUP-M-001**, document the final backup where required, including its location, encryption status, access restrictions, retention expiry, and eventual secure-deletion method. Do not create a final backup where retention or deletion obligations prohibit it.

3. **Destroy or de-identify residual data.**  
   Per **DECOM-M-001**, sanitize databases, storage, virtual disks, snapshots, caches, logs, queues, replicas, removable media, and physical hardware using a method appropriate to the media. Where deletion is impossible, document irreversible de-identification and the reason the source records could not be deleted.

4. **Obtain supplier disposal assurance.**  
   For SaaS or externally managed infrastructure, obtain a certificate of assurance confirming that systems, hardware, copies, and sensitive data were securely disposed of and cannot be recovered. The implementation standard aligns this assurance to NIST SP 800-88: **VeriFy-DECOM-002**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/720666741).

5. **Remove identities and credentials.**  
   Per **DECOM-M-001**, deprovision application and service accounts, access groups, secrets, tokens, keys, and other credentials. Per **IAM-M-004**, update the authoritative identity inventory for affected CI/CD identities and retain the deprovisioning record.

6. **Remove external and internal exposure.**  
   Per **DECOM-M-001**, remove public and private DNS records, redundant APIs, firewall rules, WAF rules, cloud resources, and monitoring entries. Evidence should demonstrate that no route to the retired service remains. **NSEG-M-002** and **WAF-M-001** govern the affected network and WAF configurations.

7. **Retire certificates.**  
   Per **DECOM-M-001**, retire certificates associated with the service and notify certificate management that renewal is no longer required. **CRYPT-M-005** governs certificate inventory and management.

8. **Update authoritative inventories and close the change.**  
   Update the CMDB, application portfolio, cloud inventory, certificate inventory, identity inventory, API catalogue, and monitoring inventory. The application owner, data owner, infrastructure owner, and independent security reviewer should approve the closure record.

9. **Record any incomplete action as a deviation.**  
   Per **GOV-G-006**, any departure must identify the affected control, technical justification, compensating controls, residual-risk owner, independent approver, and expiry date. An unresolved action must not be silently accepted as decommissioning completion.

## Evidence for audit

The minimum audit pack should contain:

| Evidence artefact | What it must demonstrate |
|---|---|
| Approved decommissioning change record | Scope, component inventory, owners, dates, approvals, and completion status |
| Data-disposition register | Each dataset and copy, classification, system location, retention basis, legal hold status, and disposition decision |
| Retention approval | Approval from the data owner or relevant governance authority and reference to the applicable retention schedule |
| Final-backup record | Completion timestamp, encryption, repository, authorized users, retention expiry, and deletion plan |
| Sanitization evidence | Tool logs, cloud deletion records, media destruction certificates, cryptographic-erasure records, or signed destruction attestations |
| De-identification evidence | Method used, validation that re-identification is not possible, retained-data scope, and recorded reason deletion was not possible |
| Supplier certificate of assurance | Confirmation that externally managed systems, hardware, copies, backups, and sensitive data were securely disposed of and cannot be recovered |
| Identity-removal report | Deleted or disabled users, service accounts, CI/CD identities, groups, roles, tokens, secrets, and privileged access |
| Certificate retirement record | Certificate revocation or retirement, inventory update, key disposition, and cancellation of renewal |
| Network closure evidence | Approved firewall and security-group changes plus post-change validation showing the service is no longer reachable |
| DNS, WAF, and API removal evidence | Before-and-after configuration, change logs, deleted records or routes, and validation scans |
| Infrastructure destruction record | Deleted cloud resources, securely formatted operating systems, factory-reset devices, or physical destruction records |
| Inventory updates | CMDB, application portfolio, cloud asset inventory, API catalogue, certificate inventory, and monitoring records showing retired status |
| Independent closure approval | Security or governance sign-off confirming that evidence was reviewed before closure |
| Deviation record, if applicable | Approved, unexpired exception satisfying **GOV-G-006**, including residual-risk ownership and compensating controls |

Per **DECOM-M-001**, the decommissioning workflow should prevent closure until secure-erasure or de-identification evidence, external assurance where applicable, and proof of identity, DNS, firewall, WAF, certificate, and asset-inventory cleanup are attached.

## Assumptions and limits

The application architecture, hosting model, data classification, retention schedule, legal holds, backup topology, and supplier contract were not provided and therefore were not verified. The precise evidence set must be scoped against every production, disaster-recovery, backup, analytics, logging, test, and supplier-held copy of the application’s sensitive data.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**BACKUP-M-001**](https://verify.example-org.internal/?id=BACKUP-M-001) | High | Backup & Recovery | CCPA_CPRA (Storage Limitation); CIS_CONTROLS (CIS 11, CIS 3); COBIT_2019 (DSS04); CSA_CCM (BCR); CWE (CWE-327); ENISA_SMLA (SMLA-29); +13 more |
| [**CRYPT-M-005**](https://verify.example-org.internal/?id=CRYPT-M-005) | High | Cryptography | CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.13, A.8.14); MITRE_ATT&CK (M1041); +9 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DECOM-M-001**](https://verify.example-org.internal/?id=DECOM-M-001) | High | Decommissioning & Destruction | CCPA_CPRA (Consumer Right to Delete, Storage Limitation); CIS_CONTROLS (CIS 1, CIS 3); GDPR (Article 17); ISO_27001 (A.8.10); NIST_CSF (ID.AM, PR.DS); NIST_SP_800_53 (AC-2, CM-8, MP-6); +1 more |
| [**IAM-M-004**](https://verify.example-org.internal/?id=IAM-M-004) | High | Identity & Access Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.18); MITRE_ATT&CK (M1018, M1026, M1032); +10 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |
| [**WAF-M-001**](https://verify.example-org.internal/?id=WAF-M-001) | High | Web Application Firewall | CIS_CONTROLS (CIS 12, CIS 16); CWE (CWE-77, CWE-79, CWE-89); ISO_27001 (A.8.20, A.8.22, A.8.26); MITRE_ATT&CK (M1020, M1021, M1031); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, CM-6, SA-11); +6 more |

Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
## Scoring notes
- actionability: pass (provisional auto-score)
- citation_correctness: pass (provisional auto-score)
- evidence_audit: pass (provisional auto-score)
- framework_mapping: pass (provisional auto-score)
- risk_impact: pass (provisional auto-score)
- bottom_line: pass (provisional auto-score)
- governing_mandards: pass (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass