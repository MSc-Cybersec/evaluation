# G32-ERR

## Question
What is an acceptable production error-handling policy for sensitive systems?

## Sage response

## Bottom line

Production systems handling sensitive data must return generic errors to users and must never expose stack traces, file paths, connection strings, secrets, code fragments, or platform details. Per **ERR-M-003**: .NET production applications must enable custom errors with a generic redirect; failure is rated **Critical**.

The catalogue does not contain a technology-neutral error-handling Mandard. The policy below is therefore a recommended enterprise baseline; approve it as an internal policy and consider creating a broader Mandard covering non-.NET systems.

## Risk and impact

Detailed production errors can disclose database objects, filesystem paths, API keys, code snippets, software versions, and internal architecture. Attackers can use this information for credential theft, vulnerability targeting, lateral movement, and data compromise.

| Exposure | Treatment |
|---|---|
| .NET detailed error disclosure | **Critical**, per **ERR-M-003** |
| Other platforms | No directly applicable SAGF Mandard was found; risk rating is unverified |
| Business impact | Increased likelihood of system compromise, sensitive-data disclosure, service interruption, and regulatory exposure |

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **ERR-M-003** | .NET Custom Errors Enabled | **Critical** | Per **ERR-M-003**: configure .NET `web.config` with `<customErrors mode="On">` and a generic `defaultRedirect` so detailed system errors are not shown to users. |

No technology-neutral production error-handling Mandard was found. A new Mandard should be drafted to extend equivalent requirements to Java, Node.js, Python, Go, mobile, API gateway, serverless, and other production platforms.

## Framework mapping

The following mappings were returned for **ERR-M-003**:

| Framework | Control | Requirement |
|---|---|---|
| OWASP ASVS 5.0 | V16 | Security Logging and Error Handling |
| OWASP ASVS 5.0 | V13 | Configuration |
| OWASP Top 10:2025 | A02:2025 | Security Misconfiguration |
| OWASP Top 10:2025 | A10:2025 | Mishandling of Exceptional Conditions |
| NIST SP 800-53 Rev. 5 | SA-11 | Developer Testing and Evaluation |
| NIST SP 800-53 Rev. 5 | SI-10 | Information Input Validation |
| ISO/IEC 27001:2022 | A.8.26 | Application security requirements |
| ISO/IEC 27001:2022 | A.8.28 | Secure coding |
| PCI DSS v4.0 | Req 6 | Develop and Maintain Secure Systems |
| CIS Controls v8 | CIS 16 | Application Software Security |
| NIST CSF 2.0 | PR.PS-01 | Configuration Management Practices |
| OWASP SAMM 2.0 | Verification: Security Testing | Security Testing |

## Required actions

1. **Prevent detailed .NET errors in production — Critical**
   
   Per **ERR-M-003**, the application owner must configure:

   ```xml
   <configuration>
     <system.web>
       <customErrors
         mode="On"
         defaultRedirect="~/ErrorPages/GenericError.html" />
     </system.web>
   </configuration>
   ```

   Treat `customErrors mode="Off"` as a production release blocker.

2. **Adopt this enterprise production policy**
   
   **Advisory (not catalogue-backed):**
   
   - External responses must contain only a stable error category, safe message, and opaque correlation identifier.
   - Responses must not contain stack traces, source code, queries, database or host names, internal paths, credentials, tokens, personal data, cryptographic material, dependency versions, or security-control details.
   - Authentication and authorization failures should not reveal whether an account, resource, or identifier exists.
   - Unhandled exceptions must be caught at the application boundary and converted to approved protocol responses.
   - Applications must fail securely: deny uncertain authorization, roll back incomplete transactions, release resources, and avoid returning partial sensitive results.
   - Diagnostic details must be recorded only in access-controlled server-side telemetry. Logs must apply data minimisation and secret redaction.
   - Client-facing correlation identifiers must allow authorized responders to locate the corresponding diagnostic event without exposing internal context.
   - Expected client errors, security-relevant failures, transient dependency failures, and unexpected defects must be classified separately.
   - Alerting must cover unexpected error-rate increases, repeated authorization failures, malformed-input campaigns, dependency outages, and evidence of error-triggering reconnaissance.
   - Debug modes, developer exception pages, and verbose framework errors must be disabled in every production deployment.
   - Any exception must be time-bound, risk accepted, approved through the formal deviation process, and supported by compensating controls.

3. **Add release enforcement**
   
   Per **ERR-M-003**, use a CI static check to inspect the deployed `web.config`. Run authenticated dynamic testing that deliberately triggers invalid input and confirms that responses do not disclose stack traces, paths, version numbers, or database details. The Mandard identifies OWASP ZAP, Burp Suite, AppScan, Veracode Dynamic Analysis, Acunetix, error-message scanning, and manual testing as enforcement options.

4. **Draft a technology-neutral Mandard**
   
   **Advisory (not catalogue-backed):** GRC and Application Security should create a production error-handling Mandard defining platform-independent requirements, risk rating, approved response formats, prohibited disclosures, logging boundaries, pipeline gates, and exception governance.

## Evidence for audit

For **ERR-M-003**, retain:

- The deployed `web.config` showing `customErrors mode="On"` and the generic redirect.
- A CI lint result proving the deployed artifact was checked.
- Dynamic scan results demonstrating that malformed requests do not reveal sensitive implementation details.
- Test cases covering handled and unhandled exceptions, authentication failures, dependency failures, and malformed input.
- Screenshots or response captures showing generic production error pages.
- Release-gate records showing that critical error-disclosure findings block promotion.
- Approved and time-bound deviation records for any temporary non-compliance.

## Assumptions and limits

No knowledge document was found that directly implements **ERR-M-003**, and `get_mandard_guidance` returned no mapped guidance documents. The broader policy recommendations are therefore labelled **Advisory (not catalogue-backed)**.

The knowledge search returned tangential documents concerning logging, authentication, release management, and decommissioning; these were set aside because they did not provide substantive production error-handling procedures. The framework table includes only mappings returned for **ERR-M-003** and is not represented as an exhaustive mapping list.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ERR-M-003**](https://verify.example-org.internal/?id=ERR-M-003) | Critical | Error Handling | CIS_CONTROLS (CIS 16); CWE (CWE-798); ISO_27001 (A.5.17, A.8.24, A.8.26); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (IA-5, SA-11, SC-12); OWASP (A02:2025, A10:2025); +5 more |

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