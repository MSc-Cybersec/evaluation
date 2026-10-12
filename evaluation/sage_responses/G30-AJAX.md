# G30-AJAX

## Question
How should async client requests be governed to prevent token leakage?

## Sage response

## Bottom line

Async browser requests must be governed like any other authenticated API call: tokens must not appear in URLs, browser storage, source code, telemetry, or error output; every request must use encrypted transport and server-side token validation. Prefer a backend-for-frontend or `Secure`, `HttpOnly`, `SameSite=Strict` session cookie so JavaScript never handles the token directly. Failure exposes reusable credentials and can result in account takeover and unauthorized data access.

## Risk and impact

The principal exposure is **Critical**: injected scripts, browser extensions, referrer propagation, logs, or weak transport can capture a bearer token and replay it as the user. Over-broad or long-lived tokens increase the blast radius, while missing server-side validation permits forged, expired, or incorrectly scoped tokens.

## Governing mandards

| Mandard | Title | Risk | Governing requirement |
|---|---|---:|---|
| **OAUTH-M-001** | OAuth 2.0 Token Security & Validation | Critical | Per **OAUTH-M-001**: native and SPA clients must use PKCE; access tokens must expire in under one hour, refresh tokens in under 30 days, tokens must not appear in URLs, and servers must validate signature, issuer, audience, expiry, and scopes. |
| **CRYPT-M-002** | Encryption in Transit TLS 1.3+ | Critical | Per **CRYPT-M-002**: client/API traffic must use TLS 1.3 or higher, with deprecated protocols and weak ciphers disabled. |
| **API-M-005** | Auth on Sensitive API | Critical | Per **API-M-005**: every sensitive endpoint must reject requests lacking a valid token with `401` or `403`. |
| **API-M-007** | JWT Signature Validation | Critical | Per **API-M-007**: every received JWT must have its signature validated, and `alg:none` must never be accepted. |
| **AUTH-M-003** | Session Management & Timeout Controls | High | Per **AUTH-M-003**: sessions require a maximum eight-hour absolute timeout, 15-minute idle timeout, and invalidation after logout, password change, or role change. Session cookies must be `Secure`, `HttpOnly`, and `SameSite=Strict`. |
| **OAUTH-M-002** | OAuth 2.0 Scope Limitation & Consent | High | Per **OAUTH-M-002**: tokens must carry minimal, specific scopes; sensitive scope changes require reauthentication, and revocation must invalidate tokens immediately. |
| **SECR-M-001** | No Hardcoded Secrets | Critical | Per **SECR-M-001**: builds must fail when high-confidence secrets are found in source code or configuration. |
| **SECR-M-004** | Short-Lived Credentials & Rotation | Critical | Per **SECR-M-004**: automation and service credentials must be short-lived or regularly rotated; long-lived production automation secrets are prohibited. |

## Framework mapping

The following directly relevant mappings were returned by the SAGF catalogue:

| Mandard | Framework mappings |
|---|---|
| **OAUTH-M-001** | NIST SP 800-53 Rev.5 `IA-2`, `IA-5`, `AC-4`, `SC-8`; PCI DSS v4.0 `Req 8`; ISO/IEC 27001:2022 `A.5.17`, `A.8.5`; OWASP ASVS 5.0 `V4`, `V6`, `V10`; SOC 2 `CC6.1` |
| **OAUTH-M-002** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-6`; PCI DSS v4.0 `Req 7`, `Req 8`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.3` |
| **CRYPT-M-002** | NIST SP 800-53 Rev.5 `SC-7`, `SC-12`, `SC-13`; PCI DSS v4.0 `Req 1`, `Req 4`; ISO/IEC 27001:2022 `A.5.14`, `A.8.20`, `A.8.24`; GDPR `Article 32`; OWASP ASVS 5.0 `V12`, `V14` |
| **AUTH-M-003** | NIST SP 800-53 Rev.5 `AC-12`, `SC-23`; PCI DSS v4.0 `Req 8`; ISO/IEC 27001:2022 `A.8.5`; SOC 2 `CC6.1` |
| **API-M-005**, **API-M-007** | NIST SP 800-53 Rev.5 `IA-2`, `IA-5`, `SA-11`; OWASP mappings returned by the catalogue include authentication-failure and JWT-validation coverage. |

## Required actions

1. **Keep tokens out of JavaScript-accessible persistence.**  
   The preferred browser pattern is a backend-for-frontend with an opaque session cookie configured as `Secure`, `HttpOnly`, and `SameSite=Strict`. The Secrets Management Guardrails state that authentication tokens must not be stored in `localStorage` or `sessionStorage`, exposed in client-side code, or committed to public repositories: **VeriFy-IS-SEC-001**, mapped to **SECR-M-001**, **SECR-M-002**, **SECR-M-003**, **SECR-M-004**, **CRYPT-M-003**, **CRYPT-M-005**, and **GOV-G-006** ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658178205)).

