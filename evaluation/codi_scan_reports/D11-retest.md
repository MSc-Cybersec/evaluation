### SAGF Compliance Report — `DVWA-master/vulnerabilities/csrf/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csrf/index.php`
**Scanned at**: 2026-10-11T17:02:10.162387+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | Cross-Origin-Resource-Policy (CORP) |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | CONFIRMED | password-changing GET request exposes credentials and permits CSRF; tokens are conditionally omitted | 54 |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | SUSPECTED | authentication is required, but no authorization check protects the admin password-change function | 6 |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | SUSPECTED | password hashing is delegated to dynamically selected code without assurance of a secure algorithm | 32 |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | SUSPECTED | password parameters are accepted without visible server-side validation or password-policy enforcement | 64 |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | SUSPECTED | CSRF protection appears to rely on browser SameSite defaults rather than explicitly secured cookies | 77 |
| 🔴 Critical | [CFG-M-003](https://verify.example-org.internal/?id=CFG-M-003) | SUSPECTED | explicit Secure, HttpOnly, and SameSite cookie configuration is not demonstrated | 77 |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | SUSPECTED | sensitive credentials are submitted in the URL and no no-store cache policy is visible | 54 |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | inline JavaScript and an inline event handler require a weakened CSP unless hashes or nonces are configured externally | 35 |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | SUSPECTED | no Referrer-Policy is visible while password values can enter the request URL | 54 |