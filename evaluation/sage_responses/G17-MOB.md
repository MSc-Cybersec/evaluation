# G17-MOB

## Question
Are backend controls enough without mobile-app hardening?

## Sage response

## Bottom line

No. Backend controls remain the authoritative security boundary, but they do not protect data stored or displayed on the device, prevent app repackaging, secure device-held credentials, or stop interception and runtime manipulation. SAGF therefore requires mobile-app hardening in addition to backend controls; release should be blocked where applicable Critical or High mobile Mandards are unmet.

## Risk and impact

The principal exposure is **Critical**: authentication tokens or PII may be extracted, traffic intercepted, applications repackaged, and sensitive transactions performed without re-authentication. High-risk gaps also expose screen content, logs, clipboard data, caches, and platform-integrity mechanisms.

Backend validation can limit the effect of a compromised client, but it cannot remediate compromise occurring entirely on the device.

## Governing mandards

| Mandard | Required control | Risk |
|---|---|---:|
| Per **MOB-M-002**: use hardware-backed Keychain or Keystore storage for sensitive data. | Secure Keychain/Keystore Storage with Hardware Backing | **Critical** |
| Per **MOB-M-004**: enforce certificate pinning for application backend connections. | Certificate Pinning Enforced | **Critical** |
| Per **MOB-M-005**: enable obfuscation, secure app signing, dependency scanning, SBOM management, and signature verification. | Code Obfuscation, Dependency Security & App Signing | **Critical** |
| Per **MOB-M-008**: require biometric or strong re-authentication for sensitive operations. | Biometric & Re-authentication Controls | **Critical** |
| Per **MOB-M-003**: protect task-switcher content, logging, clipboard use, and cached sensitive information. | No Sensitive Data in Task Switcher & Screen Content Protection | **High** |
| Per **MOB-M-009**: implement Play Integrity, StrongBox or TEE-backed keys, and release-build obfuscation on Android. | Android Platform Security Controls | **High** |
| Per **MOB-M-010**: implement App Attest, Secure Enclave, jailbreak protection, and deep-link validation on iOS. | iOS Platform Security Controls | **High** |
| Per **MOB-M-011**: check application versions and force upgrades for critical security patches. | Mobile App Update & Forced Upgrade Enforcement | **Medium** |
| Per **MOB-M-001**: enable iOS ATS and associated platform protections. | iOS ATS Enabled & Platform Security Controls | **Low** |
| Per **MOB-M-006**: detect tampering, rooting, jailbreaking, and emulator execution, with an appropriate security response. | Anti-Tampering, Root/Jailbreak Detection & Emulator Protection | **Low** |
| Per **MOB-M-007**: disable debugging in release builds and employ anti-debugging measures. | Anti-Debugging Enabled | **Low** |

## Framework mapping

The following mappings were returned by the SAGF catalogue; this is not presented as an exhaustive mapping set.

