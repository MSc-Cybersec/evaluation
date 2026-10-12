### SAGF Compliance Report — `DVWA-master/vulnerabilities/csp/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/csp/index.php`
**Scanned at**: 2026-10-11T17:01:24.058855+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CFG-M-009](https://verify.example-org.internal/?id=CFG-M-009) | Policy and Tool Configuration as Code |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | Enforce X-Content-Type-Options |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | Enforce Referrer Policy |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | CSP behavior is delegated to security-level code not provided and is explicitly designed for bypass testing | 39 |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | SUSPECTED | response is emitted without visible `X-Content-Type-Options: nosniff` enforcement | 55 |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | SUSPECTED | response is emitted without visible `Referrer-Policy` enforcement | 55 |
| 🔴 Critical | [HDR-M-008](https://verify.example-org.internal/?id=HDR-M-008) | SUSPECTED | response is emitted without visible `Permissions-Policy` enforcement | 55 |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | SUSPECTED | response is emitted without visible `Cross-Origin-Resource-Policy` enforcement | 55 |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | SUSPECTED | response is emitted without visible `Cross-Origin-Embedder-Policy` enforcement | 55 |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | SUSPECTED | response is emitted without visible content type and charset enforcement | 55 |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | SUSPECTED | authenticated response lacks visible sensitive-data cache controls | 55 |
| 🔴 Critical | [HDR-M-003](https://verify.example-org.internal/?id=HDR-M-003) | SUSPECTED | response lacks visible HSTS enforcement | 55 |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | SUSPECTED | legacy `X-XSS-Protection` is not visibly disabled | 55 |