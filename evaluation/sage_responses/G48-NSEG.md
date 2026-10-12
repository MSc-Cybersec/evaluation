# G48-NSEG

## Question
What policy controls govern network segmentation exceptions during incidents?

## Sage response

## Bottom line

Network-segmentation controls remain in force during an incident. Any temporary departure must be governed as a formal, time-bounded security deviation under **GOV-G-006**, while the underlying segmentation requirements of **NSEG-M-002** remain the target state. The incident commander must obtain independent approval before releasing the affected change, document compensating controls and residual risk, and ensure the exception expires or is removed.

## Risk and impact

Both applicable Mandards are rated **High**.

- Weakening segmentation can allow a compromised internet-facing service to reach internal systems or databases.
- An undocumented incident exception can become a permanent firewall exposure with no accountable risk owner, expiry, or reassessment.
- Incident urgency does not create a catalogue-backed waiver from deviation governance.

## Governing mandards

| Mandard | Title | Risk | Application during an incident |
|---|---|---:|---|
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: every departure must be formally recorded before the affected change is released. The record must include the departed control, technical justification, residual risk and accepting owner, compensating controls, expiry date, and approval by an authority independent of the delivery team. Indefinite renewal is prohibited without re-justification. |
| **NSEG-M-002** | DMZ & Network Segmentation | High | Per **NSEG-M-002**: internet-facing applications must remain in a DMZ separated from internal networks by a firewall; DMZ-to-internal access must be limited to specific ports and protocols; databases must not be placed in the DMZ. |

The applicable implementation standard is **VeriFy-NET-001**, *2. Network / Connectivity Layer*, source:  
https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652023403

Its `mandard_refs` are: **CSPM-M-001**, **EDGE-M-002**, **EDGE-M-003**, **GATE-M-003**, **GOV-G-006**, **NSEG-M-002**, **WAF-M-001**, and **ZTA-M-002**. The standard states that non-compliance must be recorded as a deviation, included in the SAF pack, and supported by technical justification. It also identifies firewall DMZ access control and, for cloud deployments, VNET/security-group micro-segmentation and private endpoints as explicitly configured controls.

No incident-specific Mandard or knowledge procedure was found that relaxes these requirements or defines a separate emergency exception route.

## Framework mapping

Mappings below are limited to those returned for the two governing Mandards.

| Mandard | Framework mappings |
|---|---|
| **GOV-G-006** | NIST SP 800-53 Rev.5: `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022: `A.5.1`, `A.5.35`; SOC 2: `CC3`, `CC5`; OWASP SAMM 2.0: `Governance: Policy & Compliance`; COBIT 2019: `APO12.01`, `MEA02`; NIST CSF 2.0: `GV.RM`, `GV.OV`, `ID.RA` |
| **NSEG-M-002** | NIST SP 800-53 Rev.5: `CM-6`, `CM-2`, `SC-7`, `AC-4`, `SC-5`; PCI DSS v4.0: `Req 1`; ISO/IEC 27001:2022: `A.8.9`, `A.8.27`, `A.8.20`, `A.8.22`, `A.8.21`; OWASP Cheat Sheet Series: `Infrastructure as Code Security`; COBIT 2019: `BAI09.01`, `DSS05.02`; CIS Controls v8: `CIS 4`, `CIS 12`; NIST CSF 2.0: `PR.IR-01`, `PR.PS-01`; TOGAF: `Infrastructure Security`; MITRE ATT&CK: `M1030`, `M1035`; NIST 800-82: `5.2.3` |

## Required actions

1. **Preserve the minimum segmentation boundary.**  
   Per **NSEG-M-002**, do not move databases into the DMZ or create unrestricted DMZ-to-internal connectivity. Limit temporary rules to named sources, destinations, ports, and protocols.

2. **Create the deviation before activating the exception.**  
   Per **GOV-G-006**, record:
   - the affected system and **NSEG-M-002** requirement;
   - incident reference and technical justification;
   - exact temporary firewall, security-group, or routing change;
   - residual risk and named accepting owner;
   - compensating controls;
   - independent approver;
   - activation and expiry timestamps.

3. **Obtain independent approval.**  
   Per **GOV-G-006**, approval must come from an authority outside the delivery team. The network standard identifies Enterprise Architecture, InfoSec Design, and Build Squads as document stakeholders, but it does not define a dedicated emergency approver.

4. **Attach the exception to the assurance record.**  
   **VeriFy-NET-001** requires non-compliance to be included in the SAF pack with technical justification.

5. **Enforce automatic expiry and review.**  
   Per **GOV-G-006**, review the exception on or before expiry and either restore compliance, re-justify it with a new bounded expiry, or formally close it. Repeated or indefinite renewal is not acceptable without re-justification.

6. **Advisory (not knowledge-doc backed):** configure the temporary network rule with automatic expiry where the platform supports it, increase logging for the affected traffic path, define rollback criteria, and reconcile the final rule set against the approved network baseline after incident containment.

## Evidence for audit

Retain:

- the approved deviation-register entry;
- the incident and change records linked to the deviation;
- the SAF pack containing the technical justification;
- before-and-after firewall, route, NACL, VNET, or security-group configuration;
- evidence that access was restricted to approved ports, protocols, sources, and destinations;
- the independent approval record;
- expiry, rollback, or removal evidence;
- the expiry-review outcome;
- network topology or reachability test showing the database was not publicly reachable.

## Assumptions and limits

No incident-specific Mandard or emergency network-exception procedure was found. Automatic expiry, enhanced monitoring, and rollback criteria are therefore advisory measures rather than explicit knowledge-document requirements.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**CSPM-M-001**](https://verify.example-org.internal/?id=CSPM-M-001) | High | Cloud Security Posture | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, BAI10, DSS02.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**EDGE-M-002**](https://verify.example-org.internal/?id=EDGE-M-002) | High | Edge Security | CIS_CONTROLS (CIS 12, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ISO_27001 (A.8.16, A.8.20, A.8.22); NIST_CSF (DE.AE-02, DE.CM-01); NIST_SP_800_53 (AC-4, AU-6, CM-6); OWASP_ASVS (V13); +5 more |
| [**EDGE-M-003**](https://verify.example-org.internal/?id=EDGE-M-003) | Medium | Edge Security | CIS_CONTROLS (CIS 12, CIS 6, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01); +8 more |
| [**GATE-M-003**](https://verify.example-org.internal/?id=GATE-M-003) | Critical | Gateway Security | CIS_CONTROLS (CIS 8); COBIT_2019 (BAI03.03, BAI04, BAI06.01); CWE (CWE-400, CWE-770); ISA_62443 (SR 7); ISO_27001 (A.8.16, A.8.25, A.8.31); NIST_CSF (DE.AE-02, DE.CM-01, PR.PS-06); +8 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |
| [**WAF-M-001**](https://verify.example-org.internal/?id=WAF-M-001) | High | Web Application Firewall | CIS_CONTROLS (CIS 12, CIS 16); CWE (CWE-77, CWE-79, CWE-89); ISO_27001 (A.8.20, A.8.22, A.8.26); MITRE_ATT&CK (M1020, M1021, M1031); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, CM-6, SA-11); +6 more |
| [**ZTA-M-002**](https://verify.example-org.internal/?id=ZTA-M-002) | High | Zero Trust Architecture | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); COBIT_2019 (APO12.01, DSS05.04, EDM03.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); MITRE_ATT&CK (M1035); +9 more |

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