# G07-ART

## Question
What controls are required for artifact integrity in our build and release chain?

## Sage response

## Bottom line

Artifact integrity requires mandatory controls across the entire build and release chain: secured CI/CD workflows, SBOM generation, artifact scanning, cryptographic signing, controlled repositories, signature verification before deployment, and centralized monitoring. Production deployment must fail closed when an artifact is unsigned, its signature is invalid, its SBOM is missing, required analysis fails, or the release path is bypassed. Engineering and Platform owners should implement these as mandatory pipeline and deployment gates; any temporary exception requires independent, time-bounded approval.

## Risk and impact

The applicable catalogue contains five CRITICAL and four HIGH mandards.

•
Critical exposure: A compromised pipeline could execute attacker-controlled code, leak signing credentials, alter release artifacts, or deploy malicious software as a trusted release.
•
High exposure: An attacker could modify artifacts in a repository, introduce unexpected components after source scanning, bypass release controls, or evade detection.
•
Business impact: Production compromise, widespread supply-chain propagation, loss of release traceability, prolonged vulnerability exposure, operational disruption, and inability to prove software provenance during an audit or incident.
## Governing mandards
Mandard	Title	Risk	Required control
ART-M-002	Generate SBOM	CRITICAL	Per ART-M-002: every build pipeline must generate and publish a complete machine-readable SBOM in a format such as CycloneDX or SPDX.
PIPE-M-001	Secure CI/CD Pipeline Configuration	CRITICAL	Per PIPE-M-001: pipelines must contain explicit security stages before promotion, use version-controlled and auditable pipeline definitions, statically analyze workflow configuration as a required merge check, and require authorized manual approval for critical deployments.
PIPE-M-012	CI/CD Workflow Least Privilege and Safe Triggers	CRITICAL	Per PIPE-M-012: pipeline tokens must default to no permissions, dangerous triggers must be avoided or restricted, untrusted code must be checked out by immutable commit SHA, credential persistence must be disabled, unsafe context interpolation must be prevented, and critical deployments require approval.
SIGN-M-001	Enforce Artifact Code Signing	CRITICAL	Per SIGN-M-001: all deployable artifacts must be digitally signed, and deployment systems must reject missing or invalid signatures.
SECR-M-002	Prevent Secret Exposure in CI/CD Logs and History	CRITICAL	Per SECR-M-002: logs and build workspaces must not retain secrets; logs and container images must be scanned, detected secrets must fail the build, and exposed credentials must be redacted and removed.
ART-M-001	Artifact Signing & Verification	HIGH	Per ART-M-001: production artifacts must be signed and verified before deployment, and the final binary must undergo producer- and consumer-side composition analysis for secrets, unexpected components, and integrity violations.
INTEG-M-002	Secure Artifact Repository	HIGH	Per INTEG-M-002: artifact repositories must enforce authentication, authorization, and audit logging for access and modifications, including push and pull operations.
LOG-M-003	Configure Centralized Log Aggregation and SIEM Alerting for CI/CD	HIGH	Per LOG-M-003: CI/CD audit logs must be centralized, with alerts for unauthorized pipeline changes, gate bypasses, signature failures, secret detection, abnormal deployments, and anomalous service-account use. Detection rules must be version-controlled and tuned at least quarterly.
GOV-G-006	Security Deviation and Exception Management	HIGH	Per GOV-G-006: any control departure must be documented before release, independently approved, assigned to a residual-risk owner, supported by compensating controls, and given a defined expiry date.
## Framework mapping

The following are selected catalogue mappings returned for these mandards; they are not presented as an exhaustive equivalence assessment.

