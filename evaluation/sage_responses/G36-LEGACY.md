# G36-LEGACY

## Question
What controls are mandatory when supporting legacy protocols temporarily?

## Sage response

## Bottom line

Temporary support for a legacy or deprecated protocol is non-compliant with the secure transport baseline and may proceed only under a formally approved, time-bounded security deviation. The release must be blocked unless the deviation identifies the affected control, technical justification, residual-risk owner, compensating controls, independent approval, and expiry date; the legacy path must then be removed when the exception ends.

## Risk and impact

The primary exposure is interception, downgrade, impersonation, lateral movement, and continued operation of an unsupported attack surface.

| Exposure | Applicable Mandard | Risk |
|---|---|---:|
| Deprecated or weak transport remains enabled | **CRYPT-M-002** | Critical |
| Service-to-service traffic is unauthenticated | **MSA-M-001** | Critical |
| Exception becomes undocumented or permanent | **GOV-G-006** | High |
| External legacy endpoint can reach internal systems | **NSEG-M-002** | High |
| Credentials, firewall rules, certificates, or interfaces remain after migration | **DECOM-M-001** | High |

## Governing mandards

- **CRYPT-M-002 — Encryption in Transit (TLS 1.3+) — Critical.** Per **CRYPT-M-002**: data in transit must use TLS 1.3 or higher, and weak ciphers and deprecated protocols must be disabled. Temporary legacy support is therefore a deviation, not an approved baseline.
- **MSA-M-001 — Service-to-Service Authentication (mTLS/JWT) — Critical.** Per **MSA-M-001**: service-to-service communication must use mTLS with certificate authentication or digitally signed JWTs; plaintext and unauthenticated calls are prohibited.
- **GOV-G-006 — Security Deviation and Exception Management — High.** Per **GOV-G-006**: before release, every departure must record the affected control, technical justification, residual risk and accepting owner, compensating controls, and expiry date. Approval must come from an authority independent of the delivery team, with review at expiry and no indefinite renewal without re-justification.
- **NSEG-M-002 — DMZ & Network Segmentation — High.** Per **NSEG-M-002**: internet-facing applications must reside in a DMZ separated from internal networks, with only explicitly required ports and protocols permitted through firewalls; databases must not reside in the DMZ.
- **DECOM-M-001 — Secure Decommissioning and Data Destruction — High.** Per **DECOM-M-001**: at decommissioning, dependent network exposure, access paths, credentials and certificates must be removed, alongside the required retention and secure-erasure activities.

## Framework mapping

Only tool-returned mappings are shown.

| Mandard | Framework mappings |
|---|---|
| **CRYPT-M-002** | NIST SP 800-53: SC-12, SC-13, SC-7, AC-4; PCI DSS v4.0: Req 1, Req 4; ISO/IEC 27001:2022: A.8.24, A.8.20, A.8.22, A.5.14; GDPR: Article 32; OWASP ASVS 5.0: V11, V12, V14 |
| **MSA-M-001** | NIST SP 800-53: IA-2, IA-5, SC-8, SC-12, SC-13, SI-4, AU-6, SC-7; PCI DSS v4.0: Req 3, Req 4, Req 8 |
| **GOV-G-006** | NIST SP 800-53: CA-5, PM-4, RA-3, PL-2; ISO/IEC 27001:2022: A.5.1, A.5.35; SOC 2: CC3, CC5; OWASP SAMM 2.0: Governance: Policy & Compliance; COBIT 2019: APO12.01, MEA02; NIST CSF 2.0: GV.RM, GV.OV, ID.RA |
| **NSEG-M-002** | NIST SP 800-53: CM-6, CM-2, SC-7, AC-4, SC-5; PCI DSS v4.0: Req 1; ISO/IEC 27001:2022: A.8.9, A.8.20, A.8.21, A.8.22, A.8.27; CIS Controls v8: CIS 4, CIS 12; NIST CSF 2.0: PR.IR-01, PR.PS-01 |
| **DECOM-M-001** | NIST SP 800-53: MP-6, CM-8, SA-22, AC-2; ISO/IEC 27001:2022: A.8.10; SOC 2: P4; GDPR: Article 17; CIS Controls v8: CIS 1, CIS 3; NIST CSF 2.0: ID.AM, PR.DS |

