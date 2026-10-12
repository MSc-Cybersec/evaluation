# G42-DEP

## Question
What governance controls should block risky third-party package updates?

## Sage response

## Bottom line

Third-party package updates should be blocked automatically when they introduce Critical or High vulnerabilities, prohibited licenses, unapproved components, unpinned inputs, missing SBOMs, or unverifiable artifacts. The release process must prevent bypass through protected branches, mandatory security stages, isolated builds, and independently approved, time-limited deviations. Approve a centrally managed dependency policy and make its checks mandatory for merge, artifact publication, and production deployment.

## Risk and impact

The principal exposure is **Critical**: malicious or vulnerable dependencies can execute during build, compromise credentials, alter artifacts, or enter production. Additional **High** risks include unassessed suppliers, compromised package repositories, mutable CI actions, and unauthorised exceptions; license violations can also create material intellectual-property and contractual exposure.

The minimum blocking decisions are:

| Decision point | Block when | Governing Mandard |
|---|---|---|
| Pull request or merge | Critical or High dependency vulnerability detected | **SCA-M-001** |
| Pull request or merge | Dependency has a non-approved license | **SCA-M-002** |
| Dependency admission | Required third-party risk assessment or approval is missing | **SUPPLY-M-001** |
| Build | Dependency lockfile is missing, changed unexpectedly, or cannot resolve from approved cached inputs | **PIPE-M-008** |
| Build | Public-internet access or unexpected egress occurs | **PIPE-M-008** |
| Pipeline change | Required security stages, workflow analysis, review, or approval gates are absent | **PIPE-M-001** |
| CI workflow update | Third-party action is not pinned to a verified full commit SHA or approved publisher | **PIPE-M-013** |
| Artifact publication | Complete machine-readable SBOM was not generated and published | **ART-M-002** |
| Deployment | Artifact is unsigned, signature verification fails, or binary composition analysis fails | **ART-M-001**, **SIGN-M-001** |
| Control override | Approved, unexpired deviation with an independent risk owner is absent | **GOV-G-006** |

## Governing Mandards

### Primary package-update controls

| Mandard | Title | Risk |
|---|---|---:|
| **SCA-M-001** | No Critical CVEs | Critical |
| **SCA-M-002** | Approved Licenses | Critical |
| **SUPPLY-M-001** | Third-Party Risk Assessment | High |
| **SUPPLY-M-002** | Secure Development Platform and Tooling Integrity | High |
| **ART-M-001** | Artifact Signing & Verification | High |
| **ART-M-002** | Generate SBOM | Critical |
| **SIGN-M-001** | Enforce Artifact Code Signing | Critical |

Per **SCA-M-001**: the build must fail if SCA detects a Critical or High severity CVE in a third-party dependency.

Per **SCA-M-002**: the build must fail when a dependency has a non-approved license.

Per **SUPPLY-M-001**: components above the defined risk threshold require a documented assessment before production. Open-source assessment must consider maintenance activity, maturity, release stability, contributor sufficiency, dependency freshness, security testing, vulnerability response, and license suitability.

Per **ART-M-002**: every build pipeline must generate and publish a complete machine-readable SBOM.

Per **ART-M-001** and **SIGN-M-001**: production artifacts must be signed and signature verification failure must block deployment; **ART-M-001** additionally requires producer and consumer binary composition analysis.

### Pipeline controls returned for this domain

