# G21-CONT

## Question
Which controls must be proven before promoting a new container image?

## Sage response

## Bottom line

A new container image must not be promoted unless the pipeline proves, against the immutable image digest, that it has no High or Critical CVEs, contains no embedded secrets, runs as non-root, has a published machine-readable SBOM, and carries a valid signature from an approved signer. Production promotion must also pass an auditable security gate and authorized manual approval; any failed or unavailable control requires a formally approved, unexpired deviation before release.

## Risk and impact

The principal exposure is software-supply-chain compromise: a vulnerable, tampered, secret-bearing, or over-privileged image could gain production access and expose credentials, customer data, or deployment infrastructure.

| Priority | Exposure if not proven |
|---|---|
| Critical | Known exploitable vulnerabilities, embedded credentials, unsigned or substituted images, absent component inventory, or compromised CI workflows |
| High | Root execution, unauthorized registry changes, incomplete artifact integrity analysis, or ungoverned control exceptions |

The release-management guidance additionally requires container images to be scanned before internal-registry publication and scanned and signed around publication. For production-destined images, it specifies Cosign signing and requires the image to run as non-root. Source: **VeriFy-IS-RMP-001**, §2, mapped to **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, and **SIGN-M-001** — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688).

## Governing mandards

### Mandatory pre-promotion gates

| Mandard | Title | Risk | Proof required before promotion |
|---|---|---:|---|
| **CONT-M-001** | No Critical Container CVEs | Critical | Final image scan passes with no High or Critical CVEs; Dockerfile hardening lint also passes |
| **CONT-M-003** | No Secrets in Container Images | Critical | Image-layer secret scan returns no plaintext secrets, keys, or credentials |
| **ART-M-002** | Generate SBOM | Critical | Complete CycloneDX or SPDX SBOM is generated and published as a build artifact |
| **SIGN-M-001** | Enforce Artifact Code Signing | Critical | Image is signed; deployment validates the signature and blocks validation failure |
| **SECR-M-002** | Prevent Secret Exposure in CI/CD Logs and History | Critical | Image and completed pipeline logs pass secret scanning; no secrets remain in the working directory or history |
| **PIPE-M-001** | Secure CI/CD Pipeline Configuration | Critical | Version-controlled security stages passed; production or critical-environment promotion has authorized manual approval |
| **PIPE-M-012** | CI/CD Workflow Least Privilege and Safe Triggers | Critical | Workflow analyzer passes; tokens and triggers are least-privileged and safe; critical deployment approval is recorded |
| **ART-M-001** | Artifact Signing & Verification | High | Production image signature is verified and final artifact composition analysis detects no secrets, unexpected components, or integrity violations |
| **CONT-M-002** | No Root User in Containers | High | Dockerfile lint proves `USER` exists and is not `root` |
| **INTEG-M-002** | Secure Artifact Repository | High | Target registry enforces authentication, authorization, and audit logging for access and modification |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | High | CI/CD audit logs are forwarded to the SIEM and required detection and alerting rules are active |
| **GOV-G-006** | Security Deviation and Exception Management | High | Any override has an independently approved, documented, owned, compensated, and unexpired deviation |

Per **CONT-M-001**: the build must fail when the final image contains High or Critical CVEs.  
Per **CONT-M-003** and **SECR-M-002**: embedded secrets or secrets exposed in pipeline logs must fail the build.  
Per **SIGN-M-001** and **ART-M-001**: production images must be signed and their signatures verified before deployment.  
Per **ART-M-002**: the pipeline must generate and publish a complete machine-readable SBOM.  
Per **PIPE-M-001** and **PIPE-M-012**: promotion must occur through an auditable security pipeline, with authorized manual approval for production or other critical environments.

### Complete container-security domain

The container catalogue also contains the following deployment and runtime controls. Their applicability must be assessed for the target platform, but their titles alone do not establish that they are image-publication gates.

| Mandard | Title | Risk |
|---|---|---:|
| **CONT-M-001** | No Critical Container CVEs | Critical |
| **CONT-M-002** | No Root User in Containers | High |
| **CONT-M-003** | No Secrets in Container Images | Critical |
| **CONT-M-004** | Mandatory Sidecar Proxy Injection for Zero Trust | Critical |
| **CONT-M-005** | mTLS Certificate Management & Rotation | Critical |
| **CONT-M-006** | Network Policy & Sidecar Traffic Enforcement | Critical |
| **CONT-M-007** | Sidecar Security Logging & Telemetry | High |
| **CONT-M-008** | Zero-Trust Policy Enforcement via Sidecar | Critical |
| **CONT-M-009** | Container Runtime Security Context Hardening | High |
| **CONT-M-010** | Container Runtime Isolation, Profiles and Resource Limits | High |

## Framework mapping

The following are confirmed mappings returned by the catalogue; this is not represented as an exhaustive list because portions of the mapping results were truncated.

