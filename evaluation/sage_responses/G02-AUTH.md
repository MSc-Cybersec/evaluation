# G02-AUTH

## Question
What minimum controls are required before granting an auth exception for privileged users?

## Sage response

## Bottom line

A privileged-user authentication exception must not be enabled until it is formally recorded, independently approved, assigned to a residual-risk owner, protected by documented compensating controls, and given a fixed expiry date. MFA remains the Critical baseline under **AUTH-M-002** and **IAM-M-002**; an exception is a temporary, auditable deviation—not removal of the requirement. Reject any request that is ownerless, open-ended, lacks operational compensating controls, or bypasses independent approval.

## Risk and impact

The baseline risk is **Critical** because compromised privileged credentials can enable administrative takeover, privilege escalation, lateral movement, and production impact. Exception governance is **High** risk: undocumented or indefinitely renewed exceptions create invisible and effectively permanent exposure.

For production administration, direct connectivity from ordinary endpoints also creates **High** risk by removing the controlled point at which authentication, access revocation, and session logging can be enforced.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: record the affected control, technical justification, residual risk and accepting owner, compensating controls, expiry date, and independent approval before release; review at expiry and do not renew indefinitely without re-justification. |
| **AUTH-M-002** | Multi-Factor Authentication Enforcement | Critical | Per **AUTH-M-002**: privileged admin, developer, and DevOps accounts must use MFA; hardware keys or TOTP are preferred, with SMS only as fallback. |
| **IAM-M-002** | Enforce MFA for Privileged Accounts | Critical | Per **IAM-M-002**: MFA must be enforced for every privileged and administrative account. |
| **IAM-M-001** | Least-Privilege IAM Policies | Critical | Per **IAM-M-001**: retain least privilege and prohibit wildcard actions or resources for production roles. |
| **AUTH-M-003** | Session Management and Timeout Controls | High | Per **AUTH-M-003**: enforce a maximum eight-hour absolute timeout, a 15-minute idle timeout, and invalidate sessions after logout, password change, or role change. |
| **IAM-M-005** | Brokered Administrative Access | High | Per **IAM-M-005**: production privileged access must use a hardened bastion, jump service, or just-in-time broker; direct management access must be denied and privileged sessions logged. |

If the requested exception removes MFA from a production access broker, the deviation must explicitly identify **AUTH-M-002**, **IAM-M-002**, and **IAM-M-005** as affected controls.

## Framework mapping

The following relevant mappings were returned by the SAGF catalogue:

| Mandard | Framework mappings |
|---|---|
| **GOV-G-006** | NIST SP 800-53 Rev.5: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |
| **AUTH-M-002** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-2, AC-3, AC-6, AC-7; PCI DSS v4.0: Requirements 7 and 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 |
| **IAM-M-002** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-2, AC-3, AC-6, AC-7; PCI DSS v4.0: Requirements 7 and 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 |
| **IAM-M-001** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-6; PCI DSS v4.0: Requirement 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3 |
| **AUTH-M-003** | NIST SP 800-53 Rev.5: AC-12, AU-2, AU-6, AU-12, SI-4; PCI DSS v4.0: Requirements 8 and 10; ISO/IEC 27001:2022: A.8.5, A.8.15, A.8.16 |
| **IAM-M-005** | NIST SP 800-53 Rev.5: AC-2, AC-6, AC-17, IA-2, AU-2; ISO/IEC 27001:2022: A.8.2, A.8.20; CIS Controls v8: CIS 5, CIS 6, CIS 12 |

## Required actions

1. **Create the deviation before access is granted.**  
   The GRC or security owner must record:
   - User or account and affected system
   - Exact Mandard and authentication control being bypassed
   - Business need and technical justification
   - Scope and duration
   - Residual-risk rating and named accepting owner
   - Compensating controls
   - Approval authority and expiry date

2. **Obtain independent approval.**  
   Per **GOV-G-006**, approval must come from an authority outside the delivery team. The approved deviation must be included in the applicable assurance or SAF pack.

3. **Keep privilege narrowly scoped.**  
   Per **IAM-M-001**, restrict the account to only the actions and resources required. Do not allow production wildcard permissions.

4. **Retain MFA wherever technically possible.**  
   Per **AUTH-M-002** and **IAM-M-002**, prefer hardware keys or TOTP. Limit the exception to the specific broken authentication step rather than exempting the account from all MFA.

5. **Route production access through a controlled path.**  
   Per **IAM-M-005**, deny direct administrative connectivity, use brokered or just-in-time access, issue short-lived credentials, and log privileged sessions. MFA at the broker remains required unless **IAM-M-005** is also explicitly included in the approved deviation.

6. **Enforce session restrictions.**  
   Per **AUTH-M-003**, configure no more than eight hours absolute duration, 15 minutes idle duration, and immediate invalidation after logout, password change, or role change.

7. **Enforce expiry automatically.**  
   Configure the IAM or PAM platform to remove the exception at the approved expiry. The release or access gate should reject missing, unapproved, or expired deviation references.

**Knowledge guidance:** **VeriFy-AUTH-INT-001**, mapped to **AUTH-M-002**, **AUTH-M-003**, **GOV-G-006**, **IAM-M-001**, and **IAM-M-002**, states that non-compliance must be formally recorded as a deviation and included in the SAF pack with technical justification. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817263

The broader authentication guidance, **VeriFy-AUTH-002**, also requires departures from authentication guardrails to be formally recorded and included in the SAF pack with technical justification; it is mapped to **AUTH-M-002**, **AUTH-M-003**, and **GOV-G-006**, among others. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817239

## Evidence for audit

Retain the following evidence:

- Approved, unexpired deviation-register record containing every field required by **GOV-G-006**
- Independent approver identity and timestamp
- Residual-risk acceptance by the named owner
- SAF or assurance pack containing the deviation and technical justification
- IAM/PAM configuration proving constrained privilege and automatic expiry
- IdP policy or test result showing where MFA remains enforced
- Bastion or just-in-time broker configuration and network rule proving direct access is denied
- Privileged-session and SIEM logs
- Session-timeout and invalidation test results
- Expiry review showing remediation, closure, or documented re-justification

## Assumptions and limits

The catalogue does not define a universal maximum exception duration or a standard set of compensating controls for every authentication technology. The expiry must therefore be explicitly approved and technically enforced; the compensating controls must be selected according to the affected system and threat scenario. No specific exception request, target platform, account type, or proposed duration was provided.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AUTH-M-002**](https://verify.example-org.internal/?id=AUTH-M-002) | Critical | Authentication | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-287); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +9 more |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |

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