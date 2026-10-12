# G25-CFG

## Question
How do we prove secure-by-default configuration in every environment?

## Sage response

## Bottom line

Prove secure-by-default through a complete, repeatable evidence chain: every environment is inventoried, its approved security configuration is version-controlled, deployment is blocked when policy fails, and runtime configuration is continuously reconciled to the approved baseline. Per **CFG-M-009**, security-tool and policy configuration must be deployed from reviewed code and every change traceable to a commit and pull-request approval; without this, configuration is not reproducible or reliably auditable.

Management should require a single control owner to attest that the environment inventory reconciles to current pipeline and drift-monitoring results, with all deviations formally approved.

## Risk and impact

The primary risk is **High** under **CFG-M-009**. GUI-only settings, unmanaged environment overrides, and configuration drift can silently disable security gates, make environments inconsistent, and prevent the organisation from proving who changed a control or whether it was operating during the audit period.

Additional exposures include:

- **Critical:** insecure cookies, sensitive-field autocomplete, or unmanaged cryptographic algorithms.
- **Medium:** externally exposed non-production systems without WAF protection, production diagnostic endpoints, weak ciphers, unnecessary HTTP methods, or directory listing.
- Non-production cannot automatically be treated as low risk. Per **CFG-M-004**, an external-facing non-production application must have WAF protection defined in IaC.
- Per **CFG-M-007**, production deployments must not publicly expose debug, diagnostic, or unsecured administrative endpoints.

## Governing mandards

The complete Configuration domain contains the following mandards:

| Mandard | Title | Risk |
|---|---|---:|
| **CFG-M-001** | No Weak Ciphers | Medium |
| **CFG-M-002** | Disable Autocomplete on Sensitive Fields | Critical |
| **CFG-M-003** | Secure Cookie Flags | Critical |
| **CFG-M-004** | WAF for Non-Prod | Medium |
| **CFG-M-005** | Reject Unused HTTP Verbs | Medium |
| **CFG-M-006** | Disable Directory Listing | Medium |
| **CFG-M-007** | Disable Debug/Diagnostic Endpoints in Prod | Medium |
| **CFG-M-008** | Cryptographic Agility — External Algorithm Management | Critical |
| **CFG-M-009** | Policy and Tool Configuration as Code | High |

The principal proof mechanism is:

- Per **CFG-M-009**: define security-tool configurations, scanning thresholds, policy rules, WAF rules and container policies in version-controlled repositories; review changes through pull requests; deploy them through CI/CD; and make each change traceable to its commit and approval.
- Per **CFG-M-004**: define WAF protection for external-facing non-production applications in IaC.
- Per **CFG-M-007**: prevent public exposure of production debug, diagnostic and unsecured administrative endpoints.

There is no single retrieved Mandard that independently establishes an omnibus “secure-by-default in every environment” control. Compliance is demonstrated by applying **CFG-M-009** as the common enforcement mechanism and testing each applicable domain Mandard against the complete environment population.

## Framework mapping

Only mappings returned by the catalogue are stated below.

| Mandard | Framework mappings |
|---|---|
| **CFG-M-004** | NIST SP 800-53 Rev. 5: `CM-2`, `CM-3`, `CM-6`, `SC-7` |
| **CFG-M-007** | NIST SP 800-53 Rev. 5: `CM-3`, `CM-6`, `SA-11`, `SA-15`, `SC-7`, `SI-10`; ISO/IEC 27001:2022: `A.8.20`, `A.8.22`, `A.8.25`, `A.8.26`, `A.8.28`, `A.8.31`, `A.8.32`; PCI DSS v4.0: Requirements `1` and `6`; OWASP ASVS 5.0: `V13`; OWASP Top 10:2025: `A02:2025`; OWASP SAMM 2.0: Secure Deployment and Security Testing |

A framework mapping for **CFG-M-009** was not available in the retrieved output and has not been inferred.

## Required actions

1. **Put configuration and policy in version control — DevOps and Security Engineering.**  
   Per **CFG-M-009**, export security-tool settings, thresholds, scanning parameters, WAF rules and container policies into repository files. Remove or restrict GUI modification, require pull-request approval, and record the approved configuration in `SECURITY_CONFIG.md`.

