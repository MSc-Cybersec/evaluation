### SAGF Compliance Report — `DVWA-master/vulnerabilities/authbypass/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/authbypass/index.php`
**Scanned at**: 2026-10-11T16:49:43.252026+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | CONFIRMED | admin-only functionality checks authentication but not the admin role | 6 |
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | CONFIRMED | critical function-level authorization weakness is present | 6 |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | SUSPECTED | user-management operations lack visible per-user object authorization | 64 |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | SUSPECTED | user records are populated without visible ownership or role checks | 64 |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | SUSPECTED | no context-aware restriction of queried user records is evident | 64 |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | SUSPECTED | user data may be exposed without fine-grained admin access control | 64 |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | SUSPECTED | user identifiers are directly exposed in the management table | 54 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | SUSPECTED | `$html` is appended without explicit contextual output encoding | 70 |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | inline JavaScript has no visible CSP nonce or hash protection | 63 |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | SUSPECTED | no sensitive-response cache-control enforcement is visible | 75 |