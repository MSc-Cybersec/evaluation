# G06-CSPM

## Question
What governance checks should CSPM findings trigger before release?

## Sage response

## Bottom line

Before release, CSPM findings must trigger a control-compliance decision: remediate and verify the finding, or record an approved, unexpired deviation before releasing the affected change. Per **CSPM-M-001**, critical cloud-configuration findings must be remediated within seven days; however, that deadline is not automatic permission to release a knowingly non-compliant change. Configure the release process to reject unresolved control departures unless the evidence pack contains an independently approved exception meeting **GOV-G-006**.

## Risk and impact

| Trigger | Governance check before release | Release outcome |
|---|---|---|
| Critical CIS or equivalent configuration finding | Confirm remediation and clean re-scan; otherwise validate a formal deviation | Block without remediation evidence or an approved deviation |
| Security-relevant drift from declared IaC | Confirm detection occurred within one hour and the drift was remediated or escalated for manual review | Block where drift represents an unresolved mandated-control departure |
| IAM or external-access finding | Confirm the quarterly IAM review is current, assess least privilege, and identify unused permissions | Remove unused permissions within 30 days; unresolved control departures require a deviation |
| Missing owner, cost centre, or environment tag | Confirm ownership and environment classification; tag or delete the resource within seven days | For a new release-created resource, treat missing mandatory tags as non-compliance |
| Any accepted CSPM finding | Check justification, residual-risk owner, compensating controls, independent approval, and expiry | Block if the deviation is missing, expired, ownerless, or not independently approved |
| False positive or not applicable | Require documented validation tied to the specific resource and CSPM rule | Release only after the disposition is recorded and approved under the applicable workflow |

The catalogue classifies the core configuration, IAM-review, drift, and exception-management controls as **High** risk. Untagged-resource detection is **Medium** risk because missing ownership and classification create security blind spots, unmanaged assets, and cost or compliance exposure.

**Advisory (not catalogue-backed):** Use finding severity together with internet exposure, data sensitivity, privilege, exploitability, and blast radius when deciding whether non-critical findings should block release. The catalogue does not establish a universal “all High findings block release” threshold.

## Governing mandards

The complete CSPM domain contains the following mandards:

| Mandard | Title | Risk | Release-relevant requirement |
|---|---|---:|---|
| **CSPM-M-001** | Cloud Configuration Compliance — CIS Benchmarks | High | Continuously scan cloud infrastructure against CIS Benchmarks or equivalent. Critical findings must be remediated within seven days. |
| **CSPM-M-002** | Untagged Resource Detection | Medium | Detect untagged resources daily. Resources must carry owner, cost centre, and environment tags and must be tagged or deleted within seven days. |
| **CSPM-M-003** | Cloud Identity & Access Review — Quarterly | High | Review cloud IAM permissions quarterly and remove identified unused permissions within 30 days. |
| **CSPM-M-004** | Drift Detection & Auto-Remediation | High | Compare live configuration with declared IaC state. Detect drift within one hour and auto-remediate or escalate it for manual review. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Record any departure before release, including justification, residual-risk owner, compensating controls, expiry, and approval independent of the delivery team. |

Per **CSPM-M-001**: critical benchmark findings require remediation within seven days.

Per **CSPM-M-004**: configuration drift requires detection within one hour and remediation or escalation.

Per **GOV-G-006**: an affected change cannot rely on an informal waiver; the departure must be formally recorded and independently approved before release.

## Framework mapping

Only catalogue-returned mappings are shown below.

| Mandard | Returned framework mappings |
|---|---|
| **CSPM-M-001** | NIST SP 800-53: CM-2, CM-6, SI-4, AU-6; PCI DSS: Req 2; ISO/IEC 27001:2022: A.8.9, A.8.16, A.8.27; SOC 2: CC7.2, CC7.3; OWASP SAMM: Operations — Environment Management |
| **CSPM-M-002** | NIST SP 800-53: CM-2, CM-6, SI-4, AU-6; ISO/IEC 27001:2022: A.8.9, A.8.16; SOC 2: CC7.2; CIS Controls v8: CIS 1, CIS 3, CIS 4, CIS 8 |
| **CSPM-M-003** | NIST SP 800-53: AC-2, AC-3, AC-6, CM-6; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3; HIPAA: 164.312(a)(1); OWASP ASVS 5.0: V8 |
| **CSPM-M-004** | NIST SP 800-53: CM-3, CM-6, SI-4, SA-15; PCI DSS: Req 11; ISO/IEC 27001:2022: A.8.25, A.8.31, A.8.32; SOC 2: CC4, A1.2 |
| **GOV-G-006** | NIST SP 800-53: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; COBIT 2019: APO12.01, MEA02; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |

## Required actions

1. **Correlate findings to the release scope.**  
   The cloud platform or security engineering owner should associate each CSPM finding with the affected account, subscription, resource, IaC component, application, data classification, and release identifier. Findings unrelated to the release may be excluded only with a documented rationale.

