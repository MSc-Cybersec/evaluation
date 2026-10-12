# G03-AC

## Question
How do we prove least-privilege access is enforced for production operators?

## Sage response
## Bottom line

Prove least privilege with a repeatable evidence chain showing: approved role design, current production assignments, technical enforcement, negative-access testing, privileged-session records, and periodic recertification. Per **IAM-M-001**, production roles must be narrowly scoped and cannot contain wildcard actions or resources; privileged access must also use MFA under **IAM-M-002** and a brokered, logged path under **IAM-M-005**. A configuration screenshot alone is insufficient because it does not demonstrate approval, effective enforcement, or continuing operation.

## Risk and impact

| Risk | Exposure if evidence or enforcement is missing |
|---|---|
| **Critical** | Excessive production permissions can enable unauthorized changes, data access, privilege escalation, and lateral movement. |
| **Critical** | Missing MFA or authorization checks can turn compromised operator credentials into direct production access. |
| **High** | Direct administration from ordinary endpoints removes the controlled chokepoint needed for session logging, rapid revocation, and network restriction. |
| **High** | Unrecorded exceptions can become permanent, ownerless production risk. |

The audit conclusion should be based on three dimensions:

1. **Design effectiveness:** operator roles contain only permissions justified by operational duties.
2. **Implementation effectiveness:** actual identities, policies, network paths, and MFA settings match the approved design.
3. **Operating effectiveness:** sampled approvals, revocations, denied actions, session logs, and reviews show the controls operated throughout the audit period.

## Governing mandards

| Mandard | Requirement | Risk |
|---|---|---|
| **AC-M-001** — Mandatory Authorization Checks | Per **AC-M-001**: sensitive operations must use explicit, deny-by-default authorization checks, including authentication, required role or permission, and resource-level access. | **Critical** |
| **IAM-M-001** — Least-Privilege IAM Policies | Per **IAM-M-001**: all production IAM policies and roles must follow least privilege; wildcard actions and resources are prohibited, and roles must be reviewed periodically. | **Critical** |
| **IAM-M-002** — Enforce MFA for Privileged Accounts | Per **IAM-M-002**: MFA must be enforced for every privileged and administrative account. | **Critical** |
| **IAM-M-005** — Brokered Administrative Access | Per **IAM-M-005**: privileged production access must use a hardened bastion, jump service, or just-in-time broker; direct administrative connectivity must be denied, MFA enforced, and sessions logged. | **High** |
| **DB-M-003** — Database Access Control & Least Privilege | Per **DB-M-003**: database accounts must be role-limited, shared accounts are prohibited, access must be audited, and reviews must occur quarterly. Applicable where operators can access production databases. | **High** |
| **GOV-G-006** — Security Deviation and Exception Management | Per **GOV-G-006**: departures must have documented justification, residual-risk ownership, compensating controls, independent approval, and an expiry date before release. | **High** |

## Framework mapping

Selected direct mappings returned for the cited mandards are:

