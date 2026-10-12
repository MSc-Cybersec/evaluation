# G53-DB

## Question
What evidence proves secure database access and encryption posture?

## Sage response

## Bottom line

Secure database posture is proven by current, system-generated evidence showing encryption at rest, enforced TLS 1.3+, separately managed and rotated keys, least-privilege access, quarterly access reviews, and tamper-resistant activity logging. Policy statements or screenshots alone are insufficient; the audit pack should combine configuration exports, effective-permission queries, negative connection tests, key-management records, access approvals, and SIEM evidence for every production database.

## Risk and impact

Failure to encrypt database data or connections is **Critical** because compromise of storage, backups, credentials, or network traffic can expose sensitive data at scale. Excessive privileges, unmanaged keys, and incomplete monitoring are **High** risk because they increase breach impact and prevent timely detection, attribution, and investigation.

A catalogue conflict requires resolution: the implementation guardrail `VeriFy-DATA-GEN-003` states that database-level encryption is not required on-premises, while **DB-M-002** and **CRYPT-M-001** require encryption of database and sensitive data at rest. The Mandards should govern unless an approved deviation explicitly resolves the conflict.

## Governing mandards

### Directly applicable

| Mandard | Title | Risk | Requirement relevant to evidence |
|---|---|---:|---|
| **DB-M-002** | Database Encryption At-Rest & In-Transit | Critical | Per **DB-M-002**: database data must use AES-256 with approved keys, database connections must use TLS 1.3+, and sensitive columns require TDE or column-level encryption. |
| **CRYPT-M-001** | Encryption at Rest | Critical | Per **CRYPT-M-001**: sensitive databases, file systems, backups, and caches must use AES-256 or equivalent, with keys managed separately from encrypted data. |
| **CRYPT-M-002** | Encryption in Transit TLS 1.3+ | Critical | Per **CRYPT-M-002**: data in transit must use TLS 1.3 or higher, with weak ciphers and deprecated protocols disabled. |
| **DB-M-003** | Database Access Control & Least Privilege | High | Per **DB-M-003**: application accounts must have minimum permissions, administrative privileges must be role-limited, shared accounts are prohibited, and access must be audited and reviewed quarterly. |
| **DB-M-005** | Database Activity Monitoring and Audit Logging | High | Per **DB-M-005**: privileged actions, schema changes, authentication events, and sensitive-data access must be captured in tamper-resistant logs, forwarded to central monitoring or SIEM, retained, and monitored for anomalies. |
| **CRYPT-M-003** | Key Rotation & Lifecycle Management | High | Per **CRYPT-M-003**: key generation, rotation, revocation, and destruction must be documented and automated; static keys must rotate at least annually. |

### Other retrieved database and cryptography mandards

These may affect the wider database security assessment and should not be excluded without scoping:

| Mandard | Title | Risk |
|---|---|---:|
| **DB-M-001** | SQL Injection Prevention Parameterized Queries | Critical |
| **DB-M-004** | Database Security Hardening and Configuration | High |
| **DB-M-006** | Sensitive Data Masking and Fine-Grained Access | High |
| **CRYPT-M-004** | Algorithm Selection & Post-Quantum Readiness | High |
| **CRYPT-M-005** | Certificate Management & Pinning | High |
| **CRYPT-M-006** | Hardware Security Module for High-Value Keys | High |

## Framework mapping

Selected mappings returned by the Mandard catalogue:

| Mandard | Framework controls |
|---|---|
| **DB-M-002** | NIST SP 800-53 Rev.5: CM-6, SC-12, SC-13, SC-28; PCI DSS v4.0: Req 3, Req 4; ISO/IEC 27001:2022: A.8.24 |
| **CRYPT-M-001** | NIST SP 800-53 Rev.5: SC-12, SC-13, SC-28; PCI DSS v4.0: Req 3; ISO/IEC 27001:2022: A.8.24; HIPAA: 164.312(a)(2)(iv) |
| **CRYPT-M-002** | NIST SP 800-53 Rev.5: SC-12, SC-13, SC-7, AC-4; PCI DSS v4.0: Req 4; ISO/IEC 27001:2022: A.8.24, A.8.20, A.5.14; GDPR: Article 32 |
| **DB-M-003** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-6; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3 |
| **DB-M-005** | NIST SP 800-53 Rev.5: AU-2, AU-6, AU-12, SI-4; PCI DSS v4.0: Req 10; ISO/IEC 27001:2022: A.8.16 |
| **CRYPT-M-003** | NIST SP 800-53 Rev.5: SC-12, SC-13; PCI DSS v4.0: Req 3, Req 4; ISO/IEC 27001:2022: A.8.24; GDPR: Article 32 |

