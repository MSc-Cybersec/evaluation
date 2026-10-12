# G41-IDOR

## Question
How should we evidence object-level authorization for tenant data access?

## Sage response

## Bottom line

Evidence object-level authorization with a repeatable, pipeline-gated test suite proving that a user from Tenant A can access permitted Tenant A objects but cannot read, modify, delete, enumerate, or export Tenant B objects. Per **AC-M-001**, every sensitive endpoint must explicitly validate authentication, permission, and access to the specific resource using deny-by-default logic; missing this control creates a Critical risk of cross-tenant disclosure or modification.

## Risk and impact

The primary exposure is **Critical** broken access control, including IDOR and privilege escalation. A single missing object check can expose tenant records even when authentication and role-based access control are otherwise working.

Database over-privilege creates a **High** secondary risk because an application identity with excessive permissions increases the blast radius of an authorization defect or compromised service.

## Governing mandards

| Mandard | Title | Risk | Relevance |
|---|---|---:|---|
| **AC-M-001** | Mandatory Authorization Checks | Critical | Primary control: sensitive endpoints must check authentication, required permission, and access to the specific resource using deny-by-default behavior. |
| **IAM-M-001** | Least-Privilege IAM Policies | Critical | Production IAM roles must be narrowly scoped; wildcard actions and resources are prohibited. |
| **IAM-M-002** | Enforce MFA for Privileged Accounts | Critical | Administrative and privileged accounts require MFA. Relevant to support or administrative cross-tenant access. |
| **SECR-M-001** | No Hardcoded Secrets | Critical | Builds must fail when high-confidence secrets are detected in source or configuration. |
| **SECR-M-004** | Short-Lived Credentials & Rotation | Critical | Production automation credentials must be short-lived or regularly rotated. |
| **DB-M-003** | Database Access Control & Least Privilege | High | Application database accounts must have minimal permissions; access must be audited and reviewed quarterly. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Any departure must be approved before release, risk-owned, compensated, and time-bounded. |

Per **AC-M-001**: an authenticated session or valid tenant claim is insufficient by itself; authorization must be evaluated against the requested object.

## Framework mapping

The following mappings were returned by the SAGF catalogue and are directly relevant:

| Mandard | Framework controls |
|---|---|
| **AC-M-001** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-4`, `AC-6`, `IA-2`, `IA-4` |
| **DB-M-003** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-4`, `AC-6`, `SA-11`, `SI-10`, `CM-6`; PCI DSS v4.0 `Req 6`, `Req 7`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.2`, `A.8.3`, `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V8`, `V13`; OWASP Top 10:2025 `A01`, `A02` |
| **IAM-M-001** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-4`, `AC-6`; PCI DSS v4.0 `Req 7`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.2`, `A.8.3`; SOC 2 `CC6.1`; OWASP ASVS 5.0 `V8` |
| **IAM-M-002** | NIST SP 800-53 Rev.5 `IA-2`, `IA-5`, `AC-2`, `AC-3`, `AC-6`; PCI DSS v4.0 `Req 7`, `Req 8`; ISO/IEC 27001:2022 `A.5.17`, `A.8.5` |
| **GOV-G-006** | NIST SP 800-53 Rev.5 `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022 `A.5.1`, `A.5.35`; SOC 2 `CC3`, `CC5`; COBIT 2019 `APO12.01`, `MEA02` |

## Required actions

1. **Build an authorization coverage matrix — Application owner**
   
   Per **AC-M-001**, inventory every endpoint, resolver, queue consumer, batch operation, export function, and administrative operation that handles tenant data. Record:
   - Operation and object type.
   - Required role or permission.
   - Tenant relationship required.
   - Ownership or delegated-access rule.
   - Enforcement component.
   - Automated test identifier.

2. **Enforce tenant and object authorization server-side — Engineering**
   
   Per **AC-M-001**, centralize deny-by-default authorization and evaluate the authenticated principal against the stored resource before returning or changing it.

   **Advisory (not knowledge-doc backed):** Resolve the tenant from trusted identity or membership data, not from an unvalidated request header, query parameter, or object body. Prefer tenant-scoped retrieval such as `object_id AND tenant_id`, rather than loading by object ID and relying on later filtering.

