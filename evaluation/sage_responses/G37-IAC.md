# G37-IAC

## Question
What evidence proves IaC changes are security-reviewed and policy-compliant?

## Sage response

## Bottom line

IaC changes are proven security-reviewed and policy-compliant by a traceable evidence chain linking the exact commit to an approved pull request, successful mandatory IaC and secrets checks, an authorized deployment, and immutable deployment logs. A reviewer approval alone is insufficient: the evidence must show that required checks could not be bypassed and that the deployed commit is the reviewed commit. Any failed or overridden control requires an approved, unexpired deviation before release.

## Risk and impact

The principal exposure is deployment of insecure or unauthorized infrastructure, including public resources, unrestricted network access, embedded credentials, excessive IAM permissions, and changes that cannot be reconstructed during an incident.

- **Critical:** Hardcoded secrets in IaC; insecure or bypassable CI/CD workflows.
- **High:** Critical or high IaC misconfigurations, unreviewed manual infrastructure changes, excessive deployment permissions, and unmanaged exceptions.
- **Medium:** Incomplete deployment audit trails and failure to detect post-deployment drift or compliance violations.

## Governing mandards

### Primary evidence requirements

| Mandard | Title | Risk | Evidence implication |
|---|---|---:|---|
| **IAC-M-002** | No Hardcoded Secrets in IaC | Critical | The commit-linked scan must show no clear-text secrets or keys; the pipeline must fail when they are detected. |
| **PIPE-M-001** | Secure CI/CD Pipeline Configuration | Critical | Pipeline definitions must be version-controlled and auditable, security checks must be required before promotion, and critical-environment deployment must require authorized approval. |
| **PIPE-M-012** | CI/CD Workflow Least Privilege and Safe Triggers | Critical | Workflow-analysis results, restricted permissions and triggers, immutable checkout references, and production approval records must be available. |
| **IAC-M-001** | No Critical IaC Misconfigs | High | The build must fail when the IaC scanner finds Critical or High misconfigurations. |
| **IAC-M-003** | Infrastructure Immutability & Drift Prevention | High | Infrastructure changes must flow exclusively through IaC; drift must be detected and alerted on or remediated. |
| **IAC-M-005** | Principle of Least Privilege in IaC | High | Deployment identities must have restricted permissions, supported by policy validation and permission-audit evidence. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Every overridden control requires an independently approved, time-bounded deviation linked to the release. |
| **IAC-M-007** | Infrastructure Change Logging & Audit Trail | Medium | Logs must record who deployed, what changed, when, the source commit, and deployment status, and must be centrally stored and immutable. |
| **IAC-M-008** | Continuous Infrastructure Monitoring & Compliance | Medium | Post-deployment policy, drift, and compliance reports must show continuing compliance or tracked remediation. |

### Complete IaC mandard set

The IaC domain also includes:

| Mandard | Title | Risk |
|---|---|---:|
| **IAC-M-001** | No Critical IaC Misconfigs | High |
| **IAC-M-002** | No Hardcoded Secrets in IaC | Critical |
| **IAC-M-003** | Infrastructure Immutability & Drift Prevention | High |
| **IAC-M-004** | Comprehensive Infrastructure Inventory & Tagging | Medium |
| **IAC-M-005** | Principle of Least Privilege in IaC | High |
| **IAC-M-006** | Open Source Dependencies in Infrastructure Code | High |
| **IAC-M-007** | Infrastructure Change Logging & Audit Trail | Medium |
| **IAC-M-008** | Continuous Infrastructure Monitoring & Compliance | Medium |

Per **IAC-M-001**: policy compliance requires a blocking result, not merely evidence that a scanner ran.  
Per **IAC-M-007**: the audit trail must connect the deployment to its actor, timestamp, source commit, changes, and outcome.  
Per **GOV-G-006**: an exception is valid only when independently approved, risk-owned, justified, compensated, and unexpired.

## Framework mapping

The catalogue returned the following relevant mappings:

