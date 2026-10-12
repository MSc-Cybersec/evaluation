# G34-CRED

## Question
What governance controls prevent misuse of privileged credentials in CI/CD?

## Sage response

## Bottom line

Privileged CI/CD credentials must be short-lived, least-privileged, inaccessible to untrusted code, protected by MFA for human administrators, and monitored through centralized audit logging. The primary controls are **PIPE-M-012**, **SECR-M-004**, **IAM-M-001**, and **IAM-M-002**; failure exposes production systems, source repositories, and release artifacts to credential theft and unauthorized deployment. Platform Engineering should enforce these controls centrally and block production releases that do not comply.

## Risk and impact

The applicable Mandards are predominantly **Critical** because a compromised pipeline credential can allow an attacker to:

- Exfiltrate secrets through malicious pull requests, workflow triggers, logs, caches, or persistent runners.
- Modify pipeline definitions and deploy unauthorized code.
- Tamper with packages, container images, and release artifacts.
- Escalate from a repository or build runner into production infrastructure.
- Operate through service accounts without timely detection or individual accountability.

High-risk supporting controls address centralized detection and formally governed exceptions.

## Governing mandards

### Controls directly preventing privileged-credential misuse

| Mandard | Title | Risk | Governance effect |
|---|---|---:|---|
| **PIPE-M-012** | CI/CD Workflow Least Privilege and Safe Triggers | Critical | Pipeline tokens default to no permissions; jobs receive only required scopes. Elevated workflows cannot execute untrusted code, credential persistence is disabled, and critical deployments require approval. |
| **SECR-M-004** | Short-Lived Credentials & Rotation | Critical | Production automation cannot use long-lived credentials; use ephemeral OIDC or STS tokens, or regularly rotate unavoidable stored credentials. |
| **IAM-M-001** | Least-Privilege IAM Policies | Critical | Production roles cannot contain wildcard actions or resources; privileges must be restricted to required operations and targets. |
| **IAM-M-002** | Enforce MFA for Privileged Accounts | Critical | MFA is mandatory for privileged and administrative human accounts. |
| **SECR-M-001** | No Hardcoded Secrets | Critical | Builds must fail when high-confidence credentials are detected in source or configuration. Exposed credentials must be invalidated and moved to an approved vault. |
| **SECR-M-002** | Prevent Secret Exposure in CI/CD Logs and History | Critical | Secrets must be masked and excluded from logs, command history, working directories, and container images; detection must fail the build. |
| **PIPE-M-003** | Use Ephemeral Build Agents | Critical | Build agents must be single-use and destroyed after execution, preventing residual credentials from being recovered or reused. |
| **PIPE-M-001** | Secure CI/CD Pipeline Configuration | Critical | Pipeline definitions must be version-controlled, scanned, auditable, and protected by approval gates for critical deployments. |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High | CI/CD audit logs must be forwarded to a SIEM with alerts for privilege escalation, credential anomalies, unauthorized workflow changes, and gate bypasses. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Any control bypass requires an independently approved, time-bounded deviation recording residual risk, owner, justification, and compensating controls. |

### Complete pipeline-security domain

The complete `PIPE-M` domain was retrieved. In addition to the directly applicable controls above, the domain contains:

| Mandard | Title | Risk |
|---|---|---:|
| **PIPE-M-001** | Secure CI/CD Pipeline Configuration | Critical |
| **PIPE-M-002** | Pre-Commit Hooks Enforced | Critical |
| **PIPE-M-003** | Use Ephemeral Build Agents | Critical |
| **PIPE-M-004** | Pin Build Tool Versions | Medium |
| **PIPE-M-005** | Vulnerability Scans for Non-Prod | Medium |
| **PIPE-M-006** | Implement Plugin and Integration Governance in CI/CD Platforms | High |
| **PIPE-M-007** | Sequential Security Pipeline Execution | High |
| **PIPE-M-008** | Hermetic Builds — Isolated Build Environment | Critical |
| **PIPE-M-009** | Restrict Build Parameters to Whitelisted Values | Medium |
| **PIPE-M-010** | Maintain Inventory of Build Tools and Versions | High |
| **PIPE-M-011** | Enforce Build Immutability and Tamper-Proofing | High |
| **PIPE-M-012** | CI/CD Workflow Least Privilege and Safe Triggers | Critical |
| **PIPE-M-013** | Pin and Verify Third-Party CI Actions and Reusable Workflows | High |
| **PIPE-M-014** | CI Runner Hardening and Cache Poisoning Prevention | High |

