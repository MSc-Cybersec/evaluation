# G33-TM

## Question
How should threat-model outputs be enforced as release requirements?

## Sage response

## Bottom line

Threat-model outputs should become traceable, testable release criteria rather than remain design documentation. The SAGF catalogue does not currently contain a dedicated threat-model release-gate Mandard; however, **Critical/High SAST and SCA findings must block builds**, and any override of a mandated control must use an approved, unexpired deviation under **GOV-G-006**. Approve a policy requiring each applicable threat to be mitigated, verified, or formally accepted before production release, and consider drafting a dedicated Mandard to close the catalogue gap.

## Risk and impact

- **Critical:** Releasing code with Critical or High SAST findings violates **SAST-M-001** and may expose exploitable code-level flaws.
- **Critical:** Releasing dependencies with Critical or High CVEs violates **SCA-M-001** and may expose known supply-chain vulnerabilities.
- **High:** Bypassing a mandated control without a formally governed deviation violates **GOV-G-006**, leaving residual risk unowned, invisible, or indefinitely accepted.
- **Advisory (not catalogue-backed):** Threat-model findings that are not translated into release controls can result in insecure design, broken trust boundaries, missing abuse-case tests, and controls that exist only on paper.

## Governing mandards

| Mandard | Title | Risk level | Release implication |
|---|---|---:|---|
| **SAST-M-001** | No Critical SAST Findings | Critical | Per **SAST-M-001**: the build must fail when the SAST quality gate detects a new Critical or High vulnerability. |
| **SCA-M-001** | No Critical CVEs | Critical | Per **SCA-M-001**: the build must fail when SCA detects a Critical or High CVE in a dependency. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: any departure from a mandated security control must be recorded and independently approved before release, with justification, residual-risk owner, compensating controls, and expiry date. |

No dedicated Mandard governing threat-model completion or converting every threat-model output into a release gate was found. A new Mandard should be considered if this is intended to be an organisation-wide mandatory control.

**Implementation guidance:** **VeriFy-CE-001**, *Consumer / Endpoint Layer Guardrails*, requires applicable client designs to address identified security-risk areas and retain security-assessment results, deviations, and release-pipeline evidence.  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082  
Mapped Mandards: **AC-M-001**, **AUTH-M-001**, **GOV-G-006**, **LOG-M-001**, **MOB-M-001** through **MOB-M-011**, **SAST-M-001**, **SCA-M-001**.

## Framework mapping

The directly relevant mappings returned for **GOV-G-006** are:

| Framework | Controls |
|---|---|
| NIST SP 800-53 Rev. 5 | CA-5, PM-4, RA-3, PL-2 |
| ISO/IEC 27001:2022 Annex A | A.5.1, A.5.35 |
| SOC 2 Trust Services Criteria | CC3, CC5 |
| OWASP SAMM 2.0 | Governance: Policy & Compliance |
| COBIT 2019 | APO12.01, MEA02 |
| NIST CSF 2.0 | GV.RM, GV.OV, ID.RA |

## Required actions

1. **Enforce existing Critical release gates.**
   - **Engineering and DevSecOps:** Configure CI/CD to fail on new Critical or High SAST findings, as required by **SAST-M-001**.
   - **Engineering and DevSecOps:** Configure SCA to fail on Critical or High dependency CVEs, as required by **SCA-M-001**.
   - Do not allow manual pipeline overrides without a valid deviation reference.

2. **Govern every override.**
   - **Risk owner and independent security authority:** Per **GOV-G-006**, require an approved deviation containing:
     - Departed Mandard or control
     - Technical justification
     - Residual-risk rating and accountable owner
     - Compensating controls
     - Independent approval
     - Expiry date
   - Configure the release gate to reject missing, expired, ownerless, or unapproved deviations.

