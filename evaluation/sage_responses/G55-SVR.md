# G55-SVR

## Question
What server hardening baseline is mandatory before production release?

## Sage response

## Bottom line

Before production release, servers must comply with the **System / Infrastructure Layer baseline**, including CIS security hardening, patching, privileged-access controls, endpoint/runtime protection, asset registration, vulnerability management, and operational readiness. For cloud-hosted servers, **CSPM-M-001** explicitly requires continuous assessment against CIS Benchmarks or an equivalent baseline; production activation must also satisfy **PROV-M-002**. Release must be blocked where these controls are unmet unless an approved, unexpired deviation exists under **GOV-G-006**.

## Risk and impact

The highest exposure is privileged account compromise: **IAM-M-002** is Critical and requires MFA for every privileged or administrative account. High-risk exposures include insecure configuration, uncontrolled deployment, unbrokered administrative access, configuration drift, unmanaged endpoints, data exfiltration, and insecure maintenance.

An unhardened release can expose production data, credentials, management interfaces, service availability, and recovery capability. The catalogue does not specify one universal CIS profile, benchmark version, or passing score for every server technology; the applicable approved platform build pattern must therefore be identified before approval.

## Governing mandards

| Mandard | Title | Risk | Production requirement |
|---|---|---:|---|
| **IAM-M-002** | Enforce MFA for Privileged Accounts | Critical | Per **IAM-M-002**: MFA must be enforced for all privileged and administrative accounts. |
| **PROV-M-002** | Secure Application Provisioning and Operational Readiness | High | Per **PROV-M-002**: production promotion must use approved, repeatable, access-controlled deployment and demonstrate monitoring, alerting, backup, recovery, rollback, ownership, configuration and secret delivery, capacity assumptions, and incident readiness. |
| **PROV-M-003** | Secure Software Maintenance and Remote Servicing | High | Per **PROV-M-003**: maintenance must be approved, tested, traceable, use trusted artifacts, preserve or improve the security baseline, support rollback, and undergo post-change verification. |
| **RUNTIME-M-002** | Managed Endpoint and Secure Client Protection | High | Per **RUNTIME-M-002**: endpoints used to administer production must be managed and compliant; access from unmanaged or materially non-compliant endpoints must be denied or formally excepted. |
| **DLP-M-001** | Data Loss Prevention Controls | High | Per **DLP-M-001**: where applicable, DLP must detect and prevent unauthorized exfiltration of sensitive data. |
| **CSPM-M-001** | Cloud Configuration Compliance (CIS Benchmarks) | High | Per **CSPM-M-001**: cloud infrastructure must be continuously scanned against CIS Benchmarks or equivalent; Critical findings must be remediated within seven days. |
| **MON-M-001** | Monitor for Config Drift | High | Per **MON-M-001**: active monitoring must alert on unauthorized production configuration changes. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: any departure must be approved before release, independently authorized, risk-owned, compensated, documented, and time-bound. |
| **IAM-M-005** | Brokered Administrative Access | High | Per **IAM-M-005**: production administration must use a hardened bastion, jump service, or just-in-time broker; direct management access must be denied, MFA enforced, and sessions logged. |
| **RUNTIME-M-001** | Runtime Protection / EDR | Medium | Per **RUNTIME-M-001**: production hosts and containers must have host-level EDR or runtime protection enabled and reporting. |

The implementation standard identifies the broader infrastructure baseline as covering deployment, domain management, authentication, service accounts, secure access through MFA and jump boxes, patch management, endpoint security, DLP, CIS hardening, CMDB/asset management, and vulnerability management. Source: **VeriFy-INF-002**, mapped to **CSPM-M-001**, **DLP-M-001**, **GOV-G-006**, **IAM-M-002**, **IAM-M-005**, **MON-M-001**, **PROV-M-002**, **PROV-M-003**, **RUNTIME-M-001**, and **RUNTIME-M-002** — [System / Infrastructure Layer](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658243766).

## Framework mapping

Only directly tool-returned mappings are shown.

| Mandard | Framework mappings |
|---|---|
| **IAM-M-002** | NIST SP 800-53: IA-2, IA-5, AC-2, AC-3, AC-6, AC-7; PCI DSS v4.0: Requirements 7 and 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 |
| **PROV-M-002** | ISO/IEC 27034: ASMP.4 |
| **PROV-M-003** | NIST SP 800-53 Rev. 5: MA; NIST SP 800-82r3: 6.2.5 |
| **RUNTIME-M-002** | ISO/IEC 27001:2022: A.8.1; CIS Controls v8: CIS 9; CSA CCM v4: UEM |
| **DLP-M-001** | NIST SP 800-53: AC-2, AC-3, AC-4, AC-6, SC-28, SI-4; PCI DSS v4.0: Requirements 1, 3 and 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3, A.8.24 |
| **CSPM-M-001** | NIST SP 800-53: CM-2, CM-6, SI-4, AU-6; PCI DSS: Requirement 2; ISO/IEC 27001:2022: A.8.9, A.8.16, A.8.27 |
| **MON-M-001** | NIST SP 800-53: CM-2, SI-4, SI-7, AU-6 |
| **GOV-G-006** | NIST SP 800-53: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |
| **IAM-M-005** | NIST SP 800-53: AC-2, AC-6, AC-17, IA-2, AU-2; ISO/IEC 27001:2022: A.8.2, A.8.20; CIS Controls v8: CIS 5, CIS 6, CIS 12 |
| **RUNTIME-M-001** | NIST SP 800-53: SI-4, AU-6, SI-7, CM-2, CM-7, SC-7; PCI DSS: Requirement 5; ISO/IEC 27001:2022: A.8.7, A.8.9, A.8.16, A.8.27; CIS Controls v8: CIS 4, CIS 8, CIS 10 |

