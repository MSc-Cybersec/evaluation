# G29-CLOUD

## Question
What cloud governance evidence is required before onboarding a new subscription?

## Sage response

## Bottom line

A new cloud subscription must not be approved for production use until ownership, risk, shared-responsibility, landing-zone, identity, exposure, logging, data-residency, and applicable recovery evidence is complete. The highest exposures are persistent credential compromise and unintended public access; onboarding should therefore be blocked automatically where **Critical** controls fail or where material exceptions lack documented, time-bound approval.

## Risk and impact

| Priority | Exposure if evidence is missing |
|---|---|
| **Critical** | Static or excessive cloud credentials can enable persistent compromise; unapproved public endpoints can expose data, administration interfaces, and workloads. |
| **High** | Unclear ownership, inconsistent landing-zone controls, missing telemetry, unsuitable regions, and untested recovery can create regulatory exposure, undetected compromise, data loss, and prolonged outages. |
| **Medium** | Missing portability evidence can create provider lock-in and prevent timely service or data recovery during an exit. |

## Governing mandards

The complete cloud domain contains the following mandards:

| Mandard | Title | Risk | Onboarding evidence required |
|---|---|---:|---|
| **CLOUD-M-001** | Cloud Governance and Shared Responsibility | High | Per **CLOUD-M-001**: documented provider/customer responsibility model, named business and technical owners, approved risk assessment, reviewed security obligations, and residual-risk approval before production deployment. |
| **CLOUD-M-002** | Secure Cloud Landing Zone Baseline | High | Per **CLOUD-M-002**: proof that the subscription was provisioned through an approved landing zone enforcing centralized identity, networking, logging, encryption, tagging, and policy baselines. Material exceptions must be approved and time-bound. |
| **CLOUD-M-003** | Cloud Workload Identity and Federation | Critical | Per **CLOUD-M-003**: evidence of federated, short-lived workload and pipeline identities with least-privilege roles; no long-lived access keys or shared service accounts unless formally excepted. |
| **CLOUD-M-004** | Cloud Public Exposure Management | Critical | Per **CLOUD-M-004**: deny-by-default internet exposure and an inventory of approved public endpoints showing justification, owner, data classification, access controls, and compensating controls. |
| **CLOUD-M-005** | Cloud Logging, Detection and Response | High | Per **CLOUD-M-005**: proof that control-plane, identity, network, and data-access logs are centrally collected, protected from alteration, monitored, and integrated with incident response. |
| **CLOUD-M-006** | Cloud Resilience, Backup and Recovery | High | Per **CLOUD-M-006**: for business-critical workloads, approved RTO/RPO, protected backup configuration, documented restore procedures, and completed restore-test evidence. |
| **CLOUD-M-007** | Cloud Data Residency and Sovereignty | High | Per **CLOUD-M-007**: data classification, approved service and region, cross-border transfer safeguards, encryption requirements, and deletion obligations before regulated or restricted data is processed. |
| **CLOUD-M-008** | SaaS Approval, Configuration and Supplier Governance | High | Per **CLOUD-M-008**: where the onboarding is SaaS, supplier-risk approval, approved security configuration, SSO/MFA, access and data-handling review, contractual obligations, and exit/data-deletion arrangements. |
| **CLOUD-M-009** | Cloud Service Interoperability and Portability Assurance | Medium | Per **CLOUD-M-009**: for services storing business data or delivering material capabilities, a tested export and exit design covering data, metadata, identity, configuration, non-portable dependencies, integrity, and recovery objectives. |

## Framework mapping

The following are direct catalogue mappings relevant to the onboarding gate:

