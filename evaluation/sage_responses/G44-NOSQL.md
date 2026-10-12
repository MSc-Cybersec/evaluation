# G44-NOSQL

## Question
What security controls are mandatory for production NoSQL data stores?

## Sage response

## Bottom line

Production NoSQL data stores must implement the NoSQL-specific injection control and the broader database controls for encryption, least privilege, hardening, audit monitoring, and sensitive-data protection. Production deployment should be blocked where any Critical control is unmet; High-risk exceptions require formal, independently approved, time-bounded deviations.

## Risk and impact

| Priority | Exposure if unaddressed |
|---|---|
| Critical | NoSQL injection, complete database disclosure, exposed credentials, or compromise through unrestricted cloud identities |
| High | Excessive access, exploitable default or unpatched configurations, undetected data exfiltration, exposed regulated data, inadequate backup protection, and lateral movement |
| Governance | Undocumented exceptions become permanent, unowned security risk |

The catalogue contains one dedicated NoSQL Mandard, **NOSQL-M-001**. The technology-neutral database Mandards **DB-M-002** through **DB-M-006** also apply to NoSQL implementations where the datastore provides the relevant capability.

## Governing mandards

### Mandatory baseline

| Mandard | Title | Risk | Mandatory requirement |
|---|---|---:|---|
| **NOSQL-M-001** | NoSQL Injection Prevention | Critical | Per **NOSQL-M-001**: use parameterized queries or injection-safe query builders; never concatenate user input; validate against schema; allowlist database operations; disable database-side JavaScript when unnecessary. |
| **DB-M-002** | Database Encryption At-Rest & In-Transit | Critical | Per **DB-M-002**: encrypt database data at rest using AES-256 with FIPS 140-2-approved keys, require TLS 1.3 or later for connections, and apply database- or field-level encryption to sensitive data. |
| **SECR-M-001** | No Hardcoded Secrets | Critical | Per **SECR-M-001**: fail the build when high-confidence database passwords, connection strings, or other secrets are detected in source or configuration. Remove and invalidate exposed secrets and use an approved vault. |
| **IAM-M-001** | Least-Privilege IAM Policies | Critical | Per **IAM-M-001**: production IAM roles must use least privilege; wildcard actions and resources are prohibited. |
| **DB-M-003** | Database Access Control & Least Privilege | High | Per **DB-M-003**: use minimally privileged, application-specific accounts; prohibit shared accounts; restrict administrative roles; audit access and review it quarterly. |
| **DB-M-004** | Database Security Hardening and Configuration | High | Per **DB-M-004**: remove or disable default and unused accounts, change default credentials, disable unnecessary features and interfaces, apply a secure baseline, monitor drift, and run supported, patched versions. |
| **DB-M-005** | Database Activity Monitoring and Audit Logging | High | Per **DB-M-005**: record privileged operations, schema changes, authentication events, and sensitive-data access in tamper-resistant logs; forward them to central monitoring or SIEM and alert on anomalies. |
| **DB-M-006** | Sensitive Data Masking and Fine-Grained Access | High | Per **DB-M-006**: restrict sensitive data using row- and column-level controls, mask or tokenize it for non-privileged users and non-production environments, and periodically review regulated-data access. |
| **BACKUP-M-001** | Encrypted Backups & Retention | High | The catalogue search identified this Mandard as applicable to database backup and recovery. Detailed requirements were not retrieved, so retention periods and recovery-testing conditions must be confirmed from the Mandard before release. |
| **NSEG-M-002** | DMZ & Network Segmentation | High | The catalogue search identified this Mandard for database network segmentation and public exposure. Detailed network conditions were not retrieved and must be confirmed before release. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: record every control departure before release with justification, residual-risk owner, compensating controls, independent approval, and an expiry date. |

The DB domain lookup also returned **DB-M-001**, SQL Injection Prevention — *Critical*. It is SQL-specific and is not a substitute for the NoSQL requirement in **NOSQL-M-001**.

### Platform guidance for MongoDB

Knowledge document **VeriFy-AUTH-INT-DB-MDB-001**, [6.1.2.5 MongoDB](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/771686766), is mapped to **DB-M-002**, **DB-M-003**, **DB-M-004**, **GOV-G-006**, **IAM-M-001**, and **SECR-M-001**.

Its MongoDB guardrail specifies:

