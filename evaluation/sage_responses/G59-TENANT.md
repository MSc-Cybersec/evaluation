# G59-TENANT

## Question
How do we verify tenant isolation in multi-tenant services?

## Sage response

## Bottom line

Tenant isolation must be verified through automated negative tests, database-policy inspection, and production monitoring—not only application code review. Per **TENANT-M-001**, every data access must enforce verified tenant context, with row-level security, globally enforced tenant predicates, separate schemas, or separate databases; cross-tenant attempts must be logged. Per **TENANT-M-002**, also prove that one tenant cannot exhaust shared capacity or degrade other tenants.

## Risk and impact

| Risk | Exposure if unaddressed |
|---|---|
| **Critical — TENANT-M-001** | Cross-tenant disclosure, modification, or deletion of customer data; regulatory breach; contractual failure; loss of customer trust. |
| **High — TENANT-M-002** | A noisy or malicious tenant can exhaust API, storage, or database capacity and affect service availability for every tenant. |

Isolation verification should fail the release if Tenant A can read, list, search, update, delete, export, or otherwise affect Tenant B’s resources.

## Governing mandards

- **TENANT-M-001 — Tenant Data Isolation & Access Control — Critical.**  
  Per **TENANT-M-001**: multi-tenant applications must use strong tenant isolation, enforce tenant identity in all queries, verify tenant context before access, and audit cross-tenant attempts.

- **TENANT-M-002 — Multi-Tenant Resource Quotas & Rate Limiting — High.**  
  Per **TENANT-M-002**: systems must enforce per-tenant API, storage, and database resource limits, and monitor and alert on quota violations.

## Framework mapping

Mappings returned by the SAGF catalogue:

| Mandard | Framework mappings |
|---|---|
| **TENANT-M-001** | NIST SP 800-53 Rev.5: AC-2, AC-3, AC-4, AC-6, AU-2, AU-6, AU-12, SI-4, CM-2, SC-7, CA-9; PCI DSS v4.0: Req 7, Req 10; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.2, A.8.3, A.8.9, A.8.15, A.8.16, A.8.27; HIPAA: 164.312(a)(1), 164.312(b); SOC 2: CC6.1, CC7.2; OWASP ASVS: V8. |
| **TENANT-M-002** | NIST SP 800-53 Rev.5: AC-3, AC-4, AC-6, SC-8, SI-4, AU-6, SI-7, CM-2, SC-7, CA-9, CP-9, CP-10; PCI DSS v4.0: Req 7; ISO/IEC 27001:2022: A.5.15, A.5.18, A.8.3, A.8.9, A.8.13, A.8.14, A.8.16, A.8.27; HIPAA: 164.312(a)(1); SOC 2: CC6.1, CC7.2, A1.2. |

## Required actions

### 1. Inventory every tenant-aware path

**Owner: Service architect and engineering lead**

Per **TENANT-M-001**, identify every path that stores, retrieves, modifies, or propagates tenant data:

- Synchronous APIs and service-to-service calls
- Database tables, views, stored procedures, and reporting replicas
- Search indexes and caches
- Object storage and generated exports
- Message queues, events, and background jobs
- Backups, restore procedures, analytics, and support tooling
- Administrative and impersonation functions

**Advisory (not knowledge-doc backed):** Record the authoritative source of tenant identity at each trust boundary. Tenant context should come from authenticated and server-validated identity data, not an untrusted request header or object identifier.

### 2. Inspect the enforcement mechanism

**Owner: Application engineer and database administrator**

Per **TENANT-M-001**, verify one of these controls is consistently applied:

- Separate database per tenant
- Separate schema per tenant
- Database row-level security
- A global ORM filter that automatically adds `tenant_id`
- An equivalent centrally enforced policy

For PostgreSQL row-level security, inspect the deployed policy:

```sql
SELECT tablename, policyname, permissive, roles, cmd, qual, with_check
FROM pg_policies
ORDER BY tablename, policyname;
```

Confirm that:

- Every tenant-owned table is covered.
- Both reads and writes are constrained.
- `INSERT` and `UPDATE` cannot assign another tenant’s identifier.
- Service accounts cannot bypass the policy unintentionally.
- Missing or invalid tenant context fails closed.
- Administrative bypass is explicitly authorised and audited.

### 3. Run a two-tenant negative-test suite

**Owner: QA automation and security testing**

Create isolated Tenant A and Tenant B fixtures with unique canary records. Authenticate as Tenant A and attempt all operations against Tenant B identifiers.