| Mandards | Framework controls returned |
|---|---|
| **MOB-M-001**, **MOB-M-004**, **MOB-M-006**, **MOB-M-007**, **MOB-M-011** | NIST SP 800-53 Rev.5 `SC-8`, `SC-18`, `AC-19` |
| **MOB-M-002**, **MOB-M-009**, **MOB-M-010** | NIST SP 800-53 Rev.5 `SC-12`, `SC-13`, `SC-28`, `SI-12`, `MP-4` |
| **MOB-M-003** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-4`, `AC-6`, `AU-2`, `AU-6`, `AU-12` |
| **MOB-M-005** | NIST SP 800-53 Rev.5 `AC-4`, `SC-8`, `AU-2`, `AU-6`, `AU-12`, `SI-4` |
| **MOB-M-008** | NIST SP 800-53 Rev.5 `IA-2`, `IA-4`, `IA-5`, `IA-8`, `AC-2`, `AC-3`, `AC-4`, `AC-6`, `AC-7` |
| **MOB-M-007** | ISO/IEC 27001:2022 `A.8.16`; SOC 2 `CC7.2` |
| **MOB-M-009**, **MOB-M-010** | PCI DSS v4.0 `Req 3`; **MOB-M-010** also maps to `Req 4` |
| Mobile Mandards above | Returned OWASP Mobile Top 10:2024 mappings include `M1`, `M3`, `M4`, `M5`, `M7`, `M8`, `M9`, and `M10`, depending on the Mandard |

## Required actions

1. **Mobile engineering — Critical:** implement hardware-backed secure storage, certificate pinning, protected signing and dependency controls, and re-authentication for sensitive operations per **MOB-M-002**, **MOB-M-004**, **MOB-M-005**, and **MOB-M-008**.
2. **Mobile engineering — High:** prevent screen, log, clipboard, and cache leakage per **MOB-M-003**; implement the applicable Android or iOS platform controls per **MOB-M-009** and **MOB-M-010**.
3. **Release engineering — Medium:** enforce minimum supported versions and mandatory security upgrades per **MOB-M-011**.
4. **Mobile engineering — Low:** complete ATS, anti-tampering, compromised-device detection, and anti-debugging controls per **MOB-M-001**, **MOB-M-006**, and **MOB-M-007**.
5. **Security engineering:** gate release builds on mobile SAST/MAST, dependency, signing, storage, pinning, and runtime-manipulation tests as identified in the cited Mandards.
6. **Advisory (not catalogue-backed):** keep authorization, transaction validation, rate limiting, fraud controls, and integrity-token verification server-side. Never treat mobile hardening as permission to trust client-supplied decisions.

The native-application guidance document **VeriFy-AUTH-NAT-001** ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981070)) identifies application-specific authentication, password protection, MFA assessment, and account lockout considerations. It is mapped to **AUTH-M-003**, **GOV-G-006**, **MOB-M-002**, **MOB-M-004**, **MOB-M-008**, and **OAUTH-M-001**; any deviation must be recorded in the SAF pack with technical justification.

## Evidence for audit

- Signed production `.apk`, `.aab`, or `.ipa` and signature-verification result.
- Passing mobile SAST/MAST report covering storage, pinning, leakage, debuggability, tampering, root/jailbreak, and platform controls.
- SBOM and dependency vulnerability scan.
- CI/CD gates proving release obfuscation, non-debuggable configuration, and secure signing.
- Dynamic tests demonstrating pinning enforcement, sensitive-operation re-authentication, compromised-device response, and forced-upgrade behaviour.
- Android Play Integrity or iOS App Attest server-validation records, as applicable.
- Approved SAF deviation record for any unmet Mandard.

## Assumptions and limits

No application, backend design, mobile binary, pipeline configuration, or scan evidence was reviewed. Applicability between Android and iOS must be determined from the actual supported platforms.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**MOB-M-001**](https://verify.example-org.internal/?id=MOB-M-001) | Low | Mobile Security | NIST_SP_800_53 (AC-19, SC-18, SC-8); OWASP_CHEATSHEETS (DOM based XSS Prevention); OWASP_MOBILE (M10:2024, M1:2024, M3:2024); TOGAF (Application Security) |
| [**MOB-M-002**](https://verify.example-org.internal/?id=MOB-M-002) | Critical | Mobile Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327, CWE-798); GDPR (Article 17, Article 25, Article 32); HIPAA (164.312(a)(2)(iv), 164.502); ISO_27001 (A.5.17, A.5.34, A.8.11); +9 more |
| [**MOB-M-003**](https://verify.example-org.internal/?id=MOB-M-003) | High | Mobile Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 3, CIS 6, CIS 8); COBIT_2019 (APO12.01, DSS05.07, EDM03.01); CWE (CWE-284, CWE-285); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.312(b), 164.502); +11 more |
| [**MOB-M-004**](https://verify.example-org.internal/?id=MOB-M-004) | Critical | Mobile Security | NIST_SP_800_53 (AC-19, SC-18, SC-8); OWASP_CHEATSHEETS (DOM based XSS Prevention); OWASP_MOBILE (M10:2024, M1:2024, M3:2024); TOGAF (Application Security) |
| [**MOB-M-005**](https://verify.example-org.internal/?id=MOB-M-005) | Critical | Mobile Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AC-19, AC-4, AU-12); +11 more |
| [**MOB-M-006**](https://verify.example-org.internal/?id=MOB-M-006) | Low | Mobile Security | CIS_CONTROLS (CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ISO_27001 (A.8.16); NIST_CSF (DE.AE-02, DE.CM-01); NIST_SP_800_53 (AC-19, AU-6, SC-18); OWASP_CHEATSHEETS (DOM based XSS Prevention); +4 more |
| [**MOB-M-007**](https://verify.example-org.internal/?id=MOB-M-007) | Low | Mobile Security | CIS_CONTROLS (CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ISO_27001 (A.8.16); NIST_CSF (DE.AE-02, DE.CM-01); NIST_SP_800_53 (AC-19, AU-6, SC-18); OWASP_CHEATSHEETS (DOM based XSS Prevention); +4 more |
| [**MOB-M-008**](https://verify.example-org.internal/?id=MOB-M-008) | Critical | Mobile Security | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (PR.AA-01, PR.AA-05); +7 more |
| [**MOB-M-009**](https://verify.example-org.internal/?id=MOB-M-009) | High | Mobile Security | CIS_CONTROLS (CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); NIST_SP_800_53 (AC-19, MP-4, SC-12); +7 more |
| [**MOB-M-010**](https://verify.example-org.internal/?id=MOB-M-010) | High | Mobile Security | CIS_CONTROLS (CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); NIST_SP_800_53 (AC-19, MP-4, SC-12); +7 more |
| [**MOB-M-011**](https://verify.example-org.internal/?id=MOB-M-011) | Medium | Mobile Security | NIST_SP_800_53 (AC-19, SC-18, SC-8); OWASP_CHEATSHEETS (DOM based XSS Prevention); OWASP_MOBILE (M10:2024, M1:2024, M3:2024); TOGAF (Application Security) |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |

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