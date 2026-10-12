# G76-LLM

## Question
What controls are required before exposing an LLM endpoint to employees?

## Sage response

## Bottom line

Do not expose the LLM endpoint to employees until all five LLM Mandards have been addressed; **LLM-M-003** applies when retrieval-augmented generation is used. The highest exposures are sensitive-data disclosure and prompt injection, both rated **Critical**. Release should be blocked until control tests and configuration evidence demonstrate compliance.

## Risk and impact

- **Critical:** Employee prompts, retrieved content, or model responses could expose PII, financial data, credentials, system instructions, or other confidential information.
- **High:** Unvalidated output could introduce malicious content into browsers or downstream systems; poisoned RAG content could manipulate responses; uncontrolled access could cause unauthorized use, denial of service, and excessive cost.
- Internal employee access does not remove these risks: compromised accounts, malicious insiders, and accidental submission of sensitive data remain relevant.

## Governing mandards

### Required controls — source: Mandard catalogue

| Mandard | Title | Risk | Requirement before exposure |
|---|---|---:|---|
| **LLM-M-001** | LLM Prompt Injection Prevention | Critical | Per **LLM-M-001**: validate and sanitize direct prompts, external content, and encoded data; separate user data from system instructions and test for prompt injection. |
| **LLM-M-005** | Sensitive Data Handling in LLM Contexts | Critical | Per **LLM-M-005**: classify data before processing; prevent prohibited sensitive data from reaching the model; encrypt permitted data and enforce retention requirements. |
| **LLM-M-002** | LLM Output Validation & Sanitization | High | Per **LLM-M-002**: treat model output as untrusted and validate, sanitize, encode, redact, or block it before display or downstream use. |
| **LLM-M-003** | RAG System Poisoning Prevention | High | Per **LLM-M-003**: where RAG is used, protect knowledge sources with access controls, validate documents before indexing, verify integrity, and filter retrieved content. |
| **LLM-M-004** | LLM Model Access & Rate Limiting | High | Per **LLM-M-004**: authenticate and authorize every request and enforce per-user or per-key rate limits, quotas, generation limits, and usage monitoring. |

No LLM Mandard in the retrieved domain set separately mandates human approval or a formal go-live committee decision.

## Framework mapping

The following are directly returned mappings relevant to this deployment; this is not presented as an exhaustive list.

| Mandard | Returned framework mappings |
|---|---|
| **LLM-M-001** | NIST SP 800-53 Rev.5: SI-10, SA-11, SI-4; ISO/IEC 27001:2022: A.8.26, A.8.28; OWASP ASVS 5.0: V1 |
| **LLM-M-002** | NIST SP 800-53 Rev.5: SI-10, SA-11, SI-4; ISO/IEC 27001:2022: A.8.26, A.8.28; OWASP LLM: LLM05 |
| **LLM-M-003** | NIST SP 800-53 Rev.5: AC-3, AC-4, AC-6, SA-11; OWASP LLM: LLM04 |
| **LLM-M-004** | NIST SP 800-53 Rev.5: IA-2, AC-3, AC-6, SI-4; PCI DSS v4.0: Requirements 7 and 8; ISO/IEC 27001:2022: A.8.5 |
| **LLM-M-005** | NIST SP 800-53 Rev.5: SC-13, SI-12, AU-2, AU-6, AU-12, PT-3; PCI DSS v4.0: Requirements 3, 4, and 10; ISO/IEC 27001:2022: A.5.34, A.8.11, A.8.15, A.8.16 |

## Required actions

1. **Protect sensitive data — Security and Data Owners**
   - Implement input-path data classification, data minimization, and detection or redaction of PII, PHI, financial data, and credentials.
   - Use an approved model endpoint with documented retention and model-training-use settings.
   - Encrypt transport and define retention and deletion periods.
   - Block prohibited data classes before model invocation.
   - Mandard basis: **LLM-M-005**.

2. **Prevent prompt injection — Application Security and Engineering**
   - Validate direct prompts, uploaded documents, external content, and encoded input.
   - Use parameterized prompt templates with explicit separation between system instructions, retrieved content, and user data.
   - Test direct and indirect prompt-injection scenarios, including system-prompt extraction and instruction override attempts.
   - Mandard basis: **LLM-M-001**.