| Test | Expected result |
|---|---|
| Read Tenant B object by identifier | `403`, `404`, or an empty result according to the approved API contract |
| List or search records | No Tenant B records returned |
| Create an object using Tenant B’s `tenant_id` | Rejected or server-side tenant value substituted |
| Update or delete Tenant B object | No change; request rejected |
| Supply mismatched token and tenant header | Rejected |
| Change path, query, body, or GraphQL tenant fields | No cross-tenant access |
| Reuse cached Tenant B response as Tenant A | No data returned |
| Consume or replay Tenant B job/event as Tenant A | No processing under Tenant A context |
| Export, report, or bulk-download | Output contains only the authorised tenant |
| Invoke support or administrative functionality | Requires explicit privileged authorisation and produces an audit record |

Per **TENANT-M-001**, the catalogue specifically requires penetration testing that attempts to access Tenant B data with Tenant A credentials and expects `403 Forbidden` or an empty result set. Make this suite a mandatory CI/CD and pre-production gate.

### 4. Test direct and indirect access separately

**Owner: Security tester**

Per **TENANT-M-001**, tenant enforcement must not depend on one API route. Test:

- Alternate API versions and undocumented endpoints
- Batch and bulk operations
- GraphQL aliases and nested resolvers
- Signed download links
- Search, analytics, and reporting interfaces
- Background workers and scheduled tasks
- Retry and dead-letter processing
- Database access using the deployed application role
- Support, migration, and maintenance scripts

**Advisory (not knowledge-doc backed):** Include concurrency tests to detect tenant context leaking between pooled threads, reused database connections, asynchronous tasks, and cache entries.

### 5. Verify cross-tenant attempt logging

**Owner: Security operations and service owner**

Per **TENANT-M-001**, cross-tenant attempts must be auditable. Verify that a denied test creates a record containing:

- Authenticated actor or service identity
- Source tenant
- Target tenant or resource
- Operation and decision
- Timestamp, service, and correlation identifier

**Advisory (not knowledge-doc backed):** Avoid placing sensitive record contents or credentials in the event. Configure an alert for repeated or distributed cross-tenant attempts and validate the alert through a controlled test.

### 6. Prove noisy-neighbour containment

**Owner: Platform engineering and SRE**

Per **TENANT-M-002**:

- Configure API limits keyed by validated tenant identity.
- Enforce tenant storage and database connection limits.
- Generate a load spike from one tenant.
- Confirm excess requests receive `429` or another approved throttling response.
- Confirm control-tenant latency and availability remain within approved service objectives.
- Verify quota-violation monitoring and alerting.

The catalogue gives `1000 requests/minute` as an actionable example, but the production threshold should be set through approved capacity and service-level requirements rather than adopted without analysis.

## Evidence for audit

Retain the following evidence for each release or scheduled control test:

1. Tenant-isolation architecture and data-store inventory.
2. Deployed RLS, schema, database, ORM-filter, or equivalent policy configuration.
3. CI/CD results for the two-tenant negative-test matrix.
4. Penetration-test report showing attempted cross-tenant access and expected denial.
5. Database-policy inspection output from the deployed environment.
6. Audit event and alert generated by a controlled cross-tenant attempt.
7. Per-tenant quota and rate-limit configuration.
8. Load-test report showing the attacking tenant was throttled without affecting the control tenant.
9. Approved exception or deviation record for any uncovered access path.

## Assumptions and limits

No knowledge document is currently mapped to **TENANT-M-001** or **TENANT-M-002**. No knowledge document was found for the detailed test procedure above; steps explicitly marked advisory are therefore not knowledge-document backed. General data-access and authentication documents were found but set aside because their `mandard_refs` do not identify either tenant mandard.

### Evidence and framework mapping

| Mandard | Risk | Domain | Frameworks cited (controls) |
| --- | --- | --- | --- |
| [**TENANT-M-001**](https://verify.example-org.internal/?id=TENANT-M-001) | Critical | Multi-Tenancy | CIS_CONTROLS (CIS 4, CIS 6, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-285); HIPAA (164.312(a)(1), 164.312(b)); ISO_27001 (A.5.15, A.5.18, A.8.15); +9 more |
| [**TENANT-M-002**](https://verify.example-org.internal/?id=TENANT-M-002) | High | Multi-Tenancy | AIUC1 (A005); CIS_CONTROLS (CIS 11, CIS 4, CIS 8); COBIT_2019 (BAI09.01, DSS05.02, DSS05.07); CSA_CCM (DSP: Data Security & Privacy, IVS: Infrastructure & Virtualization Security); CWE (CWE-284, CWE-400); HIPAA (164.312(a)(1)); +11 more |

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