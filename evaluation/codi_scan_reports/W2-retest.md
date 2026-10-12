# SAGF Workspace Scan Results

**Files Found**: 650
**Files Scanned**: 650
**Files Skipped** (>500KB): 0
**Files with Violations**: 40
**Errors**: 0

## 🚨 Files with Mandard Violations

---

## SAGF Compliance Scan: `services/gateway-service/main.go`
**Scanned at**: 2026-10-11T16:24:56.606790+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 102 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```go
// Line 102
owner.RegistrationID = fake.Hash().MD5()
```
**Suggested fix:**
```go
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 102, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}]
-->

---

## SAGF Compliance Scan: `services/workshop/utils/jwt.py`
**Scanned at**: 2026-10-11T16:24:56.345722+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 54 |
| 🔴 CRITICAL | [API-M-007](https://verify.example-org.internal/?id=API-M-007) | JWT Signature Validation | 61 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 54
identity_url, json=tokenJson, verify=False
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

#### [API-M-007](https://verify.example-org.internal/?id=API-M-007) — jwt.decode() skips signature verification — use jwt.verify()
```py
// Line 61
decoded = jwt.decode(token, options={"verify_signature": False})
```
**Suggested fix:**
```py
// Suggested fix: always verify the JWT signature before trusting claims
// WRONG:  const payload = jwt.decode(token);  // no signature check!
const payload = jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });
```
> 💡 **Why**: Risk: Failure to validate the signature, or accepting the `alg:none` header, allows an attacker to forge a valid token for *any user* (including an admin) simply by creating the payload, setting `alg:none`, and sending it.
> 🔧 **Guidance**: A developer must ensure the JWT validation library is correctly configured to *always* check the signature and to *reject* the 'none' algorithm.
> [Full remediation →](https://verify.example-org.internal/?id=API-M-007)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |

_+ 47 more applicable mandards — [view all 55 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 54, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}, {"mandard_id": "API-M-007", "severity": "CRITICAL", "line": 61, "message": "jwt.decode() skips signature verification \u2014 use jwt.verify()", "fix_snippet": "// Suggested fix: always verify the JWT signature before trusting claims\n// WRONG:  const payload = jwt.decode(token);  // no signature check!\nconst payload = jwt.verify(token, process.env.JWT_SECRET, { algorithms: ['HS256'] });"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/workshop/core/management/commands/seed_database.py`
**Scanned at**: 2026-10-11T16:24:57.505787+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 220 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 220
request = requests.get(identity_health_url, headers, verify=False)
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 220, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}]
-->

---

## SAGF Compliance Scan: `services/web/src/sagas/userSaga.ts`
**Scanned at**: 2026-10-11T16:25:07.059723+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM | 50 |

#### [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) — Sensitive data logged to console
```ts
// Line 50
console.log("validateAccessToken invoked fn", action);
// Line 75
console.log("validateAccessToken error", e);
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
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "LOG-M-001", "severity": "HIGH", "line": 50, "message": "Sensitive data logged to console", "fix_snippet": "// Suggested fix: never log credentials \u2014 log a masked reference instead\n// WRONG:  console.log('Auth', password, apiKey);\nconst logger = require('./logger');  // structured logger (e.g. winston, pino)\nlogger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/workshop/crapi/shop/views.py`
**Scanned at**: 2026-10-11T16:25:09.421909+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 148 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 389 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 148
verify=False,
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```py
// Line 389
"SELECT coupon_code from applied_coupon WHERE user_id = "
```
**Suggested fix:**
```py
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
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 148, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 389, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/workshop/crapi/shop/tests.py`
**Scanned at**: 2026-10-11T16:25:08.791013+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 166 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```py
// Line 166
"coupon_code": "'; SELECT number FROM user_login WHERE email='"
```
**Suggested fix:**
```py
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
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |

_+ 49 more applicable mandards — [view all 57 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 166, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}]
-->

---

## SAGF Compliance Scan: `services/workshop/crapi/merchant/views.py`
**Scanned at**: 2026-10-11T16:25:13.031284+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 91 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 91
verify=False,
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 91, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/utils/SMTPMailServer.java`
**Scanned at**: 2026-10-11T16:25:20.074072+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) | Stack trace or exception detail sent to client | 82 |

