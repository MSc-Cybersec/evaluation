# G10-GATE

## Question
How should we define security gate pass/fail criteria for release approval?

## Sage response

## Bottom line

Define release approval as a default-deny, evidence-based pipeline decision: production deployment passes only when mandatory security stages succeed, the exact artifact is verified and approved, and no control is bypassed without an approved, unexpired deviation. Per PIPE-M-001, security checks and authorized manual approval must occur before production promotion; per GOV-G-006, any exception must be independently approved, risk-owned, compensated, and time-bounded.

The SAGF results retrieved do not prescribe a universal numeric vulnerability threshold across all applications. Adopt the risk-tiered baseline below as Advisory (not catalogue-backed), then calibrate it by application criticality, data classification, exposure, and regulatory scope.

## Risk and impact

Release gates should address these decision risks in priority order:

| Priority | Exposure | Release consequence |
|---|---|---|
| CRITICAL | Pipeline compromise, secret disclosure, unsigned artifacts, missing SBOM, unsafe workflow privileges | Automatic fail unless a deviation is permitted and approved under GOV-G-006; some risks should be designated non-waivable |
| HIGH | Artifact repository compromise, missing centralized monitoring, incomplete artifact analysis | Fail or require formal, independent risk acceptance before release |
| MEDIUM | Pipeline hardening or non-production scanning deficiencies | Remediate before release or manage through a documented, expiring deviation |
| Evidence failure | Scanner did not run, timed out, scanned the wrong commit, or produced unusable evidence | Treat as fail, not pass |

The principal business impacts are unauthorized production change, compromised software supply chains, credential theft, inability to identify vulnerable deployed components, regulatory exceptions without accountable ownership, and insufficient evidence during incident response or audit.

## Governing mandards

### Direct release-gate mandards

| Mandard | Title | Risk |
|---|---|---|
| PIPE-M-001 | Secure CI/CD Pipeline Configuration | CRITICAL |
| PIPE-M-012 | CI/CD Workflow Least Privilege and Safe Triggers | CRITICAL |
| ART-M-002 | Generate SBOM | CRITICAL |
| SECR-M-002 | Prevent Secret Exposure in CI/CD Logs and History | CRITICAL |
| SIGN-M-001 | Enforce Artifact Code Signing | CRITICAL |
| ART-M-001 | Artifact Signing & Verification | HIGH |
| GOV-G-006 | Security Deviation and Exception Management | HIGH |
| INTEG-M-002 | Secure Artifact Repository | HIGH |
| LOG-M-003 | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | HIGH |

Key requirements are:

- Per PIPE-M-001: security stages must validate code before promotion; pipeline definitions must be version-controlled, auditable, statically analyzed, and production deployments manually approved by authorized accounts.
- Per PIPE-M-012: workflows must use least-privilege tokens, safe triggers, immutable commit references for untrusted code, disabled credential persistence, safe handling of untrusted context, and manual approval for critical environments.
- Per ART-M-002: every build pipeline must generate and publish a complete, machine-readable SBOM.
- Per SECR-M-002: detected secrets in pipeline logs must fail the build; artifacts and container images must also be checked for embedded secrets.
- Per SIGN-M-001: deployment must be blocked when a deployable artifact lacks a valid signature.
- Per ART-M-001: production artifacts must be signed, verified before deployment, and undergo final binary composition analysis.
- Per GOV-G-006: every control departure must have technical justification, residual-risk ownership, compensating controls, independent approval, and an expiry date.
- Per INTEG-M-002: artifact repositories must enforce authentication, authorization, and audit logging.
- Per LOG-M-003: CI/CD audit logs must be centralized and monitored for gate bypass, signature failure, unauthorized modification, secrets, and related anomalies.

### Complete pipeline domain returned by SAGF

The pipeline-domain lookup returned all of the following; applicability should be determined in the project control profile.

| Mandard | Title | Risk |
|---|---|---|
| PIPE-M-001 | Secure CI/CD Pipeline Configuration | CRITICAL |
| PIPE-M-002 | Pre-Commit Hooks Enforced | CRITICAL |
| PIPE-M-003 | Use Ephemeral Build Agents | CRITICAL |
| PIPE-M-004 | Pin Build Tool Versions | MEDIUM |
| PIPE-M-005 | Vulnerability Scans for Non-Prod | MEDIUM |
| PIPE-M-006 | Implement Plugin and Integration Governance in CI/CD Platforms | HIGH |
| PIPE-M-007 | Sequential Security Pipeline Execution | HIGH |
| PIPE-M-008 | Hermetic Builds — Isolated Build Environment | CRITICAL |
| PIPE-M-009 | Restrict Build Parameters to Whitelisted Values | MEDIUM |
| PIPE-M-010 | Maintain Inventory of Build Tools and Versions | HIGH |
| PIPE-M-011 | Enforce Build Immutability and Tamper-Proofing | HIGH |
| PIPE-M-012 | CI/CD Workflow Least Privilege and Safe Triggers | CRITICAL |
| PIPE-M-013 | Pin and Verify Third-Party CI Actions and Reusable Workflows | HIGH |
| PIPE-M-014 | CI Runner Hardening and Cache Poisoning Prevention | HIGH |

## Framework mapping

Framework mapping details were returned but are truncated in this capture. Use full Sage copy for complete control-level mapping when scoring citation completeness.


## Scoring notes
- actionability: pass (manual review)
- citation_correctness: pass (manual review)
- evidence_audit: pass (manual review)
- framework_mapping: pass (manual review)
- risk_impact: pass (manual review)
- bottom_line: pass (manual review)
- governing_mandards: pass (manual review)
- required_actions: pass (manual review)
- assumptions_limits: pass (manual review)
- hallucination_check: pass (manual review)
- overall_pass: pass