## Required actions

1. **Prove encryption at rest — Database/Cloud Platform Owner**
   - Export the live configuration showing TDE, storage encryption, or approved column-level encryption is enabled.
   - Record the algorithm, key identifier, key-management service, and coverage of primary databases, replicas, snapshots, exports, and backups.
   - Reconcile the database inventory against encryption status so omitted instances are visible.
   - Per **DB-M-002** and **CRYPT-M-001**, evidence must establish AES-256 or equivalent and separation of encryption keys from encrypted data.

2. **Prove encryption in transit — Database and Network Owners**
   - Export database server settings enforcing encrypted connections and rejecting plaintext sessions.
   - Run an independent TLS scan against each database endpoint and record negotiated protocol and cipher.
   - Perform a negative test demonstrating that TLS versions below 1.3 and non-TLS connections fail.
   - Per **DB-M-002** and **CRYPT-M-002**, the acceptance threshold is TLS 1.3+ with weak protocols and ciphers disabled.

3. **Prove key governance — Key Management Owner**
   - Export key metadata showing ownership, purpose, status, creation date, rotation policy, next rotation date, and separate storage in KMS, Key Vault, Vault, or an approved HSM.
   - Retain rotation-event logs and evidence that failed or overdue rotations generate alerts.
   - Per **CRYPT-M-003**, static keys must rotate at least annually and the complete lifecycle must be documented and automated.

4. **Prove least privilege — Database Owner and Identity Governance**
   - Export users, service accounts, groups, database roles, object grants, inherited privileges, and last-use information.
   - Demonstrate unique service identities by application and environment, absence of shared accounts, and no unnecessary owner, `CREATE`, `DROP`, `ALTER`, or equivalent administrative permissions.
   - Link every active account to an approved request, data owner, accountable owner, and business purpose.
   - Complete and retain quarterly access certification and removal evidence.
   - Per **DB-M-003**, effective permissions—not merely role definitions—must demonstrate least privilege.

5. **Prove monitoring — Database and SOC Owners**
   - Enable audit capture for authentication, privilege changes, privileged activity, schema changes, and access to sensitive data.
   - Demonstrate delivery to the SIEM, retention according to policy, tamper resistance, alert rules, and a successful test alert.
   - Per **DB-M-005**, local logging without central monitoring and anomaly alerting does not prove the full control.

Implementation guidance is provided by:

- `VeriFy-DATA-AM-001`, mapped to **AC-M-001**, **DB-M-003**, **DB-M-006**, **GOV-G-006**, **IAM-M-002**, and **IAM-M-004**. Its “Data Access Management Guardrails” section describes approved access-request paths, group-based access, DBA assignment of database permissions, data-owner approval, and IIQ/SailPoint review processes.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817601

- `VeriFy-AUTHZ-GEN-001`, mapped to **AC-M-001**, **DB-M-003**, **GOV-G-006**, **IAM-M-001**, **IAM-M-002**, **SECR-M-001**, and **SECR-M-004**. Its “General Authorization Guardrails” section calls for unique service accounts, least-privilege database roles, host restriction, access logging, privileged-access logging, Key Vault use, read-only analyst roles, and accountable service-account ownership.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766

- `VeriFy-DATA-GEN-003`, mapped to **CRYPT-M-002**, **DATA-M-001**, **DATA-M-002**, **DB-M-002**, **DB-M-004**, **DB-M-006**, and **GOV-G-006**. Its data-security section specifies encrypted database protocols and, for Azure, private endpoints, database encryption, AES-256, and Azure Key Vault.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947951

## Evidence for audit

| Control objective | Minimum persuasive evidence |
|---|---|
| Complete scope | Authoritative database inventory, data classification, environment, owner, endpoint, backup location, and encryption status |
| At-rest encryption | Timestamped API or database configuration export showing TDE/storage encryption; key ID and algorithm; backup, snapshot, replica, and export encryption evidence |
| In-transit encryption | Server configuration requiring TLS; independent scan output; successful TLS 1.3 connection; failed plaintext and pre-TLS-1.3 tests |
| Key separation and lifecycle | KMS/Key Vault inventory, access policy, rotation configuration, rotation logs, revocation/destruction procedure, and overdue-rotation alert |
| Least privilege | Effective grants query, role membership export, privileged-role list, service-account inventory, and evidence that application accounts lack administrative permissions |
| Approval and accountability | ServiceNow/IIQ/SailPoint request, data-owner approval, named account owner, business justification, and time limitation where applicable |
| Quarterly review | Signed access-certification report, reviewer identity, review date, exceptions, and evidence that revoked access was actually removed |
| Monitoring | Database audit configuration, sample authentication/DDL/privileged/sensitive-data events, SIEM ingestion record, retention setting, tamper protection, alert rule, and test-alert ticket |
| Deviations | Approved deviation in the SAF pack, technical justification, compensating controls, risk owner, expiry date, and remediation plan |

The strongest audit pack preserves raw machine-readable exports and query results, collection timestamps, database identifiers, evidence owner, and reviewer approval. Credentials, key material, and sensitive query results must be redacted without obscuring the control status.

## Assumptions and limits

No database environment, configuration, access list, TLS endpoint, KMS record, SIEM feed, or quarterly review was inspected; this answer defines the evidence needed rather than attesting that it exists. The catalogue output for some framework mappings was truncated, so the framework table contains only mappings explicitly returned and is not asserted to be exhaustive.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**CRYPT-M-003**](https://verify.example-org.internal/?id=CRYPT-M-003) | High | Cryptography | CIS_CONTROLS (CIS 3); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); +10 more |
| [**CRYPT-M-004**](https://verify.example-org.internal/?id=CRYPT-M-004) | High | Cryptography | CIS_CONTROLS (CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-005**](https://verify.example-org.internal/?id=CRYPT-M-005) | High | Cryptography | CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.13, A.8.14); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-006**](https://verify.example-org.internal/?id=CRYPT-M-006) | High | Cryptography | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04); CSA_CCM (CEK); CWE (CWE-327); DORA (Art. 17-23, Art. 24-27, Art. 28-44); GDPR (Article 32); +14 more |
| [**DATA-M-001**](https://verify.example-org.internal/?id=DATA-M-001) | Medium | Data Protection | AIUC1 (E005); CIS_CONTROLS (CIS 11, CIS 3, CIS 6); CWE (CWE-284, CWE-285, CWE-327); GDPR (Article 32); HIPAA (164.312(a)(1), 164.312(a)(2)(iv)); ISO_27001 (A.5.15, A.5.18, A.5.34); +9 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-001**](https://verify.example-org.internal/?id=DB-M-001) | Critical | Database Security | CIS_CONTROLS (CIS 16); CWE (CWE-77, CWE-89); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SI-10); NIST_SSDF (PW.5); +6 more |
| [**DB-M-002**](https://verify.example-org.internal/?id=DB-M-002) | Critical | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 16, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-327, CWE-798); GDPR (Article 17, Article 25, Article 32); HIPAA (164.312(a)(2)(iv), 164.502); +10 more |
| [**DB-M-003**](https://verify.example-org.internal/?id=DB-M-003) | High | Database Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**DB-M-004**](https://verify.example-org.internal/?id=DB-M-004) | High | Database Security | CIS_CONTROLS (CIS 12, CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-798); ISO_27001 (A.5.17, A.8.16, A.8.20); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, CM-6); +7 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**DB-M-006**](https://verify.example-org.internal/?id=DB-M-006) | High | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 17, CIS 3, CIS 6); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.502); +10 more |

Showing 15 of 20 cited mandards.

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