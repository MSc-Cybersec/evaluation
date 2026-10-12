# G56-RTC

## Question
What controls are required for real-time communications carrying sensitive data?

## Sage response

## Bottom line

Real-time communications carrying sensitive data must apply the SAGF baseline for data classification, encryption in transit, strong privileged authentication, least-privilege access, session security, key lifecycle management, secrets protection, and governed exceptions. The catalogue does not contain a real-time-communications-specific Mandard for WebRTC, RTP/SRTP, voice, or video; therefore, protocol-specific media protections require an approved security design, and any departure from the baseline must be recorded before release.

## Risk and impact

The principal exposure is interception of signalling or media, unauthorised meeting or channel access, session hijacking, misuse of recording privileges, and compromise of cryptographic credentials.

| Priority | Exposure |
|---|---|
| Critical | Unencrypted traffic, compromised privileged accounts, excessive service permissions, or exposed credentials could disclose live conversations and sensitive content. |
| High | Weak session controls, unmanaged key lifecycles, incorrect data handling, or undocumented exceptions increase breach duration and regulatory exposure. |
| Unverified | The catalogue does not define a specific risk level or control for SRTP, WebRTC, TURN/STUN, recording consent, or end-to-end encryption. |

## Governing mandards

| Mandard | Required control | Risk |
|---|---|---:|
| **CRYPT-M-002**, Encryption in Transit TLS 1.3+ | Per **CRYPT-M-002**: encrypt all HTTPS, gRPC, and internal service-to-service traffic using TLS 1.3 or higher; disable weak ciphers and deprecated protocols. | Critical |
| **AUTH-M-002**, Multi-Factor Authentication MFA Enforcement | Per **AUTH-M-002**: privileged accounts must use MFA, preferably hardware keys or TOTP; SMS is fallback only. | Critical |
| **IAM-M-001**, Least-Privilege IAM Policies | Per **IAM-M-001**: production roles must be narrowly scoped; wildcard actions and resources are prohibited. | Critical |
| **SECR-M-001**, No Hardcoded Secrets | Per **SECR-M-001**: builds must fail when high-confidence secrets are detected in source or configuration. | Critical |
| **DATA-M-002**, Data Classification and Handling | Per **DATA-M-002**: services must declare data sensitivity and apply classification-based controls to storage, transit, retention, and DLP. | High |
| **AUTH-M-003**, Session Management and Timeout Controls | Per **AUTH-M-003**: sessions must have a maximum eight-hour absolute timeout and 15-minute idle timeout, with invalidation after logout, password change, or role change. | High |
| **CRYPT-M-003**, Key Rotation and Lifecycle Management | Per **CRYPT-M-003**: key generation, rotation, revocation, and destruction must be documented and automated; static keys must rotate at least annually and dynamic keys more frequently. | High |
| **GOV-G-006**, Security Deviation and Exception Management | Per **GOV-G-006**: departures must be independently approved before release, with justification, residual-risk owner, compensating controls, and an expiry date. | High |

No dedicated RTC Mandard was found. In particular, the catalogue search did not establish requirements for media-layer encryption, end-to-end encryption, TURN/STUN security, recording consent, or participant identity verification.

## Framework mapping

The following are catalogue-returned mappings; they are not independent assessments of compliance.

| Mandard | Selected returned mappings |
|---|---|
| **CRYPT-M-002** | NIST SP 800-53 SC-12, SC-13, SC-7, AC-4; PCI DSS Req 4; ISO/IEC 27001:2022 A.8.24, A.8.20, A.5.14; GDPR Article 32; OWASP ASVS V11, V12, V14 |
| **AUTH-M-002** | NIST SP 800-53 IA-2, IA-5, AC-3, AC-6; PCI DSS Req 7 and Req 8; ISO/IEC 27001:2022 A.8.5, A.5.15, A.8.2; OWASP ASVS V6 and V8 |
| **IAM-M-001** | NIST SP 800-53 AC-2, AC-3, AC-6; PCI DSS Req 7; ISO/IEC 27001:2022 A.5.15, A.5.18, A.8.2, A.8.3; OWASP ASVS V8 |
| **DATA-M-002** | NIST SP 800-53 SC-28, SI-12, SI-4, AU-6; ISO/IEC 27001:2022 A.5.12, A.5.13, A.8.16; PCI DSS Req 3 |
| **AUTH-M-003** | NIST SP 800-53 AC-12, SC-23, AU-2, AU-12; PCI DSS Req 8 and Req 10; ISO/IEC 27001:2022 A.8.15 and A.8.16 |
| **CRYPT-M-003** | NIST SP 800-53 SC-12 and SC-13; PCI DSS Req 3 and Req 4; ISO/IEC 27001:2022 A.8.24; GDPR Article 32 |
| **GOV-G-006** | NIST SP 800-53 CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022 A.5.1 and A.5.35; NIST CSF 2.0 GV.RM, GV.OV, ID.RA |

