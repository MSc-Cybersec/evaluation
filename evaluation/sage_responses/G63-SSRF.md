# G63-SSRF

## Question
How should SSRF risk be governed for services that call external URLs?

## Sage response

## Bottom line

Services that construct outbound requests from user-influenced URLs, hostnames, file paths, webhook destinations, or configuration must comply with **SSRF-M-001**. Enforce destination allowlisting in the application and restrict outbound connectivity at the network layer; otherwise, attackers may access internal services or cloud metadata, steal credentials, exfiltrate data, and move laterally. Treat deployment without these controls as an unmitigated **High** risk requiring remediation or formally approved risk acceptance.

## Risk and impact

**Risk level: High.**

Per **SSRF-M-001**: server-side requests influenced by external input must validate permitted schemes, hosts, and ports; block internal, link-local, and cloud metadata destinations; control redirects and DNS rebinding; and restrict network egress.

If unaddressed, exposure includes:

- Cloud instance credentials and metadata services.
- Internal APIs, administration interfaces, and data stores.
- Lateral movement into otherwise inaccessible network segments.
- Data exfiltration and, where vulnerable internal services exist, remote code execution.
- Availability impact through requests to unintended or resource-intensive destinations.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---|
| **SSRF-M-001** | Server-Side Request Forgery Prevention | **High** |

This is the complete `SSRF-M` domain set currently returned by the catalogue.

## Framework mapping

The catalogue maps **SSRF-M-001** to:

| Framework | Controls returned |
|---|---|
| NIST SP 800-53 Rev. 5 | SI-10 Information Input Validation; SI-15 Information Output Filtering; SA-11 Developer Testing and Evaluation; IA-5 Authenticator Management; SC-12 Cryptographic Key Establishment and Management; SC-7 Boundary Protection; AC-4 Information Flow Enforcement; SC-5 Denial-of-Service Protection |
| PCI DSS v4.0 | Req 1 Install and Maintain Network Security Controls; Req 6 Develop and Maintain Secure Systems |
| ISO/IEC 27001:2022 Annex A | A.8.24 Use of cryptography; A.5.17 Authentication information; A.8.26 Application security requirements; A.8.28 Secure coding; A.8.20 Networks security; A.8.22 Segregation of networks |
| OWASP ASVS 5.0 | V1 Encoding and Sanitization; V13 Configuration |
| OWASP SAMM 2.0 | Verification: Security Testing |
| OWASP Top 10:2025 | A01 Broken Access Control; A02 Security Misconfiguration; A05 Injection |
| OWASP API Security | API7:2023 Server Side Request Forgery |
| OWASP Cheat Sheet Series | Input Validation; Injection Prevention; Secrets Management |

## Required actions

1. **Constrain destinations in application code — Application owner**
   - Per **SSRF-M-001**: permit only explicitly approved URL schemes, hosts, and ports.
   - Prefer centrally managed allowlists over denylist-only validation.
   - Reject internal, loopback, private, link-local, and cloud metadata destinations.

2. **Control DNS and redirects — Application owner**
   - Per **SSRF-M-001**: control DNS rebinding and redirect following.
   - Revalidate every redirect destination before following it.
   - Do not permit a validated public hostname to resolve or redirect to a prohibited address.

3. **Enforce independent network egress restrictions — Network or cloud platform owner**
   - Per **SSRF-M-001**: restrict workload egress at the network layer.
   - Route URL-fetching workloads through an egress proxy or equivalent policy-enforcement point that permits only approved destinations.
   - Block direct access to internal and metadata networks regardless of application validation.

4. **Protect cloud metadata — Cloud platform owner**
   - Per **SSRF-M-001**: block cloud metadata addresses.
   - Where applicable, require session-based metadata access such as IMDSv2 as defence in depth.

5. **Test before release — Engineering and application security**
   - Per **SSRF-M-001**: test URL-fetching features for SSRF, metadata access, DNS rebinding, and redirect bypass.
   - Make failed SSRF tests or prohibited egress attempts release-blocking findings.

6. **Govern destination changes — Service owner**
   - **Advisory (not knowledge-doc backed):** assign an owner to each allowlist entry, document the business purpose, review changes through code/configuration control, and expire temporary entries.
   - **Advisory (not knowledge-doc backed):** exceptions should document the destination scope, data exposed, compensating controls, approver, and expiry date.

No knowledge document was found for this point: the authoritative guidance lookup returned no knowledge document mapped to **SSRF-M-001**. The implementation requirements above therefore come from the Mandard catalogue; additional governance suggestions are explicitly marked advisory.

## Evidence for audit

Retain:

- Version-controlled scheme, hostname, and port allowlist configuration.
- Egress proxy, firewall, security-group, or network-policy configuration showing default-deny outbound controls.
- Automated test results covering internal addresses, link-local and metadata endpoints, redirects, and DNS rebinding.
- CI/CD evidence demonstrating that failed SSRF tests block deployment.
- Cloud configuration evidence showing metadata endpoint restrictions and, where applicable, IMDSv2 enforcement.
- Logs showing rejected destinations and denied outbound connections, with sensitive URL components redacted.
- **Advisory (not knowledge-doc backed):** approved, time-limited exception records for any destination not covered by standard policy.

## Assumptions and limits

No service architecture, source code, deployment configuration, DNS behavior, redirect handling, or network egress policy was inspected. No knowledge document is currently mapped to **SSRF-M-001**; therefore, organisation-specific implementation procedures could not be verified.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**SSRF-M-001**](https://verify.example-org.internal/?id=SSRF-M-001) | High | SSRF Prevention | CIS_CONTROLS (CIS 12, CIS 16); CWE (CWE-20, CWE-77, CWE-798); ISO_27001 (A.5.17, A.8.20, A.8.22); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, IA-5, SA-11); OWASP (A01:2025, A02:2025, A05:2025); +6 more |

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