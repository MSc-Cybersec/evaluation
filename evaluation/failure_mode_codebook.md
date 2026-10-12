# Failure-Mode Codebook

Inductive open coding of incorrect and incomplete agent output, following Braun and Clarke
(2006) and the protocol set out in §3.6 of the dissertation. A single coder applied the
codes; no reliability coefficient is computed and none is claimed (§3.8).

**Scope of the coded corpus**

| Source | Units coded |
| :--- | ---: |
| DVWA workspace scan — complete finding set (`codi-response/W1.md`) | 61 findings |
| Targeted module scans, semantic findings (`codi-response/D1.md`–`D22.md`, 19 distinct modules) | 114 findings |
| Domain consultations (`sage-response/domain-runs/G01`–`G80`) | 80 responses |

Only the DVWA set was audited line by line against source code, because it is the one
stimulus for which every finding could be adjudicated against the file it cites. Counts
below state their denominator in each case.

**Unit of analysis.** One finding (Codi) or one response (Sage). A single source line
carrying two findings is two units; this is itself coded as F2.

**Adjudication rule.** A finding is scored on two independent properties:

- **Detection correctness** — does the flagged line exhibit the condition the message describes?
- **Citation correctness** — does the cited mandard govern that condition?

Both are determined against the stimulus code and the application's documented defect
inventory, not against the coder's impression of the output.

---

## F1 — Detector matches an adjacent construct

**Definition.** The detector fires on a token appearing near, but not constituting, the
condition reported. Detection is incorrect; the line may still be defective for another reason.

**Include when** the flagged construct does not instantiate the reported condition, and the
match is explicable by keyword proximity rather than by value, assignment or program structure.

**Exclude when** the construct does instantiate the condition but the citation is wrong
(no such cases remain after the AUTH-M-001 rebinding), or when the line is non-executable (F3).

**Count.** 20 of 61 audited findings. Systematic.

**Evidence.** Ten `SECR-M-001` findings report *"Potential hardcoded secret detected"* against
SQL interpolation of the form `$query = "SELECT * FROM users WHERE user='$user' AND password='$pass';"`.
The line contains no secret — it contains the token `password` beside a quoted string — and is
in fact a SQL injection vulnerability, governed by a different record and not reported as such.
Ten `AUTH-M-001` findings report *"Hardcoded password literal detected"* against the same lines.

**Negative cases.** Two genuine hardcoded credentials were correctly caught:
`$password = "password";` in `vulnerabilities/sqli/test.php`, and an embedded `ACCESS_TOKEN_SECRET`
in `vulnerabilities/api/src/Login.php`.

## F2 — Single line attributed to multiple mandards

**Definition.** One source line is reported more than once under different records, producing
duplicate entries for a single construct.

**Include when** the same file and line number appear in two or more findings in one report.

**Exclude when** a file legitimately contains distinct defects on different lines.

**Count.** 11 lines. Systematic.

**Evidence.** Eleven lines are each reported twice, under `SECR-M-001` and `AUTH-M-001`,
yielding two Critical-severity entries per construct. In ten of the eleven the underlying
detection is a false positive (F1), so duplication amplifies noise rather than a true signal.

## F3 — Non-executable code flagged as executable

**Definition.** The detector matches identifier text inside a comment, a string, or a call that
is not the primitive named.

**Include when** parsing context would have excluded the match.

**Exclude when** the construct is executable but governed by a different record (F1).

**Count.** 2 findings. Incidental.

**Evidence.** In `dvwa/js/dvwaPage.js` the flagged line is a comment containing `eval(`.
In `vulnerabilities/cryptography/source/oracle_attack.php` the flagged construct is `curl_exec()`,
an HTTP request rather than a code-execution primitive.

**Negative cases.** The remaining ten `SAST-M-001` findings are correct, identifying genuine
`eval()`, `exec()` and `shell_exec()` calls, several with concatenated user input.

## F4 — Generic record cited where no close match is retrieved

**Definition.** Semantic retrieval returns a broadly applicable record instead of declining to
cite, where the corpus carries a record specific to the defect class.

**Include when** a more specific record exists in the applicable set and was not returned.

**Exclude when** no specific record exists, or when the agent declares the record as requiring
tool verification rather than asserting a violation.

**Count.** 3 of 19 modules. Systematic.

**Evidence.** The `cryptography` module cited the output-encoding record `INPUT-M-002` despite a
dedicated `CRYPT` domain existing; `open_redirect` likewise returned only `INPUT-M-002`;
`fi` (file inclusion) returned `INPUT-M-001` and `SAST-M-001` rather than the `FILE` records
available to it and correctly retrieved for the `upload` module.

**Why coded separately from F1.** F1 is a pattern-matching error in the static layer. F4 is a
retrieval behaviour in the semantic layer: the response retains the *form* of grounded citation
while the substance is absent.

## F5 — Response contract truncated from the tail

**Definition.** One or more of the seven mandatory sections is absent, and the absent sections
are terminal rather than interior.

**Include when** a section is missing and every section preceding it is present.

**Exclude when** the section is present under a non-conforming heading (F6).

**Count.** 3 of 80 responses. Systematic.

**Evidence.** `G10-GATE` omitted `Required actions`, `Evidence for audit` and
`Assumptions and limits`; `G12-BOT` and `G67-AIDEV` each omitted the latter two. No response
omitted an interior section while completing those after it — consistent with output-length
exhaustion rather than selective disregard.

## F6 — Section labels deviate from the specification

**Definition.** Contract content is present and correct, but rendered under a heading that does
not match the specification, defeating automated verification.

**Include when** the section content satisfies the contract but the heading string differs.

**Exclude when** the content itself is absent (F5).

**Count.** 4 of 80 responses. Systematic.

**Evidence.** `G04-BACKUP`, `G42-DEP`, `G58-INTEG` and `G69-TXN` rendered the governing-records
section as `Governing Mandards` or `Governing mandates`. Two further undocumented sections are
emitted routinely — `Evidence and framework mapping` in 74 responses and `Scoring notes` in all 80.

---

## Codes considered and not retained

Two candidate codes were assessed against the corpus and are recorded here so the coding frame
is inspectable in full.

- **Remediation snippet in a language other than the file's.** Initially read as a defect.
  Rejected on inspection of the mechanism: the snippet shown in a scan report is the corpus
  record's illustrative example, which is deliberately language-neutral because one record
  governs code in every language. The applied patch is inferred and written in the file's own
  language at the point a developer accepts the fix. Not a failure mode.

- **Cited record does not govern the detected condition.** Observed in the captured scan output,
  where 31 weak-hash detections across the six applications cited `CRYPT-M-001` (*Encryption at
  Rest*). `AUTH-M-001` (*Secure Password Hashing*) is the only corpus record whose statement
  prohibits MD5 and SHA-1 by name. The detector binding was corrected before the results were
  finalised, so the condition does not arise in the artefact as evaluated. Retained here, and
  disclosed in the §5.1.1 provenance note, because the captured evidence files still show the
  superseded citation.

## Negative-case analysis

Consistent with §3.6, cases contradicting each emerging theme were sought:

- No fabricated identifier in any of the 316 workspace findings, 114 semantic findings or
  80 responses.
- All six applications completed without a scan error.
- Detection wholly correct in the `CORS-M-001` and `DEP-M-001` findings, in ten of twelve
  `SAST-M-001` findings, and in all 31 weak-hash detections.
- Citation tracked the documented defect class in sixteen of nineteen module scans.
- 73 of 80 responses reproduced the contract exactly.
