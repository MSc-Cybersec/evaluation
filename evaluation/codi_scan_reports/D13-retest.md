### SAGF Compliance Report — `DVWA-master/vulnerabilities/fi/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/fi/index.php`
**Scanned at**: 2026-10-11T17:04:35.874397+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DB-M-004](https://verify.example-org.internal/?id=DB-M-004) | Database Security Hardening and Configuration |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | Content Security Policy CSP |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | Cache-Control for Sensitive Data |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | Excessive Data Exposure Prevention |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | SUSPECTED | dynamic file inclusion may permit local or remote file inclusion | 36 |
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | SUSPECTED | included file path is not visibly constrained to an allowlist | 36 |