2. **Establish the environment population — Platform owner.**  
   **Advisory (not knowledge-doc backed):** maintain an authoritative register covering development, integration, test, UAT, staging, disaster recovery, production, ephemeral environments, cloud accounts/subscriptions, clusters and externally hosted instances. Automatically reconcile it with cloud, orchestration and deployment inventories so that “every environment” is measurable rather than asserted.

3. **Deploy one approved baseline through CI/CD — DevOps.**  
   Per **CFG-M-009**, pipelines must source configuration from the repository rather than hardcoded defaults or portal settings. Validate syntax and policy before deployment and retain the commit SHA, pull-request approval and deployment identity.

4. **Use preventive deployment gates — DevSecOps.**  
   Per **CFG-M-009**, validate that required configuration files exist and are deployed before the corresponding tool or workload. Fail deployment when policy validation detects a missing or non-compliant control.

5. **Test environment-specific requirements.**
   - Per **CFG-M-004**, block deployment of an external-facing non-production application unless its IaC deploys and attaches the required WAF.
   - Per **CFG-M-007**, run post-deployment endpoint discovery against production and fail or roll back if public debug, diagnostic or unsecured administrative routes are reachable.
   - Test the remaining applicable Configuration mandards across each environment rather than assuming that a shared template proves runtime compliance.

6. **Detect runtime drift — Platform Security.**  
   Per **CFG-M-009**, continuously compare deployed configuration with the repository baseline and alert on differences. Findings must identify the environment, resource, expected state, observed state, detection time and remediation status.

7. **Govern deviations — Architecture and InfoSec.**  
   The release-management and application-layer guidance requires non-compliance to be recorded as a deviation with technical justification in the SAF pack:
   - **VeriFy-IS-RMP-001**, mapped to `ART-M-001`, `ART-M-002`, `GOV-G-006`, `INTEG-M-002`, `LOG-M-003`, `PIPE-M-001`, `PIPE-M-012`, `SECR-M-002`, `SIGN-M-001` — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688).
   - **VeriFy-APP-002**, mapped to `ASSURE-M-001`, `CLOUD-M-007`, `CRYPT-M-001`, `DATA-M-002`, `GOV-G-006`, `OAUTH-M-001`, `SUPPLY-M-001` — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782).

   These documents also cover On-Premises, Azure and, for application governance, offsite environments. They are implementation guidance and are not directly mapped to **CFG-M-009**.

## Evidence for audit

The minimum audit package should contain:

| Proof objective | Audit artefact |
|---|---|
| Complete environment coverage | Timestamped environment inventory and reconciliation report showing every registered environment has a deployment and compliance result |
| Approved baseline | Version-controlled configuration files, `SECURITY_CONFIG.md`, immutable commit SHA and repository history |
| Independent review | Pull request, named approvers, branch-protection result and change ticket |
| Preventive enforcement | CI/CD policy-gate logs showing pass/fail outcomes and blocked non-compliant deployments |
| Reproducible deployment | Deployment record linking environment, artifact, baseline version, pipeline run and service identity |
| Runtime effectiveness | Post-deployment scan results and signed or immutable compliance attestations for each environment |
| Drift control | Scheduled comparison report showing expected versus deployed configuration, including alerts and remediation records |
| Non-production WAF | IaC definition, scanner result, deployed-resource evidence and WAF attachment for each externally exposed non-production application |
| Production endpoint control | Endpoint-discovery or DAST result demonstrating that debug, diagnostic and unsecured administrative endpoints are not publicly reachable |
| Exceptions | Time-bound deviation record, technical justification, risk owner approval, compensating controls and expiry date in the SAF pack |
| Period effectiveness | Trend or control report showing the gate and drift checks operated throughout the audit period, not only on the audit date |

A defensible attestation should therefore be expressed as:

> All inventoried environments were deployed from an approved configuration commit, passed the applicable pre-deployment policy gates, passed post-deployment verification, and had no unresolved drift or unapproved deviations during the reporting period.

## Assumptions and limits

