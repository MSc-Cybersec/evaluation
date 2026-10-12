# G27-GRAPHQL

## Question
What controls are mandatory before enabling GraphQL in production?

## Sage response

## Bottom line

Production enablement is a **no-go** until both GraphQL Mandards are satisfied: field-level authorization and mutation permissions under **GRAPHQL-M-002**, followed by query depth, complexity, and rate controls under **GRAPHQL-M-001**. Failure exposes sensitive data and creates a denial-of-service path through computationally expensive queries. The release owner should require passing security-test evidence before opening the endpoint to production traffic.

## Risk and impact

| Priority | Exposure | Business impact |
|---|---|---|
| Critical | Missing resolver or field-level authorization; unauthorized mutations; production introspection | Sensitive-data disclosure, unauthorized transactions, privilege escalation, and schema reconnaissance |
| High | Unbounded query depth or complexity and inadequate rate limiting | Resource exhaustion, service degradation, increased infrastructure cost, and denial of service |

## Governing mandards

- **GRAPHQL-M-002 — GraphQL Authorization & Field-Level Control — Critical**  
  Per **GRAPHQL-M-002**: every resolver must perform authorization before returning data; sensitive fields require field-level protection; mutations require explicit permission; and introspection must be disabled in production.

- **GRAPHQL-M-001 — GraphQL Query Complexity & Depth Limiting — High**  
  Per **GRAPHQL-M-001**: maximum query depth must be `10`, complexity must be capped at `100`, rate limiting must operate per user/IP, and abuse must be monitored.

These are the complete GraphQL-domain Mandards returned by the catalogue.

## Framework mapping

The following mappings were returned for the two GraphQL Mandards:

| Mandard | Framework mappings |
|---|---|
| **GRAPHQL-M-002** | NIST SP 800-53 Rev.5: `AC-2`, `AC-3`, `AC-4`, `AC-6`, `SA-11`, `SI-10`, `SC-8`; PCI DSS v4.0: `Req 6`, `Req 7`; ISO/IEC 27001:2022: `A.5.15`, `A.5.18`, `A.8.2`, `A.8.3`, `A.8.26`, `A.8.28`; HIPAA: `164.312(a)(1)`; OWASP ASVS 5.0: `V4`, `V8`, `V13`; OWASP SAMM 2.0: `Verification: Security Testing`; OWASP Top 10:2025: `A01:2025`, `A02:2025`; OWASP API Security Top 10:2023: `API1`, `API2`, `API3`, `API4` |
| **GRAPHQL-M-001** | NIST SP 800-53 Rev.5: `AC-4`, `AU-6`, `SA-11`, `SC-8`, `SI-4`, `SI-7`, `SI-10`; PCI DSS v4.0: `Req 6`; ISO/IEC 27001:2022: `A.8.16`, `A.8.26`, `A.8.28`; SOC 2: `CC7.2`; OWASP ASVS 5.0: `V4`, `V13`; OWASP SAMM 2.0: `Verification: Security Testing`, `Operations: Incident Management`; OWASP Top 10:2025: `A02:2025`; OWASP API Security Top 10:2023: `API1`, `API2`, `API3`, `API4`, `API5`, `API8`, `API9` |

## Required actions

1. **Application/API owner — enforce authorization**
   - Check the authenticated principal and permissions in every resolver before retrieving or returning data.
   - Apply object- and field-level authorization to sensitive fields.
   - Require explicit permissions for every mutation.
   - Test owner, non-owner, privileged, anonymous, and cross-tenant access.
   - Per **GRAPHQL-M-002**, endpoint-level authentication alone is insufficient.

2. **Application/API owner — disable production introspection**
   - Disable schema introspection and interactive development or landing-page tooling in the production configuration.
   - Per **GRAPHQL-M-002**, introspection must not be available in production.

3. **Application/API owner — constrain query execution**
   - Reject queries deeper than `10` levels.
   - Calculate query cost before execution and reject complexity scores above `100`.
   - Ensure expensive fields, pagination sizes, aliases, fragments, and nested list relationships contribute appropriately to query cost.
   - Per **GRAPHQL-M-001**, both depth and complexity enforcement are mandatory.

4. **Platform/API gateway owner — control request volume**
   - Apply rate limiting per authenticated user and source IP.
   - Monitor rejected queries, depth and complexity violations, rate-limit events, and resource-consumption anomalies.
   - Per **GRAPHQL-M-001**, rate enforcement and abuse monitoring are mandatory.

5. **Release owner — establish the production gate**
   - Block release until negative authorization tests, over-depth tests, over-complexity tests, rate-limit tests, and introspection checks pass.
   - **Advisory (not knowledge-doc backed):** treat any bypass or missing evidence for these controls as a failed production-readiness gate.

## Evidence for audit

Retain:

- Production GraphQL configuration showing introspection disabled.
- Configuration or source defining depth limit `10` and complexity cap `100`.
- API gateway or application rate-limit policy showing user/IP keys.
- Resolver authorization policy or middleware configuration.
- Automated test results proving:
  - unauthorized fields and objects are denied;
  - unauthorized mutations are denied;
  - cross-user and cross-tenant access fails;
  - depth greater than `10` is rejected;
  - complexity greater than `100` is rejected;
  - rate limits activate;
  - production introspection fails.
- Monitoring dashboard or alert configuration for abuse and resource-exhaustion events.
- CI/CD approval record linking the passing evidence to the deployed release.

## Assumptions and limits

No knowledge document is currently mapped to **GRAPHQL-M-001** or **GRAPHQL-M-002**. Therefore, the implementation procedure above is derived from the Mandard catalogue; additional release-gate guidance is explicitly marked advisory.

This assessment covers the complete GraphQL-specific Mandard domain. It does not verify broader production controls—such as TLS, authentication token validation, secrets management, logging, vulnerability scanning, or general API gateway requirements—which may independently apply based on the deployment architecture and data classification. Some framework-mapping tool responses were truncated; only mappings visible in the returned results are listed.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**GRAPHQL-M-001**](https://verify.example-org.internal/?id=GRAPHQL-M-001) | High | GraphQL Security | CIS_CONTROLS (CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ISO_27001 (A.8.16, A.8.26, A.8.28); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, SA-11); OWASP (A02:2025); +7 more |
| [**GRAPHQL-M-002**](https://verify.example-org.internal/?id=GRAPHQL-M-002) | Critical | GraphQL Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +7 more |

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