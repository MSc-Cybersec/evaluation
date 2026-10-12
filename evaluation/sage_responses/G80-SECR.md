# G80-SECR

## Question
What evidence demonstrates end-to-end secrets governance compliance?

## Sage response

## Bottom line

End-to-end secrets governance is demonstrated by a traceable evidence chain covering source control, CI/CD execution, approved secret storage, credential issuance and rotation, build artefacts, monitoring, and remediation. The minimum defensible pack must prove that secrets are blocked before repository entry, never exposed in logs or artefacts, obtained through short-lived mechanisms, rotated or revoked when required, and continuously audited. Without this evidence, credential compromise may remain persistent and unauditable, creating direct exposure to production systems and data.

## Risk and impact

The secrets-management domain contains four **Critical** and one **High** Mandard. Failure can expose production credentials through repositories, retained pipeline logs, build images, working directories, or long-lived automation keys; the resulting impact includes unauthorized access, data compromise, supply-chain intrusion, and inability to reconstruct or prove control operation.

An audit should not accept a policy or vault screenshot alone. It should require evidence that preventive, detective, and corrective controls operated across representative repositories, pipelines, environments, and credentials during the audit period.

## Governing mandards

| Mandard | Title | Risk | Required outcome |
|---|---|---:|---|
| **SECR-M-001** | No Hardcoded Secrets | Critical | Per **SECR-M-001**: high-confidence secret findings in source or configuration must fail the build; exposed secrets must be invalidated and moved to an approved vault. |
| **SECR-M-002** | Prevent Secret Exposure in CI/CD Logs and History | Critical | Per **SECR-M-002**: pipeline logs, command history, working directories, and container images must not retain secrets; scans must fail the build when secrets are detected. |
| **SECR-M-004** | Short-Lived Credentials & Rotation | Critical | Per **SECR-M-004**: production automation must use short-lived credentials or regularly rotated credentials; long-lived production automation secrets are prohibited. |
| **SECR-M-005** | No Secrets in Build Logs | Critical | Per **SECR-M-005**: CI output must mask or redact credentials, and automated log scanning must identify and block exposed secrets. |
| **SECR-M-003** | Enforce Temporary Credentials and Credential Rotation in CI/CD | High | Per **SECR-M-003**: pipelines must use temporary credential exchange such as OIDC; interactive credentials have a maximum TTL of 15 minutes and automated credentials one hour. Remaining CI/CD service-account credentials must rotate at least every 90 days, with overdue credentials automatically revoked. |

## Framework mapping

The following principal mappings were returned by the SAGF catalogue:

| Mandard | Returned framework mappings |
|---|---|
| **SECR-M-001** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-2, AC-3, AC-4, AC-6, AC-7, SI-4, AU-6, SR-3, SR-4, SA-12 |
| **SECR-M-003** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-4, AC-7, SC-8, AU-2 |
| **SECR-M-004** | NIST SP 800-53 Rev. 5: IA-5, SC-12, SR-3, SR-4, SA-12; ISO/IEC 27001:2022: A.5.17, A.5.19, A.5.21, A.8.24, A.8.30; SOC 2: CC6.1; OWASP SAMM 2.0: Implementation—Secure Build; OWASP Cheat Sheet Series: Secrets Management; SLSA: L1, L2 |
| **SECR-M-005** | NIST SP 800-53 Rev. 5: AU-2, AU-6, AU-12, SI-4, IA-5, SC-12, SR-3, SR-4, SA-12; PCI DSS v4.0: Requirement 10; ISO/IEC 27001:2022: A.5.17, A.5.19, A.5.21, A.8.15, A.8.16, A.8.24, A.8.30; HIPAA: 164.312(b); SOC 2: CC6.1, CC7.2 |

## Required actions

1. **Block secrets throughout source-control history — Application and DevSecOps owners**
   - Enable secret scanning on every commit or pull request.
   - Configure high-confidence findings as mandatory pipeline failures.
   - Scan the repository’s full history, not only the current branch.
   - For every confirmed exposure, retain proof of immediate invalidation, history remediation where applicable, vault migration, and issue closure.
   - Per **SECR-M-001**, detection without build enforcement and credential invalidation is insufficient.

2. **Prove approved runtime retrieval — Platform and IAM owners**
   - Maintain an inventory linking each secret or credential to its owner, consuming workload, environment, approved secret store, access policy, rotation method, and current status.
   - Retain vault configuration exports showing access policies and audit logging.
   - Retain workload configuration showing secret references or runtime injection without recording secret values.
   - The release guardrail prescribes secure-vault injection and publication credentials held in secret stores: **VeriFy-IS-RMP-001**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688), mapped to **SECR-M-002** and other pipeline Mandards.

3. **Eliminate secret exposure from pipelines and artefacts — CI/CD owner**
   - Enable masking and redaction for pipeline variables.
   - Scan completed logs, generated artefacts, filesystems, and container images.
   - Fail the pipeline before registry publication when a secret is detected.
   - Clear shell history and remove temporary credential material during teardown.
   - Retain negative scan results and a controlled positive test showing that an injected test credential is redacted and blocks the build.
   - Per **SECR-M-002** and **SECR-M-005**, a successful build with an unredacted secret is a control failure.

