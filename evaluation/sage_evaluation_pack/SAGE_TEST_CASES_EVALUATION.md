# Sage Test Cases and Example Responses (Evaluation Pack)

This pack provides additional Sage-style governance consultation examples for dissertation evaluation.
Each example follows the seven-section auditable response contract used in existing Sage artefacts.

---

## Test Case G5

### Question
Our product team wants to delay MFA for privileged admin APIs by one release cycle. What should we require before any temporary approval?

### Example response

## Bottom line

Do not allow a default deferral. A temporary exception can only proceed through a formal deviation process with explicit residual-risk acceptance, compensating controls, fixed expiry, and independent approval before release.

## Risk and impact

High to Critical risk where privileged APIs are involved. Delaying MFA increases probability of account takeover, privilege abuse, and unauthorized administrative changes.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| GOV-G-006 | Security Deviation and Exception Management | High |
| AUTH-M-002 | Multi-Factor Authentication Enforcement | Critical |
| API-M-003 | Broken Function Level Authorization | Critical |

## Framework mapping

Relevant controls typically include NIST SP 800-53 IA/AC control families and ISO/IEC 27001 access-control and authentication controls.

## Required actions

1. Define scope: list impacted admin endpoints, identities, and environments.
2. Capture risk: document threat scenarios and business impact during exception window.
3. Apply compensation: stricter network policy, step-up auth on sensitive operations, enhanced monitoring.
4. Approve independently: security or risk authority outside delivery team.
5. Set expiry: hard stop date with remediation milestone plan.

## Evidence for audit

- Approved deviation record with owner and expiry.
- Endpoint inventory and privileged function map.
- Compensating-control configuration and validation results.
- SIEM detections and response procedures for admin actions.
- Closure evidence after MFA rollout.

## Assumptions and limits

Assumes admin APIs are business-critical and internet-adjacent. Exact risk rating depends on exposure model and current identity controls.

---

## Test Case G6

### Question
Can one enterprise key vault prove compliance for all secret-management controls across all CI/CD pipelines?

### Example response

## Bottom line

No. A key vault is necessary but not sufficient. Compliance requires lifecycle, scanning, rotation, and revocation evidence across each pipeline and workload.

## Risk and impact

Critical risk if secrets remain in source, logs, or long-lived automation credentials despite vault usage.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| SECR-M-001 | No Hardcoded Secrets | Critical |
| SECR-M-002 | Prevent Secret Exposure in CI/CD Logs and History | Critical |
| SECR-M-004 | Short-Lived Credentials and Rotation | Critical |
| SECR-M-005 | No Secrets in Build Logs | Critical |
| SECR-M-003 | Temporary Credentials and Rotation in CI/CD | High |

## Framework mapping

Mapped evidence usually aligns to NIST IA/AU/SC families and ISO/IEC 27001 controls for authentication information, logging, and cryptography.

## Required actions

1. Enforce secret scanning gates in every repository and pipeline.
2. Enforce masking and post-run log scanning for CI/CD output.
3. Replace long-lived automation credentials with short-lived federation.
4. Implement rotation SLA and auto-revocation for overdue credentials.
5. Link all artefacts through one evidence key per secret lifecycle.

## Evidence for audit

- Vault policy and access logs.
- Pipeline scan reports and failed-gate records.
- Rotation and revocation ledger with timestamps.
- Incident records for exposed-secret remediation.
- Quarterly control-effectiveness review.

## Assumptions and limits

Assumes centralized vault adoption exists. Does not validate runtime secret handling inside applications.

---

## Test Case G7

### Question
For an internal-only REST API, which API controls are truly mandatory and which can be marked not applicable?

### Example response

## Bottom line

Most API controls still apply to internal APIs. Only GraphQL-specific controls are not applicable for strictly REST-only interfaces.

## Risk and impact

Critical risk from unauthorized object access, excessive data exposure, weak token validation, and insufficient auditability even on private networks.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| API-M-001 | Broken Object Level Authorization Prevention | Critical |
| API-M-002 | Excessive Data Exposure Prevention | Critical |
| API-M-003 | Broken Function Level Authorization | Critical |
| API-M-005 | Authentication on Sensitive API | Critical |
| API-M-007 | JWT Signature Validation | Critical |
| API-M-008 | API Security Configuration Baseline | High |
| API-M-009 | API Inventory and Versioning Management | High |
| API-M-010 | API Audit Logging and Monitoring | High |
| API-M-011 | GraphQL Query Complexity Limits | Critical (GraphQL only) |
| API-M-012 | Disable GraphQL Introspection in Production | High (GraphQL only) |