3. **Create a two-tenant negative-test suite — Security testing**
   
   Per **AC-M-001**, integration and DAST testing should exercise unauthenticated and low-privilege access and verify rejection. For Tenant A and Tenant B, test every applicable operation:
   - Read by object identifier.
   - Update, delete, approve, and other state changes.
   - List, search, pagination, and filtering.
   - Bulk operations and exports.
   - Nested resources and alternate identifiers.
   - File downloads and pre-signed URLs.
   - GraphQL nodes or API batch requests, where applicable.
   - Administrative and support routes.

   **Advisory (not knowledge-doc backed):** Include identifier substitution, stale authorization, changed tenant claims, object reassignment, and guessed identifiers. Assert both denial and absence of Tenant B data in the response body, metadata, counts, error details, and side effects.

4. **Gate release on authorization tests — Engineering and DevSecOps**
   
   Per **AC-M-001**, configure SAST to identify sensitive endpoints without authorization middleware or equivalent enforcement, and fail the build for uncovered endpoints. Run cross-tenant integration tests on every relevant build and retain machine-readable results.

5. **Constrain the data path — Database and cloud platform owners**
   
   Per **DB-M-003**, use dedicated, minimally privileged application roles, prohibit shared accounts, audit database access, and review access quarterly. Per **IAM-M-001**, remove wildcard production permissions and scope identities to required actions and resources.

6. **Log authorization decisions — Engineering and SOC**
   
   The implementation guidance requires access and privileged-access logging, RBAC, segregation of duties, and least-privileged application and database identities: **VeriFy-AUTHZ-GEN-001**, mapped to **AC-M-001**, **DB-M-003**, **GOV-G-006**, **IAM-M-001**, **IAM-M-002**, **SECR-M-001**, and **SECR-M-004**. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766

   **Advisory (not knowledge-doc backed):** Log actor, effective tenant, object type, object identifier or approved pseudonym, action, decision, policy version, reason code, and correlation ID. Avoid placing sensitive record content in logs.

7. **Govern exceptions — Risk owner and independent approver**
   
   Per **GOV-G-006**, an endpoint that cannot meet object-level authorization must not be silently released. Record the affected control, justification, residual risk owner, compensating controls, independent approval, and expiry date.

## Evidence for audit

The audit pack should contain:

| Evidence | What it proves |
|---|---|
| Authorization coverage matrix | Every sensitive operation has a defined object and tenant authorization rule. |
| Architecture or policy configuration | Authorization is centralized, deny-by-default, and applied server-side. |
| Version-controlled policy or middleware | The exact authorization logic associated with the released build. |
| Cross-tenant test report | Tenant A cannot access Tenant B objects across read, write, delete, list, search, export, and bulk paths. |
| Positive test report | Legitimate same-tenant access still works, reducing the risk of meaningless blanket denial. |
| CI pipeline record | SAST and integration authorization gates ran against the released commit and passed. |
| Endpoint coverage output | Sensitive endpoints are mapped to authorization enforcement and tests; approved public endpoints are explicitly identified. |
| DAST or penetration-test report | Runtime resistance to identifier substitution and privilege manipulation. |
| Sanitized authorization logs | Successful and denied decisions are attributable and traceable through correlation IDs. |
| Database grants report | Application identities have only the required permissions. |
| Quarterly database access review | Compliance with the review requirement in **DB-M-003**. |
| Privileged-access evidence | MFA status and access approval for support or administrative identities under **IAM-M-002**. |
| Deviation record | Any unmet control has the evidence required by **GOV-G-006**. |

A concise acceptance statement should be tied to the release:

> For build `<build-id>`, all inventoried tenant-data operations were tested using independent Tenant A and Tenant B identities. Permitted same-tenant operations succeeded; cross-tenant read and state-changing attempts were denied without disclosure or side effects. The pipeline, test results, policy version, and exception register are attached.

## Assumptions and limits

The application architecture, tenancy model, endpoint inventory, database isolation model, logging configuration, and current test coverage were not verified. The catalogue contains a general authorization knowledge document, but no knowledge document was found that specifies a tenant-specific object-authorization test procedure; the tenant-specific testing recommendations above are therefore marked as advisory. Tangential knowledge results concerning general data-access processes, enterprise authentication, application governance, and Example Org ID were set aside because they did not provide object-level tenant authorization evidence procedures.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**DB-M-003**](https://verify.example-org.internal/?id=DB-M-003) | High | Database Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
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