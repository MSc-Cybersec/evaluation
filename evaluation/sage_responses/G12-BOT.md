# G12-BOT

## Question
What policy controls should govern autonomous security bots in production?

## Sage response

## Bottom line

Autonomous security bots should not receive blanket production authority. Production use should be approved only where every action is policy-validated, identities and credentials are tightly scoped, consequential actions require authenticated human approval, and monitoring can independently halt the bot. Without these controls, a compromised or malfunctioning bot can escalate privilege, delete or alter assets, expose sensitive data, disrupt services, and generate unbounded cost.

## Risk and impact

The governing catalogue rates authorization, human approval, identity governance, and emergency shutdown as **Critical**. Adversarial testing, execution limits, trust boundaries, telemetry privacy, and decision traceability are **High**.

Primary exposure includes:

- Unauthorized privileged changes or destructive remediation.
- Credential theft and lateral movement through over-privileged bot identities.
- Prompt injection or manipulated observations causing malicious tool calls.
- Untraceable actions that cannot be reconstructed, challenged, or attributed.
- Cascading failures, repeated actions, resource exhaustion, and denial-of-wallet.
- Sensitive data leakage through prompts, tool output, logs, and observability platforms.

## Governing mandards

### Core production controls

| Mandard | Title | Risk | Policy requirement |
|---|---|---:|---|
| **AI-M-005** | LLM Agent Tool Call Validation & Least Privilege | Critical | Per **AI-M-005**: validate each tool call against the authenticated principal’s permissions; use explicit allowlists, fixed tool schemas, parameter validation, least privilege, and complete tool-call audit records. |
| **AI-M-013** | Human Approval for High-Impact Agent Actions | Critical | Per **AI-M-013**: require authenticated human approval immediately before irreversible, destructive, financial, privileged, or externally consequential actions. Approval must bind the user, action, resolved parameters, and expiry. |
| **AI-M-016** | Continuous AI Evaluation, Drift and Emergency Shutdown | Critical | Per **AI-M-016**: continuously monitor production behavior and maintain tested, independently authorized controls to disable the agent, model, tool access, or affected capability. |
| **AI-M-022** | AI Agent and Non-Human Identity Governance | Critical | Per **AI-M-022**: assign each bot a distinct identity and use short-lived, environment-specific, tool-specific credentials held in a secret manager, with inventory, rotation, de-provisioning, and anomaly monitoring. |
| **AI-M-017** | Multi-Agent Trust Boundaries and Secure Agent Communication | High | Per **AI-M-017**: authenticate and integrity-protect inter-agent messages, prevent replay, authorize recipients and message types, sanitize untrusted output, and use circuit breakers. |
| **AI-M-018** | AI Agent Adversarial Testing and Release Gates | High | Per **AI-M-018**: run a repeatable abuse-case suite before release and after material changes; CI/CD must block regressions and retain test evidence. |
| **AI-M-019** | Agent Resource, Loop and Cost Bounds | High | Per **AI-M-019**: enforce fail-closed limits on steps, recursion, retries, execution time, tokens, and cost; halt safely when a limit is exceeded. |
| **AI-M-025** | AI Telemetry and Trace Privacy | High | Per **AI-M-025**: minimize or redact sensitive trace content before capture and apply encryption, least-privilege access, retention, deletion, and access logging. |
| **AI-M-028** | Model Explainability and Decision Traceability | High | Per **AI-M-028**: security-relevant or customer-impacting decisions require a proportionate explainability approach and a per-decision explanation available for review. |

### Complete AI-domain catalogue returned for applicability assessment

The following complete AI-domain set was returned. Controls beyond the core set above should be made applicable based on whether the bot uses an LLM, retrieval, memory, multiple agents, natural-language data access, training data, or customer-impacting decisions.

