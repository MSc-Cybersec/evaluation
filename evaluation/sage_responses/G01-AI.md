# G01-AI

## Question
What evidence do we need to approve a high-impact AI model release?

## Sage response
## Bottom line

Approve a high-impact AI model release only when the release record contains traceable evidence for model provenance, data governance, independent performance and fairness evaluation, security testing, human oversight, production monitoring, emergency shutdown, staged deployment, and accountable risk acceptance. Any failed CRITICAL control, unresolved material stakeholder concern, or untested rollback/shutdown capability should block production release. Conditional controls must be explicitly marked applicable or not applicable with documented justification.

## Risk and impact

The applicable SAGF AI Mandards range from CRITICAL to MEDIUM. The principal exposures are discriminatory or incorrect customer decisions, leakage of personal or confidential information, unauthorized agent actions, model or supply-chain compromise, regulatory non-compliance, and an inability to stop harmful production behavior.

For approval purposes:

•
Critical findings: release-blocking.
•
High findings: release-blocking unless formally remediated or accepted through the authorized deviation process.
•
Medium findings: require an owner and time-bound treatment plan; acceptance depends on risk appetite.
•
Controls concerning agents, LLMs, RAG, multimodal processing, or in-house training apply only where those capabilities exist, but applicability must be documented.
## Governing mandards

The complete AI domain contains the following Mandards:

Mandard	Title	Risk
AI-M-001	AI/LLM Prompt Injection Scanning	CRITICAL
AI-M-002	Prompt Injection Input Validation & Sanitization	CRITICAL
AI-M-003	Structured Prompts with System/User Data Separation	CRITICAL
AI-M-004	Output Monitoring & Data Exfiltration Prevention	CRITICAL
AI-M-005	LLM Agent Tool Call Validation & Least Privilege	CRITICAL
AI-M-006	RAG Source Attribution & Filtering	HIGH
AI-M-007	AI Model Bill of Materials AI-SBOM	HIGH
AI-M-008	LLM Prompt Injection Mitigation	CRITICAL
AI-M-009	Training Data Privacy & Sanitization	CRITICAL
AI-M-010	AI Model Fairness & Bias Testing	HIGH
AI-M-011	AI Content Safety and Acceptable Use Guardrails	CRITICAL
AI-M-012	Groundedness, Hallucination and Abstention	HIGH
AI-M-013	Human Approval for HIGH-Impact Agent Actions	CRITICAL
AI-M-014	AI Conversation Memory and Tenant Isolation	CRITICAL
AI-M-015	AI Model Integrity and Extraction Protection	HIGH
AI-M-016	Continuous AI Evaluation, Drift and Emergency Shutdown	CRITICAL
AI-M-017	Multi-Agent Trust Boundaries and Secure Agent Communication	HIGH
AI-M-018	AI Agent Adversarial Testing and Release Gates	HIGH
AI-M-019	Agent Resource, Loop and Cost Bounds	HIGH
AI-M-020	AI/ML Workload Runtime and Hardware Isolation	HIGH
AI-M-021	Model Registry Governance and Safe Deployment Lifecycle	HIGH
AI-M-022	AI Agent and Non-Human Identity Governance	CRITICAL
AI-M-023	Shadow AI Discovery and Governance	HIGH
AI-M-024	Natural-Language Data Gateway Safety	CRITICAL
AI-M-025	AI Telemetry and Trace Privacy	HIGH
AI-M-026	Multimodal Cross-Channel Data Protection	HIGH
AI-M-027	Adversarial Robustness Training and Evaluation	HIGH
AI-M-028	Model Explainability and Decision Traceability	HIGH
AI-M-029	Resilient Model Architecture Selection	HIGH
AI-M-030	Training Data Sufficiency, Representativeness and Augmentation	MEDIUM
AI-M-031	Privacy-Preserving Training for Sensitive Datasets	HIGH
AI-M-032	AI Interaction Disclosure and Content Labelling	HIGH
AI-M-033	AI Stakeholder Engagement and Accountability	HIGH

The central release-evidence requirements are:

