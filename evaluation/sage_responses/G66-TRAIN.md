# G66-TRAIN

## Question
What security training evidence is required for privileged engineering roles?

## Sage response

## Bottom line

Per **TRAIN-M-001**: anyone who designs, writes, reviews, tests, or operates software must complete role-based secure-development training **before receiving production-affecting privileges** and refresh it at least annually. Audit evidence must record, for each person and role, the training completion, assessment outcome, and refresh date; access should not be granted or retained where this evidence is missing or expired.

## Risk and impact

**Medium risk.** Without current, role-specific training, privileged engineers may introduce or fail to detect vulnerabilities in production systems. The principal exposure is that production access could remain assigned based on stale, trivial, or irrelevant training rather than demonstrated competence against the weakness classes affecting the engineer’s actual technology stack.

## Governing mandards

| Mandard | Title | Risk |
|---|---|---:|
| **TRAIN-M-001** | Secure Development Training and Security Awareness | Medium |

Per **TRAIN-M-001**:

- Training must be completed before production-affecting privileges are granted.
- Training must be refreshed at least annually.
- Curriculum must be role-based and cover applicable Mandard domains, languages, frameworks, and weakness classes present in the codebases the person touches.
- Curriculum must be revised when the Mandard catalogue changes or organisational finding trends change.
- Teams building, fine-tuning, or integrating AI/ML systems must also receive training on catalogue-defined AI risks.
- Completion, assessment outcome, and refresh date must be recorded per person and per role as auditable evidence.
- Curriculum delivery, record-keeping, and exception handling are operated by Tier 3 governance in the CISO office.

## Framework mapping

The catalogue maps **TRAIN-M-001** to:

| Framework | Control |
|---|---|
| NIST SP 800-53 Rev. 5 | AT; AT-2; AT-3 |
| ISO/IEC 27001:2022 Annex A | A.6.3 |
| OWASP SAMM 2.0 | Governance: Education & Guidance |
| CIS Critical Security Controls v8 | CIS 14 |
| NIST CSF 2.0 | PR.AT; PR.AT-01; PR.AT-02 |
| NIST AI RMF 1.0 | GOVERN-4 |
| NIST SSDF SP 800-218 | PO.2; PO.2.2 |
| TOGAF | Secure Development Lifecycle |
| MITRE ATT&CK | M1013; M1017 |
| ENISA SMLA | SMLA-31 |
| NIST SP 800-82r3 | 5.2.1; 6.2.2 |

## Required actions

1. **CISO Tier 3 governance:** Establish and maintain a role-to-curriculum matrix covering applicable technologies, weakness classes, and Mandard domains.
2. **Engineering and IAM owners:** Prevent assignment of production-affecting privileges until required training and assessment are complete.
3. **Training owner:** Assign training when a person joins or changes a privileged engineering role and set it to expire no later than 365 days after completion.
4. **IAM or GRC operations:** Reconcile training records against the identity directory and privileged-access inventory to identify missing or expired training.
5. **Security governance:** Update curricula following catalogue changes or shifts in internal vulnerability and incident findings.
6. **AI/ML engineering leadership:** Add AI-specific security training for personnel who build, fine-tune, or integrate AI/ML systems.

No knowledge document currently references **TRAIN-M-001**. Consequently, no organisation-specific procedure beyond the Mandard’s own implementation instructions was found.

## Evidence for audit

The minimum evidence package is:

- A named-user training record showing:
  - person or identity;
  - privileged engineering role;
  - assigned role-based curriculum;
  - completion status and date;
  - assessment outcome;
  - next refresh or expiry date.
- The approved role-to-curriculum matrix.
- A training-system completion export covering the audit population.
- A reconciliation report comparing training status with identities holding production-affecting privileges, including missing and expired records.
- Evidence that access was gated until completion, such as an IAM/PAM workflow, access-control configuration, or access approval record containing the training check.

**Advisory (not knowledge-doc backed):** Retain curriculum version, assessment score or pass/fail threshold, access-grant date, reviewer, and any approved exception alongside the required record. These fields make it easier to prove that training was relevant and current when privilege was granted.

## Assumptions and limits

Actual training records, IAM/PAM configurations, access gates, curricula, and exception records were not inspected. No knowledge document is currently mapped to **TRAIN-M-001**, so organisation-specific retention periods, evidence formats, and exception procedures could not be verified.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**TRAIN-M-001**](https://verify.example-org.internal/?id=TRAIN-M-001) | Medium | Security Training & Awareness | CIS_CONTROLS (CIS 14); ENISA_SMLA (SMLA-31); ISO_27001 (A.6.3); MITRE_ATT&CK (M1013, M1017); NIST_800_82 (5.2.1, 6.2.2); NIST_AI_RMF (GOVERN-4); +5 more |

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