## Framework mapping

Only mappings returned by the SAGF catalogue are listed.

| Mandard | Selected mapped controls |
|---|---|
| **PIPE-M-012** | NIST SP 800-53: AC-2, AC-3, AC-4, AC-6, IA-5, SC-12, CM-3, SA-15; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.3, A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.24, A.8.25, A.8.31, A.8.32; HIPAA: 164.312(a)(1); OWASP ASVS 5.0: V8. |
| **SECR-M-004** | NIST SP 800-53: IA-5, SC-12, SR-3, SR-4, SA-12; ISO/IEC 27001:2022: A.5.17, A.5.19, A.5.21, A.8.24, A.8.30; SOC 2: CC6.1; OWASP SAMM 2.0: Implementation—Secure Build; OWASP Top 10:2025: A03; SLSA: L1, L2. |
| **IAM-M-001** | NIST SP 800-53: AC-2, AC-3, AC-4, AC-6, IA-2, IA-4, IA-8; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.3, A.5.15, A.5.16, A.5.18, A.8.2, A.8.3, A.8.5, A.8.18; SOC 2: CC6.1. |
| **IAM-M-002** | NIST SP 800-53: IA-2, IA-5, AC-2, AC-3, AC-6, AC-7; PCI DSS v4.0: Req 7 and Req 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5. |
| **GOV-G-006** | NIST SP 800-53: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; OWASP SAMM 2.0: Governance—Policy & Compliance; COBIT 2019: APO12.01, MEA02; NIST CSF 2.0: GV.RM, GV.OV, ID.RA. |

## Required actions

1. **Remove standing production credentials.**  
   Per **SECR-M-004**: migrate pipelines to short-lived workload identities such as OIDC federation or role assumption. Rotate any unavoidable stored credentials and prohibit long-lived production automation secrets.  
   **Owner:** IAM and Platform Engineering.

2. **Default pipeline permissions to deny.**  
   Per **PIPE-M-012**: set workflow-level token permissions to none and grant only narrowly scoped, per-job permissions. Restrict dangerous fork, comment, `workflow_run`, and equivalent triggers; disable credential persistence and ensure untrusted code cannot run in a privileged context.  
   **Owner:** CI/CD Platform Engineering.

3. **Constrain every deployment identity.**  
   Per **IAM-M-001**: remove wildcard actions and resources, use separate identities for each environment and workload, and apply permission boundaries to production roles.  
   **Owner:** Cloud IAM and application owners.

4. **Enforce human approval and MFA.**  
   Per **IAM-M-002**: require MFA for platform administrators and production approvers. Per **PIPE-M-001** and **PIPE-M-012**: require authorized manual approval before deployment to production or other critical environments.  
   **Owner:** Identity Operations and Release Management.

5. **Eliminate credential persistence and exposure.**  
   Per **SECR-M-001** and **SECR-M-002**: enforce secret scanning on commits and pull requests, mask secrets in logs, scan completed logs and built images, and fail the build on detection. Immediately revoke any exposed credential.  
   **Owner:** Security Engineering and repository owners.

6. **Use disposable execution environments.**  
   Per **PIPE-M-003**: run jobs on ephemeral, single-use agents that are destroyed after each execution. Do not reuse workspaces containing production tokens.  
   **Owner:** CI/CD Platform Engineering.

7. **Detect anomalous privileged activity.**  
   Per **LOG-M-003**: forward CI/CD audit logs to the SIEM and alert on privilege escalation, unauthorized pipeline modification, approval bypass, secret detection, and service-account use outside expected patterns. Detection rules must be version-controlled and tuned at least quarterly.  
   **Owner:** SOC and Detection Engineering.

8. **Govern exceptions rather than silently bypassing controls.**  
   Per **GOV-G-006**: block releases unless an override references an approved, unexpired deviation with an independent approver, residual-risk owner, compensating controls, and expiry date.  
   **Owner:** GRC and independent security authority.

