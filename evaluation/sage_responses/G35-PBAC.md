# G35-PBAC

## Question
How do we validate policy-based access control decisions for critical APIs?

## Sage response

## Bottom line

Critical APIs must enforce explicit, deny-by-default authorization and validate every protected function and object path through automated positive and negative tests. Per **AC-M-002**, these tests must cover horizontal and vertical privilege escalation and IDOR, run on every build, and block merges when they fail. Release approval should require a passing authorization regression suite, authenticated role-based API scan, and evidence that authorization denials are centrally logged.

## Risk and impact

Authorization failure is **Critical** where it permits unauthenticated access, cross-user or cross-tenant object access, or invocation of privileged functions. Without automated regression testing, policy changes can expose sensitive data, administrative operations, and state-changing API functions without detection.

The principal exposures are:

- **Object-level bypass:** A caller changes an object identifier and accesses another user’s or tenant’s data.
- **Function-level bypass:** A low-privilege identity invokes administrative or privileged operations.
- **Policy fail-open:** Missing attributes, unavailable policy services, or unmatched rules result in access being granted.
- **Credential-claim abuse:** Forged or improperly validated JWT claims influence the policy decision.
- **Undetected denial bypass:** Authorization decisions are not logged or correlated, preventing effective investigation.

## Governing mandards

### Primary access-control mandards

| Mandard | Title | Risk |
|---|---|---:|
| **AC-M-001** | Mandatory Authorization Checks | Critical |
| **AC-M-002** | Authorization Testing Automation and Regression | High |

Per **AC-M-001**: all sensitive endpoints must perform explicit authentication, permission or role, and resource-access checks using deny-by-default authorization.

Per **AC-M-002**: every protected function and object-level path must have automated positive and negative authorization tests, including horizontal escalation, vertical escalation, and IDOR. Tests must run on every build, block merges on failure, and retain regressions for previously corrected defects.

### API security mandards

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
| **API-M-009** | API Inventory and Versioning Management | High |
| **API-M-010** | API-Specific Audit Logging and Monitoring | High |
| **API-M-011** | GraphQL Query Complexity Limits | Critical |
| **API-M-012** | Disable Introspection in Production | High |
| **API-M-013** | Message-Level Integrity and Confidentiality | High |

For authorization-decision validation, the most directly applicable API controls are:

- Per **API-M-001**: verify access to each requested object; authorization must not depend on identifiers being difficult to guess.
- Per **API-M-003**: test every privileged operation using low-privilege credentials and reject unauthorized calls.
- Per **API-M-005**: sensitive endpoints called without valid authentication must return `401` or `403`.
- Per **API-M-007**: validate every JWT signature and reject `alg:none`.
- Per **API-M-010**: log API calls, authentication failures, authorization denials, sensitive access, status codes, and correlation IDs in structured format and forward them to the SIEM.

## Framework mapping

The following directly relevant mappings were returned by the SAGF catalogue:

| Mandard | Framework | Controls |
|---|---|---|
| **AC-M-001** | NIST SP 800-53 Rev. 5 | AC-2 Account Management; AC-3 Access Enforcement; AC-4 Information Flow Enforcement; AC-6 Least Privilege; IA-2 Identification and Authentication |
| **AC-M-002** | NIST SP 800-53 Rev. 5 | AC-2, AC-3, AC-4, AC-6, CM-3, SA-15, SC-5, SC-7 |
| **AC-M-002** | PCI DSS v4.0 | Requirements 1, 7, and 11 |
| **AC-M-002** | ISO/IEC 27001:2022 | A.5.15, A.5.18, A.8.2, A.8.3, A.8.20, A.8.22, A.8.25, A.8.29, A.8.31, A.8.32 |
| **AC-M-002** | HIPAA Security Rule | 164.312(a)(1) |
| **AC-M-002** | SOC 2 Type II | CC6.1 |
| **AC-M-002** | OWASP ASVS 5.0 | V8 Authorization |

## Required actions

### 1. Build an authorization decision matrix

**Owner:** API owner with Security Champion and business authorization owner.

For each protected OpenAPI operation, define:

- Principal type and authentication state.
- Role, permission, scope, and relevant claims.
- Action or HTTP method.
- Resource type and object identifier.
- Ownership and tenant relationship.
- Relevant contextual attributes, such as environment or transaction state.
- Expected policy decision: `allow` or `deny`.
- Expected API result.

At minimum, include:

| Scenario | Expected outcome |
|---|---|
| Valid identity with correct permission and permitted object | Allow |
| No token or invalid token | `401` or `403`, per **API-M-005** |
| Authenticated identity without permission | `403` |
| User accessing another user’s object | Deny, per **API-M-001** |
| User accessing another tenant’s object | Deny |
| Normal user invoking an administrative operation | Deny, per **API-M-003** |
| Missing, null, malformed, or unexpected policy attribute | Deny, per **AC-M-001** |
| Expired or forged JWT, or JWT using `alg:none` | Reject, per **API-M-007** |
| Previously exploited authorization path | Deny through a permanent regression test |

### 2. Test the policy separately from the API

