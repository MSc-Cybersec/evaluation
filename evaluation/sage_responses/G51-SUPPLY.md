# G51-SUPPLY

## Question
What supply-chain assurances are required before onboarding a new vendor library?

## Sage response

## Bottom line

A new vendor library must not enter production until it has passed vulnerability and licence gates and, where it exceeds the organisation’s defined third-party risk threshold, has a documented and approved risk assessment. Open-source libraries require additional evidence of project health, maintenance, release maturity, security response capability, and licence compatibility. If the library is an IDE extension, plugin, build tool, or development tool, it must also be vetted, approved, inventoried, and allowlisted.

## Risk and impact

| Assurance | Risk | Exposure if unaddressed |
|---|---:|---|
| No Critical or High CVEs | Critical | Exploitation through known vulnerable dependencies and supply-chain compromise |
| Approved licence | Critical | Intellectual-property, contractual, and source-disclosure obligations |
| Third-party risk assessment | High | Unassessed vendor, provenance, maintenance, vulnerability-response, and continuity risks |
| Development-tool integrity, where applicable | High | Malicious tooling gaining access to source code, credentials, endpoints, or build systems |

## Governing mandards

- **SCA-M-001 — No Critical CVEs — Critical.** Per **SCA-M-001**: the build must fail when SCA detects a Critical or High severity CVE in any third-party library or dependency. The component must be patched or replaced before admission.
- **SCA-M-002 — Approved Licenses — Critical.** Per **SCA-M-002**: the build must fail when a dependency has a non-approved licence. The library must be replaced or handled through an approved exception before use.
- **SUPPLY-M-001 — Third-Party Risk Assessment — High.** Per **SUPPLY-M-001**: components and services above the defined risk threshold must have a documented risk assessment before production use. Open-source components must also be assessed for:
  - Active maintenance and project maturity
  - Stable release status rather than alpha or beta
  - Sufficient maintainers and contributors
  - Dependency freshness
  - Security-relevant test coverage
  - Documented vulnerability reporting and response
  - Licence consistency with intended use
- **SUPPLY-M-002 — Secure Development Platform and Tooling Integrity — High.** Per **SUPPLY-M-002**: when the library is a plugin, extension, IDE component, build tool, or development tool, it must be vetted, approved, inventoried, and restricted to trusted tooling; unreviewed extensions must be blocked.

## Framework mapping

The catalogue returned the following relevant mappings:

| Mandard | Framework mappings |
|---|---|
| **SUPPLY-M-001** | NIST SP 800-53 Rev. 5: RA-3, SI-4, AU-6, SR-3, SR-4, SA-12, SA-22, PL-8, PM-9, PL-2, IR-4, IR-6; ISO/IEC 27001:2022: A.8.16 |
| **SUPPLY-M-002** | NIST SP 800-53 Rev. 5: RA-3, SR-3, SR-4, SA-12, IA-5, SC-12, PL-8, PM-9, PL-2; ISO/IEC 27001:2022: A.5.19, A.5.21, A.8.30, A.8.24, A.5.17; OWASP Top 10:2025: A03 Software Supply Chain Failures; CIS Controls v8: CIS 2 |
| **SCA-M-001** | NIST SP 800-53 Rev. 5: RA-3, AU-2, AU-6, AU-12, SI-4, SR-3, SR-4, SA-12 |
| **SCA-M-002** | NIST SP 800-53 Rev. 5: RA-3, SI-4, AU-6, SR-3, SR-4, SA-12, SA-22; ISO/IEC 27001:2022: A.8.16, A.5.19, A.5.21, A.8.30, A.8.19, A.5.31, A.5.32 |

## Required actions

1. **Product Security or engineering:** Run SCA against the direct library and its transitive dependency tree. Reject the version if any Critical or High CVE is present, per **SCA-M-001**.
2. **Legal or open-source governance:** Validate the detected licence against the approved licence policy. Configure the pipeline to reject non-approved licences, per **SCA-M-002**.
3. **Third-Party Risk Management:** Determine whether the component exceeds the defined risk threshold. If it does, complete and approve the vendor risk assessment before production use, per **SUPPLY-M-001**.
4. **Security Champion or architect:** For open-source components, document the structured project-health assessment required by **SUPPLY-M-001**, including maintenance, maturity, stable release status, contributor sufficiency, dependency freshness, tests, vulnerability handling, and licence consistency.
5. **Engineering:** Register the exact component name, version, source, approval status, and associated assessment record in the dependency or vendor registry. Gate CI/CD so unapproved components cannot proceed, per **SUPPLY-M-001**.
6. **Product Security:** Establish ongoing vulnerability monitoring because approval is not permanent; new CVEs must be detected and acted upon, per **SUPPLY-M-001** and **SCA-M-001**.
7. **Developer Platform team, if applicable:** For plugins and development tooling, add the item to the approved-tool inventory, enforce an allowlist, block unreviewed tools, and confirm endpoint-security coverage, per **SUPPLY-M-002**.

**Implementation guidance:**  
**VeriFy-CE-001**, mapped to **SCA-M-001**, requires relevant software designs and security testing to address vulnerable and outdated components and software/data integrity failures. It also identifies approval and release-pipeline activities for applicable endpoint deployments. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082

No knowledge document was found for **SUPPLY-M-002** or **SCA-M-002**. The concrete pipeline and inventory steps above are catalogue implementation content from the relevant mandards, not separate knowledge-document procedures.

## Evidence for audit

Retain the following in the onboarding or change record:

- SCA report covering direct and transitive dependencies, showing no Critical or High CVEs
- Successful CI/CD security gate result
- Licence scan and approved-licence policy result
- Approved third-party risk assessment, where the threshold applies
- Open-source project-health assessment, where applicable
- Component inventory or SBOM entry recording name, exact version, source, owner, and approval status
- Vendor security questionnaire and contractual security requirements, where applicable
- Evidence of ongoing vulnerability monitoring and accountable ownership
- For development tooling, approved-tool inventory entry, allowlist configuration, and endpoint-security posture
- Any formally approved exception or deviation record

## Assumptions and limits

The organisation’s risk threshold, approved licence list, and exception authority were not provided and must be obtained from the applicable internal policies. The specific library, version, provenance, licence, dependency tree, vendor status, and current vulnerabilities were not assessed. Framework mappings shown are limited to mappings visible in the tool results.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**SCA-M-001**](https://verify.example-org.internal/?id=SCA-M-001) | Critical | Supply Chain Analysis | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CSA_CCM (TVM); ENISA_SMLA (SMLA-08); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); +16 more |
| [**SCA-M-002**](https://verify.example-org.internal/?id=SCA-M-002) | Critical | Supply Chain Analysis | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); ISO_27001 (A.5.19, A.5.21, A.5.31); MITRE_ATT&CK (M1016, M1051); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AU-6, RA-3, SA-12); +7 more |
| [**SUPPLY-M-001**](https://verify.example-org.internal/?id=SUPPLY-M-001) | High | Supply Chain Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (STA); ENISA_SMLA (SMLA-20, SMLA-22); +18 more |
| [**SUPPLY-M-002**](https://verify.example-org.internal/?id=SUPPLY-M-002) | High | Supply Chain Security | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); NIST_CSF (GV.OC-01, GV.RM-01, GV.SC-01); NIST_SP_800_53 (IA-5, PL-2, PL-8); +6 more |

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