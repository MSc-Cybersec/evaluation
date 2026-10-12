# G58-INTEG

## Question
What controls govern secure system-to-system integrations?

## Sage response

## Bottom line

Secure system-to-system integrations require authenticated service identities, deny-by-default authorization, TLS 1.3 or higher, and protection of every sensitive endpoint. External, token-based, or intermediary-routed integrations require additional controls for segmentation, certificate lifecycle, token validation, rate limiting, and message-level protection; any exception must be formally approved before release.

## Risk and impact

The governing Mandards carry **Critical** and **High** risk. Failure can permit service impersonation, unauthorized data access, token forgery, interception or alteration of data, lateral movement from external systems, denial of service, and unmanaged residual risk.

Controls apply according to the integration pattern:

- **All integrations:** service authentication, authorization and encrypted transport.
- **Sensitive APIs:** authentication on every endpoint.
- **mTLS integrations:** automated certificate rotation and service identity verification.
- **OAuth/JWT integrations:** full token and signature validation.
- **Public APIs:** rate limiting.
- **External integrations:** network segmentation.
- **Cross-boundary or TLS-terminating intermediaries:** message-level signing and, for confidential payloads, encryption.
- **Any non-compliance:** approved, time-bounded deviation.

## Governing Mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **MSA-M-001** | Service-to-Service Authentication (mTLS/JWT) | Critical | Per **MSA-M-001**: authenticate service-to-service traffic with mTLS or digitally signed JWTs; plaintext and unauthenticated calls are prohibited. |
| **AC-M-001** | Mandatory Authorization Checks | Critical | Per **AC-M-001**: sensitive endpoints must perform explicit, deny-by-default authorization, including role, permission and resource-access checks. |
| **CRYPT-M-002** | Encryption in Transit (TLS 1.3+) | Critical | Per **CRYPT-M-002**: use TLS 1.3 or higher for HTTPS, gRPC and internal service traffic; disable deprecated protocols and weak ciphers. |
| **API-M-005** | Auth on Sensitive API | Critical | Per **API-M-005**: every sensitive API endpoint must reject requests lacking valid authentication with `401` or `403`. |
| **CONT-M-005** | mTLS Certificate Management & Rotation | Critical | Per **CONT-M-005**: mTLS certificates must rotate automatically within 90 days, use TLS 1.3+, verify service identity and undergo revocation checking. |
| **OAUTH-M-001** | OAuth 2.0 Token Security & Validation | Critical | Per **OAUTH-M-001**: validate token signature, issuer, audience, expiry and scopes; enforce token lifetimes and prevent tokens appearing in URLs. |
| **API-M-007** | JWT Signature Validation | Critical | Per **API-M-007**: verify every received JWT signature and explicitly reject `alg:none`. |
| **API-M-006** | Rate Limiting Enforced | Critical | Per **API-M-006**: public APIs must enforce throttling and return `429 Too Many Requests` when limits are exceeded. |
| **NSEG-M-002** | DMZ & Network Segmentation | High | Per **NSEG-M-002**: place Internet-facing components in a DMZ, restrict connections through explicit firewall rules and keep databases outside the DMZ. |
| **API-M-013** | Message-Level Integrity and Confidentiality | High | Per **API-M-013**: sign sensitive messages crossing organisational boundaries or TLS-terminating intermediaries, and encrypt confidential payloads to the intended recipient. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: document departures before release, including justification, residual-risk owner, compensating controls, independent approval and expiry. |

## Framework mapping

The following are catalogue-returned mappings relevant to these controls; this is a concise selection rather than an exhaustive reproduction of every mapping.

