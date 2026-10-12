### SAGF Compliance Report — `DVWA-master/vulnerabilities/sqli_blind/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli_blind/index.php`
**Scanned at**: 2026-10-11T17:09:16.390407+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | Opaque Object Identifiers |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SUSPECTED | dynamically selected handlers intentionally include vulnerable SQL-injection implementations | 34 |
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | SUSPECTED | SQL-injection-prone handlers are enabled by security-level routing | 18 |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | SUSPECTED | arbitrary user ID input is accepted without visible whitelist validation | 71 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | SUSPECTED | handler-generated HTML is rendered without visible contextual encoding | 83 |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | SUSPECTED | object IDs are user-controlled without visible object-level authorization | 71 |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | CONFIRMED | predictable sequential user identifiers are exposed | 67 |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | CONFIRMED | the default GET method exposes the user ID in the URL | 16 |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | SUSPECTED | only authentication is enforced; no user or tenant context is visibly applied to ID queries | 6 |