- The organisation’s actual environment inventory, repositories, pipeline controls, runtime state and deviations were not inspected.
- No knowledge document is currently mapped directly to **CFG-M-009** or **CFG-M-004**.
- The proposed environment reconciliation and consolidated attestation format are **Advisory (not knowledge-doc backed)**.
- Framework mappings were included only where they were returned by the Mandard catalogue.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**ASSURE-M-001**](https://verify.example-org.internal/?id=ASSURE-M-001) | High | Independent Assurance | AIUC1 (B001, C010, C011); CIS_CONTROLS (CIS 18); ISO_27001 (A.5.35); ISO_27034 (ASMP.5); NIST_800_82 (5.2.1); NIST_CSF (GV.OV, GV.OV-01, GV.OV-03); +4 more |
| [**CFG-M-001**](https://verify.example-org.internal/?id=CFG-M-001) | Medium | Configuration | CIS_CONTROLS (CIS 16, CIS 3); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24, A.8.25); +11 more |
| [**CFG-M-002**](https://verify.example-org.internal/?id=CFG-M-002) | Critical | Configuration | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 16, CIS 3, CIS 5); COBIT_2019 (BAI03.03, BAI06.01, DSS05.04); CWE (CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.502); +11 more |
| [**CFG-M-003**](https://verify.example-org.internal/?id=CFG-M-003) | Critical | Configuration | CIS_CONTROLS (CIS 12, CIS 16, CIS 3); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-327, CWE-384, CWE-77); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.20, A.8.22); +11 more |
| [**CFG-M-004**](https://verify.example-org.internal/?id=CFG-M-004) | Medium | Configuration | CIS_CONTROLS (CIS 12, CIS 16, CIS 4); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-77, CWE-79, CWE-89); ISO_27001 (A.8.16, A.8.20, A.8.22); MITRE_ATT&CK (M1022, M1028, M1042); +10 more |
| [**CFG-M-005**](https://verify.example-org.internal/?id=CFG-M-005) | Medium | Configuration | CIS_CONTROLS (CIS 16); COBIT_2019 (APO12.01, BAI03.03, BAI06.01); CWE (CWE-384); ISO_27001 (A.8.25, A.8.26, A.8.28); MITRE_ATT&CK (M1022, M1028, M1042); NIST_CSF (GV.OC-01, GV.RM-01, PR.DS-01); +8 more |
| [**CFG-M-006**](https://verify.example-org.internal/?id=CFG-M-006) | Medium | Configuration | CIS_CONTROLS (CIS 11, CIS 16); COBIT_2019 (BAI03.03, BAI06.01); ISO_27001 (A.8.13, A.8.14, A.8.25); MITRE_ATT&CK (M1022, M1028, M1042); NIST_CSF (PR.DS-01, PR.PS-01, PR.PS-06); NIST_SP_800_53 (CM-3, CM-6, CP-10); +8 more |
| [**CFG-M-007**](https://verify.example-org.internal/?id=CFG-M-007) | Medium | Configuration | CIS_CONTROLS (CIS 12, CIS 16); COBIT_2019 (BAI03.03, BAI06.01); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); ISO_27001 (A.8.20, A.8.22, A.8.25); MITRE_ATT&CK (M1022, M1028, M1042); NIST_800_82 (5.2.3, 6.2.1); +9 more |
| [**CFG-M-008**](https://verify.example-org.internal/?id=CFG-M-008) | Critical | Configuration | CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, DSS02.01); ISO_27001 (A.5.24, A.5.26, A.8.16); MITRE_ATT&CK (M1022, M1028, M1042); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); NIST_SP_800_53 (AU-6, CM-3, CM-6); +8 more |
| [**CFG-M-009**](https://verify.example-org.internal/?id=CFG-M-009) | High | Configuration | CIS_CONTROLS (CIS 16, CIS 4, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); HIPAA (164.312(b)); ISO_27001 (A.5.36, A.8.15, A.8.16); MITRE_ATT&CK (M1022, M1028, M1042); +11 more |
| [**CLOUD-M-007**](https://verify.example-org.internal/?id=CLOUD-M-007) | High | Cloud Security | AIUC1 (E005, E011); CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (APO12.01, APO13.01, BAI09.01); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32, Article 44); +11 more |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |

Showing 15 of 23 cited mandards.

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