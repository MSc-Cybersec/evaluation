# SAGF Workspace Scan Results

**Files Found**: 179
**Files Scanned**: 179
**Files Skipped** (>500KB): 0
**Files with Violations**: 53
**Errors**: 0

## 🚨 Files with Mandard Violations

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/test_credentials.php`
**Scanned at**: 2026-10-11T16:21:38.919169+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 19 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 21 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 19
$pass = md5( $pass );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 21
$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [CFG-M-002](https://verify.example-org.internal/?id=CFG-M-002) | Disable Autocomplete on Sensitive Fields |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 19, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 21, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/login.php`
**Scanned at**: 2026-10-11T16:21:39.492100+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 27 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 39 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 27
$pass = md5( $pass );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 39
$query  = "SELECT * FROM `users` WHERE user='$user' AND password='$pass';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 27, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 39, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/xss_s/source/medium.php`
**Scanned at**: 2026-10-11T16:21:38.293375+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 18
$query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [DB-M-002](https://verify.example-org.internal/?id=DB-M-002) | Database Encryption (At-Rest & In-Transit) |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/setup.php`
**Scanned at**: 2026-10-11T16:21:38.480353+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 51 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 51
$git_log = shell_exec ("git -c 'safe.directory=*' log -1");
// Line 59
$out = shell_exec ("apachectl -M | grep rewrite_module");
```
**Suggested fix:**
```php
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
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [FILE-M-001](https://verify.example-org.internal/?id=FILE-M-001) | File Upload Type Validation & Scanning |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 51, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/xss_s/source/low.php`
**Scanned at**: 2026-10-11T16:21:38.628132+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 16 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 16
$query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [DB-M-002](https://verify.example-org.internal/?id=DB-M-002) | Database Encryption (At-Rest & In-Transit) |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 16, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/xss_s/source/high.php`
**Scanned at**: 2026-10-11T16:21:37.443854+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 18 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 18
$query  = "INSERT INTO guestbook ( comment, name ) VALUES ( '$message', '$name' );";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [DB-M-002](https://verify.example-org.internal/?id=DB-M-002) | Database Encryption (At-Rest & In-Transit) |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/dvwa/js/dvwaPage.js`
**Scanned at**: 2026-10-11T16:21:39.042309+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 7 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 7
//eval("page" + id + " = window.open(URL, '" + id + "', 'toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=800,height=300,left=540,top=250');");
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
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [COOK-M-002](https://verify.example-org.internal/?id=COOK-M-002) | Cookie Theft Prevention & Rotation |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DEP-M-003](https://verify.example-org.internal/?id=DEP-M-003) | Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion) |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 7, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/source/medium.php`
**Scanned at**: 2026-10-11T16:21:39.703001+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 14 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 18 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 14
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 18
$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 14, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 18, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/source/low.php`
**Scanned at**: 2026-10-11T16:21:42.008351+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 12 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 16 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 12
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 16
$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . $current_user . "';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 12, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 16, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/source/impossible.php`
**Scanned at**: 2026-10-11T16:21:41.834702+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 15 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 15
$pass_curr = md5( $pass_curr );
// Line 29
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 15, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/source/high.php`
**Scanned at**: 2026-10-11T16:21:40.499681+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 39 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 43 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 39
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 43
$insert = "UPDATE `users` SET password = '" . $pass_new . "' WHERE user = '" . $current_user . "';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [FILE-M-001](https://verify.example-org.internal/?id=FILE-M-001) | File Upload Type Validation & Scanning |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 39, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 43, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/dvwa/includes/dvwaPage.inc.php`
**Scanned at**: 2026-10-11T16:21:43.330854+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 651 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 651
$_SESSION[ 'session_token' ] = md5( uniqid() );
```
**Suggested fix:**
```php
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
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 651, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/gen_openapi.php`
**Scanned at**: 2026-10-11T16:21:41.144264+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) | No Reflected Origin (CORS) | 6 |

#### [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) — Wildcard CORS origin (*) allows any domain
```php
// Line 6
header("Access-Control-Allow-Origin: *");
```
**Suggested fix:**
```php
// Suggested fix: restrict CORS to an explicit allowlist
const cors = require('cors');
const allowed = ['https://app.example.com', 'https://admin.example.com'];
app.use(cors({
    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),
    credentials: true
}));
```
> 💡 **Why**: Risk: A reflective CORS policy allows *any* malicious site to make authenticated requests from a logged-in user's browser, bypassing the Same-Origin Policy and stealing their data. This was a critical finding.
> 🔧 **Guidance**: A developer must configure the API backend to use a strict whitelist of allowed domains for CORS, and *never* reflect the `Origin` header from the request.
> [Full remediation →](https://verify.example-org.internal/?id=CORS-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | Cross-Origin-Embedder-Policy (COEP) |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CORS-M-001", "severity": "HIGH", "line": 6, "message": "Wildcard CORS origin (*) allows any domain", "fix_snippet": "// Suggested fix: restrict CORS to an explicit allowlist\nconst cors = require('cors');\nconst allowed = ['https://app.example.com', 'https://admin.example.com'];\napp.use(cors({\n    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),\n    credentials: true\n}));"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/brute/source/medium.php`
**Scanned at**: 2026-10-11T16:21:42.282103+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 11 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 14 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 11
$pass = md5( $pass );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 14
$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 11, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 14, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/brute/source/low.php`
**Scanned at**: 2026-10-11T16:21:42.158975+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 9 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 12 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 9
$pass = md5( $pass );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 12
$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 9, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 12, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/brute/source/impossible.php`
**Scanned at**: 2026-10-11T16:21:42.954513+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 16 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 16
$pass = md5( $pass );
```
**Suggested fix:**
```php
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
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 16, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/brute/source/high.php`
**Scanned at**: 2026-10-11T16:21:42.614077+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 16 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 19 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 16
$pass = md5( $pass );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 19
$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 16, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 19, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/public/index.php`
**Scanned at**: 2026-10-11T16:21:44.829393+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) | No Reflected Origin (CORS) | 11 |

#### [CORS-M-001](https://verify.example-org.internal/?id=CORS-M-001) — Wildcard CORS origin (*) allows any domain
```php
// Line 11
header("Access-Control-Allow-Origin: *");
```
**Suggested fix:**
```php
// Suggested fix: restrict CORS to an explicit allowlist
const cors = require('cors');
const allowed = ['https://app.example.com', 'https://admin.example.com'];
app.use(cors({
    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),
    credentials: true
}));
```
> 💡 **Why**: Risk: A reflective CORS policy allows *any* malicious site to make authenticated requests from a logged-in user's browser, bypassing the Same-Origin Policy and stealing their data. This was a critical finding.
> 🔧 **Guidance**: A developer must configure the API backend to use a strict whitelist of allowed domains for CORS, and *never* reflect the `Origin` header from the request.
> [Full remediation →](https://verify.example-org.internal/?id=CORS-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "CORS-M-001", "severity": "HIGH", "line": 11, "message": "Wildcard CORS origin (*) allows any domain", "fix_snippet": "// Suggested fix: restrict CORS to an explicit allowlist\nconst cors = require('cors');\nconst allowed = ['https://app.example.com', 'https://admin.example.com'];\napp.use(cors({\n    origin: (origin, cb) => allowed.includes(origin) ? cb(null, true) : cb(new Error('Not allowed')),\n    credentials: true\n}));"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/index.php`
**Scanned at**: 2026-10-11T16:21:46.795161+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 33 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 33
$out = shell_exec ("apachectl -M | grep rewrite_module");
```
**Suggested fix:**
```php
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
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [CFG-M-009](https://verify.example-org.internal/?id=CFG-M-009) | Policy and Tool Configuration as Code |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 33, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/dvwa/includes/DBMS/MySQL.php`
**Scanned at**: 2026-10-11T16:21:45.837762+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 55 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 55
('1','admin','admin','admin',MD5('password'),'{$avatarUrl}admin.jpg', NOW(), '0'),
// Line 56
('2','Gordon','Brown','gordonb',MD5('abc123'),'{$avatarUrl}gordonb.jpg', NOW(), '0'),
// Line 57
('3','Hack','Me','1337',MD5('charley'),'{$avatarUrl}1337.jpg', NOW(), '0'),
```
**Suggested fix:**
```php
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 55, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/dvwa/includes/DBMS/PGSQL.php`
**Scanned at**: 2026-10-11T16:21:46.644063+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 61 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 61
('1','admin','admin','admin',MD5('password'),'{$baseUrl}admin.jpg'),
// Line 62
('2','Gordon','Brown','gordonb',MD5('abc123'),'{$baseUrl}gordonb.jpg'),
// Line 63
('3','Hack','Me','1337',MD5('charley'),'{$baseUrl}1337.jpg'),
```
**Suggested fix:**
```php
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 61, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/src/Login.php`
**Scanned at**: 2026-10-11T16:21:46.358425+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets | 10 |

#### [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) — Potential hardcoded secret detected
```php
// Line 10
private const ACCESS_TOKEN_SECRET = "12345";
// Line 12
private const REFRESH_TOKEN_SECRET = "98765";
```
**Suggested fix:**
```php
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
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [OAUTH-M-001](https://verify.example-org.internal/?id=OAUTH-M-001) | OAuth 2.0 Token Security & Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SECR-M-001", "severity": "CRITICAL", "line": 10, "message": "Potential hardcoded secret detected", "fix_snippet": "# Suggested fix: store secrets in environment variables, never in code\nimport os\nAPI_KEY = os.environ['API_KEY']        # Python\n# const apiKey = process.env.API_KEY   # Node.js\n# $apiKey = getenv('API_KEY');          # PHP\n# Use Azure Key Vault, HashiCorp Vault, or AWS Secrets Manager in production."}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/bac/source/medium.php`
**Scanned at**: 2026-10-11T16:21:48.578513+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 7 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 7
$query = "SELECT user_id FROM users WHERE user = '" . dvwaCurrentUser() . "';";
// Line 21
$check_query = "SELECT user_id FROM users WHERE user_id = '$id'";
// Line 28
$query = "SELECT first_name, last_name, user_id, avatar FROM users WHERE user_id = '$id';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 7, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/bac/source/low.php`
**Scanned at**: 2026-10-11T16:21:49.040026+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 7 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 7
$query = "SELECT user_id, role FROM users WHERE user = '" . dvwaCurrentUser() . "';";
// Line 22
$check_query = "SELECT user_id FROM users WHERE user_id = $id";
// Line 35
$query = "SELECT first_name, last_name, user_id, avatar FROM users WHERE user_id = $id;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [CFG-M-003](https://verify.example-org.internal/?id=CFG-M-003) | Secure Cookie Flags |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 7, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/src/HealthController.php`
**Scanned at**: 2026-10-11T16:21:49.784538+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 88 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 88
exec ("ping -c 4 " . $target, $output, $ret_var);
```
**Suggested fix:**
```php
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
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [FILE-M-001](https://verify.example-org.internal/?id=FILE-M-001) | File Upload Type Validation & Scanning |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 88, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/cryptography/source/oracle_attack.php`
**Scanned at**: 2026-10-11T16:21:51.066030+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 57 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 57
$response = curl_exec($ch);
```
**Suggested fix:**
```php
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
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [API-M-013](https://verify.example-org.internal/?id=API-M-013) | Message-Level Integrity and Confidentiality |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🔴 Critical | [CRYPT-M-001](https://verify.example-org.internal/?id=CRYPT-M-001) | Encryption at Rest |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 57, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/authbypass/change_user_details.php`
**Scanned at**: 2026-10-11T16:21:52.839651+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 47 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 47
$query = "UPDATE users SET first_name = '" . $data->first_name . "', last_name = '" .  $data->surname . "' where user_id = " . $data->id . "";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 47, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/authbypass/authbypass.js`
**Scanned at**: 2026-10-11T16:21:53.387216+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL query built by string interpolation or concatenation | 49 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```js
// Line 49
cell3.innerHTML = '<input type="button" value="Update" onclick="submit_change(' + user['user_id'] + ')" />';
```
**Suggested fix:**
```js
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
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |

_+ 56 more applicable mandards — [view all 64 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 49, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli/test.php`
**Scanned at**: 2026-10-11T16:21:52.967965+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 4 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Hardcoded password literal detected
```php
// Line 4
$password = "password";
```
**Suggested fix:**
```php
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
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [DB-M-002](https://verify.example-org.internal/?id=DB-M-002) | Database Encryption (At-Rest & In-Transit) |
| 🔴 Critical | [INJECT-M-002](https://verify.example-org.internal/?id=INJECT-M-002) | OS Command Injection Prevention |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 4, "message": "Hardcoded password literal detected", "fix_snippet": "# Suggested fix: load passwords from environment, hash with bcrypt\nimport os, bcrypt\n# Never store plain-text passwords\npassword_hash = bcrypt.hashpw(os.environ['USER_PASSWORD'].encode(), bcrypt.gensalt())\n# Verify: bcrypt.checkpw(supplied_password.encode(), password_hash)"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csp/help/help.php`
**Scanned at**: 2026-10-11T16:21:54.179486+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | External CDN dependency detected | 25 |

#### [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) — External CDN dependency detected
```php
// Line 25
https://cdn.jsdelivr.net/gh/digininja/csp_bypass/alert.js - Using jsDelivr to server a JavaScript file stored on GitHub.
// Line 26
https://unpkg.com/@digininja/csp_bypass@1.0.0/index.js - Using UNPKG to access a JavaScript file in an NPM package.
```
**Suggested fix:**
```php
# Suggested fix: bundle and pin all dependencies locally
# Install:  npm install tailwindcss@3.4.1
# Reference the locally bundled file:
# <script src="/assets/js/tailwind.min.js"></script>  <!-- served from your own origin -->
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | Cross-Origin-Embedder-Policy (COEP) |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DEP-M-001", "severity": "MEDIUM", "line": 25, "message": "External CDN dependency detected", "fix_snippet": "# Suggested fix: bundle and pin all dependencies locally\n# Install:  npm install tailwindcss@3.4.1\n# Reference the locally bundled file:\n# <script src=\"/assets/js/tailwind.min.js\"></script>  <!-- served from your own origin -->"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csp/source/low.php`
**Scanned at**: 2026-10-11T16:21:56.978696+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟡 MEDIUM | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | External CDN dependency detected | 3 |

#### [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) — External CDN dependency detected
```php
// Line 3
$headerCSP = "Content-Security-Policy: script-src 'self' https://pastebin.com hastebin.com www.toptal.com example.com code.jquery.com https://ssl.google-analytics.com unpkg.com cdn.jsdelivr.net dig...
// Line 8
# https://cdn.jsdelivr.net/gh/digininja/csp_bypass/alert.js
// Line 9
# https://unpkg.com/@digininja/csp_bypass@1.0.0/index.js
```
**Suggested fix:**
```php
# Suggested fix: bundle and pin all dependencies locally
# Install:  npm install tailwindcss@3.4.1
# Reference the locally bundled file:
# <script src="/assets/js/tailwind.min.js"></script>  <!-- served from your own origin -->
```

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | Enforce Referrer Policy |
| 🔴 Critical | [HDR-M-008](https://verify.example-org.internal/?id=HDR-M-008) | Enforce Permissions Policy |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DEP-M-001", "severity": "MEDIUM", "line": 3, "message": "External CDN dependency detected", "fix_snippet": "# Suggested fix: bundle and pin all dependencies locally\n# Install:  npm install tailwindcss@3.4.1\n# Reference the locally bundled file:\n# <script src=\"/assets/js/tailwind.min.js\"></script>  <!-- served from your own origin -->"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/view_help.php`
**Scanned at**: 2026-10-11T16:21:55.835814+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 20 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 20
eval( '?>' . file_get_contents( DVWA_WEB_PAGE_TO_ROOT . "vulnerabilities/{$id}/help/help.php" ) . '<?php ' );
// Line 22
eval( '?>' . file_get_contents( DVWA_WEB_PAGE_TO_ROOT . "vulnerabilities/{$id}/help/help.{$locale}.php" ) . '<?php ' );
```
**Suggested fix:**
```php
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
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [FILE-M-001](https://verify.example-org.internal/?id=FILE-M-001) | File Upload Type Validation & Scanning |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | Enforce Content-Type and Charset |
| 🔴 Critical | [API-M-005](https://verify.example-org.internal/?id=API-M-005) | Auth on Sensitive API |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [OAUTH-M-001](https://verify.example-org.internal/?id=OAUTH-M-001) | OAuth 2.0 Token Security & Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 20, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/upload/source/impossible.php`
**Scanned at**: 2026-10-11T16:21:56.819038+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 18 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 18
$target_file   =  md5( uniqid() . $uploaded_name ) . '.' . $uploaded_ext;
// Line 20
$temp_file    .= DIRECTORY_SEPARATOR . md5( uniqid() . $uploaded_name ) . '.' . $uploaded_ext;
```
**Suggested fix:**
```php
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
| 🟠 High | [FILE-M-001](https://verify.example-org.internal/?id=FILE-M-001) | File Upload Type Validation & Scanning |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [SAST-M-002](https://verify.example-org.internal/?id=SAST-M-002) | Secure File Upload Validation |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | Multi-Factor Authentication (MFA) Enforcement |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 18, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/javascript/index.php`
**Scanned at**: 2026-10-11T16:21:57.260054+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 43 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 43
if ($token == md5(str_rot13("success"))) {
```
**Suggested fix:**
```php
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
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🟠 High | [API-M-013](https://verify.example-org.internal/?id=API-M-013) | Message-Level Integrity and Confidentiality |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [OAUTH-M-001](https://verify.example-org.internal/?id=OAUTH-M-001) | OAuth 2.0 Token Security & Validation |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 43, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli/source/medium.php`
**Scanned at**: 2026-10-11T16:21:57.406685+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 11 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 11
$query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
// Line 27
$query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🔴 Critical | [DB-M-002](https://verify.example-org.internal/?id=DB-M-002) | Database Encryption (At-Rest & In-Transit) |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 11, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli/source/low.php`
**Scanned at**: 2026-10-11T16:21:58.295457+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 10 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 10
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
// Line 31
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 10, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli/source/high.php`
**Scanned at**: 2026-10-11T16:21:59.478915+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 10 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 10
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
// Line 28
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 10, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/javascript/source/low.php`
**Scanned at**: 2026-10-11T16:22:00.184184+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 18 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 18
document.getElementById("token").value = md5(rot13(phrase));
```
**Suggested fix:**
```php
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
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 18, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/javascript/source/high_unobfuscated.js`
**Scanned at**: 2026-10-11T16:22:01.714064+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 83 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 83
var crypto = eval("require('crypto')");
// Line 84
var Buffer = eval("require('buffer').Buffer");
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
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 83, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/javascript/source/high.js`
**Scanned at**: 2026-10-11T16:22:01.835797+00:00
**Mandard DB coverage**: 64 applicable mandards checked (SECR, SAST, HDR, CORS, INPUT, INJECT…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 1 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```js
// Line 1
var a=['fromCharCode','toString','replace','BeJ','\x5cw+','Lyg','SuR','(w(){\x273M\x203L\x27;q\x201l=\x273K\x203I\x203J\x20T\x27;q\x201R=1c\x202I===\x271n\x27;q\x20Y=1R?2I:{};p(Y.3N){1R=1O}q\x202L=...
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
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [SAST-M-006](https://verify.example-org.internal/?id=SAST-M-006) | Native Memory Safety and Unsafe Code Assurance |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🔴 Critical | [DEP-M-001](https://verify.example-org.internal/?id=DEP-M-001) | Pin Dependency Versions in Production Builds |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |

_+ 55 more applicable mandards — [view all 63 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 1, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DEP-M-001", "title": "Pin Dependency Versions in Production Builds", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "DEP-M-002", "title": "Package Manager Lifecycle Script Hardening", "risk_level": "High"}, {"id": "DEP-M-003", "title": "Dependency Name-Confusion Defense (Typosquatting, Slopsquatting, Dependency Confusion)", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AJAX-M-002", "title": "AJAX Response Sanitization & XSS Prevention", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "AJAX-M-001", "title": "AJAX Request Validation & CSRF Protection", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/captcha/source/impossible.php`
**Scanned at**: 2026-10-11T16:22:00.653923+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 14 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 14
$pass_new  = md5( $pass_new );
// Line 19
$pass_conf = md5( $pass_conf );
// Line 24
$pass_curr = md5( $pass_curr );
```
**Suggested fix:**
```php
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
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 14, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/captcha/source/high.php`
**Scanned at**: 2026-10-11T16:22:00.019308+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 27 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 30 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 27
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 30
$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "' LIMIT 1;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 27, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 30, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/captcha/source/low.php`
**Scanned at**: 2026-10-11T16:22:00.403085+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 57 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 60 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 57
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 60
$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 57, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 60, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/captcha/source/medium.php`
**Scanned at**: 2026-10-11T16:22:01.280659+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (2)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 65 |
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 68 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 65
$pass_new = md5( $pass_new );
```
**Suggested fix:**
```php
# Suggested fix: use a salted key derivation function for passwords
import bcrypt
password_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
# Non-credential digests (checksums, cache keys): use hashlib.sha256()
```
> 💡 **Why**: Risk: If a password database is breached, using weak or unsalted hashes (like MD5 or SHA1) allows attackers to use 'rainbow tables' to crack millions of passwords in seconds. Strong KDFs make this computationally infeasible.
> 🔧 **Guidance**: A developer must refactor the authentication code to use a modern, approved library for password hashing (e.g., `spring-security-crypto`) and not use deprecated functions like `java.security.MessageDigest.getInstance("MD5")`.
> [Full remediation →](https://verify.example-org.internal/?id=AUTH-M-001)

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 68
$insert = "UPDATE `users` SET password = '$pass_new' WHERE user = '" . dvwaCurrentUser() . "';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-011](https://verify.example-org.internal/?id=API-M-011) | GraphQL Query Complexity Limits |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |

_+ 83 more applicable mandards — [view all 91 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 65, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}, {"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 68, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli_blind/source/high.php`
**Scanned at**: 2026-10-11T16:22:03.229392+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 11 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 11
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
// Line 33
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id' LIMIT 1;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 11, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli_blind/source/low.php`
**Scanned at**: 2026-10-11T16:22:02.796416+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 11 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 11
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
// Line 32
$query  = "SELECT first_name, last_name FROM users WHERE user_id = '$id';";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 11, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli_blind/source/medium.php`
**Scanned at**: 2026-10-11T16:22:03.502375+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SQL Injection Prevention (Parameterized Queries) | 13 |

#### [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) — SQL query built by string interpolation or concatenation
```php
// Line 13
$query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
// Line 34
$query  = "SELECT first_name, last_name FROM users WHERE user_id = $id;";
```
**Suggested fix:**
```php
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
> 💡 **Why**: Risk: SQL injection allows database compromise. Parameterized queries separate code from data.
> 🔧 **Guidance**: Use prepared statements exclusively. Never concatenate user input into queries.
> [Full remediation →](https://verify.example-org.internal/?id=DB-M-001)

### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | IDOR Protection |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | Avoid Exposing IDs in URLs |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |
| 🟠 High | [IDOR-M-007](https://verify.example-org.internal/?id=IDOR-M-007) | Validate Nested Resource Ownership |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "DB-M-001", "severity": "CRITICAL", "line": 13, "message": "SQL query built by string interpolation or concatenation", "fix_snippet": "# Suggested fix: always use parameterised queries\n# WRONG (PHP):  $q = \"SELECT * FROM users WHERE id = '$id'\";\n# WRONG (Py):   query = 'SELECT * FROM users WHERE id = ' + user_id\n# Python (psycopg2 / sqlite3):\ncursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))\n# PHP (PDO):  $s = $pdo->prepare('SELECT * FROM users WHERE id = ?'); $s->execute([$id]);\n# Node.js (pg):  pool.query('SELECT * FROM users WHERE id = $1', [userId])\n# Java:  PreparedStatement ps = conn.prepareStatement('SELECT * FROM users WHERE id = ?');\n#        ps.setInt(1, userId);"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/weak_id/source/impossible.php`
**Scanned at**: 2026-10-11T16:22:04.925710+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 6 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function SHA-1 detected
```php
// Line 6
$cookie_value = sha1(mt_rand() . time() . "Impossible");
```
**Suggested fix:**
```php
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
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [COOK-M-002](https://verify.example-org.internal/?id=COOK-M-002) | Cookie Theft Prevention & Rotation |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [CFG-M-003](https://verify.example-org.internal/?id=CFG-M-003) | Secure Cookie Flags |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 6, "message": "Deprecated hash function SHA-1 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/weak_id/source/high.php`
**Scanned at**: 2026-10-11T16:22:06.785095+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🔴 CRITICAL | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing | 10 |

#### [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) — Deprecated hash function MD5 detected
```php
// Line 10
$cookie_value = md5($_SESSION['last_session_id_high']);
```
**Suggested fix:**
```php
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
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [COOK-M-002](https://verify.example-org.internal/?id=COOK-M-002) | Cookie Theft Prevention & Rotation |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [HDR-M-002](https://verify.example-org.internal/?id=HDR-M-002) | No Server Banners |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🔴 Critical | [CFG-M-003](https://verify.example-org.internal/?id=CFG-M-003) | Secure Cookie Flags |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "AUTH-M-001", "severity": "CRITICAL", "line": 10, "message": "Deprecated hash function MD5 detected", "fix_snippet": "# Suggested fix: use a salted key derivation function for passwords\nimport bcrypt\npassword_hash = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())\n# Non-credential digests (checksums, cache keys): use hashlib.sha256()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-001", "title": "No Critical SAST Findings", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/exec/source/high.php`
**Scanned at**: 2026-10-11T16:22:07.582171+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 26 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 26
$cmd = shell_exec( 'ping  ' . $target );
// Line 30
$cmd = shell_exec( 'ping  -c 4 ' . $target );
```
**Suggested fix:**
```php
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
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 26, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/exec/source/low.php`
**Scanned at**: 2026-10-11T16:22:07.391977+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 10 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 10
$cmd = shell_exec( 'ping  ' . $target );
// Line 14
$cmd = shell_exec( 'ping  -c 4 ' . $target );
```
**Suggested fix:**
```php
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
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 10, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/exec/source/medium.php`
**Scanned at**: 2026-10-11T16:22:08.293697+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 19 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 19
$cmd = shell_exec( 'ping  ' . $target );
// Line 23
$cmd = shell_exec( 'ping  -c 4 ' . $target );
```
**Suggested fix:**
```php
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
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🟠 High | [CRYPT-M-004](https://verify.example-org.internal/?id=CRYPT-M-004) | Algorithm Selection & Post-Quantum Readiness |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 19, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

---

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/exec/source/impossible.php`
**Scanned at**: 2026-10-11T16:22:07.721783+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### 🚨 Confirmed Violations (1)
| Sev | Mandard | Title | Line |
|-----|---------|-------|------|
| 🟠 HIGH | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | No Critical SAST Findings | 22 |

#### [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) — Dangerous code execution function detected
```php
// Line 22
$cmd = shell_exec( 'ping  ' . $target );
// Line 26
$cmd = shell_exec( 'ping  -c 4 ' . $target );
```
**Suggested fix:**
```php
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
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | Rate Limiting Enforced |
| 🔴 Critical | [INJECT-M-003](https://verify.example-org.internal/?id=INJECT-M-003) | XML External Entity (XXE) Prevention |
| 🟠 High | [INJECT-M-001](https://verify.example-org.internal/?id=INJECT-M-001) | LDAP Injection Prevention |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |

_+ 84 more applicable mandards — [view all 92 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.

<!-- CODI_FINDINGS_JSON
[{"mandard_id": "SAST-M-001", "severity": "HIGH", "line": 22, "message": "Dangerous code execution function detected", "fix_snippet": "# Suggested fix: avoid eval/exec; use subprocess with a list (no shell=True)\nimport subprocess\n# WRONG:  subprocess.call('ls ' + user_input, shell=True)\nresult = subprocess.run(['ls', user_input], capture_output=True, text=True)  # safe\n# For dynamic config: use ast.literal_eval() or json.loads() instead of eval()"}]
-->

<!-- CODI_ADVISORY_JSON
[{"id": "INJECT-M-002", "title": "OS Command Injection Prevention", "risk_level": "Critical"}, {"id": "AUTH-M-003", "title": "Session Management & Timeout Controls", "risk_level": "High"}, {"id": "INPUT-M-001", "title": "Whitelist-Based Input Validation", "risk_level": "High"}, {"id": "INPUT-M-002", "title": "Input Encoding & Output Encoding", "risk_level": "High"}, {"id": "API-M-006", "title": "Rate Limiting Enforced", "risk_level": "Critical"}, {"id": "INJECT-M-003", "title": "XML External Entity (XXE) Prevention", "risk_level": "Critical"}, {"id": "INJECT-M-001", "title": "LDAP Injection Prevention", "risk_level": "High"}, {"id": "AUTH-M-001", "title": "Secure Password Hashing", "risk_level": "Critical"}, {"id": "AUTH-M-002", "title": "Multi-Factor Authentication (MFA) Enforcement", "risk_level": "Critical"}, {"id": "IDOR-M-001", "title": "IDOR Protection", "risk_level": "Critical"}, {"id": "IDOR-M-004", "title": "Context-Aware Data Queries", "risk_level": "Critical"}, {"id": "OAUTH-M-001", "title": "OAuth 2.0 Token Security & Validation", "risk_level": "Critical"}, {"id": "AUTH-M-004", "title": "Password Reset & Account Recovery", "risk_level": "High"}, {"id": "CRYPT-M-004", "title": "Algorithm Selection & Post-Quantum Readiness", "risk_level": "High"}, {"id": "IDOR-M-002", "title": "Opaque Object Identifiers", "risk_level": "High"}, {"id": "IDOR-M-003", "title": "Avoid Exposing IDs in URLs", "risk_level": "High"}, {"id": "IDOR-M-005", "title": "IDOR Test Coverage Matrix", "risk_level": "High"}, {"id": "IDOR-M-006", "title": "Log Authorization Failures", "risk_level": "High"}, {"id": "IDOR-M-007", "title": "Validate Nested Resource Ownership", "risk_level": "High"}, {"id": "API-M-001", "title": "Broken Object Level Authorization (BOLA/IDOR) Prevention", "risk_level": "Critical"}, {"id": "API-M-002", "title": "Excessive Data Exposure Prevention", "risk_level": "Critical"}, {"id": "API-M-003", "title": "Broken Function Level Authorization (BFLA)", "risk_level": "Critical"}, {"id": "API-M-004", "title": "Mass Assignment Protection", "risk_level": "Critical"}, {"id": "API-M-005", "title": "Auth on Sensitive API", "risk_level": "Critical"}, {"id": "API-M-007", "title": "JWT Signature Validation", "risk_level": "Critical"}, {"id": "API-M-011", "title": "GraphQL Query Complexity Limits", "risk_level": "Critical"}, {"id": "COOK-M-001", "title": "Secure Cookie Attributes (HttpOnly, Secure, SameSite)", "risk_level": "Critical"}, {"id": "SECR-M-001", "title": "No Hardcoded Secrets", "risk_level": "Critical"}, {"id": "SECR-M-002", "title": "Prevent Secret Exposure in CI/CD Logs and History", "risk_level": "Critical"}, {"id": "SECR-M-004", "title": "Short-Lived Credentials & Rotation", "risk_level": "Critical"}, {"id": "SECR-M-005", "title": "No Secrets in Build Logs", "risk_level": "Critical"}, {"id": "API-M-008", "title": "API Security Configuration Baseline", "risk_level": "High"}, {"id": "API-M-009", "title": "API Inventory & Versioning Management", "risk_level": "High"}, {"id": "API-M-010", "title": "API-Specific Audit Logging & Monitoring", "risk_level": "High"}, {"id": "API-M-012", "title": "Disable Introspection in Production", "risk_level": "High"}, {"id": "API-M-013", "title": "Message-Level Integrity and Confidentiality", "risk_level": "High"}, {"id": "COOK-M-002", "title": "Cookie Theft Prevention & Rotation", "risk_level": "High"}, {"id": "SECR-M-003", "title": "Enforce Temporary Credentials and Credential Rotation in CI/CD", "risk_level": "High"}, {"id": "CFG-M-002", "title": "Disable Autocomplete on Sensitive Fields", "risk_level": "Critical"}, {"id": "CFG-M-003", "title": "Secure Cookie Flags", "risk_level": "Critical"}, {"id": "CFG-M-008", "title": "Cryptographic Agility (External Algorithm Management)", "risk_level": "Critical"}, {"id": "CRYPT-M-001", "title": "Encryption at Rest", "risk_level": "Critical"}, {"id": "CRYPT-M-002", "title": "Encryption in Transit (TLS 1.3+)", "risk_level": "Critical"}, {"id": "DB-M-001", "title": "SQL Injection Prevention (Parameterized Queries)", "risk_level": "Critical"}, {"id": "DB-M-002", "title": "Database Encryption (At-Rest & In-Transit)", "risk_level": "Critical"}, {"id": "ERR-M-003", "title": ".NET Custom Errors Enabled", "risk_level": "Critical"}, {"id": "HDR-M-001", "title": "Enforce X-Content-Type-Options", "risk_level": "Critical"}, {"id": "HDR-M-002", "title": "No Server Banners", "risk_level": "Critical"}, {"id": "HDR-M-003", "title": "Enforce HSTS", "risk_level": "Critical"}, {"id": "HDR-M-005", "title": "Disable Legacy X-XSS-Protection Filter", "risk_level": "Critical"}, {"id": "HDR-M-007", "title": "Enforce Referrer Policy", "risk_level": "Critical"}, {"id": "HDR-M-008", "title": "Enforce Permissions Policy", "risk_level": "Critical"}, {"id": "HDR-M-011", "title": "Cross-Origin-Resource-Policy (CORP)", "risk_level": "Critical"}, {"id": "HDR-M-012", "title": "Cross-Origin-Embedder-Policy (COEP)", "risk_level": "Critical"}, {"id": "HDR-M-014", "title": "Content Security Policy CSP", "risk_level": "Critical"}, {"id": "SAML-M-001", "title": "SAML Assertion Validation & Signature", "risk_level": "Critical"}, {"id": "SAST-M-002", "title": "Secure File Upload Validation", "risk_level": "Critical"}, {"id": "SAST-M-003", "title": "Disable XXE Processing", "risk_level": "Critical"}, {"id": "SAST-M-004", "title": "Prevent Insecure Deserialization", "risk_level": "Critical"}, {"id": "SAST-M-005", "title": "Prevent Mass Assignment", "risk_level": "Critical"}, {"id": "SAST-M-006", "title": "Native Memory Safety and Unsafe Code Assurance", "risk_level": "Critical"}, {"id": "CFG-M-009", "title": "Policy and Tool Configuration as Code", "risk_level": "High"}, {"id": "CORS-M-001", "title": "No Reflected Origin (CORS)", "risk_level": "High"}, {"id": "CRYPT-M-003", "title": "Key Rotation & Lifecycle Management", "risk_level": "High"}, {"id": "CRYPT-M-005", "title": "Certificate Management & Pinning", "risk_level": "High"}, {"id": "CRYPT-M-006", "title": "Hardware Security Module (HSM) for High-Value Keys", "risk_level": "High"}, {"id": "DB-M-003", "title": "Database Access Control & Least Privilege", "risk_level": "High"}, {"id": "DB-M-004", "title": "Database Security Hardening and Configuration", "risk_level": "High"}, {"id": "DB-M-005", "title": "Database Activity Monitoring and Audit Logging", "risk_level": "High"}, {"id": "DB-M-006", "title": "Sensitive Data Masking and Fine-Grained Access", "risk_level": "High"}, {"id": "FILE-M-001", "title": "File Upload Type Validation & Scanning", "risk_level": "High"}, {"id": "FILE-M-002", "title": "File Storage & Execution Prevention", "risk_level": "High"}, {"id": "HDR-M-006", "title": "Enforce Content-Type and Charset", "risk_level": "High"}, {"id": "HDR-M-009", "title": "Cache-Control for Sensitive Data", "risk_level": "High"}, {"id": "LOG-M-001", "title": "Stream Logs to SIEM", "risk_level": "High"}, {"id": "LOG-M-002", "title": "Implement Comprehensive CI/CD Audit Logging", "risk_level": "High"}, {"id": "LOG-M-003", "title": "Configure Centralized Log Aggregation and SIEM Alerting for CI/CD", "risk_level": "High"}, {"id": "LOG-M-004", "title": "Trusted Time Synchronization for Security Events", "risk_level": "High"}, {"id": "OAUTH-M-002", "title": "OAuth 2.0 Scope Limitation & Consent", "risk_level": "High"}, {"id": "SAML-M-002", "title": "SAML Encryption & Attribute Protection", "risk_level": "High"}]
-->

