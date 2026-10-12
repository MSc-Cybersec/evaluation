# G19-EXCEPT

## Question
What must be documented to approve a 60-day security exception?

## Sage response

## Bottom line

Per **GOV-G-006**, a 60-day security exception must be formally recorded before release, time-bounded with explicit start and expiry dates, and approved by an authority independent of the delivery team. Approval requires the affected control, technical justification, residual risk and accepting owner, compensating controls, and expiry review arrangements; without these, the exception is not approval-ready.

## Risk and impact

**High risk.** An incomplete or undocumented exception creates invisible and potentially permanent non-compliance, leaving residual exposure without accountable ownership, compensating safeguards, or a mandatory reconsideration date. Release should be blocked if the exception is unapproved, expired, ownerless, or not linked to the affected system and control.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| **GOV-G-006** | Security Deviation and Exception Management | High |

Per **GOV-G-006**, document:

1. Unique exception or deviation reference.
2. Affected system, service, change, and release.
3. Specific mandated control being departed from.
4. Technical justification explaining why compliance is not currently feasible.
5. Residual risk created by the exception.
6. Named owner who accepts that residual risk.
7. Compensating controls operating during the exception.
8. Approval authority independent of the delivery team.
9. Approval date and explicit expiry date establishing the 60-day period.
10. Review requirement on or before expiry.
11. Linkage to the assurance pack for the affected change.

The exception must not be renewed indefinitely. Any extension requires renewed justification, risk acceptance, compensating-control review, an independent approval, and a new expiry date.

## Framework mapping

The catalogue maps **GOV-G-006** to:

| Framework | Controls |
|---|---|
| NIST SP 800-53 Rev. 5 | CA-5, PM-4, RA-3, PL-2 |
| ISO/IEC 27001:2022 Annex A | A.5.1, A.5.35 |
| SOC 2 Type II Trust Services Criteria | CC3, CC5 |
| OWASP SAMM 2.0 | Governance: Policy & Compliance |
| COBIT 2019 | APO12.01, MEA02 |
| NIST CSF 2.0 | GV.RM, GV.OV, ID.RA |

## Required actions

1. **Delivery owner:** Create the exception entry before the affected change is released and link it to the applicable system, release, and control.
2. **Risk owner:** Record and formally accept the residual risk.
3. **Control owner or engineering team:** Identify implemented compensating controls and retain proof that they are operational.
4. **Independent approval authority:** Approve or reject the exception outside the delivery-team reporting line.
5. **GRC or assurance:** Set an expiry review for no later than the stated expiry date and prevent use after expiration.
6. **Release management:** Configure the release gate to require an approved, linked, and unexpired exception reference when a mandated check is overridden.
7. **Assurance owner:** Include the deviation and technical justification in the SAF pack. This procedure is stated in **VeriFy-BR-002**, mapped to **GOV-G-006**: [13. Business Risk](https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/659981693).

**Advisory (not catalogue-backed):** Also record the remediation owner, remediation milestones, target compliance date, affected data classification, and rollback or containment plan. These improve expiry decisions but are not explicit mandatory fields in **GOV-G-006**.

## Evidence for audit

Retain:

- Approved deviation-register record with immutable approval history.
- Named residual-risk owner and dated acceptance.
- Independent approver identity and approval timestamp.
- Exact approval/start and expiry dates showing the authorized 60-day term.
- Evidence that compensating controls are operating, such as configurations, test results, monitoring reports, or tickets.
- Link to the affected control, system, change record, release, and SAF pack.
- Release-gate result confirming the exception was approved and unexpired.
- Expiry-review record showing remediation, closure, or separately re-justified approval.

## Assumptions and limits

The catalogue establishes that exceptions must have a defined expiry but does not establish 60 days as a universal maximum or define whether day one is the approval date or release date. The approving authority’s specific job title and the organisation’s calendar-day calculation convention were not verified. Other mapped knowledge documents are domain-specific and should be consulted only when the exception affects those application, authentication, data, infrastructure, integration, logging, or decommissioning layers.
## Scoring notes
- actionability: pass (manual review)
- citation_correctness: pass (manual review)
- evidence_audit: pass (manual review)
- framework_mapping: pass (manual review)
- risk_impact: pass (manual review)
- bottom_line: pass (manual review)
- governing_mandards: pass (manual review)
- required_actions: pass (manual review)
- assumptions_limits: pass (manual review)
- hallucination_check: pass (manual review)
- overall_pass: pass