| Mandard | Title | Risk |
|---|---|---:|
| **PIPE-M-001** | Secure CI/CD Pipeline Configuration | Critical |
| **PIPE-M-002** | Pre-Commit Hooks Enforced | Critical |
| **PIPE-M-003** | Use Ephemeral Build Agents | Critical |
| **PIPE-M-004** | Pin Build Tool Versions | Medium |
| **PIPE-M-005** | Vulnerability Scans for Non-Prod | Medium |
| **PIPE-M-006** | Implement Plugin and Integration Governance in CI/CD Platforms | High |
| **PIPE-M-007** | Sequential Security Pipeline Execution | High |
| **PIPE-M-008** | Hermetic Builds — Isolated Build Environment | Critical |
| **PIPE-M-009** | Restrict Build Parameters to Whitelisted Values | Medium |
| **PIPE-M-010** | Maintain Inventory of Build Tools and Versions | High |
| **PIPE-M-011** | Enforce Build Immutability and Tamper-Proofing | High |
| **PIPE-M-012** | CI/CD Workflow Least Privilege and Safe Triggers | Critical |
| **PIPE-M-013** | Pin and Verify Third-Party CI Actions and Reusable Workflows | High |
| **PIPE-M-014** | CI Runner Hardening and Cache Poisoning Prevention | High |

Per **PIPE-M-001**: security stages must run before promotion, pipeline configuration must be version-controlled and auditable, workflow analysis must be a required merge check, and critical-environment deployments require authorised manual approval.

Per **PIPE-M-008**: builds must be isolated from the public internet, use pre-fetched dependencies and lockfiles, reject unexpected egress, and run on ephemeral environments.

Per **PIPE-M-012**: workflows must use least-privilege tokens, safe triggers, immutable references for untrusted code, disabled credential persistence, and manual approval for critical deployments.

Per **PIPE-M-013**: third-party CI actions and reusable workflows must be pinned to verified full commit SHAs, sourced from reviewed publishers, and updated with a release-age cooldown.

Per **PIPE-M-004**: build tools must use specific known-good versions rather than mutable versions such as `latest`.

### Supporting governance controls

| Mandard | Title | Risk |
|---|---|---:|
| **GOV-G-006** | Security Deviation and Exception Management | High |
| **INTEG-M-002** | Secure Artifact Repository | High |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High |
| **SECR-M-002** | Prevent Secret Exposure in CI/CD Logs and History | Critical |

Per **GOV-G-006**: every override must have technical justification, residual-risk ownership, compensating controls, independent approval, and an expiry date.

Per **INTEG-M-002**: npm, Maven, container, and other artifact repositories must enforce authentication, authorization, and audit logging.

## Framework mapping

The following are verified mappings returned by the catalogue; this is a focused subset rather than an exhaustive crosswalk.

| Mandards | Framework controls returned |
|---|---|
| **SCA-M-001**, **SCA-M-002**, **SUPPLY-M-001**, **SUPPLY-M-002**, **PIPE-M-004**, **PIPE-M-008**, **PIPE-M-013**, **ART-M-001**, **ART-M-002**, **SIGN-M-001** | NIST SP 800-53 Rev. 5: **SR-3 Supply Chain Controls and Processes**, **SR-4 Provenance**, **SA-12 Supply Chain Protection** |
| **SCA-M-002**, **SUPPLY-M-002**, **PIPE-M-004**, **PIPE-M-013**, **ART-M-002** | ISO/IEC 27001:2022: **A.5.19 Information security in supplier relationships**, **A.5.21 Managing information security in the ICT supply chain** |
| **SUPPLY-M-002**, **PIPE-M-013** | OWASP Top 10:2025: **A03 Software Supply Chain Failures** |
| **PIPE-M-012** | PCI DSS v4.0: **Requirement 7 Restrict Access by Business Need to Know** |
| **ART-M-002** | PCI DSS v4.0: **Requirement 10 Log and Monitor All Access** |
| **GOV-G-006** | NIST CSF 2.0: **GV.RM**, **GV.OV**, **ID.RA** |
| **GOV-G-006** | SOC 2 Type II: **CC3 Risk Assessment**, **CC5 Control Activities** |

## Required actions

1. **Enforce mandatory SCA merge gates — Application Security and DevOps.**  
   Configure every dependency-update pull request to fail on Critical or High vulnerabilities per **SCA-M-001**, and on non-approved licenses per **SCA-M-002**. Scan direct and transitive dependencies using the resolved dependency graph, not only the manifest.

