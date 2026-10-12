# G14-LOG

## Question
What is the minimum forensic logging baseline we cannot waive?

## Sage response

## Bottom line

The catalogue does **not** identify any logging control as categorically “non-waivable.” The defensible minimum is therefore: all four High-risk logging Mandards are mandatory by default and **must not be informally waived**; any exception requires the formal deviation process and recorded technical justification.

For every application, central SIEM streaming and trusted timestamps are the baseline. CI/CD environments additionally require comprehensive, immutable audit records retained for at least 90 days, centralized detection, alert routing, and quarterly rule tuning.

## Risk and impact

All four logging Mandards are rated **High**. Failure leaves the organisation unable to reconstruct incidents reliably, detect pipeline compromise promptly, establish event chronology, preserve evidence, or demonstrate non-repudiation.

For Highly Confidential and Confidential information, the implementation standard sets a stronger baseline: transactional and administrative logs across architectural layers, centralized SIEM and log-platform collection, seven-year retention, and non-repudiation. This is knowledge-document guidance rather than a separate Mandard requirement and remains subject to the documented deviation process.

## Governing mandards

| Mandard | Title | Risk | Minimum requirement |
|---|---|---:|---|
| **LOG-M-001** | Stream Logs to SIEM | High | Per **LOG-M-001**: application logging must actively stream logs at `INFO` level or higher to a central SIEM endpoint. |
| **LOG-M-002** | Implement Comprehensive CI/CD Audit Logging | High | Per **LOG-M-002**: CI/CD audit logs must be structured and parsable; include build, identity, artifact and security-event context; exclude plaintext secrets; and be retained for at least 90 days in immutable or append-only storage. |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High | Per **LOG-M-003**: all CI/CD audit logs must reach centralized aggregation or SIEM, with documented and version-controlled anomaly rules, severity-based routing, and at least quarterly tuning. |
| **LOG-M-004** | Trusted Time Synchronization for Security Events | High | Per **LOG-M-004**: security-event systems must use approved redundant authoritative time sources, emit unambiguous UTC timestamps, monitor synchronization health and drift, and not treat unreliable timestamps as authoritative evidence. |

**Implementation standard:** **VeriFy-AUD-002**, *11. Audit Trails, Event & Log Management*, mapped to **LOG-M-001**, **LOG-M-003**, and **LOG-M-004**, requires for Highly Confidential and Confidential information:

- End-to-end technical, security, and compliance event coverage across architectural layers.
- Transactional and administrative logging at minimum.
- SIEM or Azure Sentinel enforcement where applicable.
- Centralized ELP collection.
- Seven-year retention.
- Encrypted, audited, read-only evidence supporting non-repudiation.

Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664

No knowledge document is currently mapped to **LOG-M-002**; its implementation baseline therefore comes directly from the Mandard.

## Framework mapping

The catalogue returned the following mappings relevant to this baseline:

| Mandard | Framework controls returned |
|---|---|
| **LOG-M-001** | NIST SP 800-53 Rev. 5 `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SI-7`, `IR-4`, `IR-6`; PCI DSS v4.0 `Req 10`; ISO/IEC 27001:2022 `A.8.15`, `A.8.16`, `A.5.24`, `A.5.26`, `A.5.28`; HIPAA `164.312(b)`; SOC 2 `CC7.2`, `CC7.3`, `P8`; GDPR `Article 12`; OWASP ASVS `V16`. |
| **LOG-M-002** | NIST SP 800-53 Rev. 5 `AC-2`, `AC-3` were returned in the available result. |
| **LOG-M-003** | NIST SP 800-53 Rev. 5 `IA-2`, `IA-5`, `AC-7`, `AC-2`, `AC-3` were returned in the available result. |
| **LOG-M-004** | ISO/IEC 27001:2022 `A.8.17`; MITRE ATT&CK `M1029`, `M1047`; NIST SP 800-82r3 `6.2.12`. |

## Required actions

1. **Security Operations:** Enforce centralized SIEM ingestion for application logs at `INFO` or higher, with monitoring for ingestion failure. Per **LOG-M-001**.
2. **Platform Operations:** Configure approved redundant time sources, UTC application timestamps, drift/source-loss monitoring, and quarantine or flag evidence generated while synchronization is unreliable. Per **LOG-M-004**.
3. **CI/CD Platform Owner:** Enable structured audit records containing the complete build, actor, artifact, deployment, approval, scan, policy, and security-event context required by **LOG-M-002**.
4. **CI/CD Platform Owner:** Prevent plaintext secrets in logs and rotate any secret discovered. Store audit records for at least 90 days using immutable or append-only controls. Per **LOG-M-002**.
5. **SOC/SIEM Engineering:** Implement the anomaly detections specified by **LOG-M-003**, including failed authentication, privilege escalation, unauthorized pipeline changes, gate bypass, signature failure, secret exposure, unusual deployment activity, and anomalous service-account use.
6. **SOC/SIEM Engineering:** Version-control detection content, route alerts according to severity, test routing, and record quarterly tuning. Per **LOG-M-003**.
7. **Data Owner and Architecture:** For Highly Confidential or Confidential workloads, apply the seven-year, end-to-end logging and non-repudiation baseline in **VeriFy-AUD-002**, or submit a formal deviation with technical justification in the SAF pack.

## Evidence for audit

- SIEM source inventory showing each in-scope application and CI/CD platform actively ingesting.
- Test events proving successful end-to-end collection and searchable correlation.
- Logging configuration demonstrating `INFO` or higher and centralized destination.
- Sample CI/CD audit records proving all required build, identity, artifact, approval, scan, and security fields are present.
- Storage policy proving at least 90-day CI/CD retention and immutable or append-only enforcement.
- Secret-scanning results proving logs contain no plaintext credentials.
- Version-controlled SIEM rules, alert routing tests, incident tickets, and quarterly tuning records.
- Time-source configuration, synchronization-health dashboard, drift alerts, and UTC timestamp samples.
- For classified workloads, seven-year retention configuration and read-only/non-repudiation controls.
- Any approved deviation record and associated SAF-pack technical justification.

## Assumptions and limits

No catalogue evidence was found that makes these controls absolutely ineligible for exception. **VeriFy-AUD-002** explicitly provides for formally recorded deviations, so “cannot waive” should be interpreted as **cannot waive informally or without approved governance**, not as an absolute prohibition. Framework mapping output for **LOG-M-002** and **LOG-M-003** was truncated; only mappings visible in the returned tool results are stated.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-002**](https://verify.example-org.internal/?id=LOG-M-002) | High | Logging | CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |

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