## Framework mapping

Applicable mappings typically span NIST AC/SC/AU and ISO/IEC 27001 controls for access, secure configuration, and monitoring.

## Required actions

1. Document applicability matrix for all API mandards.
2. Mark API-M-011 and API-M-012 not applicable only if no GraphQL endpoint exists.
3. Verify authz/authn and field filtering through automated tests.
4. Enforce endpoint inventory and version deprecation process.
5. Forward structured API logs to central SIEM.

## Evidence for audit

- Applicability decision register with approver.
- OpenAPI inventory and route reconciliation evidence.
- Negative tests for unauthorized object and function access.
- JWT validation test artefacts.
- SIEM ingestion samples with correlation IDs.

## Assumptions and limits

Assumes REST-only architecture and no hidden GraphQL gateway.

---

## Test Case G8

### Question
What proof is strongest when auditors ask whether SAST actually blocks risky releases rather than just generating reports?

### Example response

## Bottom line

The strongest proof is a failed pipeline run caused by a known Critical or High issue, linked to a blocked merge or release decision.

## Risk and impact

Critical risk if scans are advisory-only. Known exploitable flaws can reach production.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| SAST-M-001 | No Critical SAST Findings | Critical |
| GOV-G-006 | Security Deviation and Exception Management | High |

## Framework mapping

Common mapping covers secure-development and verification control families (for example SA/SI/AC style controls).

## Required actions

1. Show pipeline-as-code with mandatory SAST and quality gate.
2. Run controlled negative test that triggers a Critical or High finding.
3. Capture gate-fail output and blocked promotion evidence.
4. Show successful rerun post-remediation.
5. Attach any approved deviation if override occurred.

## Evidence for audit

- Pipeline definition at commit hash.
- SAST policy export.
- Failed and passed run IDs with timestamps.
- Branch protection requiring security checks.
- Release decision log tied to security gate outcome.

## Assumptions and limits

Requires immutable build records and stable rule versions to avoid disputes on reproducibility.

---

## Test Case G9

### Question
We need to onboard a new SaaS dependency quickly. What supply-chain evidence is mandatory before production use?

### Example response

## Bottom line

Do not onboard without supplier security due diligence, dependency provenance checks, contractual controls, and ongoing monitoring.

## Risk and impact

High risk of dependency compromise, data leakage, legal non-compliance, and transitive vulnerability introduction.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| SUPPLY-M-001 | Third-Party and Supply-Chain Assurance | High |
| SCA-M-001 | Software Composition Analysis Gate | Critical |
| GOV-G-006 | Security Deviation and Exception Management | High |

## Framework mapping

Typical mappings include supplier-security and software-integrity controls across ISO/IEC 27001, NIST, and sector frameworks.

## Required actions

1. Classify dependency criticality and data access profile.
2. Verify SBOM/provenance and vulnerability posture.
3. Confirm legal, privacy, and security clauses in supplier contract.
4. Define patch cadence and incident notification obligations.
5. Register owner and continuous-review schedule.

## Evidence for audit

- Supplier assessment report.
- SBOM and artifact provenance evidence.
- SCA scan outputs with gating outcomes.
- Signed contractual security addendum.
- Ongoing monitoring tickets and review minutes.

## Assumptions and limits

Assumes procurement and legal workflows are integrated with engineering release process.

---

## Test Case G10

### Question
How should we assess a request to cache OAuth access tokens in a shared distributed cache for performance?

### Example response

## Bottom line

Permit only with strict controls: short token TTL, audience scoping, encryption at rest, cache isolation, rotation, and auditable exception if baseline policy is bypassed.

## Risk and impact

Critical risk if cached tokens are stolen or replayed, potentially enabling lateral movement and privileged API abuse.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| OAUTH-M-001 | OAuth Token Security Baseline | Critical |
| CRYPT-M-001 | Encryption at Rest and In Transit | Critical |
| SECR-M-004 | Short-Lived Credentials and Rotation | Critical |
| GOV-G-006 | Security Deviation and Exception Management | High |

## Framework mapping

Usually maps to token-management, cryptographic protection, and session control requirements.

## Required actions

1. Enforce token TTL minimization and strict audience binding.
2. Encrypt cache content and restrict cache namespace per service.
3. Disable token logging and debugging exposure.
4. Add replay-detection and anomaly monitoring.
5. If baseline is not met, process formal time-bound exception.

