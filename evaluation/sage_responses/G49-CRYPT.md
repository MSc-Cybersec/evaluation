# G49-CRYPT

## Question
What cryptographic controls are mandatory for regulated customer data?

## Sage response

## Bottom line

Regulated customer data must be encrypted at rest and in transit, with controlled key lifecycles, approved algorithms, managed certificates, and hardware protection for high-value keys. Failure exposes customer records to disclosure, interception, regulatory breach, and loss of cryptographic trust. Approve these controls as release gates and require a formally documented deviation where compliance is not technically feasible.

## Risk and impact

- **Critical:** Unencrypted stored data or network traffic can expose customer data directly following storage compromise, interception, or man-in-the-middle attack.
- **High:** Weak algorithms, long-lived keys, expired certificates, or software-stored master keys increase compromise duration, service disruption, and future decryption risk.
- Regulated customer data is exposed across databases, file systems, backups, caches, APIs, internal service traffic, and cryptographic key stores.

## Governing mandards

| Mandard | Mandatory control | Risk |
|---|---|---:|
| **CRYPT-M-001**, Encryption at Rest | Per **CRYPT-M-001**: encrypt all sensitive data in databases, file systems, backups, and caches using AES-256 or equivalent; manage keys separately from encrypted data. | **Critical** |
| **CRYPT-M-002**, Encryption in Transit TLS 1.3+ | Per **CRYPT-M-002**: use TLS 1.3 or higher for HTTPS, gRPC, and internal service-to-service traffic; disable deprecated protocols and weak ciphers. | **Critical** |
| **CRYPT-M-003**, Key Rotation & Lifecycle Management | Per **CRYPT-M-003**: document and automate key generation, rotation, revocation, and destruction; rotate static keys at least annually and dynamic keys more frequently. | **High** |
| **CRYPT-M-004**, Algorithm Selection & Post-Quantum Readiness | Per **CRYPT-M-004**: use current NIST-approved algorithms, inventory cryptographic dependencies, and establish a post-quantum migration plan by 2030. | **High** |
| **CRYPT-M-005**, Certificate Management & Pinning | Per **CRYPT-M-005**: automate certificate management and renewal before expiry; implement certificate pinning for critical APIs. | **High** |
| **CRYPT-M-006**, HSM for High-Value Keys | Per **CRYPT-M-006**: store master keys, payment-processing keys, and long-term signing keys in FIPS 140-2 Level 3+ HSMs or equivalent secure hardware. | **High** |

## Framework mapping

The catalogue returned the following direct mappings. Only verified mappings are shown.

| Framework | Returned controls |
|---|---|
| NIST SP 800-53 Rev. 5 | `SC-12` Cryptographic Key Establishment and Management; `SC-13` Cryptographic Protection; `SC-28` Protection of Information at Rest |
| PCI DSS v4.0 | `Req 3` Protect Stored Account Data; `Req 4` Protect Cardholder Data in Transit |
| ISO/IEC 27001:2022 | `A.8.24` Use of cryptography; `A.5.34` Privacy and protection of PII |
| HIPAA Security Rule | `164.312(a)(2)(iv)` Encryption |
| GDPR | `Article 32` Security of Processing |
| OWASP ASVS 5.0 | `V11` Cryptography; `V14` Data Protection |
| CIS Controls v8 | `CIS 3` Data Protection |
| NIST CSF 2.0 | `PR.PS-06` Secure Software Development Practices |
| CWE | `CWE-327` Use of a Broken or Risky Cryptographic Algorithm |

## Required actions

1. **Encrypt every regulated-data store.**  
   Per **CRYPT-M-001**, enable AES-256 or equivalent encryption for databases, object storage, file systems, volumes, backups, snapshots, and caches. Keep keys in a separate KMS or vault rather than alongside ciphertext.  
   **Owner:** Data platform and cloud/platform engineering.

2. **Enforce encrypted transport end to end.**  
   Per **CRYPT-M-002**, set TLS 1.3 as the minimum for customer endpoints, APIs, gRPC, message channels, database connections, and internal service traffic. Disable deprecated protocols and weak cipher suites.  
   **Owner:** Network, platform, and application engineering.

