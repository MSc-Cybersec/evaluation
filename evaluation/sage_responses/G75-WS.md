# G75-WS

## Question
What controls apply to secure web-service endpoints beyond REST basics?

## Sage response

## Bottom line

Secure web-service endpoints require the full API control set, not only REST validation and transport security. Eight Critical controls address authorization, data exposure, mass assignment, authentication, throttling, JWT validation, and GraphQL resource exhaustion; five High controls address configuration, inventory, monitoring, GraphQL discovery, and end-to-end message protection. The architecture owner should identify which endpoints are sensitive, public, GraphQL-based, or cross an intermediary or organisational boundary, then make the applicable controls release gates.

## Risk and impact

The principal exposure is unauthorized access or modification, privilege escalation, credential/token forgery, sensitive-data disclosure, denial of service, unmonitored attacks, forgotten endpoint versions, and message tampering after TLS termination.

Controls apply according to endpoint characteristics:

- **All API styles:** object and function authorization, input/output allow-listing, authentication, configuration, inventory, and audit monitoring.
- **Public endpoints:** rate limiting.
- **JWT-protected endpoints:** cryptographic signature and algorithm validation.
- **GraphQL endpoints:** query depth/cost limits and production introspection restrictions.
- **Services crossing intermediaries or organisational boundaries:** message-level signing and, for confidential payloads, recipient-specific encryption.

## Governing mandards

| Mandard | Title | Risk | Required control |
|---|---|---:|---|
| **API-M-001** | Broken Object Level Authorization Prevention | Critical | Per **API-M-001**: verify that the authenticated principal is authorized for each requested object; identifier obscurity is not authorization. |
| **API-M-002** | Excessive Data Exposure Prevention | Critical | Per **API-M-002**: allow-list response fields and prevent exposure of credentials, secrets, PII, internal identifiers, network details, and debug information. |
| **API-M-003** | Broken Function Level Authorization | Critical | Per **API-M-003**: enforce role or permission checks on every privileged function and administrative endpoint. |
| **API-M-004** | Mass Assignment Protection | Critical | Per **API-M-004**: use explicit property allow-lists or dedicated request DTOs for object creation and updates. |
| **API-M-005** | Auth on Sensitive API | Critical | Per **API-M-005**: sensitive endpoints must reject requests without valid authentication using `401` or `403`. |
| **API-M-006** | Rate Limiting Enforced | Critical | Per **API-M-006**: public endpoints must throttle excessive requests and return `429 Too Many Requests`. |
| **API-M-007** | JWT Signature Validation | Critical | Per **API-M-007**: validate every JWT signature against an explicit algorithm allow-list and reject `alg:none`. |
| **API-M-011** | GraphQL Query Complexity Limits | Critical | Per **API-M-011**: apply query-depth and cost analysis before execution and reject excessive GraphQL queries with `400`. |
| **API-M-008** | API Security Configuration Baseline | High | Per **API-M-008**: enforce security headers, restricted CORS, allowed HTTP methods, non-verbose errors, and controlled version deprecation. |
| **API-M-009** | API Inventory and Versioning Management | High | Per **API-M-009**: maintain an automatically generated endpoint inventory, prohibit undocumented production endpoints, and manage deprecation with at least six months’ notice. |
| **API-M-010** | API-Specific Audit Logging and Monitoring | High | Per **API-M-010**: generate structured, sanitized API audit logs with identities, outcomes, timing, correlation IDs, and centralized SIEM forwarding. |
| **API-M-012** | Disable Introspection in Production | High | Per **API-M-012**: production GraphQL endpoints must reject `__schema` and `__type` introspection requests with `403`. |
| **API-M-013** | Message-Level Integrity and Confidentiality | High | Per **API-M-013**: when TLS is terminated by an intermediary or a message crosses an organisational boundary, sign sensitive payloads and additionally encrypt confidential payloads to the intended recipient. |

## Framework mapping

The catalogue returned the following complete mapping for the protocol-neutral message-protection control:

| Mandard | Framework mappings |
|---|---|
| **API-M-013** | NIST SP 800-53 Rev. 5: `SC-8`, `SC-13`, `SC-23`, `SI-7`; ISO/IEC 27001:2022: `A.8.24`, `A.5.14`; SOC 2: `CC6`; OWASP ASVS 5.0: `V11`, `V14`; NIST CSF 2.0: `PR.DS`, `PR.AA` |

Mappings for several other returned records were truncated by the tool response and are therefore not reproduced as complete mappings.

