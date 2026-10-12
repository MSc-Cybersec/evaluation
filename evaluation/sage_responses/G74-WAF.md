# G74-WAF

## Question
What governance checks are required before tuning WAF blocking rules?

## Sage response

## Bottom line

Do not tune production WAF blocking rules until the proposed change has been peer-reviewed, tested against legitimate and malicious traffic, assessed for OWASP CRS impact, and supported by measured false-positive evidence. Per **WAF-M-001**, configuration must be version-controlled as Infrastructure as Code rather than changed manually; per **WAF-M-003**, tuning must remain granular and maintain a false-positive rate below 5%.

## Risk and impact

- **High:** Poorly controlled changes can weaken protection against injection, XSS, malicious IPs, and other web attacks, or unintentionally remove OWASP CRS coverage.
- **Medium:** Overly aggressive blocking can disrupt legitimate transactions. Broad exclusions can also create exploitable protection gaps and encourage operators to disable the WAF.

## Governing mandards

| Mandard | Title | Risk | Required governance check |
|---|---|---:|---|
| **WAF-M-001** | WAF Rule Configuration & Management | High | Per **WAF-M-001**: confirm the WAF remains deployed for HTTP/HTTPS inspection, rules remain current on at least a weekly cycle, and changes are defined through version-controlled, peer-reviewed IaC rather than manual portal changes. |
| **WAF-M-002** | OWASP CRS Core Rule Set Enforcement | High | Per **WAF-M-002**: confirm OWASP CRS remains enforced, the CRS is updated within 30 days of release, application-tolerant anomaly thresholds are defined, and updates are tested. |
| **WAF-M-003** | WAF False Positive Tuning Process | Medium | Per **WAF-M-003**: review false positives weekly, maintain a false-positive rate below 5%, use application-specific customization, and prefer individual exclusions or overrides over disabling entire rule groups. Its implementation guidance calls for justification linked to a ticket for 90% of false-positive exclusions. |

## Framework mapping

Directly relevant mappings returned by the catalogue include:

| Mandard | Framework mappings |
|---|---|
| **WAF-M-001** | NIST SP 800-53 Rev.5: CM-6, SA-11, SI-4, SI-10, SI-7, SC-7, SC-5, SC-8, SC-18, AC-4; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.20, A.8.22, A.8.26, A.8.28; OWASP ASVS 5.0: V1, V13; OWASP SAMM 2.0: Verification—Security Testing. |
| **WAF-M-002** | NIST SP 800-53 Rev.5: CM-6, SA-11, SI-4, SI-10, SI-7, SC-7, SC-5, SC-8, SC-18, AC-4; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.20, A.8.22, A.8.26, A.8.28; OWASP ASVS 5.0: V13; OWASP SAMM 2.0: Verification—Security Testing; OWASP Top 10:2025: A02 Security Misconfiguration; CIS Controls v8: CIS 16. |
| **WAF-M-003** | NIST SP 800-53 Rev.5: CM-6, SA-11, SI-4, SI-10, AU-6, SI-7, SC-7, SC-5, SC-8, SC-18, AC-4; PCI DSS v4.0: Req 1, Req 6; ISO/IEC 27001:2022: A.8.16, A.8.20, A.8.22, A.8.26, A.8.28; SOC 2: CC7.2; OWASP ASVS 5.0: V13; OWASP SAMM 2.0: Verification—Security Testing and Operations—Incident Management; OWASP Top 10:2025: A02 Security Misconfiguration. |

## Required actions

1. **Establish the baseline.** Record the current rule set, CRS version, operating mode, anomaly threshold, exclusions, protected endpoints, and weekly update status. Per **WAF-M-001** and **WAF-M-002**, tuning must not remove WAF inspection or required CRS enforcement.

2. **Require a version-controlled change.** Per **WAF-M-001**, implement the proposal through IaC and subject it to peer review; do not make an untracked portal change.

3. **Substantiate the false positive.** Per **WAF-M-003**, use blocked-request telemetry to demonstrate that the traffic is legitimate and calculate the current false-positive rate. The required operating target is below 5%.

4. **Assess security coverage.** Per **WAF-M-002**, determine which CRS rule and attack class are affected. Test both legitimate requests and representative malicious payloads before enabling the change in blocking mode.

5. **Use the narrowest exception.** Per **WAF-M-003**, prefer a rule-specific, parameter-specific, path-specific, or similarly granular exclusion. Do not disable an entire managed rule group merely to address one false positive.

6. **Document the justification.** Per **WAF-M-003**, link exclusions to a ticket and record the affected rule, endpoint, evidence, security impact, and justification.

7. **Validate application-specific thresholds.** The mapped guidance in **VeriFy-WS-002**, referencing **WAF-M-001**, requires analysis before enforcing acceptable WAF rate-limiting thresholds for externally exposed on-premises web services. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817293.

8. **Advisory (not catalogue-backed):** Require the application owner and security/WAF owner to approve the production change, define a rollback trigger, use a controlled deployment window, and perform heightened monitoring immediately after activation.

## Evidence for audit

Retain:

- IaC pull request, peer-review record, approved deployment output, and configuration diff.
- Pre-change WAF configuration export and post-change effective policy.
- CRS version and evidence that it is within the required update window.
- False-positive analysis, blocked-request samples, and calculated false-positive rate.
- Test results showing legitimate traffic succeeds while representative attacks remain blocked.
- Ticket-linked justification for each exclusion or override.
- Post-deployment WAF metrics, alerts, and weekly tuning-review record.
- Approval and rollback records where the advisory change-control process is adopted.

## Assumptions and limits

No target WAF configuration, telemetry, false-positive sample, approval workflow, or proposed rule change was inspected. No knowledge document is currently mapped to **WAF-M-002** or **WAF-M-003**; implementation detail for those controls therefore comes from the mandard catalogue itself. **VeriFy-DECOM-002** was set aside because it addresses removal of WAF rules during decommissioning, not rule tuning; general endpoint and pipeline documents were also set aside because they are not mapped to these WAF tuning mandards.

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