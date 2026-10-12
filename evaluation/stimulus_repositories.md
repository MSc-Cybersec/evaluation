# Evaluation Stimulus — Repository Manifest

This manifest records the stimulus applications used in the evaluation reported
in Chapter 5 and summarised in Table F.1 of the dissertation. All six are
open-source, community-maintained applications built deliberately to contain
documented security defects for teaching and research use, which is what permits
their redistribution and what supplies the ground truth against which citation
correctness is assessed.

The applications are **not vendored into this package**. They are redistributable
but large, and mirroring them would obscure their provenance. Each is identified
below by its canonical upstream repository and the revision used.

| Application | Upstream repository | Branch used | Commit SHA | Primary technology | Files scanned |
| :--- | :--- | :--- | :--- | :--- | ---: |
| DVWA | `github.com/digininja/DVWA` | `master` | *(see note)* | PHP / MySQL | 179 |
| crAPI | `github.com/OWASP/crAPI` | `develop` | *(see note)* | Go, Java, Python, TypeScript | 650 |
| OWASP Juice Shop | `github.com/juice-shop/juice-shop` | `master` | *(see note)* | Node.js / Angular (TypeScript) | 968 |
| OWASP Mutillidae II | `github.com/webpwnized/mutillidae` | `main` | *(see note)* | PHP | 186 |
| OWASP NodeGoat | `github.com/OWASP/NodeGoat` | `master` | *(see note)* | Node.js / Express | 100 |
| OWASP WebGoat | `github.com/WebGoat/WebGoat` | `main` | *(see note)* | Java / Spring / Maven | 503 |
| **Total** | | | | | **2,586** |

> **Note on revision pinning.** The scans were executed against the branch heads
> current at the time of capture. Commit SHAs are required for exact replication
> of the file census, because a branch head moves: a replicator checking out
> `master` today will not necessarily scan 179 files in DVWA. Where a SHA is not
> recorded above, the file counts in the final column are the authoritative
> description of the revision scanned, and a replicator should expect the census
> to differ if upstream has changed. This is a known limitation of the capture
> and is the first thing a replication should correct.

## Scope boundary

The stimulus spans PHP, Java, Python, Go and JavaScript/TypeScript, and both
traditional web applications and polyglot microservices. It does **not** exercise
the infrastructure-facing domains of the corpus — `IAC`, `CONT`, `K8S` and `PIPE`,
35 records in total — because these applications contain application code rather
than deployment configuration. Findings are accordingly confined to
application-layer governance.

## Ground truth

Correctness is adjudicated against each application's own documented defect
inventory: these are teaching applications whose vulnerabilities are catalogued
by their maintainers, by lesson or module name. The targeted module scans
(Table 5.3) exploit this directly — a module named `sqli` is known to contain
SQL injection, so a citation of the record governing SQL injection is
independently verifiable without researcher judgement.

The scored agent output is published in `codi_scan_reports/` and
`sage_responses/`; `analysis.py` regenerates Tables 5.1, 5.2 and 5.4 from it.
