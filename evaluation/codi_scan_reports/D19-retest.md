### SAGF Compliance Report — `DVWA-master/vulnerabilities/weak_id/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/weak_id/index.php`
**Scanned at**: 2026-10-11T17:12:16.932650+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | Secure Cookie Attributes (HttpOnly, Secure, SameSite) |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [COOK-M-002](https://verify.example-org.internal/?id=COOK-M-002) | Cookie Theft Prevention & Rotation |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | CONFIRMED | endpoint intentionally loads implementations that generate weak session identifiers | 33 |
| 🔴 Critical | [COOK-M-001](https://verify.example-org.internal/?id=COOK-M-001) | SUSPECTED | cookie-setting implementation is external and secure attributes cannot be verified | 33 |
| 🟠 High | [COOK-M-002](https://verify.example-org.internal/?id=COOK-M-002) | SUSPECTED | weak session identifiers may enable cookie prediction or theft | 33 |
| 🔴 Critical | [CFG-M-003](https://verify.example-org.internal/?id=CFG-M-003) | SUSPECTED | Secure, HttpOnly, and SameSite cookie flags are not demonstrably enforced | 33 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | SUSPECTED | `$html` is inserted into the response without contextual output encoding | 46 |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | SUSPECTED | `X-Content-Type-Options` is not visibly enforced before output | 64 |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | no Content Security Policy is visibly enforced | 64 |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | SUSPECTED | response Content-Type and charset are not visibly enforced | 64 |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | SUSPECTED | authenticated response lacks visible sensitive-data cache controls | 64 |
| 🔴 Critical | [HDR-M-003](https://verify.example-org.internal/?id=HDR-M-003) | SUSPECTED | HSTS is not visibly enforced | 64 |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | SUSPECTED | legacy `X-XSS-Protection` is not visibly disabled | 64 |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | SUSPECTED | Referrer-Policy is not visibly enforced | 64 |
| 🔴 Critical | [HDR-M-008](https://verify.example-org.internal/?id=HDR-M-008) | SUSPECTED | Permissions-Policy is not visibly enforced | 64 |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | SUSPECTED | Cross-Origin-Resource-Policy is not visibly enforced | 64 |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | SUSPECTED | Cross-Origin-Embedder-Policy is not visibly enforced | 64 |