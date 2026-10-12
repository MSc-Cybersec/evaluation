# G65-MON

## Question
What monitoring controls prove timely detection of security incidents?

## Sage response

## Bottom line

Timely incident detection is demonstrated by a chain of **centralized telemetry, automated detection rules, immediate routing, trusted timestamps, and recorded response activity**. The primary controls are **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, and **MON-M-001**, supported by **LOG-M-002** for CI/CD auditability. Management should require timestamped detection tests and incident records because the catalogue does not define a universal mean-time-to-detect target.

## Risk and impact

All identified monitoring and logging Mandards are rated **High**. Without them, security events may remain local or unanalyzed, unauthorized production changes may go undetected, and inconsistent timestamps may invalidate forensic timelines.

The principal exposures are:

- Delayed or missed detection of account compromise, privilege escalation, pipeline manipulation, and control bypass.
- Attackers deleting or altering local evidence before investigation.
- Alerts not reaching an accountable responder.
- Inability to prove elapsed time between the originating event, SIEM ingestion, alert generation, and analyst action.
- Unreliable incident evidence caused by clock drift.

## Governing mandards

### Directly applicable controls

| Mandard | Title | Risk | Contribution to timely detection |
|---|---|---:|---|
| **LOG-M-001** | Stream Logs to SIEM | High | Requires active application logging at `INFO` or higher to a central SIEM endpoint. |
| **LOG-M-002** | Implement Comprehensive CI/CD Audit Logging | High | Requires structured CI/CD audit records containing event, identity, artifact, security, and timing context; minimum retention is 90 days using immutable or append-only storage. |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High | Requires centralized CI/CD monitoring, defined detection rules, severity-based routing, version-controlled alerts, and quarterly tuning. P1 alerts require instant notification. |
| **LOG-M-004** | Trusted Time Synchronization for Security Events | High | Requires approved redundant time sources, UTC event timestamps, synchronization-health monitoring, and alerts for material drift or source loss. |
| **MON-M-001** | Monitor for Config Drift | High | Requires active alerting for unauthorized production configuration changes, including firewall and IAM-policy changes. |

Per **LOG-M-001**: security-relevant application logs must be streamed to a central SIEM so that they remain available for detection and incident response.

Per **LOG-M-003**: CI/CD logs must be analyzed through documented SIEM rules for failed authentication, privilege escalation, unauthorized pipeline changes, gate bypasses, signature failures, exposed secrets, unusual deployments, and anomalous service-account use.

Per **LOG-M-004**: event timestamps must be trustworthy; synchronization loss or material drift must alert operations, and unreliable timestamps must not be treated as authoritative evidence.

Per **MON-M-001**: unauthorized production configuration changes must generate active alerts.

### Complete monitoring and logging domain context

The catalogue also returned the following **High**-risk Mandards. They address operational resilience or vulnerability prioritization rather than directly proving incident-detection elapsed time:

| Mandard | Title | Risk | Applicability |
|---|---|---:|---|
| **MON-M-002** | Service Capacity Management and Scaling Assurance | High | Detects capacity threshold breaches and exhausted scaling headroom. |
| **MON-M-003** | Threat-Intelligence-Informed Vulnerability and Exploit Prioritization | High | Detects changes in exploit risk and reprioritizes remediation using threat intelligence. |

## Framework mapping

Only tool-returned mappings are stated below.

| Mandard | Verified framework mappings |
|---|---|
| **LOG-M-001** | NIST SP 800-53 Rev. 5: `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SI-7`, `IR-4`, `IR-6`; PCI DSS v4.0: `Req 10`; ISO/IEC 27001:2022: `A.8.15`, `A.8.16`, `A.5.24`, `A.5.26`, `A.5.28`; HIPAA: `164.312(b)`; SOC 2: `CC7.2`, `CC7.3`, `P8` |
| **LOG-M-003** | NIST SP 800-53 Rev. 5: `IA-2`, `IA-5`, `AC-7`, `AC-2`, `AC-3` |
| **LOG-M-004** | ISO/IEC 27001:2022: `A.8.17`; NIST SP 800-82r3: `6.2.12`; MITRE ATT&CK: `M1029`, `M1047` |
| **MON-M-001** | NIST SP 800-53 Rev. 5: `SI-4`, `AU-6`, `SI-7`, `CM-2`, `AC-2`, `AC-3`, `AC-4`, `AC-6`, `SC-7` |
| **MON-M-002** | ISO/IEC 27001:2022: `A.8.6` |
| **MON-M-003** | NIST SP 800-53 Rev. 5: `RA-3`; CIS Controls v8: `CIS 7`; NIST CSF 2.0: `ID.RA`; MITRE ATT&CK: `M1019` |