| ID | Title | Risk |
|---|---|---:|
| **AI-M-001** | AI/LLM Prompt Injection Scanning | Critical |
| **AI-M-002** | Prompt Injection Input Validation & Sanitization | Critical |
| **AI-M-003** | Structured Prompts with System/User Data Separation | Critical |
| **AI-M-004** | Output Monitoring & Data Exfiltration Prevention | Critical |
| **AI-M-005** | LLM Agent Tool Call Validation & Least Privilege | Critical |
| **AI-M-006** | RAG Source Attribution & Filtering | High |
| **AI-M-007** | AI Model Bill of Materials AI-SBOM | High |
| **AI-M-008** | LLM Prompt Injection Mitigation | Critical |
| **AI-M-009** | Training Data Privacy & Sanitization | Critical |
| **AI-M-010** | AI Model Fairness & Bias Testing | High |
| **AI-M-011** | AI Content Safety and Acceptable Use Guardrails | Critical |
| **AI-M-012** | Groundedness, Hallucination and Abstention | High |
| **AI-M-013** | Human Approval for High-Impact Agent Actions | Critical |
| **AI-M-014** | AI Conversation Memory and Tenant Isolation | Critical |
| **AI-M-015** | AI Model Integrity and Extraction Protection | High |
| **AI-M-016** | Continuous AI Evaluation, Drift and Emergency Shutdown | Critical |
| **AI-M-017** | Multi-Agent Trust Boundaries and Secure Agent Communication | High |
| **AI-M-018** | AI Agent Adversarial Testing and Release Gates | High |
| **AI-M-019** | Agent Resource, Loop and Cost Bounds | High |
| **AI-M-020** | AI/ML Workload Runtime and Hardware Isolation | High |
| **AI-M-021** | Model Registry Governance and Safe Deployment Lifecycle | High |
| **AI-M-022** | AI Agent and Non-Human Identity Governance | Critical |
| **AI-M-023** | Shadow AI Discovery and Governance | High |
| **AI-M-024** | Natural-Language Data Gateway Safety | Critical |
| **AI-M-025** | AI Telemetry and Trace Privacy | High |
| **AI-M-026** | Multimodal Cross-Channel Data Protection | High |
| **AI-M-027** | Adversarial Robustness Training and Evaluation | High |
| **AI-M-028** | Model Explainability and Decision Traceability | High |
| **AI-M-029** | Resilient Model Architecture Selection | High |
| **AI-M-030** | Training Data Sufficiency, Representativeness and Augmentation | Medium |
| **AI-M-031** | Privacy-Preserving Training for Sensitive Datasets | High |
| **AI-M-032** | AI Interaction Disclosure and Content Labelling | High |
| **AI-M-033** | AI Stakeholder Engagement and Accountability | High |

## Framework mapping

The table lists only mappings returned for the core mandards. It is a concise selection rather than an assertion of complete cross-framework coverage.

| Mandard | Returned framework mappings |
|---|---|
| **AI-M-013** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, IA-2, IA-4, IA-8, SI-4, SA-11; PCI DSS v4.0: Req 3, Req 7; ISO/IEC 27001:2022: A.5.15, A.5.16, A.5.18, A.8.2, A.8.3, A.8.5; GDPR Article 22; OWASP LLM06; ISO/IEC 42001: A.6.2, A.8.3, A.9.2. |
| **AI-M-016** | NIST SP 800-53 Rev.5: AU-2, AU-6, AU-12, SI-4, SI-7, IR-4, IR-6, SA-11; PCI DSS v4.0: Req 7, Req 10; ISO/IEC 27001:2022: A.8.15, A.8.16, A.5.24, A.5.26. |
| **AI-M-017** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, IA-2, IA-4, IA-8, SI-4, SI-10, SA-11; PCI DSS v4.0: Req 6, Req 7; ISO/IEC 27001:2022: A.5.15, A.5.16, A.5.18, A.8.2, A.8.3, A.8.5, A.8.26, A.8.28. |
| **AI-M-018** | NIST SP 800-53 Rev.5: CM-3, SA-11, SA-15, SI-4, AU-6, SC-7, AC-4; ISO/IEC 27001:2022: A.8.16, A.8.25, A.8.31, A.8.32; PCI DSS v4.0: Req 1. |
| **AI-M-019** | NIST SP 800-53 Rev.5: SI-4, AU-6, SI-7, AC-12, SA-11; ISO/IEC 27001:2022: A.8.16; OWASP LLM10; SOC 2: CC7.2. |
| **AI-M-022** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, AU-2, AU-6, AU-12, IA-2, IA-4, IA-5, IA-8, SI-4, SC-12, SA-11; PCI DSS v4.0: Req 7, Req 10; ISO/IEC 27001:2022: A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.15, A.8.16, A.8.24. |
| **AI-M-025** | NIST SP 800-53 Rev.5: AU-2, AU-6, AU-12, SC-12, SC-13, SC-28, SI-4, SI-7, SI-12, PT-3, PT-5; PCI DSS v4.0: Req 3, Req 4, Req 10; ISO/IEC 27001:2022: A.5.34, A.8.15, A.8.24. |
| **AI-M-028** | GDPR Article 22; ISO/IEC 42001: A.9.2; NIST AI RMF 1.0: MAP-3, MEASURE-2; EU AI Act: Articles 13 and 14; ENISA SMLA: SMLA-07. |

## Required actions

1. **Security architecture and IAM:** Per **AI-M-005** and **AI-M-022**, place all execution behind a server-side policy-enforcement gateway. Give each bot a distinct workload identity and allow only approved tools, targets, paths, operations, and environments. The model must never directly hold unrestricted production credentials.