| Mandard | Returned framework mappings |
|---|---|
| **MSA-M-001** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-4, SC-7, SC-8, SC-12, SC-13; PCI DSS v4.0: Req 4, Req 8 |
| **AC-M-001** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, IA-2 |
| **CRYPT-M-002** | NIST SP 800-53 Rev.5: SC-12, SC-13, SC-7, AC-4; PCI DSS v4.0: Req 1, Req 4; ISO/IEC 27001:2022: A.8.20, A.8.22, A.8.24, A.5.14; GDPR: Article 32; OWASP ASVS 5.0: V11, V12, V14 |
| **API-M-005** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-4, SA-11, SI-10 |
| **API-M-006** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-7, AC-4, SC-8, SA-11, SI-10 |
| **API-M-007** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-7, SA-11 |
| **OAUTH-M-001** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-4, SC-8; ISO/IEC 27001:2022: A.5.16, A.5.17, A.8.5; OWASP ASVS 5.0: V4, V6, V10 |
| **CONT-M-005** | NIST SP 800-53 Rev.5: CM-6, SC-12, SC-13, SC-28 |
| **NSEG-M-002** | NIST SP 800-53 Rev.5: SC-7, AC-4, CM-2, CM-6; PCI DSS v4.0: Req 1; ISO/IEC 27001:2022: A.8.20, A.8.21, A.8.22, A.8.27; NIST CSF 2.0: PR.IR-01, PR.PS-01 |
| **API-M-013** | NIST SP 800-53 Rev.5: SC-8, SC-13, SC-23, SI-7; ISO/IEC 27001:2022: A.5.14, A.8.24; OWASP ASVS 5.0: V11, V14; SOC 2: CC6 |
| **GOV-G-006** | NIST SP 800-53 Rev.5: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |

## Required actions

1. **Establish service identity and authentication — Integration Engineering**
   - Enforce mTLS or signed service JWTs under **MSA-M-001**.
   - Reject plaintext and unidentified callers.
   - Where mTLS is used, automate issuance, revocation checking and rotation within 90 days under **CONT-M-005**.
   - The integration guidance identifies mTLS, service credentials, and user-context JWT/OAuth patterns by trust context. The Mandard requirement takes precedence: a client secret alone must not replace the authentication required by **MSA-M-001**.  
     Source: **VeriFy-INT-REST-001**, mapped to **MSA-M-001**, **CONT-M-005**, **OAUTH-M-001**, and **API-M-007** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

2. **Enforce least-privilege authorization — Application/API Owner**
   - Apply centralized, deny-by-default authorization to every sensitive operation under **AC-M-001**.
   - Check the caller’s service identity, allowed role or scope, operation and target resource.
   - Ensure sensitive endpoints return `401` or `403` when credentials are absent or invalid, per **API-M-005**.
   - The REST integration standard requires system roles or user scopes and claims to be enforced at the endpoint according to least privilege.  
     Source: **VeriFy-INT-REST-001**, mapped to **AC-M-001** and **API-M-005** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

3. **Protect transport — Platform and Network Engineering**
   - Configure TLS 1.3 as the minimum and disable weak protocols and cipher suites under **CRYPT-M-002**.
   - Configure certificate hostname and service-identity verification; do not merely encrypt the channel without authenticating the peer.
   - The REST knowledge document still references TLS 1.2. That conflicts with **CRYPT-M-002** and **CONT-M-005**; the current Mandard requirement of TLS 1.3+ governs.  
     Source of the conflicting guidance: **VeriFy-INT-REST-001**, mapped to **CRYPT-M-002** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

4. **Validate OAuth and JWT credentials — Identity and API Engineering**
   - Validate signature, issuer, audience, expiry and scopes on every request under **OAUTH-M-001**.
   - Use an explicit algorithm allow-list and reject unsigned tokens and `alg:none` under **API-M-007**.
   - Apply user-context tokens only where user delegation is required; maintain distinct authorization policies for system and user identities.

5. **Protect external integration boundaries — Network Security**
   - Place Internet-facing providers or consumers behind segmented ingress/egress controls under **NSEG-M-002**.
   - Permit only required source identities, destinations, ports and protocols; do not locate databases in the DMZ.
   - Apply public API rate limits under **API-M-006**.
   - The integration standard makes network segmentation applicable to external integrations.  
     Source: **VeriFy-INT-002**, mapped to **NSEG-M-002** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947827