| Mandard | Confirmed framework mappings |
|---|---|
| **CONT-M-001** | NIST SP 800-53 Rev.5: `CM-2`, `CM-6`, `CM-7`, `SI-4`, `AU-6`, `SR-3`, `SR-4`, `SA-12`, `SA-22` |
| **CONT-M-002** | NIST SP 800-53 Rev.5: `AC-2`, `AC-3`, `AC-4`, `AC-6`, `CM-2`, `CM-6`, `CM-7`; PCI DSS v4.0: `Req 7`, `Req 10` |
| **CONT-M-003** | NIST SP 800-53 Rev.5: `CM-2`, `CM-6`, `CM-7`, `IA-5`, `SC-12`; ISO/IEC 27001:2022: `A.5.17`, `A.8.9`, `A.8.24`, `A.8.27`; CIS Controls v8: `CIS 4` |
| **ART-M-002** | NIST SP 800-53 Rev.5: `AU-2`, `AU-6`, `AU-12`, `SR-3`, `SR-4`, `SA-12`; PCI DSS v4.0: `Req 10`; ISO/IEC 27001:2022: `A.8.15`, `A.8.16`, `A.5.19`, `A.5.21`, `A.8.30` |
| **SIGN-M-001** | NIST SP 800-53 Rev.5: `SR-3`, `SR-4`, `SA-12`, `SA-22` |
| **PIPE-M-012** | NIST SP 800-53 Rev.5: `AC-2`, `AC-3`, `AC-4`, `AC-6`, `CM-3`, `IA-5`, `SA-15`, `SC-12`; PCI DSS v4.0: `Req 7`; ISO/IEC 27001:2022: `A.5.3`, `A.5.15`, `A.5.17`, `A.5.18`, `A.8.2`, `A.8.3`, `A.8.24`, `A.8.25`, `A.8.31`, `A.8.32` |
| **GOV-G-006** | NIST SP 800-53 Rev.5: `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022: `A.5.1`, `A.5.35`; NIST CSF 2.0: `GV.RM`, `GV.OV`, `ID.RA` |

## Required actions

1. **Block vulnerable images — Critical**  
   **Owner:** Development and DevSecOps  
   Per **CONT-M-001**, scan the final image—not only source dependencies—and fail promotion on any High or Critical CVE. Run Dockerfile hardening lint for a non-root `USER`, pinned base image and package versions, `COPY` preference, and prohibited remote-script piping.

2. **Block secrets — Critical**  
   **Owner:** Development and DevSecOps  
   Per **CONT-M-003** and **SECR-M-002**, scan every image layer and completed pipeline logs for credentials or sensitive material. Rotate any exposed secret, remove it from all layers, rebuild the image, and inject secrets only at runtime.

3. **Generate the inventory — Critical**  
   **Owner:** Build engineering  
   Per **ART-M-002**, generate and publish a complete CycloneDX or SPDX SBOM tied to the promoted image digest.

4. **Sign and verify the exact digest — Critical/High**  
   **Owner:** Platform engineering  
   Per **SIGN-M-001** and **ART-M-001**, sign the immutable image digest with an approved identity or key. Verify the signature, signer, digest, and final artifact composition at the promotion gate; configure deployment admission control to reject missing or invalid signatures.

5. **Enforce pipeline integrity and approval — Critical**  
   **Owner:** DevOps and release management  
   Per **PIPE-M-001** and **PIPE-M-012**, require all gates through version-controlled pipeline configuration, scan the workflow definition, use least-privileged tokens and safe triggers, prevent pipeline bypass, and require an authorized manual approval for production or critical environments.

6. **Verify non-root execution — High**  
   **Owner:** Development  
   Per **CONT-M-002**, fail Dockerfile lint when `USER` is absent or set to `root`.

7. **Protect the registry and audit trail — High**  
   **Owner:** Platform and security operations  
   Per **INTEG-M-002**, restrict image publication and retrieval using authenticated, least-privileged identities and retain push/pull audit records. Per **LOG-M-003**, forward pipeline audit events to the SIEM and alert on gate bypasses, signature failures, unauthorized pipeline changes, or secret detections.

8. **Govern exceptions — High**  
   **Owner:** Risk owner and independent approval authority  
   Per **GOV-G-006**, do not use a manual override as a substitute for evidence. Promotion may proceed exceptionally only with an approved, unexpired deviation containing the affected control, technical justification, residual-risk owner, compensating controls, and expiry.

**Implementation guidance:** **VeriFy-IS-RMP-001**, §2 states that approved base images should be sourced from `registry.example-org.internal`, images should pass vulnerability scanning before internal-registry publication, production images should be signed using Cosign, images should run as non-root, and scanning/signing should occur around publication. It is mapped to **ART-M-001**, **ART-M-002**, **GOV-G-006**, **INTEG-M-002**, **LOG-M-003**, **PIPE-M-001**, **PIPE-M-012**, **SECR-M-002**, and **SIGN-M-001** — [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688).

## Evidence for audit

The release record should retain the following against one immutable digest:

| Evidence | Acceptance condition |
|---|---|
| Image vulnerability report | Correct digest scanned; zero High and Critical CVEs |
| Dockerfile lint report | Required hardening passes; non-root `USER` confirmed |
| Image secret-scan report | No embedded secrets in any layer |
| Pipeline log secret-scan result | No plaintext secrets; successful cleanup recorded |
| SBOM | Complete CycloneDX or SPDX file published and linked to the digest |
| Signature and verification output | Valid signature from approved signer for the same digest |
| Composition/integrity analysis | No exposed secrets, unexpected components, or integrity violation |
| Pipeline configuration result | Version-controlled definition and workflow analyzer passed |
| Promotion approval | Authorized approver, timestamp, target environment, and digest |
| Registry evidence | Authenticated publication record and registry audit event |
| SIEM evidence | Log-ingestion status and active CI/CD detection rules |
| Deviation record, if applicable | Independent approval, risk owner, compensating controls, and future expiry |

## Assumptions and limits

“Promotion” is interpreted as moving an image to a higher-trust environment or production, not merely assigning another tag. Evidence should be digest-bound because mutable tags do not prove that the scanned, signed, approved, and deployed image is identical.

The implementation document applies to on-premises and Azure environments in the SA and NAR regions. Broader application, endpoint, data, and infrastructure governance documents returned by the search were set aside because they did not directly define the container-image promotion gate.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**ART-M-001**](https://verify.example-org.internal/?id=ART-M-001) | High | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI03.03); CSA_CCM (IVS: Infrastructure & Virtualization Security, STA); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.17, A.5.18); +13 more |
| [**ART-M-002**](https://verify.example-org.internal/?id=ART-M-002) | Critical | Artifact Management | CIS_CONTROLS (CIS 15, CIS 2, CIS 8); COBIT_2019 (APO10.01, APO10.04, BAI03.03); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); MITRE_ATT&CK (M1045); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); +10 more |
| [**CONT-M-001**](https://verify.example-org.internal/?id=CONT-M-001) | Critical | Container Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 4); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.5.19, A.5.21, A.8.16); MITRE_ATT&CK (M1022, M1028, M1039); NIST_800_190 (4.1); +9 more |
| [**CONT-M-002**](https://verify.example-org.internal/?id=CONT-M-002) | High | Container Security | CIS_CONTROLS (CIS 4, CIS 6, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.18, A.8.15); +11 more |
| [**CONT-M-003**](https://verify.example-org.internal/?id=CONT-M-003) | Critical | Container Security | CIS_CONTROLS (CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); ISO_27001 (A.5.17, A.8.24, A.8.27); MITRE_ATT&CK (M1022, M1028, M1039); +5 more |
| [**CONT-M-004**](https://verify.example-org.internal/?id=CONT-M-004) | Critical | Container Security | CIS_CONTROLS (CIS 3, CIS 4, CIS 5); COBIT_2019 (BAI09.01, DSS05.02, DSS05.04); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285, CWE-327); GDPR (Article 32); HIPAA (164.312(a)(1), 164.312(a)(2)(iv), 164.312(b)); +11 more |
| [**CONT-M-005**](https://verify.example-org.internal/?id=CONT-M-005) | Critical | Container Security | CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-327, CWE-798); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +10 more |
| [**CONT-M-006**](https://verify.example-org.internal/?id=CONT-M-006) | Critical | Container Security | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.20, A.8.22, A.8.27); MITRE_ATT&CK (M1022, M1028, M1039); NIST_800_190 (4.4); +5 more |
| [**CONT-M-007**](https://verify.example-org.internal/?id=CONT-M-007) | High | Container Security | CIS_CONTROLS (CIS 17, CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS02.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv), 164.312(b)); +13 more |
| [**CONT-M-008**](https://verify.example-org.internal/?id=CONT-M-008) | Critical | Container Security | CIS_CONTROLS (CIS 4, CIS 6, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.18, A.8.15); +10 more |
| [**CONT-M-009**](https://verify.example-org.internal/?id=CONT-M-009) | High | Container Security | CIS_CONTROLS (CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.27, A.8.9); MITRE_ATT&CK (M1022, M1028, M1039); NIST_800_190 (4.4); +4 more |
| [**CONT-M-010**](https://verify.example-org.internal/?id=CONT-M-010) | High | Container Security | CIS_CONTROLS (CIS 4, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (IVS: Infrastructure & Virtualization Security); ISO_27001 (A.8.16, A.8.27, A.8.9); MITRE_ATT&CK (M1022, M1028, M1039); NIST_800_190 (4.4); +9 more |
| [**INTEG-M-002**](https://verify.example-org.internal/?id=INTEG-M-002) | High | Integrity Verification | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); +11 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**PIPE-M-001**](https://verify.example-org.internal/?id=PIPE-M-001) | Critical | Pipeline Security | CIS_CONTROLS (CIS 6); COBIT_2019 (BAI03.03, BAI06.01); CSA_CCM (CCC); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +10 more |

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