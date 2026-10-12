# Prepared Instruments for the Deferred Practitioner Evaluation

These are the qualitative protocols and Likert batteries prepared for the
practitioner evaluation described as future work in the dissertation. **No
responses were collected and no participant was recruited**; the artefact was
evaluated analytically, with its outputs rather than its users as the unit of
analysis. The instruments are published so that a continuation study can adopt
or adapt them, and so that the claim that the design is "prepared rather than
merely proposed" is independently checkable.

Ethical approval obtained for the present study does not extend to a
practitioner study. Any continuation must secure fresh Ethics Review Board
approval before recruiting. The consent instrument is reproduced in Appendix C
of the dissertation.

---
### Appendix A: Qualitative Interview Protocols
Two semi-structured protocols are used, matched to the persona under assessment .

#### A.1 Cohort D — Developer Protocol (Codi)
The following protocol evaluates software engineers' experience following interaction with the localised MCP agent within their VSCode workspace:
1.  **Warm-up:** Could you briefly describe your experience level in software engineering and your familiarity with secure coding practices and DevSecOps pipelines?
2.  **Perceived Friction:** How did the localised MCP agent affect your coding flow? Did the inline, statement-level warnings and suggested patches save time compared to traditional backend pipeline alerts?
3.  **Trust and Explainability:** How did you perceive the trustworthiness of the security recommendations? Did the inclusion of direct URI links back to the centralised 'mandards' portal influence your confidence in the AI's suggestions?
4.  **Standard Fatigue:** To what extent did the automated, explainable advisory loop help you understand the abstract regulatory mandates (e.g., ISO 27001 or NIST controls)? Did this approach reduce standard fatigue or cognitive load?
5.  **Future Work:** What features, changes, or visual assets would you recommend adding to the portal or IDE extension to further improve your experience and make security compliance feel more seamless?

#### A.2 Cohort G — Governance Protocol (Sage)
The following protocol evaluates security architects, security champions, GRC analysts and compliance officers following a governance-consultation task with the portal persona:
1.  **Warm-up:** Could you briefly describe your role, your experience in security architecture or GRC, and which compliance frameworks you work with most regularly?
2.  **Decision Confidence:** Would you be prepared to act on the response you received — for example, to take it into a design review or an exception request? What, if anything, would you need to verify independently first, and why?
3.  **Transparency and Citation:** How did the cited mandard identifiers and the explicit separation of catalogue-backed content from advisory content affect your confidence? Did the "Assumptions and limits" section change how far you were willing to rely on the answer?
4.  **Cross-Framework Reasoning:** How accurately did the response map between frameworks you know well? Did it surface obligations you would otherwise have had to reconcile manually across separate standards?
5.  **Audit Readiness:** Would the "Evidence for audit" content identify artefacts you would actually be asked for in an audit or assurance review? Could the response be used in a governance pack, and with how much editing?
6.  **Standard Fatigue and Future Work:** Did consolidating multi-framework obligations into cited, unified records reduce the effort of navigating overlapping requirements? What would you change about the portal or the response format?

### Appendix B: Survey Question Matrices
Two structurally parallel Likert batteries are administered, matched to the persona under assessment . Both use a 5-point scale (1 - Strongly Disagree, 2 - Disagree, 3 - Neutral, 4 - Agree, 5 - Strongly Agree). Items are deliberately constructed in parallel across the shared constructs of Trust, Transparency, Friction and Fatigue, permitting cautious cross-persona comparison; Audit Readiness is unique to the governance battery, since Sage's output is intended to withstand audit scrutiny rather than to patch code.

#### B.1 HAX-D Battery — Cohort D (Codi, 12 items)

| Item ID | Category | Survey Question Statement |
| :--- | :--- | :--- |
| **HAX-D-01** | Trust | *I trust the security patches and code remediations recommended by the MCP agent.* |
| **HAX-D-02** | Trust | *The recommendations provided by the localised agent felt reliable and contextually accurate.* |
| **HAX-D-03** | Trust | *I felt comfortable applying the automated code patches directly within my local workspace.* |
| **HAX-D-04** | Transparency | *The agent made it clear why a specific line of code violated corporate security controls.* |
| **HAX-D-05** | Transparency | *The direct URI links back to the online portal were highly helpful for clarifying policy rules.* |
| **HAX-D-06** | Transparency | *The explanations provided by the agent were written in clear, human-understandable language.* |
| **HAX-D-07** | Friction | *The inline warnings and interactive patches did not disrupt my natural development velocity.* |
| **HAX-D-08** | Friction | *Remediating vulnerabilities in the IDE was easier than reviewing late-stage pipeline failure logs.* |
| **HAX-D-09** | Friction | *The user interface of the VSCode extension was clean, non-intrusive, and easy to navigate.* |
| **HAX-D-10** | Fatigue | *The explainable feedback loop significantly reduced my mental cognitive load during development.* |
| **HAX-D-11** | Fatigue | *I feel less "standard fatigue" when compliance laws are automated and explained contextually.* |
| **HAX-D-12** | Fatigue | *I am more likely to adhere to security standards when they are made directly actionable in my IDE.* |

#### B.2 HAX-G Battery — Cohort G (Sage, 12 items)

| Item ID | Category | Survey Question Statement |
| :--- | :--- | :--- |
| **HAX-G-01** | Trust | *I trust the mandards and framework mappings that Sage cited in its responses.* |
| **HAX-G-02** | Trust | *Sage's mapping to frameworks I know well (e.g., ISO/IEC 27001 or NIST SP 800-53) matched my own professional judgement.* |
| **HAX-G-03** | Trust | *I would be comfortable using a Sage response as the basis for a documented governance decision or exception.* |
| **HAX-G-04** | Transparency | *Sage made clear which parts of its answer were drawn from the mandard catalogue and which were advisory.* |
| **HAX-G-05** | Transparency | *The "Assumptions and limits" section helped me judge how far to rely on the response.* |
| **HAX-G-06** | Transparency | *The cited mandard identifiers allowed me to verify Sage's claims independently.* |
| **HAX-G-07** | Friction | *Consulting Sage was faster than locating equivalent guidance through existing policy documentation.* |
| **HAX-G-08** | Friction | *The structure of Sage's responses let me find the information I needed without re-reading.* |
| **HAX-G-09** | Audit Readiness | *The "Evidence for audit" section identified artefacts I would genuinely be asked to produce in an assurance review.* |
| **HAX-G-10** | Audit Readiness | *A Sage response could be included in a governance pack with little or no editing.* |
| **HAX-G-11** | Fatigue | *Sage reduced the effort required to reconcile overlapping requirements across multiple frameworks.* |
| **HAX-G-12** | Fatigue | *I feel less "standard fatigue" when multi-framework obligations are consolidated and cited automatically.* |

