# G52-PARAM

## Question
How should parameter tampering risks be controlled in sensitive transactions?

## Sage response

## Bottom line

Sensitive transactions must treat every client-supplied parameter as untrusted. Enforce deny-by-default authorization on the transaction and affected resource, bind only explicitly permitted fields, reject unknown fields, and block releases unless automated tampering and privilege-escalation tests pass. Without these controls, attackers may alter amounts, beneficiaries, ownership identifiers, approval states, or privileged attributes.

## Risk and impact

The primary exposure is **Critical** broken access control, including unauthorized transactions, IDOR, horizontal or vertical privilege escalation, and modification of another customer’s resources. **High** risks arise from mass assignment and from access-control defects recurring because tampering scenarios are not continuously tested.

## Governing mandards

| Mandard | Title | Risk level | Requirement |
|---|---|---:|---|
| **AC-M-001** | Mandatory Authorization Checks | Critical | Per **AC-M-001**: every sensitive endpoint must explicitly verify authentication, required permission, and access to the specific resource, using deny-by-default authorization. |
| **PARAM-M-001** | Mass Assignment Prevention | High | Per **PARAM-M-001**: explicitly allowlist parameters for each action, reject unknown parameters, use DTOs or strong parameter binding, and disable automatic binding to sensitive domain models. |
| **AC-M-002** | Authorization Testing Automation and Regression | High | Per **AC-M-002**: every protected function and object-level path must have positive and negative authorization tests, including IDOR and horizontal and vertical escalation tests; CI/CD must block failures. |

## Framework mapping

Only mappings returned by the SAGF catalogue are shown.

| Mandard | Framework mappings |
|---|---|
| **AC-M-001** | NIST SP 800-53 Rev.5 **AC-3** Access Enforcement; **AC-6** Least Privilege; **AC-4** Information Flow Enforcement |
| **PARAM-M-001** | NIST SP 800-53 Rev.5 **SI-10** Information Input Validation and **SA-11** Developer Testing and Evaluation; PCI DSS v4.0 **Requirement 6**; ISO/IEC 27001:2022 **A.8.26** Application Security Requirements and **A.8.28** Secure Coding |
| **AC-M-002** | NIST SP 800-53 Rev.5 **AC-3** Access Enforcement and **SA-15** Development Process, Standards, and Tools; PCI DSS v4.0 **Requirement 11**; ISO/IEC 27001:2022 **A.8.29** Security Testing; OWASP ASVS 5.0 **V8** Authorization |

## Required actions

1. **Enforce transaction authorization server-side — Application owner**
   - Per **AC-M-001**, apply centralized, deny-by-default authorization to every sensitive transaction endpoint.
   - Verify authentication, role or permission, tenant boundary, resource ownership, and entitlement for the requested operation.
   - Do not rely on hidden fields, disabled controls, URL identifiers, gateway routing, or client-side validation as authorization.
   - Return `401` for absent authentication and `403` for denied access without executing any state change.

2. **Constrain parameter binding — Development team**
   - Per **PARAM-M-001**, define a request DTO and action-specific allowlist.
   - Reject unknown, duplicate, unexpected, or read-only fields.
   - Never bind requests directly to persistence entities.
   - Prevent clients from setting fields such as `ownerId`, `tenantId`, `isAdmin`, approval state, transaction status, audit attributes, or internal risk decisions.

3. **Derive security-sensitive values on the server — Development team**
   - **Advisory (not catalogue-backed):** obtain customer, account, tenant, limits, fees, exchange rates, approval state, and entitlement data from authoritative server-side records rather than accepting them as trusted client values.
   - **Advisory (not catalogue-backed):** immediately before commit, recalculate transaction totals and revalidate beneficiary, limits, account status, and authorization inside the transaction boundary.
   - **Advisory (not catalogue-backed):** use single-use transaction identifiers or idempotency keys and atomic updates to reduce replay and time-of-check/time-of-use exposure.

4. **Automate tampering tests — QA and DevSecOps**
   - Per **AC-M-002**, test each protected transaction with:
     - No authentication and invalid authentication.
     - A lower-privilege user.
     - Another customer’s or tenant’s object identifier.
     - Added privileged or read-only fields.
     - Modified amounts, beneficiaries, account identifiers, status, ownership, and approval parameters.
     - Previously reported access-control exploits.
   - Run these tests on every build and block merge or deployment on failure.

5. **Apply the implementation guardrails**
   - **VeriFy-AUTHZ-GEN-001**, mapped to **AC-M-001**, requires application RBAC, least-privilege service accounts, segregation of duties, and access logging. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766
   - **VeriFy-AUTHZ-002**, mapped to **AC-M-001** and **AC-M-002**, establishes authorization-layer governance across applications, web services, databases, and operating systems. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445204
   - **VeriFy-INT-REST-001**, mapped to **AC-M-001**, requires least-privilege roles and scopes at REST API endpoints; for external integrations it also identifies rate limiting and, where technically feasible, JWS signing and JWE encryption. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

No knowledge document was found specifically for **PARAM-M-001**. Its DTO, field-allowlisting, and auto-binding remediation above comes directly from the Mandard catalogue.

## Evidence for audit

Retain:

- Endpoint inventory identifying every sensitive and state-changing operation.
- Authorization policy showing required roles, permissions, ownership, tenant boundaries, and deny-by-default behavior.
- DTO or schema definitions demonstrating action-specific allowlists and rejection of unknown fields.
- SAST or Semgrep results identifying direct entity binding and unprotected endpoints.
- CI results showing positive and negative authorization tests executed on every build.
- DAST or API security test results covering IDOR, mass assignment, privilege escalation, and transaction-field manipulation.
- Pipeline configuration proving failed authorization or tampering tests block merges and deployment.
- Regression tests linked to previously remediated access-control findings.
- Approved deviation record and technical justification where prescribed guardrails cannot be implemented.

## Assumptions and limits

No application code, API contract, authorization policy, transaction workflow, pipeline configuration, or test evidence was inspected. Transaction recalculation, anti-replay, idempotency, and atomic commit recommendations are advisory because no directly applicable transaction-integrity Mandard was identified in the retrieved catalogue results.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**AC-M-002**](https://verify.example-org.internal/?id=AC-M-002) | High | Access Control | CIS_CONTROLS (CIS 12, CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.PS-06); +9 more |
| [**PARAM-M-001**](https://verify.example-org.internal/?id=PARAM-M-001) | High | Parameter Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-20); ISO_27001 (A.5.19, A.5.21, A.8.26); NIST_CSF (GV.SC-01, ID.RA-09, PR.DS-01); NIST_SP_800_53 (SA-11, SA-12, SI-10); +8 more |

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