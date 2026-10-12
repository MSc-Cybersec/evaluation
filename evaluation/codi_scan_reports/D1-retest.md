### SAGF Compliance Report — `DVWA-master/vulnerabilities/sqli/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/sqli/index.php`
**Scanned at**: 2026-10-11T16:47:22.419292+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [AUTH-M-003](https://verify.example-org.internal/?id=AUTH-M-003) | Session Management & Timeout Controls |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | Whitelist-Based Input Validation |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | Input Encoding & Output Encoding |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🔴 Critical | [OAUTH-M-001](https://verify.example-org.internal/?id=OAUTH-M-001) | OAuth 2.0 Token Security & Validation |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | SUSPECTED | arbitrary user ID input is accepted without visible server-side allowlist validation | 56 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | SUSPECTED | generated HTML is appended without visible contextual output encoding | 68 |
| 🔴 Critical | [DB-M-001](https://verify.example-org.internal/?id=DB-M-001) | SUSPECTED | selectable vulnerable SQL handlers are loaded without evidence of parameterized queries | 34 |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | SUSPECTED | user-selected object IDs are processed without visible object-level authorization | 56 |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | CONFIRMED | sequential numeric object identifiers are exposed | 52 |
| 🟠 High | [IDOR-M-003](https://verify.example-org.internal/?id=IDOR-M-003) | CONFIRMED | the default GET method places the object ID in the URL query string | 16 |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | SUSPECTED | no user or tenant context is visibly applied when processing the selected ID | 34 |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | inline event-handler JavaScript may require a weakened CSP | 42 |
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | SUSPECTED | the page dynamically enables handlers explicitly designed to contain SQL-injection vulnerabilities | 34 |