## Evidence for audit

- Token policy configuration and TTL validation.
- Cache encryption and access-control settings.
- Security test results for replay and theft scenarios.
- Monitoring alerts and incident runbook.
- Exception record with expiry if applicable.

## Assumptions and limits

Assumes OAuth bearer tokens are used. Alternative token models may require different controls.

---

## Test Case G11

### Question
Are mobile app controls enough if backend APIs already enforce strong security?

### Example response

## Bottom line

No. Mobile and backend controls are complementary. Mobile-layer controls remain mandatory for device-level threats and client-side abuse.

## Risk and impact

Medium to High risk from reverse engineering, insecure local storage, client tampering, and credential extraction.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| MOB-M-001 | Mobile Application Security Baseline | Low to Medium |
| AUTH-M-003 | Session Management and Timeout Controls | High |
| CRYPT-M-002 | Encryption in Transit Requirements | High |

## Framework mapping

Mappings generally include mobile-application hardening, cryptographic use, and session-control requirements.

## Required actions

1. Enforce secure local storage and certificate validation.
2. Prevent sensitive data leakage through logs and screenshots.
3. Apply session hardening and inactivity timeouts.
4. Validate backend authorization independently of client claims.
5. Run periodic mobile security testing per release.

## Evidence for audit

- Mobile hardening checklist and test evidence.
- Session timeout and token-refresh behaviour tests.
- Pen-test or MASVS-aligned assessment summary.
- Backend logs proving server-side enforcement.

## Assumptions and limits

Risk depends on platform mix, BYOD policy, and threat model maturity.

---

## Test Case G12

### Question
What should governance require before approving a temporary waiver on data-retention logging due to SIEM storage cost pressure?

### Example response

## Bottom line

Cost pressure alone is not sufficient justification. A waiver requires formal risk acceptance, minimum forensic baseline preservation, and a short, measurable remediation window.

## Risk and impact

High risk of delayed incident detection, weak investigations, and potential non-compliance with legal and regulatory retention obligations.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| LOG-M-001 | Security Logging and Monitoring Baseline | High |
| GOV-G-006 | Security Deviation and Exception Management | High |
| DATA-M-002 | Data Governance and Protection Controls | High |

## Framework mapping

Typical controls include event logging, monitoring, accountability, and records-management requirements.

## Required actions

1. Define minimum forensic dataset that cannot be reduced.
2. Evaluate alternative cost controls before retention reduction.
3. Approve only time-bound deviation with independent authority.
4. Track detection coverage during waiver period.
5. Execute funded remediation plan to restore full retention.

## Evidence for audit

- Deviation record with expiry and accountable owner.
- Retention-policy delta and risk assessment.
- Monitoring coverage analysis before and after change.
- Restoration plan and completion evidence.

## Assumptions and limits

Assumes organization already has a defined baseline logging policy and data-classification model.

---

## Test Case G13

### Question
How should we evaluate a proposal to allow undocumented emergency API endpoints in production during major incidents?

### Example response

## Bottom line

Reject undocumented production endpoints as a standard practice. Emergency paths must still be inventoried, controlled, and reviewed post-incident.

## Risk and impact

High to Critical risk: unmanaged attack surface, bypassed controls, and weak audit traceability.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| API-M-009 | API Inventory and Versioning Management | High |
| API-M-008 | API Security Configuration Baseline | High |
| GOV-G-006 | Security Deviation and Exception Management | High |

## Framework mapping

Mappings commonly include asset inventory, secure configuration, and change-control requirements.

## Required actions

1. Define emergency endpoint lifecycle with auto-expiry.
2. Require same authentication and authorization controls as normal endpoints.
3. Register endpoint metadata immediately at creation.
4. Trigger post-incident security review and removal verification.
5. Record any emergency waiver through formal deviation process.

## Evidence for audit

- Incident ticket linked to endpoint creation and removal.
- API inventory updates with timestamps.
- Access logs and alert coverage for emergency routes.
- Post-incident review approval.

## Assumptions and limits

Assumes emergency response requires temporary operational APIs; permanent use is non-compliant.

---

## Test Case G14

### Question
What minimum governance evidence is needed to claim that policy exceptions are not becoming permanent technical debt?

### Example response

## Bottom line

Track exception lifecycle metrics and enforce closure discipline. Exceptions must be measurable, expiring, and tied to funded remediation outcomes.

## Risk and impact

