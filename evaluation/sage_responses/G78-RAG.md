# G78-RAG

## Question
What governance controls are required for grounded retrieval in production?

## Sage response

## Bottom line

Production grounded-retrieval systems must satisfy all five LLM security Mandards, with immediate priority on prompt-injection prevention and sensitive-data handling. The production release should be blocked unless content ingestion, retrieval, model access, and output handling are controlled and independently evidenced; otherwise the system is exposed to data leakage, poisoned knowledge, unauthorized use, and unsafe downstream actions.

The catalogue does not contain a separate Mandard requiring citation accuracy, retrieval-quality thresholds, or factual-grounding metrics. Those measures are recommended below as **Advisory (not catalogue-backed)**.

## Risk and impact

| Priority | Exposure | Business impact |
|---|---|---|
| Critical | Direct or indirect prompt injection through user input or retrieved documents | System-instruction override, unauthorized actions, confidential-data disclosure, or system compromise |
| Critical | Sensitive information entering model context or provider logs | Privacy breach, regulatory non-compliance, credential exposure, and third-party data leakage |
| High | Poisoned or unauthorized content entering the retrieval index | Manipulated answers, persistent indirect prompt injection, and loss of knowledge-base integrity |
| High | Unvalidated model output reaching users or downstream systems | Data exfiltration, XSS or content injection, and unsafe automated actions |
| High | Unauthenticated or unrestricted model access | Denial of service, excessive cost, repeated extraction attempts, and unauthorized use |

## Governing mandards

The complete LLM Mandard set applicable to this domain is:

| Mandard | Title | Risk | Production requirement |
|---|---|---:|---|
| **LLM-M-001** | LLM Prompt Injection Prevention | Critical | Per **LLM-M-001**: validate and sanitize all user input, external content, and encoded data processed by the LLM; maintain clear separation between instructions and untrusted data. |
| **LLM-M-005** | Sensitive Data Handling in LLM Contexts | Critical | Per **LLM-M-005**: classify sensitive data before model processing, encrypt it in transit, control provider retention and training use, and apply compliant retention periods. |
| **LLM-M-002** | LLM Output Validation & Sanitization | High | Per **LLM-M-002**: treat model output as untrusted and validate, sanitize, encode, redact, or block it before display or downstream use. |
| **LLM-M-003** | RAG System Poisoning Prevention | High | Per **LLM-M-003**: apply access control and validation to knowledge bases, vector stores, and external content sources; validate documents before indexing and protect document integrity. |
| **LLM-M-004** | LLM Model Access & Rate Limiting | High | Per **LLM-M-004**: require authentication, authorization, rate limits, usage quotas, token limits, and usage monitoring for model services. |

## Framework mapping

The following are catalogue-returned mappings relevant to grounded retrieval:

| Mandard | Framework controls |
|---|---|
| **LLM-M-001** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, SI-10, SA-11, SI-4; PCI DSS v4.0: Requirements 6 and 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3, A.8.26, A.8.28; OWASP ASVS 5.0: V1, V8, V13 |
| **LLM-M-002** | NIST SP 800-53 Rev. 5: SI-10, SA-11, SI-4; ISO/IEC 27001:2022: A.8.26, A.8.28; OWASP ASVS 5.0: V1, V13; OWASP LLM: LLM05 Improper Output Handling; ISO/IEC 42001: A.6.2, A.8.3 |
| **LLM-M-003** | NIST SP 800-53 Rev. 5: AC-2, AC-3, AC-4, AC-6, MP-4, SC-28, SI-12, SI-4, SA-11; PCI DSS v4.0: Requirement 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3; OWASP LLM: LLM04 Data and Model Poisoning |
| **LLM-M-004** | NIST SP 800-53 Rev. 5: IA-2, IA-4, IA-5, IA-8, AC-2, AC-3, AC-4, AC-6, AC-7, SC-8, SI-4, SI-7, SA-11; PCI DSS v4.0: Requirements 3, 7, and 8; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.3, A.8.5 |
| **LLM-M-005** | NIST SP 800-53 Rev. 5: SC-12, SC-13, SC-28, SI-12, MP-4, AU-2, AU-6, AU-12, SI-4, IA-5, PT-3, PT-5, SA-11; PCI DSS v4.0: Requirements 3, 4, and 10; ISO/IEC 27001:2022: A.5.17, A.5.34, A.8.11, A.8.15, A.8.16, A.8.24; HIPAA: 164.312(a)(2)(iv) |

