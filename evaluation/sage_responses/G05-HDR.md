# G05-HDR

## Question
Which security headers are non-negotiable for internet-facing apps?

## Sage response

## Bottom line

Internet-facing applications must implement every applicable **HDR-M** control; the minimum release baseline is not limited to HSTS and CSP. The highest-priority controls prevent transport downgrade, XSS, MIME confusion, information leakage, excessive browser permissions, cross-origin exposure, and technology fingerprinting. Production release should be blocked for any unmet Critical or High control; other applicable controls require remediation or a formally approved deviation.

## Risk and impact

| Priority | Exposure if missing |
|---|---|
| Critical | XSS and data exfiltration, SSL stripping, MIME-sniffing attacks, sensitive URL leakage, browser-feature abuse, cross-origin data exposure, and attacker reconnaissance |
| High | Encoding-based XSS, incorrect content handling, and sensitive information retained in browser or intermediary caches |
| Medium | Clickjacking, search-engine indexing of protected resources, and obsolete or hazardous header configurations |
| Low | Legacy cross-domain access, tab-nabbing/window isolation weaknesses, and browsing-metadata leakage |

## Governing mandards

The complete HTTP-header domain contains the following controls. “Conditional” means the control applies when the stated content or application behaviour exists; it is still mandatory when applicable.

| Mandard | Title | Risk | Required posture |
|---|---|---:|---|
| **HDR-M-001** | Enforce X-Content-Type-Options | Critical | All responses: `X-Content-Type-Options: nosniff` |
| **HDR-M-002** | No Server Banners | Critical | Remove or obfuscate `Server`, `X-Powered-By`, `X-AspNet-Version`, and `X-AspNetMvc-Version` |
| **HDR-M-003** | Enforce HSTS | Critical | HTTPS responses: `Strict-Transport-Security` with a valid `max-age`, for example `31536000` |
| **HDR-M-004** | Clickjacking Protection | Medium | `X-Frame-Options: SAMEORIGIN` or CSP `frame-ancestors 'self'`/`'none'` |
| **HDR-M-005** | Disable Legacy X-XSS-Protection Filter | Critical | Omit `X-XSS-Protection` or set it to `0`; never enable `1; mode=block` |
| **HDR-M-006** | Enforce Content-Type and Charset | High | Accurate `Content-Type` on every response; HTML must include `charset=UTF-8` |
| **HDR-M-007** | Enforce Referrer Policy | Critical | `Referrer-Policy: strict-origin-when-cross-origin` or stricter |
| **HDR-M-008** | Enforce Permissions Policy | Critical | Disable unnecessary high-risk features, such as `camera=(), microphone=(), geolocation=()` |
| **HDR-M-009** | Cache-Control for Sensitive Data | High | **Conditional:** sensitive responses require `Cache-Control: no-cache, no-store, must-revalidate` |
| **HDR-M-010** | X-Permitted-Cross-Domain-Policies | Low | `X-Permitted-Cross-Domain-Policies: none` |
| **HDR-M-011** | Cross-Origin-Resource-Policy CORP | Critical | `Cross-Origin-Resource-Policy: same-origin` or `same-site` |
| **HDR-M-012** | Cross-Origin-Embedder-Policy COEP | Critical | `Cross-Origin-Embedder-Policy: require-corp` |
| **HDR-M-013** | Cross-Origin-Opener-Policy COOP | Low | `Cross-Origin-Opener-Policy: same-origin` |
| **HDR-M-014** | Content Security Policy CSP | Critical | Application-specific restrictive CSP; avoid `unsafe-inline` and `unsafe-eval` where possible |
| **HDR-M-015** | Enforce X-Robots-Tag for Non-Public Content | Medium | **Conditional:** protected content requires `X-Robots-Tag: noindex, nofollow` |
| **HDR-M-016** | Disable DNS Prefetching for Untrusted Links | Low | **Conditional:** pages with untrusted or third-party links require `X-DNS-Prefetch-Control: off` |
| **HDR-M-017** | Remove Deprecated Security Headers | Medium | Production must not emit `Expect-CT` or `Public-Key-Pins` |

Per **HDR-M-001**, **HDR-M-003**, **HDR-M-007**, **HDR-M-008**, **HDR-M-011**, **HDR-M-012**, and **HDR-M-014**, these headers are Critical controls and should be treated as release-blocking. Per **HDR-M-002** and **HDR-M-005**, removing unsafe or disclosing headers is equally non-negotiable.

## Framework mapping

Key catalogue-returned mappings include:

| Mandard | Direct framework mappings |
|---|---|
| **HDR-M-001** | NIST SP 800-53 Rev.5 `CM-6`, `SA-11`, `SI-10`, `SI-4`, `AU-6`, `SC-8`, `SC-18`, `IR-4`, `IR-6`; PCI DSS v4.0 `Req 6` |
| **HDR-M-006** | NIST SP 800-53 Rev.5 `CM-6`, `SI-10`, `SC-8`, `SC-18`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V1`, `V13`; NIST CSF 2.0 `PR.PS-01`, `PR.DS-01`; CIS Controls v8 `CIS 16` |
| **HDR-M-014** | NIST SP 800-53 Rev.5 `CM-6`, `SI-10`, `SI-15`, `SA-11`, `SC-8`, `SC-18`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V1`, `V13`; NIST CSF 2.0 `PR.PS-01`, `PR.DS-01`; CIS Controls v8 `CIS 16` |
| **HDR-M-016** | NIST SP 800-53 Rev.5 `CM-6`, `SC-7`; ISO/IEC 27001:2022 `A.8.26`; GDPR `Article 32`; OWASP ASVS 5.0 `V13`; NIST CSF 2.0 `PR.PS-01` |
| **HDR-M-017** | NIST SP 800-53 Rev.5 `CM-6`, `CM-7`, `SC-8`; PCI DSS v4.0 `Req 2`; ISO/IEC 27001:2022 `A.8.9`, `A.8.26`; OWASP ASVS 5.0 `V13`; CIS Controls v8 `CIS 4`; NIST CSF 2.0 `PR.PS-01` |