#### [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) — Stack trace or exception detail sent to client
```java
// Line 82
e.printStackTrace();
```
**Suggested fix:**
```java
// Suggested fix: log full error server-side; send a generic message to client
app.use((err, req, res, next) => {
    logger.error({ err }, 'Unhandled error');           // full detail — server only
    res.status(500).json({ error: 'Internal server error' });  // generic to client
});
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |

_+ 49 more applicable mandards — [view all 57 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "ERR-M-001", "severity": "HIGH", "line": 82, "message": "Stack trace or exception detail sent to client", "fix_snippet": "// Suggested fix: log full error server-side; send a generic message to client\napp.use((err, req, res, next) => {\n    logger.error({ err }, 'Unhandled error');           // full detail \u2014 server only\n    res.status(500).json({ error: 'Internal server error' });  // generic to client\n});"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/utils/OTPGenerator.java`
**Scanned at**: 2026-10-11T16:25:19.341061+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 39 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```java
// Line 39
int r = (int) (n * Math.random());
```
**Suggested fix:**
```java
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 39, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/utils/GenerateVIN.java`
**Scanned at**: 2026-10-11T16:25:19.604639+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 28 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```java
// Line 28
random = new Random();
```
**Suggested fix:**
```java
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 28, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/utils/EmailTokenGenerator.java`
**Scanned at**: 2026-10-11T16:25:19.471413+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 36 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```java
// Line 36
int r = (int) (n * Math.random());
// Line 42
int r = (int) (n * Math.random());
```
**Suggested fix:**
```java
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 36, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/utils/BashCommand.java`
**Scanned at**: 2026-10-11T16:25:20.311795+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 44 |
| 🟠 HIGH | [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) | Stack trace or exception detail sent to client | 58 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```java
// Line 44
Process p = r.exec(commands);
```
**Suggested fix:**
```java
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

#### [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) — Stack trace or exception detail sent to client
```java
// Line 58
e.printStackTrace();
```
**Suggested fix:**
```java
// Suggested fix: log full error server-side; send a generic message to client
app.use((err, req, res, next) => {
    logger.error({ err }, 'Unhandled error');           // full detail — server only
    res.status(500).json({ error: 'Internal server error' });  // generic to client
});
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 44, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "ERR-M-001", "severity": "HIGH", "line": 58, "message": "Stack trace or exception detail sent to client", "fix_snippet": "// Suggested fix: log full error server-side; send a generic message to client\napp.use((err, req, res, next) => {\n    logger.error({ err }, 'Unhandled error');           // full detail \u2014 server only\n    res.status(500).json({ error: 'Internal server error' });  // generic to client\n});"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lithammer/shortuuid/shortuuid.go`
**Scanned at**: 2026-10-11T16:25:20.525265+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 37 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function SHA-1 detected
```go
// Line 37
u = uuid.NewSHA1(uuid.NameSpaceURL, []byte(name))
// Line 39
u = uuid.NewSHA1(uuid.NameSpaceDNS, []byte(name))
```
**Suggested fix:**
```go
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 37, "message": "Deprecated hash function SHA-1 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/service/Impl/VehicleServiceImpl.java`
**Scanned at**: 2026-10-11T16:25:24.970510+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 92 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```java
// Line 92
Random random = new Random();
// Line 178
Random random = new Random();
// Line 261
Random random = new Random();
```
**Suggested fix:**
```java
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🟠 High | [API-M-013](https://verify.example-org.internal/?id=API-M-013) | Message-Level Integrity and Confidentiality |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 92, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/google/uuid/hash.go`
**Scanned at**: 2026-10-11T16:25:26.678522+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 39 |
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 47 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```go
// Line 39
// NewMD5 returns a new MD5 (Version 3) UUID based on the
// Line 43
func NewMD5(space UUID, data []byte) UUID {
```
**Suggested fix:**
```go
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function SHA-1 detected
```go
// Line 47
// NewSHA1 returns a new SHA1 (Version 5) UUID based on the
// Line 51
func NewSHA1(space UUID, data []byte) UUID {
```
**Suggested fix:**
```go
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |
| 🔴 Critical | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 39, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 47, "message": "Deprecated hash function SHA-1 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/google/uuid/version4.go`
**Scanned at**: 2026-10-11T16:25:29.340939+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 12 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```go
// Line 12
//    uuid.Must(uuid.NewRandom())
// Line 14
return Must(NewRandom())
// Line 29
func NewRandom() (UUID, error) {
```
**Suggested fix:**
```go
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 12, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lib/pq/copy.go`
**Scanned at**: 2026-10-11T16:25:30.727211+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 216 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 216
// You need to call Exec(nil) to sync the COPY stream and to get any
// Line 219
func (ci *copyin) Exec(v []driver.Value) (r driver.Result, err error) {
```
**Suggested fix:**
```go
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 216, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lib/pq/conn_go18.go`
**Scanned at**: 2026-10-11T16:25:31.380708+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 42 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 42
return cn.Exec(query, list)
```
**Suggested fix:**
```go
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
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 42, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lib/pq/conn.go`
**Scanned at**: 2026-10-11T16:25:31.564827+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 522 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 1570 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 522
_, commandTag, err := cn.simpleExec("BEGIN" + mode)
// Line 564
_, commandTag, err := cn.simpleExec("COMMIT")
// Line 590
_, commandTag, err := cn.simpleExec("ROLLBACK")
```
**Suggested fix:**
```go
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```go
// Line 1570
//    err := db.Exec(fmt.Sprintf("INSERT INTO %s VALUES ($1)", quoted), data)
```
**Suggested fix:**
```go
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 522, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 1570, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lib/pq/array.go`
**Scanned at**: 2026-10-11T16:25:34.644726+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 22 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```go
// Line 22
//  db.Query(`SELECT * FROM t WHERE id = ANY($1)`, pq.Array([]int{235, 401}))
```
**Suggested fix:**
```go
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [LOG-M-002](https://verify.example-org.internal/?id=LOG-M-002) | Implement Comprehensive CI/CD Audit Logging |

_+ 47 more applicable mandards — [view all 55 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 22, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/exception/ExceptionHandler.java`
**Scanned at**: 2026-10-11T16:25:39.509955+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) | Stack trace or exception detail sent to client | 56 |

#### [ERR-M-001](https://verify.example-org.internal/?id=ERR-M-001) — Stack trace or exception detail sent to client
```java
// Line 56
e.printStackTrace();
```
**Suggested fix:**
```java
// Suggested fix: log full error server-side; send a generic message to client
app.use((err, req, res, next) => {
    logger.error({ err }, 'Unhandled error');           // full detail — server only
    res.status(500).json({ error: 'Internal server error' });  // generic to client
});
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [API-M-007](https://verify.example-org.internal/?id=API-M-007) | JWT Signature Validation |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |

_+ 49 more applicable mandards — [view all 57 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "ERR-M-001", "severity": "HIGH", "line": 56, "message": "Stack trace or exception detail sent to client", "fix_snippet": "// Suggested fix: log full error server-side; send a generic message to client\napp.use((err, req, res, next) => {\n    logger.error({ err }, 'Unhandled error');           // full detail \u2014 server only\n    res.status(500).json({ error: 'Internal server error' });  // generic to client\n});"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/joho/godotenv/godotenv.go`
**Scanned at**: 2026-10-11T16:25:44.248670+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 138 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 138
func Exec(filenames []string, cmd string, cmdArgs []string) error {
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 138, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/lib/pq/doc.go`
**Scanned at**: 2026-10-11T16:25:46.750842+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (3)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 78 |
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 168 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 21 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Hardcoded password literal detected
```go
// Line 78
"user=pqgotest password='with spaces'"
```
**Suggested fix:**
```go
# Suggested fix: load passwords from environment, hash with bcrypt
import os, bcrypt
# Never store plain-text passwords
password_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())
# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 168
After all data has been processed you should call Exec() once with no arguments
// Line 169
to flush all buffered data. Any call to Exec() might return an error which
// Line 171
returned by Exec() might not be related to the data passed in the call that
```
**Suggested fix:**
```go
# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)
import subprocess
# WRONG:  subprocess.call('ls ' + user_input, shell=True)
result = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe
# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()
```
> 💡 **Why**: Risk: This is the primary defense against code-level flaws. It directly blocks the introduction of vulnerabilities like those found in penetration tests (e.g., Insecure File Upload, IDOR logic). It shifts discovery from a late-stage pen test to the d
> 🔧 **Guidance**: A developer must remediate the flagged vulnerability (e.g., use a parameterized query instead of string concatenation) to meet the quality gate standards.
> [Full remediation →](https://verify.example-org.internal/?id=SAST-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```go
// Line 21
rows, err := db.Query("SELECT name FROM users WHERE age = $1", age)
// Line 111
rows, err := db.Query(`SELECT name FROM users WHERE favorite_fruit = $1
```
**Suggested fix:**
```go
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |

_+ 45 more applicable mandards — [view all 53 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 78, "message": "Hardcoded password literal detected", "fix_snippet": "# Suggested fix: load passwords from environment, hash with bcrypt\nimport os, bcrypt\n# Never store plain-text passwords\npassword_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())\n# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)"}, {"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 168, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 21, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/chatbot/src/mcpserver/server.py`
**Scanned at**: 2026-10-11T16:25:47.354350+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 48 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 48
verify=False,
// Line 91
verify=False,
// Line 113
async with httpx.AsyncClient(base_url=BASE_URL, verify=False) as client:
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 48, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/chatbot/src/mcpserver/auth/middleware.py`
**Scanned at**: 2026-10-11T16:25:50.673867+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest | 74 |

#### [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) — TLS/SSL certificate verification disabled
```py
// Line 74
async with httpx.AsyncClient(verify=False) as client:
// Line 107
async with httpx.AsyncClient(verify=False) as client:
```
**Suggested fix:**
```py
# Suggested fix: always verify TLS certificates
import requests
# WRONG:  requests.get(url, verify=False)
response = requests.get(url, verify=True)   # verify=True is default
# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'
```
> 💡 **Why**: Risk: Unencrypted data at rest is vulnerable to theft if storage is compromised, breached, or mishandled. Encryption ensures confidentiality even if physical access is gained.
> 🔧 **Guidance**: Configure encryption for all databases, file systems, and backups. Use AES-256 or better. Store encryption keys in a separate key management system.
> [Full remediation →](https://verify.example-org.internal/?id=CRYPT-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-001", "severity": "CRITICAL", "line": 74, "message": "TLS/SSL certificate verification disabled", "fix_snippet": "# Suggested fix: always verify TLS certificates\nimport requests\n# WRONG:  requests.get(url, verify=False)\nresponse = requests.get(url, verify=True)   # verify=True is default\n# For custom CA:  verify='/etc/ssl/certs/ca-bundle.crt'"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SCA-M-001", "title": "No Critical CVEs", "risk_level": "Critical"}, {"id": "SCA-M-002", "title": "Approved Licenses", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/identity/src/main/java/com/crapi/config/InitialDataConfig.java`
**Scanned at**: 2026-10-11T16:25:54.265304+00:00
**Mandard DB coverage**: 57 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) | Encryption in Transit (TLS 1.3+) | 113 |

#### [CRYPT-M-002](https://verify.example-org.internal/?id=CRYPT-M-002) — Non-cryptographic random number generator detected
```java
// Line 113
random = new Random();
```
**Suggested fix:**
```java
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |

_+ 48 more applicable mandards — [view all 56 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CRYPT-M-002", "severity": "MEDIUM", "line": 113, "message": "Non-cryptographic random number generator detected", "fix_snippet": "// Suggested fix: use a cryptographically secure RNG\n// WRONG:  const token = Math.random().toString(36);\nconst token = crypto.randomUUID();                          // browser / Node 19+\n// or:  const buf = crypto.getRandomValues(new Uint8Array(32));  // raw bytes\n# Python:  import secrets; token = secrets.token_urlsafe(32)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/api/models/comments.go`
**Scanned at**: 2026-10-11T16:25:53.351149+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 50 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```go
// Line 50
update := bson.D{{Key: "$set", Value: bson.D{{Key: "comments", Value: updatePost.Comments}}}}
```
**Suggested fix:**
```go
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 47 more applicable mandards — [view all 55 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 50, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/api/middlewares/middlewares.go`
**Scanned at**: 2026-10-11T16:26:00.714467+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) | Wildcard CORS origin (*) allows any domain | 30 |

