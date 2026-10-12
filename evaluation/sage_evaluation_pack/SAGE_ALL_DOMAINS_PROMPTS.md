# SAGE All Domains Prompts

Usage: answer each domain prompt in its corresponding response file, then score the responses using the scoring template.
The response file paths use zero-padded domain indexes.

Quick commands:

1. Run full validation and reporting pipeline:
	`python scripts/analysis/run_sage_evaluation_pipeline.py .`
2. Rebuild master scoring table and totals:
	`python scripts/analysis/build_sage_domain_summary.py .`
3. Rebuild progress by 10-domain batches:
	`python scripts/analysis/build_sage_batch_progress.py .`
4. Prefill scoring hints for a batch (example G01-G10):
	`python scripts/analysis/prefill_sage_scoring_hints.py --start 1 --end 10`
5. Show next pending runs (example next 12):
	`python scripts/analysis/next_sage_pending.py --count 12`

1. [AI] What evidence do we need to approve a high-impact AI model release?
Response file: domain-runs/G01-AI.md

2. [AUTH] What minimum controls are required before granting an auth exception for privileged users?
Response file: domain-runs/G02-AUTH.md

3. [AC] How do we prove least-privilege access is enforced for production operators?
Response file: domain-runs/G03-AC.md

4. [BACKUP] What backup evidence is mandatory before go-live of a critical service?
Response file: domain-runs/G04-BACKUP.md

5. [HDR] Which security headers are non-negotiable for internet-facing apps?
Response file: domain-runs/G05-HDR.md

6. [CSPM] What governance checks should CSPM findings trigger before release?
Response file: domain-runs/G06-CSPM.md

7. [ART] What controls are required for artifact integrity in our build and release chain?
Response file: domain-runs/G07-ART.md

8. [BIZ] How should business-risk owners accept residual cyber risk from delayed fixes?
Response file: domain-runs/G08-BIZ.md

9. [PIPE] What evidence proves pipeline controls prevent unsafe code promotion?
Response file: domain-runs/G09-PIPE.md

10. [GATE] How should we define security gate pass/fail criteria for release approval?
Response file: domain-runs/G10-GATE.md

11. [ASSURE] What independent assurance artefacts are needed for quarterly compliance attestation?
Response file: domain-runs/G11-ASSURE.md

12. [BOT] What policy controls should govern autonomous security bots in production?
Response file: domain-runs/G12-BOT.md

13. [API] Which API controls remain mandatory for internal-only services?
Response file: domain-runs/G13-API.md

14. [LOG] What is the minimum forensic logging baseline we cannot waive?
Response file: domain-runs/G14-LOG.md

15. [COOK] What cookie controls are required for session-bearing web applications?
Response file: domain-runs/G15-COOK.md

16. [CORS] When is wildcard CORS prohibited and what is the safe alternative?
Response file: domain-runs/G16-CORS.md

17. [MOB] Are backend controls enough without mobile-app hardening?
Response file: domain-runs/G17-MOB.md

18. [MCP] What governance controls apply to MCP tools that can change system state?
Response file: domain-runs/G18-MCP.md

19. [EXCEPT] What must be documented to approve a 60-day security exception?
Response file: domain-runs/G19-EXCEPT.md

20. [DECOM] What evidence is required when decommissioning an application handling sensitive data?
Response file: domain-runs/G20-DECOM.md

21. [CONT] Which controls must be proven before promoting a new container image?
Response file: domain-runs/G21-CONT.md

22. [SVRL] How should we govern serverless function identity and secrets usage?
Response file: domain-runs/G22-SVRL.md

23. [FILE] What file-upload governance checks are mandatory for public endpoints?
Response file: domain-runs/G23-FILE.md

24. [DLP] What controls should trigger DLP incident escalation for source repositories?
Response file: domain-runs/G24-DLP.md

25. [CFG] How do we prove secure-by-default configuration in every environment?
Response file: domain-runs/G25-CFG.md

26. [ZTA] What minimum Zero Trust controls are required for internal admin portals?
Response file: domain-runs/G26-ZTA.md

27. [GRAPHQL] What controls are mandatory before enabling GraphQL in production?
Response file: domain-runs/G27-GRAPHQL.md

28. [EMAIL] What governance controls reduce phishing and spoofing risk for enterprise mail?
Response file: domain-runs/G28-EMAIL.md

29. [CLOUD] What cloud governance evidence is required before onboarding a new subscription?
Response file: domain-runs/G29-CLOUD.md

30. [AJAX] How should async client requests be governed to prevent token leakage?
Response file: domain-runs/G30-AJAX.md

31. [OAUTH] What controls are required for secure OAuth token lifecycle management?
Response file: domain-runs/G31-OAUTH.md

32. [ERR] What is an acceptable production error-handling policy for sensitive systems?
Response file: domain-runs/G32-ERR.md

33. [TM] How should threat-model outputs be enforced as release requirements?
Response file: domain-runs/G33-TM.md

34. [CRED] What governance controls prevent misuse of privileged credentials in CI/CD?
Response file: domain-runs/G34-CRED.md

35. [PBAC] How do we validate policy-based access control decisions for critical APIs?
Response file: domain-runs/G35-PBAC.md

36. [LEGACY] What controls are mandatory when supporting legacy protocols temporarily?
Response file: domain-runs/G36-LEGACY.md

37. [IAC] What evidence proves IaC changes are security-reviewed and policy-compliant?
Response file: domain-runs/G37-IAC.md

38. [DATA] How do we prove data minimization and lawful processing in application workflows?
Response file: domain-runs/G38-DATA.md

39. [REST] What governance checks are required before publishing new REST endpoints?
Response file: domain-runs/G39-REST.md

40. [NET] What network-segmentation evidence is required for tiered application deployment?
Response file: domain-runs/G40-NET.md

41. [IDOR] How should we evidence object-level authorization for tenant data access?
Response file: domain-runs/G41-IDOR.md

42. [DEP] What governance controls should block risky third-party package updates?
Response file: domain-runs/G42-DEP.md

43. [SAML] What controls are required before federating SAML with an external IdP?
Response file: domain-runs/G43-SAML.md

44. [NOSQL] What security controls are mandatory for production NoSQL data stores?
Response file: domain-runs/G44-NOSQL.md

45. [REMEDI] How do we evidence that remediation actions are effective, not just recorded?
Response file: domain-runs/G45-REMEDI.md

46. [EDGE] What controls are required for edge-delivered application traffic?
Response file: domain-runs/G46-EDGE.md

47. [SCA] What is the minimum SCA evidence required to block vulnerable dependencies?
Response file: domain-runs/G47-SCA.md

48. [NSEG] What policy controls govern network segmentation exceptions during incidents?
Response file: domain-runs/G48-NSEG.md

49. [CRYPT] What cryptographic controls are mandatory for regulated customer data?
Response file: domain-runs/G49-CRYPT.md

50. [INJECT] Which controls are required to prevent command and query injection classes?
Response file: domain-runs/G50-INJECT.md

51. [SUPPLY] What supply-chain assurances are required before onboarding a new vendor library?
Response file: domain-runs/G51-SUPPLY.md

52. [PARAM] How should parameter tampering risks be controlled in sensitive transactions?
Response file: domain-runs/G52-PARAM.md

53. [DB] What evidence proves secure database access and encryption posture?
Response file: domain-runs/G53-DB.md

54. [INPUT] What governance policy defines acceptable input-validation standards?
Response file: domain-runs/G54-INPUT.md

55. [SVR] What server hardening baseline is mandatory before production release?
Response file: domain-runs/G55-SVR.md

56. [RTC] What controls are required for real-time communications carrying sensitive data?
Response file: domain-runs/G56-RTC.md

57. [GOV] Which governance artefacts are mandatory for annual control assurance review?
Response file: domain-runs/G57-GOV.md

58. [INTEG] What controls govern secure system-to-system integrations?
Response file: domain-runs/G58-INTEG.md

59. [TENANT] How do we verify tenant isolation in multi-tenant services?
Response file: domain-runs/G59-TENANT.md

60. [SIGN] What digital-signature evidence is required for non-repudiable workflows?
Response file: domain-runs/G60-SIGN.md

61. [REPO] What repository controls are mandatory to reduce source and secret risk?
Response file: domain-runs/G61-REPO.md

62. [K8S] What Kubernetes controls are required before onboarding a new namespace?
Response file: domain-runs/G62-K8S.md

63. [SSRF] How should SSRF risk be governed for services that call external URLs?
Response file: domain-runs/G63-SSRF.md

64. [SAST] What evidence proves SAST gates actively block high-risk code?
Response file: domain-runs/G64-SAST.md

65. [MON] What monitoring controls prove timely detection of security incidents?
Response file: domain-runs/G65-MON.md

66. [TRAIN] What security training evidence is required for privileged engineering roles?
Response file: domain-runs/G66-TRAIN.md

67. [AIDEV] What controls govern safe use of AI coding assistants in regulated development?
Response file: domain-runs/G67-AIDEV.md

68. [PROV] What evidence confirms provenance integrity for released binaries and images?
Response file: domain-runs/G68-PROV.md

69. [TXN] What controls are required for transaction integrity across distributed services?
Response file: domain-runs/G69-TXN.md

70. [IAM] How do we prove IAM controls are enforced consistently across platforms?
Response file: domain-runs/G70-IAM.md

71. [RUNTIME] What runtime protections are mandatory for internet-facing workloads?
Response file: domain-runs/G71-RUNTIME.md

72. [VDP] What controls are needed to run a vulnerability disclosure process safely?
Response file: domain-runs/G72-VDP.md

73. [INC] What incident-response evidence is required for major security events?
Response file: domain-runs/G73-INC.md

74. [WAF] What governance checks are required before tuning WAF blocking rules?
Response file: domain-runs/G74-WAF.md

75. [WS] What controls apply to secure web-service endpoints beyond REST basics?
Response file: domain-runs/G75-WS.md

76. [LLM] What controls are required before exposing an LLM endpoint to employees?
Response file: domain-runs/G76-LLM.md

77. [MSA] What controls are required to secure service-to-service calls in microservices?
Response file: domain-runs/G77-MSA.md

78. [RAG] What governance controls are required for grounded retrieval in production?
Response file: domain-runs/G78-RAG.md

79. [SBOM] What SBOM evidence is required at release and how should it be verified?
Response file: domain-runs/G79-SBOM.md

80. [SECR] What evidence demonstrates end-to-end secrets governance compliance?
Response file: domain-runs/G80-SECR.md