These are representative direct mappings returned for the cited controls, not an exhaustive cross-framework matrix.

## Required actions

1. **Platform or edge owner:** Establish the Critical and High headers as centrally managed defaults at the CDN, ingress controller, reverse proxy, API gateway, or web-server layer.
2. **Application team:** Develop an application-specific CSP under **HDR-M-014**. Start in report-only mode for compatibility analysis, then enforce it; do not accept a permanently permissive policy as compliance.
3. **Platform and application teams:** Test **HDR-M-012** before enforcement because `require-corp` can block third-party resources that do not explicitly permit embedding. Any inability to comply requires a documented deviation rather than silent omission.
4. **Data owner and application team:** Identify sensitive routes and enforce **HDR-M-009**; identify non-public downloads and enforce **HDR-M-015**.
5. **DevSecOps:** Add a post-deployment header scan covering HTML, API, static-file, error, redirect, authenticated, and sensitive responses. Fail the pipeline on Critical or High violations.
6. **Security architecture:** Review exceptions for cross-origin integrations, framing, browser permissions, and third-party scripts. Record approved deviations with scope, expiry, compensating controls, and accountable owner.

No header-specific knowledge document mapped to the **HDR-M** controls was found. The knowledge search returned eight documents, but they were set aside because they concerned broader authentication, endpoint, web-service, or architecture guardrails and did not carry **HDR-M** references.

## Evidence for audit

Retain:

- The production edge, proxy, gateway, or application middleware configuration.
- A CI/CD header-scan report showing expected values across representative routes and response types.
- DAST results from OWASP ZAP, Burp Suite, AppScan, or an equivalent scanner.
- CSP report-only telemetry and the approval record for transition to enforcement.
- An endpoint inventory identifying sensitive and non-public routes covered by **HDR-M-009** and **HDR-M-015**.
- Formal, time-bound deviation approvals for any unmet applicable control.

## Assumptions and limits

The application’s current headers, route inventory, third-party dependencies, CSP compatibility, and approved deviations were not inspected. No header-specific implementation knowledge document mapped to **HDR-M** was available; implementation details above are taken from the Mandard catalogue itself.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**HDR-M-001**](https://verify.example-org.internal/?id=HDR-M-001) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CM-6, IR-4); OWASP (A02:2025); +6 more |
| [**HDR-M-002**](https://verify.example-org.internal/?id=HDR-M-002) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16); CWE (CWE-200); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025); +5 more |
| [**HDR-M-003**](https://verify.example-org.internal/?id=HDR-M-003) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CM-6, IR-4); OWASP (A02:2025); +6 more |
| [**HDR-M-004**](https://verify.example-org.internal/?id=HDR-M-004) | Medium | HTTP Headers | CIS_CONTROLS (CIS 16); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025); OWASP_ASVS (V13, V3); +4 more |
| [**HDR-M-005**](https://verify.example-org.internal/?id=HDR-M-005) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16); CWE (CWE-77, CWE-79); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025, A05:2025); +5 more |
| [**HDR-M-006**](https://verify.example-org.internal/?id=HDR-M-006) | High | HTTP Headers | CIS_CONTROLS (CIS 16); CWE (CWE-436, CWE-79); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SC-18, SC-8); OWASP (A02:2025, A05:2025); +3 more |
| [**HDR-M-007**](https://verify.example-org.internal/?id=HDR-M-007) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025); OWASP_ASVS (V13); +4 more |
| [**HDR-M-008**](https://verify.example-org.internal/?id=HDR-M-008) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285, CWE-77); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**HDR-M-009**](https://verify.example-org.internal/?id=HDR-M-009) | High | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CM-6, IR-4); OWASP (A02:2025); +6 more |
| [**HDR-M-010**](https://verify.example-org.internal/?id=HDR-M-010) | Low | HTTP Headers | CIS_CONTROLS (CIS 16); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025); OWASP_ASVS (V13); +4 more |
| [**HDR-M-011**](https://verify.example-org.internal/?id=HDR-M-011) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.26, A.8.27, A.8.28); NIST_CSF (PR.DS-01, PR.IR-01, PR.PS-01); NIST_SP_800_53 (CM-2, CM-6, CM-7); +6 more |
| [**HDR-M-012**](https://verify.example-org.internal/?id=HDR-M-012) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**HDR-M-013**](https://verify.example-org.internal/?id=HDR-M-013) | Low | HTTP Headers | CIS_CONTROLS (CIS 16); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025); OWASP_ASVS (V13); +4 more |
| [**HDR-M-014**](https://verify.example-org.internal/?id=HDR-M-014) | Critical | HTTP Headers | CIS_CONTROLS (CIS 16); CWE (CWE-77, CWE-79); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (CM-6, SA-11, SC-18); OWASP (A02:2025, A05:2025); +5 more |
| [**HDR-M-015**](https://verify.example-org.internal/?id=HDR-M-015) | Medium | HTTP Headers | CWE (CWE-200); ISO_27001 (A.5.34, A.8.26); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-22, CM-6, SC-8); OWASP (A02:2025); OWASP_ASVS (V13); +2 more |

Showing 15 of 17 cited mandards.

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