## Required actions

1. **Application teams — authorization and data controls**
   - Apply authentication middleware to every sensitive operation.
   - Enforce authorization separately at object and function levels.
   - Use request and response DTOs with explicit field allow-lists.
   - Add negative tests using different users, tenants, roles, object identifiers, and unauthorized fields.
   - These actions implement **API-M-001**, **API-M-002**, **API-M-003**, **API-M-004**, and **API-M-005**.

2. **Identity and application teams — token validation**
   - Verify JWT signatures before trusting claims.
   - Pin permitted signing algorithms and reject unsigned tokens.
   - Resolve and validate signing keys securely; do not use unverified decoded claims for authorization.
   - This implements **API-M-007**.

3. **Platform/API gateway team — abuse resistance**
   - Apply rate limits to public endpoints, with stricter policies for authentication, OTP, search, export, and expensive operations.
   - Test that sustained or excessive traffic eventually produces `429`.
   - This implements **API-M-006**.

4. **GraphQL service owners**
   - Configure maximum query depth and calculated query cost.
   - Reject excessive queries before resolver execution.
   - Disable production introspection and verify rejection of `__schema` and `__type`.
   - These actions implement **API-M-011** and **API-M-012**.

5. **Platform and application teams — endpoint baseline**
   - Restrict CORS to approved origins for sensitive endpoints.
   - Disable unnecessary methods, including `TRACE` and `DEBUG`.
   - Apply the required HTTP security headers and generic external error handling.
   - Manage deprecated endpoints with `Deprecation` and `Sunset` headers.
   - This implements **API-M-008**.

6. **API product owner — inventory and lifecycle**
   - Generate the API contract from source where supported.
   - Reconcile deployed routes against the approved contract.
   - Record endpoint owner, authentication requirement, version, status, and decommission date.
   - Remove or block undocumented and expired endpoints.
   - This implements **API-M-009**.

7. **Security operations and service teams — monitoring**
   - Log timestamp, method, route, authenticated identity, sanitized parameters, status, duration, denials, and sensitive operations in structured JSON.
   - Propagate correlation IDs and forward records to the centralized SIEM.
   - Configure detections for repeated authentication failures, authorization denials, enumeration, scraping, and abnormal volume.
   - This implements **API-M-010**.

8. **Security architecture and cryptography owners — end-to-end message protection**
   - Identify flows where TLS terminates before the trusted receiver or where payloads cross organisational boundaries.
   - Sign sensitive payloads and verify the signature and key identifier before processing.
   - Encrypt confidential payloads to the recipient’s key.
   - Store and rotate signing and encryption keys through the approved key-management service.
   - This implements **API-M-013** and is particularly important for brokered, partner, and intermediary-routed services.

## Evidence for audit

| Control area | Minimum evidence |
|---|---|
| **API-M-001**, **API-M-003** | Role-switching authorization test results showing object and privileged-function denials |
| **API-M-002** | Approved response schemas plus scans demonstrating that sensitive fields are absent |
| **API-M-004** | Request DTO definitions and tests proving unauthorized fields cannot modify protected properties |
| **API-M-005** | Endpoint test report showing unauthenticated sensitive requests return `401` or `403` |
| **API-M-006** | Gateway policy and load-test result demonstrating `429` responses |
| **API-M-007** | JWT verifier configuration, SAST result, and tests for invalid signatures and `alg:none` |
| **API-M-008** | Header, CORS, method, and error-leak scan results; deprecation-header tests |
| **API-M-009** | Approved API inventory, generated contract, endpoint reconciliation report, and lifecycle records |
| **API-M-010** | Sanitized JSON log sample, correlation trace, SIEM ingestion evidence, and alert test |
| **API-M-011** | GraphQL depth/cost configuration and rejection tests for excessive queries |
| **API-M-012** | Production test showing introspection receives `403` |
| **API-M-013** | Signed/encrypted contract configuration, key-management record, and tests rejecting unsigned, tampered, or incorrectly encrypted messages |

## Assumptions and limits

The endpoint technology, exposure model, data classification, authentication mechanism, and intermediary trust boundaries were not provided, so applicability must be assessed per service. The knowledge search returned governance material, but no directly applicable API-mapped knowledge document was confirmed from the retrieved results; therefore, the implementation actions above are based on the Mandard catalogue rather than a separate organisational procedure. Framework mappings are intentionally limited to the complete mapping returned for **API-M-013**.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
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