2. **Force approved, deterministic dependency resolution — Platform Engineering.**  
   Per **PIPE-M-008**, require committed lockfiles, immutable versions or digests, pre-fetched dependencies, ephemeral builders, and no public-internet access during build. Unexpected egress must fail the build.

3. **Route package acquisition through controlled repositories — Platform Engineering.**  
   Per **INTEG-M-002**, require authenticated internal npm, Maven, NuGet, Python, container, or equivalent repositories with RBAC and audit logging.  
   The implementation standard **VeriFy-IS-RMP-001**, mapped to **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, and **SIGN-M-001**, directs teams to route approved public repositories through corporate proxies, block non-approved sources, enforce lockfile integrity and dependency pinning, and restrict arbitrary code execution during resolution. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688

4. **Require approval for new or materially changed components — Product Owner and Security.**  
   Per **SUPPLY-M-001**, block production admission until the required assessment and approval record exist. Updates involving maintainer changes, dormant projects, unstable releases, unexpected ownership changes, or unsuitable licenses should be escalated against the Mandard’s structured assessment criteria.

5. **Generate and compare SBOMs — DevOps.**  
   Per **ART-M-002**, generate CycloneDX or SPDX output for each build and publish it as an immutable artifact. Compare the proposed SBOM with the approved baseline so unexpected additions, removals, or version changes are visible before promotion.

6. **Sign and verify release artifacts — Release Engineering.**  
   Per **ART-M-001** and **SIGN-M-001**, sign packages, binaries, and images after successful validation. Block publication or deployment when the signature, signer identity, digest, or required binary composition analysis is invalid.

7. **Protect automated-update workflows — CI Platform Owner.**  
   Per **PIPE-M-013**, pin third-party actions and reusable workflows to verified full commit SHAs and apply a release-age cooldown. Per **PIPE-M-012**, give dependency-update jobs read-only permissions unless a specific write permission is necessary; do not expose production secrets to untrusted update code.

8. **Prevent gate bypass — Repository Administrators.**  
   Per **PIPE-M-001**, protect release branches, require pull-request review and successful security checks, version-control pipeline definitions, and prevent direct deployment outside the approved pipeline.

9. **Govern exceptions — Risk Owner and independent InfoSec approver.**  
   Per **GOV-G-006**, fail the release unless an override references an approved and unexpired deviation containing the affected Mandard, justification, residual risk, owner, compensating controls, and expiry. Critical or High findings must not be suppressed informally in scanner configuration.

10. **Monitor attempted bypasses — Security Operations.**  
    Per **LOG-M-003**, alert on pipeline modifications, deployment-gate bypasses, signature failures, privilege escalation, and abnormal service-account use.

No knowledge document directly mapped to **SCA-M-001** or **SCA-M-002** was found. Their blocking thresholds and remediation steps above come from the Mandard catalogue; the broader repository and pipeline procedure comes from **VeriFy-IS-RMP-001**.

## Evidence for audit

Retain the following against each dependency update:

- SCA report showing the resolved dependency tree, vulnerability severity, and pass/fail result for **SCA-M-001**.
- License inventory and policy decision for **SCA-M-002**.
- Third-party assessment and component approval record for **SUPPLY-M-001**.
- Protected-branch configuration and mandatory status-check policy for **PIPE-M-001**.
- Lockfile, integrity hash, internal-repository resolution log, and successful egress-denial test for **PIPE-M-008**.
- Workflow analyzer result proving full-SHA pinning and source verification for **PIPE-M-013**.
- Published CycloneDX or SPDX SBOM and comparison report for **ART-M-002**.
- Artifact signature, signer identity, digest, verification result, and binary composition report for **ART-M-001** and **SIGN-M-001**.
- Repository RBAC configuration and immutable access logs for **INTEG-M-002**.
- Approved, independently authorised, unexpired deviation record for any override under **GOV-G-006**.
- SIEM event and alert-test evidence for attempted gate bypasses under **LOG-M-003**.

