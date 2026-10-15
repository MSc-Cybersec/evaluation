"""Extracts a redistributable mapping manifest from the governance corpus.

The corpus itself is withheld (Appendix F): it carries the organisation's
normative requirements, tool bindings and framework control text. This extract
keeps only what is needed to verify the synthesis claims of the dissertation —
record identifier, domain, risk, category, and the framework control
*identifiers* each record discharges. Statements, rationale, remediation,
tooling and any framework control titles are dropped.

This script is published for inspection rather than execution: its input,
`mandards.js`, is in `mandard_corpus.zip` of this package. It is included
because the normalisation it performs is a measurement decision, not a mechanical one. An
entry may appear as "A.8.2" or as "A.8.2 Privileged access rights"; counting
those as two controls inflates the distinct-control figure, while truncating at
the first token collapses "CIS 1" and "CIS 10" into one. The rules below strip a
trailing title without merging distinct identifiers, and the resulting count is
the one reported in Table 5.6.

Output: corpus/mapping_manifest.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "repo" / "verify-backend" / "app" / "data" / "mandards.js"
OUT = ROOT / "docs" / "dissertation" / "replication-package" / "corpus" / "mapping_manifest.json"

# Mapping arrays appear under varying key names across frameworks.
ID_FIELDS = (
    "controls requirements practices functions objectives criteria weaknesses rules "
    "articles levels api_security techniques sections risks web_top_10 mobile_top_10 cheatsheets"
).split()

# An entry may be "ID", "ID - Title" or "ID Title". Only the identifier is kept, so
# that no framework's control wording is redistributed. Two failure modes are avoided:
# counting "A.8.2" and "A.8.2 Privileged access rights" as different controls, and
# collapsing "CIS 1" and "CIS 10" into a common prefix.
DASH = re.compile(r"\s+[-\u2013]\s+")
SCHEME = re.compile(
    r"^(A\.\d+\.\d+"                      # ISO 27001 Annex A
    r"|[A-Z]{2}-\d+(?:\(\d+\))?"           # NIST SP 800-53
    r"|CWE-\d+"                            # CWE
    r"|[A-Z]{3}\d{2}\.\d{2}"               # COBIT 2019
    r"|[A-Z]{2}\.[A-Z]{2}-\d{2}"           # NIST CSF 2.0
    r"|\d+(?:\.\d+)+(?:\([A-Za-z0-9]+\))*"  # HIPAA, ISA 62443, NIST 800-190
    r"|[A-Z]+\d+)"                         # MITRE technique and mitigation IDs
    r"(?=[\s:]|$)"                         # a title may follow after a space or colon
)


def normalise(entry: str) -> str:
    """Return the control identifier, with any trailing title removed."""
    head = DASH.split(entry.strip(), 1)[0].strip()
    m = SCHEME.match(head)
    return m.group(1) if m else head


def load_records():
    """Parse the `const mandards = [...]` array out of the JavaScript source."""
    text = SRC.read_text(encoding="utf-8")
    start = text.index("[", text.index("const mandards ="))
    depth, in_str, quote = 0, False, None
    for i in range(start, len(text)):
        ch, prev = text[i], text[i - 1]
        if ch in "\"'`" and prev != "\\":
            if not in_str:
                in_str, quote = True, ch
            elif ch == quote:
                in_str = False
        if in_str:
            continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unterminated mandards array")


def control_ids(value):
    """Return bare control identifiers from a mapping array."""
    ids = []
    for entry in value or []:
        if not isinstance(entry, str) or not entry.strip():
            continue
        ids.append(normalise(entry))
    return ids


def main() -> int:
    records = load_records()
    out = []
    for rec in records:
        mappings = {}
        for fw, body in (rec.get("complianceFramework") or {}).items():
            if not isinstance(body, dict):
                continue
            ids = []
            for field in ID_FIELDS:
                ids.extend(control_ids(body.get(field)))
            if ids:
                mappings[fw] = ids
        out.append({
            "id": rec.get("id"),
            "domain": rec.get("domain"),
            "risk": rec.get("risk"),
            "category": rec.get("category"),
            "mappings": mappings,
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "_comment": (
            "Structural extract of the SAGF governance corpus, published to make the "
            "synthesis claims of the dissertation independently verifiable. Contains "
            "record identifiers, domains, risk and category, and the framework control "
            "IDENTIFIERS each record discharges. It deliberately contains no mandard "
            "statement, rationale, remediation, tooling reference, or framework control "
            "title: the corpus itself is withheld under the terms set out in Appendix F, "
            "and control wording belongs to the respective standards bodies. Verify any "
            "control identifier against your own licensed copy of the standard."
        ),
        "records": len(out),
        "corpus": out,
    }, indent=1), encoding="utf-8")

    # Guard: the extract must carry identifiers and metadata only, never corpus prose.
    text = OUT.read_text(encoding="utf-8")
    for banned in ("MUST", "SonarQube", "Snyk", "Key Vault", "Enforced by"):
        if re.search(rf"\b{re.escape(banned)}\b", text, re.I):
            print(f"FAILED - extract contains '{banned}'")
            return 1

    print(f"{len(out)} records -> {OUT.relative_to(ROOT)}")
    print(f"{OUT.stat().st_size / 1024:.0f} KB (corpus is {SRC.stat().st_size / 1024 / 1024:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
