# G46-EDGE

## Question
What controls are required for edge-delivered application traffic?

## Sage response

## Bottom line

Edge-delivered HTTP/HTTPS application traffic must pass through a WAF that is actively managed, enforces the OWASP Core Rule Set, and is tuned using monitored false-positive data. The primary exposure is successful injection, cross-site scripting, other OWASP Top 10 attacks, or operational pressure to disable the WAF because legitimate traffic is blocked.

## Risk and impact

| Mandard | Risk | Exposure if unaddressed |
|---|---:|---|
| **WAF-M-001** | High | Malicious HTTP/HTTPS patterns may reach the application without inspection; stale rules may miss current threats. |
| **WAF-M-002** | High | OWASP Top 10 attack patterns and known exploits may bypass an absent or outdated CRS. |
| **WAF-M-003** | Medium | Excessive false positives may disrupt customers or cause teams to weaken or disable WAF protection. |

## Governing mandards

- **WAF-M-001 — WAF Rule Configuration & Management — High.** Per **WAF-M-001**: deploy a WAF to inspect HTTP/HTTPS traffic for malicious patterns and update its rules at least weekly using threat intelligence.
- **WAF-M-002 — OWASP CRS Core Rule Set Enforcement — High.** Per **WAF-M-002**: enforce the OWASP CRS, keep it current within 30 days of a release, and test after updates.
- **WAF-M-003 — WAF False Positive Tuning Process — Medium.** Per **WAF-M-003**: monitor and tune the WAF to maintain a false-positive rate below 5%, customising rules for legitimate application-specific traffic.

## Framework mapping

The catalogue returned the following mappings:

| Mandard | Framework mappings |
|---|---|
| **WAF-M-001** | NIST SP 800-53 Rev. 5: CM-6, SI-10, SI-15, SA-11, SI-4, SI-7, SC-8, SC-18, SC-7, AC-4, SC-5; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.20, A.8.22, A.8.26, A.8.28; OWASP ASVS 5.0: V1, V13; OWASP SAMM 2.0: Verification—Security Testing. |
| **WAF-M-002** | NIST SP 800-53 Rev. 5: CM-6, SA-11, SI-10, SI-4, SI-7, SC-8, SC-18, SC-7, AC-4, SC-5; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.20, A.8.22, A.8.26, A.8.28; OWASP ASVS 5.0: V13; OWASP SAMM 2.0: Verification—Security Testing; OWASP Top 10:2025: A02; CIS Controls v8: CIS 16. |
| **WAF-M-003** | NIST SP 800-53 Rev. 5: CM-6, SA-11, SI-10, SI-4, AU-6, SI-7, SC-8, SC-18, SC-7, AC-4, SC-5; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.16, A.8.20, A.8.22, A.8.26, A.8.28; SOC 2: CC7.2; OWASP ASVS 5.0: V13; OWASP SAMM 2.0: Verification—Security Testing and Operations—Incident Management; OWASP Top 10:2025: A02. |

## Required actions

1. **Route applicable edge traffic through the WAF.**  
   Per **WAF-M-001**, ensure HTTP and HTTPS requests are inspected before reaching the application origin. The platform/network security owner should verify association with each public application endpoint, load balancer, or API gateway.

2. **Manage WAF policy as reviewed configuration.**  
   Per **WAF-M-001**, define WAF configurations through Infrastructure as Code with version control and peer review rather than unmanaged portal changes. Cover common attack vectors such as SQL injection, XSS, and malicious IP reputation.

3. **Enable preventive OWASP CRS enforcement.**  
   Per **WAF-M-002**, activate the OWASP CRS and configure application-appropriate anomaly scoring. Maintain the CRS within 30 days of each release and test updates before or during controlled rollout.

4. **Update threat-driven rules at least weekly.**  
   Per **WAF-M-001**, establish a weekly rule-update cycle informed by threat intelligence. This applies independently of the 30-day CRS release deadline.

5. **Monitor and tune false positives weekly.**  
   Per **WAF-M-003**, measure the false-positive rate and keep it below 5%. Use granular rule exclusions or overrides for confirmed legitimate requests rather than disabling complete managed-rule groups.

6. **Record tuning decisions.**  
   Per **WAF-M-003**, link exclusions to tickets and document their justification so security impact, approver, affected rule, scope, and expiry or review date are traceable.

**Knowledge-document linkage:**  
The authoritative guidance mapping identifies these documents for **WAF-M-001**:

- **VeriFy-NET-001**, mapped to **WAF-M-001** — [2. Network / Connectivity Layer](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652023403)
- **VeriFy-WS-002**, mapped to **WAF-M-001** — [4. Web Services Layer](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817293)
- **VeriFy-DECOM-002**, mapped to **WAF-M-001** — [14. Decommissioning & Destruction](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/720666741)

No knowledge document was found for **WAF-M-002** or **WAF-M-003**. The procedural actions above therefore rely on the implementation information in the mandard catalogue; no additional knowledge-document procedure is asserted.

## Evidence for audit

Retain:

- An inventory mapping every edge-delivered application hostname or endpoint to its WAF policy.
- Exported WAF configuration showing HTTP/HTTPS inspection and attachment to the public ingress.
- Version-controlled IaC, peer-review records, deployment history, and evidence that manual drift is detected.
- WAF scan or cloud-policy results confirming managed rule groups are enabled.
- CRS configuration showing enabled version, prevention mode, and request-body inspection where applicable.
- Release records proving CRS updates occur within 30 days and general rule updates occur at least weekly.
- Post-update test results demonstrating malicious test traffic is blocked and legitimate business flows continue.
- Weekly false-positive reports demonstrating a rate below 5%.
- Tickets and approvals for granular exclusions, including justification and review history.

## Assumptions and limits

“Edge-delivered application traffic” was interpreted as HTTP/HTTPS traffic delivered through a CDN, reverse proxy, application gateway, load balancer, or comparable edge service. The catalogue search returned the complete **WAF-M** domain set above; it did not identify a mandard specifically titled for “edge-delivered application traffic.” TLS, certificate management, DDoS protection, bot management, origin restriction, and security-header requirements were not asserted because they were not established by the retrieved mandards.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**WAF-M-001**](https://verify.example-org.internal/?id=WAF-M-001) | High | Web Application Firewall | CIS_CONTROLS (CIS 12, CIS 16); CWE (CWE-77, CWE-79, CWE-89); ISO_27001 (A.8.20, A.8.22, A.8.26); MITRE_ATT&CK (M1020, M1021, M1031); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, CM-6, SA-11); +6 more |
| [**WAF-M-002**](https://verify.example-org.internal/?id=WAF-M-002) | High | Web Application Firewall | CIS_CONTROLS (CIS 12, CIS 16); ISO_27001 (A.8.20, A.8.22, A.8.26); MITRE_ATT&CK (M1021, M1031, M1037); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, CM-6, SA-11); OWASP (A02:2025); +5 more |
| [**WAF-M-003**](https://verify.example-org.internal/?id=WAF-M-003) | Medium | Web Application Firewall | CIS_CONTROLS (CIS 12, CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ISO_27001 (A.8.16, A.8.20, A.8.22); MITRE_ATT&CK (M1021, M1031, M1037); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AC-4, AU-6, CM-6); +7 more |

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