## Assumptions and limits

The organisation’s current package managers, CI/CD platforms, repository configuration, risk threshold, approved-license list, exception authority, and deployed gate settings were not inspected. The catalogue explicitly defines the vulnerability blocking threshold as Critical or High under **SCA-M-001**; any stricter blocking of Medium or Low findings would require an organisation-specific policy decision.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |
| [**PIPE-M-002**](https://verify.example-org.internal/?id=PIPE-M-002) | Critical | Pipeline Security | COBIT_2019 (BAI03.03, BAI06.01); CWE (CWE-798); ISO_27001 (A.5.17, A.8.24, A.8.25); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, IA-5); NIST_SSDF (PO.1.1, PS.1.1, PS.2.1); +3 more |
| [**PIPE-M-003**](https://verify.example-org.internal/?id=PIPE-M-003) | Critical | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); NIST_CSF (GV.SC-01, ID.RA-09, PR.PS-06); NIST_SP_800_53 (AC-3, CM-3, IA-5); +7 more |
| [**PIPE-M-004**](https://verify.example-org.internal/?id=PIPE-M-004) | Medium | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.19, A.5.21, A.8.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.IR-01); NIST_SP_800_53 (AC-3, CM-2, CM-3); +6 more |
| [**PIPE-M-005**](https://verify.example-org.internal/?id=PIPE-M-005) | Medium | Pipeline Security | CIS_CONTROLS (CIS 12); COBIT_2019 (BAI03.03, BAI06.01); ISO_27001 (A.8.20, A.8.22, A.8.25); NIST_CSF (PR.PS-06); NIST_SP_800_53 (AC-3, AC-4, CM-3); NIST_SSDF (PO.1.1, PS.1.1, PS.2.1); +3 more |
| [**PIPE-M-006**](https://verify.example-org.internal/?id=PIPE-M-006) | High | Pipeline Security | CIS_CONTROLS (CIS 12, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, APO12.01); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.5.19); NIST_CSF (DE.AE-02, DE.CM-01, GV.OC-01); +10 more |
| [**PIPE-M-007**](https://verify.example-org.internal/?id=PIPE-M-007) | High | Pipeline Security | CIS_CONTROLS (CIS 4); COBIT_2019 (BAI03.03, BAI06.01, BAI07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.25, A.8.27, A.8.31); NIST_CSF (PR.IR-01, PR.PS-01, PR.PS-06); NIST_SP_800_53 (AC-3, CA-9, CM-2); +5 more |
| [**PIPE-M-008**](https://verify.example-org.internal/?id=PIPE-M-008) | Critical | Pipeline Security | CIS_CONTROLS (CIS 12, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AC-19, AC-3, AC-4); +10 more |
| [**PIPE-M-009**](https://verify.example-org.internal/?id=PIPE-M-009) | Medium | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-20); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); +11 more |
| [**PIPE-M-010**](https://verify.example-org.internal/?id=PIPE-M-010) | High | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 6); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CWE (CWE-284, CWE-285); EU_AI_ACT (Article 14, Article 15, Article 9); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.18, A.5.19); +16 more |
| [**PIPE-M-011**](https://verify.example-org.internal/?id=PIPE-M-011) | High | Pipeline Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); ISO_27001 (A.5.19, A.5.21, A.8.16); NIST_800_218A (PW.6); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AC-3, AU-6, CM-3); +7 more |

Showing 15 of 24 cited mandards.

Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
## Scoring notes
- actionability: pass (provisional auto-score)
- citation_correctness: pass (provisional auto-score)
- evidence_audit: pass (provisional auto-score)
- framework_mapping: pass (provisional auto-score)
- risk_impact: pass (provisional auto-score)
- bottom_line: pass (provisional auto-score)
- governing_mandards: fail (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass