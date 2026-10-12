# G61-REPO

## Question
What repository controls are mandatory to reduce source and secret risk?

## Sage response

## Bottom line

SAGF mandates **six repository controls** and **five secrets-management controls** that collectively protect source integrity, enforce independent review, block unsafe changes, prevent credential disclosure, and restrict build inputs. The immediate decision is to make these controls centrally enforced and non-bypassable across production repositories; otherwise malicious or erroneous code and exposed credentials can reach protected branches and downstream environments.

## Risk and impact

The highest exposure is failure of the merge gate or secret controls. This can permit unilateral code changes, deployment of vulnerable code, credential theft from repository history or build logs, and compromise of production automation.

| Priority | Exposure |
|---|---|
| **Critical** | Unreviewed or untested code merged; credentials committed, logged, or retained; long-lived production credentials stolen |
| **High** | Untraceable changes, compromised dependencies or images, and excessive credential lifetime |
| **Medium** | Direct pushes bypass governance or untrained contributors introduce preventable vulnerabilities |

## Governing mandards

### Repository controls

| Mandard | Title | Risk | Mandatory requirement |
|---|---|---:|---|
| **REPO-M-002** | PR Review Required | **Critical** | Per **REPO-M-002**: branch protection must require at least one approval from a CODEOWNER or other qualified reviewer. |
| **REPO-M-003** | Status Checks Must Pass | **Critical** | Per **REPO-M-003**: all required CI checks, including build, SAST, and SCA, must pass before merge. |
| **REPO-M-004** | Link Work Items | **High** | Per **REPO-M-004**: every pull request must link to a valid work item before merge. |
| **REPO-M-005** | Trusted Registry Allowlist | **High** | Per **REPO-M-005**: pipelines may pull base images and artifacts only from approved registries. |
| **REPO-M-001** | Branch Protection Enabled | **Medium** | Per **REPO-M-001**: protect every `main` or `master` branch and block all direct pushes. |
| **REPO-M-006** | Training-Based Access Control | **Medium** | Per **REPO-M-006**: production-repository write access requires relevant secure-coding assessment completion with at least 80%; training must be renewed annually and verified by a merge gate. |

### Secret-risk controls

| Mandard | Title | Risk | Mandatory requirement |
|---|---|---:|---|
| **SECR-M-001** | No Hardcoded Secrets | **Critical** | Per **SECR-M-001**: fail the build when high-confidence secrets are found in source or configuration. Remove and invalidate exposed credentials and use an approved secret vault. |
| **SECR-M-002** | Prevent Secret Exposure in CI/CD Logs and History | **Critical** | Per **SECR-M-002**: scan logs for secrets, fail on detection, redact sensitive values, clean working directories and command history, and scan built images for embedded secrets before registry push. |
| **SECR-M-004** | Short-Lived Credentials & Rotation | **Critical** | Per **SECR-M-004**: production automation must use short-lived credentials; long-lived secrets are prohibited. |
| **SECR-M-005** | No Secrets in Build Logs | **Critical** | Per **SECR-M-005**: CI systems and build logs must not contain plaintext secrets, tokens, or credentials. |
| **SECR-M-003** | Enforce Temporary Credentials and Credential Rotation in CI/CD | **High** | Per **SECR-M-003**: use OIDC or equivalent temporary credentials, with TTL no greater than 15 minutes for interactive and one hour for automated credentials. Remaining stored credentials must rotate at least every 90 days and overdue credentials must be revoked automatically. |

## Framework mapping

The following are verified mappings returned by the mandard catalogue; they are grouped for readability rather than presented as an exhaustive crosswalk.