3. **Convert threat-model outputs into release records.**
   
   **Advisory (not catalogue-backed):** Store threat-model outputs in a machine-readable register linked to the application, release, architecture version, and work items. Each threat should contain:

   - Stable threat ID
   - Affected asset and trust boundary
   - Scenario and impact
   - Inherent and residual risk
   - Treatment decision: mitigate, avoid, transfer, or accept
   - Linked security requirement or Mandard
   - Implementation work item
   - Verification method and result
   - Accountable owner
   - Approved deviation where a mandated control is not satisfied

4. **Implement deterministic release decisions.**
   
   **Advisory (not catalogue-backed):** Block release when any of the following is true:

   - The threat model is missing, stale, or does not cover the release’s material architecture changes.
   - An applicable threat has no treatment decision or owner.
   - A mitigation lacks implementation and verification evidence.
   - A Critical or High finding violates **SAST-M-001** or **SCA-M-001**.
   - A mandated control is unmet without an approved, unexpired deviation satisfying **GOV-G-006**.
   - The release artefact differs from the artefact against which security verification was performed.

5. **Require change-triggered review.**
   
   **Advisory (not catalogue-backed):** Re-open the threat model when a release introduces a new trust boundary, identity flow, external integration, sensitive-data flow, privilege model, execution environment, or material dependency. Low-impact releases may reuse the existing model only when the change assessment records why it remains valid.

6. **Issue a release attestation.**
   
   **Advisory (not knowledge-doc backed):** Make the final pipeline job generate a signed or immutable attestation containing the release identifier, threat-model version, unresolved findings, test results, deviations, approvals, source commit, and deployed artefact digest.

## Evidence for audit

Retain the following against each release:

- Versioned threat model and architecture/data-flow diagrams
- Threat-to-requirement-to-test traceability record
- SAST quality-gate result proving compliance with **SAST-M-001**
- SCA report proving compliance with **SCA-M-001**
- Test results for each implemented mitigation
- CI/CD policy and gate execution logs
- Approved deviation records satisfying **GOV-G-006**
- Evidence that deviations were valid and unexpired at release time
- Independent approval history
- Release attestation linking the reviewed commit to the deployed artefact
- Applicable security-assessment, deviation, and pipeline records described by **VeriFy-CE-001**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082

## Assumptions and limits

- No dedicated threat-model release-gate Mandard was found in the searches performed.
- The severity policy for threat-model findings themselves is not defined by a retrieved Mandard; recommendations for handling those findings are therefore labelled advisory.
- The applicability of **VeriFy-CE-001** depends on whether the release includes a consumer, endpoint, thick-client, browser, or mobile component.
- A dedicated Mandard should be drafted if threat-model currency, traceability, severity thresholds, and release blocking are to be mandatory across all systems.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**AUTH-M-001**](https://verify.example-org.internal/?id=AUTH-M-001) | Critical | Authentication | CIS_CONTROLS (CIS 17, CIS 5, CIS 6); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-287, CWE-798); GDPR (Article 7); ISO_27001 (A.5.16, A.5.17, A.5.24); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**MOB-M-001**](https://verify.example-org.internal/?id=MOB-M-001) | Low | Mobile Security | NIST_SP_800_53 (AC-19, SC-18, SC-8); OWASP_CHEATSHEETS (DOM based XSS Prevention); OWASP_MOBILE (M10:2024, M1:2024, M3:2024); TOGAF (Application Security) |
| [**MOB-M-011**](https://verify.example-org.internal/?id=MOB-M-011) | Medium | Mobile Security | NIST_SP_800_53 (AC-19, SC-18, SC-8); OWASP_CHEATSHEETS (DOM based XSS Prevention); OWASP_MOBILE (M10:2024, M1:2024, M3:2024); TOGAF (Application Security) |
| [**SAST-M-001**](https://verify.example-org.internal/?id=SAST-M-001) | Critical | Static Analysis | AIUC1 (B010); CIS_CONTROLS (CIS 16, CIS 6, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CSA_CCM (AIS); CWE (CWE-20, CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); +13 more |
| [**SCA-M-001**](https://verify.example-org.internal/?id=SCA-M-001) | Critical | Supply Chain Analysis | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CSA_CCM (TVM); ENISA_SMLA (SMLA-08); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); +16 more |

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