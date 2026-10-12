# G39-REST

## Question
What governance checks are required before publishing new REST endpoints?

## Sage response

## Bottom line

New REST endpoints must not be published until the API release gate has verified authorization, authentication, data minimisation, input allow-listing, abuse protection, token validation, secure configuration, inventory, logging, and—where applicable—message-level protection. Critical failures under **API-M-001** through **API-M-007** are release blockers; High-risk failures require remediation or a formally recorded deviation before production publication.

## Risk and impact

Failure exposes the organisation to cross-customer data access, privilege escalation, sensitive-data disclosure, unauthorized modification, forged identities, brute-force attacks, denial of service, unmonitored compromise, and unsupported “shadow” endpoints.

| Priority | Pre-publication decision |
|---|---|
| Critical | Do not publish while any applicable Critical Mandard fails. |
| High | Remediate before publication or record and approve a formal security deviation. |
| GraphQL-only | **API-M-011** and **API-M-012** do not apply to a REST-only endpoint. Reassess if GraphQL is introduced. |

## Governing mandards

### Critical REST controls

| Mandard | Title | Risk | Required governance check |
|---|---|---:|---|
| **API-M-001** | Broken Object Level Authorization Prevention | Critical | Per **API-M-001**: every endpoint handling an object identifier must prove that the authenticated principal may access that specific object. |
| **API-M-002** | Excessive Data Exposure Prevention | Critical | Per **API-M-002**: responses must use allow-listed DTOs or serializers and exclude credentials, tokens, keys, PII and internal/debug fields. |
| **API-M-003** | Broken Function Level Authorization | Critical | Per **API-M-003**: privileged functions must enforce role or permission checks and reject lower-privileged callers. |
| **API-M-004** | Mass Assignment Protection | Critical | Per **API-M-004**: create and update operations must allow-list writable properties through dedicated request DTOs or equivalent mapping. |
| **API-M-005** | Auth on Sensitive API | Critical | Per **API-M-005**: sensitive endpoints must reject calls without valid authentication with `401` or `403`. |
| **API-M-006** | Rate Limiting Enforced | Critical | Per **API-M-006**: public endpoints must throttle excessive traffic and return `429 Too Many Requests`. |
| **API-M-007** | JWT Signature Validation | Critical | Per **API-M-007**: received JWT signatures must be validated against an explicit algorithm allow-list; `alg:none` must never be accepted. |

### High-risk REST controls

| Mandard | Title | Risk | Required governance check |
|---|---|---:|---|
| **API-M-008** | API Security Configuration Baseline | High | Per **API-M-008**: validate security headers, restricted CORS, disabled unnecessary HTTP methods, non-verbose errors, and managed version deprecation. |
| **API-M-009** | API Inventory & Versioning Management | High | Per **API-M-009**: every deployed endpoint must appear in an automatically generated OpenAPI specification and owned API inventory. Deprecated versions require `Deprecation` and `Sunset` headers and at least six months’ notice. |
| **API-M-010** | API-Specific Audit Logging & Monitoring | High | Per **API-M-010**: API calls must produce sanitized structured logs with user, method, path, status, timing and correlation ID; logs must reach the central SIEM. |
| **API-M-013** | Message-Level Integrity and Confidentiality | High | Per **API-M-013**: sensitive payloads crossing an organisational boundary or a TLS-terminating intermediary must be signed; confidential payloads must also be encrypted for the intended recipient. |

### API-domain controls not applicable to REST-only endpoints

| Mandard | Title | Risk | Applicability |
|---|---|---:|---|
| **API-M-011** | GraphQL Query Complexity Limits | Critical | GraphQL only |
| **API-M-012** | Disable Introspection in Production | High | GraphQL only |

## Framework mapping

The following mappings were explicitly returned by the catalogue. The tool payload truncated portions of several mapping lists, so this is a verified subset rather than a complete cross-framework matrix.

| Mandard | Verified framework mappings |
|---|---|
| **API-M-004** | NIST SP 800-53 Rev.5: `AC-2`, `AC-3`, `AC-4`, `AC-6`, `SI-10`, `SA-11`, `SA-12`, `SC-8`, `SR-3`, `SR-4`; PCI DSS v4.0: `Req 6`, `Req 7` |
| **API-M-005** | NIST SP 800-53 Rev.5: `IA-2`, `IA-5`, `AC-7`, `SA-11`, `SI-10`, `AC-4`, `SC-8` |
| **API-M-006** | NIST SP 800-53 Rev.5: `IA-2`, `IA-5`, `AC-7`, `SA-11`, `SI-10`, `AC-4`, `SC-8` |
| **API-M-013** | NIST SP 800-53 Rev.5: `SC-8`, `SC-13`, `SC-23`, `SI-7`; ISO/IEC 27001:2022: `A.8.24`, `A.5.14`; SOC 2: `CC6`; OWASP ASVS 5.0: `V11`, `V14`; NIST CSF 2.0: `PR.DS`, `PR.AA` |