2. **If a SPA must hold an OAuth token, use Authorization Code with PKCE.**  
   Per **OAUTH-M-001**, keep the access token short-lived and memory-only, never place it in query strings, fragments, route state, analytics, or exception messages, and validate it server-side on every request.

3. **Constrain where credentials may be sent.**  
   Centralize `fetch` or HTTP-client construction and permit credentials only for an explicit HTTPS origin allowlist.  
   **Advisory (not knowledge-doc backed):** do not attach `Authorization` headers to arbitrary URLs; reject cross-origin redirects and use restrictive CORS rules rather than wildcard origins with credentials.

4. **Enforce token validation at the API boundary.**  
   Per **OAUTH-M-001** and **API-M-007**, validate signature, allowed algorithm, issuer, audience, expiry, and scope. Per **API-M-005**, deny missing or invalid credentials with `401/403`; never rely on a successful client-side authentication check.

5. **Minimize privilege and lifetime.**  
   Per **OAUTH-M-002**, issue audience-restricted, narrowly scoped tokens. Per **AUTH-M-003**, terminate idle and expired sessions and invalidate them after logout, password changes, or role changes.

6. **Protect transport.**  
   Per **CRYPT-M-002**, enforce TLS 1.3+ from browser to gateway and onward to services. The REST guidance in **VeriFy-INT-REST-001** describes OAuth/JWT, least-privilege endpoint authorization, and encrypted REST integrations ([source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099)); its TLS 1.2 text is superseded by the stricter TLS 1.3+ Mandard requirement.

7. **Prevent accidental disclosure through development and operations tooling.**  
   Per **SECR-M-001**, run secret scanning on commits and pull requests and block releases on detected tokens. Redact request headers and credentials from browser diagnostics, application logs, APM traces, proxy logs, and CI output; rotate and revoke any token found exposed.

## Evidence for audit

- OAuth client configuration proving Authorization Code with PKCE, approved redirect URIs, token lifetimes, scopes, and revocation behavior.
- Browser inspection showing no token in URLs, `localStorage`, `sessionStorage`, source maps, console output, or telemetry.
- `Set-Cookie` evidence showing `Secure`, `HttpOnly`, and `SameSite=Strict`.
- API integration tests proving absent, expired, forged, wrong-audience, and insufficient-scope tokens return `401/403`.
- SAST results proving JWT signature validation and rejection of `alg:none`.
- TLS scan confirming TLS 1.3+ and rejection of deprecated protocols and weak ciphers.
- CI secret-scan report and merge gate demonstrating no embedded tokens or credentials.
- Approved SAF deviation with technical justification where the prescribed guardrails cannot be met.

## Assumptions and limits

“Async client requests” is interpreted as browser-side `fetch`, XMLHttpRequest, or equivalent SPA HTTP calls. CORS restrictions, redirect handling, memory-only token handling, and the backend-for-frontend preference are advisory where not explicitly stated by the cited catalogue or knowledge documents.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**API-M-005**](https://verify.example-org.internal/?id=API-M-005) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (AIS); CWE (CWE-306, CWE-798); ISO_27001 (A.5.16, A.5.17, A.8.24); NIST_CSF (PR.AA-01, PR.AA-05, PR.DS-01); +8 more |
| [**API-M-007**](https://verify.example-org.internal/?id=API-M-007) | Critical | API Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**CRYPT-M-003**](https://verify.example-org.internal/?id=CRYPT-M-003) | High | Cryptography | CIS_CONTROLS (CIS 3); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); +10 more |
| [**CRYPT-M-005**](https://verify.example-org.internal/?id=CRYPT-M-005) | High | Cryptography | CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.13, A.8.14); MITRE_ATT&CK (M1041); +9 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**OAUTH-M-002**](https://verify.example-org.internal/?id=OAUTH-M-002) | High | OAuth Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 3, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.502); +10 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
| [**SECR-M-002**](https://verify.example-org.internal/?id=SECR-M-002) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**SECR-M-003**](https://verify.example-org.internal/?id=SECR-M-003) | High | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); MITRE_ATT&CK (M1039); +12 more |
| [**SECR-M-004**](https://verify.example-org.internal/?id=SECR-M-004) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); MITRE_ATT&CK (M1039); NIST_CSF (GV.SC-01, ID.RA-09, PR.PS-06); +9 more |

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