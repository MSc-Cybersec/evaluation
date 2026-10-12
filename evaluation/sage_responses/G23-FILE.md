# G23-FILE

## Question
What file-upload governance checks are mandatory for public endpoints?

## Sage response

## Bottom line

The catalogue contains no dedicated Mandard for file-upload validation, malware scanning, extension/MIME allowlisting, file-size limits, filename handling, quarantine, or storage isolation. Public upload APIs must nevertheless enforce transport encryption, rate limiting, the API security baseline, and API audit logging; authentication and deny-by-default authorization are additionally mandatory when the upload operation is sensitive.

Do not approve a public upload endpoint on the strength of the catalogue alone without documented file-specific controls. Any departure from an applicable Mandard requires an approved, time-bounded deviation before release.

## Risk and impact

| Exposure | Applicable requirement | Risk |
|---|---|---:|
| Resource exhaustion or upload flooding | Per **API-M-006**: public API endpoints must rate-limit and return `429 Too Many Requests` when flooded. | Critical |
| Interception or modification in transit | Per **CRYPT-M-002**: all data in transit must use TLS 1.3 or higher, with deprecated protocols and weak ciphers disabled. | Critical |
| Unauthenticated sensitive uploads | Per **API-M-005**: sensitive APIs must reject requests without valid authentication using `401` or `403`. | Critical |
| Unauthorized state changes or cross-tenant access | Per **AC-M-001**: sensitive and state-changing endpoints must use explicit, deny-by-default authorization. | Critical |
| API misconfiguration and information leakage | Per **API-M-008**: enforce security headers, restricted CORS, allowed HTTP methods, generic errors, and managed API versions. | High |
| Missing forensic trail | Per **API-M-010**: log every API call in structured form and forward logs to the SIEM. | High |
| Recurring authorization defects | Per **AC-M-002**: protected paths require positive and negative authorization tests on every build. | High |
| Undocumented control bypass | Per **GOV-G-006**: deviations must be approved, risk-owned, compensated, and time-bounded before release. | High |

Without file-specific validation, an attacker may upload malware, active content, decompression bombs, oversized files, path-manipulating names, or files that become publicly executable. These are material risks, but the retrieved catalogue does not currently establish them as named Mandard requirements.

## Governing mandards

### Directly applicable

| Mandard | Title | Risk | Application to the endpoint |
|---|---|---:|---|
| **API-M-006** | Rate Limiting Enforced | Critical | Mandatory for every public upload API. |
| **CRYPT-M-002** | Encryption in Transit TLS 1.3+ | Critical | Mandatory for uploaded content and associated metadata in transit. |
| **API-M-005** | Auth on Sensitive API | Critical | Mandatory if the upload handles user data or is otherwise sensitive. |
| **AC-M-001** | Mandatory Authorization Checks | Critical | Mandatory for sensitive/state-changing upload operations; deny by default. |
| **API-M-008** | API Security Configuration Baseline | High | Mandatory API baseline, including CORS, headers, methods, errors, and versioning. |
| **API-M-010** | API-Specific Audit Logging & Monitoring | High | Mandatory logging and SIEM forwarding for all API calls. |
| **AC-M-002** | Authorization Testing Automation and Regression | High | Mandatory when the endpoint is protected by authorization. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Mandatory for any control departure before release. |

### Complete API-M catalogue reviewed

The API-domain lookup returned all of the following Mandards. Those not identified above may become applicable according to endpoint behavior, token use, object access, request binding, response data, or message-security design.

| Mandard | Title | Risk |
|---|---|---:|
| **API-M-001** | Broken Object Level Authorization BOLA/IDOR Prevention | Critical |
| **API-M-002** | Excessive Data Exposure Prevention | Critical |
| **API-M-003** | Broken Function Level Authorization BFLA | Critical |
| **API-M-004** | Mass Assignment Protection | Critical |
| **API-M-005** | Auth on Sensitive API | Critical |
| **API-M-006** | Rate Limiting Enforced | Critical |
| **API-M-007** | JWT Signature Validation | Critical |
| **API-M-008** | API Security Configuration Baseline | High |
| **API-M-009** | API Inventory & Versioning Management | High |
| **API-M-010** | API-Specific Audit Logging & Monitoring | High |
| **API-M-011** | GraphQL Query Complexity Limits | Critical |
| **API-M-012** | Disable Introspection in Production | High |
| **API-M-013** | Message-Level Integrity and Confidentiality | High |

