### SAGF Compliance Report — `DVWA-master/vulnerabilities/api/index.php`

## SAGF Compliance Scan: `DVWA-master/vulnerabilities/api/index.php`
**Scanned at**: 2026-10-11T16:54:20.654889+00:00
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
### 🤖 AI Semantic Analysis
_Checked all 80 applicable advisory mandards against this code:_

| Risk | Mandard | Status | Finding | Line |
|------|---------|--------|---------|------|
| 🟠 High | [API-M-008](https://verify.example-org.internal/?id=API-M-008) | CONFIRMED | runtime security level can load intentionally weaker API implementations | 17 |
| 🟠 High | [INPUT-M-002](https://verify.example-org.internal/?id=INPUT-M-002) | SUSPECTED | HTML from the included implementation is interpolated without explicit output encoding | 55 |
| 🔴 Critical | [API-M-006](https://verify.example-org.internal/?id=API-M-006) | SUSPECTED | no API rate-limiting enforcement is visible | 68 |
| 🟠 High | [API-M-010](https://verify.example-org.internal/?id=API-M-010) | SUSPECTED | no API-specific security audit logging is visible | 68 |
| 🔴 Critical | [HDR-M-014](https://verify.example-org.internal/?id=HDR-M-014) | SUSPECTED | no Content-Security-Policy enforcement is visible | 68 |
| 🔴 Critical | [HDR-M-001](https://verify.example-org.internal/?id=HDR-M-001) | SUSPECTED | no X-Content-Type-Options enforcement is visible | 68 |
| 🔴 Critical | [HDR-M-003](https://verify.example-org.internal/?id=HDR-M-003) | SUSPECTED | no HSTS enforcement is visible | 68 |
| 🔴 Critical | [HDR-M-005](https://verify.example-org.internal/?id=HDR-M-005) | SUSPECTED | legacy X-XSS-Protection is not explicitly disabled | 68 |
| 🔴 Critical | [HDR-M-007](https://verify.example-org.internal/?id=HDR-M-007) | SUSPECTED | no Referrer-Policy enforcement is visible | 68 |
| 🔴 Critical | [HDR-M-008](https://verify.example-org.internal/?id=HDR-M-008) | SUSPECTED | no Permissions-Policy enforcement is visible | 68 |
| 🟠 High | [HDR-M-009](https://verify.example-org.internal/?id=HDR-M-009) | SUSPECTED | authenticated content lacks visible sensitive-data cache controls | 68 |
| 🔴 Critical | [HDR-M-011](https://verify.example-org.internal/?id=HDR-M-011) | SUSPECTED | no Cross-Origin-Resource-Policy enforcement is visible | 68 |
| 🔴 Critical | [HDR-M-012](https://verify.example-org.internal/?id=HDR-M-012) | SUSPECTED | no Cross-Origin-Embedder-Policy enforcement is visible | 68 |
| 🟠 High | [HDR-M-006](https://verify.example-org.internal/?id=HDR-M-006) | SUSPECTED | response content type and charset are not explicitly enforced | 68 |