## Required actions

1. **Centralize security telemetry — Security Engineering / Application Owners**  
   Per **LOG-M-001**, forward application security logs at `INFO` or higher to the enterprise SIEM. Monitor source health so that stopped, delayed, or malformed feeds generate operational alerts.

2. **Implement automated detection and escalation — SOC / Detection Engineering**  
   Per **LOG-M-003**, deploy documented and version-controlled detection rules, assign alert severity, and route P1 alerts instantly to the on-call security function. Test the required CI/CD scenarios and retain quarterly tuning records.

3. **Preserve complete event context — DevSecOps / Platform Engineering**  
   Per **LOG-M-002**, record build, identity, artifact, security-event, and timing context in structured JSON or syslog. Retain records for at least 90 days in immutable or append-only storage and ensure plaintext secrets are excluded.

4. **Protect timestamp integrity — Infrastructure Operations**  
   Per **LOG-M-004**, synchronize event-producing systems with approved redundant sources, emit unambiguous UTC timestamps, monitor offset and source changes, and alert on synchronization loss or material drift.

5. **Detect unauthorized production changes — Cloud Security / DevOps**  
   Per **MON-M-001**, continuously monitor production configuration for drift, including manual firewall, IAM, logging, and cloud-console changes, and route findings into the SIEM or incident workflow.

6. **Measure and test detection latency — SOC Management**  
   **Advisory (not catalogue-backed):** define approved detection and acknowledgement objectives by incident severity. Run controlled alert simulations and calculate:

   `Detection latency = SIEM alert timestamp − originating event timestamp`

   Also record ingestion latency and analyst acknowledgement time separately. Do not use average time alone; retain percentile and breach data to expose slow outliers.

The implementation standard states that highly confidential and confidential systems should support end-to-end transactional and administrative audit trails, SIEM enforcement where applicable, centralized log retention, and non-repudiation. Source: **VeriFy-AUD-002**, *Audit Trails, Event & Log Management*, mapped to **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, and **MON-M-001**:  
https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664

## Evidence for audit

A defensible evidence pack should contain:

| Evidence | What it proves |
|---|---|
| SIEM source inventory and ingestion-health dashboard | Required systems are connected and feeds remain active under **LOG-M-001**. |
| Sample source and SIEM records with matching event identifiers | Events arrive centrally and can be correlated. |
| Version-controlled SIEM rules and approval history | Detection logic is governed under **LOG-M-003**. |
| Alert-routing configuration and on-call integration | High-severity alerts reach an accountable responder. |
| Controlled alert-test records | A known event generated the expected alert and route. |
| Incident tickets containing event, ingestion, alert, and acknowledgement timestamps | Actual detection and response latency can be calculated. |
| Quarterly rule-tuning record | Required tuning under **LOG-M-003** occurred. |
| CI/CD audit-log samples and immutable-retention configuration | Completeness and preservation under **LOG-M-002**. |
| Time-source configuration, offset dashboard, and drift-alert test | Timestamp reliability under **LOG-M-004**. |
| CSPM/configuration-drift dashboard and simulated-change alert | Runtime change detection under **MON-M-001**. |
| Approved exceptions in the SAF pack | Any departure from the logging guardrail is formally documented, as described in **VeriFy-AUD-002**: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664 |

## Assumptions and limits

- No production configuration, SIEM rule, alert route, incident record, or detection test was inspected.
- The returned Mandards do not establish a universal numeric mean-time-to-detect or acknowledgement target. Any such target requires an approved organizational risk decision.
- **LOG-M-003** provides explicit alerting expectations for CI/CD. Broader enterprise detection use cases may require additional Mandards; no suitable generic incident-detection SLA Mandard was found in this search.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-002**](https://verify.example-org.internal/?id=LOG-M-002) | High | Logging | CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**MON-M-002**](https://verify.example-org.internal/?id=MON-M-002) | High | Monitoring | ISO_27001 (A.8.6) |
| [**MON-M-003**](https://verify.example-org.internal/?id=MON-M-003) | High | Monitoring | CIS_CONTROLS (CIS 7); MITRE_ATT&CK (M1019); NIST_CSF (ID.RA); NIST_SP_800_53 (RA-3) |

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