## Required actions

1. **Authorization gate — API owner and security tester**
   - Implement and test object-level authorization for every path, query, or body object identifier under **API-M-001**.
   - Test every privileged operation using anonymous, ordinary-user, and privileged-user credentials under **API-M-003**.
   - Fail the release if a caller can retrieve another principal’s object or invoke a function outside its assigned role.

2. **Data and input gate — development team**
   - Under **API-M-002**, return response DTOs containing only contract-approved fields; do not serialize persistence models directly.
   - Under **API-M-004**, bind requests to allow-listed input DTOs and test attempts to modify fields such as roles, ownership, approval status, limits, or internal identifiers.

3. **Authentication and token gate — identity/API team**
   - Under **API-M-005**, call every sensitive operation without credentials and with invalid or expired credentials; verify `401` or `403`.
   - Under **API-M-007**, test unsigned, tampered, wrong-key and disallowed-algorithm JWTs; all must be rejected before business processing.

4. **Abuse-protection gate — API gateway/platform team**
   - Under **API-M-006**, run burst and sustained-load tests against public endpoints and confirm that configured thresholds produce `429`.
   - Apply endpoint-specific limits to authentication, OTP, search, export and other resource-intensive operations.

5. **Configuration gate — platform and application teams**
   - Under **API-M-008**, scan production-equivalent responses for required headers, prohibited wildcard CORS on sensitive endpoints, enabled `TRACE`/debug methods, stack traces, software versions, internal addresses and other error leakage.
   - Confirm deprecated versions are clearly marked.

6. **Contract and inventory gate — API product owner**
   - Under **API-M-009**, generate and validate the OpenAPI contract, assign endpoint ownership and compare deployed routes with documented paths and methods.
   - Block production publication where an undocumented route is discovered.

7. **Logging and monitoring gate — service owner and SOC**
   - Under **API-M-010**, verify structured JSON audit records include timestamp, method, path, authenticated identity, sanitized parameters, status, response time and correlation ID.
   - Confirm `401`, `403`, sensitive-data access and privileged operations reach the SIEM and exercise at least one associated alert.

8. **Boundary-protection gate — security architect**
   - Under **API-M-013**, identify whether TLS terminates at a proxy or partner intermediary or whether the message crosses an organisational boundary.
   - Where applicable, verify signatures before payload processing, reject unsigned or tampered messages, encrypt confidential payloads to the recipient, and use approved key management and rotation.

9. **Governance approval**
   - The REST API guardrail requires non-compliance to be formally recorded as a deviation with technical justification in the SAF pack. This procedure comes from **VeriFy-INT-REST-001**, mapped to **API-M-005**, **API-M-006**, **API-M-007**, **API-M-013**, `AC-M-001`, `CONT-M-005`, `CRYPT-M-002`, `GOV-G-006`, `MSA-M-001`, and `OAUTH-M-001`: [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099).
   - Its REST decision tree selects authentication and least-privilege authorization according to trust context and adds IP allow-listing, rate limiting, JWS signing and JWE encryption for applicable external patterns.
   - Release-pipeline guidance in **VeriFy-IS-RMP-001**, mapped to `ART-M-001`, `ART-M-002`, `GOV-G-006`, `INTEG-M-002`, `LOG-M-003`, `PIPE-M-001`, `PIPE-M-012`, `SECR-M-002`, and `SIGN-M-001`, calls for pull-request review and CI checks plus SAST, DAST and fuzz testing: [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688).

## Evidence for audit

The release record should contain:

- Approved OpenAPI specification and generated endpoint inventory.
- Route-to-owner, data-classification, authentication and authorization matrix.
- Role-based DAST results covering BOLA and function-level authorization.
- Tests proving unauthenticated access receives `401` or `403`.
- Response-field and mass-assignment negative-test results.
- JWT tampering and algorithm-validation results.
- Rate-limit test showing `429`.
- Security-header, CORS, method and error-leakage scan results.
- Sample sanitized JSON audit event, correlation trace, SIEM ingestion proof and alert-test result.
- Where applicable, message-signature tampering and encryption tests.
- CI/CD gate result and production approval record.
- Any approved deviation, technical justification, compensating controls, owner and expiry date in the SAF pack.

## Assumptions and limits

The answer assumes the endpoints are REST-only; GraphQL controls were therefore marked non-applicable. Actual endpoint code, OpenAPI contracts, gateway configuration, data classification, tests, SIEM ingestion and approvals were not inspected. The framework mapping is incomplete because portions of the catalogue tool response were truncated; no unreturned mappings have been inferred.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
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
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |

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