### Implementation guidance

- **VeriFy-IS-RMP-001**, *10.3 InfoSec – Release Management & CI/CD Pipelines*  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688  
  Mandard refs: **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, **SIGN-M-001**.  
  Section 2 directs teams to keep publication credentials in secret stores, enforce zero hardcoded credentials, inject deployment secrets through secure vaults, segregate environments, apply identity-based access to deployment targets, and require branch reviews and CI checks.

- **VeriFy-AUTHZ-GEN-001**, *7.1 Authorization – General*  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766  
  Mandard refs: **AC-M-001**, **DB-M-003**, **GOV-G-006**, **IAM-M-001**, **IAM-M-002**, **SECR-M-001**, **SECR-M-004**.  
  Section 2 directs teams to use least-privileged and environment-specific service accounts, restrict them to designated hosts, retrieve credentials through Azure Key Vault, log privileged access, prohibit credentials in code, and assign an accountable staff owner to every service account.

## Evidence for audit

Retain the following:

- Pipeline policy showing default-deny token permissions and per-job scopes.
- Workload-identity or OIDC federation configuration and evidence that production static keys are absent.
- IAM policy scan proving that production roles contain no wildcard permissions.
- Privileged-account report demonstrating MFA enforcement.
- Protected-environment configuration and production approval records.
- Secret-scanning results for source, pipeline logs, artifacts, and container images.
- Runner configuration proving agents are ephemeral and workspaces are destroyed.
- Central SIEM ingestion status, version-controlled detection rules, alert tests, and quarterly tuning records.
- Service-account inventory showing owner, environment, permitted resources, last use, and rotation or token lifetime.
- Approved and unexpired **GOV-G-006** deviation records for any remaining exception.

## Assumptions and limits

No CI/CD platform configuration, IAM policies, workload identities, repositories, logs, or approval settings were inspected. The controls above describe catalogue requirements and mapped organisational guidance; they do not establish that a particular pipeline is compliant. Two initially identified knowledge-document IDs could not be retrieved and were not used.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**DB-M-003**](https://verify.example-org.internal/?id=DB-M-003) | High | Database Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |
| [**PIPE-M-002**](https://verify.example-org.internal/?id=PIPE-M-002) | Critical | Pipeline Security | COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-798); ISO_27001 (A.5.17, A.8.24, A.8.25); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, IA-5); NIST_SSDF (PO.1.1, PS.1.1, PS.2.1); +3 more |
| [**PIPE-M-003**](https://verify.example-org.internal/?id=PIPE-M-003) | Critical | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); NIST_CSF (GV.SC-01, ID.RA-09, PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, IA-5); +7 more |
| [**PIPE-M-004**](https://verify.example-org.internal/?id=PIPE-M-004) | Medium | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.19, A.5.21, A.8.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.IR-01); NIST_SP_800_53 (AC-3, CM-2, CM-3); +6 more |
| [**PIPE-M-005**](https://verify.example-org.internal/?id=PIPE-M-005) | Medium | Pipeline Security | CIS_CONTROLS (CIS 12); COBIT_2019 (BAI03.03, BAI06.01); ISO_27001 (A.8.20, A.8.22, A.8.25); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, AC-4, CM-3); NIST_SSDF (PO.1.1, PS.1.1, PS.2.1); +3 more |
| [**PIPE-M-006**](https://verify.example-org.internal/?id=PIPE-M-006) | High | Pipeline Security | CIS_CONTROLS (CIS 12, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, APO12.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.5.19); NIST_CSF (DE.AE-02, DE.CM-01, GV.OC-01); +10 more |
| [**PIPE-M-007**](https://verify.example-org.internal/?id=PIPE-M-007) | High | Pipeline Security | CIS_CONTROLS (CIS 4); COBIT_2019 (BAI03.03, BAI06.01, BAI07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.25, A.8.27, A.8.31); NIST_CSF (PR.IR-01, PR.PS-01, PR.PS-06); NIST_SP_800_53 (AC-3, CA-9, CM-2); +5 more |

Showing 15 of 26 cited mandards.

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