# G13-API

## Question
Which API controls remain mandatory for internal-only services?

## Sage response

## Bottom line

Internal-only status does **not** create a general exemption from API security controls. Twelve API Mandards remain mandatory when their stated conditions apply; only **API-M-006** is expressly scoped to public endpoints and therefore is not mandatory solely for a genuinely internal-only service. GraphQL, JWT, sensitive-data, privileged-function, and intermediary-specific controls apply only where those technologies or conditions exist.

## Risk and impact

The applicable controls address Critical risks including unauthorized object access, privilege escalation, data disclosure, mass assignment, authentication bypass, forged JWTs, and GraphQL denial of service. Internal network placement does not mitigate compromised identities, malicious insiders, lateral movement, service-to-service abuse, configuration errors, or accidental exposure.

## Governing mandards

| Mandard | Title | Risk | Internal-only applicability |
|---|---|---:|---|
| **API-M-001** | Broken Object Level Authorization BOLA/IDOR Prevention | Critical | **Mandatory where object identifiers are handled.** Per **API-M-001**: verify that the authenticated caller is authorized for the requested object. |
| **API-M-002** | Excessive Data Exposure Prevention | Critical | **Mandatory.** Per **API-M-002**: API responses must allow-list necessary fields and exclude sensitive data. |
| **API-M-003** | Broken Function Level Authorization BFLA | Critical | **Mandatory where privileged functions exist.** Per **API-M-003**: administrative and privileged endpoints must enforce function-level authorization. |
| **API-M-004** | Mass Assignment Protection | Critical | **Mandatory.** Per **API-M-004**: endpoints and service facades must explicitly allow-list properties accepted during creation and updates. |
| **API-M-005** | Auth on Sensitive API | Critical | **Mandatory for sensitive endpoints, explicitly including internal ones.** Per **API-M-005**: sensitive endpoints without valid authentication must return `401` or `403`. |
| **API-M-006** | Rate Limiting Enforced | Critical | **Not mandated by this control for internal-only endpoints.** Per **API-M-006**: the requirement expressly applies to public API endpoints. |
| **API-M-007** | JWT Signature Validation | Critical | **Mandatory if JWTs are received.** Per **API-M-007**: validate every JWT signature and reject `alg:none`. |
| **API-M-008** | API Security Configuration Baseline | High | **Mandatory.** Per **API-M-008**: every API deployment must enforce the prescribed headers, CORS, method, error-handling, and versioning baseline. |
| **API-M-009** | API Inventory and Versioning Management | High | **Mandatory.** Per **API-M-009**: maintain an up-to-date API inventory, document versions and deprecations, and prevent undocumented production endpoints. |
| **API-M-010** | API-Specific Audit Logging and Monitoring | High | **Mandatory.** Per **API-M-010**: log all API calls in structured form with correlation IDs and forward the logs to the centralized SIEM. |
| **API-M-011** | GraphQL Query Complexity Limits | Critical | **Mandatory if GraphQL is used.** Per **API-M-011**: enforce query depth and cost limits and reject excessive queries. |
| **API-M-012** | Disable Introspection in Production | High | **Mandatory for production GraphQL, including internal services.** Per **API-M-012**: reject `__schema` and `__type` introspection queries in production. |
| **API-M-013** | Message-Level Integrity and Confidentiality | High | **Conditionally mandatory.** Per **API-M-013**: protect sensitive payloads at message level where TLS is terminated by an intermediary or traffic crosses an organisational boundary. |

## Framework mapping

No framework-specific scope was requested. The conclusion above is based directly on the applicability language of the API Mandards rather than on framework equivalence.

## Required actions

1. **Service owner:** Record which conditional controls apply—object identifiers, privileged operations, sensitive data, JWT, GraphQL, TLS-terminating intermediaries, and organisational-boundary crossings.
2. **Engineering:** Apply all applicable Critical controls: **API-M-001** through **API-M-005**, **API-M-007**, and, for GraphQL, **API-M-011**.
3. **Platform and operations:** Enforce **API-M-008**, maintain the inventory required by **API-M-009**, and provide centralized monitoring under **API-M-010**.
4. **Security architect:** Assess **API-M-013** whenever gateways, proxies, service meshes, brokers, or partner systems terminate transport security.
5. **Risk owner:** Do not treat **API-M-006** as mandatory for a genuinely internal-only endpoint under its current wording. **Advisory (not catalogue-backed):** consider internal throttling where resource exhaustion, brute force, or noisy-neighbour risks remain.

## Evidence for audit

- API applicability assessment linked to every **API-M** control.
- Authorization tests for object-level and privileged-function access.
- Response-schema and mass-assignment test results.
- Unauthenticated endpoint tests demonstrating `401` or `403`.
- JWT signature-validation test or static-analysis result, where applicable.
- Approved API baseline configuration and deployment scan.
- Current OpenAPI inventory and version/deprecation records.
- Structured API log samples, correlation-ID trace, SIEM ingestion record, and alert test.
- GraphQL complexity and introspection test results, where applicable.
- Message-signing, encryption, and tamper-rejection tests where **API-M-013** applies.

## Assumptions and limits

“Internal-only” is assumed to mean the service has no public endpoint or public ingress path. Network exposure, approved exceptions, actual API features, and implementation compliance were not verified. No knowledge-document implementation guidance was requested or assessed.

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