•
Per AI-M-007: every production model must have a published Model Card or AI-SBOM covering provenance, training-data sources, architecture, and versioning.
•
Per AI-M-009: training and fine-tuning data must be sanitized for PII, secrets, and sensitive intellectual property, using reproducible and auditable pipelines.
•
Per AI-M-010: high-impact decision models must pass automated fairness and bias testing against protected groups before deployment.
•
Per AI-M-012: factual, regulated, or high-impact systems must measure groundedness, cite approved sources, and abstain or escalate below approved thresholds.
•
Per AI-M-016: production systems must have continuous evaluation, drift monitoring, recurring adversarial evaluation, and a tested emergency-disable mechanism.
•
Per AI-M-021: models must be promoted from an access-controlled registry using staged rollout and tested rollback.
•
Per AI-M-028: customer-impacting or security-relevant decisions require a proportionate explainability approach and reproducible per-decision explanations.
•
Per AI-M-033: affected stakeholders, material concerns, accountable owners, and dispositions must be recorded.
## Framework mapping

The following mappings were returned for the principal high-impact release controls:

Mandard	Returned framework mappings
AI-M-010	NIST AI RMF MAP-5, MEASURE-2; ISO/IEC 42001 A.5, A.6.2, A.8.3; EU AI Act Articles 9 and 15; GDPR Article 22
AI-M-013	NIST SP 800-53 AC-2, AC-3, AC-4, AC-6, IA-2, IA-4, IA-8, SI-4, SA-11; GDPR Article 22; OWASP LLM LLM06
AI-M-027	NIST AI RMF MEASURE-2, MANAGE-2; ISO/IEC 42001 A.6.2; ISO/IEC 27001 A.8.29; EU AI Act Article 15
AI-M-028	NIST AI RMF MAP-3, MEASURE-2; ISO/IEC 42001 A.9.2; EU AI Act Articles 13 and 14; GDPR Article 22
AI-M-030	NIST AI RMF MAP-2, MEASURE-2; ISO/IEC 42001 A.7.4, A.8.3; EU AI Act Article 10
AI-M-031	NIST AI RMF MEASURE-2, MANAGE-2; ISO/IEC 42001 A.8.3; EU AI Act Article 10; GDPR Articles 25, 32, and 44
AI-M-032	NIST AI RMF MAP-5; ISO/IEC 42001 A.9.2; EU AI Act Article 50
AI-M-033	NIST AI RMF GOVERN-5
## Required actions
1.
Establish the release decision record — Governance owner Record the use case, high-impact classification, intended users, affected populations, jurisdictions, decision authority, prohibited uses, and release scope. Complete an applicability assessment against all AI Mandards above. Per AI-M-033, assign owners and dispositions to all material stakeholder concerns. Do not approve while a CRITICAL control is failed or a material concern remains unowned.
2.
Lock model and data provenance — Model owner and data owner Per AI-M-007, publish the Model Card or AI-SBOM and bind it to the exact model digest and release version. Per AI-M-009, provide dataset versions, provenance, permitted-use basis, PII/secret scan results, sanitization results, parameters, code version, and reproducible training records. Per AI-M-030, where the model is trained in-house, demonstrate dataset coverage, representativeness, augmentation provenance, and absence of train/test leakage. Per AI-M-031, where sensitive or cross-jurisdictional data is involved, document the privacy-preserving training decision and residual privacy risk.
3.
Demonstrate independent model validation — Model risk or validation function Approve documented thresholds before reviewing results. Per AI-M-010, test fairness across applicable protected groups and block promotion below the approved threshold. Per AI-M-012, test accuracy, groundedness, citations, abstention, and escalation against an approved evaluation set. Per AI-M-027, for applicable in-house models, record attack types, perturbation budgets, robust accuracy, and the promotion result. Per AI-M-028, validate the explainability method and demonstrate a reproducible explanation for representative individual decisions.
4.
Complete security and abuse testing — Security assurance For LLM deployments, provide prompt-injection, jailbreak, output leakage, credential exposure, content-safety, and abuse-case results under AI-M-001, AI-M-004, and AI-M-011. Per AI-M-015, verify the model’s signature or digest and test controls against unauthorized replacement, extraction, inversion, and high-volume probing. For agents, per AI-M-005, AI-M-013, and AI-M-018, test tool authorization, parameter validation, least privilege, approval bypass, replay, expiry, privilege escalation, exfiltration, and recursive tool abuse. Ensure the CI/CD gate identifies the exact model, prompts, tools, policies, retrieval configuration, and test suite used.
5.
Prove human oversight — Business control owner Per AI-M-013, demonstrate authenticated, single-use approval immediately before any irreversible, financial, privileged, destructive, or externally consequential agent action. Per AI-M-012, demonstrate deterministic abstention or escalation where evidence or confidence is insufficient. Per AI-M-028, document how operators can understand, contest, override, or review customer-impacting decisions.
6.
Approve production controls — Platform and operations owners Per AI-M-016, configure monitoring thresholds for quality, safety, security, cost, and distribution drift; assign alert and incident owners. Per AI-M-025, demonstrate prompt and trace minimization, redaction, encryption, access control, retention, deletion, and access logging. Per AI-M-021, deploy through a controlled model registry using shadow or canary rollout and prove rapid rollback. Execute and record an emergency-disable exercise covering the model and, where applicable, agent tools and affected capabilities.
7.
Issue the final approval — Accountable risk executive Sign the release decision against the immutable evidence package. Record residual risks, deviations, expiry dates, compensating controls, conditions of use, monitoring obligations, and reapproval triggers. Require reapproval after material changes to the model, training data, prompts, retrieval sources, tools, memory, policies, provider, or operating context.
## Evidence for audit

