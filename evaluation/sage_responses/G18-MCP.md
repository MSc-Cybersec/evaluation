# G18-MCP

## Question
What governance controls apply to MCP tools that can change system state?

## Sage response

## Bottom line

All four MCP mandards apply to tools capable of changing system state. Such tools must not be enabled unless their definitions are approved and integrity-pinned, requests are authenticated and authorized in the requesting user’s context, messages are protected against tampering and replay, and the MCP server is isolated and supply-chain verified. The current MCP catalogue does not explicitly mandate human approval for every state-changing invocation; that additional control should be adopted for destructive or high-impact actions and considered for a new Mandard.

## Risk and impact

| Mandard | Risk | Exposure for state-changing tools |
|---|---:|---|
| **MCP-M-001** | Critical | A poisoned or silently modified tool definition could cause unauthorized changes, execute substituted parameters, or redirect actions to unintended systems. |
| **MCP-M-002** | Critical | Weak authentication or authorization could let an MCP server act with broader privileges than the requester, resulting in confused-deputy abuse and unauthorized changes. |
| **MCP-M-003** | High | A captured or modified request could be replayed to duplicate transactions, deployments, deletions, or configuration changes. |
| **MCP-M-004** | High | An over-privileged or compromised MCP server could modify files, access credentials, move across trust boundaries, or introduce malicious packages and tools. |

For state-changing operations, the principal business impacts are unauthorized transactions, destructive configuration changes, service disruption, fraud, data loss, and loss of accountability for who initiated an action.

## Governing mandards

- **MCP-M-001 — MCP Tool Definition Integrity and Poisoning Prevention — Critical.**  
  Per **MCP-M-001**: inspect and approve the complete tool schema, cryptographically pin it at discovery, and verify it again before every execution. Parameters must use strict JSON Schema, including `additionalProperties: false`, and tools must be checked for poisoned descriptions and cross-server shadowing.

- **MCP-M-002 — MCP Server Authentication, Authorization and Transport Hardening — Critical.**  
  Per **MCP-M-002**: remote endpoints must use OAuth 2.0 with PKCE, bind sessions to the authenticated user, verify token or session ownership on every request, use TLS with server identity verification, validate the host, and enforce per-session or per-tenant limits and timeouts.

- **MCP-M-003 — MCP Message Integrity and Replay Protection — High.**  
  Per **MCP-M-003**: each JSON-RPC message must be signed over its complete serialized payload with an identity-bound asymmetric key and include a unique nonce and timestamp. Duplicate, expired, unsigned, or invalidly signed requests must fail closed.

- **MCP-M-004 — MCP Server Isolation, Supply Chain and Consent — High.**  
  Per **MCP-M-004**: local servers must run in a least-privilege sandbox; each server must be treated as an independent untrusted domain; packages and publishers must be verified; and installation or connection requires explicit user consent showing the command and publisher. Consent must be renewed when tool definitions change and cannot be initiated by untrusted web content.

## Framework mapping

Selected mappings returned by the catalogue are:

| Mandard | Framework controls |
|---|---|
| **MCP-M-001** | NIST SP 800-53 Rev. 5: AC-4, SC-8, SI-4, AU-6, SA-11; ISO/IEC 27001:2022: A.8.16; SOC 2: CC7.2 |
| **MCP-M-002** | NIST SP 800-53 Rev. 5: IA-2, IA-5, AC-2, AC-3, AC-4, AC-6, AC-7, AC-12, SC-8, SC-23 |
| **MCP-M-003** | NIST SP 800-53 Rev. 5: SC-12, SC-13, SC-8, SI-10, SR-3, SR-4, SA-11, SA-12; PCI DSS v4.0: Requirements 3, 4, and 6; ISO/IEC 27001:2022: A.8.24 |
| **MCP-M-004** | NIST SP 800-53 Rev. 5: AC-4, SC-7, CM-2, CM-7, AU-6, SR-3, SR-4, SA-12, SA-22 |

## Required actions

1. **Block changed or unapproved tools — Platform Security / MCP gateway owner**  
   Per **MCP-M-001**, create an approved inventory containing the canonical tool name, description, input schema, and return schema. Pin its cryptographic hash and reject execution whenever the current definition differs from the approved version.

2. **Enforce requester-context authorization — IAM and application owners**  
   Per **MCP-M-002**, authenticate remote sessions using OAuth 2.0 with PKCE and authorize each invocation against the current requester. Do not allow an MCP server’s service identity to confer broader authority than the requesting user.

3. **Prevent duplicate or altered state changes — MCP client and server owners**  
   Per **MCP-M-003**, sign the complete message, validate the sender-bound key, and reject reused nonces, stale timestamps, missing signatures, and modified payloads. Both endpoints should sign and verify messages.

4. **Constrain blast radius — Infrastructure and platform owners**  
   Per **MCP-M-004**, sandbox each server with only the filesystem paths, network destinations, credentials, and system capabilities needed for its approved tools. Isolate MCP servers from one another and monitor cross-server data flows.

5. **Control server onboarding and change — Security Architecture and application owner**  
   Per **MCP-M-004**, permit installation only from verified sources using reviewed code and integrity-checked packages. Record explicit consent for the exact command and publisher, and require renewed consent after a tool-definition change.

6. **Apply capacity and execution boundaries — API platform owner**  
   Per **MCP-M-002**, enforce per-user, per-session, or per-tenant rate limits, quotas, and timeouts. This limits repeated or runaway state-changing calls.

7. **Add invocation-level safeguards for consequential actions**  
   **Advisory (not catalogue-backed):** classify MCP tools as read-only, mutating, or destructive. Default-deny mutating tools until explicitly approved; require step-up confirmation showing the target, proposed change, and impact; use dual approval for destructive or high-value actions; require idempotency keys and rollback procedures; and retain immutable records of approvals and outcomes.

No knowledge document specifically mapped to the MCP mandards was found for these implementation safeguards.

## Evidence for audit

- Approved MCP tool inventory containing full schemas, owners, permitted environments, and pinned hashes.
- Gateway logs showing a hash check immediately before each execution and rejection of modified definitions.
- OAuth client registration, PKCE configuration, authorization policy, session-binding tests, TLS verification, host allowlist, quotas, and timeout configuration.
- Automated negative tests for cross-user sessions, confused-deputy attempts, unexpected hosts, and excessive request rates.
- Message-signing configuration and test results showing rejection of tampered payloads, duplicate nonces, stale timestamps, and unsigned requests.
- Sandbox configuration demonstrating restricted filesystem, network, capabilities, and credentials.
- Package provenance, code-review, publisher-verification, and integrity-check records.
- User consent records showing the server publisher and exact installation or connection command, including re-consent after changes.
- For advisory invocation controls: approval records, transaction identifiers, before-and-after state, execution outcome, and rollback evidence.

## Assumptions and limits

The framework table contains selected mappings visible in the tool results and is not represented as the complete mapping set. The knowledge search returned tangential application and authentication documents but no MCP-specific document mapped to **MCP-M-001** through **MCP-M-004**, so those documents were set aside. The catalogue does not currently provide a dedicated Mandard requiring per-invocation human approval, separation of duties, rollback, or immutable audit logging specifically for state-changing MCP tools; a new Mandard should be drafted if these are to be enforceable requirements.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**MCP-M-001**](https://verify.example-org.internal/?id=MCP-M-001) | Critical | Model Context Protocol | AIUC1 (D003); CIS_CONTROLS (CIS 8); COBIT_2019 (DSS05.07, MEA03.01); EU_AI_ACT (Article 14, Article 15, Article 9); ISO_27001 (A.8.16); ISO_42001 (A.6.2, A.8.3, A.9.2); +12 more |
| [**MCP-M-002**](https://verify.example-org.internal/?id=MCP-M-002) | Critical | Model Context Protocol | AIUC1 (B006, E009); CIS_CONTROLS (CIS 3, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285, CWE-327); EU_AI_ACT (Article 14, Article 15, Article 9); GDPR (Article 32); +16 more |
| [**MCP-M-003**](https://verify.example-org.internal/?id=MCP-M-003) | High | Model Context Protocol | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04); CWE (CWE-327); EU_AI_ACT (Article 14, Article 15, Article 9); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +18 more |
| [**MCP-M-004**](https://verify.example-org.internal/?id=MCP-M-004) | High | Model Context Protocol | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 12, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, BAI09.01); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-798); ENISA_SMLA (SMLA-20); +23 more |

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