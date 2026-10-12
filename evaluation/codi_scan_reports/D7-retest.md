### SAGF Compliance Report — `DVWA-master/vulnerabilities/bac/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/bac/index.php`
**Scanned at**: 2026-10-11T16:55:48.404637+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | Broken Function Level Authorization (BFLA) |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | Broken Object Level Authorization (BOLA/IDOR) Prevention |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | Context-Aware Data Queries |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | Database Access Control & Least Privilege |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | Sensitive Data Masking and Fine-Grained Access |
| 🟠 High | [IDOR-M-005](https://verify.example-org.internal/?id=IDOR-M-005) | IDOR Test Coverage Matrix |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | Log Authorization Failures |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🔴 Critical | [API-M-003](https://verify.example-org.internal/?id=API-M-003) | CONFIRMED | any authenticated user can access the log-viewing function without role authorization | 51 |
| 🔴 Critical | [API-M-001](https://verify.example-org.internal/?id=API-M-001) | CONFIRMED | all log objects are returned without ownership or authorization filtering | 51 |
| 🔴 Critical | [IDOR-M-001](https://verify.example-org.internal/?id=IDOR-M-001) | CONFIRMED | records associated with arbitrary users are exposed without object-level authorization | 51 |
| 🔴 Critical | [IDOR-M-004](https://verify.example-org.internal/?id=IDOR-M-004) | CONFIRMED | query lacks user, role, or tenant context restrictions | 51 |
| 🟠 High | [DB-M-003](https://verify.example-org.internal/?id=DB-M-003) | CONFIRMED | runtime web code performs privileged schema alterations, implying excessive database permissions | 33 |
| 🟠 High | [DB-M-006](https://verify.example-org.internal/?id=DB-M-006) | CONFIRMED | usernames, identifiers, and IP addresses are displayed without masking or fine-grained access control | 69 |
| 🟠 High | [IDOR-M-002](https://verify.example-org.internal/?id=IDOR-M-002) | CONFIRMED | predictable numeric object and user identifiers are exposed | 68 |
| 🟠 High | [IDOR-M-006](https://verify.example-org.internal/?id=IDOR-M-006) | CONFIRMED | no authorization decision occurs, so unauthorized log-access attempts cannot be recorded | 51 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | CONFIRMED | database values are interpolated into HTML without contextual output encoding | 69 |
| 🔴 Critical | [API-M-002](https://verify.example-org.internal/?id=API-M-002) | CONFIRMED | the response exposes unrestricted access-log records and IP addresses | 71 |
| 🔴 Critical | [SAST-M-001](https://verify.example-org.internal/?id=SAST-M-001) | CONFIRMED | unencoded database content creates a stored cross-site scripting finding | 69 |