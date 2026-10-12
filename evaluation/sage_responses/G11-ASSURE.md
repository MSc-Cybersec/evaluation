# G11-ASSURE

## Question
What independent assurance artefacts are needed for quarterly compliance attestation?

## Sage response

## Bottom line

For each quarterly attestation, retain a dated evidence pack demonstrating that assurance was performed independently, with the assessor’s independence, scope, method, limitations, results, and finding closure status recorded. Per **ASSURE-M-001**, testing frequency is determined by system risk tier and material change; the catalogue does not establish quarterly testing as a universal requirement, so a quarter-end attestation may reference still-current assurance unless the risk schedule or a material change requires retesting.

## Risk and impact

Both applicable mandards are rated **High**.

Without adequate evidence, management cannot demonstrate that security claims were independently challenged or that unresolved findings received accountable risk treatment. This creates exposure to undetected vulnerabilities, ineffective self-assessment, expired third-party assurance, unsupported risk acceptance, and audit qualification.

Pipeline scans and delivery-team testing are supporting evidence only; they do not replace the independent assurance required by **ASSURE-M-001**.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **ASSURE-M-001** | Independent Security Assurance and Third-Party Testing | High | Security claims must be independently validated at a depth and frequency proportionate to risk. Assessor independence, scope, method, limitations, results, and finding remediation must be recorded. Highest-risk systems require an assessor independent of both delivery and the internal security function, including after material change. |
| **ASSURE-M-002** | Software Assurance Roles, Responsibilities and Authorities | High | Named and accepted accountability must cover business ownership, technical ownership, security risk ownership, control implementation, independent assurance, and production operations. Decision rights, segregation of duties, escalation paths, and delegated authorities must be documented. |

## Framework mapping

Only mappings returned by the SAGF catalogue are shown.

| Mandard | Framework | Controls |
|---|---|---|
| **ASSURE-M-001** | NIST SP 800-53 Rev. 5 | CA, CA-2, CA-8 |
| **ASSURE-M-001** | ISO/IEC 27001:2022 | A.5.35 |
| **ASSURE-M-001** | SOC 2 Type II | CC4 |
| **ASSURE-M-001** | OWASP SAMM 2.0 | Verification: Security Testing |
| **ASSURE-M-001** | ISO/IEC 27034 | ASMP.5 |
| **ASSURE-M-001** | CIS Critical Security Controls v8 | CIS 18 |
| **ASSURE-M-001** | NIST CSF 2.0 | GV.OV, GV.OV-01, GV.OV-03 |
| **ASSURE-M-001** | TOGAF | Security Governance |
| **ASSURE-M-001** | AIUC-1 | B001, C010, C011, C012, D002, D004 |
| **ASSURE-M-001** | NIST SP 800-82r3 | 5.2.1 |
| **ASSURE-M-002** | ISO/IEC 27001:2022 | A.5.2, A.5.4 |
| **ASSURE-M-002** | ISO/IEC 42001 | A.3 |
| **ASSURE-M-002** | NIST CSF 2.0 | GV.RR |
| **ASSURE-M-002** | TOGAF | Security Governance |
| **ASSURE-M-002** | NIST SP 800-82r3 | 5.2.1 |

## Required actions

1. **Establish the quarter-end assurance population.**  
   Per **ASSURE-M-001**, record each in-scope system, its risk tier, last independent assessment, next due date, and whether a material change occurred during the quarter.

2. **Obtain evidence of assessor independence.**  
   Per **ASSURE-M-001**, retain an independence declaration identifying the assessor, employing organisation, reporting line, conflicts of interest, and relationship to the delivery and internal security teams. For the highest-risk tier, retain evidence that the assessor is external to both teams.

3. **Retain the signed assurance report.**  
   Per **ASSURE-M-001**, the report must record:
   - System, version, environment, and assessment dates
   - Assessment scope and exclusions
   - Methods and tools used
   - Assumptions and limitations
   - Results and findings
   - Assessor identity and approval
   - Retest or validation results where findings were closed

4. **Provide finding and remediation evidence.**  
   Per **ASSURE-M-001**, maintain a finding register showing severity, accountable owner, remediation SLA, due date, status, risk decision, and closure evidence. Findings cannot be treated as implicitly accepted merely because the attestation period has ended.