| Mandards | Verified framework controls |
|---|---|
| **REPO-M-001**, **REPO-M-002**, **REPO-M-003** | NIST SP 800-53 Rev.5 `CM-3`, `SA-15`, `AC-3`; ISO/IEC 27001:2022 `A.8.25`, `A.8.31`, `A.8.32`; SOC 2 `CC6.1`; NIST CSF 2.0 `PR.PS-06`; NIST SSDF `PS.1.1`, `PS.2.1`, `PW.4.1` |
| **REPO-M-002** | ISO/IEC 27001:2022 `A.5.3`, `A.8.4`; SOC 2 `CC8` |
| **REPO-M-004** | NIST SP 800-53 Rev.5 `AU-6`, `CM-3`, `IR-4`, `IR-6`, `SI-4`; ISO/IEC 27001:2022 `A.8.16`, `A.5.24`, `A.5.26`; SOC 2 `CC7.2`, `CC7.3` |
| **REPO-M-005** | NIST SP 800-53 Rev.5 `SR-3`, `SR-4`, `SA-12`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.5.21`, `A.8.9`, `A.8.28` |
| **REPO-M-006** | NIST SP 800-53 Rev.5 `AC-2`, `AC-3`, `AC-6`, `AC-4`, `CM-3` |
| **SECR-M-001** | NIST SP 800-53 Rev.5 `IA-5`, `AC-6`, `SI-4`, `AU-6`, `SR-3`, `SR-4`, `SA-12` |
| **SECR-M-003** | NIST SP 800-53 Rev.5 `IA-5`, `SC-8`, `AU-2` |
| **SECR-M-004** | NIST SP 800-53 Rev.5 `IA-5`, `SC-12`; ISO/IEC 27001:2022 `A.5.17`, `A.8.24`; SOC 2 `CC6.1` |
| **SECR-M-005** | NIST SP 800-53 Rev.5 `AU-2`, `AU-6`, `AU-12`, `SI-4`; PCI DSS v4.0 `Req 10`; ISO/IEC 27001:2022 `A.8.15`, `A.8.16`; HIPAA `164.312(b)`; SOC 2 `CC7.2` |

## Required actions

### Required controls — source: mandards

1. **Make the protected-branch gate non-bypassable**
   - Repository administrators must protect `main` and `master` and block direct pushes under **REPO-M-001**.
   - Require one or more qualified independent reviewers under **REPO-M-002**.
   - Require build, test, SAST, SCA, secret-scan, and applicable policy checks to pass under **REPO-M-003**.
   - Restrict policy-administration privileges so contributors cannot remove or bypass these checks.

2. **Block secrets before merge**
   - Run secret scanning on every pull request and commit under **SECR-M-001**.
   - Configure the scanner as a required status check under **REPO-M-003**.
   - On detection, block the build, invalidate the credential, remove it from code and relevant history, and replace it with a vault reference.

3. **Prevent secret persistence in CI/CD**
   - Mask sensitive variables and prohibit commands that print secrets under **SECR-M-002** and **SECR-M-005**.
   - Scan logs, artifacts, working directories, and container images; fail the build when an unredacted or embedded secret is found.
   - Clean temporary files and shell history during runner teardown.

4. **Eliminate long-lived pipeline credentials**
   - Use OIDC, managed identities, STS, or equivalent temporary credential exchange under **SECR-M-003** and **SECR-M-004**.
   - Enforce the prescribed TTL limits and automatically revoke credentials that exceed rotation deadlines.
   - Log credential creation, rotation, expiry, and revocation.

5. **Establish change traceability**
   - Require each pull request to reference a valid user story, change, or defect under **REPO-M-004**.
   - Prevent merge where the work item is missing or invalid.

6. **Restrict build inputs**
   - Maintain an approved registry allowlist under **REPO-M-005**.
   - Lint Dockerfiles and pipeline definitions and fail builds that reference unapproved registries.

7. **Gate repository access by secure-coding competence**
   - Validate the contributor’s language-relevant training before granting production-repository write access under **REPO-M-006**.
   - Enforce the 80% threshold, annual renewal, access revocation when expired, and a required training-status check before merge.

### Implementation guidance — source: knowledge

**VeriFy-IS-RMP-001**, *10.3 InfoSec – Release Management & CI/CD Pipelines*  
Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688  
Mapped mandards include **SECR-M-002** together with `ART-M-001`, `ART-M-002`, `GOV-G-006`, `INTEG-M-002`, `LOG-M-003`, `PIPE-M-001`, `PIPE-M-012`, and `SIGN-M-001`.

Its “Release Management and Pipeline Guardrails” section directs teams to:

- Enforce repository least privilege, commit authenticity, secret prevention, pull-request reviews, and CI checks.
- Route dependency acquisition through approved repositories and corporate policy enforcement.
- Keep publication credentials in secret stores and prohibit hardcoded credentials.
- Use approved base-image registries, scan images before publication, and sign production-destined images.
- Record any non-compliance formally as a deviation with technical justification in the SAF pack.

The document is not currently mapped through `mandard_refs` to the **REPO-M** controls. Therefore, its repository instructions are supporting guidance, not the authoritative source of the **REPO-M** requirements. No repository-specific mapped knowledge document was found for this point.

## Evidence for audit

Retain the following evidence per repository:

- Export or API result showing protected branches, blocked direct pushes, required reviewers, and mandatory status checks.
- Sample merged pull request showing independent approval, linked work item, and successful required checks.
- Secret-scanning configuration and successful scan reports for source, history, logs, artifacts, and images.
- Failed-pipeline evidence demonstrating that a seeded test secret is blocked.
- CI log showing masked values and runner cleanup without retaining credentials.
- OIDC or managed-identity trust configuration, credential TTL policy, rotation records, and revocation logs.
- Registry allowlist policy and a test showing an unapproved registry reference is rejected.
- Contributor training result, assessment score, expiry date, access decision, and training-gate result.
- Approved deviation record where any control cannot be implemented.

## Assumptions and limits

No repository, branch policy, pipeline, secret store, registry allowlist, identity configuration, training record, or audit artefact was inspected. Compliance therefore remains unverified until the listed evidence is produced and tested.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |
| [**PIPE-M-012**](https://verify.example-org.internal/?id=PIPE-M-012) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); NIST_CSF (PR.PS-06); +8 more |
| [**REPO-M-001**](https://verify.example-org.internal/?id=REPO-M-001) | Medium | Repository | COBIT_2019 (BAI03.03, BAI06.01); ISO_27001 (A.8.25, A.8.31, A.8.32); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, SA-15); NIST_SSDF (PS.1.1, PS.2.1, PW.4.1); OWASP_SAMM (Implementation: Secure Deployment); +2 more |
| [**REPO-M-002**](https://verify.example-org.internal/?id=REPO-M-002) | Critical | Repository | COBIT_2019 (BAI03.03, BAI06.01); ISO_27001 (A.5.3, A.8.25, A.8.31); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, SA-15); NIST_SSDF (PS.1.1, PS.2.1, PW.4.1); OWASP_SAMM (Implementation: Secure Deployment); +2 more |
| [**REPO-M-003**](https://verify.example-org.internal/?id=REPO-M-003) | Critical | Repository | COBIT_2019 (BAI03.03, BAI06.01, BAI07); ISO_27001 (A.8.25, A.8.31, A.8.32); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, SA-15); NIST_SSDF (PS.1.1, PS.2.1, PW.4.1); OWASP_SAMM (Implementation: Secure Deployment); +2 more |
| [**REPO-M-004**](https://verify.example-org.internal/?id=REPO-M-004) | High | Repository | CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, DSS02.01); ISO_27001 (A.5.24, A.5.26, A.8.16); NIST_CSF (DE.AE-02, DE.CM-01, PR.PS-06); NIST_SP_800_53 (AC-3, AU-6, CM-3); NIST_SSDF (PS.1.1, PS.2.1, PW.4.1); +3 more |
| [**REPO-M-005**](https://verify.example-org.internal/?id=REPO-M-005) | High | Repository | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-20); ISO_27001 (A.5.19, A.5.21, A.8.25); NIST_800_190 (4.2); +11 more |
| [**REPO-M-006**](https://verify.example-org.internal/?id=REPO-M-006) | Medium | Repository | CIS_CONTROLS (CIS 14, CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-31); HIPAA (164.308, 164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.6.3); +11 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
| [**SECR-M-002**](https://verify.example-org.internal/?id=SECR-M-002) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**SECR-M-003**](https://verify.example-org.internal/?id=SECR-M-003) | High | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); MITRE_ATT&CK (M1039); +12 more |

Showing 15 of 18 cited mandards.

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