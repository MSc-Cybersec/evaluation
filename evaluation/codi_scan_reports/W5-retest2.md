# SAGF Workspace Scan Results

**Files Found**: 100
**Files Scanned**: 100
**Files Skipped** (>500KB): 0
**Files with Violations**: 18
**Errors**: 0

## 🚨 Files with Mandard Violations

---

## SAGF Compliance Scan: `artifacts/db-reset.js`
**Scanned at**: 2026-10-11T17:55:45.816169+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 113 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 113
const stocks = Math.floor((Math.random() * 40) + 1);
// Line 114
const funds = Math.floor((Math.random() * 40) + 1);
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 113, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/e2e/support/commands.js`
**Scanned at**: 2026-10-11T17:55:45.237729+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 30 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 30
cy.exec("npm run db:seed", {
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 30, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/data/user-dao.js`
**Scanned at**: 2026-10-11T17:55:45.469198+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 51 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 51
const day = (Math.floor(Math.random() * 10) + today.getDay()) % 29;
// Line 52
const month = (Math.floor(Math.random() * 10) + today.getMonth()) % 12;
// Line 53
const year = Math.ceil(Math.random() * 30) + today.getFullYear();
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 51, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/routes/index.js`
**Scanned at**: 2026-10-11T17:55:45.090167+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 72 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Open redirect using unvalidated user input
```js
// Line 72
return res.redirect(req.query.url);
```
**Suggested fix:**
```js
// Suggested fix: validate redirect target against an explicit allowlist
const ALLOWED = ['/dashboard', '/profile', '/home'];
const target = req.query.next || '/home';
if (!ALLOWED.includes(target)) { return res.redirect('/home'); }
res.redirect(target);
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 72, "message": "Open redirect using unvalidated user input", "fix_snippet": "// Suggested fix: validate redirect target against an explicit allowlist\nconst ALLOWED = ['/dashboard', '/profile', '/home'];\nconst target = req.query.next || '/home';\nif (!ALLOWED.includes(target)) { return res.redirect('/home'); }\nres.redirect(target);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/routes/contributions.js`
**Scanned at**: 2026-10-11T17:55:45.574106+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 31 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 31
// Insecure use of eval() to parse inputs
// Line 32
const preTax = eval(req.body.preTax);
// Line 33
const afterTax = eval(req.body.afterTax);
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🔴 Critical | [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) | Prevent Insecure Deserialization |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 31, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/routes/session.js`
**Scanned at**: 2026-10-11T17:55:49.467381+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 16 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 16
const stocks = Math.floor((Math.random() * 40) + 1);
// Line 17
const funds = Math.floor((Math.random() * 40) + 1);
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 16, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/Gruntfile.js`
**Scanned at**: 2026-10-11T17:55:49.339875+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 165 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 165
exec(
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 165, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/artifacts/db-reset.js`
**Scanned at**: 2026-10-11T17:55:47.923662+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 113 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 113
const stocks = Math.floor((Math.random() * 40) + 1);
// Line 114
const funds = Math.floor((Math.random() * 40) + 1);
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 113, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/assets/vendor/chart/raphael-min.js`
**Scanned at**: 2026-10-11T17:55:52.886709+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 10 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 10
(function(a){var b="0.3.4",c="hasOwnProperty",d=/[\.\/]/,e="*",f=function(){},g=function(a,b){return a-b},h,i,j={n:{}},k=function(a,b){var c=j,d=i,e=Array.prototype.slice.call(arguments,2),f=k.list...
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 10, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `app/assets/vendor/jquery.min.js`
**Scanned at**: 2026-10-11T17:55:52.682513+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 4 |
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 4 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 4
(function(e,t){var n,r,i=typeof t,o=e.location,a=e.document,s=a.documentElement,l=e.jQuery,u=e.$,c={},p=[],f="1.10.2",d=p.concat,h=p.push,g=p.slice,m=p.indexOf,y=c.toString,v=c.hasOwnProperty,b=f.t...
// Line 5
}({});var B=/(?:\{[\s\S]*\}|\[[\s\S]*\])$/,P=/([A-Z])/g;function R(e,n,r,i){if(x.acceptData(e)){var o,a,s=x.expando,l=e.nodeType,u=l?x.cache:e,c=l?e[s]:e[s]&&s;if(c&&u[c]&&(i||u[c].data)||r!==t||"s...
// Line 6
u[o]&&(delete u[o],c?delete n[l]:typeof n.removeAttribute!==i?n.removeAttribute(l):n[l]=null,p.push(o))}},_evalUrl:function(e){return x.ajax({url:e,type:"GET",dataType:"script",async:!1,global:!1,"...
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 4
(function(e,t){var n,r,i=typeof t,o=e.location,a=e.document,s=a.documentElement,l=e.jQuery,u=e.$,c={},p=[],f="1.10.2",d=p.concat,h=p.push,g=p.slice,m=p.indexOf,y=c.toString,v=c.hasOwnProperty,b=f.t...
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | Cross-Origin-Embedder-Policy (COEP) |

_+ 54 more applicable mandards — [view all 62 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 4, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 4, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/test/e2e/support/commands.js`
**Scanned at**: 2026-10-11T17:55:51.762137+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 30 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 30
cy.exec("npm run db:seed", {
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 30, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `Gruntfile.js`
**Scanned at**: 2026-10-11T17:55:52.039424+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 165 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 165
exec(
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 165, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/data/user-dao.js`
**Scanned at**: 2026-10-11T17:55:55.856786+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 51 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 51
const day = (Math.floor(Math.random() * 10) + today.getDay()) % 29;
// Line 52
const month = (Math.floor(Math.random() * 10) + today.getMonth()) % 12;
// Line 53
const year = Math.ceil(Math.random() * 30) + today.getFullYear();
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 51, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/routes/contributions.js`
**Scanned at**: 2026-10-11T17:55:56.899991+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 31 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 31
// Insecure use of eval() to parse inputs
// Line 32
const preTax = eval(req.body.preTax);
// Line 33
const afterTax = eval(req.body.afterTax);
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🔴 Critical | [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) | Prevent Insecure Deserialization |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 31, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/routes/index.js`
**Scanned at**: 2026-10-11T17:55:57.299657+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 72 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Open redirect using unvalidated user input
```js
// Line 72
return res.redirect(req.query.url);
```
**Suggested fix:**
```js
// Suggested fix: validate redirect target against an explicit allowlist
const ALLOWED = ['/dashboard', '/profile', '/home'];
const target = req.query.next || '/home';
if (!ALLOWED.includes(target)) { return res.redirect('/home'); }
res.redirect(target);
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 72, "message": "Open redirect using unvalidated user input", "fix_snippet": "// Suggested fix: validate redirect target against an explicit allowlist\nconst ALLOWED = ['/dashboard', '/profile', '/home'];\nconst target = req.query.next || '/home';\nif (!ALLOWED.includes(target)) { return res.redirect('/home'); }\nres.redirect(target);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/routes/session.js`
**Scanned at**: 2026-10-11T17:55:58.095829+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 16 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 16
const stocks = Math.floor((Math.random() * 40) + 1);
// Line 17
const funds = Math.floor((Math.random() * 40) + 1);
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 16, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/assets/vendor/chart/raphael-min.js`
**Scanned at**: 2026-10-11T17:55:58.838444+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 10 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 10
(function(a){var b="0.3.4",c="hasOwnProperty",d=/[\.\/]/,e="*",f=function(){},g=function(a,b){return a-b},h,i,j={n:{}},k=function(a,b){var c=j,d=i,e=Array.prototype.slice.call(arguments,2),f=k.list...
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 10, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `NodeGoat-master/app/assets/vendor/jquery.min.js`
**Scanned at**: 2026-10-11T17:55:59.089503+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 4 |
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 4 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 4
(function(e,t){var n,r,i=typeof t,o=e.location,a=e.document,s=a.documentElement,l=e.jQuery,u=e.$,c={},p=[],f="1.10.2",d=p.concat,h=p.push,g=p.slice,m=p.indexOf,y=c.toString,v=c.hasOwnProperty,b=f.t...
// Line 5
}({});var B=/(?:\{[\s\S]*\}|\[[\s\S]*\])$/,P=/([A-Z])/g;function R(e,n,r,i){if(x.acceptData(e)){var o,a,s=x.expando,l=e.nodeType,u=l?x.cache:e,c=l?e[s]:e[s]&&s;if(c&&u[c]&&(i||u[c].data)||r!==t||"s...
// Line 6
u[o]&&(delete u[o],c?delete n[l]:typeof n.removeAttribute!==i?n.removeAttribute(l):n[l]=null,p.push(o))}},_evalUrl:function(e){return x.ajax({url:e,type:"GET",dataType:"script",async:!1,global:!1,"...
```
**Suggested fix:**
```js
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```js
// Line 4
(function(e,t){var n,r,i=typeof t,o=e.location,a=e.document,s=a.documentElement,l=e.jQuery,u=e.$,c={},p=[],f="1.10.2",d=p.concat,h=p.push,g=p.slice,m=p.indexOf,y=c.toString,v=c.hasOwnProperty,b=f.t...
```
**Suggested fix:**
```js
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | Cross-Origin-Embedder-Policy (COEP) |

_+ 54 more applicable mandards — [view all 62 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 4, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 4, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