## Required actions

1. **Platform/Infrastructure owner:** Apply the approved server-specific CIS or equivalent build pattern and run a compliance scan. For cloud infrastructure, enable continuous CSPM assessment per **CSPM-M-001**.
2. **Identity owner:** Enforce MFA for every privileged account per **IAM-M-002**.
3. **Infrastructure and IAM owners:** Deny direct SSH, RDP, and equivalent administrative access from user networks or the internet. Route access through a hardened bastion or just-in-time broker and log sessions per **IAM-M-005**.
4. **Release owner:** Gate production activation on the operational-readiness record required by **PROV-M-002**, including tested rollback and restore, monitoring, alerting, support ownership, incident runbooks, and controlled configuration and secret delivery.
5. **Endpoint/SOC owner:** Confirm production hosts or containers have EDR/runtime protection installed, healthy, and reporting per **RUNTIME-M-001**. Confirm administrator endpoints comply with **RUNTIME-M-002**.
6. **Operations owner:** Complete patching, vulnerability management, CMDB/asset registration, and the other infrastructure controls identified by **VeriFy-INF-002** — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658243766).
7. **Cloud/SOC owner:** Enable configuration-drift detection and alert routing per **MON-M-001**.
8. **Data owner:** Where sensitive data is processed, configure and test applicable DLP controls per **DLP-M-001**.
9. **Risk owner and independent approver:** Record any unresolved departure under **GOV-G-006** before release. The record must include justification, residual risk, owner, compensating controls, independent approval, and expiry.

## Evidence for audit

The release assurance pack should contain:

- Dated CIS or equivalent hardening scan identifying the host/image, benchmark, profile, version, score, and findings.
- CSPM dashboard or exported report showing cloud resources are continuously assessed.
- Critical-finding remediation records, including evidence that the **CSPM-M-001** seven-day deadline was met.
- Privileged-account MFA compliance report.
- Firewall or security-group evidence denying direct access to management interfaces.
- Bastion or just-in-time access configuration and sample privileged-session logs.
- EDR/runtime agent inventory and current heartbeat status.
- Patch and vulnerability scan results.
- CMDB/asset record for each production server.
- Configuration-drift monitoring policy and alert-routing test.
- Completed operational-readiness record with backup, restore and rollback test results.
- Approved and unexpired deviation records for any failed or overridden control.

## Assumptions and limits

The catalogue establishes CIS hardening explicitly for cloud infrastructure, while **VeriFy-INF-002** applies CIS security hardening across on-premises and Azure workloads. It does not identify the mandatory operating-system-specific CIS benchmark version, profile level, tailoring decisions, or minimum passing score; those details reside in referenced Level 3 InfoSec Build Patterns, which were not available in the retrieved document. Release teams must obtain the applicable approved build pattern rather than selecting a benchmark profile independently.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**CSPM-M-001**](https://verify.example-org.internal/?id=CSPM-M-001) | High | Cloud Security Posture | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, BAI10, DSS02.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**DLP-M-001**](https://verify.example-org.internal/?id=DLP-M-001) | High | Data Loss Prevention | AIUC1 (A004, A006); CCPA_CPRA (Data Minimization, Reasonable Security Procedures, Right to Limit Sensitive Personal Information); CIS_CONTROLS (CIS 12, CIS 3, CIS 6); COBIT_2019 (APO14, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285); GDPR (Article 25, Article 32, Article 5); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**PROV-M-002**](https://verify.example-org.internal/?id=PROV-M-002) | High | Provisioning | ISO_27034 (ASMP.4) |
| [**PROV-M-003**](https://verify.example-org.internal/?id=PROV-M-003) | High | Provisioning | NIST_800_82 (6.2.5); NIST_SP_800_53 (MA) |
| [**RUNTIME-M-001**](https://verify.example-org.internal/?id=RUNTIME-M-001) | Medium | Runtime Protection | CIS_CONTROLS (CIS 10, CIS 4, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (IVS: Infrastructure & Virtualization Security); ENISA_SMLA (SMLA-18); ISO_27001 (A.8.16, A.8.27, A.8.7); MITRE_ATT&CK (M1025, M1040, M1049); +9 more |
| [**RUNTIME-M-002**](https://verify.example-org.internal/?id=RUNTIME-M-002) | High | Runtime Protection | CIS_CONTROLS (CIS 9); CSA_CCM (UEM); ISO_27001 (A.8.1); MITRE_ATT&CK (M1021, M1040, M1049) |

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