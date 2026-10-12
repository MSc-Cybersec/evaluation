### SAGF Compliance Report — `DVWA-master/vulnerabilities/brute/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/brute/index.php`
**Scanned at**: 2026-10-11T16:52:11.072919+00:00
**Mandard DB coverage**: 93 applicable mandards checked (SECR, AUTH, CRYPT, SAST, HDR, ERR…)
**Attestation**: `eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ0aW1lc3RhbXAiOiA...`

### ✅ No violations detected by static pattern analysis


### ⚠️ Most Relevant Mandards Requiring Tool Verification
_Ranked by relevance to this code. Static scan did not detect violations — use the SAGF Tier 2 toolchain to verify:_

| Risk | Mandard | Title |
|------|---------|-------|
| 🟠 High | [SECR-M-003](https://verify.example-org.internal/?id=SECR-M-003) | Enforce Temporary Credentials and Credential Rotation in CI/CD |
| 🟠 High | [AUTH-M-004](https://verify.example-org.internal/?id=AUTH-M-004) | Password Reset & Account Recovery |
| 🔴 Critical | [SECR-M-002](https://verify.example-org.internal/?id=SECR-M-002) | Prevent Secret Exposure in CI/CD Logs and History |
| 🔴 Critical | [SECR-M-004](https://verify.example-org.internal/?id=SECR-M-004) | Short-Lived Credentials & Rotation |
| 🟠 High | [CRYPT-M-006](https://verify.example-org.internal/?id=CRYPT-M-006) | Hardware Security Module (HSM) for High-Value Keys |
| 🔴 Critical | [AUTH-M-001](https://verify.example-org.internal/?id=AUTH-M-001) | Secure Password Hashing |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | Trusted Time Synchronization for Security Events |
| 🔴 Critical | [SECR-M-001](https://verify.example-org.internal/?id=SECR-M-001) | No Hardcoded Secrets |

_+ 85 more applicable mandards — [view all 93 in SAGF UI →](https://verify.example-org.internal/)_

> Run SonarQube, Snyk, Semgrep, and other SAGF Tier 2 tools for comprehensive coverage per SAGF-STD-004.
### 🤖 AI Semantic Analysis
_Checked all 81 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🟠 High | [INPUT-M-001](https://verify.example-org.internal/?id=INPUT-M-001) | CONFIRMED | username accepts arbitrary POST input without whitelist validation | 107 |
| 🔴 Critical | [AUTH-M-002](https://verify.example-org.internal/?id=AUTH-M-002) | CONFIRMED | MFA uses one process-wide secret instead of a per-user secret | 72 |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | SUSPECTED | IP-only throttling permits distributed brute-force attempts and shared-IP denial of service | 108 |
| 🔴 Critical | [CFG-M-008](https://verify.example-org.internal/?id=CFG-M-008) | CONFIRMED | cryptographic algorithm SHA-1 is hardcoded and not externally configurable | 79 |
| 🟠 High | [CRYPT-M-003](https://verify.example-org.internal/?id=CRYPT-M-003) | SUSPECTED | MFA secret has no visible rotation or lifecycle mechanism | 72 |
| 🟠 High | [LOG-M-001](https://verify.example-org.internal/?id=LOG-M-001) | SUSPECTED | security events use local `error_log` without demonstrated SIEM streaming | 23 |
| 🟠 High | [LOG-M-004](https://verify.example-org.internal/?id=LOG-M-004) | SUSPECTED | audit timestamps rely on the local system clock without trusted synchronization assurance | 21 |