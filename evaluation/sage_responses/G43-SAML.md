# G43-SAML

## Question
What controls are required before federating SAML with an external IdP?

## Sage response

## Bottom line

Do not approve external SAML federation until the service provider rejects unsigned, invalid, expired, misdirected, or improperly confirmed assertions, as required by **SAML-M-001**. If assertions contain confidential attributes, go-live also requires assertion encryption, HTTPS, and HTTP-POST binding under **SAML-M-002**. Failure exposes the application to account takeover, assertion forgery, and disclosure of personal or authorization data.

## Risk and impact

| Priority | Exposure | Business impact |
|---|---|---|
| Critical | Acceptance of forged, unsigned, expired, or misdirected assertions | Account takeover, unauthorized access, and privilege misuse |
| High | Confidential attributes exposed in plaintext | PII disclosure, credential or role leakage, and regulatory exposure |

## Governing mandards

- **SAML-M-001 — SAML Assertion Validation & Signature — Critical**  
  Per **SAML-M-001**: assertions must be digitally signed by a trusted IdP and signature validation must occur before acceptance. Validate `NotOnOrAfter`, bearer subject confirmation, `Destination`, `Audience`, and `Recipient`; never accept unsigned assertions.

- **SAML-M-002 — SAML Encryption & Attribute Protection — High**  
  Per **SAML-M-002**: assertions containing confidential attributes must use `EncryptedAssertion`; sensitive attributes must not appear unencrypted. SAML transport must use HTTPS and assertion delivery must use HTTP-POST rather than HTTP-Redirect binding.

## Framework mapping

Only catalogue-returned mappings are shown.

| Mandard | Framework mappings |
|---|---|
| **SAML-M-001** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-7, AC-4, SC-8, SR-3, SR-4, SA-12, IA-4, IA-8; PCI DSS v4.0: Req 8; ISO/IEC 27001:2022: A.5.17, A.8.5, A.5.19, A.5.21, A.8.30, A.5.16; SOC 2: CC6.1; OWASP ASVS 5.0: V6, V4; OWASP Top 10:2025: A03, A07, A08; OWASP API Security Top 10:2023: API1, API2, API3, API4 |
| **SAML-M-002** | NIST SP 800-53 Rev.5: IA-2, IA-5, AC-7, SC-12, SC-13, SC-28, SI-12, MP-4, AC-4, SC-8, IA-4, IA-8, PT-3, PT-5; PCI DSS v4.0: Req 3, Req 4, Req 8; ISO/IEC 27001:2022: A.5.17, A.8.5, A.8.24, A.5.34, A.8.11, A.5.16; HIPAA Security Rule: 164.312(a)(2)(iv), 164.502; SOC 2: CC6.1 |

## Required actions

1. **Enforce assertion authenticity — Critical; owner: application/IAM engineering**
   - Per **SAML-M-001**, require signed assertions and perform XML signature validation before processing identity or authorization attributes.
   - Pin trust to the approved external IdP certificate and trusted metadata source; reject unknown, invalid, or expired certificates.
   - Do not derive roles, create a session, or provision access until validation succeeds.

2. **Validate assertion context and lifetime — Critical; owner: application/IAM engineering**
   - Per **SAML-M-001**, validate `NotOnOrAfter` and bearer subject confirmation.
   - Require exact expected values for `Destination`, `Audience`, and `Recipient`.
   - Fail closed for absent, malformed, expired, or mismatched values.

3. **Test parser and signature handling — Critical; owner: security testing**
   - Per **SAML-M-001**, test manipulated assertions, XML signature-wrapping attacks, invalid signatures, unsigned assertions, and XML External Entity payloads.
   - Confirm every negative test is rejected before session creation.

4. **Protect confidential attributes — High; owner: IAM engineering and data owner**
   - Identify whether the assertion carries confidential information such as email, personal identifiers, or sensitive role information.
   - Per **SAML-M-002**, require `EncryptedAssertion` when confidential attributes are present.
   - Configure the SP encryption certificate and retain the corresponding private key under SP control. The catalogue implementation specifies AES-256.

5. **Secure the binding and transport — High; owner: platform/network engineering**
   - Per **SAML-M-002**, expose assertion-consumer endpoints only over HTTPS.
   - Use HTTP-POST binding for assertion delivery; do not use HTTP-Redirect for assertions.
   - Verify that captured SAML responses do not disclose confidential attributes in decoded plaintext.

6. **Complete design governance**
   - Knowledge guidance **VeriFy-AUTH-002** `[mandard_refs: SAML-M-001, AUTH-M-001, AUTH-M-002, AUTH-M-003, CRED-M-002, GOV-G-006, OAUTH-M-001]` states that external authentication is within scope and that non-compliance must be recorded as a formal deviation in the SAF pack with technical justification.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659817239
   - Knowledge guidance **VeriFy-AUTH-INT-EC-001** `[mandard_refs: SAML-M-001, AUTH-M-001, AUTH-M-002, AUTH-M-003, CRYPT-M-002, GOV-G-006, IAM-M-001, OAUTH-M-001, SECR-M-001]` identifies Entra ID and Entra ID App Proxy using SAML or OIDC for externally exposed web services, with MFA determined by the classification matrix and short-lived access/session lifetimes.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652445334
   - Knowledge guidance **VeriFy-AUTH-NID-001** `[mandard_refs: SAML-M-001, API-M-007, AUTH-M-001, AUTH-M-002, AUTH-M-003, CRED-M-002, CRYPT-M-002, GOV-G-006, OAUTH-M-001]` describes cryptographic token validation, claims mediation, and support for SP- and IdP-initiated SAML in the customer authentication context.  
     Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981012

**Advisory (not catalogue-backed):** Before production approval, document IdP ownership, certificate-rotation contacts, metadata change control, break-glass disablement, attribute minimisation, user deprovisioning, MFA expectations, and authentication-event monitoring. These are prudent third-party federation controls, but the retrieved SAML mandards do not establish them as universal SAML preconditions.

## Evidence for audit

Retain the following in the federation approval record:

- Approved IdP and SP metadata, including signing and encryption certificates.
- SP configuration proving mandatory signature and XML validation.
- Configuration proving exact audience, destination, recipient, lifetime, and bearer-confirmation checks.
- SAML trace showing `EncryptedAssertion` and no plaintext confidential attributes where **SAML-M-002** applies.
- HTTPS endpoint and HTTP-POST binding configuration.
- Negative security-test results for unsigned assertions, invalid signatures, expired assertions, destination/audience mismatch, signature wrapping, and XXE.
- Successful end-to-end authentication test showing that no application session is created before validation.
- SAF approval or a formally approved deviation with technical justification.

## Assumptions and limits

The catalogue returned two SAML-domain mandards. No knowledge document is currently mapped to **SAML-M-002**. The external IdP, assertion schema, data classification, MFA posture, provisioning process, certificate lifecycle, and application configuration were not examined; framework mapping records were truncated by the tool, so the mapping table may not be exhaustive.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**API-M-007**](https://verify.example-org.internal/?id=API-M-007) | Critical | API Security | CIS_CONTROLS (CIS 15, CIS 16, CIS 2); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**AUTH-M-001**](https://verify.example-org.internal/?id=AUTH-M-001) | Critical | Authentication | CIS_CONTROLS (CIS 17, CIS 5, CIS 6); COBIT_2019 (DSS02.01, DSS05.04, DSS05.07); CWE (CWE-287, CWE-798); GDPR (Article 7); ISO_27001 (A.5.16, A.5.17, A.5.24); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**AUTH-M-002**](https://verify.example-org.internal/?id=AUTH-M-002) | Critical | Authentication | CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-284, CWE-285, CWE-287); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +9 more |
| [**AUTH-M-003**](https://verify.example-org.internal/?id=AUTH-M-003) | High | Authentication | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (DSS05.04, DSS05.07, MEA03.01); CWE (CWE-287, CWE-384, CWE-798); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); MITRE_ATT&CK (M1027, M1032, M1036); +9 more |
| [**CRED-M-002**](https://verify.example-org.internal/?id=CRED-M-002) | High | Credential Management | CIS_CONTROLS (CIS 5, CIS 6, CIS 8); COBIT_2019 (BAI03.03, BAI06.01, DSS05.04); HIPAA (164.312(b)); ISO_27001 (A.5.16, A.5.17, A.8.15); NIST_CSF (DE.AE-02, DE.CM-01, PR.AA-01); NIST_SP_800_53 (AC-7, AU-12, AU-2); +8 more |
| [**CRYPT-M-002**](https://verify.example-org.internal/?id=CRYPT-M-002) | Critical | Cryptography | AIUC1 (B008); CIS_CONTROLS (CIS 12, CIS 3); CWE (CWE-327); GDPR (Article 32); HIPAA (164.312(a)(2)(iv)); ISA_62443 (SR 4); +11 more |
| [**IAM-M-001**](https://verify.example-org.internal/?id=IAM-M-001) | Critical | Identity & Access Management | AIUC1 (B007); CIS_CONTROLS (CIS 5, CIS 6); COBIT_2019 (DSS05.04); CSA_CCM (IAM); CWE (CWE-269, CWE-284, CWE-285); ENISA_SMLA (SMLA-02, SMLA-17); +14 more |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**SAML-M-001**](https://verify.example-org.internal/?id=SAML-M-001) | Critical | SAML Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); NIST_SSDF (PS.3.1, PW.4.1); +8 more |
| [**SAML-M-002**](https://verify.example-org.internal/?id=SAML-M-002) | High | SAML Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 3, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-327); GDPR (Article 17, Article 25, Article 32); HIPAA (164.312(a)(2)(iv), 164.502); +10 more |
| [**SECR-M-001**](https://verify.example-org.internal/?id=SECR-M-001) | Critical | Secrets Management | AIUC1 (A008); CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-284, CWE-285, CWE-798); HIPAA (164.312(a)(1)); ISO_27001 (A.5.15, A.5.16, A.5.17); +12 more |

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