4. **Use temporary credentials and prove their lifetime — IAM and Cloud Platform owners**
   - Replace static pipeline keys with OIDC, managed identities, STS role assumption, or an equivalent temporary exchange.
   - Export trust relationships, token TTL settings, workload identity bindings, and sampled token issuance records.
   - Confirm the limits prescribed by **SECR-M-003**: no more than 15 minutes for interactive credentials and one hour for automated credentials.
   - Per **SECR-M-004**, long-lived production automation secrets are prohibited.

5. **Operate rotation and revocation controls — Secret owner and IAM operations**
   - Produce an inventory-based credential-age report.
   - Retain rotation history, failed-rotation alerts, and proof that overdue credentials are automatically revoked.
   - For remaining CI/CD service-account credentials and API keys, demonstrate rotation at least every 90 days as required by **SECR-M-003**.
   - Test emergency revocation and retain the test result, approval, execution timestamps, and downstream validation.

6. **Centralize and protect audit evidence — SOC and Platform owners**
   - Forward secret-access, policy-change, issuance, rotation, revocation, denial, and pipeline secret-detection events to centralized logging or SIEM.
   - Use synchronized timestamps and immutable or access-restricted storage so events can be correlated from code change through deployment.
   - For Confidential and Highly Confidential classifications, the audit guardrail calls for transactional and administrative logs across architectural layers, SIEM where applicable, centralized logging, seven-year retention, and non-repudiation: **VeriFy-AUD-002**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664), mapped to **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, **DB-M-005**, **DATA-M-002**, **MON-M-001**, and **GOV-G-006**.

7. **Record and govern exceptions — Risk owner and Security Architecture**
   - Record every non-compliant repository, static credential, unsupported workload, scanner suppression, or failed rotation as a formal deviation.
   - Include scope, technical justification, compensating controls, accountable risk owner, approval, expiry date, and remediation plan in the SAF pack.
   - The retrieved release, logging, and database-authentication guardrails require non-compliance to be formally recorded as a deviation:
     - **VeriFy-IS-RMP-001**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688)
     - **VeriFy-AUD-002**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664)
     - **VeriFy-AUTH-INT-DB-001**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/655459253), mapped to **SECR-M-001** for database authentication context.

## Evidence for audit

| Lifecycle stage | Minimum evidence | Acceptance test |
|---|---|---|
| Governance and inventory | Approved secrets standard; secret and credential inventory; named owners; application/environment mapping; exception register | Inventory reconciles to deployed workloads, CI/CD variables, service identities, and vault records. |
| Source and repository history | Scanner configuration; branch protection; pre-commit or PR gate; current and historical scan reports; failed-build sample | A controlled test secret is detected and prevents merge or build. No unresolved high-confidence findings exist without approved deviations. |
| Approved storage | Vault configuration export; secret metadata without values; encryption and access-policy configuration; backup/recovery evidence where applicable | Production workloads reference an approved secret store rather than source code or plaintext configuration. |
| Access and retrieval | Least-privilege policy exports; workload identity bindings; vault access logs; periodic access-review approvals | Sampled applications can retrieve only authorized secret paths; denied access generates an auditable event. |
| CI/CD credentials | OIDC or managed-identity trust configuration; token TTL settings; token issuance logs; confirmation that static pipeline keys are absent | Sampled credentials expire within the **SECR-M-003** limits and cannot be reused after expiry. |
| Build logs and workspaces | Masking configuration; completed log-scan reports; redaction test; agent teardown records; workspace inspection | Test values appear as redacted; no plaintext credential remains in logs, shell history, caches, or working directories. |
| Build artefacts and images | Secret-scan reports for packages, images, layers, and registry-bound artefacts; pipeline gate result | A positive finding blocks publication or deployment. |
| Rotation and revocation | Credential-age dashboard; rotation schedule; completed rotation logs; failed-rotation alerts; automatic-revocation record | No CI/CD credential exceeds the **SECR-M-003** rotation deadline unless covered by a current approved deviation. |
| Monitoring and response | SIEM ingestion configuration; alert rules; sampled correlated events; incident tickets; credential invalidation records | Access, change, rotation, revocation, and detection events can be reconstructed end to end with consistent timestamps. |
| Exceptions and assurance | SAF deviation records; risk acceptance; compensating-control evidence; expiry and remediation tracking; periodic control-owner attestation | Every exception is approved, time-bound, owned, and traceable to closure or renewal. |

A strong audit sample should connect a single production deployment through: commit and scan result → pipeline identity issuance → vault retrieval event → masked build log → artefact scan → deployment → rotation or expiry record → centralized audit trail. Secret values must never be included in the evidence pack.

## Assumptions and limits

No repository, pipeline, vault, identity platform, SIEM configuration, credential inventory, scan result, or exception record was inspected. Compliance therefore cannot be concluded from this response; the table defines the evidence needed to substantiate it. Other retrieved knowledge documents were set aside because they concerned adjacent application, certificate, infrastructure, or data guardrails rather than direct secrets-governance evidence.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |
| [**SECR-M-002**](https://verify.example-org.internal/?id=SECR-M-002) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**SECR-M-003**](https://verify.example-org.internal/?id=SECR-M-003) | High | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.19); MITRE_ATT&CK (M1039); +12 more |
| [**SECR-M-004**](https://verify.example-org.internal/?id=SECR-M-004) | Critical | Secrets Management | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); MITRE_ATT&CK (M1039); NIST_CSF (GV.SC-01, ID.RA-09, PR.PS-06); +9 more |
| [**SECR-M-005**](https://verify.example-org.internal/?id=SECR-M-005) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CWE (CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.17, A.5.19, A.5.21); +12 more |

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