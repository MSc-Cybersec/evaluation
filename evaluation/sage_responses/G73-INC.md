# G73-INC

## Question
What incident-response evidence is required for major security events?

## Sage response

## Bottom line

For a major security event, retain a single, time-correlated incident record proving detection, escalation, automated response, evidence collection, root-cause analysis, corrective actions, post-incident review, and notification decisions. Critical incidents must evidence alerting within 15 minutes and a post-incident review within five business days; every security incident requires a documented RCA within 30 days. Missing or incomplete records expose the organisation to regulatory breach, repeat incidents, and inability to demonstrate an effective response.

## Risk and impact

- **Critical:** Failure to prove timely detection and alerting increases compromise duration and prevents demonstration of SLA compliance.
- **High:** Missing response-execution, RCA, or notification evidence can result in inconsistent containment, repeated failures, missed statutory deadlines, and unsubstantiated external communications.
- **Medium:** Missing review and performance metrics prevents management from assessing and improving incident-response effectiveness.

Where personal data is involved, the notification clock runs from awareness rather than resolution. Per **INC-M-005**, GDPR-covered incidents require supervisory-authority notification within 72 hours of awareness unless a shorter applicable local deadline exists; a reasoned decision must be recorded when notification is deemed unnecessary.

## Governing mandards

| Mandard | Title | Risk level | Required evidence |
|---|---|---:|---|
| **INC-M-001** | Incident Detection & Alerting SLA | Critical | Detection timestamp, alert timestamp, severity classification, escalation/acknowledgement record, and evidence of monthly alert testing. Critical: 15 minutes; High: 1 hour; Medium: 4 hours; Low: 24 hours. |
| **INC-M-002** | Incident Response Automation | High | Approved playbook used, automation/SOAR execution logs, isolation or blocking actions, collected evidence references, and notification output. |
| **INC-M-003** | Root Cause Analysis Process | High | RCA completed within 30 days, including contributing factors, systemic issues, recurrence prevention, corrective actions, owners, and linked remediation tickets. |
| **INC-M-004** | Post-Incident Review & Metrics | Medium | For Critical incidents, review record completed within five business days; documented lessons learned and metrics for detection time, response time, resolution time, and recurrence rate. |
| **INC-M-005** | Incident and Breach Notification and Stakeholder Communication | High | Awareness timestamp, notification deadline, impact/notifiability assessment, legal or governance review, approval record, notices sent, delivery timestamps, contact register, exercise evidence, or the reasoned decision not to notify. |

Per **INC-M-001**: incident alerting must meet severity-based SLAs.  
Per **INC-M-002**: playbooks must automate initial isolation, evidence collection, and notification for common incident types.  
Per **INC-M-003**: every security incident must have a documented RCA completed within 30 days.  
Per **INC-M-004**: Critical incidents require a post-incident review within five business days and defined response metrics.  
Per **INC-M-005**: notification authority, statutory timing, stakeholder communication, and decisions not to notify must be documented.

## Framework mapping

The SAGF catalogue returned the following directly relevant mappings:

| Mandard | Framework mappings |
|---|---|
| **INC-M-001** | NIST SP 800-53 Rev.5: SI-4, AU-6, IR-4, IR-6, IR; ISO/IEC 27001:2022: A.8.16, A.5.24, A.5.25, A.5.26, A.6.8; SOC 2: CC7.2, CC7.3; GDPR: Articles 33 and 34; CIS Controls v8: CIS 8, CIS 17 |
| **INC-M-002** | NIST SP 800-53 Rev.5: SI-4, AU-6, IR-4, IR-6; ISO/IEC 27001:2022: A.8.16, A.5.24, A.5.26; SOC 2: CC7.2, CC7.3; CIS Controls v8: CIS 8, CIS 17; NIST CSF 2.0: DE.CM-01, DE.AE-02, RS.MA-01, RS.AN-03, RS.MI |
| **INC-M-003** | NIST SP 800-53 Rev.5: SI-4, AU-6, IR-4, IR-6; ISO/IEC 27001:2022: A.5.24, A.5.26, A.5.27, A.5.28, A.8.16; SOC 2: CC7.2, CC7.3; CIS Controls v8: CIS 8, CIS 17; NIST SSDF: RV.3 |
| **INC-M-004** | NIST SP 800-53 Rev.5: SI-4, AU-6, IR-4, IR-6; ISO/IEC 27001:2022: A.5.24, A.5.26, A.5.27, A.8.16; SOC 2: CC7.2, CC7.3; NIST CSF 2.0: ID.IM, RS.CO, RC.CO |
| **INC-M-005** | NIST SP 800-53 Rev.5: IR-6, IR; ISO/IEC 27001:2022: A.6.8; SOC 2: P6; GDPR: Articles 33 and 34; NIST CSF 2.0: RS.CO-02, RS.CO-03, RC.CO-03, RC.CO-04, RS.CO, RC.CO; DORA: Articles 17–23 and 45 |

