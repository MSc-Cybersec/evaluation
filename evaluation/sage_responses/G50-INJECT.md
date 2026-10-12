# G50-INJECT

## Question
Which controls are required to prevent command and query injection classes?

## Sage response

## Bottom line

The catalogue contains two controls directly applicable to command and query injection: **INJECT-M-002** for OS commands and **INJECT-M-001** for LDAP queries. **INJECT-M-003** is also in the Injection Prevention domain but addresses XXE rather than command/query injection and applies only where XML is processed. No specific Mandard was found for SQL, NoSQL, XPath, or XQuery injection; this is a catalogue gap that should be addressed before claiming comprehensive injection-class coverage.

## Risk and impact

| Priority | Exposure | Business impact |
|---|---|---|
| Critical | User-controlled data reaches an operating-system command interpreter | Remote code execution, host compromise, credential theft, data loss, and lateral movement |
| High | User-controlled data is concatenated into LDAP filters | Authentication bypass, unauthorized directory access, and directory traversal |
| Critical when XML applies | XML parsers resolve DTDs or external entities | File disclosure, server-side request forgery, and denial of service |
| Unverified catalogue coverage | SQL, NoSQL, XPath, and XQuery injection | Data disclosure or modification, authorization bypass, and service compromise |

## Governing mandards

| Mandard | Title | Risk | Required control |
|---|---|---:|---|
| **INJECT-M-002** | OS Command Injection Prevention | **Critical** | Per **INJECT-M-002**: user input must not be executed as an OS command. Use APIs that separate executable and arguments, prohibit shell interpretation such as `shell=True`, and allowlist permitted commands and parameters. |
| **INJECT-M-003** | XML External Entity XXE Prevention | **Critical** | Per **INJECT-M-003**: XML parsers must disable DTD processing and external-entity expansion, use safe parser configurations, and validate XML input. This is conditional on XML processing and is not itself a command/query control. |
| **INJECT-M-001** | LDAP Injection Prevention | **High** | Per **INJECT-M-001**: LDAP queries must use parameterized or prepared mechanisms where supported, otherwise RFC 4515 LDAP escaping. Special characters must be escaped, direct concatenation is prohibited, and anonymous binds must not be used. |

No suitable Mandard was found for SQL, NoSQL, XPath, or XQuery injection. A new or expanded Mandard is required if those query technologies are in scope.

## Framework mapping

Only catalogue-returned mappings are shown.

| Mandard | Framework mappings |
|---|---|
| **INJECT-M-002** | NIST SP 800-53 Rev.5: `SI-10`, `SI-15`, `SA-11`; PCI DSS v4.0: `Req 6`; ISO/IEC 27001:2022: `A.8.26`, `A.8.28`; OWASP ASVS 5.0: `V1`, `V13`; OWASP Top 10:2025: `A02:2025`, `A05:2025`; CIS Controls v8: `CIS 16`; CWE: `CWE-20`, `CWE-77`, `CWE-78`, `CWE-94` |
| **INJECT-M-003** | NIST SP 800-53 Rev.5: `AC-4`, `SC-5`, `SC-7`, `SC-8`, `SI-4`, `SI-7`, `SI-10`, `SI-15`, `SA-11`; PCI DSS v4.0: `Req 1`, `Req 6`; ISO/IEC 27001:2022: `A.8.20`, `A.8.22`, `A.8.26`, `A.8.28`; OWASP ASVS 5.0: `V1`, `V4`, `V13`; OWASP Top 10:2025: `A01:2025`, `A02:2025`, `A05:2025` |
| **INJECT-M-001** | NIST SP 800-53 Rev.5: `IA-2`, `IA-4`, `IA-5`, `IA-8`, `AC-7`, `SI-10`, `SI-15`, `SA-11`; PCI DSS v4.0: `Req 6`, `Req 8`; ISO/IEC 27001:2022: `A.5.16`, `A.5.17`, `A.8.5`, `A.8.26`, `A.8.28`; OWASP ASVS 5.0: `V1`, `V6`, `V13`; OWASP Top 10:2025: `A02:2025`, `A05:2025`, `A07:2025` |

## Required actions

1. **Application engineering — Critical:** Enforce **INJECT-M-002** wherever applications invoke operating-system processes. Remove shell-based execution, pass arguments as discrete values, and restrict executable and parameter choices through allowlists.
2. **Application engineering — Critical where applicable:** Enforce **INJECT-M-003** for every XML parser. Disable DTDs, external entities, XInclude, and entity expansion; validate expected XML structure.
3. **Identity and application engineering — High:** Enforce **INJECT-M-001** for LDAP access. Replace filter concatenation with LDAP-aware query builders or RFC 4515 escaping and require authenticated binds.
4. **Security architecture/GRC:** Identify every database and query interpreter in scope. SQL, NoSQL, XPath, and XQuery currently have no dedicated catalogue Mandard; initiate a Mandard addition or formally document the coverage gap.
5. **DevSecOps:** Configure SAST pipeline gates for unsafe shell execution, concatenated LDAP filters, and insecure XML parser initialization.

No knowledge document was found that is mapped to **INJECT-M-001**, **INJECT-M-002**, or **INJECT-M-003** for implementation procedures. The steps above are taken from the Mandard catalogue itself.

## Evidence for audit

- Passing SAST results showing no unsafe shell invocation, LDAP filter concatenation, or insecure XML parser configuration.
- CI/CD configuration demonstrating that Critical and High injection findings block release.
- Code-review records showing use of argument-array process APIs and LDAP-aware query builders or escaping.
- XML parser configuration or automated tests proving that DTDs and external entities are rejected.
- Inventory of query technologies, including SQL, NoSQL, LDAP, XPath/XQuery, and operating-system process execution.
- Approved deviation record in the SAF pack for any non-compliance, with technical justification and accountable risk acceptance.
- Catalogue-gap record or approved draft Mandard covering SQL, NoSQL, XPath, and XQuery injection.

## Assumptions and limits

The application technology stack and actual use of LDAP, XML, SQL, NoSQL, XPath, XQuery, or operating-system commands were not provided. SQL, NoSQL, XPath, and XQuery coverage could not be established from the current Mandard catalogue. The knowledge search returned tangential application and authentication governance documents, but no implementation document mapped to the three Injection Prevention Mandards.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**INJECT-M-001**](https://verify.example-org.internal/?id=INJECT-M-001) | High | Injection Prevention | CIS_CONTROLS (CIS 16, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-20, CWE-77, CWE-89); ISO_27001 (A.5.16, A.5.17, A.8.26); NIST_CSF (PR.AA-01, PR.AA-05, PR.DS-01); NIST_SP_800_53 (AC-7, IA-2, IA-4); +6 more |
| [**INJECT-M-002**](https://verify.example-org.internal/?id=INJECT-M-002) | Critical | Injection Prevention | CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-77, CWE-78); ISO_27001 (A.8.26, A.8.28); NIST_CSF (PR.DS-01, PR.PS-01); NIST_SP_800_53 (SA-11, SI-10, SI-15); OWASP (A02:2025, A05:2025); +5 more |
| [**INJECT-M-003**](https://verify.example-org.internal/?id=INJECT-M-003) | Critical | Injection Prevention | CIS_CONTROLS (CIS 12, CIS 16); CWE (CWE-20, CWE-77, CWE-918); ISO_27001 (A.8.20, A.8.22, A.8.26); NIST_CSF (DE.CM-01, PR.DS-01, PR.PS-01); NIST_SP_800_53 (AC-4, SA-11, SC-5); OWASP (A01:2025, A02:2025, A05:2025); +6 more |

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