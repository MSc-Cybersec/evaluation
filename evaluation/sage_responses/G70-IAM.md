# G70-IAM

## Question
How do we prove IAM controls are enforced consistently across platforms?

## Sage response

## Bottom line

Prove consistent IAM enforcement through a single control-to-platform evidence matrix that reconciles every in-scope platform against the same IAM assertions: least privilege, MFA, identity lifecycle, CI/CD access, and brokered administration. Configuration screenshots alone are insufficient; assurance should combine authoritative inventory, machine-readable configuration, automated negative tests, operational records, and formally approved deviations.

Management should require accountable platform owners to submit this evidence continuously or at a defined review cadence, with unresolved Critical failures blocking production access or release.

## Risk and impact

Failure to establish consistent enforcement leaves gaps where attackers can use excessive permissions, password-only privileged accounts, orphaned identities, or direct administrative connections to production.

| Priority | Exposure |
|---|---|
| Critical | Excessive permissions can enable privilege escalation and lateral movement; privileged accounts without MFA materially increase account-takeover risk. |
| High | CI/CD compromise can permit unauthorized production deployment. Incomplete lifecycle management leaves orphaned or stale accounts. Direct administration bypasses centralized MFA, session logging, and rapid revocation. |

Consistency means that the same control outcome is enforced across platforms; it does not require every platform to use identical technical configuration.

## Governing mandards

| Mandard | Risk | Required control |
|---|---:|---|
| **IAM-M-001**, Least-Privilege IAM Policies | Critical | Per **IAM-M-001**: all policies and roles must follow least privilege; wildcard actions or resources are prohibited for production roles, and roles must be reviewed periodically. |
| **IAM-M-002**, Enforce MFA for Privileged Accounts | Critical | Per **IAM-M-002**: MFA must be enforced for all privileged and administrative accounts. |
| **IAM-M-003**, Enforce Multi-Factor Authentication in CI/CD Systems | High | Per **IAM-M-003**: all CI/CD platform access must require non-bypassable MFA, including administrator access. |
| **IAM-M-004**, Maintain Identity Lifecycle Management for CI/CD Accounts | High | Per **IAM-M-004**: maintain a centralized CI/CD identity inventory, use controlled joiner/mover/leaver processes, deprovision leavers within 24 hours, and deprovision or review accounts unused for more than 90 days. |
| **IAM-M-005**, Brokered Administrative Access | High | Per **IAM-M-005**: production administration must traverse a hardened broker or bastion; direct management access from general-purpose endpoints must be denied, MFA enforced, and privileged sessions logged. |

## Framework mapping

The following are decision-relevant mappings returned by the SAGF catalogue; this is not presented as an exhaustive list of every available mapping.

| Mandard | Returned mappings |
|---|---|
| **IAM-M-001** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, IA-2, IA-4, IA-8; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.3, A.5.15, A.5.16, A.5.18, A.8.2, A.8.3, A.8.5, A.8.18; SOC 2: CC6.1; OWASP ASVS 5.0: V8. |
| **IAM-M-002** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-2, AC-3, AC-6, AC-7; PCI DSS v4.0: Req 7, Req 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5, A.8.24. |
| **IAM-M-003** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-2, AC-3, AC-4, AC-6, AC-7, SR-3, SR-4, SA-12, SC-12. |
| **IAM-M-004** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, IA-2, SR-3, SR-4, SA-12. |
| **IAM-M-005** | NIST SP 800-53 Rev. 5: AC-2, AC-6, AC-17, IA-2, AU-2; ISO/IEC 27001:2022: A.8.2, A.8.20; SOC 2: CC6; CIS Controls v8: CIS 5, CIS 6, CIS 12; NIST CSF 2.0: PR.AA, PR.IR, DE.CM. |

## Required actions

### Required controls

1. **Establish the control population and denominator — IAM governance owner**
   - Create an authoritative register of cloud subscriptions, SaaS platforms, CI/CD systems, operating systems, applications, databases, directories, and privileged-access systems.
   - Assign a platform owner and record the authoritative identity provider and evidence source for each platform.
   - Per **IAM-M-004**, the CI/CD portion must include identity name, owner, identity provider, creation date, last-used date, last-updated date, assigned permissions, and permissions actually used.

2. **Define common machine-testable assertions — IAM engineering**
   - Per **IAM-M-001**, test production policies for wildcard actions/resources and permissions exceeding approved role definitions.
   - Per **IAM-M-002**, reconcile every privileged identity with MFA enforcement status.
   - Per **IAM-M-003**, test that CI/CD users and administrators cannot authenticate without MFA.
   - Per **IAM-M-004**, detect local, shared, orphaned, unowned, stale, and overdue leaver accounts.
   - Per **IAM-M-005**, scan for production management interfaces reachable from user networks or the internet, standing privileged roles, and unlogged broker sessions.

3. **Collect evidence directly from enforcement points — platform owners**
   - Use IdP, cloud, SaaS, PAM, network, database, and CI/CD APIs rather than self-attestation wherever supported.
   - Store timestamped policy exports, role assignments, group memberships, MFA enforcement states, last-use information, network reachability results, and privileged-session logging status.
   - Tie every record to platform, environment, account or role, control ID, collection time, and evidence owner.

