# G31-OAUTH

## Question
What controls are required for secure OAuth token lifecycle management?

## Sage response

## Bottom line

Secure OAuth token lifecycle management requires both SAGF OAuth mandards: **OAUTH-M-001** for token security and validation, and **OAUTH-M-002** for least-privilege scopes, consent, and immediate revocation. Systems must enforce PKCE for native and SPA clients, short token lifetimes, server-side validation, granular scopes, explicit consent, step-up authentication for sensitive scope changes, and immediate invalidation upon revocation.

## Risk and impact

| Priority | Exposure |
|---|---|
| **Critical** | Weak issuance or validation can permit forged, expired, redirected, or stolen tokens to cause account takeover and unauthorized API access. |
| **High** | Excessive scopes or ineffective revocation can preserve unauthorized access and expose more data or functionality than the user intended. |

The catalogue does not explicitly establish requirements for refresh-token rotation, replay-family detection, token storage mechanisms, or signing-key rotation. These controls should not be represented as SAGF requirements until mapped to another applicable Mandard or a new Mandard is approved.

## Governing mandards

| Mandard | Title | Risk | Required control |
|---|---|---:|---|
| **OAUTH-M-001** | OAuth 2.0 Token Security & Validation | **Critical** | Per **OAUTH-M-001**: native and SPA clients must use PKCE; access tokens must expire in under one hour and refresh tokens in under 30 days; token validation must verify signature, expiration, and scopes; tokens must not appear in URLs. The implementation detail also requires validation of `iss` and `aud` on every request and recommends asymmetric `RS256` rather than `HS256`. |
| **OAUTH-M-002** | OAuth 2.0 Scope Limitation & Consent | **High** | Per **OAUTH-M-002**: scopes must be minimal and specific, users must explicitly consent to each scope, sensitive scope changes require re-authentication, and revocation must immediately invalidate all tokens. Resource servers must enforce required scopes. |

## Framework mapping

Selected mappings returned by the SAGF catalogue are:

| Mandard | Framework | Mapped controls |
|---|---|---|
| **OAUTH-M-001** | NIST SP 800-53 Rev. 5 | IA-2, IA-4, IA-5, IA-8, AC-4, AC-7, SC-8, SC-12, SR-3, SR-4, SA-12 |
| **OAUTH-M-001** | PCI DSS v4.0 | Req 8 |
| **OAUTH-M-001** | ISO/IEC 27001:2022 | A.5.16, A.5.17, A.5.19, A.5.21, A.8.5, A.8.24, A.8.30 |
| **OAUTH-M-001** | SOC 2 | CC6.1 |
| **OAUTH-M-001** | OWASP ASVS 5.0 | V4, V6, V10 |
| **OAUTH-M-002** | NIST SP 800-53 Rev. 5 | AC-2, AC-3, AC-4, AC-6, AC-7, IA-2, IA-4, IA-5, IA-8, SC-8, SC-12, SC-28, MP-4, SI-12, PT-3, PT-5 |
| **OAUTH-M-002** | PCI DSS v4.0 | Req 7, Req 8 |
| **OAUTH-M-002** | ISO/IEC 27001:2022 | A.5.15, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5, A.8.24 |

## Required actions

1. **Enforce token validation at every resource server — Application Security and API owners**
   - Per **OAUTH-M-001**, verify the signature, approved signing algorithm, `iss`, `aud`, `exp`, and required scopes before granting access.
   - Reject unsigned tokens, the `none` algorithm, modified payloads, expired tokens, untrusted issuers, and tokens issued for another audience.
   - Use asymmetric `RS256` signing rather than shared-secret `HS256`, as specified by the Mandard implementation detail.

2. **Apply PKCE to applicable clients — Identity Platform owner**
   - Per **OAUTH-M-001**, require PKCE for native applications and SPAs.
   - Configure the authorization server to reject applicable authorization-code requests that lack a valid PKCE challenge and verifier.

3. **Configure maximum token lifetimes — Identity Platform owner**
   - Per **OAUTH-M-001**, configure access-token lifetime below one hour and refresh-token lifetime below 30 days.
   - Ensure resource servers enforce expiry independently rather than relying only on client behavior.

4. **Prevent URL exposure — Application and API owners**
   - Per **OAUTH-M-001**, do not place tokens in query strings, URL paths, redirects, browser history, referrer-bearing URLs, or URL-based logging fields.
   - Use the `Authorization: Bearer` header for access-token presentation.

5. **Enforce granular authorization — Product owner and API owner**
   - Per **OAUTH-M-002**, define narrow, operation-specific scopes rather than broad scopes such as `all`.
   - Validate the required scope at each protected operation and return an authorization failure when the token lacks it.

6. **Control consent and scope elevation — Identity and UX owners**
   - Per **OAUTH-M-002**, present each requested scope for explicit user consent.
   - Require re-authentication before granting sensitive new or expanded scopes.
   - Retain a record of the scopes, user decision, client, and decision time.

7. **Implement immediate revocation — Identity Platform owner**
   - Per **OAUTH-M-002**, revocation must invalidate all applicable tokens immediately.
   - Test access and refresh-token use after revocation to demonstrate that previously issued credentials no longer grant access.

**Knowledge-backed implementation context:** **VeriFy-AUTH-NID-001**, mapped to **OAUTH-M-001**, describes the identity provider as responsible for token issuance, federation, claims handling, and cryptographic token validation; it identifies OIDC with JWT access, refresh, and identity tokens as a preferred integration pattern. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981012

**Advisory (not catalogue-backed):** Consider refresh-token rotation with reuse detection, sender-constrained tokens, secure platform storage, signing-key rotation, token-family revocation, and telemetry for replay attempts. No OAuth Mandard retrieved in this review explicitly makes those lifecycle controls mandatory.

## Evidence for audit

Retain the following:

- Authorization-server configuration proving PKCE enforcement and configured access/refresh-token lifetimes.
- Automated tests showing rejection of:
  - altered or unsigned tokens;
  - unapproved algorithms;
  - expired tokens;
  - invalid `iss` or `aud`;
  - missing scopes;
  - tokens used after revocation.
- API gateway or resource-server policy showing validation on every protected request.
- Source-code and log scans demonstrating that tokens do not appear in URLs.
- OAuth client registration records containing approved redirect URIs and permitted scopes.
- Consent and re-authentication records for sensitive scope changes.
- Revocation test results proving immediate invalidation.
- Approved exception records for any departure from these requirements.

Knowledge documents authoritatively mapped to these Mandards include:

- **OAUTH-M-001**: `VeriFy-APP-002`, `VeriFy-AUTH-002`, `VeriFy-AUTH-INT-EC-001`, `VeriFy-AUTH-NAT-001`, `VeriFy-AUTH-NID-001`, `VeriFy-AUTH-SOC-001`, `VeriFy-INT-GRPH-001`, and `VeriFy-INT-REST-001`.
- **OAUTH-M-002**: `VeriFy-AUTH-SOC-001` and `VeriFy-AUTHZ-002`.

## Assumptions and limits

- No implementation, authorization-server configuration, source code, or test evidence was supplied for verification.
- The framework table contains selected mappings returned by the catalogue; the detailed tool response was truncated and the table should not be treated as an exhaustive mapping inventory.
- Refresh-token rotation, replay-family detection, token storage, and signing-key rotation were not explicitly required by the two retrieved OAuth Mandards.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**OAUTH-M-001**](https://verify.example-org.internal/?id=OAUTH-M-001) | Critical | OAuth Security | CIS_CONTROLS (CIS 15, CIS 2, CIS 5); COBIT_2019 (APO10.01, APO10.04, DSS05.04); CWE (CWE-798); ISO_27001 (A.5.16, A.5.17, A.5.19); NIST_CSF (GV.SC-01, ID.RA-09, PR.AA-01); NIST_SP_800_53 (AC-4, AC-7, IA-2); +9 more |
| [**OAUTH-M-002**](https://verify.example-org.internal/?id=OAUTH-M-002) | High | OAuth Security | CCPA_CPRA (Consumer Right to Delete, Data Minimization, Reasonable Security Procedures); CIS_CONTROLS (CIS 3, CIS 5, CIS 6); COBIT_2019 (DSS05.04); CWE (CWE-284, CWE-285, CWE-798); GDPR (Article 17, Article 25, Article 5); HIPAA (164.312(a)(1), 164.502); +10 more |

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