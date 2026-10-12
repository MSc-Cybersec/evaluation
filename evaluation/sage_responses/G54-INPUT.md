# G54-INPUT

## Question
What governance policy defines acceptable input-validation standards?

## Sage response

## Bottom line

The SAGF catalogue defines acceptable input-validation standards through the **INPUT-M** control family, rather than a single mapped governance-policy document. The primary requirement is **INPUT-M-001**, supported by **INPUT-M-002** and **INPUT-M-003**; applications must implement all applicable controls to reduce injection, cross-site scripting, denial-of-service, and malformed-input exposure.

## Risk and impact

Failure to enforce these controls can allow untrusted input to alter application behaviour, execute injected content, traverse paths, or exhaust system resources. The catalogue rates validation and encoding failures **High**, and missing input-size restrictions **Medium**.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **INPUT-M-001** | Whitelist-Based Input Validation | High | Per **INPUT-M-001**: validate all user input server-side against field-specific allowlists, reject non-conforming values, and use anchored patterns where regular expressions are used. |
| **INPUT-M-002** | Input Encoding & Output Encoding | High | Per **INPUT-M-002**: encode untrusted input for its destination context—such as HTML, JavaScript, URL, or CSS—using established encoding libraries rather than manual escaping. |
| **INPUT-M-003** | Input Length & Size Limits | Medium | Per **INPUT-M-003**: enforce server-side maximum lengths for fields, file uploads, and request bodies, with limits appropriate to their purpose. |

## Framework mapping

Directly relevant mappings returned by the catalogue include:

| Mandard | Framework controls |
|---|---|
| **INPUT-M-001** | NIST SP 800-53 Rev. 5 `SI-10`, `SA-11`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V1`, `V13`; CIS Controls v8 `CIS 16`; CWE `CWE-20`, `CWE-22`, `CWE-94` |
| **INPUT-M-002** | NIST SP 800-53 Rev. 5 `SI-10`, `SA-11`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V1`, `V13`; CIS Controls v8 `CIS 16`; CWE `CWE-20` |
| **INPUT-M-003** | NIST SP 800-53 Rev. 5 `SI-10`, `SA-11`; PCI DSS v4.0 `Req 6`; ISO/IEC 27001:2022 `A.8.26`, `A.8.28`; OWASP ASVS 5.0 `V1`, `V4`, `V13`; OWASP API Security 2023 `API4`; CIS Controls v8 `CIS 16` |

## Required actions

1. **Application owners:** document an allowlist and rejection rule for every externally supplied field.
2. **Developers:** enforce validation and size constraints server-side; client-side validation may supplement but cannot replace it.
3. **Developers:** apply context-specific output encoding through approved framework or library functions.
4. **Engineering assurance:** add negative security tests covering malformed, oversized, encoded, and injection-oriented inputs.
5. **DevSecOps:** gate releases on applicable static, dynamic, fuzz, and security-unit-test results.

## Evidence for audit

Retain:

- API schemas or validated data models showing patterns, types, `maxLength`, and request-size constraints.
- Unit and integration test results demonstrating rejection of invalid and oversized input.
- SAST/DAST and fuzz-testing reports covering injection and encoding weaknesses.
- CI/CD gate records showing that failed validation-security checks block release.
- Approved exception or deviation records for any unmet control.

## Assumptions and limits

No knowledge document was found for this point: none is currently mapped through `mandard_refs` to **INPUT-M-001**, **INPUT-M-002**, or **INPUT-M-003**. A Web Services guardrail references the Example Org Application Security Standard and OWASP for injection risk, but the retrieved evidence does not establish that document as the authoritative implementation mapping for these three mandards.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**INPUT-M-001**](https://verify.example-org.internal/?id=INPUT-M-001) | High | Input Validation | CIS_CONTROLS (CIS 16); CSA_CCM (AIS); CWE (CWE-20, CWE-22, CWE-94); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (SA-11, SI-10); +7 more |
| [**INPUT-M-002**](https://verify.example-org.internal/?id=INPUT-M-002) | High | Input Validation | CIS_CONTROLS (CIS 16); CWE (CWE-20); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (SA-11, SI-10); OWASP (A02:2025); +5 more |
| [**INPUT-M-003**](https://verify.example-org.internal/?id=INPUT-M-003) | Medium | Input Validation | CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-770); ISO_27001 (A.8.26, A.8.28); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, SA-11, SC-8); OWASP (A02:2025); +6 more |

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