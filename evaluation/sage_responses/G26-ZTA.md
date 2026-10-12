# G26-ZTA

## Question
What minimum Zero Trust controls are required for internal admin portals?

## Sage response

## Bottom line

Internal admin portals must implement all four Zero Trust mandards: authenticate and authorize every access attempt, eliminate trust based on internal network location, continuously reassess identity/device risk, and isolate the portal through micro-segmentation or ZTNA. The two foundational requirements are **Critical**; failure permits compromised internal devices or credentials to obtain privileged access and move laterally. Production approval should be withheld until these controls are evidenced or a formally approved deviation is included in the security assurance pack.

## Risk and impact

| Risk | Exposure if unaddressed |
|---|---|
| **Critical** | Internal IP addresses, VPN access, or prior login could be treated as sufficient proof of trust, exposing privileged functions to compromised accounts and devices. |
| **High** | Long-lived sessions may remain authorized after risk changes, while flat network access increases lateral movement and blast radius. |

“Internal-only” is not a compensating control: per **ZTA-M-004**, corporate network location, VPN connectivity, and internal IP ranges must not establish trust.

## Governing mandards

All Zero Trust mandards apply:

| Mandard | Title | Risk | Minimum required outcome |
|---|---|---:|---|
| **ZTA-M-001** | Zero Trust: Never Trust, Always Verify | **Critical** | Per **ZTA-M-001**: authenticate and authorize users, services, and devices on every access attempt, regardless of origin. Apply conditional access using user, device, location, and risk factors. |
| **ZTA-M-004** | Implicit Trust Elimination | **Critical** | Per **ZTA-M-004**: do not grant access merely because a device is on the corporate network, connected through VPN, or using an internal IP. Require device identity and health verification. |
| **ZTA-M-002** | Micro-Segmentation Implementation | **High** | Per **ZTA-M-002**: place the portal in a separate security zone, require separate authentication and authorization, and use ZTNA or a service mesh with least-privilege policies. |
| **ZTA-M-003** | Continuous Authentication & Authorization | **High** | Per **ZTA-M-003**: continuously reassess user and service access. Changes in location, time, device health, or behavior must cause reauthentication or access reduction. |

## Framework mapping

The catalogue returned the following principal mappings:

| Mandard | Returned framework controls |
|---|---|
| **ZTA-M-001** | NIST SP 800-53 Rev. 5: IA-2, IA-5, IA-4, IA-8, AC-2, AC-3, AC-4, AC-6, AC-7, SC-7; PCI DSS v4.0: Requirements 1, 7, 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 |
| **ZTA-M-002** | NIST SP 800-53 Rev. 5: AC-3, AC-4, AC-6, SC-7; PCI DSS v4.0: Requirements 1, 7, 8; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.20 |
| **ZTA-M-003** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-2, AC-3, AC-6, AU-2, AU-6, AU-12, SI-4; PCI DSS v4.0: Requirements 1, 7, 8, 10 |
| **ZTA-M-004** | NIST SP 800-53 Rev. 5: AC-3, AC-4, AC-6, SC-7; PCI DSS v4.0: Requirements 1 and 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.3, A.8.20, A.8.22; SOC 2: CC6.1; OWASP ASVS 5.0: V8 |

## Required actions

1. **Enforce explicit identity on every route — Identity and application owners**
   - Per **ZTA-M-001**, place every portal page, API, administrative action, and supporting service behind authentication and server-side authorization.
   - Deny by default; evaluate authorization at each request rather than only when the user logs in.
   - Apply least-privilege administrative roles and do not rely on hidden URLs or network reachability.

2. **Remove network-based trust — Network and endpoint security owners**
   - Per **ZTA-M-004**, remove broad rules that grant access solely from corporate CIDRs, office networks, jump networks, or VPN address pools.
   - Require a verified user identity and device identity.
   - Gate access on device health, including required patch, encryption, and endpoint-protection state.

3. **Isolate the portal — Network or platform owner**
   - Per **ZTA-M-002**, expose the portal through ZTNA or an equivalent identity-aware access layer.
   - Place the portal and its backend services in restricted security zones.
   - Use default-deny rules and allow only documented user-to-portal and portal-to-service flows.