Mandard	Returned framework mappings
ART-M-001	NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, AU-6, IA-5, SI-4, SC-12, SR-3, SR-4, SA-12
ART-M-002	NIST SP 800-53 Rev.5: AU-2, AU-6, AU-12, SI-4, SR-3, SR-4, SA-12, CM-3, SA-15; PCI DSS v4.0: Req 10; ISO/IEC 27001:2022: A.8.15, A.8.16, A.5.19, A.5.21, A.8.30
INTEG-M-002	NIST SP 800-53 Rev.5: IA-2, IA-5, AC-2, AC-3, AC-4, AC-6, AC-7, AU-2, AU-6, AU-12, SI-4, SR-3, SR-4, SA-12, CM-2, CM-7, SC-7
PIPE-M-001	NIST SP 800-53 Rev.5: AC-2, AC-3
PIPE-M-012	NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, IA-5, SC-12, CM-3, SA-15; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.3, A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.24, A.8.25, A.8.31, A.8.32; HIPAA: 164.312(a)(1); OWASP ASVS 5.0: V8
SIGN-M-001	NIST SP 800-53 Rev.5: SR-3, SR-4, SA-12, SA-22
GOV-G-006	NIST SP 800-53 Rev.5: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; OWASP SAMM 2.0: Governance—Policy & Compliance; COBIT 2019: APO12.01, MEA02; NIST CSF 2.0: GV.RM, GV.OV, ID.RA
## Required actions
DIAGRAM
Actual size
View source

Protected source

Isolated build

Security gates

Generate SBOM

Scan artifact

Sign by digest

Controlled registry

Verify signature

Approved deployment

1.
Secure the pipeline execution path — Platform Engineering Implement version-controlled pipeline definitions and mandatory build, test, security, publication, and deployment stages per PIPE-M-001. Make workflow static analysis a required merge check. Prevent direct production deployment outside the approved pipeline. Require independent manual approval for production and other critical environments.
2.
Restrict workflow privileges and untrusted execution — DevOps Apply default-deny token permissions and grant only per-job scopes per PIPE-M-012. Restrict risky fork, comment, pull_request_target, and workflow_run triggers. Pin untrusted source checkouts to full commit SHAs and set credential persistence off. Prevent untrusted workflow values from being interpolated directly into shell commands.
3.
Generate an SBOM for every build — Build Engineering Generate CycloneDX or SPDX output and publish it as a build artifact per ART-M-002. Fail the pipeline when the SBOM is absent or generation fails. Associate the SBOM with the immutable artifact digest.
4.
Scan the final artifact — Product Security and Build Engineering Perform producer-side and consumer-side binary composition analysis per ART-M-001. Detect embedded secrets, unauthorized or unexpected components, and integrity violations. Resolve failures before promotion; do not rely solely on source-level SAST or SCA.
5.
Sign every deployable artifact — Release Engineering Sign container images, binaries, and packages using an approved cryptographic identity or key per SIGN-M-001 and ART-M-001. Sign immutable digests rather than mutable tags. Protect signing authority from ordinary build jobs and prevent untrusted pull-request workflows from reaching it.
6.
Enforce verification at deployment — Platform and Runtime Engineering Configure the deployment platform or admission policy to verify the artifact signature against approved signers. Block unsigned artifacts, invalid signatures, altered digests, and unapproved signers per SIGN-M-001. Test the fail-closed path with deliberately unsigned and incorrectly signed artifacts.
7.
Protect the artifact repository — Repository Administrators Require authenticated access, least-privilege RBAC, controlled publishing identities, and audit logging per INTEG-M-002. Ensure publication credentials are held in an approved secret store rather than pipeline files. Record artifact digest, publisher identity, timestamp, SBOM, signature, and promotion history.
8.
Prevent secret contamination — DevOps and Security Operations Mask secrets in console output, scan logs and artifacts, scan container images before publication, and clean ephemeral workspaces per SECR-M-002. Fail the build when secrets are detected and immediately rotate any exposed credential.
9.
Monitor integrity failures — Security Operations Forward CI/CD and repository audit events to the SIEM per LOG-M-003. Alert on signature failures, unauthorized publication, workflow changes, gate bypasses, unusual destinations, and anomalous service-account activity. Keep detection rules version-controlled and conduct quarterly tuning.
10.
Govern exceptions — Risk Owner and independent approving authority Do not suppress a failed integrity gate without an approved, unexpired deviation meeting GOV-G-006. Record the affected mandard, justification, residual risk, owner, compensating controls, approval, and expiry.
•
Implementation guidance: The knowledge standard VeriFy-IS-RMP-001, 10.3 InfoSec – Release Management & CI/CD Pipelines, maps to ART-M-001, ART-M-002, GOV-G-006, INTEG-M-002, LOG-M-003, PIPE-M-001, PIPE-M-012, SECR-M-002, and SIGN-M-001. It calls for isolated builds, dependency and vulnerability scanning, checksums and signed artifacts, restricted build-script changes, controlled artifact publication, secure credential storage, dependency pinning, artifact scanning before and after publication, and segregated deployment environments. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817688
## Evidence for audit
Control area	Minimum evidence
Pipeline governance	Version-controlled pipeline definition, branch protection export, workflow analyzer report, and deployment approval record
SBOM	CycloneDX or SPDX file associated with the build identifier and immutable artifact digest; pipeline log proving publication
Artifact analysis	Producer and consumer binary composition scan reports with gate outcome
Signing	Signature, certificate or signer identity, transparency record where applicable, and digest-bound signing log
Deployment verification	Admission or deployment policy configuration plus tests proving unsigned and invalidly signed artifacts are rejected
Repository protection	RBAC configuration, service-account inventory, authentication policy, access review, and push/pull audit records
Secret protection	Log-redaction configuration, completed secret scan, container scan, workspace-cleanup record, and credential-rotation incident where detection occurred
Monitoring	SIEM ingestion evidence, version-controlled detection rules, test alerts, incident tickets, and quarterly tuning record
Deviations	Approved and unexpired deviation record linked to the release and assurance pack
## Assumptions and limits

