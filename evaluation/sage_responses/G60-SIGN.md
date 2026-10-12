# G60-SIGN

## Question
What digital-signature evidence is required for non-repudiable workflows?

## Sage response

## Bottom line

SAGF does not currently contain a dedicated Mandard defining the complete evidence package for a digital signature. The catalogue does require High-risk supporting controls for trusted timestamps, centralized tamper-resistant audit records, classification-based retention, and formal exceptions; for Highly Confidential and Confidential workflows, the implementation standard mandates encrypted, audited, read-only non-repudiation evidence retained for seven years. Approve a standard signature-evidence package as described below and raise a new Mandard to remove the current control gap.

## Risk and impact

The applicable supporting Mandards are all rated **High**. Without reliable identity attribution, document integrity, trusted event time, certificate status, and immutable workflow history, the organization may be unable to prove who signed what, when they signed it, or whether the record was subsequently altered.

This exposes the organization to disputed transactions, unenforceable approvals, fraud, failed investigations, and audit or regulatory findings.

## Governing mandards

| Mandard | Title | Risk | Relevance |
|---|---|---:|---|
| **DATA-M-002** | Data Classification & Handling | High | Requires declared sensitivity and classification-appropriate storage, transit, and retention controls. |
| **LOG-M-001** | Stream Logs to SIEM | High | Requires application logs to be streamed to a central SIEM endpoint. |
| **LOG-M-004** | Trusted Time Synchronization for Security Events | High | Requires approved time sources, UTC timestamps, synchronization monitoring, and rejection of unreliable timestamps as authoritative evidence. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Requires any departure to be independently approved, risk-owned, justified, compensated, and time-bounded. |
| **DB-M-005** | Database Activity Monitoring and Audit Logging | High | Applies where signature evidence is stored in a database; requires tamper-resistant monitoring of sensitive-data and privileged activity. |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High | Applies to CI/CD components supporting the workflow, including alerting on artifact-signature validation failures. |
| **MON-M-001** | Monitor for Config Drift | High | Applies to production configuration protecting signature validation, evidence storage, and logging. |

Per **DATA-M-002**: classify the workflow evidence and apply corresponding storage, transit, and retention rules.

Per **LOG-M-004**: timestamps cannot be treated as authoritative evidence when time synchronization is unreliable.

Per **LOG-M-001**: workflow audit events must be sent to centralized monitoring.

Per **GOV-G-006**: any omission or weakening of a mandated supporting control requires a formal, independently approved deviation before release.

## Framework mapping

The following directly relevant mappings were returned by the Mandard catalogue:

| Mandard | Framework | Control |
|---|---|---|
| **DATA-M-002** | NIST SP 800-53 Rev. 5 | SC-28 Protection of Information at Rest; SI-12 Information Management and Retention |
| **DATA-M-002** | ISO/IEC 27001:2022 | A.5.12 Classification of Information; A.5.13 Labelling of Information |
| **LOG-M-001** | NIST SP 800-53 Rev. 5 | AU-2 Event Logging; AU-6 Audit Record Review, Analysis, and Reporting; AU-12 Audit Record Generation |
| **LOG-M-001** | ISO/IEC 27001:2022 | A.8.15 Logging; A.5.28 Collection of Evidence |
| **LOG-M-004** | ISO/IEC 27001:2022 | A.8.17 Clock Synchronization |
| **DB-M-005** | NIST SP 800-53 Rev. 5 | AU-2 Event Logging; AU-12 Audit Record Generation; SI-7 Software, Firmware, and Information Integrity |
| **DB-M-005** | PCI DSS v4.0 | Requirement 10 Log and Monitor All Access |
| **GOV-G-006** | NIST SP 800-53 Rev. 5 | CA-5; PM-4; RA-3 Risk Assessment; PL-2 System Security and Privacy Plans |
| **GOV-G-006** | ISO/IEC 27001:2022 | A.5.1 Policies for Information Security; A.5.35 Independent Review of Information Security |

## Required actions

1. **Classify and retain the evidence.**  
   Per **DATA-M-002**, assign the workflow and evidence a data classification and enforce corresponding storage, encryption, access, transit, and retention controls. The applicable implementation standard mandates seven-year retention for Highly Confidential and Confidential records.

2. **Create an immutable workflow audit trail.**  
   Per **LOG-M-001**, forward security-relevant signature and approval events to the central SIEM. Where evidence is database-resident, apply **DB-M-005** so privileged actions, authentication, sensitive-data access, and changes are recorded in tamper-resistant logs.

3. **Use trustworthy event time.**  
   Per **LOG-M-004**, use approved redundant time sources, record unambiguous UTC timestamps, monitor synchronization state and offset, and prevent timestamps generated during material drift or synchronization loss from being accepted as authoritative evidence.

4. **Protect the evidence record.**  
   The implementation standard requires non-repudiation records for Highly Confidential and Confidential workflows to be encrypted, audited, and read-only.

5. **Govern exceptions before release.**  
   Per **GOV-G-006**, document any unavailable evidence component or weakened control, including justification, residual risk owner, compensating controls, independent approval, and expiry.

6. **Define the signature evidence packet.**  
   **Advisory (not catalogue-backed):** Because no dedicated digital-signature Mandard was found, retain the following as one logically bound evidence package:
   - Exact signed content, or its canonical representation.
   - Cryptographic digest and digest algorithm.
   - Signature value, signature format, and signature algorithm.
   - Signer identity and the authenticated account or credential used.
   - Evidence of signer intent and consent, including the action and disclosure shown.
   - Signing time and, where required, a trusted timestamp token.
   - Signer certificate and relevant certificate chain.
   - Certificate validity and revocation evidence captured at signing or validation time.
   - Signature-validation result, validation policy, software/version, and failure reason where applicable.
   - Workflow, transaction, document, and correlation identifiers.
   - Authentication and step-up authentication events associated with signing.
   - Before-and-after workflow state, approver role, and authorization decision.
   - Delivery, viewing, rejection, cancellation, retry, and completion events.
   - Evidence-store integrity protection, access history, export history, and retention/disposal status.

## Evidence for audit

Provide:

- The signed artefact and its detached or embedded digital signature.
- A signature-validation report showing content integrity and the validation outcome.
- Certificate chain and contemporaneous certificate-status evidence.
- Trusted-time configuration, synchronization-health report, and UTC event records.
- End-to-end transactional and administrative audit trail with correlation identifiers.
- SIEM ingestion proof and sample event searches.
- Read-only or immutable-storage configuration and access-control evidence.
- Data-classification record and approved retention configuration.
- For Highly Confidential or Confidential workflows, proof of seven-year archive retention.
- Any approved, unexpired deviation record required by **GOV-G-006**.

Implementation guidance source: **VeriFy-AUD-002**, mapped to **DATA-M-002**, **DB-M-005**, **GOV-G-006**, **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, and **MON-M-001** — [Audit Trails, Event & Log Management](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664). Section 2 requires end-to-end transactional and administrative audit trails and, for Highly Confidential and Confidential data, centralized logging, seven-year retention, and encrypted, audited, read-only non-repudiation controls.

## Assumptions and limits

No dedicated SAGF Mandard for digital-signature evidence was found. The exact signature-evidence fields above are advisory rather than catalogue requirements; legal enforceability, jurisdiction-specific electronic-signature requirements, approved certificate authorities, signature formats, and retention periods outside Highly Confidential and Confidential classifications were not verified. The implementation standard contains ambiguity because its overall classification row mandates non-repudiation while individual architectural-layer rows state that it is not mandated; this should be resolved through a dedicated Mandard or formal governance interpretation.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |

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