| Mandard | Framework mappings |
|---|---|
| **IAC-M-001** | NIST SP 800-53 Rev. 5: `CM-6`, `SI-4`, `AU-6`, `CM-2`, `SC-7`, `CA-9`, `CM-3`, `SA-15`; ISO/IEC 27001:2022: `A.8.16`, `A.8.9`, `A.8.27`, `A.8.25` |
| **IAC-M-002** | NIST SP 800-53 Rev. 5: `CM-6`, `IA-2`, `IA-5`, `AC-7`, `SC-12`, `CM-2`, `SC-7`, `CA-9`, `CM-3`, `SA-15`, `IA-4`, `IA-8` |
| **PIPE-M-012** | NIST SP 800-53 Rev. 5: `AC-2`, `AC-3`, `AC-6`, `AC-4`, `IA-5`, `SC-12`, `CM-3`, `SA-15`; PCI DSS v4.0: `Req 7`; ISO/IEC 27001:2022: `A.5.15`, `A.5.18`, `A.8.3`, `A.8.2`, `A.8.24`, `A.5.17`, `A.8.25`, `A.8.31`, `A.8.32`, `A.5.3`; HIPAA: `164.312(a)(1)`; OWASP ASVS 5.0: `V8`; OWASP SAMM 2.0: `Implementation: Secure Deployment` |
| **IAC-M-007** | NIST SP 800-53 Rev. 5: `CM-6`, `AU-2`, `AU-6`, `AU-12`, `SI-4`, `CM-2`, `SC-7`, `CA-9` |
| **GOV-G-006** | NIST SP 800-53 Rev. 5: `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022: `A.5.1`, `A.5.35`; SOC 2: `CC3`, `CC5`; OWASP SAMM 2.0: `Governance: Policy & Compliance`; COBIT 2019: `APO12.01`, `MEA02`; NIST CSF 2.0: `GV.RM`, `GV.OV`, `ID.RA` |

## Required actions

1. **Enforce commit-linked, blocking checks.**  
   Per **IAC-M-001** and **IAC-M-002**, configure IaC and secret scanning as required merge checks. Preserve the scanner identity, policy pack or rule version, findings, severity, result, timestamp, and commit SHA.

2. **Protect the merge path.**  
   Per **PIPE-M-001**, place pipeline configuration under version control, require successful security checks and pull-request approval, prevent direct pushes, and retain pipeline audit logs.

3. **Make security review identifiable.**  
   The pull-request record should identify the reviewer, approval time, reviewed commit, comments or findings, and final disposition.  
   **Advisory (not catalogue-backed):** use `CODEOWNERS` or an equivalent rule so changes to IaC, IAM, networking, encryption, pipeline, or policy files require approval from a designated security-qualified owner. A generic developer approval does not by itself prove a security review.

4. **Secure the CI/CD execution context.**  
   Per **PIPE-M-012**, use least-privileged job permissions, safe triggers, immutable full commit SHAs, disabled credential persistence, and manual approval for production or other critical environments. Run workflow analysis as a required check.

5. **Bind deployment to the reviewed revision.**  
   Per **IAC-M-003** and **IAC-M-007**, deploy only through the controlled IaC pipeline and record the same commit SHA that passed review and policy checks. Prohibit or detect direct console changes.

6. **Preserve exceptions as governed decisions.**  
   Per **GOV-G-006**, a bypass must reference a deviation containing the affected control, justification, residual risk owner, compensating controls, independent approval, and expiry date.

7. **Verify the deployed state continuously.**  
   Per **IAC-M-003** and **IAC-M-008**, retain drift-detection and runtime compliance reports and track each violation through remediation or an approved deviation.

### Implementation guidance

**VeriFy-IS-RMP-001**, *10.3 InfoSec – Release Management & CI/CD Pipelines*  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688  
Mapped mandards: **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, **SIGN-M-001**.

The document’s “Release Management and Pipeline Guardrails” section calls for pull-request reviews and CI checks before merge, IaC scanning during deployment to detect misconfigurations, and enforcement of application and IaC security controls. Its “Purpose, Scope and Deviations” section requires non-compliance to be formally recorded as a deviation with technical justification and included in the SAF pack. This document is not currently mapped to the **IAC-M** mandards in its `mandard_refs`; its IaC scanning statement is implementation guidance rather than the source of the IaC requirements.

## Evidence for audit

A defensible evidence package for each sampled IaC change should contain:

| Evidence artefact | What it must prove |
|---|---|
| Pull request or merge request export | Repository, author, changed IaC files, reviewer identity, approval decision, timestamps, comments, and exact approved commit SHA |
| Branch-protection or repository-rule configuration | Direct pushes are blocked; review and named security/policy checks are mandatory; delivery staff cannot silently bypass the rules |
| IaC scanner report | Scope, rule or policy version, findings and severities, pass/fail threshold, execution time, and commit SHA; no unresolved Critical or High result under **IAC-M-001** |
| Secret-scanning report | No clear-text secrets or keys in the changed IaC; failure behavior is configured under **IAC-M-002** |
| Policy-as-code result | Each applicable policy’s decision, input plan or manifest, policy version, and blocking outcome |
| CI/CD run record | Build, security, approval, and deployment stages executed in the required order against the same commit |
| Production approval record | Named authorized approver, approval timestamp, target environment, deployment or release identifier, and commit SHA |
| IaC plan and apply output | Reviewed proposed changes correspond to the applied changes; final status and resource changes are recorded |
| Immutable deployment audit log | Actor, changed resources, timestamp, source commit, pipeline run, environment, and success or failure, as required by **IAC-M-007** |
| Cloud activity log | The infrastructure APIs were invoked by the approved pipeline identity rather than an unauthorized human or alternate path |
| Drift and runtime compliance report | Deployed state remains aligned with IaC and policy baselines under **IAC-M-003** and **IAC-M-008** |
| Deviation record, when applicable | Approved and unexpired exception satisfying every field required by **GOV-G-006** |

**Advisory (not knowledge-doc backed):** screenshots should be supporting evidence only. Prefer immutable system exports, API records, signed reports, or centrally retained logs because they preserve identifiers and can be independently reconciled. Audit should be able to follow one key—normally the commit SHA—from review, through every policy decision, to the deployed resources.

## Assumptions and limits

No repository settings, pull requests, scanner configurations, pipeline runs, deployment logs, reviewer qualifications, or deviation records were supplied for verification. Therefore, this answer defines the required evidence pattern but does not attest that a particular project complies.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**IAC-M-001**](https://verify.example-org.internal/?id=IAC-M-001) | High | Infrastructure as Code | CIS_CONTROLS (CIS 4, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.16, A.8.25, A.8.27); NIST_CSF (DE.AE-02, DE.CM-01, PR.IR-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**IAC-M-002**](https://verify.example-org.internal/?id=IAC-M-002) | Critical | Infrastructure as Code | CIS_CONTROLS (CIS 4, CIS 5, CIS 6); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.8.24); NIST_CSF (PR.AA-01, PR.AA-05, PR.IR-01); +8 more |
| [**IAC-M-003**](https://verify.example-org.internal/?id=IAC-M-003) | High | Infrastructure as Code | CIS_CONTROLS (CIS 4, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.16, A.8.25, A.8.27); NIST_CSF (DE.AE-02, DE.CM-01, PR.IR-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +5 more |
| [**IAC-M-004**](https://verify.example-org.internal/?id=IAC-M-004) | Medium | Infrastructure as Code | CIS_CONTROLS (CIS 1, CIS 4); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.9, A.8.25, A.8.27); NIST_800_82 (6.1.1); NIST_CSF (ID.AM, PR.IR-01, PR.PS-01); +5 more |
| [**IAC-M-005**](https://verify.example-org.internal/?id=IAC-M-005) | High | Infrastructure as Code | CIS_CONTROLS (CIS 4, CIS 6); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +9 more |
| [**IAC-M-006**](https://verify.example-org.internal/?id=IAC-M-006) | High | Infrastructure as Code | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.19, A.5.21, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +7 more |
| [**IAC-M-007**](https://verify.example-org.internal/?id=IAC-M-007) | Medium | Infrastructure as Code | CIS_CONTROLS (CIS 17, CIS 4, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); HIPAA (164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); ISO_27001 (A.5.24, A.5.26, A.8.15); +11 more |
| [**IAC-M-008**](https://verify.example-org.internal/?id=IAC-M-008) | Medium | Infrastructure as Code | CIS_CONTROLS (CIS 4, CIS 6, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.16); +10 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |
| [**PIPE-M-012**](https://verify.example-org.internal/?id=PIPE-M-012) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); NIST_CSF (PR.PS-06); +8 more |
| [**SECR-M-002**](https://verify.example-org.internal/?id=SECR-M-002) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |

Showing 15 of 16 cited mandards.

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