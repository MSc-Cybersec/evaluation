# G47-SCA

## Question
What is the minimum SCA evidence required to block vulnerable dependencies?

## Sage response

## Bottom line

The minimum evidence is a **CI/CD SCA scan result tied to the build or commit, plus an enforced pipeline-gate result showing that the build fails when any High or Critical CVE is detected**. Per **SCA-M-001**, a report without proof of enforcement is insufficient: the normative requirement is to block both **High and Critical** vulnerable dependencies.

## Risk and impact

**Critical risk.** An unenforced or incomplete SCA gate can allow known exploitable third-party components into production, exposing applications to supply-chain compromise.

The catalogue contains two SCA mandards. Only **SCA-M-001** governs vulnerability blocking; **SCA-M-002** separately governs dependency licences.

## Governing mandards

| Mandard | Title | Risk | Requirement |
|---|---|---:|---|
| **SCA-M-001** | No Critical CVEs | Critical | Per **SCA-M-001**: the build MUST fail when SCA detects a **Critical or High** severity CVE in a third-party library or dependency. |
| **SCA-M-002** | Approved Licenses | Critical | Per **SCA-M-002**: the build MUST fail when SCA detects a dependency with a non-approved licence. This is separate from vulnerability blocking. |

## Framework mapping

Mappings returned for **SCA-M-001** include:

| Framework | Controls |
|---|---|
| NIST SP 800-53 Rev. 5 | RA-3, AU-2, AU-6, AU-12, SI-4, SR-3, SR-4, SA-12, SA-22 |

## Required actions

1. **Configure the SCA scan in the build pipeline.** Per **SCA-M-001**, scan project dependency manifests and resolve third-party component versions against a vulnerability database.
2. **Set the blocking threshold to High and Critical.** The mandard description requires both severities to fail the build. Do not rely on the example configuration that shows only `critical`; that example is narrower than the normative requirement.
3. **Ensure the gate cannot be skipped silently.** The pipeline must record a failed status when the threshold is breached.
4. **Remediate blocked dependencies.** Upgrade to a patched version or replace the component where no patch exists.
5. **Separately enforce licence policy.** Per **SCA-M-002**, non-approved licences must also fail the build.

**Advisory (not knowledge-doc backed):** Retain the scanner and vulnerability-database versions where available, because they improve repeatability during audit.

## Evidence for audit

Retain this minimum evidence set for each release candidate:

1. **SCA result linked to the commit/build**, identifying:
   - scanned dependency and version;
   - CVE identifier;
   - severity;
   - scan timestamp or pipeline run.
2. **Pipeline gate configuration** demonstrating that both `High` and `Critical` findings are blocking.
3. **Pipeline execution result** showing:
   - a pass where no blocking findings exist; or
   - a failed build when a High or Critical CVE is present.
4. **Remediation result**, where applicable, showing the patched or replacement dependency and a successful rescan.

The mapped knowledge document **VeriFy-CE-001**, *Consumer / Endpoint Layer Guardrails*—mapped to **SCA-M-001**—requires applicable security-assessment results and release-pipeline evidence to be maintained for consumer and endpoint solutions. Source: https://wiki.example-org.internal/wiki/spaces/PMDAAME/pages/652022082

No knowledge document was found that defines a more specific evidence package for **SCA-M-002**.

## Assumptions and limits

The catalogue does not prescribe a retention period, mandatory report format, or named SCA product. The four-part evidence set above is the minimum defensible interpretation of **SCA-M-001**; scanner-version retention is advisory rather than knowledge-document-backed.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**SCA-M-001**](https://verify.example-org.internal/?id=SCA-M-001) | Critical | Supply Chain Analysis | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); CSA_CCM (TVM); ENISA_SMLA (SMLA-08); HIPAA (164.312(b)); ISO_27001 (A.5.19, A.5.21, A.8.15); +16 more |
| [**SCA-M-002**](https://verify.example-org.internal/?id=SCA-M-002) | Critical | Supply Chain Analysis | CIS_CONTROLS (CIS 15, CIS 2, CIS 7); COBIT_2019 (APO10.01, APO10.04, DSS05.07); ISO_27001 (A.5.19, A.5.21, A.5.31); MITRE_ATT&CK (M1016, M1051); NIST_CSF (DE.AE-02, DE.CM-01, GV.SC-01); NIST_SP_800_53 (AU-6, RA-3, SA-12); +7 more |

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