2. **Apply the configuration-compliance gate.**  
   Per **CSPM-M-001**, run the applicable CIS or equivalent posture assessment and create a remediation workflow. Critical findings affecting the release must have remediation evidence and a clean re-scan within seven days, or follow **GOV-G-006** before release.

3. **Reconcile live state with IaC.**  
   Per **CSPM-M-004**, compare the deployed configuration with the version-controlled declaration. Security-relevant or unexplained drift must be auto-remediated where safe or escalated for manual review; detection must occur within one hour.

4. **Validate cloud identity exposure.**  
   Per **CSPM-M-003**, verify that the quarterly review remains current for affected roles, policies, service accounts, and federated identities. Record excessive or unused privileges and remove unused permissions within 30 days.

5. **Check ownership and classification tags.**  
   Per **CSPM-M-002**, confirm that each release-created resource has owner, cost centre, and environment tags. Untagged resources must be detected daily and tagged or deleted within seven days.

6. **Govern unresolved findings as deviations.**  
   Per **GOV-G-006**, require the following before allowing an override:
   - The specific mandard and affected resource
   - Technical justification
   - Residual risk and named accepting owner
   - Compensating controls
   - Independent approval outside the delivery team
   - Defined expiry date
   - Link to the release assurance pack

7. **Prevent invalid overrides.**  
   Per **GOV-G-006**, fail the release gate when the deviation is missing, expired, ownerless, lacks independent approval, or cannot be linked to the affected system. Repeated renewals require re-justification and must not become indefinite acceptance.

8. **Retain deployment and pipeline controls.**  
   Implementation guidance in **VeriFy-IS-RMP-001**, mapped to **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, and **SIGN-M-001**, calls for IaC scanning during deployment, remediation of build-stage security non-compliance, environment segregation, and release evidence.  
   Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688

9. **Include infrastructure and network posture in the assurance review.**
   - **VeriFy-INF-002**, mapped to **CSPM-M-001** and **GOV-G-006** among other controls, covers CIS hardening, asset management, vulnerability management, deployment, authentication, service accounts, secure access, and infrastructure deviations. Non-compliance must be recorded in the SAF pack with technical justification.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658243766
   - **VeriFy-NET-001**, mapped to **CSPM-M-001** and **GOV-G-006** among other controls, requires consideration of cloud-edge protections such as firewall access control, segmentation, private endpoints, inspection, and security-event management; deviations belong in the SAF pack.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652023403

## Evidence for audit

The release assurance pack should contain:

- Timestamped CSPM report identifying the policy set, scope, affected resources, severity, and scan time
- Finding-to-release correlation record
- Remediation ticket and change record
- Post-remediation clean re-scan
- IaC plan or drift report demonstrating declared-versus-live state
- Evidence that drift was detected within the **CSPM-M-004** one-hour requirement
- Current quarterly IAM review and permission-removal records
- Daily tagging report and evidence of tagging or deletion
- False-positive or not-applicable disposition with reviewer identity
- Approved, unexpired deviation record where remediation was not completed
- Residual-risk acceptance, compensating-control evidence, and independent approval
- Pipeline gate log showing pass, fail, or authorised override
- SAF or equivalent assurance-pack approval tied to the release identifier

## Assumptions and limits

No actual CSPM findings, cloud environment, data classification, deployment architecture, or configured pipeline thresholds were provided, so release readiness was not assessed. The universal blocking recommendation for unresolved mandated-control departures is grounded in **GOV-G-006**; severity thresholds beyond the explicit critical-finding requirement in **CSPM-M-001** remain organisation-defined.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**CSPM-M-001**](https://verify.example-org.internal/?id=CSPM-M-001) | High | Cloud Security Posture | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, BAI10, DSS02.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**CSPM-M-002**](https://verify.example-org.internal/?id=CSPM-M-002) | Medium | Cloud Security Posture | CIS_CONTROLS (CIS 1, CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.16, A.8.27, A.8.9); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +4 more |
| [**CSPM-M-003**](https://verify.example-org.internal/?id=CSPM-M-003) | High | Cloud Security Posture | CIS_CONTROLS (CIS 3, CIS 4, CIS 6); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.16); +9 more |
| [**CSPM-M-004**](https://verify.example-org.internal/?id=CSPM-M-004) | High | Cloud Security Posture | CIS_CONTROLS (CIS 11, CIS 3, CIS 4); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.13, A.8.14, A.8.16); NIST_800_82 (6.3.2); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); +7 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |
| [**PIPE-M-012**](https://verify.example-org.internal/?id=PIPE-M-012) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); NIST_CSF (PR.PS-06); +8 more |
| [**SECR-M-002**](https://verify.example-org.internal/?id=SECR-M-002) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**SIGN-M-001**](https://verify.example-org.internal/?id=SIGN-M-001) | Critical | Code Signing | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.19, A.5.21, A.8.19); MITRE_ATT&CK (M1045); NIST_800_190 (4.2); +9 more |

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