3. **Centralise and automate key management.**  
   Per **CRYPT-M-003**, maintain a key inventory, named owners, intended purpose, cryptoperiod, rotation schedule, revocation process, and destruction record. Enable automated rotation and alert on failed or overdue rotations.  
   **Owner:** Cryptographic key custodian or platform security.

4. **Eliminate weak or unmanaged cryptography.**  
   Per **CRYPT-M-004**, restrict implementations to approved algorithms and libraries, detect prohibited algorithms through code scanning, inventory RSA and ECC dependencies, and maintain the required post-quantum migration roadmap.  
   **Owner:** Security architecture and engineering leads.

5. **Automate certificate lifecycle management.**  
   Per **CRYPT-M-005**, automate certificate issuance and renewal, monitor expiration, and apply certificate pinning to critical APIs.  
   **Owner:** PKI, platform, and API teams.

6. **Move high-value keys into qualifying hardware.**  
   Per **CRYPT-M-006**, identify master, payment-processing, root CA, and long-term signing keys and place them in FIPS 140-2 Level 3+ HSMs or equivalent secure hardware. Prevent plaintext export and provide resilient HSM backup arrangements.  
   **Owner:** PKI and cryptographic key custodians.

7. **Record deviations in the governance pack.**  
   The knowledge guidance states that non-compliance must be formally recorded as a deviation in the SAF pack with technical justification. Source: **VeriFy-APP-002**, mapped to **CRYPT-M-001** — [Application Layer Governance](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817782).

No knowledge document was found that was directly mapped to **CRYPT-M-002** through **CRYPT-M-006** in the returned results. The remaining search hits were set aside because they were database/authentication documents or did not provide authoritative mappings to those cryptographic mandards.

## Evidence for audit

| Mandard | Minimum audit evidence |
|---|---|
| **CRYPT-M-001** | Data-store inventory; encryption configuration exports; KMS key references; infrastructure scan showing encrypted databases, storage, backups, and caches |
| **CRYPT-M-002** | TLS scan results; load-balancer and service-mesh configurations; pipeline gate rejecting deprecated protocols or weak ciphers |
| **CRYPT-M-003** | Key register; approved lifecycle procedure; rotation configuration; rotation, revocation, and destruction logs; overdue-rotation alerts |
| **CRYPT-M-004** | Approved-algorithm standard; static-analysis results; cryptographic inventory; documented post-quantum migration roadmap |
| **CRYPT-M-005** | Certificate inventory; automated renewal configuration; expiry monitoring; critical-API pinning test results |
| **CRYPT-M-006** | High-value-key classification; HSM certification and configuration; evidence of non-exportability; key-origin and backup verification |
| Governance | SAF approval or formally approved deviation with technical justification, owner, expiry date, and compensating controls |

## Assumptions and limits

“Regulated customer data” is assumed to fall within the mandard definition of sensitive data. The precise legal obligations depend on data type, processing jurisdiction, contractual requirements, and whether payment-card or health data is involved. Some framework-mapping payloads were truncated by the tool, so the mapping table includes only mappings visible in the returned results.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**CRYPT-M-001**](https://verify.example-org.internal/?id=CRYPT-M-001) | Critical | Cryptography | CIS_CONTROLS (CIS 11, CIS 17, CIS 3); COBIT_2019 (DSS02.01, DSS05.07, MEA03.01); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +13 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**CRYPT-M-003**](https://verify.example-org.internal/?id=CRYPT-M-003) | High | Cryptography | CIS_CONTROLS (CIS 3); CSA_CCM (CEK); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); +10 more |
| [**CRYPT-M-004**](https://verify.example-org.internal/?id=CRYPT-M-004) | High | Cryptography | CIS_CONTROLS (CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.24); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-005**](https://verify.example-org.internal/?id=CRYPT-M-005) | High | Cryptography | CIS_CONTROLS (CIS 11, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.34, A.8.13, A.8.14); MITRE_ATT&CK (M1041); +9 more |
| [**CRYPT-M-006**](https://verify.example-org.internal/?id=CRYPT-M-006) | High | Cryptography | CIS_CONTROLS (CIS 15, CIS 2, CIS 3); COBIT_2019 (APO10.01, APO10.04); CSA_CCM (CEK); CWE (CWE-327); DORA (Art. 17-23, Art. 24-27, Art. 28-44); GDPR (Article 32); +14 more |

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