## Framework mapping

Only mappings returned by the catalogue are stated below.

| Mandard | Framework mappings |
|---|---|
| **AC-M-001** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, IA-2 |
| **AC-M-002** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, CM-3, SA-15, SC-5, SC-7; PCI DSS v4.0: Requirements 1, 7, 11; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3, A.8.20, A.8.22, A.8.25, A.8.29, A.8.31, A.8.32; OWASP ASVS 5.0: V8 |
| **CRYPT-M-002** | NIST SP 800-53 Rev. 5: AC-4, MP-4, SC-5, SC-7, SC-12, SC-13, SC-28, SI-12; PCI DSS v4.0: Requirements 1, 3, 4; ISO/IEC 27001:2022: A.5.14, A.5.34, A.8.20, A.8.22, A.8.24; GDPR: Article 32; OWASP ASVS 5.0: V11, V12, V14 |
| **GOV-G-006** | NIST SP 800-53 Rev. 5: CA-5, PL-2, PM-4, RA-3; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; COBIT 2019: APO12.01, MEA02; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |

## Required actions

1. **Rate-limit the public endpoint.**  
   Per **API-M-006**, configure throttling at the gateway or application and verify that flooding eventually produces `429 Too Many Requests`. Apply limits to request frequency and, as an additional file-specific safeguard, uploaded bytes and concurrent uploads.

2. **Require TLS 1.3 or higher.**  
   Per **CRYPT-M-002**, reject plaintext traffic and disable deprecated TLS protocols and weak ciphers.

3. **Classify the endpoint as sensitive or intentionally anonymous.**  
   Per **API-M-005** and **AC-M-001**, sensitive uploads must require authentication and explicit, deny-by-default authorization. Anonymous access is not an acceptable classification for an endpoint that exposes user data, protected storage, administrative functions, or unrestricted state changes.

4. **Apply the API baseline.**  
   Per **API-M-008**, restrict CORS to approved origins where applicable, allow only necessary HTTP methods, prevent stack traces and infrastructure details from reaching clients, apply required security headers, and manage the API version.

5. **Create a complete audit trail.**  
   Per **API-M-010**, record timestamp, method, endpoint, authenticated identity or anonymous status, sanitized parameters, response code, response time, authentication failures, authorization denials, and correlation ID in structured JSON. Forward the records to the centralized SIEM; do not log file contents, tokens, passwords, or other sensitive payload data.

6. **Test protected upload paths in CI/CD.**  
   Per **AC-M-002**, include positive and negative tests for every protected operation, including unauthenticated use, insufficient privilege, cross-user or cross-tenant access, and regressions of previously fixed defects. Block the merge when tests fail.

7. **Implement file-specific controls before release.**  
   No knowledge document was found for this point. **Advisory (not knowledge-doc backed):**
   - Use a server-side allowlist of permitted file types.
   - Validate extension, declared MIME type, and detected file signature; reject mismatches.
   - Enforce request, file, decompressed-content, and file-count limits before fully buffering content.
   - Stream uploads into a non-executable quarantine area.
   - Perform malware scanning and, where appropriate, content disarm and reconstruction before release.
   - Generate server-side object names; do not use client filenames as storage paths.
   - Normalize names and reject traversal, control characters, double extensions, and unsafe archive entries.
   - Store files outside the web root with private access and encryption at rest.
   - Serve downloads through an authorized broker using safe `Content-Type` and `Content-Disposition` headers.
   - Prevent public access until validation and scanning complete; define retention and secure deletion rules.

8. **Record any exception before deployment.**  
   Per **GOV-G-006**, an exception must identify the affected Mandard, technical justification, residual risk owner, compensating controls, independent approver, and expiry date.

**Implementation guidance:** The REST API guardrail requires least-privilege authorization at API endpoints and rate limiting for external provider patterns. It also requires formal recording of non-compliance in the assurance pack. Source: **VeriFy-INT-REST-001**, mapped to **AC-M-001**, **API-M-005**, **API-M-006**, **API-M-007**, **API-M-013**, **CONT-M-005**, **CRYPT-M-002**, **GOV-G-006**, **MSA-M-001**, and **OAUTH-M-001** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