## Required actions

1. **Classify the communication data.**  
   The service owner must document whether audio, video, screen sharing, chat, signalling metadata, transcripts, recordings, and diagnostics contain PII, regulated, confidential, or internal information. Apply transit, storage, retention, and DLP rules based on that classification per **DATA-M-002**.

2. **Encrypt every signalling and service path.**  
   Enforce TLS 1.3 or higher for signalling, authentication, APIs, WebSockets, service-to-service calls, administrative interfaces, and recording transfer paths per **CRYPT-M-002**. Reject protocol downgrade and weak cipher suites.

3. **Protect the media path.**  
   **Advisory (not catalogue-backed):** TLS protection of signalling does not itself protect RTP media. For WebRTC or similar systems, require authenticated SRTP using DTLS-SRTP; secure TURN access with short-lived credentials; and determine whether end-to-end media encryption is required from the threat model.  
   **No knowledge document was found for this point.**

4. **Enforce identity and meeting/channel authorisation.**  
   Apply least-privilege roles for participants, hosts, moderators, recording operators, support staff, bots, and service accounts per **IAM-M-001**. Require MFA for administrators, developers, DevOps personnel, and other privileged accounts per **AUTH-M-002**.

5. **Constrain sessions and tokens.**  
   Apply the eight-hour absolute and 15-minute idle limits, rotate session identifiers after authentication, and revoke sessions following logout, password change, or role change per **AUTH-M-003**. Authorisation must be re-evaluated when a participant joins, changes role, starts recording, or accesses stored content.

6. **Manage certificates and cryptographic keys centrally.**  
   Automate generation, rotation, revocation, expiry monitoring, and destruction per **CRYPT-M-003**. The implementation guidance directs teams to enterprise certificate and key-management standards and covers internal/public certificates and TLS lifecycle management: **VeriFy-IS-CERT-001**, mapped to **CRYPT-M-002**, **CRYPT-M-003**, **CRYPT-M-004**, **CRYPT-M-005**, **CRYPT-M-006**, **CFG-M-001**, and **GOV-G-006** ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659948009)).

7. **Keep credentials out of source and configuration.**  
   Store API credentials, TURN credentials, signing keys, private keys, and integration secrets in an approved secret-management service. Block commits and builds containing secrets per **SECR-M-001**.

8. **Protect recordings, transcripts, and chat exports.**  
   Apply classification-driven encryption, retention, masking, and access controls per **DATA-M-002**. The data-security guidance requires encrypted data-in-transit and classification-dependent storage and backup controls: **VeriFy-DATA-GEN-003**, mapped to **CRYPT-M-002**, **DATA-M-001**, **DATA-M-002**, **DB-M-002**, **DB-M-004**, **DB-M-006**, and **GOV-G-006** ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947951)).

9. **Use approved enterprise identity patterns.**  
   For staff access, the guidance identifies enterprise identity providers, SAML/OIDC over protected channels, MFA, SSO where feasible, and short-lived access/session lifetimes: **VeriFy-AUTH-INT-EC-001**, mapped to **AUTH-M-001**, **AUTH-M-002**, **AUTH-M-003**, **CRYPT-M-002**, **IAM-M-001**, **OAUTH-M-001**, **SAML-M-001**, **SECR-M-001**, and **GOV-G-006** ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445334)).

10. **Govern any unsupported protocol or legacy integration.**  
    If a client, carrier, gateway, or conferencing provider cannot meet a mandated control, block release unless an approved, unexpired deviation exists under **GOV-G-006**.