5. **Demonstrate accountability and segregation of duties.**  
   Per **ASSURE-M-002**, include the accepted responsibility record for:
   - Business owner
   - Technical owner
   - Security risk owner
   - Control implementation owner
   - Independent assurance owner
   - Production operations owner  
   
   The record must also document decision rights, delegated authorities, escalation paths, and segregation between implementation, assurance, and risk acceptance.

6. **Include applicable external-platform assurance.**  
   For external I/PaaS or SaaS, the implementation standard identifies independent security or penetration-test attestation reports and applicable certifications such as SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018, ISO 27034, PCI DSS, or AI assurance evidence according to the service involved. Source: **VeriFy-APP-002**, mapped to `ASSURE-M-001`, `CLOUD-M-007`, `CRYPT-M-001`, `DATA-M-002`, `GOV-G-006`, `OAUTH-M-001`, and `SUPPLY-M-001`:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782

7. **Record exceptions formally.**  
   Where evidence is missing or a guardrail is not met, record the deviation and technical justification in the SAF pack. Source: **VeriFy-APP-002**, mapped to `ASSURE-M-001`, `CLOUD-M-007`, `CRYPT-M-001`, `DATA-M-002`, `GOV-G-006`, `OAUTH-M-001`, and `SUPPLY-M-001`:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782  
   
   The Business Risk standard similarly requires non-compliance to be documented as a deviation in the SAF pack. Source: **VeriFy-BR-002**, mapped to `ASSURE-M-002`, `DATA-M-002`, `GOV-G-006`, `SUPPLY-M-001`, and `TM-M-003`:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981693

8. **Approve the quarterly attestation.**  
   **Advisory (not catalogue-backed):** Require dated sign-off from the independent assurance function and security risk owner, with the business owner approving any residual risk or overdue findings. The sign-off should state the evidence cut-off date and whether the conclusion is compliant, compliant with exceptions, or non-compliant.

## Evidence for audit

The minimum quarter-end pack should contain:

| Artefact | What it proves |
|---|---|
| In-scope system inventory and risk-tier record | Assurance depth and cadence were risk-based |
| Assurance schedule/register | Reviews are current and material-change triggers were considered |
| Assessor independence declaration | Assurance was separate from implementation |
| Engagement letter or statement of work | Assessor, scope, timing, and authority were established |
| Signed independent assessment or penetration-test report | Testing occurred and records scope, method, limitations, and results |
| External assessor credentials, where applicable | Highest-tier third-party assurance was suitably commissioned |
| Finding and remediation register | Findings have owners, SLAs, decisions, and status |
| Closure and retest evidence | Remediation was independently validated where required |
| Accepted responsibility matrix | Required ownership, decision rights, and segregation exist |
| Applicable supplier assurance reports or certificates | External platform assurance was current and relevant |
| SAF approval and deviation records | Exceptions were explicitly documented and governed |
| Dated quarterly attestation approval | Management reviewed the quarter-end evidence and residual exposure |

## Assumptions and limits

- The catalogue does not specify a universal quarterly independent-testing cadence; it requires cadence based on risk tier and testing after material change.
- The system risk tier, material-change status, external-service use, AI use, and existing assurance expiry dates were not provided.
- Requirements associated with the additional mandard references in the knowledge documents were not evaluated here.
- Other search results relating primarily to CI/CD and logging were set aside because they did not define the independent-assurance attestation requirement.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ASSURE-M-001**](https://verify.example-org.internal/?id=ASSURE-M-001) | High | Independent Assurance | AIUC1 (B001, C010, C011); CIS_CONTROLS (CIS 18); ISO_27001 (A.5.35); ISO_27034 (ASMP.5); NIST_800_82 (5.2.1); NIST_CSF (GV.OV, GV.OV-01, GV.OV-03); +4 more |
| [**ASSURE-M-002**](https://verify.example-org.internal/?id=ASSURE-M-002) | High | Independent Assurance | ISO_27001 (A.5.2, A.5.4); ISO_42001 (A.3); NIST_800_82 (5.2.1); NIST_CSF (GV.RR) |
| [**CLOUD-M-007**](https://verify.example-org.internal/?id=CLOUD-M-007) | High | Cloud Security | AIUC1 (E005, E011); CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32, Article 44); +11 more |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
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