- Preferred Azure application and tooling access uses OIDC with Entra ID.
- Azure Workload Identity federation is the first preference.
- Managed Identity integration is used where supported.
- SCRAM local database accounts are documented as the alternative.
- Less-preferred patterns require technical motivation; deviations must be documented in the architecture artefact.

This is implementation guidance, not a replacement for the cited Mandards. The document’s purpose text refers to PostgreSQL while its scope and guardrails identify MongoDB; that drafting inconsistency should be clarified with the document owner.

## Framework mapping

The following are representative mappings returned directly with the cited Mandards:

| Mandard | Returned framework mappings |
|---|---|
| **NOSQL-M-001** | NIST SP 800-53 SI-10, SI-15, SA-11; PCI DSS v4.0 Req 6; ISO/IEC 27001:2022 A.8.26, A.8.28; OWASP ASVS 5.0 V1, V13; OWASP Top 10:2025 A02, A05; CIS Controls v8 CIS 16 |
| **DB-M-002** | NIST SP 800-53 SC-12, SC-13, SC-28; PCI DSS v4.0 Req 3, Req 4; ISO/IEC 27001:2022 A.8.24 |
| **DB-M-003** | NIST SP 800-53 AC-2, AC-3, AC-6; PCI DSS v4.0 Req 7; ISO/IEC 27001:2022 A.5.15, A.5.18, A.8.2, A.8.3 |
| **DB-M-004** | NIST SP 800-53 CM-6, SC-7; PCI DSS v4.0 Req 1, Req 2, Req 6; ISO/IEC 27001:2022 A.8.20, A.8.22 |
| **DB-M-005** | NIST SP 800-53 AU-2, AU-6, AU-12, SI-4; PCI DSS v4.0 Req 10; ISO/IEC 27001:2022 A.8.16 |
| **DB-M-006** | NIST SP 800-53 AC-2, AC-3, AC-6, SC-28; PCI DSS v4.0 Req 7; ISO/IEC 27001:2022 A.5.15, A.5.18, A.8.3 |
| **IAM-M-001** | NIST SP 800-53 AC-2, AC-3, AC-6; PCI DSS v4.0 Req 7; ISO/IEC 27001:2022 A.5.15, A.5.16, A.5.18 |
| **GOV-G-006** | NIST SP 800-53 CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022 A.5.1, A.5.35; SOC 2 CC3, CC5; COBIT 2019 APO12.01, MEA02 |

No framework mappings are asserted here for **BACKUP-M-001** or **NSEG-M-002**, because their detailed records were not retrieved.

## Required actions

1. **Application engineering — prevent NoSQL injection**
   - Use driver-supported typed parameters, safe query builders, or strict ODM schemas.
   - Reject request objects where scalar values are expected; do not pass request JSON directly into query filters.
   - Allowlist fields and permitted operators.
   - Disable server-side JavaScript if it is not required.
   - Add SAST and active injection testing as release gates.

2. **Database/platform engineering — encrypt all data paths**
   - Enable encryption for primary storage, replicas, snapshots, and backups.
   - Enforce TLS 1.3 or later and reject plaintext database connections.
   - Apply field-level encryption or equivalent protection to PII and secrets.
   - Manage encryption keys through an approved key-management service.

3. **IAM and database owners — enforce distinct, least-privileged identities**
   - Create a separate identity for each application or workload.
   - Remove shared and unused accounts.
   - Separate application, operational, and administrative roles.
   - Prohibit production IAM wildcards and conduct quarterly access reviews.
   - For Azure MongoDB, follow the mapped guidance preference for OIDC with Entra ID and Workload Identity or Managed Identity.

4. **Platform engineering — harden and isolate the service**
   - Remove defaults and disable unused services, interfaces, scripting engines, and features.
   - Apply an approved vendor or CIS-aligned baseline and continuously detect drift.
   - Use a supported, patched database version.
   - Confirm the detailed requirements of **NSEG-M-002** and enforce them before production release.

5. **Security operations — enable database audit monitoring**
   - Capture authentication, authorization changes, privileged actions, schema changes, and access to sensitive collections or fields.
   - Forward logs to the SIEM using tamper-resistant storage.
   - Alert on failed authentication, unusual administrative activity, bulk reads, permission changes, and anomalous export behavior.

6. **Data owner — protect sensitive records**
   - Apply document-, field-, tenant-, or collection-level authorization as supported.
   - Mask or tokenize regulated fields for non-privileged consumers.
   - Do not copy unmasked production data into non-production environments.