4. **Continuously re-evaluate access — Identity and application owners**
   - Per **ZTA-M-003**, reassess location, device health, time, and behavioral risk throughout the session.
   - Reauthenticate or downgrade access when risk thresholds are crossed.
   - Apply short-lived sessions or tokens and validate authorization claims on each request.

5. **Apply the available enterprise authentication guidance**
   - Knowledge document **VeriFy-AUTH-INT-EC-001**, mapped to **AUTH-M-001**, **AUTH-M-002**, **AUTH-M-003**, **CRYPT-M-002**, **GOV-G-006**, **IAM-M-001**, **OAUTH-M-001**, **SAML-M-001**, and **SECR-M-001**, directs internally exposed web services toward Entra ID using SAML or OIDC, or approved domain protocols where applicable. It also identifies BeyondTrust PAM for infrastructure administrators, MFA for web/application access, domain lockout alignment, and short-lived access/session lifetimes.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445334

A knowledge document is mapped to **ZTA-M-002**: **VeriFy-NET-001**, *2. Network / Connectivity Layer*. Its detailed implementation content was not retrieved and is therefore not asserted here.  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652023403

No knowledge document was found for **ZTA-M-001**, **ZTA-M-003**, or **ZTA-M-004**.

## Evidence for audit

Minimum evidence should include:

- Identity-provider application configuration showing authentication is mandatory for every portal route.
- Conditional-access policy export showing user, device, location, and risk evaluation.
- Role and permission matrix, including privileged-role owners and approval records.
- Device-compliance policy and a test showing that an unhealthy or unmanaged device is denied.
- Network or ZTNA configuration showing default-deny segmentation and explicitly permitted flows.
- Test results proving that access from an internal IP or VPN without valid identity and device posture is rejected.
- Session/token configuration and test evidence showing reauthentication or access reduction after a risk change.
- Access logs recording authentication, authorization decisions, privileged actions, denials, and risk-triggered challenges.
- Approved security-assurance deviation where any requirement cannot be met.

## Assumptions and limits

The portal’s deployment platform, data classification, user population, existing identity provider, and current control configuration were not verified. Technology-specific controls may add requirements beyond this Zero Trust baseline. The initial governance search returned other knowledge documents concerning databases, Kubernetes, integration platforms, pipelines, logging, and Azure networking; these were set aside because they were technology-specific or tangential to the minimum portal baseline.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AUTH-M-001**](https://verify.example-org.internal/?id=AUTH-M-001) | Critical | Authentication | CIS_CONTROLS (CIS 17, CIS 5, CIS 6); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-287, CWE-798); GDPR (Article 7); ISO_27001 (A.5.16, A.5.17, A.5.24); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**AUTH-M-002**](https://verify.example-org.internal/?id=AUTH-M-002) | Critical | Authentication | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-287); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +9 more |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**SAML-M-001**](https://verify.example-org.internal/?id=SAML-M-001) | Critical | SAML Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); NIST_SSDF (PS.3.1, PW.4.1); +8 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
| [**ZTA-M-001**](https://verify.example-org.internal/?id=ZTA-M-001) | Critical | Zero Trust Architecture | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); COBIT_2019 (APO12.01, DSS05.04, EDM03.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); MITRE_ATT&CK (M1035); +9 more |
| [**ZTA-M-002**](https://verify.example-org.internal/?id=ZTA-M-002) | High | Zero Trust Architecture | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); COBIT_2019 (APO12.01, DSS05.04, EDM03.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); MITRE_ATT&CK (M1035); +9 more |
| [**ZTA-M-003**](https://verify.example-org.internal/?id=ZTA-M-003) | High | Zero Trust Architecture | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); COBIT_2019 (APO12.01, DSS05.04, DSS05.07); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); MITRE_ATT&CK (M1035); +9 more |
| [**ZTA-M-004**](https://verify.example-org.internal/?id=ZTA-M-004) | Critical | Zero Trust Architecture | CIS_CONTROLS (CIS 12); COBIT_2019 (APO12.01, EDM03.01); CWE (CWE-284); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.20); MITRE_ATT&CK (M1035); +9 more |

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