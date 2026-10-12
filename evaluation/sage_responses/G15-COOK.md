# G15-COOK

## Question
What cookie controls are required for session-bearing web applications?

## Sage response

## Bottom line

Session-bearing web applications must enforce secure cookie attributes and robust session-token lifecycle controls. Specifically, session cookies require `HttpOnly`, `Secure`, and `SameSite=Strict`, a narrowly scoped path and non-wildcard domain; session identifiers must also be cryptographically random, generic in name, and rotated after authentication or privilege changes. Failure exposes the application to session theft, fixation, reuse, cross-site request forgery and account takeover.

## Risk and impact

| Priority | Exposure | Business impact |
|---|---|---|
| Critical | Missing or weak cookie attributes permit JavaScript access, insecure transmission, cross-site requests, and unnecessarily broad cookie exposure. | Session compromise, unauthorized transactions, data exposure and account takeover. |
| High | Predictable, unrotated or reusable session identifiers enable session fixation and continued use of stolen sessions. | Unauthorized authenticated access and privilege misuse. |

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **COOK-M-001** | Secure Cookie Attributes (HttpOnly, Secure, SameSite) | Critical | Per **COOK-M-001**: every session cookie must use `HttpOnly`, `Secure`, and `SameSite=Strict`; its `Path` must be application-specific rather than `/`, and its `Domain` must not be wildcarded. |
| **COOK-M-002** | Cookie Theft Prevention & Rotation | High | Per **COOK-M-002**: session identifiers must use at least 256 bits of cryptographically secure randomness, have generic rather than application-revealing names, and rotate after login and privilege changes. |

## Framework mapping

The following directly relevant mappings were returned by the catalogue:

| Mandard | Framework | Mapped controls |
|---|---|---|
| **COOK-M-001** | NIST SP 800-53 Rev. 5 | CM-6 Configuration Settings; SA-11 Developer Testing and Evaluation; SC-8 Transmission Confidentiality and Integrity; AC-12 Session Termination; SC-23 Session Authenticity |
| **COOK-M-001** | PCI DSS v4.0 | Req 6 Develop and Maintain Secure Systems |
| **COOK-M-001** | ISO/IEC 27001:2022 | A.8.26 Application security requirements; A.8.28 Secure coding |
| **COOK-M-001** | OWASP ASVS 5.0 | V7 Session Management; V13 Configuration |
| **COOK-M-001** | CIS Controls v8 | CIS 16 Application Software Security |
| **COOK-M-002** | NIST SP 800-53 Rev. 5 | IA-5 Authenticator Management; SA-11 Developer Testing and Evaluation; AC-12 Session Termination; SC-23 Session Authenticity |
| **COOK-M-002** | PCI DSS v4.0 | Req 6 Develop and Maintain Secure Systems; Req 8 Identify Users and Authenticate Access; Req 10 Log and Monitor All Access |
| **COOK-M-002** | ISO/IEC 27001:2022 | A.5.17 Authentication information; A.8.5 Secure authentication; A.8.15 Logging; A.8.16 Monitoring activities |

## Required actions

1. **Application owner — enforce cookie attributes centrally.**  
   Per **COOK-M-001**, configure the session framework or gateway so every session cookie is issued with:
   - `HttpOnly`
   - `Secure`
   - `SameSite=Strict`
   - An application-specific path, such as `/app`, rather than `/`
   - A host-specific or otherwise non-wildcard domain

   Example:

   ```http
   Set-Cookie: SESSIONID=<opaque-value>; Path=/app; Secure; HttpOnly; SameSite=Strict
   ```

2. **Application engineering — strengthen session identifiers.**  
   Per **COOK-M-002**:
   - Generate session identifiers using a cryptographically secure random generator with at least 256 bits of randomness.
   - Use a generic cookie name such as `SESSIONID`; do not expose product, framework or application details through the name.
   - Do not encode sensitive or predictable information in the identifier.

3. **Application engineering — rotate sessions at trust changes.**  
   Per **COOK-M-002**:
   - Regenerate the session identifier immediately after successful login.
   - Regenerate it after any privilege or role elevation.
   - Immediately invalidate the previous identifier so replay produces `401` or `403`.
   - Apply absolute and idle session timeouts through the session manager.

4. **DevSecOps — implement release gates.**  
   Per **COOK-M-001** and **COOK-M-002**, automate tests that:
   - Inspect every relevant `Set-Cookie` response.
   - Fail when required attributes, path restrictions or domain restrictions are absent.
   - Compare identifiers before and after login and privilege changes.
   - Attempt replay with the old identifier and fail the release if it remains valid.
   - Validate identifier entropy using an approved session-analysis tool.

## Evidence for audit

Retain:

- HTTP response captures demonstrating compliant `Set-Cookie` headers.
- Framework or middleware configuration enforcing cookie attributes globally.
- Automated pipeline results covering cookie flags, path and domain scope.
- Test results proving session identifiers change after login and privilege changes.
- Replay-test results proving old identifiers are rejected.
- Session entropy or randomness analysis showing at least 256-bit secure generation.
- Timeout configuration and associated automated tests.

## Assumptions and limits

No application configuration or runtime traffic was supplied, so actual compliance was not verified. No knowledge document currently references **COOK-M-001** or **COOK-M-002**; implementation steps above are catalogue-derived rather than knowledge-document-backed.

The remediation text for **COOK-M-001** mentions `SameSite=Strict` or `Lax`, but the mandard requirement explicitly states `SameSite=Strict`. Use `Strict` to demonstrate compliance unless the mandard is formally revised or an approved deviation exists.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**COOK-M-001**](https://verify.example-org.internal/?id=COOK-M-001) | Critical | Cookie Security | CIS_CONTROLS (CIS 16); CWE (CWE-384, CWE-77, CWE-79); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-12, CM-6, SA-11); OWASP (A02:2025, A05:2025); +5 more |
| [**COOK-M-002**](https://verify.example-org.internal/?id=COOK-M-002) | High | Cookie Security | CIS_CONTROLS (CIS 16, CIS 5, CIS 6); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-384); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |

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