## Required actions

1. **Incident Commander and SOC — Critical:** Create one authoritative incident record with severity, start/detection/alert/acknowledgement timestamps, affected assets, accountable roles, and a chronological response log. Use it to demonstrate the **INC-M-001** SLA.
2. **SOC/Security Engineering — High:** Attach the executed playbook and SOAR or platform logs showing isolation, account suspension, IP blocking, evidence collection, and notifications under **INC-M-002**.
3. **Incident Commander and system owners — High:** Complete the RCA within 30 days, record contributing and systemic factors, and link each corrective action to an owner and tracked remediation ticket under **INC-M-003**.
4. **CISO office, Privacy, and Legal — High:** Record the awareness timestamp, statutory deadline, notifiability decision, legal basis, approver, recipients, notices, and delivery times under **INC-M-005**. Preserve a reasoned decision where notification is not required.
5. **Incident Commander — Medium:** For Critical incidents, complete the post-incident review within five business days and capture lessons learned under **INC-M-004**.
6. **Security Operations — Medium:** Retain metrics showing detection, response, and resolution times and recurrence rate; include the source timestamps or dashboard query used to calculate them.

## Evidence for audit

A defensible evidence pack should contain:

- Incident-management ticket and immutable event chronology.
- Original SIEM alert, source-event references, severity decision, escalation, and acknowledgement timestamps.
- SOAR/playbook version, execution log, action results, and exceptions or manual overrides.
- References to collected logs or forensic artefacts and the systems from which they were obtained.
- Containment and recovery records, including affected assets and action timestamps.
- Completed RCA with contributing factors, systemic causes, corrective actions, owners, and linked tickets.
- Critical-incident review minutes or approved report dated within five business days.
- MTTD, response-time, resolution-time, and recurrence-rate report with source data.
- Awareness timestamp, notification assessment, legal/governance approval, statutory countdown, submitted notices, delivery confirmation, and stakeholder communications.
- Written rationale and approval where notification was assessed as unnecessary.
- Current regulator/customer/partner contact register and evidence that the communication route was exercised.

## Assumptions and limits

No knowledge document is currently mapped to **INC-M-001** through **INC-M-005**. The evidence checklist above is derived from the mandard descriptions, implementation fields, and verification intent; no separate organisation-specific incident evidence procedure was found. Preserving immutable timelines, forensic artefact provenance, and manual-override records is **Advisory (not knowledge-doc backed)** where not expressly stated by the cited mandard.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**INC-M-001**](https://verify.example-org.internal/?id=INC-M-001) | Critical | Incident Response | AIUC1 (E001, E002, E003); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (APO13.01, DSS02.01, DSS05.07); CSA_CCM (SEF); DORA (Art. 17-23); ENISA_SMLA (SMLA-28); +10 more |
| [**INC-M-002**](https://verify.example-org.internal/?id=INC-M-002) | High | Incident Response | AIUC1 (E001); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (APO13.01, DSS02.01, DSS05.07); CSA_CCM (SEF); GDPR (Article 33); ISO_27001 (A.5.24, A.5.26, A.8.16); +7 more |
| [**INC-M-003**](https://verify.example-org.internal/?id=INC-M-003) | High | Incident Response | CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (APO13.01, DSS02.01, DSS03); CSA_CCM (SEF); ISO_27001 (A.5.24, A.5.26, A.5.27); NIST_800_218A (RV.3); NIST_800_82 (6.4.3); +6 more |
| [**INC-M-004**](https://verify.example-org.internal/?id=INC-M-004) | Medium | Incident Response | CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (APO13.01, DSS02.01, DSS05.07); GDPR (Article 34); HIPAA (164.400); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); ISO_27001 (A.5.24, A.5.26, A.5.27); +7 more |
| [**INC-M-005**](https://verify.example-org.internal/?id=INC-M-005) | High | Incident Response | DORA (Art. 17-23, Art. 45); GDPR (Article 33, Article 34); HIPAA (164.400); ISO_27001 (A.6.8); MITRE_ATT&CK (M1060); NIST_800_82 (6.4.2, 6.5.3); +4 more |

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