The minimum approval pack should contain:

Evidence artefact	Minimum content	Mandard basis
Release decision and applicability matrix	Applicable/not-applicable determination, justification, owners, unresolved issues, approval signatures	AI-M-033 and applicable AI Mandards
Model Card or AI-SBOM	Model and base-model versions, digest, architecture, provenance, training-data sources, license, dependencies, limitations	AI-M-007
Reproducibility record	Dataset, code, parameters, environment, pipeline run, model digest, immutable registry reference	AI-M-009
Privacy and data assessment	Data classification, lawful/approved use, PII and secret scans, sanitization, retention, residency, residual risk	AI-M-009, AI-M-025, conditionally AI-M-031
Dataset-quality report	Coverage, representativeness, class balance, augmentation provenance, duplication and leakage tests	AI-M-030
Model validation report	Approved thresholds, baseline comparison, performance by relevant cohort, edge cases, limitations, independent sign-off	AI-M-010, AI-M-012
Fairness report	Protected groups assessed, metrics, thresholds, confidence information, exceptions, reviewer decision	AI-M-010
Explainability evidence	Method, risk-tier justification, representative and per-decision explanations, review/dispute process	AI-M-028
Security test report	Prompt injection, jailbreak, leakage, unsafe output, adversarial robustness, extraction and inversion tests as applicable	AI-M-001, AI-M-004, AI-M-015, AI-M-027
Agent assurance report	Tool inventory, permissions, abuse-case matrix, approval-control tests, tool-call audit trail	AI-M-005, AI-M-013, AI-M-018
Content-safety evaluation	Prohibited categories, thresholds, representative tests, false-positive/negative review, safe-refusal behavior	AI-M-011
Pipeline gate record	Immutable pass/fail output linked to model, data, prompt, policy, tool and test-suite versions	AI-M-007, AI-M-010, AI-M-018
Deployment and rollback evidence	Registry access controls, signed artifact verification, canary/shadow record, rollback test, retired endpoints	AI-M-015, AI-M-021
Monitoring and shutdown evidence	Dashboards, alert thresholds, drift tests, incident routing, kill-switch test, fallback behavior	AI-M-016
Telemetry privacy configuration	Redaction tests, encryption, RBAC, retention/deletion settings, processor assessment, access logs	AI-M-025
Stakeholder and risk record	Actor register, concerns, challenge outcomes, accountable dispositions, residual-risk acceptance	AI-M-033
Final approval record	Named accountable approver, decision date, scope, conditions, deviations, expiry and reapproval triggers	AI-M-033
## Assumptions and limits
csharp
“High-impact” was treated as a customer-impacting, security-relevant, regulated, financial, privileged, or otherwise consequential use case; the project’s formal classification was not provided.
Applicability of LLM, RAG, agent, multimodal, and in-house-training controls was not verified.
No AI-specific knowledge document was found for this point. The retrieved knowledge material concerned general application and endpoint governance, including SAF approval, onboarding records, security assessment results, deviations, and release-pipeline evidence: **VeriFy-CE-001**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082), and **VeriFy-APP-002**, [source](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782). These documents are not mapped to the AI Mandards and were therefore not used as the authority for the AI release criteria.
Detailed framework mappings were reported only where returned by the Mandard tool; no broader equivalence or coverage claim is made.
Evidence and framework mapping
Catalogue-verified
15 of 33 cited
Exec
Engineer
Auditor
Critical
High
Frameworks
Sort
Risk
Mandard
Coverage
Mandard	Risk	Domain	Frameworks cited	Actions