High risk when exceptions accumulate: control erosion, unmanaged exposure, and normalization of policy bypass.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| GOV-G-006 | Security Deviation and Exception Management | High |
| ASSURE-M-001 | Independent Assurance | High |

## Framework mapping

Generally maps to governance oversight, risk acceptance, and independent-assurance control objectives.

## Required actions

1. Maintain centralized exception register with owner, scope, and expiry.
2. Enforce renewal criteria with independent re-approval.
3. Measure open, overdue, and repeated exceptions by control domain.
4. Link exceptions to remediation backlog and budget owner.
5. Escalate repeated exceptions to governance committee.

## Evidence for audit

- Exception dashboard snapshots and monthly trend reports.
- Samples of expired exceptions closed on time.
- Independent assurance review notes.
- Remediation completion artefacts tied to exception IDs.

## Assumptions and limits

Assumes consistent taxonomy and ownership model across business units.

---

## Usage notes for dissertation scoring

Use this pack with the same response-contract checklist applied to G1-G4:

1. Section-presence scoring across the seven mandated sections.
2. Citation and mandard-ID correctness checks.
3. Advisory-labelling checks where implementation detail is not catalogue-backed.
4. Hallucination checks for non-existent controls, IDs, or counts.
5. Actionability scoring of required actions and audit evidence.

---

## Full domain coverage matrix (80 domains)

The table below gives at least one governance consultation test question per domain prefix in the corpus.
Use each prompt in Sage and score the output with the same response-contract rubric.

| # | Domain | Test question | Expected response focus |
|---:|---|---|---|
| 1 | AI | What evidence do we need to approve a high-impact AI model release? | AI governance controls, risk classification, monitoring, human oversight, audit evidence. |
| 2 | AUTH | What minimum controls are required before granting an auth exception for privileged users? | Authentication baseline, MFA, risk owner approval, expiry and compensating controls. |
| 3 | AC | How do we prove least-privilege access is enforced for production operators? | Access model, role review cadence, segregation of duties, audit logs. |
| 4 | BACKUP | What backup evidence is mandatory before go-live of a critical service? | Backup scope, restore testing, retention, encryption, recovery objectives. |
| 5 | HDR | Which security headers are non-negotiable for internet-facing apps? | Header baseline, enforcement testing, policy exceptions, monitoring. |
| 6 | CSPM | What governance checks should CSPM findings trigger before release? | Misconfiguration triage, risk-based remediation SLA, exception path, evidence closure. |
| 7 | ART | What controls are required for artifact integrity in our build and release chain? | Signed artifacts, provenance, repository trust, verification at deploy time. |
| 8 | BIZ | How should business-risk owners accept residual cyber risk from delayed fixes? | Formal risk acceptance, quantified impact, accountability, time-bound plan. |
| 9 | PIPE | What evidence proves pipeline controls prevent unsafe code promotion? | Required gates, failed-run proof, branch protections, immutable logs. |
| 10 | GATE | How should we define security gate pass/fail criteria for release approval? | Blocking thresholds, ownership, override governance, review cadence. |
| 11 | ASSURE | What independent assurance artefacts are needed for quarterly compliance attestation? | Independent review scope, test methods, findings tracking, sign-off evidence. |
| 12 | BOT | What policy controls should govern autonomous security bots in production? | Bot identity, action boundaries, approval paths, safety guardrails, logging. |
| 13 | API | Which API controls remain mandatory for internal-only services? | AuthN/AuthZ, data minimization, inventory, logging, not-applicable handling. |
| 14 | LOG | What is the minimum forensic logging baseline we cannot waive? | Event scope, retention, tamper resistance, SIEM ingestion and alerting. |
| 15 | COOK | What cookie controls are required for session-bearing web applications? | Secure/HttpOnly/SameSite, rotation, invalidation, transport protections. |
| 16 | CORS | When is wildcard CORS prohibited and what is the safe alternative? | Explicit allowlist, credentials policy, preflight handling, test evidence. |
| 17 | MOB | Are backend controls enough without mobile-app hardening? | Client hardening, local storage protections, tamper resistance, server-side enforcement. |
| 18 | MCP | What governance controls apply to MCP tools that can change system state? | Tool scoping, least privilege, auditability, approval and rollback controls. |
| 19 | EXCEPT | What must be documented to approve a 60-day security exception? | Scope, rationale, compensating controls, risk owner, expiry, closure criteria. |
| 20 | DECOM | What evidence is required when decommissioning an application handling sensitive data? | Data disposal, access revocation, dependency cleanup, audit records. |
| 21 | CONT | Which controls must be proven before promoting a new container image? | Image scanning, base image policy, runtime controls, registry trust. |
| 22 | SVRL | How should we govern serverless function identity and secrets usage? | Managed identity, secret handling, permission scoping, event logging. |
| 23 | FILE | What file-upload governance checks are mandatory for public endpoints? | Content validation, malware scanning, storage isolation, execution prevention. |
| 24 | DLP | What controls should trigger DLP incident escalation for source repositories? | Classification policy, detection confidence, response workflow, containment evidence. |
| 25 | CFG | How do we prove secure-by-default configuration in every environment? | Baseline policy, drift detection, change approvals, periodic validation. |
| 26 | ZTA | What minimum Zero Trust controls are required for internal admin portals? | Strong identity, device trust, policy enforcement, continuous verification. |
| 27 | GRAPHQL | What controls are mandatory before enabling GraphQL in production? | Complexity limits, introspection policy, auth model, abuse monitoring. |
| 28 | EMAIL | What governance controls reduce phishing and spoofing risk for enterprise mail? | DMARC/SPF/DKIM posture, monitoring, incident handling, training linkage. |
| 29 | CLOUD | What cloud governance evidence is required before onboarding a new subscription? | Landing-zone controls, identity model, policy guardrails, monitoring setup. |
| 30 | AJAX | How should async client requests be governed to prevent token leakage? | Secure request patterns, token handling, origin controls, error hygiene. |
| 31 | OAUTH | What controls are required for secure OAuth token lifecycle management? | Token TTL, scope/audience, storage protections, rotation and revocation. |
| 32 | ERR | What is an acceptable production error-handling policy for sensitive systems? | No sensitive leakage, structured codes, secure diagnostics, alerting links. |
| 33 | TM | How should threat-model outputs be enforced as release requirements? | Threat ranking, control mapping, ownership, closure evidence before release. |
| 34 | CRED | What governance controls prevent misuse of privileged credentials in CI/CD? | Short-lived creds, vault integration, rotation policy, access logging. |
| 35 | PBAC | How do we validate policy-based access control decisions for critical APIs? | Policy correctness tests, denial-by-default, audit trail, drift monitoring. |
| 36 | LEGACY | What controls are mandatory when supporting legacy protocols temporarily? | Exposure constraints, compensating controls, migration timeline, risk acceptance. |
| 37 | IAC | What evidence proves IaC changes are security-reviewed and policy-compliant? | Policy-as-code results, peer review, drift controls, deployment attestations. |
| 38 | DATA | How do we prove data minimization and lawful processing in application workflows? | Data mapping, minimization checks, retention/deletion controls, approvals. |
| 39 | REST | What governance checks are required before publishing new REST endpoints? | Contract/versioning, auth and authz, schema validation, monitoring. |
| 40 | NET | What network-segmentation evidence is required for tiered application deployment? | Segment design, flow allowlists, firewall policy, verification tests. |
| 41 | IDOR | How should we evidence object-level authorization for tenant data access? | Ownership checks, negative testing, identifier handling, log correlation. |
| 42 | DEP | What governance controls should block risky third-party package updates? | Dependency risk scoring, approval rules, SCA gating, rollback readiness. |
| 43 | SAML | What controls are required before federating SAML with an external IdP? | Assertion validation, certificate lifecycle, audience restrictions, monitoring. |
| 44 | NOSQL | What security controls are mandatory for production NoSQL data stores? | Access controls, encryption, query safety, backup and monitoring evidence. |
| 45 | REMEDI | How do we evidence that remediation actions are effective, not just recorded? | Verification testing, closure criteria, regression checks, accountable owner. |
| 46 | EDGE | What controls are required for edge-delivered application traffic? | Edge auth, WAF/rate limits, cache policy, certificate governance. |
| 47 | SCA | What is the minimum SCA evidence required to block vulnerable dependencies? | Scanner policy, fail thresholds, exception governance, remediation tracking. |
| 48 | NSEG | What policy controls govern network segmentation exceptions during incidents? | Temporary segmentation changes, approvals, monitoring, rollback and closure. |
| 49 | CRYPT | What cryptographic controls are mandatory for regulated customer data? | Algorithm policy, key management, rotation, crypto boundary evidence. |
| 50 | INJECT | Which controls are required to prevent command and query injection classes? | Input validation, parameterization, output encoding, test and scan evidence. |
| 51 | SUPPLY | What supply-chain assurances are required before onboarding a new vendor library? | Provenance, contract controls, vulnerability posture, continuous monitoring. |
| 52 | PARAM | How should parameter tampering risks be controlled in sensitive transactions? | Server-side validation, signing/integrity, replay protections, logging. |
| 53 | DB | What evidence proves secure database access and encryption posture? | Least privilege, encryption at rest/in transit, audit logs, backup controls. |
| 54 | INPUT | What governance policy defines acceptable input-validation standards? | Allowlist strategy, canonicalization, validation coverage, exception handling. |
| 55 | SVR | What server hardening baseline is mandatory before production release? | Patch baseline, service minimization, secure configs, continuous checks. |
| 56 | RTC | What controls are required for real-time communications carrying sensitive data? | Authenticated sessions, encryption, integrity checks, abuse monitoring. |
| 57 | GOV | Which governance artefacts are mandatory for annual control assurance review? | Policy set, accountability, metrics, independent review, exceptions. |
| 58 | INTEG | What controls govern secure system-to-system integrations? | Trust boundaries, token handling, message validation, monitoring and retries. |
| 59 | TENANT | How do we verify tenant isolation in multi-tenant services? | Isolation tests, data boundary controls, noisy-neighbor risk handling. |
| 60 | SIGN | What digital-signature evidence is required for non-repudiable workflows? | Signing keys, verification path, timestamping, audit evidence. |
| 61 | REPO | What repository controls are mandatory to reduce source and secret risk? | Branch protections, signed commits, scanner gates, access governance. |
| 62 | K8S | What Kubernetes controls are required before onboarding a new namespace? | RBAC, network policy, workload identity, image policy and audit logs. |
| 63 | SSRF | How should SSRF risk be governed for services that call external URLs? | Egress controls, URL allowlists, metadata endpoint protection, logging. |
| 64 | SAST | What evidence proves SAST gates actively block high-risk code? | Failed-run evidence, policy thresholds, mandatory checks, remediation rerun. |
| 65 | MON | What monitoring controls prove timely detection of security incidents? | Coverage model, detection rules, alert latency, response verification. |
| 66 | TRAIN | What security training evidence is required for privileged engineering roles? | Role-based curricula, completion evidence, assessment outcomes, renewal cycle. |
| 67 | AIDEV | What controls govern safe use of AI coding assistants in regulated development? | Prompt/data handling, review policy, output validation, auditability. |
| 68 | PROV | What evidence confirms provenance integrity for released binaries and images? | Build attestation, signer trust, chain-of-custody, verification records. |
| 69 | TXN | What controls are required for transaction integrity across distributed services? | Idempotency, integrity validation, rollback controls, fraud monitoring. |
| 70 | IAM | How do we prove IAM controls are enforced consistently across platforms? | Role model, joiner-mover-leaver process, periodic recertification, logs. |
| 71 | RUNTIME | What runtime protections are mandatory for internet-facing workloads? | Runtime detection, policy enforcement, isolation, incident response hooks. |
| 72 | VDP | What controls are needed to run a vulnerability disclosure process safely? | Intake policy, triage SLA, legal safe harbor, communication workflow. |
| 73 | INC | What incident-response evidence is required for major security events? | Timeline, decision records, containment actions, lessons learned tracking. |
| 74 | WAF | What governance checks are required before tuning WAF blocking rules? | Rule-change approvals, false-positive handling, telemetry, rollback path. |
| 75 | WS | What controls apply to secure web-service endpoints beyond REST basics? | Protocol hardening, authn/authz, message validation, observability. |
| 76 | LLM | What controls are required before exposing an LLM endpoint to employees? | Safety filters, access policy, prompt handling, abuse and output monitoring. |
| 77 | MSA | What controls are required to secure service-to-service calls in microservices? | Mutual auth, policy enforcement, secrets handling, distributed tracing. |
| 78 | RAG | What governance controls are required for grounded retrieval in production? | Source trust, citation discipline, poisoning controls, evaluation evidence. |
| 79 | SBOM | What SBOM evidence is required at release and how should it be verified? | SBOM completeness, signature/provenance, vulnerability linkage, retention. |
| 80 | SECR | What evidence demonstrates end-to-end secrets governance compliance? | Source/log scanning, rotation and revocation, vault controls, audit trail. |

### Execution recommendation

1. Run these 80 prompts in Sage and save each output as `GXX-<DOMAIN>.md`.
2. Score each output with the response-contract checklist and hallucination checks.
3. Produce a domain coverage dashboard: pass/fail by section presence, citation correctness, and actionability.