| Mandard | Framework mappings |
|---|---|
| **IAM-M-001** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-6`; PCI DSS v4.0 `Req 7`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.2`; SOC 2 `CC6.1` |
| **IAM-M-002** | NIST SP 800-53 Rev.5 `IA-2`, `IA-5`, `AC-2`, `AC-3`, `AC-6`; PCI DSS v4.0 `Req 7`, `Req 8`; ISO/IEC 27001:2022 `A.8.2`, `A.8.5` |
| **IAM-M-005** | NIST SP 800-53 Rev.5 `AC-2`, `AC-6`, `AC-17`, `IA-2`, `AU-2`; ISO/IEC 27001:2022 `A.8.2`, `A.8.20`; SOC 2 `CC6`; CIS Controls v8 `CIS 5`, `CIS 6`, `CIS 12`; NIST CSF 2.0 `PR.AA`, `PR.IR`, `DE.CM` |
| **DB-M-003** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-6`; PCI DSS v4.0 `Req 7`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.2`; CIS Controls v8 `CIS 6` |
| **GOV-G-006** | NIST SP 800-53 Rev.5 `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022 `A.5.1`, `A.5.35`; SOC 2 `CC3`, `CC5`; NIST CSF 2.0 `GV.RM`, `GV.OV`, `ID.RA` |

## Required actions

1. **Define and approve the production role model — IAM owner and production service owner**
   - Per **IAM-M-001**, document each operator role, permitted actions, permitted production resources, prohibited actions, eligibility criteria, and business owner.
   - Remove wildcard actions and resources from production policies.
   - Separate routine operations, deployment, security administration, database administration, and emergency access.
   - Record who approved each role and why each permission is necessary.

2. **Export actual effective access — IAM and cloud/platform teams**
   - Produce machine-readable exports of all production operators, groups, nested memberships, role assignments, permission boundaries, and direct grants.
   - Reconcile the export against HR status, team membership, approved access requests, and the role model.
   - Flag direct user grants, shared accounts, dormant accounts, orphaned accounts, wildcard permissions, and unapproved role combinations.

3. **Prove privileged access is strongly authenticated and brokered — IAM and infrastructure teams**
   - Per **IAM-M-002**, export the privileged population and the applicable MFA or conditional-access policy; demonstrate that no privileged operator is excluded.
   - Per **IAM-M-005**, provide network policy showing that production management interfaces are reachable only from the bastion or broker.
   - Show that standing privilege is replaced by just-in-time activation where implemented, and that activations are time-limited and logged.
   - Test that direct access from a standard workstation or user network is denied.

4. **Test effective permissions, including negative cases — security assurance and service teams**
   - Per **AC-M-001**, test with representative operator roles that permitted actions succeed and prohibited actions return a denial.
   - Include attempts to access another application, subscription, namespace, database, region, or administrative function.
   - Retain test identity, role, target, timestamp, expected outcome, actual outcome, and immutable result.
   - Test emergency-access and low-privilege identities separately.

5. **Prove lifecycle governance — line manager, role owner, and IAM operations**
   - Sample joiner, mover, and leaver events and trace each from request and approval through provisioning or revocation.
   - Run periodic recertification for production roles and retain reviewer decisions, removed access, overdue items, and completion status.
   - Per **DB-M-003**, database access must be reviewed quarterly where production database access exists.

6. **Prove activity is attributable and monitored — SOC and platform operations**
   - Per **IAM-M-005**, retain broker and privileged-session logs showing the named identity, role activation, MFA result, source, target, commands or actions, start and end time, and session outcome.
   - Reconcile privileged activity against approved change, incident, or operational tickets.
   - Demonstrate that logs are forwarded to the SIEM and that privileged-access alerts are reviewed.

7. **Govern every exception — risk owner and independent security authority**
   - Per **GOV-G-006**, record any standing privilege, direct production path, shared account, MFA exclusion, or excessive permission as a formal deviation.
   - Require technical justification, residual-risk owner, compensating controls, independent approval, and expiry.
   - Do not treat an undocumented exception as compliant.

**Implementation guidance from the knowledge corpus**

- **VeriFy-AUTHZ-GEN-001**, mapped to **AC-M-001**, **DB-M-003**, **GOV-G-006**, **IAM-M-001**, **IAM-M-002**, **SECR-M-001**, and **SECR-M-004**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947766  
  Section 2 specifies RBAC, segregation of duties, managed provisioning and deprovisioning, least-privileged service accounts, restriction to specific hosts, and logging of both ordinary and privileged access across operating-system, database, and application environments. It also states that non-compliance must be recorded as a deviation with technical justification in the SAF pack.

- **VeriFy-AUTHZ-PRC-001**, mapped to **AC-M-001**, **IAM-M-001**, **IAM-M-002**, and **IAM-M-005**  
  Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652282497  
  The retrieved document confirms applicability to privileged access management and RBAC, but its available text does not provide the detailed request, approval, or review procedure. It should therefore support control alignment, not serve as the sole operating-evidence procedure.

Other search results concerning general data and service-account access were set aside because the question concerns human production operators rather than application or data-service identities.

## Evidence for audit

Provide an evidence pack with the following artefacts:

| Evidence | What it proves |
|---|---|
| Approved role and permission matrix | Every production permission has a defined operational purpose and owner. |
| Current IAM export | The complete operator population and effective permissions match approved roles. |
| Policy-analysis or IaC scan result | No production operator role contains prohibited wildcard actions or resources under **IAM-M-001**. |
| MFA and conditional-access export | Every privileged identity is covered by enforced MFA under **IAM-M-002**. |
| Bastion, broker, firewall, and routing configuration | Direct management access is denied and privileged access traverses the required path under **IAM-M-005**. |
| Just-in-time activation records | Privilege is activated for a bounded period rather than held permanently. |
| Positive and negative authorization-test results | Allowed actions succeed and unauthorized actions are denied under **AC-M-001**. |
| Access requests and approvals | Assignments were authorized by the correct owner before provisioning. |
| Joiner, mover, and leaver samples | Access is created, changed, and removed according to employment and role status. |
| Access-review report and reviewer sign-off | Continued access was actively recertified; for database access, retain quarterly evidence under **DB-M-003**. |
| Privileged-session and SIEM records | Operator activity is attributable, logged, monitored, and traceable to an approved purpose. |
| Exception register | Every non-compliant case is approved, owned, compensated, and time-bounded under **GOV-G-006**. |

A defensible audit sample should trace individual operators end to end:

`employment status → approved request → role assignment → MFA → brokered session → authorized action → session log → periodic recertification or revocation`

## Assumptions and limits

The current production environment, IAM configuration, operator population, access-review records, network paths, and session logs were not inspected. The evidence model above defines how compliance should be demonstrated; it does not certify that the controls are presently effective.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**DB-M-003**](https://verify.example-org.internal/?id=DB-M-003) | High | Database Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-2, AC-3, AC-4); +6 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**IAM-M-002**](https://verify.example-org.internal/?id=IAM-M-002) | Critical | Identity & Access Management | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-798); ENISA_SMLA (SMLA-17); HIPAA (164.312(a)(1)); +12 more |
| [**IAM-M-005**](https://verify.example-org.internal/?id=IAM-M-005) | High | Identity & Access Management | CIS_CONTROLS (CIS 12, CIS 5, CIS 6); ISO_27001 (A.8.2, A.8.20); MITRE_ATT&CK (M1018, M1026, M1032); NIST_CSF (DE.CM, PR.AA, PR.IR); NIST_SP_800_53 (AC-17, AC-2, AC-6); SOC2 (CC6) |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
| [**SECR-M-004**](https://verify.example-org.internal/?id=SECR-M-004) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); MITRE_ATT&CK (M1039); NIST_CSF (GV.SC-01, ID.RA-09, PR.PS-06); +9 more |

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