7. **Resilience owner — protect backups**
   - Implement **BACKUP-M-001** after retrieving its detailed encryption and retention criteria.
   - Do not assume that storage-level encryption of the primary database automatically covers exports, snapshots, or backup copies.

8. **Risk owner — govern exceptions**
   - Block release for unmet Critical controls.
   - Where a control cannot be met, create an approved deviation under **GOV-G-006** before release.

## Evidence for audit

| Control area | Minimum audit artefact |
|---|---|
| NoSQL injection | Passing SAST result, injection test report, schema-validation tests, and code-review approval |
| Encryption | Configuration export showing storage encryption, key reference, TLS policy, and failed plaintext-connection test |
| Secrets | Passing secret-scanning pipeline gate and vault configuration; rotation record for any exposed credential |
| Access control | Role and privilege export, named workload identities, quarterly access-review record, and evidence that shared accounts are absent |
| Hardening | Baseline assessment, configuration-drift report, patch/version inventory, and disabled-feature configuration |
| Monitoring | Database audit configuration, SIEM ingestion evidence, sample events, alert rules, and alert test results |
| Sensitive data | Data classification, field-level policy or masking configuration, and positive and negative authorization tests |
| Backup | Backup configuration, encryption evidence, retention configuration, and evidence required by **BACKUP-M-001** once confirmed |
| Segmentation | Network rule or private-endpoint configuration and connectivity test required by **NSEG-M-002** once confirmed |
| Exceptions | Approved, unexpired deviation record containing owner, justification, compensating controls, residual risk, and expiry |

## Assumptions and limits

- The datastore product, hosting model, data classification, and jurisdiction were not specified.
- Detailed records for **BACKUP-M-001** and **NSEG-M-002** were not retrieved; only their IDs, titles, and High risk levels were verified.
- The returned MongoDB guidance applies specifically to MongoDB in the documented on-premises and Azure contexts. Equivalent platform guidance was not established for Cassandra, DynamoDB, Cosmos DB, Couchbase, Redis, or other NoSQL technologies.
- Authentication search results also returned **AUTH-M-001** through **AUTH-M-004**. They were not classified as datastore-specific requirements here because the retrieved evidence did not establish their direct applicability to production NoSQL database connections.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AUTH-M-001**](https://verify.example-org.internal/?id=AUTH-M-001) | Critical | Authentication | CIS_CONTROLS (CIS 17, CIS 5, CIS 6); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-287, CWE-798); GDPR (Article 7); ISO_27001 (A.5.16, A.5.17, A.5.24); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**AUTH-M-004**](https://verify.example-org.internal/?id=AUTH-M-004) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.8.24); MITRE_ATT&CK (M1027, M1032, M1036); NIST_CSF (PR.AA-01, PR.AA-05); +7 more |
| [**BACKUP-M-001**](https://verify.example-org.internal/?id=BACKUP-M-001) | High | Backup & Recovery | CCPA_CPRA (Storage Limitation); CIS_CONTROLS (CIS 11, CIS 3); COBIT_2019 (DSS04); CSA_CCM (BCR); CWE (CWE-327); ENISA_SMLA (SMLA-29); +13 more |
| [**DB-M-001**](https://verify.example-org.internal/?id=DB-M-001) | Critical | Database Security | CIS_CONTROLS (CIS 16); CWE (CWE-77, CWE-89); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SI-10); NIST_SSDF (PW.5); +6 more |
| [**DB-M-002**](https://verify.example-org.internal/?id=DB-M-002) | Critical | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 16, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-327, CWE-798); GDPR (Article 17, Article 25, Article 32); HIPAA (164.312(a)(2)(iv), 164.502); +10 more |
| [**DB-M-003**](https://verify.example-org.internal/?id=DB-M-003) | High | Database Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**DB-M-004**](https://verify.example-org.internal/?id=DB-M-004) | High | Database Security | CIS_CONTROLS (CIS 12, CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-798); ISO_27001 (A.5.17, A.8.16, A.8.20); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, CM-6); +7 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**DB-M-006**](https://verify.example-org.internal/?id=DB-M-006) | High | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 17, CIS 3, CIS 6); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.502); +10 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**NOSQL-M-001**](https://verify.example-org.internal/?id=NOSQL-M-001) | Critical | NoSQL Security | CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-77, CWE-89); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (SA-11, SI-10, SI-15); OWASP (A02:2025, A05:2025); +5 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |

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