| Mandard | Framework controls returned by the catalogue |
|---|---|
| **CLOUD-M-001** | NIST SP 800-53 Rev.5: CM-2, CM-6, CA-9, PL-2, PL-8, PM-9, SC-7; ISO/IEC 27001:2022: A.5.23, A.8.9, A.8.27; NIST CSF 2.0: GV.OC-01, GV.RM-01, PR.IR-01, PR.PS-01 |
| **CLOUD-M-002** | NIST SP 800-53 Rev.5: CM-2, CM-6, AC-4, AU-2, AU-6, AU-12, SC-7, SC-12, SC-13, SC-28, SI-4 |
| **CLOUD-M-003** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-6, IA-2, IA-4, IA-5, IA-8; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3 |
| **CLOUD-M-004** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, AU-6, SC-7, SI-4; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3, A.8.16 |
| **CLOUD-M-005** | NIST SP 800-53 Rev.5: AU-2, AU-6, AU-12, SI-4, IR-4, IR-6; PCI DSS v4.0: Req 10 |
| **CLOUD-M-006** | NIST SP 800-53 Rev.5: CP-9, CP-10; ISO/IEC 27001:2022: A.8.13, A.8.14, A.5.29, A.5.30; SOC 2: A1.2 |
| **CLOUD-M-007** | GDPR: Articles 32 and 44; PCI DSS v4.0: Req 3 and Req 4; ISO/IEC 27001:2022: A.5.31, A.5.34, A.8.24 |
| **CLOUD-M-008** | ISO/IEC 27001:2022: A.5.22, A.5.23; GDPR: Article 28 |
| **CLOUD-M-009** | CSA Cloud Controls Matrix v4: IPY, Interoperability and Portability |

## Required actions

1. **Cloud Platform and IAM teams — close Critical gates**
   - Configure enterprise federation and least-privilege roles.
   - Demonstrate that no unapproved static cloud keys or shared service accounts exist.
   - Enforce deny-by-default public access.
   - Register and approve every required public endpoint.

2. **Cloud Platform team — provision through the approved landing zone**
   - Attach the subscription to the approved management hierarchy.
   - Apply centralized identity, network, encryption, diagnostic, tagging, and policy controls.
   - Retain the Infrastructure-as-Code deployment and policy evaluation results.
   - Do not manually create production subscriptions outside this process.

3. **Business owner, technical owner, and Risk/BISO — complete governance**
   - Record the business purpose, service criticality, data classification, owners, review date, and shared-responsibility allocation.
   - Complete the risk assessment and approve residual risks.
   - Record all deviations with technical justification, compensating controls, owner, expiry date, and approval.

4. **Security Operations — verify monitoring**
   - Confirm delivery of control-plane, identity, network, and applicable data-access logs to the central security platform.
   - Confirm protection against alteration and the presence of alerting and incident-response integration.

5. **Data owner, Privacy, and Legal — approve data location**
   - Confirm permitted regions and services against the data classification.
   - Document encryption, retention, deletion, and cross-border transfer obligations.
   - Apply technical region restrictions before data is introduced.

6. **Service owner and Business Continuity — address resilience**
   - For business-critical use, approve RTO and RPO.
   - Configure protected backups and complete a recorded restore test.

7. **Service owner — address portability**
   - For a material service, document exportable data, metadata, identity, and configuration.
   - Record non-portable dependencies and demonstrate export or reconstruction through a test.

**Implementation guidance from the knowledge corpus:**  
**VeriFy-APP-002**, mapped to **ASSURE-M-001**, **CLOUD-M-007**, **CRYPT-M-001**, **DATA-M-002**, **GOV-G-006**, **OAUTH-M-001**, and **SUPPLY-M-001** — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782).

Its “Application Governance Guardrails” section requires, as organisational implementation guidance:

- SAF approval and Alfabet onboarding.
- For externally hosted IaaS/PaaS or SaaS: hosting-jurisdiction confirmation, Cloud Materiality Assessment, third-party and cybersecurity assessments, data-risk assessment, and applicable legal/privacy agreements.
- Applicable supplier assurance and independent security or penetration-test attestations.
- Data-destruction terms and backup encryption.
- Any non-compliance must be documented as a deviation in the SAF pack with technical justification.

These are knowledge-document procedures, not themselves mandard requirements.

## Evidence for audit

The onboarding record should contain:

