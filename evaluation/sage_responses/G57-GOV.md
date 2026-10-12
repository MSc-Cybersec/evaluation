# G57-GOV

## Question
Which governance artefacts are mandatory for annual control assurance review?

## Sage response

## Bottom line

The catalogue does not prescribe a single named “annual control assurance review pack.” However, the annual review must retain two mandatory evidence sets: an **independent assurance record** and a **current responsibility and authority model**. Missing or stale evidence means assurance cannot demonstrate control effectiveness, ownership, assessor independence, or accountable remediation.

## Risk and impact

Both applicable Mandards are rated **High**.

Without the required artefacts:

- Security claims may remain self-assessed or unsupported.
- Findings may be implicitly accepted instead of remediated.
- Control implementation, risk acceptance, and production responsibilities may be unassigned or conflicted.
- Production approval must be blocked where required responsibilities are unassigned.
- Audit and regulatory assurance may fail because assessor independence, review scope, results, or management accountability cannot be demonstrated.

## Governing mandards

| Mandard | Title | Risk | Mandatory annual-review artefacts |
|---|---|---:|---|
| **ASSURE-M-001** | Independent Security Assurance and Third-Party Testing | High | Assurance report recording assessor independence, scope, method, limitations and results; associated findings and evidence that they are tracked to closure; assurance schedule/register aligned to system risk tier and material changes. |
| **ASSURE-M-002** | Software Assurance Roles, Responsibilities and Authorities | High | Accepted responsibility model identifying required owners, decision rights, segregation of duties, escalation paths and delegated authorities; evidence of annual review and review following material change. |

Per **ASSURE-M-001**: security claims must receive assurance independent of the delivery team at a depth and frequency proportionate to risk. Highest-tier systems also require an assessor independent of both delivery and the internal security function.

Per **ASSURE-M-002**: every system must have named and accepted accountability for business ownership, technical ownership, security risk ownership, control implementation, independent assurance and production operation.

## Framework mapping

The following mappings were returned by the SAGF catalogue:

| Mandard | Framework mappings |
|---|---|
| **ASSURE-M-001** | NIST SP 800-53 Rev.5: `CA`, `CA-2`, `CA-8`; ISO/IEC 27001:2022: `A.5.35`; SOC 2 Type II: `CC4`; OWASP SAMM 2.0: `Verification: Security Testing`; ISO/IEC 27034: `ASMP.5`; CIS Controls v8: `CIS 18`; NIST CSF 2.0: `GV.OV`, `GV.OV-01`, `GV.OV-03`; TOGAF: `Security Governance`; AIUC-1: `B001`, `C010`, `C011`, `C012`, `D002`, `D004`; NIST SP 800-82r3: `5.2.1`. |
| **ASSURE-M-002** | ISO/IEC 27001:2022: `A.5.2`, `A.5.4`; ISO/IEC 42001: `A.3`; NIST CSF 2.0: `GV.RR`; NIST SP 800-82r3: `5.2.1`. |

## Required actions

1. **Control or system owner:** assemble the annual evidence set containing:
   - Current system risk tier and assurance cadence.
   - Independent assurance report.
   - Assessor independence statement.
   - Approved assessment scope and method.
   - Recorded assessment limitations.
   - Test results and findings register.
   - Remediation status, owners, due dates and closure evidence.

2. **Business and security risk owners:** approve and accept the current responsibility model covering:
   - Business owner.
   - Technical owner.
   - Security risk owner.
   - Control implementer.
   - Independent assurance owner.
   - Production operations owner.
   - Decision rights, delegated authorities and escalation paths.
   - Segregation-of-duties arrangements.

3. **CISO governance function:** confirm that:
   - Assurance remains current for the system’s risk tier.
   - Material changes have triggered additional review where required.
   - Highest-tier systems have the required third-party testing.
   - Open findings are governed by remediation SLAs and have not been accepted implicitly.
   - Role assignments are complete, accepted and reviewed within the annual period.

4. **Advisory (not knowledge-doc backed):** maintain an indexed review cover sheet recording review date, period covered, attendees, evidence references, exceptions, decisions and formal approval. This simplifies audit sampling but is not explicitly mandated as a named artefact.

## Evidence for audit

| Evidence | Minimum content |
|---|---|
| Assurance register | System, risk tier, last assessment, next due date, material-change reviews and assessor. |
| Independent assurance report | Assessor independence, scope, method, limitations, results and date. |
| Findings register | Severity, accountable owner, remediation deadline, status and closure evidence. |
| Responsibility model | Named and accepted roles, decision rights, segregation of duties, escalation paths and delegated authority. |
| Annual review record | Review date, reviewed assignments, changes made and accountable approval. |
| Production gate record | Evidence that incomplete, stale or unaccepted accountability blocks production approval. |
| Exception or deviation record | Technical justification, accountable approval and inclusion in the applicable SAF pack. |

Implementation guidance found in **VeriFy-APP-002**, *5. Application Layer (Governance)*, states that non-compliance must be formally recorded as a deviation, supported by technical justification, and included in the SAF pack.  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782  
Mapped Mandards recorded by the document: **ASSURE-M-001**, **CLOUD-M-007**, **CRYPT-M-001**, **DATA-M-002**, **GOV-G-006**, **OAUTH-M-001**, **SUPPLY-M-001**.

## Assumptions and limits

No knowledge document was found that defines a dedicated, organisation-wide procedure or fixed template specifically titled “annual control assurance review.” Technology-specific documents returned by the search were set aside because they address domain guardrails rather than the composition of the annual assurance evidence set. The mandatory artefacts above are therefore derived directly from **ASSURE-M-001** and **ASSURE-M-002**, rather than from a prescribed review-pack template.

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