#### [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) — Wildcard CORS origin (*) allows any domain
```go
// Line 30
w.Header().Set("Access-Control-Allow-Origin", "*")
// Line 43
w.Header().Set("Access-Control-Allow-Origin", "*")
```
**Suggested fix:**
```go
// Suggested fix: restrict CORS to an explicit allowlist
const cors = require('cors');
const allowed = ['https://app.example.com', 'https://admin.example.com'];
app.use(cors({
    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),
    credentials: true
}));
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | API-Specific Audit Logging & Monitoring |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |

_+ 47 more applicable mandards — [view all 55 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CORS-M-001", "severity": "HIGH", "line": 30, "message": "Wildcard CORS origin (*) allows any domain", "fix_snippet": "// Suggested fix: restrict CORS to an explicit allowlist\nconst cors = require('cors');\nconst allowed = ['https://app.example.com', 'https://admin.example.com'];\napp.use(cors({\n    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),\n    credentials: true\n}));"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/scope.go`
**Scanned at**: 2026-10-11T16:26:02.947272+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 360 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 360
func (scope *Scope) Exec() *Scope {
// Line 364
if result, err := scope.SQLDB().Exec(scope.SQL, scope.SQLVars...); scope.Err(err) == nil {
// Line 1161
scope.Err(scope.NewDB().Exec(fmt.Sprintf("CREATE TABLE %v (%v, PRIMARY KEY (%v))%s", scope.Quote(joinTable), strings.Join(sqlTypes, ","), strings.Join(primaryKeys, ","), scope.getTableOptions())).E...
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 360, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/main.go`
**Scanned at**: 2026-10-11T16:26:02.767963+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 499 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 499
func (s *DB) Exec(sql string, values ...interface{}) *DB {
// Line 504
return scope.Exec().db
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 499, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/join_table_handler.go`
**Scanned at**: 2026-10-11T16:26:05.562522+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 140 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 140
return db.Exec(sql, values...).Error
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 140, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/interface.go`
**Scanned at**: 2026-10-11T16:26:03.585448+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 10 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 10
Exec(query string, args ...interface{}) (sql.Result, error)
```
**Suggested fix:**
```go
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 10, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/dialect_postgres.go`
**Scanned at**: 2026-10-11T16:26:05.433714+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 96 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```go
// Line 96
s.db.QueryRow("SELECT count(*) FROM pg_indexes WHERE tablename = $1 AND indexname = $2 AND schemaname = CURRENT_SCHEMA()", tableName, indexName).Scan(&count)
// Line 102
s.db.QueryRow("SELECT count(con.conname) FROM pg_constraint con WHERE $1::regclass::oid = con.conrelid AND con.conname = $2 AND con.contype='f'", tableName, foreignKeyName).Scan(&count)
// Line 108
s.db.QueryRow("SELECT count(*) FROM INFORMATION_SCHEMA.tables WHERE table_name = $1 AND table_type = 'BASE TABLE' AND table_schema = CURRENT_SCHEMA()", tableName).Scan(&count)
```
**Suggested fix:**
```go
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |

_+ 47 more applicable mandards — [view all 55 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 96, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/dialect_mysql.go`
**Scanned at**: 2026-10-11T16:26:05.187004+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 133 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 133
_, err := s.db.Exec(fmt.Sprintf("DROP INDEX %v ON %v", indexName, s.Quote(tableName)))
// Line 138
_, err := s.db.Exec(fmt.Sprintf("ALTER TABLE %v MODIFY COLUMN %v %v", tableName, columnName, typ))
```
**Suggested fix:**
```go
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
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 133, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/dialect_common.go`
**Scanned at**: 2026-10-11T16:26:04.408160+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 110 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 110
_, err := s.db.Exec(fmt.Sprintf("DROP INDEX %v", indexName))
// Line 133
_, err := s.db.Exec(fmt.Sprintf("ALTER TABLE %v ALTER COLUMN %v TYPE %v", tableName, columnName, typ))
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [SECR-M-005](https://verify.example-org.internal/?id=SECR-M-005) | No Secrets in Build Logs |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 110, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/callback_update.go`
**Scanned at**: 2026-10-11T16:26:14.069738+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 106 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 106
)).Exec()
```
**Suggested fix:**
```go
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
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [ERR-M-003](https://verify.example-org.internal/?id=ERR-M-003) | .NET Custom Errors Enabled |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 106, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/callback_delete.go`
**Scanned at**: 2026-10-11T16:26:14.476235+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 46 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 46
)).Exec()
// Line 53
)).Exec()
```
**Suggested fix:**
```go
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
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [ERR-M-003](https://verify.example-org.internal/?id=ERR-M-003) | .NET Custom Errors Enabled |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 46, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/community/vendor/github.com/jinzhu/gorm/callback_create.go`
**Scanned at**: 2026-10-11T16:26:16.810645+00:00
**Mandard DB coverage**: 55 applicable mandards checked (SECR, AUTH, CRYPT, SAST, ERR, LOG…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 133 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```go
// Line 133
if result, err := scope.SQLDB().Exec(scope.SQL, scope.SQLVars...); scope.Err(err) == nil {
// Line 149
if result, err := scope.SQLDB().Exec(scope.SQL, scope.SQLVars...); scope.Err(err) == nil {
```
**Suggested fix:**
```go
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
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [DEP-M-002](https://verify.example-org.internal/?id=DEP-M-002) | Package Manager Lifecycle Script Hardening |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |

_+ 46 more applicable mandards — [view all 54 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 133, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/web/src/actions/userActions.ts`
**Scanned at**: 2026-10-11T16:26:31.540852+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | Stream Logs to SIEM | 122 |

#### [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) — Sensitive data logged to console
```ts
// Line 122
console.log("validateAccessTokenAction action");
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
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "LOG-M-001", "severity": "HIGH", "line": 122, "message": "Sensitive data logged to console", "fix_snippet": "// Suggested fix: never log credentials \u2014 log a masked reference instead\n// WRONG:  console.log('Auth', password, apiKey);\nconst logger = require('./logger');  // structured logger (e.g. winston, pino)\nlogger.info('Auth attempt', { userId, tokenPresent: !!apiKey });  // mask value"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `services/web/src/constants/actionTypes.ts`
**Scanned at**: 2026-10-11T16:26:57.660386+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 34 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Hardcoded credential in named variable detected
```ts
// Line 34
VALIDATE_ACCESS_TOKEN: "VALIDATE_ACCESS_TOKEN",
// Line 35
VALIDATED_ACCESS_TOKEN: "VALIDATED_ACCESS_TOKEN",
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
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 34, "message": "Hardcoded credential in named variable detected", "fix_snippet": "# Suggested fix: load all credentials from environment variables or a vault\nimport os\nJWT_SECRET = os.environ['JWT_SECRET']          # Python\n// const jwtSecret = process.env.JWT_SECRET;   // Node.js\n# Use Azure Key Vault / AWS Secrets Manager / HashiCorp Vault in production"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}]
-->

