# G08-BIZ

## Question
How should business-risk owners accept residual cyber risk from delayed fixes?

## Sage response

## Bottom line

Business-risk owners should accept delayed remediation only through a **formal, time-bounded security deviation**, not through email, backlog prioritisation, or an open-ended waiver. Per **GOV-G-006**, acceptance must document the residual risk, accountable owner, compensating controls, technical justification, independent approval, and expiry date before release; indefinite renewal is prohibited.

## Risk and impact

The governance risk is **High**. An undocumented or expired exception leaves the organisation knowingly exposed without clear accountability, effective interim protection, or a binding remediation deadline.

The underlying cyber-risk severity remains finding-specific. Acceptance should consider the affected assets, exploitability, data sensitivity, threat activity, customer and regulatory impact, and effectiveness of compensating controls.

**Advisory (not catalogue-backed):** Residual risk should be accepted only where it is within the owner’s formally delegated risk appetite. Risks exceeding that authority should be escalated to the appropriate executive risk committee rather than accepted locally.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: record every departure before release, including technical justification, residual risk and accepting owner, compensating controls, expiry, and approval independent of delivery. Review at expiry and do not renew indefinitely without re-justification. |
| **ASSURE-M-002** | Software Assurance Roles, Responsibilities and Authorities | High | Per **ASSURE-M-002**: business ownership, security-risk ownership, decision rights, delegated authorities, segregation of duties, and escalation paths must be named, accepted, and documented. |
| **TM-M-003** | Threat Register & Documentation | High | Per **TM-M-003**: identified threats must be recorded centrally with their description, risk level, and status. |

The applicable implementation standard is **VeriFy-BR-002**, mapped to **ASSURE-M-002**, **DATA-M-002**, **GOV-G-006**, **SUPPLY-M-001**, and **TM-M-003**. Its “Purpose, Scope and Deviations” section requires non-compliance to be formally recorded as a deviation, supported by technical justification, and included in the SAF pack. Source: [VeriFy-BR-002 — Business Risk](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981693).

## Framework mapping

Mappings below are limited to mappings returned by the SAGF catalogue.

| Mandard | Framework controls |
|---|---|
| **GOV-G-006** | NIST SP 800-53 Rev. 5: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; NIST CSF 2.0: GV.RM, GV.OV, ID.RA; COBIT 2019: APO12.01, MEA02; OWASP SAMM 2.0: Governance — Policy & Compliance |
| **ASSURE-M-002** | ISO/IEC 27001:2022: A.5.2, A.5.4; NIST CSF 2.0: GV.RR; ISO/IEC 42001: A.3; NIST SP 800-82r3: 5.2.1 |
| **TM-M-003** | NIST SP 800-53 Rev. 5: RA-3, AU-2, AU-6, AU-12, SI-4, PL-8 |

## Required actions

1. **Create the deviation before release — Risk owner and delivery owner.**  
   Per **GOV-G-006**, record:
   - Affected system, finding, and mandated control
   - Scope and duration of exposure
   - Technical reason the fix is delayed
   - Residual-risk rating and supporting assessment
   - Named accepting risk owner
   - Compensating controls
   - Committed remediation date and deviation expiry date
   - Independent approver and approval date

2. **Confirm the owner has decision authority — GRC or CISO governance.**  
   Per **ASSURE-M-002**, verify that the accepting person is the documented security-risk owner, has appropriate delegated authority, and has explicitly accepted responsibility. The delivery team cannot independently approve its own deviation.

3. **Require an explicit acceptance statement.**  
   The owner should confirm that they understand:
   - The credible threat scenario and affected business service
   - Potential operational, financial, customer, legal, and regulatory impacts
   - Which control remains unsatisfied
   - What risk remains after compensating controls
   - The expiry date and funded remediation commitment

4. **Apply and monitor compensating controls — Technical and security owners.**  
   Per **GOV-G-006**, document the interim controls. Examples may include restricting exposure, stronger authentication, additional monitoring, segmentation, disabling vulnerable functionality, or reducing privileges.  
   **Advisory (not knowledge-doc backed):** Test control effectiveness rather than accepting a planned or unverified control as risk reduction.

5. **Record the threat and remediation status — Security team.**  
   Per **TM-M-003**, link the deviation to the central threat or finding register and maintain its description, risk level, status, remediation work item, and affected assets.

6. **Attach the decision to the assurance record.**  
   **VeriFy-BR-002**, mapped to **GOV-G-006**, requires the deviation and technical justification to be included in the SAF pack. Source: [VeriFy-BR-002](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981693).

7. **Enforce the exception at release gates — DevSecOps or platform engineering.**  
   Per **GOV-G-006**, a control override should proceed only when the referenced deviation is approved, applicable to the system and release, and unexpired.

8. **Review on or before expiry — Risk owner and independent approver.**  
   Per **GOV-G-006**, the outcome must be one of:
   - Fix and close the deviation
   - Reassess and re-justify it with a new bounded expiry
   - Stop or constrain the affected activity

   Repeated renewal without new justification must be escalated rather than treated as permanent acceptance.

## Evidence for audit

Retain the following:

- Approved deviation-register entry with immutable approval history
- Named ownership and delegated-authority record
- Residual-risk assessment and technical justification
- Evidence that compensating controls are operating
- Link to the vulnerability, threat, incident, or remediation work item
- SAF pack containing the deviation
- Release-gate result showing an approved, unexpired exception
- Expiry-review notifications and decision record
- Fix verification or rescan result used to close the exception
- Reports identifying expired, ownerless, or repeatedly renewed deviations

## Assumptions and limits

The organisation’s risk-appetite thresholds, approval authority matrix, remediation service levels, and severity of the underlying vulnerabilities were not provided or verified. **VeriFy-BR-002** specifies deviation recording and SAF-pack inclusion but does not provide a complete residual-risk scoring methodology or escalation timetable.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ASSURE-M-002**](https://verify.example-org.internal/?id=ASSURE-M-002) | High | Independent Assurance | ISO_27001 (A.5.2, A.5.4); ISO_42001 (A.3); NIST_800_82 (5.2.1); NIST_CSF (GV.RR) |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**SUPPLY-M-001**](https://verify.example-org.internal/?id=SUPPLY-M-001) | High | Supply Chain Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (STA); ENISA_SMLA (SMLA-20, SMLA-22); +18 more |
| [**TM-M-003**](https://verify.example-org.internal/?id=TM-M-003) | High | Threat Modeling | CIS_CONTROLS (CIS 8); COBIT_2019 (APO12.01, DSS05.07, EDM03.01); CSA_CCM (GRC); ENISA_SMLA (SMLA-10); GDPR (Article 35); HIPAA (164.312(b)); +12 more |

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