# G69-TXN

## Question
What controls are required for transaction integrity across distributed services?

## Sage response

## Bottom line

The SAGF catalogue contains no Mandard that directly governs distributed transaction semantics such as atomicity, idempotency, ordering, exactly-once processing, compensation, or reconciliation. A new Mandard is therefore required if these behaviours are to be enforceable and auditable; existing Mandards provide supporting security controls for authenticated and encrypted service communication, authorization, auditability, segmentation, monitoring, and exception management.

## Risk and impact

Failure to control distributed transactions can cause duplicate payments, lost or out-of-order updates, inconsistent ledgers, unreconciled balances, and disputes that cannot be reconstructed. The supporting SAGF exposure is **Critical** where service identities, authorization, or transport protection are absent, and **High** where auditability, data handling, segmentation, monitoring, or deviation governance is deficient.

The catalogue does not assign a risk level specifically to failed atomicity, idempotency, or reconciliation because no corresponding Mandard was found.

## Governing Mandards

### Critical

| Mandard | Title | Required control |
|---|---|---|
| **AC-M-001** | Mandatory Authorization Checks | Per **AC-M-001**: every sensitive or state-changing endpoint must perform explicit, deny-by-default authorization, including permission and resource-level checks. |
| **MSA-M-001** | Service-to-Service Authentication (mTLS/JWT) | Per **MSA-M-001**: service calls must be authenticated using mTLS or digitally signed JWTs; plaintext and unauthenticated calls are prohibited. |
| **CONT-M-005** | mTLS Certificate Management & Rotation | Per **CONT-M-005**: inter-service mTLS must verify service identity, use TLS 1.3 or higher, rotate certificates automatically within 90 days, and check revocation on every connection. |
| **CRYPT-M-002** | Encryption in Transit (TLS 1.3+) | Per **CRYPT-M-002**: HTTPS, gRPC, messaging, and internal service traffic must use TLS 1.3 or higher with deprecated protocols and weak ciphers disabled. |

### High

| Mandard | Title | Required control |
|---|---|---|
| **DATA-M-002** | Data Classification & Handling | Per **DATA-M-002**: services must declare data sensitivity and apply classification-appropriate transit, storage, and retention controls. |
| **DB-M-005** | Database Activity Monitoring and Audit Logging | Per **DB-M-005**: privileged actions, schema changes, authentication, and sensitive-data access must be captured in tamper-resistant logs, forwarded centrally, retained, and monitored. |
| **LOG-M-001** | Stream Logs to SIEM | Per **LOG-M-001**: applications must actively stream logs at `INFO` level or higher to a central SIEM. |
| **LOG-M-003** | Configure Centralized Log Aggregation and SIEM Alerting for CI/CD | Per **LOG-M-003**: CI/CD audit logs and alerts must detect unauthorized pipeline changes, gate bypasses, and artifact-validation failures. This supports the integrity of deployed transaction-processing components rather than runtime transaction semantics. |
| **LOG-M-004** | Trusted Time Synchronization for Security Events | Per **LOG-M-004**: participating systems must use approved redundant time sources, unambiguous UTC timestamps, and alert on material drift or synchronization failure. |
| **MON-M-001** | Monitor for Config Drift | Per **MON-M-001**: unauthorized production configuration changes must be continuously detected and alerted. |
| **NSEG-M-002** | DMZ & Network Segmentation | Per **NSEG-M-002**: public, application, and database tiers must be segmented, with only explicitly required ports and protocols allowed between them. |
| **GOV-G-006** | Security Deviation and Exception Management | Per **GOV-G-006**: departures must be independently approved before release, risk-owned, supported by compensating controls, recorded in the assurance pack, and assigned an expiry date. |

## Framework mapping

The following mappings were returned by the Mandard catalogue and are directly relevant:

