# G67-AIDEV

## Question
What controls govern safe use of AI coding assistants in regulated development?

## Sage response

## Bottom line

AI coding assistants may be used in regulated development only through approved, inventoried services with controlled data flows, least-privileged access, human authorization for consequential actions, protected telemetry, and security testing. The principal exposure is leakage of source code, credentials or regulated data, together with unsafe code changes or autonomous actions entering production. Management should approve a controlled-use model and prohibit unsanctioned assistants; the SAGF catalogue does not currently contain a dedicated control explicitly requiring human review and licence/IP scanning of every AI-generated code contribution, so that requirement should be added or formally adopted through the secure-development standard.

## Risk and impact

| Risk | Exposure |
|---|---|
| **Critical** | Prompt injection hidden in repositories, issues, comments or documentation; credential disclosure; unauthorized tool execution; privileged or destructive changes; unsafe generated content; insufficient ability to disable compromised AI capabilities. |
| **High** | Shadow AI and unapproved data transfer; sensitive prompt and trace retention; supply-chain opacity; weak provenance; inadequate release testing; model or service changes invalidating prior assurance. |
| **Regulatory and business impact** | Disclosure of personal, cardholder, customer or proprietary data; intellectual-property loss; insecure production code; fraud or destructive changes; inability to demonstrate approval, accountability, testing and traceability to auditors. |

A particularly relevant requirement is: per **AI-M-002**, repository and external content—including issue bodies, pull-request comments, README files, error traces, dependency changelogs and fetched web pages—must be treated as an untrusted instruction source, and resulting agent actions must be reviewed.

## Governing mandards

### Primary controls for coding-assistant use

| Mandard | Title | Risk | Application |
|---|---|---:|---|
| **AI-M-002** | Prompt Injection Input Validation & Sanitization | Critical | Treat repository and external content as untrusted; sanitize rendered output and review resulting actions. |
| **AI-M-004** | Output Monitoring & Data Exfiltration Prevention | Critical | Detect credentials, internal configuration and other sensitive material in model output; log suspected exfiltration. |
| **AI-M-005** | LLM Agent Tool Call Validation & Least Privilege | Critical | Authorize every tool call, validate parameters, use explicit allowlists and retain tool-call audit records. |
| **AI-M-011** | AI Content Safety and Acceptable Use Guardrails | Critical | Establish risk-based acceptable-use controls and log guardrail decisions without unnecessary sensitive payloads. |
| **AI-M-013** | Human Approval for High-Impact Agent Actions | Critical | Require authenticated, action-specific approval immediately before privileged, destructive or externally consequential operations. |
| **AI-M-016** | Continuous AI Evaluation, Drift and Emergency Shutdown | Critical | Monitor AI behavior, alert on anomalies and provide a tested mechanism to disable the assistant or its tools. |
| **AI-M-022** | AI Agent and Non-Human Identity Governance | Critical | Give each agent an attributable identity and short-lived, scoped credentials held in a secret manager. |
| **AI-M-018** | AI Agent Adversarial Testing and Release Gates | High | Test prompt override, tool misuse, privilege escalation, exfiltration and approval bypass; block unsafe releases. |
| **AI-M-023** | Shadow AI Discovery and Governance | High | Inventory assistants, approve sensitive-data flows, and use CASB/DLP to block unsanctioned AI services. |
| **AI-M-025** | AI Telemetry and Trace Privacy | High | Minimize and redact prompts, completions and traces; encrypt, restrict and time-limit their retention. |
| **AI-M-007** | AI Model Bill of Materials (AI-SBOM) | High | Maintain model provenance and version information where the organization deploys or controls the model. |

### Complete AI domain control set

The AI domain contains the following 33 mandards. Applicability beyond the primary controls above depends on whether the assistant is SaaS-only, internally integrated, agentic, retrieval-enabled, multi-agent or internally hosted.

| ID | Title | Risk |
|---|---|---:|
| **AI-M-001** | AI/LLM Prompt Injection Scanning | Critical |
| **AI-M-002** | Prompt Injection Input Validation & Sanitization | Critical |
| **AI-M-003** | Structured Prompts with System/User Data Separation | Critical |
| **AI-M-004** | Output Monitoring & Data Exfiltration Prevention | Critical |
| **AI-M-005** | LLM Agent Tool Call Validation & Least Privilege | Critical |
| **AI-M-006** | RAG Source Attribution & Filtering | High |
| **AI-M-007** | AI Model Bill of Materials (AI-SBOM) | High |
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

The following are representative direct mappings returned by the SAGF catalogue; they are not inferred equivalences.

| Mandard | Returned framework mappings most relevant to regulated development |
|---|---|
| **AI-M-011** | NIST SP 800-53 `SA-11`, `SI-10`, `AU-2`, `AU-6`, `AU-12`, `SI-4`; PCI DSS `Req 6`, `Req 10`; ISO/IEC 27001:2022 `A.8.15`, `A.8.16`, `A.8.26`, `A.8.28`; ISO/IEC 42001 `A.2`, `A.6.2`, `A.8.3`. |
| **AI-M-013** | NIST SP 800-53 `AC-2`, `AC-3`, `AC-4`, `AC-6`, `IA-2`, `IA-4`, `IA-8`, `SA-11`; PCI DSS `Req 3`, `Req 7`; ISO/IEC 27001:2022 `A.5.15`, `A.5.18`, `A.8.2`, `A.8.3`, `A.8.5`; GDPR `Article 22`; OWASP LLM `LLM06`. |
| **AI-M-016** | NIST SP 800-53 `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SI-7`, `IR-4`, `IR-6`, `SA-11`; PCI DSS `Req 7`, `Req 10`; ISO/IEC 27001:2022 `A.8.15`, `A.8.16`, `A.5.24`, `A.5.26`. |
| **AI-M-018** | NIST SP 800-53 `CM-3`, `SA-11`, `SA-15`, `SI-4`, `AU-6`; ISO/IEC 27001:2022 `A.8.25`, `A.8.31`, `A.8.32`; OWASP SAMM security-testing mappings. |
| **AI-M-022** | NIST SP 800-53 `AC-2`, `AC-3`, `AC-4`, `AC-6`, `IA-2`, `IA-4`, `IA-5`, `AU-2`, `AU-6`, `AU-12`; PCI DSS `Req 7`, `Req 10`; ISO/IEC 27001:2022 `A.5.15`, `A.5.17`, `A.5.18`, `A.8.2`, `A.8.3`, `A.8.15`, `A.8.16`. |
| **AI-M-023** | NIST SP 800-53 `SI-4`, `AU-6`, `PL-2`, `PL-8`, `PM-9`, `SC-7`, `AC-4`, `SA-11`; PCI DSS `Req 1`; ISO/IEC 27001:2022 `A.8.16`, `A.8.20`, `A.8.22`; ISO/IEC 42001 `A.2`, `A.6.2`, `A.8.3`; SOC 2 `CC7.2`. |
| **AI-M-025** | NIST SP 800-53 `SC-12`, `SC-13`, `SC-28`, `SI-12`, `AU-2`, `AU-6`, `AU-12`, `PT-3`, `PT-5`; PCI DSS `Req 3`, `Req 4`, `Req 10`; ISO/IEC 27001:2022 `A.5.34`, `A.8.15`, `A.8.24`. |
| **AI-M-007** | NIST SP 800-53 `SR-3`, `SR-4`, `SA-12`, `SA-11`; ISO/IEC 27001:2022 `A.5.19`, `A.5.21`, `A.8.30`, `A.5.34`; GDPR `Articles 5, 17, 25`; OWASP LLM `LLM03`. |

## Required actions

1. **Approve and constrain assistant use — GRC, CISO and Enterprise Architecture.**  
   Per **AI-M-023**: maintain an inventory and allowlist of assistants, models, IDE extensions and embedded AI features; require approval before sensitive data is submitted; block unapproved destinations through CASB, proxy and DLP controls.

2. **Define prohibited inputs — Data Protection, Legal and Engineering.**  
   Per **AI-M-023** and **AI-M-022**: prohibit credentials, keys, production data and other unapproved sensitive content from prompts. Use managed enterprise accounts and ensure assistant or agent credentials are short-lived, scoped and stored outside prompts, code and logs.

3. **Treat repository content as hostile input — Engineering and AppSec.**  
   Per **AI-M-002**: scan and normalize issue text, pull-request comments, documentation, error traces and fetched content before an assistant or agent processes it. Sanitize rendered output to remove exfiltration links, bidirectional-override characters and zero-width characters, and review resulting actions.

4. **Restrict agent capabilities — Platform Engineering and IAM.**  
   Per **AI-M-005**: allowlist tools, repositories, paths and operations; enforce the authenticated developer’s permissions server-side; validate every tool parameter; and deny arbitrary shell,

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