## Required actions

1. **Create and approve the deviation before release — Security owner and independent risk authority.**  
   Per **GOV-G-006**, record:
   - The exact legacy protocol, versions, endpoints, systems, and affected control.
   - Technical and business justification.
   - Residual risk and named accepting owner.
   - Enforced compensating controls.
   - Migration or retirement milestone and fixed expiry date.
   - Approval by an authority independent of the delivery team.

   The deviation must be included in the Security Assurance Framework pack. This procedure is supported by **VeriFy-INT-002**, mapped to **GOV-G-006**, **CRYPT-M-002**, **MSA-M-001**, and **NSEG-M-002**:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947827

2. **Minimise the protocol exposure — Network and platform owners.**  
   Per **NSEG-M-002**, place an external legacy endpoint in the DMZ and restrict firewall rules to the specific source, destination, port, and protocol required. Do not expose databases or unrelated internal services.

   For external transfers, **VeriFy-DATA-EA-001**, mapped to **CRYPT-M-002**, **NSEG-M-002**, and **GOV-G-006**, specifies approved transfer patterns such as SFTP, certificate-authenticated Connect Direct, isolated inbound folders, and controlled HTTPS access:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659947980

3. **Preserve authenticated service communication — Application and integration owners.**  
   Per **MSA-M-001**, retain mTLS or signed-JWT authentication for service-to-service communication. A protocol exception does not authorise plaintext or unauthenticated service calls.

4. **Enforce an expiry gate — Release management and GRC.**  
   Per **GOV-G-006**, fail deployment or continued operation when the deviation is missing, unapproved, expired, ownerless, or not linked to the affected system. At expiry, remediate, close, or submit a newly justified approval; do not renew indefinitely.

5. **Remove the legacy path completely — Service owner.**  
   Per **DECOM-M-001**, after migration remove obsolete firewall and WAF rules, DNS entries, API interfaces, service accounts, access groups, certificates, infrastructure, and monitoring inventory entries. Update the CMDB and asset register.

   The detailed retirement checklist is in **VeriFy-DECOM-002**, mapped to **DECOM-M-001**, **GOV-G-006**, and **NSEG-M-002**:  
   https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/720666741

6. **Advisory (not knowledge-doc backed):** Restrict the exception to dedicated gateways where possible, prohibit general client negotiation of the legacy protocol, alert on every legacy connection, and track usage reduction toward zero.

## Evidence for audit

- Approved, unexpired deviation record linked to the affected change and system.
- Security assurance pack containing the technical justification and approval.
- Residual-risk acceptance identifying the accountable owner.
- Configuration proving the exact permitted protocol, endpoints, sources, destinations, ports, and ciphers.
- TLS or protocol scan showing secure protocols elsewhere and the narrowly scoped exception.
- Firewall, DMZ, security-group, or network-policy export proving segmentation.
- mTLS or signed-JWT configuration and failed unauthenticated-connection test.
- Expiry review, migration plan, and tracked retirement date.
- Decommissioning record proving removal of rules, DNS, certificates, identities, interfaces, and asset records.

## Assumptions and limits

“Legacy protocol” was interpreted as a deprecated or weak transport protocol. No dedicated legacy-protocol Mandard was found; the mandatory treatment derives from **CRYPT-M-002** and the exception process in **GOV-G-006**, with segmentation, service authentication, and decommissioning controls applying according to architecture and lifecycle. The **CRYPT-M-002** implementation text mentions TLS 1.2 and 1.3, but its normative description requires TLS 1.3 or higher; the normative requirement should govern unless an approved deviation states otherwise.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**DECOM-M-001**](https://verify.example-org.internal/?id=DECOM-M-001) | High | Decommissioning & Destruction | CCPA_CPRA (Consumer Right to Delete, Storage Limitation); CIS_CONTROLS (CIS 1, CIS 3); GDPR (Article 17); ISO_27001 (A.8.10); NIST_CSF (ID.AM, PR.DS); NIST_SP_800_53 (AC-2, CM-8, MP-6); +1 more |
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
- governing_mandards: pass (provisional auto-score)
- required_actions: pass (provisional auto-score)
- assumptions_limits: pass (provisional auto-score)
- hallucination_check: pass (provisional auto-score)
- overall_pass: pass