| Mandard | Framework mappings |
|---|---|
| **MSA-M-001** | NIST SP 800-53 Rev.5: `SC-8` Transmission Confidentiality and Integrity, `SI-7` Software, Firmware, and Information Integrity, `IA-5` Authenticator Management, `AC-4` Information Flow Enforcement |
| **CRYPT-M-002** | NIST SP 800-53 Rev.5: `SC-12`, `SC-13`, `SC-7`, `AC-4`; PCI DSS v4.0: `Req 4`; ISO/IEC 27001:2022: `A.8.24`, `A.5.14`, `A.8.20`; GDPR: `Article 32`; OWASP ASVS 5.0: `V12` |
| **DB-M-005** | NIST SP 800-53 Rev.5: `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SI-7`; PCI DSS v4.0: `Req 10` |
| **LOG-M-001** | NIST SP 800-53 Rev.5: `AU-2`, `AU-6`, `AU-12`, `SI-4`, `SI-7`; PCI DSS v4.0: `Req 10`; ISO/IEC 27001:2022: `A.8.15`, `A.8.16`, `A.5.28` |
| **LOG-M-004** | ISO/IEC 27001:2022: `A.8.17`; NIST SP 800-82r3: `6.2.12` |
| **NSEG-M-002** | NIST SP 800-53 Rev.5: `SC-7`, `AC-4`; PCI DSS v4.0: `Req 1`; ISO/IEC 27001:2022: `A.8.20`, `A.8.22`, `A.8.21`; CIS Controls v8: `CIS 12` |
| **GOV-G-006** | NIST SP 800-53 Rev.5: `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022: `A.5.1`, `A.5.35`; SOC 2: `CC3`, `CC5`; NIST CSF 2.0: `GV.RM`, `GV.OV`, `ID.RA` |

## Required actions

1. **Enforce authenticated, encrypted service paths — Critical.**  
   Platform Engineering must enforce strict mTLS or signed JWT authentication, TLS 1.3 or higher, service-identity verification, automatic certificate rotation, and revocation checking across synchronous APIs and message brokers. This implements **MSA-M-001**, **CONT-M-005**, and **CRYPT-M-002**.

2. **Authorize every transaction mutation — Critical.**  
   Application teams must apply centralized, deny-by-default authorization to transaction creation, update, reversal, replay, compensation, and administrative endpoints. Authorization must consider caller identity, permission, and the affected resource, per **AC-M-001**.

3. **Restrict messaging and data paths — High.**  
   Per **NSEG-M-002**, restrict network flows to named service paths and required ports. The MQ implementation standard **VeriFy-INT-MQ-001**—mapped to **AC-M-001**, **CONT-M-005**, **CRYPT-M-002**, **GOV-G-006**, **MSA-M-001**, and **NSEG-M-002**—requires mutual authentication of message-channel peers, service-account mapping, and subscriber access limited to required topics or queues.  
   Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981128

4. **Build an end-to-end transaction audit trail — High.**  
   Per **DB-M-005**, **LOG-M-001**, and **LOG-M-004**, propagate a transaction or correlation identifier through every participating service and record state changes, caller/service identity, trusted UTC time, outcome, and affected resource in tamper-resistant centralized logs. Avoid sensitive payloads unless classification and handling controls under **DATA-M-002** permit them.

   The audit standard **VeriFy-AUD-002**—mapped to **DATA-M-002**, **DB-M-005**, **GOV-G-006**, **LOG-M-001**, **LOG-M-003**, **LOG-M-004**, and **MON-M-001**—requires end-to-end transactional and administrative logging across architectural layers for Confidential and Highly Confidential data, centralized collection, and non-repudiation.  
   Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981664

5. **Monitor control drift and delivery-pipeline bypasses — High.**  
   Operations must alert when mTLS, broker authorization, audit forwarding, time synchronization, or network policies are disabled or modified outside approved deployment paths, per **MON-M-001**. CI/CD Security must monitor gate bypasses and unauthorized pipeline changes per **LOG-M-003**.

6. **Govern exceptions — High.**  
   Any inability to meet these controls must be recorded before release with technical justification, compensating controls, residual-risk owner, independent approval, and expiry date per **GOV-G-006**.

7. **Define the missing transaction-integrity control.**  
   No knowledge document was found for atomicity, idempotency, ordering, duplicate suppression, compensation, or reconciliation.

   **Advisory (not knowledge-doc backed):** draft a new Mandard requiring:
   - Globally unique transaction and idempotency keys.
   - Atomic persistence of local state and outbound events, such as a transactional outbox.
   - Idempotent consumers with durable duplicate detection.
   - Explicit delivery and ordering semantics for each transaction flow.
   - Bounded retries with backoff, dead-letter handling, and controlled replay.
   - Saga compensation or an equivalent recovery model for partially completed workflows.
   - Automated reconciliation against the system of record.
   - Integrity constraints, version checks, and protection against stale concurrent writes.
   - Failure-injection tests covering duplicates, reordering, timeouts, broker outages, and partial commits.
   - Defined ownership and service-level objectives for unresolved or inconsistent transactions.

## Evidence for audit

- Service-mesh policy proving strict mTLS, service identity verification, TLS version, and certificate rotation.
- Broker channel-authentication records, topic/queue access controls, and service-account mappings.
- API authorization test results proving unauthorized transaction mutations return `401` or `403`.
- Network-policy or firewall evidence showing only approved service and database flows.
- SIEM records demonstrating end-to-end correlation across application, integration, and database layers.
- Database audit configuration and sample tamper-resistant audit events.
- Time-synchronization health reports and drift alerts.
- Configuration-drift monitoring reports and tested alerts.
- CI/CD evidence for security gates and attempted gate-bypass detection.
- Approved, unexpired deviation records where any Mandard is not met.
- Once the proposed transaction-integrity Mandard exists: duplicate-delivery, replay, partial-failure, compensation, and reconciliation test reports.

## Assumptions and limits

The catalogue search returned no direct Mandard for distributed transaction semantics. Existing controls therefore secure and evidence the transaction path but do not, by themselves, prove business-level atomicity, exactly-once effects, successful compensation, or ledger reconciliation. The retrieved MQ guidance references TLS 1.2, but **CRYPT-M-002** and **CONT-M-005** require TLS 1.3 or higher; the Mandards take precedence, and any incompatibility requires governance under **GOV-G-006**.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**CONT-M-005**](https://verify.example-org.internal/?id=CONT-M-005) | Critical | Container Security | CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-327, CWE-798); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +10 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**DB-M-005**](https://verify.example-org.internal/?id=DB-M-005) | High | Database Security | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.16, A.5.17); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); +8 more |
| [**LOG-M-001**](https://verify.example-org.internal/?id=LOG-M-001) | High | Logging | AIUC1 (E009, E015); CIS_CONTROLS (CIS 17, CIS 8); COBIT_2019 (DSS01, DSS02.01, DSS05.07); CSA_CCM (LOG); ENISA_SMLA (SMLA-28); EU_AI_ACT (Article 12); +14 more |
| [**LOG-M-003**](https://verify.example-org.internal/?id=LOG-M-003) | High | Logging | CIS_CONTROLS (CIS 13, CIS 15, CIS 17); COBIT_2019 (APO10.01, APO10.04, DSS02.01); CSA_CCM (LOG); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1), 164.312(b)); ISA_62443 (SR 1.1, SR 3.1, SR 5.1); +14 more |
| [**LOG-M-004**](https://verify.example-org.internal/?id=LOG-M-004) | High | Logging | ISO_27001 (A.8.17); MITRE_ATT&CK (M1029, M1047); NIST_800_82 (6.2.12) |
| [**MON-M-001**](https://verify.example-org.internal/?id=MON-M-001) | High | Monitoring | AIUC1 (C008); CIS_CONTROLS (CIS 12, CIS 17, CIS 4); COBIT_2019 (APO13.01, BAI03.03, BAI06.01); CSA_CCM (CCC, DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); ENISA_SMLA (SMLA-12); +13 more |
| [**MSA-M-001**](https://verify.example-org.internal/?id=MSA-M-001) | Critical | Microservices | CIS_CONTROLS (CIS 12, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-327, CWE-798); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |

Source: VeriFy mandard catalogue. Framework citations are read from the recorded control mappings, not inferred by the assistant.
## Scoring notes
- actionability: pass (provisional auto-score)
- citation_correctness: pass (provisional auto-score)
- evidence_audit: pass (provisional auto-score)
- framework_mapping: pass (provisional auto-score)
- risk_impact: pass (provisional auto-score)
- bottom_line: pass (provisional auto-score)
- governing_mandards: fail (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass