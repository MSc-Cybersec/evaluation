# G16-CORS

## Question
When is wildcard CORS prohibited and what is the safe alternative?

## Sage response

## Bottom line

Wildcard CORS (`Access-Control-Allow-Origin: *`) is prohibited for SAGF-controlled APIs because **CORS-M-001** requires a static allowlist of approved origins and rejects both wildcards and arbitrary origin reflection. It is especially unsafe for authenticated or sensitive endpoints; the safe alternative is exact-origin allowlisting, returning the requesting origin only after a strict match.

## Risk and impact

**High risk.** A permissive or reflected CORS policy can allow a malicious website to issue cross-origin requests from a victim’s browser and potentially access sensitive responses using the victim’s authenticated session.

Separately, browsers do not permit `Access-Control-Allow-Origin: *` with credentialed CORS requests. For public, non-credentialed resources a wildcard may be valid under the web standard, but it does **not** comply with the SAGF control retrieved here.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---|
| **CORS-M-001** | No Reflected Origin (CORS) | High |

Per **CORS-M-001**: `Access-Control-Allow-Origin` must not contain `*` or reflect an arbitrary request `Origin`; the server must use a static whitelist of approved domains.

## Framework mapping

**CORS-M-001** maps to the following retrieved controls:

- NIST SP 800-53 Rev. 5: `CM-6`, `SI-10`, `SA-11`, `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SC-8`, `SC-18`
- PCI DSS v4.0: `Req 6`, `Req 10`

## Required actions

1. **Application/API owner:** Define an explicit allowlist using complete origins, including scheme, hostname, and non-default port where applicable.
2. **Backend engineer:** Compare the supplied `Origin` against that allowlist and emit `Access-Control-Allow-Origin` only for an exact match.
3. Do not dynamically echo the request’s `Origin`, use weak suffix matching, or treat `null` as trusted.
4. Enable `Access-Control-Allow-Credentials: true` only where operationally required and only with explicitly approved origins.
5. **DevSecOps:** Add a pipeline test that sends untrusted origins and fails if the response returns `*` or echoes the untrusted value.

```javascript
const allowedOrigins = new Set([
  'https://app.example.com',
  'https://admin.example.com'
]);

const corsOptions = {
  origin(origin, callback) {
    if (origin && allowedOrigins.has(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Origin not allowed'));
    }
  },
  credentials: true
};

app.use(cors(corsOptions));
```

No knowledge document currently references **CORS-M-001**. The exact-match and credential-minimisation details above are **Advisory (not knowledge-doc backed)** where they extend beyond the Mandard’s explicit whitelist requirement.

## Evidence for audit

Retain:

- The approved origin allowlist and change history.
- Application or gateway CORS configuration.
- CI/CD DAST results from OWASP ZAP or an equivalent scanner.
- Negative tests proving an attacker-controlled origin receives neither `Access-Control-Allow-Origin: *` nor a reflected origin.
- Any formally approved exception or deviation record.

## Assumptions and limits

No CORS-specific implementation knowledge document was found. Unrelated authentication documents returned by the knowledge search were set aside because they do not provide CORS implementation guidance.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**CORS-M-001**](https://verify.example-org.internal/?id=CORS-M-001) | High | CORS Policy | CIS_CONTROLS (CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-20); HIPAA (164.312(b)); ISO_27001 (A.8.15, A.8.16, A.8.26); NIST_CSF (DE.AE-02, DE.CM-01, PR.DS-01); +8 more |

Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
## Scoring notes
- actionability: pass (provisional auto-score)
- citation_correctness: pass (provisional auto-score)
- evidence_audit: pass (provisional auto-score)
- framework_mapping: pass (provisional auto-score)
- risk_impact: pass (provisional auto-score)
- bottom_line: pass (provisional auto-score)
- governing_mandards: pass (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass