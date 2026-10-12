# G28-EMAIL

## Question
What governance controls reduce phishing and spoofing risk for enterprise mail?

## Sage response

## Bottom line

Enterprise mail domains and subdomains must enforce SPF, DKIM, and DMARC, explicitly authorise third-party senders, and prevent those providers from using shared sending IP pools. Per **EMAIL-M-001**, absent or weak sender authentication creates a **High** risk of domain spoofing, phishing, business email compromise, loss of sender reputation, and reduced visibility of abuse. Approve a domain-wide authentication programme, with production gating for unauthorised senders and formally governed exceptions.

## Risk and impact

All applicable mandards identified are rated **High**.

- **Identity deception:** Attackers can impersonate trusted organisational domains to target employees, customers, and suppliers.
- **Financial and operational loss:** Spoofing enables credential theft, fraudulent payment instructions, malware delivery, and business email compromise.
- **Reputation and deliverability:** Shared IP pools expose organisational mail delivery to unrelated tenants’ behaviour.
- **Third-party exposure:** Email providers can introduce unapproved sending paths or inadequate authentication controls.
- **Data exposure:** Sensitive information sent through email must receive handling protections appropriate to its classification.
- **Governance exposure:** Unrecorded exceptions can turn temporary weaknesses into permanent, unowned risk.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **EMAIL-M-001** | Email Authentication and Anti-Spoofing Controls | High | Per **EMAIL-M-001**: every sending domain and subdomain must publish SPF, DKIM, and DMARC; DMARC must enforce `quarantine` or `reject`; third-party senders must be explicitly authorised, use approved domains or subdomains, and not use shared IP pools. |
| **SUPPLY-M-001** | Third-Party Risk Assessment | High | Per **SUPPLY-M-001**: third-party email services above the defined risk threshold must complete documented risk assessment before production use. |
| **DATA-M-002** | Data Classification & Handling | High | Per **DATA-M-002**: services must declare data sensitivity and apply suitable storage, transit, and retention controls. This applies to content processed by third-party email services. |
| **GOV-G-006** | Security Deviation and Exception Management | High | Per **GOV-G-006**: departures must be documented before release with justification, residual-risk owner, compensating controls, independent approval, and an expiry date. |

The complete `EMAIL-M` domain lookup returned **EMAIL-M-001** as the applicable email-specific mandard.

## Framework mapping

Relevant mappings returned by the catalogue include:

| Mandard | Framework controls |
|---|---|
| **EMAIL-M-001** | NIST SP 800-53 Rev.5: `SI-8`, `SC-8`, `SC-20`, `AC-4`; ISO/IEC 27001:2022: `A.5.14`, `A.8.20`; CIS Controls v8: `CIS 9`; SOC 2: `CC6`; NIST CSF 2.0: `PR.DS`, `PR.IR`, `DE.CM` |
| **SUPPLY-M-001** | NIST SP 800-53 Rev.5: `RA-3`, `SI-4`, `AU-6`, `SR-3`, `SR-4`, `SA-12`, `SA-22`, `PL-8`, `PM-9`, `PL-2`, `IR-4`, `IR-6`; ISO/IEC 27001:2022: `A.8.16` |
| **DATA-M-002** | NIST SP 800-53 Rev.5: `SC-28`, `SI-12`, `MP-4`, `SI-4`, `AU-6`, `IR-4`, `IR-6`; ISO/IEC 27001:2022: `A.8.24`, `A.5.34`, `A.8.16`, `A.5.24`, `A.5.26`, `A.5.12`, `A.5.13`, `A.8.33`; PCI DSS v4.0: `Req 3`; SOC 2: `CC7.2`, `CC7.3`, `C1.1`, `P1` |
| **GOV-G-006** | NIST SP 800-53 Rev.5: `CA-5`, `PM-4`, `RA-3`, `PL-2`; ISO/IEC 27001:2022: `A.5.1`, `A.5.35`; SOC 2: `CC3`, `CC5`; OWASP SAMM 2.0: `Governance: Policy & Compliance`; COBIT 2019: `APO12.01`, `MEA02`; NIST CSF 2.0: `GV.RM`, `GV.OV`, `ID.RA` |

## Required actions

1. **Inventory every sending identity and owner.**  
   Identify all organisational domains, subdomains, mail platforms, applications, marketing systems, and third parties that send mail. Per **EMAIL-M-001**, only explicitly authorised senders may send on behalf of the organisation.

2. **Enforce sender authentication.**  
   Per **EMAIL-M-001**:
   - Publish SPF records containing only authorised senders and remain within the SPF ten-lookup limit.
   - DKIM-sign all outbound mail and rotate signing keys.
   - Enable DMARC aggregate reporting.
   - Progress DMARC from monitored rollout to `p=quarantine`, then `p=reject` after confirming legitimate sender alignment.
   - Monitor for missing records, invalid syntax, policy weakening to `p=none`, and newly introduced senders.

3. **Govern third-party email routing.**  
   Per **EMAIL-M-001** and **SUPPLY-M-001**, require provider assessment and approval before production use. The implementation standard directs providers to confirm SPF, DKIM, and DMARC capability, avoid shared IP pools, and use the primary organisational domain where possible or an approved subdomain where justified.  
   Source: **VeriFy-INT-EMAIL-001**, mandard refs **EMAIL-M-001**, **SUPPLY-M-001**, **DATA-M-002**, **GOV-G-006** — [resource](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/853443233).

4. **Establish clear DNS and provider responsibilities.**  
   The provider is responsible for platform capability and avoiding shared IP pools; the organisation is responsible for corresponding DNS, SPF, DKIM, and DMARC updates when its primary domain or approved subdomain is used.  
   Source: **VeriFy-INT-EMAIL-001**, mandard refs **EMAIL-M-001**, **SUPPLY-M-001**, **DATA-M-002**, **GOV-G-006** — [resource](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/853443233).

5. **Apply data-handling requirements to email services.**  
   Per **DATA-M-002**, classify the information processed through enterprise and third-party email, then apply the required transit, storage, retention, encryption, and DLP controls for that classification.

6. **Block or govern exceptions.**  
   Per **GOV-G-006**, production release gates should reject unauthorised senders or weak authentication unless an approved, unexpired deviation exists. The deviation must identify the affected control, technical justification, residual-risk owner, compensating controls, independent approver, and expiry date.

7. **Additional anti-phishing layers.**  
   No knowledge document was found for this point. **Advisory (not knowledge-doc backed):** complement domain authentication with phishing-resistant MFA, malicious-link and attachment analysis, impersonation detection, external-sender labelling, user reporting, awareness exercises, and tested account-compromise response procedures.

## Evidence for audit

- Complete register of sending domains, subdomains, third-party providers, sending IPs, DKIM selectors, and accountable owners.
- DNS scan results proving valid SPF, DKIM, and DMARC records for every sending domain.
- DMARC configuration showing `p=quarantine` or `p=reject`, plus aggregate reports and investigation records.
- DKIM key inventory and rotation history.
- SPF lookup-limit test and authorised-sender reconciliation report.
- Evidence that third-party providers use approved domains or subdomains and do not use shared IP pools.
- Completed third-party risk assessments, contractual security requirements, and production approvals under **SUPPLY-M-001**.
- Data-classification and handling record for email content under **DATA-M-002**.
- Release-gate results showing unauthorised or non-compliant sending paths are blocked.
- Approved, time-bounded deviation records and expiry-review reports under **GOV-G-006**.

## Assumptions and limits

The catalogue’s email-specific domain returned only **EMAIL-M-001**. The retrieved implementation standard, **VeriFy-INT-EMAIL-001**, addresses third-party SMTP integration; it does not provide catalogue-backed procedures for user awareness, mailbox MFA, malicious-content inspection, or phishing incident response, so those items are explicitly labelled advisory. General integration and authentication documents returned by the initial search were set aside because they did not provide directly relevant enterprise-mail implementation detail.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**DATA-M-002**](https://verify.example-org.internal/?id=DATA-M-002) | High | Data Protection | AIUC1 (A001, A002); CCPA_CPRA (Consumer Right to Correct, Consumer Right to Delete, Notice at Collection); CIS_CONTROLS (CIS 17, CIS 3, CIS 8); COBIT_2019 (APO14, DSS02.01, DSS05.07); ENISA_SMLA (SMLA-14, SMLA-16); GDPR (Article 13, Article 16, Article 18); +13 more |
| [**EMAIL-M-001**](https://verify.example-org.internal/?id=EMAIL-M-001) | High | Email Security | CIS_CONTROLS (CIS 9); ISO_27001 (A.5.14, A.8.20); NIST_CSF (DE.CM, PR.DS, PR.IR); NIST_SP_800_53 (AC-4, SC-20, SC-8); SOC2 (CC6) |
| [**SUPPLY-M-001**](https://verify.example-org.internal/?id=SUPPLY-M-001) | High | Supply Chain Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (STA); ENISA_SMLA (SMLA-20, SMLA-22); +18 more |

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