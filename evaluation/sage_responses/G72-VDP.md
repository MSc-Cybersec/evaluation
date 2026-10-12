# G72-VDP

## Question
What controls are needed to run a vulnerability disclosure process safely?

## Sage response

## Bottom line

Per **VDP-M-001**, the organisation must publish a vulnerability disclosure policy and reachable reporting channel, operate monitored intake, triage and acknowledge reports under defined SLAs, coordinate remediation and disclosure, and document safe-harbor terms for good-faith research. Failure creates a **Medium** risk that vulnerabilities are publicly disclosed or exploited before remediation. Assign an accountable security owner and approve the policy, SLAs, safe-harbor language, and operating workflow before launch.

## Risk and impact

**Risk level: Medium.**

Without a controlled disclosure process:

- External researchers may have no safe or reliable way to report vulnerabilities.
- Reports may be lost, mishandled, or remain unremediated.
- Premature public disclosure can expose customers, systems, data, and organisational reputation.
- Poorly defined safe harbor may discourage legitimate reporting or create avoidable legal disputes.
- Lack of evidence and SLA tracking prevents management oversight and audit assurance.

## Governing mandards

| Mandard | Title | Risk | Required control |
|---|---|---:|---|
| **VDP-M-001** | Vulnerability Disclosure and Coordinated Response | Medium | Operate a published vulnerability disclosure policy, reachable reporting channel, monitored intake, defined acknowledgement and remediation SLAs, coordinated disclosure, and documented safe harbor for good-faith research. |

This is the complete `VDP-M` domain set returned by the catalogue.

## Framework mapping

The catalogue maps **VDP-M-001** to the following controls:

| Framework | Mapped controls |
|---|---|
| NIST SP 800-53 Rev. 5 | SI-4 System Monitoring; AU-6 Audit Record Review, Analysis, and Reporting; PL-8 Security and Privacy Architectures; PM-9 Risk Management Strategy; PL-2 System Security and Privacy Plans; IR-4 Incident Handling; IR-6 Incident Reporting |
| ISO/IEC 27001:2022 Annex A | A.8.16 Monitoring activities; A.5.24 Information security incident management planning and preparation; A.5.26 Response to information security incidents |
| SOC 2 Type II | CC7.2 System Monitoring; CC7.3 Incident Response |
| OWASP SAMM 2.0 | Governance: Policy & Compliance; Operations: Incident Management |
| COBIT 2019 | EDM03.01 Evaluate Risk Management; APO12.01 Collect Data; DSS05.07 Manage Vulnerabilities and Monitor Infrastructure; MEA03.01 Identify External Requirements; DSS02.01 Define Classification Schemes |
| CIS Controls v8 | CIS 8 Audit Log Management; CIS 17 Incident Response Management |
| NIST CSF 2.0 | GV.OC-01 Organizational Context; GV.RM-01 Risk Management Strategy; DE.CM-01 Networks and Network Services Monitored; DE.AE-02 Potentially Adverse Events Analyzed |

## Required actions

1. **Publish the disclosure policy and reporting channel — Security/GRC owner**  
   Per **VDP-M-001**: provide a public policy, a reachable `/.well-known/security.txt`, and a monitored intake mechanism.

   Minimum catalogue example:

   ```text
   Contact: mailto:security@example.com
   Policy: https://example.com/vdp
   Expires: 2027-01-01T00:00:00Z
   ```

   Use organisation-specific addresses, URLs, and a maintained future expiry date.

2. **Document safe-harbor terms — Legal and Security**  
   Per **VDP-M-001**: clearly document the protections and expectations applying to good-faith security research.

3. **Establish intake and ownership — Security Operations or Product Security**  
   Per **VDP-M-001**: continuously monitor the reporting channel and route each submission to an accountable handler. Avoid relying on an individual mailbox without coverage.

4. **Define and track response SLAs — Product Security and service owners**  
   Per **VDP-M-001**: establish measurable SLAs for acknowledgement, triage, and remediation. The catalogue does not prescribe numeric targets; management must approve targets appropriate to organisational risk.

5. **Operate a triage and remediation workflow — Product Security and engineering**  
   Per **VDP-M-001**: assess incoming reports, acknowledge receipt, assign remediation ownership, track progress against SLA, and verify remediation before closure.

6. **Coordinate disclosure — Security, Communications, Legal, and affected owners**  
   Per **VDP-M-001**: coordinate publication timing and communication with the reporter so that disclosure does not unnecessarily precede remediation.

7. **Monitor channel availability and SLA performance — Security Operations**  
   Per **VDP-M-001**: verify that the disclosure endpoint remains reachable and that intake and remediation SLAs are being met. A basic availability check is:

   ```bash
   curl -sf https://example.com/.well-known/security.txt
   ```

**Advisory (not knowledge-doc backed):** Protect reporter information using role-based access, encryption, retention rules, and restricted case visibility. Include an escalation path for active exploitation, sensitive-data exposure, extortion, duplicate reports, and reports affecting third parties or suppliers.

**Advisory (not knowledge-doc backed):** Test the process periodically using a simulated external submission, including out-of-hours receipt, escalation, engineering assignment, reporter communication, and closure.

## Evidence for audit

Retain the following evidence for **VDP-M-001**:

- Approved, version-controlled vulnerability disclosure policy.
- Public `security.txt` response and automated availability-monitoring history.
- Approved safe-harbor terms and Legal approval record.
- Documented triage, acknowledgement, remediation, escalation, and coordinated-disclosure SLAs.
- Case-management records showing timestamps, severity, owner, communications, remediation, verification, and closure.
- SLA dashboards or reports covering acknowledgement and remediation performance.
- Monitoring alerts and evidence that unreachable or expired disclosure endpoints are corrected.
- Periodic process-test results and resulting corrective actions.
- Management approval for exceptions or overdue remediation.

## Assumptions and limits

No knowledge document is currently mapped to **VDP-M-001**. No knowledge document was found for VDP-specific operating procedures; tangential infrastructure and CI/CD documents were set aside because they do not implement this mandard. Recommendations explicitly marked advisory are not knowledge-document backed, and applicable legal requirements for safe harbor, privacy, evidence handling, export controls, and law-enforcement engagement were not assessed.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**VDP-M-001**](https://verify.example-org.internal/?id=VDP-M-001) | Medium | Vulnerability Disclosure | CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (APO12.01, DSS02.01, DSS05.07); DORA (Art. 45); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, GV.OC-01); NIST_SP_800_53 (AU-6, IR-4, IR-6); +3 more |

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