**Owner:** Authorization or platform engineering team.

Create policy unit tests that supply a complete authorization input—subject, action, resource, and context—and compare the returned decision with the approved matrix. Exercise every permit rule, deny rule, boundary value, missing attribute, conflicting attribute, and default rule.

Per **AC-M-001**, unmatched or incomplete policy input must not produce an implicit grant.

### 3. Test the complete enforcement path

**Owner:** API engineering team.

Policy-unit tests alone are insufficient. Run integration tests through the actual API gateway or application enforcement point to verify that:

1. The authenticated identity and validated claims are passed correctly.
2. The correct action and resource identifiers reach the policy decision point.
3. The API enforces the returned decision.
4. A deny decision cannot be bypassed through an alternate route, HTTP verb, API version, batch operation, or direct service call.
5. Denied operations do not modify state or return protected response data.

The REST API guardrail states that system roles must be enforced using least privilege at the API endpoint and user-context tokens must map to application roles and relevant scopes or claims, either in the application or through an authorization policy service. Source: **VeriFy-INT-REST-001**, mapped to **AC-M-001**, **API-M-005**, **API-M-006**, **API-M-007**, **API-M-013**, **CONT-M-005**, **CRYPT-M-002**, **GOV-G-006**, **MSA-M-001**, and **OAUTH-M-001** — [authoritative resource](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099).

### 4. Automate adversarial authorization tests

**Owner:** Quality engineering and application security.

Per **AC-M-002**, run the following on every build:

- **Horizontal escalation:** User A attempts every relevant operation on User B’s objects.
- **Cross-tenant escalation:** A principal from Tenant A attempts access to Tenant B.
- **Vertical escalation:** Standard users invoke administrator, support, export, configuration, and approval functions.
- **IDOR/BOLA:** Substitute valid object identifiers belonging to other principals.
- **Method substitution:** Test `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` independently.
- **Token variation:** Remove tokens; alter roles, scopes, audience, issuer, expiry, and signature; test `alg:none`.
- **Route variation:** Exercise alternate versions, aliases, bulk routes, nested resources, and direct service endpoints.
- **Regression:** Preserve a test for every remediated authorization vulnerability.

Per **API-M-001** and **API-M-003**, use authenticated role-switching DAST against a deployed test environment, not only source-code or policy-unit tests.

### 5. Enforce a CI/CD release gate

**Owner:** DevSecOps or platform engineering.

Per **AC-M-002**, the pipeline must:

1. Run policy-unit and API integration suites on every build.
2. Fail on any unexpected allow or authorization regression.
3. Block merge and deployment after failure.
4. retain machine-readable results linked to the commit and policy version.
5. Run authenticated DAST for object- and function-level authorization before production release.

Per **AC-M-001**, SAST should identify sensitive endpoints without required authorization middleware, filters, or decorators and fail the build when an unprotected endpoint is found.

### 6. Validate runtime decision records

**Owner:** Security operations and API operations.

Per **API-M-010**, capture structured audit records containing:

- Timestamp and correlation ID.
- Method and endpoint.
- Authenticated identity.
- Sanitized request parameters.
- Response status and duration.
- Authentication failure or authorization denial.
- Access to sensitive APIs or data.

Forward records to the central SIEM and confirm that denial and unusual-access alerts work. Do not log access tokens, secrets, passwords, or unredacted sensitive payloads.

### 7. Govern exceptions

**Owner:** Security architecture and risk owner.

The authorization guardrail requires non-compliance to be recorded as a formal deviation with technical justification in the SAF pack. Source: **VeriFy-AUTHZ-002**, mapped to **AC-M-001**, **AC-M-002**, **GOV-G-006**, **IAM-M-001**, and **OAUTH-M-002** — [authoritative resource](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445204).

No knowledge document was found containing a detailed platform-specific policy-engine test procedure. **Advisory (not knowledge-doc backed):** where possible, replay the same approved decision vectors against both the policy engine and deployed API; differences indicate claim transformation, resource mapping, caching, or enforcement defects.

## Evidence for audit

Retain the following evidence for each critical API release:

- Approved authorization decision matrix linked to API operations and policy version.
- Policy-unit test report showing all expected allow and deny decisions.
- API integration report covering unauthenticated, horizontal, vertical, cross-tenant, and IDOR scenarios.
- Authenticated DAST report using at least two privilege levels and separate tenant or ownership contexts.
- CI/CD record proving failed authorization tests block merge and deployment.
- SAST report showing no unprotected sensitive endpoint findings.
- JWT validation test results, including rejection of invalid signatures and `alg:none`.
- Policy source, review approval, version history, and deployment digest.
- Sample structured authorization-denial records and proof of SIEM ingestion.
- Regression tests linked to previously remediated access-control defects.
- Approved deviation and risk-acceptance record where any required control is not implemented.

## Assumptions and limits

No API specification, policy source, identity model, gateway configuration, CI pipeline, runtime logs, or test results were provided or verified. The detailed test procedure must therefore be adapted to the organisation’s policy engine and API technology.

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

Showing 15 of 21 cited mandards.

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