## Evidence for audit

- Gateway or middleware configuration showing upload-endpoint rate limits.
- Automated flood-test result demonstrating `429 Too Many Requests`.
- TLS scan proving TLS 1.3+ and absence of deprecated protocols or weak ciphers.
- OpenAPI specification identifying whether the endpoint is anonymous or protected.
- Authentication and authorization configuration for sensitive uploads.
- CI results covering unauthenticated, unauthorized, cross-user, and cross-tenant attempts.
- API baseline scan covering headers, CORS, HTTP methods, error leakage, and versioning.
- Structured audit-log samples with correlation IDs and evidence of SIEM ingestion.
- File-validation and malware-scanning test results, including malformed, mismatched, oversized, archived, and infected samples.
- Storage policy proving quarantine, non-executable private storage, retention, and deletion settings.
- Approved, unexpired deviation record where any applicable Mandard is not met.

## Assumptions and limits

No dedicated file-upload Mandard or file-upload implementation knowledge document was found in the searches performed. Therefore, extension/MIME/signature validation, malware scanning, quarantine, filename normalization, archive handling, storage isolation, and file-size controls are identified as advisory safeguards rather than catalogue-backed mandatory requirements. Applicability of authentication and authorization depends on whether the upload operation is sensitive; that classification was not provided.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**AC-M-002**](https://verify.example-org.internal/?id=AC-M-002) | High | Access Control | CIS_CONTROLS (CIS 12, CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.PS-06); +9 more |
| [**API-M-001**](https://verify.example-org.internal/?id=API-M-001) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); GDPR (Article 15); HIPAA (164.312(a)(1), 164.524); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); +9 more |
| [**API-M-002**](https://verify.example-org.internal/?id=API-M-002) | Critical | API Security | CCPA_CPRA (Consumer Right to Delete, Consumer Right to Know, Data Minimization); CIS_CONTROLS (CIS 16, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-20, CWE-200, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.502); +11 more |
| [**API-M-003**](https://verify.example-org.internal/?id=API-M-003) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +7 more |
| [**API-M-004**](https://verify.example-org.internal/?id=API-M-004) | Critical | API Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-20, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.DS-01); +10 more |
| [**API-M-005**](https://verify.example-org.internal/?id=API-M-005) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (AIS); CWE (CWE-306, CWE-798); ISO_27001 (A.5.16, A.5.17, A.8.24); NIST_CSF (PR.AA-01, PR.AA-05, PR.DS-01); +8 more |
| [**API-M-006**](https://verify.example-org.internal/?id=API-M-006) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 5); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.24); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, AU-12); +8 more |
| [**API-M-007**](https://verify.example-org.internal/?id=API-M-007) | Critical | API Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**API-M-008**](https://verify.example-org.internal/?id=API-M-008) | High | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-77, CWE-79); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, IR-4); +8 more |
| [**API-M-009**](https://verify.example-org.internal/?id=API-M-009) | High | API Security | CCPA_CPRA (Consumer Right to Know, Notice at Collection); CIS_CONTROLS (CIS 16); GDPR (Article 12, Article 13, Article 20); ISO_27001 (A.5.9, A.8.26, A.8.28); NIST_CSF (ID.AM, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, SA-11, SC-18); +8 more |
| [**API-M-010**](https://verify.example-org.internal/?id=API-M-010) | High | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 5); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-20, CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +9 more |
| [**API-M-011**](https://verify.example-org.internal/?id=API-M-011) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, IR-4); OWASP (A02:2025); +7 more |
| [**API-M-012**](https://verify.example-org.internal/?id=API-M-012) | High | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 6); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.5.24); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); +9 more |
| [**API-M-013**](https://verify.example-org.internal/?id=API-M-013) | High | API Security | ISO_27001 (A.5.14, A.8.24); NIST_CSF (PR.AA, PR.DS); NIST_SP_800_53 (SC-13, SC-23, SC-8); OWASP_ASVS (V11, V14); SOC2 (CC6) |

Showing 15 of 19 cited mandards.

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