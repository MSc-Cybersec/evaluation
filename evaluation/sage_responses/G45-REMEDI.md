# G45-REMEDI

## Question
How do we evidence that remediation actions are effective, not just recorded?

## Sage response

## Bottom line

A remediation record proves activity, not effectiveness. Close a remediation only when objective evidence shows the original condition is removed, the control operates as intended, and the result has been independently validated; however, the SAGF search returned no Mandard specifically defining this effectiveness test, so the workflow below is **Advisory (not catalogue-backed)**.

## Risk and impact

No catalogue risk level was returned for remediation-effectiveness validation.

**Advisory (not catalogue-backed):** Without validation, ineffective fixes can be reported as closed while vulnerabilities, control failures, or compliance exposure remain. This creates false assurance for management and weakens audit defensibility.

## Governing mandards

No suitable Mandard was found that specifically requires or defines evidence of remediation effectiveness. A Mandard should be drafted to establish closure criteria, retesting, independence requirements, recurrence monitoring, and exception handling.

The governance search returned knowledge documents concerning architecture guardrails and formal deviation recording, but none directly established how remediation effectiveness must be demonstrated. These were therefore set aside, including:

- `VeriFy-APP-002`, *Application Layer Governance* — mapped to **ASSURE-M-001**, **CLOUD-M-007**, **CRYPT-M-001**, **DATA-M-002**, **GOV-G-006**, **OAUTH-M-001**, **SUPPLY-M-001**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782
- `VeriFy-AUD-002`, *Audit Trails, Event & Log Management* — mapped to **DATA-M-002**, **DB-M-005**, **GOV-G-006**, **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, **MON-M-001**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664
- `VeriFy-INF-002`, *System / Infrastructure Layer* — mapped to **CSPM-M-001**, **DLP-M-001**, **GOV-G-006**, **IAM-M-002**, **IAM-M-005**, **MON-M-001**, **PROV-M-002**, **PROV-M-003**, **RUNTIME-M-001**, **RUNTIME-M-002**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/658243766

These documents state that non-compliance should be formally recorded as a deviation with technical justification, but that is not evidence that a remediation worked.

## Framework mapping

No framework mappings were returned for a remediation-effectiveness Mandard. No mapping is asserted.

## Required actions

**Advisory (not catalogue-backed):**

1. **Define measurable closure criteria before remediation begins.**  
   Record the failed control, affected assets, expected secure state, acceptance threshold, test method, and required monitoring period.

2. **Preserve baseline evidence.**  
   Retain the original finding, vulnerable configuration or test result, severity, scope, timestamps, and asset identifiers. This enables before-and-after comparison.

3. **Capture implementation evidence.**  
   Link the remediation ticket to the approved change, code commit, pull request, deployment record, configuration diff, package version, or infrastructure-as-code update.

4. **Retest the original condition.**  
   Repeat the same test that generated the finding where possible. A ticket status, developer statement, or screenshot of changed code is not sufficient by itself.

5. **Test for control outcomes, not only changed settings.**  
   For example:
   - Vulnerability: authenticated rescan plus targeted exploit-negative test.
   - Access issue: verify revoked access and test that an unauthorised identity is denied.
   - Logging issue: generate a representative event and verify ingestion, alerting, timestamp, attribution, and retention.
   - Code defect: regression test plus pipeline security scan.
   - Cloud misconfiguration: configuration assessment plus runtime verification.

6. **Use independent validation proportionate to risk.**  
   The person or function validating a material issue should not be solely responsible for implementing the fix. Security Assurance, Internal Audit, a control owner, or an independent engineer should validate higher-risk findings.

7. **Check scope and recurrence.**  
   Determine whether the same defect exists in related assets, environments, branches, accounts, or services. Monitor for recurrence over a defined period where a one-time test cannot prove sustained operation.

8. **Separate four closure outcomes.**
   - **Validated:** the fix passed the defined effectiveness test.
   - **Partially remediated:** exposure remains or scope is incomplete.
   - **Risk accepted:** exposure remains under an authorised, time-bound exception.
   - **Not effective:** retesting failed and the issue remains open.

9. **Require accountable approval.**  
   The control owner should approve closure based on attached validation evidence. Residual risk acceptance should be approved by the designated risk owner, not treated as remediation.

## Evidence for audit

A defensible remediation evidence pack should contain:

| Evidence | What it proves |
|---|---|
| Original finding and baseline result | The initial condition and affected scope |
| Defined closure criteria | What “effective” means for the issue |
| Change record and approval | The authorised remediation was implemented |
| Code or configuration diff | The technical state changed |
| Deployment record | The change reached the affected environment |
| Dated retest or rescan | The original condition no longer reproduces |
| Regression or negative test | The control blocks the unwanted outcome |
| Scope assessment | Related assets were checked |
| Monitoring results | The fix continues to operate and has not recurred |
| Independent validator sign-off | Effectiveness was not merely self-attested |
| Residual-risk decision, if applicable | Remaining exposure was consciously authorised |
| Immutable ticket history | Traceability from finding through closure |

A practical closure statement is:

> “The original finding was reproduced on [date], remediated through change [ID], and retested in [environment] on [date] using [method]. The expected secure outcome was observed across [scope]. No recurrence was detected during [period]. Validation was completed by [independent role], with evidence attached.”

## Assumptions and limits

- No SAGF Mandard specifically governing remediation-effectiveness evidence was found.
- No relevant knowledge document defining an effectiveness-validation procedure was found.
- The proposed workflow and evidence pack are **Advisory (not catalogue-backed)**.
- Framework control mappings and catalogue risk levels remain unverified and are therefore omitted.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ASSURE-M-001**](https://verify.example-org.internal/?id=ASSURE-M-001) | High | Independent Assurance | AIUC1 (B001, C010, C011); CIS_CONTROLS (CIS 18); ISO_27001 (A.5.35); ISO_27034 (ASMP.5); NIST_800_82 (5.2.1); NIST_CSF (GV.OV, GV.OV-01, GV.OV-03); +4 more |
| [**CLOUD-M-007**](https://verify.example-org.internal/?id=CLOUD-M-007) | High | Cloud Security | AIUC1 (E005, E011); CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32, Article 44); +11 more |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**CSPM-M-001**](https://verify.example-org.internal/?id=CSPM-M-001) | High | Cloud Security Posture | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, BAI10, DSS02.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CA-9, CM-2); +6 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**DLP-M-001**](https://verify.example-org.internal/?id=DLP-M-001) | High | Data Loss Prevention | AIUC1 (A004, A006); CCPA_CPRA (Data Minimization, Reasonable Security Procedures, Right to Limit Sensitive Personal Information); CIS_CONTROLS (CIS 12, CIS 3, CIS 6); COBIT_2019 (APO14, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285); GDPR (Article 25, Article 32, Article 5); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**PROV-M-002**](https://verify.example-org.internal/?id=PROV-M-002) | High | Provisioning | ISO_27034 (ASMP.4) |

Showing 15 of 19 cited mandards.

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