AI-M-001
AI/LLM Prompt Injection Scanning
	CRITICAL	AI/ML Security	
AIUC1
1
CWE
2
ENISA SMLA
1
+13 more
	
Open
Copy
Link


AI-M-002
Prompt Injection Input Validation & Sanitization
	CRITICAL	AI/ML Security	
AIUC1
2
CIS CONTROLS
6
COBIT 2019
4
+23 more
	
Open
Copy
Link


AI-M-003
Structured Prompts with System/User Data Separation
	CRITICAL	AI/ML Security	
CIS CONTROLS
2
COBIT 2019
2
EU AI ACT
2
+14 more
	
Open
Copy
Link


AI-M-004
Output Monitoring & Data Exfiltration Prevention
	CRITICAL	AI/ML Security	
AIUC1
3
CIS CONTROLS
1
COBIT 2019
2
+20 more
	
Open
Copy
Link


AI-M-005
LLM Agent Tool Call Validation & Least Privilege
	CRITICAL	AI/ML Security	
AIUC1
5
CIS CONTROLS
3
COBIT 2019
2
+20 more
	
Open
Copy
Link


AI-M-008
LLM Prompt Injection Mitigation
	CRITICAL	AI/ML Security	
CIS CONTROLS
2
CWE
3
EU AI ACT
2
+15 more
	
Open
Copy
Link


AI-M-009
Training Data Privacy & Sanitization
	CRITICAL	AI/ML Security	
AIUC1
1
CCPA CPRA
3
CIS CONTROLS
3
+21 more
	
Open
Copy
Link


AI-M-011
AI Content Safety and Acceptable Use Guardrails
	CRITICAL	AI/ML Security	
AIUC1
7
CIS CONTROLS
2
COBIT 2019
2
+19 more
	
Open
Copy
Link


AI-M-013
Human Approval for High-Impact Agent Actions
	CRITICAL	AI/ML Security	
AIUC1
4
CIS CONTROLS
2
COBIT 2019
1
+21 more
	
Open
Copy
Link


AI-M-014
AI Conversation Memory and Tenant Isolation
	CRITICAL	AI/ML Security	
AIUC1
1
CIS CONTROLS
1
ENISA FAICP
1
+9 more
	
Open
Copy
Link


AI-M-006
RAG Source Attribution & Filtering
	HIGH	AI/ML Security	
AIUC1
1
CIS CONTROLS
5
COBIT 2019
4
+20 more
	
Open
Copy
Link


AI-M-007
AI Model Bill of Materials (AI-SBOM)
	HIGH	AI/ML Security	
AIUC1
2
CCPA CPRA
3
CIS CONTROLS
3
+20 more
	
Open
Copy
Link


AI-M-010
AI Model Fairness & Bias Testing
	HIGH	AI/ML Security	
COBIT 2019
2
ENISA SMLA
1
EU AI ACT
2
+12 more
	
Open
Copy
Link


AI-M-012
Groundedness, Hallucination and Abstention
	HIGH	AI/ML Security	
AIUC1
4
CIS CONTROLS
3
COBIT 2019
3
+18 more
	
Open
Copy
Link


AI-M-015
AI Model Integrity and Extraction Protection
	HIGH	AI/ML Security	
AIUC1
1
CIS CONTROLS
6
COBIT 2019
7
+22 more
	
Open
Copy
Link
Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
Filter Explorer
CSV
JSON

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