3. **Control model output — Engineering**
   - Treat every response as untrusted.
   - Apply context-aware encoding before browser rendering.
   - Validate machine-consumed output against a strict schema.
   - Detect and block or redact credentials, sensitive data, system prompts, malicious markup, and unexpected executable content.
   - Mandard basis: **LLM-M-002**.

4. **Enforce access and consumption controls — IAM and Platform Engineering**
   - Place the endpoint behind authenticated enterprise access.
   - Enforce RBAC and least privilege before requests reach model inference.
   - Apply per-user and per-IP or per-key rate limits and usage quotas.
   - Set input and output token limits and monitor rejected requests, anomalous use, and consumption.
   - Mandard basis: **LLM-M-004**.

5. **Secure RAG, if present — Data Platform and Knowledge Owners**
   - Restrict write access to knowledge bases and vector stores.
   - Separate ingestion and query roles.
   - Validate trusted sources and sanitize documents before indexing.
   - Verify document integrity and test using deliberately poisoned documents.
   - Mandard basis: **LLM-M-003**.

6. **Advisory (not catalogue-backed):** Use a documented go/no-go approval involving the service owner, security, privacy, and data owner. Require employee usage guidance identifying prohibited data and approved use cases.

### Implementation guidance — source: knowledge corpus

No knowledge document was found that is authoritatively mapped to **LLM-M-001** through **LLM-M-005**. Generic application, authentication, API, endpoint, and CI/CD documents returned by the governance search were set aside because their `mandard_refs` did not include these LLM Mandards.

## Evidence for audit

- **LLM-M-001:** Prompt-injection test report, fuzzing results, prompt-template configuration, and pipeline scan results.
- **LLM-M-005:** Data-classification record, DLP/redaction test results, encryption configuration, provider retention/training-use terms, and retention policy.
- **LLM-M-002:** Output schema definitions, sanitization configuration, XSS/content-injection tests, and sensitive-output canary results.
- **LLM-M-004:** Identity-provider and RBAC configuration, API-gateway policy, quota and token-limit settings, load-test results showing rejected excess requests, and monitoring records.
- **LLM-M-003:** RAG source inventory, vector-store IAM policy, ingestion validation results, integrity controls, and poisoned-document test evidence.
- **Advisory:** Recorded security/privacy approval and employee acceptable-use guidance.

## Assumptions and limits

The deployment architecture, data classes, provider terms, authentication configuration, RAG usage, and test results were not supplied and therefore were not verified. The knowledge corpus currently contains no documents mapped to the five LLM Mandards; implementation steps above are based on the Mandard catalogue, with additional non-catalogue guidance explicitly labelled.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**LLM-M-001**](https://verify.example-org.internal/?id=LLM-M-001) | Critical | LLM Security | AIUC1 (B005); CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-20, CWE-284, CWE-285); ENISA_SMLA (SMLA-04); EU_AI_ACT (Article 15, Article 9); HIPAA (164.312(a)(1)); +14 more |
| [**LLM-M-002**](https://verify.example-org.internal/?id=LLM-M-002) | High | LLM Security | AIUC1 (B009, C003, C006); CIS_CONTROLS (CIS 16); CWE (CWE-20, CWE-798); ENISA_SMLA (SMLA-34); EU_AI_ACT (Article 15, Article 9); ISO_27001 (A.5.17, A.8.24, A.8.26); +13 more |
| [**LLM-M-003**](https://verify.example-org.internal/?id=LLM-M-003) | High | LLM Security | CIS_CONTROLS (CIS 3, CIS 6); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-11, SMLA-32, SMLA-37); EU_AI_ACT (Article 10, Article 15, Article 9); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); +13 more |
| [**LLM-M-004**](https://verify.example-org.internal/?id=LLM-M-004) | High | LLM Security | AIUC1 (B004); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285); DORA (Art. 17-23, Art. 24-27, Art. 28-44); EU_AI_ACT (Article 15, Article 9); +16 more |
| [**LLM-M-005**](https://verify.example-org.internal/?id=LLM-M-005) | Critical | LLM Security | AIUC1 (A006); CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 3, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-327, CWE-798); DORA (Art. 17-23, Art. 24-27, Art. 28-44); +18 more |

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