# G64-SAST

## Question
What evidence proves SAST gates actively block high-risk code?

## Sage response

## Bottom line

Per **SAST-M-001**, the build must fail when SAST detects a new **Critical or High** severity vulnerability. The strongest proof is a traceable negative test showing the same commit produced a qualifying finding, failed the required pipeline check, and was prevented from merging or releasing; scanner configuration or a successful scan alone does not prove enforcement.

## Risk and impact

**Critical risk.** Without an enforced gate, vulnerabilities such as SQL injection and remote-code execution can progress into production despite being detected. The exposure includes application compromise, data loss, service disruption, and an inability to demonstrate that security testing operates as a preventive control.

## Governing mandards

| Mandard | Title | Risk | Relevance |
|---|---|---:|---|
| **SAST-M-001** | No Critical SAST Findings | Critical | Directly requires the build to fail for new Critical or High SAST findings. |
| **SAST-M-002** | Secure File Upload Validation | Critical | SAST can enforce detection of insecure upload validation. |
| **SAST-M-003** | Disable XXE Processing | Critical | Unsafe XML parser patterns must fail the quality gate. |
| **SAST-M-004** | Prevent Insecure Deserialization | Critical | Unsafe deserialization must be detected and blocked. |
| **SAST-M-005** | Prevent Mass Assignment | Critical | Direct model-binding patterns can be enforced through SAST rules. |
| **SAST-M-006** | Native Memory Safety and Unsafe Code Assurance | Critical | Specified native-code findings must block release unless a time-bound Tier 3 exception is approved. |

Per **SAST-M-001**: “The build MUST fail if the SAST quality gate detects a new Critical or High severity vulnerability.”

## Framework mapping

The catalogue returned these mappings for **SAST-M-001**:

| Framework | Control | Requirement |
|---|---|---|
| NIST SP 800-53 Rev. 5 | AC-2 | Account Management |
| NIST SP 800-53 Rev. 5 | AC-3 | Access Enforcement |
| NIST SP 800-53 Rev. 5 | AC-4 | Information Flow Enforcement |
| NIST SP 800-53 Rev. 5 | AC-6 | Least Privilege |
| NIST SP 800-53 Rev. 5 | SA-11 | Developer Testing and Evaluation |
| NIST SP 800-53 Rev. 5 | SI-10 | Information Input Validation |
| NIST SP 800-53 Rev. 5 | SI-15 | Information Output Filtering |

## Required actions

1. **Platform Engineering:** Configure SAST as a mandatory pipeline check on protected branches and release workflows.
2. **Application Security:** Set the gate to fail on every new Critical or High finding, consistent with **SAST-M-001**.
3. **Repository Administrators:** Prevent merging when the SAST status check fails; restrict bypass privileges.
4. **Application Security and Engineering:** Run a controlled negative test using a test branch containing a known-detectable High or Critical pattern.
5. Confirm that:
   - the scanner records the finding and severity;
   - the pipeline exits unsuccessfully;
   - the pull request reports the failed required check;
   - merge or release is unavailable;
   - remediation removes the finding and the rerun passes.
6. Retain any override as a formally approved, time-bound exception. For native memory-safety findings, **SAST-M-006** specifically requires Tier 3 governance approval.

**Implementation guidance found:** **VeriFy-CE-001**, mapped to **SAST-M-001**, identifies SAST as applicable and directs projects to release-management and CI/CD pipeline controls.  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082

No knowledge document was found that defines a complete SAST gate-evidence procedure.

## Evidence for audit

**Advisory (not knowledge-doc backed):** Retain one linked evidence bundle containing:

| Evidence artefact | What it proves |
|---|---|
| Version-controlled pipeline definition | SAST executes in the build or release path. |
| Exported quality-gate policy | New Critical and High findings are configured as failures. |
| Protected-branch or environment rule | The SAST check is mandatory and cannot ordinarily be bypassed. |
| Negative-test commit hash | A known test condition was introduced into a specific revision. |
| Scanner report or SARIF output | The same revision generated a Critical or High finding. |
| Failed pipeline record and non-zero exit | Detection caused technical failure rather than an informational warning. |
| Blocked pull-request or release record | The failure actually prevented progression. |
| Remediation commit and passing rerun | Progression became possible only after correction. |
| Administrative audit log | Gate settings were active and no unauthorized bypass occurred. |
| Approved exception record, if applicable | Any override was authorized, scoped, time-bound, and traceable. |

The minimum persuasive chain is:

`commit → qualifying SAST finding → failed required check → blocked merge/release`

## Assumptions and limits

No repository settings, scanner policy, pipeline execution, pull request, release record, or exception record was provided for verification. Therefore, this answer defines the evidence needed but does not attest that any specific SAST gate is operating effectively.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**SAST-M-001**](https://verify.example-org.internal/?id=SAST-M-001) | Critical | Static Analysis | AIUC1 (B010); CIS_CONTROLS (CIS 16, CIS 6, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CSA_CCM (AIS); CWE (CWE-20, CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); +13 more |
| [**SAST-M-002**](https://verify.example-org.internal/?id=SAST-M-002) | Critical | Static Analysis | CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-434); ISO_27001 (A.8.26, A.8.28, A.8.7); MITRE_ATT&CK (M1013, M1016); NIST_CSF (PR.DS-01, PR.PS-01, PR.PS-06); NIST_SP_800_53 (SA-11, SC-18, SC-8); +7 more |
| [**SAST-M-003**](https://verify.example-org.internal/?id=SAST-M-003) | Critical | Static Analysis | CIS_CONTROLS (CIS 12, CIS 16); ISO_27001 (A.8.20, A.8.22, A.8.26); MITRE_ATT&CK (M1013, M1016); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, SA-11, SC-5); NIST_SSDF (PO.1.1, PW.7.1); +7 more |
| [**SAST-M-004**](https://verify.example-org.internal/?id=SAST-M-004) | Critical | Static Analysis | CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-502, CWE-77); ISO_27001 (A.8.26, A.8.28); MITRE_ATT&CK (M1013, M1016); NIST_CSF (PR.DS-01, PR.PS-01, PR.PS-06); NIST_SP_800_53 (SA-11, SI-10, SI-15); +7 more |
| [**SAST-M-005**](https://verify.example-org.internal/?id=SAST-M-005) | Critical | Static Analysis | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04); ISO_27001 (A.5.19, A.5.21, A.8.26); MITRE_ATT&CK (M1013, M1016); NIST_CSF (GV.SC-01, ID.RA-09, PR.DS-01); NIST_SP_800_53 (AC-4, SA-11, SA-12); +9 more |
| [**SAST-M-006**](https://verify.example-org.internal/?id=SAST-M-006) | Critical | Static Analysis | CWE (CWE-119, CWE-120, CWE-121); MITRE_ATT&CK (M1013, M1016, M1050) |

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