The current CI/CD platform, artifact types, repository configuration, signing-key custody, admission controls, SBOM coverage, and existing enforcement status were not verified. Framework mappings above are limited to mappings visible in the returned catalogue records and should not be treated as a complete cross-framework assessment.

Evidence and framework mapping
Catalogue-verified
8 cited
Exec
Engineer
Auditor
Critical
High
Frameworks
Sort
Risk
Mandard
Coverage
Mandard	Risk	Domain	Frameworks cited	Actions

ART-M-002
Generate SBOM
	CRITICAL	Artifact Management	
CIS CONTROLS
3
COBIT 2019
6
HIPAA
1
+13 more
	
Open
Copy
Link


PIPE-M-001
Secure CI/CD Pipeline Configuration
	CRITICAL	Pipeline Security	
CIS CONTROLS
1
COBIT 2019
2
CSA CCM
1
+13 more
	
Open
Copy
Link


PIPE-M-012
CI/CD Workflow Least Privilege and Safe Triggers
	CRITICAL	Pipeline Security	
CIS CONTROLS
1
COBIT 2019
2
CWE
3
+11 more
	
Open
Copy
Link


SECR-M-002
Prevent Secret Exposure in CI/CD Logs and History
	CRITICAL	Secrets Management	
CIS CONTROLS
6
COBIT 2019
7
CSA CCM
1
+15 more
	
Open
Copy
Link


SIGN-M-001
Enforce Artifact Code Signing
	CRITICAL	Code Signing	
CIS CONTROLS
4
COBIT 2019
6
CSA CCM
1
+12 more
	
Open
Copy
Link


ART-M-001
Artifact Signing & Verification
	HIGH	Artifact Management	
CIS CONTROLS
5
COBIT 2019
8
CSA CCM
2
+16 more
	
Open
Copy
Link


INTEG-M-002
Secure Artifact Repository
	HIGH	Integrity Verification	
CIS CONTROLS
7
COBIT 2019
7
CSA CCM
1
+14 more
	
Open
Copy
Link


LOG-M-003
Configure Centralized Log Aggregation and SIEM Alerting for CI/CD
	HIGH	Logging	
CIS CONTROLS
7
COBIT 2019
6
CSA CCM
1
+17 more
	
Open
Copy
Link
Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
Filter Explorer
CSV
JSON

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