"""
Replication analysis for the SAGF/VeriFy evaluation (Chapter 5).

Regenerates every quantitative claim in Chapter 5 from the captured agent output:

  1. Workspace scan outcomes          -> Table 5.1
  2. Violations by governing mandard  -> Table 5.2
  3. Response-contract audit          -> Table 5.4, and response_contract_audit.csv

Two builds are published. The corrected build is the one Chapter 5 reports; the
baseline build is the superseded detector layer whose evaluation exposed failure
modes F1 and F2. Both columns of Table J.1 are reproducible:

    python evaluation/analysis.py              # corrected build  -> Chapter 5
    python evaluation/analysis.py --baseline   # baseline build   -> Table J.1

Inputs are the captured evidence directories inside this package; nothing is
fetched at run time.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODI = HERE / "codi_scan_reports"
SAGE = HERE / "sage_responses"
OUT = HERE / "response_contract_audit.csv"

# The baseline capture predates the weak-hash rebinding, so it must be applied in
# analysis; the corrected build already emits AUTH-M-001 and must not be rebound.
BASELINE = "--baseline" in sys.argv
SUFFIX = "" if BASELINE else "-retest2"

APPS = {
    "W1": "DVWA", "W2": "crAPI", "W3": "OWASP Juice Shop",
    "W4": "OWASP Mutillidae II", "W5": "OWASP NodeGoat", "W6": "OWASP WebGoat",
}

# Findings are emitted as a single-line JSON array of objects.
FINDING_ARRAY = re.compile(r'^\[\{"mandard_id".*\}\]$', re.M)
WEAK_HASH = re.compile(r"Weak hash algorithm (?:MD5|SHA-1) detected")

# The seven mandatory sections of the response contract (s4.4.2.1, Table 4.5).
CONTRACT = [
    "Bottom line",
    "Risk and impact",
    "Governing mandards",
    "Framework mapping",
    "Required actions",
    "Evidence for audit",
    "Assumptions and limits",
]
# Observed label variants that carry correct content under a non-conforming heading (F6).
VARIANTS = {
    "Governing mandards": ["Governing Mandards", "Governing mandates", "Governing Mandates"],
}
HEADING = re.compile(r"^#{1,4}\s+(.+?)\s*$", re.M)
MANDARD_ID = re.compile(r"\b[A-Z][A-Z0-9]{1,8}-[MG]-\d{3}\b")


def load_findings() -> tuple[Counter, dict[str, Counter], Counter]:
    """Return (totals by mandard, per-application counts, severity counts) after rebinding."""
    totals: Counter = Counter()
    per_app: dict[str, Counter] = {}
    severity: Counter = Counter()

    for stem, app in APPS.items():
        path = CODI / f"{stem}{SUFFIX}.md"
        counts: Counter = Counter()
        for raw in FINDING_ARRAY.findall(path.read_text(encoding="utf-8")):
            for finding in json.loads(raw):
                mandard = finding["mandard_id"]
                # Weak-hash detectors were rebound to AUTH-M-001 after the baseline
                # capture; see retrieval_config.json -> detector_binding_note. The
                # corrected build emits the rebound identifier directly.
                if BASELINE and WEAK_HASH.search(finding.get("message", "")):
                    mandard, sev = "AUTH-M-001", "CRITICAL"
                else:
                    sev = finding["severity"].upper()
                counts[mandard] += 1
                totals[mandard] += 1
                severity[sev] += 1
        per_app[app] = counts
    return totals, per_app, severity


def audit_contract() -> list[dict[str, object]]:
    """Score each domain consultation against the seven-section contract."""
    rows = []
    for path in sorted(SAGE.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        headings = {h.strip() for h in HEADING.findall(text)}
        row: dict[str, object] = {"domain_run": path.stem}

        exact = variant = 0
        for section in CONTRACT:
            if section in headings:
                state, exact, variant = "present", exact + 1, variant + 1
            elif any(v in headings for v in VARIANTS.get(section, [])):
                state, variant = "label_variant", variant + 1
            else:
                state = "absent"
            row[section] = state

        row["sections_exact"] = exact
        row["sections_allowing_variants"] = variant
        row["contract_exact"] = exact == len(CONTRACT)
        row["advisory_label"] = "Advisory (not catalogue-backed)" in text
        row["evidence_and_framework_mapping"] = "Evidence and framework mapping" in headings
        row["scoring_notes"] = "Scoring notes" in headings
        row["truncated_tool_output"] = "truncated" in text.lower()
        row["distinct_mandards_cited"] = len(set(MANDARD_ID.findall(text)))
        rows.append(row)
    return rows


def main() -> None:
    build = "BASELINE build (Appendix J.1, Table J.1 left column)" if BASELINE \
        else "CORRECTED build (Chapter 5)"
    print(f"=== {build} ===\n")
    totals, per_app, severity = load_findings()
    grand = sum(totals.values())

    print("Table 5.1 - Workspace scan outcomes")
    for app, counts in per_app.items():
        print(f"  {app:<22} {sum(counts.values()):>4} violations, {len(counts):>2} mandards")
    print(f"  {'Total':<22} {grand:>4} violations, {len(totals):>2} mandards\n")

    print("Table 5.2 - Violations by governing mandard")
    for mandard, n in totals.most_common():
        print(f"  {mandard:<14} {n:>4}  {n / grand * 100:>5.1f}%")
    print(f"  severity: {dict(severity)}\n")

    rows = audit_contract()
    if rows:
        with OUT.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    exact = sum(r["contract_exact"] for r in rows)
    variant_ok = sum(r["sections_allowing_variants"] == len(CONTRACT) for r in rows)
    print("Table 5.4 - Response-contract audit")
    print(f"  responses audited                     {len(rows)}")
    print(f"  reproducing all seven sections        {exact}")
    print(f"  all seven allowing label variants     {variant_ok}")
    print(f"  genuinely truncated                   {len(rows) - variant_ok}")
    print(f"  advisory label present                {sum(r['advisory_label'] for r in rows)}")
    print(f"  'Scoring notes' present               {sum(r['scoring_notes'] for r in rows)}")
    print(f"  truncated tool output disclosed       {sum(r['truncated_tool_output'] for r in rows)}")
    print(f"\n  wrote {OUT.relative_to(Path.cwd()) if OUT.is_relative_to(Path.cwd()) else OUT}")


if __name__ == "__main__":
    main()