2. **Business and control owners:** Per **AI-M-013**, classify actions before deployment:
   - **Autonomous:** reversible, bounded, low-impact actions.
   - **Approval required:** privileged, destructive, irreversible, financial, externally consequential, or customer-impacting actions.
   - **Prohibited:** actions outside the approved purpose, environment, or data boundary.

   Approval must occur after final parameters are resolved and use a short-lived, single-use authorization bound to those exact

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AI-M-001**](https://verify.example-org.internal/?id=AI-M-001) | Critical | AI/ML Security | AIUC1 (B002); CWE (CWE-77, CWE-89); ENISA_SMLA (SMLA-26); EU_AI_ACT (Article 15, Article 9); ISO_42001 (A.6.2, A.8.3); MAESTRO (L1, L6); +10 more |
| [**AI-M-002**](https://verify.example-org.internal/?id=AI-M-002) | Critical | AI/ML Security | AIUC1 (B002, B005); CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CWE (CWE-20, CWE-284, CWE-285); ENISA_FAICP (FAICP-2); ENISA_SMLA (SMLA-04, SMLA-26); +20 more |
| [**AI-M-003**](https://verify.example-org.internal/?id=AI-M-003) | Critical | AI/ML Security | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04); EU_AI_ACT (Article 15, Article 9); ISO_27001 (A.5.19, A.5.21, A.8.30); ISO_42001 (A.6.2, A.8.3); MAESTRO (L1, L6); +11 more |
| [**AI-M-004**](https://verify.example-org.internal/?id=AI-M-004) | Critical | AI/ML Security | AIUC1 (A004, B009, C006); CIS_CONTROLS (CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-798); ENISA_SMLA (SMLA-34); EU_AI_ACT (Article 14, Article 15, Article 9); +17 more |
| [**AI-M-005**](https://verify.example-org.internal/?id=AI-M-005) | Critical | AI/ML Security | AIUC1 (A003, B006, D003); CIS_CONTROLS (CIS 16, CIS 6, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); CWE (CWE-20, CWE-284, CWE-285); ENISA_SMLA (SMLA-02); EU_AI_ACT (Article 14, Article 15, Article 9); +17 more |
| [**AI-M-006**](https://verify.example-org.internal/?id=AI-M-006) | High | AI/ML Security | AIUC1 (D001); CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CWE (CWE-798); EU_AI_ACT (Article 10, Article 15, Article 9); HIPAA (164.312(b)); +17 more |
| [**AI-M-007**](https://verify.example-org.internal/?id=AI-M-007) | High | AI/ML Security | AIUC1 (E006, E017); CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04); ENISA_SMLA (SMLA-03, SMLA-08, SMLA-22); EU_AI_ACT (Article 11, Article 15, Article 53); +17 more |
| [**AI-M-008**](https://verify.example-org.internal/?id=AI-M-008) | Critical | AI/ML Security | CIS_CONTROLS (CIS 16, CIS 6); CWE (CWE-20, CWE-284, CWE-285); EU_AI_ACT (Article 15, Article 9); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.18, A.8.2); ISO_42001 (A.6.2, A.8.3); +12 more |
| [**AI-M-009**](https://verify.example-org.internal/?id=AI-M-009) | Critical | AI/ML Security | AIUC1 (A001); CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 16, CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-20, CWE-798); +18 more |
| [**AI-M-010**](https://verify.example-org.internal/?id=AI-M-010) | High | AI/ML Security | COBIT_2019 (APO12.01, EDM03.01); ENISA_SMLA (SMLA-23); EU_AI_ACT (Article 15, Article 9); GDPR (Article 22); ISO_42001 (A.5, A.6.2, A.8.3); MAESTRO (L1, L6); +9 more |
| [**AI-M-011**](https://verify.example-org.internal/?id=AI-M-011) | Critical | AI/ML Security | AIUC1 (A007, C003, C004); CIS_CONTROLS (CIS 16, CIS 8); COBIT_2019 (DSS05.07, MEA03.01); ENISA_FAICP (FAICP-3); ENISA_SMLA (SMLA-06, SMLA-30); EU_AI_ACT (Article 15, Article 9); +16 more |
| [**AI-M-012**](https://verify.example-org.internal/?id=AI-M-012) | High | AI/ML Security | AIUC1 (C004, D001, D002); CIS_CONTROLS (CIS 16, CIS 17, CIS 8); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); EU_AI_ACT (Article 13, Article 15, Article 9); GDPR (Article 22); ISO_27001 (A.5.24, A.5.26, A.8.16); +15 more |
| [**AI-M-013**](https://verify.example-org.internal/?id=AI-M-013) | Critical | AI/ML Security | AIUC1 (B006, C005, C007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285); DORA (Art. 17-23, Art. 24-27, Art. 28-44); ENISA_FAICP (FAICP-3); +18 more |
| [**AI-M-014**](https://verify.example-org.internal/?id=AI-M-014) | Critical | AI/ML Security | AIUC1 (A005); CIS_CONTROLS (CIS 3); ENISA_FAICP (FAICP-1); EU_AI_ACT (Article 15, Article 9); ISO_42001 (A.6.2, A.8.3); MAESTRO (L1, L6); +6 more |
| [**AI-M-015**](https://verify.example-org.internal/?id=AI-M-015) | High | AI/ML Security | AIUC1 (B003); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CWE (CWE-284, CWE-285); ENISA_FAICP (FAICP-2); ENISA_SMLA (SMLA-05, SMLA-33, SMLA-34); +19 more |

Showing 15 of 33 cited mandards.

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
- assumptions_limits: fail (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass