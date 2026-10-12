# G24-DLP

## Question
What controls should trigger DLP incident escalation for source repositories?

## Sage response

## Bottom line

Per **DLP-M-001**, source repositories must detect and either block or alert on suspected unauthorized exfiltration of sensitive data. Escalate immediately when sensitive data or a usable secret is exposed outside an approved boundary, when repository controls are bypassed, or when suspicious bulk extraction indicates likely exfiltration. The catalogue does not prescribe repository-specific severity thresholds or response SLAs; the trigger matrix below is **Advisory (not catalogue-backed)** and should be approved by the incident response and data-owner functions.

## Risk and impact

**High risk.** Unaddressed repository DLP events can expose customer or regulated data, credentials, proprietary source code, signing material, infrastructure configuration, and intellectual property. Repository history, forks, build logs, pull requests, issues, releases, and cached clones can preserve exposed information after the original file is deleted.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **DLP-M-001** | Data Loss Prevention Controls | High | Per **DLP-M-001**: where applicable, configure DLP controls to detect and prevent unauthorized exfiltration of sensitive data; policies must block or alert on suspected exfiltration attempts. |

## Framework mapping

Mappings returned for **DLP-M-001** include:

| Framework | Controls |
|---|---|
| NIST SP 800-53 Rev. 5 | AC-2 Account Management; AC-3 Access Enforcement; AC-4 Information Flow Enforcement; AC-6 Least Privilege; AU-6 Audit Record Review, Analysis, and Reporting; MP-4 Media Storage; PT-3 PII Processing Purposes; PT-5 Privacy Notice; SC-5 Denial-of-Service Protection; SC-7 Boundary Protection; SC-28 Protection of Information at Rest; SI-4 System Monitoring; SI-12 Information Management and Retention |
| PCI DSS v4.0 | Requirement 1 Network Security Controls; Requirement 3 Protect Stored Account Data; Requirement 7 Restrict Access by Business Need to Know |
| ISO/IEC 27001:2022 Annex A | A.5.15 Access control; A.5.18 Access rights; A.5.34 Privacy and protection of PII; A.8.2 Privileged access rights; A.8.3 Information access restriction; A.8.24 Use of cryptography |

## Required actions

### Escalation trigger matrix

**Advisory (not catalogue-backed):** use the following as the minimum repository escalation policy implementing **DLP-M-001**.

| Detection control | Escalate when | Recommended response |
|---|---|---|
| Secret scanning at commit, push, pull request, and repository-history levels | A valid or potentially usable password, API token, private key, signing key, certificate key, cloud credential, database credential, or production connection string is detected | Immediately block where possible; open a security incident; revoke or rotate the credential; preserve evidence; scan history, forks, artifacts, and logs |
| Content classification and DLP scanning | Customer, payment, authentication, health, employee, confidential, or other classified data appears in source, fixtures, test data, attachments, issues, wikis, releases, or CI logs | Block the push or publication and escalate to Security Operations and the data owner for exposure assessment |
| Repository visibility monitoring | A private or internal repository containing sensitive content becomes public, externally shared, or accessible to an unapproved group | Treat as confirmed boundary exposure; immediately restrict access, preserve access logs, assess downloads and forks, and initiate incident response |
| Fork, mirror, export, and transfer monitoring | A repository is copied to a personal namespace, unapproved organisation, unmanaged platform, removable destination, or external collaboration space | Block where technically possible and escalate for ownership and authorization validation |
| Clone and download anomaly detection | Bulk cloning, archive downloads, repeated API extraction, or unusual access occurs from a new geography, device, IP address, service token, dormant account, privileged user, or departing employee | Escalate when the activity is inconsistent with the user’s role or approved workflow; suspend tokens when compromise is credible |
| Egress and proxy DLP | Source code or repository archives are uploaded to personal cloud storage, public paste sites, external AI services, webmail, or unapproved source-control services | Block and escalate, particularly where classified code, data, credentials, or production configuration is present |
| CI/CD output scanning | Sensitive data or secrets appear in job logs, test reports, build artifacts, container layers, caches, SBOM attachments, or release packages | Stop publication or deployment; restrict the artifact; rotate exposed secrets; determine who retrieved it |
| Control-integrity monitoring | Secret scanning, DLP, branch protection, audit logging, retention, or repository access controls are disabled, bypassed, or reduced without approval | Escalate as suspected control evasion; restore controls and review the actor’s related activity |
| Repeat-attempt correlation | A user, token, workload, or repository generates repeated blocked events or distributes sensitive content across multiple small commits | Escalate as potential intentional or automated exfiltration rather than handling each alert independently |
| Scanner-health monitoring | DLP or secret scanning stops, loses repository coverage, cannot inspect encrypted content, or fails open on repositories handling sensitive assets | Escalate operationally; prevent public release or external transfer until coverage is restored or a formally approved compensating control exists |

### Implementation sequence

1. **Repository/platform owner:** enable pre-receive or equivalent push protection and continuous scanning across default branches, full history, forks, pull requests, issues, wikis, releases, CI logs, and artifacts.
2. **Data governance:** define sensitive-data classifiers, approved test-data patterns, code-classification rules, and authorized external destinations.
3. **Security Operations:** route high-confidence DLP detections, visibility changes, control tampering, and anomalous extraction events to the SIEM and incident-management platform.
4. **Secrets management owner:** automate revocation or rotation for confirmed credentials; deleting the commit alone is insufficient.
5. **Incident response:** document containment steps covering repository restriction, token suspension, fork and clone analysis, history cleanup, legal/privacy assessment, and notification decisions.
6. **Platform engineering:** test policies using synthetic sensitive data and test credentials. Per **DLP-M-001**, simulated exfiltration tests should demonstrate that attempts are blocked or logged and that applicable CI gates fail when DLP is absent.

### Knowledge guidance

- **VeriFy-DATA-EA-001**, *9.3 Data – External Transfer Patterns*  
  Mandard references: **CRYPT-M-002**, **DATA-M-001**, **DATA-M-002**, **DATA-M-003**, **DLP-M-001**, **GOV-G-006**, **NSEG-M-002**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947980  
  Section 2 establishes controlled external-transfer patterns and identifies DLP as applicable to data leaving the estate. Its documented scope covers file-transfer and collaboration technologies, not source repositories specifically.

- **VeriFy-INF-002**, *3. System / Infrastructure Layer*  
  Mandard references: **CSPM-M-001**, **DLP-M-001**, **GOV-G-006**, **IAM-M-002**, **IAM-M-005**, **MON-M-001**, **PROV-M-002**, **PROV-M-003**, **RUNTIME-M-001**, **RUNTIME-M-002**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658243766  
  Section 2 includes DLP among the infrastructure processes and controls applicable across on-premises and Azure workloads, but does not define repository incident thresholds.

- **VeriFy-IS-RMP-001**, *10.3 InfoSec – Release Management & CI/CD Pipelines*  
  Mandard references: **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, **SIGN-M-001**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688  
  Section 2 calls for repository least privilege, secrets detection, prevention of hardcoded credentials, branch protection, pull-request review, CI checks, and security-event management. This document is useful supplemental repository guidance but is **not currently mapped to DLP-M-001**.

## Evidence for audit

Retain:

- Approved repository DLP policy and escalation matrix.
- Screenshots or exported configuration showing organization-wide scanning and push protection.
- Repository inventory and evidence of scanner coverage, including forks and archived repositories.
- Synthetic exfiltration and secret-detection test results showing block or alert behavior.
- SIEM routing rules, alert samples, incident tickets, and response timestamps.
- Credential revocation or rotation records for confirmed exposure.
- Repository visibility-change, clone, download, fork, export, and administrator audit logs.
- Records showing investigation of build logs, artifacts, caches, releases, and repository history.
- Approved deviation records and technical justification where required controls cannot be enforced.

## Assumptions and limits

The repository platform, organisational data-classification scheme, incident severity model, and response SLAs were not specified. No knowledge document was found that defines source-repository-specific DLP escalation thresholds; therefore, the trigger matrix and response prioritisation are **Advisory (not knowledge-doc backed)**.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**CSPM-M-001**](https://verify.example-org.internal/?id=CSPM-M-001) | High | Cloud Security Posture | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, BAI10, DSS02.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**DATA-M-001**](https://verify.example-org.internal/?id=DATA-M-001) | Medium | Data Protection | AIUC1 (E005); CIS_CONTROLS (CIS 11, CIS 3, CIS 6); CWE (CWE-284, CWE-285, CWE-327); GDPR (Article 32); HIPAA (164.312(a)(1), 164.312(a)(2)(iv)); ISO_27001 (A.5.15, A.5.18, A.5.34); +9 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DATA-M-003**](https://verify.example-org.internal/?id=DATA-M-003) | High | Data Protection | CIS_CONTROLS (CIS 3); ISO_27001 (A.5.14, A.8.20, A.8.24); MITRE_ATT&CK (M1041); NIST_CSF (PR.AA, PR.DS, PR.IR); NIST_SP_800_53 (AC-4, IA-5, SC-13); SOC2 (CC6) |
| [**DLP-M-001**](https://verify.example-org.internal/?id=DLP-M-001) | High | Data Loss Prevention | AIUC1 (A004, A006); CCPA_CPRA (Data Minimization, Reasonable Security Procedures, Right to Limit Sensitive Personal Information); CIS_CONTROLS (CIS 12, CIS 3, CIS 6); COBIT_2019 (APO14, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285); GDPR (Article 25, Article 32, Article 5); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |

Showing 15 of 22 cited mandards.

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