4. **Execute independent outcome tests — security assurance**
   - Attempt privileged authentication without the second factor and confirm denial.
   - Attempt unauthorized access using representative low-privilege identities and confirm denial.
   - Attempt direct access to production management interfaces outside the broker path and confirm network-layer denial.
   - Test a leaver event and demonstrate deprovisioning within the **IAM-M-004** 24-hour requirement.
   - Confirm a CI/CD user cannot bypass MFA through an alternative authentication route.

5. **Reconcile and report exceptions — control owners and risk management**
   - Compare the platform inventory with collected evidence so missing evidence is reported as a failure, not excluded from reporting.
   - Record deviations with affected assets, technical justification, risk owner, compensating controls, approval, expiry date, and remediation plan.
   - Prioritize unresolved **IAM-M-001** and **IAM-M-002** failures ahead of High-risk findings.

6. **Introduce enforcement gates**
   - Per **IAM-M-001**, fail CI/IaC validation when production IAM policies contain prohibited wildcards.
   - Per **IAM-M-003**, block CI/CD access where MFA is not enforced.
   - Per **IAM-M-004**, flag or deprovision CI/CD accounts unused for more than 90 days.
   - Per **IAM-M-005**, fail configuration checks when management ports are directly reachable, privileged roles remain standing rather than just-in-time, or broker sessions are not logged.

### Implementation guidance

The knowledge corpus supports standardizing IAM patterns across technology layers:

- **VeriFy-AUTH-INT-EC-001**, mapped to **IAM-M-001** among other mandards, describes enterprise authentication patterns using centralized directory and IdP integration across infrastructure, web services, applications, databases, and middleware.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445334

- **VeriFy-AUTHZ-GEN-001**, mapped to **IAM-M-001** and **IAM-M-002**, applies privileged-access and authorization guardrails across on-premises and Azure operating-system, application, and database environments. It requires non-compliance to be recorded as a formal deviation.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766

- **VeriFy-DATA-AM-001**, mapped to **IAM-M-002** and **IAM-M-004**, covers database and file-level access provisioning across on-premises and Azure environments and calls for formal recording of non-compliance.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817601

- **VeriFy-IS-RMP-001**, mapped to **IAM-M-001** among other mandards, identifies least-privilege repository access as a CI/CD source-stage guardrail.  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688

Database-specific guidance was also returned for DB2, MongoDB, Oracle, and PostgreSQL. Each is mapped to **IAM-M-001**, covers on-premises and Azure authentication patterns, and requires less-preferred variants to have a technical motivation with deviations documented in the enterprise architecture design artefact:

- **VeriFy-AUTH-INT-DB-DB2-001**: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/655069728
- **VeriFy-AUTH-INT-DB-MDB-001**: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/771686766
- **VeriFy-AUTH-INT-DB-ORA-001**: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/771686482
- **VeriFy-AUTH-INT-DB-PG-001**: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/772046938

**Advisory (not knowledge-doc backed):** Publish a dashboard with one row per platform and columns for evidence freshness, least-privilege result, privileged MFA coverage, lifecycle exceptions, direct-administration exposure, session logging, deviation status, and accountable owner. Do not report aggregate compliance unless every in-scope platform is represented in the denominator.

## Evidence for audit

| Control claim | Minimum audit artefact |
|---|---|
| Scope is complete | Approved platform inventory reconciled to CMDB, cloud accounts, SaaS register, CI/CD inventory, and database inventory; unmatched records documented. |
| **IAM-M-001** is enforced | Machine-readable policy exports, scanner output showing prohibited wildcard checks, pipeline gate results, role-review approvals, and remediation tickets. |
| **IAM-M-002** is enforced | Privileged-account inventory reconciled to IdP MFA policy and registration/enforcement exports; failed password-only authentication test. |
| **IAM-M-003** is enforced | CI/CD organization configuration export, user MFA exception report, alternative-login-path test, and recovery procedure. |
| **IAM-M-004** is enforced | Identity inventory, IdP/SCIM provisioning configuration, joiner/mover/leaver tickets, termination timestamps, stale-account report, and access-review approvals. |
| **IAM-M-005** is enforced | Network rules restricting management interfaces to broker subnets, external/internal reachability scans, just-in-time activation records, MFA logs, and privileged-session records forwarded to the SIEM. |
| Deviations are controlled | Approved deviation record containing rationale, affected scope, compensating controls, risk acceptance, expiry date, and remediation owner. |
| Evidence is reliable | Immutable or access-controlled evidence repository containing source system, collection timestamp, collector identity, query or rule version, and integrity hash. |

A defensible audit sample should trace each selected identity from authoritative source, through provisioning and assigned roles, to platform enforcement and activity logs—and trace a terminated identity through timely revocation.

## Assumptions and limits

No live platform configurations, identity populations, access paths, scan outputs, exception records, or evidence-retention controls were verified. The organisation’s exact platform scope, evidence cadence, retention period, sampling method, and risk-acceptance authority were not provided. Framework mappings above are limited to mappings returned by the SAGF tools and should not be treated as a complete cross-framework assessment.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-003**](https://verify.example-org.internal/?id=IAM-M-003) | High | Identity & Access Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); MITRE_ATT&CK (M1018, M1026, M1032); +10 more |
| [**IAM-M-004**](https://verify.example-org.internal/?id=IAM-M-004) | High | Identity & Access Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.18); MITRE_ATT&CK (M1018, M1026, M1032); +10 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |

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