## Required actions

1. **Protect every route into the model context — Application Security and AI Engineering**
   - Per **LLM-M-001**, validate direct prompts, retrieved passages, metadata, encoded content, and external tool responses.
   - Use structured prompt templates and explicit boundaries between system instructions, user input, and retrieved content.
   - Filter indirect prompt-injection payloads before retrieved content reaches the model.
   - Run dynamic prompt-injection testing before release.

2. **Control sensitive data before retrieval or generation — Data Owner and Privacy/Security**
   - Per **LLM-M-005**, classify documents and query data before processing.
   - Detect and redact prohibited PII, PHI, financial information, credentials, and secrets.
   - Encrypt model-bound traffic and document approved provider retention and model-training settings.
   - Apply retention and deletion requirements to prompts, retrieved passages, responses, traces, caches, and vector-store records.

3. **Secure ingestion and index integrity — Knowledge Owner and Platform Engineering**
   - Per **LLM-M-003**, permit ingestion only from approved sources and validate documents before indexing.
   - Separate the ingestion role from the query role; grant write permissions only to controlled ingestion services and read-only permissions to runtime retrieval services.
   - Sanitize documents and retrieval results for control characters, hidden instructions, and prompt-injection payloads.
   - Protect document integrity using signing or HMAC and require approval before suspicious content is indexed.
   - Test with deliberately poisoned documents to confirm detection and blocking.

4. **Enforce authorization at retrieval time — Platform Engineering**
   - Per **LLM-M-003**, enforce access controls over knowledge bases and vector stores.
   - Ensure retrieval applies the requesting user’s authorization context rather than relying solely on index-level separation.
   - Prevent cross-tenant or cross-classification retrieval through role, tenant, and document metadata filters.

5. **Validate all outputs — Application Engineering**
   - Per **LLM-M-002**, validate response structure against an expected schema.
   - Redact sensitive-data patterns and block system-prompt, credential, or confidential-data leakage.
   - Apply context-appropriate encoding before rendering model output.
   - Do not pass free-form output to tools, databases, browsers, or workflow engines without strict validation and authorization.

6. **Protect production capacity and access — API and Platform Owners**
   - Per **LLM-M-004**, authenticate and authorize users before retrieval or inference.
   - Apply per-user, per-IP, and per-credential rate limits and quotas.
   - Set input, retrieval-context, and generation-token limits.
   - Monitor violations and verify that excessive traffic is rejected.

7. **Advisory (not catalogue-backed): establish a groundedness release gate**
   - Require each material answer to retain source identifiers and document versions.
   - Measure retrieval relevance, citation support, unsupported-claim rate, access-control leakage, and abstention behavior against an approved evaluation set.
   - Make the application abstain or escalate when evidence is absent, conflicting, stale, or below an approved confidence threshold.
   - Re-run evaluation when the embedding model, reranker, prompt, index, source corpus, or generation model changes.

## Evidence for audit

| Mandard | Minimum evidence |
|---|---|
| **LLM-M-001** | Input-validation configuration; prompt-template review; direct and indirect injection test results; pipeline scan results; blocked-payload logs |
| **LLM-M-005** | Data-classification record; data-flow assessment; DLP/redaction test results; TLS configuration; provider retention and training-use approval; retention schedule |
| **LLM-M-003** | Approved-source inventory; ingestion validation configuration; document approval records; vector-store IAM policies; integrity-check records; poisoned-document test results |
| **LLM-M-002** | Output schemas; sanitizer and encoding configuration; sensitive-output canary tests; XSS/content-injection test results; downstream action allowlists |
| **LLM-M-004** | API gateway authentication policy; RBAC configuration; rate-limit and quota settings; token-limit configuration; load-test results showing enforced rejection; monitoring alerts |
| Advisory grounding gate | Versioned evaluation dataset, acceptance thresholds, evaluation report, citation-to-source trace, change-triggered regression record, and accountable-owner approval |

## Assumptions and limits

No system architecture, provider configuration, data classification, retrieval authorization model, or production test evidence was supplied, so compliance has not been verified. No knowledge document is currently mapped to **LLM-M-001** through **LLM-M-005**; therefore, the implementation points above come from the Mandard catalogue itself, while the groundedness evaluation gate is explicitly advisory.

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