6. **Protect messages end to end — Integration Engineering**
   - Where TLS terminates at a gateway, proxy or partner intermediary, sign sensitive messages and verify the signature before processing under **API-M-013**.
   - Encrypt confidential payloads to the recipient’s key.
   - Manage signing and encryption keys through the approved key-management service with defined rotation.
   - The REST standard identifies JWS signing and JWE encryption for external patterns where technically feasible; **API-M-013** makes this mandatory when its boundary or intermediary conditions apply.  
     Source: **VeriFy-INT-REST-001**, mapped to **API-M-013** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981099

7. **Govern exceptions — Risk Owner and independent InfoSec authority**
   - Before release, register any unmet control under **GOV-G-006**.
   - Record the affected Mandard, technical justification, compensating controls, residual-risk owner, independent approval and expiry.
   - Attach the approved deviation to the security assurance pack.  
     Source: **VeriFy-INT-002**, mapped to **GOV-G-006** — https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947827

## Evidence for audit

Retain the following artefacts:

- Service-mesh or gateway policy proving strict mTLS or signed-token enforcement.
- TLS scan showing TLS 1.3 and approved cipher suites only.
- PKI configuration and reports showing certificate validity, identity verification, revocation checks and automated rotation.
- API inventory linking each sensitive endpoint to authentication and authorization middleware.
- Negative integration tests showing unauthenticated and unauthorized requests return `401` or `403`.
- JWT tests showing rejection of tampered, expired, wrong-audience and `alg:none` tokens.
- Rate-limit tests showing public endpoints return `429`.
- Network diagrams, firewall rules and reachability scans proving DMZ and database separation.
- Message-signature tampering tests and evidence of payload encryption where **API-M-013** applies.
- Approved, unexpired deviation records for any control override.

## Assumptions and limits

No specific protocol, trust boundary, data classification or deployment platform was provided. The answer therefore uses the enterprise integration-layer standard **VeriFy-INT-002

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**AC-M-001**](https://verify.example-org.internal/?id=AC-M-001) | Critical | Access Control | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-269, CWE-284, CWE-285); HIPAA (164.312(a)(1)); ISA_62443 (SR 2); ISO_27001 (A.5.15, A.5.16, A.5.18); +9 more |
| [**API-M-005**](https://verify.example-org.internal/?id=API-M-005) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (AIS); CWE (CWE-306, CWE-798); ISO_27001 (A.5.16, A.5.17, A.8.24); NIST_CSF (PR.AA-01, PR.AA-05, PR.DS-01); +8 more |
| [**API-M-006**](https://verify.example-org.internal/?id=API-M-006) | Critical | API Security | CIS_CONTROLS (CIS 16, CIS 17, CIS 5); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.5.24); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, AU-12); +8 more |
| [**API-M-007**](https://verify.example-org.internal/?id=API-M-007) | Critical | API Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**API-M-013**](https://verify.example-org.internal/?id=API-M-013) | High | API Security | ISO_27001 (A.5.14, A.8.24); NIST_CSF (PR.AA, PR.DS); NIST_SP_800_53 (SC-13, SC-23, SC-8); OWASP_ASVS (V11, V14); SOC2 (CC6) |
| [**CONT-M-005**](https://verify.example-org.internal/?id=CONT-M-005) | Critical | Container Security | CIS_CONTROLS (CIS 3, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); CSA_CCM (IVS: Infrastructure & Virtualization Security); CWE (CWE-327, CWE-798); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); +10 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**MSA-M-001**](https://verify.example-org.internal/?id=MSA-M-001) | Critical | Microservices | CIS_CONTROLS (CIS 12, CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-327, CWE-798); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISO_27001 (A.5.16, A.5.17, A.5.19); +12 more |
| [**NSEG-M-002**](https://verify.example-org.internal/?id=NSEG-M-002) | High | Network Segmentation | CIS_CONTROLS (CIS 12, CIS 4); COBIT_2019 (BAI09.01, DSS05.02); ISO_27001 (A.8.20, A.8.21, A.8.22); MITRE_ATT&CK (M1030, M1035); NIST_800_82 (5.2.3); NIST_CSF (PR.IR-01, PR.PS-01); +4 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |

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