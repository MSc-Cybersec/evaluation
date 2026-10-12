# G68-PROV

## Question
What evidence confirms provenance integrity for released binaries and images?

## Sage response

## Bottom line

Provenance integrity is confirmed when each released binary or container image is cryptographically bound by digest to a verifiable build-provenance attestation, and the signature resolves to an approved build identity. The SAGF catalogue maps supply-chain mandards to provenance controls but does not currently contain a mandard explicitly requiring signed provenance for every released artifact; the evidence criteria below are therefore advisory pending a dedicated mandard.

## Risk and impact

**High risk.** Without verifiable provenance, malicious or accidentally altered artifacts can be substituted after build, during registry promotion, or before deployment. This exposes production systems to unauthorized code, compromised dependencies, unapproved build tooling, and an inability to establish release accountability during audit or incident response.

Per **SUPPLY-M-001**: third-party components above the defined risk threshold require documented assessment and production approval, including structured evaluation of open-source components.

Per **SUPPLY-M-002**: development platforms and build tooling must be vetted, approved, inventoried, and protected from untrusted tooling.

Neither mandard expressly requires digest-bound, signed release attestations.

## Governing mandards

| Mandard | Title | Risk level | Relevance |
|---|---|---:|---|
| **SUPPLY-M-001** | Third-Party Risk Assessment | High | Requires assessment, approval, monitoring, and pipeline gating for applicable third-party components. |
| **SUPPLY-M-002** | Secure Development Platform and Tooling Integrity | High | Requires trusted, approved development and build tooling. |

## Framework mapping

The following relevant mappings were returned by the mandard catalogue:

| Mandard | Framework | Control |
|---|---|---|
| **SUPPLY-M-001** | NIST SP 800-53 Rev. 5 | SR-4 — Provenance |
| **SUPPLY-M-001** | NIST SP 800-53 Rev. 5 | SR-3 — Supply Chain Controls and Processes |
| **SUPPLY-M-001** | NIST SP 800-53 Rev. 5 | SA-12 — Supply Chain Protection |
| **SUPPLY-M-002** | NIST SP 800-53 Rev. 5 | SR-4 — Provenance |
| **SUPPLY-M-002** | NIST SP 800-53 Rev. 5 | SR-3 — Supply Chain Controls and Processes |
| **SUPPLY-M-002** | NIST SP 800-53 Rev. 5 | SA-12 — Supply Chain Protection |
| **SUPPLY-M-002** | ISO/IEC 27001:2022 | A.5.21 — Managing information security in the ICT supply chain |
| **SUPPLY-M-002** | OWASP Top 10:2025 | A03:2025 — Software Supply Chain Failures |

## Required actions

**Advisory (not catalogue-backed):** Require the following evidence package for every released binary and image:

1. **Digest-bound provenance attestation**
   - Identifies the released artifact using an immutable cryptographic digest, such as `SHA-256`.
   - Records source repository and commit, approved builder identity, build workflow, build parameters, timestamps, and input materials.
   - Uses an established machine-verifiable provenance format.

2. **Valid cryptographic signature**
   - Signature verification succeeds against an approved key or workload identity.
   - The signer is the authorized CI/CD builder, not an uncontrolled developer workstation.
   - Certificate validity, identity claims, revocation status, and—where used—transparency-log inclusion are verified.

3. **Digest continuity**
   - The binary checksum or container manifest digest matches the subject digest in the attestation.
   - The promoted and deployed artifact uses that same digest; mutable image tags alone are insufficient.
   - Repackaging or modification after attestation invalidates the release.

4. **Pipeline enforcement record**
   - The release pipeline blocks unsigned artifacts, invalid attestations, unapproved builders, and digest mismatches.
   - The retained job record identifies the workflow revision, source commit, builder identity, verification policy, result, and released digest.

5. **Artifact-bound SBOM**
   - The SBOM identifies the same artifact digest and is generated from the released output.
   - For applicable third-party components, link the SBOM to the assessment and approval required by **SUPPLY-M-001**.

6. **Trusted build environment evidence**
   - Per **SUPPLY-M-002**, retain the approved build-tool inventory and evidence that unreviewed tools or extensions were blocked.
   - Record the build-runner image, toolchain versions, and endpoint or workload security posture.

7. **Immutable publication and promotion history**
   - Preserve registry or repository events showing who published and promoted the artifact, when it occurred, and which digest was involved.
   - Prevent released versions and tags from being overwritten.

## Evidence for audit

A defensible audit sample should contain:

- Released binary checksum or container manifest digest.
- Signed provenance attestation naming that exact digest.
- Successful signature and identity-verification output.
- Trusted-root or signer policy used for verification.
- Source commit and protected release-tag record.
- CI/CD build and release-gate logs.
- Artifact-bound SBOM and its verification result.
- Build-tool approval inventory supporting **SUPPLY-M-002**.
- Third-party assessment and approval records supporting **SUPPLY-M-001**, where applicable.
- Immutable registry publication and environment-promotion logs.
- Exception or deviation approval for any release that did not pass the standard gate.

The strongest confirmation is an independently repeatable verification showing:

```text
released digest
= attested subject digest
= repository digest
= promoted digest
= deployed digest
```

## Assumptions and limits

No released binary, image, signature, attestation, SBOM, pipeline configuration, or registry record was inspected. No knowledge document was found that defines an organization-specific procedure for binary or image provenance verification; the retrieved documents were set aside because they address general application governance, endpoint guardrails, authentication, or third-party risk rather than artifact-level provenance. A dedicated release-provenance mandard should be drafted if this evidence is to be mandatory across projects.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**SUPPLY-M-001**](https://verify.example-org.internal/?id=SUPPLY-M-001) | High | Supply Chain Security | AIUC1 (E006); CCPA_CPRA (Service Provider and Contractor Obligations); CIS_CONTROLS (CIS 15, CIS 17, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CSA_CCM (STA); ENISA_SMLA (SMLA-20, SMLA-22); +18 more |
| [**SUPPLY-M-002**](https://verify.example-org.internal/?id=SUPPLY-M-002) | High | Supply Chain Security | CIS_CONTROLS (CIS 15, CIS 2); COBIT_2019 (APO10.01, APO10.04, APO12.01); CWE (CWE-798); ISO_27001 (A.5.17, A.5.19, A.5.21); NIST_CSF (GV.OC-01, GV.RM-01, GV.SC-01); NIST_SP_800_53 (IA-5, PL-2, PL-8); +6 more |

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