- Approved subscription or service request with named business and technical owners.
- Shared-responsibility matrix and current review date.
- Approved risk assessment and residual-risk decision.
- Landing-zone pipeline execution record and Infrastructure-as-Code version.
- Policy-compliance export showing management hierarchy, required tags, network controls, encryption, diagnostics, and permitted regions.
- IAM role inventory, federation configuration, privileged-access approval, and static-key scan.
- Public-exposure scan and approval record for each permitted endpoint.
- Central logging configuration, sample log-ingestion evidence, alert test, and incident-routing record.
- Data-classification and residency decision, including transfer and deletion approvals where applicable.
- RTO/RPO approval, backup-policy status, and latest restore-test report where the workload is business-critical.
- Portability design and latest export/reconstruction test where the service is material.
- SAF approval, Alfabet record, and applicable supplier/legal/security assessments.
- Approved, time-bound exception records for every unmet baseline requirement.

## Assumptions and limits

The cloud provider, production date, data classification, workload criticality, and whether the request concerns an infrastructure subscription or SaaS tenant were not specified. **CLOUD-M-006**, **CLOUD-M-008**, and **CLOUD-M-009** therefore apply conditionally as described above. No knowledge document specifically dedicated to a “new subscription onboarding checklist” was found; the cited application-governance standard is the closest retrieved organisational procedure.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ASSURE-M-001**](https://verify.example-org.internal/?id=ASSURE-M-001) | High | Independent Assurance | AIUC1 (B001, C010, C011); CIS_CONTROLS (CIS 18); ISO_27001 (A.5.35); ISO_27034 (ASMP.5); NIST_800_82 (5.2.1); NIST_CSF (GV.OV, GV.OV-01, GV.OV-03); +4 more |
| [**CLOUD-M-001**](https://verify.example-org.internal/?id=CLOUD-M-001) | High | Cloud Security | CIS_CONTROLS (CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.23, A.8.27, A.8.9); NIST_CSF (GV.OC-01, GV.RM-01, PR.IR-01); NIST_SP_800_53 (CA-9, CM-2, CM-6); +3 more |
| [**CLOUD-M-002**](https://verify.example-org.internal/?id=CLOUD-M-002) | High | Cloud Security | CIS_CONTROLS (CIS 12, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv), 164.312(b)); +13 more |
| [**CLOUD-M-003**](https://verify.example-org.internal/?id=CLOUD-M-003) | Critical | Cloud Security | CIS_CONTROLS (CIS 4, CIS 5, CIS 6); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +8 more |
| [**CLOUD-M-004**](https://verify.example-org.internal/?id=CLOUD-M-004) | Critical | Cloud Security | CIS_CONTROLS (CIS 4, CIS 6, CIS 8); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.16); +9 more |
| [**CLOUD-M-005**](https://verify.example-org.internal/?id=CLOUD-M-005) | High | Cloud Security | CIS_CONTROLS (CIS 12, CIS 13, CIS 17); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security, LOG); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.18, A.5.24); +9 more |
| [**CLOUD-M-006**](https://verify.example-org.internal/?id=CLOUD-M-006) | High | Cloud Security | CIS_CONTROLS (CIS 11, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (BCR, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ENISA_SMLA (SMLA-29); ISA_62443 (SR 7); ISO_27001 (A.5.19, A.5.21, A.5.29); +10 more |
| [**CLOUD-M-007**](https://verify.example-org.internal/?id=CLOUD-M-007) | High | Cloud Security | AIUC1 (E005, E011); CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32, Article 44); +11 more |
| [**CLOUD-M-008**](https://verify.example-org.internal/?id=CLOUD-M-008) | High | Cloud Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ENISA_SMLA (SMLA-20); +7 more |
| [**CLOUD-M-009**](https://verify.example-org.internal/?id=CLOUD-M-009) | Medium | Cloud Security | CSA_CCM (IPY) |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**SUPPLY-M-001**](https://verify.example-org.internal/?id=SUPPLY-M-001) | High | Supply Chain Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (STA); ENISA_SMLA (SMLA-20, SMLA-22); +18 more |

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