## Evidence for audit

- Data inventory and service manifest containing the approved classification and retention rules.
- TLS scan results for signalling, API, administrative, and service endpoints showing accepted protocol versions and cipher suites.
- Packet-capture or platform test proving media confidentiality; where applicable, evidence of SRTP negotiation and authenticated key exchange.
- IAM role definitions and access-review records demonstrating least privilege and absence of production wildcards.
- Identity-provider policy exports proving privileged-user MFA.
- Session tests showing idle timeout, absolute timeout, token rotation, and invalidation events.
- Certificate inventory, expiry alerts, key-rotation logs, revocation records, and KMS or vault configuration.
- CI/CD secret-scanning results showing a blocking gate for high-confidence findings.
- Recording and transcript configuration showing encryption, restricted access, deletion schedules, and disabled recording where it is not authorised.
- Approved architecture/security review and penetration-test results covering unauthorised joining, role escalation, session replay, media interception, and recording access.
- Any deviation record, including independent approval, residual-risk owner, compensating controls, and expiry date.

## Assumptions and limits

The communication technology, data classification, deployment environment, recording behaviour, and applicable jurisdiction were not specified. No dedicated RTC/WebRTC/voice/video Mandard or RTC-specific knowledge document was found; SRTP, DTLS-SRTP, TURN credential, end-to-end encryption, participant-notification, and recording-consent recommendations are therefore **Advisory (not catalogue-backed)** and should be confirmed through the project security assessment. The catalogue wording for **CRYPT-M-002** requires TLS 1.3 or higher, although some associated implementation text and knowledge guidance also mentions TLS 1.2; the normative Mandard requirement should govern unless an approved **GOV-G-006** deviation applies.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AUTH-M-001**](https://verify.example-org.internal/?id=AUTH-M-001) | Critical | Authentication | CIS_CONTROLS (CIS 17, CIS 5, CIS 6); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-287, CWE-798); GDPR (Article 7); ISO_27001 (A.5.16, A.5.17, A.5.24); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**AUTH-M-002**](https://verify.example-org.internal/?id=AUTH-M-002) | Critical | Authentication | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-287); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +9 more |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**CFG-M-001**](https://verify.example-org.internal/?id=CFG-M-001) | Medium | Configuration | CIS_CONTROLS (CIS 16, CIS 3); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24, A.8.25); +11 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**CRYPT-M-003**](https://verify.example-org.internal/?id=CRYPT-M-003) | High | Cryptography | CIS_CONTROLS (CIS 3); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); +10 more |
| [**CRYPT-M-004**](https://verify.example-org.internal/?id=CRYPT-M-004) | High | Cryptography | CIS_CONTROLS (CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-005**](https://verify.example-org.internal/?id=CRYPT-M-005) | High | Cryptography | CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.13, A.8.14); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-006**](https://verify.example-org.internal/?id=CRYPT-M-006) | High | Cryptography | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04); CSA_CCM (CEK); CWE (CWE-327); DORA (Art. 17-23, Art. 24-27, Art. 28-44); GDPR (Article 32); +14 more |
| [**DATA-M-001**](https://verify.example-org.internal/?id=DATA-M-001) | Medium | Data Protection | AIUC1 (E005); CIS_CONTROLS (CIS 11, CIS 3, CIS 6); CWE (CWE-284, CWE-285, CWE-327); GDPR (Article 32); HIPAA (164.312(a)(1), 164.312(a)(2)(iv)); ISO_27001 (A.5.15, A.5.18, A.5.34); +9 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-002**](https://verify.example-org.internal/?id=DB-M-002) | Critical | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 16, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-327, CWE-798); GDPR (Article 17, Article 25, Article 32); HIPAA (164.312(a)(2)(iv), 164.502); +10 more |
| [**DB-M-004**](https://verify.example-org.internal/?id=DB-M-004) | High | Database Security | CIS_CONTROLS (CIS 12, CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-798); ISO_27001 (A.5.17, A.8.16, A.8.20); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, CM-6); +7 more |
| [**DB-M-006**](https://verify.example-org.internal/?id=DB-M-006) | High | Database Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 17, CIS 3, CIS 6); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.502); +10 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |

Showing 15 of 18 cited mandards.

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